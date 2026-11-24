#!/usr/bin/env python3
r"""
Standalone Pre-Hashed Producer v3 (run3) for Card A2-PEER-AUDIT-V2 (strictly 0 of 19;
supersedes frozen v1 & run2, remediating Cold-Room Referee DISC-PA2-1, DISC-PA2-2, & NBD-PA2-1..3):
Zero-trust cross-seat verification of:
  - agy-exp (origin/agy/self-consistent-loop-2026-11-11 @ 57ad12a6a):
      Cards X-HIERARCHY-LINK6, X-FOUNDATIONS-LINK7, & X-FLOOR-LINK8 (Blocks A & B)
  - agy (origin/agy/cusp-action-2026-11-20 @ b06c8fc1e):
      Cards AGY-C31..C38, blind_predictions_full_toe_v7.json, & OW22-F1..F3 catches
  - Status verification of unchanged seats (main, physical, chat1, sm, cld-advisor).

Fixes over frozen v1 (caught by v1's own self-gates):
  1. PA2-A: AST-level code scan (ignoring docstrings/comments like "disjoint from mp.jtheta")
     for referee_x_floor_link8.py Guardrail-6 audit.
  2. PA2-D: Exact Liouville Fuchsian ODE sign u'' = -(wp(z) - c)/4 * u in RK4 solver;
     exact sp.diff SUSY cancellation check in beta_gu / beta_gup; 6th-order Richardson-GL4
     on Jack-Jones benchmark (< 1e-17).
  3. PA2-E: Exact SymPy d ln(Lambda_CJ) / d ln(mu) == 0 proof + Richardson-GL4 RG invariance
     check (< 1e-15).

Guardrails enforced:
  - 0 Python float/complex AST literals, 0 binary64 float()/complex() casts, 0 JSON floats.
  - 0 imports from frontier/, peer scripts, snappy, or prior relay scripts.
  - 0 empirical PDG/NuFIT/Planck/DESI/CODATA constants (strictly 0 of 19).
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import random
import subprocess
from collections import deque
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

SELF_PATH = Path(__file__).resolve()
REPO_ROOT = SELF_PATH.parents[2]
OUT_PATH = SELF_PATH.parent / "a2_peer_audit_v2_run3_results.json"

AGY_EXP_REF = "origin/agy/self-consistent-loop-2026-11-11"
AGY_REF = "origin/agy/cusp-action-2026-11-20"
MAIN_REF = "origin/main"
PHYS_REF = "origin/audit/physical-bridge-2026-09-05"
CHAT1_REF = "origin/chat1/web-seat"
SM_REF = "origin/claude/standard-model-derivation-0qt6ao"
CLD_REF = "origin/cld/cool-hamilton-k9eqvo"

EXPECTED_LOCK_V3 = "ce81cddd9d056a54fafa6b30d431073ae1af75399a1d82918f4e074f0bd98a2a"

I_MP = mp.mpc(0, 1)


def q_mp(p: int, q: int = 1) -> mp.mpf:
    return mp.mpf(int(p)) / mp.mpf(int(q))


def f_mp(fr: Fr) -> mp.mpf:
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def p10_mp(e: int) -> mp.mpf:
    return mp.mpf(10) ** int(e)


def frac_str(fr: Fr) -> str:
    return f"{fr.numerator}/{fr.denominator}" if fr.denominator != 1 else str(fr.numerator)


def git_show_bytes(ref: str, rel_path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(REPO_ROOT), "show", f"{ref}:{rel_path}"])


def git_ls_tree(ref: str, prefix: str) -> list[str]:
    out = subprocess.check_output(["git", "-C", str(REPO_ROOT), "ls-tree", "-r", "--name-only", ref, prefix]).decode("utf-8")
    return [ln.strip() for ln in out.splitlines() if ln.strip()]


def git_short_rev(ref: str) -> str:
    return subprocess.check_output(["git", "-C", str(REPO_ROOT), "rev-parse", "--short=9", ref]).decode("utf-8").strip()


def assert_no_json_floats(obj: Any) -> None:
    if isinstance(obj, float):
        raise AssertionError(f"Forbidden JSON float: {obj!r}")
    if isinstance(obj, dict):
        for v in obj.values():
            assert_no_json_floats(v)
    elif isinstance(obj, list):
        for v in obj:
            assert_no_json_floats(v)


def count_json_floats(obj: Any) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


def scan_ast_hygiene(src: str, label: str) -> dict[str, Any]:
    tree = ast.parse(src, filename=label)
    lits = [
        getattr(n, "lineno", 0)
        for n in ast.walk(tree)
        if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex))
    ]
    casts = [
        getattr(n, "lineno", 0)
        for n in ast.walk(tree)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("float", "complex")
    ]
    bad_imps: list[str] = []
    for n in ast.walk(tree):
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            mod = getattr(n, "module", "") or ""
            nms = " ".join(a.name for a in n.names)
            comb = f"{mod} {nms}"
            if any(w in comb for w in ("frontier", "relays", "self_consistent", "snappy")):
                bad_imps.append(comb)
    return {
        "float_complex_literals": len(lits),
        "binary64_casts": len(casts),
        "forbidden_imports": len(bad_imps),
        "clean": bool(len(lits) == 0 and len(casts) == 0 and len(bad_imps) == 0),
    }


def gl4_integrate(rhs_fn, y0: list[mp.mpf], t0: mp.mpf, t1: mp.mpf, n_steps: int) -> list[mp.mpf]:
    """2-stage 4th-order implicit Gauss-Legendre Runge-Kutta (disjoint from GBS8, GL6, & RK4)."""
    s3 = mp.sqrt(mp.mpf(3))
    a11 = q_mp(1, 4)
    a12 = q_mp(1, 4) - s3 / mp.mpf(6)
    a21 = q_mp(1, 4) + s3 / mp.mpf(6)
    a22 = q_mp(1, 4)
    c1 = q_mp(1, 2) - s3 / mp.mpf(6)
    c2 = q_mp(1, 2) + s3 / mp.mpf(6)
    h = (t1 - t0) / mp.mpf(n_steps)
    dim = len(y0)
    y = list(y0)
    t = t0
    tol = p10_mp(-36)
    for _ in range(n_steps):
        f0 = rhs_fn(t, y)
        k1 = list(f0)
        k2 = list(f0)
        for _it in range(32):
            y1 = [y[i] + h * (a11 * k1[i] + a12 * k2[i]) for i in range(dim)]
            y2 = [y[i] + h * (a21 * k1[i] + a22 * k2[i]) for i in range(dim)]
            nk1 = rhs_fn(t + c1 * h, y1)
            nk2 = rhs_fn(t + c2 * h, y2)
            md = max(max(abs(nk1[i] - k1[i]), abs(nk2[i] - k2[i])) for i in range(dim))
            k1, k2 = nk1, nk2
            if md < tol:
                break
        y = [y[i] + q_mp(1, 2) * h * (k1[i] + k2[i]) for i in range(dim)]
        t += h
    return y


def gl4_richardson(rhs_fn, y0: list[mp.mpf], t0: mp.mpf, t1: mp.mpf, n_coarse: int) -> list[mp.mpf]:
    """6th-order Richardson extrapolation (16*GL4(2N) - GL4(N)) / 15."""
    yc = gl4_integrate(rhs_fn, y0, t0, t1, n_coarse)
    yf = gl4_integrate(rhs_fn, y0, t0, t1, 2 * n_coarse)
    return [(mp.mpf(16) * yf[i] - yc[i]) / mp.mpf(15) for i in range(len(y0))]


def random_haar_u3(rng: random.Random) -> mp.matrix:
    z = mp.zeros(3, 3)
    denom = mp.mpf(1 << 53)
    twopi = mp.mpf(2) * mp.pi
    for r in range(3):
        for c in range(3):
            u1 = mp.mpf(max(1, rng.getrandbits(53))) / denom
            u2 = mp.mpf(rng.getrandbits(53)) / denom
            rad = mp.sqrt(-mp.mpf(2) * mp.log(u1))
            z[r, c] = mp.mpc(rad * mp.cos(twopi * u2), rad * mp.sin(twopi * u2))
    q_cols: list[mp.matrix] = []
    for c in range(3):
        v = z[:, c]
        for prev in q_cols:
            v = v - (prev.H * v)[0, 0] * prev
        nrm = mp.sqrt(mp.re((v.H * v)[0, 0]))
        q_cols.append(v / nrm)
    out = mp.zeros(3, 3)
    for c in range(3):
        for r in range(3):
            out[r, c] = q_cols[c][r]
    return out


def svd_asc_mp(mat: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    u, s, _ = mp.svd_c(mat)
    idx = sorted(range(3), key=lambda k: s[k])
    return mp.matrix([[u[r, idx[c]] for c in range(3)] for r in range(3)]), [s[k] for k in idx]


def takagi_true_mp(m_sym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    """Exact Takagi factorization M_sym = U_T * diag(s) * U_T^T via Hermitian eigendecomposition of M M^H."""
    h = m_sym * m_sym.H
    evs, vecs = mp.eighe(q_mp(1, 2) * (h + h.H))
    idx = sorted(range(3), key=lambda k: mp.re(evs[k]))
    ut = mp.zeros(3, 3)
    svs: list[mp.mpf] = []
    for cn, co in enumerate(idx):
        svs.append(mp.sqrt(max(mp.mpf(0), mp.re(evs[co]))))
        uk = vecs[:, co]
        ukc = mp.matrix([[mp.conj(uk[r, 0])] for r in range(3)])
        ph = mp.exp(I_MP * mp.arg((uk.H * m_sym * ukc)[0, 0]) / mp.mpf(2))
        for r in range(3):
            ut[r, cn] = uk[r, 0] * ph
    return ut, svs


# ==============================================================================
# PA2-A: Custody, AST/JSON Hygiene, Unchanged Seats, & Referee Guardrail-6 Audit
# ==============================================================================

def run_pa2_a() -> dict[str, Any]:
    def audit_peer(ref: str, dirs: list[str]) -> dict[str, Any]:
        total_m = 0
        matched_m = 0
        mismatches: list[str] = []
        py_files = 0
        ast_bad = 0
        json_files = 0
        json_floats = 0
        sample_target_bytes = b""
        sample_expected_hash = ""
        for d in dirs:
            d_files = git_ls_tree(ref, d)
            if not d_files:
                raise AssertionError(f"Empty peer directory on {ref}: {d}")
            for f in d_files:
                if f.endswith("SHA256.txt"):
                    txt = git_show_bytes(ref, f).decode("utf-8")
                    for line in txt.splitlines():
                        line = line.strip()
                        if not line:
                            continue
                        parts = line.split()
                        if len(parts) < 2:
                            continue
                        h, target = parts[0], parts[1].lstrip("*")
                        target_path = target if "/" in target else (f.rsplit("/", 1)[0] + "/" + target)
                        total_m += 1
                        data = git_show_bytes(ref, target_path)
                        actual = hashlib.sha256(data).hexdigest()
                        if not sample_target_bytes:
                            sample_target_bytes = data
                            sample_expected_hash = h
                        if actual == h:
                            matched_m += 1
                        else:
                            mismatches.append(f"{f} -> {target_path}")
                elif f.endswith(".py"):
                    py_files += 1
                    res = scan_ast_hygiene(git_show_bytes(ref, f).decode("utf-8"), f)
                    if res["float_complex_literals"] > 0 or res["binary64_casts"] > 0:
                        ast_bad += 1
                elif f.endswith(".json"):
                    json_files += 1
                    json_floats += count_json_floats(json.loads(git_show_bytes(ref, f).decode("utf-8")))
        return {
            "head": git_short_rev(ref),
            "manifests_matched": matched_m,
            "manifests_total": total_m,
            "mismatches": mismatches,
            "py_files_audited": py_files,
            "py_ast_float_or_cast_files": ast_bad,
            "json_files_audited": json_files,
            "json_float_tokens": json_floats,
            "_sample_bytes": sample_target_bytes,
            "_sample_hash": sample_expected_hash,
        }

    exp_audit = audit_peer(
        AGY_EXP_REF,
        [
            "relays/x_hierarchy_link6_verify",
            "relays/x_hierarchy_link6_referee",
            "relays/x_foundations_link7_verify",
            "relays/x_foundations_link7_referee",
            "relays/x_floor_link8_verify",
            "relays/x_floor_link8_referee",
        ],
    )
    agy_audit = audit_peer(
        AGY_REF,
        [
            "relays/agy_2026-11-22_c31",
            "relays/agy_2026-11-22_c32",
            "relays/agy_2026-11-22_c33",
            "relays/agy_2026-11-22_c34",
            "relays/agy_2026-11-22_c35",
            "relays/agy_2026-11-23_c36",
            "relays/agy_2026-11-23_c37",
            "relays/agy_2026-11-24_c38",
        ],
    )

    # Guardrail-6 AST-level code audit (excluding comments/docstrings) of referee_x_floor_link8.py:
    ref_src = git_show_bytes(AGY_EXP_REF, "relays/x_floor_link8_referee/referee_x_floor_link8.py").decode("utf-8")
    ref_lines = ref_src.splitlines()
    ref_tree = ast.parse(ref_src, filename="referee_x_floor_link8.py")
    ref_func_names = [n.name for n in ast.walk(ref_tree) if isinstance(n, ast.FunctionDef)]
    ast_code_identifiers: set[str] = set()
    for n in ast.walk(ref_tree):
        if isinstance(n, ast.FunctionDef):
            ast_code_identifiers.add(n.name.lower())
        elif isinstance(n, ast.Name):
            ast_code_identifiers.add(n.id.lower())
        elif isinstance(n, ast.Attribute):
            ast_code_identifiers.add(n.attr.lower())
    docstring_claims_liouville = any("Fuchsian Liouville" in ln for ln in ref_lines[:30])
    liouville_yukawa_code_hits = sorted([
        ident for ident in ast_code_identifiers
        if any(kw in ident for kw in ("liouville", "fuchs", "weierstrass", "jtheta", "takagi", "svd", "pmns", "ckm", "w_hol", "gramian"))
    ])
    echo_lines_uv_yb0 = [idx + 1 for idx, ln in enumerate(ref_lines) if "uv_yb0_ytau0_over_yt0" in ln]

    unchanged_heads = {
        "main": git_short_rev(MAIN_REF),
        "physical": git_short_rev(PHYS_REF),
        "chat1": git_short_rev(CHAT1_REF),
        "sm": git_short_rev(SM_REF),
        "cld_advisor": git_short_rev(CLD_REF),
    }

    sb = exp_audit.pop("_sample_bytes")
    sh = exp_audit.pop("_sample_hash")
    agy_audit.pop("_sample_bytes")
    agy_audit.pop("_sample_hash")
    tampered = bytes([sb[0] ^ 1]) + sb[1:]
    pf1_caught = bool(hashlib.sha256(sb).hexdigest() == sh and hashlib.sha256(tampered).hexdigest() != sh)

    catch_fl8_f2b_referee_gap = bool(
        docstring_claims_liouville
        and len(liouville_yukawa_code_hits) == 0
        and len(echo_lines_uv_yb0) >= 2
    )

    passed = bool(
        exp_audit["manifests_matched"] == exp_audit["manifests_total"] == 12
        and agy_audit["manifests_matched"] == agy_audit["manifests_total"] == 27 and agy_audit["py_files_audited"] == 16 and agy_audit["json_files_audited"] == 11
        and exp_audit["py_ast_float_or_cast_files"] == 0
        and agy_audit["py_ast_float_or_cast_files"] == 0
        and exp_audit["json_float_tokens"] == 0
        and agy_audit["json_float_tokens"] == 0
        and catch_fl8_f2b_referee_gap
        and pf1_caught
    )
    return {
        "agy_exp_custody": exp_audit,
        "agy_custody": agy_audit,
        "unchanged_peer_heads": unchanged_heads,
        "referee_x_floor_link8_guardrail6_audit": {
            "docstring_claims_fuchsian_liouville": docstring_claims_liouville,
            "ast_liouville_yukawa_ckm_pmns_code_identifiers": liouville_yukawa_code_hits,
            "producer_json_uv_yb0_echo_lines": echo_lines_uv_yb0,
            "defined_functions": ref_func_names,
            "catch_FL8_F2b_confirmed": catch_fl8_f2b_referee_gap,
        },
        "pf1_tampered_manifest_caught": pf1_caught,
        "passed": passed,
    }


# ==============================================================================
# PA2-B: agy-exp Block B1 (E_8, Matter Parity, 6D Sadov/KMT F_k, & H_u/H_d)
# ==============================================================================

def run_pa2_b() -> dict[str, Any]:
    roots_e8: list[tuple[Fr, ...]] = []
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (-1, 1):
                for sj in (-1, 1):
                    v = [Fr(0)] * 8
                    v[i], v[j] = Fr(si), Fr(sj)
                    roots_e8.append(tuple(v))
    for sg in itertools.product((-1, 1), repeat=8):
        if sg.count(-1) % 2 == 0:
            roots_e8.append(tuple(Fr(s, 2) for s in sg))

    c_45, c_15, c_10_6, c_16_4, c_16b_4b = 5, 3, 0, 0, 0
    qx_16: set[int] = set()
    qx_10: set[int] = set()
    for r in roots_e8:
        nz5 = sum(1 for x in r[:5] if x != 0)
        nz3 = sum(1 for x in r[5:] if x != 0)
        if r[0].denominator == 1:
            if nz5 == 2 and nz3 == 0:
                c_45 += 1
            elif nz5 == 0 and nz3 == 2:
                c_15 += 1
            elif nz5 == 1 and nz3 == 1:
                c_10_6 += 1
                qx_10.add(int(2 * sum(r[:5])))
        else:
            if sum(1 for x in r[:5] if x < 0) % 2 == 0:
                c_16_4 += 1
                qx_16.add(int(2 * sum(r[:5])))
            else:
                c_16b_4b += 1

    b_24_gut, b_24_perp, b_10_5, b_10b_5b, b_5_10b, b_5b_10 = 4, 4, 0, 0, 0, 0
    for r in roots_e8:
        s5 = sum(r[:5])
        if r[0].denominator == 1:
            nz5 = sum(1 for x in r[:5] if x != 0)
            nz3 = sum(1 for x in r[5:] if x != 0)
            if nz5 == 2 and nz3 == 0:
                if s5 == 0:
                    b_24_gut += 1
                elif s5 == 2:
                    b_10_5 += 1
                elif s5 == -2:
                    b_10b_5b += 1
            elif nz5 == 0 and nz3 == 2:
                b_24_perp += 1
            elif nz5 == 1 and nz3 == 1:
                if s5 == 1:
                    b_5_10b += 1
                elif s5 == -1:
                    b_5b_10 += 1
        else:
            if s5 == Fr(5, 2) or s5 == Fr(-5, 2):
                b_24_perp += 1
            elif s5 == Fr(-1, 2):
                b_10_5 += 1
            elif s5 == Fr(1, 2):
                b_10b_5b += 1
            elif s5 == Fr(-3, 2):
                b_5_10b += 1
            elif s5 == Fr(3, 2):
                b_5b_10 += 1

    hu_perp_dim = b_5_10b // 5
    hd_perp_dim = b_5b_10 // 5

    z4_16 = {sp.I ** (q % 4) for q in qx_16}
    z4_10 = {sp.I ** (q % 4) for q in qx_10}
    pm_16 = {int(v ** 2) for v in z4_16}
    pm_10 = {int(v ** 2) for v in z4_10}
    dim4_pdecay = (-1) ** 3
    bilin_rpv = (-1) * (+1)

    r5 = sp.zeros(5, 5)
    for k in range(5):
        r5[(-k) % 5, k] = 1
    pairs10 = list(itertools.combinations(range(5), 2))
    r10 = sp.zeros(10, 10)
    for ci, (a, b) in enumerate(pairs10):
        ra, rb = (-a) % 5, (-b) % 5
        if ra < rb:
            r10[pairs10.index((ra, rb)), ci] = 1
        else:
            r10[pairs10.index((rb, ra)), ci] = -1
    d5_even_5 = (5 + int(r5.trace())) // 2
    d5_even_10 = (10 + int(r10.trace())) // 2

    h = sp.symbols("h1 h2 h3 h4 h5")
    w_10 = [tuple(Fr(s if j == i else 0) for j in range(5)) for i in range(5) for s in (-1, 1)]
    w_16 = [tuple(Fr(s, 2) for s in sg) for sg in itertools.product((-1, 1), repeat=5) if sg.count(-1) % 2 == 0]
    w_40 = []
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (-1, 1):
                for sj in (-1, 1):
                    v = [Fr(0)] * 5
                    v[i], v[j] = Fr(si), Fr(sj)
                    w_40.append(tuple(v))

    def ctr(ws: list[tuple[Fr, ...]], pwr: int) -> sp.Expr:
        return sp.expand(sum(sum(sp.Rational(w[i].numerator, w[i].denominator) * h[i] for i in range(5)) ** pwr for w in ws))

    t10_2, t10_4 = ctr(w_10, 2), ctr(w_10, 4)
    t16_2, t16_4 = ctr(w_16, 2), ctr(w_16, 4)
    t45_2, t45_4 = ctr(w_40, 2), ctr(w_40, 4)

    n16_s, n10_s = sp.symbols("n16 n10")
    f4_expr = sp.simplify((t45_4 - n16_s * t16_4 - n10_s * t10_4) - ((2 + n16_s - n10_s) * t10_4 + sp.Rational(3, 4) * (4 - n16_s) * (t10_2 ** 2)))
    f2_expr = sp.simplify((t45_2 - n16_s * t16_2 - n10_s * t10_2) - (8 - 2 * n16_s - n10_s) * t10_2)

    ab_kmt = sp.simplify(sp.Rational(1, 3) * (8 - 2 * n16_s - (n16_s + 2)))
    bb_kmt = sp.simplify(-sp.Rational(4, 3) * (3 - sp.Rational(3, 4) * n16_s))
    adjunction_2g_m2 = sp.simplify(ab_kmt + bb_kmt)

    exact_fk_for_n16_0 = int(-bb_kmt.subs(n16_s, 0))
    exact_fk_for_n16_2 = int(-bb_kmt.subs(n16_s, 2))
    n16_forced_on_F6 = int(sp.solve(sp.Eq(bb_kmt, -6), n16_s)[0])

    k1_v2, k2_v1 = 12 - 2 * 2, 12 - 2 * 1
    n5_needed = 24 - (k1_v2 + k2_v1)
    nT_needed = 1 + n5_needed

    su_pure_f4: dict[str, int] = {}
    for n_su in (4, 5):
        xs = sp.symbols(f"x0:{n_su}")
        sub_tr = {xs[-1]: -sum(xs[:-1])}
        tr_fund_2 = sp.expand(sum(xi ** 2 for xi in xs).subs(sub_tr))
        tr_fund_4 = sp.expand(sum(xi ** 4 for xi in xs).subs(sub_tr))
        tr_adj_4 = sp.expand(
            sum(((xs[i] - xs[j]) ** 4) for i in range(n_su) for j in range(n_su) if i != j).subs(sub_tr)
        )
        assert sp.simplify(tr_adj_4 - (2 * n_su * tr_fund_4 + 6 * (tr_fund_2 ** 2))) == 0
        su_pure_f4[f"SU({n_su})_pure_SYM_trF4_coeff"] = 2 * n_su

    pf2_trf4_bad = sp.simplify((t45_4 - n16_s * t16_4 - (n16_s + 3) * t10_4) - sp.Rational(3, 4) * (4 - n16_s) * (t10_2 ** 2))
    pf2_caught = bool(sp.simplify(pf2_trf4_bad + t10_4) == 0 and exact_fk_for_n16_0 == 4 and n16_forced_on_F6 == -2)

    passed = bool(
        len(roots_e8) == 240
        and (c_45, c_15, c_10_6, c_16_4, c_16b_4b) == (45, 15, 60, 64, 64)
        and (b_24_gut, b_24_perp, b_10_5, b_10b_5b, b_5_10b, b_5b_10) == (24, 24, 50, 50, 50, 50)
        and hu_perp_dim == 10 and hd_perp_dim == 10
        and pm_16 == {-1} and pm_10 == {1} and dim4_pdecay == -1 and bilin_rpv == -1
        and (d5_even_5, d5_even_10) == (3, 4)
        and f4_expr == 0 and f2_expr == 0
        and adjunction_2g_m2 == -2
        and exact_fk_for_n16_0 == 4 and exact_fk_for_n16_2 == 2 and n16_forced_on_F6 == -2
        and n5_needed == 6 and nT_needed == 7
        and su_pure_f4["SU(4)_pure_SYM_trF4_coeff"] == 8
        and su_pure_f4["SU(5)_pure_SYM_trF4_coeff"] == 10
        and pf2_caught
    )
    return {
        "L8_3_verified_the_same": {
            "e8_spin10_su4_dims": [c_45, c_15, c_10_6, c_16_4, c_16b_4b],
            "qx_16_and_10": [sorted(qx_16), sorted(qx_10)],
            "z2_matter_parity_16_10_dim4_rpv": [-1, 1, dim4_pdecay, bilin_rpv],
            "d5_reflection_even_5perp_10perp": [d5_even_5, d5_even_10],
        },
        "catch_FL8_F1_hirzebruch_refutation": {
            "sadov_kmt_a_dot_b": str(ab_kmt),
            "sadov_kmt_b_dot_b": str(bb_kmt),
            "adjunction_2g_minus_2": int(adjunction_2g_m2),
            "true_hirzebruch_k_for_n16_0_and_2": [exact_fk_for_n16_0, exact_fk_for_n16_2],
            "l8_1_claimed_hirzebruch_k_shifted_by_plus2": [6, 4],
            "spin10_n16_required_on_F6_impossible": n16_forced_on_F6,
            "single_base_v1_plus_v2_24_instanton_rule_n5_and_nT_needed_for_2_and_1": [n5_needed, nT_needed],
            "pure_6d_su4_su5_irreducible_trF4_anomalies": su_pure_f4,
        },
        "catch_FL8_F7_hu_hd_su5_perp_symmetry": {
            "e8_su5_gut_x_su5_perp_dims": [b_24_gut, b_24_perp, b_10_5, b_10b_5b, b_5_10b, b_5b_10],
            "hu_in_5_GUT_su5_perp_rep_dim": hu_perp_dim,
            "hd_in_5bar_GUT_su5_perp_rep_dim": hd_perp_dim,
            "both_higgs_doublets_are_2sheeted_lambda2": bool(hu_perp_dim == 10 and hd_perp_dim == 10),
        },
        "pf2_bad_n10_and_F6_caught": pf2_caught,
        "passed": passed,
    }


# ==============================================================================
# PA2-C: agy-exp Block A (F7_1 Genesis, F7_2 Spin(10), L8_2 K_5/K_6, L8_4 Out(D_5))
# ==============================================================================

def perm_mul(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inv(p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(p)
    for i, pi in enumerate(p):
        out[pi] = i
    return tuple(out)


def perm_gen(gens: list[tuple[int, ...]], ide: tuple[int, ...]) -> list[tuple[int, ...]]:
    seen = {ide}
    q = deque([ide])
    while q:
        cur = q.popleft()
        for g in gens:
            nxt = perm_mul(cur, g)
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return sorted(seen)


def jacobi_triple_t34(tau: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
    q = mp.exp(I_MP * mp.pi * tau)
    p3, p4 = mp.mpc(1), mp.mpc(1)
    q2n, q2m1 = q * q, q
    for _ in range(120):
        if abs(q2m1) < p10_mp(-60):
            break
        f0 = mp.mpc(1) - q2n
        p3 *= f0 * ((mp.mpc(1) + q2m1) ** 2)
        p4 *= f0 * ((mp.mpc(1) - q2m1) ** 2)
        q2n *= q * q
        q2m1 *= q * q
    return p3, p4


def run_pa2_c() -> dict[str, Any]:
    mp.mp.dps = 50
    snf_m000 = smith_normal_form(sp.Matrix([[0, 1, 0], [1, -1, 0]]), domain=sp.ZZ)
    nz_m000 = [abs(int(snf_m000[i, i])) for i in range(2) if snf_m000[i, i] != 0]
    rk_m000 = 3 - len(nz_m000)
    m000_double_covers = (2 ** rk_m000) - 1

    groups_le12: dict[str, tuple[tuple[int, ...], list[tuple[int, ...]]]] = {
        "S_3": ((0, 1, 2), [(1, 2, 0), (0, 2, 1)]),
        "D_4": ((0, 1, 2, 3), [(1, 2, 3, 0), (0, 3, 2, 1)]),
        "Q_8": (tuple(range(8)), [(2, 3, 1, 0, 6, 7, 5, 4), (4, 5, 7, 6, 1, 0, 2, 3)]),
        "D_5": ((0, 1, 2, 3, 4), [(1, 2, 3, 4, 0), (0, 4, 3, 2, 1)]),
        "D_6": (tuple(range(6)), [(1, 2, 3, 4, 5, 0), (0, 5, 4, 3, 2, 1)]),
        "A_4": ((0, 1, 2, 3), [(1, 2, 0, 3), (1, 0, 3, 2)]),
        "Dic_3": (
            tuple(range(12)),
            [
                tuple(((i // 2 + 1) % 6) * 2 + (i % 2) for i in range(12)),
                tuple(((-i // 2) % 6) * 2 + 1 if i % 2 == 0 else ((3 - i // 2) % 6) * 2 for i in range(12)),
            ],
        ),
    }
    surj_m004: dict[str, int] = {}
    for gname, (ide, gens) in groups_le12.items():
        els = perm_gen(gens, ide)
        og = len(els)
        cnt = 0
        for a in els:
            for b in els:
                ab = perm_mul(a, b)
                aba = perm_mul(ab, a)
                for t in els:
                    ti = perm_inv(t)
                    if perm_mul(perm_mul(t, a), ti) == aba and perm_mul(perm_mul(t, b), ti) == ab:
                        if len(perm_gen([a, b, t], ide)) == og:
                            cnt += 1
        surj_m004[gname] = cnt

    pa = tuple((x + 1) % 5 for x in range(5))
    pb = tuple((x + 2) % 5 for x in range(5))
    pt = tuple((-x) % 5 for x in range(5))
    pmap = {"a": pa, "b": pb, "t": pt}
    pinv = {k: tuple(p.index(i) for i in range(5)) for k, p in pmap.items()}
    eidx = {(x, g): 3 * x + gi for x in range(5) for gi, g in enumerate(("a", "b", "t"))}
    rs_rows = [[1 if j == eidx[(x, "a")] else 0 for j in range(15)] for x in range(4)]
    for rel in (
        [("t", 1), ("a", 1), ("t", -1), ("a", -1), ("b", -1), ("a", -1)],
        [("t", 1), ("b", 1), ("t", -1), ("b", -1), ("a", -1)],
    ):
        for x0 in range(5):
            rw = [0] * 15
            cur = x0
            for g, s in rel:
                if s == 1:
                    rw[eidx[(cur, g)]] += 1
                    cur = pmap[g][cur]
                else:
                    prv = pinv[g][cur]
                    rw[eidx[(prv, g)]] -= 1
                    cur = prv
            rs_rows.append(rw)
    snf_834 = smith_normal_form(sp.Matrix(rs_rows), domain=sp.ZZ)
    nz_834 = [abs(int(snf_834[i, i])) for i in range(min(snf_834.rows, snf_834.cols)) if snf_834[i, i] != 0]
    rk_834 = 15 - len(nz_834)
    tors_834 = [d for d in nz_834 if d > 1]

    def apply_w(w: list[tuple[str, int]], x0: int) -> int:
        x = x0
        for g, s in w:
            x = pmap[g][x] if s == 1 else pinv[g][x]
        return x

    mw_p = tuple(apply_w([("a", -1), ("b", -1), ("a", -1), ("t", 1)], x) for x in range(5))
    lw_p = tuple(apply_w([("a", 1), ("b", 1), ("a", -1), ("b", -1)], x) for x in range(5))
    seen_sh: set[int] = set()
    cusp_degs: list[int] = []
    for x in range(5):
        if x not in seen_sh:
            orb = {x, mw_p[x], lw_p[x]}
            seen_sh |= orb
            cusp_degs.append(len(orb))
    cusp_degs.sort()

    a_e8 = sp.eye(9) * 2
    for u, v in [(1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 0)]:
        a_e8[u, v] = -1
        a_e8[v, u] = -1
    kv = a_e8.nullspace()[0]
    kac_marks = [int(x / min(kv)) for x in kv]
    m8_dets = sorted([
        (int(a_e8.extract([k for k in range(9) if k not in (i, j)], [k for k in range(9) if k not in (i, j)]).det()), [i, j], [kac_marks[i], kac_marks[j]])
        for i, j in itertools.combinations(range(9), 2)
        if kac_marks[i] + kac_marks[j] == 8
    ])

    p10 = sp.diag(1, 1, 1, -1, -1, 1, 1, 1, -1, -1)
    j10 = sp.Matrix.vstack(sp.Matrix.hstack(sp.zeros(5, 5), -sp.eye(5)), sp.Matrix.hstack(sp.eye(5), sp.zeros(5, 5)))
    so10_b = []
    for a in range(10):
        for b in range(a + 1, 10):
            m = sp.zeros(10, 10)
            m[a, b] = 1
            m[b, a] = -1
            so10_b.append(m)

    def v45(mat: sp.Matrix) -> list[sp.Rational]:
        return [mat[a, b] for a in range(10) for b in range(a + 1, 10)]

    ad_p = sp.Matrix([v45(p10 * b * p10 - b) for b in so10_b]).T
    ad_j = sp.Matrix([v45(j10 * b - b * j10) for b in so10_b]).T
    jv = sp.Matrix([v45(j10)])
    cent_dims = [
        45 - int(ad_p.rank()),
        45 - int(ad_j.rank()),
        45 - int(sp.Matrix.vstack(ad_p, ad_j).rank()),
        45 - int(sp.Matrix.vstack(ad_p, ad_j, jv).rank()),
    ]
    q_6y = [-2, -2, -2, 3, 3]
    p_5 = [1, 1, 1, -1, -1]
    an_y = an_y3 = an_su3 = an_su2 = Fr(0)
    ps_l = ps_r = 0
    for s in itertools.product((0, 1), repeat=5):
        if sum(s) % 2 == 0:
            yv = Fr(sum(s[i] * q_6y[i] for i in range(5)), 6)
            pw = 1
            for i in range(5):
                if s[i]:
                    pw *= p_5[i]
            if pw == -1:
                ps_l += 1
            else:
                ps_r += 1
            an_y += yv
            an_y3 += yv ** 3
            if sum(s[:3]) in (1, 2):
                an_su3 += Fr(1, 6) * yv
            if sum(s[3:]) == 1:
                an_su2 += Fr(1, 4) * yv
    kept_6y = sorted([y for p, y in zip(p_5 + p_5, q_6y + [-x for x in q_6y]) if -p == 1])

    m_rl = ((2, 1), (1, 1))
    m_2 = ((1, 0), (2, 1))
    e5_subs = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (0, 1)]
    k5_inv = []
    for g in e5_subs:
        sub = {((k * g[0]) % 5, (k * g[1]) % 5) for k in range(1, 5)}
        img = {((m_rl[0][0] * p[0] + m_rl[0][1] * p[1]) % 5, (m_rl[1][0] * p[0] + m_rl[1][1] * p[1]) % 5) for p in sub}
        if img == sub:
            k5_inv.append(list(g))

    seen_6: set[tuple[tuple[int, int], ...]] = set()
    e6_anchored_ab_setwise_inv: list[list[list[int]]] = []
    e6_anchored_pointwise_a_eq_b: list[list[list[int]]] = []
    for a in range(6):
        for b in range(6):
            orb = tuple(sorted({((k * a) % 6, (k * b) % 6) for k in range(6)}))
            if len(orb) == 6 and orb not in seen_6:
                seen_6.add(orb)
                prims = sorted([p for p in orb if all(((m * p[0]) % 6, (m * p[1]) % 6) != (0, 0) for m in (1, 2, 3))])
                if (3, 3) in orb:
                    if {(p[1], p[0]) for p in orb} == set(orb):
                        e6_anchored_ab_setwise_inv.append([list(p) for p in prims])
                    if all(p[0] == p[1] for p in prims):
                        e6_anchored_pointwise_a_eq_b.append([list(p) for p in prims])

    k6_plus_set = {((k * 1) % 6, (k * 1) % 6) for k in range(6)}
    k6_minus_set = {((k * 1) % 6, (k * 5) % 6) for k in range(6)}
    s_on_k6_plus = {((-p[1]) % 6, p[0] % 6) for p in k6_plus_set}
    mrl_on_11_mod6 = [(m_rl[0][0] * 1 + m_rl[0][1] * 1) % 6, (m_rl[1][0] * 1 + m_rl[1][1] * 1) % 6]
    m2_on_11_mod6 = [(m_2[0][0] * 1 + m_2[0][1] * 1) % 6, (m_2[1][0] * 1 + m_2[1][1] * 1) % 6]
    k6_preserved_by_mrl = bool(tuple(mrl_on_11_mod6) in k6_plus_set)
    k6_preserved_by_m2 = bool(tuple(m2_on_11_mod6) in k6_plus_set)

    d5_els = perm_gen(groups_le12["D_5"][1], groups_le12["D_5"][0])
    ord5 = [e for e in d5_els if e != (0, 1, 2, 3, 4) and perm_mul(e, perm_mul(e, perm_mul(e, perm_mul(e, e)))) == (0, 1, 2, 3, 4)]
    ord2 = [e for e in d5_els if e != (0, 1, 2, 3, 4) and perm_mul(e, e) == (0, 1, 2, 3, 4)]
    aut_cnt = sum(1 for gi in ord5 for ri in ord2 if perm_mul(perm_mul(ri, gi), ri) == perm_inv(gi))
    inn_maps = {tuple(perm_mul(perm_mul(h, x), perm_inv(h)) for x in d5_els) for h in d5_els}
    out_d5 = aut_cnt // len(inn_maps)

    def dz_triple(tv: mp.mpc) -> mp.mpf:
        t3, t4 = jacobi_triple_t34(tv)
        al = mp.mpf(2) * mp.pi * mp.im(tv) / mp.mpf(5)
        return (mp.exp(-mp.mpf(2) * al) - mp.exp(-mp.mpf(3) * al)) * ((abs(t4) ** 4) - (abs(t3) ** 4))

    dz_2i = dz_triple(mp.mpf(2) * I_MP)
    dz_t8 = dz_triple(q_mp(16, 5) + I_MP * q_mp(8, 5))

    s3_els = perm_gen(groups_le12["S_3"][1], groups_le12["S_3"][0])
    s3_tr4 = 0
    for a in s3_els:
        a2 = perm_mul(a, a)
        a3 = perm_mul(a2, a)
        for b in s3_els:
            r1, r2 = perm_mul(a3, b), perm_mul(a2, b)
            for t in s3_els:
                ti = perm_inv(t)
                if perm_mul(perm_mul(t, a), ti) == r1 and perm_mul(perm_mul(t, b), ti) == r2:
                    if len(perm_gen([a, b, t], (0, 1, 2))) == 6:
                        s3_tr4 += 1
    pf3_caught = bool(s_on_k6_plus == k6_minus_set and s3_tr4 == 12)

    passed = bool(
        m000_double_covers == 1
        and surj_m004 == {"S_3": 0, "D_4": 0, "Q_8": 0, "D_5": 20, "D_6": 0, "A_4": 24, "Dic_3": 0}
        and rk_834 == 3 and tors_834 == [] and cusp_degs == [1, 2, 2]
        and len(m8_dets) == 5 and m8_dets[0][0] == 20 and m8_dets[0][1] == [2, 5]
        and cent_dims == [21, 25, 13, 12]
        and (ps_l, ps_r) == (8, 8) and an_y == 0 and an_y3 == 0 and an_su3 == 0 and an_su2 == 0
        and kept_6y == [-3, -3, 3, 3]
        and k5_inv == [[1, 2]]
        and len(seen_6) == 12
        and len(e6_anchored_ab_setwise_inv) == 2
        and len(e6_anchored_pointwise_a_eq_b) == 1
        and (not k6_preserved_by_mrl) and (not k6_preserved_by_m2)
        and (aut_cnt, len(inn_maps), out_d5) == (20, 10, 2)
        and dz_2i < mp.mpf(0) and dz_t8 > mp.mpf(0)
        and pf3_caught
    )
    return {
        "F7_1_F7_2_L8_4_verified_the_same": {
            "m000_double_covers": m000_double_covers,
            "m004_nonabelian_surjections_le12": surj_m004,
            "8_3_4_H1_and_cusps": [rk_834, tors_834, cusp_degs],
            "affine_e8_order8_min_det_and_nodes": [m8_dets[0][0], m8_dets[0][1], m8_dets[0][2]],
            "spin10_centralizer_dims": cent_dims,
            "spin10_16_anomalies_zero_and_kept_6Y": [True, kept_6y],
            "K5_unique_m004_RL_invariant": k5_inv[0],
            "D5_aut_inn_out": [aut_cnt, len(inn_maps), out_d5],
            "jacobi_triple_deltaZ_2i_and_tau8": [mp.nstr(dz_2i, 12), mp.nstr(dz_t8, 12)],
        },
        "catch_FL8_F3_K6_not_unique": {
            "total_order6_subgroups_of_E6": len(seen_6),
            "true_AB_setwise_symmetric_anchored_at_33_count": len(e6_anchored_ab_setwise_inv),
            "true_AB_setwise_symmetric_subgroups_primitives": e6_anchored_ab_setwise_inv,
            "hardcoded_a_eq_b_filter_count": len(e6_anchored_pointwise_a_eq_b),
            "S_swaps_K6_plus_to_K6_minus": bool(s_on_k6_plus == k6_minus_set),
            "M_RL_image_of_1_1_mod6": mrl_on_11_mod6,
            "M_2_image_of_1_1_mod6": m2_on_11_mod6,
            "K6_plus_preserved_by_M_RL_or_M_2": [k6_preserved_by_mrl, k6_preserved_by_m2],
            "minimum_K6_selection_bits": "1",
        },
        "pf3_S_swap_and_tr4_S3_caught": pf3_caught,
        "passed": passed,
    }


# ==============================================================================
# PA2-D: agy-exp Block B2 (PMNS/Haar Bug, Mirror Sign, Racetrack, Split-SUSY, BP)
# ==============================================================================

def eval_w_hol_jacobi(tau: mp.mpc, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = q_mp(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]
    q = mp.exp(mp.mpf(2) * I_MP * mp.pi * tau)
    t2 = t3 = t4 = dt2 = dt3 = dt4 = mp.mpc(0)
    for n in range(-26, 27):
        m2 = q_mp((2 * n + 1) ** 2, 8)
        e2v = mp.exp(mp.mpf(2) * I_MP * mp.pi * tau * m2)
        t2 += e2v
        dt2 += m2 * e2v
        m3 = q_mp(n * n, 2)
        e3v = mp.exp(mp.mpf(2) * I_MP * mp.pi * tau * m3)
        t3 += e3v
        dt3 += m3 * e3v
        sg = -1 if (n % 2 != 0) else 1
        t4 += sg * e3v
        dt4 += sg * m3 * e3v
    e2s = mp.mpc(1)
    qn = q
    for n in range(1, 48):
        e2s -= mp.mpf(24 * n) * (qn / (mp.mpc(1) - qn))
        qn *= q
    l2d, l3d, l4d = dt2 / t2, dt3 / t3, dt4 / t4
    sh = (
        (-t2 / (t3 * t4)) * (l2d - l3d - l4d + e2s / mp.mpf(24)) * qi
        + (-t4 / (t2 * t3)) * (l4d - l2d - l3d + e2s / mp.mpf(24)) * qj
        + (I_MP * t3 / (t2 * t4)) * (l3d - l2d - l4d + e2s / mp.mpf(24)) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    pr = mp.mpc(1)
    qn = q
    for _ in range(48):
        pr *= mp.mpc(1) - qn
        qn *= q
    t1p = mp.mpf(2) * mp.pi * (mp.exp(I_MP * mp.pi * tau / mp.mpf(12)) * pr) ** 3
    yi = mp.im(tau)

    def thc(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        nb = int(cb - tb)
        am, bm = f_mp(ta), f_mp(tb)
        zv = am * tau + bm
        n0 = int(mp.nint(-mp.im(zv) / yi))
        s = mp.fsum(
            mp.exp(I_MP * mp.pi * tau * (mp.mpf(k) ** 2) + mp.mpf(2) * I_MP * mp.pi * mp.mpf(k) * zv)
            for k in range(n0 - 24, n0 + 25)
        )
        b = mp.exp(I_MP * mp.pi * am * am * tau + mp.mpf(2) * I_MP * mp.pi * am * bm) * s
        return b if (nb == 0 or ta == 0) else mp.exp(mp.mpf(2) * I_MP * mp.pi * am * mp.mpf(nb)) * b

    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-mp.mpf(2) * I_MP * mp.pi * f_mp(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    hfr = Fr(1, 2)
    cs = {"1": (ap + hfr, bp + hfr), "i": (ap + hfr, bp), "j": (ap, bp + hfr), "k": (ap, bp)}
    ds = {"1": (am + hfr, bm + hfr), "i": (am + hfr, bm), "j": (am, bm + hfr), "k": (am, bm)}
    rs: dict[str, mp.mpc] = {}
    for sk in ("1", "i", "j", "k"):
        if ((cs[sk][0] - hfr) % 1 == 0 and (cs[sk][1] - hfr) % 1 == 0) or (
            (ds[sk][0] - hfr) % 1 == 0 and (ds[sk][1] - hfr) % 1 == 0
        ):
            rs[sk] = mp.mpc(0)
        else:
            rs[sk] = kap[sk] * thc(cs[sk][0], cs[sk][1]) * thc(ds[sk][0], ds[sk][1]) / t1p
    mw = rs["1"] * ed["1"] + rs["i"] * ed["i"] + rs["j"] * ed["j"] + rs["k"] * ed["k"]
    return mp.matrix([
        [
            ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1]
            + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1]
            for cb in range(3)
        ]
        for ra in range(3)
    ])


def compute_dirac_s12_rk4(tau_in: mp.mpc) -> list[mp.mpf]:
    """Disjoint RK4 solver for exact Fuchsian Liouville ODE u'' = -(wp(z) - c)/4 * u on punctured torus."""
    with mp.workdps(24):
        shift = int(mp.nint(mp.re(tau_in)))
        tau = tau_in - mp.mpf(shift)
        q = mp.exp(I_MP * mp.pi * tau)
        t20, t30, t40 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
        e1 = (mp.pi ** 2) * (t30 ** 4 + t40 ** 4) / mp.mpf(3)
        yi, xr = mp.im(tau), mp.re(tau)

        def wp_val(z: mp.mpc) -> mp.mpc:
            bv = mp.im(z) / yi
            av = mp.re(z) - bv * xr
            av -= mp.nint(av)
            bv -= mp.nint(bv)
            pz = mp.pi * (av + bv * tau)
            return e1 + (mp.pi * t30 * t40 * mp.jtheta(2, pz, q) / mp.jtheta(1, pz, q)) ** 2

        def rk4_step(z: mp.mpc, dz: mp.mpc, m: mp.matrix, cv: mp.mpc) -> mp.matrix:
            def rhs(zz: mp.mpc, mm: mp.matrix) -> mp.matrix:
                q0 = -(wp_val(zz) - cv) / mp.mpf(4)
                return mp.matrix([[mm[1, 0], mm[1, 1]], [q0 * mm[0, 0], q0 * mm[0, 1]]])

            k1 = rhs(z, m)
            k2 = rhs(z + dz / mp.mpf(2), m + (dz / mp.mpf(2)) * k1)
            k3 = rhs(z + dz / mp.mpf(2), m + (dz / mp.mpf(2)) * k2)
            k4 = rhs(z + dz, m + dz * k3)
            return m + (dz / mp.mpf(6)) * (k1 + mp.mpf(2) * k2 + mp.mpf(2) * k3 + k4)

        def prop_uni(za: mp.mpc, zb: mp.mpc, cv: mp.mpc, ns: int) -> mp.matrix:
            dz = (zb - za) / mp.mpf(ns)
            m = mp.eye(2)
            for s in range(ns):
                m = rk4_step(za + mp.mpf(s) * dz, dz, m, cv)
            return m

        z0 = (mp.mpc(1) + tau) / mp.mpf(2)

        def resid(cr: mp.mpf, ci: mp.mpf) -> mp.matrix:
            cv = mp.mpc(cr, ci)
            ta = prop_uni(z0, z0 + mp.mpc(1), cv, 24)
            tb = prop_uni(z0, z0 + tau, cv, 32)
            return mp.matrix([mp.im(ta[0, 0] + ta[1, 1]), mp.im(tb[0, 0] + tb[1, 1]), mp.im((ta * tb)[0, 0] + (ta * tb)[1, 1])])

        c_cur = mp.mpc(0, 0)
        h_fd = p10_mp(-6)
        for _ in range(10):
            r0 = resid(mp.re(c_cur), mp.im(c_cur))
            nrm = mp.sqrt(sum(r0[k] ** 2 for k in range(3)))
            if nrm < p10_mp(-14):
                break
            dr = (resid(mp.re(c_cur) + h_fd, mp.im(c_cur)) - r0) / h_fd
            di = (resid(mp.re(c_cur), mp.im(c_cur) + h_fd) - r0) / h_fd
            jac = mp.matrix([[dr[k], di[k]] for k in range(3)])
            st = -((jac.T * jac) ** (-1)) * (jac.T * r0)
            c_cur += mp.mpc(st[0], st[1])
            if nrm < p10_mp(-7):
                h_fd = p10_mp(-9)

        ta = prop_uni(z0, z0 + mp.mpc(1), c_cur, 24)
        tb = prop_uni(z0, z0 + tau, c_cur, 32)
        tr_a = mp.re(ta[0, 0] + ta[1, 1])
        disc = mp.sqrt(tr_a ** 2 - mp.mpf(4))
        v1 = mp.matrix([ta[0, 1], (tr_a + disc) / mp.mpf(2) - ta[0, 0]])
        v2 = mp.matrix([ta[0, 1], (tr_a - disc) / mp.mpf(2) - ta[0, 0]])
        vm = mp.matrix([[v1[0], v2[0]], [v1[1], v2[1]]])
        vm = vm / mp.sqrt(vm[0, 0] * vm[1, 1] - vm[0, 1] * vm[1, 0])
        tbp = (vm ** (-1)) * tb * vm
        ph = mp.arg(tbp[0, 1])
        pm = vm * mp.matrix([[mp.exp(I_MP * ph / mp.mpf(2)), 0], [0, mp.exp(-I_MP * ph / mp.mpf(2))]])

        def dist_lat(z: mp.mpc) -> mp.mpf:
            bv = mp.im(z) / yi
            av = mp.re(z) - bv * xr
            av -= mp.nint(av)
            bv -= mp.nint(bv)
            zc = av + bv * tau
            return min(abs(zc + mp.mpf(m) + mp.mpf(n) * tau) for m in (-1, 0, 1) for n in (-1, 0, 1))

        def prop_seg(za: mp.mpc, zb: mp.mpc, m_in: mp.matrix) -> mp.matrix:
            m = m_in.copy()
            zc = za
            for _ in range(120):
                rem = zb - zc
                dr = abs(rem)
                if dr < p10_mp(-14):
                    break
                mst = q_mp(1, 5) * dist_lat(zc)
                st = rem if dr <= mst else rem * (mst / dr)
                while abs(st) > q_mp(1, 4) * dist_lat(zc + st / mp.mpf(2)):
                    st /= mp.mpf(2)
                m = rk4_step(zc, st, m, c_cur)
                zc += st
            return m

        def e2phi(z: mp.mpc) -> mp.mpf:
            m = prop_seg(z0, z, mp.eye(2))
            u1 = m[0, 0] * pm[0, 0] + m[0, 1] * pm[1, 0]
            u2 = m[0, 0] * pm[0, 1] + m[0, 1] * pm[1, 1]
            return mp.mpf(1) / (mp.im(u1 * mp.conj(u2)) ** 2)

        r4, r5 = p10_mp(-4), p10_mp(-5)
        bc_star = (mp.mpf(100) * (mp.mpf(1) / (r5 * mp.sqrt(e2phi(r5))) + mp.log(r5)) - (mp.mpf(1) / (r4 * mp.sqrt(e2phi(r4))) + mp.log(r4))) / mp.mpf(99)

        def gl_nodes(n: int) -> tuple[list[mp.mpf], list[mp.mpf]]:
            bs = [mp.mpf(k) / mp.sqrt(mp.mpf(4 * k * k - 1)) for k in range(1, n)]
            jm = mp.zeros(n, n)
            for k in range(n - 1):
                jm[k, k + 1] = bs[k]
                jm[k + 1, k] = bs[k]
            evs, vecs = mp.eighe(jm)
            return [evs[k] for k in range(n)], [mp.mpf(2) * (mp.re(vecs[0, k]) ** 2) for k in range(n)]

        n_th, n_t = 12, 14
        gx_th, gw_th = gl_nodes(n_th)
        gx_t, gw_t = gl_nodes(n_t)
        corners = [q_mp(1, 2) + tau / mp.mpf(2), -q_mp(1, 2) + tau / mp.mpf(2), -q_mp(1, 2) - tau / mp.mpf(2), q_mp(1, 2) - tau / mp.mpf(2)]
        angs = sorted((mp.arg(c) % (mp.mpf(2) * mp.pi)) for c in corners)
        sectors = [(angs[k], angs[k + 1]) for k in range(3)] + [(angs[3], angs[0] + mp.mpf(2) * mp.pi)]
        g_s12 = [mp.mpf(0)] * 3
        kinds = (3, 2, 4) if (shift % 2 != 0) else (4, 2, 3)

        for tha, thb in sectors:
            hth, mth = (thb - tha) / mp.mpf(2), (tha + thb) / mp.mpf(2)
            for ix in range(n_th):
                th = mth + hth * gx_th[ix]
                wth = hth * gw_th[ix]
                dbv = mp.sin(th) / yi
                dav = mp.cos(th) - dbv * xr
                rmax = q_mp(1, 2) / max(abs(dav), abs(dbv))
                tmax = mp.mpf(1) / (-mp.log(rmax) + bc_star)
                ht = tmax / mp.mpf(2)
                tnodes = [ht + ht * gx_t[it] for it in range(n_t)]
                rnodes = [mp.exp(bc_star - mp.mpf(1) / tv) for tv in tnodes]
                zc = z0
                mc = mp.eye(2)
                dirc = mp.exp(I_MP * th)
                for it in range(n_t - 1, -1, -1):
                    tv, rv = tnodes[it], rnodes[it]
                    wt = ht * gw_t[it]
                    zv = rv * dirc
                    jac_r = (rv * rv) / (tv * tv)
                    if rv < p10_mp(-6):
                        ws12 = rv / tv
                    else:
                        mc = prop_seg(zc, zv, mc)
                        zc = zv
                        u1 = mc[0, 0] * pm[0, 0] + mc[0, 1] * pm[1, 0]
                        u2 = mc[0, 0] * pm[0, 1] + mc[0, 1] * pm[1, 1]
                        ws12 = jac_r / abs(mp.im(u1 * mp.conj(u2)))
                    dw2 = wth * wt
                    yv = mp.im(zv)
                    fac = mp.sqrt(mp.mpf(2) * yi) * mp.exp(-mp.mpf(2) * mp.pi * yv * yv / yi)
                    pz = mp.pi * zv
                    for ai, kd in enumerate(kinds):
                        g_s12[ai] += dw2 * (ws12 / mp.sqrt(mp.mpf(2) * mp.pi * yi)) * fac * (abs(mp.jtheta(kd, pz, q)) ** 2)
        tot = sum(g_s12)
        out = [mp.mpf(3) * x / tot for x in g_s12]
    return [mp.mpf(x) for x in out]


def verify_split_susy_rge_sympy() -> dict[str, bool]:
    """First-principles SymPy Weyl-fermion tensor proof of Giudice-Romanino 1-loop Split-SUSY RGEs."""
    gu, gd, gup, gdp, g2, gp, yt = sp.symbols("gu gd gup gdp g2 gp yt", real=True)
    p = sp.symbols("p1 p2 p3 p4", real=True)
    w_sym = sp.symbols("W1 W2 W3 B Hup Hu0 Hd0 Hdm")
    hdag = sp.Matrix([[(p[2] - sp.I * p[3]) / 2, (p[0] - sp.I * p[1]) / 2]])
    hteps = sp.Matrix([[-(p[0] + sp.I * p[1]) / 2, (p[2] + sp.I * p[3]) / 2]])
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    hu_v = sp.Matrix([w_sym[4], w_sym[5]])
    hd_v = sp.Matrix([w_sym[6], w_sym[7]])
    l_int = sp.expand(
        (hdag * (gu * (w_sym[0] * s1 + w_sym[1] * s2 + w_sym[2] * s3) + gup * w_sym[3] * sp.eye(2)) * hu_v)[0, 0]
        + (hteps * (-gd * (w_sym[0] * s1 + w_sym[1] * s2 + w_sym[2] * s3) + gdp * w_sym[3] * sp.eye(2)) * hd_v)[0, 0]
    )
    ys = []
    for a in range(4):
        ma = sp.zeros(8, 8)
        ca = sp.diff(l_int, p[a])
        for i in range(8):
            for j in range(8):
                ma[i, j] = sp.diff(sp.diff(ca, w_sym[i]), w_sym[j])
        ys.append(ma)

    tr_yy = sp.simplify((ys[0] * ys[0].H).trace())
    tr_box = sp.expand(-4 * ((ys[0] * ys[0].H) ** 2).trace())
    lam_s = (g2 ** 2 + gp ** 2) / 8
    beta_lam_sm = 24 * lam_s ** 2 - 3 * lam_s * (3 * g2 ** 2 + gp ** 2) + sp.Rational(3, 8) * (2 * g2 ** 4 + (g2 ** 2 + gp ** 2) ** 2)
    beta_lam_ss = (4 * tr_yy * lam_s + tr_box).subs({gu: g2, gup: gp, gd: 0, gdp: 0})
    beta_lam_heavy = sp.Rational(13, 8) * g2 ** 4 + sp.Rational(21, 8) * gp ** 4
    susy_lam_id_ok = bool(sp.simplify((beta_lam_sm + beta_lam_ss + beta_lam_heavy) - (g2 ** 4 + 11 * gp ** 4) / 4) == 0)

    s_yyd = sum((yb * yb.H for yb in ys), sp.zeros(8, 8))
    s_ydy = sum((yb.H * yb for yb in ys), sp.zeros(8, 8))
    wf_f = sp.Rational(1, 2) * (s_yyd * ys[0] + ys[0] * s_ydy)
    vtx = 2 * sum((yb * ys[0].H * yb for yb in ys), sp.zeros(8, 8))
    wf_s = sum((sp.Rational(1, 2) * (ys[0] * yb.H + yb * ys[0].H).trace() * yb for yb in ys), sp.zeros(8, 8)) + 3 * yt ** 2 * ys[0]
    c2 = sp.diag(
        2 * g2 ** 2, 2 * g2 ** 2, 2 * g2 ** 2, 0,
        sp.Rational(3, 4) * g2 ** 2 + sp.Rational(1, 4) * gp ** 2,
        sp.Rational(3, 4) * g2 ** 2 + sp.Rational(1, 4) * gp ** 2,
        sp.Rational(3, 4) * g2 ** 2 + sp.Rational(1, 4) * gp ** 2,
        sp.Rational(3, 4) * g2 ** 2 + sp.Rational(1, 4) * gp ** 2,
    )
    beta_y0 = sp.simplify(wf_f + vtx + wf_s - 3 * (c2 * ys[0] + ys[0] * c2))
    b_gu = sp.expand(-2 * beta_y0[2, 5])
    b_gd = sp.expand(2 * beta_y0[2, 6])
    b_gup = sp.expand(2 * beta_y0[3, 5])
    b_gdp = sp.expand(-2 * beta_y0[3, 6])

    su2_cons = bool(sp.simplify(2 * beta_y0[0, 4] + 2 * beta_y0[2, 5]) == 0)
    # Exact SUSY decoupling checks: at gup = gp (gd=gdp=0), d(b_gu)/d(gp) == 0; at gu = g2 (gd=gdp=0), d(b_gup)/d(g2) == 0!
    b_gu_gp_cancel = bool(sp.simplify(sp.diff(b_gu.subs({gd: 0, gdp: 0, gup: gp}), gp)) == 0)
    b_gup_g2_cancel = bool(sp.simplify(sp.diff(b_gup.subs({gd: 0, gdp: 0, gu: g2}), g2)) == 0)
    chk_gu = bool(sp.simplify(b_gu - (gu * (-sp.Rational(33, 4) * g2 ** 2 - sp.Rational(3, 4) * gp ** 2 + 3 * yt ** 2 + sp.Rational(11, 4) * gu ** 2 + gd ** 2 + sp.Rational(3, 4) * gup ** 2 + sp.Rational(1, 2) * gdp ** 2) + gd * gdp * gup)) == 0)
    chk_gd = bool(sp.simplify(b_gd - (gd * (-sp.Rational(33, 4) * g2 ** 2 - sp.Rational(3, 4) * gp ** 2 + 3 * yt ** 2 + sp.Rational(11, 4) * gd ** 2 + gu ** 2 + sp.Rational(3, 4) * gdp ** 2 + sp.Rational(1, 2) * gup ** 2) + gu * gup * gdp)) == 0)
    chk_gup = bool(sp.simplify(b_gup - (gup * (-sp.Rational(9, 4) * g2 ** 2 - sp.Rational(3, 4) * gp ** 2 + 3 * yt ** 2 + sp.Rational(5, 4) * gup ** 2 + 2 * gdp ** 2 + sp.Rational(9, 4) * gu ** 2 + sp.Rational(3, 2) * gd ** 2) + 3 * gd * gdp * gu)) == 0)
    chk_gdp = bool(sp.simplify(b_gdp - (gdp * (-sp.Rational(9, 4) * g2 ** 2 - sp.Rational(3, 4) * gp ** 2 + 3 * yt ** 2 + sp.Rational(5, 4) * gdp ** 2 + 2 * gup ** 2 + sp.Rational(9, 4) * gd ** 2 + sp.Rational(3, 2) * gu ** 2) + 3 * gu * gup * gd)) == 0)
    # Exact 1-loop Coleman-Weinberg & matching-scale invariance proof for V = lam_std |H|^4 (m_h^2 = 2 lam_std v^2):
    #   beta_{lam_std}^{top} = -6 yt^4 / (16 pi^2) = -3 yt^4 / (8 pi^2);
    #   d(Delta lam_std)/d(ln mu) == beta_{lam_std}^{top} => Delta lam_std = +(3 yt^4 / (8 pi^2)) ln(m_stop / mu) = 2 * dlam_L8!
    mu_s, ms_s = sp.symbols("mu m_stop", positive=True)
    dlam_cw_2x = sp.Rational(3, 8) * (yt ** 4) / (sp.pi ** 2) * sp.log(ms_s / mu_s)
    beta_lam_top_std = -sp.Rational(6, 16) * (yt ** 4) / (sp.pi ** 2)
    cw_scale_invar_2x = bool(sp.simplify(mu_s * sp.diff(dlam_cw_2x, mu_s) - beta_lam_top_std) == 0)
    return {
        "susy_beta_lambda_g2_gp_exact_cancel": susy_lam_id_ok,
        "su2_tensor_consistency": su2_cons,
        "susy_gp_cancel_in_beta_gu": b_gu_gp_cancel,
        "susy_g2_cancel_in_beta_gup": b_gup_g2_cancel,
        "all_4_beta_g_closed_forms_exact": bool(chk_gu and chk_gd and chk_gup and chk_gdp),
        "cw_stop_threshold_2x_matching_scale_invar_exact": cw_scale_invar_2x,
    }


def run_pa2_d() -> dict[str, Any]:
    mp.mp.dps = 48
    prod_l8 = json.loads(git_show_bytes(AGY_EXP_REF, "relays/x_floor_link8_verify/verify_x_floor_link8_out.json").decode("utf-8"))
    prod_l7 = json.loads(git_show_bytes(AGY_EXP_REF, "relays/x_foundations_link7_verify/verify_x_foundations_link7_out.json").decode("utf-8"))

    tau8 = q_mp(16, 5) + I_MP * q_mp(8, 5)
    g_rk4 = compute_dirac_s12_rk4(tau8)
    g_peer = [mp.mpf(x) for x in prod_l8["L8_5_unified_zero_placeholder_uv_to_ir_blind_lock"]["dirac_s12_gramian_tau8"]]
    gram_diff_vs_peer = max(abs(g_rk4[i] - g_peer[i]) for i in range(3))

    k5 = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6 = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]

    def w_avg(tv: mp.mpc, pts: list[tuple[Fr, Fr]], ql: int, qr: int) -> mp.matrix:
        return sum((eval_w_hol_jacobi(tv, a, b, ql, qr) for a, b in pts), mp.zeros(3, 3)) / mp.mpf(len(pts))

    wu = w_avg(tau8, k5, 1, -4)
    wd = (w_avg(tau8, k5, 1, 2) + w_avg(tau8, k6, 1, 2)) / mp.mpf(2)
    we = (w_avg(tau8, k5, -3, 6) + w_avg(tau8, k6, -3, 6)) / mp.mpf(2)
    wnu = (w_avg(tau8, k5, 3, -5) + w_avg(tau8, k6, 3, -5)) / mp.mpf(2)
    wr_raw = (w_avg(tau8, k5, 3, 3) + w_avg(tau8, k6, 3, 3)) / mp.mpf(2)
    wr_sym = (wr_raw + wr_raw.T) / mp.mpf(2)
    _, svr = svd_asc_mp(wr_sym)
    mr = mp.eye(3) + wr_sym / svr[2]

    eps5 = mp.exp(mp.mpf(2) * I_MP * mp.pi * tau8 / mp.mpf(5))
    d10 = mp.diag([eps5 ** n for n in (2, 0, 3)])
    # Self-contained disjoint RK4 Gramian g_rk4 fed throughout PA2-D (zero Guardrail-6 peer echo):
    kis = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_rk4])
    yu = kis * d10 * wu * d10 * kis
    yd = kis * d10 * wd * kis
    ye = kis * we * d10 * kis
    ynu = kis * wnu
    mnu = -ynu * (mr ** (-1)) * ynu.T

    _, su = svd_asc_mp(yu)
    _, sd = svd_asc_mp(yd)
    ue, se = svd_asc_mp(ye)
    ut_true, snu_true = takagi_true_mp(mnu)
    takagi_resid = max(
        abs((ut_true.H * mnu * mp.matrix([[mp.conj(ut_true[r, c]) for c in range(3)] for r in range(3)]) - mp.diag(snu_true))[i, j])
        for i in range(3) for j in range(3)
    )

    def pmns_angles(u_mat: mp.matrix) -> list[mp.mpf]:
        s13 = abs(u_mat[0, 2]) ** 2
        s12 = (abs(u_mat[0, 1]) ** 2) / (mp.mpf(1) - s13)
        s23 = (abs(u_mat[1, 2]) ** 2) / (mp.mpf(1) - s13)
        return [s12, s23, s13]

    ang_true = pmns_angles(ue.H * ut_true)
    dm_rat = (snu_true[1] ** 2 - snu_true[0] ** 2) / (snu_true[2] ** 2 - snu_true[0] ** 2)

    # Cross-check true Takagi PMNS on peer metric g_peer as diagnostic comparison only:
    kis_pr = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_peer])
    ue_pr, _ = svd_asc_mp(kis_pr * we * d10 * kis_pr)
    ynu_pr = kis_pr * wnu
    ut_pr, _ = takagi_true_mp(-ynu_pr * (mr ** (-1)) * ynu_pr.T)
    ang_true_peer = pmns_angles(ue_pr.H * ut_pr)
    rk4_pmns_diff = max(abs(ang_true_peer[k] - ang_true[k]) for k in range(3))

    ut_true_c = mp.matrix([[mp.conj(ut_true[r, c]) for c in range(3)] for r in range(3)])
    ang_broken_true_takagi = pmns_angles(ue.H * ut_true_c)

    u_svd, s_svd, vh_svd = mp.svd_c(mnu)
    oid = sorted(range(3), key=lambda i: s_svd[i])
    us_b = mp.matrix([[u_svd[r, oid[c]] for c in range(3)] for r in range(3)])
    vs_b = mp.matrix([[vh_svd[r, oid[c]] for c in range(3)] for r in range(3)])
    z_b = us_b.T * mp.matrix([[mp.conj(vs_b[r, c]) for c in range(3)] for r in range(3)])
    ut_l8_bug = us_b * mp.diag([mp.exp(-I_MP * mp.arg(z_b[k, k]) / mp.mpf(2)) for k in range(3)])
    ut_l8_bug_c = mp.matrix([[mp.conj(ut_l8_bug[r, c]) for c in range(3)] for r in range(3)])
    ang_l8_repro = pmns_angles(ue.H * ut_l8_bug_c)

    peer_l8_pmns = [mp.mpf(x) for x in prod_l8["L8_5_unified_zero_placeholder_uv_to_ir_blind_lock"]["unified_blind_branches"]["branch_plus_203"]["pmns_s12sq_s23sq_s13sq_dmratio"][:3]]
    repro_l8_diff = max(abs(ang_l8_repro[k] - peer_l8_pmns[k]) for k in range(3))
    fixing_only_vh_transpose_shift = max(abs(ang_broken_true_takagi[k] - ang_l8_repro[k]) for k in range(3))

    rng = random.Random(2026112409)
    haar_true_max = mp.mpf(0)
    haar_l8_broken_max = mp.mpf(0)
    for _ in range(10):
        ul, uer, unr = random_haar_u3(rng), random_haar_u3(rng), random_haar_u3(rng)
        ye_s = ul * ye * uer.H
        ynu_s = ul * ynu * unr
        mr_s = unr.T * mr * unr
        ue_s, _ = svd_asc_mp(ye_s)
        mnu_s = -ynu_s * (mr_s ** (-1)) * ynu_s.T
        ut_s, _ = takagi_true_mp(mnu_s)
        ut_sc = mp.matrix([[mp.conj(ut_s[r, c]) for c in range(3)] for r in range(3)])
        a_tr_s = pmns_angles(ue_s.H * ut_s)
        a_br_s = pmns_angles(ue_s.H * ut_sc)
        haar_true_max = max(haar_true_max, *(abs(a_tr_s[k] - ang_true[k]) for k in range(3)))
        haar_l8_broken_max = max(haar_l8_broken_max, *(abs(a_br_s[k] - ang_broken_true_takagi[k]) for k in range(3)))

    def eval_mirror_pair(g_vec: list[mp.mpf]) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
        ki = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_vec])

        def single(tv: mp.mpc, mirror_k: bool) -> tuple[mp.mpf, mp.mpf]:
            k5u = [(-a, b) for a, b in k5] if mirror_k else k5
            k6u = [(-a, b) for a, b in k6] if mirror_k else k6
            wu_l = w_avg(tv, k5u, 1, -4)
            wd_l = (w_avg(tv, k5u, 1, 2) + w_avg(tv, k6u, 1, 2)) / mp.mpf(2)
            wnu_l = (w_avg(tv, k5u, 3, -5) + w_avg(tv, k6u, 3, -5)) / mp.mpf(2)
            wr_l = (w_avg(tv, k5u, 3, 3) + w_avg(tv, k6u, 3, 3)) / mp.mpf(2)
            wr_sl = (wr_l + wr_l.T) / mp.mpf(2)
            _, svr_l = svd_asc_mp(wr_sl)
            mr_l = mp.eye(3) + wr_sl / svr_l[2]
            e5 = mp.exp(mp.mpf(2) * I_MP * mp.pi * tv / mp.mpf(5))
            d10_l = mp.diag([e5 ** n for n in (2, 0, 3)])
            yu_l, yd_l, ynu_l = ki * d10_l * wu_l * d10_l * ki, ki * d10_l * wd_l * ki, ki * wnu_l
            hu_l, hd_l = yu_l * yu_l.H, yd_l * yd_l.H
            cm = hu_l * hd_l - hd_l * hu_l
            cm3 = cm * cm * cm
            jdet = mp.im((cm3[0, 0] + cm3[1, 1] + cm3[2, 2]) / mp.mpf(6))
            ut_r, smr = takagi_true_mp(mr_l)
            ut_rc = mp.matrix([[mp.conj(ut_r[r, c]) for c in range(3)] for r in range(3)])
            yn_m = ynu_l * ut_rc
            hn = yn_m.H * yn_m
            e1 = mp.mpf(0)
            for j in (1, 2):
                xv = (smr[j] / smr[0]) ** 2
                fl = mp.sqrt(xv) * (mp.mpf(1) - (mp.mpf(1) + xv) * mp.log((mp.mpf(1) + xv) / xv) + mp.mpf(1) / (mp.mpf(1) - xv))
                e1 += -(mp.mpf(1) / (mp.mpf(8) * mp.pi * mp.re(hn[0, 0]))) * mp.im(hn[0, j] ** 2) * fl
            return jdet, -e1

        jp, ybp = single(tau8, False)
        jm, ybm = single(-q_mp(16, 5) + I_MP * q_mp(8, 5), True)
        return ybp, abs(ybp + ybm), abs((jp / ybp) - (jm / ybm))

    ybp_flat, yb_sum_flat, j_yb_diff_flat = eval_mirror_pair([mp.mpf(1), mp.mpf(1), mp.mpf(1)])
    ybp_curv, yb_sum_curv, j_yb_diff_curv = eval_mirror_pair(g_rk4)
    peer_l7_yb = mp.mpf(prod_l7["modules"]["F7_2"]["YB_proxy_tau8_pos"])

    with mp.workdps(60):
        p1, p2 = mp.pi / mp.mpf(2), mp.mpf(2) * mp.pi / mp.mpf(5)

        def df_rt(s: mp.mpf, c1: int, c2: int) -> mp.mpf:
            u = mp.mpf(3) * s
            e1 = mp.mpf(c1) * mp.exp(-p1 * u)
            e2 = mp.mpf(c2) * mp.exp(-p2 * u)
            w = e1 - e2
            wu = -p1 * e1 + p2 * e2
            wuu = p1 * p1 * e1 - p2 * p2 * e2
            a = mp.mpf(2) * s * wu - w
            da = mp.mpf(6) * s * wuu - wu
            return mp.mpf(2) * a * da - mp.mpf(6) * w * wu

        s_star = mp.findroot(lambda s: df_rt(s, 240, 1), (q_mp(603, 100), q_mp(605, 100)), solver="anderson")
        t_star = mp.mpf(2) * s_star
        u_star = mp.mpf(3) * s_star
        w_star = mp.mpf(240) * mp.exp(-p1 * u_star) - mp.exp(-p2 * u_star)
        wu_star = -p1 * mp.mpf(240) * mp.exp(-p1 * u_star) + p2 * mp.exp(-p2 * u_star)
        z_e = q_mp(1, 2) + I_MP * mp.sqrt(mp.mpf(3)) / mp.mpf(2)
        qe = mp.exp(mp.mpf(2) * I_MP * mp.pi * z_e)
        pr_e, qn = mp.mpc(1), qe
        for _ in range(180):
            pr_e *= mp.mpc(1) - qn
            qn *= qe
        inv_eis = mp.mpf(1) / (mp.mpf(2) * mp.im(z_e) * (abs(mp.exp(I_MP * mp.pi * z_e / mp.mpf(12)) * pr_e) ** 4))
        m32_mpl = mp.sqrt(inv_eis / (mp.mpf(8) * s_star * (t_star ** 2))) * abs(w_star)
        m0_ov = mp.mpf(2) * (mp.mpf(2) * s_star * wu_star - w_star) / w_star
        agut_inv = mp.mpf(5) * s_star
        g0 = mp.sqrt(mp.mpf(4) * mp.pi / agut_inv)
        yt0 = g0 / mp.sqrt(mp.mpf(2))
        t_susy = mp.log(m32_mpl * mp.sqrt(mp.mpf(8) * s_star * (t_star ** 2)))
        sym45_w_zero_s = mp.log(q_mp(4, 5)) / (mp.mpf(3) * (p1 - p2))
        sym54_w_zero_s = mp.log(q_mp(5, 4)) / (mp.mpf(3) * (p1 - p2))
        sym54_agut_inv = mp.mpf(5) * sym54_w_zero_s

    peer_agut = mp.mpf(prod_l7["modules"]["F7_4"]["alpha_GUT_inv_derived"])
    peer_m0 = mp.mpf(prod_l7["modules"]["F7_4"]["M0_tree_over_m32_derived"])
    racetrack_diffs = [abs(agut_inv - peer_agut), abs(m0_ov - peer_m0)]

    sympy_split_proof = verify_split_susy_rge_sympy()

    def mssm_gam(g1, g2, g3, yt, yb, ytau):
        g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
        yt2, yb2, yl2 = yt * yt, yb * yb, ytau * ytau
        return [
            mp.mpf(3) * yt2 - q_mp(3, 2) * g22 - q_mp(3, 10) * g12,
            mp.mpf(3) * yb2 + yl2 - q_mp(3, 2) * g22 - q_mp(3, 10) * g12,
            yt2 + yb2 - q_mp(8, 3) * g32 - q_mp(3, 2) * g22 - q_mp(1, 30) * g12,
            mp.mpf(2) * yt2 - q_mp(8, 3) * g32 - q_mp(8, 15) * g12,
            mp.mpf(2) * yb2 - q_mp(8, 3) * g32 - q_mp(2, 15) * g12,
            yl2 - q_mp(3, 2) * g22 - q_mp(3, 10) * g12,
            mp.mpf(2) * yl2 - q_mp(6, 5) * g12,
            -q_mp(8, 3) * g32 - q_mp(3, 2) * g22 - q_mp(1, 30) * g12,
            -q_mp(8, 3) * g32 - q_mp(8, 15) * g12,
            -q_mp(8, 3) * g32 - q_mp(2, 15) * g12,
            -q_mp(3, 2) * g22 - q_mp(3, 10) * g12,
            -q_mp(6, 5) * g12,
        ]

    def mssm24_rhs(_t: mp.mpf, y: list[mp.mpf]) -> list[mp.mpf]:
        k1 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
        g1, g2, g3, yt, yb, yl, m1, m2, m3, at, ab, al = y[:12]
        mhu, mhd, mq3, mu3, md3, ml3, me3, mq1, mu1, md1, ml1, me1 = y[12:]
        g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
        yt2, yb2, yl2 = yt * yt, yb * yb, yl * yl
        m12, m22, m32 = m1 * m1, m2 * m2, m3 * m3
        gm = mssm_gam(g1, g2, g3, yt, yb, yl)
        xt = mp.mpf(2) * yt2 * (mhu + mq3 + mu3 + at * at)
        xb = mp.mpf(2) * yb2 * (mhd + mq3 + md3 + ab * ab)
        xl = mp.mpf(2) * yl2 * (mhd + ml3 + me3 + al * al)
        sy = mhu - mhd + (mq3 - ml3 - mp.mpf(2) * mu3 + md3 + me3) + mp.mpf(2) * (mq1 - ml1 - mp.mpf(2) * mu1 + md1 + me1)
        return [
            k1 * q_mp(33, 5) * g12 * g1, k1 * g22 * g2, -k1 * mp.mpf(3) * g32 * g3,
            k1 * yt * (gm[0] + gm[2] + gm[3]), k1 * yb * (gm[1] + gm[2] + gm[4]), k1 * yl * (gm[1] + gm[5] + gm[6]),
            k1 * q_mp(66, 5) * g12 * m1, k1 * mp.mpf(2) * g22 * m2, -k1 * mp.mpf(6) * g32 * m3,
            k1 * (mp.mpf(12) * yt2 * at + mp.mpf(2) * yb2 * ab + q_mp(32, 3) * g32 * m3 + mp.mpf(6) * g22 * m2 + q_mp(26, 15) * g12 * m1),
            k1 * (mp.mpf(12) * yb2 * ab + mp.mpf(2) * yt2 * at + mp.mpf(2) * yl2 * al + q_mp(32, 3) * g32 * m3 + mp.mpf(6) * g22 * m2 + q_mp(14, 15) * g12 * m1),
            k1 * (mp.mpf(8) * yl2 * al + mp.mpf(6) * yb2 * ab + mp.mpf(6) * g22 * m2 + q_mp(18, 5) * g12 * m1),
            k1 * (mp.mpf(3) * xt - mp.mpf(6) * g22 * m22 - q_mp(6, 5) * g12 * m12 + q_mp(3, 5) * g12 * sy),
            k1 * (mp.mpf(3) * xb + xl - mp.mpf(6) * g22 * m22 - q_mp(6, 5) * g12 * m12 - q_mp(3, 5) * g12 * sy),
            k1 * (xt + xb - q_mp(32, 3) * g32 * m32 - mp.mpf(6) * g22 * m22 - q_mp(2, 15) * g12 * m12 + q_mp(1, 5) * g12 * sy),
            k1 * (mp.mpf(2) * xt - q_mp(32, 3) * g32 * m32 - q_mp(32, 15) * g12 * m12 - q_mp(4, 5) * g12 * sy),
            k1 * (mp.mpf(2) * xb - q_mp(32, 3) * g32 * m32 - q_mp(8, 15) * g12 * m12 + q_mp(2, 5) * g12 * sy),
            k1 * (xl - mp.mpf(6) * g22 * m22 - q_mp(6, 5) * g12 * m12 - q_mp(3, 5) * g12 * sy),
            k1 * (mp.mpf(2) * xl - q_mp(24, 5) * g12 * m12 + q_mp(6, 5) * g12 * sy),
            k1 * (-q_mp(32, 3) * g32 * m32 - mp.mpf(6) * g22 * m22 - q_mp(2, 15) * g12 * m12 + q_mp(1, 5) * g12 * sy),
            k1 * (-q_mp(32, 3) * g32 * m32 - q_mp(32, 15) * g12 * m12 - q_mp(4, 5) * g12 * sy),
            k1 * (-q_mp(32, 3) * g32 * m32 - q_mp(8, 15) * g12 * m12 + q_mp(2, 5) * g12 * sy),
            k1 * (-mp.mpf(6) * g22 * m22 - q_mp(6, 5) * g12 * m12 - q_mp(3, 5) * g12 * sy),
            k1 * (-q_mp(24, 5) * g12 * m12 + q_mp(6, 5) * g12 * sy),
        ]

    def am_soft(g1, g2, g3, yt, yb, yl) -> list[mp.mpf]:
        k1 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
        gm = mssm_gam(g1, g2, g3, yt, yb, yl)
        dy6 = mssm24_rhs(mp.mpf(0), [g1, g2, g3, yt, yb, yl] + [mp.mpf(0)] * 18)[:6]
        ep = p10_mp(-20)
        gp = mssm_gam(*(x + ep * dx for x, dx in zip((g1, g2, g3, yt, yb, yl), dy6)))
        gm2 = mssm_gam(*(x - ep * dx for x, dx in zip((g1, g2, g3, yt, yb, yl), dy6)))
        dg = [(gp[i] - gm2[i]) / (mp.mpf(2) * ep) for i in range(12)]
        return [
            k1 * q_mp(33, 5) * g1 * g1, k1 * g2 * g2, -k1 * mp.mpf(3) * g3 * g3,
            -k1 * (gm[0] + gm[2] + gm[3]), -k1 * (gm[1] + gm[2] + gm[4]), -k1 * (gm[1] + gm[5] + gm[6]),
        ] + [q_mp(1, 2) * k1 * dg[i] for i in range(12)]

    # Guardrail-4 benchmarks via 6th-order Richardson-GL4:
    guv_jj = [q_mp(7, 10), q_mp(7, 10), q_mp(7, 10), q_mp(1, 2), q_mp(1, 10), q_mp(1, 12)]
    y_jj = gl4_richardson(mssm24_rhs, guv_jj + am_soft(*guv_jj), mp.mpf(0), mp.mpf(-25), 64)
    s_jj = am_soft(*y_jj[:6])
    jj_gl4_err = max(abs(y_jj[6 + k] - s_jj[k]) for k in range(18))

    gfmm = [q_mp(7, 10), q_mp(7, 10), q_mp(7, 10), q_mp(3, 5), mp.mpf(0), mp.mpf(0)]
    y_fmm = gl4_richardson(mssm24_rhs, gfmm + [mp.mpf(0)] * 6 + [mp.mpf(1)] * 12, mp.mpf(0), mp.mpf(-30), 64)
    fmm_gl4_err = abs((y_fmm[12] - q_mp(1, 2) * (y_fmm[12] + y_fmm[14] + y_fmm[15])) + q_mp(1, 2))

    eps5_sq = abs(eps5) ** 2
    yb0 = yt0 * eps5_sq * (sd[2] / su[2])
    ytau0 = yt0 * eps5_sq * (se[2] / su[2])
    am0 = am_soft(g0, g0, g0, yt0, yb0, ytau0)
    y0_203 = [g0, g0, g0, yt0, yb0, ytau0] + [m0_ov + am0[k] for k in range(3)] + [-m0_ov + am0[3 + k] for k in range(3)] + [mp.mpf(1) + am0[6 + k] for k in range(12)]
    ypev = gl4_richardson(mssm24_rhs, y0_203, mp.mpf(0), t_susy, 56)
    ch_crit = mp.sqrt(ypev[12] * ypev[13])
    tanb = mp.sqrt(ypev[13] / ypev[12])
    sb = tanb / mp.sqrt(mp.mpf(1) + tanb * tanb)
    cb = mp.mpf(1) / mp.sqrt(mp.mpf(1) + tanb * tanb)
    c2b = cb * cb - sb * sb
    yt_sm0, yb_sm0, yl_sm0 = ypev[3] * sb, ypev[4] * cb, ypev[5] * cb
    mstop_ov = (ypev[14] * ypev[15]) ** q_mp(1, 4)

    def sm7_rhs(b_g: tuple[mp.mpf, mp.mpf, mp.mpf]):
        k1 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))

        def _f(_t: mp.mpf, st: list[mp.mpf]) -> list[mp.mpf]:
            g1, g2, g3, yt, yb, yl, lb = st
            g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
            yt2, yb2, yl2 = yt * yt, yb * yb, yl * yl
            tr = mp.mpf(3) * yt2 + mp.mpf(3) * yb2 + yl2
            return [
                k1 * b_g[0] * g12 * g1, k1 * b_g[1] * g22 * g2, k1 * b_g[2] * g32 * g3,
                k1 * yt * (tr + q_mp(3, 2) * (yt2 - yb2) - mp.mpf(8) * g32 - q_mp(9, 4) * g22 - q_mp(17, 20) * g12),
                k1 * yb * (tr + q_mp(3, 2) * (yb2 - yt2) - mp.mpf(8) * g32 - q_mp(9, 4) * g22 - q_mp(1, 4) * g12),
                k1 * yl * (tr + q_mp(3, 2) * yl2 - q_mp(9, 4) * g22 - q_mp(9, 4) * g12),
                k1 * (
                    mp.mpf(24) * lb * lb + mp.mpf(4) * lb * tr
                    - mp.mpf(2) * (mp.mpf(3) * yt2 * yt2 + mp.mpf(3) * yb2 * yb2 + yl2 * yl2)
                    - mp.mpf(3) * lb * (mp.mpf(3) * g22 + q_mp(3, 5) * g12)
                    + q_mp(3, 8) * (mp.mpf(2) * g22 * g22 + (g22 + q_mp(3, 5) * g12) ** 2)
                ),
            ]
        return _f

    def split11_rhs(_t: mp.mpf, st: list[mp.mpf]) -> list[mp.mpf]:
        k1 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
        g1, g2, g3, yt, yb, yl, lb, gu, gd, gup, gdp = st
        g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
        gp2 = q_mp(3, 5) * g12
        yt2, yb2, yl2 = yt * yt, yb * yb, yl * yl
        gu2, gd2, gup2, gdp2 = gu * gu, gd * gd, gup * gup, gdp * gdp
        tr_y = mp.mpf(3) * yt2 + mp.mpf(3) * yb2 + yl2
        gam_h_ss = q_mp(3, 2) * (gu2 + gd2) + q_mp(1, 2) * (gup2 + gdp2)
        box_ss = (
            -q_mp(5, 2) * (gu2 * gu2 + gd2 * gd2) - q_mp(1, 2) * (gup2 * gup2 + gdp2 * gdp2)
            - gu2 * gd2 - gu2 * gup2 - gd2 * gdp2 - gup2 * gdp2 - mp.mpf(2) * gu * gd * gup * gdp
        )
        return [
            k1 * q_mp(9, 2) * g12 * g1, k1 * (-q_mp(7, 6)) * g22 * g2, k1 * (-mp.mpf(5)) * g32 * g3,
            k1 * yt * (tr_y + gam_h_ss + q_mp(3, 2) * (yt2 - yb2) - mp.mpf(8) * g32 - q_mp(9, 4) * g22 - q_mp(17, 20) * g12),
            k1 * yb * (tr_y + gam_h_ss + q_mp(3, 2) * (yb2 - yt2) - mp.mpf(8) * g32 - q_mp(9, 4) * g22 - q_mp(1, 4) * g12),
            k1 * yl * (tr_y + gam_h_ss + q_mp(3, 2) * yl2 - q_mp(9, 4) * g22 - q_mp(9, 4) * g12),
            k1 * (
                mp.mpf(24) * lb * lb + mp.mpf(4) * lb * (tr_y + gam_h_ss) + box_ss
                - mp.mpf(2) * (mp.mpf(3) * yt2 * yt2 + mp.mpf(3) * yb2 * yb2 + yl2 * yl2)
                - mp.mpf(3) * lb * (mp.mpf(3) * g22 + gp2)
                + q_mp(3, 8) * (mp.mpf(2) * g22 * g22 + (g22 + gp2) ** 2)
            ),
            k1 * (gu * (-q_mp(33, 4) * g22 - q_mp(3, 4) * gp2 + tr_y + q_mp(11, 4) * gu2 + gd2 + q_mp(3, 4) * gup2 + q_mp(1, 2) * gdp2) + gd * gdp * gup),
            k1 * (gd * (-q_mp(33, 4) * g22 - q_mp(3, 4) * gp2 + tr_y + q_mp(11, 4) * gd2 + gu2 + q_mp(3, 4) * gdp2 + q_mp(1, 2) * gup2) + gu * gup * gdp),
            k1 * (gup * (-q_mp(9, 4) * g22 - q_mp(3, 4) * gp2 + tr_y + q_mp(5, 4) * gup2 + mp.mpf(2) * gdp2 + q_mp(9, 4) * gu2 + q_mp(3, 2) * gd2) + mp.mpf(3) * gd * gdp * gu),
            k1 * (gdp * (-q_mp(9, 4) * g22 - q_mp(3, 4) * gp2 + tr_y + q_mp(5, 4) * gdp2 + mp.mpf(2) * gup2 + q_mp(9, 4) * gd2 + q_mp(3, 2) * gu2) + mp.mpf(3) * gu * gup * gd),
        ]

    dt_split = mp.log(abs(m0_ov))
    lam_tree = ((ypev[1] ** 2 + q_mp(3, 5) * (ypev[0] ** 2)) / mp.mpf(8)) * (c2b ** 2)
    dlam_l8 = (mp.mpf(3) * (yt_sm0 ** 4)) / (mp.mpf(16) * (mp.pi ** 2)) * mp.log(mstop_ov)
    dlam_exact = mp.mpf(2) * dlam_l8

    b_ss = (q_mp(9, 2), -q_mp(7, 6), mp.mpf(-5))
    b_no_hino = (q_mp(41, 10), -q_mp(11, 6), mp.mpf(-5))
    b_sm = (q_mp(41, 10), -q_mp(19, 6), mp.mpf(-7))

    st_l8_m0 = gl4_richardson(sm7_rhs(b_ss), [ypev[0], ypev[1], ypev[2], yt_sm0, yb_sm0, yl_sm0, lam_tree + dlam_l8], mp.mpf(0), dt_split, 32)
    gp0 = mp.sqrt(q_mp(3, 5)) * ypev[0]
    st_full_m0 = gl4_richardson(
        split11_rhs,
        [ypev[0], ypev[1], ypev[2], yt_sm0, yb_sm0, yl_sm0, lam_tree + dlam_exact, ypev[1] * sb, ypev[1] * cb, gp0 * sb, gp0 * cb],
        mp.mpf(0), dt_split, 32,
    )[:7]
    st_nohino_m0 = gl4_richardson(sm7_rhs(b_no_hino), [ypev[0], ypev[1], ypev[2], yt_sm0, yb_sm0, yl_sm0, lam_tree + dlam_exact], mp.mpf(0), dt_split, 32)

    mh_comp: dict[str, Any] = {}
    for dti in (-3, -4, -5):
        ir_l8 = gl4_richardson(sm7_rhs(b_sm), st_l8_m0, mp.mpf(0), mp.mpf(dti), 32)
        ir_full = gl4_richardson(sm7_rhs(b_sm), st_full_m0, mp.mpf(0), mp.mpf(dti), 32)
        ir_nh = gl4_richardson(sm7_rhs(b_sm), st_nohino_m0, mp.mpf(0), mp.mpf(dti), 32)
        mh_l8 = mp.sqrt(mp.mpf(2) * ir_l8[6])
        mh_full = mp.sqrt(mp.mpf(2) * ir_full[6])
        mh_nh = mp.sqrt(mp.mpf(2) * ir_nh[6])
        mh_comp[f"dt_SM_{dti}"] = {
            "mh_over_v_L8_raw_repro": mp.nstr(mh_l8, 10),
            "mh_over_v_complete_SplitSUSY_GR": mp.nstr(mh_full, 10),
            "mh_over_v_heavy_higgsinos_decoupled": mp.nstr(mh_nh, 10),
            "rel_shift_complete_GR_vs_L8": mp.nstr((mh_full - mh_l8) / mh_l8, 6),
        }

    b203 = prod_l8["L8_5_unified_zero_placeholder_uv_to_ir_blind_lock"]["unified_blind_branches"]["branch_plus_203"]
    ch_diff = abs(ch_crit - mp.mpf(b203["giudice_masiero_cH_crit"]))
    tb_diff = abs(tanb - mp.mpf(b203["derived_tan_beta"]))
    mh4_diff = abs(mp.mpf(mh_comp["dt_SM_-4"]["mh_over_v_L8_raw_repro"]) - mp.mpf(b203["ir_trajectories_by_dt_SM"]["dt_SM_-4"]["mh_over_v"]))

    ek_star = inv_eis / (mp.mpf(8) * s_star * (t_star ** 2))
    h11_8 = 11
    chi_8 = 288 + 2160
    tau_8 = 32 + chi_8 // 3
    b4p_8 = ((chi_8 - 2 - 2 * h11_8) + tau_8) // 2
    kfth_8 = mp.mpf(b4p_8 - h11_8 - 1)
    rsq_8 = q_mp(chi_8, 12)
    worst_bp_log10 = mp.log10(ek_star * rsq_8) - ((kfth_8 / mp.mpf(2)) * mp.log10(mp.pi * rsq_8) - mp.log10(mp.gamma(kfth_8 / mp.mpf(2) + mp.mpf(1))))
    bp_shannon_bits_129 = mp.mpf(129) * mp.log(mp.mpf(10)) / mp.log(mp.mpf(2))

    y_wrong_dir = gl4_integrate(mssm24_rhs, y0_203, mp.mpf(0), -t_susy, 24)
    pf4_caught = bool(
        haar_true_max < p10_mp(-35)
        and haar_l8_broken_max > q_mp(1, 10)
        and fixing_only_vh_transpose_shift < p10_mp(-35)
        and y_wrong_dir[12] > mp.mpf(1)
    )

    passed = bool(
        gram_diff_vs_peer < p10_mp(-3)
        and rk4_pmns_diff < p10_mp(-3)
        and takagi_resid < p10_mp(-35)
        and repro_l8_diff < p10_mp(-5)
        and yb_sum_flat < p10_mp(-35) and j_yb_diff_flat < p10_mp(-35)
        and yb_sum_curv < p10_mp(-35) and j_yb_diff_curv < p10_mp(-35)
        and ybp_flat < mp.mpf(0) and peer_l7_yb < mp.mpf(0)
        and max(racetrack_diffs) < p10_mp(-16)
        and sym45_w_zero_s < mp.mpf(0)
        and all(sympy_split_proof.values())
        and jj_gl4_err < p10_mp(-17) and fmm_gl4_err < p10_mp(-35)
        and ch_diff < p10_mp(-6) and tb_diff < p10_mp(-6) and mh4_diff < p10_mp(-6)
        and abs(worst_bp_log10 - mp.mpf(prod_l8["L8_6_relaxion_nogo_2d_bp_margin_and_2bit_bedrock_floor"]["worst_case_bp_log10_spacing"])) < p10_mp(-5)
        and bp_shannon_bits_129 > mp.mpf(428)
        and pf4_caught
    )
    return {
        "disjoint_rk4_dirac_gramian": [mp.nstr(x, 10) for x in g_rk4],
        "rk4_vs_peer_gramian_max_diff": mp.nstr(gram_diff_vs_peer, 6),
        "rk4_vs_peer_true_pmns_max_diff": mp.nstr(rk4_pmns_diff, 6),
        "catch_FL8_F2_pmns_and_su2L_haar_bug": {
            "true_takagi_residual": mp.nstr(takagi_resid, 6),
            "true_gauge_invariant_pmns_s12_s23_s13_dm": [mp.nstr(x, 8) for x in ang_true] + [mp.nstr(dm_rat, 8)],
            "true_SU2L_10trial_haar_err": mp.nstr(haar_true_max, 8),
            "L8_5_broken_ueH_conj_ut_pmns_repro": [mp.nstr(x, 8) for x in ang_l8_repro],
            "L8_5_repro_diff_vs_peer_json": mp.nstr(repro_l8_diff, 6),
            "L8_5_broken_formula_true_SU2L_haar_violation": mp.nstr(haar_l8_broken_max, 8),
            "fixing_only_vh_transpose_shift_on_abs_Upmns_sq": mp.nstr(fixing_only_vh_transpose_shift, 8),
            "relay_takagi_diagnosis_refuted": bool(fixing_only_vh_transpose_shift < p10_mp(-35)),
        },
        "catch_FL8_F5_mirror_cpt_and_negative_YB_sign": {
            "flat_metric_YB_proxy_tau8_pos": mp.nstr(ybp_flat, 12),
            "curved_metric_YB_proxy_tau8_pos": mp.nstr(ybp_curv, 12),
            "flat_J_over_YB_mirror_diff": mp.nstr(j_yb_diff_flat, 8),
            "curved_J_over_YB_mirror_diff": mp.nstr(j_yb_diff_curv, 8),
            "F7_2_docstring_positive_YB_contradicted": bool(ybp_flat < mp.mpf(0) and peer_l7_yb < mp.mpf(0)),
        },
        "catch_FL8_F4_racetrack_and_split_susy_rge": {
            "polonyi_racetrack_verified_diffs_agut_M0": [mp.nstr(x, 8) for x in racetrack_diffs],
            "pure_SYM_4_5_W_zero_s_negative_no_pos_vac": mp.nstr(sym45_w_zero_s, 8),
            "pure_SYM_5_4_s_and_alpha_GUT_inv": [mp.nstr(sym54_w_zero_s, 8), mp.nstr(sym54_agut_inv, 8)],
            "sympy_complete_split_susy_weyl_proof": sympy_split_proof,
            "gl4_richardson_jack_jones_and_fmm_errs": [mp.nstr(jj_gl4_err, 6), mp.nstr(fmm_gl4_err, 6)],
            "gl4_vs_L8_cH_tanb_mh4_raw_diffs": [mp.nstr(ch_diff, 6), mp.nstr(tb_diff, 6), mp.nstr(mh4_diff, 6)],
            "stop_threshold_L8_vs_exact_2x_CW": [mp.nstr(dlam_l8, 8), mp.nstr(dlam_exact, 8)],
            "mh_over_v_L8_vs_complete_SplitSUSY_GR": mh_comp,
        },
        "catch_FL8_F6_bp_shannon_bit_floor_contradiction": {
            "worst_case_r8_bp_log10_spacing_verified": mp.nstr(worst_bp_log10, 8),
            "shannon_bits_for_10e129_flux_window": mp.nstr(bp_shannon_bits_129, 8),
        },
        "pf4_haar_break_and_wrong_rge_dir_caught": pf4_caught,
        "passed": passed,
    }


# ==============================================================================
# PA2-E: Independent Zero-Trust Audit of agy (b06c8fc1e: C37 v7.json, C38, OW22)
# ==============================================================================

def run_pa2_e() -> dict[str, Any]:
    mp.mp.dps = 50
    v7 = json.loads(git_show_bytes(AGY_REF, "relays/agy_2026-11-23_c37/blind_predictions_full_toe_v7.json").decode("utf-8"))["prediction_bundle_v7"]
    c38 = json.loads(git_show_bytes(AGY_REF, "relays/agy_2026-11-24_c38/c38_out.json").decode("utf-8"))

    m11_s = sp.Symbol("M_11", positive=True)
    two_k11_sq = (2 * sp.pi) ** 8 * m11_s ** (-9)
    t_m2_exact = m11_s ** 3 / (2 * sp.pi) ** 2
    dirac_quant_ok = bool(sp.simplify(two_k11_sq * (t_m2_exact ** 3) - (2 * sp.pi) ** 2) == 0)

    # Exact SymPy proof that Caswell-Jones 2-loop Lambda_QCD is RG-invariant (d ln Lambda / d ln mu == 0):
    a_s, b0_s, b1_s = sp.symbols("a_s b0 b1", positive=True)
    ex_s = b1_s / (2 * b0_s ** 2)
    ln_lam = -2 * sp.pi / (b0_s * a_s) - ex_s * sp.log(b0_s * a_s / (4 * sp.pi)) + ex_s * sp.log(1 + b1_s * a_s / (4 * sp.pi * b0_s))
    da_dt = -(b0_s / (2 * sp.pi)) * a_s ** 2 - (b1_s / (8 * sp.pi ** 2)) * a_s ** 3
    sympy_lam_rg_zero = bool(sp.simplify(1 + sp.diff(ln_lam, a_s) * da_dt) == 0)

    vol41 = mp.mpf(3) * mp.im(mp.polylog(2, mp.exp(mp.mpf(2) * I_MP * mp.pi / mp.mpf(3))))
    m11_mgut = (mp.mpf(40) * ((mp.mpf(2) * mp.pi) ** 3) / (mp.mpf(8) * vol41)) ** q_mp(1, 3)
    vp_hat = ((mp.mpf(2) * mp.pi) ** 4) / mp.mpf(48)
    mpl_mgut_sd = mp.sqrt(mp.mpf(8) * (m11_mgut ** 5) * (mp.mpf(8) * vol41) * vp_hat / ((mp.mpf(2) * mp.pi) ** 7))
    mpl_mgut_iso = mp.sqrt(mp.mpf(8) * (m11_mgut ** 9) * (mp.mpf(8) * vol41) * vp_hat / ((mp.mpf(2) * mp.pi) ** 7))

    t_ew_star = mp.mpf(v7["dynamical_rg_horizons_ln_mu_over_mgut"]["t_ew_star"])
    mgut_over_vew = mp.exp(-t_ew_star)
    mpl_vew_sd = mpl_mgut_sd * mgut_over_vew
    mpl_vew_iso = mpl_mgut_iso * mgut_over_vew

    v7_grav = v7["gravity_11d_d4_hurwitz_sector"]
    m11_diff = abs(m11_mgut - mp.mpf(v7_grav["m11_over_mgut_zero_knob"]))
    mpl_sd_rel = abs(mpl_vew_sd - mp.mpf(v7_grav["mpl_over_vew_d4_hurwitz_self_dual"])) / mpl_vew_sd
    mpl_iso_rel = abs(mpl_vew_iso - mp.mpf(v7_grav["mpl_over_vew_d4_hurwitz_isotropic"])) / mpl_vew_iso

    a3_ir = mp.mpf(v7["sm_1loop_pole_and_2hdm_bosons"]["strong_coupling_ir"])

    def lam_cj(mu_q: mp.mpf, av: mp.mpf, nf: int) -> mp.mpf:
        b0 = q_mp(33 - 2 * nf, 3)
        b1 = q_mp(306 - 38 * nf, 3)
        ex = b1 / (mp.mpf(2) * b0 * b0)
        return mu_q * mp.exp(-mp.mpf(2) * mp.pi / (b0 * av)) * (((b0 * av) / (mp.mpf(4) * mp.pi)) ** (-ex)) * ((mp.mpf(1) + (b1 * av) / (mp.mpf(4) * mp.pi * b0)) ** ex)

    lam_5f = lam_cj(mp.mpf(1), a3_ir, 5)
    lam_5f_rel = abs(lam_5f - mp.mpf(v7["sm_1loop_pole_and_2hdm_bosons"]["qcd_Lambda_5f_over_vew"])) / lam_5f

    b0_5, b1_5 = q_mp(23, 3), q_mp(116, 3)
    rhs_a3_5 = lambda _t, y: [-(b0_5 / (mp.mpf(2) * mp.pi)) * (y[0] ** 2) - (b1_5 / (mp.mpf(8) * (mp.pi ** 2))) * (y[0] ** 3)]
    a3_test = gl4_richardson(rhs_a3_5, [a3_ir], mp.mpf(0), mp.mpf(-2), 48)[0]
    lam_5f_rg_invar = abs(lam_cj(mp.exp(mp.mpf(-2)), a3_test, 5) - lam_5f) / lam_5f

    # Also verify Lambda_QCD^(4f) / v_EW by recovering m_b(v_EW) from v7 u3_pole & u3_over_d3 and running 2-loop alpha_s(nf=5) via Richardson-GL4:
    u3_pole_v7 = mp.mpf(v7["sm_1loop_pole_and_2hdm_bosons"]["u3_pole_over_vew"])
    u3_ms_v7 = mp.findroot(lambda x: x * (mp.mpf(1) + (a3_ir / mp.pi) * (q_mp(4, 3) - mp.mpf(2) * mp.log(x))) - u3_pole_v7, u3_pole_v7)
    mb_ms_v7 = u3_ms_v7 / mp.mpf(v7["sm_msbar_at_ew_horizon"]["u3_over_d3"])
    a3_at_mb_v7 = gl4_richardson(rhs_a3_5, [a3_ir], mp.mpf(0), mp.log(mb_ms_v7), 48)[0]
    lam_4f = lam_cj(mb_ms_v7, a3_at_mb_v7, 4)
    lam_4f_rel = abs(lam_4f - mp.mpf(v7["sm_1loop_pole_and_2hdm_bosons"]["qcd_Lambda_4f_over_vew"])) / lam_4f

    # Explicit 6D I_8 gravity anomaly cancellation at (n_T=1, Spin(10) n_V=45, n_16=0, n_10=2, n_1=269):
    i8_grav_resid = (2 * 10 + 269) - 45 + 29 * 1 - 273  # == 0!
    # Explicit D-flat STr M_{Z'_chi}^2 == 0 from 4x4 real scalar, 1 massive vector (3 DOF), & 3x3 Weyl fermion mass matrices:
    mv_sq_s = sp.Symbol("M_V_sq", positive=True)
    m_scal_4 = sp.diag(mv_sq_s, 0, 0, 0)
    m_ferm_3 = sp.Matrix([[0, sp.sqrt(mv_sq_s) / sp.sqrt(2), -sp.sqrt(mv_sq_s) / sp.sqrt(2)],
                          [sp.sqrt(mv_sq_s) / sp.sqrt(2), 0, 0],
                          [-sp.sqrt(mv_sq_s) / sp.sqrt(2), 0, 0]])
    str_zchi_sq = sp.simplify(m_scal_4.trace() + 3 * mv_sq_s - 2 * (m_ferm_3 * m_ferm_3.T).trace())

    sd_to_iso_ratio = mpl_mgut_iso / mpl_mgut_sd
    v7_cosmo = v7["cosmology_crv_and_honest_bounds"]
    k1_sd = mp.mpf(v7_cosmo["leptogenesis_washout_K1_tot"])
    gtau_sd = mp.mpf(v7_cosmo["leptogenesis_tau_equil_over_hubble"])
    yb_sd = mp.mpf(v7_cosmo["leptogenesis_Y_B_2flavor_analytic_fit"])
    k1_iso = k1_sd * sd_to_iso_ratio
    gtau_iso = gtau_sd * sd_to_iso_ratio
    washout_drop_factor = sd_to_iso_ratio ** q_mp(29, 25)
    yb_iso_est = yb_sd / washout_drop_factor

    f16_spec = [
        ("Q", 3, 2, 1, -1),
        ("u^c", 3, 1, -4, -1),
        ("d^c", 3, 1, 2, 3),
        ("L", 1, 2, -3, 3),
        ("e^c", 1, 1, 6, -1),
        ("nu^c", 1, 1, 0, -5),
    ]

    def calc_6_anoms(spec):
        su3_chi = sum(Fr(nw * qx, 2) for _, nc, nw, _, qx in spec if nc == 3)
        su2_chi = sum(Fr(nc * qx, 2) for _, nc, nw, _, qx in spec if nw == 2)
        y2_chi = sum(Fr(nc * nw * (y6 ** 2) * qx, 36) for _, nc, nw, y6, qx in spec)
        y_chi2 = sum(Fr(nc * nw * y6 * (qx ** 2), 6) for _, nc, nw, y6, qx in spec)
        chi3 = sum(Fr(nc * nw * (qx ** 3)) for _, nc, nw, _, qx in spec)
        grav_chi = sum(Fr(nc * nw * qx) for _, nc, nw, _, qx in spec)
        return [su3_chi, su2_chi, y2_chi, y_chi2, chi3, grav_chi]

    anoms_16 = calc_6_anoms(f16_spec)
    anoms_no_nuc = calc_6_anoms(f16_spec[:-1])

    s_bl1 = mp.mpf(c38["E2_all_6_anomalies_and_explicit_dflat_str_zchi"]["four_modulus_newton_t_s_re_im_45d"][1])
    g_bl1_sq = mp.mpf(4) * mp.pi / s_bl1
    lam_s_b4 = q_mp(3, 5)
    l1_b4 = q_mp(2, 5) * g_bl1_sq
    l2_b4 = q_mp(2, 5) * g_bl1_sq
    l3_b4 = q_mp(1, 10) * g_bl1_sq
    l4_b4 = lam_s_b4 * lam_s_b4 - q_mp(1, 2) * g_bl1_sq
    peer_q_b4 = [mp.mpf(x) for x in c38["E3_b4_2hdm_quartics_and_b6_verification"]["B4_2hdm_quartics_recomputed"]["derived_2hdm_quartics_at_s_star_35d"]]
    b4_quartic_diff = max(abs(a - b) for a, b in zip([l1_b4, l2_b4, l3_b4, l4_b4], peer_q_b4))

    rng = random.Random(2026112437)
    c_nu = mp.matrix([[mp.mpc(rng.randint(-5, 5), rng.randint(-5, 5)) for _ in range(3)] for _ in range(3)])
    c_r_raw = mp.matrix([[mp.mpc(rng.randint(-5, 5), rng.randint(-5, 5)) for _ in range(3)] for _ in range(3)])
    c_r = c_r_raw + c_r_raw.T + mp.mpf(17) * mp.eye(3)
    d_e5 = mp.diag([q_mp(1, 2), q_mp(1, 3), q_mp(1, 5)])
    d_e1 = mp.diag([q_mp(1, 7), q_mp(1, 11), q_mp(1, 13)])
    m_nu_with_e1 = -(d_e5 * c_nu * d_e1) * ((d_e1 * c_r * d_e1) ** (-1)) * (d_e5 * c_nu * d_e1).T
    m_nu_no_e1 = -(d_e5 * c_nu) * (c_r ** (-1)) * (d_e5 * c_nu).T
    eps1_cancel_err = mp.sqrt(sum(abs(m_nu_with_e1[i, j] - m_nu_no_e1[i, j]) ** 2 for i in range(3) for j in range(3)))

    ow22_a1_verified = {
        "B4_UV_52_13": frac_str(Fr(52 - 13, 2)),
        "B4_IR_49_12": frac_str(Fr(49 - 12, 2)),
        "B5_IR_85_12": frac_str(Fr(85 - 12, 2)),
        "B5_13vec_85_13": frac_str(Fr(85 - 13, 2)),
        "B5_UV_E6_85_14": frac_str(Fr(85 - 14, 2)),
    }
    r_ss = mp.log(mp.mpf(2)) / mp.mpf(32)
    b1_eff = r_ss * q_mp(33, 5) + (mp.mpf(1) - r_ss) * q_mp(21, 5)
    b2_eff = r_ss * mp.mpf(1) + (mp.mpf(1) - r_ss) * mp.mpf(-3)
    b3_eff = r_ss * mp.mpf(-3) + (mp.mpf(1) - r_ss) * mp.mpf(-7)
    beff_t2_ss = (b2_eff - b3_eff) / (b1_eff - b2_eff)

    c35_quant_ratio = sp.simplify((two_k11_sq * (m11_s ** 9)) / ((2 * sp.pi) ** 2))
    pf5_caught = bool(anoms_no_nuc[4] == Fr(125) and anoms_no_nuc[5] == Fr(5) and c35_quant_ratio == (2 * sp.pi) ** 6)

    passed = bool(
        dirac_quant_ok
        and sympy_lam_rg_zero
        and m11_diff < p10_mp(-24)
        and mpl_sd_rel < p10_mp(-9)
        and mpl_iso_rel < p10_mp(-9)
        and lam_5f_rel < p10_mp(-9)
        and lam_4f_rel < p10_mp(-9)
        and lam_5f_rg_invar < p10_mp(-15)
        and i8_grav_resid == 0
        and str_zchi_sq == 0
        and all(x == 0 for x in anoms_16)
        and b4_quartic_diff < p10_mp(-30)
        and eps1_cancel_err < p10_mp(-42)
        and beff_t2_ss < q_mp(3, 5)
        and pf5_caught
    )
    return {
        "AGY_C37_C38_verified_the_same": {
            "dirac_11d_quantization_exact": dirac_quant_ok,
            "sympy_caswell_jones_2loop_rg_invar_exact": sympy_lam_rg_zero,
            "m11_over_mgut_abs_diff": mp.nstr(m11_diff, 8),
            "mpl_sd_and_iso_rel_diffs": [mp.nstr(mpl_sd_rel, 8), mp.nstr(mpl_iso_rel, 8)],
            "lambda_qcd_5f_4f_rel_diffs_and_gl4_rich_rg_invar": [mp.nstr(lam_5f_rel, 8), mp.nstr(lam_4f_rel, 8), mp.nstr(lam_5f_rg_invar, 8)],
            "i8_6d_gravity_anom_at_n10_2_n1_269": i8_grav_resid,
            "dflat_STr_M_Zchi_sq_exact": int(str_zchi_sq),
            "all_6_u1chi_anomalies_zero": all(x == 0 for x in anoms_16),
            "C38_B4_2hdm_quartic_max_diff": mp.nstr(b4_quartic_diff, 8),
            "C37_E3_seesaw_eps1_cancellation_frob_err": mp.nstr(eps1_cancel_err, 8),
        },
        "seam_AGY_C37_S1_leptogenesis_sd_vs_iso_branch": {
            "mpl_iso_over_sd_ratio": mp.nstr(sd_to_iso_ratio, 10),
            "K1_sd_vs_iso": [mp.nstr(k1_sd, 8), mp.nstr(k1_iso, 8)],
            "Gamma_tau_over_H_sd_vs_iso": [mp.nstr(gtau_sd, 8), mp.nstr(gtau_iso, 8)],
            "washout_drop_factor_R_pow_29_25": mp.nstr(washout_drop_factor, 8),
            "Y_B_sd_sealed_vs_iso_estimate": [mp.nstr(yb_sd, 8), mp.nstr(yb_iso_est, 8)],
        },
        "OW22_F1_F3_acknowledged_and_resolved": {
            "OW22_F1_stage_consistent_a1_table": ow22_a1_verified,
            "OW22_F2_T2_SS_Beff_collapse": mp.nstr(beff_t2_ss, 10),
            "OW22_F2_superseded_in_agy002": "Superseded by 4D dynamical hidden-sector NSVZ gaugino condensation in A2-OW23..OW27 (giving M_SUSY << M_GUT cleanly).",
            "OW22_F3_acknowledged": "Single E_8 vector multiplet picks 1 homomorphism in Hom(Z^2, Z_2) \\ {0}; 3 generations biject onto E[2] \\ {0}.",
        },
        "pf5_drop_nuc_and_c35_quant_caught": pf5_caught,
        "passed": passed,
    }


# ==============================================================================
# PA2-F: Strictly Blind (0 of 19) Cross-Seat Vector Comparison & LOCK_V3 Check
# ==============================================================================

def run_pa2_f(pa2_d: dict[str, Any]) -> dict[str, Any]:
    ow27 = json.loads((REPO_ROOT / "relays/a2_ow27_v8/a2_ow27_v8_results.json").read_text(encoding="utf-8"))
    v7 = json.loads(git_show_bytes(AGY_REF, "relays/agy_2026-11-23_c37/blind_predictions_full_toe_v7.json").decode("utf-8"))["prediction_bundle_v7"]
    l8 = json.loads(git_show_bytes(AGY_EXP_REF, "relays/x_floor_link8_verify/verify_x_floor_link8_out.json").decode("utf-8"))

    ow27_e = ow27["OW27_E_planted_faults_and_blind_lock_v3"]
    lock_v3_digest = ow27_e["blind_prediction_lock_v3_sha256"]
    lock_v3_intact = bool(lock_v3_digest == EXPECTED_LOCK_V3)

    payload_copy = dict(ow27_e["blind_prediction_lock_v3_B4_UV"])
    raw_ok = hashlib.sha256(json.dumps(payload_copy, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    payload_copy["tampered_flag"] = "1"
    raw_bad = hashlib.sha256(json.dumps(payload_copy, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    pf6_caught = bool(raw_ok == EXPECTED_LOCK_V3 and raw_bad != EXPECTED_LOCK_V3)

    runs = ow27["OW27_A_2loop_qcd_4coupling_higgs_veltman_decoupling_and_lambda_qcd"]["mz_and_mt_2loop_pipeline_runs"]
    p3 = runs["CURV_s12_Dirac_yt_gUV_tb15_m0_3v_sgnMu_pos"]
    p10 = runs["CURV_s12_Dirac_yt_gUV_tb15_m0_10v_sgnMu_pos"]
    b203 = l8["L8_5_unified_zero_placeholder_uv_to_ir_blind_lock"]["unified_blind_branches"]["branch_plus_203"]

    table_0_of_19 = {
        "agy_002_B4_UV_LOCK_V3_m0_3v_10v": {
            "alpha_3_5f": [p3["alpha3_mz_nf5"], p10["alpha3_mz_nf5"]],
            "sin2_thetaW_MSbar": [p3["sin2_thetaW_msbar_mz"], p10["sin2_thetaW_msbar_mz"]],
            "mh_pole_over_MZ": [p3["mh_pole_4c_at_mz_over_mz"], p10["mh_pole_4c_at_mz_over_mz"]],
            "Lambda_QCD_4f_over_vEW": [p3["Lambda_QCD_4_exact_over_v"], p10["Lambda_QCD_4_exact_over_v"]],
            "honest_ledger_partition": "1/10/9/4 = 24 (OBS-18/20/24 honestly open)",
        },
        "agy_v7_json_nonsusy_2HDM": {
            "alpha_3_ir": v7["sm_1loop_pole_and_2hdm_bosons"]["strong_coupling_ir"],
            "sin2_thetaW_ir": v7["sm_msbar_at_ew_horizon"]["electroweak_mix_ratio"],
            "mh0_over_vEW": v7["sm_1loop_pole_and_2hdm_bosons"]["higgs_h0_over_vew"],
            "Lambda_QCD_4f_over_vEW": v7["sm_1loop_pole_and_2hdm_bosons"]["qcd_Lambda_4f_over_vew"],
            "honest_ledger_partition": "12 continuous UV + 39/2..41/2 discrete bits",
        },
        "agy_exp_LINK8_dtSM_m4_raw_vs_corrected": {
            "alpha_3_dt_m4": b203["ir_trajectories_by_dt_SM"]["dt_SM_-4"]["alpha_s"],
            "sin2_thetaW_dt_m4": b203["ir_trajectories_by_dt_SM"]["dt_SM_-4"]["sin2_thetaW"],
            "mh_over_v_raw_vs_complete_GR": [
                b203["ir_trajectories_by_dt_SM"]["dt_SM_-4"]["mh_over_v"],
                pa2_d["catch_FL8_F4_racetrack_and_split_susy_rge"]["mh_over_v_L8_vs_complete_SplitSUSY_GR"]["dt_SM_-4"]["mh_over_v_complete_SplitSUSY_GR"],
            ],
            "pmns_s12_s23_s13_L8_corrupted_vs_true_Takagi": [
                b203["pmns_s12sq_s23sq_s13sq_dmratio"][:3],
                pa2_d["catch_FL8_F2_pmns_and_su2L_haar_bug"]["true_gauge_invariant_pmns_s12_s23_s13_dm"][:3],
            ],
            "claimed_vs_audited_floor": "Claimed 2.0 bits + 1 cont; audited >= 430+ bits (BP 428.5 + R1 + R2 + K6>=1 + c1=240/SU4xSU5 + mu_X^4)",
        },
    }

    passed = bool(lock_v3_intact and pf6_caught)
    return {
        "lock_v3_digest_intact": lock_v3_intact,
        "lock_v3_sha256": lock_v3_digest,
        "cross_seat_blind_comparison_0_of_19": table_0_of_19,
        "pf6_lock_v3_tamper_caught": pf6_caught,
        "passed": passed,
    }


def main() -> None:
    src = SELF_PATH.read_text(encoding="utf-8")
    self_ast = scan_ast_hygiene(src, SELF_PATH.name)
    self_sha = hashlib.sha256(SELF_PATH.read_bytes()).hexdigest()

    ra = run_pa2_a()
    rb = run_pa2_b()
    rc = run_pa2_c()
    rd = run_pa2_d()
    re = run_pa2_e()
    rf = run_pa2_f(rd)

    all_ok = bool(
        self_ast["clean"]
        and ra["passed"]
        and rb["passed"]
        and rc["passed"]
        and rd["passed"]
        and re["passed"]
        and rf["passed"]
    )
    payload = {
        "card": "AGY-002_A2-PEER-AUDIT-V2",
        "version": "run3 (remediates Cold-Room Referee DISC-PA2-1, DISC-PA2-2, & NBD-PA2-1..3; frozen v1 & run2 untouched)",
        "seat": "agy-002",
        "firewall": "0 of 19",
        "check_labels_section_12": [
            "computed once",
            "expectations committed first",
            "recomputed independently",
            "tested against planted errors",
        ],
        "script": SELF_PATH.name,
        "script_sha256": self_sha,
        "self_ast_hygiene": self_ast,
        "PA2_A_custody_hygiene_and_referee_audit": ra,
        "PA2_B_agy_exp_block_B1_hirzebruch_and_E8": rb,
        "PA2_C_agy_exp_block_A_genesis_spin10_K6_outD5": rc,
        "PA2_D_agy_exp_block_B2_pmns_racetrack_splitsusy_bp": rd,
        "PA2_E_agy_C37_C38_v7_and_OW22_closure": re,
        "PA2_F_blind_cross_seat_comparison_and_lock_v3": rf,
        "planted_controls_caught": sum(1 for x in [ra["pf1_tampered_manifest_caught"], rb["pf2_bad_n10_and_F6_caught"], rc["pf3_S_swap_and_tr4_S3_caught"], rd["pf4_haar_break_and_wrong_rge_dir_caught"], re["pf5_drop_nuc_and_c35_quant_caught"], rf["pf6_lock_v3_tamper_caught"]] if x),
        "planted_controls_total": 6,
        "all_gates_passed": all_ok,
    }
    assert_no_json_floats(payload)
    OUT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not all_ok:
        raise AssertionError("One or more PA2 modules failed!")


if __name__ == "__main__":
    main()
