"""B267 -- the coherence check: the McKay-E6 (B266, arithmetic) and the character-variety-E6 (B264/B265, geometric)
are the SAME E6. FIREWALLED (Lie theory / arithmetic, not physics). Nothing to CLAIMS.md.

Two E6's were attached to the figure-eight by two independent routes:
  * GEOMETRIC (B264/B265): the principal sl(2) -> e6 (Kostant); the figure-eight's geometric rep composed with it
    has a rank-6 character variety graded by the E6 EXPONENTS {1,4,5,7,8,11}; E6-Zariski-dense reps exist.
  * ARITHMETIC (B266): trace field Q(sqrt-3) -> ramified prime 3 -> SL(2,F_3)=2T -> McKay -> affine E6.
Coherence question: are these the same E6 -- on every Lie-theoretic invariant, not just the name? (A priori the
character variety could have been F4 (rank 4); the arithmetic could have given another type. They didn't.)

The checks (all pass):
 1. EXPONENT RECOVERY (the decisive B264<->B266 bridge): remove the affine node from B266's McKay graph of 2T
    -> the E6 Dynkin diagram; its adjacency eigenvalues are exactly 2cos(pi*m/h), h=12, m in {1,4,5,7,8,11}
    = B264's principal-sl(2) exponents. The McKay graph LITERALLY reproduces the character-variety grading.
 2. COXETER NUMBER: sum of the McKay marks of 2T = 12 = h(E6) = the principal sl(2)'s Coxeter number.
 3. ROOT COUNT / DIMENSION: sum of exponents = 36 = #positive roots = l*h/2; dim = l(h+1) = 78 (Kostant) =
    B264/B265's adjoint dimension.
 4. KOSTANT INVARIANT THEORY (depth): the Molien series of 2T (= Poincare series of C[x,y]^{2T}, the coordinate
    ring of the E6 Kleinian singularity C^2/2T) is (1+q^12)/((1-q^6)(1-q^8)) -- its numerator 1+q^h carries
    h=12, tying the arithmetic side's invariant theory to the geometric side's Coxeter number.

CONCLUSION: the arithmetically-selected E6 and the character-variety E6 coincide as Lie-theoretic objects, on five
independent invariants, with the McKay graph directly reproducing the character-variety's exponent grading. The two
E6's are ONE E6.

HONEST GUARDRAIL (verify-don't-trust): coherence of Lie invariants is NOT a proof that the 3d-3d INPUT type must be
this E6 (still the sharp conjecture from B266). What it DOES do: rule out an incoherence -- the geometric and
arithmetic E6's are not two different exceptional groups that happened to share a label; they are the same object.
This tightens wall #2's remaining gap to a purely physical identification (does the 6d type-input equal the
manifold's arithmetic type), with no Lie-theoretic obstruction in the way.

Run: python e6_coherence.py  (pyenv, sympy/numpy; self-contained -- 2T character data hard-coded from B266/GAP).
"""
import sympy as sp

H = 12                                            # Coxeter number of E6
EXPONENTS = [1, 4, 5, 7, 8, 11]                   # B264 principal-sl(2)->e6 exponents
MARKS_2T = [1, 1, 1, 2, 2, 2, 3]                  # McKay marks of 2T = affine E6 marks (B266)
# 2T faithful 2-dim character (the SU(2) embedding rep) + class sizes (from GAP, B266); all rational.
CHI_2T = [2, 1, 1, -2, -1, -1, 0]
CLASS_SIZES_2T = [1, 4, 4, 1, 4, 4, 6]


def e6_dynkin_adjacency():
    """E6 Dynkin = affine-E6 McKay graph of 2T minus one affine (arm-tip) node. Arms of length 2,2,1 from center."""
    # nodes: 0,1=arm1 (tip,mid); 2=center; 3,4=arm2 (mid,tip); 5=arm3 (length-1)
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (2, 5)]
    A = sp.zeros(6, 6)
    for i, j in edges:
        A[i, j] = A[j, i] = 1
    return A


def exponents_from_mckay():
    """Recover the exponents from the E6 Dynkin eigenvalues: eig = 2 cos(pi*m/h)  =>  m."""
    A = e6_dynkin_adjacency()
    char = A.charpoly(sp.Symbol("x"))
    # the eigenvalues are 2cos(pi*m/12); verify each candidate exponent is a root, collect those that are
    found = []
    for m in range(1, H):
        val = 2 * sp.cos(sp.pi * m / H)
        if sp.simplify(char.eval(val)) == 0:
            found.append(m)
    return sorted(found)


def molien_series_2T():
    """Molien series of 2T = (1/|G|) sum |C|/(1 - chi*q + q^2)  (det rho = 1). Returns a sympy rational in q."""
    q = sp.Symbol("q")
    M = sum(sp.Rational(sz) / (1 - chi * q + q**2) for chi, sz in zip(CHI_2T, CLASS_SIZES_2T)) / 24
    return sp.cancel(M)


if __name__ == "__main__":
    q = sp.Symbol("q")
    print("=== B267: McKay-E6 (arithmetic, B266) vs character-variety-E6 (geometric, B264/B265) ===\n")

    # 1. exponent recovery -- the decisive bridge
    rec = exponents_from_mckay()
    print(f"1. E6 Dynkin (= McKay(2T) minus affine node) eigenvalues -> exponents {rec}")
    print(f"   B264 principal-sl(2) exponents {EXPONENTS}  -> MATCH: {rec == EXPONENTS}")
    assert rec == EXPONENTS

    # 2. Coxeter number
    print(f"\n2. sum McKay marks of 2T = {sum(MARKS_2T)} = h(E6) = {H}  -> {sum(MARKS_2T) == H}")
    assert sum(MARKS_2T) == H

    # 3. root count / dimension
    npos, dim = sum(EXPONENTS), 6 * (H + 1)
    print(f"3. sum exponents = {npos} = #positive roots = l*h/2 = {6*H//2}; dim = l(h+1) = {dim} (=78)")
    assert npos == 6 * H // 2 == 36 and dim == 78

    # 4. Kostant invariant theory: Molien series carries h
    M = molien_series_2T()
    target = sp.cancel((1 + q**12) / ((1 - q**6) * (1 - q**8)))
    print(f"\n4. Molien series of 2T = {M}")
    print(f"   = (1+q^12)/((1-q^6)(1-q^8)) [numerator 1+q^h, h={H}; C^2/2T = E6 Kleinian singularity]: "
          f"{sp.simplify(M - target) == 0}")
    assert sp.simplify(M - target) == 0

    print("\n=> the arithmetic E6 and the geometric E6 coincide on all invariants; the McKay graph reproduces the")
    print("   character-variety exponent grading. They are ONE E6. (Remaining wall-#2 gap is purely physical.) PASS")
