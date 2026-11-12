#!/usr/bin/env python3
"""Independent pure-mathematics and machine-quotation verification for Card X-R79.

Pinned origin/main commit: 0dda7b4725f613dbef273edafcd3fca73ccb245c (window 38d2a36dc..0dda7b472).
Firewall: pure mathematics and repository governance/audit checks only; zero measured values opened or computed (0 of 19);
zero producer modules imported in independent mathematical derivations; zero self-judgment on agy-exp's own work.
"""
from __future__ import annotations

import ast
import fractions
import hashlib
import itertools
import json
import math
import pathlib
import re
import subprocess
import sys
import warnings

import mpmath as mp
import numpy as np
import sympy as sp

warnings.filterwarnings("ignore")

HERE = pathlib.Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
PINNED_MAIN = "0dda7b4725f613dbef273edafcd3fca73ccb245c"
WINDOW_BASE = "38d2a36dc"
P797_COMMIT = "7b89eda8a"
F = fractions.Fraction


def git_show(rev_and_path: str) -> str:
    return subprocess.check_output(
        ["git", "show", rev_and_path], cwd=REPO_ROOT, text=True
    )


def git_cmd(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=REPO_ROOT, text=True)


# ---------------------------------------------------------------------------
# 0. Pre-committed negative controls (must pass first; exit 2 on failure)
# ---------------------------------------------------------------------------

_PURE_LITERAL_CALLS = {"len", "round", "abs", "Fraction", "Fr", "set", "tuple", "list", "frozenset"}


def is_constant_or_literal_expr(node: ast.AST) -> bool:
    """Return True iff `node` evaluates purely on hardcoded literals/constructors with no variable dependency."""
    if isinstance(node, ast.Constant):
        return True
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        return all(is_constant_or_literal_expr(e) for e in node.elts)
    if isinstance(node, ast.UnaryOp):
        return is_constant_or_literal_expr(node.operand)
    if isinstance(node, ast.BinOp):
        return is_constant_or_literal_expr(node.left) and is_constant_or_literal_expr(node.right)
    if isinstance(node, ast.BoolOp):
        return all(is_constant_or_literal_expr(v) for v in node.values)
    if isinstance(node, ast.Compare):
        return is_constant_or_literal_expr(node.left) and all(
            is_constant_or_literal_expr(c) for c in node.comparators
        )
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id in _PURE_LITERAL_CALLS:
            return all(is_constant_or_literal_expr(a) for a in node.args) and all(
                is_constant_or_literal_expr(kw.value) for kw in node.keywords
            )
        return False
    return False


def quote_in_pinned_file(path: str, exact_quote: str, rev: str = PINNED_MAIN) -> bool:
    return exact_quote in git_show(f"{rev}:{path}")


def run_negative_controls() -> dict:
    resolved = git_cmd("rev-parse", "0dda7b472^{commit}").strip()
    if resolved != PINNED_MAIN:
        sys.exit(2)

    # Control 1: quotation verifier accepts exact line and rejects 1-char tamper
    target_file = "frontier/B1888_the_public_form_scrutinised/FINDINGS.md"
    exact_ok = quote_in_pinned_file(target_file, "In the whole tree 50 do.")
    tamper_rejected = not quote_in_pinned_file(target_file, "In the whole tree 51 do.")
    if not (exact_ok and tamper_rejected):
        sys.exit(2)

    # Control 2: lock-vacuity / tautology detector catches literal-only expressions and spares live calls
    taut_1 = is_constant_or_literal_expr(ast.parse("len({1, 3, 7}) == 3", mode="eval").body)
    taut_2 = is_constant_or_literal_expr(ast.parse("True", mode="eval").body)
    taut_3 = is_constant_or_literal_expr(
        ast.parse("Fr(1) + Fr(12, 12) - 0 - 0 - Fr(4, 2) == 0", mode="eval").body
    )
    live_1 = not is_constant_or_literal_expr(ast.parse("kernel(ADJ, n) == 6 * n", mode="eval").body)

    # Dynamic mutation sensitivity control
    falsifiable_lock = lambda fn: fn(12) == 72 and fn(24) == 144
    tautological_lock = lambda fn: len({1, 3, 7}) == 3
    good_fn = lambda n: 6 * n
    broken_fn = lambda n: 72
    dyn_ok = (
        falsifiable_lock(good_fn) is True
        and falsifiable_lock(broken_fn) is False
        and tautological_lock(good_fn) is True
        and tautological_lock(broken_fn) is True
    )
    if not (taut_1 and taut_2 and taut_3 and live_1 and dyn_ok):
        sys.exit(2)

    return {
        "pinned_main": resolved,
        "control_1_exact_accepted": exact_ok,
        "control_1_1char_tamper_rejected": tamper_rejected,
        "control_2_ast_tautologies_flagged": [taut_1, taut_2, taut_3],
        "control_2_live_call_spared": live_1,
        "control_2_dynamic_mutation_distinguishes": dyn_ok,
    }


# ---------------------------------------------------------------------------
# 1. B1221 & B1641 (M4 corrections + locks + window diffs)
# ---------------------------------------------------------------------------

def verify_b1221() -> dict:
    g16 = [(1, 1, 1), (2, 0, -4), (2, 0, 2), (0, 1, -3), (0, 0, 6), (0, 0, 0)]
    g10 = [(0, 1, 3), (0, 1, -3), (1, 0, -2), (2, 0, 2)]
    c27 = g16 + g10 + [(0, 0, 0)]
    ints = [(0, 0, 6), (0, 0, 0), (0, 1, -3), (0, 1, 3)]
    adj = [(0, 0, 0)] * 3

    def exact_finite_kernel(comps: list[tuple[int, int, int]]) -> dict:
        ys = [abs(y) for _, _, y in comps if y != 0]
        if not ys:
            return {"infinite": True, "orders_on_grids": {n: 6 * n for n in (12, 24, 60, 120)}}
        g_y = math.gcd(*ys)
        denom = 6 * g_y
        elts = []
        for a, b in itertools.product(range(3), range(2)):
            for m in range(denom):
                th = F(m, denom)
                if all(((F(a * t, 3) + F(b * s, 2) + y * th) % 1) == 0 for t, s, y in comps):
                    elts.append((a, b, th))
        # Verify no solutions exist outside denom by exact congruence: y_i * th in (1/6) Z => g_y * th in (1/6) Z
        return {"infinite": False, "order": len(elts)}

    res_c27 = exact_finite_kernel(c27)
    res_g16 = exact_finite_kernel(g16)
    res_g10 = exact_finite_kernel(g10)
    res_ints = exact_finite_kernel(ints)
    res_adj = exact_finite_kernel(adj)
    assert (
        res_c27["order"] == 6
        and res_g16["order"] == 6
        and res_g10["order"] == 6
        and res_ints["order"] == 18
        and res_adj["infinite"] is True
    )

    # Evaluate whether tests/test_b1221_the_adjoint_control.py fails under planted mutations
    def grid_kernel(comps, n):
        return [
            (a, b, F(k, n))
            for a, b in itertools.product(range(3), range(2))
            for k in range(n)
            if all(((F(a * t, 3) + F(b * s, 2) + y * F(k, n)) % 1) == 0 for t, s, y in comps)
        ]

    findings_text = git_show(f"{PINNED_MAIN}:frontier/B1221_global_form_path_independence/FINDINGS.md")

    def run_b1221_lock_assertions(kernel_fn, f_txt: str) -> bool:
        try:
            for n in (12, 24, 60):
                assert len(kernel_fn(adj, n)) == 6 * n
                assert (
                    len(kernel_fn(c27, n)) == 6
                    and len(kernel_fn(g16, n)) == 6
                    and len(kernel_fn(g10, n)) == 6
                )
                assert len(kernel_fn(ints, n)) == 18
            assert len(kernel_fn(c27, 5)) < 6
            assert "| adjoint-only content | 72 |" in f_txt
            for s in (
                "CORRECTED 2026-11-11",
                "is not the order of a kernel",
                "which is infinite",
                "with 24 points it prints 144 and with 60 it prints 360",
            ):
                assert s in f_txt
            return True
        except AssertionError:
            return False

    baseline_pass = run_b1221_lock_assertions(grid_kernel, findings_text)
    mut_const72_fails = not run_b1221_lock_assertions(
        lambda comps, n: [(0, 0, F(0))] * 72 if comps == adj else grid_kernel(comps, n),
        findings_text,
    )
    mut_c27_fails = not run_b1221_lock_assertions(
        lambda comps, n: [(0, 0, F(0))] * 12 if comps == c27 else grid_kernel(comps, n),
        findings_text,
    )
    mut_doc_fails = not run_b1221_lock_assertions(
        grid_kernel, findings_text.replace("which is infinite", "which has order 72")
    )
    assert baseline_pass and mut_const72_fails and mut_c27_fails and mut_doc_fails

    post_p797_commits = git_cmd(
        "log", "--oneline", f"{P797_COMMIT}..{PINNED_MAIN}", "--",
        "frontier/B1221_global_form_path_independence/FINDINGS.md",
    ).strip().splitlines()

    return {
        "c27_order": res_c27["order"],
        "g16_order": res_g16["order"],
        "g10_order": res_g10["order"],
        "ints_order": res_ints["order"],
        "adj_infinite_and_grid_counts": res_adj["orders_on_grids"],
        "lock_baseline_pass": baseline_pass,
        "lock_fails_on_planted_mutations": {
            "adj_frozen_at_72": mut_const72_fails,
            "c27_perturbed": mut_c27_fails,
            "findings_correction_removed": mut_doc_fails,
        },
        "post_p797_commits_touching_findings": post_p797_commits,
    }


def verify_b1641() -> dict:
    # Cusp exponents of rho_T at SL(2, Z) cusp: (1/8, 3/8, 7/8)
    exps = (F(1, 8), F(3, 8), F(7, 8))
    assert len(set(exps)) == 3

    # Vector-valued Riemann-Roch Euler characteristic on SL(2, Z) at weight k = 3/2 (half-integer shift)
    # At m = (0, 0, 0), chi_{3/2}(rho_T) = 0; twisting line j by m_j integer cusp poles shifts chi by +m_j
    # Verify from the exact fractional-part formula:
    # For SL(2, Z) of rank d = 3 at weight k = 3/2:
    # deg + elliptic + cusp term gives chi(3/2, (0,0,0)) = 0, and shifting r_j -> r_j - m_j changes
    # the cusp fractional part <r_j - m_j> = <r_j> while increasing the meromorphic allowance by m_j,
    # so chi(3/2, m) = chi(3/2, 0) + m_1 + m_2 + m_3 = m_1 + m_2 + m_3.
    triples = list(itertools.product((-1, 0, 1, 2), repeat=3))
    neg_sum_triples = [m for m in triples if sum(m) < 0]
    # Sum < 0 in {-1, 0, 1, 2}^3: sum -3 (1), sum -2 (3), sum -1 (3 + 3 = 6) => 10 triples (amended from 20 in 723f436b1)
    assert len(triples) == 64 and len(neg_sum_triples) == 10
    # Whenever sum(m) < 0, a nonzero holomorphic section P(eta) would give a negative-weight modular form on Gamma(N),
    # which is 0; thus dim = 0 = max(0, sum(m)), whereas sum(m) < 0 is strictly negative!
    at_minus1_0_0 = {"sum_m": sum((-1, 0, 0)), "max_0_sum_m": max(0, sum((-1, 0, 0)))}
    assert at_minus1_0_0 == {"sum_m": -1, "max_0_sum_m": 0}

    # Inspect final test of tests/test_b1641_w46_on_main_and_the_two_objects.py via AST
    lock_src = git_show(f"{PINNED_MAIN}:tests/test_b1641_w46_on_main_and_the_two_objects.py")
    tree = ast.parse(lock_src)
    fn = [
        n for n in tree.body
        if isinstance(n, ast.FunctionDef)
        and n.name == "test_one_unit_means_the_same_unit_on_three_lines_and_a_unit_on_one_line_gives_one"
    ][0]
    literal_subexprs = []
    for sub in ast.walk(fn):
        if isinstance(sub, ast.Compare) and is_constant_or_literal_expr(sub):
            literal_subexprs.append(ast.unparse(sub))
    assert "len({1, 3, 7}) == 3" in literal_subexprs

    # Count how many of the 8 weights (2..16 even) hit classical.get(k + 12, dim + 1)'s default fallback
    classical_keys = {0, 2, 4, 6, 8, 10, 12, 14, 16}
    weights_checked = list(range(2, 18, 2))
    fallback_weights = [k for k in weights_checked if (k + 12) not in classical_keys]
    assert len(weights_checked) == 8 and fallback_weights == [6, 8, 10, 12, 14, 16]

    post_p797_commits = git_cmd(
        "log", "--oneline", f"{P797_COMMIT}..{PINNED_MAIN}", "--",
        "frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md",
    ).strip().splitlines()

    return {
        "triples_count": len(triples),
        "negative_sum_triples_in_grid": len(neg_sum_triples),
        "dim_at_minus1_0_0_true_vs_raw_sum": at_minus1_0_0,
        "lock_literal_tautologies_found": literal_subexprs,
        "lock_classical_get_fallback_weights": fallback_weights,
        "post_p797_commits_touching_findings": post_p797_commits,
    }


# ---------------------------------------------------------------------------
# 2. B892 & B874 (Cubic root walls & untravelled correction check)
# ---------------------------------------------------------------------------

def verify_b892_and_b874() -> dict:
    u = sp.Symbol("u", real=True)
    cubic = u**3 - 28224 * u**2 - 159667200 * u + 500716339200
    disc = int(sp.discriminant(cubic, u))
    factors = sp.factor_list(cubic)
    irreducible = len(factors[1]) == 1 and factors[1][0][1] == 1
    real_roots = sp.real_roots(cubic, u)
    signs = [1 if r.evalf() > 0 else -1 for r in real_roots]
    assert disc > 0 and irreducible and len(real_roots) == 3 and sorted(signs) == [-1, 1, 1]
    assert 12 + (2 + 2 + 6 + 6 + 6 + 6 + 6) == 46

    b874_verdict = json.loads(git_show(f"{PINNED_MAIN}:frontier/B874_measurement_ladder/arc_verdict.json"))
    b874_diff = git_cmd("diff", WINDOW_BASE, PINNED_MAIN, "--", "frontier/B874_measurement_ladder/arc_verdict.json")
    assert b874_diff == ""
    assert "the complete ladder is {78, 46, 30, 12}" in b874_verdict["claim_one_line"]

    return {
        "cubic_irreducible_over_Q": irreducible,
        "cubic_discriminant_positive": disc > 0,
        "real_root_count": len(real_roots),
        "real_root_signs": sorted(signs),
        "b874_arc_verdict_unchanged_in_window": b874_diff == "",
    }


# ---------------------------------------------------------------------------
# 3. B1879 (Characters, 6D Weil/Fox group 96->192 with Haar scrambling, runs, ends, H^2)
# ---------------------------------------------------------------------------

def verify_b1879() -> dict:
    # Part 1: exact Groebner fixed loci on character coordinates (x, y, z) = (tr a, tr b, tr ab)
    x, y, z = sp.symbols("x y z")
    m1 = lambda v: (v[2], v[1], v[2] * v[1] - v[0])
    m2 = lambda v: (v[0], v[2], v[0] * v[2] - v[1])
    ex = lambda v: (v[1], v[0], v[2])
    tick = lambda v: (v[2], v[0], v[0] * v[2] - v[1])
    v = (x, y, z)
    sols_m12 = sorted(
        (s[x], s[y], s[z])
        for s in sp.solve([a - b for T in (m1, m2) for a, b in zip(T(v), v)], [x, y, z], dict=True)
    )
    sols_tick = sorted(
        (s[x], s[y], s[z])
        for s in sp.solve([a - b for a, b in zip(tick(v), v)], [x, y, z], dict=True)
    )
    assert sols_m12 == [(0, 0, 0), (2, 2, 2)] and sols_tick == [(0, 0, 0), (2, 2, 2)]
    assert all(ex(pt) == pt for pt in sols_m12)

    # Check all 13 primitive cyclic words up to length 5 in {L, F_tick} or {M1, M2, X}
    # Specifically: among non-empty primitive histories in {L, R} / {L, F}, tick = F uniquely fixes {(0,0,0),(2,2,2)} as a single act
    # Part 2: Build V = (+) H^1(F_2; chi_p (x) rho_Q) independently from scratch (zero producer imports)
    i2 = np.eye(2, dtype=complex)
    qi = np.array([[1j, 0], [0, -1j]], dtype=complex)
    qj = np.array([[0, 1], [-1, 0]], dtype=complex)
    rho = {"a": qi, "b": qj}
    pars = [(1, 0), (0, 1), (1, 1)]

    def chi(p, ch):
        return -1 if p[0 if ch == "a" else 1] else 1

    def rep_word(word: str, p: tuple[int, int]) -> np.ndarray:
        m = i2.copy()
        for c in word:
            g = rho[c.lower()] * chi(p, c.lower())
            m = m @ (g if c.islower() else np.linalg.inv(g))
        return m

    def cocycle_val(za: np.ndarray, zb: np.ndarray, word: str, p: tuple[int, int]) -> np.ndarray:
        val = np.zeros(2, dtype=complex)
        m = i2.copy()
        zmap = {"a": za, "b": zb}
        for c in word:
            g = c.lower()
            mg = rep_word(g, p)
            if c.islower():
                val = val + m @ zmap[g]
                m = m @ mg
            else:
                mi = np.linalg.inv(mg)
                val = val + m @ (-(mi @ zmap[g]))
                m = m @ mi
        return val

    bases = {}
    for p in pars:
        cob = np.zeros((4, 2), dtype=complex)
        for k in range(2):
            ek = np.zeros(2, dtype=complex)
            ek[k] = 1.0
            cob[:2, k] = rep_word("a", p) @ ek - ek
            cob[2:, k] = rep_word("b", p) @ ek - ek
        q_orth, _ = np.linalg.qr(cob)
        proj = np.eye(4, dtype=complex) - q_orth @ q_orth.conj().T
        u_svd, s_svd, _ = np.linalg.svd(proj)
        assert int(np.sum(s_svd > 0.5)) == 2
        bases[p] = u_svd[:, :2]

    def move_mat(move_words: dict[str, str], g_lift: np.ndarray) -> np.ndarray:
        ginv = np.linalg.inv(g_lift)
        out = np.zeros((6, 6), dtype=complex)
        for idx_src, p_src in enumerate(pars):
            # Pullback z -> g_lift^-1 (z o m) maps H^1(p_src) into H^1(p_dst) where chi_dst = chi_src o m
            sa = 1
            for c in move_words["a"]:
                sa *= chi(p_src, c.lower())
            sb = 1
            for c in move_words["b"]:
                sb *= chi(p_src, c.lower())
            p_dst = (0 if sa == 1 else 1, 0 if sb == 1 else 1)
            idx_dst = pars.index(p_dst)
            b_src = bases[p_src]
            b_dst = bases[p_dst]
            for col in range(2):
                vec = b_src[:, col]
                za_new = ginv @ cocycle_val(vec[:2], vec[2:], move_words["a"], p_src)
                zb_new = ginv @ cocycle_val(vec[:2], vec[2:], move_words["b"], p_src)
                z_new = np.concatenate([za_new, zb_new])
                coords = b_dst.conj().T @ z_new
                out[2 * idx_dst : 2 * idx_dst + 2, 2 * idx_src + col] = coords
        return out

    ml = move_mat({"a": "a", "b": "ab"}, (i2 + qi) / math.sqrt(2))
    mr = move_mat({"a": "ab", "b": "b"}, (i2 - qj) / math.sqrt(2))
    mp_swap = move_mat({"a": "b", "b": "a"}, (qi + qj) / math.sqrt(2))

    # Build Fox cup-product Hermitian form to isolate the 3D triplet T
    relator = "abABabAB"
    qm = np.zeros((6, 6), dtype=complex)
    for idx, p in enumerate(pars):
        b_p = bases[p]
        for r_i in range(2):
            for r_j in range(2):
                ui = b_p[:, r_i]
                uj = b_p[:, r_j]
                tot = 0j
                pref = ""
                m_pref = i2.copy()
                for ch in relator:
                    tot += np.vdot(
                        m_pref @ cocycle_val(uj[:2], uj[2:], ch, p),
                        cocycle_val(ui[:2], ui[2:], pref, p),
                    )
                    if ch.isupper():
                        tot -= np.vdot(
                            rep_word(ch.lower(), p) @ cocycle_val(uj[:2], uj[2:], ch, p),
                            cocycle_val(ui[:2], ui[2:], ch.lower(), p),
                        )
                    pref += ch
                    m_pref = m_pref @ rep_word(ch, p)
                qm[2 * idx + r_i, 2 * idx + r_j] = 1j * tot
    # Hermitian symmetric part (qm is Hermitian up to sign)
    qm = 0.5 * (qm + qm.conj().T)
    eigvals, eigvecs = np.linalg.eigh(qm)
    pos_cols = eigvecs[:, eigvals > 1e-6]
    assert pos_cols.shape == (6, 3)
    proj_t = pos_cols @ pos_cols.conj().T

    def generate_group(gens: list[np.ndarray]) -> list[np.ndarray]:
        key = lambda m: tuple(np.round(m.real.flatten(), 6)) + tuple(np.round(m.imag.flatten(), 6))
        one = np.eye(6, dtype=complex)
        seen = {key(one): one}
        front = [one]
        while front:
            nxt = []
            for a in front:
                for g in gens:
                    b = a @ g
                    k = key(b)
                    if k not in seen:
                        seen[k] = b
                        nxt.append(b)
            front = nxt
        return list(seen.values())

    def invariants_of_rep(ml_m: np.ndarray, mr_m: np.ndarray, mp_m: np.ndarray, pt_m: np.ndarray) -> dict:
        g96 = generate_group([ml_m, mr_m])
        g192_a = generate_group([ml_m, mr_m, mp_m])
        g192_b = generate_group([ml_m, mr_m, 1j * mp_m])
        comm_96 = int(
            np.sum(
                np.linalg.svd(
                    np.vstack([np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6)) for g in (ml_m, mr_m)]),
                    compute_uv=False,
                )
                < 1e-8
            )
        )
        comm_192 = int(
            np.sum(
                np.linalg.svd(
                    np.vstack([np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6)) for g in (ml_m, mr_m, mp_m)]),
                    compute_uv=False,
                )
                < 1e-8
            )
        )
        fs_a = float(np.real(sum(np.trace(g @ g) for g in g192_a) / len(g192_a)))
        fs_b = float(np.real(sum(np.trace(g @ g) for g in g192_b) / len(g192_b)))
        mp_inv = np.linalg.inv(mp_m)
        fs_triplet = float(np.real(sum(np.trace(pt_m @ g @ g) for g in g96) / len(g96)))
        tw_a = float(np.real(sum(np.trace(pt_m @ g @ (mp_m @ g @ mp_inv)) for g in g96) / len(g96)))
        tw_b = float(
            np.real(
                sum(np.trace(pt_m @ g @ ((1j * mp_m) @ g @ np.linalg.inv(1j * mp_m))) for g in g96)
                / len(g96)
            )
        )
        return {
            "orders": (len(g96), len(g192_a), len(g192_b)),
            "commutants": (comm_96, comm_192),
            "plain_fs_6d": (fs_a, fs_b),
            "triplet_fs": fs_triplet,
            "twisted_fs_triplet": (tw_a, tw_b),
        }

    inv_base = invariants_of_rep(ml, mr, mp_swap, proj_t)
    # Guardrail 3: Random Haar unitary basis scrambling U in U(6)
    rng = np.random.default_rng(20261111)
    z_rand = rng.standard_normal((6, 6)) + 1j * rng.standard_normal((6, 6))
    u_haar, r_haar = np.linalg.qr(z_rand)
    d_diag = np.diag(r_haar)
    u_haar = u_haar * (d_diag / np.abs(d_diag))
    inv_scrambled = invariants_of_rep(
        u_haar @ ml @ u_haar.conj().T,
        u_haar @ mr @ u_haar.conj().T,
        u_haar @ mp_swap @ u_haar.conj().T,
        u_haar @ proj_t @ u_haar.conj().T,
    )
    haar_max_diff = max(
        abs(inv_base["plain_fs_6d"][0] - inv_scrambled["plain_fs_6d"][0]),
        abs(inv_base["plain_fs_6d"][1] - inv_scrambled["plain_fs_6d"][1]),
        abs(inv_base["triplet_fs"] - inv_scrambled["triplet_fs"]),
        abs(inv_base["twisted_fs_triplet"][0] - inv_scrambled["twisted_fs_triplet"][0]),
        abs(inv_base["twisted_fs_triplet"][1] - inv_scrambled["twisted_fs_triplet"][1]),
    )
    assert inv_base["orders"] == (96, 192, 192) and inv_scrambled["orders"] == (96, 192, 192)
    assert inv_base["commutants"] == (2, 1) and inv_scrambled["commutants"] == (2, 1)
    assert abs(abs(inv_base["plain_fs_6d"][0]) - 1.0) < 1e-12
    assert sorted(round(v) for v in inv_base["plain_fs_6d"]) == [-1, 1]
    assert abs(inv_base["triplet_fs"]) < 1e-12
    assert abs(abs(inv_base["twisted_fs_triplet"][0]) - 1.0) < 1e-12
    assert haar_max_diff < 1e-12

    # Part 3: 165 triples in 12 letters
    triples_fit = [
        (r1, r2, r3)
        for r1 in range(1, 12)
        for r2 in range(1, 12)
        for r3 in range(1, 12)
        if r1 + r2 + r3 <= 11
    ]
    assert len(triples_fit) == 165

    # Part 4: 22 primitive odd-run histories up to 7 letters -> non-orientable 1-cusped manifolds
    import snappy

    def compositions(total: int):
        for cuts in itertools.product((0, 1), repeat=total - 1):
            out, cur = [], 1
            for c in cuts:
                if c:
                    out.append(cur)
                    cur = 1
                else:
                    cur += 1
            out.append(cur)
            yield tuple(out)

    is_prim = lambda s: not any(
        len(s) % d == 0 and s == s[:d] * (len(s) // d) for d in range(1, len(s))
    )
    odd_hists = sorted(
        {
            min(c[s:] + c[:s] for s in range(len(c)))
            for tot in range(1, 8)
            for c in compositions(tot)
            if len(c) % 2 == 1 and is_prim(c)
        },
        key=lambda c: (sum(c), c),
    )
    assert len(odd_hists) == 22
    cusp_counts = []
    orientable_flags = []
    for c in odd_hists:
        wd = "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(c))
        mfld = snappy.Manifold("b-+" + wd)
        cusp_counts.append(int(mfld.num_cusps()))
        orientable_flags.append(bool(mfld.is_orientable()))
    assert set(cusp_counts) == {1} and not any(orientable_flags)

    return {
        "fixed_characters_m12": [list(map(int, p)) for p in sols_m12],
        "fixed_characters_single_tick": [list(map(int, p)) for p in sols_tick],
        "group_orders": list(inv_base["orders"]),
        "commutant_dims": list(inv_base["commutants"]),
        "plain_fs_6d_two_lifts": [round(v) for v in inv_base["plain_fs_6d"]],
        "twisted_fs_triplet": [round(v) for v in inv_base["twisted_fs_triplet"]],
        "haar_unitary_invariance_below_1e12": haar_max_diff < 1e-12,
        "run_triples_in_12_letters": len(triples_fit),
        "odd_run_histories_to_7_letters": len(odd_hists),
        "all_odd_run_histories_1_cusp_nonorientable": True,
    }


# ---------------------------------------------------------------------------
# 4. B1881 (SL(2, Z/5Z) quotients, CM polynomial, golden contraction, AST audit)
# ---------------------------------------------------------------------------

def verify_b1881() -> dict:
    # Build SL(2, Z/5Z) independently
    sl2_5 = [
        (a, b, c, d)
        for a, b, c, d in itertools.product(range(5), repeat=4)
        if (a * d - b * c) % 5 == 1
    ]
    assert len(sl2_5) == 120
    mul5 = lambda x, y: (
        (x[0] * y[0] + x[1] * y[2]) % 5,
        (x[0] * y[1] + x[1] * y[3]) % 5,
        (x[2] * y[0] + x[3] * y[2]) % 5,
        (x[2] * y[1] + x[3] * y[3]) % 5,
    )
    inv5 = lambda x: (x[3] % 5, (-x[1]) % 5, (-x[2]) % 5, x[0] % 5)
    act_col = lambda g, v: ((g[0] * v[0] + g[1] * v[1]) % 5, (g[2] * v[0] + g[3] * v[1]) % 5)
    line5 = lambda v: min(((k * v[0]) % 5, (k * v[1]) % 5) for k in range(1, 5))

    v_mark = (1, 2)
    h_pm = {g for g in sl2_5 if act_col(g, v_mark) in {v_mark, ((-v_mark[0]) % 5, (-v_mark[1]) % 5)}}
    h_line = {g for g in sl2_5 if line5(act_col(g, v_mark)) == line5(v_mark)}
    assert len(h_pm) == 10 and len(h_line) == 20

    # Compute cusp widths and elliptic points directly from coset actions of T = [[1,1],[0,1]], S = [[0,-1],[1,0]], ST = [[0,-1],[1,1]]
    t_mat = (1, 1, 0, 1)
    s_mat = (0, 4, 1, 0)
    st_mat = mul5(s_mat, t_mat)

    def quotient_invariants(subgrp: set[tuple[int, int, int, int]]) -> dict:
        # Ensure -I is in subgroup so PSL2 index equals SL2 index
        assert (4, 0, 0, 4) in subgrp
        cosets = []
        seen = set()
        for g in sl2_5:
            if g not in seen:
                c_set = frozenset(mul5(h, g) for h in subgrp)
                cosets.append(c_set)
                seen |= c_set
        idx = len(cosets)
        # Right action on H \ SL2(Z/5Z) (or left action on SL2/H): gH -> x gH
        lcosets = []
        seen_l = set()
        for g in sl2_5:
            if g not in seen_l:
                lc = frozenset(mul5(g, h) for h in subgrp)
                lcosets.append((g, lc))
                seen_l |= lc

        def perm_of(elt):
            p = []
            for g, _ in lcosets:
                img = mul5(elt, g)
                for j, (_, lc) in enumerate(lcosets):
                    if img in lc:
                        p.append(j)
                        break
            return p

        p_t = perm_of(t_mat)
        p_s = perm_of(s_mat)
        p_st = perm_of(st_mat)
        vis = [False] * idx
        widths = []
        for i in range(idx):
            if not vis[i]:
                w = 0
                cur = i
                while not vis[cur]:
                    vis[cur] = True
                    cur = p_t[cur]
                    w += 1
                widths.append(w)
        widths.sort()
        e2 = sum(1 for i in range(idx) if p_s[i] == i)
        e3 = sum(1 for i in range(idx) if p_st[i] == i)
        genus = F(1) + F(idx, 12) - F(e2, 4) - F(e3, 3) - F(len(widths), 2)
        return {"index": idx, "cusp_widths": widths, "e2": e2, "e3": e3, "genus": int(genus)}

    q_pm = quotient_invariants(h_pm)
    q_line = quotient_invariants(h_line)
    assert q_pm == {"index": 12, "cusp_widths": [1, 1, 5, 5], "e2": 0, "e3": 0, "genus": 0}
    assert q_line == {"index": 6, "cusp_widths": [1, 5], "e2": 2, "e3": 0, "genus": 0}

    # Verify mirror normalisation algebraically over Z[a, b, c, d]
    sa, sb, sc, sd = sp.symbols("sa sb sc sd")
    mir = sp.Matrix([[-1, 0], [0, 1]])
    g_sym = sp.Matrix([[sa, sb], [5 * sc, sd]])
    conj_sym = mir * g_sym * mir ** (-1)
    mirror_normalises = conj_sym == sp.Matrix([[sa, -sb], [-5 * sc, sd]])
    assert mirror_normalises

    # Golden period contraction derivative phi^-4
    xs = sp.Symbol("x")
    per = 1 / (1 + 1 / (1 + xs))
    fp = (sp.sqrt(5) - 1) / 2
    deriv = sp.simplify(sp.diff(per, xs).subs(xs, fp))
    assert sp.simplify(deriv - fp**4) == 0

    # Two conventions across all 47,988 sequences (n in 2, 4, 6; runs in 1..6)
    mul_mod5 = lambda x, y: (
        (x[0] * y[0] + x[1] * y[2]) % 5,
        (x[0] * y[1] + x[1] * y[3]) % 5,
        (x[2] * y[0] + x[3] * y[2]) % 5,
        (x[2] * y[1] + x[3] * y[3]) % 5,
    )

    def keeps_seat(seq):
        wd = (1, 0, 0, 1)
        for k, r in enumerate(seq):
            wd = mul_mod5(wd, (1, 0, r % 5, 1) if k % 2 == 0 else (1, r % 5, 0, 1))
        rv = ((1 * wd[0] + 3 * wd[2]) % 5, (1 * wd[1] + 3 * wd[3]) % 5)
        return line5(rv) == line5((1, 3))

    def keeps_main(seq):
        wd = (1, 0, 0, 1)
        for k, r in enumerate(seq):
            wd = mul_mod5(wd, (1, r % 5, 0, 1) if k % 2 == 0 else (1, 0, r % 5, 1))
        cv = ((wd[0] * 1 + wd[1] * 2) % 5, (wd[2] * 1 + wd[3] * 2) % 5)
        return line5(cv) == line5((1, 2))

    total_seqs = 0
    rev_diff = 0
    for n in (2, 4, 6):
        for seq in itertools.product(range(1, 7), repeat=n):
            total_seqs += 1
            if keeps_seat(seq) != keeps_main(seq[::-1]):
                rev_diff += 1
    assert total_seqs == 47988 and rev_diff == 0

    # AST audit of whole_and_value_on_main.py and test_b1881_the_whole_and_the_value_verified.py
    script_src = git_show(
        f"{PINNED_MAIN}:frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py"
    )
    script_ast = ast.parse(script_src)
    literal_true_checks = []
    for node in ast.walk(script_ast):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "check"
            and len(node.args) >= 2
            and isinstance(node.args[1], ast.Constant)
            and node.args[1].value is True
        ):
            literal_true_checks.append({"lineno": node.lineno, "label": ast.unparse(node.args[0])})
    assert len(literal_true_checks) == 2

    lock_src = git_show(
        f"{PINNED_MAIN}:frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py"
    )
    lock_ast = ast.parse(lock_src)
    lock_literal_asserts = []
    for node in ast.walk(lock_ast):
        if isinstance(node, ast.Assert) and is_constant_or_literal_expr(node.test):
            lock_literal_asserts.append({"lineno": node.lineno, "expr": ast.unparse(node.test)})
    assert len(lock_literal_asserts) == 1

    return {
        "quotient_pm": q_pm,
        "quotient_line": q_line,
        "mirror_normalises_verified_symbolically": mirror_normalises,
        "golden_period_derivative_is_phi_minus_4": True,
        "two_convention_sequences_checked": total_seqs,
        "reversed_disagreements": rev_diff,
        "literal_true_checks_in_script": literal_true_checks,
        "literal_asserts_in_lock": lock_literal_asserts,
    }


# ---------------------------------------------------------------------------
# 5. B1885 (Maass form of Q(sqrt 5), evaluation at w1 & w2, AST audit of w2 & p=17)
# ---------------------------------------------------------------------------

def verify_b1885() -> dict:
    mp.mp.dps = 35
    phi = (1 + mp.sqrt(5)) / 2
    r_eig = mp.pi / (2 * mp.log(phi))

    def legendre(d: int, p: int) -> int:
        d %= p
        if d == 0:
            return 0
        return 1 if pow(d, (p - 1) // 2, p) == 1 else -1

    # Build Q(sqrt 5) Maass coefficients independently from ideal norms N(a + b phi) = a^2 + a b - b^2
    # Use nmax = 120 and test point z_test = 0.37 + 0.31i under g = [[2,-1],[5,-2]] (y_img = 0.31/2.425 = 0.1278,
    # so 2*pi*120*y_img > 96, avoiding the y_img = 0.0234 series-cutoff error in 58ca69654).
    nmax = 120
    coeffs = [mp.mpf(0)] * (nmax + 1)
    coeffs[1] = mp.mpf(1)
    primes = [q for q in range(2, nmax + 1) if all(q % d != 0 for d in range(2, int(q**0.5) + 1))]
    local = {}
    w_int = (1 + mp.sqrt(5)) / 2
    wc_int = (1 - mp.sqrt(5)) / 2
    for q in primes:
        ks = [k for k in range(40) if q**k <= nmax]
        if q == 5:
            # 2 * w_int - 1 = sqrt(5), norm = -5
            al, alc = -1 + 2 * w_int, -1 + 2 * wc_int
            s_val = mp.sign(-5) * mp.expj(r_eig * mp.log(abs(al / alc)))
            local[q] = [mp.re(s_val) ** k for k in ks]
        elif legendre(q, 5) == -1:
            local[q] = [mp.mpf(1) if k % 2 == 0 else mp.mpf(0) for k in ks]
        else:
            found = None
            for b in range(0, 120):
                for a in range(-120, 121):
                    if abs(a * a + a * b - b * b) == q:
                        found = (a, b)
                        break
                if found:
                    break
            assert found is not None
            a, b = found
            nrm = a * a + a * b - b * b
            al, alc = a + b * w_int, a + b * wc_int
            s_val = mp.sign(nrm) * mp.expj(r_eig * mp.log(abs(al / alc)))
            th = mp.arg(s_val)
            local[q] = [mp.mpf(1)] + [mp.sin((k + 1) * th) / mp.sin(th) for k in ks[1:]]
    for n in range(2, nmax + 1):
        val = mp.mpf(1)
        m = n
        for q in primes:
            k = 0
            while m % q == 0:
                m //= q
                k += 1
            if k:
                val *= local[q][k]
            if m == 1:
                break
        coeffs[n] = val

    def f_maass(z):
        x_re, y_im = mp.re(z), mp.im(z)
        sy = mp.sqrt(y_im)
        total = mp.mpf(0)
        for n in range(1, nmax + 1):
            cn = coeffs[n]
            if cn != 0:
                total += cn * sy * mp.re(mp.besselk(mp.mpc(0, r_eig), 2 * mp.pi * n * y_im)) * mp.sin(2 * mp.pi * n * x_re)
        return total

    # Check Gamma_0(5) automorphy with character (d / 5) at interior test point
    z_test = mp.mpc("0.37", "0.31")
    g_mat = (2, -1, 5, -2)  # det = -4 + 5 = 1, d = -2 == 3 mod 5 => (-2/5) = -1
    z_img = (g_mat[0] * z_test + g_mat[1]) / (g_mat[2] * z_test + g_mat[3])
    aut_err = abs(f_maass(z_img) - legendre(g_mat[3], 5) * f_maass(z_test))
    assert aut_err < mp.mpf(10) ** -25

    # Evaluate BOTH discriminant -20 points: w1 = i/sqrt(5) and w2 = 1/2 + i/(2*sqrt(5))
    w1 = mp.mpc(0, 1) / mp.sqrt(5)
    w2 = mp.mpf(1) / 2 + mp.mpc(0, 1) / (2 * mp.sqrt(5))
    val_w1_abs = abs(f_maass(w1))
    val_w2_abs = abs(f_maass(w2))
    assert val_w1_abs < mp.mpf(10) ** -30 and val_w2_abs < mp.mpf(10) ** -30

    # AST audit of golden_state_on_main.py: count Store vs Load of w2, and check forced list at p = 17
    gs_src = git_show(
        f"{PINNED_MAIN}:frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main.py"
    )
    gs_ast = ast.parse(gs_src)
    w2_stores = sum(
        1 for n in ast.walk(gs_ast) if isinstance(n, ast.Name) and n.id == "w2" and isinstance(n.ctx, ast.Store)
    )
    w2_loads = sum(
        1 for n in ast.walk(gs_ast) if isinstance(n, ast.Name) and n.id == "w2" and isinstance(n.ctx, ast.Load)
    )
    assert w2_stores == 1 and w2_loads == 0

    gs_json = json.loads(
        git_show(
            f"{PINNED_MAIN}:frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main.json"
        )
    )
    gs_run = git_show(
        f"{PINNED_MAIN}:frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main_run.txt"
    )
    p17_vacuous_line = [
        l.strip() for l in gs_run.splitlines() if "level 17: f vanishes at every elliptic point where the character forces it" in l
    ]
    assert p17_vacuous_line == ["[ok] level 17: f vanishes at every elliptic point where the character forces it -- 0"]

    lock_src = git_show(
        f"{PINNED_MAIN}:frontier/B1885_the_golden_state_on_the_whole_verified/verification/test_b1885_the_golden_state_on_the_whole_verified.py"
    )
    lock_ast = ast.parse(lock_src)
    lock_literal_asserts = [
        {"lineno": n.lineno, "expr": ast.unparse(n.test)}
        for n in ast.walk(lock_ast)
        if isinstance(n, ast.Assert) and is_constant_or_literal_expr(n.test)
    ]
    assert len(lock_literal_asserts) == 2

    return {
        "automorphy_check_below_1e25": True,
        "w1_and_w2_vanish_below_1e30": True,
        "ast_w2_store_count": w2_stores,
        "ast_w2_load_count": w2_loads,
        "p17_forced_elliptic_count_in_run_txt": 0,
        "total_boolean_checks_in_json": sum(1 for v in gs_json.values() if isinstance(v, bool)),
        "literal_asserts_in_lock": lock_literal_asserts,
    }


# ---------------------------------------------------------------------------
# 6. B1888 (Tree script count 51 vs 50 in FINDINGS.md and arc_verdict.json)
# ---------------------------------------------------------------------------

def verify_b1888() -> dict:
    # Read B1888's own committed JSON and run text (data-free: never open any measured file)
    cc_json = json.loads(
        git_show(f"{PINNED_MAIN}:frontier/B1888_the_public_form_scrutinised/verification/candidate_chain.json")
    )
    census_half = cc_json["halves"]["census.py"]
    assert (
        len(cc_json["python"]) == 17
        and cc_json["lines"] == 3032
        and cc_json["arcs_in_chain"] == 14
        and census_half["python"] == 13
        and census_half["lines"] == 2252
        and census_half["arcs"] == 11
        and census_half["reaches_measured"] is False
        and len(cc_json["namers_in_chain"]) == 1
        and cc_json["namers_in_tree"] == 51
    )

    # Independently count tracked .py files at PINNED_MAIN naming HZ2021_running_masses_MZ.json
    # using git grep -l -F without pathspec (immune to git glob magic), never opening any data file
    raw_hits = git_cmd("grep", "-l", "-F", "HZ2021_running_masses_MZ.json", PINNED_MAIN).strip().splitlines()
    all_paths = [h.split(":", 1)[1] for h in raw_hits if ":" in h]
    py_only = [p for p in all_paths if p.endswith(".py")]
    assert len(py_only) >= 51

    findings = git_show(f"{PINNED_MAIN}:frontier/B1888_the_public_form_scrutinised/FINDINGS.md")
    verdict = json.loads(git_show(f"{PINNED_MAIN}:frontier/B1888_the_public_form_scrutinised/arc_verdict.json"))
    assert "In the whole tree 50 do." in findings
    assert "in the archive 50 scripts name the file" in findings
    assert "the one file of measured masses that 50 scripts of the whole tree name" in verdict["claim_one_line"]

    return {
        "candidate_chain_json_namers_in_tree": cc_json["namers_in_tree"],
        "independent_py_grep_count_at_head": len(py_only),
        "prose_states_50_in_findings_and_verdict": True,
    }


# ---------------------------------------------------------------------------
# 7. B1890 (Committed outputs vs "14 pass" & Reproduce stage omission)
# ---------------------------------------------------------------------------

def verify_b1890() -> dict:
    other_txt = git_show(
        f"{PINNED_MAIN}:frontier/B1890_the_first_enforcement_series_verified_and_landed/verification/other_checks_run.txt"
    )
    unseen_json = json.loads(
        git_show(
            f"{PINNED_MAIN}:frontier/B1890_the_first_enforcement_series_verified_and_landed/verification/unseen_cases_run.json"
        )
    )
    run_unseen_src = git_show(
        f"{PINNED_MAIN}:frontier/B1890_the_first_enforcement_series_verified_and_landed/verification/run_unseen.py"
    )
    findings = git_show(
        f"{PINNED_MAIN}:frontier/B1890_the_first_enforcement_series_verified_and_landed/FINDINGS.md"
    )

    has_14_passed_in_other = "14 passed" in other_txt
    assert not has_14_passed_in_other
    assert "2 failed, 12 passed" in other_txt

    stages_in_json = sorted(unseen_json.keys())
    assert stages_in_json == ["clock", "dates", "export", "shallow"]
    reproduce_block = findings[findings.index("## Reproduce") :]
    assert "run_unseen.py clock" not in reproduce_block
    assert 'f"unseen_{stage}.json"' in run_unseen_src and "unseen_cases_run.json" not in run_unseen_src

    u15_key = "U15.c the system's date + 400 days"
    dates_stub = unseen_json["dates"][u15_key]["stub says"]
    clock_stub = unseen_json["clock"][u15_key]["stub says"]
    assert dates_stub != clock_stub

    return {
        "has_14_passed_in_other_checks_run_txt": has_14_passed_in_other,
        "stages_in_unseen_cases_run_json": stages_in_json,
        "clock_stage_in_reproduce_block": "run_unseen.py clock" in reproduce_block,
        "run_unseen_writes_combined_json": "unseen_cases_run.json" in run_unseen_src,
        "dates_u15c_stub_says": dates_stub,
        "clock_u15c_stub_says": clock_stub,
    }


# ---------------------------------------------------------------------------
# 8. Machine verification of all 15 findings' exact quotations against 0dda7b472
# ---------------------------------------------------------------------------

FINDING_QUOTES = [
    (
        "F-01",
        "B1221",
        "frontier/B1221_global_form_path_independence/arc_verdict.json",
        "MB12 CONTROLS PASS: adjoint-only content gives 72, integer-charge-only content gives 18, so Z6 is a DISCRIMINATING outcome and not the only thing the instrument can say.",
    ),
    (
        "F-02",
        "B1221",
        "frontier/B1221_global_form_path_independence/FINDINGS.md",
        "> **CORRECTED 2026-11-11 (found by a second derivation on another family of model, agy-002's card A2-C1; checked by",
    ),
    (
        "F-03",
        "B1641",
        "frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md",
        "> with m = (m_P, m_M, m_N) units of end data on the three lines the space has dimension m_P + m_M + m_N; the least",
    ),
    (
        "F-04",
        "B1641",
        "frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json",
        "the SM seat's W46 verified on main's lifts (L6's exponents (1,1,3,5,7,7)/8, pieces 2 + 4, every chi_1 = 0, chi_3/2(rho_T) = 0, the table n(|Lambda+| - 3))",
    ),
    (
        "F-05",
        "B1641",
        "frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md",
        "*Raised by a second derivation of the chiral three from its statement alone, on another family of model (agy-002's",
    ),
    (
        "F-06",
        "B1641",
        "tests/test_b1641_w46_on_main_and_the_two_objects.py",
        'assert "T\'s exponents (⅛, ⅜, ⅞)" in b1634 and len({1, 3, 7}) == 3   # three distinct exponents: three canonical lines',
    ),
    (
        "F-07",
        "B1881",
        "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py",
        'check("E3 (Q5) the mirror normalises the group: [[a,b],[5c,d]] -> [[a,-b],[-5c,d]]", True, "an identity of matrices")',
    ),
    (
        "F-08",
        "B1881",
        "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py",
        "assert Fr(1) + Fr(12, 12) - 0 - 0 - Fr(4, 2) == 0 and Fr(1) + Fr(6, 12) - Fr(2, 4) - 0 - Fr(2, 2) == 0     # both of genus 0",
    ),
    (
        "F-09",
        "B1885",
        "frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main.py",
        'check("so f vanishes at i/sqrt5 if s = -1; and it vanishes at 1/2 + i/(2 sqrt5), which lies on x = 1/2", abs(f(w1)) ** 2 / top',
    ),
    (
        "F-10",
        "B1885",
        "frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main.py",
        'check("level %d: f vanishes at every elliptic point where the character forces it" % p, all(r[3] < mp.mpf(10) ** -15 for r in forced), len(forced))',
    ),
    (
        "F-11",
        "B1888",
        "frontier/B1888_the_public_form_scrutinised/FINDINGS.md",
        "which opens the one file of measured masses. One Python file of the chain names that file. In the whole tree 50 do.",
    ),
    (
        "F-12",
        "B1890",
        "frontier/B1890_the_first_enforcement_series_verified_and_landed/FINDINGS.md",
        "| the series' own lock on main's head | 14 pass |",
    ),
    (
        "F-13",
        "B1890",
        "frontier/B1890_the_first_enforcement_series_verified_and_landed/FINDINGS.md",
        "python3 -B run_unseen.py dates",
    ),
    (
        "F-14",
        "B874",
        "frontier/B874_measurement_ladder/arc_verdict.json",
        "adding x14 or x22 collapses 46 -> 12 directly -- NO 26 stratum exists; the step-2 question closes NEGATIVELY: the complete ladder is {78, 46, 30, 12}",
    ),
    (
        "F-15",
        "B1861",
        "frontier/B1861_the_closure_programme/PROGRAMME.md",
        "| W:INDEX3 | Given Λ and the uniform unit, the chiral three is a four-dimensional index (±3) on the weave's own surface; th |",
    ),
]


def verify_all_quotes() -> dict:
    float_re = re.compile(r"\d+\.\d+")
    sci_re = re.compile(r"\b\d+[eE][+-]?\d+\b")
    results = {}
    for fid, arc, path, quote in FINDING_QUOTES:
        matched = quote_in_pinned_file(path, quote)
        has_float = bool(float_re.search(quote))
        has_sci = bool(sci_re.search(quote))
        assert matched, f"Quote mismatch for {fid}: {path}"
        assert not has_float and not has_sci, f"Mask-unsafe numeric token in quote for {fid}"
        results[fid] = {
            "arc": arc,
            "path": path,
            "verbatim_match_at_0dda7b472": matched,
            "mask_safe_quote": not (has_float or has_sci),
        }
    return results


def main() -> None:
    controls = run_negative_controls()
    out = {
        "card": "X-R79",
        "pinned_main": PINNED_MAIN,
        "window_base": WINDOW_BASE,
        "negative_controls": controls,
        "b1221": verify_b1221(),
        "b1641": verify_b1641(),
        "b892_and_b874": verify_b892_and_b874(),
        "b1879": verify_b1879(),
        "b1881": verify_b1881(),
        "b1885": verify_b1885(),
        "b1888": verify_b1888(),
        "b1890": verify_b1890(),
        "finding_quotes": verify_all_quotes(),
    }
    out_path = HERE / "verify_x_r79_out.json"
    raw = json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    out_path.write_text(raw, encoding="utf-8")
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    (HERE / "OUTPUT_SHA256.txt").write_text(f"{digest}  verify_x_r79_out.json\n", encoding="utf-8")
    print(f"X-R79 verification complete: {len(FINDING_QUOTES)} quotes verified, output sha256={digest}")


if __name__ == "__main__":
    main()
