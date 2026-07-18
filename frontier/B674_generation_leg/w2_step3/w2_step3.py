#!/usr/bin/env python3
# w2_step3.py -- STEP (iii): the coefficient comparison (PREREG_W2.md, sealed
# sha b4c9a6bb; step (iii) UNLOCKED by the cc2 gate, GATE_VERIFIED_CC.md).
#
# Sealed frame (verbatim from the banked record):
#   - Molien doublet (step ii): M(q)  = phi^2      * prod_{k>=1} prod_t (1 - zeta10^t q^k)^{-m_k(t)}
#                               M'(q) = (1-phi)^2  * same with the conjugate seed (t -> 3t)
#     weight-step grading g(k) = k (INTEGER q-support; the reduced side of the
#     Yang-Lee convention) -- exactly as step_ii_support.md wrote the product.
#   - Sealed dressing (banked B672 recognition, used verbatim):
#       comp_a = q^{nu_a} * eta^{48/5} * (reduced series),  nu = (0, 1/5),
#       eta^{48/5} = q^{2/5} * (q;q)_infty^{48/5}  (carries q^{2/5} exactly).
#   - Targets (banked W33 / B672): Y^(5)_2hat = (F1, F2) * eta^{48/5} with
#       F1 = N1/(q;q)^{3/5}, F2 = q^{1/5} N2/(q;q)^{3/5},
#       N1 = (q^2;q^5)(q^3;q^5)(q^5;q^5), N2 = (q;q^5)(q^4;q^5)(q^5;q^5).
#     Reduced-side target streams = F1_stream, F2_stream (banked JSON, 42 terms);
#     dressed-side integer streams = N1*(q;q)^9, N2*(q;q)^9 (banked, 60 terms).
#   - Freedom: ONE rational constant in the eta-bookkeeping. Nothing else.
#   - Outcome vocabulary: MATCH / STRUCTURED NEAR-MISS / KILLED-AT-(iii).
#
# All arithmetic exact: Fraction pairs (a, b) meaning a + b*sqrt5.
# Paths are __file__-relative. Coefficients computed: n = 0..119 (>= 100).
#
# GRADE EXTENSION (declared): coefficients n <= 40 use ONLY gate-verified
# grades k <= 40 (eigen_distribution.json, cc2-gate exact agreement).
# Coefficients n = 41..119 additionally use the closed-form law recorded in
# the gate artifact itself ("closed_form_law"), verified here to reproduce
# every banked grade k = 0..40 exactly before being used for k = 41..119.

import json, math, os, sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ARC = os.path.dirname(HERE)
GATE_JSON = os.path.join(ARC, "w2_molien_cell", "eigen_distribution.json")
W33_JSON = os.path.join(ARC, "..", "B666_leads_campaign", "cellW33",
                        "cellW33_doublet_streams.json")
OUT_TXT = os.path.join(HERE, "step3_output.txt")
OUT_JSON = os.path.join(HERE, "coefficients_both_conjugates.json")

N = 120  # number of q-coefficients (0..119), >= 100 per the sealed prereg

_out_lines = []
def emit(s=""):
    _out_lines.append(s)
    print(s)

FAILS = []
def gate(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILS.append(name)
    emit("  [%s] %s%s" % (tag, name, ("  [" + detail + "]") if detail else ""))
    return ok

# ---------- Q(sqrt5) exact arithmetic: x = (a, b) = a + b*sqrt5 ----------
ZERO = (Fr(0), Fr(0)); ONE = (Fr(1), Fr(0))
def q5(a, b=0): return (Fr(a), Fr(b))
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def mul(x, y): return (x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def smul(c, x): return (c*x[0], c*x[1])
def conj(x): return (x[0], -x[1])
def inv(x):
    n = x[0]*x[0] - 5*x[1]*x[1]
    if n == 0: raise ZeroDivisionError
    return (x[0]/n, -x[1]/n)
def q5float(x): return float(x[0]) + float(x[1])*math.sqrt(5)
def q5str(x):
    return "%s + %s*sqrt5" % (x[0], x[1])
PHI = q5(Fr(1, 2), Fr(1, 2))               # phi = (1+sqrt5)/2
PHI2 = mul(PHI, PHI)                        # phi^2 = (3+sqrt5)/2
ONE_M_PHI = sub(ONE, PHI)                   # 1-phi
CPHI2 = mul(ONE_M_PHI, ONE_M_PHI)           # (1-phi)^2 = (3-sqrt5)/2

# c(r) = zeta10^r + zeta10^{-r} exactly (zeta10 = e^{i pi/5})
CTAB = {0: q5(2), 1: PHI, 2: sub(PHI, ONE), 3: sub(ONE, PHI), 4: smul(Fr(-1), PHI), 5: q5(-2)}
def c_of(r):
    r %= 10
    return CTAB[min(r, 10 - r)]

# ---------- series helpers (lists of Q(sqrt5) pairs, length N) ----------
def ser_mul(A, B, n=N):
    C = [ZERO]*n
    for i, ai in enumerate(A):
        if i >= n or ai == ZERO: continue
        for j in range(0, n - i):
            bj = B[j]
            if bj == ZERO: continue
            C[i+j] = add(C[i+j], mul(ai, bj))
    return C
def ser_exp(L, n=N):
    E = [ZERO]*n; E[0] = ONE
    for m in range(1, n):
        s = ZERO
        for j in range(1, m+1):
            if L[j] == ZERO: continue
            s = add(s, smul(Fr(j), mul(L[j], E[m-j])))
        E[m] = smul(Fr(1, m), s)
    return E
def ser_inv(A, n=N):
    B = [ZERO]*n; B[0] = inv(A[0])
    for m in range(1, n):
        s = ZERO
        for j in range(1, m+1):
            if A[j] == ZERO: continue
            s = add(s, mul(A[j], B[m-j]))
        B[m] = smul(Fr(-1), mul(B[0], s))
    return B
def ser_pow(A, e, n=N):
    R = [ZERO]*n; R[0] = ONE; base = A[:]
    while e:
        if e & 1: R = ser_mul(R, base, n)
        e >>= 1
        if e: base = ser_mul(base, base, n)
    return R
def rat_ser(A):  # rational series -> Q(sqrt5) series
    return [(Fr(x), Fr(0)) for x in A]

# ---------- PART A: gate artifact + law verification ----------
emit("== PART A: the gate artifact and the closed-form law ==")
gj = json.load(open(GATE_JSON))
GP = gj["GATE_PRIMARY"]

def law_mults(k):
    # m_k(t) = 2k+1 at t = 5k+-1 (mod 10); 2k at other classes of parity
    # k+1 (mod 2); 0 at parity k (mod 2).  (gate artifact "closed_form_law")
    m = {}
    hi = {(5*k + 1) % 10, (5*k - 1) % 10}
    for t in range(10):
        if t % 2 == (k + 1) % 2:
            v = (2*k + 1) if t in hi else 2*k
            if v: m[t] = v
    return m

ok = True
for ks, rec in GP.items():
    k = int(ks)
    banked = {int(t): v for t, v in rec["mult_by_zeta10_exponent"].items()}
    if banked != law_mults(k): ok = False; break
    if rec["dim"] != 2*(5*k + 1): ok = False; break
    if sum(banked.values()) != 2*(5*k + 1): ok = False; break
    if any(banked.get(t, 0) != banked.get((10 - t) % 10, 0) for t in range(10)):
        ok = False; break
gate("closed-form law == banked GATE_PRIMARY, ALL grades k=0..40 (mults, dims, t<->-t)", ok)
gate("41 grades present in the gate artifact", len(GP) == 41, "len=%d" % len(GP))
emit("  GRADE EXTENSION DECLARED: k=41..%d via the gate artifact's own closed_form_law" % (N - 1))
emit("  (verified above against every banked grade; coefficients n<=40 use ONLY gate-verified grades)")

# ---------- PART B: the Molien doublet, exact ----------
emit("")
emit("== PART B: the Molien doublet M, M' to %d coefficients, exact in Q(sqrt5) ==" % N)

def trace_Wj(k, j):
    # tr(W^j | V_k) from the distribution (law form, verified == banked k<=40)
    if k % 2 == 0:
        return add(add(smul(Fr(2*k + 1), c_of(j)), smul(Fr(2*k), c_of(3*j))),
                   q5(2*k * (-1 if j % 2 else 1)))
    else:
        return add(add(smul(Fr(2*k + 1), c_of(4*j)), smul(Fr(2*k), c_of(2*j))),
                   q5(2*k))

ok = all(trace_Wj(k, 1) == (PHI if k % 2 == 0 else smul(Fr(-1), PHI)) for k in range(0, N))
gate("trace law tr(W|V_k) = (-1)^k phi reproduced from the distribution, k=0..%d" % (N-1), ok)

L = [ZERO]*N
for k in range(1, N):
    for j in range(1, (N - 1)//k + 1):
        L[j*k] = add(L[j*k], smul(Fr(1, j), trace_Wj(k, j)))
E = ser_exp(L)
M = [mul(PHI2, e) for e in E]        # M(q)  = phi^2 * exp(sum ...)
Mc = [conj(x) for x in M]            # M'(q) = Galois conjugate series

gate("grade-0 constants: M_0 = phi^2, M'_0 = (1-phi)^2, gap sqrt5",
     M[0] == PHI2 and Mc[0] == CPHI2 and sub(M[0], Mc[0]) == q5(0, 1))

# cross-check 1: direct product route (no exp/log), first NCK coefficients
NCK = 24
S = [ZERO]*NCK; S[0] = ONE
for k in range(1, NCK):
    if k % 2 == 0:
        facs = [([ONE, smul(Fr(-1), PHI), ONE], 2*k + 1),
                ([ONE, smul(Fr(-1), ONE_M_PHI), ONE], 2*k),
                ([ONE, ONE], 2*k)]
    else:
        facs = [([ONE, PHI, ONE], 2*k + 1),
                ([ONE, ONE_M_PHI, ONE], 2*k),
                ([ONE, smul(Fr(-1), ONE)], 2*k)]
    for poly, e in facs:
        f = [ZERO]*NCK
        for i, cf in enumerate(poly):
            if i*k < NCK: f[i*k] = cf
        S = ser_mul(S, ser_pow(ser_inv(f, NCK), e, NCK), NCK)
S = [mul(PHI2, x) for x in S]
gate("cross-check (independent route): direct product == exp route, n<%d" % NCK,
     all(S[n] == M[n] for n in range(NCK)))

# cross-check 2: conjugate-seed direct build (t -> 3t) == conj(M), first NCK
Lc = [ZERO]*NCK
for k in range(1, NCK):
    for j in range(1, (NCK - 1)//k + 1):
        if k % 2 == 0:
            t = add(add(smul(Fr(2*k + 1), c_of(3*j)), smul(Fr(2*k), c_of(9*j))),
                    q5(2*k * (-1 if j % 2 else 1)))
        else:
            t = add(add(smul(Fr(2*k + 1), c_of(2*j)), smul(Fr(2*k), c_of(4*j))),
                    q5(2*k))
        Lc[j*k] = add(Lc[j*k], smul(Fr(1, j), t))
Ec = ser_exp(Lc, NCK)
gate("cross-check: conjugate-seed (t->3t) build == conj(M) coefficientwise, n<%d" % NCK,
     all(mul(CPHI2, Ec[n]) == Mc[n] for n in range(NCK)))

# ring landing
def in_Zphi(x):
    return (2*x[0]).denominator == 1 and (2*x[1]).denominator == 1 \
        and (x[0] - x[1]).denominator == 1
all_Zphi = all(in_Zphi(x) for x in M)
tr_int = all((x[0] + y[0]).denominator == 1 and x[1] + y[1] == 0
             for x, y in zip(M, Mc))
gate("coefficient ring: every M_n lands in Z[phi] (and M+M' in Z)", all_Zphi and tr_int)
emit("  first coefficients M : " + "; ".join(q5str(M[n]) for n in range(4)))
emit("  first coefficients M': " + "; ".join(q5str(Mc[n]) for n in range(4)))

# ---------- PART C: the banked targets, reconstructed and verified ----------
emit("")
emit("== PART C: the W33/B672 targets to %d terms, verified against the banked JSON ==" % N)
wj = json.load(open(W33_JSON))
F1_banked = [Fr(x) for x in wj["F1_stream"]]
F2_banked = [Fr(x) for x in wj["F2_stream"]]
Y1_banked = [Fr(x) for x in wj["doublet_streams_integer"]["2hat.comp1"]]
Y2_banked = [Fr(x) for x in wj["doublet_streams_integer"]["2hat.comp2"]]

def sparse_prod(residues, n=N):  # prod_{m>=1, m mod 5 in residues} (1 - q^m)
    S = [Fr(0)]*n; S[0] = Fr(1)
    for m in range(1, n):
        if m % 5 in residues:
            for i in range(n - 1, m - 1, -1):
                S[i] -= S[i - m]
    return S
def qq_pow(alpha, n=N):  # (q;q)_infty^alpha = exp(-alpha * sum_{m} D_m q^m)
    Lr = [Fr(0)]*n
    for m in range(1, n):
        Lr[m] = -alpha * sum(Fr(1, j) for j in range(1, m + 1) if m % j == 0)
    E = [Fr(0)]*n; E[0] = Fr(1)
    for m in range(1, n):
        E[m] = sum(Fr(j)*Lr[j]*E[m - j] for j in range(1, m + 1)) / m
    return E

N1 = sparse_prod({2, 3, 0}); N2 = sparse_prod({1, 4, 0})
QQm35 = qq_pow(Fr(-3, 5)); QQ9 = qq_pow(Fr(9)); QQ485 = qq_pow(Fr(48, 5))
def rmul(A, B, n=N):
    C = [Fr(0)]*n
    for i, ai in enumerate(A):
        if ai == 0: continue
        for j in range(n - i):
            if B[j]: C[i + j] += ai*B[j]
    return C
F1 = rmul(N1, QQm35); F2s = rmul(N2, QQm35)     # reduced target streams
Y1 = rmul(N1, QQ9);   Y2 = rmul(N2, QQ9)        # dressed integer streams

gate("recomputed F1 stream == banked (all %d banked terms)" % len(F1_banked),
     all(F1[i] == F1_banked[i] for i in range(len(F1_banked))))
gate("recomputed F2 stream == banked (all %d banked terms)" % len(F2_banked),
     all(F2s[i] == F2_banked[i] for i in range(len(F2_banked))))
gate("recomputed Y_2hat.comp1 = N1*(q;q)^9 == banked (all %d terms)" % len(Y1_banked),
     all(Y1[i] == Y1_banked[i] for i in range(len(Y1_banked))))
gate("recomputed Y_2hat.comp2 = N2*(q;q)^9 == banked (all %d terms)" % len(Y2_banked),
     all(Y2[i] == Y2_banked[i] for i in range(len(Y2_banked))))
gate("banked identity re-proved as series: F1*(q;q)^{48/5} == N1*(q;q)^9, n<%d" % N,
     rmul(F1, QQ485) == Y1)
gate("banked identity re-proved as series: F2s*(q;q)^{48/5} == N2*(q;q)^9, n<%d" % N,
     rmul(F2s, QQ485) == Y2)
b1 = all(abs(x) <= 1 for x in F1); b2 = all(abs(x) <= 1 for x in F2s)
gate("W33 bounded finding reproduced: |F1_n|, |F2_n| <= 1 for all n<%d" % N, b1 and b2)
emit("  class bookkeeping: dressed classes (2/5, 3/5) select the 2hat doublet")
emit("  (2hat' lives at classes (1/5, 4/5) -- outside the sealed step-(ii) landing).")

# dressed Molien streams (the sealed dressing, applied verbatim):
#   comp_a = q^{nu_a} * eta^{48/5} * M_a  ==>  integer-power stream part =
#   (q;q)^{48/5} * M_a, carried at class nu_a + 2/5.
QQ485_5 = rat_ser(QQ485)
DM = ser_mul(M, QQ485_5)      # dressed comp (trace-phi conjugate), class 2/5 or 3/5 per nu
DMc = [conj(x) for x in DM]   # dressed conjugate stream ((q;q)^{48/5} is rational)
gate("dressing consistency: dressed conjugate == conj(dressed), n<%d" % N,
     all(ser_mul(Mc, QQ485_5)[n] == DMc[n] for n in range(N)))

# ---------- PART D: THE SEALED COMPARISON ----------
emit("")
emit("== PART D: the sealed comparison (>= 100 coefficients, both conjugates x both components) ==")

def as5(r): return (Fr(r), Fr(0))
def first_mm(A, B):
    for n in range(N):
        if A[n] != as5(B[n]): return n
    return None
def ratio(Bn, An):
    return mul(as5(Bn), inv(An)) if An != ZERO else None

PAIRS = [("M  vs F1 (reduced)", M, F1), ("M  vs F2 (reduced)", M, F2s),
         ("M' vs F1 (reduced)", Mc, F1), ("M' vs F2 (reduced)", Mc, F2s),
         ("dressed M  vs Y_2hat.comp1", DM, Y1), ("dressed M  vs Y_2hat.comp2", DM, Y2),
         ("dressed M' vs Y_2hat.comp1", DMc, Y1), ("dressed M' vs Y_2hat.comp2", DMc, Y2)]
results = {}
for name, A, B in PAIRS:
    n0 = first_mm(A, B)
    r0 = ratio(B[0], A[0]); r1 = ratio(B[1], A[1])
    const_alg = (r0 is not None and r1 is not None and r0 == r1)
    if const_alg:  # extend the constancy check over the full window
        const_alg = all((A[n] == ZERO and B[n] == 0) or
                        (A[n] != ZERO and ratio(B[n], A[n]) == r0) for n in range(N))
    rational_c = const_alg and r0[1] == 0
    results[name] = dict(first_mismatch=n0,
                         r0=None if r0 is None else q5str(r0),
                         r1=None if r1 is None else q5str(r1),
                         one_algebraic_constant=bool(const_alg),
                         one_RATIONAL_constant=bool(rational_c))
    emit("  %s: first mismatch at n=%s; target/molien ratio r_0 = %s, r_1 = %s;" %
         (name, n0, results[name]["r0"], results[name]["r1"]))
    emit("      single ALGEBRAIC constant works: %s; single RATIONAL constant works: %s" %
         (const_alg, rational_c))

emit("")
emit("  -- the sealed one-rational-constant freedom, decided at n=0 --")
emit("  M_0  = phi^2   = %s;  target comp streams start at 1" % q5str(M[0]))
emit("  c * phi^2 = 1 requires c = phi^{-2} = %s : NOT rational" % q5str(inv(PHI2)))
emit("  c * (1-phi)^2 = 1 requires c = (1-phi)^{-2} = %s : NOT rational" % q5str(inv(CPHI2)))
emit("  => NO rational constant (shared or even per-component) survives n=0, any orientation")
emit("")
emit("  -- the diagnostic single ALGEBRAIC constant, decided at n=1 --")
emit("  after normalizing away the grade-0 unit: M_1/M_0 = %s vs F1_1 = 3/5, F2_1 = -2/5" %
     q5str(mul(M[1], inv(M[0]))))
emit("  M'_1/M'_0 = %s  -- neither equals 3/5 nor -2/5" % q5str(mul(Mc[1], inv(Mc[0]))))
emit("  ratio drift witnesses (M vs F1): r_0 = %s ; r_1 = %s ; r_0 != r_1" %
     (results["M  vs F1 (reduced)"]["r0"], results["M  vs F1 (reduced)"]["r1"]))

# growth separation (exact witnesses, no asymptotic claim)
emit("")
emit("  -- growth separation (exact coefficients at checkpoints; n<=40 is gate-verified-only region) --")
emit("  %4s | %28s | %14s | %14s | %s" % ("n", "|M_n| (approx of exact)", "F1_n", "Y1_n (int)", "|DM_n| approx"))
CKPTS = [1, 2, 5, 10, 20, 40, 60, 80, 100, 119]
growth = []
for n in CKPTS:
    growth.append(dict(n=n, M_abs=abs(q5float(M[n])), F1=str(F1[n]),
                       Y1=str(Y1[n]), DM_abs=abs(q5float(DM[n]))))
    emit("  %4d | %28.6g | %14s | %14s | %.6g" %
         (n, abs(q5float(M[n])), str(F1[n])[:14], str(Y1[n])[:14], abs(q5float(DM[n]))))
mono = all(abs(q5float(DM[CKPTS[i+1]])) > 10*abs(q5float(DM[CKPTS[i]])) for i in range(4, len(CKPTS)-1))
emit("  dressed-Molien/target excess at n=40: |DM_40|/|Y1_40| = %.6g ; at n=100: %.6g" %
     (abs(q5float(DM[40])/float(Y1[40])) if Y1[40] else float('inf'),
      abs(q5float(DM[100])/float(Y1[100])) if Y1[100] else float('inf')))

# ---------- PART E: diagnostics for the kill bank (DIAGNOSTIC-ONLY; ----------
# ---------- outside the sealed comparison; hint-grade patterns) ----------
emit("")
emit("== PART E: diagnostics for the kill bank (labeled; outside the sealed pairings) ==")

def v5den(fr):  # 5-adic valuation of the denominator of a Fraction
    d = fr.denominator; v = 0
    while d % 5 == 0: d //= 5; v += 1
    return v
def pure5(fr):
    d = fr.denominator
    while d % 5 == 0: d //= 5
    return d == 1

# (e1) 5-adic ring separation, reduced side
p5 = all(pure5(x) for x in F1) and all(pure5(x) for x in F2s)
v5F = [max(v5den(F1[n]), v5den(F2s[n])) for n in range(N)]
gate("(e1) reduced targets: denominators are PURE 5-powers, n<%d (banked W33 fact reproduced)" % N, p5)
emit("      v5(denom) checkpoints n=1,10,40,80,119: %s ; max in window = %d (non-decreasing envelope)" %
     ([v5F[n] for n in [1, 10, 40, 80, 119]], max(v5F)))
emit("      vs the Molien doublet: EVERY M_n, M'_n in Z[phi] (v5 of denominators = 0, all n<%d)" % N)
emit("      => ONE constant c (rational OR algebraic) has FIXED v5(c); it cannot map a" )
emit("         5-integral stream onto denominators 5^v with v growing -- the same 5-adic")
emit("         exclusion pattern W33 banked against the ladder, now killing the Molien lift.")

# (e2) 5-adic separation, dressed side
v5DM = [max(v5den(DM[n][0]), v5den(DM[n][1])) for n in range(N)]
emit("  (e2) dressed Molien (q;q)^{48/5}*M: v5(denom) checkpoints n=1,10,40,80,119: %s (max %d)" %
     ([v5DM[n] for n in [1, 10, 40, 80, 119]], max(v5DM)))
gate("(e2) dressed Molien is NOT 5-integral while the dressed targets Y_2hat are integers",
     max(v5DM) > 0)

# (e3) paired rational combos (examined so the bank shows they fail too)
TRC = [add(x, y) for x, y in zip(M, Mc)]                    # M + M'  (in Z)
DIF = [smul(Fr(1, 5), mul(q5(0, 1), sub(x, y))) for x, y in zip(M, Mc)]  # (M-M')/sqrt5 (in Z)
DTR = [add(x, y) for x, y in zip(DM, DMc)]
DDF = [smul(Fr(1, 5), mul(q5(0, 1), sub(x, y))) for x, y in zip(DM, DMc)]
for nm, A, B in [("(M+M') vs F1", TRC, F1), ("(M-M')/sqrt5 vs F1", DIF, F1),
                 ("(M-M')/sqrt5 vs F2", DIF, F2s),
                 ("dressed (M-M')/sqrt5 vs Y_2hat.comp1", DDF, Y1),
                 ("dressed (M-M')/sqrt5 vs Y_2hat.comp2", DDF, Y2),
                 ("dressed (M+M') vs Y_2hat.comp1", DTR, Y1)]:
    n0 = first_mm(A, B)
    w = "" if n0 is None else "  [witness: %s vs %s]" % (q5str(A[n0]), B[n0])
    emit("  (e3) DIAGNOSTIC %s: first mismatch at n=%s%s" % (nm, n0, w))

# (e4) the freeness caveat (GATE_VERIFIED_CC.md), addressed with computed facts
emit("  (e4) the freeness caveat: the kill is NOT a freeness artifact at the decisive")
emit("       coefficients -- n=0 uses only V_0 = span(F1,F2) (dim 2, free by definition;")
emit("       grade-0 factor phi^{+-2} exact) and n=1 uses only V_1 (gate-verified");
emit("       distribution, cc2-agreed). No freeness assumption enters n<=1; the")
emit("       mismatch is already decided there. Freeness first affects which higher")
emit("       grades feed n>=2; it cannot repair the unit phi^{+-2} or the n=1 drift.")

# ---------- VERDICT ----------
emit("")
emit("== VERDICT (sealed vocabulary; two-outcome at every sub-check) ==")
any_match = any(v["first_mismatch"] is None for v in results.values())
any_rat = any(v["one_RATIONAL_constant"] for v in results.values())
any_alg = any(v["one_algebraic_constant"] for v in results.values())
emit("  exact MATCH in any orientation (c = 1): %s" % any_match)
emit("  MATCH after the sealed one-rational-constant freedom: %s" % any_rat)
emit("  match after a single ALGEBRAIC constant (diagnostic, outside the freedom): %s" % any_alg)
if any_match or any_rat:
    verdict = "MATCH"
elif any_alg:
    verdict = "STRUCTURED NEAR-MISS"
else:
    verdict = "KILLED-AT-(iii)"
emit("  VERDICT: %s" % verdict)
emit("  gate failures in this cell: %d %s" % (len(FAILS), FAILS if FAILS else ""))

# ---------- artifacts ----------
def fs(x): return str(x)  # Fraction -> "p/q"
json.dump({
  "artifact": "coefficients_both_conjugates.json (STEP (iii), PREREG_W2 sealed b4c9a6bb)",
  "conventions": {
    "field": "Q(sqrt5); every coefficient stored as [a, b] meaning a + b*sqrt5 (exact Fractions)",
    "molien": "M(q) = phi^2 * prod_{k>=1} prod_t (1 - zeta10^t q^k)^{-m_k(t)}, weight-step grading g(k)=k (step_ii_support.md verbatim); M' = Galois conjugate (seed t->3t == sqrt5 -> -sqrt5)",
    "grades": "k<=40 from the gate artifact eigen_distribution.json (cc2-verified); k=41..119 from the gate artifact's closed_form_law, verified against all 41 banked grades",
    "dressing": "comp_a = q^{nu_a} * eta^{48/5} * reduced, nu=(0,1/5); eta^{48/5} = q^{2/5} (q;q)^{48/5}; dressed integer-part stream = (q;q)^{48/5} * M",
    "targets": "reduced: F1, F2 streams (banked W33 JSON, re-derived from N1/(q;q)^{3/5}, N2/(q;q)^{3/5}); dressed: Y_2hat = N1*(q;q)^9, N2*(q;q)^9 (banked identity re-proved as series here)"
  },
  "coefficient_ring": "every M_n in Z[phi]; M_n + M'_n in Z (verified n<120)",
  "M_coefficients": [[fs(x[0]), fs(x[1])] for x in M],
  "Mconj_coefficients": [[fs(x[0]), fs(x[1])] for x in Mc],
  "dressed_M_coefficients_first60": [[fs(x[0]), fs(x[1])] for x in DM[:60]],
  "targets_F1_first120": [fs(x) for x in F1],
  "targets_F2_first120": [fs(x) for x in F2s],
  "targets_Y2hat_comp1_first120": [fs(x) for x in Y1],
  "targets_Y2hat_comp2_first120": [fs(x) for x in Y2],
  "comparison": results,
  "growth_checkpoints": growth,
  "five_adic_separation": {
    "molien_v5_denominators": "0 for every M_n, M'_n (all in Z[phi], n<120)",
    "reduced_target_v5_denominators_checkpoints_n_1_10_40_80_119": [v5F[n] for n in [1, 10, 40, 80, 119]],
    "dressed_molien_v5_denominators_checkpoints_n_1_10_40_80_119": [v5DM[n] for n in [1, 10, 40, 80, 119]],
    "dressed_targets": "integers (Y_2hat streams)",
    "statement": "a single constant (rational or algebraic) has fixed v5 and cannot bridge integral vs growing 5-power denominators -- the W33 5-adic exclusion pattern, recurring here"
  },
  "verdict": verdict,
}, open(OUT_JSON, "w"), indent=1)
open(OUT_TXT, "w").write("\n".join(_out_lines) + "\n")
emit("")
emit("artifacts written: coefficients_both_conjugates.json, step3_output.txt")
