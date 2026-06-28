"""B271 reproducibility -- the amphichiral tau (= E6 outer automorphism) decomposition (run with sage-python).
Verifies: tau = (+1 on f4, -1 on the 26) is a genuine Lie automorphism of e6, with fixed subalgebra f4 (exponents
{1,5,7,11}, dim 52) and -1 eigenspace the 26 = e6/f4 (exponents {4,8}, dim 26). The -1 eigenspace IS B265's
E6-Zariski-dense direction set. Output hard-coded into walls_3_4.py."""
from sage.all import LieAlgebra, QQ, matrix, vector, identity_matrix

L = LieAlgebra(QQ, cartan_type=['E', 6]); dim = L.dimension(); idx = list(L.cartan_type().index_set())
Hh = {i: L.bracket(L.e(i), L.f(i)) for i in idx}
A = L.cartan_type().cartan_matrix(); c = 2 * A.inverse() * vector(QQ, [1] * len(idx))
e = sum(L.e(i) for i in idx)
h = sum(c[k] * Hh[idx[k]] for k in range(len(idx)))
f = sum(c[k] * L.f(idx[k]) for k in range(len(idx)))
B = list(L.basis())
adh = matrix(QQ, [L.bracket(h, b).to_vector() for b in B]).transpose()
ade = matrix(QQ, [L.bracket(e, b).to_vector() for b in B]).transpose()
adf = matrix(QQ, [L.bracket(f, b).to_vector() for b in B]).transpose()
Ke = ade.right_kernel()


def module(m):
    hw = (adh - 2 * m * identity_matrix(QQ, dim)).right_kernel().intersection(Ke).basis()[0]
    vecs, cur = [hw], hw
    for _ in range(2 * m):
        cur = adf * cur; vecs.append(cur)
    return matrix(QQ, vecs)


def span(ms):
    rows = []
    for m in ms:
        rows += list(module(m).rows())
    return matrix(QQ, rows)


def _in(vec, M):
    return M.rank() == M.stack(vec).rank()


def bracket_in(S1, S2, T):
    for r1 in S1.rows():
        x = sum(r1[i] * B[i] for i in range(dim))
        for r2 in S2.rows():
            y = sum(r2[i] * B[i] for i in range(dim))
            if not _in(L.bracket(x, y).to_vector(), T):
                return False
    return True


if __name__ == "__main__":
    F4, P26 = span([1, 5, 7, 11]), span([4, 8])
    print("dim f4 (exp 1,5,7,11) =", F4.rank(), "  dim 26 (exp 4,8) =", P26.rank())
    print("[f4,f4]<=f4:", bracket_in(F4, F4, F4),
          " [f4,26]<=26:", bracket_in(F4, P26, P26),
          " [26,26]<=f4:", bracket_in(P26, P26, F4))
    print("=> tau (+1 on f4, -1 on 26) is a Lie automorphism; fixed=f4, broken=26={4,8}=B265 E6-dense dirs.")
