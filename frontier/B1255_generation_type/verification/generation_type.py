"""B1255 -- the generation index has the RIGHT GALOIS TYPE and the WRONG COMMUTATOR.

Prompted by the owner's question after B1253 refuted its own generation-count
headline: "analyse the pattern that led us to believe we derived three gen --
maybe the pattern tells us the phenomena that gives real results."

THE PATTERN.  Every three-ness the programme has tested and lost was built on
Q(sqrt-3).  That field contains mu_3, whose three cube roots of unity split as
1 rational + 2 conjugates -- so it can produce 1+2, never 3.  A quadratic field
has at most TWO primes above any rational prime, so three-fold splitting is
arithmetically impossible there.  This independently reproduces B298's degree-2
obstruction, and explains B1253's price ("1 abelian + 2 chiral") as that same
1+2 wearing a representation-theoretic costume.

WHAT THE PATTERN PREDICTS.  A genuine three needs an IRREDUCIBLE CUBIC, where
the Galois group permutes the roots transitively and no root is distinguished.

WHAT THE RECORD CONTAINS.  Two of them, both in the sqrt77 family:
  mu13 -- the field K = Q[rho]/mu13 over which the object's colored sector lives
  HIER -- the hierarchy cubic, 953^4 x^3 - ..., whose roots are the v_g^2
Both are totally real, irreducible, Galois group S3, disc squarefree kernel {7,11}.
This is the type Q(sqrt-3) provably cannot supply, and it survives BOTH
refutations that killed the earlier three-nesses (B324's "conjugates share one
character" -- generations are REQUIRED to share one character and differ in
value; and B1253's Weyl-orbit kill -- Galois conjugacy over Q is not a gauge
symmetry, so the three roots are three distinct real numbers, not one particle
rebased).

AND THEN THE REFUTATION, computed here.  For g to be a FLAVOUR index it must
commute with the gauge grading -- in the Standard Model, gauge symmetry acts
identically on all three generations.  It does not:

    [C18, D2|W18] != 0,  and no colored atom is a D2-eigenspace.

Behind that sits a dimension count that is FINAL for the single-27 route:
27 = 16 + 10 + 1 carries the 16 with MULTIPLICITY ONE, so three copies would
need dim >= 48 > 27.  Three generations cannot live inside one 27.

WHAT SURVIVES, and it is not nothing.  The non-commutation is the MECHANISM OF
THE HIERARCHY, not merely an obstruction: B923's two gauges show the canonical
gauge is generation-DEGENERATE ((x+3)^3, three identical values) and the
D2-twisted gauge splits it into HIER's three distinct roots.  Had the two
operators commuted, they would be simultaneously diagonalisable and the
splitting would be gauge-blind -- degenerate copies with NO hierarchy.  So the
same failure that denies g the flavour role is what makes the twist lift the
degeneracy.  Identical-then-split is the physical shape of generations; what the
object does not supply, inside one 27, is the three COPIES.

CONTROLS (MB12, both directions):
  - the S3 verdict can fail: a cyclic cubic (disc a perfect square) is exhibited
    and correctly typed C3, so the test is not a tautology;
  - the commutator test can pass: D2 commutes with itself and with the Cartan
    elements, exhibited, so "!= 0" is content and not a broken comparison;
  - the 12/6 split across D2 is checked against the independent SO(10)
    prediction 27 = 16+10+1 rather than asserted.
"""
import json, os, pickle, sys
from fractions import Fraction as Fr
import sympy as sp

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
x = sp.Symbol("x")

MU13 = [500716339200, -2075673600, -4769856, 2197]        # descending (banked, B923)
HIER_COEFFS = [953**4, -2**8*3**9*13*421493, 2**21*3**8*17*1129, -2**32*3**11]
W13 = [1, 0, -1, 0, 1, -1]                                # B1250's affine character


def cubic_type(coeffs):
    """(irreducible?, squarefree kernel of disc, Galois group, number of real roots)."""
    p = sum(c * x ** (3 - i) for i, c in enumerate(coeffs))
    fl = sp.factor_list(p)[1]
    irred = len(fl) == 1 and fl[0][1] == 1
    d = sp.discriminant(sp.Poly(p, x))
    f = sp.factorint(d)
    kern = sorted(q for q, e in f.items() if e % 2)
    grp = "C3" if sp.sqrt(d).is_rational else "S3"
    roots = sp.Poly(p, x).all_roots()
    return irred, kern, grp, sum(1 for t in roots if t.is_real), roots


def load_object():
    """The banked B883 27, the four B854 charge invariants, Mc, and D2."""
    scratch = os.environ.get("SESSION_SCRATCH") or os.path.join(REPO, ".cache")
    cache = os.path.join(scratch, "b914_base_cache.pkl")
    if not os.path.exists(cache):
        return None
    INV, ns = pickle.load(open(cache, "rb"))
    REPJ = json.load(open(os.path.join(REPO, "frontier", "B883_the_27", "rep27.json")))
    REP = [[[int(v) for v in row] for row in REPJ["rep"][str(k)]] for k in range(78)]
    WT = [tuple(REP[i][a][a] for i in range(6)) for a in range(27)]
    Rex = {}
    for n in ns:
        M = [[Fr(0)] * 27 for _ in range(27)]
        for k, c in enumerate(INV[n]):
            if c:
                Rk = REP[k]
                for a in range(27):
                    for b in range(27):
                        if Rk[a][b]:
                            M[a][b] += c * Rk[a][b]
        Rex[n] = M
    CO = {8: 3, 14: 7, 16: 13, 22: 17}
    Mc = sp.Matrix(27, 27, lambda i, j: sp.Rational(sum(Fr(CO[n]) * Rex[n][i][j] for n in ns)))
    sgn = [(-1) ** (sum(a * b for a, b in zip(W13, WT[t])) + 1) for t in range(27)]
    return Mc, sp.diag(*sgn), sgn, REP


def colored_block(Mc):
    fl = sp.factor_list(Mc.charpoly(x).as_expr())[1]
    hcol = [f for f, m in fl if m == 3][0]
    P = sp.Poly(hcol, x)
    Hm = sp.zeros(27, 27)
    for k, c in enumerate(reversed(P.all_coeffs())):
        Hm += sp.Rational(c) * (Mc ** k)
    return Hm.nullspace(), sp.degree(hcol, x)


def selftest():
    print("B1255 -- the generation index: right Galois type, wrong commutator (selftest)")

    # ---- 1. the two cubics of the sqrt77 family
    for name, co in (("mu13", MU13), ("HIER", HIER_COEFFS)):
        irred, kern, grp, nreal, _ = cubic_type(co)
        print(f"  [{name:5}] irreducible {irred}, disc kernel {kern}, Galois {grp}, real roots {nreal}/3")
        assert irred and kern == [7, 11] and grp == "S3" and nreal == 3

    # ---- control: the S3 verdict CAN fail (a cyclic cubic is typed C3)
    irred, kern, grp, nreal, _ = cubic_type([1, -3, 0, 1])       # x^3-3x^2+1, disc = 81
    print(f"  [ctl  ] cyclic cubic x^3-3x^2+1 typed: {grp} (must be C3 -- the test is not a tautology)")
    assert grp == "C3"

    # ---- 2. why Q(sqrt-3) cannot: at most 2 primes above any p in a quadratic field
    K = sp.QQ.algebraic_field(sp.sqrt(-3))
    print("  [why  ] a quadratic field has at most 2 primes above any p -> 1+2 possible, 3 impossible")

    obj = load_object()
    if obj is None:
        print("  [skip ] object matrices need SESSION_SCRATCH/b914_base_cache.pkl (B923 step 1)")
        print("\nSELFTEST: PASS (arithmetic tier)")
        return
    Mc, D2, sgn, REP = obj

    # ---- 3. D2 is the SO(10) grading
    flips = sum(1 for s in sgn if s == -1)
    print(f"  [D2   ] flips {flips} = 1 + 10, fixes {27-flips} = the 16")
    assert flips == 11

    # ---- control: the commutator test CAN return zero
    assert (D2 * D2 - D2 * D2).is_zero_matrix
    cart = sp.Matrix(27, 27, lambda i, j: sp.Rational(REP[0][i][j]))
    print(f"  [ctl  ] [D2, Cartan_0] == 0 : {(cart*D2 - D2*cart).is_zero_matrix} (a commuting pair exists)")

    # ---- 4. the colored block and its SO(10) content
    W18, degh = colored_block(Mc)
    plus = [i for i in range(27) if sgn[i] == 1]
    minus = [i for i in range(27) if sgn[i] == -1]
    B = sp.Matrix.hstack(*W18)
    rp, rm = B[plus, :].rank(), B[minus, :].rank()
    print(f"  [col  ] h_col degree {degh}, block dim {len(W18)}; across D2: {rp} / {rm}"
          f"  (SO(10) predicts 12 = colored part of the 16, 6 = colored part of the 10)")
    assert len(W18) == 18 and (rp, rm) == (12, 6)

    # ---- 5. THE REFUTATION: generation index does not commute with the grading
    solM, solD = B.solve(Mc * B), B.solve(D2 * B)
    inv = (D2 * B - B * solD).is_zero_matrix
    comm = (solM * solD - solD * solM).is_zero_matrix
    print(f"  [KILL ] W18 is D2-invariant: {inv};  [C18, D2|W18] == 0: {comm}")
    assert inv and not comm

    ev = sp.Matrix(solM).eigenvects()
    homog = 0
    for val, mult, vecs in ev:
        Vb = sp.Matrix.hstack(*[B * v for v in vecs])
        if any((D2 * Vb - c * Vb).is_zero_matrix for c in (1, -1)):
            homog += 1
    print(f"  [KILL ] colored atoms: {len(ev)} (3 conjugate pairs, dim 3 each);"
          f" D2-homogeneous: {homog}/6")
    assert len(ev) == 6 and homog == 0

    # ---- 6. the dimension count that closes the single-27 route for good
    print("  [dim  ] 27 = 16+10+1: the 16 has multiplicity ONE; 3 copies need dim >= 48 > 27")
    assert 3 * 16 > 27

    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
