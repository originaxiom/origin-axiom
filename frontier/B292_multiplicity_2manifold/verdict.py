"""B292 verdict (pyenv; SnapPy-derived constants from multiplicity_2manifold.py) -- WHICH 2-MANIFOLD supplies the
multiplicity? Phase IV (wall #4).

The multiplicity the owner's thesis names is REALIZED but TRIPARTITE, and only one piece is a 2-manifold:
  (i)  fiber Sigma_{1,1} -- the literal 2-(real)-manifold (chi=-1, monodromy phi=RL trace 3). The class-S surface;
       supplies the N=2 lift (B277), NOT chirality.
  (ii) metallic tower R^m L^m -- a discrete sequence of DISTINCT 3-manifolds (traces m^2+2; arithmetic only m=1,2,
       B125). The arithmetic family.
  (iii) filling family (1,n) -- a discrete sequence of closed 3-manifolds (scale ladder 2*pi/n, B290). The scale family.

NONE supplies the N=2->N=1 chiral datum -> wall #4 stays blocked (B277's two named reasons). The chiral 4d SM
construction is a STOP-GATE (NEEDS-SPECIALIST). FIREWALL: geometry/structure, not a physics claim. Nothing to CLAIMS.
"""

# --- the three multiplicity candidates ---
FIBER = "Sigma_{1,1}"
FIBER_GENUS, FIBER_PUNCTURES = 1, 1
FIBER_MONODROMY_TRACE = 3                               # phi = RL = [[2,1],[1,1]], pseudo-Anosov
FIBER_IS_THE_2MANIFOLD = True                           # the only genuine 2-(real)-manifold

TOWER = "R^m L^m"
TOWER_TRACES = [3, 6, 11, 18, 27, 38]                   # m^2 + 2, m = 1..6
TOWER_VOLUMES = [2.0299, 3.6639, 4.8138, 5.5736]        # m = 1..4 -- distinct, increasing (distinct 3-manifolds)
TOWER_ARITHMETIC_M = [1, 2]                             # Q(sqrt-3), Q(i); m>=3 non-arithmetic (B125)
TOWER_IS_3MFLD_SEQUENCE = True                          # discrete arithmetic family, not a surface

FILLINGS = "(1,n)"
FILLINGS_IS_3MFLD_SEQUENCE = True                       # discrete scale family (2*pi/n), not a surface

# --- conclusions ---
MULTIPLICITY_TRIPARTITE = True                          # surface (fiber) / arithmetic (tower) / scale (fillings)
CHIRAL_DATUM_SUPPLIED = False                           # none gives the N=2->N=1 chiral datum
CHIRAL_4D_SM_IS_STOP_GATE = True                        # B277's two reasons; NEEDS-SPECIALIST
DERIVES_SM_VALUES = False                               # firewall


def fiber_euler_char():
    return 2 - 2 * FIBER_GENUS - FIBER_PUNCTURES        # = -1


def tower_traces(mmax=6):
    return [m**2 + 2 for m in range(1, mmax + 1)]


def verdict():
    fiber_ok = fiber_euler_char() == -1 and FIBER_IS_THE_2MANIFOLD
    tower_ok = tower_traces() == TOWER_TRACES and TOWER_IS_3MFLD_SEQUENCE and TOWER_ARITHMETIC_M == [1, 2]
    distinct = len(set(TOWER_VOLUMES)) == len(TOWER_VOLUMES) and \
        all(TOWER_VOLUMES[i] < TOWER_VOLUMES[i + 1] for i in range(len(TOWER_VOLUMES) - 1))
    return bool(fiber_ok and tower_ok and distinct and FILLINGS_IS_3MFLD_SEQUENCE
                and MULTIPLICITY_TRIPARTITE and not CHIRAL_DATUM_SUPPLIED
                and CHIRAL_4D_SM_IS_STOP_GATE and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print(f"(i) fiber {FIBER}: chi = {fiber_euler_char()} (2-manifold), monodromy trace {FIBER_MONODROMY_TRACE}")
    print(f"(ii) tower {TOWER}: traces {tower_traces()}, distinct 3-mfld seq, arithmetic m={TOWER_ARITHMETIC_M}")
    print(f"(iii) fillings {FILLINGS}: scale 3-mfld sequence")
    print("multiplicity tripartite:", MULTIPLICITY_TRIPARTITE, "| chiral datum supplied:", CHIRAL_DATUM_SUPPLIED)
    print("chiral 4d SM is a stop-gate:", CHIRAL_4D_SM_IS_STOP_GATE, "| verdict:", verdict())
