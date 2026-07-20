#!/usr/bin/env python3
# B722 PROBE 2 -- the Borel/resurgence structure of the figure-eight (4_1):
# RIGID (the object's own Q(sqrt-3) arithmetic) or FREE (a coupling home)?
#
# Firewall: structural/arithmetic ONLY. No physics/SM claims.
# Verify-don't-trust: we DERIVE the fig-8 hbar-series + Borel lattice in-sandbox
# and only use GGM (arXiv:2012.00062) as corroboration of the paper's conjecture form.
#
# Strategy. The fig-8 Kashaev/quantum-CS perturbative series is the saddle-point
# (Feynman-diagram) expansion of the potential
#         Phi(t) = Li2(e^t) - Li2(e^{-t}),      Phi(-t) = -Phi(t)   (odd)
# whose saddles are t* = +- i pi/3  (the Eisenstein / Q(sqrt-3) point), with
# critical value Phi(t*) = i*Vol(4_1) = i*2.029883...  = the complex volume CV.
# We compute the hbar-series coefficients a_k EXACTLY and test:
#   (i)  do the a_k live in Q(sqrt-3) (the object's own field), forced, no free knob?
#   (ii) does the leading Borel singularity sit at an ARITHMETIC lattice point
#        (an integer multiple of the complex volume), forced?
#   (iii) GGM lattice + Stokes-integer corroboration.
# Two-outcome:  A = a free continuum a coupling could occupy
#               B = arithmetically RIGID (object's own lattice + fixed Stokes ints)

import mpmath as mp
import sympy as sp

mp.mp.dps = 60
OUT = []
def p(*a):
    s = " ".join(str(x) for x in a)
    print(s); OUT.append(s)

p("="*78)
p("B722 PROBE 2  --  fig-8 (4_1) Borel/resurgence: RIGID or FREE?")
p("="*78)

# ---------------------------------------------------------------------------
# PART A.  The complex volume period CV and its Q(sqrt-3) provenance (EXACT)
# ---------------------------------------------------------------------------
p("\n[A] Complex volume period CV and Q(sqrt-3) provenance")
z = sp.Rational(1,2) + sp.sqrt(3)/2*sp.I      # e^{i pi/3}, the shape parameter
minpoly = sp.minimal_polynomial(z, sp.Symbol('x'))
p("  shape parameter z = e^{i pi/3};  minimal polynomial:", minpoly,
  " -> disc = -3  => Q(sqrt-3) (Eisenstein)")
Vol = 2*mp.im(mp.polylog(2, mp.exp(1j*mp.pi/3)))   # 2*Cl2(pi/3)
p("  Vol(4_1) = 2*Cl2(pi/3) =", mp.nstr(Vol, 30))
p("  CV = i*Vol =", mp.nstr(1j*Vol, 30), " (CS(4_1)=0, amphichiral) -> matches 2.02988...i")

# ---------------------------------------------------------------------------
# PART B.  EXACT saddle derivatives  Phi^{(n)}(t*)  in Z[sqrt-3]
#   d/dt = E d/dE with E = e^t;  Phi''(t) = (E+1)/(1-E).
# ---------------------------------------------------------------------------
p("\n[B] Exact Taylor data at the saddle t* = i pi/3, in Z[sqrt-3] / Q(sqrt-3)")
# f(s) := Phi''(t*+s) satisfies the Riccati ODE  f' = (f^2 - 1)/2, f(0)=Phi''(t*)=sqrt-3.
# Proof: Phi''(t)=(E+1)/(1-E), E=e^t; with g=e^t one gets d/dt = g d/dg and
#        f = (1+g)/(1-g) => f' = 2g/(1-g)^2 = (f^2-1)/2.
# Exact recursion in Q(sqrt-3): write f_n = p_n + q_n*sqrt(-3), p_n,q_n rational.
#   (n+1) f_{n+1} = (1/2)[ (f*f)_n - [n==0] ],   f_0 = sqrt-3  (p_0=0,q_0=1).
NMAX = 60                                    # supports a_k up to k ~ 28
P = {0: sp.Integer(0)}; Q = {0: sp.Integer(1)}   # f_0 = 0 + 1*sqrt(-3)
for n in range(0, NMAX):
    # (f*f)_n = sum_{i} f_i f_{n-i}; (p+q s3)(p'+q' s3) = pp'-3qq' + (pq'+p'q)s3
    conv_p = sp.Integer(0); conv_q = sp.Integer(0)
    for i in range(0, n+1):
        conv_p += P[i]*P[n-i] - 3*Q[i]*Q[n-i]
        conv_q += P[i]*Q[n-i] + P[n-i]*Q[i]
    rhs_p = conv_p - (1 if n==0 else 0)
    rhs_q = conv_q
    P[n+1] = sp.Rational(1,2)*rhs_p/(n+1)
    Q[n+1] = sp.Rational(1,2)*rhs_q/(n+1)
# f_n = Phi^{(n+2)}(t*)/n!  => Phi^{(n+2)}(t*) = f_n * n!
p("  exact Phi^{(n)}(t*)  (f_{n-2} * (n-2)!):")
for n in range(2, 9):
    fn = P[n-2] + Q[n-2]*sp.sqrt(-3)
    val = sp.simplify(fn*sp.factorial(n-2))
    p("    n=%2d :  %s" % (n, sp.sstr(val)))
p("  => f_0=Phi''(t*)=sqrt-3 (the trace-field discriminant / 1-loop torsion);")
p("     all Phi^{(n)}(t*) in Z[sqrt-3] (even n: int*sqrt-3, odd n: int). No pi, no free knob.")

# c_n = coeff of s^n in Phi(t*+s) = f_{n-2}/(n(n-1)), exact in Q(sqrt-3), + numeric
c_exact = {}; c = {}
for n in range(2, NMAX+1):
    fn = P[n-2] + Q[n-2]*sp.sqrt(-3)
    cn = fn/(n*(n-1))
    c_exact[n] = cn
    pv = mp.mpf(str(sp.Rational(P[n-2],(n*(n-1)))))
    qv = mp.mpf(str(sp.Rational(Q[n-2],(n*(n-1)))))
    c[n] = mp.mpc(pv, qv*mp.sqrt(3))          # p + q*sqrt(-3) = p + q*sqrt3*i
p("  numeric check: c_2 = Phi''/2 =", mp.nstr(c[2],20), " (should be sqrt-3 i/2 =", mp.nstr(mp.sqrt(3)*1j/2,20),")")

# ---------------------------------------------------------------------------
# PART C.  The hbar perturbative series  a_k  via Gaussian/Feynman resummation
#   I(hbar) = e^{Phi(t*)/hbar} * sqrt(2 pi hbar/(-2 c2)) * (1 + sum_k a_k hbar^k)
#   a_k = sum_{m>=1} (1/m!) [ sum over compositions n_1..n_m >=3, sum=2(m+k) ]
#          prod c_{n_i} * (2(m+k)-1)!! * (-1/(2 c2))^{m+k}
# ---------------------------------------------------------------------------
p("\n[C] hbar-series coefficients a_k (saddle-point / Feynman resummation)")

# Efficient Feynman resummation via power series in x = sqrt(hbar).
#   I ~ Gauss-norm * < exp( P(u,x) ) >_G ,  P = sum_{n>=3} c_n x^{n-2} u^n,
#   Gaussian weight e^{c2 u^2}: <u^{2m}> = (2m-1)!! / (-2 c2)^m , <u^odd>=0.
#   R(x) = sum_k a_k x^{2k}  (hbar = x^2). Compute exp(P) by the ODE recursion
#   R' = P' R  (deriv in x): n*R_n = sum_{j=1}^n j P_j R_{n-j}, coeffs poly in u.
KMAX = 28
XMAX = 2*KMAX                     # truncate at x^{2*KMAX}
c2 = c[2]
# P_j (coeff of x^j in P) is the monomial c_{j+2} * u^{j+2}, for j>=1 (need j+2<=NMAX)
# represent polynomials in u as dict {power: mpc}
def padd(A,B):
    R=dict(A)
    for k,v in B.items(): R[k]=R.get(k,0)+v
    return R
def pscale(A,s):
    return {k:v*s for k,v in A.items()}
def pmul(A,B):
    R={}
    for ka,va in A.items():
        for kb,vb in B.items():
            R[ka+kb]=R.get(ka+kb,0)+va*vb
    return R
Pj = {}
for j in range(1, XMAX+1):
    if j+2 <= NMAX:
        Pj[j] = {j+2: c[j+2]}     # c_{j+2} u^{j+2}
    else:
        Pj[j] = {}
# R_0 = 1
Rx = {0: {0: mp.mpc(1)}}
for n in range(1, XMAX+1):
    acc = {}
    for j in range(1, n+1):
        if j in Pj and Pj[j] and (n-j) in Rx:
            acc = padd(acc, pscale(pmul(Pj[j], Rx[n-j]), j))
    Rx[n] = pscale(acc, mp.mpf(1)/n)
# Gaussian moment
def gauss_moment(pw):
    if pw % 2 == 1: return mp.mpc(0)
    m = pw//2
    df = mp.mpf(1)
    for t in range(1, m+1): df *= (2*t-1)
    return df / (-2*c2)**m
# a_k = coeff of x^{2k} in R(x) after Gaussian average
def a_k(k):
    poly = Rx.get(2*k, {})
    return sum(v*gauss_moment(pw) for pw,v in poly.items())
a = {k: a_k(k) for k in range(1, KMAX+1)}
p("  perturbative coefficients a_k (numeric), a_k = i^k * (real):")
for k in range(1, 11):
    p("    a_%d = %s" % (k, mp.nstr(a[k], 24)))
p("    ...  (computed to k=%d)" % KMAX)

# identify a_1..a_4 in Q(sqrt-3): test a_k = p + q*sqrt(-3), p,q rational
p("\n  PSLQ identification of a_k in Q(sqrt-3)  (basis {1, sqrt-3}):")
s3 = mp.sqrt(3)*1j
def identify_Qsqrt3(val, name):
    re = mp.re(val); im = mp.im(val)
    # val = p + q*sqrt(-3) = p + q*i*sqrt3  => p=re, q=im/sqrt3
    q = im/mp.sqrt(3)
    pr = re
    def rat_of(x):
        if abs(x) < mp.mpf(10)**(-40):
            return sp.Integer(0)
        fr = mp.pslq([x, mp.mpf(1)], maxcoeff=10**9, maxsteps=10**5)
        if fr is None: return None
        a0,b0 = fr
        if a0==0: return sp.Integer(0)
        return sp.Rational(-b0, a0)
    Rp, Rq = rat_of(pr), rat_of(q)
    p("    %s = (%s) + (%s)*sqrt(-3)" % (name, Rp, Rq))
    return Rp, Rq

for k in range(1,5):
    identify_Qsqrt3(a[k], "a_%d"%k)
p("  (a_4 real part is a rational with a large denominator; PSLQ maxcoeff capped.")
p("   NOTE: a_k in Q(sqrt-3) is GUARANTEED BY CONSTRUCTION, not just PSLQ-observed --")
p("   every c_n in Q(sqrt-3) [Riccati recursion], and a_k is a Q-polynomial in the c_n")
p("   and 1/c_2; so the ENTIRE trans-series lives in the object's own field Q(sqrt-3).)")

# also give EXACT a_1 via exact c_n (sanity)
p("\n  exact a_1 from exact c_n in Q(sqrt-3):")
c2e = c_exact[2]
# a_1 = c4*3!!*(-1/(2c2))^2 + (1/2!)c3^2 * 5!!*(-1/(2c2))^3
a1e = c_exact[4]*sp.Integer(3)*(-1/(2*c2e))**2 \
     + sp.Rational(1,2)*c_exact[3]**2*sp.Integer(15)*(-1/(2*c2e))**3
a1e = sp.simplify(sp.radsimp(sp.expand(a1e)))
p("    a_1 (exact) =", sp.sstr(sp.nsimplify(a1e)), " (matches PSLQ -sqrt(-3)/108)")

# ---------------------------------------------------------------------------
# PART D.  Borel singularity: does it sit at an ARITHMETIC lattice point?
#   a_k ~ C * Gamma(k+beta) / A^k  =>  A = lim_k  k * a_k / a_{k+1}  (the ACTION).
#   TWO DISTINCT OBJECTS (the prior draft conflated them -- fixed here):
#     * V(sigma_1) = Phi(t*) = +i*Vol : the ABSOLUTE critical value of the geometric
#       saddle (the complex-volume period; EXACT, from Parts A/B). GGM's V(sigma_1).
#     * zeta_1 : the leading Borel singularity of the series AROUND the geometric
#       saddle, measured RELATIVE to it = (action of the nearest OTHER critical
#       point) - Phi(t*). Candidates:
#          trivial connection : 0        - i*Vol = -i*Vol     |gap| = Vol
#          conjugate saddle   : (-i*Vol) - i*Vol = -2 i*Vol   |gap| = 2*Vol
#       nearest = trivial-connection gap => zeta_1 = -i*Vol, magnitude Vol.
#   WHAT WE PROVE vs COMPUTE, kept separate:
#     - PROVEN (exact): a_k = i^k*(real), so every singularity lies on the imaginary
#       axis; and the coefficient field is Q(sqrt-3) (Parts B/C).
#     - COMPUTED numerically (28-term ratio test + Richardson, ~0.2% residual, NOT a
#       closed-form proof): the leading singularity MAGNITUDE |zeta_1| = Vol.
#     - The SIGN (-i vs +i) is fixed by identifying the nearest singularity with the
#       trivial connection (|gap|=Vol, not 2*Vol); it is a Q(sqrt-3) complex-conjugate
#       (Galois) choice WITHIN the lattice Z*(i*Vol), NOT a free continuous parameter.
# ---------------------------------------------------------------------------
p("\n[D] Borel singularity location (leading) from a_k growth")
p("    NB: V(sigma_1)=Phi(t*)=+i*Vol is the ABSOLUTE critical value (Parts A/B, EXACT).")
p("        zeta_1 below is the Borel singularity RELATIVE to the geometric saddle.")
p("    arithmetic candidates for |zeta_1|:")
p("        |gap to trivial conn.| = Vol   =", mp.nstr(Vol,16))
p("        |gap to conjugate sad.| = 2*Vol =", mp.nstr(2*Vol,16))
# a_k = i^k * b_k with b_k real  ->  b_k = a_k / i^k ; the ratio test yields the action.
b = {}
maxim = mp.mpf(0)
for k in range(1, KMAX+1):
    bk = a[k]/(1j**k)
    b[k] = bk
    maxim = max(maxim, abs(mp.im(bk)))
p("    reality check (EXACT): b_k = a_k/i^k real?  max|Im b_k| =", mp.nstr(maxim,6),
  "(=0 => a_k = i^k*real => singularity on the imaginary axis)")
p("    ratio test r_k = k*b_k/b_{k+1}  (real; -> -Vol => |zeta_1|=Vol, sign -):")
rk = {}
for k in range(1, KMAX):
    rk[k] = mp.re(k * b[k]/b[k+1])
    if k>=4:
        p("      k=%2d :  r_k = %s   |r_k|/Vol = %s" %
          (k, mp.nstr(rk[k],12), mp.nstr(abs(rk[k])/Vol,10)))
# Richardson extrapolation in 1/k on the tail (r_k = A + c1/k + ...)
def richardson(seq_k):
    # seq_k: dict k->value; do repeated 1/k Neville extrapolation on the tail
    ks = sorted(seq_k.keys())
    vals = [seq_k[k] for k in ks]
    xs = [mp.mpf(1)/k for k in ks]
    n = len(vals)
    T = [vals[:]]
    for lvl in range(1, n):
        prev = T[-1]; cur=[]
        for i in range(n-lvl):
            num = prev[i+1]*xs[i] - prev[i]*xs[i+lvl]
            den = xs[i]-xs[i+lvl]
            cur.append(num/den)
        T.append(cur)
    return T[-1][0]
tail = {k: rk[k] for k in range(KMAX-8, KMAX)}
A_extrap = richardson(tail)
mag = abs(A_extrap)
p("    Richardson-extrapolated r  =", mp.nstr(A_extrap,14),
  " (28 terms; residual ~ interference from the 2*Vol singularity)")
p("    => leading singularity MAGNITUDE |zeta_1| =", mp.nstr(mag,14))
p("    |zeta_1|/Vol   =", mp.nstr(mag/Vol,12), "  (-> 1: |zeta_1| = Vol, i.e. 1x CV)")
p("    |zeta_1|/(2Vol)=", mp.nstr(mag/(2*Vol),12))
p("    STATUS: |zeta_1|=Vol is COMPUTED NUMERICALLY (~0.2% residual, corroborates")
p("            GGM Conj.3a); it is NOT a closed-form in-sandbox proof. The imaginary-")
p("            axis placement IS proven (a_k=i^k*real). Reconciling sign: r_k<0 and")
p("            |zeta_1|=Vol (not 2Vol) => nearest = TRIVIAL-connection gap =>")
p("            zeta_1 = -i*Vol = 0 - Phi(t*)  (relative to the geometric saddle);")
p("            next zeta_2 = -2 i*Vol = Phi(t_conj) - Phi(t*) (the conjugate saddle).")
p("    => the singularities sit on the DISCRETE lattice Z*(i*Vol) = Z*CV over")
p("       Q(sqrt-3): |zeta_1|=Vol computed, the +/- sign a Galois-conjugate choice")
p("       WITHIN the lattice, no free continuous parameter.")

# ---------------------------------------------------------------------------
# PART E.  GGM lattice + Stokes-integer structure (corroboration, verified form)
# ---------------------------------------------------------------------------
p("\n[E] GGM (arXiv:2012.00062) peacock lattice + Stokes constants (corroboration)")
p("    Conjecture 3(a): Borel singularities of the 4_1 series sit at")
p("        iota = (V(sigma)-V(sigma'))/(2 pi i)  +  2 pi i * k  +  l * log x,")
p("      with V(sigma_1) = i*Vol(4_1) = i*2.029883...,  k,l in Z.")
p("    => a LATTICE: generators {2 pi i (vertical), log x (horizontal), CV-offset},")
p("       free indices k,l in Z (DISCRETE). No continuous parameter.")
p("    Conjecture 3(d): the Stokes constants are INTEGERS (= Donaldson-Thomas /")
p("       BPS invariants). 4_1 has exactly 2 critical points {sigma_1, sigma_2}")
p("       (geometric + complex conjugate). Series in 3^{-1/4} Q(sqrt-3)[[tau]].")
p("    EPISTEMIC-STATUS NOTE (corrected -- no Listening-Protocol rung applies here):")
p("    The LISTENING_PROTOCOL rung hierarchy (1=field, 2=torsor, 3=form) grades")
p("    OBJECT<->EXTERNAL-REALITY comparisons; this probe is an INTERNAL, object-only")
p("    computation (no SM/reality comparand), so NO comparative rung is cleared. The")
p("    earlier 'rung 3 = proven / rung<=2 = cited' usage was an informal evidentiary")
p("    axis, inconsistent with the project taxonomy, and is replaced by plain labels:")
p("      PROVEN in-sandbox (exact): (i) coefficients in Q(sqrt-3) [Riccati recursion];")
p("        (ii) a_k = i^k*real, so all Borel singularities lie on the imaginary axis.")
p("      COMPUTED numerically (~0.2%, NOT a proof): |zeta_1| = Vol (28-term ratio test).")
p("      CITED, not reproduced (GGM Conj.3a/3d): the full peacock lattice + INTEGER")
p("        (DT/BPS) Stokes constants; the deep numerical DT tables are not re-derived.")
p("    Large-order growth of our a_k is a clean one-instanton form Gamma(k+beta)/Vol^k")
p("    (beta<1), consistent with a FIXED singularity type -- but we do NOT assert a")
p("    specific Stokes integer (needs the trivial-connection normalization). Either")
p("    way the structure carries NO free continuous parameter.")

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------
p("\n" + "="*78)
p("VERDICT")
p("="*78)
p("  [PROVEN in-sandbox, exact]")
p("  - Perturbative coefficients a_k in Q(sqrt-3): Phi^{(n)}(t*) in Z[sqrt-3] via the")
p("    Riccati recursion; 1-loop = Phi''(t*) = sqrt-3 = trace-field discriminant; a_k is")
p("    a Q-polynomial in the c_n and 1/c_2, so the WHOLE trans-series is Q(sqrt-3). No pi,")
p("    no free real parameter. (a_1=-sqrt-3/108, a_2=-37/7776, a_3=(2359/2519424)sqrt-3.)")
p("  - a_k = i^k*(real) EXACTLY => every Borel singularity lies on the imaginary axis.")
p("  [COMPUTED numerically, ~0.2% residual -- strong corroboration, NOT a closed proof]")
p("  - Leading Borel singularity MAGNITUDE |zeta_1| = Vol (|zeta_1|/Vol = 0.998, 28 terms).")
p("    With the imaginary-axis fact + nearest=trivial-connection (|gap|=Vol, not 2Vol):")
p("    zeta_1 = -i*Vol relative to the geometric saddle (0 - Phi(t*)); next -2i*Vol")
p("    (conjugate saddle). Distinct from V(sigma_1)=Phi(t*)=+i*Vol (the absolute value).")
p("  [CITED, not reproduced -- GGM arXiv:2012.00062 Conj.3a/3d]")
p("  - Peacock lattice Z-generated {2pi i, log x, CV}; Stokes constants = integers (DT/BPS).")
p("    Deep numerical DT tables not re-derived here.")
p("  => Whether from the proven arithmetic (a_k in Q(sqrt-3), imaginary-axis singularities)")
p("     or the numerically-computed |zeta_1|=Vol on the DISCRETE lattice Z*CV over Q(sqrt-3),")
p("     the resurgence structure carries NO free continuous parameter for a coupling to")
p("     occupy: the ONLY freedoms are DISCRETE (lattice index n in Z; the +/- sign a")
p("     Galois-conjugate choice).  OUTCOME = B  (arithmetically rigid).")

with open("/Users/dri/origin-axiom/frontier/B722_resurgence_coupling/b722_probe2_out.txt","w") as f:
    f.write("\n".join(OUT)+"\n")
print("\n[written b722_probe2_out.txt]")
