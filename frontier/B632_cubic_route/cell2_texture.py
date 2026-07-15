"""B632 cell 2 — the corrected texture computation (prereg:
CELL2_PREREGISTRATION.md, sealed before this ran).

(1) C = the unique cubic invariant on the 27, exact (gate: dim 1).
(2) v0 = the forced vev; B_C = C(v0,.,.) block structure; C's census.
(3) block cocycles (non-coboundary gates) + the O2 obstruction gates.
(4) Omega: Lambda^2 H^1(27) -> H^2(M; 27*), the exact class table.
"""
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = os.path.join(HERE, "..", "B575_bridge_obstruction", "l51_obstruction.py")
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time()
print("executing B575 stages 0-3...", flush=True)
exec(compile(src[:cut], B575, "exec"), ns)
print(f"prefix done in {time.time()-t0:.1f}s", flush=True)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
W27 = ns["W27"]
E6_e, E6_f = ns["E6_e"], ns["E6_f"]
h_pr, e_pr, f_pr = ns["h_pr"], ns["e_pr"], ns["f_pr"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
REL = ns["REL"]
nullspace = ns["nullspace"]
meye, mmul, madd, mscale = ns["meye"], ns["mmul"], ns["madd"], ns["mscale"]
Solver = ns["Solver"]

def apply(M, v):
    return [sum((M[i][j] * v[j] for j in range(27) if not v[j].is_zero()), K0)
            for i in range(27)]

# ---------------- (1) the cubic invariant C ----------------------------------
print("\n(1) the unique cubic invariant:", flush=True)
support, SUPIDX = [], {}
for p in range(27):
    for q in range(p, 27):
        for r in range(q, 27):
            if all(W27[p][k] + W27[q][k] + W27[r][k] == 0 for k in range(6)):
                SUPIDX[(p, q, r)] = len(support)
                support.append((p, q, r))
nsup = len(support)
print(f"  zero-weight-sum sorted triples: {nsup}", flush=True)

eqs = {}
for gi, X in enumerate(list(E6_e) + list(E6_f)):
    xent = [(s, t) for s in range(27) for t in range(27)
            if not X[s][t].is_zero()]
    for (a, b, c) in support:
        k = SUPIDX[(a, b, c)]
        for (u, v, w) in ((a, b, c), (b, a, c), (c, a, b)):
            for s, t in xent:
                if s == u:
                    key = (gi,) + tuple(sorted((t, v, w)))
                    row = eqs.setdefault(key, {})
                    row[k] = row.get(k, K0) + X[u][t]
rows = [[row.get(k, K0) for k in range(nsup)] for row in eqs.values()
        if any(not cv.is_zero() for cv in row.values())]
print(f"  invariance equations: {len(rows)}", flush=True)
sol = nullspace(rows)
assert len(sol) == 1, f"GATE FAIL: invariant space dim {len(sol)} != 1"
print("  GATE PASS: the invariant space is EXACTLY 1-dim "
      "(B308's multiplicity, this basis)", flush=True)
Cvals = sol[0]
CFULL = {}
for (p, q, r), k in SUPIDX.items():
    if not Cvals[k].is_zero():
        for perm in {(p, q, r), (p, r, q), (q, p, r), (q, r, p),
                     (r, p, q), (r, q, p)}:
            CFULL[perm] = Cvals[k]
print(f"  nonzero sorted coefficients: "
      f"{sum(1 for k in range(nsup) if not Cvals[k].is_zero())}/{nsup}",
      flush=True)

def C3(u, v):
    """covector m -> C(u, v, e_m)."""
    cov = [K0] * 27
    for (p, q, r), cval in CFULL.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r] = cov[r] + cval * u[p] * v[q]
    return cov

def dot(f, v):
    return sum((f[t] * v[t] for t in range(27) if not v[t].is_zero()), K0)

# invariance spot-gate: C(gu, gv, gw) = C(u,v,w) for g = A27 on random-ish vecs
u1 = [K(i % 5 - 2) for i in range(27)]
v1 = [K((2 * i) % 7 - 3) for i in range(27)]
w1 = [K((3 * i) % 4 - 1) for i in range(27)]
lhs = dot(C3(apply(A27, u1), apply(A27, v1)), apply(A27, w1))
rhs = dot(C3(u1, v1), w1)
assert (lhs - rhs).is_zero(), "C not A27-invariant?!"
print("  spot gate PASS: C(A.u, A.v, A.w) = C(u,v,w) exactly", flush=True)

# ---------------- (2) v0, block bases, B_C, census ----------------------------
print("\n(2) the forced vev and B_C:", flush=True)
def rows_minus(M, lam):
    return [[M[i][j] - (lam if i == j else K0) for j in range(27)]
            for i in range(27)]

fix = nullspace(rows_minus(A27, K1) + rows_minus(B27, K1))
assert len(fix) == 1
v0 = fix[0]
for op in (e_pr, f_pr, h_pr):
    assert all(x.is_zero() for x in apply(op, v0))
print("  v0 exact (1-dim, sl2-invariant) — the forced vev", flush=True)

BLOCKV = {}
for T in (16, 8):
    ker_h = nullspace(rows_minus(h_pr, K(T)))
    print(f"  diag: dim ker(h_pr - {T}) = {len(ker_h)}", flush=True)
    # stacked system: h v = T v AND e v = 0
    e_rows = [[e_pr[i][j] for j in range(27)] for i in range(27)]
    stacked = nullspace(rows_minus(h_pr, K(T)) + e_rows)
    print(f"  diag: dim (ker(h-{T}) ∩ ker e) = {len(stacked)}", flush=True)
    if len(stacked) >= 1:
        if len(stacked) > 1:
            print(f"  diag: WARNING multiplicity {len(stacked)} at V({T})",
                  flush=True)
        hi = stacked[0]
    else:
        if not ker_h:
            mults = {}
            for t in range(-20, 21):
                kk = nullspace(rows_minus(h_pr, K(t)))
                if kk:
                    mults[t] = len(kk)
            print(f"  diag: FULL h_pr multiset = {mults}", flush=True)
        assert len(ker_h) >= 1, f"no h-eigenspace at {T}"
        hi = ker_h[0]
        img = apply(e_pr, hi)
        iz = all(x.is_zero() for x in img)
        print(f"  diag: e_pr on ker(h-{T})[0] zero: {iz}", flush=True)
        if not iz:
            himg = apply(h_pr, img)
            cmp18 = all((himg[t] - K(T + 2) * img[t]).is_zero()
                        for t in range(27))
            print(f"  diag: h.(e.v) = {T+2}.(e.v): {cmp18}", flush=True)
    vecs = [hi]
    for _ in range(T):
        vecs.append(apply(f_pr, vecs[-1]))
    assert not all(x.is_zero() for x in vecs[-1]), f"string short at V({T})"
    assert all(x.is_zero() for x in apply(f_pr, vecs[-1])), \
        f"string does not terminate at V({T})"
    BLOCKV[T] = vecs
BLOCKV[0] = [v0]
order = [(16, i) for i in range(17)] + [(8, i) for i in range(9)] + [(0, 0)]
ALLB = [BLOCKV[T][i] for (T, i) in order]
SL = {16: (0, 17), 8: (17, 26), 0: (26, 27)}

# B_C full matrix in the block basis
BC = []
for w in ALLB:
    cov = C3(v0, w)
    BC.append([dot(cov, x) for x in ALLB])
off_zero = True
diag_nz = {}
for T in (16, 8, 0):
    s, e = SL[T]
    diag_nz[T] = any(not BC[i][j].is_zero()
                     for i in range(s, e) for j in range(s, e))
    for T2 in (16, 8, 0):
        if T2 == T:
            continue
        s2, e2 = SL[T2]
        if any(not BC[i][j].is_zero() for i in range(s, e)
               for j in range(s2, e2)):
            off_zero = False
print(f"  B_C off-block entries all zero: {off_zero} (sl2 prediction)",
      flush=True)
for T in (16, 8, 0):
    print(f"    c_{T//2} (V({T}) block of B_C): "
          f"{'NONZERO' if diag_nz[T] else 'ZERO'}", flush=True)

print("  C component census (spin triples, witness search):", flush=True)
census = {}
for Ta in (16, 8, 0):
    for Tb in (16, 8, 0):
        key0 = tuple(sorted((Ta, Tb), reverse=True))
        for va in BLOCKV[Ta]:
            for vb in BLOCKV[Tb]:
                cov = C3(va, vb)
                for Tc in (16, 8, 0):
                    key = tuple(sorted((Ta // 2, Tb // 2, Tc // 2),
                                       reverse=True))
                    if census.get(key):
                        continue
                    if any(not dot(cov, vc).is_zero() for vc in BLOCKV[Tc]):
                        census[key] = True
for Ta in (8, 4, 0):
    for Tb in (8, 4, 0):
        for Tc in (8, 4, 0):
            key = tuple(sorted((Ta, Tb, Tc), reverse=True))
            census.setdefault(key, False)
for key in sorted(census, reverse=True):
    print(f"    spins {key}: {'PRESENT' if census[key] else 'absent'}",
      flush=True)

# ---------------- (3) cocycles + O2 gates --------------------------------------
print("\n(3) block cocycles and the obstruction gates:", flush=True)
acts = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
PREFIX = [meye(27)]
for ch in REL[:-1]:
    PREFIX.append(mmul(PREFIX[-1], acts[ch]))

def fox_LaLb(actmap):
    La = [[K0] * 27 for _ in range(27)]
    Lb = [[K0] * 27 for _ in range(27)]
    Pi = meye(27)
    for ch in REL:
        if ch == 'a':   contrib, tgt, sgn = meye(27), 'a', 1
        elif ch == 'A': contrib, tgt, sgn = actmap['A'], 'a', -1
        elif ch == 'b': contrib, tgt, sgn = meye(27), 'b', 1
        else:           contrib, tgt, sgn = actmap['B'], 'b', -1
        term = mmul(Pi, contrib)
        if sgn < 0:
            term = mscale(K(-1), term)
        if tgt == 'a':
            La = madd(La, term)
        else:
            Lb = madd(Lb, term)
        Pi = mmul(Pi, actmap[ch])
    return La, Lb

La, Lb = fox_LaLb(acts)

def in_span(vecs, w):
    if not vecs:
        return all(x.is_zero() for x in w)
    try:
        Solver([v[:] for v in vecs] + []).coords(w)
        return True
    except ValueError:
        return False

Z = {}
for T in (0, 8, 16):
    d = 2 * (T // 2) + 1
    bas = BLOCKV[T]
    # cocycle condition restricted to block-supported (za, zb)
    cols = []
    for slot in range(2):
        for j in range(d):
            za = bas[j] if slot == 0 else [K0] * 27
            zb = bas[j] if slot == 1 else [K0] * 27
            img = [sum((La[i][t] * za[t] for t in range(27)
                        if not za[t].is_zero()), K0)
                   + sum((Lb[i][t] * zb[t] for t in range(27)
                          if not zb[t].is_zero()), K0) for i in range(27)]
            cols.append(img)
    rowsys = [[cols[c][i] for c in range(2 * d)] for i in range(27)]
    kerc = nullspace(rowsys)
    # coboundaries from block-supported v
    cobs = []
    for j in range(d):
        v = bas[j]
        da = [x - v[i] for i, x in enumerate(apply(A27, v))]
        db = [x - v[i] for i, x in enumerate(apply(B27, v))]
        # express (da, db) in block coordinates: coefficients against bas
        bs = Solver([b[:] for b in bas])
        cobs.append(bs.coords(da) + bs.coords(db))
    # pick a kernel vector NOT in the coboundary span
    pick = None
    for kv in kerc:
        if not in_span(cobs, kv):
            pick = kv
            break
    assert pick is not None, f"no non-coboundary cocycle in block V({T})"
    za = [sum((pick[j] * bas[j][i] for j in range(d)
               if not pick[j].is_zero()), K0) for i in range(27)]
    zb = [sum((pick[d + j] * bas[j][i] for j in range(d)
               if not pick[d + j].is_zero()), K0) for i in range(27)]
    Z[T] = za + zb
    print(f"    V({T}): cocycles {len(kerc)}, coboundaries {len(cobs)}, "
          f"non-coboundary representative chosen", flush=True)

def cup_covector(z, w):
    """[z cup w] evaluated on the CORRECTED 2-cell chain
    c2 = sum_i [p_{i-1}|x_i]  -  sum_{i: x_i = l^-1} p_{i-1}[l^-1|l],
    so that bar-coboundaries land exactly in the cellular Fox image
    (the naive chain misses the inverse-letter correction; caught by
    the coboundary-invariance O2 gate on the first run)."""
    za, zb = z[:27], z[27:]
    wa, wb = w[:27], w[27:]
    def lv(a_, b_, ch):
        if ch == 'a':
            return a_
        if ch == 'b':
            return b_
        if ch == 'A':
            return [K0 - x for x in apply(A27i, a_)]
        return [K0 - x for x in apply(B27i, b_)]
    n = len(REL)
    total = [K0] * 27
    cur = [K0] * 27
    for i, ch in enumerate(REL):
        Vv = apply(PREFIX[i], lv(wa, wb, ch))
        cv = C3(cur, Vv)
        total = [total[t] + cv[t] for t in range(27)]
        if ch in 'AB':                      # inverse-letter correction
            ell = ch.lower()
            P_next = PREFIX[i + 1] if i + 1 < n else meye(27)
            u_c = apply(PREFIX[i], lv(za, zb, ch))       # p_{i-1}.z(l^-1)
            v_c = apply(P_next, wa if ell == 'a' else wb)  # p_i.w(l)
            cc = C3(u_c, v_c)
            total = [total[t] - cc[t] for t in range(27)]
        add = apply(PREFIX[i], lv(za, zb, ch))
        cur = [cur[t] + add[t] for t in range(27)]
    return total

# H^2(27*) coker functionals: y with y^T La* = 0 = y^T Lb*
def transpose(M):
    return [[M[j][i] for j in range(27)] for i in range(27)]
dacts = {'a': transpose(A27i), 'b': transpose(B27i),
         'A': transpose(A27), 'B': transpose(B27)}
Lad, Lbd = fox_LaLb(dacts)
rowsT = ([[Lad[i][j] for i in range(27)] for j in range(27)] +
         [[Lbd[i][j] for i in range(27)] for j in range(27)])
phis = nullspace(rowsT)
print(f"  h^2(27*) = {len(phis)} (expected 2)", flush=True)
assert len(phis) == 2

def klass(cov):
    return tuple(dot(ph, cov) for ph in phis)

def kstr(kk):
    return "(" + ", ".join("0" if x.is_zero() else str(x) for x in kk) + ")"

print("\n  O2 gates:", flush=True)
sp = klass(cup_covector(Z[8], Z[8]))
print(f"    diagonal class [z4 cup z4] = "
      f"{'(0, 0)' if all(x.is_zero() for x in sp) else kstr(sp)} "
      f"(O2 predicts zero)", flush=True)
sp16 = klass(cup_covector(Z[16], Z[16]))
print(f"    diagonal class [z8 cup z8] zero: "
      f"{all(x.is_zero() for x in sp16)}", flush=True)
anti_ok = []
pairs = [(0, 8), (0, 16), (8, 16)]
for (Ta, Tb) in pairs:
    k1 = klass(cup_covector(Z[Ta], Z[Tb]))
    k2 = klass(cup_covector(Z[Tb], Z[Ta]))
    anti_ok.append(all((k1[t] + k2[t]).is_zero() for t in range(2)))
print(f"    class-level antisymmetry on the three pairs: {anti_ok}",
      flush=True)

# coboundary control
v = [K(1) if i in (2, 11, 19) else K0 for i in range(27)]
da = [x - v[i] for i, x in enumerate(apply(A27, v))]
db = [x - v[i] for i, x in enumerate(apply(B27, v))]
zs = [Z[8][t] + (da + db)[t] for t in range(54)]
inv_ok = klass(cup_covector(zs, Z[16])) == klass(cup_covector(Z[8], Z[16]))
raw_ch = any(not (a - b).is_zero() for a, b in
             zip(cup_covector(zs, Z[16]), cup_covector(Z[8], Z[16])))
print(f"    coboundary control: class invariant {inv_ok}, "
      f"raw cochain changed {raw_ch}", flush=True)

# ---------------- (4) Omega -----------------------------------------------------
print("\n(4) Omega: Lambda^2 H^1(27) -> H^2(M; 27*) (classes per pair):",
      flush=True)
for (Ta, Tb) in pairs:
    kk = klass(cup_covector(Z[Ta], Z[Tb]))
    tag = "ZERO" if all(x.is_zero() for x in kk) else "NONZERO " + kstr(kk)
    print(f"    Omega(z{Ta//2}, z{Tb//2}) = {tag}", flush=True)
print("\nB632 cell 2 DONE", flush=True)
