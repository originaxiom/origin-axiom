#!/usr/bin/env python3
# B674 generation leg / ramanujan_trifocal
# The three Ramanujan continued fractions (RR p=5, cubic p=3, octic p=2)
# at the metallic cusp parameters, per the web-seat handoff AS CORRECTED by
# the main-seat adjudication:
#   golden cusp: tau = 2*sqrt(3)*i  (lattice Z[2*sqrt(-3)], disc -48, h=2; NOT j=0)
#   silver cusp: tau = 2i           (disc -16 order Z[2i]; CM)
#   bronze     : NOT CM (Galois S4) -> leg does not run (pre-adjudicated).
# All arithmetic: mpmath, working dps 200, independent re-verification at dps 320.
# Identification: PSLQ minimal polynomials, degree cap 8, |coeff| cap 1e24,
# maxsteps 20000; stated candidate fields Q(sqrt2,sqrt3,sqrt5,phi,zeta5,zeta6,i)
# tested via sympy factorization over QQ(sqrt2,sqrt3,sqrt5) (values are real).
# Failed identification is reported as UNIDENTIFIED, never forced.
import os, sys, hashlib, time
from mpmath import mp, mpf, mpc, exp, pi, sqrt, log, pslq, polyroots, nstr, fabs
try:
    from mpmath import kleinj
    HAVE_KLEINJ = True
except ImportError:
    HAVE_KLEINJ = False
import sympy as sp

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
OUTPATH = os.path.join(HERE, "values_output.txt")
OUTBUF = []
def emit(s=""):
    print(s, flush=True)
    OUTBUF.append(str(s))
def flush_out():
    with open(OUTPATH, "w") as f:
        f.write("\n".join(OUTBUF) + "\n")

def qpow(q, num, den):
    # q^(num/den) for real q in (0,1)
    return exp(mpf(num) / mpf(den) * log(q))

def emax_for(q, extra=50):
    # exponent E with q^E < 10^-(dps+extra)
    return int((mp.dps + extra) * mp.log(10) / (-log(q))) + 12

def poch_minus(q, r, m, E=None):
    # prod_{k>=0, e=r+km<=E} (1 - q^e)
    if E is None:
        E = emax_for(q)
    p = mpf(1)
    e = r
    while e <= E:
        p *= (1 - q**e)
        e += m
    return p

def poch_plus(q, r, m, E=None):
    if E is None:
        E = emax_for(q)
    p = mpf(1)
    e = r
    while e <= E:
        p *= (1 + q**e)
        e += m
    return p

# ---------------- the three continued fractions (product forms) -------------
def R_rr(q, E=None):
    # Rogers-Ramanujan: q^{1/5} (q;q^5)(q^4;q^5)/((q^2;q^5)(q^3;q^5))
    return qpow(q, 1, 5) * poch_minus(q, 1, 5, E) * poch_minus(q, 4, 5, E) \
        / (poch_minus(q, 2, 5, E) * poch_minus(q, 3, 5, E))

def V_cubic(q, E=None):
    # Ramanujan cubic CF: q^{1/3} (q;q^6)(q^5;q^6)/(q^3;q^6)^2
    return qpow(q, 1, 3) * poch_minus(q, 1, 6, E) * poch_minus(q, 5, 6, E) \
        / poch_minus(q, 3, 6, E)**2

def U_octic(q, E=None):
    # ADOPTED octic definition (see report):
    #   U(q) = sqrt(2) q^{1/8} prod (1+q^{2n})/(1+q^{2n-1}) = (theta2/theta3)^{1/2}
    # the unique modular sign-variant of the handoff's stated shape.
    return sqrt(2) * qpow(q, 1, 8) * poch_plus(q, 2, 2, E) / poch_plus(q, 1, 2, E)

def U_handoff(q, E=None):
    # the handoff's LITERAL product: sqrt(2) q^{1/8} prod (1-q^{2n-1})/(1+q^{2n})
    # = sqrt(2) q^{1/4} eta(tau)/eta(4tau)  (NOT weight-0 modular; see control C5)
    return sqrt(2) * qpow(q, 1, 8) * poch_minus(q, 1, 2, E) / poch_plus(q, 2, 2, E)

# ---------------- thetas, eta, Eisenstein j ---------------------------------
def theta2(q):
    E = emax_for(q)
    n, s = 0, mpf(0)
    while n * (n + 1) <= E:
        s += q**(n * (n + 1))
        n += 1
    return 2 * qpow(q, 1, 4) * s

def theta3(q):
    E = emax_for(q)
    n, s = 1, mpf(1)
    while n * n <= E:
        s += 2 * q**(n * n)
        n += 1
    return s

def eta_q(q):
    # Dedekind eta as a function of the nome q = e^{2 pi i tau}
    return qpow(q, 1, 24) * poch_minus(q, 1, 1)

def j_eisenstein(q, nmax):
    E4 = mpf(1)
    E6 = mpf(1)
    for n in range(1, nmax + 1):
        t = q**n / (1 - q**n)
        E4 += 240 * n**3 * t
        E6 -= 504 * n**5 * t
    num = E4**3
    den = num - E6**2
    return 1728 * num / den

# ---------------- PSLQ minimal-polynomial machinery -------------------------
DEG_CAP = 8
COEFF_CAP = 10**24
MAXSTEPS = 20000
LO_DPS = 200
HI_DPS = 320
# NOTE (honesty): at working dps 200, PSLQ can reliably detect a degree-8
# relation only up to coefficient height ~10^(200/9) ~ 10^22; the effective
# joint cap is min(1e24, that ceiling). Stated in the report.

def try_pslq_minpoly(x, maxdeg=DEG_CAP):
    """Return (deg, coeffs ascending) of the first (=lowest-degree) integer
    relation found for [1, x, ..., x^d], or None. NO verification here."""
    for d in range(1, maxdeg + 1):
        vec = [x**k for k in range(d + 1)]
        try:
            rel = pslq(vec, tol=mpf(10)**(-(LO_DPS - 30)),
                       maxcoeff=COEFF_CAP, maxsteps=MAXSTEPS)
        except Exception:
            rel = None
        if rel is not None and any(c != 0 for c in rel) and rel[d] != 0:
            from math import gcd
            g = 0
            for c in rel:
                g = gcd(g, abs(c))
            rel = [c // g for c in rel]
            if rel[d] < 0:
                rel = [-c for c in rel]
            return (d, rel)
    return None

def verify_relation(coeffs, x_hi):
    """Junk guard: evaluate at the INDEPENDENTLY recomputed dps-320 value,
    under dps-340 arithmetic.  True relations give residual ~ scale*10^-315;
    spurious dps-200 artifacts floor at ~ scale*10^-170 and are rejected."""
    with mp.workdps(HI_DPS + 20):
        val = mpf(0)
        scale = mpf(0)
        for k, c in enumerate(coeffs):
            term = mpf(c) * x_hi**k
            val += term
            scale = max(scale, fabs(term))
        thresh = max(scale, mpf(1)) * mpf(10)**(-(HI_DPS - 40))
        return fabs(val) < thresh, fabs(val), thresh

def poly_root_check(coeffs, x_hi):
    """Confirm x_hi is a root of the integer polynomial to near-full precision."""
    with mp.workdps(HI_DPS + 20):
        try:
            roots = polyroots([mpf(c) for c in coeffs[::-1]], maxsteps=300,
                              extraprec=200)
        except Exception:
            return False, None
        best = min(fabs(r - x_hi) for r in roots)
        return best < mpf(10)**(-(HI_DPS - 50)), best

def sympy_field_report(coeffs, x_val_60):
    """Factor the found minpoly over QQ and over QQ(sqrt2,sqrt3,sqrt5) (the
    real subfield generated by the stated candidate fields; all our values are
    real).  Return (irreducible?, closed_form or None)."""
    xs = sp.symbols('x')
    P = sum(sp.Integer(c) * xs**k for k, c in enumerate(coeffs))
    fl_q = sp.factor_list(P)[1]
    irred = (len(fl_q) == 1 and fl_q[0][1] == 1)
    closed = None
    try:
        fl_e = sp.factor_list(P, extension=[sp.sqrt(2), sp.sqrt(3), sp.sqrt(5)])[1]
        target = sp.Float(x_val_60, 60)
        for fac, mult in fl_e:
            pf = sp.Poly(fac, xs)
            if pf.degree() == 1:
                a, b = pf.all_coeffs()
                root = sp.simplify(-b / a)
                if abs(sp.N(root, 70) - target) < sp.Float(10)**(-50):
                    closed = root
                    break
    except Exception as ex:
        closed = None
    return irred, closed

def identify(name, x_lo, x_hi, maxdeg=DEG_CAP, field_check=True):
    """Full identification pipeline with junk guards. Returns coeffs or None."""
    emit(f"  [{name}] value = {nstr(x_lo, 62)}")
    agree = fabs(x_lo - x_hi)
    emit(f"  [{name}] dps-{LO_DPS} vs dps-{HI_DPS} recomputation |diff| = {nstr(agree, 3)}")
    res = try_pslq_minpoly(x_lo, maxdeg)
    if res is None:
        emit(f"  [{name}] PSLQ: NO relation, degrees 1..{maxdeg} "
             f"(caps: |coeff|<=1e24, maxsteps={MAXSTEPS}, dps={LO_DPS}) -> UNIDENTIFIED")
        return None
    d, coeffs = res
    ok1, resid, thr = verify_relation(coeffs, x_hi)
    ok2, rootdist = poly_root_check(coeffs, x_hi)
    emit(f"  [{name}] PSLQ candidate deg {d}: coeffs (asc) = {coeffs}")
    emit(f"  [{name}]   high-precision residual {nstr(resid,3)} "
         f"(threshold {nstr(thr,3)}) -> {'PASS' if ok1 else 'FAIL'}")
    emit(f"  [{name}]   root-match dist {nstr(rootdist,3) if rootdist is not None else 'n/a'}"
         f" -> {'PASS' if ok2 else 'FAIL'}")
    if not (ok1 and ok2):
        emit(f"  [{name}] candidate REJECTED by the dps-{HI_DPS} guard -> UNIDENTIFIED")
        return None
    if field_check:
        irred, closed = sympy_field_report(coeffs, nstr(x_hi, 60))
        emit(f"  [{name}]   minpoly irreducible over Q: {irred}")
        if closed is not None:
            emit(f"  [{name}]   closed form IN the stated fields: {closed}"
                 f"  = {sp.N(closed, 30)}")
        else:
            emit(f"  [{name}]   no linear factor over QQ(sqrt2,sqrt3,sqrt5): "
                 f"value is algebraic (minpoly above) but NOT in the stated "
                 f"candidate fields")
    unit = abs(coeffs[0]) == 1 and abs(coeffs[-1]) == 1
    emit(f"  [{name}]   algebraic unit (|lead|=|const|=1): {unit}")
    return coeffs

# ============================================================================
mp.dps = HI_DPS       # HIGH-precision pass first (guard values)
HI = {}

def compute_all(store):
    q_g = exp(-4 * pi * sqrt(3))     # golden: tau = 2*sqrt(3)*i, q = e^{-4 pi sqrt3}
    q_s = exp(-4 * pi)               # silver: tau = 2i,          q = e^{-4 pi}
    q_a = exp(-2 * pi)               # anchor/control point:      tau = i
    store['q_g'], store['q_s'], store['q_a'] = q_g, q_s, q_a
    # j at golden, two Eisenstein truncations + conjugate form (3,0,4)
    n1 = max(30, emax_for(q_g))
    store['j_g_t1'] = j_eisenstein(q_g, n1)
    store['j_g_t2'] = j_eisenstein(q_g, 2 * n1)
    q_g2 = exp(-4 * pi / sqrt(3))    # tau2 = 2i/sqrt(3), the (3,0,4) form of disc -48
    n2 = max(60, emax_for(q_g2))
    store['j_g2'] = j_eisenstein(q_g2, n2)
    store['j_2i'] = j_eisenstein(q_s, max(60, emax_for(q_s)))   # control: must be 66^3
    # CF values
    for tag, q in (('g', q_g), ('s', q_s), ('a', q_a)):
        store['R_' + tag] = R_rr(q)
        store['V_' + tag] = V_cubic(q)
        store['U_' + tag] = U_octic(q)
        store['Uh_' + tag] = U_handoff(q)
        store['t23_' + tag] = theta2(q) / theta3(q)     # = sqrt(k)
    # helpers
    for tag in ('g', 's', 'a'):
        R = store['R_' + tag]
        store['R5_' + tag] = R**5
        store['tR_' + tag] = 1 / R**5 - 11 - R**5       # = (eta(tau)/eta(5tau))^6
        V = store['V_' + tag]
        store['V3_' + tag] = V**3
        U = store['U_' + tag]
        store['U2_' + tag] = U**2
        store['U4_' + tag] = U**4
    # eta-based identity controls at the anchor
    q = q_a
    store['etaq_a'] = eta_q(q)
    store['etaq5_a'] = eta_q(q**5)
    store['etaq4_a'] = eta_q(q**4)
    store['eta_ratio6_a'] = (store['etaq_a'] / store['etaq5_a'])**6
    return store

compute_all(HI)
HI_SNAP = dict(HI)

mp.dps = LO_DPS       # working pass
LO = {}
compute_all(LO)

def hi(name):
    # bring the dps-260 value into the current (160) context untouched
    return HI_SNAP[name]

emit("=" * 78)
emit("B674 / ramanujan_trifocal - values_output.txt")
emit("The three Ramanujan CFs at the metallic cusp parameters (main-seat-corrected)")
emit(f"working dps = {LO_DPS}; independent guard recomputation at dps = {HI_DPS}")
emit(f"PSLQ caps: degree <= {DEG_CAP}, |coeff| <= 1e24, maxsteps = {MAXSTEPS}")
emit("  (effective reliable height ceiling at deg 8, dps 200: ~1e22)")
emit("stated candidate fields: Q(sqrt2, sqrt3, sqrt5, phi, zeta5, zeta6, i);")
emit("  real values => field test = linear factor over QQ(sqrt2, sqrt3, sqrt5)")
emit("=" * 78)

# ---------------- C: pipeline controls --------------------------------------
emit("")
emit("## C. PIPELINE CONTROLS (all in-sandbox; no cited values)")
sqrt5 = sqrt(mpf(5)); phi = (1 + sqrt5) / 2

# C1: j(2i) must equal 66^3 = 287496 (disc -16, h=1)
d = fabs(LO['j_2i'] - 287496)
emit(f"C1 j(2i) via Eisenstein q-series = {nstr(LO['j_2i'], 30)}")
emit(f"   |j(2i) - 287496| = {nstr(d, 3)}  -> {'PASS' if d < mpf(10)**-120 else 'FAIL'}")

# C2: R(e^-2pi) vs sqrt(phi*sqrt5) - phi (classical RR value at tau=i)
rr_exact = sqrt(phi * sqrt5) - phi
d = fabs(LO['R_a'] - rr_exact)
emit(f"C2 R(e^-2pi) = {nstr(LO['R_a'], 62)}")
emit(f"   sqrt(phi*sqrt5)-phi = {nstr(rr_exact, 62)}")
emit(f"   |diff| = {nstr(d, 3)}  -> {'PASS' if d < mpf(10)**-140 else 'FAIL'}")

# C3: U(q) == (theta2/theta3)^(1/2) (adopted octic = sqrt of the modulus ratio)
qt = mpf(1) / 10
d = fabs(U_octic(qt) - sqrt(theta2(qt) / theta3(qt)))
emit(f"C3 U(q) - sqrt(theta2/theta3) at q=0.1: |diff| = {nstr(d, 3)}"
     f"  -> {'PASS' if d < mpf(10)**-140 else 'FAIL'}")
d = fabs(LO['U_a'] - sqrt(LO['t23_a']))
emit(f"   same at q=e^-2pi: |diff| = {nstr(d, 3)}"
     f"  -> {'PASS' if d < mpf(10)**-140 else 'FAIL'}")

# C4: theta2/theta3 at e^-2pi: PSLQ singular modulus (expected x^2+2x-1, root sqrt2-1)
emit("C4 theta2/theta3 at q=e^-2pi (the 4th singular value, derived in-sandbox):")
c4 = identify("t23_a", LO['t23_a'], hi('t23_a'), maxdeg=4)
d = fabs(LO['t23_a'] - (sqrt(mpf(2)) - 1))
emit(f"   |theta2/theta3 - (sqrt2-1)| = {nstr(d, 3)}"
     f"  -> {'PASS (= 1/delta silver!)' if d < mpf(10)**-140 else 'FAIL'}")

# C5: the handoff's literal octic product = sqrt2 q^{1/4} eta(tau)/eta(4tau)
d = fabs(LO['Uh_a'] - sqrt(mpf(2)) * qpow(LO['q_a'], 1, 4)
         * LO['etaq_a'] / LO['etaq4_a'])
emit(f"C5 Uh(q) - sqrt2 q^(1/4) eta(tau)/eta(4tau) at q=e^-2pi: |diff| = {nstr(d, 3)}"
     f"  -> {'PASS' if d < mpf(10)**-140 else 'FAIL'}")
emit("   (bare q^(1/4) factor => NOT a weight-0 modular function; no CM algebraicity)")

# C6: the RR eta identity 1/R^5 - 11 - R^5 = (eta(tau)/eta(5tau))^6 at anchor
d = fabs(LO['tR_a'] - LO['eta_ratio6_a'])
emit(f"C6 (1/R^5-11-R^5) - (eta/eta5)^6 at q=e^-2pi: |diff| = {nstr(d, 3)}"
     f"  -> {'PASS' if d < mpf(10)**-130 else 'FAIL'}")

# C7: cubic CF eta-quotient identity V = eta(t)eta(6t)^3/(eta(2t)eta(3t)^3)
qt = mpf(1) / 10
lhs = V_cubic(qt)
rhs = eta_q(qt) * eta_q(qt**6)**3 / (eta_q(qt**2) * eta_q(qt**3)**3)
d = fabs(lhs - rhs)
emit(f"C7 V(q) - eta(t)eta(6t)^3/(eta(2t)eta(3t)^3) at q=0.1: |diff| = {nstr(d, 3)}"
     f"  -> {'PASS' if d < mpf(10)**-140 else 'FAIL'}")

# C8: octic anchor value U(e^-2pi) and its minpoly (expected sqrt(sqrt2-1))
emit("C8 U(e^-2pi) (the octic anchor special value, derived in-sandbox):")
identify("U_a", LO['U_a'], hi('U_a'), maxdeg=4)
d = fabs(LO['U_a'] - sqrt(sqrt(mpf(2)) - 1))
emit(f"   |U(e^-2pi) - sqrt(sqrt2-1)| = {nstr(d, 3)}"
     f"  -> {'PASS' if d < mpf(10)**-140 else 'FAIL'}")

# C9: the handoff-literal octic at the anchor: PSLQ must FAIL (non-modular)
emit("C9 Uh(e^-2pi) (handoff-literal octic) identification attempt:")
identify("Uh_a", LO['Uh_a'], hi('Uh_a'))
flush_out()

# ---------------- T1: j at the golden cusp ----------------------------------
emit("")
emit("## T1. j(tau) AT THE GOLDEN CUSP  tau = 2*sqrt(3)*i  (disc -48, h=2)")
emit(f"q_golden = exp(-4 pi sqrt3) = {nstr(LO['q_g'], 62)}")
d_trunc = fabs(LO['j_g_t1'] - LO['j_g_t2'])
emit(f"j via Eisenstein, truncation N: |j(N) - j(2N)| = {nstr(d_trunc, 3)} (stability)")
emit(f"j(2*sqrt3*i) = {nstr(LO['j_g_t1'], 62)}")
if HAVE_KLEINJ:
    jk = 1728 * kleinj(mpc(0, 2 * sqrt(mpf(3))))
    emit(f"cross-check 1728*kleinj: |diff| = {nstr(fabs(LO['j_g_t1'] - jk.real), 3)}")
emit("PSLQ on [1, j, j^2]:")
jrel = try_pslq_minpoly(LO['j_g_t1'], maxdeg=2)
if jrel is None:
    emit("  NO quadratic relation found -> UNIDENTIFIED (unexpected)")
else:
    dj, cj = jrel
    emit(f"  degree {dj} relation, coeffs (asc) = {cj}")
    ok1, resid, thr = verify_relation(cj, hi('j_g_t1'))
    ok2, rootdist = poly_root_check(cj, hi('j_g_t1'))
    emit(f"  dps-{HI_DPS} residual {nstr(resid,3)} (thr {nstr(thr,3)}) -> {'PASS' if ok1 else 'FAIL'}")
    emit(f"  root-match dist {nstr(rootdist,3)} -> {'PASS' if ok2 else 'FAIL'}")
    # class-polynomial check: the second root must be j at the (3,0,4) form
    xs = sp.symbols('x')
    P = sum(sp.Integer(c) * xs**k for k, c in enumerate(cj))
    emit(f"  H_-48 candidate: {sp.expand(P)} = 0")
    sols = sp.solve(sp.Eq(P, 0), xs)
    for s_ in sols:
        emit(f"    exact root: {sp.radsimp(s_)}")
        emit(f"      = {sp.N(s_, 65)}")
    d2 = min(fabs(LO['j_g2'] - mpf(sp.N(s_, 200).__str__())) for s_ in sols)
    emit(f"  conjugate check: j(2i/sqrt3) [form (3,0,4)] = {nstr(LO['j_g2'], 40)}")
    emit(f"    min dist to a root of the found quadratic = {nstr(d2, 3)}"
         f" -> {'PASS' if d2 < mpf(10)**-120 else 'FAIL'}")
emit("VERDICT: j(2*sqrt3*i) != 0 - the handoff's j=0 hypothesis is refuted "
     "(adjudication point 1 confirmed numerically).")
flush_out()

# ---------------- T2-T4: the three CFs at the golden cusp -------------------
emit("")
emit("## T2. R(q_golden)  (Rogers-Ramanujan, p=5)")
identify("R_g", LO['R_g'], hi('R_g'))
emit("  structured attempt via R^5 and the level-5 eta variable t = 1/R^5-11-R^5:")
identify("R5_g", LO['R5_g'], hi('R5_g'))
identify("tR_g", LO['tR_g'], hi('tR_g'))
emit("  explicit phi-expression checks (T2):")
for nm, val in [("phi", phi), ("1/phi", 1/phi), ("1/(2phi)", 1/(2*phi)),
                ("phi^2", phi**2), ("sqrt(phi*sqrt5)-phi", rr_exact),
                ("1/phi^2", 1/phi**2)]:
    emit(f"    |R_g - {nm}| = {nstr(fabs(LO['R_g'] - val), 8)}")
flush_out()

emit("")
emit("## T3. V(q_golden)  (Ramanujan cubic, p=3)")
identify("V_g", LO['V_g'], hi('V_g'))
emit("  structured attempt via V^3:")
identify("V3_g", LO['V3_g'], hi('V3_g'))
emit("  explicit sqrt3/zeta6-adjacent checks (T3):")
s3 = sqrt(mpf(3))
for nm, val in [("sqrt3-1", s3-1), ("2-sqrt3", 2-s3), ("(sqrt3-1)/2", (s3-1)/2),
                ("2*sqrt3-3", 2*s3-3), ("1/2", mpf(1)/2), ("sqrt3/2", s3/2)]:
    emit(f"    |V_g - {nm}| = {nstr(fabs(LO['V_g'] - val), 8)}")
flush_out()

emit("")
emit("## T4. U(q_golden)  (octic, p=2)  [adopted definition; see C3-C5, C8-C9]")
identify("U_g", LO['U_g'], hi('U_g'))
emit("  structured attempts via U^2 = theta2/theta3 = sqrt(k48) and U^4 = k48:")
identify("U2_g", LO['U2_g'], hi('U2_g'))
identify("U4_g", LO['U4_g'], hi('U4_g'))
emit("  the handoff-literal octic at golden (non-modular; expected UNIDENTIFIED):")
identify("Uh_g", LO['Uh_g'], hi('Uh_g'))
flush_out()

# ---------------- T5: ratios at golden --------------------------------------
emit("")
emit("## T5. RATIOS AT THE GOLDEN CUSP")
rat = {}
for nm, a, b in (("R/V", 'R_g', 'V_g'), ("R/U", 'R_g', 'U_g'), ("V/U", 'V_g', 'U_g')):
    rat[nm] = (LO[a] / LO[b], hi(a) / hi(b))
    identify(nm, rat[nm][0], rat[nm][1])
flush_out()

# ---------------- T6: the silver cusp ---------------------------------------
emit("")
emit("## T6. THE SILVER CUSP  tau = 2i, q = exp(-4 pi)  (disc -16; CM)")
emit(f"q_silver = {nstr(LO['q_s'], 62)}")
emit("octic (the handoff's primary silver test):")
identify("U_s", LO['U_s'], hi('U_s'))
identify("U2_s", LO['U2_s'], hi('U2_s'))
identify("U4_s", LO['U4_s'], hi('U4_s'))
emit("  handoff-literal octic at silver (non-modular; expected UNIDENTIFIED):")
identify("Uh_s", LO['Uh_s'], hi('Uh_s'))
emit("RR at silver:")
identify("R_s", LO['R_s'], hi('R_s'))
identify("R5_s", LO['R5_s'], hi('R5_s'))
identify("tR_s", LO['tR_s'], hi('tR_s'))
emit("cubic at silver:")
identify("V_s", LO['V_s'], hi('V_s'))
identify("V3_s", LO['V3_s'], hi('V3_s'))
emit("silver-ratio checks (delta = 1+sqrt2):")
s2 = sqrt(mpf(2))
for nm, val in [("sqrt2-1", s2-1), ("1+sqrt2", 1+s2), ("sqrt2", s2),
                ("sqrt(sqrt2-1)", sqrt(s2-1))]:
    emit(f"    |U_s - {nm}| = {nstr(fabs(LO['U_s'] - val), 8)}")
flush_out()

# ---------------- T7: cross-check against the banked menu -------------------
emit("")
emit("## T7. CROSS-CHECK AGAINST BANKED QUANTITIES")
emit("h3 candidates derived in-sandbox from the banked minpoly 5x^4+5x^3+1:")
h3roots = polyroots([5, 5, 0, 0, 1])
h3mods = sorted(set(round(float(fabs(r)), 12) for r in h3roots))
h3c = {}
seen = []
for r in h3roots:
    m = fabs(r)
    if not any(fabs(m - s) < mpf(10)**-30 for s in seen):
        seen.append(m)
for i_, m in enumerate(seen):
    h3c[f"|h3_root{i_+1}|"] = m
    h3c[f"|h3_root{i_+1}|^2"] = m**2
    emit(f"  |h3 root {i_+1}| = {nstr(m, 30)}   modulus^2 = {nstr(m**2, 30)}")
emit(f"  norm check: prod|roots|*5 ... N(h3) = 1/5 -> prod moduli^2 = "
     f"{nstr((seen[0]*seen[1])**2 if len(seen)>1 else seen[0]**4, 30)} (expect 0.2)")

CAND = {"phi": phi, "1/phi": 1/phi, "1/(2phi)": 1/(2*phi), "phi^2": phi**2,
        "sqrt5": sqrt5, "1/2": mpf(1)/2, "sqrt3/2": s3/2, "sqrt3": s3,
        "2sqrt3-3": 2*s3-3, "sqrt3-1": s3-1, "1/delta=sqrt2-1": s2-1,
        "delta=1+sqrt2": 1+s2, "24": mpf(24), "1": mpf(1), "sqrt2": s2,
        "2": mpf(2), "D4ceiling~1.7849887(8-digit ref)": mpf("1.7849887")}
CAND.update(h3c)

VALS = {"j_golden": LO['j_g_t1'], "R_g": LO['R_g'], "V_g": LO['V_g'],
        "U_g": LO['U_g'], "Uh_g(nonmod)": LO['Uh_g'],
        "R/V_g": rat["R/V"][0], "R/U_g": rat["R/U"][0], "V/U_g": rat["V/U"][0],
        "V/R_g": 1/rat["R/V"][0], "U/R_g": 1/rat["R/U"][0], "U/V_g": 1/rat["V/U"][0],
        "R_s": LO['R_s'], "V_s": LO['V_s'], "U_s": LO['U_s'],
        "Uh_s(nonmod)": LO['Uh_s'],
        "sqrt(k48)=U_g^2": LO['U2_g'], "sqrt(k16)=U_s^2": LO['U2_s']}

emit("")
emit("hit table (exact: |diff|<1e-40; near-miss flag: |diff|<1e-6):")
nhits = 0
for vn, vv in VALS.items():
    for cn, cv in CAND.items():
        dd = fabs(vv - cv)
        if dd < mpf(10)**-40:
            emit(f"  EXACT HIT: {vn} = {cn}   (|diff| = {nstr(dd,3)})")
            nhits += 1
        elif dd < mpf(10)**-6:
            tag = " [8-digit reference only - coincidence-candidate]" \
                if "1.7849887" in cn else " [coincidence-candidate only]"
            emit(f"  near-miss: {vn} ~ {cn}   (|diff| = {nstr(dd,3)}){tag}")
            nhits += 1
if nhits == 0:
    emit("  NO exact hits and NO near-misses within 1e-6 across the full table.")
emit("")
emit("full 60-digit value dump:")
for vn, vv in VALS.items():
    emit(f"  {vn:20s} = {nstr(vv, 62)}")
flush_out()

# ---------------- provenance ------------------------------------------------
emit("")
emit("## PROVENANCE")
with open(os.path.abspath(__file__), "rb") as f:
    emit(f"sha256(trifocal_values.py) = {hashlib.sha256(f.read()).hexdigest()}")
emit(f"runtime {time.time()-T0:.1f} s; mpmath working dps {LO_DPS}, guard dps {HI_DPS}")
emit("bronze leg: NOT RUN - pre-adjudicated (cusp field certified non-abelian "
     "S4, degree 8, B675 addendum; no CM/Duke algebraicity guarantee; the "
     "bronze column of the proposed trifocal VALUE table cannot run as proposed).")
flush_out()
print("DONE")
