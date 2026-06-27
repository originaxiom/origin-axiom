"""B241 -- resolving the sec.6 horizon question: is the Gang-Yonekura twist-knot SU(3) the same as our
level-rank SU(3)_2 (B238)? ANSWER: NO -- they are two different SU(3)'s. Firewall-clean (a quantum-topology /
structural distinction; the physics framing -- "strong-force SU(3)" -- stays firewalled, H37 deflated). Nothing
to CLAIMS.md.

THE TWO SU(3)'s (verify-don't-trust, incl. verifying the negative):
  (A) Gang-Yonekura, arXiv:1803.04009 (JHEP 07(2018)145): a global FLAVOR symmetry of the 3d N=2 theory T[K],
      enhanced from u(1), present for ALL hyperbolic twist knots, built from the A_1 (=SU(2)) 6d (2,0) theory.
      => UNIVERSAL across the twist-knot family; a *surprise* (not predicted from CS level structure).
  (B) ours, B238: a Chern-Simons GAUGE group SU(3)_2, the level-rank dual of SU(2)_3 (shared kappa=k+N=5), whose
      figure-eight WRT coincides at -1/phi. => FIGURE-EIGHT-SPECIFIC (fails for silver/bronze) and golden.

They differ in TYPE (flavor symmetry of an SCFT vs CS gauge group) and SPECIFICITY (twist-universal vs golden).
If they were the same, the level-rank coincidence would be twist-knot-universal -- it is not.

COMPUTATIONAL CORROBORATION (this file):
  * within the twist-knot family (GY's own family), ONLY 4_1 is amphicheiral, so ONLY 4_1 gives a real (golden,
    in Q(sqrt5)) SU(2)_3 colored Jones at the golden root; 5_2, 6_1 are chiral -> complex (in Q(zeta_5)).
    So the golden/level-rank structure is 4_1-specific WITHIN GY's family -- orthogonal to GY's universal SU(3).
  * (reused B238) the level-rank SU(2)_3<->SU(3)_2 WRT coincidence is figure-eight-specific in the metallic family.

Run: python twist_su3.py (pyenv). Braid words verified via SnapPy.
"""
import importlib.util
import pathlib

_B240 = pathlib.Path(__file__).resolve().parents[1] / "B240_golden_jones_integrality" / "colored_jones_sweep.py"
_s = importlib.util.spec_from_file_location("b240_sweep", _B240)
cj = importlib.util.module_from_spec(_s); _s.loader.exec_module(cj)

# the twist-knot family (SnapPy-verified braid words); only 4_1 is amphicheiral (Jones-palindromic).
TWIST = {
    "4_1": ([1, -2, 1, -2], 3),                                   # the figure-eight (amphicheiral, golden bundle)
    "5_2": ([-1, 2, -3, 2, 2, 1, 2, 3, 2], 4),                    # chiral
    "6_1": ([-1, 2, -3, 4, -3, 2, 1, -3, 2, -4, 3, 2], 5),       # chiral
}


def golden_profile(braid, strands):
    """(is_real_in_Q(sqrt5), is_pure_integer) for the SU(2)_3 colored Jones at the golden root."""
    _, _, real = cj.galois_decomp(braid, strands, 2)
    return real, cj.is_pure_integer(braid, strands)


if __name__ == "__main__":
    print("=== golden SU(2)_3 colored Jones across the twist-knot family (GY's family) ===")
    for nm, (bw, s) in TWIST.items():
        real, pure = golden_profile(bw, s)
        tag = "amphicheiral -> REAL (golden)" if real else "chiral -> COMPLEX"
        print(f"  {nm:4s}: real(in Q(sqrt5))={real}  pure-integer={pure}   [{tag}]")
    # the decisive contrast: 4_1 unique within the twist family
    real_ones = [nm for nm, (bw, s) in TWIST.items() if golden_profile(bw, s)[0]]
    assert real_ones == ["4_1"], real_ones
    assert cj.is_pure_integer(*TWIST["4_1"])
    print("\n  => within GY's twist-knot family, the golden structure is 4_1-SPECIFIC")
    print("     (only 4_1 amphicheiral -> real golden value; 5_2,6_1 chiral -> complex).")

    print("\n=== contrast with Gang-Yonekura SU(3) (arXiv:1803.04009) ===")
    print("  GY SU(3): FLAVOR symmetry of T[K], UNIVERSAL across ALL hyperbolic twist knots, from A_1.")
    print("  B238 SU(3)_2: CS GAUGE group, level-rank dual of SU(2)_3, figure-eight-specific (-1/phi, kappa=5).")
    print("  => DIFFERENT SU(3)'s: type (flavor vs gauge) AND specificity (universal vs golden).")
    print("\nVERDICT: the sec.6 question resolves to a clean DISTINCTION (no bridge). Firewall-clean.")
    print("ALL CHECKS PASS")
