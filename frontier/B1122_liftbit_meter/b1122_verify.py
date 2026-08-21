#!/usr/bin/env python3
"""
L179 -- THE LIFT-BIT METER.  Is the relative spin lift (the Z/2 spin-structure
choice, B1112) pair-measurable by seam-word traces on the mirror double, the way
the theta-odd dial t is (the t-meter, B1113)?

THE TWO BANKED FACTS UNDER BRIDGE-TEST
  (1) B1112 (projective hatch): the object's holonomy is PSL(2,C); the SL(2,C)
      lift is a spin-structure CHOICE, H^1(M;Z/2)=Z/2, the two lifts differing by
      the sign character chi: pi_1 -> {+-1}.  On a rep phi, the lift is INVISIBLE
      iff phi kills -I iff every sl2-weight of the holonomy is EVEN.  The PRINCIPAL
      embedding (the object's own 27) is EVEN.
  (2) B1113 (t-meter): free data of ONE object (the dial t) -- undefinable on one
      closed copy (B1087, by non-commutativity of the charge H with the peripheral
      holonomies) -- becomes FORCED class-function data of the COUPLED PAIR:
      tr(B_L . B_R(t)) and tr([B_L,B_R]) separate all four dial values, while
      tr(A . B_R(t)) is dial-blind (A = the seam meridian, centralized by the dial).

THE QUESTION: does "free-of-one = forced-of-pair" hold for the LIFT BIT too?

METHOD (built on the SAME machinery the t-meter used):
  * field Q(q), q^2 = q - 1 (primitive 6th root of unity); exact Fraction pairs.
  * the vendored, sha256-provenanced E6 Chevalley module (repo B1102 bank).
  * principal sl2 (e,h,f) + the 27 (crystal of omega_1) + Riley generators
    A27 = exp(rho(e)) = rho(a), B27 = exp(q.rho(f)) = rho(b) -- reproduces the
    t-meter's operators, and reproduces its dial-blind NUMBER (positive control).
  * the sign operator S_R := phi_R(-I) of a rep R, which is exactly
    diag((-1)^weight) in the sl2-weight basis: S is the whole content of the lift.
    lift_-(g) = chi(g) . lift_+(g) on the group, so on the rep the nontrivial lift
    multiplies each generator by S (chi(a)=chi(b)=-1, a~b in H_1=Z).
  * THREE reps, spanning even and odd:
      - the 2-dim SL(2,C) Riley rep (Sym^1, ODD): S = -I; the raw holonomy, where
        the lift literally lives (tr(meridian) = +-2).
      - the principal 27 (Sym^16 + Sym^8 + Sym^0, EVEN): S = I; the OBJECT'S OWN rep.
      - a single-simple-root sl2 on the 27 (minuscule => weights in {-1,0,+1}, ODD):
        S = diag(+-1), a genuine mixed sign -- an odd E6 embedding (cf. B1112's A1
        landing "needs the lift"), to show the odd-rep story is not special to 2-dim.
  * for each rep, SINGLE-COPY (does a trace see the lift?) and the PAIR/SEAM test
    (reference = same lift both copies vs. opposite lift; three seam traces).

PATHS: repo-relative.  The E6 module is located by walking up from CWD (and via
env L179_REPO_ROOT) looking for frontier/B1102_exact_hypercharge_solve/...; no
machine path is baked into the logic.  The repo is read-only and never written.
"""
import os
import sys
import time
import json
import importlib.util
from fractions import Fraction as F

import sympy as sp

T0 = time.time()


def say(msg):
    print(f"[{time.time()-T0:7.2f}s] {msg}")


# --------------------------------------------------------------------------
# 0. locate the repo's vendored E6 module -- machine-independent
# --------------------------------------------------------------------------
REL_CCB = "frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py"


def find_ccb():
    cands = []
    env = os.environ.get("L179_REPO_ROOT")
    if env:
        cands.append(env)
    d = os.path.abspath(os.getcwd())
    while True:
        cands.append(d)
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    # also the directory this script lives in, walking up
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        cands.append(d)
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    for c in cands:
        p = os.path.join(c, REL_CCB)
        if os.path.exists(p):
            return p
    sys.exit(
        "Cannot find the E6 module.  Set L179_REPO_ROOT to the origin-axiom "
        f"checkout root (expected {REL_CCB} beneath it)."
    )


CCB_PATH = find_ccb()


def load_ccb():
    spec = importlib.util.spec_from_file_location("ccb", CCB_PATH)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# --------------------------------------------------------------------------
# 1. field Q(q), q^2 = q - 1  (elements: Fraction pairs (x,y) = x + y*q)
# --------------------------------------------------------------------------
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
QQ = (F(0), F(1))          # q
NEG1 = (F(-1), F(0))


def fadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def fsub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def fneg(u):
    return (-u[0], -u[1])


def fmul(u, v):
    a = u[0] * v[0]
    b = u[0] * v[1] + u[1] * v[0]
    c = u[1] * v[1]
    return (a - c, b + c)          # uses q^2 = q - 1


def finv(u):
    x, y = u
    n = x * x + x * y + y * y      # norm form (disc -3), positive definite
    return ((x + y) / n, -y / n)


def frat(r):
    return (F(r), F(0))


def ffmt(u):
    x, y = u
    if y == 0:
        return str(x)
    if x == 0:
        return f"{y}q" if y != 1 else "q"
    sign = "+" if y > 0 else "-"
    ay = abs(y)
    yterm = "q" if ay == 1 else f"{ay}q"
    return f"{x}{sign}{yterm}"


# --------------------------------------------------------------------------
# 2. dense matrices over the field
# --------------------------------------------------------------------------
def meye(n):
    M = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = ONE
    return M


def mscalar(n, s):
    M = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = s
    return M


def mmul(A, B):
    n = len(A)
    k = len(B)
    m = len(B[0])
    C = [[ZERO] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for t in range(k):
            a = Ai[t]
            if a == ZERO:
                continue
            Bt = B[t]
            Ci = C[i]
            for j in range(m):
                if Bt[j] != ZERO:
                    Ci[j] = fadd(Ci[j], fmul(a, Bt[j]))
    return C


def madd(A, B):
    return [[fadd(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]


def msub(A, B):
    return [[fsub(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]


def meq(A, B):
    return all(a == b for r1, r2 in zip(A, B) for a, b in zip(r1, r2))


def mtrace(A):
    t = ZERO
    for i in range(len(A)):
        t = fadd(t, A[i][i])
    return t


def toF(Mq):
    return [[(v, F(0)) for v in row] for row in Mq]


def nilexp(Mp, scale):
    """exp(scale . Mp) for Mp nilpotent, exact truncating power series."""
    n = len(Mp)
    out = meye(n)
    P = meye(n)
    fact = F(1)
    sc = ONE
    for k in range(1, 80):
        P = mmul(P, Mp)
        fact *= k
        sc = fmul(sc, scale)
        if all(x == ZERO for row in P for x in row):
            break
        coef = fmul(sc, finv((fact, F(0))))
        out = madd(out, [[fmul(coef, xx) for xx in row] for row in P])
    return out


def word(letters, dd):
    M = meye(len(dd['a']))
    for ch in letters:
        M = mmul(M, dd[ch])
    return M


def minv2(M):
    """inverse of a 2x2 field matrix (used for the 2-dim rep only)."""
    a, b = M[0]
    c, d = M[1]
    det = fsub(fmul(a, d), fmul(b, c))
    di = finv(det)
    return [[fmul(di, d), fmul(di, fneg(b))],
            [fmul(di, fneg(c)), fmul(di, a)]]


# ==========================================================================
# STAGE 0-1: e6, principal sl2, the 27, rho27  (t-meter machinery, verbatim)
# ==========================================================================
say(f"loading E6 Chevalley module: {CCB_PATH}")
ccb = load_ccb()
br, add_, smul_, is_zero = ccb.br, ccb.add, ccb.smul, ccb.is_zero
evec, hvec, eps, ip = ccb.evec, ccb.hvec, ccb.eps, ccb.ip
ROOTS, IDX, N, DIM = ccb.ROOTS, ccb.IDX, ccb.N, ccb.DIM
assert len(ROOTS) == 72 and DIM == 78, "E6 shape mismatch"
say(f"E6 loaded: {len(ROOTS)} roots, dim {DIM}")

simple6 = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
Cart = sp.Matrix(N, N, lambda i, j: ip(simple6[i], simple6[j]))
hcoef = Cart.solve(sp.Matrix([2] * N))
e6h = [F(0)] * DIM
for j in range(N):
    e6h[j] = F(int(hcoef[j]))
e6e = [F(0)] * DIM
for i in range(N):
    e6e[N + IDX[simple6[i]]] = F(1)
e6f = [F(0)] * DIM
for j in range(N):
    neg = tuple(-1 if i2 == j else 0 for i2 in range(N))
    e6f[N + IDX[neg]] = e6h[j] / F(eps(simple6[j], neg))
assert br(e6e, e6f) == e6h, "principal sl2 triple failed"
say("principal sl2 (e,h,f) built: [e,f]=h  PASS")

# the 27 (crystal of omega_1)
Msys = sp.Matrix(N, N, lambda i, j: ip(simple6[i], simple6[j]))
w1 = Msys.solve(sp.Matrix([1, 0, 0, 0, 0, 0]))
omega1 = tuple(sp.Rational(w1[k]) for k in range(N))


def tadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def tsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def ipr(a, b):
    return sum(a[i] * b[j] * Msys[i, j] for i in range(N) for j in range(N))


weights = [omega1]
seen = {omega1}
queue = [omega1]
while queue:
    lam = queue.pop()
    for al in simple6:
        if ipr(lam, al) == 1:
            mu = tsub(lam, al)
            if mu not in seen:
                seen.add(mu)
                weights.append(mu)
                queue.append(mu)
assert len(weights) == 27, f"expected 27 weights, got {len(weights)}"
WIDX = {w: i for i, w in enumerate(weights)}
qlat = {w: tuple(int(x) for x in tsub(w, omega1)) for w in weights}
say("the 27 built (crystal of omega_1)  PASS")


def act_root(r):
    out = {}
    for w in weights:
        tgt = tadd(w, r)
        if tgt in WIDX:
            out[WIDX[w]] = (WIDX[tgt], F(eps(r, qlat[w])))
    return out


ROOTACT = {r: act_root(r) for r in ROOTS}
CJ = []
for j in range(N):
    vals = sp.Matrix([[br(hvec(j), evec(al))[N + IDX[al]] for al in simple6]])
    CJ.append([sp.Rational(vals[0, k]) for k in range(N)])


def cartan_eig(j, lam):
    return sum(sp.Rational(CJ[j][k]) * sp.Rational(lam[k]) for k in range(N))


def rho27_Q(vec):
    Mq = [[F(0)] * 27 for _ in range(27)]
    for j in range(N):
        if vec[j]:
            for w in weights:
                ev = cartan_eig(j, w)
                if ev:
                    i2 = WIDX[w]
                    Mq[i2][i2] += vec[j] * F(sp.Rational(ev).p, sp.Rational(ev).q)
    for r in ROOTS:
        c = vec[N + IDX[r]]
        if c:
            for col, (row, s) in ROOTACT[r].items():
                Mq[row][col] += c * s
    return Mq


def highest_vector(n):
    cands = [r for r in ROOTS if br(e6h, evec(r))[N + IDX[r]] == n]
    for r in cands:
        v = evec(r)
        if is_zero(br(e6e, v)):
            return v
    cols = [evec(r) for r in cands]
    Mx = sp.zeros(DIM, len(cols))
    for j, c in enumerate(cols):
        img = br(e6e, c)
        for i2, val in enumerate(img):
            Mx[i2, j] = sp.Rational(val.numerator, val.denominator)
    ns = Mx.nullspace()
    vec = ns[0]
    out = [F(0)] * DIM
    for j, c in enumerate(cols):
        coef = sp.Rational(vec[j])
        if coef:
            out = add_(out, smul_(F(coef.p, coef.q), c))
    return out


# principal Riley generators on the 27
E27p = toF(rho27_Q(e6e))
F27p = toF(rho27_Q(e6f))
A27 = nilexp(E27p, ONE)
B27 = nilexp(F27p, QQ)
A27i = nilexp(E27p, fneg(ONE))
B27i = nilexp(F27p, fneg(QQ))
d27 = {'a': A27, 'A': A27i, 'b': B27, 'B': B27i}
say("principal Riley generators A27, B27 on the 27 built  PASS")

RELATOR = 'abABaBAbaB'   # a.w.B.w^-1, w = bABa
results = {"id": "L179", "field": "Q(q)/(q^2-q+1); pairs (x,y)=x+y*q"}
controls = {}

# ==========================================================================
# CONTROL A -- reproduce a B1113 t-meter NUMBER (positive control the machinery)
#   tr(A27.B27) = 141750 + 1011915 q  (the dial-blind value, t-independent);
#   verified dial-blind at a nontrivial dial D(1)=exp(rho(x8)); t=0 sharp = 27.
# ==========================================================================
X8 = highest_vector(8)
X8p = toF(rho27_Q(X8))
D1 = nilexp(X8p, ONE)
D1i = nilexp(X8p, fneg(ONE))
BR1 = mmul(mmul(D1, B27), D1i)              # B_R(t=1) = D.B27.D^-1
trA_B27 = mtrace(mmul(A27, B27))
trA_BR1 = mtrace(mmul(A27, BR1))
DIALBLIND_NUM = (F(141750), F(1011915))
ctrlA_num = (trA_B27 == DIALBLIND_NUM)
ctrlA_blind = (trA_BR1 == trA_B27)          # dial-blind: same at t=1 as t=0
ctrlA_t0 = (mtrace(mmul(B27, B27)) == frat(27))   # tr(B_L.B_R)|t=0 = dim
# the dial genuinely twists the interior generator but NOT the seam (the whole
# mechanism): D centralizes A27 but NOT B27.
dial_centralizes_A = meq(mmul(D1, A27), mmul(A27, D1))
dial_centralizes_B = meq(mmul(D1, B27), mmul(B27, D1))
controls["A_reproduce_b1113_dialblind_number"] = {
    "tr_A27_B27": ffmt(trA_B27),
    "equals_141750+1011915q": ctrlA_num,
    "dial_blind_tr_A_BR_t1_equals_t0": ctrlA_blind,
    "t0_sharp_tr_BL_BR_equals_27": ctrlA_t0,
    "dial_centralizes_seam_A": dial_centralizes_A,
    "dial_centralizes_interior_B_(must_be_False)": dial_centralizes_B,
}
say(f"CONTROL A: tr(A27.B27) = {ffmt(trA_B27)}  == 141750+1011915q: {ctrlA_num}; "
    f"dial-blind: {ctrlA_blind}; t0=27: {ctrlA_t0}; "
    f"dial centralizes A/B = {dial_centralizes_A}/{dial_centralizes_B}")

# ==========================================================================
# CONTROL B -- rho27 is a genuine Lie-algebra representation (Chevalley brackets)
# ==========================================================================
import itertools


def matQ_mul(A, B):
    n = len(A)
    C = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        for t in range(n):
            a = A[i][t]
            if a:
                Bt = B[t]
                Ci = C[i]
                for j in range(n):
                    if Bt[j]:
                        Ci[j] += a * Bt[j]
    return C


def matQ_sub(A, B):
    return [[x - y for x, y in zip(r, s)] for r, s in zip(A, B)]


basis_ad = [hvec(j) for j in range(N)] + [evec(r) for r in ROOTS]
say(f"CONTROL B: verifying rho27 respects all C({len(basis_ad)},2) Chevalley brackets ...")
RHO = [rho27_Q(v) for v in basis_ad]
fails = 0
for (i2, j2) in itertools.combinations(range(len(basis_ad)), 2):
    lhs = rho27_Q(br(basis_ad[i2], basis_ad[j2]))
    rhs = matQ_sub(matQ_mul(RHO[i2], RHO[j2]), matQ_mul(RHO[j2], RHO[i2]))
    if lhs != rhs:
        fails += 1
ctrlB = (fails == 0)
controls["B_rho27_is_a_representation_all_3003_brackets"] = ctrlB
say(f"CONTROL B: rho27 respects all Chevalley brackets: {'PASS' if ctrlB else f'FAIL({fails})'}")

# ==========================================================================
# STAGE 2 -- the sign operator S = phi(-I) of a rep.
#   -I = exp(i.pi.H) with H the sl2 Cartan, so phi(-I) = diag((-1)^weight) in the
#   sl2-weight basis.  For a CARTAN element h, rho(h) is diagonal; S = diag of
#   (-1)^(diagonal entry).  This S is the ENTIRE content of the lift on the rep.
# ==========================================================================
def sign_operator_from_cartan_rho(rho_h):
    n = len(rho_h)
    S = [[ZERO] * n for _ in range(n)]
    weights_seen = []
    for i in range(n):
        wt = rho_h[i][i]
        assert wt[1] == 0 and wt[0].denominator == 1, "sl2 Cartan weight not integral"
        w = int(wt[0])
        # off-diagonal of a Cartan rep must vanish (diagonal in weight basis)
        for j in range(n):
            if j != i:
                assert rho_h[i][j] == ZERO, "rho(cartan) not diagonal in weight basis"
        weights_seen.append(w)
        S[i][i] = ONE if (w % 2 == 0) else NEG1
    return S, weights_seen


# ---- rep 1: principal 27 (EVEN) -- the OBJECT's own rep ----
rho_h_principal = toF(rho27_Q(e6h))
S_principal, wts_principal = sign_operator_from_cartan_rho(rho_h_principal)
principal_even = all(w % 2 == 0 for w in wts_principal)
principal_S_is_I = meq(S_principal, meye(27))
say(f"principal 27 weights all even = {principal_even}; S_principal == I: {principal_S_is_I}")

# ---- rep 3: single-simple-root sl2 on the 27 (ODD, minuscule) ----
def single_root_triple(i):
    a = simple6[i]
    na = tuple(-x for x in a)
    e = evec(a)
    f0 = evec(na)
    h0 = br(e, f0)
    c = br(h0, e)[N + IDX[a]]          # <a, h0>; want [h,e]=2e so rescale f
    f = smul_(F(2) / c, f0)
    h = br(e, f)
    # exact sl2 relations
    assert br(e, f) == h
    assert all(br(h, e)[k] == F(2) * e[k] for k in range(DIM))
    assert all(br(h, f)[k] == F(-2) * f[k] for k in range(DIM))
    return e, h, f


e_r, h_r, f_r = single_root_triple(0)
Aro = nilexp(toF(rho27_Q(e_r)), ONE)
Bro = nilexp(toF(rho27_Q(f_r)), QQ)
Aroi = nilexp(toF(rho27_Q(e_r)), fneg(ONE))
Broi = nilexp(toF(rho27_Q(f_r)), fneg(QQ))
dro = {'a': Aro, 'A': Aroi, 'b': Bro, 'B': Broi}
rho_h_root = toF(rho27_Q(h_r))
S_root, wts_root = sign_operator_from_cartan_rho(rho_h_root)
root_even = all(w % 2 == 0 for w in wts_root)
root_S_is_I = meq(S_root, meye(27))
say(f"single-root 27 weights = {sorted(set(wts_root))} (minuscule); "
    f"even = {root_even}; S_root == I: {root_S_is_I}")

# ---- rep 2: the 2-dim SL(2,C) Riley rep (ODD, Sym^1) -- the raw holonomy ----
A2 = [[ONE, ONE], [ZERO, ONE]]                 # exp(e_2)  = [[1,1],[0,1]]
B2 = [[ONE, ZERO], [QQ, ONE]]                  # exp(q.f_2)= [[1,0],[q,1]]
A2i = minv2(A2)
B2i = minv2(B2)
d2 = {'a': A2, 'A': A2i, 'b': B2, 'B': B2i}
S2 = mscalar(2, NEG1)                            # phi(-I) = -I on Sym^1
say("2-dim Riley rep A2, B2 built; S2 = -I")

# ==========================================================================
# CONTROL C -- both lifts are valid reps, and genuinely different.
#   * relator holds under lift_+ in every rep (valid figure-eight rep).
#   * relator holds under lift_- = flip-both (the other valid lift).
#   * the two lifts differ: S != I in the ODD reps (sign character nontrivial).
#   * S is CENTRAL: commutes with A and B in every rep (S = phi(-I)).
# ==========================================================================
def relator_ok(dd):
    n = len(dd['a'])
    return meq(word(RELATOR, dd), meye(n))


def flip_both(dd, S):
    # lift_-: multiply each generator (and its inverse) by the central S
    return {'a': mmul(S, dd['a']), 'A': mmul(S, dd['A']),
            'b': mmul(S, dd['b']), 'B': mmul(S, dd['B'])}


REPS = {
    "2dim_odd":       dict(dd=d2,  S=S2,        n=2,  parity="ODD"),
    "principal27_even": dict(dd=d27, S=S_principal, n=27, parity="EVEN"),
    "singleroot27_odd": dict(dd=dro, S=S_root,   n=27, parity="ODD"),
}
ctrlC = {}
for name, R in REPS.items():
    dd, S, n = R["dd"], R["S"], R["n"]
    lift_plus_ok = relator_ok(dd)
    lift_minus_ok = relator_ok(flip_both(dd, S))
    S_neq_I = not meq(S, meye(n))
    S_central = (meq(mmul(S, dd['a']), mmul(dd['a'], S)) and
                 meq(mmul(S, dd['b']), mmul(dd['b'], S)))
    S_sq_I = meq(mmul(S, S), meye(n))
    ctrlC[name] = {
        "lift_plus_valid_rep_relator=I": lift_plus_ok,
        "lift_minus(flip_both)_valid_rep_relator=I": lift_minus_ok,
        "lifts_differ_S_neq_I": S_neq_I,
        "S_central_commutes_A_and_B": S_central,
        "S_squared=I": S_sq_I,
    }
    say(f"CONTROL C [{name}]: lift+ ok={lift_plus_ok}, lift- ok={lift_minus_ok}, "
        f"S!=I={S_neq_I}, S central={S_central}, S^2=I={S_sq_I}")
controls["C_both_lifts_valid_and_distinct"] = ctrlC

# ==========================================================================
# STAGE 3 -- SINGLE-COPY: does a closed-copy trace see the lift?
#   meridian a: odd homology (chi(a)=-1)  -> lift_-(a) = S.A
#   longitude lam = bABaaBAb: even homology (chi=+1), peripheral -> lift-blind
# ==========================================================================
LONGITUDE = 'bABaaBAb'
single_copy = {}
for name, R in REPS.items():
    dd, S = R["dd"], R["S"]
    A_op = dd['a']
    lam_plus = word(LONGITUDE, dd)
    tr_a_plus = mtrace(A_op)
    tr_a_minus = mtrace(mmul(S, A_op))         # lift_-(a) = S.A
    tr_lam_plus = mtrace(lam_plus)
    # lift_-(lam): even length 8 -> S^8 = I; compute explicitly by flipping
    dd_minus = flip_both(dd, S)
    tr_lam_minus = mtrace(word(LONGITUDE, dd_minus))
    meridian_sees = (tr_a_plus != tr_a_minus)
    longitude_sees = (tr_lam_plus != tr_lam_minus)
    single_copy[name] = {
        "tr_meridian_lift_plus": ffmt(tr_a_plus),
        "tr_meridian_lift_minus": ffmt(tr_a_minus),
        "meridian_trace_SEES_lift": meridian_sees,
        "tr_longitude_lift_plus": ffmt(tr_lam_plus),
        "tr_longitude_lift_minus": ffmt(tr_lam_minus),
        "longitude_trace_sees_lift": longitude_sees,
        "single_copy_blind": (not meridian_sees) and (not longitude_sees),
    }
    say(f"SINGLE-COPY [{name}]: tr(meridian) {ffmt(tr_a_plus)} vs {ffmt(tr_a_minus)} "
        f"-> sees={meridian_sees}; longitude sees={longitude_sees}")
results["single_copy"] = single_copy

# ==========================================================================
# STAGE 4 -- THE COUPLED PAIR / SEAM.
#   reference : same lift both copies.  B_L = B, B_R = B.
#   opposite  : right copy on the opposite lift.  chi(a)=chi(b)=-1 forces the
#               WHOLE right copy to be flipped: a_R = S.A, b_R = S.B.  (Flipping
#               only b is NOT a homomorphism: a ~ b in H_1.)
#   symmetric : both copies flipped (the only nontrivial spin structure on the
#               closed double, H^1(DM;Z/2)=Z/2 diagonal).
#
#   SEAM VALIDITY: the gluing identifies the meridian, a_L = a_R.  Under the
#   opposite lift a_R = S.A; the config is a valid doubled rep iff S.A = A.
#
#   THREE seam traces, each config:  tr(A . B_R),  tr(B_L . B_R),
#   tr([B_L,B_R]) group commutator = B_L B_R B_L^-1 B_R^-1.
# ==========================================================================
pair = {}
for name, R in REPS.items():
    dd, S, n = R["dd"], R["S"], R["n"]
    A_op, B_op, Bi_op = dd['a'], dd['b'], dd['B']

    # seam validity: is the opposite-lift a valid gluing? (a_L == a_R ?)
    SA = mmul(S, A_op)
    seam_consistent = meq(SA, A_op)

    def seam_traces(BR, BRi):
        trA = mtrace(mmul(A_op, BR))
        trBB = mtrace(mmul(B_op, BR))
        gc = mmul(mmul(mmul(B_op, BR), Bi_op), BRi)     # [B_L, B_R]
        return trA, trBB, mtrace(gc)

    # reference: B_R = B
    ref = seam_traces(B_op, Bi_op)
    # opposite: B_R = S.B ; (S.B)^-1 = B^-1 . S  (S central, S^2=I)
    SB = mmul(S, B_op)
    SBi = mmul(Bi_op, S)
    opp = seam_traces(SB, SBi)
    # symmetric: BOTH copies flipped. B_L = S.B, B_R = S.B, A_seam = S.A shared.
    ddm = flip_both(dd, S)
    Am, Bm, Bim = ddm['a'], ddm['b'], ddm['B']
    trA_sym = mtrace(mmul(Am, Bm))
    trBB_sym = mtrace(mmul(Bm, Bm))
    gc_sym = mmul(mmul(mmul(Bm, Bm), Bim), Bim)
    sym = (trA_sym, trBB_sym, mtrace(gc_sym))

    sep_trA = (ref[0] != opp[0])
    sep_trBB = (ref[1] != opp[1])
    sep_gc = (ref[2] != opp[2])
    sym_invisible = (ref[0] == sym[0] and ref[1] == sym[1] and ref[2] == sym[2])

    pair[name] = {
        "opposite_lift_is_valid_gluing_(a_L=a_R)": seam_consistent,
        "reference_same_lift": {
            "tr_A_BR": ffmt(ref[0]), "tr_BL_BR": ffmt(ref[1]),
            "tr_group_comm": ffmt(ref[2])},
        "opposite_lift_naive": {
            "tr_A_BR": ffmt(opp[0]), "tr_BL_BR": ffmt(opp[1]),
            "tr_group_comm": ffmt(opp[2])},
        "symmetric_flip_both": {
            "tr_A_BR": ffmt(sym[0]), "tr_BL_BR": ffmt(sym[1]),
            "tr_group_comm": ffmt(sym[2])},
        "separates_tr_A_BR": sep_trA,
        "separates_tr_BL_BR": sep_trBB,
        "separates_group_commutator": sep_gc,
        "symmetric_twist_invisible": sym_invisible,
        "any_seam_trace_separates_a_VALID_config":
            (seam_consistent and (sep_trA or sep_trBB or sep_gc)),
    }
    say(f"PAIR [{name}]: opp-lift valid gluing={seam_consistent}; "
        f"separates (A.BR/BL.BR/[BL,BR]) = {sep_trA}/{sep_trBB}/{sep_gc}; "
        f"group-comm ref={ffmt(ref[2])} opp={ffmt(opp[2])}; sym invisible={sym_invisible}")
results["pair"] = pair

# ==========================================================================
# VERDICT
# ==========================================================================
# PAIR-MEASURABLE iff, in the OBJECT's rep (principal 27, even) OR in any rep
# where the opposite lift is a VALID doubled gluing, some seam trace separates.
object_rep = pair["principal27_even"]
object_separates = object_rep["any_seam_trace_separates_a_VALID_config"]

# in the odd reps: does a seam trace separate a VALID config? (needs the opposite
# lift to be a valid gluing -- it is not, S.A != A)
odd_valid_separation = any(
    pair[nm]["any_seam_trace_separates_a_VALID_config"]
    for nm in ("2dim_odd", "singleroot27_odd")
)

controls_all_pass = (
    controls["A_reproduce_b1113_dialblind_number"]["equals_141750+1011915q"] and
    controls["A_reproduce_b1113_dialblind_number"]["dial_blind_tr_A_BR_t1_equals_t0"] and
    controls["A_reproduce_b1113_dialblind_number"]["t0_sharp_tr_BL_BR_equals_27"] and
    controls["B_rho27_is_a_representation_all_3003_brackets"] and
    all(v["lift_plus_valid_rep_relator=I"] and v["lift_minus(flip_both)_valid_rep_relator=I"]
        and v["S_central_commutes_A_and_B"] and v["S_squared=I"] for v in ctrlC.values()) and
    ctrlC["2dim_odd"]["lifts_differ_S_neq_I"] and
    ctrlC["singleroot27_odd"]["lifts_differ_S_neq_I"] and
    (not ctrlC["principal27_even"]["lifts_differ_S_neq_I"])   # even: S == I as required
)

if not controls_all_pass:
    VERDICT = "INCONCLUSIVE"
    REASON = "a positive control failed; see controls block"
elif object_separates or odd_valid_separation:
    VERDICT = "PAIR-MEASURABLE"
    REASON = "a seam trace separates the relative lifts in a valid doubled configuration"
else:
    VERDICT = "PAIR-INVISIBLE"
    REASON = (
        "Object's rep (principal 27) is EVEN: S=phi(-I)=I, so the two lifts are the "
        "identical operator -- no seam trace can differ (single-copy AND pair blind). "
        "In ODD reps S!=I, but (i) the lift is already a SINGLE-COPY observable there "
        "(tr(meridian) flips), so it is not 'free-of-one'; and (ii) the opposite-lift "
        "pair config is NOT a valid gluing (S.A != A breaks the seam identification "
        "a_L=a_R), unlike the dial (a seam-centralizing conjugation). The group "
        "commutator -- the t-meter's separating meter -- is identically blind to the "
        "central sign S in every rep. The only valid nontrivial double spin structure "
        "(symmetric flip, H^1(DM;Z/2)=Z/2) is invisible (the two S's cancel)."
    )

results["controls"] = controls
results["verdict"] = VERDICT
results["reason"] = REASON
results["object_rep_seam_separates"] = object_separates
results["odd_rep_valid_seam_separation"] = odd_valid_separation
results["all_controls_pass"] = controls_all_pass
RUNTIME = round(time.time() - T0, 2)
results["runtime_seconds"] = RUNTIME
results["ccb_path"] = CCB_PATH

print()
print("=" * 78)
print(f"VERDICT: {VERDICT}")
print(f"REASON:  {REASON}")
print(f"runtime: {RUNTIME}s")
print("=" * 78)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "L179_results.json")
with open(OUT, "w") as fh:
    json.dump(results, fh, indent=2)
say(f"results written to {OUT}")
