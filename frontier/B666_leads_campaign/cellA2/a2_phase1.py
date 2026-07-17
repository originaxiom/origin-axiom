"""B666 CELL A' — phase 1: coefficient systems, projectors, invariant
functionals, and the exact relator-evaluations E(c) of the three
uncomputed cups on the golden double D.

  cup L : H^1(D;27) x H^1(D;27)    -> H^2(D;Lambda^2 27) = H^2(D;351)
  cup S : H^1(D;27) x H^1(D;27)    -> H^2(D;Sym^2 27); 351'-part via P_W
  cup A : H^1(D;27) x H^1(D;27bar) -> H^2(D;78)   (both slot orders)

Gates: G0 (banked-Y basis match, decisive), action-matrix bookkeeping,
pi equivariance, dual-basis duality, p78 equivariance + Ad closure,
split-Casimir minimal polynomial + U/W splitting, P_W projector axioms,
CONTROL-A sign conventions per module, 2-cocycle identity, and the
27bar-consistency gate pi(E_S)/2 == banked-machinery cross-cup E.

All arithmetic exact over K = Q(sqrt-3).  Output: checkpoint JSON.
"""
import os
import sys
import time
import json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from a2_common import load, log, kser, vser, mser   # noqa: E402

n = load(run_g0=True, need_bar=True)
K, K0, K1 = n.K, n.K0, n.K1
apply_ = n.apply
applyg = n.applyg
mat, dmat = n.mat, n.dmat
freduce = n.freduce
LT, LE = n.LT, n.LE
wedgeco, symco = n.wedgeco, n.symco
coofLam, matofLam = n.coofLam, n.matofLam
coofSym, matofSym = n.coofSym, n.matofSym
conjT, piSym = n.conjT, n.piSym
rvec = n.rvec
CKPT = os.path.join(HERE, "ckpt_phase1.json")

# ---------------------------------------------------------------------------
log("P1: module action matrices + bookkeeping gates...")
# SLam_g[m'][m] : coords of  M A_m M^T  in the Lambda basis; SSym likewise.
SLam, SSym = {}, {}
for ch in "abcdABCD":
    M = n.lets4[ch]
    colM = [[M[a][p] for a in range(27)] for p in range(27)]
    SL = [[K0] * 351 for _ in range(351)]
    for m, (p, q) in enumerate(LT):
        w = wedgeco(colM[p], colM[q])
        for mp in range(351):
            SL[mp][m] = w[mp]
    SLam[ch] = SL
    SS = [[K0] * 378 for _ in range(378)]
    for m, (p, q) in enumerate(LE):
        if p == q:
            cp = colM[p]
            w = [cp[a] * cp[b] for (a, b) in LE]
        else:
            w = symco(colM[p], colM[q])
        for mp in range(378):
            SS[mp][m] = w[mp]
    SSym[ch] = SS

for ch in "abcdABCD":
    for sd in (11, 29):
        x, y = rvec(sd), rvec(sd + 100)
        Mx = apply_(n.lets4[ch], x)
        My = apply_(n.lets4[ch], y)
        wl = applyg(SLam[ch], wedgeco(x, y))
        wr = wedgeco(Mx, My)
        assert all((wl[t] - wr[t]).is_zero() for t in range(351)), \
            f"SLam bookkeeping FAILS at {ch}"
        sl = applyg(SSym[ch], symco(x, y))
        sr = symco(Mx, My)
        assert all((sl[t] - sr[t]).is_zero() for t in range(378)), \
            f"SSym bookkeeping FAILS at {ch}"
log("  P1 PASS: SLam/SSym act as wedge/sym of the 27-action "
    "(8 letters x 2 seeds)")

# ---------------------------------------------------------------------------
log("P2: pi equivariance (Sym^2 -> 27bar)...")
for ch in "abcdABCD":
    for sd in (5, 17):
        x, y = rvec(sd), rvec(sd + 50)
        S = matofSym(symco(x, y))
        lhs = piSym(conjT(n.lets4[ch], S))
        rhs = apply_(n.DACT[ch], piSym(S))
        assert all((lhs[t] - rhs[t]).is_zero() for t in range(27)), \
            f"pi equivariance FAILS at {ch}"
log("  P2 PASS: pi(g.S) = rhobar(g) pi(S) (8 letters x 2 seeds)")

# ---------------------------------------------------------------------------
log("P3: trace form, dual basis, Ad letters, 78-pairing...")


def trAB(A, B):
    s = K0
    for a in range(27):
        Aa = A[a]
        for b in range(27):
            x = Aa[b]
            if not x.is_zero():
                y = B[b][a]
                if not y.is_zero():
                    s = s + x * y
    return s


X78 = n.E6_BASIS
G = [[trAB(X78[i], X78[j]) for j in range(78)] for i in range(78)]
aug = [G[i][:] + [K1 if j == i else K0 for j in range(78)]
       for i in range(78)]
R, piv = n.rref(aug)
assert piv == list(range(78)), "Gram matrix singular?!"
Ginv = [[R[i][78 + j] for j in range(78)] for i in range(78)]
Yd = []
for i in range(78):
    Mi = [[K0] * 27 for _ in range(27)]
    for j in range(78):
        c = Ginv[i][j]
        if not c.is_zero():
            Xj = X78[j]
            for a in range(27):
                Xja = Xj[a]
                for b in range(27):
                    if not Xja[b].is_zero():
                        Mi[a][b] = Mi[a][b] + c * Xja[b]
    Yd.append(Mi)
for i in range(0, 78, 11):
    for j in range(78):
        want = K1 if i == j else K0
        assert (trAB(Yd[i], X78[j]) - want).is_zero(), "duality FAILS"
log("  trace-form Gram inverted; tr(Yd_i X_j) = delta_ij "
    "(spot rows, all j)")


def p78(x, w):
    out = []
    for i in range(78):
        yx = apply_(Yd[i], x)
        s = K0
        for a in range(27):
            wa = w[a]
            if not wa.is_zero():
                ya = yx[a]
                if not ya.is_zero():
                    s = s + wa * ya
        out.append(s)
    return out


def ad_matrix(P, Pi, name):
    t0 = time.time()
    cols = []
    for X in X78:
        img = n.mmul(n.mmul(P, X), Pi)
        cols.append(n.E6_SOLVER.coords(n.flat(img)))
    M = [[cols[j][i] for j in range(78)] for i in range(78)]
    log(f"  Ad({name}) built ({time.time()-t0:.0f}s) [closure PASS]")
    return M


AD = {}
for ch in "abcd":
    AD[ch] = ad_matrix(n.lets4[ch], n.lets4[ch.upper()], ch)
    AD[ch.upper()] = ad_matrix(n.lets4[ch.upper()], n.lets4[ch],
                               ch.upper())
for ch in "abcd":
    P = n.mmul(AD[ch], AD[ch.upper()])
    assert all((P[i][j] - (K1 if i == j else K0)).is_zero()
               for i in range(78) for j in range(78)), "Ad inverse FAILS"
log("  Ad(g)Ad(g^-1) = I (4 letters); E6_SOLVER closure = letters are E6")

for ch in "abcdABCD":
    x, w = rvec(3), rvec(7)
    lhs = p78(apply_(n.lets4[ch], x), apply_(n.DACT[ch], w))
    rhs = applyg(AD[ch], p78(x, w))
    assert all((lhs[t] - rhs[t]).is_zero() for t in range(78)), \
        f"p78 equivariance FAILS at {ch}"
log("  P3 PASS: p78(rho x, rhobar w) = Ad p78(x, w) (8 letters)")

# Ad word cache
ADC = {"": [[K1 if i == j else K0 for j in range(78)] for i in range(78)]}


def adw(w):
    w = freduce(w)
    if w not in ADC:
        ADC[w] = n.mmul(adw(w[:-1]), AD[w[-1]])
    return ADC[w]


for w in n.RELATORS:
    Mw = adw(w)
    assert all((Mw[i][j] - (K1 if i == j else K0)).is_zero()
               for i in range(78) for j in range(78)), \
        "Ad relator gate FAILS"
log("  Ad(relator) = I at 78 (all 4 relators)")

# ---------------------------------------------------------------------------
log("P4: split Casimir on Sym^2, U (27bar summand), W = ker pi, P_W...")
XT = [n.transpose(X) for X in X78]


def C2(S):
    out = [[K0] * 27 for _ in range(27)]
    for i in range(78):
        T = n.mmul(n.mmul(Yd[i], S), XT[i])
        for a in range(27):
            Ta = T[a]
            oa = out[a]
            for b in range(27):
                if not Ta[b].is_zero():
                    oa[b] = oa[b] + Ta[b]
    return out


S0 = matofSym(symco(rvec(101), rvec(202)))
S1 = C2(S0)
assert all((S1[a][b] - S1[b][a]).is_zero()
           for a in range(27) for b in range(27)), "C2 not symmetric"
from fractions import Fraction as Fr    # noqa: E402

# --- REPAIR of the crashed slot search (a2_phase1_output.txt line 46;
# diagnosis in a2_p4_probe_output.txt): the eigenvalues are computed
# ABSTRACTLY from one exact eigenvector per summand, no generic-slot
# 2x2 solve anywhere.
# (i) lam_W: the 27 is minuscule (every weight extreme), so e_a . e_a
#     is an extreme-weight vector of the 351' summand of Sym^2 and
#     hence a C2 eigenvector; its eigenvalue is read off exactly and
#     cross-checked over three different a.
lamW_c = None
for a in (0, 13, 26):
    Eaa = [[K0] * 27 for _ in range(27)]
    Eaa[a][a] = K1
    CE = C2(Eaa)
    lam = CE[a][a]
    ok = all((CE[p][q] - (lam if (p, q) == (a, a) else K0)).is_zero()
             for p in range(27) for q in range(27))
    assert ok, f"e_{a}.e_{a} is not a C2 eigenvector"
    if lamW_c is None:
        lamW_c = lam
    else:
        assert (lam - lamW_c).is_zero(), \
            "extreme-weight eigenvalue varies with a"
log(f"  lam_W from extreme-weight squares e_a.e_a (a = 0, 13, 26): "
    f"{lamW_c}")

# (ii) lam_U: (C2 - lam_W) kills the 351' summand and scales the 27bar
#      summand U, so any nonzero image vector is a C2 eigenvector with
#      the second eigenvalue; verified exactly on all 27x27 slots.
lamU_c = None
for sd0 in (101, 307, 509):
    Sg = S0 if sd0 == 101 else matofSym(symco(rvec(sd0), rvec(sd0 + 101)))
    CSg = S1 if sd0 == 101 else C2(Sg)
    V1 = [[CSg[a][b] - lamW_c * Sg[a][b] for b in range(27)]
          for a in range(27)]
    if all(x.is_zero() for row in V1 for x in row):
        continue          # seed happened to lie in 351'; try the next
    CV = C2(V1)
    for a in range(27):
        for b in range(27):
            if not V1[a][b].is_zero():
                lamU_c = CV[a][b] * V1[a][b].inv()
                break
        if lamU_c is not None:
            break
    assert all((CV[a][b] - lamU_c * V1[a][b]).is_zero()
               for a in range(27) for b in range(27)), \
        "(C2 - lam_W) image is not a C2 eigenvector"
    break
assert lamU_c is not None, "no generic seed met the U summand"
assert not (lamU_c - lamW_c).is_zero(), "Casimir does not split Sym^2"
log(f"  lam_U from the (C2 - lam_W)-image of a generic seed: {lamU_c}")

# (iii) cross-gate: sum_i Yd_i X_i = c27 * I on the 27 (Schur scalar)
#       and lam_U = -c27/2 (split Casimir on the 27bar summand of
#       27 x 27; c(27bar) = c(27), the dual has the same Casimir).
CAS27 = [[K0] * 27 for _ in range(27)]
for i in range(78):
    T_ = n.mmul(Yd[i], X78[i])
    for a in range(27):
        Ta = T_[a]
        Ca = CAS27[a]
        for b in range(27):
            if not Ta[b].is_zero():
                Ca[b] = Ca[b] + Ta[b]
c27 = CAS27[0][0]
assert all((CAS27[a][b] - (c27 if a == b else K0)).is_zero()
           for a in range(27) for b in range(27)), "Casimir(27) not scalar"
assert (lamU_c * K(-2) - c27).is_zero(), "lam_U != -c27/2 cross-gate"
log(f"  cross-gate PASS: Casimir(27) = ({c27}) I and lam_U = -c27/2")

lam1, lam2 = lamW_c, lamU_c
al = lam1 + lam2
assert al.b == 0 and (lam1 * lam2).b == 0, \
    "unexpected sqrt(-3) part in Casimir"
log(f"  C2 eigenvalues on Sym^2: lam1 = {lam1}, lam2 = {lam2}; "
    f"minimal polynomial t^2 - ({al}) t + ({lam1 * lam2})")
for sd in (303, 404, 505):
    T = matofSym(symco(rvec(sd), rvec(sd + 1)))
    V = C2(T)
    Vm = [[V[a][b] - lam1 * T[a][b] for b in range(27)] for a in range(27)]
    W2 = C2(Vm)
    Wm = [[W2[a][b] - lam2 * Vm[a][b] for b in range(27)]
          for a in range(27)]
    assert all(x.is_zero() for row in Wm for x in row), \
        "(C2-lam1)(C2-lam2) != 0"
log("  gate PASS: (C2 - lam1)(C2 - lam2) = 0 on 3 fresh seeds")

# W = ker pi (the 351' subspace): nullspace of the 27x378 pi matrix
PIMAT = []
for r_ in range(27):
    row = [K0] * 378
    for (p, q, cv) in n.PIR[r_]:
        if p == q:
            row[n.LEIDX[(p, p)]] = row[n.LEIDX[(p, p)]] + cv
        else:
            key = (p, q) if p < q else (q, p)
            row[n.LEIDX[key]] = row[n.LEIDX[key]] + cv
    PIMAT.append(row)
WBAS = n.nullspace(PIMAT)
log(f"  W = ker(pi) dim = {len(WBAS)} (want 351)")
assert len(WBAS) == 351

# identify lam_W: C2 on a W vector
wv = WBAS[0]
Wm0 = matofSym(wv)
CW = C2(Wm0)
lamW = None
for cand in (lam1, lam2):
    diff = [[CW[a][b] - cand * Wm0[a][b] for b in range(27)]
            for a in range(27)]
    if all(x.is_zero() for row in diff for x in row):
        lamW = cand
        break
assert lamW is not None, "W vector is not a C2 eigenvector?!"
lamU = lam2 if lamW == lam1 else lam1
log(f"  lam_W (351') = {lamW}; lam_U (27bar) = {lamU}")
for wv2 in (WBAS[100], WBAS[250]):
    Wm2 = matofSym(wv2)
    CW2 = C2(Wm2)
    assert all((CW2[a][b] - lamW * Wm2[a][b]).is_zero()
               for a in range(27) for b in range(27))
log("  gate PASS: C2 = lam_W on sampled W basis vectors")

# U = im(C2 - lam_W) from pure seeds
Uco = []
sd = 900
while True:
    S = matofSym(symco(rvec(sd), rvec(sd + 7)))
    V = C2(S)
    Vm = [[V[a][b] - lamW * S[a][b] for b in range(27)]
          for a in range(27)]
    Uco.append(coofSym(Vm))
    sd += 13
    if len(Uco) >= 35:
        break
RU, pivU = n.rref(Uco)
UBAS = RU
log(f"  U = im(C2 - lam_W) dim = {len(UBAS)} (want 27)")
assert len(UBAS) == 27
UMAT = [matofSym(u) for u in UBAS]
for u in UMAT[:3]:
    CU = C2(u)
    assert all((CU[a][b] - lamU * u[a][b]).is_zero()
               for a in range(27) for b in range(27))
log("  gate PASS: C2 = lam_U on U")

# pi|U invertible: PU27[r][k] = pi(U_k)_r
PU27 = [[K0] * 27 for _ in range(27)]
for k in range(27):
    pk = piSym(UMAT[k])
    for r_ in range(27):
        PU27[r_][k] = pk[r_]
augU = [PU27[i][:] + [K1 if j == i else K0 for j in range(27)]
        for i in range(27)]
RUi, pivUi = n.rref(augU)
assert pivUi == list(range(27)), "pi|U singular"
PU27inv = [[RUi[i][27 + j] for j in range(27)] for i in range(27)]
log("  pi|U invertible (27bar summand confirmed as a complement of W)")

USOLVER = n.Solver([u[:] for u in UBAS])
for ch in "abcd":
    for k in (0, 13, 26):
        img = coofSym(conjT(n.lets4[ch], UMAT[k]))
        USOLVER.coords(img)          # ValueError => U not invariant
log("  gate PASS: letters preserve U (sampled)")


def PW(S):
    """projection of a symmetric matrix onto W = ker pi along U."""
    al_ = apply_(PU27inv, piSym(S))
    out = [row[:] for row in S]
    for k in range(27):
        c = al_[k]
        if not c.is_zero():
            Uk = UMAT[k]
            for a in range(27):
                Oa = out[a]
                Ua = Uk[a]
                for b in range(27):
                    if not Ua[b].is_zero():
                        Oa[b] = Oa[b] - c * Ua[b]
    return out


for sd in (21, 22):
    S = matofSym(symco(rvec(sd), rvec(sd + 5)))
    P1_ = PW(S)
    assert all(x.is_zero() for x in piSym(P1_)), "pi(P_W S) != 0"
    P2_ = PW(P1_)
    assert all((P1_[a][b] - P2_[a][b]).is_zero()
               for a in range(27) for b in range(27)), "P_W not idempotent"
    for ch in "abcdABCD":
        lhs = PW(conjT(n.lets4[ch], S))
        rhs = conjT(n.lets4[ch], P1_)
        assert all((lhs[a][b] - rhs[a][b]).is_zero()
                   for a in range(27) for b in range(27)), \
            f"P_W not equivariant at {ch}"
wm = matofSym(WBAS[7])
pwm = PW(wm)
assert all((wm[a][b] - pwm[a][b]).is_zero()
           for a in range(27) for b in range(27)), "P_W|W != id"
log("  P4 PASS: P_W idempotent, equivariant (8 letters x 2 seeds), "
    "pi P_W = 0, P_W|W = id")

# ---------------------------------------------------------------------------
log("P5: invariant vectors and functionals (h^0) for the three modules...")


def progressive_nullspace(cond_mats, dim):
    """joint kernel of the given dim x dim condition matrices."""
    basis = None
    for C in cond_mats:
        if basis is None:
            rows = [[C[i][j] for j in range(dim)] for i in range(dim)]
            basis = n.nullspace(rows)
        else:
            if not basis:
                return []
            imgs = [n.applyg(C, b) for b in basis]
            rows = [[imgs[j][a] for j in range(len(basis))]
                    for a in range(dim)]
            sub = n.nullspace(rows)
            basis = [[sum((sv[j] * basis[j][t] for j in range(len(basis))
                           if not sv[j].is_zero()), K0)
                      for t in range(dim)] for sv in sub]
    return basis or []


def minusI(M, dim):
    return [[M[i][j] - (K1 if i == j else K0) for j in range(dim)]
            for i in range(dim)]


def transpose_m(M):
    return [list(r) for r in zip(*M)]


h0 = {}
fun = {}
# Lambda^2 (351)
h0["lam_vec"] = progressive_nullspace(
    [minusI(SLam[g], 351) for g in "abcd"], 351)
fun["lam"] = progressive_nullspace(
    [minusI(transpose_m(SLam[g]), 351) for g in "abcd"], 351)
log(f"  h^0(D;Lambda^2 27) = {len(h0['lam_vec'])}; "
    f"invariant functionals on Lambda^2: {len(fun['lam'])}")
# Sym^2 (378)
h0["sym_vec"] = progressive_nullspace(
    [minusI(SSym[g], 378) for g in "abcd"], 378)
fun["sym"] = progressive_nullspace(
    [minusI(transpose_m(SSym[g]), 378) for g in "abcd"], 378)
log(f"  h^0(D;Sym^2 27) = {len(h0['sym_vec'])}; "
    f"invariant functionals on Sym^2: {len(fun['sym'])}")
# Sym^2 functionals killing U (= functionals of the 351' component)
fun351p = []
if fun["sym"]:
    rows = [[sum((f[m] * UBAS[k][m] for m in range(378)
                  if not f[m].is_zero()), K0) for f in fun["sym"]]
            for k in range(27)]
    sub = n.nullspace(rows)
    for sv in sub:
        fun351p.append([sum((sv[j] * fun["sym"][j][t]
                             for j in range(len(fun["sym"]))
                             if not sv[j].is_zero()), K0)
                        for t in range(378)])
fun["sym351p"] = fun351p
log(f"  invariant Sym^2 functionals killing U (351'-functionals): "
    f"{len(fun351p)}")
# 78
h0["ad_vec"] = progressive_nullspace(
    [minusI(AD[g], 78) for g in "abcd"], 78)
fun["ad"] = progressive_nullspace(
    [minusI(transpose_m(AD[g]), 78) for g in "abcd"], 78)
log(f"  h^0(D;78) = {len(h0['ad_vec'])}; "
    f"invariant functionals on 78: {len(fun['ad'])}")

# re-verify each functional exactly on 2 random vectors x 4 letters
for kind, dim, act in (("lam", 351, SLam), ("sym", 378, SSym),
                       ("ad", 78, AD)):
    for f in fun[kind]:
        for g in "abcd":
            for sd in (31,):
                v = [K((sd * (t + 3)) % 5 - 2, (sd * (t + 1)) % 3 - 1)
                     for t in range(dim)]
                gv = applyg(act[g], v)
                s1 = sum((f[t] * gv[t] for t in range(dim)
                          if not f[t].is_zero()), K0)
                s2 = sum((f[t] * v[t] for t in range(dim)
                          if not f[t].is_zero()), K0)
                assert (s1 - s2).is_zero(), f"functional gate FAILS {kind}"
log("  P5 PASS: functionals re-verified (f o rho(g) = f)")

# ---------------------------------------------------------------------------
log("P6: CONTROL-A sign conventions per module (E_M(delta f) = Fox f)...")


def E_mod(cval, act, dim):
    """evaluate a module-valued 2-cochain on the 4 relator chains.
    cval(s1, s2) -> coords; act(w, coords) -> coords."""
    out = []
    for cells in n.RELCELLS:
        acc = [K0] * dim
        for (cw, s1, s2, sgn) in cells:
            v = cval(s1, s2)
            if cw:
                v = act(cw, v)
            if sgn > 0:
                acc = [acc[t] + v[t] for t in range(dim)]
            else:
                acc = [acc[t] - v[t] for t in range(dim)]
        out.extend(acc)
    return out


def act_lam(w, co):
    M = mat(w)
    return coofLam(conjT(M, matofLam(co)))


def act_sym(w, co):
    M = mat(w)
    return coofSym(conjT(M, matofSym(co)))


def act_ad(w, co):
    return applyg(adw(w), co)


def fox_apply(fgen, act, dim):
    """PHI_M f_gen via the position lists (no big matrices)."""
    out = []
    for r in range(4):
        acc = [K0] * dim
        for g in "abcd":
            fg = fgen[g]
            for (w, sgn) in n.POSLIST[r][g]:
                v = act(w, fg) if w else fg[:]
                if sgn > 0:
                    acc = [acc[t] + v[t] for t in range(dim)]
                else:
                    acc = [acc[t] - v[t] for t in range(dim)]
        out.extend(acc)
    return out


for kind, act, dim, mkxi in (
        ("lam", act_lam, 351,
         lambda sd: [a + b for a, b in
                     zip(wedgeco(rvec(sd), rvec(sd + 2)),
                         wedgeco(rvec(sd + 4), rvec(sd + 6)))]),
        ("sym", act_sym, 378,
         lambda sd: [a + b for a, b in
                     zip(symco(rvec(sd), rvec(sd + 2)),
                         symco(rvec(sd + 4), rvec(sd + 6)))]),
        ("ad", act_ad, 78,
         lambda sd: p78(rvec(sd), rvec(sd + 2)))):
    for sd in (41, 43):
        xi = mkxi(sd)

        def fval(w, xi=xi, act=act):
            gv = act(w, xi) if w else xi[:]
            return [gv[t] - xi[t] for t in range(len(xi))]

        def dffun(s1, s2, fval=fval, act=act):
            a_ = fval(s1)
            b_ = act(s1, fval(s2)) if s1 else fval(s2)
            c_ = fval(freduce(s1 + s2))
            return [a_[t] + b_[t] - c_[t] for t in range(len(a_))]

        lhs = E_mod(dffun, act, dim)
        fgen = {g: fval(g) for g in "abcd"}
        rhs = fox_apply(fgen, act, dim)
        assert all((lhs[t] - rhs[t]).is_zero() for t in range(4 * dim)), \
            f"CONTROL A FAILS for module {kind}"
    log(f"  CONTROL A PASS [{kind}]: E(delta f) = PHI f_gen (2 seeds)")

# ---------------------------------------------------------------------------
log("P7: the cup values + exact relator evaluations E(c)...")
UEV, ZBEV = n.UEV, n.ZBEV


def cup_pure(i, j):
    """(u_i cup u_j)(s1,s2) -> pure pair (x, y), value = pairing(x, y)."""
    cache = {}

    def c(s1, s2):
        s1, s2 = freduce(s1), freduce(s2)
        key = (s1, s2)
        if key not in cache:
            if not s1 or not s2:
                cache[key] = None
            else:
                cache[key] = (UEV[i](s1), apply_(mat(s1), UEV[j](s2)))
        return cache[key]
    return c


def cup78_pure(i, t, order):
    """order 'ub': u_i cup zbar_t (27 x 27bar); order 'bu': zbar_t cup u_i."""
    cache = {}

    def c(s1, s2):
        s1, s2 = freduce(s1), freduce(s2)
        key = (s1, s2)
        if key not in cache:
            if not s1 or not s2:
                cache[key] = None
            elif order == "ub":
                cache[key] = (UEV[i](s1), apply_(dmat(s1), ZBEV[t](s2)))
            else:
                cache[key] = (apply_(mat(s1), UEV[i](s2)), ZBEV[t](s1))
        return cache[key]
    return c


def fdot(f, v, dim):
    return sum((f[t] * v[t] for t in range(dim)
                if not f[t].is_zero()), K0)


def E_and_med_matrix(cfun, kind, funcs):
    """E(c) stacked exactly + mediated H^2(D;C) scalars phi(E(f o c))
    per invariant functional (f(rho(cw)v) = f(v): transport dropped).
    kind in {'lam','sym','pw'}."""
    dim = 351 if kind == "lam" else 378
    E = []
    med4 = [[] for _ in funcs]
    for cells in n.RELCELLS:
        acc = [K0] * dim
        macc = [K0] * len(funcs)
        for (cw, s1, s2, sgn) in cells:
            pv = cfun(s1, s2)
            if pv is None:
                continue
            x, y = pv
            if kind == "lam":
                raw = wedgeco(x, y)
            else:
                raw = symco(x, y)
            if kind == "pw":
                raw = coofSym(PW(matofSym(raw)))
            for fi, f in enumerate(funcs):
                s = fdot(f, raw, dim)
                macc[fi] = macc[fi] + s if sgn > 0 else macc[fi] - s
            if cw:
                M = mat(cw)
                if kind == "lam":
                    v = coofLam(conjT(M, matofLam(raw)))
                else:
                    v = coofSym(conjT(M, matofSym(raw)))
            else:
                v = raw
            if sgn > 0:
                acc = [acc[t] + v[t] for t in range(dim)]
            else:
                acc = [acc[t] - v[t] for t in range(dim)]
        E.extend(acc)
        for fi in range(len(funcs)):
            med4[fi].append(macc[fi])
    return E, [n.phi(e4) for e4 in med4]


def E_and_med_78(cfun, funcs):
    E = []
    med4 = [[] for _ in funcs]
    for cells in n.RELCELLS:
        acc = [K0] * 78
        macc = [K0] * len(funcs)
        for (cw, s1, s2, sgn) in cells:
            pv = cfun(s1, s2)
            if pv is None:
                continue
            x, w = pv
            raw = p78(x, w)
            for fi, f in enumerate(funcs):
                s = fdot(f, raw, 78)
                macc[fi] = macc[fi] + s if sgn > 0 else macc[fi] - s
            if cw:
                xx = apply_(mat(cw), x)
                ww = apply_(dmat(cw), w)
                v = p78(xx, ww)
            else:
                v = raw
            if sgn > 0:
                acc = [acc[t] + v[t] for t in range(78)]
            else:
                acc = [acc[t] - v[t] for t in range(78)]
        E.extend(acc)
        for fi in range(len(funcs)):
            med4[fi].append(macc[fi])
    return E, [n.phi(e4) for e4 in med4]


# 2-cocycle identity gate (matrix-valued): delta c = 0 on word triples
TRIPLE_WORDS = [("ab", "cA", "Db"), ("a", "bC", "dA"), ("Bc", "aD", "bd")]
for (i, j) in [(2, 3), (3, 4), (2, 2)]:
    c = cup_pure(i, j)
    for (g, h, l_) in TRIPLE_WORDS:
        gh, hl = freduce(g + h), freduce(h + l_)

        def co_of(s1, s2):
            pv = c(s1, s2)
            return wedgeco(*pv) if pv else [K0] * 351

        t1 = act_lam(g, co_of(h, l_))
        t2 = co_of(gh, l_)
        t3 = co_of(g, hl)
        t4 = co_of(g, h)
        assert all((t1[t] - t2[t] + t3[t] - t4[t]).is_zero()
                   for t in range(351)), f"delta c != 0 (lam) at ({i},{j})"
log("  gate PASS: Lambda-cup 2-cocycle identity (3 pairs x 3 triples)")
for (i, t_) in [(2, 3), (4, 0)]:
    c = cup78_pure(i, t_, "ub")
    for (g, h, l_) in TRIPLE_WORDS:
        gh, hl = freduce(g + h), freduce(h + l_)

        def co_of(s1, s2):
            pv = c(s1, s2)
            return p78(*pv) if pv else [K0] * 78

        t1 = act_ad(g, co_of(h, l_))
        t2 = co_of(gh, l_)
        t3 = co_of(g, hl)
        t4 = co_of(g, h)
        assert all((t1[x] - t2[x] + t3[x] - t4[x]).is_zero()
                   for x in range(78)), f"delta c != 0 (78) at ({i},{t_})"
log("  gate PASS: 78-cup 2-cocycle identity (2 pairs x 3 triples)")

E_LAM, E_SYM, E_PW = {}, {}, {}
MEDV = {}
t0 = time.time()
for i in range(5):
    for j in range(5):
        c = cup_pure(i, j)
        E_LAM[(i, j)], ml = E_and_med_matrix(c, "lam", fun["lam"])
        E_SYM[(i, j)], ms = E_and_med_matrix(c, "sym", fun["sym"])
        E_PW[(i, j)], mp = E_and_med_matrix(c, "pw", fun["sym351p"])
        for fi, v in enumerate(ml):
            MEDV.setdefault(f"lam_f{fi}", {})[(i, j)] = v
        for fi, v in enumerate(ms):
            MEDV.setdefault(f"sym_f{fi}", {})[(i, j)] = v
        for fi, v in enumerate(mp):
            MEDV.setdefault(f"pw_f{fi}", {})[(i, j)] = v
log(f"  E vectors (lam, sym, pw) for 25 pairs ({time.time()-t0:.0f}s)")
E_78 = {}
t0 = time.time()
for i in range(5):
    for t_ in range(5):
        E_78[("ub", i, t_)], mu = E_and_med_78(
            cup78_pure(i, t_, "ub"), fun["ad"])
        E_78[("bu", t_, i)], mb = E_and_med_78(
            cup78_pure(i, t_, "bu"), fun["ad"])
        for fi, v in enumerate(mu):
            MEDV.setdefault(f"ad_f{fi}", {})[("ub", i, t_)] = v
        for fi, v in enumerate(mb):
            MEDV.setdefault(f"ad_f{fi}", {})[("bu", t_, i)] = v
log(f"  E vectors (78, both orders) for 25+25 pairs "
    f"({time.time()-t0:.0f}s)")

# ---------------------------------------------------------------------------
log("P8: 27bar consistency gate: pi(E_SYM)/2 == banked cross-cup E...")
CR = [[] for _ in range(27)]
for (p, q, r_), cval in n.CFULL.items():
    CR[r_].append((p, q, cval))


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


def E_bar_cross(i, j):
    out = []
    for cells in n.RELCELLS:
        acc = [K0] * 27
        for (cw, s1, s2, sgn) in cells:
            if not s1 or not s2:
                v = [K0] * 27
            else:
                v = cross(UEV[i](s1), apply_(mat(s1), UEV[j](s2)))
                if cw:
                    v = apply_(dmat(cw), v)
            if sgn > 0:
                acc = [acc[t] + v[t] for t in range(27)]
            else:
                acc = [acc[t] - v[t] for t in range(27)]
        out.extend(acc)
    return out


half = K(Fr(1, 2))
for (i, j) in [(0, 1), (2, 3), (3, 4), (2, 2), (4, 4)]:
    ec = E_bar_cross(i, j)
    es = E_SYM[(i, j)]
    for r in range(4):
        Sblk = matofSym(es[r * 378:(r + 1) * 378])
        pi_blk = [half * v for v in piSym(Sblk)]
        assert all((pi_blk[t] - ec[r * 27 + t]).is_zero()
                   for t in range(27)), f"pi(E_SYM)/2 mismatch at ({i},{j})"
log("  P8 PASS: pi(E_SYM)/2 = banked-machinery cross-cup E (5 pairs)")

# banked 27bar class-table regression (cellH SOLVBAR pattern)
cols = []
for gi, g in enumerate("abcd"):
    for jj in range(27):
        col = []
        for L in n.LBAR:
            col.extend([L[g][ii][jj] for ii in range(27)])
        cols.append(col)
SOLVBAR = n.Solver(cols)
BANKED27 = [[True, True, False, False, False],
            [True, True, False, False, False],
            [False, False, True, False, False],
            [False, False, False, True, False],
            [False, False, False, False, True]]
for i in range(5):
    for j in range(5):
        ec = E_bar_cross(i, j)
        try:
            SOLVBAR.coords(ec)
            iszero = True
        except ValueError:
            iszero = False
        assert iszero == BANKED27[i][j], \
            f"banked 27bar table regression FAILS at ({i},{j})"
log("  P8 PASS: banked 27bar cup class table reproduced (25 pairs)")

# ---------------------------------------------------------------------------
log("P9: mediated class tables (invariant functionals -> H^2(D;C))...")
MED = MEDV
for name, tab in MED.items():
    log(f"  mediated table [{name}]:")
    if name.startswith("ad"):
        for order in ("ub", "bu"):
            for a in range(5):
                row = [str(tab[k]) for k in sorted(tab)
                       if k[0] == order and k[1] == a]
                log(f"    {order}[{a}] = [" + ", ".join(row) + "]")
    else:
        for i in range(5):
            log("    [" + ", ".join(str(tab[(i, j)])
                                    for j in range(5)) + "]")
if not MED:
    log("  (no invariant functionals on any module: no mediated tables)")

# ---------------------------------------------------------------------------
log("P10: checkpoint dump...")
ck = {
    "E_LAM": {f"{i},{j}": vser(E_LAM[(i, j)])
              for i in range(5) for j in range(5)},
    "E_SYM": {f"{i},{j}": vser(E_SYM[(i, j)])
              for i in range(5) for j in range(5)},
    "E_PW": {f"{i},{j}": vser(E_PW[(i, j)])
             for i in range(5) for j in range(5)},
    "E_78": {f"{k[0]},{k[1]},{k[2]}": vser(v) for k, v in E_78.items()},
    "UBAS": [vser(u) for u in UBAS],
    "PU27inv": mser(PU27inv),
    "lamW": kser(lamW), "lamU": kser(lamU),
    "h0_dims": {k: len(v) for k, v in h0.items()},
    "fun_dims": {k: len(v) for k, v in fun.items()},
    "fun": {k: [vser(f) for f in v] for k, v in fun.items()},
    "h0_vecs": {k: [vser(f) for f in v] for k, v in h0.items()},
    "AD": {ch: mser(AD[ch]) for ch in "abcdABCD"},
    "mediated": {name: {f"{k}": kser(v) for k, v in tab.items()}
                 for name, tab in MED.items()},
}
with open(CKPT, "w") as fh:
    json.dump(ck, fh)
log(f"checkpoint written: {CKPT} ({os.path.getsize(CKPT)//1024} KB)")
log("PHASE 1 COMPLETE")
