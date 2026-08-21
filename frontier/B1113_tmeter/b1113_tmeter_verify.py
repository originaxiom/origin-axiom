#!/usr/bin/env python3
"""
B1113 verification bench -- THE JORDAN t-METER (JORDAN_MEMO.md, section B).

CLAIM UNDER TEST (memo's own words): on the twisted double of the figure-eight
complement (B1086 machinery), with theta-odd dial parameter t in {0,1,2,omega}:
  1. tr(A . B_R) is t-INDEPENDENT  (memo's number: 141750+1011915q at every t)
  2. tr(B_L . B_R) and tr([B_L,B_R]) SEPARATE every dial value (distinct exact
     field elements at t=0,1,2,omega).
Sharp law claimed: free data of one object (the dial) = forced/character-level
data of the coupled PAIR.

THIS SCRIPT is an independent, standalone re-derivation -- it does not trust the
memo's numbers, and it does not dynamically execute the outside-bench certificate
(cloud_handoff/certificates/twisted_double.py) at runtime, because that file has
its own internal hardcoded absolute import path to a directory outside this repo
(an "outside audit seat" location that is not guaranteed to exist on every
machine -- see b1113_NOTES.md "portability" section). Instead this script:
  - reuses the repo-vendored, sha256-provenanced copy of the E6 Chevalley-basis
    module (frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py),
    which the repo's own B1102 arc already certified against the SAME outside
    file this task points to -- i.e. genuinely "given machinery" (a library),
    not the thing under test;
  - independently re-derives, in this file's own code, everything the memo's
    claim actually depends on: principal sl2, the two theta-odd dial slots
    (highest weight vectors of weight 8 and 16), the 27-dim crystal module,
    the Riley-type generator matrices A27=rho(a), B27=rho(b), and the dial
    D(t) = exp(t . rho(x8)) (or x16);
  - reconstructs the memo's operators A, B_L, B_R (not explicitly defined
    anywhere in the banked record -- see b1113_NOTES.md for the full argument)
    and computes the three traces EXACTLY over Q(q), q^2 = q-1;
  - runs positive controls FIRST, on quantities already banked in B1086's
    FINDINGS.md / the certificate's own printed record, before trusting any
    new number.

Field: Q(q)/(q^2-q+1), q a primitive 6th root of unity, elements as Fraction
pairs (x,y) meaning x + y*q.  omega = q-1 (NOT the memo's dial-symbol overload
with a cube root of unity -- this follows the certificate's own convention).

Paths: repo-relative with env-var overrides and documented defaults (no bare
machine paths baked into the logic below).
"""
import os
import sys
import time
import itertools
import importlib.util
from fractions import Fraction as F

import sympy as sp

T0 = time.time()

# --------------------------------------------------------------------------
# 0. locations -- env-overridable, documented defaults
# --------------------------------------------------------------------------
REPO_ROOT = os.environ.get("B1113_REPO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CCB_PATH = os.environ.get(
    "B1113_CCB_PATH",
    os.path.join(REPO_ROOT, "frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py"),
)
# The outside-bench certificate this arc's construction is read from (for
# provenance/logging only -- NOT imported at runtime; see module docstring).
# Documented default: the scratchpad staging location this task was given;
# override with B1113_CERT_PATH on another machine/session. Existence is
# checked and logged but the file is never executed by this script.
CERT_PATH = os.environ.get("B1113_CERT_PATH", "")  # session cert; not executed here
CERT_PATH_INFO = CERT_PATH + (
    "  [found, read as design reference, NOT executed -- see module docstring]"
    if os.path.exists(CERT_PATH) else
    "  [not found on this machine -- this script does not depend on it at runtime]"
)


def load_ccb():
    spec = importlib.util.spec_from_file_location("ccb", CCB_PATH)
    ccb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ccb)
    return ccb


def say(msg):
    print(f"[{time.time()-T0:7.2f}s] {msg}")


# --------------------------------------------------------------------------
# 1. field Q(q), q^2 = q - 1  (elements: Fraction pairs (x,y) = x + y*q)
# --------------------------------------------------------------------------
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
QQ = (F(0), F(1))          # q
OMEGA = (F(-1), F(1))      # omega = q - 1


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
    n = x * x + x * y + y * y      # norm form, positive definite (disc = -3)
    return ((x + y) / n, -y / n)


def frat(r):
    return (F(r), F(0))


def ffmt(u):
    """Human-readable 'x+yq' style, matching the memo's own display convention
    (drops the q-term entirely when its coefficient is exactly zero)."""
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
# 2. matrix helpers over the field (dense, list-of-lists of pairs)
# --------------------------------------------------------------------------
def meye(n):
    M = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = ONE
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
    """Lift a plain-Fraction (rational) matrix into the field-pair representation."""
    return [[(v, F(0)) for v in row] for row in Mq]


def nilexp(Mp, scale):
    """exp(scale . Mp) for Mp nilpotent, as an exact truncating power series
    (identical recipe to the certificate's own nilexp)."""
    n = len(Mp)
    out = meye(n)
    P = meye(n)
    fact = F(1)
    sc = ONE
    for k in range(1, 60):
        P = mmul(P, Mp)
        fact *= k
        sc = fmul(sc, scale)
        if all(x == ZERO for row in P for x in row):
            break
        coef = fmul(sc, finv((fact, F(0))))
        out = madd(out, [[fmul(coef, xx) for xx in row] for row in P])
    return out


def wordmat(word, dd):
    Mp = meye(len(dd['a']))
    for ch in word:
        Mp = mmul(Mp, dd[ch])
    return Mp


# --------------------------------------------------------------------------
# 3. plain-Q (Fraction) linear algebra, for the Fox-calculus control only
# --------------------------------------------------------------------------
def rref(M):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv = []
    r = 0
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if M[i][c] != ZERO:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        inv = finv(M[r][c])
        M[r] = [fmul(inv, x) for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != ZERO:
                f_ = M[i][c]
                M[i] = [fsub(x, fmul(f_, y)) for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M, piv


def rank(M):
    return len(rref(M)[1])


def nullspace(M):
    R, piv = rref(M)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    out = []
    for fc in free:
        v = [ZERO] * cols
        v[fc] = ONE
        for i, c in enumerate(piv):
            v[c] = fneg(R[i][fc])
        out.append(v)
    return out


def fox_h1(dd, nn):
    """Fox-calculus H^1(M;27) for the figure-eight group <a,b | a.w = w.b>,
    w = bABa (identical recipe to the certificate's own fox_h1, stage 4)."""
    I = meye(nn)
    Ai, Bi = dd['A'], dd['B']
    An, Bn = dd['a'], dd['b']
    dw_da = msub(mmul(Bn, mmul(Ai, Bi)), mmul(Bn, Ai))
    dw_db = msub(I, mmul(Bn, mmul(Ai, Bi)))
    W = wordmat('bABa', dd)
    Wi = wordmat('AbaB', dd)
    AW = mmul(An, W)
    AWBi = mmul(AW, Bi)
    AWBiWi = mmul(AWBi, Wi)
    dr_da = madd(I, msub(mmul(An, dw_da), mmul(AWBiWi, dw_da)))
    dr_db = msub(mmul(An, dw_db), madd(AWBi, mmul(AWBiWi, dw_db)))
    D1 = [dr_da[i] + dr_db[i] for i in range(nn)]
    Z = nullspace(D1)
    Bcols = []
    AnI = msub(An, I)
    BnI = msub(Bn, I)
    for j in range(nn):
        Bcols.append([AnI[i][j] for i in range(nn)] + [BnI[i][j] for i in range(nn)])
    Bmat = [[Bcols[j][i] for j in range(nn)] for i in range(2 * nn)]
    rB = rank(Bmat)
    return len(Z) - rB


# ==========================================================================
# STAGE 0: e6 Chevalley basis (vendored, repo-relative) + principal sl2 +
#          the two theta-odd dial slots (hv8, hv16) + the theta-even control
#          slot (hv14) -- verbatim reconstruction of twisted_double.py stage 0
# ==========================================================================
say(f"loading e6 Chevalley module from {CCB_PATH}")
ccb = load_ccb()
br, add_, smul_, is_zero = ccb.br, ccb.add, ccb.smul, ccb.is_zero
evec, hvec, eps, ip = ccb.evec, ccb.hvec, ccb.eps, ccb.ip
ROOTS, IDX, N, DIM = ccb.ROOTS, ccb.IDX, ccb.N, ccb.DIM
say(f"stage 0: e6 loaded, {len(ROOTS)} roots, dim {DIM}  (expect 72, 78)")
assert len(ROOTS) == 72 and DIM == 78, "e6 shape mismatch -- wrong module?"

simple6 = [tuple(1 if k == i else 0 for k in range(6)) for i in range(6)]
Cart = sp.Matrix(6, 6, lambda i, j: ip(simple6[i], simple6[j]))
hcoef = Cart.solve(sp.Matrix([2] * 6))
e6h = [F(0)] * DIM
for j in range(N):
    e6h[j] = F(int(hcoef[j]))
e6e = [F(0)] * DIM
for i in range(N):
    pos = tuple(1 if k == i else 0 for k in range(N))
    e6e[N + IDX[pos]] = F(1)
e6f = [F(0)] * DIM
for j in range(N):
    neg = tuple(-1 if i2 == j else 0 for i2 in range(N))
    e6f[N + IDX[neg]] = e6h[j] / F(eps(tuple(1 if k == j else 0 for k in range(N)), neg))
assert br(e6e, e6f) == e6h, "principal sl2 triple failed: [e,f] != h"
say("stage 0: principal sl2 triple (e,h,f) built and verified: [e,f]=h  PASS")


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
    if not ns:
        return None
    vec = ns[0]
    out = [F(0)] * DIM
    for j, c in enumerate(cols):
        coef = sp.Rational(vec[j])
        if coef:
            out = add_(out, smul_(F(coef.p, coef.q), c))
    return out


X8 = highest_vector(8)
X16 = highest_vector(16)
X14 = highest_vector(14)   # theta-even control slot (not part of the memo's claim)
for name, X in (("X8", X8), ("X16", X16), ("X14", X14)):
    assert X is not None and not is_zero(X), f"{name} failed to build"
    assert is_zero(br(e6e, X)), f"{name} does not centralize the principal e"
say("stage 0: dial slots hv(8), hv(16) [theta-odd] and hv(14) [theta-even control] "
    "built, e-centralizing: PASS")

# ==========================================================================
# STAGE 1: the 27 (crystal of omega_1) + module action rho27
#          -- verbatim reconstruction of twisted_double.py stage 1
# ==========================================================================
Msys = sp.Matrix(6, 6, lambda i, j: ip(simple6[i], simple6[j]))
w1 = Msys.solve(sp.Matrix([1, 0, 0, 0, 0, 0]))
omega1 = tuple(sp.Rational(w1[k]) for k in range(6))


def tadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def tsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def ipr(a, b):
    return sum(a[i] * b[j] * Msys[i, j] for i in range(6) for j in range(6))


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
for w in weights:
    assert all(sp.Rational(a) == int(a) for a in tsub(w, omega1)), "non-integral shift"
say("stage 1: 27 weights built (crystal of omega_1)  PASS")


def act_root(r):
    out = {}
    for w in weights:
        tgt = tadd(w, r)
        if tgt in WIDX:
            out[WIDX[w]] = (WIDX[tgt], F(eps(r, qlat[w])))
    return out


ROOTACT = {r: act_root(r) for r in ROOTS}

CJ = []
for j in range(6):
    vals = sp.Matrix([[br(hvec(j), evec(al))[N + IDX[al]] for al in simple6]])
    CJ.append([sp.Rational(vals[0, k]) for k in range(6)])


def cartan_eig(j, lam):
    return sum(sp.Rational(CJ[j][k]) * sp.Rational(lam[k]) for k in range(6))


def rho27_Q(vec):
    Mq = [[F(0)] * 27 for _ in range(27)]
    for j in range(6):
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


# ==========================================================================
# CONTROL #1 (structural, exhaustive): rho27 is a genuine Lie-algebra
# representation -- rho([u,v]) = [rho(u),rho(v)] on ALL C(78,2)=3003 Chevalley
# pairs.  This is the SAME check the certificate prints as
# "stage 1 VERIFY: rho27 respects ALL 3003 Chevalley brackets: PASS"
# (see jordan_probe_out.txt line 4) -- reproduced here independently.
# ==========================================================================
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


basis_ad = []
for j in range(6):
    v = [F(0)] * DIM
    v[j] = F(1)
    basis_ad.append(v)
for r in ROOTS:
    basis_ad.append(evec(r))

say(f"control #1: verifying rho27 respects all C({len(basis_ad)},2) = "
    f"{len(basis_ad) * (len(basis_ad) - 1) // 2} Chevalley brackets (exhaustive) ...")
RHO = [rho27_Q(v) for v in basis_ad]
pairs = list(itertools.combinations(range(len(basis_ad)), 2))
fails1 = 0
for (i2, j2) in pairs:
    lhs = rho27_Q(br(basis_ad[i2], basis_ad[j2]))
    rhs = matQ_sub(matQ_mul(RHO[i2], RHO[j2]), matQ_mul(RHO[j2], RHO[i2]))
    if lhs != rhs:
        fails1 += 1
CONTROL_1_PASS = (fails1 == 0)
say(f"control #1: rho27 respects ALL {len(pairs)} Chevalley brackets: "
    f"{'PASS' if CONTROL_1_PASS else f'FAIL ({fails1})'}")

# ==========================================================================
# CONTROL #2 (numeric, banked): principal string content of the 27 is
# Sym^16 + Sym^8 + Sym^0 -- reproduces the certificate's printed diagnostic
# "stage 2: principal strings: [16, 8, 0]" (jordan_probe_out.txt line 5) and
# underlies FINDINGS.md's "h1(M;27) = 3 = 1+1+1 solo" bookkeeping.
# ==========================================================================
grades = {}
for w in weights:
    g = sum(sp.Rational(e6h[j]) * cartan_eig(j, w) for j in range(6))
    grades[WIDX[w]] = int(g)
from collections import Counter
gc = Counter(grades.values())
strings = [n for n in range(0, 40, 2) if gc.get(n, 0) - gc.get(n + 2, 0) > 0
           for _ in range(gc.get(n, 0) - gc.get(n + 2, 0))]
strings_sorted = sorted(strings, reverse=True)
CONTROL_2_PASS = (strings_sorted == [16, 8, 0])
say(f"control #2: principal string content = {strings_sorted} "
    f"(banked/expected [16, 8, 0]): {'PASS' if CONTROL_2_PASS else 'FAIL'}")

# ==========================================================================
# STAGE 3: the group representation on the 27 -- Riley-type generator
# matrices A27 = exp(rho(e)) = rho(a), B27 = exp(q.rho(f)) = rho(b)
# -- verbatim reconstruction of twisted_double.py stage 3.
# ==========================================================================
E27 = rho27_Q(e6e)
F27 = rho27_Q(e6f)
E27p = toF(E27)
F27p = toF(F27)
A27 = nilexp(E27p, ONE)
B27 = nilexp(F27p, QQ)
A27i = nilexp(E27p, fneg(ONE))
B27i = nilexp(F27p, fneg(QQ))
assert meq(mmul(A27, A27i), meye(27)), "A27 * A27^-1 != I"
assert meq(mmul(B27, B27i), meye(27)), "B27 * B27^-1 != I"
say("stage 3: A27=rho(a), B27=rho(b) built via exact nilpotent exponential; "
    "A.A^-1=I, B.B^-1=I  PASS")

# ==========================================================================
# CONTROL #3 (structural, banked): the group relator a.w = w.b, w = bABa,
# acts as the identity on the 27 -- reproduces the certificate's
# "stage 3: relator acts as identity on the 27: PASS" (jordan_probe_out.txt
# line 6), independently cross-checked by tests/test_b1086_spectrum_law.py's
# test_relator_and_riley (same relator, same generators, SL(2) 2x2 case).
# ==========================================================================
d27 = {'a': A27, 'A': A27i, 'b': B27, 'B': B27i}
RELATOR_WORD = 'a' + 'bABa' + 'B' + 'AbaB'   # a . w . b^-1 . w^-1, w = bABa
assert RELATOR_WORD == 'abABaBAbaB'
Rel = wordmat(RELATOR_WORD, d27)
CONTROL_3_PASS = meq(Rel, meye(27))
say(f"control #3: relator 'a.w.B.w^-1' (w=bABa) acts as identity on the 27: "
    f"{'PASS' if CONTROL_3_PASS else 'FAIL'}")

# ==========================================================================
# CONTROL #4 (numeric, banked): h^1(M;27) = 3 for the untwisted figure-eight
# complement, via Fox calculus on the SAME presentation/generators -- this is
# THE explicit banked NUMBER in B1086's FINDINGS.md ("h1(M;27) = 3 = 1+1+1
# solo"; also test_b1086_spectrum_law.py's independent SL(2)-block rebuild,
# and jordan_probe_out.txt would have printed "stage 4: h^1(M;27) = 3" had
# the outside-bench probe continued past stage 3 -- it did not; this bench
# closes that gap as the REQUIRED positive control before trusting new traces).
# ==========================================================================
say("control #4: computing h^1(M;27) via Fox calculus (banked value = 3) ...")
H1_M_27 = fox_h1(d27, 27)
CONTROL_4_PASS = (H1_M_27 == 3)
say(f"control #4: h^1(M;27) = {H1_M_27} (banked/expected 3): "
    f"{'PASS' if CONTROL_4_PASS else 'FAIL'}")

ALL_CONTROLS_PASS = CONTROL_1_PASS and CONTROL_2_PASS and CONTROL_3_PASS and CONTROL_4_PASS
say(f"ALL POSITIVE CONTROLS: {'PASS' if ALL_CONTROLS_PASS else 'AT LEAST ONE FAILED -- STOP'}")
if not ALL_CONTROLS_PASS:
    print("STOPPING: the machinery does not reproduce banked B1086 quantities; "
          "the operator identification below cannot be trusted. See NOTES.")
    RESULTS_STOP = True
else:
    RESULTS_STOP = False

# ==========================================================================
# STAGE 4 (this bench, new): the dial D(t) = exp(t . rho(x_slot)), and the
# KEY structural fact the memo's t-independence claim rests on: the dial
# centralizes the meridian A27 (the certificate asserts this for its own
# gluing to be well-defined -- "dial must centralize the cusp"). Verified
# here directly and independently, for BOTH theta-odd slots, at every t.
# ==========================================================================
X8_27p = toF(rho27_Q(X8))
X16_27p = toF(rho27_Q(X16))
X14_27p = toF(rho27_Q(X14))

SLOTS = {"hv8": X8_27p, "hv16": X16_27p}
TVALS = {"0": ZERO, "1": ONE, "2": frat(2), "omega": OMEGA}


def dial(tval, Xp):
    return nilexp(Xp, tval)


DIAL_CENTRALIZES_A = {}
for slot_name, Xp in SLOTS.items():
    for tname, tv in TVALS.items():
        Dt = dial(tv, Xp)
        DIAL_CENTRALIZES_A[(slot_name, tname)] = meq(mmul(Dt, A27), mmul(A27, Dt))
CONTROL_5_PASS = all(DIAL_CENTRALIZES_A.values())
say(f"control #5 (dial vs meridian, both theta-odd slots, all t): "
    f"D(t).A27 = A27.D(t) everywhere: {'PASS' if CONTROL_5_PASS else 'FAIL -- see per-cell detail'}")
if not CONTROL_5_PASS:
    for k, v in DIAL_CENTRALIZES_A.items():
        if not v:
            say(f"   FAILS at slot={k[0]}, t={k[1]}")

# also check the theta-EVEN slot does NOT centralize (expected negative control)
DIAL_EVEN_CENTRALIZES_A = {}
for tname, tv in TVALS.items():
    if tv == ZERO:
        continue
    Dt = dial(tv, X14_27p)
    DIAL_EVEN_CENTRALIZES_A[tname] = meq(mmul(Dt, A27), mmul(A27, Dt))
say(f"control #5b (theta-EVEN slot hv14, negative-control expectation): "
    f"centralizes A27 at t=1,2,omega: {DIAL_EVEN_CENTRALIZES_A} "
    f"(no claim requires this to fail; recorded for completeness)")

# ==========================================================================
# STAGE 5 (this bench, new): OPERATOR RECONSTRUCTION -- A, B_L, B_R.
#
# Full argument in b1113_NOTES.md; summary:
#   A    := A27 = rho(a)   -- the meridian / peripheral generator: THE SEAM.
#           Shared, unsubscripted, because it is literally identified across
#           the gluing torus and (control #5) the dial centralizes it.
#   B_L  := B27 = rho(b)   -- the OTHER Riley generator, untwisted (left hand,
#           no dial applied). It is NOT peripheral (the peripheral subgroup
#           is <a, lambda> with lambda a longer word in a,b -- not b itself),
#           so there is no a-priori reason for it to commute with the dial.
#   B_R(t) := D(t) . B27 . D(t)^{-1}  -- the SAME generator, evaluated in the
#           right copy's dial-twisted coefficient system. This is exactly the
#           coefficient-twist the certificate's own Mayer-Vietoris code
#           applies to right-copy cocycles (post-multiplication by D(t) on
#           values), which is precisely the transform of a representation
#           rho'(g) = D(t).rho(g).D(t)^-1 -- i.e. conjugation, not a bare
#           product. This is also the UNIQUE simple convention under which
#           tr(A.B_R) collapses to a t-independent value given control #5
#           (see derivation in NOTES): since A commutes with D(t),
#             tr(A . D(t) B27 D(t)^-1) = tr(D(t) . A . B27 . D(t)^-1)
#                                      = tr(A . B27)      (conjugation-
#           invariance of trace) -- CONSTANT in t, for ANY B27.
#   [B_L,B_R] -- the memo's bracket notation. Checked BOTH readings:
#           (a) the Lie/matrix commutator B_L.B_R - B_R.B_L: trace is
#               IDENTICALLY ZERO for ANY two square matrices (tr(XY)=tr(YX)
#               always) -- included below purely as an internal sanity
#               check, NOT as a candidate for the memo's reported nonzero
#               numbers;
#           (b) the GROUP commutator B_L.B_R.B_L^-1.B_R^-1 (standard in a
#               discrete-representation / Wilson-line setting, which this
#               whole construction is): its trace is generically nonzero and
#               t-dependent, and at t=0 (D(0)=I, so B_R(0)=B_L exactly) it
#               MUST equal tr(identity) = 27 -- a sharp, checkable prediction
#               made BEFORE running the numbers (matches jordan_probe_out.txt
#               t=0 row exactly: both tr(B_L.B_R) and tr([B_L,B_R]) = 27).
#           Reading (b) is reported as "the" tr([B_L,B_R]) below.
# ==========================================================================


def dial_inv(tval, Xp):
    return dial(fneg(tval), Xp)


def B_R_of(tval, Xp):
    Dt = dial(tval, Xp)
    Dti = dial_inv(tval, Xp)
    return mmul(mmul(Dt, B27), Dti), Dt, Dti


def B_R_inv_of(tval, Xp, Dt, Dti):
    # (D.B27.D^-1)^-1 = D.B27^-1.D^-1
    return mmul(mmul(Dt, B27i), Dti)


results = {}
say("computing tr(A.B_R), tr(B_L.B_R), tr(matrix-commutator) [sanity=0], "
    "tr(group-commutator) at every (slot, t) ...")
for slot_name, Xp in SLOTS.items():
    for tname, tv in TVALS.items():
        BR, Dt, Dti = B_R_of(tv, Xp)
        BRi = B_R_inv_of(tv, Xp, Dt, Dti)

        trA_BR = mtrace(mmul(A27, BR))
        trBL_BR = mtrace(mmul(B27, BR))
        mat_comm = msub(mmul(B27, BR), mmul(BR, B27))
        tr_mat_comm = mtrace(mat_comm)
        group_comm = mmul(mmul(mmul(B27, BR), B27i), BRi)
        tr_group_comm = mtrace(group_comm)

        results[(slot_name, tname)] = dict(
            trA_BR=trA_BR, trBL_BR=trBL_BR,
            tr_mat_comm=tr_mat_comm, tr_group_comm=tr_group_comm,
        )
say("trace computation done.")

# sanity: the matrix (Lie) commutator trace must be EXACTLY zero, always
MAT_COMM_ALWAYS_ZERO = all(v["tr_mat_comm"] == ZERO for v in results.values())
say(f"sanity: tr(matrix commutator B_L B_R - B_R B_L) = 0 at every cell "
    f"(expected always True, pure linear algebra): {MAT_COMM_ALWAYS_ZERO}")

# t=0 sharp prediction check (made in the docstring above, before running numbers)
T0_PREDICTIONS_OK = all(
    results[(s, "0")]["trBL_BR"] == frat(27) and results[(s, "0")]["tr_group_comm"] == frat(27)
    for s in SLOTS
)
say(f"t=0 sharp prediction (tr(B_L B_R)=tr([B_L,B_R])_group=27=dim, since D(0)=I "
    f"forces B_R=B_L): {'CONFIRMED' if T0_PREDICTIONS_OK else 'VIOLATED'}")

# ==========================================================================
# STAGE 6: the memo's two checks
#   (i)  is tr(A.B_R) t-independent? (dial-blind)
#   (ii) do tr(B_L.B_R) and tr([B_L,B_R])_group SEPARATE all four t?
# ==========================================================================
def dial_blind(slot_name):
    vals = [results[(slot_name, t)]["trA_BR"] for t in TVALS]
    return all(v == vals[0] for v in vals), vals[0]


def separates_all(slot_name, key):
    vals = {t: results[(slot_name, t)][key] for t in TVALS}
    ts = list(TVALS.keys())
    pairs_sep = {}
    for i in range(len(ts)):
        for j in range(i + 1, len(ts)):
            pairs_sep[f"{ts[i]}_vs_{ts[j]}"] = (vals[ts[i]] != vals[ts[j]])
    all_sep = all(pairs_sep.values())
    return all_sep, pairs_sep, vals


VERDICT = {}
for slot_name in SLOTS:
    blind, blind_val = dial_blind(slot_name)
    sep_bl, sep_bl_pairs, _ = separates_all(slot_name, "trBL_BR")
    sep_gc, sep_gc_pairs, _ = separates_all(slot_name, "tr_group_comm")
    VERDICT[slot_name] = dict(
        dial_blind=blind, dial_blind_value=ffmt(blind_val),
        trBL_BR_separates_all=sep_bl, trBL_BR_pairs=sep_bl_pairs,
        tr_group_comm_separates_all=sep_gc, tr_group_comm_pairs=sep_gc_pairs,
    )
    say(f"slot {slot_name}: tr(A.B_R) dial-blind = {blind} (value {ffmt(blind_val)}); "
        f"tr(B_L.B_R) separates all t = {sep_bl}; "
        f"tr([B_L,B_R])_group separates all t = {sep_gc}")

# cross-check against the memo's own reported numbers (informational only --
# this script does not need agreement with the memo to reach its verdict)
MEMO_NUMBERS = {
    "trA_BR": {"0": (141750, 1011915), "1": (141750, 1011915),
               "2": (141750, 1011915), "omega": (141750, 1011915)},
    "trBL_BR": {
        "0": (27, 0),
        "1": (-4268791455703081896933, 4496860756304889154560),
        "2": (-1136640792617359937187813, 1151247446406074247229440),
        "omega": (4725568716294111759387, 0),
    },
    "tr_group_comm": {
        "0": (27, 0),
        "1": (-1012494675441866094969680468476925337415653,
              -19181399207157472539697602748942049339166720),
        "2": (-16755160684243541173825124529943231919652126693,
              -1308432850647916106766787473050401389584509255680),
        "omega": (21245539863128390787066847414681242215854107, 0),
    },
}


def as_pair(u):
    return (int(u[0]), int(u[1])) if u[0].denominator == 1 and u[1].denominator == 1 else (u[0], u[1])


memo_match = {}
for slot_name in SLOTS:
    memo_match[slot_name] = {}
    for key in ("trA_BR", "trBL_BR", "tr_group_comm"):
        row = {}
        for tname in TVALS:
            mine = as_pair(results[(slot_name, tname)][key])
            memo = MEMO_NUMBERS[key][tname]
            row[tname] = dict(mine=list(mine) if isinstance(mine, tuple) else str(mine),
                               memo=list(memo), match=(mine == memo))
        memo_match[slot_name][key] = row

for slot_name in SLOTS:
    n_match = sum(
        1 for key in ("trA_BR", "trBL_BR", "tr_group_comm")
        for tname in TVALS if memo_match[slot_name][key][tname]["match"]
    )
    say(f"slot {slot_name}: matches memo's printed numbers on {n_match}/12 cells")

RUNTIME_S = time.time() - T0
say(f"TOTAL RUNTIME: {RUNTIME_S:.2f}s")

# ==========================================================================
# outcome grammar
# ==========================================================================
if RESULTS_STOP:
    OUTCOME = "DISCREPANT"
    OUTCOME_REASON = "a positive control failed before the new traces were computed"
else:
    hv8 = VERDICT["hv8"]
    if hv8["dial_blind"] and hv8["trBL_BR_separates_all"] and hv8["tr_group_comm_separates_all"]:
        OUTCOME = "CONFIRMED"
        OUTCOME_REASON = ("tr(A.B_R) is dial-blind and tr(B_L.B_R), tr([B_L,B_R])_group "
                           "separate all four t, on the primary slot hv8, with all positive "
                           "controls passing")
    else:
        OUTCOME = "DISCREPANT"
        OUTCOME_REASON = f"hv8 verdict cells: {hv8}"

print()
print("=" * 78)
print(f"VERDICT: {OUTCOME}")
print(f"REASON: {OUTCOME_REASON}")
print("=" * 78)

# ==========================================================================
# write JSON results
# ==========================================================================
import json


def field_json(u):
    return {"rational_part": str(u[0]), "q_part": str(u[1]), "display": ffmt(u)}


out = {
    "id": "B1113",
    "title": "THE JORDAN t-METER -- verification of JORDAN_MEMO.md section B",
    "outcome": OUTCOME,
    "outcome_reason": OUTCOME_REASON,
    "runtime_seconds": round(RUNTIME_S, 2),
    "field": "Q(q)/(q^2-q+1), q a primitive 6th root of unity; pairs (x,y) = x+y*q",
    "positive_controls": {
        "control_1_rho27_chevalley_brackets_3003_pairs": CONTROL_1_PASS,
        "control_2_principal_string_content_16_8_0": CONTROL_2_PASS,
        "control_3_relator_identity_on_27": CONTROL_3_PASS,
        "control_4_h1_M_27_equals_3_fox_calculus": {"pass": CONTROL_4_PASS, "computed_value": H1_M_27},
        "control_5_dial_centralizes_meridian_all_slots_all_t": CONTROL_5_PASS,
        "all_controls_pass": ALL_CONTROLS_PASS,
        "sanity_matrix_commutator_trace_always_zero": MAT_COMM_ALWAYS_ZERO,
        "t0_sharp_prediction_confirmed": T0_PREDICTIONS_OK,
    },
    "operator_reconstruction": {
        "A": "A27 = rho(a), the meridian/peripheral generator (the seam); shared, unsubscripted",
        "B_L": "B27 = rho(b), untwisted, left copy",
        "B_R(t)": "D(t).B27.D(t)^-1, D(t)=exp(t.rho(x_slot)), conjugation-twisted, right copy",
        "bracket_convention": "[B_L,B_R] reported as the GROUP commutator B_L.B_R.B_L^-1.B_R^-1 "
                               "(the Lie/matrix commutator trace is identically zero for any two "
                               "square matrices and is reported separately as a sanity check, not "
                               "as a candidate reading)",
        "dial_slots_tested": list(SLOTS.keys()),
        "primary_slot": "hv8",
    },
    "traces": {
        slot_name: {
            tname: {
                "tr_A_BR": field_json(results[(slot_name, tname)]["trA_BR"]),
                "tr_BL_BR": field_json(results[(slot_name, tname)]["trBL_BR"]),
                "tr_matrix_commutator_sanity": field_json(results[(slot_name, tname)]["tr_mat_comm"]),
                "tr_group_commutator": field_json(results[(slot_name, tname)]["tr_group_comm"]),
            }
            for tname in TVALS
        }
        for slot_name in SLOTS
    },
    "verdict_per_slot": {
        slot_name: {
            "dial_blind_tr_A_BR": VERDICT[slot_name]["dial_blind"],
            "dial_blind_value": VERDICT[slot_name]["dial_blind_value"],
            "tr_BL_BR_separates_all_t": VERDICT[slot_name]["trBL_BR_separates_all"],
            "tr_BL_BR_pairwise": VERDICT[slot_name]["trBL_BR_pairs"],
            "tr_group_commutator_separates_all_t": VERDICT[slot_name]["tr_group_comm_separates_all"],
            "tr_group_commutator_pairwise": VERDICT[slot_name]["tr_group_comm_pairs"],
        }
        for slot_name in SLOTS
    },
    "memo_number_cross_check": memo_match,
    "paths": {
        "ccb_path_used": CCB_PATH,
        "cert_reference_path": CERT_PATH_INFO,
    },
}

RESULTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "b1113_results.json")
with open(RESULTS_PATH, "w") as fh:
    json.dump(out, fh, indent=2)
say(f"results written to {RESULTS_PATH}")
