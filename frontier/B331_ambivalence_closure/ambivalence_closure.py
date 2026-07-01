"""B331 -- the SL(2,C) holomorphic escape is closed at its root: the generation element is ELLIPTIC.

Chat-1's meditation (2026-07-01): the wall is between the real and the complex. Structure = real
invariants (traces, volumes, magnitudes); values = phases. The proposed escape: the geometric
holonomy is in SL(2,C), NOT SU(2); holomorphic reps are not self-dual, so their 27|_2T need not
pair omega, omega^2 -> n1 != n2 possible -> Level 3.

Chat-1 then self-corrected (every route gives n1=n2). This probe VERIFIES the closure and gives the
clean reason, sharper than both the "center/non-center" heuristic and B329's sigma-stability framing:

  The generation-permuting element  g = [[0,-1],[1,-1]]  (order 3) is ELLIPTIC and AMBIVALENT:
  its eigenvalue set {omega, omega^2} is inverse-closed, so g ~ g^-1. For ANY finite-order element,
  chi_R(g^-1) = conj(chi_R(g)); with g ~ g^-1 this forces chi_27(g) REAL -> n1 = n2 -- in EVERY
  representation, compact OR holomorphic. Holomorphicity is INVISIBLE at a finite-order element:
  the compact and holomorphic characters of g coincide (both = 0). The SL(2,C)-vs-SU(2) distinction
  only bites on LOXODROMIC (infinite-order) elements -- which carry volume/CS (STRUCTURE), not the
  finite Z/3 that would have to split the PHASES.

Correction (verify-don't-trust on Chat-1): "every order-3 element gives a real character" is FALSE --
the CENTRAL order-3 element z acts on the 27 by the scalar omega (triality), chi_27(z) = 27*omega
(COMPLEX). z is not ~ z^-1. The real content is g's AMBIVALENCE (g non-central + elliptic), not a
blanket order-3 property.

SCOPE (honest): this closes the escape for any lift factoring through SL(2,C) -> E6 -- which INCLUDES
the arithmetically-relevant one (the Riley holonomy is an SL(2,C) rep). The fully-general "all finite
2T -> E6 embeddings give n1=n2" is still not a theorem (H103); B329 verified two, this closes the
SL(2,C)-factoring family. Level 4 confirmed for the object's actual lift. Firewalled; nothing to CLAIMS.
"""
import sympy as sp

OMEGA = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I
G = sp.Matrix([[0, -1], [1, -1]])                    # the generation Z/3 generator


def g_is_elliptic_ambivalent():
    """g has order 3, eigenvalues {omega, omega^2} (inverse-closed) => g ~ g^-1."""
    order3 = (G**3) == sp.eye(2)
    ambivalent = G.charpoly() == G.inv().charpoly()
    return order3, ambivalent


def chi27_holomorphic():
    """holomorphic principal SL(2,C) lift: 27 = V(16)+V(8)+V(0); g -> diag(omega, 1/omega)."""
    def chi_spin(twoj, lam):
        return sp.simplify(sum(lam**(twoj - 2 * i) for i in range(twoj + 1)))
    return sp.simplify(sum(chi_spin(twoj, OMEGA) for twoj in (16, 8, 0)))


def chi27_compact():
    """compact SU(2) value for the same elliptic g (trace -1, x = -1/2)."""
    return sp.simplify(sum(sp.chebyshevu(twoj, sp.Rational(-1, 2)) for twoj in (16, 8, 0)))


def chi27_central():
    """the CENTRAL order-3 element z acts by the scalar omega on the 27 (triality): chi = 27 omega."""
    return sp.simplify(27 * OMEGA)


if __name__ == "__main__":
    o3, amb = g_is_elliptic_ambivalent()
    print("g: order-3 =", o3, " ambivalent (g ~ g^-1) =", amb)
    ch, cc = chi27_holomorphic(), chi27_compact()
    print("chi_27(g) holomorphic =", ch, "  compact =", cc, "  identical & real =>", ch == cc == 0)
    z = chi27_central()
    print("chi_27(central z) =", z, "  complex =>", sp.im(z) != 0,
          " (so 'order-3 => real char' is FALSE; ambivalence is the real reason)")
    print("\n=> SL(2,C) escape closed at the elliptic generation element; Level 4 confirmed for the arithmetic lift.")
