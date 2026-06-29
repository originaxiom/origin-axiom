"""B295 verdict (pyenv) -- the SSB / gauge status of the CP sign (Chat-2 adjudicated). Imports the ssb_gauge.py
kernel (sympy) and adjudicates Chat-2's reframe verify-don't-trust.

Chat-2: the CP-sign externality (B289) is NOT a Curie wall but an SSB loophole + gauge redundancy (tau gauged ->
sign pure gauge). Verdict:
  - CORRECT: Curie is not a hard wall (SSB under a running control parameter is the loophole). Corrects P011/B286.
  - UNSUPPORTED: the SSB 'tau-symmetric double-well potential' is ABSENT -- the program's V(tau) (P15/P16) is the
    MODULAR-tau, GOLDEN (Q(sqrt5)), SINGLE-well object, disjoint from the EISENSTEIN +-pi/6 vacua (Q(sqrt-3)). The
    conflation of the two tau's is the trap. SSB-availability is not demonstrated.
  - STOP-GATE: 'tau is gauged' rests on B279's unverified parity-anomaly link (NEEDS-SPECIALIST). The 'pure gauge'
    conclusion is conditional on it.
  NET: B289 stands (the sign is external); the REASON is OPEN (not Curie, not established gauge). The honest
  statement: the sign is not object-derivable because the object is CP-symmetric, and no symmetry-breaking mechanism
  (SSB or gauge-fixing) is established in-sandbox. The dynamical-gauge-fixing question (does running k fix the sign?)
  is the live frontier -- specialist-gated.

FIREWALL: SSB/gauge/baryon physics is HELD/[LEAP] in speculations/. Nothing to CLAIMS.
"""
import importlib.util
import pathlib

_K = pathlib.Path(__file__).resolve().parent / "ssb_gauge.py"
_spec = importlib.util.spec_from_file_location("b295_kernel", _K)
ssb = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(ssb)

# --- adjudication flags (re-exported from the kernel) ---
CURIE_IS_A_HARD_WALL = ssb.CURIE_IS_A_HARD_WALL          # False -> corrects P011/B286 over-statement
SSB_POTENTIAL_PRESENT = ssb.SSB_POTENTIAL_PRESENT        # False -> the wrong-tau / golden / single-well catch
TAU_GAUGED_IS_VERIFIED = ssb.TAU_GAUGED_IS_VERIFIED      # False -> stop-gate (B279 [LEAP])
SIGN_IS_EXTERNAL = ssb.SIGN_IS_EXTERNAL                  # True  -> B289 stands
SIGN_MECHANISM_ESTABLISHED = ssb.SIGN_MECHANISM_ESTABLISHED   # False -> open (neither SSB nor gauge-fixing shown)
DERIVES_SM_VALUES = ssb.DERIVES_SM_VALUES                # False -> firewall

STOP_GATES = ["tau is gauged (B279 parity-anomaly link unverified)",
              "does running k dynamically gauge-fix the tau-sign? (the live frontier; trajectory specialist-gated)"]


def verdict():
    rf, cp, phases = ssb.cp_vacua()
    import sympy as sp
    vacua_ok = (sp.Abs(phases[0]) == sp.pi/6 and sp.Abs(phases[1]) == sp.pi/6 and phases[0] == -phases[1])
    crit, kinds = ssb.potential_critical_points()
    single_well = sorted(kinds.values()) == ["max", "min"]      # one min + one max = single-well (not double-well)
    potential_wrong = ssb.vacua_disjoint_from_potential() and not SSB_POTENTIAL_PRESENT
    return bool(vacua_ok and single_well and potential_wrong
                and not CURIE_IS_A_HARD_WALL                    # Curie refuted as a hard wall
                and not TAU_GAUGED_IS_VERIFIED                  # gauge premise gated
                and SIGN_IS_EXTERNAL and not SIGN_MECHANISM_ESTABLISHED
                and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("Curie is a hard wall:", CURIE_IS_A_HARD_WALL, "(SSB loophole -> corrects P011/B286)")
    print("SSB double-well potential present:", SSB_POTENTIAL_PRESENT, "(wrong-tau/golden/single-well catch)")
    print("'tau is gauged' verified:", TAU_GAUGED_IS_VERIFIED, "(STOP-GATE: B279 [LEAP])")
    print("sign external:", SIGN_IS_EXTERNAL, "| mechanism established:", SIGN_MECHANISM_ESTABLISHED, "(open)")
    print("stop-gates:", STOP_GATES)
    print("verdict:", verdict())
