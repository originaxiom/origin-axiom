"""P-229, first item: the SM seat's W23 (the record's E8 frames on the weave's fibre give at most two complete generations)
checked on main by its own representation-ring computation, from W23's rule as recorded (NOTE.md, W23), not its script.
Blocks: the four characters chi_p of Q8/{+-1} (p in (Z/2)^2) and the four spin doublets chi_p (x) rho_Q (rho_Q: a -> i,
b -> j). Index (W22, verified on main in B1606): a spin-doublet block counts +1, a character 0, additively. Every bundle of
rank n with trivial determinant built from blocks; the matter: E6 27 (x) V (n = 3), SO(10) 16 (x) V (n = 4), SU(5)
10 (x) W and 5bar (x) Lambda^2 W (n = 5). The decomposition of tensor and exterior products into blocks is computed with
the actual Q8 matrices (characters), not assumed."""
import itertools, json, numpy as np
I2 = np.eye(2, dtype=complex); qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]], dtype=complex); qk = qi @ qj
Q8 = [s * M for s in (1, -1) for M in (I2, qi, qj, qk)]
def word_to_pair(M):                     # the class of M in Q8/{+-1} = (Z/2)^2: which of 1, i, j, k
    for idx, B in enumerate((I2, qi, qj, qk)):
        if np.allclose(M, B) or np.allclose(M, -B): return idx
P = [(0, 0), (1, 0), (0, 1), (1, 1)]                       # i <-> a's parity, j <-> b's parity
cls = {0: (0, 0), 1: (1, 0), 2: (0, 1), 3: (1, 1)}
def chi(p, M):                                             # chi_p(g) = (-1)^{p . class(g)}
    c = cls[word_to_pair(M)]; return (-1) ** (p[0] * c[0] + p[1] * c[1])
# a representation = its character on the 8 elements; blocks
blocks = {("chr", p): np.array([chi(p, M) for M in Q8], complex) for p in P}
blocks.update({("dbl", p): np.array([chi(p, M) * np.trace(M) for M in Q8], complex) for p in P})
irr = list(blocks.items())
def decompose(ch):                                         # multiplicities by inner product (Q8's irreducibles: 4 chars + rho_Q)
    out = {}
    for k, c in [(k, c) for k, c in irr if k[0] == "chr"] + [(("dbl", (0, 0)), blocks[("dbl", (0, 0))])]:
        m = np.vdot(c, ch).real / 8
        if abs(m) > 1e-9: out[k] = int(round(m))
    return out
# the four doublets are all isomorphic to rho_Q as Q8-representations (chi_p (x) rho_Q = rho_Q, B1606's D1): check it
dbl_iso = all(np.allclose(blocks[("dbl", p)], blocks[("dbl", (0, 0))]) for p in P)
def index(ch):                                             # W22: +1 per doublet (rank 2), 0 per character
    return decompose(ch).get(("dbl", (0, 0)), 0)
def det_trivial(bundle):                                   # det of a direct sum: product of the blocks' determinants
    tot = (0, 0)
    for kind, p in bundle:
        if kind == "chr": tot = ((tot[0] + p[0]) % 2, (tot[1] + p[1]) % 2)
        # det(chi (x) rho_Q) = chi^2 det rho_Q = 1
    return tot == (0, 0)
def char_of(bundle): return sum(blocks[b] for b in bundle)
def wedge2(ch):                                            # Lambda^2 character: (chi(g)^2 - chi(g^2))/2
    sq = np.array([0] * 8, complex)
    for n_, M in enumerate(Q8):
        M2 = M @ M; j = next(k for k, N in enumerate(Q8) if np.allclose(M2, N)); sq[n_] = ch[j]
    return (ch * ch - sq) / 2
def bundles(n):
    keys = list(blocks)
    out = set()
    for r in range(0, n + 1):
        for combo in itertools.combinations_with_replacement(keys, r):
            rank = sum(1 if k[0] == "chr" else 2 for k in combo)
            if rank == n and det_trivial(combo): out.add(combo)
    return sorted(out)
res = {"doublets_all_isomorphic_to_rho_Q": bool(dbl_iso)}
res["E6_27xV_n3"] = sorted({index(char_of(b)) for b in bundles(3)})
res["SO10_16xV_n4"] = sorted({index(char_of(b)) for b in bundles(4)})
res["SU5_(10xW,5barxL2W)_n5"] = sorted({(index(char_of(b)), index(wedge2(char_of(b)))) for b in bundles(5)})
res["counts_of_bundles"] = {n: len(bundles(n)) for n in (3, 4, 5)}
res["max_complete_generations"] = max([x for x in res["E6_27xV_n3"]] + [x for x in res["SO10_16xV_n4"]] +
                                      [min(a, b) for a, b in res["SU5_(10xW,5barxL2W)_n5"]])
res["holds_as_recorded"] = (res["E6_27xV_n3"] == [0, 1] and res["SO10_16xV_n4"] == [0, 1, 2]
                            and res["SU5_(10xW,5barxL2W)_n5"] == [(0, 0), (1, 3), (2, 2)])
import pathlib; json.dump(res, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
