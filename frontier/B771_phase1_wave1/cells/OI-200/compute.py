#!/usr/bin/env python3
"""OI-200 -- B645/B678: the D4 ceiling value 1.7849887... at (n=10, kappa=8).

CELL TASK (B771 Phase-1 Wave-1, sealed prereg 7955049f): identify the
(n=10, kappa=8) D4 ceiling value exactly.  RECOMPUTE first (do not trust
the stored 39 digits), then PSLQ over extended bases, verify BOTH
directions on 10+ digits.

WHAT THE NUMBER IS (from frontier/B678_d4_annex/d4_level.py conventions):
  SU(3)_k Kac-Peterson modular data (S, T) at level k = 5 (kappa = k+3 = 8).
  Word w = R^m L with m = n-2 = 8 (n = trace of the SL(2,Z) matrix = 10).
  rho(R) = T,  rho(L) = S T^{-1} S^{-1}.
  Z_plus  = Tr(rho(w)) = Tr(T^m S T^{-1} S^{-1})
  Z_minus = det(w0) * Tr(C rho(w)),  C = S^2 (charge conjugation),
            det(w0) = -1 for A2 (w0 is a reflection).
  tr_odd  = (Z_plus + Z_minus)/2       (the theta-parity projected trace)
  CEILING VALUE = |tr_odd|  at (k=5, m=8)  ~ 1.7849887...

MACHINERY REBUILT FROM SCRATCH here (the B678 engine lives on the cc2 seat
and is not importable from this repo; rebuilding is itself an independent
seed).  Kac-Peterson for A2 level k, kappa = k+3:
  primaries: dominant weights (a,b), a,b >= 0, a+b <= k;  N = (k+1)(k+2)/2
  h_{(a,b)} = (a^2+ab+b^2+3a+3b)/(3 kappa),  c = 8k/kappa
  T = diag exp(2 pi i (h - c/24))
  S_{lm} = (i^{|Delta+|}/(kappa sqrt(|P/Q|))) sum_{w in W} eps(w)
             exp(-2 pi i (w(l+rho), m+rho)/kappa)
         = (-i/(kappa sqrt(3))) * (Weyl alternating sum),   rho = (1,1),
  inner product from the A2 quadratic-form matrix G = (1/3)[[2,1],[1,2]].

GATES (hard stops):
  G0 modular battery at k in {2, 5, 9}: S unitary, S symmetric, S^2 = C
     (the conjugation permutation (a,b)->(b,a)), S^4 = I, (ST)^3 = S^2,
     S_{00} > 0.
  G1 banked golden lock:  k=2 (kappa=5), m=1 (fig-8 word RL):
     |tr_odd| = 1/phi  (B584/B238/B678, three prior seats).
  G2 banked cross-campaign lock:  k=9 (kappa=12), m=2 (word RRL):
     |tr_odd| = sqrt(3)-1  (B678 verified against the B4 landscape).
  G3 k=5 row max: the ceiling at k=5 over n=3..10 is attained at n=10
     (this is what makes it the (10, kappa=8) ceiling cell).

VALIDATION (house method): the target is recomputed at TWO precisions
(dps 120 and dps 60, independent runs of the whole pipeline); agreement
digits set the PSLQ tolerance by the sealed rule tol = 10^-(agree-14).
The stored B678 value (39 digits, independent seat) is compared as a
third, not-trusted reference.

IDENTIFICATION TARGETS: x = |tr_odd|; also y = x^2 = |Z|^2, Re(tr_odd),
Im(tr_odd) for a complete row identification.  Sweep: PSLQ minimal
polynomial degree 1..8 on powers of x; extended linear bases
{1, sqrt2, sqrt3, sqrt5, sqrt6, sqrt10, sqrt15, sqrt30, phi} (the failed
B678 basis, recorded); then BOTH-direction verification with sympy exact
minimal_polynomial + irreducibility + 100-digit numeric agreement.
"""
import json
import sys
import time
from fractions import Fraction

import mpmath as mp
import sympy as sp

OUT = {}
T0 = time.time()
FAILED = []


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


def gate(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    log(f"GATE {name}: {status}  {detail}")
    if not ok:
        FAILED.append(name)
        print("HARD STOP: gate failed.", flush=True)
        OUT["failed_gates"] = FAILED
        json.dump(OUT, open(RESULTS, "w"), indent=1, default=str)
        sys.exit(1)


# ---------------------------------------------------------------- Weyl group
def weyl_group():
    """A2 Weyl group as 2x2 integer matrices acting on fundamental-weight
    coordinates (column vectors), with signs det(w) = (-1)^length."""
    s1 = ((-1, 0), (1, 1))    # (a,b) -> (-a, a+b)
    s2 = ((1, 1), (0, -1))    # (a,b) -> (a+b, -b)
    ident = ((1, 0), (0, 1))

    def mul(A, B):
        return tuple(
            tuple(sum(A[i][t] * B[t][j] for t in range(2)) for j in range(2))
            for i in range(2))

    elems = {ident: 1}
    frontier_ = [(ident, 1)]
    while frontier_:
        new = []
        for (M, s) in frontier_:
            for (g, gs) in ((s1, -1), (s2, -1)):
                P = mul(g, M)
                if P not in elems:
                    elems[P] = s * gs
                    new.append((P, s * gs))
        frontier_ = new
    return list(elems.items())


WEYL = weyl_group()
assert len(WEYL) == 6 and sum(s for _, s in WEYL) == 0


def wapply(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])


# ------------------------------------------------------- modular data at k
def su3_modular(k):
    """Return (primaries, S, Tlist, conj_perm) at current mp.mp.dps."""
    kappa = k + 3
    prim = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    N = len(prim)
    idx = {p: i for i, p in enumerate(prim)}
    conj = [idx[(b, a)] for (a, b) in prim]
    pref = mp.mpc(0, -1) / (mp.sqrt(3) * kappa)
    S = mp.matrix(N, N)
    for i, (a, b) in enumerate(prim):
        lam = (a + 1, b + 1)
        for j in range(i, N):
            c_, d_ = prim[j]
            mu = (c_ + 1, d_ + 1)
            tot = mp.mpc(0)
            for (M, sgn) in WEYL:
                wl = wapply(M, lam)
                t = Fraction(
                    2 * wl[0] * mu[0] + wl[0] * mu[1]
                    + wl[1] * mu[0] + 2 * wl[1] * mu[1], 3 * kappa)
                tot += sgn * mp.expjpi(-2 * mp.mpf(t.numerator) / t.denominator)
            val = pref * tot
            S[i, j] = val
            S[j, i] = val
    Tlist = []
    for (a, b) in prim:
        ph = Fraction(a * a + a * b + b * b + 3 * a + 3 * b, 3 * kappa) \
            - Fraction(8 * k, 24 * kappa)
        Tlist.append(mp.expjpi(2 * mp.mpf(ph.numerator) / ph.denominator))
    return prim, S, Tlist, conj


def maxabs(M):
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def modular_battery(k, tag):
    prim, S, Tlist, conj = su3_modular(k)
    N = len(prim)
    I = mp.eye(N)
    Sdag = mp.matrix(N, N)
    for i in range(N):
        for j in range(N):
            Sdag[i, j] = mp.conj(S[j, i])
    e_uni = maxabs(S * Sdag - I)
    e_sym = max(abs(S[i, j] - S[j, i]) for i in range(N) for j in range(N))
    S2 = S * S
    C = mp.matrix(N, N)
    for i in range(N):
        C[i, conj[i]] = 1
    e_C = maxabs(S2 - C)
    e_S4 = maxabs(S2 * S2 - I)
    ST = mp.matrix(N, N)
    for i in range(N):
        for j in range(N):
            ST[i, j] = S[i, j] * Tlist[j]
    e_ST3 = maxabs(ST * ST * ST - S2)
    s00_ok = (S[0, 0].imag == 0 or abs(S[0, 0].imag) < mp.mpf(10) ** (-mp.mp.dps + 10)) \
        and S[0, 0].real > 0
    tol = mp.mpf(10) ** (-mp.mp.dps + 12)
    gate(f"G0[{tag}] S unitary", e_uni < tol, f"err={mp.nstr(e_uni, 3)}")
    gate(f"G0[{tag}] S symmetric", e_sym < tol, f"err={mp.nstr(e_sym, 3)}")
    gate(f"G0[{tag}] S^2 = C(conjugation)", e_C < tol, f"err={mp.nstr(e_C, 3)}")
    gate(f"G0[{tag}] S^4 = I", e_S4 < tol, f"err={mp.nstr(e_S4, 3)}")
    gate(f"G0[{tag}] (ST)^3 = S^2", e_ST3 < tol, f"err={mp.nstr(e_ST3, 3)}")
    gate(f"G0[{tag}] S00 > 0", s00_ok, f"S00={mp.nstr(S[0,0], 8)}")
    return prim, S, Tlist, conj, Sdag


def tr_odd(k, m, data):
    """tr_odd for word R^m L at level k, given (prim,S,Tlist,conj,Sdag)."""
    prim, S, Tlist, conj, Sdag = data
    N = len(prim)
    # L = S T^{-1} S^{-1};  S^{-1} = S^dagger (unitary, gate-checked)
    D = mp.matrix(N, N)
    for i in range(N):
        D[i, i] = mp.conj(Tlist[i])          # |T_i| = 1
    L = S * D * Sdag
    Zp = mp.mpc(0)
    Zm = mp.mpc(0)
    for i in range(N):
        Zp += (Tlist[i] ** m) * L[i, i]
        Zm += (Tlist[conj[i]] ** m) * L[conj[i], i]
    Zm = -Zm                                  # det(w0) = -1 for A2
    return (Zp + Zm) / 2, Zp


def full_pipeline(dps):
    """One complete independent run at the given precision. Returns dict."""
    mp.mp.dps = dps
    log(f"---- pipeline run at dps={dps} ----")
    res = {}
    # gates at k=2 (golden lock)
    d2 = modular_battery(2, f"k=2,dps={dps}")
    z2, _ = tr_odd(2, 1, d2)
    phi = (1 + mp.sqrt(5)) / 2
    err = abs(abs(z2) - 1 / phi)
    gate(f"G1[dps={dps}] golden |tr_odd|(k=2,m=1) = 1/phi",
         err < mp.mpf(10) ** (-dps + 12), f"err={mp.nstr(err, 3)}")
    # target level k=5
    d5 = modular_battery(5, f"k=5,dps={dps}")
    row = {}
    for m in range(1, 9):
        z, zfull = tr_odd(5, m, d5)
        row[m + 2] = z
    zmax_n = max(row, key=lambda n: abs(row[n]))
    gate(f"G3[dps={dps}] k=5 ceiling attained at n=10", zmax_n == 10,
         f"argmax n={zmax_n}")
    z = row[10]
    res["Z"] = z
    res["Zabs"] = abs(z)
    res["row_abs"] = {n: abs(row[n]) for n in row}
    log(f"  (n=10,kappa=8): tr_odd = {mp.nstr(z, min(dps-5, 40))}")
    log(f"  |tr_odd| = {mp.nstr(abs(z), min(dps-5, 40))}")
    return res


RESULTS = __file__.replace("compute.py", "results.json")

# ---------------------------------------------------------------- main runs
log("== STEP 1: independent recomputation, two precisions ==")
run120 = full_pipeline(120)
run60 = full_pipeline(60)

# cross-campaign lock G2 at k=9 (kappa=12), m=2 -> sqrt(3)-1  (N=55; dps 50)
mp.mp.dps = 50
log("---- gate run k=9 at dps=50 (N=55) ----")
d9 = modular_battery(9, "k=9,dps=50")
z9, _ = tr_odd(9, 2, d9)
err9 = abs(abs(z9) - (mp.sqrt(3) - 1))
gate("G2 cross-campaign |tr_odd|(k=9,m=2) = sqrt(3)-1",
     err9 < mp.mpf(10) ** (-38), f"err={mp.nstr(err9, 3)}")

# agreement between the two seeds
mp.mp.dps = 130
x120 = mp.mpf(mp.nstr(run120["Zabs"], 125, strip_zeros=False))
x60 = mp.mpf(mp.nstr(run60["Zabs"], 60, strip_zeros=False))
diff = abs(x120 - x60)
agree = int(mp.floor(-mp.log10(diff / x120))) if diff > 0 else 58
log(f"seed agreement dps120 vs dps60: {agree} digits")
gate("G4 two-seed agreement >= 50 digits", agree >= 50, f"agree={agree}")

# stored B678 value (39 digits, independent seat) -- compared, not trusted
stored = mp.mpf("1.784988724784665521124751704550397770824")
dstored = abs(x120 - stored)
agree_stored = int(mp.floor(-mp.log10(dstored / x120))) if dstored > 0 else 39
log(f"agreement with stored B678 39-digit value: {agree_stored} digits")
OUT["recompute"] = {
    "Zabs_dps120": mp.nstr(run120["Zabs"], 118),
    "Z_dps120": mp.nstr(run120["Z"], 60),
    "seed_agreement_digits": agree,
    "stored_B678_agreement_digits": agree_stored,
}

# ---------------------------------------------------------------- STEP 2 PSLQ
log("== STEP 2: PSLQ identification ==")
tol_exp = agree - 14                       # sealed tolerance-height rule
log(f"tolerance-height rule: tol = 10^-{tol_exp}")

mp.mp.dps = agree
x = +x120                                  # rounded to working precision
tol = mp.mpf(10) ** (-tol_exp)

# (a) minimal-polynomial degree sweep 1..8 on powers of x
sweep = {}
for deg in range(1, 9):
    vec = [x ** j for j in range(deg + 1)]
    maxc = 10 ** 4 if deg < 8 else 10 ** 6
    rel = mp.pslq(vec, tol=tol, maxcoeff=maxc, maxsteps=10 ** 6)
    sweep[deg] = rel
    log(f"  degree {deg} (maxcoeff={maxc}): {rel}")
OUT["pslq_degree_sweep"] = {d: (list(map(int, r)) if r else None)
                           for d, r in sweep.items()}

# (b) the failed B678 extended linear basis, recorded for the ledger.
# NOTE: including phi alongside {1, sqrt5} makes the basis Q-degenerate
# (phi = (1+sqrt5)/2), so PSLQ returns the internal relation 1+sqrt5-2phi=0
# with coefficient 0 on x -- recorded as such; the honest negative is the
# NON-degenerate multiquadratic basis below.
mp.mp.dps = agree
phi_n = (1 + mp.sqrt(5)) / 2
lin_basis = [mp.mpf(1), mp.sqrt(2), mp.sqrt(3), mp.sqrt(5), mp.sqrt(6),
             mp.sqrt(10), mp.sqrt(15), mp.sqrt(30), phi_n, x]
lin_rel = mp.pslq(lin_basis, tol=tol, maxcoeff=10 ** 4, maxsteps=10 ** 6)
log(f"  linear over {{1,sqrt2,sqrt3,sqrt5,sqrt6,sqrt10,sqrt15,sqrt30,phi}}+x: "
    f"{lin_rel}")
if lin_rel is not None:
    gate("G5c degenerate-basis relation does not involve x",
         int(lin_rel[-1]) == 0,
         "internal basis relation only (phi dependent on {1,sqrt5})")
OUT["pslq_linear_multiquadratic_with_phi"] = \
    list(map(int, lin_rel)) if lin_rel else None
lin_basis2 = [mp.mpf(1), mp.sqrt(2), mp.sqrt(3), mp.sqrt(5), mp.sqrt(6),
              mp.sqrt(10), mp.sqrt(15), mp.sqrt(30), x]
lin_rel2 = mp.pslq(lin_basis2, tol=tol, maxcoeff=10 ** 4, maxsteps=10 ** 6)
log(f"  linear over the non-degenerate multiquadratic basis "
    f"{{1,sqrt2,sqrt3,sqrt5,sqrt6,sqrt10,sqrt15,sqrt30}}+x: {lin_rel2}  "
    f"(x is NOT multiquadratic -- this is WHY the B678 attempt failed)")
gate("G5d x not in Q(sqrt2,sqrt3,sqrt5) at height 10^4 (expected negative)",
     lin_rel2 is None, "")
OUT["pslq_linear_multiquadratic"] = \
    list(map(int, lin_rel2)) if lin_rel2 else None

# (c) y = x^2 over the biquadratic basis {1, sqrt2, sqrt3, sqrt6}
y = x * x
y_basis = [mp.mpf(1), y, mp.sqrt(2), mp.sqrt(3), mp.sqrt(6)]
y_rel = mp.pslq(y_basis, tol=tol, maxcoeff=10 ** 4, maxsteps=10 ** 6)
log(f"  y = x^2 over {{1, y, sqrt2, sqrt3, sqrt6}}: {y_rel}")
OUT["pslq_y_biquadratic"] = list(map(int, y_rel)) if y_rel else None
gate("G5 PSLQ found the octic", sweep[8] is not None, str(sweep[8]))
gate("G5b PSLQ found y in Q(sqrt2,sqrt3)", y_rel is not None, str(y_rel))

# ---------------------------------------------------- STEP 3 exact candidate
log("== STEP 3: exact candidate + BOTH-direction verification ==")
X = sp.symbols('x')
c8 = sweep[8]
oct_poly = sp.Poly(sum(int(c8[j]) * X ** j for j in range(9)), X)
if oct_poly.LC() < 0:
    oct_poly = sp.Poly(-oct_poly.as_expr(), X)
log(f"  PSLQ octic: {oct_poly.as_expr()}")
OUT["octic"] = str(oct_poly.as_expr())

irr = oct_poly.is_irreducible
log(f"  octic irreducible over Q: {irr}")
gate("G6 octic irreducible (degree exactly 8)", bool(irr), "")

# candidate from the y-relation: a*1 + b*y + c*sqrt2 + d*sqrt3 + e*sqrt6 = 0
a_, b_, c_, d_, e_ = map(int, y_rel)
y_exact = sp.Rational(-1, b_) * (a_ + c_ * sp.sqrt(2) + d_ * sp.sqrt(3)
                                 + e_ * sp.sqrt(6))
y_exact = sp.nsimplify(sp.expand(y_exact))
cand = sp.sqrt(y_exact)
log(f"  candidate: x = sqrt({y_exact})")
OUT["candidate"] = f"sqrt({y_exact})"

den = sp.sqrtdenest(cand)
log(f"  sqrtdenest attempt: {den}")
OUT["sqrtdenest"] = str(den)

# DIRECTION 1 (numeric -> symbolic): the 120-digit recomputed value
# satisfies the exact octic to ~full precision
mp.mp.dps = 130
resid = sum(int(oct_poly.all_coeffs()[::-1][j]) * x120 ** j for j in range(9))
log(f"  direction 1: |octic(x_recomputed)| = {mp.nstr(abs(resid), 5)}")
gate("G7 direction-1: octic residual < 1e-100",
     abs(resid) < mp.mpf(10) ** (-100), f"resid={mp.nstr(abs(resid), 3)}")

# DIRECTION 2 (symbolic -> numeric): evaluate the exact candidate to 125
# digits and compare against the independent recomputation
cand_num = mp.mpf(sp.N(cand, 128).__str__())
d2v = abs(cand_num - x120)
agree2 = int(mp.floor(-mp.log10(d2v / x120))) if d2v > 0 else 125
log(f"  direction 2: candidate vs recomputed agree to {agree2} digits")
gate("G8 direction-2: >= 100 digits agreement", agree2 >= 100,
     f"agree={agree2}")

# exact minimal polynomial of the candidate == the PSLQ octic (sympy, exact)
mp_cand = sp.minimal_polynomial(cand, X)
same = sp.expand(mp_cand - oct_poly.as_expr()) == 0
log(f"  minimal_polynomial(candidate) = {mp_cand}")
gate("G9 minpoly(candidate) == PSLQ octic (exact, sympy)", same, "")

# Galois structure: the quartic in y factors over Q(sqrt2, sqrt3) with
# conjugate roots 5 + 2s*sqrt3 + 2t*sqrt2 + s*t*sqrt6, s,t = +-1
Y = sp.symbols('y')
quart = sp.expand(sp.prod(
    Y - (5 + 2 * s * sp.sqrt(3) + 2 * t * sp.sqrt(2) + s * t * sp.sqrt(6))
    for s in (1, -1) for t in (1, -1)))
quart_target = sp.expand(oct_poly.as_expr().subs(X, sp.sqrt(Y)))
galois_ok = sp.expand(quart - quart_target) == 0
log(f"  quartic in y = x^2: {sp.expand(quart)}")
gate("G10 y-conjugates are 5+2s*sqrt3+2t*sqrt2+st*sqrt6 (exact)",
     galois_ok, "")

# ------------------------------------------------- bonus: full row identity
log("== STEP 4: complete (n=10,kappa=8) row identification ==")
mp.mp.dps = 120
zre = run120["Z"].real
zim = run120["Z"].imag
re_exact = (1 - sp.sqrt(2)) / 2
re_err = abs(zre - mp.mpf(sp.N(re_exact, 120).__str__()))
log(f"  Re(tr_odd) vs (1-sqrt2)/2: err = {mp.nstr(re_err, 3)}")
im_exact = sp.sqrt(17 + 8 * sp.sqrt(3) - 6 * sp.sqrt(2) - 4 * sp.sqrt(6)) / 2
im_err = abs(zim - mp.mpf(sp.N(im_exact, 120).__str__()))
log(f"  Im(tr_odd) vs sqrt(17+8sqrt3-6sqrt2-4sqrt6)/2: err = {mp.nstr(im_err, 3)}")
# consistency: Re^2 + Im^2 == y_exact, exact
sum_ok = sp.expand(re_exact ** 2 + im_exact ** 2 - y_exact) == 0
gate("G11 Re(tr_odd) = (1-sqrt2)/2 (110+ digits)",
     re_err < mp.mpf(10) ** (-110), f"err={mp.nstr(re_err, 3)}")
gate("G12 Im(tr_odd) = sqrt(17+8sqrt3-6sqrt2-4sqrt6)/2 (110+ digits)",
     im_err < mp.mpf(10) ** (-110), f"err={mp.nstr(im_err, 3)}")
gate("G13 Re^2 + Im^2 == y (exact, sympy)", sum_ok, "")
OUT["row_identity"] = {
    "Re": str(re_exact), "Im": str(im_exact),
    "Zabs2": str(y_exact), "Zabs": f"sqrt({y_exact})"}

OUT["verdict"] = "RESOLVED-A"
OUT["failed_gates"] = FAILED
json.dump(OUT, open(RESULTS, "w"), indent=1, default=str)
log("== DONE: all gates passed; results.json written ==")
print()
print("IDENTIFICATION (verified both directions):")
print(f"  |tr_odd|(n=10, kappa=8) = sqrt({y_exact})")
print(f"  minimal polynomial: {oct_poly.as_expr()}  (irreducible/Q, degree 8)")
print(f"  x^2 in Q(sqrt2, sqrt3); x itself degree 8 (nested radical --")
print(f"  NOT in the multiquadratic Q(sqrt2,sqrt3,sqrt5,phi) B678 searched)")
