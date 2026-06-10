"""B151 -- firewall confirmation (L15): does any quantity carry a SCALE across the (now real) L14 bridge?

L14 (B150) established that the unit's SL(2,Z) symmetry IS a known duality action (N=2* / class-S) at the character-
variety level -- FORCED, primary-source-verified. That bridge is REAL, which is exactly why the firewall must now be
tested hardest: a real symmetry bridge makes a scale-crossing feel more plausible than it is. L15 is a READING task (how
the primary sources ASSIGN UNITS), not a sandbox task -- the sandbox only re-asserts the unit's anchor numbers, which
cannot themselves give the verdict.

THE ONE QUESTION. In the 3d-3d correspondence applied to the figure-eight bundle (the unit, monodromy RL), does the
complex volume / Chern-Simons invariant enter the partition function ONLY as a dimensionless exponent ~exp[(1/hbar) i
Vol_C], with ALL dimensionful content carried by hbar<->k (the level) and the squashing / lens-space radius -- and NONE
by the invariant itself?

THE BLADE. A SYMMETRY identification is not a SCALE. On every claim: does a dimensionful quantity attach to the INVARIANT
itself, or only to hbar/k and the radius? "The partition function has units" is NOT a crossing -- the units are in
hbar/k/radius. A crossing requires the INVARIANT to carry the scale; report one only with the exact primary-text location
where a dimensionful quantity attaches to the invariant.

VERDICT (from the reading) = FIREWALL HOLDS. All dimensionful/continuous content sits in hbar<->k and the squashing/lens
radius; the complex volume enters only as a dimensionless element of C/4pi^2 Z in the exponent. No kappa-type or volume-
type invariant of the unit can source a physical scale. The unification is mathematical (the L14 symmetry identity) and
TERMINATES at the firewall -- a real bridge (L14) + a confirmed wall (L15) is the honest boundary of the picture's reach.
This BANKS the firewall HOLDING (a real result), NOT a crossing. MATH tier; firewalled; nothing to CLAIMS.md.
"""
from __future__ import annotations

# Recorded anchor (figure-eight 4_1, SnapPy complex_volume; re-runnable -- see figure_eight_complex_volume()).
VOL_FIG8 = 2.0298832128193   # = 2 * V_tet, the minimal cusped hyperbolic volume
CS_FIG8 = 0.0                 # amphichiral => Chern-Simons invariant vanishes (numerically ~ -1.1e-15)
INVARIANT_SPACE = "C/4pi^2 Z (SL2 ; C/pi^2 Z for PSL2) -- a dimensionless complex number mod a lattice"

# The candidate scale-carrier is the Chern-Simons part (orientation-sensitive / P-odd, tied to the chirality axis).
# For the figure-eight CS = 0 identically, so the unit's complex volume is PURELY the real hyperbolic volume -- no CS
# content to carry anything across. The unit is the LEAST likely object to carry a scale.
CS_PRESTRENGTHENING = ("CS=0 for the figure-eight (amphichiral): the candidate scale-carrier (the CS/P-odd part) vanishes "
                       "identically, so Vol+iCS is purely the real hyperbolic volume -- the firewall is, if anything, "
                       "stronger for this specific object.")

# The reading: per primary source, WHAT carries the units, and the tag. CROSSING requires `exhibited_text` (none found).
FIREWALL_READING = [
    {"source": "arXiv:1111.2828 (Garoufalidis-Thurston-Zickert, Duke 2015)",
     "claim": "the Cheeger-Chern-Simons invariant c-hat(rho) = i(Vol+iCS) is an element of C/4pi^2 Z, via Neumann's "
              "extended Bloch group (Rogers dilogarithm)",
     "what_carries_units": "(none) -- a dimensionless element of a quotient of C by a lattice; geometric size in "
                           "curvature units (curvature = -1, length = 1), not energy/mass/length",
     "tag": "FIREWALL_HOLDS",
     "exhibited_text": ""},
    {"source": "arXiv:1409.0857 (Dimofte, Complex Chern-Simons at level k via the 3d-3d correspondence)",
     "claim": "a state-integral model for SL(n,C) CS AT LEVEL k; partition functions of T_n[M] on squashed lens spaces "
              "L(k,1); the complex volume is the semiclassical saddle in the exponent",
     "what_carries_units": "the level k (<-> hbar) and the lens-space / squashing geometry -- NOT the invariant; the "
                           "invariant Vol_C is the fixed exponent saddle",
     "tag": "FIREWALL_HOLDS",
     "exhibited_text": ""},
    {"source": "arXiv:1305.2891 (Cordova-Jafferis, Complex Chern-Simons from M5-branes on the Squashed Three-Sphere)",
     "claim": "'a squashing parameter in the geometry controls the imaginary part of the complex Chern-Simons level'",
     "what_carries_units": "the squashing parameter b and the level -- NOT the invariant",
     "tag": "FIREWALL_HOLDS",
     "exhibited_text": ""},
]

TAGS = {"FIREWALL_HOLDS", "CROSSING"}


def figure_eight_complex_volume():
    """The unit's anchor: (Vol, CS) of the figure-eight via SnapPy, when available. Returns (vol, cs, live:bool).
    The verdict is NOT computed here -- it is a fact about how the papers assign units (FIREWALL_READING)."""
    try:
        import snappy
        cv = snappy.Manifold("4_1").complex_volume()
        return float(cv.real()), float(cv.imag()), True
    except Exception:
        return VOL_FIG8, CS_FIG8, False


def verdict():
    crossings = [r for r in FIREWALL_READING if r["tag"] == "CROSSING"]
    holds = (not crossings) and all(r["tag"] == "FIREWALL_HOLDS" for r in FIREWALL_READING)
    return {
        "verdict": "FIREWALL_HOLDS" if holds else "CROSSING_REPORTED",
        "statement": "the complex volume / CS invariant of the unit enters the 3d-3d partition function ONLY as a "
                     "dimensionless element of C/4pi^2 Z in the exponent; all dimensionful content is in hbar<->k and "
                     "the squashing/lens radius, NONE in the invariant. No kappa-type or volume-type invariant of the "
                     "unit can source a physical scale.",
        "boundary": "the unification is a SYMMETRY identity (L14) and TERMINATES at the firewall (L15). Real bridge + "
                    "confirmed wall = the honest boundary of the one-object picture; the cosmological-constant question "
                    "lies on the far side of a wall this structure does not cross.",
    }


def main():
    print("B151 -- firewall confirmation (L15): does any quantity carry a SCALE across the L14 bridge?\n")
    vol, cs, live = figure_eight_complex_volume()
    print("[anchor: the unit (figure-eight 4_1) -- %s]" % ("SnapPy live" if live else "recorded"))
    print(f"    Vol = {vol:.10f}  (= 2*V_tet, the minimal cusped hyperbolic volume)")
    print(f"    CS  = {cs:.3e}   (amphichiral => 0)")
    print(f"    Vol+iCS in {INVARIANT_SPACE}")
    print(f"    pre-strengthening: {CS_PRESTRENGTHENING}")
    print("\n[the reading -- what carries the units, per primary source]")
    for r in FIREWALL_READING:
        print(f"  [{r['tag']}] {r['source']}")
        print(f"      units in: {r['what_carries_units']}")
    v = verdict()
    print(f"\nVERDICT: {v['verdict']}")
    print(f"  {v['statement']}")
    print(f"  BOUNDARY: {v['boundary']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
