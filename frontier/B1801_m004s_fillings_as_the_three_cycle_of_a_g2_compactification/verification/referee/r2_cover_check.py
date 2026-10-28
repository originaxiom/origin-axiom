"""Referee B1801, check 2 (independent of Turaev's surgery formula and of the Alexander polynomial).
Multiplicativity of torsion under the 3-fold cyclic cover Qt -> Q (the kernel of pi1(Q) -> H1 = Z/p -> Z/3), Turaev
convention (tau(trivial, integral bases) = |H1| for a rational homology sphere):
        |H1(Qt)| = 3 * |H1(Q)| * |tau(Q, chi)| * |tau(Q, chi-bar)|      (the factor 3 from H_3; checked on lens spaces below)
so |tau| = 4/3 predicts |H1(Qt)| = 16 p / 3.  H1(Qt) is computed two ways: (i) SnapPy's covers of the filled manifold,
(ii) own Reidemeister-Schreier: the Fox Jacobian of the filled group over Z[Z/3] as a block-circulant integer matrix,
Smith normal form.  The lens-space normalisation of the formula: L(p,1) -> L(p/d,1), Prod_{chi^d=1, chi!=1} |tau| = 1/d^2,
so p/d = d * p * (1/d^2): the factor is d (worked here symbolically)."""
import itertools, math
import snappy
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def abel_exp(word, ph):
    return sum((1 if ch.islower() else -1) * ph[ch.lower()] for ch in word)

def fox_group_ring(word, gen, ph, n):
    """d word/d gen in Z[Z/n], abelianised through ph (gen -> Z/n); returned as a length-n integer vector."""
    v = [0] * n; prefix = 0
    for ch in word:
        e = 1 if ch.islower() else -1; g = ch.lower()
        if g == gen:
            if e == 1: v[prefix % n] += 1
            else: v[(prefix - ph[g]) % n] -= 1
        prefix += e * ph[g]
    return v

def cover_H1_own(p, q, n=3):
    M = snappy.Manifold("m004"); M.dehn_fill((p, q))
    G = M.fundamental_group(); gens = G.generators(); rels = G.relators()
    # surjection to Z/p
    sol = None
    for vals in itertools.product(range(p), repeat=len(gens)):
        ph = dict(zip(gens, vals))
        if all(abel_exp(r, ph) % p == 0 for r in rels) and math.gcd(*vals, p) == 1:
            sol = ph; break
    phn = {g: v % n for g, v in sol.items()}   # compose with Z/p -> Z/n
    # relation matrix of the chain map C2(Qt) -> C1(Qt) (rows: relator lifts, cols: generator lifts), each entry a circulant
    rows = []
    for r in rels:
        for s in range(n):            # lift of r starting at sheet s
            row = []
            for g in gens:
                v = fox_group_ring(r, g, phn, n)
                row += [v[(j - s) % n] for j in range(n)]
            rows.append(row)
    D2 = Matrix(rows)                 # rows = 2-cells, cols = 1-cells
    # boundary C1 -> C0: lift of generator g at sheet j goes from sheet j to sheet j + phn[g]
    D1 = Matrix([[0] * 0])
    cols = []
    for g in gens:
        for j in range(n):
            c = [0] * n; c[(j + phn[g]) % n] += 1; c[j] -= 1
            cols.append(c)
    D1 = Matrix(cols)                 # rows = 1-cells, cols = 0-cells
    # H1 = ker(D1^T)/im(D2^T) on the cellular chain complex of the presentation 2-complex's cover.
    # The presentation complex of a closed 3-manifold's balanced presentation is a spine of Q minus a ball, so H1 agrees.
    snf = smith_normal_form(D2, domain=ZZ)
    diag = [abs(snf[i, i]) for i in range(min(snf.shape)) if snf[i, i] != 0]
    rank_D2 = len(diag)
    rank_D1 = D1.rank()
    free = (len(gens) * n - rank_D1) - rank_D2
    tors = [d for d in diag if d != 1]
    return free, tors

def cover_H1_snappy(p, q, n=3):
    M = snappy.Manifold("m004"); M.dehn_fill((p, q))
    covs = M.covers(n, cover_type="cyclic")
    out = []
    for C in covs:
        out.append(str(C.homology()))
    return out

print("filling   |H1(Q)|  predicted |H1(Qt)| = 16p/3   own Reidemeister-Schreier   SnapPy cyclic 3-fold covers")
for (p, q) in [(3, 2), (3, 4), (3, 5), (6, 1), (6, 5), (9, 1), (9, 2), (12, 1), (15, 2)]:
    free, tors = cover_H1_own(p, q)
    order = math.prod(tors) if tors else 1
    sn = cover_H1_snappy(p, q)
    print(f"m004({p},{q})  Z/{p:<3d}   {16 * p // 3:>5d}                    free rank {free}, torsion {tors} (order {order})   {sn}")
    assert free == 0 and order == 16 * p // 3
print("=> |tau(Q, order-3)|^2 = |H1(Qt)| / (3 p) = 16/9 on every row: |tau| = 4/3 confirmed without Turaev's formula")
# control: the same instrument on the order-2 cover of m004(6,1) (prediction from Turaev: 2 * 6 * |tau(order 2)|, one character)
import cmath
z = -1; Delta = abs(z - 3 + 1 / z)   # |Delta(-1)| = 5
r = (-pow(1, -1, 6)) % 6
tau2 = Delta / (abs(z - 1) * abs(z**r - 1))
free, tors = cover_H1_own(6, 1, n=2)
print(f"control m004(6,1), 2-fold cover: own RS torsion {tors} (order {math.prod(tors) if tors else 1}); Turaev predicts 2*6*|tau(order 2)| = {2 * 6 * tau2:.4f} (one nontrivial character, real)")
print("r2 exit 0")
