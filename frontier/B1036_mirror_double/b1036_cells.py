"""B1036 -- THE MIRROR-DOUBLE SYMMETRIC TEXTURE (sealed a10ae240 pre-compute).

Reuses B575's exact build through stage 4 (exec; the banked pattern of B632/B639),
B637's banked longitude LONG = "abABaaBAbA", and the design's per-block MV reduction:
h1(dbl; Sym^m) = 3 - rank(r_m) for the 27's positive blocks. V5 runs the adjoint blocks
(BLOCK_DATA) for the additivity theorem's falsifier h1(M; ad) = 6.

Banked-number gates EVERYWHERE (B961's law): no export is used before reproducing a
banked value. All exact over K = Q(omega); no conjugation appears anywhere in the plain
double (the B647 hazard never arises); rref pivots used as COLUMN indices only.
"""
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = os.path.join(HERE, "..", "B575_bridge_obstruction", "l51_obstruction.py")

src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 5")
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time()
print("executing B575 stages 0-4 (exact build + holonomy + adjoint blocks)...", flush=True)
exec(compile(src[:cut], B575, "exec"), ns)
print(f"B575 prefix done in {time.time()-t0:.1f}s", flush=True)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
REL = ns["REL"]
LET = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
meye, mzero, madd, mmul, mscale, msub = (ns[k] for k in
    ("meye", "mzero", "madd", "mmul", "mscale", "msub"))
mzero_p = ns["mzero_p"]
nullspace, rref = ns["nullspace"], ns["rref"]
h_pr = ns["h_pr"]
BLOCK_DATA = ns["BLOCK_DATA"]

LONG = "abABaaBAbA"                     # banked longitude (B637/B639)
MER = "a"                               # the meridian


# ---------------------------------------------------------------- generic exact helpers
def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


def word_matrix(word, lets):
    P = meye(len(next(iter(lets.values()))))
    for ch in word:
        P = mmul(P, lets[ch])
    return P


def word_cocycle(word, lets, za, zb):
    """z(word) from z(a)=za, z(b)=zb via z(uv) = z(u) + rho(u) z(v); z(x^-1) = -rho(x)^-1 z(x)."""
    n = len(za)
    z = [K0] * n
    P = meye(n)
    for ch in word:
        if ch == 'a':
            step = za
        elif ch == 'b':
            step = zb
        elif ch == 'A':
            step = [K0 - x for x in mat_vec(lets['A'], za)]
        else:
            step = [K0 - x for x in mat_vec(lets['B'], zb)]
        z = [z[i] + x for i, x in enumerate(mat_vec(P, step))]
        P = mmul(P, lets[ch])
    return z


def fox_h1(lets, n):
    """(Z1 basis, B1 basis, h0, h1) for the two-generator one-relator group, exact."""
    La = mzero(n, n)
    Lb = mzero(n, n)
    Pi = meye(n)
    for ch in REL:
        if ch == 'a':
            term, tgt, sgn = meye(n), 'a', 1
        elif ch == 'A':
            term, tgt, sgn = lets['A'], 'a', -1
        elif ch == 'b':
            term, tgt, sgn = meye(n), 'b', 1
        else:
            term, tgt, sgn = lets['B'], 'b', -1
        term = mmul(Pi, term)
        if sgn < 0:
            term = mscale(K(-1), term)
        if tgt == 'a':
            La = madd(La, term)
        else:
            Lb = madd(Lb, term)
        Pi = mmul(Pi, lets[ch])
    big = [[La[i][j] for j in range(n)] + [Lb[i][j] for j in range(n)] for i in range(n)]
    Z1 = nullspace(big)                                    # cocycles (za|zb), dim 2n - rank
    # coboundaries: v -> ((a-1)v, (b-1)v)
    Bgen = []
    for j in range(n):
        v = [K1 if t == j else K0 for t in range(n)]
        Bgen.append([x - v[i] for i, x in enumerate(mat_vec(lets['a'], v))] +
                    [x - v[i] for i, x in enumerate(mat_vec(lets['b'], v))])
    _, pivB = rref([row[:] for row in Bgen])
    # h0 = n - rank(B) since B1 ~ V / V^inv
    h0 = n - len(pivB)
    h1 = len(Z1) - len(pivB)
    return Z1, Bgen, h0, h1


def inv_word(w):
    return w[::-1].swapcase()


def quotient_rank(vectors, modulo):
    """rank of span(vectors) in V / span(modulo), exact."""
    if not vectors:
        return 0
    base = [row[:] for row in modulo]
    _, pivm = rref([row[:] for row in base])
    r0 = len(pivm)
    _, piv = rref([row[:] for row in (modulo + vectors)])
    return len(piv) - r0


# ---------------------------------------------------------------- the 27's three blocks
print("\n[27-side] building the three sl2-blocks of the 27...", flush=True)
eig = {}
for t in range(-30, 31):
    rows = [[h_pr[i][j] - (K(t) if i == j else K0) for j in range(27)] for i in range(27)]
    ker = nullspace(rows)
    if ker:
        eig[t] = ker
# peel strings exactly as B632: tops 16, 8, 0
TOPS27 = [16, 8, 0]


# module route: the sl2 acts on the 27 through the PRINCIPAL matrices inside gl(27):
# e-action matrix = ns['e_pr'] acting BY MATRIX MULT? e_pr IS a 27x27 matrix (the principal
# nilpotent in gl(27)). Verified by gate below.
e27, f27 = ns["e_pr"], ns["f_pr"]
blocks27 = {}
for top in TOPS27:
    # highest vector: solve (h - top) v = 0 AND e v = 0 jointly (the top may be a
    # combination inside a multi-string weight space -- the first draft filtered basis
    # vectors and found none at V(8); kept as the lesson)
    rows = [[h_pr[i][j] - (K(top) if i == j else K0) for j in range(27)]
            for i in range(27)] + [[e27[i][j] for j in range(27)] for i in range(27)]
    hi = nullspace(rows)
    assert len(hi) == 1, f"27-block V({top}): highest multiplicity {len(hi)}"
    chain = [hi[0]]
    for _ in range(top):
        chain.append(mat_vec(f27, chain[-1]))
    assert not all(x.is_zero() for x in chain[-1]), f"V({top}) short"
    blocks27[top] = chain
assert sum(len(c) for c in blocks27.values()) == 27
print(f"  blocks: dims {[len(blocks27[t]) for t in TOPS27]} (17, 9, 1 expected)", flush=True)
assert [len(blocks27[t]) for t in TOPS27] == [17, 9, 1], "27 block dims wrong"

Solver = ns["Solver"]
flat_id = lambda v: v


def restrict_letters(chain):
    d = len(chain)
    bs = Solver([list(v) for v in chain])
    acts = {}
    for ch, M in LET.items():
        cols = [bs.coords(list(mat_vec(M, chain[j]))) for j in range(d)]
        acts[ch] = [[cols[j][i] for j in range(d)] for i in range(d)]
    return acts


# ---------------------------------------------------------------- V2: per-block MV
print("\n[V2] the Mayer-Vietoris ranks, per 27-block:", flush=True)
results = {}
total_dbl = 0
for top in TOPS27:
    d = len(blocks27[top])
    lets = restrict_letters(blocks27[top]) if d < 27 else dict(LET)
    Z1, Bgen, h0, h1 = fox_h1(lets, d)
    print(f"  V({top}) dim {d}: h0(M) = {h0}, h1(M) = {h1}", flush=True)
    if top > 0:
        assert h0 == 0 and h1 == 1, f"banked-number gate FAILED at V({top})"
    else:
        assert h0 == 1 and h1 == 1, f"banked-number gate FAILED at V(0)"
    # peripheral matrices + gates
    Pmu = word_matrix(MER, lets)
    Plam = word_matrix(LONG, lets)
    assert mzero_p(msub(mmul(Pmu, Plam), mmul(Plam, Pmu))), "peripheral not commuting"
    # H^1(T^2): Z1_T = {(u,v): (Plam-1)u = (Pmu-1)v}; B1_T = {((Pmu-1)w, (Plam-1)w)}
    n = d
    Mlam = msub(Plam, meye(n))
    Mmu = msub(Pmu, meye(n))
    rows = [[(Mlam[i][j] if j < n else (K0 - Mmu[i][j - n])) for j in range(2 * n)]
            for i in range(n)]
    Z1T = nullspace(rows)
    B1T = []
    for j in range(n):
        w = [K1 if t == j else K0 for t in range(n)]
        B1T.append(list(mat_vec(Mmu, w)) + list(mat_vec(Mlam, w)))
    _, pivBT = rref([row[:] for row in B1T])
    h0T = len(nullspace([[Mmu[i][j] for j in range(n)] for i in range(n)] +
                        [[Mlam[i][j] for j in range(n)] for i in range(n)]))
    h1T = len(Z1T) - len(pivBT)
    print(f"    T^2: h0 = {h0T}, h1 = {h1T}", flush=True)
    # restrictions of the M-side and Mbar-side cocycles
    restr = []
    for z in Z1:
        za, zb = list(z[:d]), list(z[d:])
        zmu = word_cocycle(MER, lets, za, zb)
        zlam = word_cocycle(LONG, lets, za, zb)
        restr.append(zmu + zlam)                                   # M-copy
    # Mbar side: THE ORIENTATION DOUBLE GLUES BY THE IDENTITY on the boundary
    # (the first draft used (mu,lambda) -> (mu,lambda^{-1}) -- a different manifold;
    # the impossible rank(r)=10 / negative h1 caught it, kept as the lesson). With the
    # identity gluing the Mbar restriction is the SAME map; the MV difference
    # (x,y) -> r(x) - r(y) has image = image(r).
    for z in Z1:
        za, zb = list(z[:d]), list(z[d:])
        zmu = word_cocycle(MER, lets, za, zb)
        zlam = word_cocycle(LONG, lets, za, zb)
        restr.append(zmu + zlam)
    # compatibility gate: every restriction satisfies (rho_lam - 1)u = (rho_mu - 1)v
    for vec in restr:
        u, v = vec[:n], vec[n:]
        lhs = mat_vec(Mlam, u)
        rhs = mat_vec(Mmu, v)
        assert all((lhs[i] - rhs[i]).is_zero() for i in range(n)), \
            "restriction not a T^2-cocycle -- convention bug"
    rk = quotient_rank(restr, B1T)
    h1_dbl = (h0T - 0 - 0 + 0) + 2 * h1 - rk if top > 0 else None
    if top > 0:
        # exact MV bookkeeping for m>0: 0->H0(dbl)->0->H0(T)->H1(dbl)->H1+H1->H1(T)...
        # H0(dbl) = 0; contribution of H0(T) = h0T; so:
        h1_dbl = h0T + 2 * h1 - rk
    else:
        # trivial block: H0(dbl)=1 (constants); 0->1->1+1->1->H1(dbl)->1+1->2->...
        # exactness: ker(H0M+H0Mbar->H0T) = 1 (diagonal) => image dim 1 => H0T->H1(dbl) has image h0T-1
        h1_dbl = (h0T - 1) + 2 * h1 - rk
    results[top] = dict(h1M=h1, h0T=h0T, h1T=h1T, rank_r=rk, h1_dbl=h1_dbl)
    total_dbl += h1_dbl
    print(f"    rank(r) = {rk}  =>  h1(dbl; V({top})) = {h1_dbl}", flush=True)

print(f"\n[V4] h1(dbl; 27) = {total_dbl}  (solo banked = 3)", flush=True)


# ---------------------------------------------------------------- V5: the adjoint falsifier
print("\n[V5] h1(M; ad) via the six banked adjoint blocks:", flush=True)
h1_ad = 0
per = {}
for m, bd in sorted(BLOCK_DATA.items()):
    Z1, Bgen, h0, h1 = fox_h1(bd['acts'], bd['d'])
    per[m] = h1
    h1_ad += h1
    print(f"  ad block m={m} (dim {bd['d']}): h1 = {h1}", flush=True)
print(f"  TOTAL h1(M; ad) = {h1_ad}   (the additivity theorem predicts 6)", flush=True)

print("\n==== B1036 core numbers done ====", flush=True)
print(f"V4: h1(dbl;27) = {total_dbl} vs solo 3;  V5: h1(M;ad) = {h1_ad} vs predicted 6",
      flush=True)
