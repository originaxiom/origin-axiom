"""B398 S1+S2 -- the spectral theorem and cross-pair claims, exactly from banked data."""
import json, os
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "..", "B367_value_map", "step0_tables.json")))

def smat(pair, o1, o2):
    """the sqrt-15 component matrix s[K1][K2] (dense, zeros where absent)."""
    d = T[pair]
    S = [[Fr(0)]*o2 for _ in range(o1)]
    for k, v in d.items():
        a, b = map(int, k.split(","))
        S[a][b] = Fr(v[3])
    return S

def gram(cols):
    n = len(cols)
    return [[sum(x*y for x, y in zip(cols[i], cols[j])) for j in range(n)] for i in range(n)]

def eig2(G):
    tr = G[0][0] + G[1][1]; det = G[0][0]*G[1][1] - G[0][1]*G[1][0]
    disc = tr*tr - 4*det
    import math
    r = Fr(math.isqrt(disc.numerator), math.isqrt(disc.denominator))
    assert r*r == disc, "discriminant not a perfect square"
    return ((tr+r)/2, (tr-r)/2)

res = {}

# ---- S1: pair (1,2), o1=20, o2=12 ----
S = smat("1,2", 20, 12)
# sector blocks: escape K1 in {0,4}? handoff says escape (K1 in {0,4}, K2 in {4,8});
# separated (K1 in {6,14}, K2 in {2,10})
def block(K1s, K2s): return [[S[a][b] for b in K2s] for a in K1s]
esc = block((0,4),(4,8)); sep = block((6,14),(2,10))
def antipair(B):
    a = B[0][0]
    return (B[0][1] == -a and B[1][0] == -a and B[1][1] == a, abs(a))
e_ok, e_a = antipair(esc); s_ok, s_a = antipair(sep)
res["S1_blocks"] = dict(escape_antipaired=e_ok, escape_a=str(e_a),
                        separated_antipaired=s_ok, separated_a=str(s_a),
                        doublet_sigma=str(2*e_a))
print("S1 blocks:", res["S1_blocks"])

# F4 Gram: K1 support {1,5,9,11,15,19}, K2 columns {1,5}
K1F = (1,5,9,11,15,19)
v1 = [S[a][1] for a in K1F]; v5 = [S[a][5] for a in K1F]
G = gram([v1, v5])
lam = eig2(G)
res["S1_F4"] = dict(G=[[str(x) for x in row] for row in G],
                    eigs=[str(lam[0]), str(lam[1])],
                    ratio=str(lam[1]/lam[0]),
                    int480=dict(norm=str(G[0][0]*480*480), inner=str(G[0][1]*480*480)))
print("S1 F4 Gram:", res["S1_F4"])

# the fork: the full-form spectrum's rational pair ratio (banked {1/768, 23/19200})
res["S1_fork"] = dict(full_rational_ratio=str(Fr(23,19200)/Fr(1,768)),
                      F4_restricted_ratio=str(lam[1]/lam[0]))
print("S1 fork:", res["S1_fork"])

# ---- S2: cross-pair ----
# (2,3): o1=12, o2=6; three K2 columns {0,2,4}
S23 = smat("2,3", 12, 6)
cols = [[S23[a][b] for a in range(12)] for b in (0,2,4)]
G3 = gram(cols)
norms = {str(G3[i][i]) for i in range(3)}
inners = {str(G3[i][j]) for i in range(3) for j in range(3) if i != j}
res["S2_23"] = dict(norms=sorted(norms), inners=sorted(inners))
# the Z/3 Gram: eigenvalues n-i (doublet) and n+2i; "F4 ratio" 1/3 claim: check eigs
n = G3[0][0]; i_ = G3[0][1]
res["S2_23"]["eig_ratio_claim"] = str((n - i_) / (n + 2*i_)) if (n + 2*i_) != 0 else "div0"
print("S2 (2,3):", res["S2_23"])

# (3,4): o1=6, o2=20; the handoff claims eigenvalues {7,5}/2304
S34 = smat("3,4", 6, 20)
# use its two nonzero-norm K2 columns... find columns with nonzero content:
colsB = [(b, [S34[a][b] for a in range(6)]) for b in range(20)]
nz = [(b, c) for b, c in colsB if any(x != 0 for x in c)]
# Gram of the distinct column pair used by the handoff: try the first two independent
from itertools import combinations
found = None
for (b1, c1), (b2, c2) in combinations(nz, 2):
    G2 = gram([c1, c2])
    if G2[0][1] == 0 and G2[0][0] == G2[1][1]: continue
    try:
        l1, l2 = eig2(G2)
    except AssertionError:
        continue
    if {l1, l2} == {Fr(7,2304), Fr(5,2304)}:
        found = (b1, b2); break
res["S2_34"] = dict(seven_five_found=bool(found), columns=list(found) if found else None,
                    n_nonzero_cols=len(nz))
print("S2 (3,4):", res["S2_34"])

# (2,4) rank 1; darks empty
S24 = smat("2,4", 12, 20)
rows24 = [r for r in S24 if any(x != 0 for x in r)]
def rank_exact(M):
    M = [row[:] for row in M]; r = 0
    if not M: return 0
    m, ncol = len(M), len(M[0])
    for c in range(ncol):
        piv = next((i for i in range(r, m) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]; M[r] = [x/pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [x - f*y for x, y in zip(M[i], M[r])]
        r += 1
    return r
res["S2_ranks"] = {p: rank_exact([row for row in smat(p, o1, o2) if any(x != 0 for x in row)])
                   for p, o1, o2 in (("1,2",20,12),("2,3",12,6),("2,4",12,20),("3,4",6,20),("1,3",20,6),("1,4",20,20))}
print("S2 ranks:", res["S2_ranks"])
json.dump(res, open(os.path.join(HERE, "s1_s2.json"), "w"), indent=1)
print("DONE")
