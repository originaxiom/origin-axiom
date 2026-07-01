"""B326 — the generation Z/3-breaking is finite congruence torsion (verified).

Chat-2 -> CC handoff (2026-07-01), verify-don't-trust. Two independent checks:
  (1) exact Alexander module  Z[t]/(Delta, t^3-1) = (Z/4)^2, deck action = companion(Delta),
      Delta mod 4 = Phi_3 = x^2+x+1 (irreducible, order 3);
  (2) SnapPy cross-check (guarded; not required for the test): H1(3-fold cyclic cover of 4_1)
      = Z + Z/4 + Z/4.
Firewalled: finite torsion => texture/selection rules, NOT mass magnitudes. Nothing to CLAIMS.
"""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

t = sp.symbols('t')
Delta = t**2 - 3*t + 1          # figure-eight Alexander polynomial


def alexander_facts():
    disc = sp.discriminant(Delta, t)
    w = sp.exp(2*sp.pi*sp.I/3)
    torsion_order = sp.nsimplify(sp.simplify(Delta.subs(t, w) * Delta.subs(t, w**2)))
    mod4 = [int(c) % 4 for c in sp.Poly(Delta, t).all_coeffs()]
    return disc, torsion_order, mod4


def torsion_module():
    """Z[t]/(Delta, t^3-1) as an abelian group, with the deck (mult-by-t) action."""
    Comp = sp.Matrix([[0, -1], [1, 3]])         # t on Z[t]/(Delta), basis {1, t}

    def vec(poly):
        p = sp.Poly(sp.rem(poly, Delta, t), t)
        c = p.all_coeffs()
        c = [0] * (2 - len(c)) + list(c)         # [coeff t^1, coeff t^0]
        return sp.Matrix([c[1], c[0]])           # (const, t) coords

    sub = sp.Matrix.hstack(vec(t**3 - 1), vec(t * (t**3 - 1)))
    snf = smith_normal_form(sub.T)
    char_mod4 = [int(c) % 4 for c in sp.Poly(Comp.charpoly(t).as_expr(), t).all_coeffs()]
    order3 = (Comp**3).applyfunc(lambda x: x % 4) == sp.eye(2)
    return snf, char_mod4, order3


def snappy_crosscheck():
    try:
        import snappy
        cov = snappy.Manifold('4_1').covers(3, cover_type='cyclic')[0]
        return str(cov.homology())
    except Exception as e:
        return f"(snappy unavailable: {e!r})"


if __name__ == '__main__':
    disc, torsion_order, mod4 = alexander_facts()
    print("Delta =", Delta, " disc =", disc, "(-> Q(sqrt5) end)")
    print("Delta mod 4 =", mod4, "= Phi_3 (-> Q(sqrt-3) end)")
    print("|torsion| = Delta(w)Delta(w^2) =", torsion_order)
    snf, char_mod4, order3 = torsion_module()
    print("Smith normal form of Z[t]/(Delta,t^3-1):", snf.tolist(), "=> (Z/4)^2")
    print("deck char poly mod 4 =", char_mod4, " order-3:", order3)
    print("SnapPy H1(3-fold cyclic cover):", snappy_crosscheck())
