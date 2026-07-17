"""B662 CELL H — the cochain program, first cell: triple Massey products
on the golden double D (unbent weld), coefficients 27 x 27 -> 27bar via
the Jordan cross (the E6 cubic's polarization), target H^2(D;C) = C.

METHOD (degree-2 presentation route; exact over K = Q(sqrt-3)):
  * The banked 5-class basis is rebuilt VERBATIM from b637_threeform.py's
    double_Y class construction (bend None); a decisive basis-match
    control recomputes two banked Y components through the full banked
    T.H evaluator (stage-3 certify peeling patch) and compares exactly.
  * cup:  (u_i cup u_j)(g,h) = u_i(g) x rho(g)u_j(h)  in 27bar,
    where (x x y)_r = sum C_{pqr} x_p y_q (CFULL, the rebuilt cubic) and
    27bar carries the contragredient action rhobar(g) = rho(g)^{-T}.
    Strict associativity dot(x x y, z) = dot(x, y x z) = N(x,y,z) holds
    by N's total symmetry, so the coefficient system
    (27, 27bar, C; cross, dual dot) is a strict pairing system.
  * class test: a bar 2-cocycle c is a coboundary in H^2(pi;M) iff its
    evaluation on the corrected relator bar 2-chains (the b637 rel_chain
    convention: [p_{i-1}|x_i] cells, correction -p_{i-1}[l^{-1}|l]) lies
    in the image of the Fox map C^1(gens;M) -> C^2(rels;M).  (H^2(pi;M)
    injects into H^2 of the presentation 2-complex; both directions of
    the iff are exact — see FINDINGS_CELL.md.)
  * primitives: solve Phi_bar . a_gen = E(c) exactly; extend a to the
    whole group by the normalized-cochain recursion
      a(w.l) = a(w) + rhobar(w).a(l) - c(w,l),
      a(X) = c(X,x) - rhobar(X).a_gen(x)  (X = x^{-1});
    well-definedness is guaranteed by the relator condition (c is a
    normalized 2-cocycle) and is GATED by relator-insertion invariance.
  * Massey representative:  m(i,j,k) = a_ij cup u_k + u_i cup b_jk
    with delta a_ij = u_i cup u_j, delta b_jk = u_j cup u_k; then
    delta m = (u_i cup u_j) cup u_k - u_i cup (u_j cup u_k) = 0 by the
    strict associativity above (GATED numerically).
  * scalar: H^2(D;C) = C (b_2 = 1 banked); the class of a C-valued
    2-cocycle is phi(E_triv(.)) with phi the left-null functional of the
    trivial Fox (abelianized relator) matrix; H^2(pi;C) -> coker is an
    iso here (both 1-dim).
  * indeterminacy of <u_i,u_j,u_k>: the K-subspace
      { phi(E(zbar cup u_k)) : zbar in H^1(D;27bar) }
    + { phi(E(u_i cup zbar)) : zbar in H^1(D;27bar) }  (0 or all of K).

Zero floats anywhere.  New files only, all under cellH/.
"""
import os
import sys
import time
import itertools as it
from fractions import Fraction as Fr

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.normpath(os.path.join(HERE, "..", "..",
                                     "B637_corrected_cell3"))

log("STEP 0: exec b637_threeform.py (banked apparatus)...")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
log("b637 module loaded")

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG, REL = mod["LONG"], mod["REL"]
apply_ = mod["apply"]
nullspace, rref = mod["nullspace"], mod["rref"]
meye, mmul, minv = mod["meye"], mod["mmul"], mod["minv"]
ns = mod["ns"]
madd, msub, mscale, mzero_p = (ns["madd"], ns["msub"], ns["mscale"],
                               ns["mzero_p"])
Solver = ns["Solver"]
CFULL = mod["CFULL"]
lets1 = mod["lets1"]
side2lets = mod["side2lets"]
side1 = mod["side1"]
Side = mod["Side"]

# stage-3 certify peeling patch (verbatim b637_stage3.py) — the banked
# unbent table was produced with this patch in place.
_base_certify = mod["certify"]


def certify_peeled(word):
    w = freduce(word)
    if w == "":
        return []
    if len(w) >= 2 and w[0] == w[-1].swapcase():
        inner = certify_peeled(w[1:-1])
        return [(freduce(w[0] + u), e) for (u, e) in inner]
    return _base_certify(w)


mod["certify"] = certify_peeled
assert mod["certify"] is certify_peeled

# ---------------------------------------------------------------------------
log("STEP 1: rebuild the banked 5-class basis (double_Y construction, "
    "bend None, VERBATIM)...")
s2 = dict(side2lets)
lets4 = {'a': lets1['a'], 'b': lets1['b'], 'A': lets1['A'],
         'B': lets1['B'], 'c': s2['a'], 'd': s2['b'],
         'C': s2['A'], 'D': s2['B']}
prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
RELATORS = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
            "aC", LONG + LONG.translate(str.maketrans("abAB", "cdCD"))]
rows_all = []
for w in RELATORS:
    L = {g: [[K0] * 27 for _ in range(27)] for g in "abcd"}
    Pi = meye(27)
    for ch in w:
        g = prim[ch]
        if ch.islower():
            term = Pi
            sgn = 1
        else:
            term = mmul(Pi, lets4[ch])
            sgn = -1
        if sgn < 0:
            term = mscale(K(-1), term)
        L[g] = madd(L[g], term)
        Pi = mmul(Pi, lets4[ch])
    assert mzero_p(msub(Pi, meye(27))), "relator does not map to identity"
    for i in range(27):
        rows_all.append([L[g][i][j] for g in "abcd" for j in range(27)])
Zc = nullspace(rows_all)
log(f"  Z^1(D;27) dim = {len(Zc)} (banked: 31)")
assert len(Zc) == 31
cob = []
for j in range(27):
    v = [K1 if t == j else K0 for t in range(27)]
    entry = []
    for g in "abcd":
        gv = apply_(lets4[g], v)
        entry.extend([gv[i] - v[i] for i in range(27)])
    cob.append(entry)
reps = []
basis = [r[:] for r in cob]
for z in Zc:
    try:
        Solver(basis).coords(z)
    except ValueError:
        reps.append(z)
        basis.append(z)
        if len(reps) == 5:
            break
assert len(reps) == 5, f"only {len(reps)} independent classes"
log("  5 class representatives rebuilt (greedy, banked order)")


def sides_of(z):
    return (z[0:27], z[27:54]), (z[54:81], z[81:108])


# ---------------------------------------------------------------------------
log("STEP 2 (CONTROL G0, decisive): recompute two banked Y components "
    "through the full banked evaluator...")
side2 = Side(dict(side2lets))
MU1, LAM1, PROD1 = "a", LONG, freduce("a" + LONG)
MU2, LAM2 = "a", inv(LONG)
PROD2 = freduce("a" + inv(LONG))
BANKED = {(0, 3, 4): K(0, Fr(2, 3)),
          (1, 3, 4): K(Fr(1, 24), Fr(1, 72))}
for (i, j, k), want in BANKED.items():
    (zi1, zi2), (zj1, zj2), (zk1, zk2) = map(
        sides_of, (reps[i], reps[j], reps[k]))
    om1 = side1.make_omega(zi1, zj1, zk1)
    om2 = side2.make_omega(zi2, zj2, zk2)
    y = ((side1.S_eval(om1, MU1, LAM1, PROD1)
          - side1.S_eval(om1, LAM1, MU1, PROD1))
         - (side2.S_eval(om2, MU2, LAM2, PROD2)
            - side2.S_eval(om2, LAM2, MU2, PROD2)))
    ok = (y - want).is_zero()
    log(f"  Y[{(i,j,k)}] recomputed = {y}  banked = {want}  MATCH: {ok}")
    assert ok, "BASIS MATCH CONTROL FAILED"
log("  G0 PASS: the rebuilt basis IS the banked basis")

# ---------------------------------------------------------------------------
log("STEP 3: the coefficient system (27, 27bar, C) + gates...")
LET = dict(lets4)


def transpose(M):
    return [list(r) for r in zip(*M)]


# contragredient action: rhobar(g) = rho(g)^{-T}; rho(g)^{-1} = rho(swapcase)
DACT = {ch: transpose(lets4[ch.swapcase()]) for ch in lets4}

for x in "abcd":
    assert mzero_p(msub(mmul(lets4[x], lets4[x.upper()]), meye(27)))
    assert mzero_p(msub(mmul(DACT[x], DACT[x.upper()]), meye(27)))

MATC, DMATC = {"": meye(27)}, {"": meye(27)}


def mat(w):
    w = freduce(w)
    if w not in MATC:
        MATC[w] = mmul(mat(w[:-1]), LET[w[-1]])
    return MATC[w]


def dmat(w):
    w = freduce(w)
    if w not in DMATC:
        DMATC[w] = mmul(dmat(w[:-1]), DACT[w[-1]])
    return DMATC[w]


for w in RELATORS:
    assert mzero_p(msub(dmat(w), meye(27))), "rhobar relator gate"
log("  rhobar(relator) = I for all 4 relators")

# the Jordan cross 27 x 27 -> 27bar from the rebuilt cubic
CR = [[] for _ in range(27)]
for (p, q, r_), cval in CFULL.items():
    CR[r_].append((p, q, cval))
n_rat = all(cv.b == 0 for cv in CFULL.values())
log(f"  CFULL: {len(CFULL)} ordered entries; all rational: {n_rat}")


def cross(x, y):
    out = []
    for r_ in range(27):
        s = K0
        for (p, q, cv) in CR[r_]:
            xp = x[p]
            if xp.is_zero():
                continue
            yq = y[q]
            if yq.is_zero():
                continue
            s = s + cv * xp * yq
        out.append(s)
    return out


def dot(x, y):
    s = K0
    for t in range(27):
        xt = x[t]
        if xt.is_zero():
            continue
        yt = y[t]
        if yt.is_zero():
            continue
        s = s + xt * yt
    return s


# deterministic exact "random" vectors
def rvec(seed):
    st = seed
    out = []
    for t in range(27):
        st = (st * 1103515245 + 12345) % (1 << 31)
        out.append(K(Fr((st % 7) - 3), Fr(((st >> 8) % 5) - 2)))
    return out


# gate: equivariance of the cross for ALL 8 letters:
#   cross(rho(g)x, rho(g)y) = rhobar(g) cross(x, y)
for ch in "abcdABCD":
    for sd in (11, 29):
        x, y = rvec(sd), rvec(sd + 100)
        lhs = cross(apply_(LET[ch], x), apply_(LET[ch], y))
        rhs = apply_(DACT[ch], cross(x, y))
        assert all((lhs[t] - rhs[t]).is_zero() for t in range(27)), \
            f"cross equivariance FAILS at letter {ch}"
log("  cross equivariance PASS (8 letters x 2 seeds)")

# gate: dot invariance dot(rhobar(g)x, rho(g)y) = dot(x,y)
for ch in "abcdABCD":
    x, y = rvec(3), rvec(7)
    assert (dot(apply_(DACT[ch], x), apply_(LET[ch], y))
            - dot(x, y)).is_zero()
log("  dual dot invariance PASS")

# gate: strict associativity dot(cross(x,y),z) = dot(x, cross(y,z))
for sd in (5, 17):
    x, y, z = rvec(sd), rvec(sd + 1), rvec(sd + 2)
    assert (dot(cross(x, y), z) - dot(x, cross(y, z))).is_zero()
log("  strict associativity (N total symmetry) PASS")

# invariant vectors
rows_v0 = []
rows_v0b = []
for g in "abcd":
    for i in range(27):
        rows_v0.append([lets4[g][i][j] - (K1 if i == j else K0)
                        for j in range(27)])
        rows_v0b.append([DACT[g][i][j] - (K1 if i == j else K0)
                         for j in range(27)])
V0S = nullspace(rows_v0)
V0BS = nullspace(rows_v0b)
log(f"  h^0(D;27) = {len(V0S)} (banked 1); h^0(D;27bar) = {len(V0BS)}")
assert len(V0S) == 1 and len(V0BS) == 1
v0, v0bar = V0S[0], V0BS[0]

# ---------------------------------------------------------------------------
log("STEP 4: presentation-complex degree-2 machinery...")


def relchain(word):
    """corrected relator bar 2-chain (b637 rel_chain convention,
    generalized to the 8-letter alphabet): cells (coeffword, s1, s2, sgn)."""
    cells = []
    pre = ""
    for ch in word:
        cells.append(("", pre, ch, +1))
        if ch.isupper():
            cells.append((pre, ch, ch.lower(), -1))
        pre = freduce(pre + ch)
    return cells


RELCELLS = [relchain(w) for w in RELATORS]


def E_bar(cfun):
    """evaluate a 27bar-valued 2-cochain on the 4 relator chains ->
    flat 108-vector."""
    out = []
    for cells in RELCELLS:
        acc = [K0] * 27
        for (cw, s1, s2, sgn) in cells:
            v = cfun(s1, s2)
            if cw:
                v = apply_(dmat(cw), v)
            if sgn > 0:
                acc = [acc[t] + v[t] for t in range(27)]
            else:
                acc = [acc[t] - v[t] for t in range(27)]
        out.extend(acc)
    return out


def E_triv(cfun):
    """evaluate a C-valued 2-cochain on the 4 relator chains -> 4 scalars."""
    out = []
    for cells in RELCELLS:
        acc = K0
        for (cw, s1, s2, sgn) in cells:
            v = cfun(s1, s2)
            acc = acc + v if sgn > 0 else acc - v
        out.append(acc)
    return out


# Fox map with 27bar coefficients: LBAR[r][g] 27x27
LBAR = []
for w in RELATORS:
    L = {g: [[K0] * 27 for _ in range(27)] for g in "abcd"}
    pre = ""
    for ch in w:
        g = prim[ch]
        if ch.islower():
            L[g] = madd(L[g], dmat(pre))
        else:
            L[g] = msub(L[g], dmat(freduce(pre + ch)))
        pre = freduce(pre + ch)
    LBAR.append(L)


def phibar_apply(fgen):
    out = []
    for L in LBAR:
        acc = [K0] * 27
        for g in "abcd":
            gv = apply_(L[g], fgen[g])
            acc = [acc[t] + gv[t] for t in range(27)]
        out.extend(acc)
    return out


# trivial-coefficient Fox map (abelianized relator matrix, 4x4)
PHITRIV = []
for w in RELATORS:
    row = {g: 0 for g in "abcd"}
    for ch in w:
        row[prim[ch]] += 1 if ch.islower() else -1
    PHITRIV.append([K(row[g]) for g in "abcd"])
log(f"  PHITRIV rows (relator abelianizations): "
    f"{[[int(x.a) for x in r] for r in PHITRIV]}")

# left-null functional phi of PHITRIV: n . PHITRIV = 0 (column-wise)
nsol = nullspace([[PHITRIV[r][gi] for r in range(4)] for gi in range(4)])
assert len(nsol) == 1, f"coker H^2(Y;C) dim = {len(nsol)} != 1"
nvec = nsol[0]
for t in range(4):
    if not nvec[t].is_zero():
        nvec = [x * nvec[t].inv() for x in nvec]
        break
log(f"  phi (left-null of PHITRIV, normalized) = "
    f"{[str(x) for x in nvec]}")


def phi(e4):
    s = K0
    for t in range(4):
        if not nvec[t].is_zero():
            s = s + nvec[t] * e4[t]
    return s


def phitriv_apply(fgen4):
    return [sum((PHITRIV[r][gi] * fgen4[gi] for gi in range(4)), K0)
            for r in range(4)]


# CONTROL A (27bar): E_bar(delta f) == PHIBAR . f_gen for the NORMALIZED
# element-function f(w) = rhobar(w).xi - xi  (f(1) = 0; the machinery
# lives in the normalized bar complex, where identity-slot cells vanish
# — all pipeline cochains are normalized since u(1) = 0)
for sd in (41, 43):
    xi = rvec(sd)

    def fval(w, xi=xi):
        gv = apply_(dmat(w), xi)
        return [gv[t] - xi[t] for t in range(27)]

    def dffun(s1, s2, fval=fval):
        a = fval(s1)
        b = apply_(dmat(s1), fval(s2))
        c = fval(freduce(s1 + s2))
        return [a[t] + b[t] - c[t] for t in range(27)]

    lhs = E_bar(dffun)
    fgen = {g: fval(g) for g in "abcd"}
    rhs = phibar_apply(fgen)
    assert all((lhs[t] - rhs[t]).is_zero() for t in range(108)), \
        "CONTROL A FAILS: relator-chain vs Fox sign mismatch"
log("  CONTROL A PASS: E_bar(delta f) = PHIBAR f_gen (2 seeds)")

# CONTROL A' (trivial): tau(w) = dot(xibar, rho(w) eta) - dot(xibar, eta)
# (normalized: tau(1) = 0)
for sd in (47,):
    xib, eta = rvec(sd), rvec(sd + 9)

    def tval(w, xib=xib, eta=eta):
        return dot(xib, apply_(mat(w), eta)) - dot(xib, eta)

    def dtfun(s1, s2, tval=tval):
        return tval(s1) + tval(s2) - tval(freduce(s1 + s2))

    lhs4 = E_triv(dtfun)
    tgen = [tval(g) for g in "abcd"]
    rhs4 = phitriv_apply(tgen)
    assert all((lhs4[t] - rhs4[t]).is_zero() for t in range(4))
    assert phi(lhs4).is_zero()
log("  CONTROL A' PASS: E_triv(delta tau) = PHITRIV tau_gen; phi = 0")

# the coboundary solver over 27bar (membership + primitive extraction)
log("  building the PHIBAR column solver (108x108 exact rref)...")
cols = []
for gi, g in enumerate("abcd"):
    for j in range(27):
        col = []
        for L in LBAR:
            col.extend([L[g][i][j] for i in range(27)])
        cols.append(col)
SOLVBAR = Solver(cols)
log("  PHIBAR solver ready")

# ---------------------------------------------------------------------------
log("STEP 5: cocycle word-evaluators...")


def z4_of(z):
    return {g: z[gi * 27:(gi + 1) * 27] for gi, g in enumerate("abcd")}


UREP = [z4_of(z) for z in reps]


def make_cocycle_eval(z4, matget):
    cache = {"": [K0] * 27}

    def ev(w):
        w = freduce(w)
        if w in cache:
            return cache[w]
        w1, l = w[:-1], w[-1]
        base = ev(w1)
        if l.islower():
            add = apply_(matget(w1), z4[l])
            val = [base[t] + add[t] for t in range(27)]
        else:
            add = apply_(matget(w), z4[l.lower()])
            val = [base[t] - add[t] for t in range(27)]
        cache[w] = val
        return val
    return ev


UEV = [make_cocycle_eval(UREP[i], mat) for i in range(5)]

# H^1(D;27bar) (needed for the indeterminacy)
rows_bar = []
for L in LBAR:
    for i in range(27):
        rows_bar.append([L[g][i][j] for g in "abcd" for j in range(27)])
Zbar = nullspace(rows_bar)
cob_bar = []
for j in range(27):
    v = [K1 if t == j else K0 for t in range(27)]
    entry = []
    for g in "abcd":
        gv = apply_(DACT[g], v)
        entry.extend([gv[i] - v[i] for i in range(27)])
    cob_bar.append(entry)
reps_bar = []
basis_b = [r[:] for r in cob_bar]
for z in Zbar:
    try:
        Solver(basis_b).coords(z)
    except ValueError:
        reps_bar.append(z)
        basis_b.append(z)
        if len(reps_bar) == 5:
            break
log(f"  Z^1(D;27bar) dim = {len(Zbar)}; h^1(D;27bar) >= {len(reps_bar)} "
    f"(theta-duality expects 5)")
assert len(reps_bar) == 5
ZBEV = [make_cocycle_eval(z4_of(z), dmat) for z in reps_bar]

# kappa vector: v0bar-contraction of the five 27-classes (C-valued
# 1-cocycles; their H^1(D;C)-coordinates)
kap = []
for i in range(5):
    kv = [dot(v0bar, UREP[i][g]) for g in "abcd"]
    resid = phitriv_apply(kv)  # must satisfy the relator condition: = 0
    assert all(x.is_zero() for x in resid), "kappa not a 1-cocycle?!"
    kap.append(kv)
log("  kappa(u_i) gen-values (each a C-valued 1-cocycle):")
for i in range(5):
    log(f"    kappa(u_{i}) = {[str(x) for x in kap[i]]}")

# ---------------------------------------------------------------------------
log("STEP 6: the cup H^1 x H^1 -> H^2(D;27bar) class table (5x5)...")


def cup27(i, j):
    """(u_i cup u_j)(s1,s2) = cross(u_i(s1), rho(s1) u_j(s2)); cached."""
    cache = {}

    def c(s1, s2):
        s1, s2 = freduce(s1), freduce(s2)
        key = (s1, s2)
        if key not in cache:
            if not s1 or not s2:
                cache[key] = [K0] * 27
            else:
                cache[key] = cross(UEV[i](s1),
                                   apply_(mat(s1), UEV[j](s2)))
        return cache[key]
    return c


CUP = {}
ECUP = {}
for i in range(5):
    for j in range(5):
        CUP[(i, j)] = cup27(i, j)
        ECUP[(i, j)] = E_bar(CUP[(i, j)])

# gate: delta c = 0 on word triples (mixed sides, mixed case)
TRIPLE_WORDS = [("ab", "cA", "Db"), ("a", "bC", "dA"), ("Bc", "aD", "bd")]
for (i, j) in [(2, 3), (3, 4), (0, 1)]:
    c = CUP[(i, j)]
    for (g, h, l) in TRIPLE_WORDS:
        gh, hl = freduce(g + h), freduce(h + l)
        t1 = apply_(dmat(g), c(h, l))
        t2 = c(gh, l)
        t3 = c(g, hl)
        t4 = c(g, h)
        assert all((t1[t] - t2[t] + t3[t] - t4[t]).is_zero()
                   for t in range(27)), f"delta c != 0 at ({i},{j})"
log("  cup 2-cocycle identity delta c = 0 PASS (3 pairs x 3 word triples)")

PRIMGEN = {}
zero_class = {}
for i in range(5):
    for j in range(5):
        try:
            x = SOLVBAR.coords(ECUP[(i, j)])
            PRIMGEN[(i, j)] = {g: [x[gi * 27 + t] for t in range(27)]
                               for gi, g in enumerate("abcd")}
            zero_class[(i, j)] = True
        except ValueError:
            zero_class[(i, j)] = False
log("  27bar cup CLASS table ([u_i cup u_j] = 0 in H^2(D;27bar)?):")
for i in range(5):
    log("    " + " ".join(
        ("ZERO " if zero_class[(i, j)] else "NONZ ") for j in range(5)))

# the v0-mediated C-valued class matrix (S4 corroboration, banked basis)
MV0 = [[None] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        c = CUP[(i, j)]

        def cv0(s1, s2, c=c):
            return dot(c(s1, s2), v0)

        MV0[i][j] = phi(E_triv(cv0))
log("  v0-mediated class matrix M_ij = phi(E(dot(c_ij, v0))):")
for i in range(5):
    log("    [" + ", ".join(str(MV0[i][j]) for j in range(5)) + "]")
antis = all((MV0[i][j] + MV0[j][i]).is_zero()
            for i in range(5) for j in range(5))
solo_zero = all(MV0[i][j].is_zero() for i in (2, 3, 4) for j in (2, 3, 4))
log(f"  MV0 antisymmetric: {antis}; solo block {{2,3,4}} zero: {solo_zero}")

# ---------------------------------------------------------------------------
log("STEP 7: definedness + primitives...")
SOLO = (2, 3, 4)
defined_pairs = [(i, j) for i in range(5) for j in range(5)
                 if zero_class[(i, j)]]
log(f"  cochain-solvable pairs: {defined_pairs}")


def make_primitive_eval(agen, cfun):
    singles = {}
    for x in "abcd":
        singles[x] = agen[x]
        X = x.upper()
        v = cfun(X, x)
        wv = apply_(dmat(X), agen[x])
        singles[X] = [v[t] - wv[t] for t in range(27)]
    cache = {"": [K0] * 27}

    def ev(w):
        w = freduce(w)
        if w in cache:
            return cache[w]
        w1, l = w[:-1], w[-1]
        base = ev(w1)
        add = apply_(dmat(w1), singles[l])
        cv = cfun(w1, l)
        val = [base[t] + add[t] - cv[t] for t in range(27)]
        cache[w] = val
        return val
    return ev


AEV = {}
for (i, j) in defined_pairs:
    AEV[(i, j)] = make_primitive_eval(PRIMGEN[(i, j)], CUP[(i, j)])

# gates on the primitives (run on the solo pairs + one boundary pair)
gate_pairs = [p for p in defined_pairs
              if (p[0] in SOLO and p[1] in SOLO) or p in ((0, 1), (1, 0))]
PAIR_WORDS = [("ab", "cA"), ("dC", "ba"), ("aD", "bc"), ("Bd", "ca")]
for p in gate_pairs:
    a_ev, c = AEV[p], CUP[p]
    # (i) relator-insertion invariance (well-definedness on the group)
    for w0 in ("", "ab", "Dc"):
        for r_ in RELATORS:
            va = a_ev(freduce(w0 + r_))
            vb = a_ev(w0)
            assert all((va[t] - vb[t]).is_zero() for t in range(27)), \
                f"primitive {p} NOT well-defined (relator insertion)"
    # (ii) delta a = c on word pairs
    for (g, h) in PAIR_WORDS:
        lhs = [a_ev(g)[t] + apply_(dmat(g), a_ev(h))[t]
               - a_ev(freduce(g + h))[t] for t in range(27)]
        rhs = c(g, h)
        assert all((lhs[t] - rhs[t]).is_zero() for t in range(27)), \
            f"delta a != c at {p}"
log(f"  primitive gates PASS on {len(gate_pairs)} pairs "
    "(relator-insertion invariance + delta a = c)")

# ---------------------------------------------------------------------------
log("STEP 8: the indeterminacy pairing "
    "H^1(27bar) x H^1(27) -> H^2(D;C) (both orders)...")
PL = [[None] * 5 for _ in range(5)]   # PL[t][s] = phi(E(zbar_t cup u_s))
PR = [[None] * 5 for _ in range(5)]   # PR[s][t] = phi(E(u_s cup zbar_t))
for t in range(5):
    for s in range(5):
        zb, us = ZBEV[t], UEV[s]

        def cl(s1, s2, zb=zb, us=us):
            if not s1 or not s2:
                return K0
            return dot(zb(s1), apply_(mat(s1), us(s2)))

        def cr(s1, s2, zb=zb, us=us):
            if not s1 or not s2:
                return K0
            return dot(apply_(dmat(s1), zb(s2)), us(s1))

        PL[t][s] = phi(E_triv(cl))
        PR[s][t] = phi(E_triv(cr))
log("  PL[t][s] = phi([zbar_t cup u_s]):")
for t in range(5):
    log("    [" + ", ".join(str(PL[t][s]) for s in range(5)) + "]")
log("  PR[s][t] = phi([u_s cup zbar_t]):")
for s in range(5):
    log("    [" + ", ".join(str(PR[s][t]) for t in range(5)) + "]")
koszul_dual = all((PL[t][s] + PR[s][t]).is_zero()
                  for t in range(5) for s in range(5))
log(f"  Koszul check PL = -PR^T: {koszul_dual}")


def indet(i, k):
    """the indeterminacy K-subspace of <u_i, ., u_k>: 0 or K."""
    vals = [PL[t][k] for t in range(5)] + [PR[i][t] for t in range(5)]
    return any(not v.is_zero() for v in vals)


# ---------------------------------------------------------------------------
log("STEP 9: the triple Massey products...")


def massey_scalar(i, j, k):
    """phi(E(m)) for m = a_ij cup u_k + u_i cup b_jk  (requires both
    primitives); returns (scalar, m-function)."""
    a_ev, b_ev = AEV[(i, j)], AEV[(j, k)]
    uk, ui = UEV[k], UEV[i]
    cache = {}

    def m(s1, s2):
        s1, s2 = freduce(s1), freduce(s2)
        key = (s1, s2)
        if key not in cache:
            t1 = dot(a_ev(s1), apply_(mat(s1), uk(s2))) if s1 and s2 else K0
            t2 = dot(apply_(dmat(s1), b_ev(s2)), ui(s1)) if s2 else K0
            # note: t2 with s1 = "" is dot(b(s2), u_i("")) = 0 anyway
            cache[key] = t1 + t2
        return cache[key]
    return phi(E_triv(m)), m


results = {}
TRIPLES = [tr for tr in it.product(range(5), repeat=3)
           if all(x in SOLO for x in tr)]
TRIPLES += [(0, 1, k) for k in SOLO] + [(1, 0, k) for k in SOLO]
TRIPLES += [(k, 0, 1) for k in SOLO]
first_gate_done = False
for (i, j, k) in TRIPLES:
    if not (zero_class[(i, j)] and zero_class[(j, k)]):
        results[(i, j, k)] = ("UNDEFINED",
                              zero_class[(i, j)], zero_class[(j, k)])
        continue
    lam, mfun = massey_scalar(i, j, k)
    if not first_gate_done:
        # gate: delta m = 0 on word triples (once; the identity is
        # structural and the inputs are shared machinery)
        for (g, h, l) in TRIPLE_WORDS:
            v = (mfun(h, l) - mfun(freduce(g + h), l)
                 + mfun(g, freduce(h + l)) - mfun(g, h))
            assert v.is_zero(), "delta m != 0"
        log("  gate delta m = 0 PASS (3 word triples)")
        first_gate_done = True
    results[(i, j, k)] = ("DEFINED", lam, indet(i, k))

log("  Massey table <u_i, u_j, u_k>  (scalar = phi of the class in "
    "H^2(D;C); indet = True means indeterminacy is ALL of K):")
for tr in TRIPLES:
    r_ = results[tr]
    if r_[0] == "UNDEFINED":
        log(f"    <{tr[0]},{tr[1]},{tr[2]}> UNDEFINED "
            f"([c_ij]=0:{r_[1]}, [c_jk]=0:{r_[2]})")
    else:
        log(f"    <{tr[0]},{tr[1]},{tr[2]}> = {r_[1]}   "
            f"indeterminacy_full={r_[2]}")

# ---------------------------------------------------------------------------
log("STEP 10 (CONTROL): representative-shift invariance on one triple...")
shift_done = False
for (i, j, k) in TRIPLES:
    if results[(i, j, k)][0] != "DEFINED" or shift_done:
        continue
    if results[(i, j, k)][2]:      # indeterminacy full: skip (uninformative)
        continue
    if i in (j, k):
        # shifting u_i would also change c_jk through the shared slot;
        # keep the control's consistency simple: distinct-slot triples only
        continue
    xi = rvec(61)
    zshift = []
    for g in "abcd":
        gv = apply_(lets4[g], xi)
        zshift.append([gv[t] - xi[t] for t in range(27)])
    # u_i' = u_i + delta xi
    z4p = {g: [UREP[i][g][t] + zshift[gi][t] for t in range(27)]
           for gi, g in enumerate("abcd")}
    uev_p = make_cocycle_eval(z4p, mat)
    UEV_SAVE, UREP_SAVE = UEV[i], UREP[i]
    UEV[i], UREP[i] = uev_p, z4p
    try:
        cp_ij = cup27(i, j)
        e_ij = E_bar(cp_ij)
        xco = SOLVBAR.coords(e_ij)
        agen_p = {g: [xco[gi * 27 + t] for t in range(27)]
                  for gi, g in enumerate("abcd")}
        CUP_SAVE, PRIM_SAVE, AEV_SAVE = (CUP[(i, j)], PRIMGEN[(i, j)],
                                         AEV[(i, j)])
        CUP[(i, j)] = cp_ij
        PRIMGEN[(i, j)] = agen_p
        AEV[(i, j)] = make_primitive_eval(agen_p, cp_ij)
        lam_p, _ = massey_scalar(i, j, k)
        same = (lam_p - results[(i, j, k)][1]).is_zero()
        log(f"  representative shift u_{i} -> u_{i} + delta(xi) on "
            f"<{i},{j},{k}>: scalar {lam_p} vs {results[(i,j,k)][1]} "
            f"EQUAL: {same}")
        assert same, "representative-shift control FAILED"
        CUP[(i, j)], PRIMGEN[(i, j)], AEV[(i, j)] = (CUP_SAVE, PRIM_SAVE,
                                                     AEV_SAVE)
    finally:
        UEV[i], UREP[i] = UEV_SAVE, UREP_SAVE
    shift_done = True
if not shift_done:
    log("  (no informative defined triple for the shift control)")

# ---------------------------------------------------------------------------
log("STEP 11: shape assembly on the solo triple...")
solo_defined = [(i, j, k) for (i, j, k) in TRIPLES
                if all(x in SOLO for x in (i, j, k))
                and results[(i, j, k)][0] == "DEFINED"]
any_nonzero = any(not results[tr][1].is_zero() for tr in solo_defined)
any_meaningful_nonzero = any(
    (not results[tr][1].is_zero()) and (not results[tr][2])
    for tr in solo_defined)
log(f"  solo-triple defined products: {len(solo_defined)}; "
    f"nonzero representatives: {any_nonzero}; "
    f"nonzero AND indeterminacy-free: {any_meaningful_nonzero}")

for jmid in SOLO:
    rowsM = []
    ok = True
    for i in SOLO:
        row = []
        for k in SOLO:
            r_ = results.get((i, jmid, k))
            if r_ is None or r_[0] != "DEFINED":
                ok = False
                break
            row.append(r_[1])
        if not ok:
            break
        rowsM.append(row)
    if ok:
        log(f"  M^(j={jmid})[i][k] = <u_i, u_{jmid}, u_k> on solo x solo:")
        for row in rowsM:
            log("    [" + ", ".join(str(x) for x in row) + "]")
        if any(not x.is_zero() for row in rowsM for x in row):
            try:
                import sympy as sp
                r3 = sp.sqrt(3) * sp.I

                def tosp(x):
                    return sp.Rational(x.a) + sp.Rational(x.b) * r3

                Msp = sp.Matrix([[tosp(x) for x in row] for row in rowsM])
                cp = Msp.charpoly()
                ev = Msp.eigenvals()
                log(f"    charpoly: {sp.expand(cp.as_expr())}")
                log(f"    eigenvalues: {ev}")
            except Exception as e:            # noqa: BLE001
                log(f"    (sympy eigen analysis unavailable: {e})")
    else:
        log(f"  M^(j={jmid}): not fully defined on solo x solo")

log("CELL H COMPUTATION COMPLETE")
