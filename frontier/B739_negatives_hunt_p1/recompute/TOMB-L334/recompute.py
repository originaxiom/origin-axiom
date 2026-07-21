"""B739 Stage-B recompute -- TOMB-L334 (TOMBSTONES.md:L334, the B565/R1 "B85 Sym(W)->trace-ring
functor wall" kill).

BANKED KILL (verbatim target): "The functor provably cannot reach the multiplicity-2 char(M^2)
sector before n=5: mult(char(M^h)) at height 2 = ceil((n-2)/2) (orbit enumeration verified
n=3..15; a theta-fixed height-2 index exists iff n odd; n=5 is the first with dimension 2)."

THE DISCRIMINATING FACT (what, if true, kills the claim that the functor could reach the
mult-2 char(M^2) sector below n=5):
  (F1) the (+1,-1) eigenspace dimensions of theta=-w0 on the height-h positive-root space of
       A_{n-1} are (ceil((n-h)/2), floor((n-h)/2));  at h=2: (ceil((n-2)/2), floor((n-2)/2));
  (F2) a theta-fixed height-2 index exists iff n is odd;
  (F3) hence NO height-2 sector has dimension 2 for n<5, and n=5 is the first n whose larger
       (char(M^2)-labeled) sector has dimension 2.

E19 COMPUTE-NOT-CITE: everything below is re-derived here by direct enumeration and exact
(Fraction) linear algebra from the source arcs' DECLARED conventions -- no repo module is
imported, no banked number is read back in.

DECLARED CONVENTIONS (one-hop sources; E1 -- every choice named):
  C1 (B112 probe.py / B62 probe.py): root system A_{n-1}; positive roots e_i-e_j, 1<=i<j<=n;
      height h = j-i; the height-h positive roots are {e_i - e_{i+h} : i=1..n-h} (m = n-h).
  C2 (B62/B112): the opposition involution theta = -w0 acts by (i,j) |-> (n+1-j, n+1-i).
  C3 (B62, declared verbatim: "The convention -- fixed roots in the +1/symmetric sector -- is
      fixed empirically by SL(3)"; = the banked B64 assignment): the +1 (theta-symmetric)
      sector carries char(M^h), the -1 sector char(-M^h). Tower-verified n<=5 (B62 height-2
      splits (1,0),(1,1),(2,1); B118 note). This LABELING is a convention input, so S3 below
      also checks the kill's robustness if the labeling were flipped at even h (the B118
      signed-fixed-root refinement).
  C4 (B62): M = [[1,1],[1,0]] (Fibonacci, m=1); char(M^h) = t^2 - L_h t + (-1)^h,
      char(-M^h) = t^2 + L_h t + (-1)^h, L_h = tr(M^h) (Lucas).
  C5 (B118): the signed realization tau(X) = -J X^T J^{-1}, J_{p,q} = eps_p delta_{q,n+1-p},
      eps_p = (-1)^{p+1}; banked fixed-root sign (-1)^{h+1} -- recomputed here.
  E1 choices made here: eigenspace dimensions are computed on the span of the POSITIVE
      height-h roots (B112's convention; B62 enumerates both signs and halves -- both are run
      and cross-checked); "theta-fixed height-2 index" is read as a fixed point of the theta
      action on the height-2 positive-root index set; the enumeration range is n=3..15, the
      depth the tombstone itself declares.

Deterministic: stdlib only (math, fractions, itertools); exact integer/rational arithmetic;
no wall-clock, no randomness, no network.
"""

from fractions import Fraction
from math import ceil, floor

NMAX = 15  # the tombstone's own declared enumeration depth: n = 3..15


# --------------------------------------------------------------------------- #
# exact linear algebra over Q (Fraction Gaussian elimination)
# --------------------------------------------------------------------------- #
def rank_QQ(rows):
    """Exact rank of a rational matrix (list of lists of Fractions)."""
    A = [[Fraction(x) for x in row] for row in rows]
    if not A:
        return 0
    nr, nc = len(A), len(A[0])
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = A[r][c]
        A[r] = [v / inv for v in A[r]]
        for i in range(nr):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
        if r == nr:
            break
    return r


def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def mat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def identity(m):
    return [[Fraction(int(i == j)) for j in range(m)] for i in range(m)]


# --------------------------------------------------------------------------- #
# S1 -- theta = -w0 on the height-h roots of A_{n-1}: enumeration from C1/C2
# --------------------------------------------------------------------------- #
def positive_height_h_roots(n, h):
    return [(i, i + h) for i in range(1, n - h + 1)]


def theta(n, root):
    i, j = root
    return (n + 1 - j, n + 1 - i)


def orbit_data(n, h):
    """Direct orbit enumeration of theta on the positive height-h roots.
    Returns (m, fixed_count, twocycle_count, index_map) after verifying:
    theta preserves the set, theta^2 = id, and the induced index action is the
    reversal sigma(i) = (n-h+1) - i."""
    roots = positive_height_h_roots(n, h)
    m = len(roots)
    rset = set(roots)
    for r in roots:
        assert theta(n, r) in rset, (n, h, r)            # closure (height-preserving)
        assert theta(n, theta(n, r)) == r, (n, h, r)     # involution
    # induced action on the index i (root (i, i+h) -> index i)
    index_map = {}
    for (i, j) in roots:
        ii, jj = theta(n, (i, j))
        assert jj - ii == h
        index_map[i] = ii
        assert ii == (n - h + 1) - i, (n, h, i, ii)      # = the reversal sigma
    fixed = sum(1 for i in index_map if index_map[i] == i)
    twocyc = sum(1 for i in index_map if index_map[i] > i)
    assert fixed + 2 * twocyc == m
    return m, fixed, twocyc, index_map


def eigsplit_orbit(n, h):
    """(+1,-1) eigenspace dims from the orbit count: a fixed vector contributes (+1),
    a 2-cycle contributes one (+1) and one (-1) (unsigned permutation involution)."""
    m, fixed, twocyc, _ = orbit_data(n, h)
    return (fixed + twocyc, twocyc)


def eigsplit_linear(n, h):
    """The same dims by INDEPENDENT exact linear algebra: P the permutation matrix of theta
    on the positive height-h roots; P^2=I verified; dims = (dim ker(P-I), dim ker(P+I))."""
    roots = positive_height_h_roots(n, h)
    m = len(roots)
    idx = {r: k for k, r in enumerate(roots)}
    P = [[Fraction(0)] * m for _ in range(m)]
    for r in roots:
        P[idx[theta(n, r)]][idx[r]] = Fraction(1)
    I = identity(m)
    assert mat_eq(mat_mul(P, P), I), (n, h)              # involution => eigenvalues +-1
    PmI = [[P[i][j] - I[i][j] for j in range(m)] for i in range(m)]
    PpI = [[P[i][j] + I[i][j] for j in range(m)] for i in range(m)]
    dplus = m - rank_QQ(PmI)
    dminus = m - rank_QQ(PpI)
    assert dplus + dminus == m                           # diagonalizable involution
    return (dplus, dminus)


def eigsplit_b62_bothsigns(n, h):
    """B62's own convention (both signs, |i-j|=h) halved -- third cross-check."""
    roots = [(i, j) for i in range(1, n + 1) for j in range(1, n + 1)
             if i != j and abs(i - j) == h]
    seen, fixed, twocyc = set(), 0, 0
    for r in roots:
        if r in seen:
            continue
        tr = theta(n, r)
        if tr == r:
            fixed += 1
            seen.add(r)
        else:
            twocyc += 1
            seen.update((r, tr))
    plus, minus = fixed + twocyc, twocyc
    assert plus % 2 == 0 and minus % 2 == 0
    return (plus // 2, minus // 2)


# --------------------------------------------------------------------------- #
# S3 -- the B118 signed check (C5): tau(X) = -J X^T J^{-1} on the lone fixed root
# --------------------------------------------------------------------------- #
def signed_fixed_root_sign(n, h):
    """Exact scalar by which tau acts on E_{i0,i0+h} at the theta-fixed index i0
    (exists iff m = n-h is odd). Built from C5; no formula assumed."""
    m = n - h
    assert m % 2 == 1
    i0 = (n - h + 1) // 2                                # the reversal's fixed index
    E = [[Fraction(0)] * n for _ in range(n)]
    E[i0 - 1][i0 + h - 1] = Fraction(1)
    J = [[Fraction(0)] * n for _ in range(n)]
    for p in range(1, n + 1):
        J[p - 1][(n + 1 - p) - 1] = Fraction((-1) ** (p + 1))
    # exact inverse of J by Gauss-Jordan
    A = [row[:] + Irow[:] for row, Irow in zip(J, identity(n))]
    for c in range(n):
        piv = next(i for i in range(c, n) if A[i][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        inv = A[c][c]
        A[c] = [v / inv for v in A[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[c])]
    Jinv = [row[n:] for row in A]
    assert mat_eq(mat_mul(J, Jinv), identity(n))
    Et = [[E[j][i] for j in range(n)] for i in range(n)]
    tauE = [[-x for x in row] for row in mat_mul(mat_mul(J, Et), Jinv)]
    # tau(E) must be a scalar multiple of E itself (the fixed root)
    s = tauE[i0 - 1][i0 + h - 1]
    for i in range(n):
        for j in range(n):
            expect = s if (i, j) == (i0 - 1, i0 + h - 1) else 0
            assert tauE[i][j] == expect, (n, h, i, j)
    return int(s)


# --------------------------------------------------------------------------- #
# S4 -- the char-factor objects (C4): the sector labels are distinct, well-defined
# --------------------------------------------------------------------------- #
def char_factor_check():
    """M=[[1,1],[1,0]]: tr(M^h)=Lucas L_h; char(M^2)=t^2-3t+1, char(-M^2)=t^2+3t+1 (distinct,
    so 'the mult-2 char(M^2) sector' is a well-defined target); phi^{+-2} are exactly the
    roots of char(M^2) -- verified in Q(sqrt5) as (a+b*sqrt5) pairs, exact."""
    M = [[1, 1], [1, 0]]
    P = [[1, 0], [0, 1]]
    lucas = []
    for _ in range(1, 5):
        P = [[sum(P[i][k] * M[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        lucas.append(P[0][0] + P[1][1])
    assert lucas == [1, 3, 4, 7], lucas                   # L_1..L_4
    L2 = lucas[1]                                         # char(M^2)=t^2-3t+1, char(-M^2)=t^2+3t+1
    assert L2 == 3 and L2 != -L2                          # the two h=2 labels are DISTINCT polynomials
    # Q(sqrt5) arithmetic: x = (a, b) means a + b*sqrt5, a,b rational
    def mul(x, y):
        return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
    phi2 = (Fraction(3, 2), Fraction(1, 2))               # phi^2 = (3+sqrt5)/2
    phim2 = (Fraction(3, 2), Fraction(-1, 2))             # phi^-2 = (3-sqrt5)/2
    assert mul(phi2, phim2) == (Fraction(1), Fraction(0))                     # product = det = 1
    assert (phi2[0] + phim2[0], phi2[1] + phim2[1]) == (Fraction(3), Fraction(0))  # sum = L_2 = 3
    for x in (phi2, phim2):                               # x^2 - 3x + 1 = 0 exactly
        x2 = mul(x, x)
        assert (x2[0] - 3 * x[0] + 1, x2[1] - 3 * x[1]) == (Fraction(0), Fraction(0))
    return True


# --------------------------------------------------------------------------- #
# main -- the recompute
# --------------------------------------------------------------------------- #
def main():
    print("=" * 78)
    print("B739 Stage-B recompute -- TOMB-L334 (B565/R1: the B85 Sym(W)->trace-ring wall)")
    print("=" * 78)

    # S1: full enumeration n=3..15, all heights, three independent methods
    print(f"\n[S1] theta=-w0 on height-h positive roots, n=3..{NMAX}, all h: "
          "orbit count vs exact-QQ eigenspaces vs B62 both-signs vs (ceil,floor)")
    all_ok = True
    for n in range(3, NMAX + 1):
        for h in range(1, n):
            m = n - h
            cf = (ceil(m / 2), floor(m / 2))
            a, b, c = eigsplit_orbit(n, h), eigsplit_linear(n, h), eigsplit_b62_bothsigns(n, h)
            ok = a == b == c == cf
            all_ok &= ok
            if not ok:
                print(f"    MISMATCH n={n} h={h}: orbit={a} linear={b} b62={c} closed={cf}")
    print(f"    all (n,h) agree with (ceil((n-h)/2), floor((n-h)/2)): {all_ok}")
    assert all_ok

    # S2: the height-2 specialization -- the discriminating numbers
    print(f"\n[S2] height h=2, n=3..{NMAX}:  (+1,-1) dims  |  theta-fixed index?  |  n odd?")
    first_dim2 = None
    iff_ok = True
    pre5_max = 0
    for n in range(3, NMAX + 1):
        dplus, dminus = eigsplit_linear(n, 2)
        _, fixed, _, imap = orbit_data(n, 2)
        has_fixed = fixed == 1
        assert fixed in (0, 1)
        iff_ok &= (has_fixed == (n % 2 == 1))
        if dplus == 2 and first_dim2 is None:
            first_dim2 = n
        if n < 5:
            pre5_max = max(pre5_max, dplus, dminus)
        fx = next((i for i in imap if imap[i] == i), "-")
        print(f"    n={n:>2}: ({dplus},{dminus})   fixed-index: {str(has_fixed):5s} (i0={fx})"
              f"   n odd: {n % 2 == 1}")
    print(f"    theta-fixed height-2 index exists IFF n odd: {iff_ok}")
    print(f"    first n with a dimension-2 (+1)-sector at height 2: n={first_dim2}")
    print(f"    max dimension of EITHER height-2 sector over n<5: {pre5_max}  (< 2)")
    assert iff_ok and first_dim2 == 5 and pre5_max == 1

    # S3: the labeling (C3) and its robustness (B118 signed refinement, recomputed)
    print("\n[S3] labeling: C3/B64 puts the +1 sector = char(M^h) (tower-fixed, n<=5)."
          "\n     B118 signed check recomputed from C5 -- tau(X) = -J X^T J^{-1}:")
    sign_ok = True
    for n in range(3, NMAX + 1):
        for h in range(1, n):
            if (n - h) % 2 == 1:
                sign_ok &= (signed_fixed_root_sign(n, h) == (-1) ** (h + 1))
    print(f"    fixed-root sign == (-1)^(h+1) for all n<=15, all h with n-h odd: {sign_ok}")
    assert sign_ok
    print("    at h=2 the signed fixed-root scalar is -1 (n odd): the char(M^2)=ceil labeling")
    print("    is the tower-fixed CONVENTION, not the signed-tau eigensector -- so check both:")
    seq_ceil = [ceil((n - 2) / 2) for n in range(3, NMAX + 1)]
    seq_floor = [floor((n - 2) / 2) for n in range(3, NMAX + 1)]
    f_ceil = 3 + seq_ceil.index(2)
    f_floor = 3 + seq_floor.index(2)
    print(f"      banked labeling  (char(M^2)=ceil):  mult n=3..15 = {seq_ceil}; first 2 at n={f_ceil}")
    print(f"      flipped labeling (char(M^2)=floor): mult n=3..15 = {seq_floor}; first 2 at n={f_floor}")
    assert f_ceil == 5 and f_floor == 6
    print("    => under EITHER labeling no mult-2 char(M^2) sector exists before n=5;")
    print("       the banked (tower-verified n<=5) labeling gives first dim-2 exactly at n=5.")

    # S4: the char-factor objects are distinct and correctly rooted
    print(f"\n[S4] C4 sanity: L_h=tr(M^h)=(1,3,4,7); char(M^2)=t^2-3t+1 != char(-M^2)=t^2+3t+1;"
          f"\n     phi^(+-2) are the exact roots of char(M^2) in Q(sqrt5): {char_factor_check()}")

    # verdict
    print("\n" + "=" * 78)
    print("VERDICT: RECONFIRMED")
    print("=" * 78)
    print("""\
Recomputed from C1-C5 by direct enumeration + exact rational linear algebra (three
independent methods agreeing at every (n,h), n=3..15):
  mult at height 2 = ceil((n-2)/2):  n=3->1, n=4->1, n=5->2 (first 2), n=6->2, ...
  theta-fixed height-2 index exists iff n odd (i0=(n-1)/2), verified n=3..15;
  no height-2 sector of ANY labeling has dimension 2 for n<5 (max dim = 1);
  n=5 is the first n whose char(M^2)-labeled sector has dimension 2.
The banked kill's discriminating fact holds: the Sym(W)->trace-ring functor's target,
the multiplicity-2 char(M^2) sector, does not exist before n=5 -- the finite-level
obstruction stands. (Robust to the B118 sign refinement: flipping the even-h labeling
only moves the first dim-2 to n=6, strengthening 'not before n=5'.)""")


if __name__ == "__main__":
    main()
