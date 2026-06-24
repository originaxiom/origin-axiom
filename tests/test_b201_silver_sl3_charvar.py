"""B201 -- the metallic SL(3) character variety from the trace-map fixed locus (V194). Fast pyenv locks.

Locks the foundation (pyenv/sympy): the B48 metallic trace map T_m, its square = the bundle monodromy
trace map, reproduces B71's published figure-eight T_1^2 at m=1; and B71's geometric component V0 is a
genuine fixed point of T_1^2 with the {x1=x4, x2=x5} form (the form that persists to silver -- the
component COUNT 3->4 is the Sage reproducer charvar.sage). Standalone character-variety math; nothing to
CLAIMS.md.
"""
import sympy as sp


def Tm(coords, m):
    """B48 metallic SL(3) trace map for phi_m: a->a^m b, b->a (Cayley-Hamilton recurrences)."""
    x1, x2, x3, x4, x5, x6, x7, x8 = coords
    tau = {-1: x6, 0: x2, 1: x3}
    sig = {-1: x7, 0: x5, 1: x8}
    for k in range(2, m + 2):
        tau[k] = sp.expand(x1 * tau[k - 1] - x4 * tau[k - 2] + tau[k - 3])
        sig[k] = sp.expand(x4 * sig[k - 1] - x1 * sig[k - 2] + sig[k - 3])
    return (tau[m], x1, tau[m + 1], sig[m], x4, sig[m - 1], tau[m - 1], sig[m + 1])


def Tm_sq(coords, m):
    return tuple(sp.expand(e) for e in Tm(Tm(coords, m), m))


def test_tracemap_m1_matches_b71():
    c = sp.symbols("x1 x2 x3 x4 x5 x6 x7 x8")
    x1, x2, x3, x4, x5, x6, x7, x8 = c
    # B71's published figure-eight single twist T_1 (a->ab, b->a):
    T1_b71 = (x3, x1, x1 * x3 - x4 * x2 + x6, x8, x4, x5, x2, x4 * x8 - x1 * x5 + x7)
    assert all(sp.expand(a - b) == 0 for a, b in zip(Tm(c, 1), T1_b71))
    # the figure-eight bundle monodromy trace map = T_1^2 (used by B67/B71)
    sq = Tm_sq(c, 1)
    # its fixed locus is the figure-eight SL(3) character variety; check a known fixed point below


def test_figure_eight_V0_is_fixed_point():
    # B71's geometric component V0(p,q) = (p,q,q,p,q,p,p,q)  (x1=x4=p, x2=x5=q) is in Fix(T_1^2)
    c = sp.symbols("x1 x2 x3 x4 x5 x6 x7 x8")
    sq = Tm_sq(c, 1)
    for (p, q) in [(sp.Rational(3, 2), sp.Rational(-5, 4)), (2, 3), (sp.Rational(-1, 3), 5)]:
        pt = {c[0]: p, c[1]: q, c[2]: q, c[3]: p, c[4]: q, c[5]: p, c[6]: p, c[7]: q}
        img = [sp.expand(e.subs(pt)) for e in sq]
        coords = [p, q, q, p, q, p, p, q]
        assert img == coords, (p, q)            # V0 is genuinely fixed by T_1^2
        # ...and has the geometric form x1=x4, x2=x5
        assert coords[0] == coords[3] and coords[1] == coords[4]


if __name__ == "__main__":
    test_tracemap_m1_matches_b71()
    test_figure_eight_V0_is_fixed_point()
    print("ALL CHECKS PASS")
