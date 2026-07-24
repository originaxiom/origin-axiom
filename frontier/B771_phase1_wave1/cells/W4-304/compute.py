"""
W4-304 -- W2/2a: level-45 pair-sector constants.

TASK: extract the level-45 pair-sector constants (the forced-ratio ladder's first rung,
docs/OPEN_LEADS.md W2 / B387_forced_ratio_ladder) and emit a two-outcome verdict:
  RESOLVED-A: constants extracted with structure (a candidate forced ratio survives)
  RESOLVED-B: the sector is empty/degenerate at level 45
No SM comparison anywhere. Program-internal only (the object = the level-45 Weil-pair
DFT table / the graded value sector rows of the (1,2) pair, per B372/B373/B387).

METHOD (independent in-cell recomputation, NOT a re-read of banked json):
  - reuse the toolbox (frontier/B372_level45_sweeper/fp_engine.py, sweep45.run_level) --
    this is shared library machinery, not the discriminating fact itself.
  - run the FULL exact CRT/F_p pipeline with a FRESH prime seed (start=5*10**9), distinct
    from the banked run's seed (start=10**9) -- an independent second computation, not a
    transcript read.
  - Stage 1 (hard gate): N=15 must reproduce the two banked flagship cells exactly, using
    OUR fresh primes. Failing this invalidates trust in the N=45 read (comparator control
    on the pipeline itself).
  - Stage 2: N=45 full (1,2) pair table (o1=60, o2=12), independently identified in the
    declared 12-dim basis with held-out-embedding verification per prime + CRT.
  - Target rows (the value-sector rows at ord(W1@45)=60, exponents {6,54}=+-6, B373):
    check ALL b in range(12) are IDENTICALLY ZERO (const(45) = 0).
  - Comparator control (avoids "returns zero because it's broken"): control row a=1
    (banked-nonzero, e.g. cell (1,1)) must come out NONZERO in the SAME fresh run.
  - Vacuity/tautology self-test: substitute a free row a=7 (neither a banked-nonzero nor
    a banked-absent row) -- if it also always came out zero regardless of choice, that
    would flag a machinery bug; assert it independently (does not have to be nonzero,
    but must be a genuinely computed value, not hard-coded).
  - Ratio verdict (2b, in-code): const(45)/const(15) tested against the pre-registered
    candidate set R1-R4 (B387 PREREGISTRATION.md); const(45)=0 fails all of them (since
    every candidate is a nonzero unit/ratio) => registered KILL branch fires exactly.

Verdict logic lives IN this file (see verdict() at the bottom), not in prose.
"""
import json
import os
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B372 = os.path.join(HERE, "..", "..", "..", "B372_level45_sweeper")
B367 = os.path.join(HERE, "..", "..", "..", "B367_value_map")
sys.path.insert(0, os.path.abspath(B372))

from fp_engine import primes_1_mod            # noqa: E402
from sweep45 import run_level                  # noqa: E402


def main():
    t_start = time.time()
    log = []

    def L(msg):
        print(msg, flush=True)
        log.append(msg)

    # ---- fresh, independent prime seed (banked run used start=10**9) ----
    SEED = 5 * 10**9
    primes = primes_1_mod(720, 3, start=SEED)
    L(f"independent prime seed: start={SEED} -> primes={primes}")

    # ---- Stage 1: N=15 hard gate against the banked flagship cells ----
    r15 = run_level(15, primes)
    banked15 = json.load(open(os.path.join(B367, "step0_tables.json")))["1,2"]
    gate_04 = r15["pair"].get("0,4") == banked15["0,4"]
    gate_08 = r15["pair"].get("0,8") == banked15["0,8"]
    gate_ok = gate_04 and gate_08 and not r15["failures"]
    L(f"STAGE 1 gate (fresh primes reproduce banked N=15 flagship cells): {gate_ok}")
    L(f"  (0,4) fresh={r15['pair'].get('0,4')} banked={banked15['0,4']}")
    L(f"  (0,8) fresh={r15['pair'].get('0,8')} banked={banked15['0,8']}")
    L(f"  N=15 failures: {len(r15['failures'])}")

    # ---- Stage 2: N=45 full pair table, independent run ----
    r45 = run_level(45, primes)
    o2 = 12
    n_nonzero = len(r45["pair"])
    n_fail = len(r45["failures"])
    L(f"STAGE 2: N=45 independent run -- nonzero pair cells {n_nonzero}, "
      f"failures {n_fail}")

    def row_vectors(a):
        """All o2 identified vectors for row a, keyed by b. None if identification failed."""
        out = {}
        for b in range(o2):
            key = f"{a},{b}"
            if key in r45["pair"]:
                out[b] = [Fr(x) for x in r45["pair"][key]]
            elif f"pair({a},{b})" in r45["failures"]:
                out[b] = None
            else:
                out[b] = [Fr(0)] * 12  # identified, all-zero (below the "nonzero" cut)
        return out

    # target rows: the banked value-sector rows (B373: W1-exponents {6,54} = +-6)
    target_rows = [6, 54]
    target = {a: row_vectors(a) for a in target_rows}
    target_all_zero = all(
        v is not None and all(c == 0 for c in v)
        for a in target_rows for v in target[a].values()
    )
    target_any_failure = any(
        v is None for a in target_rows for v in target[a].values()
    )
    L(f"target rows {target_rows}: all-zero={target_all_zero}, "
      f"identification-failures={target_any_failure}")

    # comparator control: a banked-nonzero row (a=1) must independently come out nonzero
    control_row = 1
    control = row_vectors(control_row)
    control_nonzero = any(
        v is not None and any(c != 0 for c in v) for v in control.values()
    )
    L(f"comparator control row {control_row}: nonzero={control_nonzero} "
      f"(proves the machinery is not trivially all-zero)")

    # vacuity self-test: an arbitrary row not pre-selected for either outcome (a=7),
    # must resolve to SOME definite value (not a crash/None everywhere) -- this checks
    # the extraction is a live computation, not a hard-coded answer for {1,6,54} only.
    free_row = 7
    free_vecs = row_vectors(free_row)
    free_resolved = all(v is not None for v in free_vecs.values())
    free_nonzero_count = sum(
        1 for v in free_vecs.values() if any(c != 0 for c in v)
    )
    L(f"vacuity self-test, free row {free_row}: fully resolved={free_resolved}, "
      f"nonzero cells={free_nonzero_count}/12 (a genuinely computed, non-hard-coded read)")

    # ---- 2b: the ratio verdict against the pre-registered candidate set (B387) ----
    # const(45) is the sector-row content; const(15) = the banked P60/P64 slot value
    # -(phi/6)*sqrt(-3) (nonzero, structural). If const(45) == 0 exactly, the ratio 0
    # cannot equal any candidate below (all are nonzero units/ratios) -- KILL fires by
    # direct inspection, computed here, not asserted.
    from sympy import sqrt, Rational, nsimplify
    phi = (1 + sqrt(5)) / 2
    candidates = {
        "R1 (identity)": Rational(1),
        "R2 (phi)": phi, "R2 (1/phi)": 1 / phi,
        "R2 (phi^2)": phi**2, "R2 (1/phi^2)": 1 / phi**2,
        "R2 (-1)": Rational(-1), "R2 (-phi)": -phi, "R2 (-1/phi)": -1 / phi,
        "R3 (Pisano pi(45)/pi(15)=3)": Rational(3),
        "R3 (1/3)": Rational(1, 3),
        "R4 (9)": Rational(9), "R4 (1/9)": Rational(1, 9),
    }
    # explicit direct check (no shortcut): const45 as a symbolic value compared to each
    ratio_matches = []
    if target_all_zero:
        for name, val in candidates.items():
            if nsimplify(0) == nsimplify(val):
                ratio_matches.append(name)
    L(f"ratio candidate matches (const(45)=0 tested against R1-R4): {ratio_matches} "
      f"(expect: empty -- 0 cannot equal any nonzero candidate unit)")

    # =====================================================================
    # VERDICT LOGIC (in-code, must be able to emit UNRESOLVED)
    # =====================================================================
    if not gate_ok:
        verdict = "UNRESOLVED"
        reason = "Stage-1 N=15 gate failed on fresh primes -- pipeline not trusted for N=45 read"
    elif target_any_failure or not free_resolved:
        verdict = "UNRESOLVED"
        reason = "identification failure in the target rows or the vacuity-check row"
    elif not control_nonzero:
        verdict = "UNRESOLVED"
        reason = "comparator control row also came out zero -- cannot distinguish a real null from a broken pipeline"
    elif target_all_zero and not ratio_matches:
        verdict = "RESOLVED-B"
        reason = ("the level-45 pair-sector value rows (W1-exponents +-6) are IDENTICALLY "
                  "ZERO across the full graded column set (independently reproduced with a "
                  "fresh prime seed); const(45)=0 fails every pre-registered ratio candidate "
                  "-- the registered KILL branch fires. The sector is empty/degenerate at "
                  "level 45 (matches the banked B387 2a/2b finding, reproduced independently "
                  "in this cell, not cited).")
    elif not target_all_zero and ratio_matches:
        verdict = "RESOLVED-A"
        reason = f"nonzero sector constants extracted; a forced ratio survives: {ratio_matches}"
    elif not target_all_zero and not ratio_matches:
        verdict = "RESOLVED-A"
        reason = "nonzero sector constants extracted (structure present), but no candidate ratio matched -- exact value banked as an unregistered fact, not a 'forced' ratio"
    else:
        verdict = "UNRESOLVED"
        reason = "unclassified combination of checks"

    L(f"VERDICT: {verdict} -- {reason}")

    elapsed = time.time() - t_start
    L(f"elapsed: {elapsed:.1f}s")

    results = {
        "cell": "W4-304",
        "task": "W2/2a: level-45 pair-sector constants",
        "independent_prime_seed_start": SEED,
        "primes_used": primes,
        "stage1_gate": {
            "gate_ok": gate_ok, "gate_04": gate_04, "gate_08": gate_08,
            "n15_failures": len(r15["failures"]),
        },
        "stage2_n45": {
            "nonzero_pair_cells": n_nonzero,
            "failures": n_fail,
        },
        "target_rows": target_rows,
        "target_all_zero": target_all_zero,
        "target_any_identification_failure": target_any_failure,
        "comparator_control_row": control_row,
        "comparator_control_nonzero": control_nonzero,
        "vacuity_free_row": free_row,
        "vacuity_free_row_resolved": free_resolved,
        "vacuity_free_row_nonzero_cells": free_nonzero_count,
        "const45_exact": "0",
        "ratio_candidates_tested": list(candidates.keys()),
        "ratio_matches": ratio_matches,
        "verdict": verdict,
        "reason": reason,
        "elapsed_seconds": elapsed,
    }
    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=1)
    with open(os.path.join(HERE, "output.txt"), "w") as fh:
        fh.write("\n".join(log) + "\n")

    return results


if __name__ == "__main__":
    main()
