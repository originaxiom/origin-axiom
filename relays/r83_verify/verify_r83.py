#!/usr/bin/env python3
"""
Card R83 — Blind Audit, Zero-Import Mathematical Countercheck & Sandbox Lock-Mutation Verifier at b35eac607.

Seat: agy-exp
Branch: agy/self-consistent-loop-2026-11-11
Pinned review target: b35eac607 (origin/review-83/read)
Window diff base (where referenced): 73e71e277

Isolation & Firewall Guarantees:
  1. Reads repository objects strictly from pinned commit b35eac607 (and 73e71e277 where needed);
     never touches origin/main, c8cece9be, or any other seat's branch.
  2. Extracts a self-contained pure-mathematics sandbox into a temporary directory, explicitly
     excluding B1612, B1637, and B1720 and deleting any historical comparison scripts before
     execution (0 of 19).
  3. Executes pre-registered negative controls C-R83-1, C-R83-2, and C-R83-3, runs all lock files
     in B1930..B1944 plus window governance/scoreboard locks, applies targeted sandbox mutations
     to prove lock/gate non-failure, performs zero-trust independent mathematical recomputations
     (zero imports from main or other relays folders), and verifies character-for-character and
     1-based line-number exactness of every quoted finding at b35eac607.
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
import os
import pathlib
import re
import subprocess
import sys
import tempfile
from fractions import Fraction
from typing import Any, Dict, List, Tuple

import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
OUT_PATH = HERE / "verify_r83_out.json"
PINNED = "b35eac607"
WINDOW_BASE = "73e71e277"

# Exact machine-checked quotations at b35eac607 (1-based line numbers).
FINDINGS_QUOTES: List[Dict[str, Any]] = [
    {
        "id": "F-01",
        "criterion": 2,
        "item": "B1938",
        "path": "frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/FINDINGS.md",
        "line": 83,
        "quote": "  truncation's ~1 %. They do: max |z| 2.4, so the comparison would have seen a 1 % effect.",
    },
    {
        "id": "F-02",
        "criterion": 2,
        "item": "B1940",
        "path": "frontier/B1940_the_area_options_corrected_in_extended_precision/FINDINGS.md",
        "line": 73,
        "quote": "  The largest change, 0.086 in ln, is about two-thirds of the run statistic's σ floor of 0.10. So it was material.",
    },
    {
        "id": "F-03",
        "criterion": 2,
        "item": "B1941",
        "path": "frontier/B1941_a_fermion_determinant_prefers_one_higgs_world_at_every_point_and_a_one_loop_trace_the_other/FINDINGS.md",
        "line": 33,
        "quote": "| ln det, colour weights (3, 3, 1), exact weight | **28 of 28** | +1.83 | +6.44 |",
    },
    {
        "id": "F-04",
        "criterion": 2,
        "item": "B1942",
        "path": "frontier/B1942_at_level_fifteen_the_leptons_keep_the_order_five_down_rows_and_the_quarks_move/FINDINGS.md",
        "line": 23,
        "quote": "- **Averaging.** The map w ↦ 6w takes the 192 points of exact order 15 onto the 24 of order 5, each hit six times. So the leptons'",
    },
    {
        "id": "F-05",
        "criterion": 2,
        "item": "B1943",
        "path": "frontier/B1943_the_act_fixes_one_line_of_order_five_and_the_foundations_two_postulates_enter_the_count/FINDINGS.md",
        "line": 21,
        "quote": "- **The Smith forms.** Smith(LR − I) = (1, 1) and Smith(LR + I) = (1, 3).",
    },
    {
        "id": "F-06",
        "criterion": 2,
        "item": "B1944",
        "path": "frontier/B1944_the_big_run_read_frame_c_fails_and_the_average_washes_out_the_hierarchy/FINDINGS.md",
        "line": 56,
        "quote": "  | W₊∣b | 59.3 | 3 310 | 11.3 | 15.6 | 1.21 | 7.6 | 80.9 |",
    },
    {
        "id": "F-07",
        "criterion": 1,
        "item": "Scoreboard S03 / B1943",
        "path": "docs/TOTAL_INPUTS_SCOREBOARD.md",
        "line": 19,
        "quote": "| S03 | the root: the act's first homology torsion-free (SE1), which selects the class of LR (m004, m003) and that of LP (m000) | CHOSEN | GENESIS SE1 (POSTULATED; UNIQUENESS A5); what it selects is derived (T-ROOT). [2026-11-14, B1943: added; the foundation's postulate was counted nowhere on this board] | |",
    },
    {
        "id": "F-08",
        "criterion": 4,
        "item": "Scoreboard Frame C / test_b1834",
        "path": "docs/TOTAL_INPUTS_SCOREBOARD.md",
        "line": 122,
        "quote": "*Status:* a structural frame, no value claimed (2026-11-14): no FITTED input; tau and the line are not inputs of it (B1928 PROVED); its values are computed (B1928's integral, in the json only) and NOT sealed; the canonical end's numbers are owed a second computation (agy-002's A2-CANON) before any seal. The lepton rows are not claimed: at level 5 the lepton coupling is the down coupling transposed (six times the hypercharge mod 5 is constant on SU(5)'s multiplets), minimal SU(5)'s relation, which the record already notes the measured Georgi-Jarlskog split forbids (B1839's arc, CHANGELOG); a level or structure separating them is owed (P-845). J's sign is not claimed: the tick involution flips it (agy-002's A2-OWN1), so it needs the hand. [2026-11-14, later: the values are committed and sealed (B1932) before their second computations, a corrected file to be sealed beside them if one disagrees; the run waits until every option has an agreeing second computation; the move-count options have one (B1937)] [2026-11-15: READ under the sealed rule (B1944): FAIL in every option, best chi2_7 6 679 against 22.0, the worst claimed row off by a factor of 3 314 or more; PROVISIONAL until its second computation (SM-C15); the frame's average has no hierarchy steep enough].",
    },
    {
        "id": "F-09",
        "criterion": 4,
        "item": "B1932",
        "path": "frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/test_b1932_values_and_seal.py",
        "line": 22,
        "quote": '    e = json.loads((HERE / "ergodic_both_worlds.json").read_text()); a = json.loads((HERE / "area_measure.json").read_text())',
    },
    {
        "id": "F-10",
        "criterion": 4,
        "item": "B1934",
        "path": "frontier/B1934_level_fives_weil_representation_lies_in_su3_x_su2_and_the_hand_is_the_golden_fields_quadratic_character/verification/test_b1934_level_five_structure.py",
        "line": 21,
        "quote": "    S = np.array([[L.W ** (x * y) for y in range(L.P)] for x in range(L.P)]) / np.sqrt(L.P)",
    },
    {
        "id": "F-11",
        "criterion": 1,
        "item": "B1935",
        "path": "frontier/B1935_the_modular_group_permutes_the_frames_channels_as_s3_around_a_fixed_centre_and_the_sectors_coincide_only_at_line_orders_two_to_seven/FINDINGS.md",
        "line": 25,
        "quote": "The two swaps generate S₃ on {i, j, k}; channel 1 is fixed by both. **The modular group acts on the frame's four",
    },
    {
        "id": "F-12",
        "criterion": 1,
        "item": "B1936",
        "path": "frontier/B1936_matter_sits_in_the_even_half_of_lambda_c5_and_parity_consistency_would_fix_the_higgs_world/FINDINGS.md",
        "line": 24,
        "quote": "- every conjugate at 5 − k.",
    },
    {
        "id": "F-13",
        "criterion": 1,
        "item": "B1937",
        "path": "frontier/B1937_the_big_runs_rule_amended_before_the_look/FINDINGS.md",
        "line": 46,
        "quote": "- **The lock** (`verification/test_b1937_rule_v2.py`, synthetic data only, nine tests), each with a planted case:",
    },
    {
        "id": "F-14",
        "criterion": 4,
        "item": "B1938",
        "path": "frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/verification/test_b1938_coupling_and_gauge_class.py",
        "line": 14,
        "quote": "    assert len(diffs) >= 6 and max(diffs) < 1e-12",
    },
    {
        "id": "F-15",
        "criterion": 1,
        "item": "B1939",
        "path": "frontier/B1939_the_agy_seats_unharvested_claims_recomputed/FINDINGS.md",
        "line": 119,
        "quote": '  - **B1935** prints its "Higgs triplet" T-eigenphases as {1/8, 3/8, 7/8}. Those are V\'s, the conjugate. The weave',
    },
    {
        "id": "F-16",
        "criterion": 5,
        "item": "B1940",
        "path": "frontier/B1940_the_area_options_corrected_in_extended_precision/arc_verdict.json",
        "line": 26,
        "quote": ' "claim_one_line": "THE BIG RUN\'S AREA OPTIONS CORRECTED IN EXTENDED PRECISION (PROVED; computed once, the second computation owed): the double-precision frame breaks F-bar(tau + 1) = F-bar(tau) above Im tau about 11 because the true m1/m3 falls below 1e-15 there, and neither a 50-digit SVD nor the closed-form residues repair it; the frame redone in mpmath passes tau -> tau + 1 to 1e-18 at heights 12 to 45 and matches the double frame where that is sound; the area options\' mixing moduli move by up to 0.068 in ln, their mass ratios by under 1e-4, the move-count options not at all; a corrected values file and version 3 of the run\'s script are sealed beside B1932\'s. 0 of 19.",',
    },
    {
        "id": "F-17",
        "criterion": 8,
        "item": "B1944",
        "path": "frontier/B1944_the_big_run_read_frame_c_fails_and_the_average_washes_out_the_hierarchy/arc_verdict.json",
        "line": 22,
        "quote": ' "claim_one_line": "THE BIG RUN, READ: FRAME C FAILS IN EVERY OPTION (NEGATIVE as sealed; PROVISIONAL until SM-C15 re-runs it): best chi2_7 6 679 against a bar of 22.0, every option\'s worst claimed row off by a factor of 3 314 or more, and 22 % of random targets fitted as well; version 1 FAIL too. Every mass ratio of the average is too large, about 10 times (s/b) to thousands of times (u/t), and |V_cb| and |V_ub| by similar orders; |V_us| is near (0.89 to 1.47) in every option, which the calibration calls generic. What the wall teaches: the average over the whole surface is dominated by the bulk, so the step that removed tau also removed the hierarchy. Nothing is adjusted after the look. 0 of 19.",',
    },
    {
        "id": "F-18",
        "criterion": 8,
        "item": "B1933 / B1930 / window mends",
        "path": "frontier/B1933_the_foundation_at_version_1_69/arc_verdict.json",
        "line": 26,
        "quote": ' "claim_one_line": "THE FOUNDATION AT VERSION 1.69: THE m000 ROW OF THE TABLE OF FRAMES SAYS WHAT B1926 COMPUTED (F-FC closed, b1 = 1 and cusp rank 1 at levels 1 to 8; F-CI: no sector module at an odd level, the twisted classes the double cover\'s matter seen from below, a stated choice whether they count), F-HE and F-AP not computed and offered to the SM seat; the list \'Computed nowhere yet\' narrows its m000 entry to those two frames and marks the harmonic frame\'s counts outside m004\'s levels as computed once (agy-exp\'s X-NEVER, harvest row 1797), its second computation owed. Written by the version\'s own script; its lock takes the version back and gives the page again. 0 of 19.",',
    },
    {
        "id": "F-19",
        "criterion": 1,
        "item": "THE_SWEEP_OF_2026-11-14 / companion pages",
        "path": "docs/THE_SWEEP_OF_2026-11-14.md",
        "line": 1023,
        "quote": "- The free-bit count, the E8-lattice question and the puncture-residue note are marked offrecord_origin=true because the S14 reader tied them to the session's off-record study; their mathematics may also stand on B1934 to B1936 alone.",
    },
    {
        "id": "F-20",
        "criterion": 4,
        "item": "tests/test_review_waiver_names_its_anchor.py & gates.py",
        "path": "tests/test_review_waiver_names_its_anchor.py",
        "line": 59,
        "quote": "    assert all(a in written for a in anchors if a), anchors",
    },
]

# Strictly pure-mathematical frontier prefixes (B1612, B1637, B1720 explicitly excluded under 0-of-19).
SANDBOX_B_PREFIXES = [
    "B1427", "B1432", "B1434", "B1435", "B1438",
    "B1654", "B1656", "B1667", "B1691",
    "B1716", "B1723", "B1724", "B1737",
    "B1832", "B1834", "B1838", "B1886", "B1891", "B1904",
    "B1917", "B1918", "B1919", "B1920", "B1921", "B1922", "B1923",
    "B1924", "B1925", "B1926", "B1927", "B1928", "B1929",
    "B1930", "B1931", "B1932", "B1933", "B1934", "B1935", "B1936",
    "B1937", "B1938", "B1939", "B1940", "B1941", "B1942", "B1943", "B1944",
]

FORBIDDEN_EMPIRICAL_PREFIXES = ("B1612_", "B1637_", "B1720_")


# ============================================================================
# SECTION 1: GIT OBJECT READER, QUOTE CHECKER & PRE-REGISTERED CONTROLS 1 & 2
# ============================================================================

def git_show_text(path: str, commit: str = PINNED) -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "show", f"{commit}:{path}"],
        text=True,
    )


def check_single_quote(path: str, line_no: int, quote: str, commit: str = PINNED) -> Dict[str, Any]:
    lines = git_show_text(path, commit).splitlines()
    in_range = 1 <= line_no <= len(lines)
    actual = lines[line_no - 1] if in_range else None
    exact = bool(in_range and (actual == quote))
    return {
        "path": path,
        "line": line_no,
        "in_range": in_range,
        "exact_match": exact,
    }


def run_control_c_r83_1() -> Dict[str, Any]:
    """C-R83-1: Exact quote passes; 1-char perturbation and +1 line shift are both rejected."""
    ref_path = "WORKING_RULES.md"
    ref_line = 354
    ref_text = git_show_text(ref_path).splitlines()[ref_line - 1]
    ok_exact = check_single_quote(ref_path, ref_line, ref_text)["exact_match"]
    perturbed_text = ref_text[:-1] + ("X" if ref_text[-1] != "X" else "Y")
    ok_char_pert = check_single_quote(ref_path, ref_line, perturbed_text)["exact_match"]
    ok_line_shift = check_single_quote(ref_path, ref_line + 1, ref_text)["exact_match"]
    passed = bool(ok_exact and (not ok_char_pert) and (not ok_line_shift))
    return {
        "control": "C-R83-1",
        "exact_accepted": ok_exact,
        "char_perturbation_rejected": not ok_char_pert,
        "line_shift_rejected": not ok_line_shift,
        "passed": passed,
    }


def run_control_c_r83_2() -> Dict[str, Any]:
    """C-R83-2: Lock-mutation harness classifies vacuous test CANNOT_FAIL and genuine test CAUGHT."""
    with tempfile.TemporaryDirectory() as td:
        tdp = pathlib.Path(td)
        data_file = tdp / "data.json"
        vacuous_test = tdp / "test_vacuous.py"
        genuine_test = tdp / "test_genuine.py"
        vacuous_test.write_text(
            "import json, pathlib\n"
            "def test_vac():\n"
            "    _ = json.loads((pathlib.Path(__file__).parent / 'data.json').read_text())\n"
            "    assert all(v > 0 for v in [])\n",
            encoding="utf-8",
        )
        genuine_test.write_text(
            "import json, pathlib\n"
            "def test_gen():\n"
            "    v = json.loads((pathlib.Path(__file__).parent / 'data.json').read_text())['v']\n"
            "    assert v == 1\n",
            encoding="utf-8",
        )
        data_file.write_text('{"v": 1}', encoding="utf-8")
        r_vac_base = subprocess.run([sys.executable, "-m", "pytest", "-q", str(vacuous_test)], capture_output=True)
        r_gen_base = subprocess.run([sys.executable, "-m", "pytest", "-q", str(genuine_test)], capture_output=True)
        data_file.write_text('{"v": -7}', encoding="utf-8")
        r_vac_mut = subprocess.run([sys.executable, "-m", "pytest", "-q", str(vacuous_test)], capture_output=True)
        r_gen_mut = subprocess.run([sys.executable, "-m", "pytest", "-q", str(genuine_test)], capture_output=True)
        vac_class = "CANNOT_FAIL" if (r_vac_base.returncode == 0 and r_vac_mut.returncode == 0) else "CAUGHT"
        gen_class = "CAUGHT" if (r_gen_base.returncode == 0 and r_gen_mut.returncode != 0) else "CANNOT_FAIL"
        passed = (vac_class == "CANNOT_FAIL") and (gen_class == "CAUGHT")
        return {
            "control": "C-R83-2",
            "vacuous_classification": vac_class,
            "genuine_classification": gen_class,
            "passed": passed,
        }


# ============================================================================
# SECTION 2: STANDALONE ZERO-IMPORT FRAME C & SERRE B[1] ARBITRARY-PRECISION
#            ENGINE (NO IMPORTS FROM MAIN OR OTHER RELAYS)
# ============================================================================

P5_ALL_24: List[Tuple[int, int]] = [
    (ja, jb) for ja in range(5) for jb in range(5) if (ja, jb) != (0, 0)
]

CHARGES_THREE: Dict[str, Tuple[int, int]] = {
    "sec_u": (1, -4),
    "sec_d": (1, 2),
    "sec_e": (-3, 6),
}


def build_quaternions_and_coupling_standalone() -> List[Tuple[int, int, int, int, int, int]]:
    i2 = np.eye(2, dtype=np.complex128)
    qi = np.array([[1j, 0.0], [0.0, -1j]], dtype=np.complex128)
    qj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=np.complex128)
    qk = qi @ qj
    eps = qj
    units = [i2, qi, qj, qk]
    ec = [eps @ u for u in units]
    G = np.array([[np.sum(ec[t] * units[s]) for s in range(4)] for t in range(4)], dtype=np.complex128)
    Gi = np.linalg.inv(G)
    edual = [sum(Gi[b, a] * units[b] for b in range(4)) for a in range(4)]
    blocks = [qj, qi, qk]
    higgs_units = [qi, qj, qk]
    nz: List[Tuple[int, int, int, int, int, int]] = []
    for alpha in range(3):
        S_unit = higgs_units[alpha]
        for s_idx in range(4):
            M_unit = edual[s_idx]
            for ra in range(3):
                for cb in range(3):
                    val = np.sum((blocks[ra].T @ eps @ S_unit @ blocks[cb]) * M_unit)
                    if abs(val) > 1e-14:
                        tr2 = int(round(val.real * 2.0))
                        ti2 = int(round(val.imag * 2.0))
                        assert abs(val - complex(tr2 / 2.0, ti2 / 2.0)) < 1e-14
                        nz.append((alpha, s_idx, ra, cb, tr2, ti2))
    return nz


def build_serre_b1_exact_standalone(max_k: int = 168) -> List[Tuple[int, List[Tuple[Fraction, Fraction]]]]:
    N = max_k

    def s_mul(a: Dict[int, Tuple[Fraction, Fraction]], b: Dict[int, Tuple[Fraction, Fraction]]):
        out: Dict[int, Tuple[Fraction, Fraction]] = {}
        for ka, (ar, ai) in a.items():
            for kb, (br, bi) in b.items():
                k = ka + kb
                if k <= N:
                    pr, pi_ = out.get(k, (Fraction(0), Fraction(0)))
                    out[k] = (pr + ar * br - ai * bi, pi_ + ar * bi + ai * br)
        return {k: v for k, v in out.items() if v[0] or v[1]}

    def s_inv(a: Dict[int, Tuple[Fraction, Fraction]]):
        k0 = min(a)
        c0r, c0i = a[k0]
        d = c0r * c0r + c0i * c0i
        inv0 = (c0r / d, -c0i / d)
        M = N + k0
        sj = [a.get(k0 + j, (Fraction(0), Fraction(0))) for j in range(M + 1)]
        t: List[Tuple[Fraction, Fraction]] = [inv0]
        for m in range(1, M + 1):
            ar, ai = Fraction(0), Fraction(0)
            for j in range(1, m + 1):
                sr, si = sj[j]
                if sr or si:
                    tr, ti = t[m - j]
                    ar += sr * tr - si * ti
                    ai += sr * ti + si * tr
            t.append((-(inv0[0] * ar - inv0[1] * ai), -(inv0[0] * ai + inv0[1] * ar)))
        return {m - k0: t[m] for m in range(M + 1) if m - k0 <= N and (t[m][0] or t[m][1])}

    th2: Dict[int, Tuple[Fraction, Fraction]] = {}
    n = 0
    while (2 * n + 1) ** 2 <= N:
        th2[(2 * n + 1) ** 2] = (Fraction(2), Fraction(0))
        n += 1
    th3: Dict[int, Tuple[Fraction, Fraction]] = {0: (Fraction(1), Fraction(0))}
    th4: Dict[int, Tuple[Fraction, Fraction]] = {0: (Fraction(1), Fraction(0))}
    n = 1
    while 4 * n * n <= N:
        th3[4 * n * n] = (Fraction(2), Fraction(0))
        th4[4 * n * n] = (Fraction(2 * ((-1) ** n)), Fraction(0))
        n += 1

    e2: Dict[int, Tuple[Fraction, Fraction]] = {0: (Fraction(1), Fraction(0))}
    for m in range(1, N // 8 + 1):
        sig1 = sum(d for d in range(1, m + 1) if m % d == 0)
        e2[8 * m] = (Fraction(-24 * sig1), Fraction(0))

    di = s_inv(s_mul(s_mul(th2, th3), th4))
    R0 = {k: (-v[0], -v[1]) for k, v in s_mul(s_mul(th2, th2), di).items()}
    R1 = {k: (-v[0], -v[1]) for k, v in s_mul(s_mul(th4, th4), di).items()}
    R2 = s_mul(s_mul(s_mul(th3, th3), {0: (Fraction(0), Fraction(1))}), di)

    def serre_mhalf(f: Dict[int, Tuple[Fraction, Fraction]]):
        qdf = {k: (v[0] * Fraction(k, 8), v[1] * Fraction(k, 8)) for k, v in f.items() if k != 0}
        e2f = s_mul(e2, f)
        out = dict(qdf)
        for k, (r, im) in e2f.items():
            pr, pi_ = out.get(k, (Fraction(0), Fraction(0)))
            out[k] = (pr + r * Fraction(1, 24), pi_ + im * Fraction(1, 24))
        return out

    B1 = [serre_mhalf(R0), serre_mhalf(R1), serre_mhalf(R2)]
    all_ks = sorted(set().union(*(d.keys() for d in B1)))
    exact_rows: List[Tuple[int, List[Tuple[Fraction, Fraction]]]] = []
    for k in all_ks:
        exact_rows.append((k, [d.get(k, (Fraction(0), Fraction(0))) for d in B1]))
    return exact_rows


T_COUP_NZ = build_quaternions_and_coupling_standalone()
SERRE_EXACT_ROWS = build_serre_b1_exact_standalone(168)


def eval_frame_mp(
    x_exact_or_float: Any,
    y_exact_or_float: Any,
    L2_raw_exact: Fraction,
    lines_int: List[Tuple[int, int]],
    dps_min: int = 120,
) -> Dict[str, Any]:
    """Arbitrary-precision Frame C evaluator on agy-exp's own zero-import formulas."""
    y_f = float(y_exact_or_float)
    dps_eff = max(dps_min, int(math.ceil(2.4 * y_f)) + 65)
    with mp.workdps(dps_eff):
        def to_mpf(v: Any) -> mp.mpf:
            if isinstance(v, Fraction):
                return mp.mpf(v.numerator) / v.denominator
            if isinstance(v, int):
                return mp.mpf(v)
            return mp.mpf(repr(float(v)))

        xv = to_mpf(x_exact_or_float)
        yv = to_mpf(y_exact_or_float)
        tau = mp.mpc(xv, yv)
        L2 = to_mpf(L2_raw_exact)
        tl2 = L2 + mp.mpf("0.5") * mp.log(yv) - (mp.euler + mp.log(mp.pi))
        exp_m2L2 = mp.exp(-2 * L2)

        xq = mp.exp(mp.j * mp.pi * tau / 4)
        c3_S = [mp.mpc(0), mp.mpc(0), mp.mpc(0)]
        cutoff = mp.mpf(10) ** (-(dps_eff + 8))
        for k_int, cols_frac in SERRE_EXACT_ROWS:
            pw = xq ** k_int
            if abs(pw) < cutoff and k_int > 8:
                break
            for col_j in range(3):
                fr, fi = cols_frac[col_j]
                if fr or fi:
                    c_mp = mp.mpc(mp.mpf(fr.numerator) / fr.denominator, mp.mpf(fi.numerator) / fi.denominator)
                    c3_S[col_j] += pw * c_mp
        c3_St = [mp.conj(z) for z in c3_S]

        k_lim = max(12, int(math.ceil(math.sqrt((dps_eff * math.log(10.0) + 25.0) / (math.pi * max(y_f, 0.5))))) + 2)

        def th_char(al: mp.mpf, be: mp.mpf) -> mp.mpc:
            at = al - mp.nint(al)
            s = mp.mpc(0)
            for k in range(-k_lim, k_lim + 1):
                m = mp.mpf(k) + at
                s += mp.exp(mp.j * mp.pi * tau * (m * m) + 2 * mp.j * mp.pi * m * be)
            return s

        def a0_char(al: mp.mpf, be: mp.mpf) -> mp.mpc:
            at = al - mp.nint(al)
            den = mp.mpc(0)
            num = mp.mpc(0)
            for k in range(-k_lim, k_lim + 1):
                m = mp.mpf(k) + at
                t = mp.exp(mp.j * mp.pi * tau * (m * m) + 2 * mp.j * mp.pi * m * be)
                den += t
                num += m * t
            return (2 * mp.j * mp.pi * num) / den

        th1p0 = mp.mpc(0)
        for k in range(k_lim):
            h = mp.mpf(k) + mp.mpf("0.5")
            th1p0 += ((-1) ** k) * (2 * k + 1) * mp.exp(mp.j * mp.pi * tau * (h * h))
        th1p0 *= 2 * mp.pi

        def F_kron(u1: mp.mpf, u2: mp.mpf) -> mp.mpf:
            a = u1 - mp.floor(u1)
            b = u2 - mp.floor(u2)
            az = (abs(a) < mp.mpf("1e-40")) or (abs(a - 1) < mp.mpf("1e-40"))
            bz = (abs(b) < mp.mpf("1e-40")) or (abs(b - 1) < mp.mpf("1e-40"))
            if az:
                base = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(yv))
                if not bz:
                    base += yv * (mp.pi ** 2) / (mp.sin(mp.pi * b) ** 2)
                a_eff = mp.mpf(0)
            else:
                base = -mp.pi * (2 * mp.log(2) + mp.log(yv) + mp.digamma(a) + mp.digamma(1 - a))
                a_eff = a
            tot = base
            for k in range(-18, 19):
                m = mp.mpf(k) + a_eff
                if abs(m) > mp.mpf("1e-40"):
                    w = mp.exp(-2 * mp.pi * abs(m) * yv + 2 * mp.j * mp.pi * (m * xv + u2))
                    if abs(w) > cutoff:
                        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
            return tot

        half = mp.mpf("0.5")
        zero_thr = mp.mpf(10) ** (-dps_eff + 25)

        def make_Y_mp(c_vec: List[mp.mpc], u_v: List[mp.mpc]) -> mp.matrix:
            Y = mp.zeros(3, 3)
            for al_i, s_i, ra, cb, tr2, ti2 in T_COUP_NZ:
                Y[ra, cb] += c_vec[al_i] * u_v[s_i] * mp.mpc(tr2, ti2) * half
            return Y

        def svd_asc(Y: mp.matrix) -> Tuple[mp.matrix, List[mp.mpf]]:
            U_desc, sv_desc, _ = mp.svd_c(Y)
            U_asc = mp.zeros(3, 3)
            for c_new, c_old in enumerate((2, 1, 0)):
                for r in range(3):
                    U_asc[r, c_new] = U_desc[r, c_old]
            return U_asc, [sv_desc[2], sv_desc[1], sv_desc[0]]

        def mix3(Ua: mp.matrix, Ub: mp.matrix) -> List[mp.mpf]:
            out: List[mp.mpf] = []
            for i_idx, j_idx in ((0, 1), (1, 2), (0, 2)):
                s = mp.mpc(0)
                for r in range(3):
                    s += mp.conj(Ua[r, i_idx]) * Ub[r, j_idx]
                out.append(abs(s))
            return out

        sum_wm = [mp.mpf(0)] * 7
        sum_wp = [mp.mpf(0)] * 7
        per_line_mats: List[Dict[str, Any]] = []
        for ja, jb in lines_int:
            a_p = mp.mpf(ja) / 5
            b_p = mp.mpf(jb) / 5
            u_sec: Dict[str, List[mp.mpc]] = {}
            R_sec: Dict[str, List[mp.mpc]] = {}
            for sec in ("sec_u", "sec_d"):
                qL, qR = CHARGES_THREE[sec]
                ap, bp = (qL + qR) * a_p, (qL + qR) * b_p
                am, bm = (qL - qR) * a_p, (qL - qR) * b_p
                ph1 = mp.exp(-mp.j * mp.pi * (ap + am))
                R_1 = (-mp.j) * ph1 * th_char(ap + half, bp + half) * th_char(am + half, bm + half) / th1p0
                R_i = (-1) * th_char(ap + half, bp) * th_char(am + half, bm) / th1p0
                R_j = (-1) * ph1 * th_char(ap, bp + half) * th_char(am, bm + half) / th1p0
                R_k = (+mp.j) * th_char(ap, bp) * th_char(am, bm) / th1p0
                Rs = [R_1, R_i, R_j, R_k]
                R_sec[sec] = Rs
                sh = [
                    ((ap, bp), (ap + half, bp + half)),
                    ((ap, bp - half), (ap + half, bp)),
                    ((ap - half, bp), (ap, bp + half)),
                    ((ap - half, bp - half), (ap, bp)),
                ]
                vt = [mp.mpc(0)] * 4
                for s_i in range(4):
                    if abs(Rs[s_i]) > zero_thr:
                        Fu = F_kron(sh[s_i][0][0], sh[s_i][0][1])
                        a0v = a0_char(sh[s_i][1][0], sh[s_i][1][1])
                        n_ex = 2 * mp.pi * tl2 + Fu - mp.pi * (abs(a0v) ** 2) * exp_m2L2
                        vt[s_i] = mp.sqrt(n_ex) * Rs[s_i]
                u_sec[sec] = vt

            Yu_S = make_Y_mp(c3_S, u_sec["sec_u"])
            Yu_St = make_Y_mp(c3_St, u_sec["sec_u"])
            Yd_S = make_Y_mp(c3_S, u_sec["sec_d"])
            Yd_St = make_Y_mp(c3_St, u_sec["sec_d"])

            Uu_S, svu_S = svd_asc(Yu_S)
            Uu_St, svu_St = svd_asc(Yu_St)
            Ud_S, svd_S = svd_asc(Yd_S)
            Ud_St, svd_St = svd_asc(Yd_St)

            # W- = (sec_u S~, sec_d S); W+ = (sec_u S, sec_d S~)
            row_wm = [
                svu_St[1] / svu_St[2], svu_St[0] / svu_St[2],
                svd_S[1] / svd_S[2], svd_S[0] / svd_S[2],
                *mix3(Uu_St, Ud_S),
            ]
            row_wp = [
                svu_S[1] / svu_S[2], svu_S[0] / svu_S[2],
                svd_St[1] / svd_St[2], svd_St[0] / svd_St[2],
                *mix3(Uu_S, Ud_St),
            ]
            for idx in range(7):
                sum_wm[idx] += row_wm[idx]
                sum_wp[idx] += row_wp[idx]
            per_line_mats.append({
                "line": (ja, jb),
                "Yu_S": Yu_S, "Yu_St": Yu_St, "Yd_S": Yd_S, "Yd_St": Yd_St,
                "R_sec": R_sec,
            })

        n_l = len(lines_int)
        return {
            "dps_eff": dps_eff,
            "Fbar_wm": [v / n_l for v in sum_wm],
            "Fbar_wp": [v / n_l for v in sum_wp],
            "per_line_mats": per_line_mats,
        }


def eval_frame_f64_lightest_ratio(x_val: float, y_val: float, L2_val: float, lines_int: List[Tuple[int, int]]) -> float:
    """IEEE binary64 construction of Frame C's lightest singular-value ratio (W-, index 1) to test C-R83-3."""
    tau = complex(x_val, y_val)
    tl2 = L2_val + 0.5 * math.log(y_val) - (0.5772156649015329 + math.log(math.pi))
    exp_m2L2 = math.exp(-2.0 * L2_val)
    xq = cmath.exp(1j * math.pi * tau / 4.0)
    c3_S = np.zeros(3, dtype=np.complex128)
    for k_int, cols_frac in SERRE_EXACT_ROWS:
        pw = xq ** k_int
        if abs(pw) < 1e-20 and k_int > 8:
            break
        for col_j in range(3):
            fr, fi = cols_frac[col_j]
            if fr or fi:
                c3_S[col_j] += pw * complex(float(fr), float(fi))
    c3_St = np.conj(c3_S)

    def th_f64(al: float, be: float) -> complex:
        at = al - round(al)
        s = 0j
        for k in range(-12, 13):
            m = k + at
            s += cmath.exp(1j * math.pi * tau * (m * m) + 2j * math.pi * m * be)
        return s

    def a0_f64(al: float, be: float) -> complex:
        at = al - round(al)
        den = 0j
        num = 0j
        for k in range(-12, 13):
            m = k + at
            t = cmath.exp(1j * math.pi * tau * (m * m) + 2j * math.pi * m * be)
            den += t
            num += m * t
        return (2j * math.pi * num) / den

    th1p0 = 0j
    for k in range(12):
        h = k + 0.5
        th1p0 += ((-1) ** k) * (2 * k + 1) * cmath.exp(1j * math.pi * tau * (h * h))
    th1p0 *= 2.0 * math.pi

    # Use mpmath digamma once casted to float64 so Kronecker constants are exact to 53 bits
    def F_kron_f64(u1: float, u2: float) -> float:
        a = u1 - math.floor(u1)
        b = u2 - math.floor(u2)
        az = (abs(a) < 1e-13) or (abs(a - 1.0) < 1e-13)
        bz = (abs(b) < 1e-13) or (abs(b - 1.0) < 1e-13)
        if az:
            base = math.pi * (2.0 * 0.5772156649015329 - 2.0 * math.log(2.0) - math.log(y_val))
            if not bz:
                base += y_val * (math.pi ** 2) / (math.sin(math.pi * b) ** 2)
            a_eff = 0.0
        else:
            dg = float(mp.digamma(a) + mp.digamma(1.0 - a))
            base = -math.pi * (2.0 * math.log(2.0) + math.log(y_val) + dg)
            a_eff = a
        tot = base
        for k in range(-12, 13):
            m = k + a_eff
            if abs(m) > 1e-13:
                w = cmath.exp(-2.0 * math.pi * abs(m) * y_val + 2j * math.pi * (m * x_val + u2))
                tot += (2.0 * math.pi / abs(m)) * (w / (1.0 - w)).real
        return tot

    ratios_13: List[float] = []
    for ja, jb in lines_int:
        a_p, b_p = ja / 5.0, jb / 5.0
        qL, qR = CHARGES_THREE["sec_u"]
        ap, bp = (qL + qR) * a_p, (qL + qR) * b_p
        am, bm = (qL - qR) * a_p, (qL - qR) * b_p
        ph1 = cmath.exp(-1j * math.pi * (ap + am))
        Rs = [
            (-1j) * ph1 * th_f64(ap + 0.5, bp + 0.5) * th_f64(am + 0.5, bm + 0.5) / th1p0,
            (-1.0) * th_f64(ap + 0.5, bp) * th_f64(am + 0.5, bm) / th1p0,
            (-1.0) * ph1 * th_f64(ap, bp + 0.5) * th_f64(am, bm + 0.5) / th1p0,
            (+1j) * th_f64(ap, bp) * th_f64(am, bm) / th1p0,
        ]
        sh = [
            ((ap, bp), (ap + 0.5, bp + 0.5)),
            ((ap, bp - 0.5), (ap + 0.5, bp)),
            ((ap - 0.5, bp), (ap, bp + 0.5)),
            ((ap - 0.5, bp - 0.5), (ap, bp)),
        ]
        vt = [0j] * 4
        for s_i in range(4):
            if abs(Rs[s_i]) > 1e-13 * max(abs(z) for z in Rs):
                Fu = F_kron_f64(sh[s_i][0][0], sh[s_i][0][1])
                a0v = a0_f64(sh[s_i][1][0], sh[s_i][1][1])
                n_ex = 2.0 * math.pi * tl2 + Fu - math.pi * (abs(a0v) ** 2) * exp_m2L2
                vt[s_i] = math.sqrt(n_ex) * Rs[s_i]
        Y = np.zeros((3, 3), dtype=np.complex128)
        for al_i, s_i, ra, cb, tr2, ti2 in T_COUP_NZ:
            Y[ra, cb] += c3_St[al_i] * vt[s_i] * complex(tr2 / 2.0, ti2 / 2.0)
        sv = np.linalg.svd(Y, compute_uv=False)
        ratios_13.append(float(sv[2] / sv[0]))
    return sum(ratios_13) / len(ratios_13)


def run_control_c_r83_3() -> Dict[str, Any]:
    """
    C-R83-3:
      1. Dropping the 24-line average to a single non-fixed line (1, 0) breaks tau -> tau + 1 at y = 3/2.
      2. IEEE binary64 breaks Fbar(tau + 1) = Fbar(tau) on the lightest singular ratio at y = 20.
      3. Arbitrary-precision mpmath at exact rational x = 13/100 vs 113/100 preserves Fbar(tau + 1) = Fbar(tau)
         to < 1e-55 across y in {12, 20, 35, 45}, whereas passing float64 0.13 vs 1.13 reproduces
         validate_frame_mp.py's ~7e-18 floor.
    """
    L2_test = Fraction(314159, 100000)  # fixed invariant end height for translation test (x -> x + 1 preserves L2)
    # 1. Single non-fixed line (1, 0) at moderate height y = 3/2
    s_a = eval_frame_mp(Fraction(13, 100), Fraction(3, 2), L2_test, [(1, 0)], dps_min=90)
    s_b = eval_frame_mp(Fraction(113, 100), Fraction(3, 2), L2_test, [(1, 0)], dps_min=90)
    single_line_rel = max(
        float(abs(b - a) / abs(a)) for a, b in zip(s_a["Fbar_wm"], s_b["Fbar_wm"])
    )

    # 2. IEEE binary64 at y = 20 across all 24 lines
    f64_a = eval_frame_f64_lightest_ratio(0.13, 20.0, float(L2_test), P5_ALL_24)
    f64_b = eval_frame_f64_lightest_ratio(1.13, 20.0, float(L2_test), P5_ALL_24)
    f64_y20_rel = abs(f64_b - f64_a) / max(abs(f64_a), 1e-300)

    # 3. Arbitrary-precision mpmath across y in {12, 20, 35, 45} at exact rational 13/100 vs 113/100
    worst_mp_exact_rel = 0.0
    for y_int in (12, 20, 35, 45):
        ra = eval_frame_mp(Fraction(13, 100), Fraction(y_int, 1), L2_test, P5_ALL_24, dps_min=150)
        rb = eval_frame_mp(Fraction(113, 100), Fraction(y_int, 1), L2_test, P5_ALL_24, dps_min=150)
        with mp.workdps(ra["dps_eff"]):
            for vec_a, vec_b in ((ra["Fbar_wm"], rb["Fbar_wm"]), (ra["Fbar_wp"], rb["Fbar_wp"])):
                for va, vb in zip(vec_a, vec_b):
                    worst_mp_exact_rel = max(worst_mp_exact_rel, float(abs(vb - va) / abs(va)))

    # Contrast: passing binary64 floats 0.13 and 1.13 (as validate_frame_mp.py:14 does) introduces ~7e-18 floor
    fa_float = eval_frame_mp(0.13, 12.0, L2_test, P5_ALL_24, dps_min=120)
    fb_float = eval_frame_mp(1.13, 12.0, L2_test, P5_ALL_24, dps_min=120)
    with mp.workdps(fa_float["dps_eff"]):
        float_arg_floor_rel = max(
            float(abs(vb - va) / abs(va))
            for va, vb in zip(fa_float["Fbar_wm"], fb_float["Fbar_wm"])
        )

    passed = bool(
        single_line_rel > 1e-2
        and f64_y20_rel > 1e-2
        and worst_mp_exact_rel < 1e-55
        and float_arg_floor_rel > 1e-18
    )
    return {
        "control": "C-R83-3",
        "single_line_breaks_invariance": single_line_rel > 1e-2,
        "single_line_rel_diff": single_line_rel,
        "binary64_breaks_at_y20": f64_y20_rel > 1e-2,
        "binary64_y20_lightest_rel_diff": f64_y20_rel,
        "mpmath_exact_rational_holds_to_1e55": worst_mp_exact_rel < 1e-55,
        "mpmath_exact_worst_rel_diff": worst_mp_exact_rel,
        "binary64_float_arg_reproduces_1e18_floor": float_arg_floor_rel > 1e-18,
        "binary64_float_arg_rel_diff_y12": float_arg_floor_rel,
        "passed": passed,
    }


# ============================================================================
# SECTION 3: INDEPENDENT ZERO-TRUST MATHEMATICAL COUNTERCHECKS (GUARDRAILS 2, 3, 6)
# ============================================================================

def smith_2x2_exact(M: List[List[int]]) -> Tuple[int, int]:
    a, b = M[0][0], M[0][1]
    c, d = M[1][0], M[1][1]
    g1 = math.gcd(math.gcd(abs(a), abs(b)), math.gcd(abs(c), abs(d)))
    det_abs = abs(a * d - b * c)
    if g1 == 0:
        return (0, 0)
    return (g1, det_abs // g1)


def random_haar_u3(rng: np.random.Generator) -> np.ndarray:
    Z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / math.sqrt(2.0)
    Q, R = np.linalg.qr(Z)
    d = np.diag(R)
    ph = d / np.abs(d)
    return Q * ph[None, :]


def run_independent_math_checks() -> Dict[str, Any]:
    # 1. Guardrail 3: Haar unitary basis-scrambling test on our Frame C matrices + B1940 cusp limits
    rng = np.random.default_rng(20261115)
    pt_bulk = eval_frame_mp(Fraction(17, 100), Fraction(3, 2), Fraction(314159, 100000), [(1, 2)], dps_min=90)
    Yu_np = np.array([[complex(pt_bulk["per_line_mats"][0]["Yu_St"][r, c]) for c in range(3)] for r in range(3)], dtype=np.complex128)
    Yd_np = np.array([[complex(pt_bulk["per_line_mats"][0]["Yd_S"][r, c]) for c in range(3)] for r in range(3)], dtype=np.complex128)

    def obs_from_pair(Yu_m: np.ndarray, Yd_m: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        Uu, svu, _ = np.linalg.svd(Yu_m)
        Ud, svd, _ = np.linalg.svd(Yd_m)
        Vmod = np.abs(Uu[:, ::-1].conj().T @ Ud[:, ::-1])
        rats = np.array([svu[1] / svu[0], svu[2] / svu[0], svd[1] / svd[0], svd[2] / svd[0]])
        return Vmod, rats

    V0, r0 = obs_from_pair(Yu_np, Yd_np)
    max_haar_cov_err = 0.0
    min_broken_su2_scramble = 1e9
    for _ in range(12):
        UL = random_haar_u3(rng)
        URu = random_haar_u3(rng)
        URd = random_haar_u3(rng)
        V_rot, r_rot = obs_from_pair(UL @ Yu_np @ URu.conj().T, UL @ Yd_np @ URd.conj().T)
        max_haar_cov_err = max(max_haar_cov_err, float(np.max(np.abs(V_rot - V0))), float(np.max(np.abs(r_rot - r0))))
        UL_bad = random_haar_u3(rng)
        V_bad, _ = obs_from_pair(UL @ Yu_np @ URu.conj().T, UL_bad @ Yd_np @ URd.conj().T)
        min_broken_su2_scramble = min(min_broken_su2_scramble, float(np.max(np.abs(V_bad - V0))))

    # B1940 deep-cusp limit (y = 85): W- -> (5/12, 5/12, 7/12), whereas W+ -> (7/12, 7/12, 5/12)!
    pt_cusp = eval_frame_mp(Fraction(13, 100), Fraction(85, 1), Fraction(314159, 100000), P5_ALL_24, dps_min=260)
    wm_mix_cusp = [float(x) for x in pt_cusp["Fbar_wm"][4:7]]
    wp_mix_cusp = [float(x) for x in pt_cusp["Fbar_wp"][4:7]]
    wm_err_557 = max(abs(wm_mix_cusp[0] - 5 / 12), abs(wm_mix_cusp[1] - 5 / 12), abs(wm_mix_cusp[2] - 7 / 12))
    wp_err_775 = max(abs(wp_mix_cusp[0] - 7 / 12), abs(wp_mix_cusp[1] - 7 / 12), abs(wp_mix_cusp[2] - 5 / 12))
    wp_err_557 = max(abs(wp_mix_cusp[0] - 5 / 12), abs(wp_mix_cusp[1] - 5 / 12), abs(wp_mix_cusp[2] - 7 / 12))

    # F-02: Actual max |Delta ln| between BIG_RUN_VALUES_v2.json and BIG_RUN_VALUES.json is 0.06769... (0.068), not 0.086
    v1_vals = json.loads(git_show_text("frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/BIG_RUN_VALUES.json"))
    v2_vals = json.loads(git_show_text("frontier/B1940_the_area_options_corrected_in_extended_precision/verification/BIG_RUN_VALUES_v2.json"))
    max_abs_dln_v2_vs_v1 = 0.0
    for opt_k in ("W-|b (area)", "W+|b (area)"):
        for a_v, b_v in zip(v1_vals["options"][opt_k]["values"], v2_vals["options"][opt_k]["values"]):
            max_abs_dln_v2_vs_v1 = max(max_abs_dln_v2_vs_v1, abs(math.log(b_v / a_v)))

    # 2. F-04 (B1942): Exact order-15 torsion map w |-> 6w mod 1 is 8-to-1 (192 / 24 = 8, not 6)
    pts_ord15 = [
        (a, b) for a in range(15) for b in range(15)
        if math.gcd(math.gcd(a, b), 15) == 1
    ]
    fiber_counts: Dict[Tuple[int, int], int] = {}
    for a, b in pts_ord15:
        # w = (a/15, b/15), so 6w = (6a/15, 6b/15) = ((2a mod 5)/5, (2b mod 5)/5)
        img = ((2 * a) % 5, (2 * b) % 5)
        fiber_counts[img] = fiber_counts.get(img, 0) + 1

    # 3. F-05 & F-07 (B1943 & Scoreboard S03): Smith(LR - I), Smith(LR + I), RL fixed line, and m003 (-LR) homology torsion
    LR = [[2, 1], [1, 1]]
    RL = [[1, 1], [1, 2]]
    LR_minus_I = [[LR[0][0] - 1, LR[0][1]], [LR[1][0], LR[1][1] - 1]]
    LR_plus_I = [[LR[0][0] + 1, LR[0][1]], [LR[1][0], LR[1][1] + 1]]
    neg_LR_minus_I = [[-LR[0][0] - 1, -LR[0][1]], [-LR[1][0], -LR[1][1] - 1]]
    smith_lr_m = smith_2x2_exact(LR_minus_I)
    smith_lr_p = smith_2x2_exact(LR_plus_I)
    smith_m003_h1 = smith_2x2_exact(neg_LR_minus_I)
    lr_neg_fixed_mod5 = [
        (x, y) for x in range(5) for y in range(5)
        if (x, y) != (0, 0) and ((2 * x + y) % 5 == (-x) % 5) and ((x + y) % 5 == (-y) % 5)
    ]
    rl_neg_fixed_mod5 = [
        (x, y) for x in range(5) for y in range(5)
        if (x, y) != (0, 0) and ((x + y) % 5 == (-x) % 5) and ((x + 2 * y) % 5 == (-y) % 5)
    ]

    # 4. F-10 (B1934): Unplanting T (quadratic e(x^2/5)) with test_b1934's unphased S gives order 240 != 120; -S gives 120
    w5 = cmath.exp(2j * math.pi / 5.0)
    T_quad = np.diag([w5 ** ((x * x) % 5) for x in range(5)])
    S_nophase = np.array([[w5 ** ((x * y) % 5) for y in range(5)] for x in range(5)], dtype=np.complex128) / math.sqrt(5.0)
    S_weil = -S_nophase  # (-i/sqrt(5)) * (-i)^(-1)? Wait: Gauss sum sum_{x=0}^4 e(x^2/5) = +sqrt(5), inverse DFT needs -1/sqrt(5) or check group order!

    def mat_group_order(gens: List[np.ndarray], cap: int = 400) -> int:
        seen: List[np.ndarray] = [np.eye(gens[0].shape[0], dtype=np.complex128)]
        queue = [seen[0]]
        while queue and len(seen) <= cap:
            cur = queue.pop()
            for g in gens:
                nxt = cur @ g
                if not any(np.max(np.abs(nxt - s)) < 1e-9 for s in seen):
                    seen.append(nxt)
                    queue.append(nxt)
        return len(seen)

    # Check all 8 eighth-root scalar phases on S_nophase to see which gives SL(2, F5) of order 120
    s_phase_orders = {
        k: mat_group_order([cmath.exp(2j * math.pi * k / 8.0) * S_nophase, T_quad], cap=300)
        for k in range(8)
    }

    # 5. F-11 & F-15 (B1935 & B1939): Complex channel residues R_s permute by signed matrices generating S_4 (order 24), while |R_s| generates S_3 (order 6)
    # T: tau -> tau + 1, line (a, b) -> (a, b + a). S: tau -> -1/tau, line (a, b) -> (-b, a).
    # Evaluate directly in mpmath at generic tau = 0.19 + 1.31j and generic line (1/5, 2/5):
    with mp.workdps(70):
        tau0 = mp.mpc(mp.mpf(19) / 100, mp.mpf(131) / 100)
        half = mp.mpf("0.5")

        def residues_four_mp(tau_v: mp.mpc, ap: mp.mpf, bp: mp.mpf, am: mp.mpf, bm: mp.mpf) -> List[mp.mpc]:
            def th(al: mp.mpf, be: mp.mpf) -> mp.mpc:
                at = al - mp.nint(al)
                s = mp.mpc(0)
                for k in range(-18, 19):
                    m = mp.mpf(k) + at
                    s += mp.exp(mp.j * mp.pi * tau_v * (m * m) + 2 * mp.j * mp.pi * m * be)
                return s

            th1p = mp.mpc(0)
            for k in range(18):
                h = mp.mpf(k) + half
                th1p += ((-1) ** k) * (2 * k + 1) * mp.exp(mp.j * mp.pi * tau_v * (h * h))
            th1p *= 2 * mp.pi
            ph1 = mp.exp(-mp.j * mp.pi * (ap + am))
            return [
                (-mp.j) * ph1 * th(ap + half, bp + half) * th(am + half, bm + half) / th1p,
                (-1) * th(ap + half, bp) * th(am + half, bm) / th1p,
                (-1) * ph1 * th(ap, bp + half) * th(am, bm + half) / th1p,
                (+mp.j) * th(ap, bp) * th(am, bm) / th1p,
            ]

        # Generic charges (qL=1, qR=2 -> q+=3, q-=-1) on line (a=1/5, b=2/5) so all 4 residues are non-zero
        a0, b0 = mp.mpf(1) / 5, mp.mpf(2) / 5
        R_base = residues_four_mp(tau0, 3 * a0, 3 * b0, -a0, -b0)
        # Under T: tau -> tau + 1, (a, b) -> (a, b + a)
        R_T = residues_four_mp(tau0 + 1, 3 * a0, 3 * (b0 + a0), -a0, -(b0 + a0))
        # Under S: tau -> -1/tau, (a, b) -> (-b, a)
        R_S = residues_four_mp(-1 / tau0, -3 * b0, 3 * a0, b0, -a0)

        lam_T = R_T[0] / R_base[0]
        lam_S = R_S[0] / R_base[0]
        # Verify R_T / lam_T == [R_1, R_i, R_k, -R_j] and R_S / lam_S == [R_1, -R_j, -R_i, -R_k]
        err_T_signed = max(
            float(abs(R_T[0] / lam_T - R_base[0])),
            float(abs(R_T[1] / lam_T - R_base[1])),
            float(abs(R_T[2] / lam_T - R_base[3])),
            float(abs(R_T[3] / lam_T - (-R_base[2]))),
        )
        err_S_signed = max(
            float(abs(R_S[0] / lam_S - R_base[0])),
            float(abs(R_S[1] / lam_S - (-R_base[2]))),
            float(abs(R_S[2] / lam_S - (-R_base[1]))),
            float(abs(R_S[3] / lam_S - (-R_base[3]))),
        )
        # Also verify B1938 Riemann residue sum identity sum_{s=1}^4 R_s^2 == 0
        riemann_sq_sum_abs = float(abs(sum(r * r for r in R_base)))

    P_T_complex = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]], dtype=np.complex128)
    P_S_complex = np.array([[1, 0, 0, 0], [0, 0, -1, 0], [0, -1, 0, 0], [0, 0, 0, -1]], dtype=np.complex128)
    complex_channel_group_order = mat_group_order([P_T_complex, P_S_complex], cap=100)
    mod_channel_group_order = mat_group_order([np.abs(P_T_complex), np.abs(P_S_complex)], cap=100)

    # F-15 (B1939:119): Serre B[1] T-eigenphases mod 1 are {7/8, 3/8, 1/8} = {1/8, 3/8, 7/8}, matching B1935
    col_lead_k = [min(k for k, cols in SERRE_EXACT_ROWS if cols[c] != (Fraction(0), Fraction(0))) for c in range(3)]
    serre_t_phases_eighths = sorted((k % 8) for k in col_lead_k)

    # 6. F-12 (B1936): Keeping deg_0 = 0 in exterior parity product (-1)^(deg_a + deg_b + deg_h) gives -1 on (deg_0=0, L=4, H=1)
    parity_sign_deg0_L_H = (-1) ** (0 + 4 + 1)

    # 7. F-01 (B1938), F-03 (B1941), F-06 (B1944): Direct check against committed _run.txt and pure-math monotonicity
    b1938_ctrl_txt = git_show_text("frontier/B1938_frame_cs_coupling_is_a_szego_kernel_and_its_read_out_does_not_see_the_gauge_group/verification/gauge_class_control_run.txt")
    b1938_ctrl_max_z = float(re.search(r"max \|z\|\s+([0-9.]+)", b1938_ctrl_txt).group(1))

    b1941_run_txt = git_show_text("frontier/B1941_a_fermion_determinant_prefers_one_higgs_world_at_every_point_and_a_one_loop_trace_the_other/verification/s4_pointwise_run.txt")
    b1941_first_row_min = float(re.search(r"ln det \(3,3,1\) exact\s+\|\s+28/28\s+\|\s+min ([0-9.e+-]+)", b1941_run_txt).group(1))
    # Independent pointwise determinant vs trace check at pt_bulk
    Yu_S_b = np.array([[complex(pt_bulk["per_line_mats"][0]["Yu_S"][r, c]) for c in range(3)] for r in range(3)], dtype=np.complex128)
    Yd_St_b = np.array([[complex(pt_bulk["per_line_mats"][0]["Yd_St"][r, c]) for c in range(3)] for r in range(3)], dtype=np.complex128)
    # W- = (Yu_St, Yd_S, Ye_S), W+ = (Yu_S, Yd_St, Ye_St); colour weights (3, 3, 1) -> 3 ln|det Yu| + (3+1) ln|det Yd| since det Ye = det Yd^T = det Yd
    lndet_wm_minus_wp = (
        3.0 * math.log(abs(np.linalg.det(Yu_np)) / abs(np.linalg.det(Yu_S_b)))
        + 4.0 * math.log(abs(np.linalg.det(Yd_np)) / abs(np.linalg.det(Yd_St_b)))
    )
    neg_tr_h2_wm_minus_wp = -(
        3.0 * (float(np.sum(np.abs(Yu_np) ** 2)) - float(np.sum(np.abs(Yu_S_b) ** 2)))
        + 4.0 * (float(np.sum(np.abs(Yd_np) ** 2)) - float(np.sum(np.abs(Yd_St_b) ** 2)))
    )

    b1944_run_txt = git_show_text("frontier/B1944_the_big_run_read_frame_c_fails_and_the_average_washes_out_the_hierarchy/verification/read_the_look_run.txt")
    b1944_wp_b_line = [ln for ln in b1944_run_txt.splitlines() if "W+|b (area)" in ln][0]
    # Pure-math monotonicity check (0 of 19: zero measured numbers touched!):
    wmb_idx5 = v2_vals["options"]["W-|b (area)"]["values"][5]
    wpb_idx5 = v2_vals["options"]["W+|b (area)"]["values"][5]

    return {
        "M_Haar_covariant_invariance_holds": max_haar_cov_err < 1e-12,
        "M_Haar_max_covariant_err": max_haar_cov_err,
        "M_Haar_broken_su2_scrambles": min_broken_su2_scramble > 0.1,
        "M_B1940_cusp_wm_is_5_5_7_over_12": wm_err_557 < 1e-8,
        "M_B1940_cusp_wp_is_7_7_5_over_12_not_5_5_7": (wp_err_775 < 1e-8) and (wp_err_557 > 0.15),
        "M_B1940_actual_max_dln_is_0068_not_0086": abs(max_abs_dln_v2_vs_v1 - 0.0676938) < 1e-4,
        "M_B1940_actual_max_dln": max_abs_dln_v2_vs_v1,
        "M_B1942_order15_count": len(pts_ord15),
        "M_B1942_order5_image_count": len(fiber_counts),
        "M_B1942_fiber_sizes_unique": sorted(set(fiber_counts.values())),
        "M_B1942_is_8_to_1_not_6_to_1": (len(pts_ord15) == 192 and len(fiber_counts) == 24 and set(fiber_counts.values()) == {8}),
        "M_B1943_smith_LR_minus_I": list(smith_lr_m),
        "M_B1943_smith_LR_plus_I_is_1_5_not_1_3": list(smith_lr_p) == [1, 5],
        "M_B1943_RL_fixes_swapped_line": (lr_neg_fixed_mod5 != rl_neg_fixed_mod5) and (len(rl_neg_fixed_mod5) == 4),
        "M_S03_m003_H1_torsion_is_5_not_1": list(smith_m003_h1) == [1, 5],
        "M_B1934_unphased_S_with_quadratic_T_order": s_phase_orders[0],
        "M_B1934_minus_S_with_quadratic_T_order": s_phase_orders[4],
        "M_B1934_test_passes_even_when_T_unplanted": s_phase_orders[0] == 240,
        "M_B1935_signed_channel_laws_hold": (err_T_signed < 1e-50) and (err_S_signed < 1e-50),
        "M_B1935_complex_Rs_group_order_is_24_S4": complex_channel_group_order == 24,
        "M_B1935_modulus_Rs_group_order_is_6_S3": mod_channel_group_order == 6,
        "M_B1939_serre_S_phases_eighths_are_1_3_7": serre_t_phases_eighths == [1, 3, 7],
        "M_B1936_deg0_yukawa_parity_sign": parity_sign_deg0_L_H,
        "M_B1938_riemann_sq_sum_zero": riemann_sq_sum_abs < 1e-45,
        "M_B1938_control_run_max_z_is_6_4_not_2_4": abs(b1938_ctrl_max_z - 6.4) < 1e-9,
        "M_B1941_run_min_is_1_381_not_1_83": abs(b1941_first_row_min - 1.381) < 1e-3,
        "M_B1941_pointwise_det_pos_trace_neg": (lndet_wm_minus_wp > 0.0) and (neg_tr_h2_wm_minus_wp < 0.0),
        "M_B1944_run_txt_has_17_6_not_7_6": ("17.6" in b1944_wp_b_line) and (" 7.6 " not in b1944_wp_b_line),
        "M_B1944_pure_monotonicity_wpb_gt_wmb": wpb_idx5 > wmb_idx5 > 0.0,
    }


# ============================================================================
# SECTION 4: PURE-MATH SANDBOX EXTRACTION & TARGETED LOCK-MUTATION PROBES
# ============================================================================

def build_sandbox(tmpdir: pathlib.Path) -> Dict[str, Any]:
    """Materialize a pure-math tree from b35eac607 with zero empirical data files (0 of 19)."""
    frontier_dirs: List[str] = []
    for entry in subprocess.check_output(
        ["git", "-C", str(REPO), "ls-tree", "--name-only", f"{PINNED}:frontier"],
        text=True,
    ).splitlines():
        if entry.startswith(FORBIDDEN_EMPIRICAL_PREFIXES):
            continue
        if any(entry.startswith(f"{pref}_") for pref in SANDBOX_B_PREFIXES):
            frontier_dirs.append(f"frontier/{entry}")

    top_mds = [
        e for e in subprocess.check_output(
            ["git", "-C", str(REPO), "ls-tree", "--name-only", PINNED],
            text=True,
        ).splitlines()
        if e.endswith(".md")
    ]
    archive_paths = top_mds + ["docs", "papers", "scripts", "tests"] + frontier_dirs
    proc = subprocess.Popen(
        ["git", "-C", str(REPO), "archive", PINNED, "--"] + archive_paths,
        stdout=subprocess.PIPE,
    )
    subprocess.run(["tar", "-x", "-C", str(tmpdir)], stdin=proc.stdout, check=True)
    proc.wait()
    assert proc.returncode == 0

    # Explicitly delete historical comparison scripts to enforce 0-of-19 firewall
    for rel_rm in [
        "frontier/B1723_the_golden_valley/verification/compare.py",
        "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_coefficients_are_free.py",
    ]:
        p = tmpdir / rel_rm
        if p.exists():
            p.unlink()

    # Verify zero forbidden empirical directories exist anywhere in sandbox
    forbidden_present = [
        p.name for p in (tmpdir / "frontier").iterdir()
        if p.name.startswith(FORBIDDEN_EMPIRICAL_PREFIXES)
    ]
    assert forbidden_present == []
    return {
        "frontier_dir_count": len(frontier_dirs),
        "forbidden_empirical_dirs_present": len(forbidden_present),
    }


def run_pytest(sandbox: pathlib.Path, rel_target: str) -> Dict[str, Any]:
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


def run_lock_and_mutation_suite(sandbox: pathlib.Path) -> Dict[str, Any]:
    arc_lock_targets: List[str] = []
    for arc_num in range(1930, 1945):
        for m in sorted(sandbox.glob(f"frontier/B{arc_num}_*/verification/test_*.py")):
            arc_lock_targets.append(str(m.relative_to(sandbox)))

    extra_targets = [
        "frontier/B1834_the_total_inputs_scoreboard/verification/test_b1834_the_total_inputs_scoreboard.py",
        "tests/test_review_waiver_names_its_anchor.py",
        "tests/test_the_terms_in_short.py",
        "tests/test_negative_second_computation.py",
    ]

    arc_baseline = [run_pytest(sandbox, t) for t in arc_lock_targets]
    extra_baseline = [run_pytest(sandbox, t) for t in extra_targets]

    # Verify B1931 has zero lock files
    b1931_locks = list(sandbox.glob("frontier/B1931_*/verification/test_*.py"))

    # Probe 1 (F-08): test_b1834 fails live at b35eac607 because of "22.0", and passes once "22.0" -> "22"
    b1834_rel = extra_targets[0]
    sb_json_p = sandbox / "docs" / "total_inputs_scoreboard.json"
    sb_md_p = sandbox / "docs" / "TOTAL_INPUTS_SCOREBOARD.md"
    orig_sb_json = sb_json_p.read_text(encoding="utf-8")
    orig_sb_md = sb_md_p.read_text(encoding="utf-8")
    try:
        sb_json_p.write_text(orig_sb_json.replace("22.0", "22"), encoding="utf-8")
        sb_md_p.write_text(orig_sb_md.replace("22.0", "22"), encoding="utf-8")
        b1834_after_strip_22_0 = run_pytest(sandbox, b1834_rel)
    finally:
        sb_json_p.write_text(orig_sb_json, encoding="utf-8")
        sb_md_p.write_text(orig_sb_md, encoding="utf-8")

    # Probe 2 (F-09): B1932 — corrupt W-|b (area) and W+|b (area) in BIG_RUN_VALUES.json (+ update seal sha) -> CANNOT_FAIL;
    # twin control: corrupt W-|a (move count) (+ update seal sha) -> CAUGHT
    b1932_dir = next(sandbox.glob("frontier/B1932_*/verification"))
    brv_p = b1932_dir / "BIG_RUN_VALUES.json"
    brl_p = b1932_dir / "big_run_look.py"
    orig_brv = brv_p.read_text(encoding="utf-8")
    orig_brl = brl_p.read_text(encoding="utf-8")
    b1932_rel = str((b1932_dir / "test_b1932_values_and_seal.py").relative_to(sandbox))
    try:
        d_area = json.loads(orig_brv)
        d_area["options"]["W-|b (area)"]["values"] = [-999.0] * 7
        d_area["options"]["W+|b (area)"]["values"] = [-888.0] * 7
        s_area = json.dumps(d_area)
        brv_p.write_text(s_area, encoding="utf-8")
        h_area = hashlib.sha256(s_area.encode("utf-8")).hexdigest()
        brl_p.write_text(re.sub(r'VALUES_SHA = "[0-9a-f]{64}"', f'VALUES_SHA = "{h_area}"', orig_brl), encoding="utf-8")
        mut_b1932_area = run_pytest(sandbox, b1932_rel)

        d_move = json.loads(orig_brv)
        d_move["options"]["W-|a (move count)"]["values"] = [-999.0] * 7
        s_move = json.dumps(d_move)
        brv_p.write_text(s_move, encoding="utf-8")
        h_move = hashlib.sha256(s_move.encode("utf-8")).hexdigest()
        brl_p.write_text(re.sub(r'VALUES_SHA = "[0-9a-f]{64}"', f'VALUES_SHA = "{h_move}"', orig_brl), encoding="utf-8")
        mut_b1932_move_ctrl = run_pytest(sandbox, b1932_rel)
    finally:
        brv_p.write_text(orig_brv, encoding="utf-8")
        brl_p.write_text(orig_brl, encoding="utf-8")

    # Probe 3 (F-16): B1940 — corrupt area_measure_mp.json directly without touching any seal -> CANNOT_FAIL
    b1940_dir = next(sandbox.glob("frontier/B1940_*/verification"))
    amp_p = b1940_dir / "area_measure_mp.json"
    orig_amp = amp_p.read_text(encoding="utf-8")
    b1940_rel = str((b1940_dir / "test_b1940_corrected_values_and_v3.py").relative_to(sandbox))
    try:
        amp_p.write_text('{"corrupted": [-999.0]}', encoding="utf-8")
        mut_b1940_amp = run_pytest(sandbox, b1940_rel)
    finally:
        amp_p.write_text(orig_amp, encoding="utf-8")

    # Probe 4 (F-14): B1938 — shift lhs - rhs by -100.0 on all 12 rows in residue_as_determinants.py -> CANNOT_FAIL
    b1938_dir = next(sandbox.glob("frontier/B1938_*/verification"))
    rad_p = b1938_dir / "residue_as_determinants.py"
    orig_rad = rad_p.read_text(encoding="utf-8")
    b1938_rel = str((b1938_dir / "test_b1938_coupling_and_gauge_class.py").relative_to(sandbox))
    try:
        rad_p.write_text(orig_rad.replace("lhs - rhs, small, tail", "lhs - rhs - 100.0, small, tail"), encoding="utf-8")
        mut_b1938_neg100 = run_pytest(sandbox, b1938_rel)
    finally:
        rad_p.write_text(orig_rad, encoding="utf-8")

    # Probe 5 (F-06): B1944 — corrupt all non-chi2_seven cells on W+|b row of B1944/FINDINGS.md -> CANNOT_FAIL
    b1944_dir = next(sandbox.glob("frontier/B1944_*"))
    b1944_f_p = b1944_dir / "FINDINGS.md"
    orig_b1944_f = b1944_f_p.read_text(encoding="utf-8")
    b1944_rel = str((b1944_dir / "verification" / "test_b1944_the_look_read.py").relative_to(sandbox))
    try:
        b1944_f_p.write_text(
            orig_b1944_f.replace(
                "| W₊∣b | 59.3 | 3 310 | 11.3 | 15.6 | 1.21 | 7.6 | 80.9 |",
                "| W₊∣b | 9999 | 99999 | 9999 | 9999 | 9999 | 999 | 9999 |",
            ),
            encoding="utf-8",
        )
        mut_b1944_table = run_pytest(sandbox, b1944_rel)
    finally:
        b1944_f_p.write_text(orig_b1944_f, encoding="utf-8")

    # Probe 6 (F-17, F-18, F-20): Subprocess probe of B1930 7th distinct path & gates.py bypasses
    gate_probe_code = r"""
import importlib.util, json, os, pathlib, sys
sb = pathlib.Path(sys.argv[1])
sys.dont_write_bytecode = True

# 1. B1930: distinct 7th moved path in GENESIS.md section 1 is NOT refused by W.version_1_68
b1930_t = next(sb.glob("frontier/B1930_*/verification/test_b1930_the_foundation_at_version_1_68.py"))
spec30 = importlib.util.spec_from_file_location("t30", b1930_t)
m30 = importlib.util.module_from_spec(spec30); spec30.loader.exec_module(m30)
base_167 = m30._taken_back(m30._at_1_68((sb / "GENESIS.md").read_text(encoding="utf-8")))
k = base_167.index("## 1. The principle")
distinct_7th = base_167[:k] + "See `philosophy/P999_unlisted_moved_note.md`.\n\n" + base_167[k:]
seventh_refused = False
try:
    _ = m30.W.version_1_68(distinct_7th)
except AssertionError:
    seventh_refused = True

# 2. gates.py probes
spec_g = importlib.util.spec_from_file_location("gates_probe", sb / "scripts" / "gates" / "gates.py")
g = importlib.util.module_from_spec(spec_g); spec_g.loader.exec_module(g)

# 2a (F-17): Removing PROVISIONAL from B1944 in negative_without_second bypasses gate via cites_seat[0]
b1944_v_rel = str(next(sb.glob("frontier/B1944_*/arc_verdict.json")).relative_to(sb)).replace("\\", "/")
b1944_f_rel = str(next(sb.glob("frontier/B1944_*/FINDINGS.md")).relative_to(sb)).replace("\\", "/")
v44 = json.loads((sb / b1944_v_rel).read_text(encoding="utf-8"))
v44["claim_one_line"] = v44["claim_one_line"].replace("PROVISIONAL until SM-C15 re-runs it", "settled")
v44["scope"]["hypotheses"] = "read under B1937"
f44 = (sb / b1944_f_rel).read_text(encoding="utf-8").replace("PROVISIONAL", "settled")
def reader_no_prov(rel):
    rel_n = rel.replace("\\", "/")
    if rel_n == b1944_v_rel:
        return json.dumps(v44)
    if rel_n == b1944_f_rel:
        return f44
    return (sb / rel_n).read_text(encoding="utf-8")
b1944_flagged_without_provisional = any(x[0] == "B1944" for x in g.negative_without_second(reader_no_prov))

# 2b (F-20): selection_claims_in parenthetical split false negative & false positive
sel_fn_bypass = (g.selection_claims_in("The census selects (B1906) m004.") == [])
sel_fp_denial_split = bool(g.selection_claims_in("No rule (B1204) selects one member."))

# 2c (F-20): public_face_words ignores curly quotes & public_face_unentered misses new inner word on line 1249
ctx_txt = (sb / "docs" / "views" / "CONTEXT_RECOVERY.md").read_text(encoding="utf-8")
pf_with_quotes = sum(g.public_face_words(ctx_txt).values())
pf_without_quotes = sum(g.public_face_words(ctx_txt.replace("\u201c", "").replace("\u201d", "")).values())
real_pf = {rel: (sb / rel).read_text(encoding="utf-8") for rel in g.PUBLIC_FACE_FROZEN + (g.PUBLIC_FACE_ERRATA,)}
tex_lines = real_pf["papers/P3_THE_PAPER/main.tex"].split("\n")
tex_lines[1248] = tex_lines[1248] + " as the owner's lane ruled"
mut_pf = dict(real_pf, **{"papers/P3_THE_PAPER/main.tex": "\n".join(tex_lines)})
errata_line1249_unentered = g.public_face_unentered(reader=mut_pf.get)

# 2d (F-20): test_review_waiver_names_its_anchor line 59 'if a' drops None when mixed with one valid anchor
written_anchors = ["aaaaaaa11"]
mixed_anchors = ["aaaaaaa11", None]
waiver_line59_passes_none = all(a in written_anchors for a in mixed_anchors if a)

print(json.dumps({
    "b1930_distinct_7th_path_not_refused": not seventh_refused,
    "b1944_without_provisional_bypasses_gate": not b1944_flagged_without_provisional,
    "selection_paren_false_negative": sel_fn_bypass,
    "selection_paren_false_positive": sel_fp_denial_split,
    "public_face_curly_quotes_noop": (pf_with_quotes == pf_without_quotes) and (pf_with_quotes > 0),
    "errata_existing_line_new_inner_word_bypasses": errata_line1249_unentered == [],
    "waiver_if_a_drops_none_anchor": waiver_line59_passes_none,
}))
"""
    gate_probes = json.loads(
        subprocess.check_output([sys.executable, "-B", "-c", gate_probe_code, str(sandbox)], text=True)
    )

    return {
        "arc_locks_total": len(arc_baseline),
        "arc_locks_passed_count": sum(1 for r in arc_baseline if r["passed"]),
        "b1931_lock_count": len(b1931_locks),
        "arc_baseline": arc_baseline,
        "extra_baseline": extra_baseline,
        "b1834_fails_live_at_b35eac607": not extra_baseline[0]["passed"],
        "b1834_passes_once_22_0_stripped": b1834_after_strip_22_0["passed"],
        "mut_b1932_area_corrupted_still_passes": mut_b1932_area["passed"],
        "mut_b1932_move_corrupted_caught": not mut_b1932_move_ctrl["passed"],
        "mut_b1940_area_mp_corrupted_still_passes": mut_b1940_amp["passed"],
        "mut_b1938_minus100_diff_still_passes": mut_b1938_neg100["passed"],
        "mut_b1944_48_cells_corrupted_still_passes": mut_b1944_table["passed"],
        "gate_and_lock_probes": gate_probes,
    }


# ============================================================================
# SECTION 5: GOVERNANCE, METADATA, SWEEP & LEDGER HYGIENE CHECKS AT b35eac607
# ============================================================================

def run_governance_and_doc_checks() -> Dict[str, Any]:
    # 1. B1937 test count & non-planted count
    t37_txt = git_show_text("frontier/B1937_the_big_runs_rule_amended_before_the_look/verification/test_b1937_rule_v2.py")
    t37_defs = re.findall(r"^def (test_\w+)\(", t37_txt, re.M)
    t37_reads_real = ("BIG_RUN_VALUES.json" in t37_txt) and ("second_computations_run.txt" in t37_txt)
    b1937_f = git_show_text("frontier/B1937_the_big_runs_rule_amended_before_the_look/FINDINGS.md")
    rule_v2 = git_show_text("frontier/B1937_the_big_runs_rule_amended_before_the_look/verification/BIG_RUN_RULE_v2.md")

    # 2. B1928 stale header at b35eac607
    b1928_f_line3 = git_show_text("frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/FINDINGS.md").splitlines()[2]
    b1928_v = json.loads(git_show_text("frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/arc_verdict.json"))["verdict"]

    # 3. B1944 read_the_look.py file count vs FINDINGS.md:32 ("reads only those three files")
    rtl_py = git_show_text("frontier/B1944_the_big_run_read_frame_c_fails_and_the_average_washes_out_the_hierarchy/verification/read_the_look.py")
    rtl_read_calls = len(re.findall(r"read_text\(", rtl_py))

    # 4. BLIND_ARCS.md vs arc_verdict.json instrument flag on B1937 and B1944
    blind_arcs = git_show_text("docs/atlas/BLIND_ARCS.md")
    v37_inst = json.loads(git_show_text("frontier/B1937_the_big_runs_rule_amended_before_the_look/arc_verdict.json"))["instrument"]
    v44_inst = json.loads(git_show_text("frontier/B1944_the_big_run_read_frame_c_fails_and_the_average_washes_out_the_hierarchy/arc_verdict.json"))["instrument"]
    ba_37_line = [ln for ln in blind_arcs.splitlines() if ln.startswith("| B1937 ")][0]
    ba_44_line = [ln for ln in blind_arcs.splitlines() if ln.startswith("| B1944 ")][0]

    # 5. THE_SWEEP_OF_2026-11-14.md offrecord_origin=true missing on S111..S113
    sweep = git_show_text("docs/THE_SWEEP_OF_2026-11-14.md")
    offrecord_body_occurrences = sweep[:sweep.index("## Doubtful")].count("offrecord_origin")

    # 6. HARVEST_LEDGER.md stale OWED rows after B1939 & missing @ commit pins on cited rows
    hl = git_show_text("docs/HARVEST_LEDGER.md")
    hl_rows = {}
    for ln in hl.splitlines():
        if ln.startswith("| "):
            cols = [c.strip() for c in ln.split("|")[1:-1]]
            if cols and cols[0].isdigit():
                hl_rows[int(cols[0])] = cols
    b1939_stale_owed_rows = [
        r for r in (1676, 1677, 1678, 1696, 1709, 1710, 1749, 1815)
        if "OWED" in hl_rows.get(r, ["", "", "", "", "", ""])[5]
    ]
    cited_unpinned_rows = [
        r for r in (1755, 1768, 1794, 1797, 1800, 1801, 1802, 1804)
        if "@" not in hl_rows.get(r, ["", "", "", "", ""])[4]
    ]

    # 7. Scoreboard basis 300-char truncation check on C02 and C06
    sb_json = json.loads(git_show_text("docs/total_inputs_scoreboard.json"))
    sb_md = git_show_text("docs/TOTAL_INPUTS_SCOREBOARD.md")
    c_joints = {j["id"]: j for j in sb_json["frames"]["C"]["joints"]}
    c02_truncated = len(c_joints["C02"]["basis"]) > 300 and ("| C02 |" in sb_md) and (c_joints["C02"]["basis"][-15:] not in sb_md)
    c06_truncated = len(c_joints["C06"]["basis"]) > 300 and ("| C06 |" in sb_md) and (c_joints["C06"]["basis"][-15:] not in sb_md)

    return {
        "b1937_actual_test_count": len(t37_defs),
        "b1937_reads_real_committed_files": t37_reads_real,
        "b1937_findings_line76_stale_A1_to_A12": "A1 to A12" in b1937_f and "### A15." in rule_v2,
        "b1937_rule_v2_stale_nine_joints": "nine joints" in rule_v2,
        "b1928_header_still_open_while_verdict_proved": ("**Verdict: OPEN**" in b1928_f_line3) and (b1928_v == "PROVED"),
        "b1944_read_the_look_actual_files_read": rtl_read_calls,
        "blind_arcs_b1937_b1944_instrument_mismatch": (v37_inst is False and "INSTRUMENT" in ba_37_line and v44_inst is False and "INSTRUMENT" in ba_44_line),
        "sweep_offrecord_tag_occurrences_in_body": offrecord_body_occurrences,
        "b1939_harvest_rows_still_marked_owed": b1939_stale_owed_rows,
        "cited_harvest_rows_missing_commit_pin": cited_unpinned_rows,
        "scoreboard_c02_and_c06_truncated_at_300_chars": bool(c02_truncated and c06_truncated),
    }


def main() -> int:
    c1 = run_control_c_r83_1()
    c2 = run_control_c_r83_2()
    c3 = run_control_c_r83_3()

    quote_results = []
    for q in FINDINGS_QUOTES:
        chk = check_single_quote(q["path"], q["line"], q["quote"], PINNED)
        quote_results.append({
            "id": q["id"],
            "criterion": q["criterion"],
            "item": q["item"],
            **chk,
        })
    all_quotes_exact = all(r["exact_match"] for r in quote_results)

    math_checks = run_independent_math_checks()
    gov_checks = run_governance_and_doc_checks()

    with tempfile.TemporaryDirectory() as td:
        tdp = pathlib.Path(td)
        sb_info = build_sandbox(tdp)
        lock_and_mut = run_lock_and_mutation_suite(tdp)

    all_controls_passed = bool(c1["passed"] and c2["passed"] and c3["passed"])

    out_obj = {
        "pinned_commit": PINNED,
        "window_base": WINDOW_BASE,
        "controls": {
            "C-R83-1": c1,
            "C-R83-2": c2,
            "C-R83-3": c3,
            "all_controls_passed": all_controls_passed,
        },
        "quote_verification": {
            "total_quotes": len(quote_results),
            "exact_matches": sum(1 for r in quote_results if r["exact_match"]),
            "all_exact": all_quotes_exact,
            "results": quote_results,
        },
        "sandbox_info": sb_info,
        "lock_and_mutation_suite": lock_and_mut,
        "independent_math_checks": math_checks,
        "governance_and_doc_checks": gov_checks,
    }

    OUT_PATH.write_text(json.dumps(out_obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    # Mask-clean stdout summary: booleans and integer counts only (zero decimals, zero scientific notation)
    print(f"PINNED_COMMIT_CHECKED={PINNED}")
    print(f"ALL_CONTROLS_PASSED={all_controls_passed}")
    print(f"QUOTES_EXACT={sum(1 for r in quote_results if r['exact_match'])}_OF_{len(quote_results)}")
    print(f"ARC_LOCKS_PASSED={lock_and_mut['arc_locks_passed_count']}_OF_{lock_and_mut['arc_locks_total']}")
    print(f"B1834_FAILS_LIVE={lock_and_mut['b1834_fails_live_at_b35eac607']}")
    return 0 if (all_controls_passed and all_quotes_exact) else 1


if __name__ == "__main__":
    raise SystemExit(main())
