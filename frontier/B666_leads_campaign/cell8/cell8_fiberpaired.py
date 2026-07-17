"""B666 CELL 8 (L92 + R21-4) — the fiber-paired object D_conjtheta(M): exact
realization via theta_27 o conj, its (i1, i2), the dimension grammar, and the
glued cubic.

CONVENTIONS (declared before the run; WORKING_RULES rule 4):
  * Field K = Q(sqrt(-3)), elements a + b*sqrt(-3); conj = the Galois map
    b -> -b (restricting to complex conjugation on the geometric embedding).
  * Side 1 = (K^27, rho): the banked b637 figure-eight 27-holonomy
    (a -> exp(e_pr), b -> exp(omega f_pr)); mu = "a", lambda = LONG.
  * Side 2 carries the SAME representation class as the weld's second copy:
    rho_bar = conj o rho (B639's banked structural fact: theta fixes the
    holonomy pointwise, so conj o theta o rho = conj o rho).
  * theta_27: 27 -> 27bar = the diagram-involution intertwiner — the unique
    (Schur) map with theta_27 . rho(x) = -rho(theta x)^T . theta_27 for all
    x in e6; in the weight basis it is the invariant pairing composed with
    weight negation: e_j -> t_j e*_{k(j)}, mu_{k(j)} = -theta(mu_j).
  * The fiber pairing (the gluing B639 proved is NOT a representation
    twist): beta(v, w) = w^T . theta_27 . conj(v), an exact pi_1-invariant
    sesquilinear pairing between (V, rho) and (V, rho_bar); the gluing
    chart map is phi(v) = theta_27 . conj(v) into the V2*-coordinates
    (side-2 letters there: rho_bar* = (conj(rho)^T)^{-1}).
  * Peripheral convention of the twisted double (B639, sealed): mu' = mu,
    lambda' = +lambda; presentation relators
    [REL(a,b), REL(c,d), aC, LONG(a,b) . inv(LONG(c,d))].
  * i1 = dim_K Fix(glued holonomy: all four trivialized letters);
    i2 = dim_K Fix(glued peripheral pair: rho(mu), rho(lambda)).
  * Cubics: side-1 C = banked CFULL; side-2 C* = the invariant cubic of the
    dual rep (x -> -x^T), built by the same machinery; kappa = the exact
    proportionality scalar of phi-pulled C* against C (the (C, C*)
    compatibility datum).  PRIMARY glued 3-form: the flat cubic of the
    trivialized K-local system (= C on both sides): Y = F1 - F2.
    SECONDARY (the intrinsic (C, C*) reading, antilinear leg explicit):
    Y_intr = F1 - kappa * conj(F2).  Both gated (glued-coboundary
    invariance + antisymmetry); gates decide.
All decisive steps exact over K (Fraction pairs).  No floats.
"""
import itertools as it
import os
import time

T0 = time.time()
def tlog(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "..", "B637_corrected_cell3")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
tlog("executing the b637 namespace (B575 prefix + cubic + weld)...")
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
tlog("b637 namespace ready")

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG, REL = mod["LONG"], mod["REL"]
side1, Side = mod["side1"], mod["Side"]
apply_ = mod["apply"]
kconj, mconj, minv = mod["kconj"], mod["mconj"], mod["minv"]
meye, mmul = mod["meye"], mod["mmul"]
nullspace, rref = mod["nullspace"], mod["rref"]
ns = mod["ns"]
Cval, CFULL = mod["Cval"], mod["CFULL"]
A27, B27, A27i, B27i = mod["A27"], mod["B27"], mod["A27i"], mod["B27i"]
lets1 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
W27, IDX, C6 = ns["W27"], ns["IDX"], ns["C6"]
E6_e, E6_f = ns["E6_e"], ns["E6_f"]
Solver = ns["Solver"]
msub, mzero_p, madd, mscale = ns["msub"], ns["mzero_p"], ns["madd"], ns["mscale"]


def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def meq(A, B):
    return mzero_p(msub(A, B))


# ---------------------------------------------------------------- stage 1: sigma
perms = [p for p in it.permutations(range(6))
         if all(C6[p[i]][p[j]] == C6[i][j] for i in range(6) for j in range(6))]
assert len(perms) == 2, f"Dynkin automorphism count {len(perms)} != 2"
sig = next(p for p in perms if p != tuple(range(6)))
tlog(f"stage 1: the E6 diagram involution sigma = {sig}")

# weight-negation-with-flip index map: mu_{k(j)} = -theta(mu_j)
kj = []
for j in range(27):
    tgt = tuple(-W27[j][sig[m]] for m in range(6))
    assert tgt in IDX, f"weight negation leaves W27 at j={j}"
    kj.append(IDX[tgt])
assert sorted(kj) == list(range(27)), "k(j) not a bijection"
kjinv = [0] * 27
for j in range(27):
    kjinv[kj[j]] = j
tlog("stage 1: weight-negation index map k(j) built (bijection OK)")

# ---------------------------------------------------------------- stage 2: theta_27
# unknown t_j; T[r][c] = t_c iff r = k(c).  Equations: T X + (theta X)^T T = 0
pairs = [(E6_e[i], E6_e[sig[i]]) for i in range(6)] + \
        [(E6_f[i], E6_f[sig[i]]) for i in range(6)]
rows_t = []
for (X, Xt) in pairs:
    for r in range(27):
        j0 = kjinv[r]
        for c in range(27):
            e1 = X[j0][c]           # coeff of t_{j0} from (T X)[r][c]
            e2 = Xt[kj[c]][r]       # coeff of t_c   from ((theta X)^T T)[r][c]
            if e1.is_zero() and e2.is_zero():
                continue
            row = [K0] * 27
            row[j0] = row[j0] + e1
            row[c] = row[c] + e2
            rows_t.append(row)
solt = nullspace(rows_t)
assert len(solt) == 1, f"GATE FAIL: theta_27 solution space dim {len(solt)} != 1"
tvec = solt[0]
# normalize: first nonzero -> 1
piv = next(j for j in range(27) if not tvec[j].is_zero())
sc = tvec[piv].inv()
tvec = [x * sc for x in tvec]
assert all(not x.is_zero() for x in tvec), "GATE FAIL: theta_27 not invertible"
rational = all(x.b == 0 for x in tvec)
tlog(f"stage 2: theta_27 solved (dim 1, Schur); coefficients rational: {rational}")
assert rational, "GATE FAIL: theta_27 not rational — conj-cancellation invalid"
Tm = [[K0] * 27 for _ in range(27)]
for c in range(27):
    Tm[kj[c]][c] = tvec[c]
Tmi = minv([row[:] for row in Tm])
tvals = sorted(set(str(x.a) for x in tvec))
tlog(f"stage 2: t_j value set (up to the normalization) = {tvals}")

# GATE: full Lie-level equivariance for all 12 generators
g_lie = all(mzero_p(madd(mmul(Tm, X), mmul(transpose(Xt), Tm)))
            for (X, Xt) in pairs)
print(f"GATE Lie equivariance  T x + (theta x)^T T = 0 (12 gens): {g_lie}",
      flush=True)
assert g_lie

# GATE: group level  T rho(g) = (rho(g)^T)^{-1} T  for a, b, lambda
LAM = side1.mat(LONG)
LAMi = side1.mat(inv(LONG))
g_grp = (meq(mmul(Tm, A27), mmul(transpose(A27i), Tm))
         and meq(mmul(Tm, B27), mmul(transpose(B27i), Tm))
         and meq(mmul(Tm, LAM), mmul(transpose(LAMi), Tm)))
print(f"GATE group equivariance T rho = (rho^T)^-1 T (a, b, lambda): {g_grp}",
      flush=True)
assert g_grp

# GATE: the sesquilinear fiber pairing beta(v,w) = w^T T conj(v) is
# pi_1-invariant between (V, rho) and (V, conj rho):
g_pair = all(meq(mmul(mmul(transpose(mconj(P)), Tm), mconj(P)), Tm)
             for P in (A27, B27))
print(f"GATE fiber pairing invariance rho_bar^T T rho_bar = T: {g_pair}",
      flush=True)
assert g_pair

# GATE: the antilinear gluing phi = theta_27 o conj intertwines the
# peripheral pair with the TWISTED convention mu'=mu, lambda'=+lambda:
#   T conj(rho(p)) = (conj(rho(p))^T)^{-1} T   for p = mu, lambda
g_glue = all(meq(mmul(Tm, mconj(P)), mmul(transpose(mconj(Pi)), Tm))
             for (P, Pi) in ((A27, A27i), (LAM, LAMi)))
print(f"GATE +lambda antilinear peripheral gluing: {g_glue}", flush=True)
assert g_glue

# ---------------------------------------------------------------- stage 3: trivialized letters
# side-2 letters in the V2*-chart: rho_bar*(g) = (conj(rho(g))^T)^{-1}
# pulled to the side-1 chart through phi:  g -> conj( T^-1 rho_bar*(g) T )
def trivialized(P, Pi):
    r2s = transpose(mconj(Pi))          # (conj(P)^T)^{-1} = conj(Pi)^T
    return mconj(mmul(mmul(Tmi, r2s), Tm))

c_mat = trivialized(A27, A27i)
d_mat = trivialized(B27, B27i)
c_inv = trivialized(A27i, A27)
d_inv = trivialized(B27i, B27)
collapse_c = meq(c_mat, A27)
collapse_d = meq(d_mat, B27)
print(f"COLLAPSE CHECK: trivialized c == rho(a): {collapse_c}; "
      f"d == rho(b): {collapse_d}", flush=True)
assert meq(mmul(c_mat, c_inv), meye(27))
assert meq(mmul(d_mat, d_inv), meye(27))

lets4 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i,
         'c': c_mat, 'd': d_mat, 'C': c_inv, 'D': d_inv}
prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
c_l = LONG.translate(str.maketrans("abAB", "cdCD"))
relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
            "aC", LONG + inv(c_l)]
for w in relators:
    Pi_ = meye(27)
    for ch in w:
        Pi_ = mmul(Pi_, lets4[ch])
    assert meq(Pi_, meye(27)), f"GATE FAIL: glued relator {w[:12]}..."
print("GATE glued presentation relators (all 4) = identity: True", flush=True)

# ---------------------------------------------------------------- stage 4: (i1, i2)
def fixdim(mats):
    rows = []
    for M in mats:
        for i in range(27):
            rows.append([M[i][j] - (K1 if i == j else K0) for j in range(27)])
    return len(nullspace(rows))

i1 = fixdim([lets4[g] for g in "abcd"])
i2 = fixdim([A27, LAM])
# side-2 peripheral pair (c_mat, LONG(c,d)) — computed honestly:
lam_cd = meye(27)
for ch in LONG:
    lam_cd = mmul(lam_cd, lets4[ch.translate(str.maketrans("abAB", "cdCD"))])
i2b = fixdim([c_mat, lam_cd])
i1M = fixdim([A27, B27])
print(f"\n(i1, i2) OF THE FIBER-PAIRED OBJECT: i1 = {i1}, i2 = {i2} "
      f"(side-2 peripheral check: {i2b}; side-1 holonomy fix h0(M) = {i1M})",
      flush=True)

# ---------------------------------------------------------------- stage 5: h1(M) cross-input
rowsM = []
Lm = {g: [[K0] * 27 for _ in range(27)] for g in "ab"}
Pi_ = meye(27)
for ch in REL:
    g = prim[ch]
    term = Pi_ if ch.islower() else mscale(K(-1), mmul(Pi_, lets1[ch]))
    Lm[g] = madd(Lm[g], term)
    Pi_ = mmul(Pi_, lets1[ch])
assert meq(Pi_, meye(27))
for i in range(27):
    rowsM.append([Lm[g][i][j] for g in "ab" for j in range(27)])
ZM = nullspace(rowsM)
cobM = []
for j in range(27):
    v = [K1 if t == j else K0 for t in range(27)]
    entry = []
    for g in "ab":
        gv = apply_(lets1[g], v)
        entry.extend([gv[i] - v[i] for i in range(27)])
    cobM.append(entry)
_, pivM = rref(cobM)
h1M = len(ZM) - len(pivM)
print(f"h1(M; 27) = {h1M}  [G5 side input]", flush=True)

# ---------------------------------------------------------------- stage 6: the glued grammar
rows_all = []
for w in relators:
    L = {g: [[K0] * 27 for _ in range(27)] for g in "abcd"}
    Pi_ = meye(27)
    for ch in w:
        g = prim[ch]
        term = Pi_ if ch.islower() else mscale(K(-1), mmul(Pi_, lets4[ch]))
        L[g] = madd(L[g], term)
        Pi_ = mmul(Pi_, lets4[ch])
    for i in range(27):
        rows_all.append([L[g][i][j] for g in "abcd" for j in range(27)])
tlog("stage 6: Fox rows built; solving the 108-dim cocycle space...")
Zc = nullspace(rows_all)
cob = []
for j in range(27):
    v = [K1 if t == j else K0 for t in range(27)]
    entry = []
    for g in "abcd":
        gv = apply_(lets4[g], v)
        entry.extend([gv[i] - v[i] for i in range(27)])
    cob.append(entry)
reps, basis = [], [r[:] for r in cob]
for z in Zc:
    try:
        Solver(basis).coords(z)
    except ValueError:
        reps.append(z)
        basis.append(z)
h0D = i1
h1D = len(reps)
print(f"\nTHE DIMENSION GRAMMAR (direct Fox computation):", flush=True)
print(f"  h0(D_conjtheta; 27) = {h0D}", flush=True)
print(f"  h1(D_conjtheta; 27) = {h1D}   "
      f"[cc2's withdrawn value was 3; the weld double has 5]", flush=True)
print(f"  G5-reduction cross-check: (i1, i2) = ({i1}, {i2}) "
      f"-> grammar h1(M) = 3, h0(D) = 1, h1(D) = 5 iff (1, 3)", flush=True)

# the swap involution (z1, z2) -> (z2, z1) on H^1 (structure datum)
solv_sw = Solver([r[:] for r in cob] + reps)
SW = []
ok_sw = True
for z in reps:
    sz = z[54:108] + z[0:54]
    try:
        co = solv_sw.coords(sz)
        SW.append(co[27:27 + len(reps)])
    except ValueError:
        ok_sw = False
        break
if ok_sw:
    SWm = [[SW[j][i] for j in range(len(reps))] for i in range(len(reps))]
    rp = len(rref([[SWm[i][j] - (K1 if i == j else K0)
                    for j in range(h1D)] for i in range(h1D)])[1])
    rm = len(rref([[SWm[i][j] + (K1 if i == j else K0)
                    for j in range(h1D)] for i in range(h1D)])[1])
    print(f"  swap involution on H1: dim(+1) = {h1D - rp}, "
          f"dim(-1) = {h1D - rm}", flush=True)
else:
    print("  swap involution: image not a cocycle (unexpected)", flush=True)

# ---------------------------------------------------------------- stage 7: C* and kappa
def build_cubic(gens):
    support, SUPIDX = [], {}
    for p in range(27):
        for q in range(p, 27):
            for r_ in range(q, 27):
                if all(W27[p][k] + W27[q][k] + W27[r_][k] == 0
                       for k in range(6)):
                    SUPIDX[(p, q, r_)] = len(support)
                    support.append((p, q, r_))
    eqs = {}
    for gi, X in enumerate(gens):
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
    rows = [[row.get(k, K0) for k in range(len(support))]
            for row in eqs.values()]
    sol = nullspace(rows)
    assert len(sol) == 1, f"invariant cubic space dim {len(sol)} != 1"
    FULL = {}
    for (p, q, r_), k in SUPIDX.items():
        if not sol[0][k].is_zero():
            for perm in {(p, q, r_), (p, r_, q), (q, p, r_), (q, r_, p),
                         (r_, p, q), (r_, q, p)}:
                FULL[perm] = sol[0][k]
    return FULL

# NOTE: the dual weights are the negatives; sum-zero support is identical.
gens_dual = [[[K0 - X[j][i] for j in range(27)] for i in range(27)]
             for X in (list(E6_e) + list(E6_f))]
CSTAR = build_cubic(gens_dual)
tlog(f"stage 7: dual cubic C* built ({len(CSTAR)} ordered entries, dim 1)")

kappa = None
g_kappa = True
seen_un = set()
for (p, q, r_) in CFULL:
    keyu = tuple(sorted((p, q, r_)))
    if keyu in seen_un:
        continue
    seen_un.add(keyu)
    img = tuple(sorted((kj[p], kj[q], kj[r_])))
    cs = CSTAR.get(img, K0)
    val = cs * tvec[p] * tvec[q] * tvec[r_]
    ratio = val * CFULL[(p, q, r_)].inv()
    if kappa is None:
        kappa = ratio
    elif not (ratio - kappa).is_zero():
        g_kappa = False
        break
# also check C* has no support outside the image of CFULL's support
img_sup = {tuple(sorted((kj[p], kj[q], kj[r_]))) for (p, q, r_) in CFULL}
extra = {tuple(sorted(k)) for k in CSTAR} - img_sup
print(f"GATE (C, C*) compatibility through phi: proportional {g_kappa}, "
      f"extra C* support {len(extra)}; kappa = {kappa}", flush=True)
assert g_kappa and not extra

# ---------------------------------------------------------------- stage 8: the glued cubic
if h1D >= 3:
    side2 = Side({'a': c_mat, 'b': d_mat, 'A': c_inv, 'B': d_inv})
    P1 = freduce("a" + LONG)

    def sides_of(z):
        return ((z[0:27], z[27:54]), (z[54:81], z[81:108]))

    def Fcomm(sideobj, zA, zB, zC):
        om = sideobj.make_omega(zA, zB, zC)
        S = lambda g, h, gh: sideobj.S_eval(om, g, h, gh)
        return S("a", LONG, P1) - S(LONG, "a", P1)

    tlog("stage 8: computing F1/F2 on all class triples...")
    F1 = {}
    F2 = {}
    for (i, j, k) in it.combinations(range(h1D), 3):
        (a1, a2), (b1, b2), (c1, c2) = (sides_of(reps[i]), sides_of(reps[j]),
                                        sides_of(reps[k]))
        F1[(i, j, k)] = Fcomm(side1, a1, b1, c1)
        F2[(i, j, k)] = Fcomm(side2, a2, b2, c2)
        y = F1[(i, j, k)] - F2[(i, j, k)]
        yi = F1[(i, j, k)] - kappa * kconj(F2[(i, j, k)])
        print(f"  triple {(i,j,k)}: F1 = {F1[(i,j,k)]}, F2 = {F2[(i,j,k)]}, "
              f"Y = {'0' if y.is_zero() else str(y)}, "
              f"Y_intr = {'0' if yi.is_zero() else str(yi)}", flush=True)

    def full_tensor(D):
        Y = {}
        for (i, j, k), v in D.items():
            for perm, sgn in (((i, j, k), 1), ((j, k, i), 1), ((k, i, j), 1),
                              ((j, i, k), -1), ((i, k, j), -1),
                              ((k, j, i), -1)):
                Y[perm] = v if sgn > 0 else K0 - v
        return Y

    Ylin = full_tensor({t: F1[t] - F2[t] for t in F1})
    Yintr = full_tensor({t: F1[t] - kappa * kconj(F2[t]) for t in F1})

    # gates on the primary (flat) form: coboundary invariance + antisymmetry
    def cob_shift(z, jv=5):
        v = [K1 if t == jv else K0 for t in range(27)]
        out = list(z)
        for gi, g in enumerate("abcd"):
            gv = apply_(lets4[g], v)
            for i in range(27):
                out[gi * 27 + i] = out[gi * 27 + i] + gv[i] - v[i]
        return out

    def Yval_pair(zA, zB, zC):
        (a1, a2), (b1, b2), (c1, c2) = map(sides_of, (zA, zB, zC))
        f1 = Fcomm(side1, a1, b1, c1)
        f2 = Fcomm(side2, a2, b2, c2)
        return f1 - f2, f1 - kappa * kconj(f2)

    y0l, y0i = Yval_pair(reps[0], reps[1], reps[2])
    ysl, ysi = Yval_pair(cob_shift(reps[0]), reps[1], reps[2])
    yal, yai = Yval_pair(reps[1], reps[0], reps[2])
    gA_lin = (ysl - y0l).is_zero()
    gB_lin = (yal + y0l).is_zero()
    gA_int = (ysi - y0i).is_zero()
    gB_int = (yai + y0i).is_zero()
    print(f"GATES Y (flat/primary): coboundary {gA_lin}, antisym {gB_lin}",
          flush=True)
    print(f"GATES Y_intr (C,C* w/ conj leg): coboundary {gA_int}, "
          f"antisym {gB_int}", flush=True)

    def rank_kernel(Y):
        rowsk = []
        for p in range(h1D):
            for q in range(p + 1, h1D):
                rowsk.append([Y.get((i, p, q), K0) for i in range(h1D)])
        kerd = len(nullspace(rowsk))
        return h1D - kerd, kerd

    if gA_lin and gB_lin:
        rk, kd = rank_kernel(Ylin)
        print(f"THE GLUED CUBIC (flat, C both sides in the trivialized "
              f"chart): rank {rk}, kernel dim {kd} (of h1 = {h1D})",
              flush=True)
    if gA_int and gB_int:
        rk, kd = rank_kernel(Yintr)
        print(f"THE (C, C*) INTRINSIC CUBIC: rank {rk}, kernel dim {kd}",
              flush=True)
    # the joint (F1, F2) kernel = the Q-structure kernel of the intrinsic form
    FT1, FT2 = full_tensor(F1), full_tensor(F2)
    rowsj = []
    for p in range(h1D):
        for q in range(p + 1, h1D):
            rowsj.append([FT1.get((i, p, q), K0) for i in range(h1D)])
            rowsj.append([FT2.get((i, p, q), K0) for i in range(h1D)])
    kdj = len(nullspace(rowsj))
    print(f"joint (F1, F2) kernel dim (the Q-structure kernel): {kdj}",
          flush=True)
else:
    print(f"h1 = {h1D} < 3: no cubic exists on the glued object; banked.",
          flush=True)

tlog("CELL 8 DONE")
