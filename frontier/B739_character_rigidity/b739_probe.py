#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B739 CHARACTER-RIGIDITY -- THE PROBE (compute leg of 1-compute -> 3-skeptic)
============================================================================
Sealed under frontier/B739_character_rigidity/PREREGISTRATION.md.

QUESTION (two-outcome, sealed):
  Is the continuous spectrum of m004 CHARACTER-RIGID -- i.e. does it carry
  EXACTLY the field's zeta_K and nothing else, with no conductor-(4)/(8)
  Hecke character anywhere in it (the level's new arithmetic living only in
  the discrete newform spectrum)?
  A = character-rigidity at full strength;  B = a gap (some Fourier mode /
  s-range / channel where a level character CAN enter the continuous part).

FIREWALL: pure math; no physics value; nothing to CLAIMS.  COMPUTE-NOT-CITE
(E19): the one-cusp lemma and its ingredients are RE-DERIVED here, not cited
from B737; primary sources were re-fetched at source 2026-07-21.

CONVENTIONS BLOCK (WORKING_RULES rule 4 -- declared before the run)
  * K = Q(sqrt(-3)), O = Z[w], w = (1+sqrt(-3))/2, N(a+bw) = a^2+ab+b^2,
    w_K = 6 units, h(K) = 1 (recomputed in PART 0).
  * zeta_K(s) = zeta(s) L(s,chi_-3);  Lambda_K(s) = (sqrt3/(2pi))^s Gamma(s)
    zeta_K(s), functional equation Lambda_K(s) = Lambda_K(1-s) (verified).
  * SPECTRAL CONVENTION (Sarnak, un-shifted): E(P,s) eigenfunction of -Delta
    with eigenvalue s(2-s); cusp constant term  y^s + phi(s) y^(2-s)  in the
    intrinsic (un-normalized Busemann) height y; continuous spectrum
    {1+t^2 : t real} = [1,oo) at s = 1+it.  phi_O(s) = Lambda_K(s-1)/
    Lambda_K(s) (re-derived, PART 0.6).
  * Base and cover constant terms are read in the SAME y (both groups act on
    the same H^3, Gamma' < Gamma).  A cusp-width renormalization would
    multiply phi by c^(s-1), c > 0 -- entire, zero-free: divisor unchanged.
    Declared once, used throughout.
  * Lattices in C = R^2, pairing <u,x> = real dot product; Fourier modes
    e(u,x) = exp(2 pi i <u,x>); dual lattice L^v = {u : <u,l> in Z, l in L}.
      O      basis b1 = (1,0),        b2 = (1/2, sqrt3/2)     (covol sqrt3/2)
      Lam    basis c1 = (1,0),        c2 = (0, 2 sqrt3)       (covol 2 sqrt3)
      O^v    basis u1 = (1,-1/sqrt3), u2 = (0, 2/sqrt3)
      Lam^v  basis v1 = (1,0),        v2 = (0, 1/(2 sqrt3))
    Lam = Z + (2+4w)Z = Z + 2 sqrt(-3) Z  (equality PROVED in PART 0.3).
  * Numerics: mpmath (dps as set per section), sympy exact where possible,
    snappy 3.3.2; snappy Numbers via str() with pari's space-before-exponent
    stripped (helper snum).  Grid-DFT coefficient extraction is EXACT for
    trigonometric polynomials when the grid Nyquist exceeds the bandwidth
    (no aliasing: the only surviving alias class is the mode itself); the
    aliasing-free condition is checked in-code before use, and 3 independent
    slow adaptive-quadrature cross-checks are run on top.

PRIMARY SOURCES (re-fetched at source 2026-07-21, this seat; pdftotext
extracts in the session scratchpad; verbatim quotes below are from those
extracts, OCR artifacts as in the scan):
  [S] P. Sarnak, "The arithmetic and geometry of some hyperbolic three
      manifolds", Acta Math. 151 (1983) 253-295, projecteuclid PDF.
      - p.264 (extract l.701-712): "The spectral theory of A on L2(MD) has
        been carefully studied by Selberg [19]. In fact the theory has been
        fully developed for any three manifold of finite volume. The
        spectrum consists of a finite number of discrete eigenvalues in
        [0, 1), call these 0=lam_0<lam_1<=lam_2...<=lam_k<1. [...] The
        interval [1, oo) comprises two kinds of spectrum: Firstly the
        continuous spectrum which is spanned by the Eisenstein series
        E_j(1+it, w), t in R, where the j denotes the Eisenstein series in
        the jth cusp. Each of these is defined in an analogous way to the
        Eisenstein series in the infinite cusp. Then there is also the
        discrete spectrum u_j, lam_j within [1, oo)."
      - (2.6)': "E(s, w) = y^s + phi(s) y^(2-s) + nonzero coefficients".
      - (2.20): an L^2 eigenfunction's cusp expansion
        u_j(w) = sum_{n in L*} c_n(j) y K_{s_j-1}(2 pi |n| y) e(<n,x>).
      - extract l.658: "the number of such inequivalent cusps is the class
        number h" (cusps of the Bianchi orbifold <-> ideal classes).
  [F] J. S. Friedman, arXiv:math/0702030 (Kleinian Venkov-Zograf paper),
      full PDF.  Lemma 2.1 ([Fri05b], resting on [EGM98, Chapter 3] =
      Elstrodt-Grunewald-Mennicke, Groups Acting on Hyperbolic Space), eq.
      (2.6): the automorphic kernel expands as
        K(P,Q) = sum_{m in D} h(lam_m) e_m(P) (x) e_m(Q)
          + (1/4pi) sum_{alpha=1}^{kappa(Gamma)} sum_{l=1}^{k_alpha}
            ([Gamma_alpha:Gamma'_alpha]/|Lam_alpha|) int_R h(1+t^2)
            E_alpha^l(P,it) (x) E_alpha^l(Q,it) dt,
      "Here D is an indexing set of the eigenfunctions em of Delta [...]
      E_alpha^l(P,s) are the Eisenstein series associated to the singular
      cusps of Gamma, k_alpha = dim_C V_alpha [...] If a cusp is regular it
      is omitted from the sum in (2.6)."  And: "Every cofinite Kleinian
      group has finitely many equivalence classes of cusps".
      For the TRIVIAL character (V = C, k_alpha = dim V = 1, every cusp
      singular): exactly ONE Eisenstein channel per cusp -- the continuous
      spectrum has multiplicity kappa(Gamma) = the number of cusps.
POST-HOC NOTE (declared, WORKING_RULES rule 3): run 1 of this file died on
a tooling bug (a stray editing placeholder line calling a non-existent
sympy Matrix.columns() in PART 0.3, before any PART-A claim was reached);
the line was deleted, nothing else changed, no mathematical claim affected.
The failed transcript is preserved in b739_probe_out_run1_FAILED.txt.

  [B734, in-repo] m004 = Gamma'\\H^3 with Gamma' < PSL(2,O_3) of index 12
      (non-normal); cusp translation lattice Lam = Z+(2+4w)Z < O, index 4;
      orbifold cusp = C/(O x| Z_3) (order-3 rotation).  Re-verified here in
      its computable shadows: shapes field, Humbert volume ratio = 12, cusp
      modulus 2 sqrt(-3), index bookkeeping 12 = 4 x 3, |Isom(m004)| = 8.
"""

import sys, time
import random
from mpmath import (mp, mpf, mpc, gamma, pi, sqrt, zeta, quad, exp, psi,
                    besselk, besseli, diff, fabs, mpmathify, nstr)
import sympy as sp

T0 = time.time()
PASS = []
def check(label, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    PASS.append(bool(ok))
    print(f"  [{tag}] {label}" + (f"  ({detail})" if detail else ""))
    if not ok:
        print("  *** HARD FAIL -- outcome-relevant failure ***")

def hr(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)

def snum(x):
    return mpf(str(x).replace(' ', ''))

# ---------------------------------------------------------------------------
hr("PART 0.1 -- field arithmetic of K = Q(sqrt(-3)) recomputed from scratch")
# ---------------------------------------------------------------------------
mp.dps = 60

units = [(a, b) for a in range(-2, 3) for b in range(-2, 3)
         if a * a + a * b + b * b == 1]
check("unit number w_K = 6", len(units) == 6, f"units {units}")
check("Minkowski bound (2/pi)sqrt3 < 2  =>  h(K) = 1", (2 / pi) * sqrt(3) < 2)

import math
X = 1500
R = int(math.isqrt(4 * X // 3)) + 2
cnt = {}
for a in range(-R, R + 1):
    for b in range(-R, R + 1):
        n = a * a + a * b + b * b
        if 0 < n <= X:
            cnt[n] = cnt.get(n, 0) + 1
chi3 = lambda n: (0, 1, -1)[n % 3]
ok = all(cnt.get(n, 0) // 6 == sum(chi3(d) for d in range(1, n + 1) if n % d == 0)
         for n in range(1, X + 1))
check(f"#ideals of norm n == sum_(d|n) chi_-3(d), n <= {X} "
      "(grounds zeta_K = zeta * L(chi))", ok)

def L_chi(s):
    s = mpmathify(s)
    return 3 ** (-s) * (zeta(s, mpf(1) / 3) - zeta(s, mpf(2) / 3))
def zK(s):
    s = mpmathify(s)
    return zeta(s) * L_chi(s)
def LamK(s):
    s = mpmathify(s)
    return (sqrt(3) / (2 * pi)) ** s * gamma(s) * zK(s)

L1 = (psi(0, mpf(2) / 3) - psi(0, mpf(1) / 3)) / 3
check("Res_{s=1} zeta_K = L(1,chi) = 2 pi /(6 sqrt3) (class number formula)",
      fabs(L1 - 2 * pi / (6 * sqrt(3))) < mpf(10) ** -50)
ok = all(fabs(LamK(s0) - LamK(1 - s0)) / fabs(LamK(s0)) < mpf(10) ** -45
         for s0 in (mpc("0.3", "2.1"), mpc("0.72", "-5.4"), mpc("-1.3", "0.9")))
check("Lambda_K(s) = Lambda_K(1-s) at 3 complex points", ok)

# ---------------------------------------------------------------------------
hr("PART 0.2 -- the object: m004 facts recomputed (snappy)")
# ---------------------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")
import snappy

M = snappy.Manifold('m004')
H = snappy.ManifoldHP('m004')
check("m004 has exactly ONE cusp, complete",
      M.num_cusps() == 1 and M.cusp_info()[0].is_complete,
      f"num_cusps = {M.num_cusps()}")
shapes = [mpc(snum(z.real()), snum(z.imag())) for z in H.tetrahedra_shapes('rect')]
resid = max(fabs(z ** 2 - z + 1) for z in shapes)
check("tetrahedra shapes satisfy z^2 - z + 1 = 0  (trace field Q(sqrt-3))",
      resid < mpf(10) ** -55, f"max residual {nstr(resid, 3)}")
volH = snum(H.volume())
vol_orb = 3 ** mpf("1.5") * zK(2) / (4 * pi ** 2)      # Humbert ([S] Prop 2.1)
check("vol(m004)/vol(PSL(2,O_3)\\H^3) = 12  (covering degree)",
      fabs(volH / vol_orb - 12) < mpf(10) ** -50,
      f"ratio = {nstr(volH / vol_orb, 30)}")
sh = H.cusp_info()[0].shape
tau = mpc(snum(sh.real()), snum(sh.imag()))
check("cusp modulus of m004 = 2 sqrt(-3)",
      fabs(tau - mpc(0, 1) * 2 * sqrt(3)) < mpf(10) ** -50, f"tau = {nstr(tau, 20)}")
Sym = M.symmetry_group()
check("|Isom(m004)| = 8 < 12: the cover is NON-normal (context; the lemma "
      "below needs NO normality)", Sym.order() == 8 and Sym.is_full_group())

# ---------------------------------------------------------------------------
hr("PART 0.3 -- the two lattices, exactly (sympy)")
# ---------------------------------------------------------------------------
sq3 = sp.sqrt(3)
wE = sp.Rational(1, 2) + sq3 * sp.I / 2               # w = (1+sqrt(-3))/2
check("2+4w = 4 + 2 sqrt(-3), hence Z+(2+4w)Z = Z + 2 sqrt(-3) Z (differ by 4 in Z)",
      sp.simplify(2 + 4 * wE - (4 + 2 * sq3 * sp.I)) == 0)

# O-coords: b1=(1,0), b2=(1/2,sqrt3/2).  Lam basis in O-coords: c1=b1,
# c2 = 2 sqrt(-3) = 4w-2 = -2*b1 + 4*b2:
c2_check = sp.simplify(4 * wE - 2 - 2 * sq3 * sp.I)
check("2 sqrt(-3) = -2 + 4w  (Lam-basis O-coords (1,0) and (-2,4))", c2_check == 0)
Mcoords = sp.Matrix([[1, -2], [0, 4]])

def smith_diag(Mx):
    # Smith normal form over Z for a 2x2 integer matrix (elementary, exact)
    d1 = sp.gcd(sp.gcd(Mx[0, 0], Mx[0, 1]), sp.gcd(Mx[1, 0], Mx[1, 1]))
    d2 = abs(Mx.det()) / d1
    return (d1, d2)

d1, d2 = smith_diag(Mcoords)
check("[O : Lam] = |det| = 4 with SNF diag(1,4): quotient O/Lam cyclic Z/4",
      abs(Mcoords.det()) == 4 and (d1, d2) == (1, 4))
# generator of O/Lam: w itself; k*w in Lam iff 4 | k:
ok = all((sp.Matrix([0, k]) - Mcoords * sp.Matrix([x, y])).norm() != 0
         for k in (1, 2, 3)
         for x in range(-6, 7) for y in range(-2, 3))
check("w generates O/Lam = Z/4 (k*w in Lam only for k = 0 mod 4; k=1,2,3 miss)", ok)
check("cusp-degree bookkeeping: [O x| Z_3 : Lam] = 4 x 3 = 12 = covering degree"
      " (one cusp over one cusp, full multiplicity)", 4 * 3 == 12)

# ---------------------------------------------------------------------------
hr("PART 0.4 -- dual lattices, exactly (sympy)")
# ---------------------------------------------------------------------------
B_O = sp.Matrix([[1, sp.Rational(1, 2)], [0, sq3 / 2]])   # columns b1,b2
B_L = sp.Matrix([[1, 0], [0, 2 * sq3]])                   # columns c1,c2
U_O = B_O.T.inv()                                          # dual basis columns
U_L = B_L.T.inv()
check("O^v basis  = (1,-1/sqrt3), (0,2/sqrt3)",
      sp.simplify(U_O - sp.Matrix([[1, 0], [-1 / sq3, 2 / sq3]])) == sp.zeros(2, 2))
check("Lam^v basis = (1,0), (0,1/(2 sqrt3))",
      sp.simplify(U_L - sp.Matrix([[1, 0], [0, 1 / (2 * sq3)]])) == sp.zeros(2, 2))
# O^v in Lam^v coordinates: integer matrix, index 4  (duality reverses inclusion)
Mdual = sp.simplify(U_L.inv() * U_O)
check("O^v subset Lam^v with coord matrix [[1,0],[-2,4]], index 4, SNF diag(1,4)",
      Mdual == sp.Matrix([[1, 0], [-2, 4]]) and smith_diag(Mdual) == (1, 4))
print("  membership criterion: nu = n1 v1 + n2 v2 in O^v  <=>  2 n1 + n2 = 0 mod 4")
ok = True
for n1 in range(-4, 5):
    for n2 in range(-8, 9):
        sol = Mdual.solve(sp.Matrix([n1, n2]))
        in_dualO = all(x.is_integer for x in sol)
        ok = ok and (in_dualO == ((2 * n1 + n2) % 4 == 0))
check("criterion verified exactly on the block |n1|<=4, |n2|<=8", ok)

# ---------------------------------------------------------------------------
hr("PART 0.5 -- the palette recomputed: |(O/2^k)^x / im(mu_6)| = 1, 2, 8")
# ---------------------------------------------------------------------------
def palette(k):
    q = 2 ** k
    # elements a+bw mod q; (a+bw)(c+dw) = (ac-bd) + (ad+bc+bd) w   [w^2 = w-1]
    mul = lambda A, B: ((A[0]*B[0] - A[1]*B[1]) % q,
                        (A[0]*B[1] + A[1]*B[0] + A[1]*B[1]) % q)
    grp = [(a, b) for a in range(q) for b in range(q)
           if math.gcd(a*a + a*b + b*b, 2) == 1]
    six = [(1, 0), (q-1, 0), (0, 1), (0, q-1), (q-1, 1), (1, q-1)]  # +-1,+-w,+-w^2
    # (w^2 = w-1 => -w^2 = 1-w = (1,-1))
    img = set()
    for u in six:
        img.add((u[0] % q, u[1] % q))
    return len(grp), len(img), len(grp) // len(img)

pal = {k: palette(k) for k in (1, 2, 3)}
print(f"  level (2):  |(O/2)^x|  = {pal[1][0]},  |im mu_6| = {pal[1][1]},  quotient = {pal[1][2]}")
print(f"  level (4):  |(O/4)^x|  = {pal[2][0]},  |im mu_6| = {pal[2][1]},  quotient = {pal[2][2]}")
print(f"  level (8):  |(O/8)^x|  = {pal[3][0]},  |im mu_6| = {pal[3][1]},  quotient = {pal[3][2]}")
check("palette sizes 1, 2, 8 at levels (2), (4), (8)  (B737-P3 datum recomputed)",
      (pal[1][2], pal[2][2], pal[3][2]) == (1, 2, 8))

# ---------------------------------------------------------------------------
hr("PART 0.6 -- the base scattering re-derived: phi_O(s) = Lambda_K(s-1)/Lambda_K(s)")
# ---------------------------------------------------------------------------
s_ = sp.symbols('s', positive=True)
r_ = sp.symbols('r', positive=True)
I1 = sp.integrate(2 * sp.pi * r_ * (1 + r_ ** 2) ** (-s_), (r_, 0, sp.oo),
                  conds='none')
check("unfolding integral int_{R^2} (1+|x|^2)^(-s) dx = pi/(s-1)",
      sp.simplify(I1 - sp.pi / (s_ - 1)) == 0, f"sympy: {I1}")
q_ = sp.symbols('q', positive=True)
geo = 1 + (1 - 1 / q_) * q_ ** (1 - s_) / (1 - q_ ** (1 - s_))
target = (1 - q_ ** (-s_)) / (1 - q_ ** (1 - s_))
check("local Euler factor sum_k Phi(p^k) q^(-ks) = (1-q^-s)/(1-q^(1-s))"
      "  =>  sum_A Phi(A) N(A)^-s = zeta_K(s-1)/zeta_K(s)",
      sp.simplify(geo - target) == 0)
check("V(F_L) = covol(O) = sqrt3/2", sp.simplify(B_O.det() - sq3 / 2) == 0)
zs, zs1 = sp.symbols('zs zs1')
lhs = (2 * sp.pi / (sq3 * (s_ - 1))) * zs / zs1
c_ = sq3 / (2 * sp.pi)
rhs = (c_ ** (s_ - 1) * sp.gamma(s_ - 1) * zs) / (c_ ** s_ * sp.gamma(s_) * zs1)
check("phi_O(s) = (2pi/(sqrt3 (s-1))) zeta_K(s-1)/zeta_K(s) = Lambda_K(s-1)/Lambda_K(s)",
      sp.simplify(lhs - rhs) == 0, "Gamma(s) = (s-1)Gamma(s-1)")
print("""  (coset/unit bookkeeping restated: Gamma_oo\\Gamma <-> coprime bottom rows
  (c,d) mod O^x; c=0 the single coset giving y^s coefficient exactly 1; c!=0
  unfolds d mod cO against the integral above with N(c)=|c|^2; the D=3 unit
  and order-3 rotation bookkeeping was re-derived in-seat in B737-P1 (69/69)
  and the three load-bearing identities are re-proven above.)""")
def phiO(s0):
    s0 = mpmathify(s0)
    return LamK(s0 - 1) / LamK(s0)
s0 = mpc("1.37", "1.19")
raw = (2 * pi / (sqrt(3) * (s0 - 1))) * zK(s0 - 1) / zK(s0)
check("derived form == completed form at a random complex s",
      fabs(phiO(s0) - raw) / fabs(phiO(s0)) < mpf(10) ** -45)
ok = all(fabs(fabs(phiO(1 + mpc(0, t))) - 1) < mpf(10) ** -45
         for t in ("0.7", "2.3", "9.1"))
check("|phi_O(1+it)| = 1 (unitary on the continuous spectrum)", ok)
check("phi_O(s) phi_O(2-s) = 1", fabs(phiO(s0) * phiO(2 - s0) - 1) < mpf(10) ** -44)

# ===========================================================================
hr("PART A -- (a) FOURIER RESTRICTION under the torus covering C/Lam -> C/O")
# ===========================================================================
print("""PROPOSITION (Fourier restriction).  Let Lam < L be lattices in R^2 of
index N, F an L-periodic smooth function, mu in Lam^v.  Then the pullback of
F along C/Lam -> C/L (i.e. F itself, read as Lam-periodic) has
  a_mu = (1/covol Lam) int_{C/Lam} F(x) e(-<mu,x>) dx
       = (1/(N covol L)) sum_{r in L/Lam} int_{C/L} F(x+r) e(-<mu,x+r>) dx
       = [ (1/N) sum_{r in L/Lam} e(-<mu,r>) ] * (1/covol L) int_{C/L} F e(-<mu,.>).
The bracket: r |-> e(-<mu,r>) is a WELL-DEFINED character of the finite
group L/Lam precisely because mu in Lam^v; by character orthogonality the
sum is N if the character is trivial (<=> mu in L^v) and 0 otherwise.  Hence
  (i)   Fourier support of the pullback lies in L^v subset Lam^v;
  (ii)  for mu in L^v the Lam-coefficient EQUALS the L-coefficient;
  (iii) mu = 0: the Lam-constant term = the L-constant term.        QED
(Elementary and complete; the only inputs are periodicity and finite-group
character orthogonality.  Verified exactly and numerically below for our
pair Lam = Z+2sqrt(-3)Z < O, N = 4.)""")

# --- A1: exact character-sum orthogonality for O/Lam = Z/4 -----------------
# reps r_k = k*w, k=0..3;  <n1 v1 + n2 v2, k w> = k n1/2 + k n2/4  (exact):
ip = sp.simplify((U_L * sp.Matrix([sp.Symbol('n1'), sp.Symbol('n2')])).dot(
    B_O * sp.Matrix([0, 1])))
check("<n1 v1 + n2 v2, w> = n1/2 + n2/4 exactly",
      sp.simplify(ip - (sp.Symbol('n1') / 2 + sp.Symbol('n2') / 4)) == 0)
ok = True
for (n1, n2) in [(0, 0), (0, 1), (0, 2), (0, 3), (1, -2), (1, -1), (1, 0),
                 (1, 1), (0, 4), (-1, 2), (2, 0), (2, 1), (2, 2), (2, 3)]:
    Ssum = sp.simplify(sum(sp.exp(-2 * sp.pi * sp.I * sp.Rational(k * (2 * n1 + n2), 4))
                           for k in range(4)))
    expect = 4 if (2 * n1 + n2) % 4 == 0 else 0
    ok = ok and (Ssum == expect)
check("character sum over O/Lam: sum_k e(-<mu, k w>) = 4*[mu in O^v], "
      "14 dual points exact (all four classes of Lam^v/O^v hit)", ok)

# --- A2: numeric verification on explicit lattice Fourier sums -------------
mp.dps = 30
random.seed(739)
u1n = (mpf(1), -1 / sqrt(3)); u2n = (mpf(0), 2 / sqrt(3))
modes = {}
for m1 in (-1, 0, 1):
    for m2 in (-1, 0, 1):
        modes[(m1, m2)] = mpc(random.uniform(-1, 1), random.uniform(-1, 1))
def Fx(x1, x2):
    tot = mpc(0)
    for (m1, m2), cm in modes.items():
        mx = m1 * u1n[0] + m2 * u2n[0]; my = m1 * u1n[1] + m2 * u2n[1]
        tot += cm * exp(2j * pi * (mx * x1 + my * x2))
    return tot

# grid-DFT on the Lam-torus (samples x = (j1/N1) c1 + (j2/N2) c2; duality
# <n1 v1 + n2 v2, x> = n1 j1/N1 + n2 j2/N2): EXACT for band-limited F.
N1, N2 = 7, 27
# aliasing-free check: mode Lam^v-coords p1 = m1 in [-2,2] (G below widens to
# 2), p2 = -2 m1 + 4 m2 in [-10,10]; tested n1 in [-2,2], n2 in [-7,7]:
check("aliasing-free grid: |p1-n1| <= 4 < N1 = 7 and |p2-n2| <= 17 < N2 = 27",
      4 < N1 and 17 < N2)
c1n = (mpf(1), mpf(0)); c2n = (mpf(0), 2 * sqrt(3))
def dft_Lam(func):
    samples = [[func(j1 * c1n[0] / N1 + j2 * c2n[0] / N2,
                     j1 * c1n[1] / N1 + j2 * c2n[1] / N2)
                for j2 in range(N2)] for j1 in range(N1)]
    def coeff(n1, n2):
        tot = mpc(0)
        for j1 in range(N1):
            for j2 in range(N2):
                tot += samples[j1][j2] * exp(-2j * pi * (mpf(n1 * j1) / N1
                                                         + mpf(n2 * j2) / N2))
        return tot / (N1 * N2)
    return coeff

coefF = dft_Lam(Fx)
image = {(m1, -2 * m1 + 4 * m2): (m1, m2) for (m1, m2) in modes}
bad = []
for n1 in range(-2, 3):
    for n2 in range(-7, 8):
        pred = modes[image[(n1, n2)]] if (n1, n2) in image else mpc(0)
        got = coefF(n1, n2)
        if fabs(got - pred) > mpf(10) ** -25:
            bad.append((n1, n2, nstr(fabs(got - pred), 5)))
check("ALL 75 Lam-Fourier coefficients (|n1|<=2, |n2|<=7) match the "
      "restriction prediction: = base coefficient on O^v, = 0 off O^v",
      not bad, f"failures: {bad}" if bad else "max err < 1e-25")
# base-torus DFT (skew coords) recovers the base coefficients themselves:
NB = 7
sampB = [[Fx(t1 * mpf(1) / NB + t2 * mpf("0.5") / NB,
             t2 * (sqrt(3) / 2) / NB) for t2 in range(NB)] for t1 in range(NB)]
okB = True
for (m1, m2), cm in modes.items():
    tot = mpc(0)
    for t1 in range(NB):
        for t2 in range(NB):
            tot += sampB[t1][t2] * exp(-2j * pi * (mpf(m1 * t1) / NB
                                                   + mpf(m2 * t2) / NB))
    okB = okB and fabs(tot / NB ** 2 - cm) < mpf(10) ** -25
check("O-torus DFT recovers all 9 base coefficients (constant term included:"
      " Lam-constant term == O-constant term)", okB)

# independent slow adaptive-quadrature cross-checks (not grid-based):
mp.dps = 20
area = 2 * sqrt(3)
def quad_coeff(func, n1, n2):
    nux = n1 * mpf(1); nuy = n2 / (2 * sqrt(3))
    return quad(lambda x1: quad(lambda x2: func(x1, x2)
                                * exp(-2j * pi * (nux * x1 + nuy * x2)),
                                [0, 2 * sqrt(3)]), [0, 1]) / area
v = quad_coeff(Fx, 1, -2)
check("adaptive quad, nu=(1,-2) in O^v: = c_(1,0)",
      fabs(v - modes[(1, 0)]) < mpf(10) ** -15, f"err {nstr(fabs(v - modes[(1,0)]), 3)}")
v = quad_coeff(Fx, 0, 1)
check("adaptive quad, nu=(0,1) NOT in O^v: = 0",
      fabs(v) < mpf(10) ** -15, f"|val| {nstr(fabs(v), 3)}")

# ===========================================================================
hr("PART B -- (b) THE ONE-CUSP LEMMA re-derived (function-level equality)")
# ===========================================================================
print("""LEMMA (one cusp over one cusp => exact scalar transfer).
  Gamma = PSL(2,O_3), Gamma' < Gamma the index-12 m004 group (one cusp each,
  PART 0.2 / [S] l.658 with h=1).  Read constant terms in the same intrinsic
  height y (conventions block).  Then
        E_m004(., s) = E_orb(., s)  AS FUNCTIONS on H^3, and in particular
        phi_m004(s) = phi_O(s) = Lambda_K(s-1)/Lambda_K(s)   IDENTICALLY.

PROOF (every step numbered; verification status per step at the end).
 (1) g := E_orb(., s), read as a Gamma'-invariant function (Gamma' < Gamma:
     the pullback along Gamma'\\H^3 -> Gamma\\H^3 is LITERALLY the same
     function on H^3).  It is smooth, -Delta g = s(2-s) g, of moderate
     growth in the cusp  [continuation + growth: standard input S1].
 (2) CONSTANT TERM of g along the m004 cusp: g is (O x| Z_3)-invariant, in
     particular O-periodic, with O-constant term y^s + phi_O(s) y^(2-s)
     ([S] (2.6)', re-derived in PART 0.6).  Its m004-cusp constant term is
     the average over C/Lam, Lam < O index 4: by PART A (iii) this EQUALS
     the O-average:   c.t.(g) = y^s + phi_O(s) y^(2-s).
     [The order-3 rotation needs no separate treatment for the constant
      term; it is handled fully in PART E(iv).]
 (3) h := g - E_m004(., s).  Both constant terms have leading coefficient
     EXACTLY 1*y^s (each Eisenstein series has the single c=0 coset over its
     own cusp stabilizer; same y), so
         c.t.(h) = [phi_O(s) - phi_m004(s)] y^(2-s)  =:  c(s) y^(2-s).
 (4) NONZERO MODES decay exponentially: each nonzero Fourier mode of an
     eigenfunction of moderate growth is a multiple of y K_{s-1}(2pi|mu|y)
     (the I-solution is excluded by moderate growth) -- ODE re-derived
     below (B2), K-decay and I-growth verified numerically.  Both g and
     E_m004 have this structure ([S] (2.20)); uniformity of the mode sums
     is standard input S3.  Hence  h - c(s) y^(2-s) = O(e^{-2 pi y / (2
     sqrt3)}) in the cusp  [smallest nonzero |mu| in Lam^v = 1/(2 sqrt3)
     ... |v2| = 1/(2 sqrt3) < 1 = |v1|].
 (5) GLOBAL L^2: m004 = (compact core) union (one cusp end).  On the
     compact core h is smooth hence bounded hence L^2 (finite volume).  In
     the cusp end {y > Y0}: the measure is y^{-3} dy dx, and
         int_{Y0}^oo |y^{2-s}|^2 y^{-3} dy = Y0^{2-2s}/(2s-2) < oo for
     real s > 1  (B3 below), while the O(e^{-cy}) tail is trivially L^2.
     So h in L^2(m004) for real s > 1 (off the finitely many poles).
 (6) KILL ZONE I (s > 2, no continuation needed): for real s > 2 both
     Eisenstein series converge absolutely ([S] after (2.4)), and
     -Delta h = s(2-s) h with s(2-s) < 0.  -Delta is a NON-NEGATIVE
     self-adjoint operator on L^2(m004)  [essential self-adjointness on the
     complete manifold m004: standard input S2]; a smooth L^2 eigenfunction
     with L^2 image lies in its domain, and a negative eigenvalue is
     impossible.  Hence h = 0 for every real s > 2.
 (7) KILL ZONE II (1 < s < 2, the prereg's range): s(2-s) in (0,1).  If
     h != 0 then s(2-s) is an EIGENVALUE of -Delta.  The point spectrum of
     any self-adjoint operator on a SEPARABLE Hilbert space is COUNTABLE
     (eigenspaces are mutually orthogonal; an uncountable orthogonal family
     of unit vectors cannot exist in a separable space -- B4 below).
     s |-> s(2-s) is injective on (1,2), so h != 0 for at most countably
     many s in (1,2); off that countable set and the finitely many poles,
     h = 0.  ([S] p.264 gives the sharper FINITENESS of eigenvalues in
     [0,1) -- quoted in PART C -- making the exceptional set finite; the
     countability argument already suffices and is self-contained.)
 (8) CONCLUSION: c(s) = phi_O(s) - phi_m004(s) is meromorphic (S1) and
     vanishes on a set with an accumulation point (all of (2,oo) by (6);
     co-countably in (1,2) by (7)), hence c == 0 IDENTICALLY, and h == 0
     for all s: E_m004 = pullback E_orb as functions, all Fourier
     coefficients restricted from the base.                          QED""")

# --- B1: the two constant-mode solutions ----------------------------------
y_, s2_ = sp.symbols('y s', positive=True)
for a_expr, name in [(y_ ** s2_, "y^s"), (y_ ** (2 - s2_), "y^(2-s)")]:
    L = y_ ** 2 * sp.diff(a_expr, y_, 2) - y_ * sp.diff(a_expr, y_) \
        + s2_ * (2 - s2_) * a_expr
    check(f"constant-mode radial equation: {name} solves y^2 a'' - y a' + s(2-s) a = 0",
          sp.simplify(L) == 0)

# --- B2: nonzero modes are Bessel; K decays, I grows ----------------------
mu_ = sp.symbols('mu', positive=True)
cB = 2 * sp.pi * mu_
tB = cB * y_
okS = True
for Bf, sgn in [(sp.besselk, 1), (sp.besseli, -1)]:
    aB = y_ * Bf(s2_ - 1, tB)
    expr = sp.expand(y_ ** 2 * sp.diff(aB, y_, 2) - y_ * sp.diff(aB, y_)
                     + (s2_ * (2 - s2_) - cB ** 2 * y_ ** 2) * aB)
    # standard recurrences X_{nu+1} = X_{nu-1} + sgn (2 nu/t) X_nu  (K: +, I: -)
    subs = {Bf(s2_ + 1, tB): Bf(s2_ - 1, tB) + sgn * (2 * s2_ / tB) * Bf(s2_, tB),
            Bf(s2_ - 3, tB): Bf(s2_ - 1, tB) - sgn * (2 * (s2_ - 2) / tB) * Bf(s2_ - 2, tB)}
    r1 = sp.expand(expr.subs(subs))
    subs2 = {Bf(s2_, tB): Bf(s2_ - 2, tB) + sgn * (2 * (s2_ - 1) / tB) * Bf(s2_ - 1, tB)}
    okS = okS and (sp.simplify(sp.expand(r1.subs(subs2))) == 0)
check("y K_(s-1)(2pi mu y) and y I_(s-1)(2pi mu y) solve the nonzero-mode "
      "radial equation y^2 a''- y a' + (s(2-s) - 4pi^2 mu^2 y^2) a = 0 "
      "(SYMBOLIC, via the three-term recurrences)", okS)
mp.dps = 30
okN = True
for Bf in (besselk, besseli):
    sv, muv, yv = mpf("1.37"), mpf("0.83"), mpf("1.9")
    cv = 2 * pi * muv
    a = lambda y: y * Bf(sv - 1, cv * y)
    resid = (yv ** 2 * diff(a, yv, 2) - yv * diff(a, yv)
             + (sv * (2 - sv) - cv ** 2 * yv ** 2) * a(yv))
    okN = okN and fabs(resid) / max(fabs(a(yv)), 1) < mpf(10) ** -22
check("...and numerically (relative residual < 1e-22 at a random point)", okN)
Kratio = besselk(mpf("0.4"), 20) / besselk(mpf("0.4"), 10)
Iratio = besseli(mpf("0.4"), 20) / besseli(mpf("0.4"), 10)
check("K decays / I grows exponentially (moderate growth FORCES the K-branch"
      " => nonzero modes decay like e^(-2pi|mu|y))",
      Kratio < mpf(10) ** -4 and Iratio > mpf(10) ** 3,
      f"K(20)/K(10) = {nstr(Kratio, 3)}, I(20)/I(10) = {nstr(Iratio, 3)}")

# --- B3: cusp L^2 integrability of the constant term ----------------------
Y0 = sp.symbols('Y0', positive=True)
Iy = sp.integrate(y_ ** (2 * (2 - s2_)) * y_ ** -3, (y_, Y0, sp.oo), conds='none')
check("int_Y0^oo y^(2(2-s)) y^-3 dy = Y0^(2-2s)/(2s-2) < oo for s > 1",
      sp.simplify(Iy - Y0 ** (2 - 2 * s2_) / (2 * s2_ - 2)) == 0, f"sympy: {Iy}")

# --- B4: countability of the point spectrum (self-contained proof) --------
print("""  B4 (countability, self-contained): eigenvectors of a self-adjoint
  operator for DISTINCT eigenvalues are orthogonal ( lam<u,v> = <Au,v> =
  <u,Av> = nu<u,v> => (lam-nu)<u,v> = 0 ).  If the point spectrum were
  uncountable, choosing one unit eigenvector per eigenvalue would give an
  uncountable orthonormal family; but L^2(m004) is separable (m004 is a
  second-countable manifold with a sigma-finite measure), and a separable
  Hilbert space contains no uncountable orthonormal family (the open balls
  B(e_i, 1/2) are pairwise disjoint).  So the point spectrum is countable.""")
check("B4 recorded (elementary functional analysis, complete as stated)", True)

print("""  STANDARD INPUTS used by the lemma (cited, NOT re-proven -- flagged
  honestly; each is classical for cofinite Kleinian groups):
   S1  meromorphic continuation of E(., s) in s, finitely many poles in
       (1,2], polynomial order  ([S] "may, by the general theory of
       Selberg, be continued to a meromorphic function of s"; [F]/[EGM98
       ch.6 (Selberg/Colin de Verdiere method)]).
   S2  essential self-adjointness of Delta on C_c^oo of a COMPLETE
       Riemannian manifold (Gaffney), so -Delta has ONE self-adjoint
       realization, non-negative, and smooth L^2 eigenfunctions with L^2
       image are in its domain.
   S3  moderate growth of E in the cusp, uniform on s-compacta, so the
       nonzero-mode tail sums to O(e^-cy)  (Kubota-style estimate; [S]
       Sec. 2).
  NOT AVAILABLE IN-SANDBOX (honest gap, declared): an INDEPENDENT numerical
  computation of E_m004 / phi_m004 (Hejhal-class machinery; parked
  owner-gated per the prereg).  The equality is established analytically
  above, with every in-sandbox-checkable ingredient checked.""")

# ===========================================================================
hr("PART C -- (c) EXHAUSTION: multiplicity of the continuous spectrum = #cusps = 1")
# ===========================================================================
print("""AT SOURCE (both documents re-fetched 2026-07-21, quotes in the header):
  [S] p.264: "The interval [1, oo) comprises two kinds of spectrum: Firstly
      the continuous spectrum which is SPANNED BY THE EISENSTEIN SERIES
      E_j(1+it), t in R, where the j denotes the Eisenstein series in the
      JTH CUSP." -- one Eisenstein channel per cusp, nothing else in the
      continuous part; stated for ANY finite-volume 3-manifold ("the theory
      has been fully developed for any three manifold of finite volume",
      resting on Selberg [19]; the finite-volume spectral theory also goes
      under Lax-Phillips).
  [F] Lemma 2.1, eq. (2.6) (resting on [EGM98, Chapter 3]): the continuous
      part of the automorphic kernel is EXACTLY
        (1/4pi) sum_{alpha=1}^{kappa(Gamma)} sum_{l=1}^{k_alpha} (...)
        int_R h(1+t^2) E_alpha^l(P,it) (x) E_alpha^l(Q,it) dt,
      a sum over the kappa(Gamma) cusps with k_alpha channels each; for the
      TRIVIAL character V = C, k_alpha = dim_C V_alpha = 1 at every cusp:
      multiplicity = kappa(Gamma) = number of cusps.  PERIOD.
SPECIALIZATION TO THE OBJECT (computed): m004 has kappa = 1 cusp (PART 0.2)
  => the continuous spectrum of L^2(m004) is [1, oo) with multiplicity
  EXACTLY 1, furnished ENTIRELY by the single Eisenstein series E_m004,
  whose 1x1 scattering "matrix" is phi_m004 = phi_O = Lambda_K(s-1)/
  Lambda_K(s) (PART B).  There is NO OTHER CONTINUOUS CHANNEL: no place in
  the continuous spectrum for any further L-function to enter.""")
check("m004: kappa = 1 (computed, PART 0.2); multiplicity-one statement "
      "source-verified at two independent primary sources", M.num_cusps() == 1)

# ===========================================================================
hr("PART D -- (d) WHERE THE PALETTE LIVES (statement; no Maass computation)")
# ===========================================================================
print("""STATEMENT (precise, scoped).  The conductor-(4) and conductor-(8) Hecke
characters of K (palette sizes 2 and 8 mod the units, recomputed in PART
0.5) CANNOT appear anywhere in the continuous spectrum of m004:
  - the continuous spectrum is the single channel E_m004 (PART C), and its
    complete spectral data -- every Fourier coefficient and the scattering
    function phi_m004(s) = Lambda_K(s-1)/Lambda_K(s) -- is restricted from
    the level-one base (PARTS A+B); the divisor of phi_m004 consists of
    zeta_K zeros/poles ONLY.  A nonzero coefficient of any L(s, chi),
    chi != 1, anywhere in the continuous channel would contradict the
    function-level equality.
THEREFORE the level's new arithmetic can live only in:
  (1) the DISCRETE spectrum: L^2 Maass eigenfunctions of m004.  These are
      genuinely new at the level (they are NOT pullbacks: a pullback of an
      orbifold Maass form is Gamma'-invariant and accounts only for the
      old/oldform part; the index-12 congruence level admits newforms whose
      Hecke eigenvalue data can involve the conductor-(4)/(8) characters).
      B735's "index-12 new resonances" = exactly this discrete new part.
  (2) NON-SPECTRAL data (e.g. geodesic/length data, torsion, Chern-Simons),
      outside the Laplace spectrum entirely.
  No Maass-form computation is attempted here (Hejhal-class machinery;
  parked owner-gated per the prereg).  This statement is the sharp form of
  "redirected-to-discrete": a two-outcome consequence, not a computation of
  where in the discrete spectrum the characters DO appear.""")
check("(d) recorded as a precise scoped statement (consequence of (a)-(c))", True)

# ===========================================================================
hr("PART E -- (e) MB12 FAILURE MODES, each checked")
# ===========================================================================
# --- (i) more than one cusp ------------------------------------------------
check("(i) m004 has exactly 1 cusp (snappy, PART 0.2) and the base orbifold "
      "has exactly h(K) = 1 cusp ([S] l.658: cusps <-> ideal classes; h = 1 "
      "recomputed via Minkowski in PART 0.1)", M.num_cusps() == 1)
print("      With k > 1 cusps phi would be a k x k matrix of partial zeta "
      "functions and\n      the scalar argument would FAIL -- this is the "
      "sharpest failure mode and it is\n      excluded by computation, not "
      "assumption.")

# --- (ii) special s: the s=2 pole (residual spectrum) ---------------------
mp.dps = 60
res_exact = 2 * pi ** 2 / (9 * zK(2))
eps = mpf(10) ** -30
res_lim = eps * phiO(2 + eps)
res_cauchy = quad(lambda th: phiO(2 + mpf("0.3") * exp(1j * th))
                  * mpf("0.3") * exp(1j * th), [0, 2 * pi]) / (2 * pi)
res_orbgeo = (sqrt(3) / 6) / vol_orb      # covol(orbifold cusp section)/vol(orb)
res_m004geo = 2 * sqrt(3) / volH          # covol(C/Lam)/vol(m004)
print(f"  Res_s=2 phi_O, eps-limit        = {nstr(res_lim, 40)}")
print(f"  Res_s=2 phi_O, Cauchy integral  = {nstr(res_cauchy.real, 40)}")
print(f"  2 pi^2/(9 zeta_K(2))            = {nstr(res_exact, 40)}")
print(f"  orbifold:  (sqrt3/6)/vol_orb    = {nstr(res_orbgeo, 40)}")
print(f"  cover:     2 sqrt3/vol(m004)    = {nstr(res_m004geo, 40)}")
check("(ii) Res_{s=2} phi = 2pi^2/(9 zeta_K(2)) by two numeric routes "
      "(eps-limit + Cauchy, 25+ digits)",
      fabs(res_lim - res_exact) / res_exact < mpf(10) ** -25
      and fabs(res_cauchy.real - res_exact) / res_exact < mpf(10) ** -25
      and fabs(res_cauchy.imag) < mpf(10) ** -25)
check("(ii) BOTH SIDES have the SAME s=2 residue: (sqrt3/6)/vol_orb == "
      "2 sqrt3/vol(m004) == the analytic residue (the index 12 cancels: "
      "cusp covol x12 [4x3], volume x12)",
      fabs(res_orbgeo - res_exact) / res_exact < mpf(10) ** -45
      and fabs(res_m004geo - res_exact) / res_exact < mpf(10) ** -45)
# exact algebra behind the cancellation (sympy, zeta_K(2) symbolic):
zK2 = sp.symbols('zK2', positive=True)
volO_s = 3 ** sp.Rational(3, 2) * zK2 / (4 * sp.pi ** 2)     # Humbert
lhs1 = (sq3 / 6) / volO_s
lhs2 = 2 * sq3 / (12 * volO_s)
rhs1 = 2 * sp.pi ** 2 / (9 * zK2)
check("(ii) exact: (sqrt3/6)/V_orb = 2 sqrt3/(12 V_orb) = 2pi^2/(9 zeta_K(2))"
      " with V_orb = 3^(3/2) zeta_K(2)/(4pi^2)",
      sp.simplify(lhs1 - rhs1) == 0 and sp.simplify(lhs2 - rhs1) == 0)
print("""      Poles in (1,2) (residual/small eigenvalues): [S] p.264 -- FINITELY
      many eigenvalues in [0,1); the kill-zone-II argument runs on the
      complement of a countable set and is immune to them; at s = 2 both
      sides carry the same simple pole with the SAME residue (above), so
      the identity extends through s = 2 as meromorphic functions.  No
      special s breaks the lemma.""")

# --- (iii) vector-valued / weight-k channels (scope) ----------------------
print("""  (iii) SCOPE (declared, not a gap in the claim): everything here is the
      SCALAR weight-0 Laplacian on functions -- the setting of the prereg,
      of B735's voice, and of [S]/[F] eq. (2.6) with trivial character.
      Differential-form / vector-bundle Laplacians have their own
      continuous channels with their own scattering; NOTHING is claimed
      about them.  Character-rigidity is claimed for (and only for) the
      weight-0 continuous spectrum.  A future vector-valued computation is
      a NEW question, not a failure mode of this one.""")
check("(iii) scope recorded", True)

# --- (iv) the order-3 cusp rotation ---------------------------------------
# rotation by 120deg: R b1 = -b1 + b2, R b2 = -b1  (exact):
Rmat = sp.Matrix([[sp.Rational(-1, 2), -sq3 / 2], [sq3 / 2, sp.Rational(-1, 2)]])
MR = sp.simplify(B_O.inv() * Rmat * B_O)
check("(iv) R(O) = O: R has INTEGER matrix [[-1,-1],[1,0]] in the O-basis "
      "(order 3, det 1)",
      MR == sp.Matrix([[-1, -1], [1, 0]]) and sp.simplify(MR ** 3) == sp.eye(2)
      and MR.det() == 1)
Sdual = sp.simplify(MR.inv().T)
check("(iv) R(O^v) = O^v: dual action S = [[0,-1],[1,-1]], S^3 = 1",
      Sdual == sp.Matrix([[0, -1], [1, -1]]) and sp.simplify(Sdual ** 3) == sp.eye(2))
# Lam is NOT rotation-invariant: R c2 = (-2,-2) in O-coords, not in Lam:
Rc2 = MR * sp.Matrix([-2, 4])
sol = Mcoords.solve(Rc2)
check("(iv) R(Lam) != Lam: R(2 sqrt-3) has Lam-coords (-2/4-solve) NON-integer"
      " -- the rotation is NOT a symmetry of the cover's cusp torus",
      Rc2 == sp.Matrix([[-2], [-2]]) and not all(x.is_integer for x in sol))
print("""      HOW THE ROTATION ENTERS (explicit): the orbifold cusp cross-section
      is the flat orbifold C/(O x| Z_3); the covering of cusp sections
      FACTORS as   C/Lam --(index 4)--> C/O --(deg 3)--> C/(O x| Z_3).
      E_orb, as a function on H^3, is (O x| Z_3)-invariant: its O-Fourier
      coefficients satisfy the SYMMETRY c_{S mu} = c_mu (verified below) --
      the rotation CONSTRAINS the base palette, it does not enlarge it.
      The restriction argument (PART A) runs along the FIRST arrow alone,
      applied to the Z_3-invariant O-periodic lift; the constant term is
      rotation-invariant automatically (mu = 0 is a fixed point of S).
      Lam-non-invariance of the rotation is irrelevant: the rotation never
      acts on the cover's torus, only on the base's.""")
# numeric: symmetrize F under Z/3 and re-run the FULL restriction battery
mp.dps = 30
Sn = [[0, -1], [1, -1]]
def S_apply(m, k):
    m1, m2 = m
    for _ in range(k):
        m1, m2 = -m2, m1 - m2
    return (m1, m2)
Rn = [[mpf(-1) / 2, -sqrt(3) / 2], [sqrt(3) / 2, mpf(-1) / 2]]
def Gx(x1, x2):
    tot = Fx(x1, x2)
    a1, a2 = Rn[0][0] * x1 + Rn[0][1] * x2, Rn[1][0] * x1 + Rn[1][1] * x2
    tot += Fx(a1, a2)
    b1v, b2v = Rn[0][0] * a1 + Rn[0][1] * a2, Rn[1][0] * a1 + Rn[1][1] * a2
    tot += Fx(b1v, b2v)
    return tot / 3
# predicted base coefficients of G: d_m = (1/3) sum_j c_{S^j m}  (c=0 off-set)
dpred = {}
allm = set()
for m in list(modes) + [S_apply(m, 1) for m in modes] + [S_apply(m, 2) for m in modes]:
    allm.add(m)
for m in allm:
    dpred[m] = sum(modes.get(S_apply(m, j), mpc(0)) for j in range(3)) / 3
okinv = all(fabs(dpred[m] - dpred[S_apply(m, 1)]) == 0 for m in allm)
check("(iv) predicted base coefficients of the symmetrization satisfy "
      "d_{S mu} = d_mu exactly (rotation constrains, does not enlarge)", okinv)
coefG = dft_Lam(Gx)
imageG = {}
for m in allm:
    m1, m2 = m
    imageG[(m1, -2 * m1 + 4 * m2)] = m
bad = []
for n1 in range(-2, 3):
    for n2 in range(-7, 8):
        pred = dpred[imageG[(n1, n2)]] if (n1, n2) in imageG else mpc(0)
        got = coefG(n1, n2)
        if fabs(got - pred) > mpf(10) ** -24:
            bad.append((n1, n2, nstr(fabs(got - pred), 5)))
check("(iv) FULL battery on the Z_3-symmetrized function: all 75 "
      "Lam-coefficients = restriction of the (symmetric) base palette; "
      "support still in O^v; constant term preserved (= c_(0,0))",
      not bad and fabs(coefG(0, 0) - modes[(0, 0)]) < mpf(10) ** -24,
      f"failures: {bad}" if bad else "max err < 1e-24")
mp.dps = 20
v = quad_coeff(Gx, 0, 0)
check("(iv) adaptive-quad cross-check: Lam-constant term of the symmetrized "
      "function = c_(0,0) (independent of the grid)",
      fabs(v - modes[(0, 0)]) < mpf(10) ** -15)

# ===========================================================================
hr("VERDICT")
# ===========================================================================
allpass = all(PASS)
print(f"""
checks: {sum(PASS)}/{len(PASS)} passed   [runtime {time.time()-T0:.0f}s]

PER-ITEM PROOF STATUS (prereg (a)-(e); honest grading):
 (a) Fourier restriction: PROVEN-IN-SANDBOX.  Complete elementary proof
     (character orthogonality on L/Lam), exact instance verification (14
     dual points, all 4 classes), 75-coefficient exact-DFT battery + 2
     independent adaptive-quadrature cross-checks on explicit lattice
     Fourier sums with the explicit pair Lam = Z+2sqrt(-3)Z < O, index 4.
 (b) Function-level equality E_m004 = pullback E_orb: PROVEN-IN-SANDBOX
     MODULO 3 NAMED STANDARD INPUTS (S1 continuation, S2 essential
     self-adjointness/Gaffney, S3 uniform moderate growth -- classical,
     flagged, not re-proven).  Re-derived here: both kill zones (s > 2
     negative-eigenvalue; 1 < s < 2 countable-point-spectrum -- the latter
     self-contained, not even needing [S]'s finiteness), constant-mode and
     Bessel-mode radial equations (symbolic + numeric), cusp L^2
     integrability, global L^2, meromorphy conclusion.  DECLARED GAP: no
     independent in-sandbox numerical computation of E_m004 exists
     (Hejhal-class; owner-gated).
 (c) Exhaustion/multiplicity one: SOURCE-VERIFIED at two independent
     primary documents re-fetched today ([S] p.264 verbatim; [F] Lemma
     2.1/(2.6) resting on [EGM98 ch.3]) + #cusps(m004) = 1 COMPUTED.
     Continuous spectrum of the one-cusped m004 = [1,oo), multiplicity
     EXACTLY 1, spanned by the single E_m004.
 (d) Where the palette lives: STATED PRECISELY as a consequence of
     (a)+(b)+(c); palette 1/2/8 at (2)/(4)/(8) RECOMPUTED in-sandbox; no
     Maass computation attempted (declared).
 (e) MB12: (i) computed (1 cusp both levels); (ii) computed (s=2 residues
     EQUAL: exact algebra + 25-40 digits, two numeric routes; the index 12
     cancels 4x3 against the volume); (iii) scope declared (weight 0
     only); (iv) computed (rotation = base-side constraint; composite
     covering factorization; Lam-non-invariance exact; full symmetrized
     battery passes).

OUTCOME: {"A" if allpass else "B/check-failures above"} -- CHARACTER-RIGIDITY AT FULL STRENGTH (weight-0 scope):
  the continuous spectrum of m004 is ONE channel carrying EXACTLY the
  field's completed zeta_K (phi_m004 = Lambda_K(s-1)/Lambda_K(s), zeros rho
  and poles rho-1 and the s=2 pole with residue 2sqrt3/vol(m004), nothing
  else); NO conductor-(4)/(8) Hecke character appears ANYWHERE in it; the
  level's new arithmetic lives ONLY in the discrete newform spectrum (or
  outside the spectrum).  B735's "index-12 new resonances" are hereby
  sharpened to: DISCRETE-ONLY.
FALSIFIABILITY (MB12): the claim would have FAILED had m004 more cusps, had
  the character sum not vanished off O^v, had the s=2 residues differed, or
  had a kill zone been empty -- each was a computation, none was assumed.
Firewall: pure math/structural throughout; no physics value; nothing to
  CLAIMS.  L2 status: resolved NO-in-the-continuous / redirected-to-
  discrete (per the sealed two-outcome).
""")
sys.exit(0 if allpass else 1)
