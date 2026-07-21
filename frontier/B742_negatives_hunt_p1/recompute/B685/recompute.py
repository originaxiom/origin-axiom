#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B739 Stage-B recompute — target B685 (generation-terminal kill, kind-mismatch).

CLAIM KILLED (banked): that a framework-derivable generator of the figure-eight
produces the {2/5,3/5} 5-adic hearing streams. The Habiro/Nahm leg of the kill
rests on a CITED-UNVERIFIED external fact (GSWZ): the figure-eight's symmetrised
Habiro/state-integral series Phi(h)Phi(-h) is integral away from 3 (denominators
pure powers of 3 — carrying NO 5), while the {2/5,3/5} streams require GROWING
5-adic denominators (divided-power law, B683).

THE DISCRIMINATING FACT (recomputed here, E19 compute-not-cite, both directions):
  (a) OBJECT SIDE: the coefficients of the figure-eight's symmetrised series
      Phi(h)Phi(-h), expanded in x = q-1 (q = e^h), have denominators that are
      pure powers of 3; in particular v5(denominator) = 0 at every order.
      We RE-DERIVE Phi(h) from the knot's own state-sum datum (the Kashaev
      invariant <4_1>_N = sum_{k=0}^{N-1} |(q;q)_k|^2, q = e^{2 pi i/N}) by
      exact formal Gaussian summation at the geometric saddle k ~ 5N/6 — we do
      NOT copy GSWZ's series; their displayed eq (1)/(2) coefficients are used
      only as a cross-check that our derivation lands in their convention.
  (b) HEARING SIDE: the {2/5,3/5} stream carriers (q;q)_inf^{-2/5} and
      (q;q)_inf^{-3/5} have v5(den c_n) = n + v5(n!) EXACTLY (growing without
      bound) — recomputed here from scratch (independent re-implementation of
      the B683 law, not a citation).
  KIND-MISMATCH: (a) gives v5(den) = 0 at every computed order; (b) forces
  v5(den) -> infinity. No framework-derivable generator of the object can
  produce the 5-adic hearing streams.

EXTERNAL SOURCE (tractability = needs-web; convention-pinning only, quoted +
access-dated per prereg §16 style):
  S. Garoufalidis, P. Scholze, C. Wheeler, D. Zagier, "The Habiro ring of a
  number field", arXiv:2412.04241v2 [math.NT] (27 Aug 2025), pp. 2-3.
  Accessed 2026-07-21 (arxiv.org PDF).
  Quote 1 (p.2): "One of the experiments in question involved the power series
    Phi(h) that appear in the asymptotic expansion of the Kashaev invariant of
    the 4_1 knot, whose first few terms are given (after multiplication by an
    overall eighth root of unity) by [26, Eqn.(3)]"
  Quote 2 (p.3, their Eqn (1)):
    "Phi(h) = 1/(-3)^{1/4} (1 + 11/(24*3*sqrt(-3)) h
              + 697/(1152*(3 sqrt(-3))^2) h^2
              + 724351/(414720*(3 sqrt(-3))^3) h^3 + ...)"
  Quote 3 (p.3): "the denominator of the coefficient of h^100 was given by
    2^397 3^298 5^40 7^22 11^12 13^9 17^6 19^5 23^4 29^3 31^3 37^2 41^2 43^2
    47^2 53 59 61 67 71 73 79 83 89 97 101"   [the UNsymmetrised series]
  Quote 4 (p.3, their Eqn (2)): "However, the symmetrised series Phi(h)Phi(-h),
    after a change of variable q = e^h starts with
    Phi(h)Phi(-h) = 1/sqrt(-3) (1 - 1/3^3 (q-1)^2 + 1/3^3 (q-1)^3
                    - 4/3^5 (q-1)^4 - 1/3^5 (q-1)^5 + O((q-1)^6)),
    with all coefficients being integral away from 3, e.g. the denominator of
    the coefficient of (q-1)^100 being 3^146."
  Quote 5 (p.3): "On the other hand the series (2), which lies in
    Z[1/sqrt(-3)][[q-1]] ..."

DECLARED CONVENTIONS (E1 — implicit in the original arc, declared here):
  C1. q = e^h with h = 2 pi i / N (GSWZ's variable for eq (1)/(2)); the
      Kashaev invariant of 4_1 is <4_1>_N = sum_{k=0}^{N-1} |(q;q)_k|^2
      = sum_k prod_{j<=k} 4 sin^2(pi j / N).
  C2. Saddle/window convention: N ≡ 0 (mod 6), geometric saddle at a = 5N/6;
      window sum extended to m in Z; theta/Poisson corrections (exponentially
      small, e.g. exp(-pi N/sqrt(3))) dropped — the standard formal-Gaussian-
      summation convention (GSWZ §2.5 "Formal Gaussian integration").
  C3. Normalisation: all prefactors (g(a), sqrt(pi/lambda), (-3)^{-1/4}, the
      "overall eighth root of unity") dropped; every series normalised to
      constant term 1. GSWZ's integrality statement is for the series in
      Z[1/sqrt(-3)][[q-1]]; since 1/sqrt(-3) = -sqrt(-3)/3 is a unit times
      3^{-1}, "denominator is a pure power of 3" for the normalised
      parenthetical series is equivalent to their statement.
  C4. sqrt(-3) := i*sqrt(3) (principal branch). "Denominator" of a coefficient
      u + v*sqrt(-3) (u, v in Q, reduced) := lcm(den(u), den(v)).
  C5. The symmetrised series is the FORMAL product Phi(h)*Phi(-h) of eq-(1)'s
      series with itself under h -> -h (GSWZ's own operation); it is even in h,
      so the sign convention of h (q = e^h vs q = e^{-h}) does not affect it.
  C6. Normalisation bridge to GSWZ eq (1): GSWZ/GZ normalise the Kashaev
      asymptotics by the LEADING factor N^{3/2} 3^{-1/4} e^{N Vol/(2 pi)};
      this recompute normalises by the FULL local prefactor
      g(5N/6)*sqrt(N/sqrt(3)) (g = the running state-sum product). The two
      differ by B(h) = exp(beta_1 h + beta_3 h^3 + ...), an exponential of an
      ODD series in h (Euler-Maclaurin corrections to log g(5N/6) carry only
      odd powers of 1/N), so B(h)B(-h) = 1 identically and the symmetrised
      object is convention-independent. The recompute VERIFIES this bridge:
      (i) beta_1 := a_1 - c_1 is pure sqrt(-3); (ii) the even-order lock
      a_2 = c_2 + beta_1 c_1 + beta_1^2/2 holds exactly (a_n = GSWZ eq (1),
      c_n = this derivation); (iii) numerically, g(5N/6) = N e^{N Vol/(2 pi)}
      * (1 + beta_1 h + O(h^3)) with the computed beta_1 and no h^2 term.

DETERMINISM: exact rational arithmetic (fractions.Fraction) over Q(sqrt(3)) and
Q(sqrt(-3)); no wall-clock, no randomness, no network access in this script.

Depth: object side K = 20 (q-1)-adic orders (GSWZ display only 6); hearing side
n <= 60 for both carriers.
"""

from fractions import Fraction
import math

K = 20        # depth of the object-side series (orders of h and of x = q-1)
NC = 60       # depth of the hearing-carrier check

RMAX = 2 * K + 1

FAILURES = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        FAILURES.append(label)


# ----------------------------------------------------------------------------
# Q(sqrt(3)) arithmetic: element (a, b) := a + b*sqrt(3), a, b in Q
# ----------------------------------------------------------------------------
F0 = (Fraction(0), Fraction(0))
F1 = (Fraction(1), Fraction(0))


def fadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def fmul(x, y):
    return (x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def fscale(x, c):
    return (x[0] * c, x[1] * c)


def fiszero(x):
    return x[0] == 0 and x[1] == 0


# ----------------------------------------------------------------------------
# Q(sqrt(-3)) arithmetic: element (u, v) := u + v*sqrt(-3), u, v in Q
# ----------------------------------------------------------------------------
def qmul(x, y):
    return (x[0] * y[0] - 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qscale(x, c):
    return (x[0] * c, x[1] * c)


Q1 = (Fraction(1), Fraction(0))


def qpow(x, n):
    r = Q1
    for _ in range(n):
        r = qmul(r, x)
    return r


# ----------------------------------------------------------------------------
# Step 1: gamma series — log-summand of the window ratio.
# w(t) = 4 sin^2(pi(5N/6 + t)/N) = (cos u - sqrt(3) sin u)^2,  u = pi t/N.
# gamma(u) := 2*log(cos u - sqrt(3) sin u) = sum_{r>=1} gamma_r u^r,
# gamma_r in Q(sqrt(3)).
# ----------------------------------------------------------------------------
def series_mul(A, B, nmax):
    out = [F0] * (nmax + 1)
    for i, ai in enumerate(A):
        if fiszero(ai):
            continue
        for j in range(0, nmax - i + 1):
            bj = B[j]
            if not fiszero(bj):
                out[i + j] = fadd(out[i + j], fmul(ai, bj))
    return out


cos_s = [F0] * (RMAX + 1)
sin_s = [F0] * (RMAX + 1)
for t in range(0, RMAX + 1, 2):
    cos_s[t] = (Fraction((-1) ** (t // 2), math.factorial(t)), Fraction(0))
for t in range(1, RMAX + 1, 2):
    sin_s[t] = (Fraction((-1) ** ((t - 1) // 2), math.factorial(t)), Fraction(0))

# w1 = cos u - sqrt(3) sin u - 1   (order >= 1)
w1 = [F0] * (RMAX + 1)
for t in range(RMAX + 1):
    w1[t] = fadd(cos_s[t], fscale((sin_s[t][1], sin_s[t][0]), Fraction(-1)))
    # sqrt(3)*sin term: sin coeff (a,0) -> sqrt(3)*a = (0,a); subtract
w1[0] = fadd(w1[0], (Fraction(-1), Fraction(0)))

# gamma = 2*log(1 + w1) = 2 * sum_{j>=1} (-1)^{j+1} w1^j / j
gamma = [F0] * (RMAX + 1)
w1p = [F1] + [F0] * RMAX  # w1^0
for j in range(1, RMAX + 1):
    w1p = series_mul(w1p, w1, RMAX)
    c = Fraction(2 * (-1) ** (j + 1), j)
    for t in range(RMAX + 1):
        if not fiszero(w1p[t]):
            gamma[t] = fadd(gamma[t], fscale(w1p[t], c))

print("=" * 78)
print("B739 Stage-B recompute — B685 (figure-eight: symmetrised Habiro series")
print("carries no 5; the {2/5,3/5} hearing carriers demand growing 5-powers)")
print("=" * 78)
print()
print("STEP 1 — log-summand expansion  2*log(cos u - sqrt(3) sin u):")
check("gamma_1 = -2*sqrt(3)", gamma[1] == (Fraction(0), Fraction(-2)))
check("gamma_2 = -4", gamma[2] == (Fraction(-4), Fraction(0)))
# float sanity of the composed series at u = 1/100
uf = 0.01
gf = sum((float(a) + float(b) * math.sqrt(3)) * uf ** t
         for t, (a, b) in enumerate(gamma))
gt = 2.0 * math.log(math.cos(uf) - math.sqrt(3) * math.sin(uf))
check("gamma series matches float log at u=0.01 (|diff|<1e-15)",
      abs(gf - gt) < 1e-15)

# ----------------------------------------------------------------------------
# Step 2: Bernoulli numbers (B+ convention, B1 = +1/2) and Faulhaber
# S_r(m) = sum_{t=1}^m t^r = (1/(r+1)) sum_{j=0}^{r} C(r+1,j) B+_j m^{r+1-j}
# ----------------------------------------------------------------------------
BER = [Fraction(1)]  # B-_0
for mm in range(1, RMAX + 1):
    acc = Fraction(0)
    for j in range(mm):
        acc += math.comb(mm + 1, j) * BER[j]
    BER.append(-acc / (mm + 1))
BER[1] = Fraction(1, 2)  # switch to B+ convention

FAUL = {}  # FAUL[r][s] = coefficient of m^s in S_r(m)
for r in range(1, RMAX + 1):
    row = {}
    for j in range(0, r + 1):
        s = r + 1 - j
        c = Fraction(math.comb(r + 1, j), r + 1) * BER[j]
        if c != 0:
            row[s] = c
    FAUL[r] = row

print()
print("STEP 2 — Faulhaber polynomials:")
check("S_3(5) = 225", sum(c * 5 ** s for s, c in FAUL[3].items()) == 225)
check("S_1(m) = (m^2+m)/2",
      FAUL[1] == {2: Fraction(1, 2), 1: Fraction(1, 2)})

# ----------------------------------------------------------------------------
# Step 3: the exponent polynomial
# LP(m) = sum_r gamma_r eps^r S_r(m)  (eps = pi/N; window ratio g(a+m)/g(a)
#         = exp(LP(m)) for all m in Z, a = 5N/6)
# Extract lambda: LP = -lambda m^2 + R(m, eps), lambda = sqrt(3)*eps.
# R stored as dict {(r, s): F-coeff} for monomials eps^r m^s, graded by
# half-weight W = 2r - s >= 1; monomials with W > 2K cannot contribute.
# ----------------------------------------------------------------------------
R = {}
for r in range(1, RMAX + 1):
    if fiszero(gamma[r]):
        continue
    for s, c in FAUL[r].items():
        key = (r, s)
        val = fscale(gamma[r], c)
        if key in R:
            R[key] = fadd(R[key], val)
        else:
            R[key] = val

lam_entry = R.pop((1, 2))
print()
print("STEP 3 — exponent polynomial LP(m):")
check("quadratic term is -sqrt(3)*eps*m^2 (lambda = sqrt(3) eps)",
      lam_entry == (Fraction(0), Fraction(-1)))
check("all remaining monomials have half-weight W = 2r - s >= 1",
      all(2 * r - s >= 1 for (r, s) in R))
R = {k: v for k, v in R.items() if 2 * k[0] - k[1] <= 2 * K and not fiszero(v)}

# ----------------------------------------------------------------------------
# Step 4: E = exp(R), graded by half-weight W (finite, exact).
# Recursion: W*E_W = sum_{W'=1..W} (W'*R_{W'}) * E_{W-W'}.
# ----------------------------------------------------------------------------
Rw = {}
for (r, s), c in R.items():
    Rw.setdefault(2 * r - s, {})[(r, s)] = c

Eparts = {0: {(0, 0): F1}}
for W in range(1, 2 * K + 1):
    acc = {}
    for Wp, terms in Rw.items():
        if Wp > W:
            continue
        Eprev = Eparts.get(W - Wp)
        if not Eprev:
            continue
        for (r1, s1), c1 in terms.items():
            c1w = fscale(c1, Fraction(Wp))
            for (r2, s2), c2 in Eprev.items():
                key = (r1 + r2, s1 + s2)
                prod = fmul(c1w, c2)
                if key in acc:
                    acc[key] = fadd(acc[key], prod)
                else:
                    acc[key] = prod
    invW = Fraction(1, W)
    Eparts[W] = {k: fscale(v, invW) for k, v in acc.items() if not fiszero(v)}

# ----------------------------------------------------------------------------
# Step 5: formal Gaussian summation over m in Z.
# sum_m e^{-lam m^2} m^{2j} eps^r -> sqrt(pi/lam) * (2j-1)!! (2 lam)^{-j} eps^r
# lam = sqrt(3) eps, (2 sqrt(3))^{-1} = sqrt(3)/6. Odd powers of m vanish.
# Normalised: G(eps) = 1 + sum_{n>=1} g_n eps^n, g_n in Q(sqrt(3)).
# ----------------------------------------------------------------------------
maxj = 4 * K + 2
dfact = [1] * (maxj + 1)
for j in range(1, maxj + 1):
    dfact[j] = dfact[j - 1] * (2 * j - 1)
pow6 = [F1] * (maxj + 1)
for j in range(1, maxj + 1):
    pow6[j] = fmul(pow6[j - 1], (Fraction(0), Fraction(1, 6)))

G = [F0] * (K + 1)
ok_grade = True
for W in range(0, 2 * K + 1, 2):
    n = W // 2
    for (r, s), c in Eparts.get(W, {}).items():
        if s % 2:
            continue
        j = s // 2
        if r - j != n:
            ok_grade = False
        G[n] = fadd(G[n], fscale(fmul(c, pow6[j]), Fraction(dfact[j])))

print()
print("STEP 4/5 — graded exp + formal Gaussian summation:")
check("grading consistency (eps-order = W/2 for every surviving monomial)",
      ok_grade)
check("G(0) = 1 (normalised saddle series)", G[0] == F1)

# ----------------------------------------------------------------------------
# Step 6: convert to GSWZ's variable h = 2 pi i/N:  eps = -i h/2.
# Coefficient of h^n: c_n = g_n * (-i)^n / 2^n; must land in Q(sqrt(-3)):
# even n -> g_n rational; odd n -> g_n pure sqrt(3). (sqrt(-3) := i sqrt(3).)
# ----------------------------------------------------------------------------
S = [None] * (K + 1)  # S[n] = (u, v) meaning u + v*sqrt(-3)
purity_ok = True
for n in range(K + 1):
    x, y = G[n]
    if n % 2 == 0:
        if y != 0:
            purity_ok = False
        sgn = (-1) ** ((n // 2) % 2)
        S[n] = (Fraction(sgn) * x / 2 ** n, Fraction(0))
    else:
        if x != 0:
            purity_ok = False
        sgn = (-1) ** (((n - 1) // 2 + 1) % 2)   # (-i)^n = (-1)^{(n-1)/2}*(-i)
        S[n] = (Fraction(0), Fraction(sgn) * y / 2 ** n)

print()
print("STEP 6 — h-series of the geometric-saddle expansion (h = 2 pi i/N):")
check("parity purity: even coeffs rational, odd coeffs pure sqrt(-3)",
      purity_ok)

# ----------------------------------------------------------------------------
# Step 7: reconciliation with GSWZ eq (1) (convention bridge C6; NOT an input:
# the series above was derived from the state sum alone).
# GSWZ eq (1): a_n * (3 sqrt(-3))^n = 11/24, 697/1152, 724351/414720 (n=1,2,3)
# in the leading-asymptotics normalisation. Bridge: Phi_GSWZ = B(h)*S(h) with
# B = exp(odd series). beta_1 := a_1 - c_1 must be pure sqrt(-3), and the
# even-order content is locked by a_2 = c_2 + beta_1 c_1 + beta_1^2/2.
# ----------------------------------------------------------------------------
tsq = (Fraction(0), Fraction(3))  # 3*sqrt(-3)
ratio = []
for n in range(K + 1):
    rn = qmul(S[n], qpow(tsq, n))
    ratio.append(rn)

# GSWZ eq (1) coefficients as elements of Q(sqrt(-3)):
# (3 sqrt(-3))^{-1} = -sqrt(-3)/9, (3 sqrt(-3))^{-2} = -1/27,
# (3 sqrt(-3))^{-3} = (3 sqrt(-3))^{-2} * (3 sqrt(-3))^{-1} = sqrt(-3)/243
a1 = qscale((Fraction(0), Fraction(-1, 9)), Fraction(11, 24))
a2 = qscale((Fraction(-1, 27), Fraction(0)), Fraction(697, 1152))
a3 = qscale((Fraction(0), Fraction(1, 243)), Fraction(724351, 414720))

rat_ok = all(r[1] == 0 for r in ratio[:8])
print()
print("STEP 7 — reconciliation with GSWZ eq (1) [arXiv:2412.04241v2 p.3]:")
print(f"  c_1*(3 sqrt(-3))^1 = {ratio[1][0]}   (GSWZ a_1: 11/24)")
print(f"  c_2*(3 sqrt(-3))^2 = {ratio[2][0]}   (GSWZ a_2: 697/1152)")
print(f"  c_3*(3 sqrt(-3))^3 = {ratio[3][0]}   (GSWZ a_3: 724351/414720)")
check("ratios c_n*(3 sqrt(-3))^n are rational (GSWZ shape)", rat_ok)

beta1 = (a1[0] - S[1][0], a1[1] - S[1][1])
print(f"  beta_1 = a_1 - c_1 = {beta1[0]} + ({beta1[1]})*sqrt(-3)")
check("beta_1 is pure sqrt(-3) (odd-series exponent, C6)",
      beta1[0] == 0 and beta1[1] != 0)
check("beta_1 = sqrt(-3)/12", beta1 == (Fraction(0), Fraction(1, 12)))
# even-order lock: a_2 == c_2 + beta_1*c_1 + beta_1^2/2
rhs = qadd(qadd(S[2], qmul(beta1, S[1])),
           qscale(qmul(beta1, beta1), Fraction(1, 2)))
check("even-order lock: a_2 = c_2 + beta_1*c_1 + beta_1^2/2 (exact)",
      rhs == a2)
# beta_3 (free odd parameter at order 3, reported for completeness)
b3rhs = qadd(qadd(qmul(beta1, S[2]),
                  qscale(qmul(qmul(beta1, beta1), S[1]), Fraction(1, 2))),
             qscale(qmul(qmul(beta1, beta1), beta1), Fraction(1, 6)))
beta3 = (a3[0] - S[3][0] - b3rhs[0], a3[1] - S[3][1] - b3rhs[1])
print(f"  beta_3 = {beta3[0]} + ({beta3[1]})*sqrt(-3)   [odd, unconstrained]")

# ----------------------------------------------------------------------------
# Step 7b: numerical verification of the C6 bridge at the prefactor level:
# g(5N/6) =? N * e^{N*Vol/(2 pi)} * (1 + beta_1 h + O(h^3)), h = 2 pi i/N,
# i.e. l(N) := log[g(5N/6)/(N e^{N Vol/(2 pi)})] = -pi*sqrt(3)/(6N) + O(N^-3)
# (beta_1 = sqrt(-3)/12 => beta_1*h = -pi sqrt(3)/(6N), real; NO 1/N^2 term).
# Vol(4_1) = 2*Cl2(pi/3); Cl2 via the exact-Bernoulli series
# Cl2(t) = t(1 - log t) + sum_{n>=1} |B_2n| t^{2n+1} / (2 (2n)! n (2n+1)).
# ----------------------------------------------------------------------------
theta = math.pi / 3.0
cl2 = theta * (1.0 - math.log(theta))
for n in range(1, 21):  # BER available to index RMAX = 2K+1 = 41
    b2n = abs(float(BER[2 * n]))
    cl2 += b2n * theta ** (2 * n + 1) / (2.0 * math.factorial(2 * n)
                                         * n * (2 * n + 1))
# coarse independent sanity: Cl2(t) = sum sin(k t)/k^2
cl2_direct = sum(math.sin(k * theta) / k ** 2 for k in range(1, 200001))
VOL = 2.0 * cl2

print()
print("STEP 7b — numerical check of the C6 prefactor bridge:")
print(f"  Vol(4_1) = 2*Cl2(pi/3) = {VOL:.15f}")
check("Clausen series vs direct sum (|diff| < 1e-9)",
      abs(cl2 - cl2_direct) < 1e-9)

alpha1_target = -math.pi * math.sqrt(3.0) / 6.0
devs = {}
for N in (48, 96, 192, 384):
    a = 5 * N // 6
    lg = 0.0
    for k in range(1, a + 1):
        lg += math.log(4.0 * math.sin(math.pi * k / N) ** 2)
    ell = lg - math.log(N) - N * VOL / (2.0 * math.pi)
    devs[N] = N * ell - alpha1_target
    print(f"  N={N:4d}: N*l(N) = {N * ell:+.9f}   target beta_1*h*N = "
          f"{alpha1_target:+.9f}   dev = {devs[N]:+.3e}")
check("N*l(N) -> -pi*sqrt(3)/6 with ~1/N^2 convergence (no h^2 term in B)",
      abs(devs[96]) < abs(devs[48]) / 3.2 and
      abs(devs[192]) < abs(devs[96]) / 3.2 and
      abs(devs[384]) < abs(devs[192]) / 3.2)

# unsymmetrised denominators: exhibit the 5 (and 2,7,...) that GSWZ's h^100
# denominator 2^397 3^298 5^40 7^22 ... displays — here at our depth
def prime_factor(d):
    out = []
    p = 2
    dd = d
    while p * p <= dd:
        e = 0
        while dd % p == 0:
            dd //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if dd > 1:
        out.append((dd, 1))
    return out


print()
print("  UNsymmetrised-series denominators (of c_n*(3 sqrt(-3))^n, reduced):")
first5 = None
for n in range(1, K + 1):
    d = ratio[n][0].denominator
    fac = prime_factor(d)
    if first5 is None and any(p == 5 for p, _ in fac):
        first5 = n
    if n <= 8:
        print(f"    n={n:2d}: den = {d} = "
              + "*".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in fac))
check(f"UNsymmetrised series DOES carry 5s in denominators (first at n={first5})",
      first5 is not None)

# ----------------------------------------------------------------------------
# Step 8: the symmetrised series T_h(h) = S(h) * S(-h)  (GSWZ's operation).
# ----------------------------------------------------------------------------
Th = [(Fraction(0), Fraction(0)) for _ in range(K + 1)]
for a in range(K + 1):
    for b in range(K + 1 - a):
        term = qscale(qmul(S[a], S[b]), Fraction((-1) ** b))
        Th[a + b] = qadd(Th[a + b], term)

sym_ok = all(Th[n] == (Fraction(0), Fraction(0)) for n in range(1, K + 1, 2))
rat_sym_ok = all(Th[n][1] == 0 for n in range(0, K + 1))
print()
print("STEP 8 — symmetrised product S(h)*S(-h):")
check("odd h-coefficients vanish (series even in h)", sym_ok)
check("h-coefficients are rational", rat_sym_ok)

# ----------------------------------------------------------------------------
# Step 9: change of variable to x = q - 1 (q = e^h): substitute h = log(1+x).
# ----------------------------------------------------------------------------
L = [Fraction(0)] * (K + 1)
for j in range(1, K + 1):
    L[j] = Fraction((-1) ** (j + 1), j)


def rser_mul(A, B):
    out = [Fraction(0)] * (K + 1)
    for i, ai in enumerate(A):
        if ai == 0:
            continue
        for j in range(0, K - i + 1):
            if B[j]:
                out[i + j] += ai * B[j]
    return out


T = [Fraction(0)] * (K + 1)
T[0] = Th[0][0]
Lp = [Fraction(1)] + [Fraction(0)] * K
for n in range(1, K + 1):
    Lp = rser_mul(Lp, L)
    cn = Th[n][0]
    if cn:
        for t in range(K + 1):
            if Lp[t]:
                T[t] += cn * Lp[t]

# ----------------------------------------------------------------------------
# Step 10: cross-check vs GSWZ eq (2), then THE DISCRIMINATING FACT.
# ----------------------------------------------------------------------------
print()
print("STEP 9/10 — symmetrised series in x = q-1; check vs GSWZ eq (2):")
print(f"  [x^0] = {T[0]}    (GSWZ: 1)")
print(f"  [x^1] = {T[1]}    (GSWZ: 0)")
print(f"  [x^2] = {T[2]}    (GSWZ: -1/3^3 = -1/27)")
print(f"  [x^3] = {T[3]}    (GSWZ: +1/3^3 = +1/27)")
print(f"  [x^4] = {T[4]}    (GSWZ: -4/3^5 = -4/243)")
print(f"  [x^5] = {T[5]}    (GSWZ: -1/3^5 = -1/243)")
eq2_ok = (T[0] == 1 and T[1] == 0 and T[2] == Fraction(-1, 27)
          and T[3] == Fraction(1, 27) and T[4] == Fraction(-4, 243)
          and T[5] == Fraction(-1, 243))
check("eq (2) match (all 6 displayed coefficients)", eq2_ok)

print()
print("THE DISCRIMINATING FACT — denominators of the symmetrised series")
print(f"(coefficients of (q-1)^n, n <= {K}); banked kill needs: pure powers")
print("of 3, i.e. v5(den) = 0 (and no prime other than 3) at every order:")
pure3_ok = True
v5_zero_ok = True
e3_list = []
for n in range(K + 1):
    d = T[n].denominator
    e3 = 0
    dd = d
    while dd % 3 == 0:
        dd //= 3
        e3 += 1
    v5 = 0
    d5 = d
    while d5 % 5 == 0:
        d5 //= 5
        v5 += 1
    pure = (dd == 1)
    if not pure:
        pure3_ok = False
    if v5 != 0:
        v5_zero_ok = False
    e3_list.append(e3)
    num = T[n].numerator
    print(f"  n={n:2d}: coeff = {num}/{d}"
          f"   den = 3^{e3}{'' if pure else ' * ' + str(dd) + '  <-- NOT pure 3'}"
          f"   v5(den) = {v5}")
print()
check(f"ALL denominators pure powers of 3 up to (q-1)^{K}", pure3_ok)
check(f"v5(denominator) = 0 at every order n <= {K}", v5_zero_ok)
print(f"  3-exponents e_n: {e3_list}")
print("  (GSWZ report e_100 = 146 at their depth 100 — same phenomenon,")
print("   verified here independently to n = %d.)" % K)

# ----------------------------------------------------------------------------
# Step 11: numerical (float) end-to-end validation of the derived series
# against the ACTUAL Kashaev sum <4_1>_N = sum_k prod_{j<=k} 4 sin^2(pi j/N):
# <4_1>_N ~ g(5N/6) * sqrt(N/sqrt(3)) * sum_n c_n h^n,  h = 2 pi i/N.
# Fixed N in {48, 96, 192}: deterministic. Error at truncation t should fall
# like N^{-(t+1)} (ratio ~ 2^{t+1} between N and 2N).
# ----------------------------------------------------------------------------
print()
print("STEP 11 — float validation against the actual Kashaev sum:")
sq3f = math.sqrt(3.0)


def kashaev_data(N):
    total = 0.0
    prod = 1.0
    total = 1.0  # k = 0 term
    ga = None
    a = 5 * N // 6
    for k in range(1, N):
        prod *= 4.0 * math.sin(math.pi * k / N) ** 2
        total += prod
        if k == a:
            ga = prod
    return total, ga


errs = {}
for N in (48, 96, 192):
    total, ga = kashaev_data(N)
    h = 2j * math.pi / N
    pref = ga * math.sqrt(N / sq3f)
    for t in (2, 4, 6, 8):
        sv = 0j
        for n in range(t + 1):
            u, v = S[n]
            sv += (float(u) + float(v) * 1j * sq3f) * h ** n
        errs[(N, t)] = abs(total / (pref * sv) - 1.0)
for t in (2, 4, 6, 8):
    e48, e96, e192 = errs[(48, t)], errs[(96, t)], errs[(192, t)]
    r1 = e48 / e96 if e96 else float('inf')
    r2 = e96 / e192 if e192 else float('inf')
    print(f"  trunc t={t}: |ratio-1| N=48: {e48:.3e}  N=96: {e96:.3e}"
          f"  N=192: {e192:.3e}  decay ratios {r1:.1f}, {r2:.1f}"
          f"  (expected ~{2 ** (t + 1)})")
check("series is the true asymptotic expansion (errors shrink ~N^-(t+1))",
      all(errs[(96, t)] < errs[(48, t)] / 8 and
          errs[(192, t)] < errs[(96, t)] / 8 for t in (2, 4, 6)))

# ----------------------------------------------------------------------------
# Step 12: HEARING SIDE — independent recompute of the divided-power law for
# BOTH stream carriers (q;q)_inf^{-2/5} and (q;q)_inf^{-3/5}:
#     v5(den c_n) = n + v5(n!)  exactly, for 1 <= n <= NC.
# ----------------------------------------------------------------------------
def v5_int(d):
    v = 0
    while d % 5 == 0:
        d //= 5
        v += 1
    return v


def v5_fact(n):
    s = 0
    x = n
    while x:
        s += x % 5
        x //= 5
    return (n - s) // 4


def carrier_law(anum):
    """f = (q;q)_inf^{-anum/5}; return list of (n, v5(den), target) checks."""
    g = [0] * (NC + 1)
    g[0] = 1
    for k in range(1, NC + 1):
        for j in range(NC, k - 1, -1):
            g[j] -= g[j - k]
    s = Fraction(-anum, 5)
    f = [Fraction(0)] * (NC + 1)
    f[0] = Fraction(1)
    for n in range(1, NC + 1):
        acc = Fraction(0)
        for k2 in range(1, n + 1):
            if g[k2]:
                acc += ((s + 1) * k2 - n) * g[k2] * f[n - k2]
        f[n] = acc / n
    ok = True
    rows = []
    for n in range(1, NC + 1):
        got = v5_int(f[n].denominator)
        want = n + v5_fact(n)
        rows.append((n, got, want))
        if got != want:
            ok = False
    return ok, rows


print()
print("STEP 12 — hearing carriers (q;q)_inf^{-2/5}, (q;q)_inf^{-3/5}:")
for anum in (2, 3):
    ok, rows = carrier_law(anum)
    sample = [rows[0], rows[9], rows[19], rows[39], rows[NC - 1]]
    for (n, got, want) in sample:
        print(f"    a={anum}: n={n:3d}  v5(den c_n) = {got:3d}"
              f"   n + v5(n!) = {want:3d}")
    check(f"carrier (q;q)_inf^{{-{anum}/5}}: v5(den c_n) = n + v5(n!) "
          f"for all n <= {NC}", ok)

# ----------------------------------------------------------------------------
# Verdict
# ----------------------------------------------------------------------------
print()
print("=" * 78)
obj_v5 = 0
car_v5_at_K = K + v5_fact(K)
print("KIND-MISMATCH, recomputed (not cited):")
print(f"  OBJECT side  (figure-eight symmetrised Habiro series, (q-1)-adic):")
print(f"    v5(denominator) = 0 at EVERY order n <= {K}; denominators are")
print(f"    pure powers of 3 (e_n = {e3_list[-1]} at n = {K}).")
print(f"  HEARING side ({{2/5,3/5}} stream carriers):")
print(f"    v5(denominator of c_n) = n + v5(n!) exactly (checked to n = {NC});")
print(f"    at n = {K} that is {car_v5_at_K}; it grows without bound.")
print(f"  A generator derived from the object carries no 5-adic denominators;")
print(f"  the hearing streams require them at every depth. The banked")
print(f"  KILLED-AT-SUPPORT kind-mismatch is upheld.")
print()
if FAILURES:
    print(f"OVERALL: {len(FAILURES)} CHECK(S) FAILED:")
    for f_ in FAILURES:
        print(f"  - {f_}")
    print("VERDICT SIGNAL: NOT-RECONFIRMED (see failures)")
else:
    print("OVERALL: ALL CHECKS PASS")
    print("VERDICT SIGNAL: RECONFIRMED")
print("=" * 78)
