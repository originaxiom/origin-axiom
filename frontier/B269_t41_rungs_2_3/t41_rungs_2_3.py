"""B269 -- T[4_1] Rungs 2 (flavor / cusp Weyl) + 3 (partition-function saddle). FIREWALLED (3d-3d / quantum
topology, not physics). Nothing to CLAIMS.md. Completes the deferred T[4_1] rungs (B262 audit; B268 Phase 2).

RUNG 2 -- the flavor symmetry and the cusp Weyl Z/2.
The figure-eight has ONE cusp, so it cannot host a cusp-SWAP (the multi-cusp Weyl->nonabelian test needs >=2
cusps, e.g. the Whitehead link -- S033). The single-cusp symmetry is the MERIDIAN Weyl Z/2: (M,L)->(1/M,1/L), the
hyperelliptic involution of the boundary torus. We verify it is an EXACT symmetry of the A-polynomial (the Coulomb
branch, B260), and read off the flavor symmetry.
  VERDICT: flavor = U(1)_m semidirect Z/2 = O(2) -- the Cartan + its Weyl reflection, NOT an enhanced SU(2). The
  single-cusp peripheral data is abelian (Mostow); there is no SU(2) flavor enhancement (no W-boson monopoles).
  This is the abelian wall (S029/S033) holding -- an honest NEGATIVE. The nonabelian E6 of the arc is the 3d-3d
  TYPE (the character variety, B264-B267), NOT a flavor enhancement of the abelian T[4_1]. The two are different
  layers; Rung 2 cleanly separates them (and rules out the 'multiplicity manufactures SU(2)' hope for 1 cusp).

RUNG 3 -- the partition-function saddle reproduces the complex volume (B250) and centers on e^{i pi/3}.
T[4_1] is 2 chirals + 1 gauged U(1) (B262) = 2 quantum dilogarithms + 1 integral: the figure-eight STATE INTEGRAL.
Its classical (b->0) saddle is the gluing/critical-point equation; the geometric solution is the regular ideal
tetrahedron shape z = e^{i pi/3}, and the critical value gives
   Vol(4_1) = 2 * Im Li_2(e^{i pi/3}) = 2.0298832...   (= B250's complex volume; CS = 0 at the amphichiral point).
COHERENCE (the payoff): the saddle shape e^{i pi/3} is the SAME e^{i pi/3} in Q(sqrt-3) as the Riley parameter t
(B264) and the center of the ramified-prime reduction (B266). So the partition function's geometric saddle lands
on exactly the Q(sqrt-3) point whose reduction mod (sqrt-3) produces 2T = McKay-E6. At the golden root q=zeta_5 the
colored-Jones limit is the antiperiod-5 sequence (B261). 'DOES Z KNOW ABOUT 2T?' -- honest verdict: the saddle DOES
sit at the ramified-prime center e^{i pi/3} in Q(sqrt-3) (a genuine coherence), but a full statement (the WRT at the
relevant root reflecting SL(2,F_3)) is the remaining wall-#2 conjecture, not closed here.

Run: python t41_rungs_2_3.py  (pyenv, sympy + mpmath).
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
M, L = sp.symbols("M L")
A_GEOM = M**4 * L**2 - (M**8 - M**6 - 2 * M**4 - M**2 + 1) * L + M**4   # figure-eight A-polynomial (B260)
GEOMETRIC_SHAPE = mp.e ** (1j * mp.pi / 3)                              # regular ideal tetrahedron; = Riley t (B264)


def cusp_weyl_invariant():
    """The meridian Weyl Z/2 (M,L)->(1/M,1/L) is an exact symmetry of the A-polynomial (up to a monomial unit)."""
    A_reflected = A_GEOM.subs({M: 1 / M, L: 1 / L}) * M**8 * L**2
    return sp.expand(A_GEOM - A_reflected) == 0


def complete_structure_longitude():
    """A(1,L) at the complete/amphichiral structure: (L+1)^2, double root L=-1."""
    return sp.factor(A_GEOM.subs(M, 1))


def complex_volume_from_saddle():
    """The state-integral saddle (regular ideal tetrahedron z=e^{i pi/3}) gives Vol = 2 Im Li_2(z)."""
    return 2 * mp.im(mp.polylog(2, GEOMETRIC_SHAPE))


if __name__ == "__main__":
    print("=== B269: T[4_1] Rungs 2 (flavor/Weyl) + 3 (partition-function saddle) ===\n")

    # Rung 2
    print("RUNG 2 -- flavor symmetry & the cusp Weyl Z/2:")
    inv = cusp_weyl_invariant()
    print(f"  A-poly invariant under the meridian Weyl Z/2 (M,L)->(1/M,1/L): {inv}")
    print(f"  A(1,L) at the complete structure = {complete_structure_longitude()}  (amphichiral, double root L=-1)")
    print("  => flavor = U(1)_m semidirect Z/2 = O(2), NOT SU(2). Single cusp = abelian (Mostow); no SU(2)")
    print("     enhancement (S029/S033 abelian wall). Nonabelian E6 = the 3d-3d TYPE, not a flavor enhancement.")
    assert inv and complete_structure_longitude() == (L + 1)**2

    # Rung 3
    print("\nRUNG 3 -- partition-function saddle:")
    vol = complex_volume_from_saddle()
    print(f"  saddle shape z = e^(i pi/3) (regular ideal tetrahedron) = Riley t (B264) = ramified-prime center (B266)")
    print(f"  Vol(4_1) = 2 Im Li_2(e^(i pi/3)) = {mp.nstr(vol, 11)}  (= B250 complex volume)")
    assert abs(vol - mp.mpf("2.0298832128")) < 1e-9
    print("  closes the loop B250 (complex vol) / B260 (A-poly saddle) / B261 (golden-root colored Jones).")
    print("\n  'does Z know about 2T?' -- the saddle sits at the Q(sqrt-3) ramified-prime center (coherence);")
    print("  the full WRT-reflects-SL(2,F_3) statement is the remaining wall-#2 conjecture (not closed). PASS")
