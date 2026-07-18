"""B700 cell 1 lock — the golden measurement torsor (pyenv-pure, sympy).
The two golden 2-dim irreps of 2I=SL(2,5) (character rows sage-verified,
stored as zeta_5 polynomials) are swapped simply-transitively by the Galois
automorphism tau: zeta5 -> zeta5^2 = the nontrivial elt of Gal(Q(sqrt5)/Q).
=> {golden irreps} is a Z/2 torsor = the fiber-functor ambiguity."""
import sympy as sp

z = sp.symbols('z')                       # zeta_5, root of 1+z+z^2+z^3+z^4
cyc = 1 + z + z**2 + z**3 + z**4

def reduce5(expr):
    """reduce a polynomial in z modulo the 5th cyclotomic (z^4 = -(1+z+z^2+z^3))."""
    p = sp.Poly(sp.expand(expr), z)
    r = p.rem(sp.Poly(cyc, z))
    return sp.expand(r.as_expr())

# the two golden irreps' character rows (sage-verified, in Q(zeta5))
rA = [2, z**3+z**2+1, -z**3-z**2, -2, -z**3-z**2-1, z**3+z**2, -1, 1, 0]
rB = [2, -z**3-z**2, z**3+z**2+1, -2, z**3+z**2, -z**3-z**2-1, -1, 1, 0]

def tau(expr):                            # zeta5 -> zeta5^2
    return reduce5(expr.subs(z, z**2) if hasattr(expr, 'subs') else expr)


def test_two_golden_irreps_swapped_simply_transitively():
    # tau(A) == B  (swap) and tau(A) != A (no fixed point) -> simply-transitive torsor
    tA = [tau(sp.sympify(v)) for v in rA]
    Bred = [reduce5(sp.sympify(v)) for v in rB]
    Ared = [reduce5(sp.sympify(v)) for v in rA]
    assert tA == Bred, "tau must swap irrep A -> irrep B (the torsor)"
    assert tA != Ared, "tau must NOT fix A (no Galois-fixed golden irrep)"
    # tau is an involution on the pair (order 2)
    ttA = [tau(v) for v in tA]
    assert ttA == Ared, "tau^2 = id on the pair (Z/2)"


def test_golden_values_are_the_sqrt5_orbit():
    # z^3+z^2 = (-1-sqrt5)/2 ; so z^3+z^2+1 = (1-sqrt5)/2 = -1/phi ; -(z^3+z^2)=(1+sqrt5)/2=phi
    s = sp.sqrt(5)
    val_phi = sp.Rational(1, 2) * (1 + s)          # phi
    val_neg_inv = sp.Rational(1, 2) * (1 - s)      # -1/phi
    # numeric identification of z^3+z^2 with (-1-sqrt5)/2
    zc = sp.exp(2*sp.pi*sp.I/5)
    approx = complex((zc**3 + zc**2))
    assert abs(approx - complex((-1 - 5**0.5)/2)) < 1e-9
    # phi * (-1/phi) = -1 (golden), and phi + (-1/phi) = 1 (the trace pair)
    assert sp.simplify(val_phi * val_neg_inv) == -1
    assert sp.simplify(val_phi + val_neg_inv) == 1


def test_cell2_three_ambiguities_are_V4():
    """The three ambiguity Z/2's = the three involutions of V4=Gal(Q(sqrt-3,sqrt5)/Q);
    being(sqrt-3) * hearing(sqrt5) = meeting(sqrt-15)."""
    # automorphisms of Q(sqrt-3,sqrt5) as sign pairs (e1,e2) acting on (sqrt-3, sqrt5)
    V4 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    def mul(g, h): return (g[0]*h[0], g[1]*h[1])          # group law (componentwise)
    # V4 closed, every nonidentity has order 2
    assert all(mul(g, g) == (1, 1) for g in V4)
    nonid = [g for g in V4 if g != (1, 1)]
    assert len(nonid) == 3
    # which subfield each involution fixes: sqrt-3 fixed iff e1=+1; sqrt5 iff e2=+1;
    # sqrt-15 = sqrt-3*sqrt5 fixed iff e1*e2=+1
    def fixes(g):
        return {'Q(sqrt-3)': g[0] == 1, 'Q(sqrt5)': g[1] == 1,
                'Q(sqrt-15)': g[0]*g[1] == 1}
    being = (1, -1)     # fixes Q(sqrt-3) (negates sqrt5) — the golden/hearing-side ambiguity acts here
    hearing = (-1, 1)   # fixes Q(sqrt5)
    meeting = (-1, -1)  # fixes Q(sqrt-15)
    assert fixes(being)['Q(sqrt-3)'] and not fixes(being)['Q(sqrt5)']
    assert fixes(hearing)['Q(sqrt5)'] and not fixes(hearing)['Q(sqrt-3)']
    assert fixes(meeting)['Q(sqrt-15)'] and not fixes(meeting)['Q(sqrt-3)']
    # the group law: being * hearing = meeting  (and the disc law (-3)*(5) = -15)
    assert mul(being, hearing) == meeting
    assert (-3) * 5 == -15


def test_cell4_second_stage_torsor_PSL27():
    """E6 level-2 stage: PSL(2,7)'s two 3-dim irreps form a Gal(Q(sqrt-7)/Q)=Z/2
    torsor (simply transitive), structurally identical to the golden case."""
    z = sp.symbols('z')                                # zeta_7
    cyc7 = sum(z**k for k in range(7))                 # 1+z+...+z^6
    def red7(e):
        return sp.expand(sp.Poly(sp.expand(e), z).rem(sp.Poly(cyc7, z)).as_expr())
    # the two 3-dim irreps of PSL(2,7) (sage-verified rows, in Q(zeta7))
    rA = [3, 0, -z**4-z**2-z-1, z**4+z**2+z, -1, 1]
    rB = [3, 0, z**4+z**2+z, -z**4-z**2-z-1, -1, 1]
    def sigma(e):                                      # zeta7 -> zeta7^3 (non-residue): negates sqrt-7
        return red7(sp.sympify(e).subs(z, z**3)) if not isinstance(e, int) else e
    tA = [sigma(v) for v in rA]
    Bred = [red7(sp.sympify(v)) for v in rB]
    Ared = [red7(sp.sympify(v)) for v in rA]
    assert tA == Bred, "sigma must swap the two 3-dim irreps (the torsor)"
    assert tA != Ared, "sigma must NOT fix A (no Galois-fixed shadow irrep)"
    # sqrt-7 as the quadratic Gauss sum, squares to -7 (the quadratic subfield of Q(zeta7))
    gauss = sum(z**a for a in (1, 2, 4)) - sum(z**a for a in (3, 5, 6))
    assert red7(gauss**2) == -7
    # principle: golden field disc 5 (p=5, 5=1 mod4), E6 field disc -7 (p=7, 7=3 mod4)
    for p, star in [(5, 5), (7, -7)]:
        assert star == ((-1)**((p-1)//2)) * p          # p* = quadratic-subfield disc of Q(zeta_p)


def test_cell3a_galois_is_cubing_the_weld():
    """The golden torsor's Galois Z/2 is realized on the weld as W^k -> W^{3k}
    (mod 10), NOT W^2 (chat1 Fact 5 corrected)."""
    s5 = sp.sqrt(5)
    def trW(k): return sp.expand(sp.nsimplify(2*sp.cos(3*k*sp.pi/5), [s5]))
    def gal(x): return sp.expand(x.subs(s5, -s5))
    # gal(tr W) = tr(W^3), not tr(W^2)
    assert sp.simplify(gal(trW(1)) - trW(3)) == 0
    assert sp.simplify(gal(trW(1)) - trW(2)) != 0
    # the realizing power m: tr(W^{m k}) = gal(tr W^k) for all k -> m in {3,7}
    def trWmod(j):
        j %= 10
        return sp.Integer(2) if j == 0 else trW(j)
    realizing = [m for m in range(1, 10)
                 if all(sp.simplify(trWmod(m*k) - gal(trW(k))) == 0 for k in range(1, 10))]
    assert realizing == [3, 7], f"realizing powers {realizing}, expected [3,7]"
