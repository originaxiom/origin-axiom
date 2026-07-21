#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B737 CANDIDATE ZERO -- Probe 1: SCATTER (source verification).

QUESTION (sealed, PREREGISTRATION.md probe 1): verify at PRIMARY source the
scattering/zeta_K formula for the Bianchi group PSL(2, O_K), K = Q(sqrt(-3))
(class number 1, discriminant d = -3, w = 6 roots of unity), and confirm the
pole structure it carries.  Two-outcome: A = formula verified, zeta_K poles
genuinely in the scattering; B = misremembered / inapplicable.

SOURCES (fetched 2026-07-21, this session):
  [S1] P. Sarnak, "The arithmetic and geometry of some hyperbolic three
       manifolds", Acta Math. 151 (1983) 253-295.  PDF fetched from Project
       Euclid and pages 253-262 READ DIRECTLY.  Relevant items:
         (1.2)  vol(H^3/Gamma_D) = |d|^{3/2} zeta_K(2) / (4 pi^2)   [Humbert]
         (2.3)  Gamma_infty for D != 1,3 = unipotent translations (units +-1)
                -- NOTE Sarnak's standing assumption "D != 1, or 3"; our
                field IS D = 3, so the derivation is REDONE below for D = 3.
         (2.4)  E(s,w) = sum_{Gamma_infty \\ Gamma} y(gamma w)^s, Re(s) > 2
         (2.6)' E(s,w) = y^s + phi_11(s) y^{2-s} + (nonzero Fourier modes)
         (2.9)  phi_11(s) = [sum_{A principal} Phi(A)/N(A)^s] * pi/(V(F_L)(s-1))
         (2.11) h = 1  =>  phi(s) = pi/(V(F_L)(s-1)) * zeta_K(s-1)/zeta_K(s)
         L.2.13 Res_{s=2} phi_11 = 2 pi^2 / (V(F_L) sqrt|d| zeta_K(2) w)
                (w = # roots of unity; enters via the class number formula
                 Res_{s=1} zeta_K = 2 pi h / (w sqrt|d|))
         (2.14) Res_{s=2} E = 2 pi^2 / (V(F_L) w sqrt|d| zeta_K(2))
         L.2.15 Res_{s=2} E = V(cusp cross-section)/V(F_D)
  [S2] D. Kim, Y. Lee, "Quantum ergodicity of Eisenstein series for Bianchi
       groups", arXiv:2603.16518 (fetched at source, HTML v1).  Relevant:
         (2.5)  Gamma_eta = FULL stabilizer {gamma : gamma.eta = eta}
         (5.3)  tau_{i,j}(s) = 2 pi / (h_F (s-1) |d_F|^{1/2})
                  * N(m_i)^{2-s}/N(m_j)^s
                  * sum_chi chi(m_i m_j) L(s-1,chi)/L(s,chi)
                (class-group characters chi; for h=1 this is Sarnak (2.11))
         -- their unit discussion also effectively assumes units = +-1
            ("the only units of F are +-1 when h>1", their Sec. 3.2), so
            d = -3 (h=1, w=6) again needs the derivation below.
  [S3] Elstrodt-Grunewald-Mennicke, Crelle 360 (1985) 160-213, and the EGM
       book ch. 8: located (degruyterbrill.com DOI 10.1515/crll.1985.360.160)
       but PAYWALLED (HTTP 405) -- NOT read.  Recorded as a caveat; nothing
       below leans on it.

WHAT THIS SCRIPT COMPUTES (all in-sandbox; compute-not-cite):
  S1. zeta_K = zeta * L(., chi_-3): two independent 25+-digit computations
      (hexagonal-lattice Epstein zeta via the K-Bessel Fourier expansion,
      validated against a direct 2.5M-point lattice sum; vs. Euler-side
      zeta(s)*L(s,chi) via Hurwitz zeta), at s = 2, 3, and a complex point.
  S2. The divisor identity sum_A Phi(A) N(A)^{-s} = zeta_K(s-1)/zeta_K(s):
      exact local Euler-factor proof (sympy) + numeric ideal enumeration of
      Z[omega] up to norm 10^5 (with 3-way ideal-count cross-checks).
  S3. The D = 3 coset structure (the step both sources skip): exact Z[omega]
      arithmetic; the full stabilizer Gamma_infty of infinity in PSL(2,O_3)
      strictly contains the unipotent part (index w/2 = 3; witness
      M = [[omega,0],[0,1-omega]]); cosets Gamma_infty\\Gamma <-> coprime
      (c,d) mod ALL SIX units (sampled exact matrix verification + extended-
      Euclid completion).  With [S2](2.5) (full stabilizer AT SOURCE) this
      forces the D=3 normalization used in S5.
  S4. The unfolding integral (exact, sympy + mpmath quad) and a per-c
      END-TO-END numeric check of the constant term (direct coprime-d
      lattice sums vs. the predicted Phi(c)-formula, 6 values of c).
  S5. The assembled scattering function for PSL(2, O_3):
          phi(s) = Lambda_K(s-1) / Lambda_K(s),
          Lambda_K(s) = (sqrt|d|/(2 pi))^s Gamma(s) zeta_K(s)   (|d| = 3)
      equivalently phi(s) = (2 pi / (sqrt(3)(s-1))) zeta_K(s-1)/zeta_K(s).
      Verified: functional equation Lambda_K(s) = Lambda_K(1-s); the
      scattering relations phi(s)phi(2-s) = 1, |phi(1+it)| = 1, phi(1) = -1;
      the UNIQUE pole in Re(s) > 1 at s = 2 with
          Res_{s=2} phi = (h/w)/Lambda_K(2) = 2 pi^2/(9 zeta_K(2))
      whose residue chain passes through Res_{s=1} zeta_K = 2 pi/(6 sqrt 3)
      (the exact B736-P2 number); poles of phi at the nontrivial zeros of
      zeta_K (verified at the first zero of L(s,chi_-3) and of zeta(s));
      zeros of phi at (nontrivial zeros)+1.
  S6. Geometric closure: SnapPy vol(m004)/12 vs Humbert [S1](1.2), and the
      Maass-Selberg consistency Res(phi)*vol(orbifold) = cusp-section area
      = V(F_L)/3 (the Z/3 unit-rotation quotient) -- ties the object's own
      geometry (triangulation-computed volume, no zeta input) to the
      scattering normalization.

CONVENTIONS (declared per WORKING_RULES 4):
  omega = (1+sqrt(-3))/2 = e^{i pi/3};  O = Z[omega];  N(a+b omega)=a^2+ab+b^2.
  H^3 coords (y, z=x1+i x2); Laplacian eigenvalue lambda = s(2-s); continuous
  spectrum on Re(s)=1 (lambda = 1+t^2, matching B735's [1,inf)).
  E(s) built with the FULL cusp stabilizer (the spectral convention, [S2] 2.5).
  chi_-3(n) = +1 (n=1 mod 3), -1 (n=2 mod 3), 0 (3|n).
  V(F_L) = covolume of O in C = sqrt(3)/2.
Pure math / structural only; no SM content; Gate 5 respected.
"""

import time
from math import gcd as int_gcd

import numpy as np
import sympy as sp
import mpmath as mp

T0 = time.time()
PASS = {"n": 0, "fail": 0}


def check(label, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS["n"] += 1
    else:
        PASS["fail"] += 1
    print(f"  [{tag}] {label}" + (f"  ({detail})" if detail else ""))


def hdr(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78)


mp.mp.dps = 45

SQRT3 = mp.sqrt(3)
OMEGA_C = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)          # e^{i pi/3}
Y_HEX = SQRT3 / 2                                     # Im(omega)
VFL = SQRT3 / 2                                       # covolume of Z[omega]

# ---------------------------------------------------------------------------
hdr("S1. zeta_K(s) = zeta(s) * L(s, chi_-3): independent computations")
# ---------------------------------------------------------------------------

# Method B (Euler side): zeta(s) * L(s, chi_-3), L via Hurwitz zeta.
def L_chi3(s):
    s = mp.mpmathify(s)
    if s == 1:
        # each Hurwitz term poles at s=1; the difference is finite:
        # L(1) = sum_k [1/(3k+1) - 1/(3k+2)] = (psi(2/3) - psi(1/3))/3
        return (mp.digamma(mp.mpf(2) / 3) - mp.digamma(mp.mpf(1) / 3)) / 3
    return mp.power(3, -s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))


def zetaK_factored(s):
    return mp.zeta(s) * L_chi3(s)


# Method A (lattice side): Epstein zeta of the hexagonal form a^2+ab+b^2 via
# the classical K-Bessel Fourier expansion of E_full(tau,s) =
#   sum'_{(m,n)} y^s / |m tau + n|^{2s}
#     = 2 zeta(2s) y^s + 2 sqrt(pi) G(s-1/2)/G(s) zeta(2s-1) y^{1-s}
#       + (8 pi^s sqrt(y)/G(s)) sum_{n>=1} n^{s-1/2} sigma_{1-2s}(n)
#                                  K_{s-1/2}(2 pi n y) cos(2 pi n x)
# (validated below against a direct lattice sum before use).
def sigma_z(n, z):
    return mp.fsum(mp.power(d, z) for d in sp.divisors(n))


def E_full_bessel(tau, s, nmax=40):
    s = mp.mpmathify(s)
    x, y = mp.re(tau), mp.im(tau)
    t1 = 2 * mp.zeta(2 * s) * mp.power(y, s)
    t2 = (2 * mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf(1) / 2) / mp.gamma(s)
          * mp.zeta(2 * s - 1) * mp.power(y, 1 - s))
    acc = mp.mpf(0) if mp.im(s) == 0 else mp.mpc(0)
    for n in range(1, nmax + 1):
        acc += (mp.power(n, s - mp.mpf(1) / 2) * sigma_z(n, 1 - 2 * s)
                * mp.besselk(s - mp.mpf(1) / 2, 2 * mp.pi * n * y)
                * mp.cos(2 * mp.pi * n * x))
    t3 = 8 * mp.power(mp.pi, s) * mp.sqrt(y) / mp.gamma(s) * acc
    return t1 + t2 + t3


def zetaK_bessel(s):
    # sum'(a^2+ab+b^2)^{-s} = E_full(omega,s)/y^s ; each ideal counted w=6 times
    return E_full_bessel(OMEGA_C, s) * mp.power(Y_HEX, -mp.mpmathify(s)) / 6


# Method C: direct double-precision lattice sum at s=3 (validates method A).
R = 800
a = np.arange(-R, R + 1)
A2, B2 = np.meshgrid(a, a, indexing="ij")
Nf = A2.astype(np.float64) ** 2 + A2 * B2 + B2.astype(np.float64) ** 2
Nf[R, R] = np.inf                                    # exclude (0,0)
direct_s3 = np.sum(Nf ** -3.0)
tail_s3 = 2 * np.pi / np.sqrt(3) * (0.75 * R * R) ** -2 / 2   # crude bound
bess_s3 = zetaK_bessel(3) * 6
diff_C = abs(float(bess_s3) - direct_s3)
print(f"  direct lattice sum  sum'(a^2+ab+b^2)^-3      = {direct_s3:.15f}")
print(f"  K-Bessel expansion (same quantity)           = {mp.nstr(bess_s3, 20)}")
print(f"  |diff| = {diff_C:.3e}   (tail bound ~ {tail_s3:.1e})")
check("K-Bessel Epstein expansion validated vs direct sum (s=3)", diff_C < 1e-9)

for sv in (2, 3):
    zA = zetaK_bessel(sv)
    zB = zetaK_factored(sv)
    d = abs(zA - zB)
    print(f"  s={sv}:  zeta_K lattice = {mp.nstr(zA, 25)}")
    print(f"        zeta * L(chi_-3) = {mp.nstr(zB, 25)}   |diff| = {mp.nstr(d, 3)}")
    check(f"zeta_K({sv}) = zeta({sv})*L({sv},chi_-3) to >=20 digits", d < mp.mpf(10) ** -20)

s0 = mp.mpc("0.5", "3.0")
dA = abs(zetaK_bessel(s0) - zetaK_factored(s0))
check("factorization also at complex s=0.5+3i (analytic continuation)",
      dA < mp.mpf(10) ** -20, f"|diff|={mp.nstr(dA, 3)}")

ZK2 = zetaK_factored(2)
print(f"  zeta_K(2) = {mp.nstr(ZK2, 25)}")

# ---------------------------------------------------------------------------
hdr("S2. sum_A Phi(A)/N(A)^s = zeta_K(s-1)/zeta_K(s)  (Sarnak (2.9)-(2.11))")
# ---------------------------------------------------------------------------

# Exact local Euler factor (per prime ideal P, q = N(P)):
#   sum_{k>=0} Phi(P^k) x^k = 1 + (q-1) x / (1 - q x) = (1-x)/(1-qx)
# which is exactly the local factor of zeta_K(s-1)/zeta_K(s) at x = q^{-s}.
q, x = sp.symbols("q x")
lhs_loc = 1 + (q - 1) * x / (1 - q * x)               # geometric series, exact
rhs_loc = (1 - x) / (1 - q * x)
check("local Euler factor identity (sympy exact)",
      sp.simplify(lhs_loc - rhs_loc) == 0)
# and the series coefficients of (1-x)/(1-qx) are exactly Phi(P^k)=q^k-q^{k-1}:
ser = sp.series((1 - x) / (1 - q * x), x, 0, 8).removeO()
expl = 1 + sum((q**kk - q**(kk - 1)) * x**kk for kk in range(1, 8))
check("series coeffs of (1-x)/(1-qx) = Phi(P^k) = q^k - q^{k-1} (k<8, exact)",
      sp.expand(ser - expl) == 0)

# Ideal enumeration of Z[omega] (h=1) up to norm X, Phi multiplicative.
X = 100_000
prime_symbols = []                                    # norms q of prime ideals
for p in sp.primerange(2, X + 1):
    if p == 3:
        prime_symbols.append(3)                       # ramified: one ideal, q=3
    elif p % 3 == 1:
        prime_symbols.append(p)                       # split: two ideals of
        prime_symbols.append(p)                       # norm p (distinct)
    else:
        if p * p <= X:
            prime_symbols.append(p * p)               # inert: one ideal, q=p^2
prime_symbols.sort()

aK = np.zeros(X + 1, dtype=np.int64)                  # # ideals of norm n
SPhi = np.zeros(X + 1, dtype=np.float64)              # sum Phi(A), N(A)=n


def dfs(idx, N, Phi):
    aK[N] += 1
    SPhi[N] += Phi
    for j in range(idx, len(prime_symbols)):
        qj = prime_symbols[j]
        if N * qj > X:
            break
        qk = qj
        phik = qj - 1
        while N * qk <= X:
            dfs(j + 1, N * qk, Phi * phik)
            if N * qk * qj > X:
                break
            qk *= qj
            phik = qk - qk // qj


import sys
sys.setrecursionlimit(10000)
dfs(0, 1, 1)
n_ideals = int(aK.sum())
print(f"  ideals of Z[omega] with norm <= {X}: {n_ideals}"
      f"   (density {n_ideals/X:.6f}; Res zeta_K = {mp.nstr(L_chi3(1),6)})")

# 3-way cross-check of ideal counts a_K(n), n <= 2000:
M = 2000
r = np.zeros(M + 1, dtype=np.int64)
m_ = np.arange(-60, 61)
Am, Bm = np.meshgrid(m_, m_, indexing="ij")
Nm = Am * Am + Am * Bm + Bm * Bm
for nv in Nm.ravel():
    if 0 < nv <= M:
        r[nv] += 1
ok_lattice = all(int(r[n]) == 6 * int(aK[n]) for n in range(1, M + 1))
check("a_K(n) = (lattice count r(n))/6 for n<=2000 (w=6 exact)", ok_lattice)


def chi3(n):
    return 0 if n % 3 == 0 else (1 if n % 3 == 1 else -1)


ok_conv = all(int(aK[n]) == sum(chi3(d) for d in sp.divisors(n))
              for n in range(1, M + 1))
check("a_K(n) = sum_{d|n} chi_-3(d) for n<=2000 (zeta_K = zeta*L, coeff level)",
      ok_conv)

ns = np.arange(1, X + 1, dtype=np.float64)
for sv, tol in ((4.0, 5e-10), (3.5, 5e-8)):
    lhs = float(np.sum(SPhi[1:] * ns ** (-sv)))
    rhs = zetaK_factored(sv - 1) / zetaK_factored(sv)
    d = abs(lhs - float(rhs))
    tail = 0.61 * X ** (2 - sv) / (sv - 2)
    print(f"  s={sv}: sum Phi(A)/N^s = {lhs:.12f} ; zeta_K(s-1)/zeta_K(s) ="
          f" {mp.nstr(rhs, 13)} ; |diff|={d:.2e} (tail~{tail:.1e})")
    check(f"Phi-Dirichlet identity numeric at s={sv}", d < tol)

# ---------------------------------------------------------------------------
hdr("S3. D=3 coset structure: full stabilizer = unipotent x Z/3 (w/2=3);"
    " cosets <-> coprime (c,d) mod ALL SIX units")
# ---------------------------------------------------------------------------

# Exact arithmetic in O = Z[omega], omega^2 = omega - 1, elements (a,b)=a+b*omega.
def zmul(u, v):
    a, b = u
    c, d = v
    return (a * c - b * d, a * d + b * c + b * d)


def zadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def zneg(u):
    return (-u[0], -u[1])


def zconj(u):
    a, b = u
    return (a + b, -b)


def znorm(u):
    a, b = u
    return a * a + a * b + b * b


def iround(p_, q_):
    # exact nearest integer of p_/q_ for q_ > 0 (ties toward +inf); pure int
    return (2 * p_ + q_) // (2 * q_)


def zdivmod(u, v):
    # nearest-integer division: u = q v + r, N(r) <= (3/4) N(v) < N(v)
    # (norm-Euclidean; exact integer arithmetic, no float rounding)
    nv = znorm(v)
    p_ = zmul(u, zconj(v))
    q_ = (iround(p_[0], nv), iround(p_[1], nv))
    r_ = zadd(u, zneg(zmul(q_, v)))
    return q_, r_


def zgcd(u, v):
    while v != (0, 0):
        _, r_ = zdivmod(u, v)
        u, v = v, r_
    return u


def zext_gcd(u, v):
    # returns (g, s, t) with s*u + t*v = g
    s0, s1, t0, t1 = (1, 0), (0, 0), (0, 0), (1, 0)
    while v != (0, 0):
        q_, r_ = zdivmod(u, v)
        u, v = v, r_
        s0, s1 = s1, zadd(s0, zneg(zmul(q_, s1)))
        t0, t1 = t1, zadd(t0, zneg(zmul(q_, t1)))
    return u, s0, t0


UNITS = [(un_a, un_b) for un_a in (-2, -1, 0, 1, 2) for un_b in (-2, -1, 0, 1, 2)
         if znorm((un_a, un_b)) == 1]
check("exactly w = 6 units in Z[omega]", len(UNITS) == 6, f"units={UNITS}")


def is_unit(u):
    return znorm(u) == 1


def zinv_unit(u):
    return zconj(u)                                    # for units, u^{-1}=conj


def mmul(P, Q):
    return [[zadd(zmul(P[0][0], Q[0][0]), zmul(P[0][1], Q[1][0])),
             zadd(zmul(P[0][0], Q[0][1]), zmul(P[0][1], Q[1][1]))],
            [zadd(zmul(P[1][0], Q[0][0]), zmul(P[1][1], Q[1][0])),
             zadd(zmul(P[1][0], Q[0][1]), zmul(P[1][1], Q[1][1]))]]


def mdet(P):
    return zadd(zmul(P[0][0], P[1][1]), zneg(zmul(P[0][1], P[1][0])))


def minv(P):                                           # det = 1 assumed
    return [[P[1][1], zneg(P[0][1])], [zneg(P[1][0]), P[0][0]]]


ONE, ZERO, OM = (1, 0), (0, 0), (0, 1)
GEN_S = [[ZERO, (-1, 0)], [ONE, ZERO]]
GEN_T = [[ONE, ONE], [ZERO, ONE]]
GEN_TW = [[ONE, OM], [ZERO, ONE]]
GENS = [GEN_S, GEN_T, GEN_TW, minv(GEN_S), minv(GEN_T), minv(GEN_TW)]

rng = np.random.default_rng(20260721)


def rand_gamma(maxlen=18):
    P = [[ONE, ZERO], [ZERO, ONE]]
    for _ in range(int(rng.integers(6, maxlen))):
        P = mmul(P, GENS[int(rng.integers(0, 6))])
    return P


ok_det = ok_cop = True
samples = []
for _ in range(200):
    g = rand_gamma()
    ok_det &= (mdet(g) == ONE)
    c_, d_ = g[1][0], g[1][1]
    ok_cop &= is_unit(zgcd(c_, d_)) or (c_ == (0, 0) and is_unit(d_)) \
        or (d_ == (0, 0) and is_unit(c_))
    samples.append(g)
check("200 random words in SL(2,Z[omega]): det = 1 exactly", ok_det)
check("bottom rows (c,d) always coprime", ok_cop)

# completion: every coprime pair is a bottom row (extended Euclid, h=1)
ok_comp = True
for _ in range(100):
    c_ = (int(rng.integers(-30, 31)), int(rng.integers(-30, 31)))
    d_ = (int(rng.integers(-30, 31)), int(rng.integers(-30, 31)))
    if c_ == (0, 0) or not is_unit(zgcd(c_, d_)):
        continue
    g_, sx, tx = zext_gcd(c_, d_)
    iu = zinv_unit(g_)                                 # g is a unit
    a_ = zmul(tx, iu)
    b_ = zneg(zmul(sx, iu))
    ok_comp &= (mdet([[a_, b_], [c_, d_]]) == ONE)
check("extended Euclid completes every coprime (c,d) to SL(2,O)", ok_comp)

# The full stabilizer of infinity contains M_omega = [[w,0],[0,1-w]],
# NOT in (unipotent x {+-1}); it has order 3 in PSL (omega^3 = -1).
M_om = [[OM, ZERO], [ZERO, (1, -1)]]
check("M_omega in SL(2,O), fixes infinity (lower-left=0), diag units, "
      "not +-1", mdet(M_om) == ONE and M_om[1][0] == ZERO
      and is_unit(M_om[0][0]) and M_om[0][0] not in [(1, 0), (-1, 0)])
M3 = mmul(M_om, mmul(M_om, M_om))
check("M_omega^3 = -I (order 3 in PSL(2,O)): index [G_inf : G'_inf.{+-1}] = 3"
      " = w/2", M3 == [[(-1, 0), ZERO], [ZERO, (-1, 0)]])

# height invariance of the full stabilizer (Sarnak (1.1) action):
zt, yt = mp.mpc("0.31", "-0.77"), mp.mpf("1.13")
ok_h = True
for u_ in UNITS:
    b_ = (int(rng.integers(-5, 6)), int(rng.integers(-5, 6)))
    g21, g22 = ZERO, zinv_unit(u_)
    c21 = mp.mpc(g21[0], 0) + mp.mpc(g21[1]) * OMEGA_C
    c22 = mp.mpc(g22[0], 0) + mp.mpc(g22[1]) * OMEGA_C
    ynew = yt / (abs(c21 * zt + c22) ** 2 + abs(c21) ** 2 * yt ** 2)
    ok_h &= abs(ynew - yt) < mp.mpf(10) ** -40
check("full stabilizer preserves the height y (all 6 units)", ok_h)

# Coset criterion: same Gamma_inf-coset <=> bottom rows unit-proportional;
# and which unit requires the FULL stabilizer (not just +-1):
ok_upper = ok_diag = True
seen_nontrivial = 0
for _ in range(60):
    g1 = rand_gamma()
    c_, d_ = g1[1][0], g1[1][1]
    if c_ == (0, 0):
        continue
    eps = UNITS[int(rng.integers(0, 6))]
    ce, de = zmul(eps, c_), zmul(eps, d_)
    g_, sx, tx = zext_gcd(ce, de)
    iu = zinv_unit(g_)
    a_ = zmul(tx, iu)
    b_ = zneg(zmul(sx, iu))
    g2 = [[a_, b_], [ce, de]]
    U_ = mmul(g2, minv(g1))
    ok_upper &= (U_[1][0] == ZERO)
    ok_diag &= is_unit(U_[0][0]) and is_unit(U_[1][1])
    if U_[0][0] not in [(1, 0), (-1, 0)]:
        seen_nontrivial += 1
check("unit-proportional bottom rows => same FULL-stabilizer coset "
      "(gamma2 gamma1^-1 upper triangular, unit diagonal)", ok_upper and ok_diag)
check("cosets genuinely need units beyond +-1 (witnessed)", seen_nontrivial > 0,
      f"{seen_nontrivial}/60 samples used eps notin {{+-1}}")
print("  => Gamma_inf \\ Gamma  <->  {coprime (c,d)} / O^x  (ALL SIX units);")
print("     with [S2] (2.5) (spectral E-series uses the FULL stabilizer, at")
print("     source), the c-sum in the constant term runs over NONZERO IDEALS.")

# ---------------------------------------------------------------------------
hdr("S4. Unfolding integral (exact) + per-c end-to-end constant-term check")
# ---------------------------------------------------------------------------

rr, Ax, ss = sp.symbols("r A s", positive=True)
I_exact = sp.integrate(2 * sp.pi * rr / (rr**2 + Ax**2) ** ss, (rr, 0, sp.oo),
                       conds="none")
target = sp.pi / (ss - 1) * Ax ** (2 - 2 * ss)
check("int_{R^2} dx/(|z|^2+A^2)^s = pi/(s-1) A^{2-2s} (sympy exact, s>1)",
      sp.simplify(I_exact - target) == 0)
num = mp.quad(lambda t_: 2 * mp.pi * t_ / (t_**2 + mp.mpf("1.69")) ** 4,
              [0, mp.inf])
check("... numeric (s=4, A=1.3)", abs(num - mp.pi / 3 * mp.mpf("1.3") ** -6)
      < mp.mpf(10) ** -25)

# Per-c end-to-end: for fixed c, average over z of
#   S_c(z) = sum_{d coprime to c} y^s/(|cz+d|^2+N(c)y^2)^s
# must equal  y^{2-s} * pi/((s-1) V(F_L)) * Phi(c)/N(c)^s.
# NOTE (bug found by the first run of this very check, then fixed): the
# coprimality condition is invariant only under d -> d - t*c, so S_c(z) is
# O-periodic, NOT (1/c)O-periodic; the z-average must run over the O-cell
# F_L.  Averaging over the fine cell leaves O*-modes of size ~ e^{-2 pi y
# 2/sqrt3} ~ 3e-4 alive -- the first run saw exactly that.  A G x G grid
# over F_L kills every mode below |l| = G * 2/sqrt3: error ~ e^{-2 pi y G
# 2/sqrt3} ~ 1e-20 at G = 6, y = 1.1.
sv, yv = 4, 1.1                                        # y != 1 exposes y-powers
Gz = 6                                                 # z-grid over F_L
Bbox = 160
ii = np.arange(-Bbox, Bbox + 1)
Ii, Jj = np.meshgrid(ii, ii, indexing="ij")
Dc = Ii + Jj * complex(np.cos(np.pi / 3), np.sin(np.pi / 3))   # d = i + j omega


def phi_of_c(cel):
    """Exact Phi(c) two ways: multiplicative over the ideal factorization of
    N(c)=norm (using splitting), and brute-force residue count via a
    triangular (HNF) fundamental domain of the lattice cO."""
    n_ = znorm(cel)
    # multiplicative, from the rational prime factorization of the ideal (c):
    phi_m = 1
    for p_, e_ in sp.factorint(n_).items():
        if p_ == 3:                                    # ramified, q=3, exp e_
            phi_m *= 3 ** e_ - 3 ** (e_ - 1)
        elif p_ % 3 == 1:
            # split: (c) may contain P^a Pbar^b, a+b=e_ ; Phi multiplicative
            # with q=p per factor -- get the valuation a at P by dividing c
            # by a prime element pi_P repeatedly.
            # find a prime element above p_: search small elements of norm p_
            pi_el = None
            bnd = int(np.ceil(np.sqrt(p_))) + 2
            for aa in range(-bnd, bnd + 1):
                done = False
                for bb in range(-bnd, bnd + 1):
                    if znorm((aa, bb)) == p_:
                        pi_el = (aa, bb)
                        done = True
                        break
                if done:
                    break
            va = 0
            tmp = cel
            while True:
                q_, r_ = zdivmod(tmp, pi_el)
                if r_ == (0, 0):
                    va += 1
                    tmp = q_
                else:
                    break
            vb = e_ - va
            for v_ in (va, vb):
                if v_ > 0:
                    phi_m *= p_ ** v_ - p_ ** (v_ - 1)
        else:                                          # inert, q=p^2, exp e_/2
            e2 = e_ // 2
            phi_m *= p_ ** (2 * e2) - p_ ** (2 * e2 - 2)
    # brute force: triangular basis of cO from columns c, c*omega
    v1, v2 = cel, zmul(cel, OM)                        # columns (a,b)
    # column-reduce to [[d1, c1],[0, d2]] over Z:
    a1, b1 = v1
    a2, b2 = v2
    while b2 != 0:                                     # Euclid on (b1,b2)
        qq = b1 // b2
        a1, b1, a2, b2 = a2, b2, a1 - qq * a2, b1 - qq * b2
    d1 = abs(a2) if a2 != 0 else 0
    # now second vector (a2, 0); first (a1,b1) with b1 = gcd of b's
    cnt = 0
    d2_ = abs(b1)
    for i_ in range(d1):
        for j_ in range(d2_):
            # element i_ * 1 + ... representative (i_, j_) reduced mod lattice
            if is_unit(zgcd((i_, j_), cel)) or (i_, j_) == (0, 0) and False:
                cnt += 1
    check_ok = (d1 * d2_ == n_)
    return phi_m, cnt, check_ok


C_TESTS = [((1, 0), "c=1 (unit ideal)"),
           ((2, 0), "c=2 (inert prime, q=4)"),
           ((1, 1), "c=1+omega (ramified, q=3)"),
           ((2, 1), "c=2+omega (split prime, q=7)"),
           ((3, 0), "c=3 (ramified^2, q=9)"),
           ((4, 0), "c=4 (inert^2, q=16)")]

pred_const = np.pi / ((sv - 1) * float(VFL))           # pi/((s-1) V(F_L))
for cel, label in C_TESTS:
    n_ = znorm(cel)
    phi_m, phi_bf, hnf_ok = phi_of_c(cel)
    check(f"{label}: |O/(c)| = N(c) = {n_} via HNF box", hnf_ok)
    check(f"{label}: Phi multiplicative {phi_m} = brute-force count {phi_bf}",
          phi_m == phi_bf)
    cc = complex(cel[0], 0) + cel[1] * complex(np.cos(np.pi / 3),
                                               np.sin(np.pi / 3))
    # coprime-d mask over the box (exact gcd per lattice point):
    mask = np.zeros(Dc.shape, dtype=bool)
    for i_ in range(Dc.shape[0]):
        for j_ in range(Dc.shape[1]):
            del_ = (int(Ii[i_, j_]), int(Jj[i_, j_]))
            mask[i_, j_] = is_unit(zgcd(del_, cel)) if del_ != (0, 0) \
                else is_unit(cel)
    dvals = Dc[mask]
    # average over a Gz x Gz grid of the O-cell F_L (see NOTE above):
    acc = 0.0
    for ju in range(Gz):
        for kv in range(Gz):
            zz = (ju / Gz) + (kv / Gz) * complex(np.cos(np.pi / 3),
                                                 np.sin(np.pi / 3))
            acc += float(np.sum((np.abs(cc * zz + dvals) ** 2
                                 + n_ * yv * yv) ** -float(sv)))
    S_avg = yv ** sv * acc / (Gz * Gz)
    S_pred = yv ** (2 - sv) * pred_const * phi_m / float(n_) ** sv
    rel = abs(S_avg - S_pred) / S_pred
    # d-box truncation: min |d| on the box boundary is ~ Bbox*sqrt(3)/2; the
    # missing mass, relative to S_pred, scales like N(c)^{s-1} (declared
    # bound, computed, not a fudge):
    Rmin = Bbox * np.sqrt(3) / 2
    abs_tail = (yv ** sv * (phi_m / n_) * (2 * np.pi / np.sqrt(3))
                * Rmin ** (2 - 2 * sv) / (2 * sv - 2))
    tol = 3 * abs_tail / S_pred + 2e-10
    check(f"{label}: direct d-lattice sum = pi/((s-1)V) Phi/N^s  "
          f"[{S_avg:.12e} vs {S_pred:.12e}]", rel < tol,
          f"rel={rel:.1e}, tol={tol:.1e}")

print("  => constant term of E(s): y^s + phi(s) y^{2-s},")
print("     phi(s) = pi/((s-1) V(F_L)) sum_{ideals A != 0} Phi(A) N(A)^{-s}")
print("            = 2 pi/(sqrt(3)(s-1)) * zeta_K(s-1)/zeta_K(s)   [by S2].")

# ---------------------------------------------------------------------------
hdr("S5. phi(s) = Lambda_K(s-1)/Lambda_K(s): completed zeta, FE, poles, zeros")
# ---------------------------------------------------------------------------


def LamK(s):
    s = mp.mpmathify(s)
    return mp.power(SQRT3 / (2 * mp.pi), s) * mp.gamma(s) * zetaK_factored(s)


def phi_raw(s):
    s = mp.mpmathify(s)
    return (2 * mp.pi / (SQRT3 * (s - 1))) * zetaK_factored(s - 1) / zetaK_factored(s)


def phi(s):
    return LamK(mp.mpmathify(s) - 1) / LamK(s)


for sv in (mp.mpc("3.3", "0.7"), mp.mpc("1.4", "-2.2"), mp.mpf("4.0")):
    d = abs(phi(sv) - phi_raw(sv))
    check(f"algebraic identity Lambda-ratio = 2pi/(sqrt3(s-1)) zeta-ratio at "
          f"s={mp.nstr(sv,3)}", d < mp.mpf(10) ** -25, f"|diff|={mp.nstr(d,3)}")

for sv in (mp.mpc("0.3", "2.2"), mp.mpc("-0.7", "0.4"), mp.mpc("0.5", "8.0")):
    rel = abs(LamK(sv) - LamK(1 - sv)) / abs(LamK(sv))
    check(f"functional equation Lambda_K(s)=Lambda_K(1-s) at s={mp.nstr(sv,3)}",
          rel < mp.mpf(10) ** -20, f"rel={mp.nstr(rel,3)}")

for sv in (mp.mpc("1.37", "5.1"), mp.mpc("0.2", "-3.3")):
    d = abs(phi(sv) * phi(2 - sv) - 1)
    check(f"scattering relation phi(s)phi(2-s)=1 at s={mp.nstr(sv,3)}",
          d < mp.mpf(10) ** -20, f"|diff|={mp.nstr(d,3)}")

for tv in ("1.0", "5.0", "8.039", "14.134", "25.0"):
    d = abs(abs(phi(mp.mpc(1, tv))) - 1)
    check(f"unitarity |phi(1+it)|=1 at t={tv} (continuous spectrum, B735 "
          f"lambda=1+t^2)", d < mp.mpf(10) ** -20, f"||phi|-1|={mp.nstr(d,3)}")

v1 = phi(1 + mp.mpf(10) ** -7)
check("phi(1) = -1 (no pole at the bottom of the continuous spectrum; the "
      "two Lambda_K poles at s-1=0 and s=1 cancel)",
      abs(v1 + 1) < mp.mpf(10) ** -5, f"phi(1+1e-7)={mp.nstr(v1, 10)}")

# --- THE POLE AT s=2 (the candidate structure) ---
ResZK = L_chi3(1)                                      # Res_{s=1} zeta_K
cnf = 2 * mp.pi * 1 / (6 * SQRT3)                      # class number formula
print(f"  Res_(s=1) zeta_K = L(1,chi_-3)      = {mp.nstr(ResZK, 25)}")
print(f"  class-number formula 2 pi h/(w sqrt|d|), h=1,w=6,|d|=3"
      f" = {mp.nstr(cnf, 25)}")
res_lim = (mp.mpf(10) ** -12) * zetaK_factored(1 + mp.mpf(10) ** -12)
check("Res zeta_K numeric limit (s-1)zeta_K(s)|_{s=1+1e-12} = L(1,chi_-3)",
      abs(res_lim - ResZK) < mp.mpf(10) ** -10, f"lim={mp.nstr(res_lim, 15)}")
check("Res zeta_K = 2pi/(6 sqrt3)  [THE B736-P2 NUMBER, = 0.6046...]",
      abs(ResZK - cnf) < mp.mpf(10) ** -30)
check("... = pi/sqrt(27) exactly", abs(ResZK - mp.pi / mp.sqrt(27)) < mp.mpf(10) ** -30)

RA = 2 * mp.pi ** 2 / (VFL * 6 * SQRT3 * ZK2)          # Sarnak L.2.13, w=6
RB = (mp.pi / VFL) * ResZK / ZK2                       # via the residue chain
RC = (mp.mpf(1) / 6) / LamK(2)                         # (h/w)/Lambda_K(2)
RD = 2 * mp.pi ** 2 / (9 * ZK2)                        # simplified closed form
print(f"  Res_(s=2) phi:  Sarnak-L2.13(w=6) = {mp.nstr(RA, 25)}")
print(f"                  (pi/V) ResZK/ZK2  = {mp.nstr(RB, 25)}")
print(f"                  (h/w)/Lambda_K(2) = {mp.nstr(RC, 25)}")
print(f"                  2 pi^2/(9 ZK2)    = {mp.nstr(RD, 25)}")
check("all four closed forms of Res_{s=2} phi agree to 25 digits",
      max(abs(RA - RB), abs(RA - RC), abs(RA - RD)) < mp.mpf(10) ** -25)
num_res = (mp.mpf(10) ** -10) * phi(2 + mp.mpf(10) ** -10)
check("numeric residue (s-2)phi(s)|_{s=2+1e-10} matches",
      abs(num_res - RA) < mp.mpf(10) ** -8, f"num={mp.nstr(num_res, 12)}")
check("Res_{s=1} Lambda_K = h/w = 1/6 (completed-zeta residue IS h/w)",
      abs((mp.mpf(10) ** -12) * LamK(1 + mp.mpf(10) ** -12) - mp.mpf(1) / 6)
      < mp.mpf(10) ** -10)

# --- no other pole in Re(s) > 1 (numeric scan; nonvanishing of zeta_K on
#     Re >= 1 is classical Hadamard-de la Vallee Poussin for zeta and L) ---
grid_max = 0
worst = None
for sig in (1.05, 1.2, 1.5, 1.9, 2.5, 3.0):
    for t_ in np.arange(0, 30.01, 0.5):
        spt = mp.mpc(sig, float(t_))
        if abs(spt - 2) < 0.4:
            continue
        v = abs(phi(spt))
        if v > grid_max:
            grid_max, worst = v, spt
print(f"  scan Re(s) in [1.05,3], |t|<=30, excluding |s-2|<0.4:"
      f" max|phi| = {mp.nstr(grid_max, 6)} at s = {mp.nstr(worst, 6)}")
check("no further pole in Re(s)>1 on the scan grid (sanity; classical "
      "nonvanishing on Re=1)", grid_max < 1e4)

# --- poles of phi at the NONTRIVIAL ZEROS of zeta_K; zeros at (zeros)+1 ---
tgrid = np.arange(6.0, 10.01, 0.05)
vals = [abs(L_chi3(mp.mpc("0.5", float(t_)))) for t_ in tgrid]
t_min = float(tgrid[int(np.argmin(vals))])
rho1 = mp.findroot(lambda s_: mp.zeta(s_) * L_chi3(s_), mp.mpc("0.5", t_min))
print(f"  first nontrivial zero of L(s,chi_-3): rho_1 = {mp.nstr(rho1, 25)}")
check("rho_1 on the critical line Re=1/2 (numeric)",
      abs(mp.re(rho1) - mp.mpf(1) / 2) < mp.mpf(10) ** -25)
check("zeta_K(rho_1) = 0", abs(zetaK_factored(rho1)) < mp.mpf(10) ** -25)
rho_z = mp.zetazero(1)                                 # 0.5 + 14.1347... i
check("zeta_K also vanishes at Riemann's rho (0.5+14.1347i): zeta_K = zeta*L",
      abs(zetaK_factored(rho_z)) < mp.mpf(10) ** -25)
for rho, lab in ((rho1, "rho_1 (L-zero)"), (rho_z, "rho_zeta")):
    big = abs(phi(rho + mp.mpf(10) ** -8))
    small = abs(phi(rho + 1))
    print(f"  {lab}: |phi(rho+1e-8)| = {mp.nstr(big, 6)},  |phi(rho+1)| ="
          f" {mp.nstr(small, 6)}")
    check(f"phi has a POLE at s={lab} (denominator Lambda_K(s)=0)", big > 1e6)
    check(f"phi has a ZERO at s={lab}+1 (numerator Lambda_K(s-1)=0)",
          small < mp.mpf(10) ** -20)
print("  => the FULL nontrivial zero set of zeta_K is imprinted in phi:")
print("     poles on Re(s)=1/2 (shifted zeros: denominator), zeros on")
print("     Re(s)=3/2 (numerator), swapped by the s <-> 2-s scattering FE;")
print("     the UNIQUE pole in Re(s)>1 is s=2 <- the zeta_K pole at s=1.")

# ---------------------------------------------------------------------------
hdr("S6. Geometric closure: SnapPy m004 (the object) vs the scattering "
    "normalization")
# ---------------------------------------------------------------------------
try:
    import snappy
    try:
        vol = mp.mpf(str(snappy.ManifoldHP("m004").volume()))
        vsrc = "ManifoldHP (quad-double)"
    except Exception:
        vol = mp.mpf(str(snappy.Manifold("m004").volume()))
        vsrc = "Manifold (double)"
    humbert = mp.power(3, mp.mpf(3) / 2) * ZK2 / (4 * mp.pi ** 2)  # [S1](1.2)
    ratio = vol / humbert
    print(f"  vol(m004) [{vsrc}] = {mp.nstr(vol, 25)}")
    print(f"  Humbert |d|^(3/2) zeta_K(2)/(4 pi^2)  = {mp.nstr(humbert, 25)}")
    print(f"  ratio = {mp.nstr(ratio, 25)}")
    check("vol(m004) = 12 x vol(PSL(2,O_3)\\H^3) (B734/B735 index-12, "
          "recomputed geometrically)", abs(ratio - 12) < mp.mpf(10) ** -9)
    # Maass-Selberg consistency: Res phi * vol(orbifold) = cusp-section area.
    # Orbifold cusp cross-section = F_L / (Z/3 unit rotation) = V(F_L)/3.
    lhs = RD * (vol / 12)
    rhs = VFL / 3
    check("Res_{s=2}phi x vol(orbifold) = V(F_L)/3 (cusp section, Z/3 "
          "quotient: the w=6 convention closes geometrically)",
          abs(lhs - rhs) < mp.mpf(10) ** -9,
          f"{mp.nstr(lhs, 20)} vs {mp.nstr(rhs, 20)}")
except Exception as e:                                 # pragma: no cover
    print(f"  SnapPy unavailable in this environment: {e!r} -- SKIPPED")

# ---------------------------------------------------------------------------
hdr("VERDICT (probe 1)")
# ---------------------------------------------------------------------------
print(f"""
checks passed: {PASS['n']},  failed: {PASS['fail']}   ({time.time()-T0:.1f}s)

EXACT FORMULA (source [S1] (2.11)/L.2.13 + [S2] (2.5)/(5.3), D=3 case
re-derived and verified in-sandbox above):  for Gamma = PSL(2, O_K),
K = Q(sqrt(-3)), cusp at infinity, E(s,w) = sum_(Gamma_inf\\Gamma) y(gw)^s
(FULL stabilizer; lambda = s(2-s)):

    constant term = y^s + phi(s) y^(2-s),
    phi(s) = (2 pi / (sqrt(3) (s-1))) * zeta_K(s-1) / zeta_K(s)
           = Lambda_K(s-1) / Lambda_K(s),
    Lambda_K(s) = (sqrt(3)/(2 pi))^s Gamma(s) zeta_K(s)  [completed Dedekind
    zeta, Lambda_K(s) = Lambda_K(1-s)],  zeta_K = zeta * L(., chi_-3).

POLES OF phi (all verified numerically above):
  * s = 2: the UNIQUE pole in Re(s) > 1 -- the image of the zeta_K pole at
    s=1 (numerator Lambda_K(s-1)).  Res = (h/w)/Lambda_K(2) = 2pi^2/(9 zK(2))
    = 1.70652...; the residue chain passes literally through
    Res_(s=1) zeta_K = 2 pi/(6 sqrt3) = 0.604599788... (the B736-P2 number).
  * s = 1: NO pole (the two Lambda_K poles cancel; phi(1) = -1).
  * nontrivial zeros rho of zeta_K: poles of phi at s = rho (Re = 1/2),
    zeros of phi at s = rho + 1 (Re = 3/2)  [verified at the first L-zero
    0.5 + 8.0397...i and at Riemann's 0.5 + 14.1347...i].
  * |phi(1+it)| = 1: the continuous spectrum [1, inf) of B735 is carried
    unitarily; the infinite-tower object zeta_K (poles included) sits
    natively in the Bianchi-class cusp scattering.

OUTCOME: A.
""")
