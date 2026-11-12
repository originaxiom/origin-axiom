#!/usr/bin/env python3
"""Independent pure-mathematics, AST-mutation, and machine-quotation verification for Card X-R79b.

Pinned origin/main commit read: 896cae025238cda82304de7424bf05f83cb69abe (mend diff base 0dda7b4725f613dbef273edafcd3fca73ccb245c).
Firewall: pure mathematics and repository governance/audit checks only; zero measured values opened or computed (0 of 19);
zero producer modules imported; B1887 strictly untouched under section 13 and section 9 item 2 (conflict of interest on agy-exp's own loop build).
"""
from __future__ import annotations

import ast
import cmath
import collections
import difflib
import fractions
import gzip
import hashlib
import itertools
import json
import math
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
PINNED_MAIN = "896cae025238cda82304de7424bf05f83cb69abe"
BASE_MAIN = "0dda7b4725f613dbef273edafcd3fca73ccb245c"
Frac = fractions.Fraction


def _guard_b1887(target: str) -> None:
    if "1887" in target:
        raise RuntimeError(f"Forbidden access to B1887 (self-build conflict boundary): {target}")


def git_show(commit: str, rel_path: str) -> str:
    _guard_b1887(rel_path)
    return subprocess.check_output(
        ["git", "show", f"{commit}:{rel_path}"], cwd=REPO_ROOT, text=True
    )


def git_show_bytes(commit: str, rel_path: str) -> bytes:
    _guard_b1887(rel_path)
    return subprocess.check_output(
        ["git", "show", f"{commit}:{rel_path}"], cwd=REPO_ROOT
    )


def git_cmd(*args: str) -> str:
    for a in args:
        _guard_b1887(a)
    return subprocess.check_output(["git", *args], cwd=REPO_ROOT, text=True)


# ---------------------------------------------------------------------------
# 0. Pre-committed negative controls (must pass first; exit 2 on failure)
# ---------------------------------------------------------------------------

_PURE_LITERAL_CALLS = {"len", "round", "abs", "Fraction", "Fr", "set", "tuple", "list", "frozenset", "bool", "int", "float"}


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


def is_syntactic_self_equality(node: ast.AST) -> bool:
    """Return True iff `node` compares two syntactically identical expressions with `==` or `is`."""
    if isinstance(node, ast.Compare) and len(node.ops) == 1 and isinstance(node.ops[0], (ast.Eq, ast.Is)):
        return ast.dump(node.left) == ast.dump(node.comparators[0])
    return False


def scan_non_failing_assertions_and_checks(source_code: str) -> list[dict[str, object]]:
    """Scan every `assert` statement (including `and`-joined clauses) and `check(name, cond, ...)` call for non-failing forms."""
    tree = ast.parse(source_code)
    flagged: list[dict[str, object]] = []

    def _clauses(expr: ast.AST) -> list[ast.AST]:
        if isinstance(expr, ast.BoolOp) and isinstance(expr.op, ast.And):
            out: list[ast.AST] = []
            for v in expr.values:
                out.extend(_clauses(v))
            return out
        return [expr]

    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):
            for clause in _clauses(node.test):
                if is_constant_or_literal_expr(clause) or is_syntactic_self_equality(clause):
                    flagged.append({"kind": "assert", "lineno": node.lineno, "expr": ast.unparse(clause)})
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "check":
            if len(node.args) >= 2:
                cond = node.args[1]
                if is_constant_or_literal_expr(cond) or is_syntactic_self_equality(cond):
                    flagged.append({"kind": "check_call", "lineno": node.lineno, "expr": ast.unparse(cond)})
    return flagged


def quote_present_at_commit(commit: str, rel_path: str, quote: str) -> dict[str, bool]:
    """Verify both exact literal substring match and whitespace-joined match (as in main's quote_check.py)."""
    raw = git_show(commit, rel_path)
    norm_raw = " ".join(raw.split())
    norm_quote = " ".join(quote.split())
    return {
        "exact_substring": quote in raw,
        "whitespace_joined": bool(norm_quote) and (norm_quote in norm_raw),
    }


def run_precommitted_controls() -> dict[str, object]:
    # Control 1 (Card section 5.1 -- M6 standing-tautology beside real check):
    synthetic_mended_test = (
        "from fractions import Fraction\n"
        "def test_mended_with_standing_tautology(widths, e2, e3):\n"
        "    genus = 1 + Fraction(12, 12) - Fraction(e2, 4) - Fraction(e3, 3) - Fraction(len(widths), 2)\n"
        "    assert genus == 0\n"
        "    assert 1 + (12 - 12 * Fraction(1, 2) - 4 * Fraction(3, 2)) / 12 == 0\n"
        "    assert genus == genus\n"
    )
    flagged = scan_non_failing_assertions_and_checks(synthetic_mended_test)
    if len(flagged) != 2:
        sys.stderr.write(f"CONTROL 1 FAILED: expected 2 standing non-failing assertions flagged, got {flagged}\n")
        sys.exit(2)

    # Control 2 (Card section 5.2 -- quotation verifier against 896cae025 rejects 0dda7b472 / perturbed text):
    stale_from_0dda7b472 = quote_present_at_commit(
        PINNED_MAIN,
        "frontier/B1888_the_public_form_scrutinised/FINDINGS.md",
        "In the whole tree 50 do",
    )
    valid_at_896cae025 = quote_present_at_commit(
        PINNED_MAIN,
        "frontier/B1888_the_public_form_scrutinised/FINDINGS.md",
        "In the whole tree 51 do",
    )
    perturbed_one_char = quote_present_at_commit(
        PINNED_MAIN,
        "frontier/B1888_the_public_form_scrutinised/FINDINGS.md",
        "In the whole tree 52 do",
    )
    if stale_from_0dda7b472["whitespace_joined"] or stale_from_0dda7b472["exact_substring"]:
        sys.stderr.write("CONTROL 2a FAILED: admitted stale 0dda7b472 quotation on 896cae025\n")
        sys.exit(2)
    if not (valid_at_896cae025["whitespace_joined"] and valid_at_896cae025["exact_substring"]):
        sys.stderr.write("CONTROL 2b FAILED: rejected genuine 896cae025 quotation\n")
        sys.exit(2)
    if perturbed_one_char["whitespace_joined"] or perturbed_one_char["exact_substring"]:
        sys.stderr.write("CONTROL 2c FAILED: admitted 1-char-perturbed quotation on 896cae025\n")
        sys.exit(2)

    return {
        "control_1_m6_standing_tautology_flagged_count": len(flagged),
        "control_1_flagged_lines": [f["lineno"] for f in flagged],
        "control_2_stale_rejected": not stale_from_0dda7b472["whitespace_joined"],
        "control_2_valid_accepted": valid_at_896cae025["exact_substring"],
        "control_2_perturbed_rejected": not perturbed_one_char["whitespace_joined"],
        "all_controls_passed": True,
    }


# ---------------------------------------------------------------------------
# 1. Task 1: Independent Audit of Main's Answers & Mends on X1..X15 (F-01..F-15)
# ---------------------------------------------------------------------------

def unquote_flat(text: str) -> str:
    return " ".join(re.sub(r"(?m)^>\s*", "", text).split())


def verify_task1_x1_to_x15() -> dict[str, object]:
    # First, run the AST standing-tautology / non-failing check scan across EVERY test & script touched for X1..X15
    mended_code_paths = [
        "tests/test_b1221_the_adjoint_control.py",
        "tests/test_b1641_w46_on_main_and_the_two_objects.py",
        "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py",
        "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py",
        "frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main.py",
        "frontier/B1885_the_golden_state_on_the_whole_verified/verification/test_b1885_the_golden_state_on_the_whole_verified.py",
        "frontier/B1888_the_public_form_scrutinised/verification/candidate_chain.py",
        "frontier/B1888_the_public_form_scrutinised/verification/test_b1888_the_public_form_scrutinised.py",
        "frontier/B1890_the_first_enforcement_series_verified_and_landed/verification/test_b1890_the_first_enforcement_series_verified_and_landed.py",
        "frontier/B1861_the_closure_programme/verification/build_programme.py",
        "frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py",
    ]
    standing_tautologies: dict[str, list[dict[str, object]]] = {}
    for p in mended_code_paths:
        found = scan_non_failing_assertions_and_checks(git_show(PINNED_MAIN, p))
        standing_tautologies[p] = found
        assert found == [], f"Standing non-failing assertion/check found in {p}: {found}"

    # X1 & X2 (B1221)
    b1221_verdict = json.loads(git_show(PINNED_MAIN, "frontier/B1221_global_form_path_independence/arc_verdict.json"))
    b1221_findings = git_show(PINNED_MAIN, "frontier/B1221_global_form_path_independence/FINDINGS.md")
    b1221_test = git_show(PINNED_MAIN, "tests/test_b1221_the_adjoint_control.py")
    # Independent kernel count on Z_3 x Z_2 x (Z/N) for adjoint (0,0,0) vs faithful SM/27 charges (-2, 3) vs integer-only (-6, 9)
    adj_grid_counts = {N: sum(1 for a in range(3) for b in range(2) for c in range(N) if True) for N in (12, 24, 60)}
    twenty_seven_kernel = [
        (Frac(a, 3), Frac(b, 2), Frac(c, 12))
        for a in range(3) for b in range(2) for c in range(12)
        if (a - 2 * Frac(c, 12) * 3) % 1 == 0 and (Frac(a, 3) - 2 * Frac(c, 12)) % 1 == 0 and (Frac(b, 2) + 3 * Frac(c, 12)) % 1 == 0
    ]
    assert adj_grid_counts == {12: 72, 24: 144, 60: 360} and len(twenty_seven_kernel) == 6
    x1_ok = (
        "CORRECTED 2026-11-12" in b1221_verdict["claim_one_line"]
        and "72 is six times the twelve-point grid, 144 at 24 points and 360 at 60" in b1221_verdict["claim_one_line"]
        and "infinite" in b1221_verdict["claim_one_line"]
    )
    b1221_findings_flat = unquote_flat(b1221_findings)
    x2_ok = (
        "agy-002" not in b1221_findings
        and "agy-002" not in b1221_test
        and "recomputed on another family of model, harvest row 1709" in b1221_findings_flat
        and "harvest row 1709" in unquote_flat(b1221_test)
    )
    assert x1_ok and x2_ok

    # X3, X4, X5, X6 (B1641 + lock + tables)
    b1641_findings = git_show(PINNED_MAIN, "frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md")
    b1641_verdict = json.loads(git_show(PINNED_MAIN, "frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json"))
    b1641_test = git_show(PINNED_MAIN, "tests/test_b1641_w46_on_main_and_the_two_objects.py")
    law_map = git_show(PINNED_MAIN, "docs/LAW_MAP.md")
    thm_reg = git_show(PINNED_MAIN, "docs/THEOREM_REGISTRY.md")
    seat_higgs = json.loads(
        git_show(PINNED_MAIN, "frontier/B1796_the_cusp_unit_from_the_field_checked_on_main/verification/seat_the_higgs_route_exact.json")
    )
    vecs64 = list(itertools.product((-1, 0, 1, 2), repeat=3))
    table64 = seat_higgs["d at N = 3"]
    neg_sum_vecs = [v for v in vecs64 if sum(v) < 0]
    assert len(vecs64) == 64 == len(table64) and len(neg_sum_vecs) == 10
    assert all(table64[str(v)] == max(0, sum(v)) for v in vecs64)

    # Independent computation of rS, rT, turns(rT), classical M_k(SL2Z), and 3D Riemann-Roch chi3(k, m)
    # P23 swaps coords 2 & 3, so rT = exp(7i*pi/4) * diag(i, 1, 1) @ P23 has eigenvalues exp(7i*pi/4) * {i, 1, -1}
    eigs_rT = [cmath.exp(7j * math.pi / 4) * z for z in (1j, 1.0 + 0j, -1.0 + 0j)]
    turns_rT = sorted(((cmath.phase(e) / (2 * math.pi)) % 1.0) for e in eigs_rT)
    assert all(abs(x - y) < 1e-12 for x, y in zip(turns_rT, [1 / 8, 3 / 8, 7 / 8]))
    spacing_rT = min(turns_rT[1] - turns_rT[0], turns_rT[2] - turns_rT[1], 1.0 + turns_rT[0] - turns_rT[2])
    assert abs(spacing_rT - 0.25) < 1e-12

    # Matrix multiplication in pure Python for 3x3 rS and rT
    c_s = cmath.exp(-23j * math.pi / 4)
    c_t = cmath.exp(7j * math.pi / 4)
    rS_mat = [[0j, 0j, c_s], [0j, c_s, 0j], [c_s, 0j, 0j]]
    rT_mat = [[1j * c_t, 0j, 0j], [0j, 0j, c_t], [0j, c_t, 0j]]
    # Eigenvalues of P13 are {1, 1, -1}; eigenvalues of rS @ rT: trace & det -> exact characteristic roots
    eigs_rS = [c_s, c_s, -c_s]
    # Product M = rS @ rT: row0 = [0, c_s*c_t, 0], row1 = [0, 0, c_s*c_t], row2 = [1j*c_s*c_t, 0, 0]
    # M^3 = 1j * (c_s * c_t)^3 * I_3 = 1j * exp(-6j*pi)^3 ... compute cube roots directly:
    prod_scalar = 1j * (c_s * c_t) ** 3
    base_arg = cmath.phase(prod_scalar)
    eigs_rSrT = [cmath.rect(1.0, (base_arg + 2 * math.pi * j) / 3.0) for j in range(3)]

    def _turn(z: complex) -> float:
        b = (cmath.phase(z) / (2 * math.pi)) % 1.0
        return 0.0 if abs(b - 1.0) < 1e-9 or b > 1.0 - 1e-9 else b

    def chi3_indep(k: float, m: tuple[int, int, int] = (0, 0, 0)) -> float:
        s_term = sum(_turn(cmath.exp(1j * math.pi * k / 2.0) * ev) for ev in eigs_rS)
        st_term = sum(_turn(1.0 / (cmath.exp(1j * math.pi * k / 3.0) * ev)) for ev in eigs_rSrT)
        cusp_term = sum(x - y for x, y in zip(turns_rT, m))
        return 3.0 + 3.0 * k / 12.0 - s_term - st_term - cusp_term

    w50 = json.loads(git_show(PINNED_MAIN, "frontier/B1634_w50_on_main/verification/w50_on_main.json"))
    ch_w50 = w50["V4"]["allowed_weights_chi"]
    assert len(ch_w50) == 8
    for kk, val in ch_w50.items():
        assert abs(chi3_indep(float(kk)) - val) < 1e-9
    assert [round(chi3_indep(1.5, m)) for m in ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1))] == [0, 1, 1, 1, 3]

    b1641_findings_flat = unquote_flat(b1641_findings)
    x3_ok = (
        "max(0, m_P + m_M + m_N) on every vector computed" in b1641_findings_flat
        and "negative on ten of the 64 vectors" in b1641_findings_flat
        and "all(table[str(v)] == max(0, index(v)) for v in vecs)" in b1641_test
    )
    x4_ok = (
        "P-802" in b1641_verdict["claim_one_line"]
        and "three lines" in b1641_verdict["claim_one_line"]
        and "three lines" in " ".join(law_map.split())
        and "three lines" in " ".join(thm_reg.split())
    )
    x5_ok = "agy-002" not in b1641_findings and "harvest row 1709" in b1641_findings_flat and "harvest row 1709" in " ".join(b1641_test.split())
    x6_ok = (
        "len({1, 3, 7})" not in b1641_test
        and "classical.get(" not in b1641_test
        and "classical[k + 12]" in b1641_test
        and "def chi3(" in b1641_test
    )
    assert x3_ok and x4_ok and x5_ok and x6_ok

    # X7 & X8 (B1881)
    b1881_py = git_show(PINNED_MAIN, "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py")
    b1881_run = git_show(PINNED_MAIN, "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main_run.txt")
    b1881_test = git_show(PINNED_MAIN, "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py")
    gamma0_5_box = [
        (a, b, c, d)
        for a, b, c, d in itertools.product(range(-3, 4), repeat=4)
        if a * d - b * c == 1 and c % 5 == 0
    ]
    gamma0_5_c_nonzero = [g for g in gamma0_5_box if g[2] != 0]
    mirror_closed = all((a, -b, -c, d) in set(gamma0_5_box) for (a, b, c, d) in gamma0_5_box)
    assert len(gamma0_5_box) == 290 and len(gamma0_5_c_nonzero) == 240 and mirror_closed
    # Independent coset census on Z/5 vectors up to sign (12) and projective lines (6)
    vecs5 = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
    sign5 = lambda w: min(w, ((-w[0]) % 5, (-w[1]) % 5))
    line5 = lambda w: min(((w[0] * u) % 5, (w[1] * u) % 5) for u in range(1, 5))
    pts12 = sorted({sign5(w) for w in vecs5})
    pts6 = sorted({line5(w) for w in vecs5})
    S5, T5, ST5 = (0, 4, 1, 0), (1, 1, 0, 1), (0, 4, 1, 1)
    act5 = lambda g, w: ((w[0] * g[0] + w[1] * g[2]) % 5, (w[0] * g[1] + w[1] * g[3]) % 5)

    def _coset_census(points: list[tuple[int, int]], canon) -> tuple[list[int], int, int, Frac]:
        seen, widths = set(), []
        for p0 in points:
            if p0 in seen:
                continue
            n, q = 0, p0
            while True:
                seen.add(q)
                n += 1
                q = canon(act5(T5, q))
                if q == p0:
                    break
            widths.append(n)
        e2 = sum(1 for p0 in points if canon(act5(S5, p0)) == p0)
        e3 = sum(1 for p0 in points if canon(act5(ST5, p0)) == p0)
        genus = Frac(1) + Frac(len(points), 12) - Frac(e2, 4) - Frac(e3, 3) - Frac(len(widths), 2)
        return sorted(widths), e2, e3, genus

    assert _coset_census(pts12, sign5) == ([1, 1, 5, 5], 0, 0, Frac(0))
    assert _coset_census(pts6, line5) == ([1, 5], 2, 0, Frac(0))
    x7_ok = "290 matrices, 240 with lower-left entry non-zero" in b1881_run and "CHECKS: 65, FAILING: 0" in b1881_run
    x8_ok = "def census(points, canon):" in b1881_test and "Fraction(1, 2)" not in b1881_test and "Fr(1, 2)" not in b1881_test
    assert x7_ok and x8_ok

    # X9 & X10 (B1885)
    b1885_py = git_show(PINNED_MAIN, "frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main.py")
    b1885_run = git_show(PINNED_MAIN, "frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main_run.txt")
    b1885_json = json.loads(git_show(PINNED_MAIN, "frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main.json"))
    b1885_findings = git_show(PINNED_MAIN, "frontier/B1885_the_golden_state_on_the_whole_verified/FINDINGS.md")
    b1885_verdict = json.loads(git_show(PINNED_MAIN, "frontier/B1885_the_golden_state_on_the_whole_verified/arc_verdict.json"))
    b1885_test = git_show(PINNED_MAIN, "frontier/B1885_the_golden_state_on_the_whole_verified/verification/test_b1885_the_golden_state_on_the_whole_verified.py")
    b1885_bools = {k: v for k, v in b1885_json.items() if isinstance(v, bool)}
    assert len(b1885_bools) == 31
    # Independent check of reflection normalisers R1=(0,1,5,0) and R2=(5,-2,10,-5) on Gamma_0(5) generators
    gens_g05 = (((1, 1), (0, 1)), ((2, -1), (5, -2)), ((3, -2), (5, -3)), ((1, 0), (5, 1)), ((11, 2), (5, 1)))

    def _mul2(A, B):
        return (
            (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
        )

    def _norm_g05(a: int, b: int, c: int, d: int) -> bool:
        N = ((Frac(-a), Frac(b)), (Frac(-c), Frac(d)))
        det = N[0][0] * N[1][1] - N[0][1] * N[1][0]
        if det <= 0:
            return False
        Ninv = ((N[1][1] / det, -N[0][1] / det), (-N[1][0] / det, N[0][0] / det))
        for g in gens_g05:
            mir = ((Frac(g[0][0]), Frac(-g[0][1])), (Frac(-g[1][0]), Frac(g[1][1])))
            conj = _mul2(_mul2(N, mir), Ninv)
            if not (
                all(x.denominator == 1 for row in conj for x in row)
                and conj[0][0] * conj[1][1] - conj[0][1] * conj[1][0] == 1
                and int(conj[1][0]) % 5 == 0
            ):
                return False
        return True

    assert _norm_g05(0, 1, 5, 0) and _norm_g05(5, -2, 10, -5)
    assert not _norm_g05(0, 1, 3, 0) and not _norm_g05(2, -1, 5, -2)
    x9_ok = "else True" not in b1885_py and "a sine series vanishes term by term" in b1885_run
    x10_ok = (
        'if detail != "":' in b1885_py
        and "if forced:" in b1885_py
        and "CHECKS: 31, FAILING: 1" in b1885_run
        and "31 checks" in b1885_findings
        and "31 checks" in b1885_verdict["claim_one_line"]
        and "def carries_the_group_to_itself(" in b1885_test
    )
    assert x9_ok and x10_ok

    # X11 (B1888)
    b1888_findings = git_show(PINNED_MAIN, "frontier/B1888_the_public_form_scrutinised/FINDINGS.md")
    b1888_verdict = json.loads(git_show(PINNED_MAIN, "frontier/B1888_the_public_form_scrutinised/arc_verdict.json"))
    b1888_json = json.loads(git_show(PINNED_MAIN, "frontier/B1888_the_public_form_scrutinised/verification/candidate_chain.json"))
    b1888_test = git_show(PINNED_MAIN, "frontier/B1888_the_public_form_scrutinised/verification/test_b1888_the_public_form_scrutinised.py")
    b1888_findings_flat = " ".join(b1888_findings.split())
    x11_ok = (
        b1888_json["namers_in_tree"] == 51
        and "In the whole tree 51 do" in b1888_findings_flat
        and "in the whole tree, 51" in b1888_findings_flat
        and "51 scripts of the whole tree" in b1888_verdict["claim_one_line"]
        and 'RES["namers_in_tree"]' in b1888_test
    )
    assert x11_ok

    # X12 & X13 (B1890)
    b1890_findings = git_show(PINNED_MAIN, "frontier/B1890_the_first_enforcement_series_verified_and_landed/FINDINGS.md")
    b1890_findings_flat = unquote_flat(b1890_findings)
    b1890_verdict = json.loads(git_show(PINNED_MAIN, "frontier/B1890_the_first_enforcement_series_verified_and_landed/arc_verdict.json"))
    b1890_other = git_show(PINNED_MAIN, "frontier/B1890_the_first_enforcement_series_verified_and_landed/verification/other_checks_run.txt")
    b1890_test = git_show(PINNED_MAIN, "frontier/B1890_the_first_enforcement_series_verified_and_landed/verification/test_b1890_the_first_enforcement_series_verified_and_landed.py")
    x12_ok = "14 passed" in b1890_other and "14 passed" in b1890_test and "Review 79" in b1890_verdict["claim_one_line"]
    x13_ok = "run_unseen.py clock" in b1890_findings and "unseen_cases_run.json" in b1890_findings and "put together by hand" in b1890_findings_flat
    assert x12_ok and x13_ok

    # X14 (B874)
    b874_verdict = json.loads(git_show(PINNED_MAIN, "frontier/B874_measurement_ladder/arc_verdict.json"))
    x14_ok = (
        "CORRECTED 2026-11-12" in b874_verdict["claim_one_line"]
        and "{12, 14, 16, 18, 20, 26}" in b874_verdict["claim_one_line"]
        and "{12, 16, 18}" in b874_verdict["claim_one_line"]
    )
    assert x14_ok

    # X15 (B1861 + P-813)
    b1861_builder = git_show(PINNED_MAIN, "frontier/B1861_the_closure_programme/verification/build_programme.py")
    b1861_prog = git_show(PINNED_MAIN, "frontier/B1861_the_closure_programme/PROGRAMME.md")
    point_reg = git_show(PINNED_MAIN, "docs/POINT_REGISTER.md")
    x15_ok = (
        "def short(" in b1861_builder
        and "not for a v|" not in b1861_prog
        and "[…]" in b1861_prog
        and "| P-813 |" in point_reg
        and "B1858" in point_reg
    )
    assert x15_ok

    return {
        "mended_files_scanned_for_standing_tautologies": len(mended_code_paths),
        "standing_tautologies_found": 0,
        "resolved_count": 15,
        "still_open_count": 0,
        "items": {
            f"X{i}": "resolved" for i in range(1, 16)
        },
        "independent_checks": {
            "b1221_adjoint_grid_counts": adj_grid_counts,
            "b1221_twenty_seven_kernel_order": len(twenty_seven_kernel),
            "b1641_b1796_vectors_checked": len(vecs64),
            "b1641_negative_sum_vectors": len(neg_sum_vecs),
            "b1641_rT_turns": turns_rT,
            "b1641_chi3_allowed_weights_matched": 8,
            "b1881_gamma0_5_box_counts": [len(gamma0_5_box), len(gamma0_5_c_nonzero)],
            "b1881_coset_censuses": {"twin_12": [1, 1, 5, 5, 0, 0, 0], "line_6": [1, 5, 2, 0, 0]},
            "b1885_check_count": len(b1885_bools),
            "b1885_reflections_normalise_gamma0_5": True,
            "b1888_namers_in_tree": b1888_json["namers_in_tree"],
        },
    }


# ---------------------------------------------------------------------------
# 2. Task 2: Independent Reading & Verification of B1878, B1880, B1884 at 896cae025
# ---------------------------------------------------------------------------

def verify_b1878() -> dict[str, object]:
    findings = git_show(PINNED_MAIN, "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/FINDINGS.md")
    verdict = json.loads(git_show(PINNED_MAIN, "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/arc_verdict.json"))
    lock_src = git_show(PINNED_MAIN, "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/verification/test_b1878_the_goal_as_ruled.py")
    gov = git_show(PINNED_MAIN, "GOVERNANCE.md")
    gates_src = git_show(PINNED_MAIN, "scripts/gates/gates.py")

    lock_taut = scan_non_failing_assertions_and_checks(lock_src)
    assert lock_taut == []

    # Extract ARRIVAL_PHRASES tuple from scripts/gates/gates.py via AST without importing producer module
    gates_tree = ast.parse(gates_src)
    arrival_phrases: list[str] = []
    for node in gates_tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "ARRIVAL_PHRASES":
                    arrival_phrases = list(ast.literal_eval(node.value))
    assert len(arrival_phrases) == 16
    gov_joined = " ".join(gov.lower().split())
    phrases_in_gov = [p for p in arrival_phrases if p in gov_joined]
    assert phrases_in_gov == []

    # Check commit counts at B1878 landing commit 7480c2426^ (or 7480c2426)
    b1878_commit = git_cmd("log", "-1", "--format=%H", PINNED_MAIN, "--", "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/FINDINGS.md").strip()
    fp_count = int(git_cmd("rev-list", "--first-parent", "--count", b1878_commit).strip())
    after_da25 = int(git_cmd("rev-list", "--first-parent", "--count", f"da25c4f497adf5b137f95e5f5ee98d6513c159d9..{b1878_commit}").strip())

    # Check untravelled B1880 amendments on B1878/FINDINGS.md and B1878/arc_verdict.json
    b1878_mentions_b1880 = ("B1880" in findings) or ("B1880" in verdict["claim_one_line"]) or (verdict["superseded_by"] is not None)

    return {
        "lock_standing_tautologies": len(lock_taut),
        "arrival_phrases_count": len(arrival_phrases),
        "arrival_phrases_found_in_joined_governance": len(phrases_in_gov),
        "b1878_landing_commit": b1878_commit[:9],
        "first_parent_commits_at_landing": fp_count,
        "commits_after_da25c4f49_at_landing": after_da25,
        "b1880_gate_defects_noted_on_b1878": b1878_mentions_b1880,
    }


def verify_b1880() -> dict[str, object]:
    findings = git_show(PINNED_MAIN, "frontier/B1880_the_third_and_fourth_re_audits_answered/FINDINGS.md")
    verdict = json.loads(git_show(PINNED_MAIN, "frontier/B1880_the_third_and_fourth_re_audits_answered/arc_verdict.json"))
    measure_src = git_show(PINNED_MAIN, "frontier/B1880_the_third_and_fourth_re_audits_answered/verification/measure_all_hash_lists.py")
    read_a_src = git_show(PINNED_MAIN, "frontier/B1880_the_third_and_fourth_re_audits_answered/verification/read_class_a.py")
    lock_src = git_show(PINNED_MAIN, "frontier/B1880_the_third_and_fourth_re_audits_answered/verification/test_b1880_the_third_and_fourth_re_audits_answered.py")
    data = json.loads(git_show(PINNED_MAIN, "frontier/B1880_the_third_and_fourth_re_audits_answered/verification/all_hash_lists.json"))
    frozen_bytes = git_show_bytes(PINNED_MAIN, "scripts/gates/hash_lists_frozen.json")
    frozen_obj = json.loads(frozen_bytes.decode("utf-8"))

    lock_taut = scan_non_failing_assertions_and_checks(lock_src)
    assert lock_taut == []

    # Independently verify all 3 raw gzip hashes at 896cae025 (the lock itself recomputed only 1 of 3!)
    raw_entries = data["raw_hashes_checked_against_the_tracked_gzip"]
    assert len(raw_entries) == 3
    gzip_verified = []
    hex64_re = re.compile(r"\b([0-9a-f]{64})\b")
    for r in raw_entries:
        gz_bytes = git_show_bytes(PINNED_MAIN, r["tracked_gzip"])
        decomp_sha = hashlib.sha256(gzip.decompress(gz_bytes)).hexdigest()
        list_txt = git_show(PINNED_MAIN, r["list"])
        recorded_hashes = [
            m.group(1)
            for line in list_txt.splitlines()
            if r["names"] in line and (m := hex64_re.search(line))
        ]
        assert len(recorded_hashes) == 1 and decomp_sha == recorded_hashes[0]
        gzip_verified.append({"tracked_gzip": r["tracked_gzip"], "sha256_matches": True})

    # Verify frozen table key count (417) and SHA-256
    frozen_sha = hashlib.sha256(frozen_bytes).hexdigest()
    assert len(frozen_obj["frozen"]) == 417 and frozen_sha == data["frozen_table"]["sha256"]

    # Check A4 mend non-propagation to measure_all_hash_lists.py module docstring + read_class_a.py unconditional overwrite
    measure_doc = ast.get_docstring(ast.parse(measure_src)) or ""
    docstring_mentions_keep_outputs = "--keep-outputs" in measure_doc
    docstring_claims_write_in_folder = "write nothing outside this folder" in measure_doc and "writes the table" in measure_doc
    read_class_a_unconditional_write = '(HERE / "read_class_a_run.txt").write_text(' in read_a_src and "sys.argv" not in read_a_src
    lock_calls_read_class_a_main = '_load("read_class_a_b1880", HERE / "read_class_a.py").main()' in lock_src

    return {
        "lock_standing_tautologies": len(lock_taut),
        "all_three_tracked_gzips_independently_verified": len(gzip_verified),
        "frozen_table_keys": len(frozen_obj["frozen"]),
        "frozen_table_sha256_matches": True,
        "measure_docstring_mentions_keep_outputs": docstring_mentions_keep_outputs,
        "measure_docstring_claims_write_inside_folder": docstring_claims_write_in_folder,
        "read_class_a_unconditional_write_to_tracked_file": read_class_a_unconditional_write,
        "lock_calls_read_class_a_main_on_every_pytest_run": lock_calls_read_class_a_main,
        "verdict_corrected_354_vs_342": "all 354 are in the frozen table" in verdict["claim_one_line"],
        "findings_corrected_class_table": "counts all five classes" in findings,
    }


def verify_b1884() -> dict[str, object]:
    findings = git_show(PINNED_MAIN, "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md")
    verdict = json.loads(git_show(PINNED_MAIN, "frontier/B1884_what_level_a_ground_names_verified/arc_verdict.json"))
    script_src = git_show(PINNED_MAIN, "frontier/B1884_what_level_a_ground_names_verified/verification/ground_level_on_main.py")
    lock_src = git_show(PINNED_MAIN, "frontier/B1884_what_level_a_ground_names_verified/verification/test_b1884_what_level_a_ground_names_verified.py")
    res_json = json.loads(git_show(PINNED_MAIN, "frontier/B1884_what_level_a_ground_names_verified/verification/ground_level_on_main.json"))

    assert scan_non_failing_assertions_and_checks(script_src) == []
    assert scan_non_failing_assertions_and_checks(lock_src) == []

    # Independent pure-integer verification of all B1884 claims (G0..G4 + rho(N) to 1000 + root histories to 60)
    mul = lambda A, B: (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])
    det = lambda A: A[0] * A[3] - A[1] * A[2]
    row_act = lambda v, A, n: ((v[0] * A[0] + v[1] * A[2]) % n, (v[0] * A[1] + v[1] * A[3]) % n)

    I2, L, R, P = (1, 0, 0, 1), (1, 0, 1, 1), (1, 1, 0, 1), (0, 1, 1, 0)
    F = mul(L, P)
    Fp = mul(mul(P, F), P)
    LR, RL = mul(L, R), mul(R, L)
    assert F == (0, 1, 1, 1) and Fp == (1, 1, 1, 0) and mul(F, F) == LR == (1, 1, 1, 2) and mul(Fp, Fp) == RL == (2, 1, 1, 1)
    assert det(F) == det(Fp) == -1
    assert row_act((1, 3), LR, 5) == (4, 2) and row_act((1, 3), F, 5) == (3, 4)

    def prim_vecs(n: int) -> list[tuple[int, int]]:
        return [(a, b) for a in range(n) for b in range(n) if math.gcd(math.gcd(a, b), n) == 1]

    def kept_sign_count(g: tuple[int, int, int, int], n: int) -> int:
        return sum(1 for v in prim_vecs(n) if row_act(v, g, n) in (v, ((-v[0]) % n, (-v[1]) % n)))

    def inv_lines_count(g: tuple[int, int, int, int], n: int) -> int:
        units = [u for u in range(1, n) if math.gcd(u, n) == 1]
        seen: set[frozenset[tuple[int, int]]] = set()
        cnt = 0
        for v in prim_vecs(n):
            ln = frozenset(((u * v[0]) % n, (u * v[1]) % n) for u in units)
            if ln in seen:
                continue
            seen.add(ln)
            if row_act(v, g, n) in ln:
                cnt += 1
        return cnt

    rho = lambda n: sum(1 for x in range(n) if (x * x - x - 1) % n == 0)
    rho3 = lambda n: sum(1 for x in range(n) if (x * x - 3 * x + 1) % n == 0)

    for n in range(2, 201):
        assert kept_sign_count(F, n) == 0 and kept_sign_count(Fp, n) == 0
        assert kept_sign_count(LR, n) == (4 if n == 5 else 0)
        assert kept_sign_count(RL, n) == (4 if n == 5 else 0)
        rn = rho(n)
        assert rn == rho3(n)
        for g in (F, Fp, LR, RL):
            assert inv_lines_count(g, n) == rn

    rho_to_1000 = {n: rho(n) for n in range(2, 1001)}
    assert [n for n, c in rho_to_1000.items() if c == 1] == [5]
    assert max(rho_to_1000[n] for n in range(2, 201)) == 2
    first_gt2 = min(n for n, c in rho_to_1000.items() if c > 2)
    roots_209 = [x for x in range(209) if (x * x - x - 1) % 209 == 0]
    assert first_gt2 == 209 and rho_to_1000[209] == 4 and roots_209 == [15, 81, 129, 195]

    # Coprime factorisations in 2..200 (SM-30 check: 139 total vs 47 with parts <= 14)
    coprime_levels_all = {a * b for a in range(2, 101) for b in range(a + 1, 101) if math.gcd(a, b) == 1 and a * b <= 200}
    coprime_levels_14 = {a * b for a in range(2, 15) for b in range(a + 1, 15) if math.gcd(a, b) == 1 and a * b <= 200}
    assert len(coprime_levels_all) == 139 and len(coprime_levels_14) == 47
    assert all(rho(a * b) == rho(a) * rho(b) for a in range(2, 101) for b in range(a + 1, 101) if math.gcd(a, b) == 1 and a * b <= 200)

    # G4: 87 matrices of det -1 in {0..8}^4; unique trace-1 pair {F, Fp}
    mats_pm1 = [m for m in itertools.product(range(9), repeat=4) if det(m) in (1, -1)]
    mats_m1 = [m for m in mats_pm1 if det(m) == -1]
    assert (len(mats_pm1), len(mats_m1)) == (174, 87)
    assert sorted(m for m in mats_m1 if m[0] + m[3] == 1) == sorted([F, Fp])

    # Seven other root histories to N = 60
    want_root_table = {
        "L2R": ([2, 3, 6], [2, 3, 6]),
        "LR2": ([2, 3, 6], [2, 3, 6]),
        "L3R": ([3, 7, 21], [3, 7]),
        "LR3": ([3, 7, 21], [3, 7]),
        "L4R": ([2], [2, 4, 8]),
        "LR4": ([2], [2, 4, 8]),
        "L2R2": ([], [2, 4]),
    }
    for name, word in (("L2R", "LLR"), ("LR2", "LRR"), ("L3R", "LLLR"), ("LR3", "LRRR"), ("L4R", "LLLLR"), ("LR4", "LRRRR"), ("L2R2", "LLRR")):
        g = I2
        for ch in word:
            g = mul(g, L if ch == "L" else R)
        one_at = [n for n in range(2, 61) if inv_lines_count(g, n) == 1]
        vec_at = [n for n in range(2, 61) if kept_sign_count(g, n) > 0]
        assert (one_at, vec_at) == want_root_table[name]

    # Defects found in B1884 at 896cae025:
    # 1. A5 did not travel to B1884/arc_verdict.json: still says "two at 11, 19, 29 and on"
    verdict_still_says_two_and_on = "two at 11, 19, 29 and on" in verdict["claim_one_line"] and "209" not in verdict["claim_one_line"]
    # 2. SM-11 misattribution to B1872 corrected in B1881/FINDINGS.md did not travel to B1884 (nor to B1881/arc_verdict.json)
    b1872_run = git_show(PINNED_MAIN, "frontier/B1872_all_histories_together_the_exact_facts_verified/verification/together_facts_run.txt")
    b1872_uses_rows_1_3 = "((1, 1), (1, 2))" in b1872_run and "(1, 3)" in b1872_run
    b1884_misattributes_b1872 = "in B1872's convention** (columns, the ground [[2, 1], [1, 1]], the mark (1, 2))" in findings
    b1881_verdict = json.loads(git_show(PINNED_MAIN, "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json"))
    b1881_verdict_misattributes_b1872 = "the seat's convention and B1872's name one allowed set" in b1881_verdict["claim_one_line"] and "CORRECTED" not in b1881_verdict["claim_one_line"]
    # 3. SM-06 / SM-16 one-commit "expectations were written before the run" still stands in B1884/FINDINGS.md, and "is reproduced to N = 60" in section 2
    b1884_commits_before_review79 = git_cmd(
        "log", "--format=%h", f"{BASE_MAIN}", "--", "frontier/B1884_what_level_a_ground_names_verified"
    ).strip().splitlines()
    b1884_script_commits_before_review79 = git_cmd(
        "log", "--format=%h", f"{BASE_MAIN}", "--", "frontier/B1884_what_level_a_ground_names_verified/verification/ground_level_on_main.py"
    ).strip().splitlines()
    assert len(b1884_commits_before_review79) == 1 and b1884_commits_before_review79 == b1884_script_commits_before_review79

    return {
        "checks_in_json": sum(1 for v in res_json.values() if isinstance(v, bool)),
        "rho_unique_one_to_1000": [5],
        "rho_first_gt_two": [209, 4, roots_209],
        "coprime_levels_to_200": [len(coprime_levels_14), len(coprime_levels_all)],
        "det_minus_one_matrices_to_8": len(mats_m1),
        "root_histories_table_verified": True,
        "verdict_still_says_two_and_on": verdict_still_says_two_and_on,
        "b1872_uses_rows_1_3_not_columns": b1872_uses_rows_1_3,
        "b1884_misattributes_b1872_columns": b1884_misattributes_b1872,
        "b1881_verdict_still_says_b1872_convention": b1881_verdict_misattributes_b1872,
        "b1884_pre_review79_commits": b1884_commits_before_review79,
    }


# ---------------------------------------------------------------------------
# 3. Machine-quotation verification at 896cae025 for every reported finding
# ---------------------------------------------------------------------------

FINDING_QUOTATIONS_AT_896CAE025 = [
    (
        "RF-01",
        "B1884",
        "frontier/B1884_what_level_a_ground_names_verified/arc_verdict.json",
        "the lines kept as sets by the tick and by its square are as many as the roots of x^2 - x - 1 modulo N -- exactly one at N = 5 and at no other N to 200, two at 11, 19, 29 and on -- so 'a canonical invariant' selects 5 only when it means the only invariant line;",
    ),
    (
        "RF-02",
        "B1884",
        "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md",
        "- **The same counts in B1872's convention** (columns, the ground [[2, 1], [1, 1]], the mark (1, 2)): the ground keeps",
    ),
    (
        "RF-03",
        "B1881",
        "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json",
        "the seat's convention and B1872's name one allowed set (47,988 run sequences, no exception);",
    ),
    (
        "RF-04",
        "B1884",
        "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md",
        "- **The expectations were written before the run,** in the script's header. All held; none was a surprise, since the",
    ),
    (
        "RF-05",
        "B1884",
        "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md",
        "**The seat's table of the seven other root histories** (reported there, not predicted) is reproduced to N = 60:",
    ),
    (
        "RF-06",
        "B1880",
        "frontier/B1880_the_third_and_fourth_re_audits_answered/verification/measure_all_hash_lists.py",
        "    python3 -B measure_all_hash_lists.py            # measure, print, write nothing outside this folder",
    ),
    (
        "RF-07",
        "B1880",
        "frontier/B1880_the_third_and_fourth_re_audits_answered/verification/read_class_a.py",
        '    (HERE / "read_class_a_run.txt").write_text("\\n".join(out) + "\\n", encoding="utf-8")',
    ),
    (
        "RF-08",
        "B1878",
        "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/FINDINGS.md",
        "- A denial, a condition or a statement of aim within the 64 characters before the phrase is not arrival. \"No value of\n  the Standard Model is derived\" is the record's own sentence and passes.\n- Three old lines are frozen, and the count may only shrink: a plan of 2026-07-24, a dated state page, and the",
    ),
]


def verify_all_finding_quotations() -> dict[str, object]:
    results = {}
    for fid, arc, path, quote in FINDING_QUOTATIONS_AT_896CAE025:
        res = quote_present_at_commit(PINNED_MAIN, path, quote)
        assert res["exact_substring"] and res["whitespace_joined"], f"Quotation check failed for {fid} ({arc}, {path}): {res}"
        results[fid] = {"arc": arc, "file": path, **res}
    return {
        "total_quotations_checked": len(FINDING_QUOTATIONS_AT_896CAE025),
        "exact_matches": sum(1 for v in results.values() if v["exact_substring"]),
        "whitespace_joined_matches": sum(1 for v in results.values() if v["whitespace_joined"]),
        "quotations": results,
    }


def main() -> None:
    controls = run_precommitted_controls()
    task1 = verify_task1_x1_to_x15()
    b1878 = verify_b1878()
    b1880 = verify_b1880()
    b1884 = verify_b1884()
    quotes = verify_all_finding_quotations()

    payload = {
        "card": "X-R79b",
        "pinned_main_commit": PINNED_MAIN,
        "mend_diff_base_commit": BASE_MAIN,
        "b1887_excluded_conflict_of_interest": True,
        "firewall": "0 of 19",
        "controls": controls,
        "task1_x1_to_x15": task1,
        "task2_arcs": {
            "B1878": b1878,
            "B1880": b1880,
            "B1884": b1884,
            "B1887": "unread_per_section_13_and_section_9_item_2",
        },
        "machine_quotation_verification": quotes,
    }
    out_path = HERE / "verify_x_r79b_out.json"
    out_text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    out_path.write_text(out_text, encoding="utf-8")
    digest = hashlib.sha256(out_text.encode("utf-8")).hexdigest()
    (HERE / "OUTPUT_SHA256.txt").write_text(f"{digest}  verify_x_r79b_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
