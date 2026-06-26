"""B226 / L43 -- the two-SUSY bridge, resolved (literature-grounded scout). Nothing to CLAIMS.md.

The same golden/figure-eight object carries supersymmetry twice, and L43 asked: one structure or two faces?
This grounds the two sides (firewall-clean central-charge/level bookkeeping) and records the literature
verdict. The physics READING is firewalled to speculations/S040.

SIDE A -- the emergent chain SUSY (B221/B222): the Fibonacci (SU(2)_3) golden chain flows to the tricritical
Ising M(4,5), c=7/10 = the first N=1 SUPERCONFORMAL minimal model. SU(2)_3 WZW boundary c = 9/5; the chain CFT =
the coset (SU(2)_2 x SU(2)_1)/SU(2)_3 = 7/10.

SIDE B -- the licensed 3d-3d SUSY (K006): the figure-eight (4_1) defines a 3d N=2 theory T[4_1] whose SUSY vacuum
moduli space = the SL(2,C) character variety (= 40a1, B211); it is the COMPLEX SL(2,C) Chern-Simons / 3d-gravity
theory, invariant Vol(4_1)=2.0299, CS=0 (Cho-Gang-Kim: irreducible flat connections, unbroken SUSY).

THE RESOLUTION (literature): the two SUSYs are TWO FACES, separated by the HYPERBOLIC / NON-HYPERBOLIC divide:
  - 2D Virasoro minimal models -- INCLUDING the supersymmetric ones (the tricritical Ising) -- are realized as 3d
    bulk theories from NON-HYPERBOLIC (Seifert / torus-knot) 3-manifolds, via T[SU(2)] with SU(2)_k Dehn-filling:
      Gang-Kang-Kim et al., "Non-hyperbolic 3-manifolds and 3D field theories for 2D Virasoro minimal models"
        (arXiv:2405.16377): M(P,Q) <-> Seifert S^2((P,P-R),(Q,S),(3,1)); TCI M(4,5) via S^2((5,-1),(4,5),(3,1)).
      "... bulk field theories for SUPERSYMMETRIC / W_N minimal models" (arXiv:2511.04524, JHEP 03(2026)066).
      "Torus Knots and Minimal Models Revisited: Rational VOA characters from NON-hyperbolic knots"
        (arXiv:2512.23122).
  - The figure-eight is HYPERBOLIC, so its 3d-3d theory T[4_1] is the complex-CS / 3d-gravity object (Vol=2.0299),
    NOT a minimal model (e.g. arXiv:2401.13900, "3d gravity from Virasoro TQFT", analyzes 4_1 explicitly).
  - The Fibonacci-state tricritical SUSY can even be FRACTIONAL (coset-CFT) supersymmetry (arXiv:1905.09960),
    distinct from the standard golden chain's N=1 superconformal.

So: the genuine shared ingredient is SU(2)_3 (via T[SU(2)] / SU(2)_k Chern-Simons), NOT the figure-eight's
hyperbolic geometry. The golden-chain CFT (TCI) lives on the NON-hyperbolic / minimal-model side; the figure-eight
KNOT (the golden m=1 bundle) lives on the HYPERBOLIC / 3d-gravity side. They are two distinct 3-manifolds /
theories in the same Class-R / 3d-3d framework -- two faces, not one structure. (This rhymes with the repo's
closed-Sol vs cusped-hyperbolic duality, B217/V200: golden sits on BOTH sides of a hyperbolicity split, as
DIFFERENT manifolds.) The exact figure-eight 3d-3d -> 2d reduction remains NEEDS-SPECIALIST, but the qualitative
answer is settled by the literature.

Firewall: dimensionless CFT/CS bookkeeping + cited literature facts; the "two SUSYs" reading is firewalled in
S040; nothing to CLAIMS.md; P1-P16 untouched. Run: python l43_grounding.py (pyenv).
"""
from fractions import Fraction as Fr


def c_su2_wzw(k):
    """SU(2)_k WZW / Sugawara central charge c = 3k/(k+2) (the boundary CFT of SU(2)_k Chern-Simons)."""
    return Fr(3 * k, k + 2)


def coset_c():
    """golden-chain CFT = (SU(2)_2 x SU(2)_1)/SU(2)_3 = the tricritical Ising c=7/10 (N=1 superconformal)."""
    return c_su2_wzw(2) + c_su2_wzw(1) - c_su2_wzw(3)


# the structural verdict (literature-grounded): which side each object lives on
SIDE_A = {"object": "golden (Fibonacci/SU(2)_3) anyon chain", "CFT": "tricritical Ising M(4,5)",
          "c": Fr(7, 10), "SUSY": "N=1 superconformal (2d)",
          "3d-3d realization": "NON-hyperbolic Seifert space S^2((5,-1),(4,5),(3,1)) via T[SU(2)] (Gang et al.)"}
SIDE_B = {"object": "figure-eight knot 4_1 (= golden m=1 bundle)", "theory": "T[4_1] (3d N=2)",
          "CS": "complex SL(2,C) = 3d gravity", "invariant": "Vol=2.0299, CS=0",
          "SUSY": "N=2 (3d), M_SUSY = M_flat = char variety 40a1 (K006/B211)"}
REFERENCES = ["arXiv:2405.16377 (minimal models <-> Seifert spaces, T[SU(2)] Dehn-filling)",
              "arXiv:2511.04524 = JHEP 03(2026)066 (SUSY / W_N minimal models from non-hyperbolic 3-manifolds)",
              "arXiv:2512.23122 (minimal models from non-hyperbolic torus knots, rational VOA)",
              "arXiv:2401.13900 (figure-eight = 3d gravity / Virasoro TQFT, hyperbolic side)",
              "arXiv:1905.09960 (Fibonacci tricritical point = FRACTIONAL SUSY, coset CFT)"]

VERDICT = ("TWO FACES, separated by the hyperbolic/non-hyperbolic divide: the TCI (golden chain CFT) is realized "
           "by a NON-hyperbolic Seifert 3-manifold via T[SU(2)]/SU(2)_k; the figure-eight is HYPERBOLIC -> 3d "
           "gravity (Vol=2.03), NOT a minimal model. Shared ingredient = SU(2)_3 (via T[SU(2)]), NOT the "
           "figure-eight's geometry. The exact 4_1 3d-3d -> 2d reduction stays NEEDS-SPECIALIST.")


if __name__ == "__main__":
    print("=== L43: the two SUSYs of the golden/figure-eight object ===\n")
    print(f"SU(2)_3 WZW boundary c = {c_su2_wzw(3)}; golden-chain coset c = {coset_c()} (= 7/10, N=1 SCFT)")
    print(f"\nSIDE A (emergent chain SUSY): {SIDE_A['object']}")
    print(f"  -> {SIDE_A['CFT']}, c={SIDE_A['c']}, {SIDE_A['SUSY']}")
    print(f"  3d-3d: {SIDE_A['3d-3d realization']}")
    print(f"\nSIDE B (licensed 3d-3d SUSY): {SIDE_B['object']}")
    print(f"  -> {SIDE_B['theory']}, {SIDE_B['CS']}, {SIDE_B['invariant']}, {SIDE_B['SUSY']}")
    print(f"\nVERDICT: {VERDICT}")
    print("\nReferences:")
    for r in REFERENCES:
        print(f"  - {r}")
    assert coset_c() == Fr(7, 10) and c_su2_wzw(3) == Fr(9, 5)
    print("\nALL CHECKS PASS")
