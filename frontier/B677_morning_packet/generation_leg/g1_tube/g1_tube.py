#!/usr/bin/env python3
# G1_TUBE -- THE GENERATION LEG, cc2 route (tube-algebra / character candidates).
# PREREG: seat-work/generation_leg/PREREG_G1.md (sealed 2026-07-18, plan 353ca003).
#
# QUESTION: which framework object GENERATES the RR streams
#   comp1 = q^{2/5} N1(q) (q;q)^9,   comp2 = q^{3/5} N2(q) (q;q)^9
# (N1=(q;q)G(q), N2=(q;q)H(q), the Rogers-Ramanujan numerators; banked in
# frontier/B672_grading_hunt/FINDINGS.md + cellG/)?
#
# THREE CANDIDATES, tested in the prereg's stated order (cheapest first):
#   T2  the weld-weighted chiral character sum (Fibonacci/Lee-Yang (2,5)-model
#       characters chi_1, chi_tau, weld = B238's kappa=5 golden-block operator).
#   T1  the double's (Z(Fib)=Fib boxtimes Fib-bar) character sum, weld-weighted
#       via the FULL modular action.
#   T0  the weld-twisted Hochschild graded trace on Tube(Fib).
#
# Mid-run intel (B674, read-only, banked): a *pure trace* functor (Eichler-
# Shimura on Gamma(5)) is TRACE-SILENT for all m -- the RR streams need the
# module/character itself, not its trace. This sharpens expectations here:
# T2/T1 (character-level) get full systematic coverage; T0 (a graded TRACE)
# is run sealed but its likely weakness would corroborate the same pattern.
#
# DISCIPLINE: repo READ-ONLY (only used to read FINDINGS.md/B238/B484 for
# object definitions -- everything below is independently recomputed here,
# nothing executed or written in the repo); exact arithmetic throughout
# (Fraction for q-series; a from-scratch exact Q(zeta_5) cyclotomic-number
# engine for the algebraic/weld side -- Q(zeta_5) properly contains Q(sqrt5)
# as its real subfield, as required for the T-matrix phases + golden data).
import json
import os
import time
from fractions import Fraction as Fr

T_START = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def log(msg=""):
    s = str(msg)
    for ln in s.split("\n"):
        print(ln, flush=True)
        OUT.append(ln)


RESULTS = {}  # assembled into g1_results.json at the end

# =====================================================================
# PART 0 -- exact q-series engine (Fraction coefficients)
# =====================================================================

def smul(a, b, N):
    c = [Fr(0)] * (N + 1)
    for i, ai in enumerate(a):
        if not ai or i > N:
            continue
        for j, bj in enumerate(b):
            if i + j > N:
                break
            if bj:
                c[i + j] += ai * bj
    return c


def sadd(a, b, N):
    c = [Fr(0)] * (N + 1)
    for i in range(N + 1):
        av = a[i] if i < len(a) else Fr(0)
        bv = b[i] if i < len(b) else Fr(0)
        c[i] = av + bv
    return c


def spow(a, n, N):
    r = [Fr(1)] + [Fr(0)] * N
    base = a[: N + 1] + [Fr(0)] * max(0, N + 1 - len(a))
    while n:
        if n & 1:
            r = smul(r, base, N)
        base = smul(base, base, N)
        n >>= 1
    return r


def sinv(a, N):
    assert a[0] == 1
    inv = [Fr(1)] + [Fr(0)] * N
    for n in range(1, N + 1):
        s = Fr(0)
        for k in range(1, n + 1):
            if k < len(a) and a[k]:
                s += a[k] * inv[n - k]
        inv[n] = -s
    return inv


def slog(a, N):
    """formal log of a series with a[0] == 1."""
    assert a[0] == 1
    l = [Fr(0)] * (N + 1)
    for n in range(1, N + 1):
        s = Fr(0)
        for k in range(1, n):
            if n - k < len(a) and a[n - k]:
                s += k * l[k] * a[n - k]
        an = a[n] if n < len(a) else Fr(0)
        l[n] = an - s / n
    return l


def sexp(l, N):
    """formal exp of a series with l[0] == 0 (inverse of slog)."""
    assert l[0] == 0
    e = [Fr(1)] + [Fr(0)] * N
    for n in range(1, N + 1):
        s = Fr(0)
        for k in range(1, n + 1):
            lk = l[k] if k < len(l) else Fr(0)
            if lk:
                s += k * lk * e[n - k]
        e[n] = s / n
    return e


def spow_frac(a, r, N):
    """a^r for rational r, a[0]==1, via exp(r * log(a)). Exact (Fraction)."""
    la = slog(a, N)
    return sexp([r * x for x in la], N)


def euler_prod(residues, modulus, N):
    """prod over k>=1, k mod modulus in residues, of (1 - q^k)."""
    r = [Fr(1)] + [Fr(0)] * N
    for k in range(1, N + 1):
        if k % modulus in residues:
            new = [Fr(0)] * (N + 1)
            for i, ri in enumerate(r):
                if ri:
                    new[i] += ri
                    if i + k <= N:
                        new[i + k] -= ri
            r = new
    return r


def theta_num(c, N):
    """sum_{m in Z} (-1)^m q^{m(5m+c)/2}  (c=1 -> N1, c=3 -> N2 numerator)."""
    s = [Fr(0)] * (N + 1)
    m = 0
    while True:
        hit = False
        for mm in ([0] if m == 0 else [m, -m]):
            e2 = mm * (5 * mm + c)
            if e2 % 2 != 0:
                continue
            e = e2 // 2
            if 0 <= e <= N:
                s[e] += Fr((-1) ** (mm % 2))
                hit = True
        if not hit and m > 0 and (m * (5 * m - abs(c))) // 2 > N:
            break
        m += 1
        if m > 20 * (N + 10):
            break
    return s


def qq_n(n, N):
    """(q;q)_n = prod_{i=1}^n (1-q^i)."""
    r = [Fr(1)] + [Fr(0)] * N
    for i in range(1, n + 1):
        if i > N:
            break
        new = [Fr(0)] * (N + 1)
        for idx, val in enumerate(r):
            if val:
                new[idx] += val
                if idx + i <= N:
                    new[idx + i] -= val
        r = new
    return r


def rr_sum(exp_fn, N):
    """sum_n q^{exp_fn(n)} / (q;q)_n, truncated to N terms -- the RR SUM route."""
    acc = [Fr(0)] * (N + 1)
    n = 0
    while True:
        e = exp_fn(n)
        if e > N:
            break
        qqn = qq_n(n, N - e)
        inv = sinv(qqn, N - e)
        for i, v in enumerate(inv):
            if v and e + i <= N:
                acc[e + i] += v
        n += 1
    return acc


def ints(s, upto=None):
    out = []
    for x in s[: (upto if upto else len(s))]:
        out.append(int(x) if x.denominator == 1 else x)
    return out


log("=" * 100)
log("G1_TUBE -- the generation leg, tube-algebra/character candidates (T2/T1/T0)")
log("=" * 100)

# =====================================================================
# PART 1 -- TARGET REPRODUCTION (independent of the banked repo numbers;
# only the FINDINGS.md *formula* is used: comp1=q^{2/5}N1(q)(q;q)^9,
# comp2=q^{3/5}N2(q)(q;q)^9, N1=(q;q)G(q), N2=(q;q)H(q)).
# Three independent routes must agree exactly to >= 120 terms, or STOP.
# =====================================================================
log("\n" + "=" * 100)
log("PART 1 -- TARGET REPRODUCTION (three independent routes, >=150 terms)")
log("=" * 100)

N = 160  # comparison horizon, well above the required 120

# Route A: RR SUM formula
G_sum = rr_sum(lambda n: n * n, N)
H_sum = rr_sum(lambda n: n * n + n, N)

# Route B: RR PRODUCT (Euler product) formula
G_prod = sinv(euler_prod({1, 4}, 5, N), N)
H_prod = sinv(euler_prod({2, 3}, 5, N), N)

route_AB_G = (G_sum == G_prod)
route_AB_H = (H_sum == H_prod)
log("Route A (RR sum: sum q^n^2/(q;q)_n)      vs Route B (Euler product 1/[(q;q^5)(q^4;q^5)]):")
log("  G(q) agree to %d terms: %s" % (N, route_AB_G))
log("  H(q) agree to %d terms: %s" % (N, route_AB_H))
assert route_AB_G and route_AB_H, "STOP: independent RR sum/product routes disagree"

# Route C: theta / Jacobi-triple-product numerator (N1=(q;q)G, N2=(q;q)H)
E1 = euler_prod({0, 1, 2, 3, 4}, 5, N)  # (q;q)_infty
N1_theta = theta_num(1, N)
N2_theta = theta_num(3, N)
E1inv = sinv(E1, N)
G_theta = smul(N1_theta, E1inv, N)
H_theta = smul(N2_theta, E1inv, N)
route_C_G = (G_theta == G_sum)
route_C_H = (H_theta == H_sum)
log("Route C (theta/JTP numerator N1,N2 divided by (q;q)) vs Route A (sum):")
log("  G(q) agree to %d terms: %s" % (N, route_C_G))
log("  H(q) agree to %d terms: %s" % (N, route_C_H))
assert route_C_G and route_C_H, "STOP: theta-numerator route disagrees with the RR sum route"

log("\n=> ALL THREE independent routes (sum / Euler product / theta-JTP numerator)")
log("   agree EXACTLY to %d terms for both G(q) and H(q). Target reproduction PASSES." % N)
log("   G(q) head: %s" % ints(G_sum, 14))
log("   H(q) head: %s" % ints(H_sum, 14))

N1 = smul(E1, G_sum, N)  # = theta_num(1,.) by route C
N2 = smul(E1, H_sum, N)
assert N1 == N1_theta and N2 == N2_theta
E1_9 = spow(E1, 9, N)
comp1_reduced = smul(N1, E1_9, N)  # comp1 = q^{2/5} * comp1_reduced
comp2_reduced = smul(N2, E1_9, N)  # comp2 = q^{3/5} * comp2_reduced
log("\ncomp1_reduced = N1(q)*(q;q)^9  [comp1 = q^{2/5} * this] head: %s" % ints(comp1_reduced, 14))
log("comp2_reduced = N2(q)*(q;q)^9  [comp2 = q^{3/5} * this] head: %s" % ints(comp2_reduced, 14))

# cross-check against the repo's OWN banked recomputation printed in
# frontier/B672_grading_hunt/cellG/cellG_output.txt (read-only; a numeric
# spot-check only, NOT used to derive anything): "2hat.comp1" ratio at n=1
# is reported there as -9, "2hat.comp2" ratio at n=1 as -10.
log("\nspot-check vs repo's independently-banked cellG_output.txt (read-only; not used to derive anything):")
log("  banked: 2hat.comp1 ratio(n=1) = -9   ; mine: comp1_reduced[1]/comp1_reduced[0] = %s  match: %s"
    % (comp1_reduced[1], comp1_reduced[1] == -9))
log("  banked: 2hat.comp2 ratio(n=1) = -10  ; mine: comp2_reduced[1]/comp2_reduced[0] = %s  match: %s"
    % (comp2_reduced[1], comp2_reduced[1] == -10))
assert comp1_reduced[1] == -9 and comp2_reduced[1] == -10

# The eta^{48/5}-reduced ("F-doublet") objects, F1 = N1*E1^{-3/5}, F2 = N2*E1^{-3/5}
# (comp = q^{r/5} * N * (q;q)^9 = F * eta^{48/5}, eta^{48/5}=q^{2/5}(q;q)^{48/5},
#  since -3/5+48/5 = 45/5 = 9 -- integer, matching (q;q)^9 exactly).
NF = 120
E1inv35 = spow_frac(E1[: NF + 1], Fr(-3, 5), NF)
F1 = smul(N1[: NF + 1], E1inv35, NF)
F2 = smul(N2[: NF + 1], E1inv35, NF)
# gate: F1 * E1^{48/5} == comp1_reduced ; F2 * E1^{48/5} == comp2_reduced  (integer powers only, NF terms)
E1_48_5 = spow_frac(E1[: NF + 1], Fr(48, 5), NF)
gate1 = smul(F1, E1_48_5, NF) == comp1_reduced[: NF + 1]
gate2 = smul(F2, E1_48_5, NF) == comp2_reduced[: NF + 1]
log("\neta^{48/5}-bookkeeping gate: F1*eta_no_qshift^{48/5} == comp1_reduced (%d terms): %s" % (NF + 1, gate1))
log("                             F2*eta_no_qshift^{48/5} == comp2_reduced (%d terms): %s" % (NF + 1, gate2))
assert gate1 and gate2
log("F1(q) head (rational coeffs, integer-exponent): %s" % [str(x) for x in F1[:10]])
log("F2(q) head (rational coeffs, integer-exponent): %s" % [str(x) for x in F2[:10]])

RESULTS["target_reproduction"] = {
    "routes_agree": {"sum_vs_product_G": route_AB_G, "sum_vs_product_H": route_AB_H,
                     "theta_vs_sum_G": route_C_G, "theta_vs_sum_H": route_C_H},
    "horizon_terms": N,
    "spotcheck_vs_repo_cellG": {"comp1_ratio_n1": comp1_reduced[1], "comp2_ratio_n1": comp2_reduced[1],
                                "banked_comp1_ratio_n1": -9, "banked_comp2_ratio_n1": -10},
    "eta_bookkeeping_gate": {"F1_times_eta48_5_eq_comp1": gate1, "F2_times_eta48_5_eq_comp2": gate2,
                             "terms": NF + 1},
    "verdict": "PASS -- proceeding to candidate tests",
}

log("\n>>> TARGET REPRODUCTION: PASS. Proceeding to candidates T2, T1, T0. <<<")

# =====================================================================
# PART 2 -- exact cyclotomic number engine: Q(zeta_5), power basis
# {1, z, z^2, z^3}  (z=zeta_5, z^5=1, z^4=-1-z-z^2-z^3).
# Q(zeta_5) is a degree-4 field over Q whose REAL subfield is exactly
# Q(sqrt5) (degree 2) -- it is the natural exact home for "golden,
# kappa=5" data: it holds phi, and it holds the 5th-root-of-unity
# T-matrix phases, in ONE field (a pure Q(sqrt5) engine is NOT enough,
# since sin(2*pi/5) etc. are genuinely degree-4, not degree-2 -- see
# the PART 3 finding below). All arithmetic here is exact Fraction
# arithmetic; "rational" means the z,z^2,z^3-components are all 0.
# =====================================================================
log("\n" + "=" * 100)
log("PART 2 -- exact Q(zeta_5) cyclotomic engine (build + validate)")
log("=" * 100)


def cmul(p, q):
    c = [Fr(0)] * 7
    for i in range(4):
        if not p[i]:
            continue
        for j in range(4):
            if q[j]:
                c[i + j] += p[i] * q[j]
    c[0] += c[5]
    c[1] += c[6]
    d4 = c[4]
    return (c[0] - d4, c[1] - d4, c[2] - d4, c[3] - d4)


def cadd(p, q):
    return tuple(p[i] + q[i] for i in range(4))


def csub(p, q):
    return tuple(p[i] - q[i] for i in range(4))


def cscale(p, k):
    k = Fr(k)
    return tuple(p[i] * k for i in range(4))


def cneg(p):
    return tuple(-p[i] for i in range(4))


def cpow(p, n):
    r = (Fr(1), Fr(0), Fr(0), Fr(0))
    base = p
    while n:
        if n & 1:
            r = cmul(r, base)
        base = cmul(base, base)
        n >>= 1
    return r


def cinv(p):
    """exact inverse in Q(zeta_5) via the regular representation + Gaussian elim."""
    basis = [(Fr(1), Fr(0), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0), Fr(0)),
             (Fr(0), Fr(0), Fr(1), Fr(0)), (Fr(0), Fr(0), Fr(0), Fr(1))]
    cols = [cmul(p, b) for b in basis]
    M = [[cols[j][i] for j in range(4)] for i in range(4)]
    aug = [row[:] + [Fr(1) if i == 0 else Fr(0)] for i, row in enumerate(M)]
    for col in range(4):
        piv = next(r for r in range(col, 4) if aug[r][col] != 0)
        aug[col], aug[piv] = aug[piv], aug[col]
        pv = aug[col][col]
        aug[col] = [v / pv for v in aug[col]]
        for r in range(4):
            if r != col and aug[r][col] != 0:
                f = aug[r][col]
                aug[r] = [a - f * b for a, b in zip(aug[r], aug[col])]
    return tuple(aug[i][4] for i in range(4))


def ceval(p):
    """numeric evaluation (complex) -- for cross-checks ONLY, never for verdicts."""
    import cmath
    z = cmath.exp(2j * 3.14159265358979323846 / 5)
    return sum(float(p[i]) * z ** i for i in range(4))


def is_rational(p):
    return p[1] == 0 and p[2] == 0 and p[3] == 0


ONE = (Fr(1), Fr(0), Fr(0), Fr(0))
ZERO = (Fr(0), Fr(0), Fr(0), Fr(0))
Z = (Fr(0), Fr(1), Fr(0), Fr(0))
Z2 = cmul(Z, Z)
Z3 = cmul(Z2, Z)
Z4 = cmul(Z3, Z)

gate_z5 = cmul(Z4, Z) == ONE
log("gate: z^5 == 1 exactly: %s" % gate_z5)
assert gate_z5

# sqrt5 via the quadratic Gauss sum: sqrt5 = z - z^2 - z^3 + z^4 (sign fixed
# by numeric check below to match +sqrt5, not -sqrt5)
SQRT5 = cadd(csub(Z, cadd(Z2, Z3)), Z4)
sqrt5_num = ceval(SQRT5)
gate_sqrt5 = abs(sqrt5_num.real - 5 ** 0.5) < 1e-9 and abs(sqrt5_num.imag) < 1e-9
log("gate: SQRT5 numeric = %.12f (+0i), matches +sqrt(5): %s" % (sqrt5_num.real, gate_sqrt5))
assert gate_sqrt5

PHI = cscale(cadd(ONE, SQRT5), Fr(1, 2))
PSI = cscale(csub(ONE, SQRT5), Fr(1, 2))  # = -1/phi
gate_phi2 = cmul(PHI, PHI) == cadd(PHI, ONE)
log("gate: phi^2 == phi+1 exactly (golden defining relation): %s" % gate_phi2)
assert gate_phi2
gate_psiphi = cmul(PSI, PHI) == cneg(ONE)
log("gate: psi*phi == -1 exactly (psi = -1/phi): %s" % gate_psiphi)
assert gate_psiphi
log("PHI numeric: %.12f  (vs golden ratio %.12f)" % (ceval(PHI).real, (1 + 5 ** 0.5) / 2))

RESULTS["cyclotomic_engine_gates"] = {"z5_eq_1": gate_z5, "sqrt5_numeric_match": gate_sqrt5,
                                       "phi2_eq_phi_plus_1": gate_phi2, "psi_phi_eq_neg1": gate_psiphi}

# =====================================================================
# PART 3 -- THE WELD OPERATOR: B238's kappa=5 golden-block RL monodromy.
#
# B238 (frontier/B238_su32_levelrank/, read-only) computes SU(2)_3 (4
# primaries) and SU(3)_2 (6 primaries) modular data (S,T), gate-verifies
# the modular relations, and finds Z(figure-eight) = tr(rho(RL)) = -1/phi
# EXACTLY for BOTH, via R=T, L=S^{-1}T^{-1}S (the standard R,L generators
# of the once-punctured-torus-bundle mapping class group). Both share
# kappa=k+N=5, the golden field Q(zeta_5).
#
# "The golden block": SU(2)_3's INTEGER-spin sector {spin0,spin1} is
# closed under FUSION exactly as Fibonacci (tau^2=1+tau, since the
# level-3 truncated SU(2) fusion spin1 x spin1 -> spin0+spin1, spin2
# truncated away) -- this is the standard "Fibonacci sits inside SU(2)_3"
# fact. The STANDALONE Fibonacci category's own canonical (S,T) --
# S=(1/sqrt(1+d^2))[[1,d],[d,-1]], d=phi, S^2=I; T=diag(1,e^{2pi i h_tau})
# -- is used here as "B238's operator restricted to the golden block"
# (this is the standard literature/repo convention: identical to B135's
# S-matrix formula, B484's F/R data, B220/B218's golden-chain data).
#
# CONTROL / FINDING: naive row/column extraction of indices {0,2} from
# the ACTUAL SU(2)_3 4x4 (S,T) matrices does NOT reproduce this -- S does
# NOT act block-diagonally on the {spin0,spin1} subspace (S mixes all 4
# spins), so that submatrix is not a genuine sub-representation and its
# RL-trace is complex, NOT -1/phi (verified below, exact-numeric via a
# fresh from-scratch sympy build of the SU(2)_3 4x4 data). The STANDALONE
# Fibonacci category's RL-monodromy trace, by contrast, is EXACTLY -1/phi
# (verified here purely from the cyclotomic engine) -- matching B238's
# banked full-4x4/6x6 headline number via an independent mechanism. This
# is the correct, standard "golden/kappa=5 block", used throughout this
# repo (B135/B220/B484/B218); the finding above is banked as an anomaly.
# =====================================================================
log("\n" + "=" * 100)
log("PART 3 -- the weld operator: B238's kappa=5 golden-block RL monodromy")
log("=" * 100)


def build_weld2(d, htau_num5):
    """htau = htau_num5/5. r = z^{-htau_num5 mod 5}, rinv = z^{htau_num5 mod 5}."""
    r = cpow(Z, (-htau_num5) % 5)
    rinv = cpow(Z, htau_num5 % 5)
    d2 = cmul(d, d)
    denom = cadd(cscale(ONE, Fr(2)), d)
    denom_inv = cinv(denom)
    W11 = cmul(cadd(ONE, cmul(d2, r)), denom_inv)
    W22 = cmul(cadd(ONE, cmul(d2, rinv)), denom_inv)
    W12 = cmul(cmul(d, csub(ONE, r)), denom_inv)
    W21 = cmul(cmul(d, csub(rinv, ONE)), denom_inv)
    return {"11": W11, "12": W12, "21": W21, "22": W22}


# Fibonacci (unitary) convention: d=phi, h_tau=2/5 (theta_tau=e^{4pi i/5}, matching
# the prereg's T0 statement exactly)
W_FIB = build_weld2(PHI, 2)
trace_fib = cadd(W_FIB["11"], W_FIB["22"])
det_fib = csub(cmul(W_FIB["11"], W_FIB["22"]), cmul(W_FIB["12"], W_FIB["21"]))
NEG_INV_PHI = PSI
gate_trace_fib = trace_fib == NEG_INV_PHI
gate_det_fib = det_fib == ONE
log("W_FIB (Fibonacci/unitary convention, d=phi, h_tau=2/5):")
log("  trace(W_FIB) == -1/phi == psi  exactly: %s   (numeric %.12f vs %.12f)"
    % (gate_trace_fib, ceval(trace_fib).real, ceval(NEG_INV_PHI).real))
log("  det(W_FIB) == 1  exactly: %s" % gate_det_fib)
assert gate_trace_fib and gate_det_fib
log("  ** MATCHES B238's banked headline number Z(4_1)=-1/phi (independent mechanism) **")

# Yang-Lee (non-unitary, sigma_3 Galois conjugate) convention: d=psi=-1/phi, h_tau=-1/5
W_YL = build_weld2(PSI, -1)
trace_yl = cadd(W_YL["11"], W_YL["22"])
det_yl = csub(cmul(W_YL["11"], W_YL["22"]), cmul(W_YL["12"], W_YL["21"]))
gate_trace_yl_eq_phi = trace_yl == PHI
log("\nW_YL (Yang-Lee/non-unitary sigma_3-conjugate, d=psi=-1/phi, h_tau=-1/5):")
log("  trace(W_YL) == +phi exactly: %s  (numeric %.12f)" % (gate_trace_yl_eq_phi, ceval(trace_yl).real))
log("  det(W_YL) == 1 exactly: %s" % (det_yl == ONE))
log("  NOTE: this does NOT match B238's -1/phi -- the Yang-Lee point is a formal")
log("  Galois conjugate of the abstract fusion data, not a literal sub-block of the")
log("  UNITARY SU(2)_3/SU(3)_2 modular data (consistent with S030/B135's own framing:")
log("  the sigma_3 conjugate is an algebraic operation, not a restriction of a real MTC).")
assert gate_trace_yl_eq_phi and det_yl == ONE

# Modular-relation gates on W_FIB's generating S,T (mirrors B238's own modular_gate).
# S = M/D with M=[[1,phi],[phi,-1]], D=sqrt(1+phi^2)=sqrt(2+phi) (D itself needs a
# radical NOT in Q(zeta_5) -- irrelevant, since "propto identity" is scale-invariant,
# so it is checked directly on the UNNORMALIZED M (S^2=I <=> M^2 = (1+phi^2)*I,
# a pure scalar-times-identity fact, checked exactly in Q(zeta_5) with no need for D).
def mat_mul2(A, B):
    return {"11": cadd(cmul(A["11"], B["11"]), cmul(A["12"], B["21"])),
            "12": cadd(cmul(A["11"], B["12"]), cmul(A["12"], B["22"])),
            "21": cadd(cmul(A["21"], B["11"]), cmul(A["22"], B["21"])),
            "22": cadd(cmul(A["21"], B["12"]), cmul(A["22"], B["22"]))}


M_mat = {"11": ONE, "12": PHI, "21": PHI, "22": cneg(ONE)}
T_mat = {"11": ONE, "12": ZERO, "21": ZERO, "22": cpow(Z, 2)}  # theta_tau=z^2=e^{4pi i/5}
M2 = mat_mul2(M_mat, M_mat)
gate_M2_scalar = (M2["12"] == ZERO and M2["21"] == ZERO and M2["11"] == M2["22"] == cadd(ONE, cmul(PHI, PHI)))
MT = mat_mul2(M_mat, T_mat)
MT3 = mat_mul2(mat_mul2(MT, MT), MT)
gate_MT3_scalar = (MT3["12"] == ZERO and MT3["21"] == ZERO and MT3["11"] == MT3["22"])
log("\nmodular-relation gates on the Fibonacci S,T (mirrors B238's modular_gate; scale-invariant")
log("  form checked directly on M=[[1,phi],[phi,-1]] so S=M/D, S^2=I <=> M^2=(1+phi^2)I):")
log("  M^2 == (1+phi^2)*I exactly (<=> S^2=I once normalized by D): %s" % gate_M2_scalar)
log("  (M T)^3 is a scalar matrix (propto M^2, i.e. (ST)^3 propto S^2) exactly: %s  (scalar=%s, numeric %.6f)"
    % (gate_MT3_scalar, MT3["11"], ceval(MT3["11"]).real))
assert gate_M2_scalar and gate_MT3_scalar
gate_S2, gate_ST3_scalar = gate_M2_scalar, gate_MT3_scalar

# --- PART 3b: independent sympy cross-check against a fresh SU(2)_3 4x4 build ---
log("\n-- PART 3b: independent cross-check -- fresh SU(2)_3 (4x4) build (sympy, numeric-exact) --")
import sympy as sp

I_ = sp.I
pi_ = sp.pi
Rat = sp.Rational


def su2_S_T(k):
    n = k + 1
    kap = k + 2
    Sm = sp.Matrix(n, n, lambda a, b: sp.sqrt(Rat(2, kap)) * sp.sin(pi_ * (a + 1) * (b + 1) / kap))
    c = Rat(k * 3, k + 2)
    Tm = sp.diag(*[sp.exp(2 * pi_ * I_ * (Rat(a, 2) * (Rat(a, 2) + 1) / kap - c / 24)) for a in range(n)])
    return Sm, Tm, c


S4, T4, c4 = su2_S_T(3)
Ti4 = T4.inv()
Si4 = S4.inv()
L4 = Si4 * Ti4 * S4
W4full = T4 * L4
tr_full_n = sp.N(sp.trace(W4full), 40)
phi_n = sp.N((1 + sp.sqrt(5)) / 2, 40)
gate_full_trace = abs(complex(tr_full_n) - complex(-1 / phi_n)) < Fr(1, 10 ** 30)
log("  fresh SU(2)_3 4x4 build: c=%s, tr(full 4x4 RL monodromy) matches -1/phi (40-digit numeric): %s"
    % (c4, gate_full_trace))

idx = [0, 2]  # spin0, spin1 = the integer-spin/"golden" labels
W2sub = W4full[idx, idx]
tr_sub_n = sp.N(sp.trace(W2sub), 40)
sub_matches_minus_inv_phi = abs(complex(tr_sub_n) - complex(-1 / phi_n)) < Fr(1, 10 ** 30)
sub_is_real = abs(complex(tr_sub_n).imag) < 1e-30
log("  naive {spin0,spin1} SUBMATRIX of the 4x4 (rows/cols 0,2): trace = %s (40-digit numeric)"
    % sp.N(tr_sub_n, 12))
log("  submatrix trace matches -1/phi: %s   submatrix trace is even real: %s"
    % (sub_matches_minus_inv_phi, sub_is_real))
log("  ANOMALY CONFIRMED: naive row/column extraction is NOT a valid sub-representation")
log("  (S mixes all 4 spins; the submatrix trace is complex, not -1/phi) -- the STANDALONE")
log("  Fibonacci S,T (W_FIB above) is the correct 'golden block', independently matching")
log("  the full ambient trace exactly via a DIFFERENT mechanism. Banked as a finding.")
assert gate_full_trace and not sub_matches_minus_inv_phi

RESULTS["weld_operator"] = {
    "W_FIB": {k: [str(x) for x in v] for k, v in W_FIB.items()},
    "W_FIB_trace_eq_neg1_phi": gate_trace_fib, "W_FIB_det_eq_1": gate_det_fib,
    "W_YL": {k: [str(x) for x in v] for k, v in W_YL.items()},
    "W_YL_trace_eq_phi": gate_trace_yl_eq_phi,
    "modular_gates": {"S2_eq_I": gate_S2, "ST3_scalar": gate_ST3_scalar},
    "su2_3_full_4x4_trace_matches_neg1_phi": gate_full_trace,
    "finding_submatrix_extraction_anomaly": {
        "naive_submatrix_trace_matches_neg1_phi": bool(sub_matches_minus_inv_phi),
        "naive_submatrix_trace_is_real": bool(sub_is_real),
        "note": "naive {spin0,spin1} row/col extraction from SU(2)_3's actual 4x4 is NOT a "
                "sub-representation (S mixes all 4 spins); standalone Fibonacci S,T is the "
                "correct golden block and matches B238's -1/phi via an independent mechanism.",
    },
}

# =====================================================================
# PART 4 -- CANDIDATE T2 (cheapest, run FIRST): the weld-weighted CHIRAL
# character sum.
#
# chi_1, chi_tau: the (2,5)-model Rocha-Caridi characters,
#   chi_{r,s}(q) = q^{h-c/24} * N_{r,s}(q)/(q;q)_infty = q^{h-c/24} * {G or H}(q)
# (N1=(q;q)G(q), N2=(q;q)H(q) already verified in PART 1 to be the exact RR
# theta numerators -- this IS the Rocha-Caridi numerator for the (2,5) model,
# a textbook identity). TWO classical normalizations, both stated explicitly:
#   YL  (Yang-Lee/M(2,5), non-unitary): c=-22/5, h_1=0, h_tau=-1/5 (c_eff=2/5)
#   FIB (unitary Fibonacci/(G2)_1):      c=+14/5, h_1=0, h_tau=+2/5
# (both banked in this repo: frontier/speculations/S030 + frontier/B135).
#
# Candidate (exactly as the prereg names it): Z_W(q) = sum_a W_aa chi_a(q),
# and the off-diagonal ROW variants sum_b W_ab chi_b(q) -- tested against
# comp1/comp2 up to the STATED eta^{48/5} bookkeeping + ONE overall rational
# constant (no other freedom).
#
# TWO READINGS tested (both licensed by "chi_a(q) ... computed exactly from
# the RR product/sum forms" -- the prereg does not pin down whether the CFT
# prefactor q^{h-c/24} is retained in the candidate or is bookkeeping-only):
#  (A) FULL characters (with the q^{h-c/24} prefactor retained).
#  (B) prefactor-STRIPPED characters (chi_1->G(q), chi_tau->H(q) directly,
#      deferring ALL q-power bookkeeping to the named eta^{48/5} factor).
# =====================================================================
log("\n" + "=" * 100)
log("PART 4 -- CANDIDATE T2: weld-weighted chiral character sum (Fibonacci/Lee-Yang)")
log("=" * 100)

CONVENTIONS = {
    "YL": {"c": Fr(-22, 5), "h1": Fr(0), "htau": Fr(-1, 5)},
    "FIB": {"c": Fr(14, 5), "h1": Fr(0), "htau": Fr(2, 5)},
}
for name, cv in CONVENTIONS.items():
    cv["exp1"] = cv["h1"] - cv["c"] / 24
    cv["exptau"] = cv["htau"] - cv["c"] / 24
    log("convention %-4s: c=%s, h_1=0 h_tau=%s  =>  chi_1=q^%s*G(q), chi_tau=q^%s*H(q)"
        % (name, cv["c"], cv["htau"], cv["exp1"], cv["exptau"]))

log("\n-- reading (A): FULL characters retained, structural (fractional-support-class) check --")
target_class1, target_class2 = Fr(2, 5), Fr(3, 5)
readingA = {}
for name, cv in CONVENTIONS.items():
    c1m = cv["exp1"] % 1
    ctm = cv["exptau"] % 1
    diff = (cv["exp1"] - cv["exptau"]) % 1
    hits1 = {"chi1_hits_comp1_class": c1m == target_class1, "chitau_hits_comp1_class": ctm == target_class1}
    hits2 = {"chi1_hits_comp2_class": c1m == target_class2, "chitau_hits_comp2_class": ctm == target_class2}
    readingA[name] = {"chi1_class_mod1": str(c1m), "chitau_class_mod1": str(ctm),
                       "mutual_class_gap_mod1": str(diff), **hits1, **hits2}
    log("  [%s] chi_1 class=%s mod1, chi_tau class=%s mod1 (mutual gap=%s, non-integer=>disjoint supports)"
        % (name, c1m, ctm, diff))
    log("       vs comp1 class(2/5): chi1 hit=%s chi_tau hit=%s | vs comp2 class(3/5): chi1 hit=%s chi_tau hit=%s"
        % (hits1["chi1_hits_comp1_class"], hits1["chitau_hits_comp1_class"],
           hits2["chi1_hits_comp2_class"], hits2["chitau_hits_comp2_class"]))
none_hit = all(not any(readingA[n][k] for k in ("chi1_hits_comp1_class", "chitau_hits_comp1_class",
                                                 "chi1_hits_comp2_class", "chitau_hits_comp2_class"))
               for n in CONVENTIONS)
log("\n  READING (A) VERDICT: for BOTH conventions, NEITHER chi_1 nor chi_tau's fractional support")
log("  class equals comp1's (2/5) or comp2's (3/5) class mod 1 (all hits False: %s)." % none_hit)
log("  => structural KILL for reading (A), independent of the numeric value of W: ANY nonzero")
log("     combination W_aa*chi_a(q) or W_ab*chi_b(q) has its ENTIRE support in the wrong")
log("     fractional-exponent class(es); every coefficient at comp1's/comp2's actual exponents")
log("     is forced to 0 while the target's leading coefficient there is 1 (n=0 mismatch: got 0, expected 1).")
assert none_hit

log("\n-- reading (B): prefactor-STRIPPED characters (chi_1->G(q), chi_tau->H(q)), numeric test --")
NB = 100
Gc = [x for x in G_sum[:NB + 1]]
Hc = [x for x in H_sum[:NB + 1]]
F1c = [x for x in F1[:NB + 1]]
F2c = [x for x in F2[:NB + 1]]

candidates_T2 = {
    "W_FIB.diag":  ("11", "22"),
    "W_FIB.row1":  ("11", "12"),
    "W_FIB.row2":  ("21", "22"),
    "W_YL.diag":   ("11", "22"),
    "W_YL.row1":   ("11", "12"),
    "W_YL.row2":   ("21", "22"),
}
welds_T2 = {"W_FIB": W_FIB, "W_YL": W_YL}
targets_T2 = {"row1": F1c, "row2": F2c}  # row1~comp1, row2~comp2; diag has no natural target pairing


def combo_coeff(wA, wB, ga, hb):
    """wA*G_n + wB*H_n as an exact cyclotomic number (ga=G_n int, hb=H_n int)."""
    return cadd(cscale(wA, ga), cscale(wB, hb))


t2_mismatches = {}
for cand_name, (kA, kB) in candidates_T2.items():
    weld_name, variant = cand_name.split(".")
    W = welds_T2[weld_name]
    wA, wB = W[kA], W[kB]
    n0 = combo_coeff(wA, wB, Gc[0], Hc[0])  # = wA+wB since G0=H0=1
    n0_rational = is_rational(n0)
    log("\n  candidate %-14s = %s*G(q) + %s*H(q)  [weld entries %s,%s]" % (cand_name, "W_" + kA, "W_" + kB, kA, kB))
    log("    leading coefficient (n=0) = %s  (numeric %.6f%+.6fi)  rational: %s"
        % (n0, ceval(n0).real, ceval(n0).imag, n0_rational))
    if not n0_rational:
        log("    => IMMEDIATE KILL at n=0: leading coefficient is not rational; the prereg's sole")
        log("       allowed freedom (ONE overall RATIONAL constant) cannot turn a non-rational")
        log("       cyclotomic number into the target's rational leading coefficient (=1).")
        t2_mismatches[cand_name] = {"first_mismatch_n": 0, "expected": "1 (rational)",
                                     "got": [str(x) for x in n0], "got_numeric": [ceval(n0).real, ceval(n0).imag],
                                     "reason": "leading coefficient not rational -- no rational rescaling can fix it"}
        continue
    # (in case it were rational) -- fall through to a real coefficient scan (not expected to trigger)
    c0 = n0[0]
    target = targets_T2.get(variant)
    if target is None:
        log("    (diag variant has no single natural target component; skipping numeric scan)")
        continue
    scale = Fr(target[0]) / c0
    mismatch = None
    for n in range(1, NB + 1):
        cn = combo_coeff(wA, wB, Gc[n], Hc[n])
        cn_scaled = cscale(cn, scale)
        if not is_rational(cn_scaled) or cn_scaled[0] != Fr(target[n]):
            mismatch = (n, str(cn_scaled), str(target[n]))
            break
    t2_mismatches[cand_name] = {"first_mismatch_n": mismatch[0] if mismatch else None,
                                 "got": mismatch[1] if mismatch else None,
                                 "expected": mismatch[2] if mismatch else None}
    log("    (rational at n=0 -- scanned to n=%d) first mismatch: %s" % (NB, mismatch))

log("\nT2 OVERALL VERDICT: KILL (every sub-candidate, both readings, both weld/character conventions;")
log("  reading (A) fails structurally at the fractional-support-class level for ALL welds;")
log("  reading (B) fails at the very leading coefficient n=0 -- the weld's diagonal/row entries")
log("  are genuine irrational Q(zeta_5) numbers, never rational, so no single rational rescaling")
log("  constant (the ONLY freedom the prereg allows) can align even the first term.)")

RESULTS["T2"] = {
    "verdict": "KILL",
    "readingA_structural": {"per_convention": readingA, "none_hit_target_class": none_hit},
    "readingB_numeric": t2_mismatches,
    "conventions": {k: {kk: str(vv) for kk, vv in v.items()} for k, v in CONVENTIONS.items()},
}

# =====================================================================
# PART 5 -- CANDIDATE T1: the DOUBLE's character sum.
#
# Fib is itself modular (S invertible: det(S)=-1 =/= 0), so by the standard
# theorem for modular categories, Z(Fib) = Fib boxtimes Fib-bar EXACTLY (4
# simples: (1,1),(1,tau),(tau,1),(tau,tau)). Its natural (S,T) are the
# Kronecker products S_Z = S tensor S-bar, T_Z = T tensor T-bar; since Fib's
# S is real (S-bar=S) and T is a pure phase (T-bar=T^{-1}), the double's own
# RL weld factors EXACTLY as W_Z = (T S T^{-1} S) tensor (T^{-1} S T S) =
# W_FIB tensor W', where W' swaps the roles of T, T^{-1} relative to W_FIB
# -- "B238's FULL modular action" on the double, built here explicitly (not
# assumed) and cross-checked against W_FIB's own closed form.
#
# chi_(a,b)(q) = chi_a(q)*chi_b(q) "restricted to the diagonal q-grading"
# (qbar=q): the 4 building blocks G*G, G*H, H*G, H*H (prefactor-stripped
# reading, as in T2 reading B -- reading A is structurally dead for the
# identical reason as T2, since each chi_(a,b) still carries the SAME
# fractional prefactor classes as PART 4, just added pairwise).
# =====================================================================
log("\n" + "=" * 100)
log("PART 5 -- CANDIDATE T1: the double Z(Fib)=Fib boxtimes Fib-bar character sum")
log("=" * 100)

det_S_fib = csub(cmul(ONE, cneg(ONE)), cmul(PHI, PHI))  # det of UNNORMALIZED M; sign only matters
log("Fib modularity check: det(M) = %s (nonzero => S invertible => Fib is modular => Z(Fib)=Fib(x)Fib-bar): %s"
    % (det_S_fib, det_S_fib != ZERO))
assert det_S_fib != ZERO


def weld_general(d, a, b):
    """T_a * M * T_b * M / (2+d), T_a=diag(1,z^a), T_b=diag(1,z^b)."""
    za, zb = cpow(Z, a % 5), cpow(Z, b % 5)
    d2 = cmul(d, d)
    denom_inv = cinv(cadd(cscale(ONE, Fr(2)), d))
    e11 = cadd(ONE, cmul(d2, zb))
    e12 = cmul(d, csub(ONE, zb))
    e21 = cmul(d, cmul(za, csub(ONE, zb)))
    e22 = cadd(cmul(d2, za), cmul(za, zb))
    return {"11": cmul(e11, denom_inv), "12": cmul(e12, denom_inv),
            "21": cmul(e21, denom_inv), "22": cmul(e22, denom_inv)}


W_check = weld_general(PHI, 2, -2)  # a=+htau_num5, b=-htau_num5 => should reproduce W_FIB
gate_weld_general = all(W_check[k] == W_FIB[k] for k in ("11", "12", "21", "22"))
log("weld_general(phi,+2,-2) reproduces W_FIB exactly (cross-check of the general formula): %s"
    % gate_weld_general)
assert gate_weld_general

Wp = weld_general(PHI, -2, 2)  # W' = T^{-1} S T S (swapped)
log("W' = T^{-1} S T S (swapped T,T^{-1}): trace=%s (numeric %.6f%+.6fi), det=%s"
    % (cadd(Wp["11"], Wp["22"]), ceval(cadd(Wp["11"], Wp["22"])).real, ceval(cadd(Wp["11"], Wp["22"])).imag,
       csub(cmul(Wp["11"], Wp["22"]), cmul(Wp["12"], Wp["21"]))))

# trace-blindness illustration (per the B674 mid-run intel): the FULLY traced
# double weld tr(W4)=tr(W_FIB)*tr(W') is a SINGLE SCALAR -- not even a
# candidate q-series -- showing explicitly how tracing destroys all the
# per-coefficient structure a character-level object could carry.
tr_W4_scalar = cmul(cadd(W_FIB["11"], W_FIB["22"]), cadd(Wp["11"], Wp["22"]))
log("\nTRACE-BLINDNESS ILLUSTRATION: tr(W4)=tr(W_FIB)*tr(W') = %s (numeric %.6f) -- a single NUMBER,"
    % (tr_W4_scalar, ceval(tr_W4_scalar).real))
log("  not a q-series at all. This is the same mechanism B674 found for the Eichler-Shimura trace")
log("  tower (tr(A1*|H^1)=0 identically): tracing collapses the per-coefficient information that")
log("  only a CHARACTER/MODULE-level object (the row/diagonal candidates below, or T0's graded")
log("  pieces) could in principle carry. Banked as a corroborating trace-blindness datum.")

# Build the 4x4 double weld W4[(i,j),(k,l)] = W_FIB[i,k] * Wp[j,l],  i,j,k,l in {1,2} (1=id,2=tau)
PAIRS = [(1, 1), (1, 2), (2, 1), (2, 2)]


def W4_entry(row, col):
    i, j = row
    k, l = col
    return cmul(W_FIB["%d%d" % (i, k)], Wp["%d%d" % (j, l)])


# chi_(i,j)(q) coefficients (prefactor-stripped): chi_1->G, chi_2(=tau)->H
CHI = {1: Gc, 2: Hc}

t1_mismatches = {}
log("\nnumeric test (prefactor-stripped reading, matching T2 reading B): diagonal + all 4 rows")


def combo4_coeff(weights, n):
    """sum_{(i,j) in PAIRS} weights[(i,j)] * CHI[i][n]*CHI[j][n]  -- exact cyclotomic."""
    acc = ZERO
    for (i, j) in PAIRS:
        gi = CHI[i][n]
        gj = CHI[j][n]
        acc = cadd(acc, cscale(weights[(i, j)], gi * gj))
    return acc


row_names = ["diag"] + ["row_%d%d" % p for p in PAIRS]
for row_name in row_names:
    if row_name == "diag":
        weights = {(i, j): W4_entry((i, j), (i, j)) for (i, j) in PAIRS}
    else:
        p_row = (int(row_name[-2]), int(row_name[-1]))
        weights = {(i, j): W4_entry(p_row, (i, j)) for (i, j) in PAIRS}
    n0 = combo4_coeff(weights, 0)  # all CHI[.][0]=1
    n0_rational = is_rational(n0)
    log("  candidate T1.%-8s leading coeff (n=0) = %s (numeric %.6f%+.6fi) rational: %s"
        % (row_name, n0, ceval(n0).real, ceval(n0).imag, n0_rational))
    if not n0_rational:
        t1_mismatches[row_name] = {"first_mismatch_n": 0, "expected": "1 (rational)",
                                    "got": [str(x) for x in n0], "reason": "leading coeff not rational"}
        continue
    # would only reach here if rational -- scan against both F1,F2 (not expected)
    c0 = n0[0]
    for tgt_name, target in (("F1", F1c), ("F2", F2c)):
        scale = Fr(target[0]) / c0
        mismatch = None
        for n in range(1, NB + 1):
            cn = combo4_coeff(weights, n)
            cns = cscale(cn, scale)
            if not is_rational(cns) or cns[0] != Fr(target[n]):
                mismatch = (n, str(cns), str(target[n]))
                break
        log("    vs %s: first mismatch %s" % (tgt_name, mismatch))
        t1_mismatches.setdefault(row_name, {})[tgt_name] = mismatch

log("\nT1 OVERALL VERDICT: KILL -- every diagonal/row combination's leading (n=0) coefficient is a")
log("  genuine irrational Q(zeta_5) number (never rational), for the identical structural reason as")
log("  T2: the weld entries are irrational, and prefactor-stripped chi's share leading coeff 1, so")
log("  no single rational rescaling constant can align even the first term.")

RESULTS["T1"] = {
    "verdict": "KILL",
    "fib_is_modular_gate": det_S_fib != ZERO,
    "weld_general_crosscheck": gate_weld_general,
    "trace_blindness_scalar": {"value": [str(x) for x in tr_W4_scalar], "numeric": ceval(tr_W4_scalar).real},
    "mismatches": t1_mismatches,
}

# =====================================================================
# PART 6 -- CANDIDATE T0 (the structural candidate): the weld-twisted
# Hochschild graded trace on Tube(Fib).
#
# Step (i): build Tube(Fib) explicitly from Fibonacci fusion data (dimension
#   count, FIRST PRINCIPLES, no citation): Tube(C) = direct sum, over triples
#   (a,b,x) of simples, of Hom(x tensor a, b tensor x); dim Hom(x(x)a,b(x)x)
#   = sum_c N_{xa}^c N_{bx}^c.  Fibonacci's fusion ring N (1=identity,2=tau):
#   N_111=1, N_1tt=N_t1t=1, N_ttt=1(c=tau)+1(c=1), all else 0. Enumerated below.
# Step (ii): verify the generating F/R data's algebra axioms (control ii):
#   F-matrix pentagon-consistency (F^2=I, F symmetric, the golden relation),
#   the hexagon-consistent B484 figure-eight-braid reproduction (tr=-3/phi),
#   and W's modular-relation gates (already verified in PART 3, reused here
#   as "W induces a consistent automorphism of the generating data").
# Step (iii): the decisive fact -- Tube(Fib) is FINITE-DIMENSIONAL (a fusion
#   category always has finitely many simples => Z(C) is again a fusion
#   category, semisimple, finitely many simples => Tube(C) is a finite-dim
#   SEMISIMPLE algebra; standard, e.g. Ostrik / Etingof-Nikshych-Ostrik).
#   Separable/semisimple algebras have HH^n(A,M)=0 for ALL n>=1 and ANY
#   bimodule M (Maschke-type separability) -- so HH^1=HH^2=0 IDENTICALLY,
#   for the untwisted OR the W-twisted bimodule A_W. HH^0(A,A_W) is bounded
#   by dim(Tube(Fib)) (<=7, computed below). Graded by the twist eigenvalues
#   theta_1=1, theta_tau=e^{4pi i/5} (a FIXED finite set of 5th roots of
#   unity, per the prereg's own T0 statement) -- ANY such graded trace is a
#   FINITE / eventually-periodic object in the grading variable, and can
#   NEVER reproduce an unboundedly-growing, non-periodic target like the RR
#   streams. This is exactly the "trace/finite-dim object is blind" pattern
#   flagged by the B674 mid-run intel -- corroborated here structurally.
# =====================================================================
log("\n" + "=" * 100)
log("PART 6 -- CANDIDATE T0: weld-twisted Hochschild graded trace on Tube(Fib)")
log("=" * 100)

# --- (i) Tube(Fib) dimension, from Fibonacci's own fusion ring (first principles) ---
FUSION = {}  # FUSION[a,b,c] = N_ab^c ,  1=identity object, 2=tau
for a in (1, 2):
    for b in (1, 2):
        for c in (1, 2):
            FUSION[a, b, c] = 0
FUSION[1, 1, 1] = 1
FUSION[1, 2, 2] = 1
FUSION[2, 1, 2] = 1
FUSION[2, 2, 1] = 1
FUSION[2, 2, 2] = 1

tube_dim = 0
tube_blocks = {}
for a in (1, 2):
    for b in (1, 2):
        for x in (1, 2):
            d = sum(FUSION[x, a, c] * FUSION[b, x, c] for c in (1, 2))
            if d:
                tube_blocks[(x, a, b)] = d
            tube_dim += d
log("Tube(Fib) basis dimension count dim Hom(x(x)a,b(x)x) summed over all (x,a,b) in {1,tau}^3:")
for (x, a, b), d in sorted(tube_blocks.items()):
    log("  x=%s a=%s b=%s : dim Hom = %d" % (x, a, b, d))
log("  TOTAL dim(Tube(Fib)) = %d" % tube_dim)
gate_tube_dim7 = (tube_dim == 7)
assert gate_tube_dim7
log("  (matches the known Ocneanu-tube-algebra dimension for the golden/Fibonacci category;")
log("   the largest block, x=a=b=tau with dim Hom=2, corresponds to the double's 2-dimensional")
log("   (tau,tau)-labeled simple module -- consistent with Z(Fib)'s 4 simples having module")
log("   dimensions {1,1,1,2}: 1+1+1+2^2 = 7.)")

# --- (ii) F/R data axiom checks (sympy, sqrt(phi) genuinely needed -- degree-4 field) ---
log("\n-- F/R generating-data axiom checks (sympy; sqrt(phi) needed -- Fib's F-matrix is NOT")
log("   expressible in Q(sqrt5) alone, an honest finding, see note below) --")
phi_sp = (1 + sp.sqrt(5)) / 2
Fmat = sp.Matrix([[1 / phi_sp, 1 / sp.sqrt(phi_sp)], [1 / sp.sqrt(phi_sp), -1 / phi_sp]])
F2mat = sp.simplify(Fmat * Fmat)
gate_F2_eq_I = sp.simplify(F2mat - sp.eye(2)) == sp.zeros(2, 2)
gate_F_sym = sp.simplify(Fmat - Fmat.T) == sp.zeros(2, 2)
gate_golden_rel = sp.simplify(phi_sp ** 2 - phi_sp - 1) == 0
log("  F^2 == I exactly (pentagon-consistency, involution property): %s" % gate_F2_eq_I)
log("  F symmetric exactly: %s" % gate_F_sym)
log("  phi^2 - phi - 1 == 0 exactly (the golden defining relation used to build F): %s" % gate_golden_rel)
log("  NOTE (honest finding): F's off-diagonal entries need sqrt(phi) -- a genuine DEGREE-4")
log("  algebraic number (phi is not a square in Q(sqrt5): x^2=phi has no solution x=a+b*sqrt5,")
log("  a,b in Q, by direct elimination). So Tube(Fib)'s generating F-data lives in Q(sqrt(phi),")
log("  sqrt5), not literally 'Q(sqrt5)' as the prereg's phrasing suggested -- banked precisely.")
assert gate_F2_eq_I and gate_F_sym and gate_golden_rel

# hexagon-consistency: reproduce B484's figure-eight-braid trace = -3/phi EXACTLY (sympy).
# (symbolic sp.simplify stalls/fails to collapse the (-1)^{fractional} branch reps here;
#  the standard, reliable exactness gate for this shape of expression is high-precision
#  numeric agreement -- 60 digits, far beyond any float-rounding concern -- exactly the
#  same style of gate B238's own modular_gate() uses, just at much higher precision.)
s1 = sp.diag(sp.exp(-4 * sp.I * sp.pi / 5), sp.exp(3 * sp.I * sp.pi / 5))
s2 = Fmat * s1 * Fmat
Braid = s1.inv() * s2 * s1.inv() * s2
tr_braid_n = sp.N(sp.trace(Braid), 60)
target_n = sp.N(-3 / phi_sp, 60)
gate_braid = abs(complex(tr_braid_n) - complex(target_n)) < Fr(1, 10 ** 50)
log("  B484 reproduction: tr(figure-eight 3-anyon braid) == -3/phi (60-digit numeric exactness): %s"
    % gate_braid)
log("    computed: %s" % sp.N(tr_braid_n, 25))
log("    -3/phi:   %s" % sp.N(target_n, 25))
assert gate_braid

log("\n  => (i)+(ii) together: Tube(Fib) is explicitly built (dim=7, from Fibonacci's own fusion")
log("     ring) on generating F/R data that is independently, exactly verified consistent")
log("     (pentagon-reduction F^2=I; hexagon-reproduction of B484's -3/phi); W's modular-relation")
log("     gates (PART 3: S^2=I up to scale, (ST)^3 propto S^2, det(W)=1 => W invertible) verify")
log("     W is a well-defined automorphism-compatible action on this generating data.")

# --- (iii) the decisive finite/periodic vs infinite/aperiodic argument ---
log("\n-- (iii) the decisive structural argument --")
log("  Tube(Fib) is FINITE-DIMENSIONAL (dim=7, computed above) => it is a finite-dim algebra;")
log("  since C=Fib is a fusion category, Z(C) is again a fusion category (standard theorem:")
log("  the center of a fusion category is a fusion category, hence semisimple with finitely")
log("  many simples) => Tube(C) (whose module category IS Z(C)) is a finite-dim SEMISIMPLE")
log("  algebra. Semisimple (separable, char 0) algebras have HH^n(A,M) = 0 for ALL n>=1 and")
log("  ANY A-bimodule M (a basic homological-algebra fact -- separable algebras have")
log("  homological dimension 0). This holds for the UNTWISTED bimodule A and identically for")
log("  the W-TWISTED bimodule A_W (A_W is still a perfectly good A-bimodule; twisting the module")
log("  structure does not change the algebra's separability).")
log("")
log("  => HH^1(A,A_W) = HH^2(A,A_W) = 0 IDENTICALLY (the zero series) -- an EXACT, provable KILL")
log("     at n=1,2 vs any nonzero target (comp1, comp2 both have nonzero coefficients throughout).")
log("  => HH^0(A,A_W) has dimension <= dim(Tube(Fib)) = 7 (bounded, in fact typically the fixed")
log("     subspace of a W-twisted center, dimension <= 4 = #simples of Z(Fib)).")
log("  => grading HH^0's trace by the twist eigenvalues theta_1=1, theta_tau=e^{4pi i/5} (a FIXED")
log("     set of at most 5 distinct values, per the prereg's own T0 statement) produces, at best,")
log("     a FINITE Laurent polynomial / eventually-PERIODIC object in the grading variable --")
log("     never an infinite, unboundedly-growing, non-periodic series.")

# explicit, named witness: RR coefficients grow without bound (partition-type growth);
# any object built from <=7 dims of at-most-5th-root-of-unity phases is bounded in absolute
# value by 7*max|phase|=7 for ANY grading power -- comp1/comp2 exceed this almost immediately.
witness_n = 40
c1w, c2w = comp1_reduced[witness_n], comp2_reduced[witness_n]
log("\n  explicit witness (n=%d): comp1_reduced[%d]=%d, comp2_reduced[%d]=%d -- |value| >> 7 =" %
    (witness_n, witness_n, c1w, witness_n, c2w))
log("  the hard bound on ANY graded trace built from <=7 dims of unit-modulus (5th-root-of-unity)")
log("  phases (|sum of <=7 unit-modulus terms| <= 7, for every single grading slot); RR growth")
log("  is unbounded (partition-type asymptotics) => an EXPLICIT, EXACT, bankable mismatch at")
log("  n=%d (and at every sufficiently large n thereafter)." % witness_n)
gate_witness = abs(c1w) > 7 and abs(c2w) > 7
assert gate_witness

log("\nT0 OVERALL VERDICT: KILL (HH^{1,2}=0 identically by semisimplicity -- a proved, not merely")
log("  observed, fact for ANY fusion category's tube algebra; HH^0's graded trace is bounded/")
log("  periodic vs the target's unbounded aperiodic growth -- explicit witness at n=%d). This" % witness_n)
log("  CORROBORATES the B674 trace-blindness pattern: T0's defining operation (a graded TRACE)")
log("  is structurally incapable of carrying the streams, exactly as tr(A1*|H^1(Gamma(5))) was.")

RESULTS["T0"] = {
    "verdict": "KILL",
    "tube_dim": tube_dim,
    "tube_dim_eq_7_gate": gate_tube_dim7,
    "tube_blocks": {("x=%s,a=%s,b=%s" % k): v for k, v in tube_blocks.items()},
    "FR_axiom_gates": {"F2_eq_I": gate_F2_eq_I, "F_symmetric": gate_F_sym,
                       "golden_relation": gate_golden_rel, "B484_braid_reproduction_neg3_phi": gate_braid},
    "field_finding": "F-matrix needs sqrt(phi) (genuine degree-4 field), not literally Q(sqrt5) alone",
    "HH_argument": {
        "HH1_HH2_identically_zero": "proved via semisimplicity of Tube(Fib) (cited theorem + "
                                     "dim=7 computed here from first principles)",
        "HH0_bound": "<= dim(Tube(Fib)) = 7 (typically <=4, #simples of Z(Fib))",
        "grading_is_finite_set": ["theta_1=1", "theta_tau=exp(4*pi*i/5)"],
    },
    "witness": {"n": witness_n, "comp1_reduced_n": c1w, "comp2_reduced_n": c2w,
                "bound_on_graded_trace": 7, "gate": gate_witness},
    "trace_blindness_corroboration": "matches B674 (Eichler-Shimura tr(A1*|H^1(Gamma(5)))=0 identically)",
}

# =====================================================================
# FINAL -- overall summary, write deliverables
# =====================================================================
log("\n" + "=" * 100)
log("OVERALL VERDICT SUMMARY")
log("=" * 100)
log("  target reproduction : PASS  (3 independent routes agree exactly to %d terms)" % N)
log("  T2 (chiral character sum, weld-weighted)      : KILL  (structural class-mismatch + n=0")
log("                                                          irrationality, all variants)")
log("  T1 (double Z(Fib) character sum, full weld)   : KILL  (same n=0 irrationality obstruction)")
log("  T0 (weld-twisted Hochschild trace on Tube(Fib)): KILL  (HH^{1,2}=0 by semisimplicity;")
log("                                                          HH^0 bounded/periodic; explicit")
log("                                                          witness at n=%d)" % witness_n)
log("")
log("  TRACE-BLINDNESS PATTERN (corroborates B674's independent finding on route 1):")
log("  every fully-diagonal-summed / fully-traced object collapses to a single SCALAR or to a")
log("  bounded/periodic object with zero chance of matching the RR streams' unbounded, aperiodic")
log("  growth; the character-level ROW candidates (T2/T1) at least have the right infinite/")
log("  growing SHAPE (built from G(q),H(q), which do grow correctly) but fail on the weld's")
log("  exact algebraic VALUE (irrational leading coefficients) rather than on shape -- itself a")
log("  bankable distinction from T0's shape-level failure.")
log("")
log("  total runtime %.1fs" % (time.time() - T_START))

RESULTS["overall"] = {
    "target_reproduction": "PASS",
    "T2_verdict": "KILL",
    "T1_verdict": "KILL",
    "T0_verdict": "KILL",
    "trace_blindness_pattern": (
        "corroborates B674 (frontier/B674_generation_leg, read-only): fully-traced objects "
        "(T0's HH graded trace; the T1 diagonal-sum, which literally equals tr(W_FIB)*tr(W')) "
        "collapse to scalars/bounded-periodic objects; T2/T1's character-level row candidates "
        "have the correct unbounded/aperiodic SHAPE (inherited from G(q),H(q)) but fail on the "
        "weld's exact algebraic VALUE (irrational, non-rational leading coefficients) -- a "
        "value-level obstruction, distinct from T0's shape-level obstruction."
    ),
    "runtime_seconds": round(time.time() - T_START, 1),
}

with open(os.path.join(HERE, "g1_run.log"), "w") as fh:
    fh.write("\n".join(OUT) + "\n")

with open(os.path.join(HERE, "g1_results.json"), "w") as fh:
    json.dump(RESULTS, fh, indent=1, default=str)

log("\nwrote g1_run.log + g1_results.json")
