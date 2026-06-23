"""B198 -- Sage/Singular Groebner leg: the EXACT m=1 metallic exponent at SL(3) + rigorous existence.

The B157 note said the wall "needs a real CAS (Singular / Macaulay2 / Sage)". Sage IS installed
(`command -v sage`), so the mark was premature. This reproduces the SL(3) cells EXACTLY:
build the m=1 ideal in t-entries over Q(zeta_o), decompose into components, and read
k = min{ j : [A,B]*mu^-j is scalar mod the geometric component prime }.

  SL3 o3 {1,w,w2} -> k=4  (geometric components; reducible components give no finite k)
  SL3 o4 {1,i,-i} -> k=3

`dim_cell` gives RIGOROUS existence via ideal dimension (dim<0 <=> empty), used to certify the
grid sparsity that random Newton can only *fail to find*.

NOTE: primary decomposition is exponential; it is fast at SL(3) (9 vars) but stalls at SL(4)
(16 vars) and the SL(5) ideal-dimension is itself heavy -- the wall MOVED to exact-symbolic at
>=16 vars, it did not vanish. Run with: `sage-python sage_groebner.py`  (NOT the pyenv python).
Standalone character-variety math; nothing to CLAIMS.md.
"""
from sage.all import CyclotomicField, PolynomialRing, matrix, ideal


def _build(o, n, exps):
    K = CyclotomicField(o); z = K.gen(); diag = [z**e for e in exps]
    A = matrix(K, n, n, lambda i, j: diag[i] if i == j else 0)
    Ai = matrix(K, n, n, lambda i, j: diag[i]**-1 if i == j else 0)
    Ai2 = matrix(K, n, n, lambda i, j: diag[i]**-2 if i == j else 0)
    names = ['t%d_%d' % (i, j) for i in range(n) for j in range(n)]
    R = PolynomialRing(K, names, order='degrevlex'); g = R.gens()
    t = matrix(R, n, n, lambda i, j: g[i * n + j])
    Rmat = t * Ai2 * t * A - Ai * t * A * t           # m=1 single-t relation
    I = ideal(list(Rmat.list()) + [t.det() - 1])
    return K, A, Ai, Ai2, t, I, n


def exact_k(o, n, exps, label, kmax=8):
    K, A, Ai, Ai2, t, I, n = _build(o, n, exps)
    print("\n=== %s (o=%d n=%d) : ideal dim %d ===" % (label, o, n, I.dimension()))
    B = Ai2 * t * A * t.adjugate()         # = B mod I (det t == 1 mod I)
    comm = A * B * Ai * B.adjugate()       # = [A,B] mod I
    mu = Ai * t; adj_mu = mu.adjugate()    # = mu^-1 mod I

    def is_scalar(M, P):
        for i in range(n):
            for j in range(n):
                if i != j and M[i, j] not in P:
                    return False
        return all((M[i, i] - M[0, 0]) in P for i in range(1, n))

    for idx, P in enumerate(I.minimal_associated_primes()):
        cur = comm; k = None
        for j in range(kmax + 1):
            if is_scalar(cur, P):
                k = j; break
            cur = cur * adj_mu
        print("  comp[%d] dim=%s : k=%s%s" % (idx, P.dimension(), k,
              "  (geometric)" if k not in (None, 0) else "  (reducible/degenerate)"))


def dim_cell(o, n, exps, label):
    """Rigorous existence: ideal dimension; dim<0 <=> V(I) empty (no rep at all)."""
    _, _, _, _, _, I, _ = _build(o, n, exps)
    d = I.dimension()
    print("%-26s : ideal dim = %d  (%s)" % (label, d, "EMPTY" if d < 0 else "nonempty"))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "dim":
        dim_cell(5, 3, [0, 1, 4], "SL3 o5 {1,z5,z5^4}")
        dim_cell(6, 3, [0, 1, 5], "SL3 o6 {1,z6,z6^5}")
    else:
        exact_k(3, 3, [0, 1, 2], "SL3 o3 {1,w,w2} expect k=4")
        exact_k(4, 3, [0, 1, 3], "SL3 o4 {1,i,-i} expect k=3")
