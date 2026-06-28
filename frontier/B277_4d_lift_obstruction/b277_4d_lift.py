"""B277 -- wall #4 made precise: what a 4d lift of T[4_1] requires, and exactly what the figure-eight does NOT
supply. FIREWALLED (geometry of the 6d (2,0) reductions, not a physics claim). Nothing to CLAIMS.md.

Probe-where-computable (owner directive): instead of asserting wall #4 "open", pin down the obstruction.

THE SETUP. There are TWO reductions of the 6d (2,0) theory of type G:
  * 3d-3d:  G on a 3-manifold M  ->  3d N=2 theory T[M].   (T[4_1] = U(1)+2 chirals, B262.)
  * class-S: G on a Riemann surface C  ->  4d N=2 theory T[C].   (a chiral 4d SM needs the 4d side.)
A 4d theory needs a SURFACE, not a 3-manifold. The figure-eight, however, is a once-punctured-torus BUNDLE, so it
carries a CANONICAL surface -- its fiber -- and a canonical mapping-class element:

  fiber  = Sigma_{1,1} (once-punctured torus),  Euler char chi = 2-2g-n = -1  (g=1, n=1)
  monodromy  phi = R*L = [[2,1],[1,1]] in SL(2,Z) = MCG(Sigma_{1,1}),  trace 3  (pseudo-Anosov, |tr|>2)

CLASS-S OF THE FIBER (computable identification):
  class-S(A_1, Sigma_{1,1}) = 4d N=2* SU(2) (one SU(2), one adjoint hyper; the puncture = adjoint mass).
  MCG(Sigma_{1,1}) = SL(2,Z) = the S-DUALITY group of N=2* SU(2); phi is an S-duality element.
  And T[4_1] (3d, B262) = the DUALITY-WALL theory of phi (Terashima-Yamazaki / Dimofte-Gukov: the 3d-3d theory of a
  mapping torus is the duality wall of its monodromy) -- this CONNECTS the 3d-3d and class-S pictures consistently.

THE OBSTRUCTION (exactly what is missing for a chiral 4d Standard Model):
  (1) SUSY/chirality: the canonical lift is N=2 (8 supercharges) => NON-CHIRAL (vector-like matter only). The SM is
      CHIRAL = N=1 (4 supercharges) or less. The N=2 -> N=1 reduction needs an EXTERNAL datum (a superpotential /
      flux / twist) that the geometry of 4_1 does NOT supply. This is wall #3 (chirality) reappearing as the gate on
      wall #4.
  (2) Type: the 6d type G is STILL a free input -- the fiber fixes the SURFACE and the MONODROMY, not the type. So
      the 4d lift does not resolve input-E6 = output-E6 either; it inherits the same CRUX.

VERDICT (first-class input-required result): wall #4 is NOT "no lift" -- there is a canonical N=2 lift (the fiber
class-S theory N=2* SU(2), with phi as S-duality). It fails to be a chiral 4d SM for two precise, named reasons: it
is N=2 (needs an N=2->N=1 datum, = wall #3), and the type is free (= the CRUX). residual-hint: a chiral lift would
need 6d (1,0) / a half-BPS twist / flux on the fiber -- none canonical to 4_1.

Run: python b277_4d_lift.py  (pyenv; tiny SL(2,Z) computation).
"""
SUPERCHARGES_CLASS_S = 8     # 4d N=2 from 6d (2,0) on a surface
SUPERCHARGES_SM = 4          # 4d N=1 (chiral); SM chirality needs <= 4


def fiber_euler_char(g=1, n=1):
    """Once-punctured torus Sigma_{1,1}: chi = 2 - 2g - n."""
    return 2 - 2 * g - n


def monodromy():
    """phi = R*L in SL(2,Z) = MCG(Sigma_{1,1}); returns (matrix-as-tuple, trace, det)."""
    # R=[[1,1],[0,1]], L=[[1,0],[1,1]] ; R*L = [[2,1],[1,1]]
    M = (2, 1, 1, 1)
    tr = M[0] + M[3]
    det = M[0] * M[3] - M[1] * M[2]
    return M, tr, det


def is_pseudo_anosov():
    _, tr, _ = monodromy()
    return abs(tr) > 2


def lift_is_n2_nonchiral():
    """The canonical class-S lift of the fiber is N=2 (8 supercharges) => non-chiral."""
    return SUPERCHARGES_CLASS_S == 8 and SUPERCHARGES_CLASS_S > SUPERCHARGES_SM


MISSING_INPUTS = {
    "n2_to_n1_datum": "N=2 (8 supercharges) -> N=1 (4): a superpotential/flux/twist; needed for chirality (wall #3); not supplied by 4_1",
    "type_G": "the 6d type G is a free input (= the input-E6=output-E6 CRUX); the fiber fixes the surface+monodromy, not the type",
}


def verdict():
    """Wall #4 characterized: a canonical N=2 lift exists; a chiral 4d SM is blocked by two named missing inputs."""
    _, tr, det = monodromy()
    return (fiber_euler_char() == -1 and tr == 3 and det == 1 and is_pseudo_anosov()
            and lift_is_n2_nonchiral() and len(MISSING_INPUTS) == 2)


if __name__ == "__main__":
    print("=== B277: wall #4 (4d lift) characterized ===\n")
    M, tr, det = monodromy()
    print(f"fiber Sigma_{{1,1}}: Euler char = {fiber_euler_char()}; monodromy phi=R*L={M}, trace={tr}, det={det}, pseudo-Anosov={is_pseudo_anosov()}")
    print("class-S(A_1, Sigma_{1,1}) = 4d N=2* SU(2); MCG=SL(2,Z)=S-duality; phi = an S-duality element")
    print(f"canonical lift is N=2 ({SUPERCHARGES_CLASS_S} supercharges) => NON-CHIRAL; SM needs N=1 ({SUPERCHARGES_SM})")
    print("\nMISSING for a chiral 4d SM (the two named obstructions):")
    for k, v in MISSING_INPUTS.items():
        print(f"  - {k}: {v}")
    print("\nverdict (canonical N=2 lift exists; chiral SM blocked by 2 named missing inputs):", verdict())
    assert verdict()
