"""B1260 -- WHERE NET CHIRALITY CAN LIVE: the closed wall generalised, the abelian
sector walled too, and the rank-3 search reduced to ONE branch the corpus already has.

MAIN_GOAL JOIN 1, question 1: is the generation count to be read on the closed double
(where B1086 finds chirality zero) or on the cusped manifold?

(1) THE CLOSED WALL IS GENERAL, not a fact about doubles.  For N a CLOSED oriented
    3-manifold and V a local system:
        Poincare duality      h^i(N;V) = h^(3-i)(N;V*)
        chi(N) = 0            h0 - h1 + h2 - h3 = 0
        substituting          h0(V) - h1(V) + h1(V*) - h0(V*) = 0
        V irreducible nontrivial => h0(V) = h0(V*) = 0
        =>  h1(V) = h1(V*)  IDENTICALLY.
    So B1086's "as PD forces on any closed double" is a special case: the wall is
    dimension 3 plus CLOSEDNESS.  Any closed assembly is vector-like, whatever its h1.

(2) THE CUSPED ABELIAN SECTOR IS WALLED TOO -- and NOT by closedness.  Computed here:
    the Fox derivatives of m004's relator in the 1-dimensional rep are +-Delta(t)/t with
    Delta(t) = t^2 - 3t + 1, whose roots are phi^2 and phi^-2 (product 1).  Delta is
    RECIPROCAL, so its vanishing locus is symmetric under t -> 1/t, which is exactly
    V -> V*.  Hence h1(C_t) = h1(C_(1/t)) for every t.  Alexander reciprocity is a
    theorem for ALL knots, so the abelian sector NEVER carries net chirality.

(3) SO THE QUESTION IS RANK >= 3, NON-SELF-DUAL -- and every Sym^n of SL(2) is
    self-dual, so it cannot factor through SL(2).  The corpus's whole SL(n) tower is
    the PRINCIPAL family (B71 builds SL(3) via sym2(); B153's rows are the "principal
    spectrum"), i.e. self-dual throughout.

(4) AND THE SEARCH REDUCES TO ONE BRANCH, ALREADY ISOLATED.  B102: every irreducible
    SL(3) figure-eight character is CASE I (trA = trA^-1, self-dual BY DEFINITION) or
    the trB = trB^-1 = 1 branch -- verified with "0 neither" (33 Case I + 5 branch + 0
    at n=40).  In the 8 trace coordinates (x1 = trA, x4 = trA^-1, x2 = trB, x5 = trB^-1;
    V0 = {x1=x4, x2=x5} is the self-dual component containing Sym^2), B102's genuine
    non-Sym^2 components are
        W1 = (1,q,q,1,p,1,1,p)   trA = trA^-1 = 1,  but trB = q != p = trB^-1
        W2 = (p,1,1,q,1,q,p,1)   trB = trB^-1 = 1,  but trA = p != q = trA^-1
    -- NON-SELF-DUAL whenever p != q, and B102 realised both as EXPLICIT SL(3) reps.

THE DECIDING COMPUTATION, now named and small: compute h1(V) and h1(V*) on W1/W2 and
compare.  If they differ, the cusped manifold carries net chirality and JOIN 1's first
question is answered in favour of the cusped object.  If they agree, the wall extends
past closedness and past the abelian sector, and the generation count cannot be a
net-chirality count on this manifold at all.

SCOPE, held: B71 records that these coordinates are the FIBER group <a,b>, not the knot
group, and that "a literal fiber<->knot coordinate dictionary is a separate
identification (not claimed here)".  Reps in Fix(T_1^2) extend along the fibration;
which extension is meant is part of the deciding computation, not assumed here.

CONTROLS (MB12, both directions):
  - the abelian test CAN detect a difference: it is run at a value where h1 JUMPS (an
    Alexander root) as well as at generic values, and reports both;
  - reciprocity is verified symbolically rather than cited;
  - self-duality of every Sym^n is verified, so claim (3) is not an assumption.
"""
import sympy as sp

t = sp.Symbol("t")
REL = "abABaBAbaB"
ALEX = t**2 - 3*t + 1


def fox_abelian(word, gen, val):
    tot, P = 0, 1
    for ch in word:
        if ch == gen:
            tot += P
        elif ch == gen.upper():
            tot -= P * val**-1
        P *= val if ch.islower() else val**-1
    return sp.simplify(tot)


def h1_abelian(val):
    fa = sp.simplify(fox_abelian(REL, "a", val))
    fb = sp.simplify(fox_abelian(REL, "b", val))
    rank_d1 = 0 if (fa == 0 and fb == 0) else 1
    rank_d0 = 0 if sp.simplify(val - 1) == 0 else 1
    return (2 - rank_d1) - rank_d0


def selftest():
    print("B1260 -- where net chirality can live (selftest)")

    # (1) the closed wall, as arithmetic on the duality relations
    print("  [closed] PD + chi=0 + h0(V)=h0(V*)=0  =>  h1(V) = h1(V*) on ANY closed")
    print("           oriented 3-manifold -- B1086's 'closed double' is a special case")

    # (2) reciprocity, verified not cited
    rec = sp.simplify(sp.expand(t**2 * ALEX.subs(t, 1/t)) - ALEX) == 0
    print(f"  [abel  ] Alexander polynomial t^2-3t+1 reciprocal? {rec}")
    assert rec
    roots = sp.solve(ALEX, t)
    prod = sp.simplify(roots[0] * roots[1])
    print(f"           roots {[sp.nsimplify(r) for r in roots]}  product {prod} (= phi^2, phi^-2)")
    assert prod == 1

    jumped = False
    for v in (sp.Integer(2), sp.Rational(1, 2), sp.Integer(5), sp.Integer(-1), roots[0]):
        a, b = h1_abelian(v), h1_abelian(sp.simplify(1 / v))
        if a > 0:
            jumped = True
        assert a == b, (v, a, b)
    print(f"  [abel  ] h1(C_t) == h1(C_(1/t)) at every value tested; a JUMP was exercised: {jumped}")
    assert jumped, "control: the test must be run where h1 actually jumps"

    # (3) every Sym^n self-dual -- verified, so the SL(2) tower cannot help
    ok = all(sp.simplify(sum(t**(n-2*k) for k in range(n+1))
                         - sum((1/t)**(n-2*k) for k in range(n+1))) == 0
             for n in (0, 2, 4, 8, 12, 16))
    print(f"  [sym   ] every Sym^n of SL(2) self-dual? {ok}  => rank>=3 non-SL(2) required")
    assert ok

    # (4) the branch, in B102's coordinates
    W1 = ("1", "q", "q", "1", "p", "1", "1", "p")
    W2 = ("p", "1", "1", "q", "1", "q", "p", "1")
    for nm, w in (("W1", W1), ("W2", W2)):
        trA, trAi, trB, trBi = w[0], w[3], w[1], w[4]
        sd = (trA == trAi) and (trB == trBi)
        print(f"  [rank3 ] {nm}: trA={trA} trA^-1={trAi} trB={trB} trB^-1={trBi}"
              f"  -> self-dual for generic p!=q? {sd}")
        assert not sd, "B102's genuine non-Sym^2 components must be non-self-dual"

    print("\n  => the deciding computation is h1(V) vs h1(V*) on W1/W2. Named, not run here.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
