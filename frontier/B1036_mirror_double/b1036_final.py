"""B1036 -- FINAL CONSOLIDATED RUN (sealed a10ae240). One script, one output, the record.

V1  control: seam-pairing gauge invariance (passable, and passed) -- after two sealed
    HALTs on wrong routes (the 3-relator chain; the per-side scalar contraction), both
    kept on disk as the process record. The per-side scalar vacuity IS O2 restated.
V2  the MV route per 27-block: h1(dbl) = h0T + 2 h1M - rank(r), identity gluing.
V3  the seam-sector symmetric pairing: the double classes' DIRECT T^2 restrictions,
    cup through the Bth-contracted torus form, support-only.
V4  the multiplicity read: total h1(dbl; 27) vs solo 3.
V5  h1(M; ad) vs the additivity theorem's 6.
Cross-gate: the double-presentation Fox h1 must equal the MV h1 per block."""
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = os.path.join(HERE, "..", "B575_bridge_obstruction", "l51_obstruction.py")
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 5")
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time()
print("B575 stages 0-4...", flush=True)
exec(compile(src[:cut], B575, "exec"), ns)
print(f"prefix {time.time()-t0:.1f}s", flush=True)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
meye, mzero, madd, mmul, mscale, msub = (ns[k] for k in
    ("meye", "mzero", "madd", "mmul", "mscale", "msub"))
mzero_p = ns["mzero_p"]
nullspace, rref = ns["nullspace"], ns["rref"]
h_pr = ns["h_pr"]
Solver = ns["Solver"]
e27, f27 = ns["e_pr"], ns["f_pr"]
BLOCK_DATA = ns["BLOCK_DATA"]
REL = ns["REL"]
LONG = "abABaaBAbA"
MER = "a"
GENS = "abd"


def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


def inv_word(w):
    return w[::-1].swapcase()


R1, R2 = REL, REL.replace('b', 'd').replace('B', 'D')
R3 = LONG + inv_word(LONG.replace('b', 'd').replace('B', 'D'))
RELS = [R1, R2, R3]

TOPS27 = [16, 8, 0]
blocks27 = {}
for top in TOPS27:
    rows = [[h_pr[i][j] - (K(top) if i == j else K0) for j in range(27)]
            for i in range(27)] + [[e27[i][j] for j in range(27)] for i in range(27)]
    hi = nullspace(rows)
    assert len(hi) == 1
    chain = [hi[0]]
    for _ in range(top):
        chain.append(mat_vec(f27, chain[-1]))
    blocks27[top] = chain
assert [len(c) for c in blocks27.values()] == [17, 9, 1]


def restrict(chain):
    d = len(chain)
    bs = Solver([list(v) for v in chain])
    out = {}
    for ch, M in {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}.items():
        cols = [bs.coords(list(mat_vec(M, chain[j]))) for j in range(d)]
        out[ch] = [[cols[j][i] for j in range(d)] for i in range(d)]
    return out


def build_Btheta(d):
    B = [[K0] * d for _ in range(d)]
    c = K1
    for i in range(d):
        B[i][d - 1 - i] = c
        c = K0 - c
    return B


def fox_M(lets, n):
    La = mzero(n, n); Lb = mzero(n, n); Pi = meye(n)
    for ch in REL:
        if ch == 'a':   term, tgt, sgn = meye(n), 'a', 1
        elif ch == 'A': term, tgt, sgn = lets['A'], 'a', -1
        elif ch == 'b': term, tgt, sgn = meye(n), 'b', 1
        else:           term, tgt, sgn = lets['B'], 'b', -1
        term = mmul(Pi, term)
        if sgn < 0: term = mscale(K(-1), term)
        if tgt == 'a': La = madd(La, term)
        else:          Lb = madd(Lb, term)
        Pi = mmul(Pi, lets[ch])
    big = [[La[i][j] for j in range(n)] + [Lb[i][j] for j in range(n)] for i in range(n)]
    Z1 = nullspace(big)
    Bgen = []
    for j in range(n):
        v = [K1 if t == j else K0 for t in range(n)]
        Bgen.append([x - v[i] for i, x in enumerate(mat_vec(lets['a'], v))] +
                    [x - v[i] for i, x in enumerate(mat_vec(lets['b'], v))])
    _, pivB = rref([row[:] for row in Bgen])
    h0 = n - len(pivB)
    h1 = len(Z1) - len(pivB)
    return Z1, Bgen, h0, h1


def word_cocycle(word, lets, vals):
    n = len(next(iter(vals.values())))
    z = [K0] * n
    P = meye(n)
    for ch in word:
        low = ch.lower()
        if ch.isupper():
            step = [K0 - x for x in mat_vec(lets[ch], vals[low])]
        else:
            step = vals[low]
        z = [z[i] + x for i, x in enumerate(mat_vec(P, step))]
        P = mmul(P, lets[ch])
    return z


def word_matrix(word, lets):
    P = meye(len(next(iter(lets.values()))))
    for ch in word:
        P = mmul(P, lets[ch])
    return P


def quotient_rank(vectors, modulo):
    if not vectors:
        return 0
    r0 = len(rref([row[:] for row in modulo])[1]) if modulo else 0
    return len(rref([row[:] for row in (list(modulo) + list(vectors))])[1]) - r0


def fox_dbl(lets3, n):
    def deriv(word):
        L = {g: mzero(n, n) for g in GENS}
        Pi = meye(n)
        for ch in word:
            low = ch.lower()
            if ch.isupper():
                term = mscale(K(-1), mmul(Pi, lets3[ch]))
            else:
                term = mmul(Pi, meye(n))
            L[low] = madd(L[low], term)
            Pi = mmul(Pi, lets3[ch])
        return L, Pi
    rows_all = []
    for w in RELS:
        L, Pi = deriv(w)
        assert mzero_p(msub(Pi, meye(n))), "relator fails"
        rows_all += [[L['a'][i][j] for j in range(n)] +
                     [L['b'][i][j] for j in range(n)] +
                     [L['d'][i][j] for j in range(n)] for i in range(n)]
    Z1 = nullspace(rows_all)
    Bgen = []
    for j in range(n):
        v = [K1 if t == j else K0 for t in range(n)]
        Bgen.append([x - v[i] for i, x in enumerate(mat_vec(lets3['a'], v))] +
                    [x - v[i] for i, x in enumerate(mat_vec(lets3['b'], v))] +
                    [x - v[i] for i, x in enumerate(mat_vec(lets3['d'], v))])
    _, pivB = rref([row[:] for row in Bgen])
    h1 = len(Z1) - len(pivB)
    return Z1, Bgen, h1


print("\n== V2 (MV) + cross-gate (double-Fox) + V3 (seam pairing) per block ==", flush=True)
tot_dbl = 0
seam_tables = {}
for top in TOPS27:
    chain = blocks27[top]
    n = len(chain)
    lets = restrict(chain)
    Z1, Bgen, h0, h1 = fox_M(lets, n)
    exp_h0, exp_h1 = (0, 1) if top > 0 else (1, 1)
    assert (h0, h1) == (exp_h0, exp_h1), f"banked gate V({top})"
    Pmu, Plam = word_matrix(MER, lets), word_matrix(LONG, lets)
    assert mzero_p(msub(mmul(Pmu, Plam), mmul(Plam, Pmu)))
    Mmu, Mlam = msub(Pmu, meye(n)), msub(Plam, meye(n))
    Z1T = nullspace([[Mlam[i][j] if j < n else (K0 - Mmu[i][j - n])
                      for j in range(2 * n)] for i in range(n)])
    B1T = []
    for j in range(n):
        w = [K1 if t == j else K0 for t in range(n)]
        B1T.append(list(mat_vec(Mmu, w)) + list(mat_vec(Mlam, w)))
    h0T = len(nullspace([[Mmu[i][j] for j in range(n)] for i in range(n)] +
                        [[Mlam[i][j] for j in range(n)] for i in range(n)]))
    h1T = len(Z1T) - len(rref([r[:] for r in B1T])[1])
    restr = []
    for z in Z1:
        vals = {'a': list(z[:n]), 'b': list(z[n:])}
        restr.append(word_cocycle(MER, lets, vals) + word_cocycle(LONG, lets, vals))
    for vec in restr:
        u, v = vec[:n], vec[n:]
        l, r_ = mat_vec(Mlam, u), mat_vec(Mmu, v)
        assert all((l[i] - r_[i]).is_zero() for i in range(n))
    rk = quotient_rank(restr, B1T)
    h1_dbl = (h0T + 2 * h1 - rk) if top > 0 else ((h0T - 1) + 2 * h1 - rk)
    print(f"  V({top}): h1M={h1} h0T={h0T} h1T={h1T} rank(r)={rk} -> h1(dbl)={h1_dbl}",
          flush=True)
    # cross-gate: double-Fox
    lets3 = {'a': lets['a'], 'A': lets['A'], 'b': lets['b'], 'B': lets['B'],
             'd': lets['b'], 'D': lets['B']}
    Z1d, Bgend, h1d = fox_dbl(lets3, n)
    print(f"    cross-gate double-Fox h1 = {h1d}", flush=True)
    assert h1d == h1_dbl, f"MV vs double-Fox MISMATCH at V({top})"
    tot_dbl += h1_dbl
    # ---- V3: the seam pairing on the double classes' direct T^2 restrictions
    base = [list(r) for r in Bgend]
    cur_rank = len(rref([r[:] for r in base])[1]) if base else 0
    reps = []
    for z in Z1d:
        new_rank = len(rref([r[:] for r in (base + [list(z)])])[1])
        if new_rank > cur_rank:
            reps.append(list(z))
            base.append(list(z))
            cur_rank = new_rank
        if len(reps) == h1d:
            break
    assert len(reps) == h1d
    Bth = build_Btheta(n)
    invBth = all(mzero_p(msub(mmul([[lets[ch][j][i] for j in range(n)]
                                    for i in range(n)], mmul(Bth, lets[ch])), Bth))
                 for ch in 'ab')
    assert invBth, "Btheta invariance"
    def t2_restrict(zd):
        vals = {'a': list(zd[:n]), 'b': list(zd[n:2*n]), 'd': list(zd[2*n:])}
        zmu = word_cocycle(MER, {'a': lets['a'], 'A': lets['A'],
                                 'b': lets['b'], 'B': lets['B']},
                           {'a': vals['a'], 'b': vals['b']})
        zlam = word_cocycle(LONG, {'a': lets['a'], 'A': lets['A'],
                                   'b': lets['b'], 'B': lets['B']},
                            {'a': vals['a'], 'b': vals['b']})
        return zmu, zlam
    def seam_pair(zd, wd):
        zmu, zlam = t2_restrict(zd)
        wmu, wlam = t2_restrict(wd)
        bl = lambda u, v: sum((Bth[s][t] * u[s] * v[t] for s in range(n)
                               for t in range(n)
                               if not (u[s].is_zero() or v[t].is_zero())), K0)
        return bl(zmu, wlam) - bl(zlam, wmu)
    # V1 control: gauge invariance of the seam pairing (z -> z + coboundary)
    if Bgend and reps:
        pert = [reps[0][i] + Bgend[0][i] for i in range(3 * n)]
        d1 = seam_pair(pert, reps[-1]) - seam_pair(reps[0], reps[-1])
        d2 = seam_pair(reps[-1], pert) - seam_pair(reps[-1], reps[0])
        gate = d1.is_zero() and d2.is_zero()
        print(f"    V1 seam-gauge control: {'PASS' if gate else 'FAIL'}", flush=True)
        assert gate, "V1 CONTROL FAILED -- HALT"
    tab = {}
    for i in range(h1d):
        for j in range(i, h1d):
            sym = seam_pair(reps[i], reps[j]) + seam_pair(reps[j], reps[i])
            tab[(i, j)] = "PRESENT" if not sym.is_zero() else "absent"
    seam_tables[top] = tab
    print(f"    seam symmetric support: {tab}", flush=True)

print(f"\n[V4] h1(dbl; 27) = {tot_dbl} (solo 3)", flush=True)

print("\n[V5] h1(M; ad):", flush=True)
h1_ad = 0
for m, bd in sorted(BLOCK_DATA.items()):
    _, _, _, h1b = fox_M(bd['acts'], bd['d'])
    h1_ad += h1b
print(f"  TOTAL h1(M; ad) = {h1_ad} (predicted 6)", flush=True)

n_present = sum(1 for t in seam_tables.values() for v in t.values() if v == "PRESENT")
print(f"\n==== FINAL: V4 = {tot_dbl}; V5 = {h1_ad}; "
      f"V3 seam symmetric support PRESENT cells = {n_present} ====", flush=True)
