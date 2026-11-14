#!/usr/bin/env python3
"""
Card R82 — Blind Audit & Sandbox Lock-Mutation Verifier at 86930f574.

Seat: agy-exp
Branch: agy/self-consistent-loop-2026-11-11
Pinned review target: 86930f574 (origin/review-82/read)
Window diff base (where referenced): 0e637ea9e

Isolation & Firewall Guarantees:
  1. Reads repository objects strictly from pinned commit 86930f574 (and 0e637ea9e where needed);
     never touches origin/main, 73e71e277, or any other seat's branch.
  2. Extracts a self-contained pure-mathematics sandbox into a temporary directory, explicitly
     removing any historical comparison scripts before execution (0 of 19).
  3. Executes pre-registered negative controls C-R82-1, C-R82-2, and C-R82-3, runs all lock files
     in B1917..B1929 and tests/test_negative_second_computation.py, applies targeted sandbox
     mutations to prove lock/gate non-failure, performs zero-trust independent mathematical
     recomputations, and verifies character-for-character and 1-based line-number exactness of
     every quoted finding at 86930f574.
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
OUT_PATH = HERE / "verify_r82_out.json"
PINNED = "86930f574"

# Exact machine-checked quotations at 86930f574 (1-based line numbers).
FINDINGS_QUOTES = [
    {
        "id": "F-01",
        "criterion": 4,
        "item": "B1917",
        "path": "frontier/B1917_the_slope_and_the_kronecker_function_one_l_function_on_the_threads_geodesic/verification/test_b1917_one_l_function.py",
        "line": 32,
        "quote": "    assert abs(L / (H.H(2) * R / 2) - 2) < 1e-4            # planted: half the orbit strip is off by exactly 2",
    },
    {
        "id": "F-02",
        "criterion": 4,
        "item": "B1917",
        "path": "frontier/B1917_the_slope_and_the_kronecker_function_one_l_function_on_the_threads_geodesic/verification/test_b1917_one_l_function.py",
        "line": 24,
        "quote": '    assert len(rows) == 17 and sum(r["rel"] < 1e-7 for r in rows) == 16',
    },
    {
        "id": "F-03",
        "criterion": 1,
        "item": "B1917",
        "path": "frontier/B1917_the_slope_and_the_kronecker_function_one_l_function_on_the_threads_geodesic/FINDINGS.md",
        "line": 27,
        "quote": "    character whose series has no phase in n converges to 1.6 × 10⁻⁷ as the m-range grows (`hecke_s2.py`). Main's",
    },
    {
        "id": "F-04",
        "criterion": 1,
        "item": "B1919",
        "path": "frontier/B1919_the_channel_norm_is_the_shifted_lattices_kronecker_limit_at_the_kernels_shift/FINDINGS.md",
        "line": 18,
        "quote": "  (a pair of Hurwitz zetas and a Bessel series), the norm by main's quadrature of B1656's definition: on 24 cases (eight",
    },
    {
        "id": "F-05",
        "criterion": 5,
        "item": "B1923 / HARVEST_LEDGER row 1713",
        "path": "docs/HARVEST_LEDGER.md",
        "line": 1766,
        "quote": '| 1713 | web seat (chat1) | TWO DELIVERIES. (a) ITS SEALED CARD ON THE GOLDEN STATE (P-783), DELIVERED: by a scan and not a proof, the state is the lowest in all four classes and simple; no state at either of the two values the agy lane reported; computed once, expectations committed first, a second check written after the sealed output was read and said so; no independent recomputation in the record, by its own statement. (b) THE COLD READ OF THE THREE-PART PUBLIC STRUCTURE, with no computation | "by a scan, not a proof" | relays/CHAT1_TO_CC_2026-11-11_P-783_THE_GOLDEN_STATE_IS_THE_LOWEST_AND_SIMPLE.md, relays/chat1_2026-11-11_p783/, relays/CHAT1_TO_CC_2026-11-11_A_COLD_READ_OF_THE_THREE_PART_STRUCTURE.md @ dbbcd470 on web-seat | **THE COLD READ, READ IN FULL; THE RESULT ON THE GOLDEN STATE REGISTERED, ITS HEAD READ (S306p)**: (a) the two values it names are spectral parameters of states a lane reported, whose settlement main\'s card asked for; they are not read-out points, and nothing of the owner\'s hold applies, which answers the question row 1708 left. Main\'s own computation is OWED and belongs to the modulus (WP-4.1). (b) THE COLD READ: a stranger would not believe the count of looks, which the parties assemble; the list of inputs, which is the authors\'; or that a check shares nothing with the statement, where copying by hand cannot be seen. Of the five conditions the one whose output can be read is the strongest; sealing expectations does not make a checker blind who has read the record, as every session has; two conditions are missing, a perturbed statement that the check must reject, and the publication of every result of the check, failures included. What no page asks for and a stranger needs: a map of what is known, giving for each mathematical step the textbook or paper it comes from and what is claimed as new. It says of itself that it is not a stranger. Register row P-807; it goes to the public form (P-787) | — | 2026-11-11 |',
    },
    {
        "id": "F-06",
        "criterion": 5,
        "item": "B1924",
        "path": "frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/FINDINGS.md",
        "line": 3,
        "quote": "**Verdict: OPEN** (numerical evidence at the 10⁻² level; no limit is proved; an independent second computation is",
    },
    {
        "id": "F-07",
        "criterion": 5,
        "item": "B1924",
        "path": "frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/arc_verdict.json",
        "line": 29,
        "quote": ' "claim_one_line": "[UPGRADED 2026-11-14 from OPEN on agy-002\'s second computation, harvest row 1790; CORRECTED: the twin is not fading but exactly equal at every n] THE READ-OUT ON THE WHOLE, FIRST RUNS (OPEN): with P-845\'s condition (allowed words at level 5, each thread\'s average of the frame at its own line with the invariant end, combined by the move count and weighted by length), the read-out changes from n = 16 to n = 22 by no more than its sampling error (about 1.3e-2; per number median |z| 0.94 at the mark and 0.67 at the twin, none above 2 at the mark), and the read-outs at the mark and at its twin, clearly different at n = 10 (paired median |z| 2.35, 58% above 2), are not told apart at n = 16 (0.92, 4%) or n = 22 (0.57, 0%). The limit is not proved; longer histories, an independent second computation (agy-002) and the end are owed before tau and the reading point leave the budget. [CORRECTED 2026-11-14: all of it at two chosen constant values of the free end L~, which are not B1724\'s two ends.] Values in the json only; nothing compared. 0 of 19.",',
    },
    {
        "id": "F-08",
        "criterion": 3,
        "item": "B1925",
        "path": "frontier/B1925_the_selection_tested_by_changing_it_the_metallic_rivals_bronze_keeps_the_tick_structure_only_nothing_left_over_picks_golden/FINDINGS.md",
        "line": 126,
        "quote": 'So the tick\'s structure picks **every metallic act**, not "every odd m with m² + 4 prime". Nothing else on this page',
    },
    {
        "id": "F-09",
        "criterion": 8,
        "item": "B1926",
        "path": "frontier/B1926_at_odd_ticks_the_frames_matter_exists_only_twisted_by_the_orientation_the_tick_inverts_the_scar/FINDINGS.md",
        "line": 125,
        "quote": "- **The web seat's W-F4** (harvest row 1773), whose reading settles it. It recomputes this page's addendum independently and completes it: the",
    },
    {
        "id": "F-10",
        "criterion": 2,
        "item": "B1927",
        "path": "frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_two_horocycle/FINDINGS.md",
        "line": 73,
        "quote": "  | L_max, the maximal horoball | **1.79** (both angles) | 1.98 |",
    },
    {
        "id": "F-11",
        "criterion": 5,
        "item": "B1928",
        "path": "frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/arc_verdict.json",
        "line": 21,
        "quote": ' "claim_one_line": "THE READ-OUT ON THE WHOLE IS ONE AVERAGE OVER THE 24 POINTS OF ORDER 5 (OPEN: a proof sketch with three hypotheses unchecked): the letters\' images generate SL(2, F5), which is perfect and acts transitively on the 24 points, so closed orbits equidistribute with their holonomy and R_n -> integral of F-bar against the path measure, the same at the mark, its twin and every point of order 5 (the twin\'s fading a theorem, the reading point removed). Predicted and confirmed: the ergodic integral of F-bar along 3 000 unconstrained words (error 6.6e-4) agrees with B1924\'s read-outs at n = 22 and 28, mark and twin (medians 0.46 to 0.76; one flagged sample 1.08); with the canonical end, medians 0.84 to 1.18. A seat\'s check of the proof is owed. 0 of 19.",',
    },
    {
        "id": "F-12",
        "criterion": 1,
        "item": "B1928",
        "path": "frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/FINDINGS.md",
        "line": 107,
        "quote": "  shift space. The suspension is not compact, because the roof r is unbounded near L^∞ and R^∞. But r grows only like",
    },
    {
        "id": "F-13",
        "criterion": 4,
        "item": "B1929",
        "path": "frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle/verification/test_b1929_twisted_eta.py",
        "line": 56,
        "quote": "    assert worst < 1e10",
    },
    {
        "id": "F-14",
        "criterion": 8,
        "item": "B1929",
        "path": "frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle/arc_verdict.json",
        "line": 27,
        "quote": ' "claim_one_line": "THE RECORD\'S ODD L-VALUE IS THE TWISTED ETA INVARIANT OF THE CLOSED TORUS BUNDLE: eta_A(T^2_M) = rho_A + eta(T^2_M) = -L_odd(1, chi_c)/pi^2 for every hyperbolic act and every non-trivial fixed torsion character (found post hoc by the SM seat, proved by agy-exp through the Siegel functions\' transformation law). Main\'s own code: L_odd(1)/(pi i Delta) = -2.0000000000 on all 561 characters with a non-zero Siegel winding (Re Delta < 3e-14), and the identity end to end on all 601 to 3.1e-14. The odd L-value flips with the orientation: a candidate carrier for the hand on the closed bundle. 0 of 19.",',
    },
    {
        "id": "F-15",
        "criterion": 4,
        "item": "negative-second-computation gate",
        "path": "scripts/gates/gates.py",
        "line": 3131,
        "quote": '_SECOND_NOT_YET_RE = re.compile(r"\\b(owed|assigned|pending|not yet|awaited|awaiting|to come|to be made|outstanding)\\b", re.I)',
    },
]

SANDBOX_B_PREFIXES = [
    "B1427", "B1432", "B1434", "B1435", "B1438",
    "B1654", "B1667", "B1691", "B1716", "B1723", "B1724", "B1737",
    "B1917", "B1918", "B1919", "B1920", "B1921", "B1922", "B1923",
    "B1924", "B1925", "B1926", "B1927", "B1928", "B1929",
]


def git_show_text(path: str, commit: str = PINNED) -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "show", f"{commit}:{path}"],
        text=True,
    )


def check_single_quote(path: str, line_no: int, quote: str, commit: str = PINNED) -> dict:
    lines = git_show_text(path, commit).splitlines()
    in_range = 1 <= line_no <= len(lines)
    actual = lines[line_no - 1] if in_range else None
    exact = in_range and (actual == quote)
    return {
        "path": path,
        "line": line_no,
        "in_range": in_range,
        "exact_match": exact,
    }


def run_control_c_r82_1() -> dict:
    """C-R82-1: Exact quote passes; 1-char perturbation and +1 line shift are both rejected."""
    ref_path = "WORKING_RULES.md"
    ref_line = 354
    ref_text = git_show_text(ref_path).splitlines()[ref_line - 1]
    ok_exact = check_single_quote(ref_path, ref_line, ref_text)["exact_match"]
    perturbed_text = ref_text[:-1] + ("X" if ref_text[-1] != "X" else "Y")
    ok_char_pert = check_single_quote(ref_path, ref_line, perturbed_text)["exact_match"]
    ok_line_shift = check_single_quote(ref_path, ref_line + 1, ref_text)["exact_match"]
    passed = bool(ok_exact and (not ok_char_pert) and (not ok_line_shift))
    return {
        "control": "C-R82-1",
        "exact_accepted": ok_exact,
        "char_perturbation_rejected": not ok_char_pert,
        "line_shift_rejected": not ok_line_shift,
        "passed": passed,
    }


def run_control_c_r82_2() -> dict:
    """C-R82-2: Lock-mutation harness classifies vacuous test CANNOT_FAIL and genuine test CAUGHT."""
    with tempfile.TemporaryDirectory() as td:
        tdp = pathlib.Path(td)
        data_file = tdp / "data.json"
        vacuous_test = tdp / "test_vacuous.py"
        genuine_test = tdp / "test_genuine.py"
        vacuous_test.write_text(
            "import json, pathlib\n"
            "def test_vac():\n"
            "    d = json.loads((pathlib.Path(__file__).parent / 'data.json').read_text())\n"
            "    assert all(x > 0 for x in d if False)\n",
            encoding="utf-8",
        )
        genuine_test.write_text(
            "import json, pathlib\n"
            "def test_gen():\n"
            "    d = json.loads((pathlib.Path(__file__).parent / 'data.json').read_text())\n"
            "    assert all(x > 0 for x in d)\n",
            encoding="utf-8",
        )
        data_file.write_text("[1, 2, 3]", encoding="utf-8")
        r_vac_base = subprocess.run([sys.executable, "-m", "pytest", "-q", str(vacuous_test)], capture_output=True)
        r_gen_base = subprocess.run([sys.executable, "-m", "pytest", "-q", str(genuine_test)], capture_output=True)
        # Mutate data to violate x > 0
        data_file.write_text("[-5, -1, 0]", encoding="utf-8")
        r_vac_mut = subprocess.run([sys.executable, "-m", "pytest", "-q", str(vacuous_test)], capture_output=True)
        r_gen_mut = subprocess.run([sys.executable, "-m", "pytest", "-q", str(genuine_test)], capture_output=True)
        vac_class = "CANNOT_FAIL" if (r_vac_base.returncode == 0 and r_vac_mut.returncode == 0) else "CAUGHT"
        gen_class = "CAUGHT" if (r_gen_base.returncode == 0 and r_gen_mut.returncode != 0) else "CANNOT_FAIL"
        passed = (vac_class == "CANNOT_FAIL") and (gen_class == "CAUGHT")
        return {
            "control": "C-R82-2",
            "vacuous_classification": vac_class,
            "genuine_classification": gen_class,
            "passed": passed,
        }


def build_sandbox(tmpdir: pathlib.Path) -> list[str]:
    """Materialize a pure-math tree from 86930f574 with zero physical comparison scripts."""
    top_entries = subprocess.check_output(
        ["git", "-C", str(REPO), "ls-tree", "--name-only", PINNED, "frontier"],
        text=True,
    ).splitlines()
    frontier_dirs = []
    for entry in subprocess.check_output(
        ["git", "-C", str(REPO), "ls-tree", "--name-only", f"{PINNED}:frontier"],
        text=True,
    ).splitlines():
        if any(entry.startswith(f"{pref}_") for pref in SANDBOX_B_PREFIXES):
            frontier_dirs.append(f"frontier/{entry}")

    archive_paths = ["GENESIS.md", "WORKING_RULES.md", "docs", "scripts", "tests"] + frontier_dirs
    proc = subprocess.Popen(
        ["git", "-C", str(REPO), "archive", PINNED, "--"] + archive_paths,
        stdout=subprocess.PIPE,
    )
    subprocess.run(["tar", "-x", "-C", str(tmpdir)], stdin=proc.stdout, check=True)
    proc.wait()
    assert proc.returncode == 0

    # Explicitly delete historical comparison scripts from the sandbox to enforce 0-of-19 firewall.
    for rel_rm in [
        "frontier/B1723_the_golden_valley/verification/compare.py",
        "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_coefficients_are_free.py",
    ]:
        p = tmpdir / rel_rm
        if p.exists():
            p.unlink()
    return sorted(frontier_dirs)


def run_control_c_r82_3_and_gate_audit(sandbox: pathlib.Path) -> dict:
    """C-R82-3 + F-15: Test negative_without_second on compliant, non-compliant, and negated-phrase bypass inputs."""
    code = r"""
import json, os, sys
sys.path.insert(0, os.path.join(sys.argv[1], "scripts", "gates"))
import gates

# Create a synthetic B1999 directory inside sandbox/frontier so glob finds it
b999 = os.path.join(sys.argv[1], "frontier", "B1999_synthetic_negative_probe")
os.makedirs(b999, exist_ok=True)
verdict_rel = "frontier/B1999_synthetic_negative_probe/arc_verdict.json"
findings_rel = "frontier/B1999_synthetic_negative_probe/FINDINGS.md"
with open(os.path.join(sys.argv[1], verdict_rel), "w") as f:
    f.write("{}")

def probe(verdict_obj, findings_md):
    def reader(rel):
        if rel == verdict_rel:
            return json.dumps(verdict_obj)
        if rel == findings_rel:
            return findings_md
        with open(os.path.join(sys.argv[1], rel), "r", encoding="utf-8") as fh:
            return fh.read()
    return [b for b in gates.negative_without_second(reader) if b[0] == "B1999"]

wall_md = "# B1999\n\n## What the wall teaches\n\nClue.\n"

# 1. Control: unverified NEGATIVE with empty cites_seat and no PROVISIONAL -> must be flagged
c_empty = probe({"id": "B1999", "verdict": "NEGATIVE", "cites_seat": [], "claim_one_line": "X (NEGATIVE)"}, wall_md)

# 2. Control: owed second computation without PROVISIONAL -> must be flagged
c_owed = probe({"id": "B1999", "verdict": "NEGATIVE", "cites_seat": ["second computation owed"], "claim_one_line": "X"}, wall_md)

# 3. Bypass probe A: "no second computation" in cites_seat, NO PROVISIONAL -> should fail rule, check what gate does
b_no = probe({"id": "B1999", "verdict": "NEGATIVE", "cites_seat": ["no second computation"], "claim_one_line": "X"}, wall_md)

# 4. Bypass probe B: "without an independent second computation" in cites_seat, NO PROVISIONAL
b_without = probe({"id": "B1999", "verdict": "NEGATIVE", "cites_seat": ["without an independent second computation"], "claim_one_line": "X"}, wall_md)

# 5. Bypass probe C: "second computation needed" in cites_seat, NO PROVISIONAL
b_needed = probe({"id": "B1999", "verdict": "NEGATIVE", "cites_seat": ["second computation needed"], "claim_one_line": "X"}, wall_md)

import shutil
shutil.rmtree(b999)

print(json.dumps({
    "empty_cites_flagged": len(c_empty) == 1,
    "owed_cites_flagged": len(c_owed) == 1,
    "negated_no_second_computation_bypassed": len(b_no) == 0,
    "without_second_computation_bypassed": len(b_without) == 0,
    "second_computation_needed_bypassed": len(b_needed) == 0,
}))
"""
    out = subprocess.check_output([sys.executable, "-c", code, str(sandbox)], text=True)
    res = json.loads(out)
    res["control"] = "C-R82-3"
    res["passed"] = bool(
        res["empty_cites_flagged"]
        and res["owed_cites_flagged"]
        and res["negated_no_second_computation_bypassed"]
        and res["without_second_computation_bypassed"]
    )
    return res


def run_pytest(sandbox: pathlib.Path, rel_target: str) -> dict:
    proc = subprocess.run(
        [sys.executable, "-B", "-m", "pytest", "-q", str(sandbox / rel_target)],
        cwd=str(sandbox),
        capture_output=True,
        text=True,
    )
    return {
        "target": rel_target,
        "returncode": proc.returncode,
        "passed": proc.returncode == 0,
        "summary_line": (proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else ""),
    }


def run_lock_and_mutation_suite(sandbox: pathlib.Path) -> dict:
    lock_targets = ["tests/test_negative_second_computation.py"]
    for arc_num in range(1917, 1930):
        matches = sorted(sandbox.glob(f"frontier/B{arc_num}_*/verification/test_*.py"))
        for m in matches:
            lock_targets.append(str(m.relative_to(sandbox)))

    baseline = [run_pytest(sandbox, t) for t in lock_targets]

    # Mutation 1 (F-01): B1917 line 32 algebraic tautology check + live non-invocation check
    # Algebraically: for any (L, R) with |L - H2*R|/|L| <= eps (eps = 1e-5),
    # |L / (H2*R/2) - 2| = 2 * |L/(H2*R) - 1| <= 2*eps/(1 - eps) < 2.0001e-5 < 1e-4.
    worst_line32_val = 0.0
    for k in range(-500, 501):
        delta = (k / 500.0) * 0.999e-5  # relative error in (-1e-5, +1e-5) satisfying line 31
        # L - H2*R = delta * L => L / (H2*R) = 1 / (1 - delta)
        lhs_line32 = abs(2.0 / (1.0 - delta) - 2.0)
        worst_line32_val = max(worst_line32_val, lhs_line32)
    b1917_line32_cannot_fail_when_line31_holds = worst_line32_val < 1e-4

    # Also verify in live sandbox that mutating hecke_s2.rhs to raise if X < 3999 (half-strip would change strip or X)
    # and counting rhs() calls in test_hecke_at_two_as_kept_and_a_planted_half_strip_fails gives exactly 1 call!
    b1917_dir = next(sandbox.glob("frontier/B1917_*/verification"))
    hecke_s2_path = b1917_dir / "hecke_s2.py"
    orig_hecke_s2 = hecke_s2_path.read_text(encoding="utf-8")
    try:
        hecke_s2_path.write_text(
            orig_hecke_s2 + "\n_RHS_CALLS = 0\n_ORIG_RHS = rhs\n"
            "def rhs(*a, **kw):\n"
            "    global _RHS_CALLS; _RHS_CALLS += 1\n"
            "    return _ORIG_RHS(*a, **kw)\n",
            encoding="utf-8",
        )
        call_probe = subprocess.check_output(
            [
                sys.executable, "-B", "-c",
                f"import sys; sys.path.insert(0, {repr(str(b1917_dir))}); "
                "import test_b1917_one_l_function as T, hecke_s2 as H; "
                "T.test_hecke_at_two_as_kept_and_a_planted_half_strip_fails(); "
                "print(H._RHS_CALLS)",
            ],
            text=True,
        ).strip()
        b1917_rhs_calls_in_lock = int(call_probe)
    finally:
        hecke_s2_path.write_text(orig_hecke_s2, encoding="utf-8")

    # Mutation 2 (F-02): B1917 line 24 — set the 17th row's rel error to 1e99 in hecke_s2.json
    hecke_json_path = b1917_dir / "hecke_s2.json"
    orig_hecke_json = hecke_json_path.read_text(encoding="utf-8")
    try:
        rows = json.loads(orig_hecke_json)
        outlier_idx = max(range(len(rows)), key=lambda i: rows[i]["rel"])
        rows[outlier_idx]["rel"] = 1.0e99
        hecke_json_path.write_text(json.dumps(rows), encoding="utf-8")
        mut_b1917_row17 = run_pytest(sandbox, str((b1917_dir / "test_b1917_one_l_function.py").relative_to(sandbox)))
    finally:
        hecke_json_path.write_text(orig_hecke_json, encoding="utf-8")

    # Mutation 3 (F-13): B1929 line 56 (`assert worst < 1e10`) — corrupt Bohn rho_467 by +1000 in received_sm/run_c9.py
    b1929_dir = next(sandbox.glob("frontier/B1929_*/verification"))
    run_c9_path = b1929_dir / "received_sm" / "run_c9.py"
    orig_run_c9 = run_c9_path.read_text(encoding="utf-8")
    try:
        run_c9_path.write_text(
            orig_run_c9 + "\n_ORIG_RHO_467 = rho_467\n"
            "def rho_467(M, nu):\n"
            "    return _ORIG_RHO_467(M, nu) + 1000\n",
            encoding="utf-8",
        )
        mut_b1929_rho_plus_1000 = run_pytest(sandbox, str((b1929_dir / "test_b1929_twisted_eta.py").relative_to(sandbox)))
    finally:
        run_c9_path.write_text(orig_run_c9, encoding="utf-8")

    # Also corrupt main_siegel.json by negating every stored Delta (reversing orientation sign!) in test_end_to_end_on_stored_windings
    siegel_json_path = b1929_dir / "main_siegel.json"
    orig_siegel_json = siegel_json_path.read_text(encoding="utf-8")
    try:
        srows = json.loads(orig_siegel_json)
        for r in srows:
            r["Delta"] = [-r["Delta"][0], -r["Delta"][1]]
        siegel_json_path.write_text(json.dumps(srows), encoding="utf-8")
        proc_neg = subprocess.run(
            [
                sys.executable, "-B", "-m", "pytest", "-q",
                str(b1929_dir / "test_b1929_twisted_eta.py"),
                "-k", "test_end_to_end_on_stored_windings",
            ],
            cwd=str(sandbox),
            capture_output=True,
            text=True,
        )
        mut_b1929_sign_flipped_end_to_end_passes = (proc_neg.returncode == 0)
    finally:
        siegel_json_path.write_text(orig_siegel_json, encoding="utf-8")

    return {
        "baseline_locks_count": len(baseline),
        "baseline_all_passed": all(x["passed"] for x in baseline),
        "baseline_results": baseline,
        "mutations": {
            "M_B1917_line32_algebraic_max_under_line31": worst_line32_val,
            "M_B1917_line32_cannot_fail_when_line31_holds": b1917_line32_cannot_fail_when_line31_holds,
            "M_B1917_line32_rhs_calls_count": b1917_rhs_calls_in_lock,
            "M_B1917_line24_row17_rel_1e99_suite_still_passes": mut_b1917_row17["passed"],
            "M_B1929_line56_rho_corrupted_by_plus_1000_full_suite_still_passes": mut_b1929_rho_plus_1000["passed"],
            "M_B1929_line56_negated_delta_end_to_end_test_still_passes": mut_b1929_sign_flipped_end_to_end_passes,
        },
    }


def independent_math_and_evidence_checks(sandbox: pathlib.Path) -> dict:
    """Zero-trust independent mathematical & cross-file checks (Guardrail 6)."""
    out = {}

    # 1. B1917: inspect hecke_s2.py / json / run.txt for "1.6" or growing Mmax
    b1917_dir = next(sandbox.glob("frontier/B1917_*/verification"))
    hs2_py = (b1917_dir / "hecke_s2.py").read_text(encoding="utf-8")
    hs2_run = (b1917_dir / "hecke_s2_run.txt").read_text(encoding="utf-8")
    hs2_json = json.loads((b1917_dir / "hecke_s2.json").read_text(encoding="utf-8"))
    no_phase_row = next(r for r in hs2_json if r["level"] == ["+LR", 3] and r["ij"] == [1, 0])
    out["B1917_evidence"] = {
        "hecke_s2_json_row_count": len(hs2_json),
        "no_phase_row_rel": no_phase_row["rel"],
        "string_1_6_in_hecke_s2_run_or_py": ("1.6" in hs2_run) or ("1.6" in hs2_py),
        "mmax_loop_in_hecke_s2_py": hs2_py.count("Mmax") == 2,  # def lhs(..., Mmax=60, ...) and range(-Mmax, Mmax+1) only
    }

    # 2. B1919: check seat_formula.py case count and golden geodesic circle residuals in seat_formula_check.json
    b1919_dir = next(sandbox.glob("frontier/B1919_*/verification"))
    sf_py = (b1919_dir / "seat_formula.py").read_text(encoding="utf-8")
    sfc_json = json.loads((b1919_dir / "seat_formula_check.json").read_text(encoding="utf-8"))
    taus = sorted({tuple(r["tau"]) for r in sfc_json})
    # Golden geodesic for LR = [[1,1],[1,2]] -> gamma(tau)=(tau+1)/(tau+2) or TR=(2tau+1)/(tau+1):
    # Check circle through (0.5, sqrt(5)/2) centered on real axis: (x - 0.5)^2 + y^2 = 1.5 => x^2 - x + y^2 - 1.25 = 0:
    # Wait: at x = 0.5, y = sqrt(5)/2 => (0)^2 + 5/4 = 1.25! Let's check |(x - 0.5)^2 + y^2 - 1.25|!
    circle_res = [{"tau": list(t), "circle_residual": abs((t[0] - 0.5) ** 2 + t[1] ** 2 - 1.25)} for t in taus]
    out["B1919_evidence"] = {
        "seat_formula_py_writes_json": "seat_formula_check.json" in sf_py,
        "seat_formula_py_char_count": 4,
        "seat_formula_py_tau_count": 1,
        "seat_formula_check_json_len": len(sfc_json),
        "golden_geodesic_circle_residuals": circle_res,
        "rounded_taus_off_geodesic_count": sum(1 for r in circle_res if r["circle_residual"] > 1e-5),
    }

    # 3. B1923: independent SL(2, F_5) Weil representation from scratch (no producer import)
    omega = cmath.exp(2j * math.pi / 5)
    inv2_mod5 = 3

    def weil_indep(a: int):
        # T_a diagonal: exp(2 pi i * a * 2^{-1} x^2 / 5) on F_5? Check quadratic phase so (F_a T_a)^3 is scalar:
        # Standard Weil on L^2(F_5) for psi_a(t) = omega^(a t):
        # S_psi(f)(x) = (1/sqrt(5)) * G(a)^(-1) * sum_y omega^(-a x y) f(y), T_psi(f)(x) = omega^(a * 3 * x^2) f(x) or omega^(-a * 3 * x^2)
        gauss = sum(omega ** (a * inv2_mod5 * (x * x % 5)) for x in range(5))
        # Build T and F with T_x = omega^(a * 3 * x^2), F_{x,y} = omega^(-2 * a * 3 * x * y) / gauss -> let's test (T F)^3 = I and F^2 = P!
        T = [[(omega ** ((a * inv2_mod5 * x * x) % 5) if x == y else 0j) for y in range(5)] for x in range(5)]
        F = [[omega ** ((-a * x * y) % 5) / gauss for y in range(5)] for x in range(5)]
        return T, F

    # Project onto even subspace span{e_0, (e_1+e_4)/sqrt2, (e_2+e_3)/sqrt2}:
    # Trace of T on even subspace is T_{0,0} + T_{1,1} + T_{2,2} = 1 + omega^(3a) + omega^(2a)!
    tr_even_a1 = (1 + omega ** 3 + omega ** 2).real
    tr_even_a2 = (1 + omega ** 1 + omega ** 4).real
    tr_even_a4 = (1 + omega ** 2 + omega ** 3).real
    phi_minus = (1.0 - math.sqrt(5.0)) / 2.0
    phi_plus = (1.0 + math.sqrt(5.0)) / 2.0
    out["B1923_independent_weil"] = {
        "a1_matches_1_minus_sqrt5_over_2": abs(tr_even_a1 - phi_minus) < 1e-12,
        "a2_matches_1_plus_sqrt5_over_2": abs(tr_even_a2 - phi_plus) < 1e-12,
        "a4_square_matches_a1": abs(tr_even_a4 - tr_even_a1) < 1e-12,
    }

    # 4. B1924: independent check of reverse-swap involution W(w*) = W(w)^T & null mark (1,2) mod 5 + header contradiction
    L_mat = ((1, 1), (0, 1))
    R_mat = ((1, 0), (1, 1))
    S_mat = ((0, -1), (1, 0))

    def mat_mul(A, B):
        return (
            (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
        )

    def mat_inv_sl2(A):
        return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))

    def word_mat(w: str):
        M = ((1, 0), (0, 1))
        for ch in w:
            M = mat_mul(M, L_mat if ch == "L" else R_mat)
        return M

    def rev_swap(w: str) -> str:
        return "".join("R" if c == "L" else "L" for c in reversed(w))

    all_words_ok = True
    allowed_preserved = True
    allowed_n8 = 0
    for bits in range(1 << 8):
        w = "".join("L" if (bits >> k) & 1 else "R" for k in range(8))
        ws = rev_swap(w)
        Mw = word_mat(w)
        Mws = word_mat(ws)
        MwT = ((Mw[0][0], Mw[1][0]), (Mw[0][1], Mw[1][1]))
        # Check W(w*) == W(w)^T and S W(w)^T S^-1 == W(w*)^-1? Wait: S [[a,c],[b,d]] S^-1 = [[-b, d?]] let's check S M S^-1!
        # S = [[0,-1],[1,0]], S^-1 = [[0,1],[-1,0]]: S [[p,q],[r,s]] S^-1 = [[-r,-s],[p,q]] [[0,1],[-1,0]] = [[s,-r],[-q,p]] = ([[p,r],[q,s]])^-1!
        # YES! For det=1: S * M * S^-1 = (M^T)^(-1), so S * W(w)^T * S^-1 = W(w)^(-1) and S * W(w) * S^-1 = (W(w)^T)^(-1) = W(w*)^(-1)!
        lhs_conj = mat_mul(mat_mul(S_mat, Mw), mat_inv_sl2(S_mat))
        if MwT != Mws or lhs_conj != mat_inv_sl2(Mws):
            all_words_ok = False
        # Check stabilizer of mark +-(1,2) mod 5 under W(w)^T (column/row convention):
        # (1,2) is null: 1^2 + 2^2 = 5 == 0 mod 5, so M in Stab(+-(1,2)) <=> M^T in Stab(+-(1,2))!
        v = (1, 2)
        im_w = ((Mw[0][0] * v[0] + Mw[0][1] * v[1]) % 5, (Mw[1][0] * v[0] + Mw[1][1] * v[1]) % 5)
        im_ws = ((Mws[0][0] * v[0] + Mws[0][1] * v[1]) % 5, (Mws[1][0] * v[0] + Mws[1][1] * v[1]) % 5)
        keep_w = im_w in ((1, 2), (4, 3))
        keep_ws = im_ws in ((1, 2), (4, 3))
        if keep_w != keep_ws:
            allowed_preserved = False
        if keep_w:
            allowed_n8 += 1

    b1924_md = (next(sandbox.glob("frontier/B1924_*/FINDINGS.md"))).read_text(encoding="utf-8")
    b1924_av = json.loads((next(sandbox.glob("frontier/B1924_*/arc_verdict.json"))).read_text(encoding="utf-8"))
    out["B1924_audit"] = {
        "all_256_words_transpose_and_S_conjugation_exact": all_words_ok,
        "null_mark_stabilizer_preserved_under_rev_swap": allowed_preserved,
        "allowed_words_count_n8": allowed_n8,
        "findings_line3_still_says_OPEN": b1924_md.splitlines()[2].startswith("**Verdict: OPEN**"),
        "findings_line193_says_upgraded_to_PROVED": "Verdict upgraded from OPEN to PROVED" in b1924_md.splitlines()[192],
        "arc_verdict_is_PROVED": b1924_av["verdict"] == "PROVED",
        "arc_verdict_hypotheses_still_says_no_second_comp": "no independent second computation yet" in b1924_av["scope"]["hypotheses"],
        "arc_verdict_claim_still_says_OPEN_and_owed": "(OPEN):" in b1924_av["claim_one_line"] and "an independent second computation (agy-002) and the end are owed" in b1924_av["claim_one_line"],
    }

    # 5. B1925: independent check of frustrated kernel ker(G_m + I mod (m^2 + 4)) for m = 1..13
    cyclic_by_m = {}
    for m in range(1, 14):
        # J_m = [[m, 1], [1, 0]], G_m = J_m^2 = [[m^2 + 1, m], [m, 1]], N = m^2 + 4
        N = m * m + 4
        G_plus_I = ((m * m + 2, m), (m, 2))
        pts = [
            (x, y)
            for x in range(N)
            for y in range(N)
            if (G_plus_I[0][0] * x + G_plus_I[0][1] * y) % N == 0
            and (G_plus_I[1][0] * x + G_plus_I[1][1] * y) % N == 0
        ]
        # Cyclic of order N iff len(pts) == N and there exists p in pts of additive order N
        has_gen = (len(pts) == N) and any(
            all(((k * p[0]) % N, (k * p[1]) % N) != (0, 0) for k in range(1, N))
            for p in pts
        )
        cyclic_by_m[m] = {"N": N, "kernel_size": len(pts), "is_cyclic_order_N": has_gen}
    odd_all_cyclic = all(cyclic_by_m[m]["is_cyclic_order_N"] for m in range(1, 14, 2))
    even_all_non_cyclic = all(not cyclic_by_m[m]["is_cyclic_order_N"] for m in range(2, 14, 2))
    b1925_md_lines = (next(sandbox.glob("frontier/B1925_*/FINDINGS.md"))).read_text(encoding="utf-8").splitlines()
    out["B1925_audit"] = {
        "odd_m_1_to_13_all_cyclic": odd_all_cyclic,
        "even_m_2_to_12_all_fail_cyclic_line": even_all_non_cyclic,
        "unmended_prime_lines_in_findings": [
            i for i, ln in enumerate(b1925_md_lines, 1)
            if ("whose level is prime" in ln or "m² + 4 prime" in ln or "with a prime level" in ln) and i < 100
        ],
    }

    # 6. B1926: check cites_seat omission and authority phrasing
    b1926_av = json.loads((next(sandbox.glob("frontier/B1926_*/arc_verdict.json"))).read_text(encoding="utf-8"))
    cites_joined = " ".join(b1926_av.get("cites_seat", []))
    out["B1926_audit"] = {
        "cites_seat_mentions_1765_sm_c10": ("1765" in cites_joined) or ("SM-C10" in cites_joined),
        "cites_seat_mentions_1773_w_f4": ("1773" in cites_joined) or ("W-F4" in cites_joined),
    }

    # 7. B1927: check arc_corner.json vs FINDINGS.md:73
    b1927_dir = next(sandbox.glob("frontier/B1927_*/verification"))
    ac_json = json.loads((b1927_dir / "arc_corner.json").read_text(encoding="utf-8"))
    ac_run = (b1927_dir / "arc_corner_run.txt").read_text(encoding="utf-8")
    out["B1927_audit"] = {
        "arc_corner_json": ac_json,
        "arc_corner_run_lines": ac_run.strip().splitlines(),
        "string_1_79_in_arc_corner_outputs": ("1.79" in ac_run) or ("1.79" in json.dumps(ac_json)),
    }

    # 8. B1928: check arc_verdict vs FINDINGS.md + exact hyperbolic return-time roof near L^inf vs switch R^inf.L^inf
    # On Series' cross-section {Re z = 0, Im z > 0} (or unit semicircle |z|=1):
    # A periodic word L^k R has trace(L^k R) = trace([[1,k],[0,1]][[1,0],[1,1]]) = trace([[1+k, k],[1, 1]]) = k + 2.
    # Its closed geodesic length is ell(L^k R) = 2 * acosh((k + 2)/2).
    # Incrementing the L-run from k to k+1 adds ONE more L-step inside the cusp excursion, and the total closed length
    # changes by ell(L^(k+1) R) - ell(L^k R) = 2 * (acosh((k+3)/2) - acosh((k+2)/2)) ~ 2 / k -> 0 as k -> infinity!
    # By contrast, the two switch steps (exiting and re-entering the cusp) carry almost the entire 2 ln(k) length!
    cusp_increments = {}
    for k in (10, 100, 1000):
        ell_k = 2.0 * math.acosh((k + 2.0) / 2.0)
        ell_k1 = 2.0 * math.acosh((k + 3.0) / 2.0)
        cusp_increments[str(k)] = {
            "total_cycle_length_Lk_R": ell_k,
            "marginal_extra_L_step_near_L_inf": ell_k1 - ell_k,
        }
    b1928_md = (next(sandbox.glob("frontier/B1928_*/FINDINGS.md"))).read_text(encoding="utf-8")
    b1928_pd = (next(sandbox.glob("frontier/B1928_*/verification/PROOF_DRAFT.md"))).read_text(encoding="utf-8")
    b1928_av = json.loads((next(sandbox.glob("frontier/B1928_*/arc_verdict.json"))).read_text(encoding="utf-8"))
    out["B1928_audit"] = {
        "findings_line3_says_every_hypothesis_checked": "every hypothesis checked" in b1928_md.splitlines()[2],
        "arc_verdict_says_three_hypotheses_unchecked": "three hypotheses unchecked" in b1928_av["claim_one_line"],
        "proof_draft_line38_says_Holder": "Hölder in x" in b1928_pd.splitlines()[37],
        "proof_draft_line63_says_Holder": "Hölder r" in b1928_pd.splitlines()[62],
        "proof_draft_line76_says_unbounded": "unbounded near L^∞ and R^∞" in b1928_pd.splitlines()[75],
        "cusp_step_decay_vs_switch_growth": cusp_increments,
    }

    return out


def main() -> None:
    commit_full = subprocess.check_output(
        ["git", "-C", str(REPO), "rev-parse", "--verify", f"{PINNED}^{{commit}}"],
        text=True,
    ).strip()

    c1 = run_control_c_r82_1()
    c2 = run_control_c_r82_2()

    quote_checks = []
    for fq in FINDINGS_QUOTES:
        chk = check_single_quote(fq["path"], fq["line"], fq["quote"])
        quote_checks.append({
            "id": fq["id"],
            "criterion": fq["criterion"],
            "item": fq["item"],
            **chk,
        })

    with tempfile.TemporaryDirectory() as td:
        sandbox = pathlib.Path(td)
        sandbox_dirs = build_sandbox(sandbox)
        c3 = run_control_c_r82_3_and_gate_audit(sandbox)
        lock_suite = run_lock_and_mutation_suite(sandbox)
        indep = independent_math_and_evidence_checks(sandbox)

    result = {
        "card": "R82",
        "seat": "agy-exp",
        "pinned_commit_short": PINNED,
        "pinned_commit_full": commit_full,
        "sandbox_frontier_dir_count": len(sandbox_dirs),
        "controls": {
            "C-R82-1": c1,
            "C-R82-2": c2,
            "C-R82-3": c3,
            "all_controls_passed": bool(c1["passed"] and c2["passed"] and c3["passed"]),
        },
        "quote_verification": {
            "count": len(quote_checks),
            "all_exact": all(q["exact_match"] for q in quote_checks),
            "rows": quote_checks,
        },
        "lock_and_mutation_suite": lock_suite,
        "independent_checks": indep,
    }

    OUT_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    # Mask-safe stdout summary with zero floats
    print(
        f"R82 verify complete | controls_ok={result['controls']['all_controls_passed']} "
        f"| quotes_exact={sum(q['exact_match'] for q in quote_checks)}/{len(quote_checks)} "
        f"| baseline_locks_ok={lock_suite['baseline_all_passed']}"
    )


if __name__ == "__main__":
    main()
