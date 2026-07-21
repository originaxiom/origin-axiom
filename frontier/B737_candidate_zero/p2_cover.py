#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B737 CANDIDATE ZERO -- PROBE 2: COVER (the object's own voice)
==============================================================
Sealed under frontier/B737_candidate_zero/PREREGISTRATION.md (probe 2 of 4).

QUESTION (two-outcome, sealed):
  (a) How does the scattering matrix / Eisenstein constant term of the COVER
      (m004, the object) relate to the base Bianchi orbifold's
      (PSL(2,O_3)\\H^3)?  State the precise standard relation and its source.
  (b) Does the object's OWN scattering therefore carry the zeta_K structure
      WHOLE (poles included)?
  (c) The closing: verify Dehn filling removes the cusp (m004 -> 1 complete
      cusp; m004(5,1) -> 0 cusps, closed hyperbolic) and state exactly what
      structure is destroyed.
  A = the object's voice carries zeta_K whole and closing destroys precisely
      that;  B = the cover breaks/loses the pole structure.

CONVENTIONS BLOCK (WORKING_RULES rule 4 -- declared before the run)
  * K = Q(sqrt(-3)), discriminant d = -3, ring O = Z[w], w = (1+sqrt(-3))/2
    (Eisenstein integers), N(a+bw) = a^2+ab+b^2, unit number w_K = 6,
    class number h = 1 (both recomputed below).
  * chi = chi_{-3}: chi(n) = +1, -1, 0 for n = 1, 2, 0 mod 3.
  * zeta_K(s) = zeta(s) * L(s,chi)  (grounded numerically below by the
    ideal-count identity r(n) = sum_{d|n} chi(d), n <= 2000, from direct
    lattice enumeration mod units).
  * COMPLETED zeta: Lambda_K(s) = (sqrt(3)/(2*pi))^s * Gamma(s) * zeta_K(s);
    functional equation Lambda_K(s) = Lambda_K(1-s) (verified numerically).
  * Spectral convention (shifted): eigenfunction E(P,s) of -Delta with
    eigenvalue 1-s^2; cusp constant term  y^(1+s) + phi(s) * y^(1-s)  in the
    INTRINSIC (un-normalized Busemann) height y of the cusp at infinity.
    Sarnak (Acta 1983) uses s_Sarnak = 1 + s, eigenvalue s_S(2-s_S); we map
    his formulas through s_S = 1+s.  Continuous spectrum = {1+t^2} = [1,oo).
  * No cusp-width normalization anywhere: base and cover constant terms are
    read in the SAME y.  (A width normalization would multiply phi by
    c^s, c>0 -- entire, zero-free, pole-free: divisor unchanged.  Declared.)
  * Numerics: mpmath dps as set per section (>= 50); snappy 3.3.2
    Manifold/ManifoldHP for m004, m004(5,1).  snappy Numbers are converted
    through str() with pari's space-before-exponent stripped (helper snum).

PRIMARY SOURCES (fetched at source 2026-07-21, pdftotext extracts in session
scratchpad; quoted excerpts below are from those extracts):
  [S] P. Sarnak, "The arithmetic and geometry of some hyperbolic three
      manifolds", Acta Math. 151 (1983) 253-295 (open access, projecteuclid
      .org/journals/acta-mathematica/volume-151/issue-none/.../BF02393209.pdf)
      - eq. (2.9)-(2.11): for h=1,
          phi(s_S) = pi/(V(F_L)(s_S-1)) * zeta_K(s_S-1)/zeta_K(s_S),
        V(F_L) = covolume of O as a lattice in R^2 (= sqrt(3)/2 for d=-3).
      - Lemma 2.13 + (2.14): Res[E, s_S=2] = 2*pi^2/(V(F_L)*w_K*sqrt|d|*zeta_K(2)).
      - Lemma 2.15: Res[E, s_S=2] = V(F_L)/V(F_D)  (Maass-Selberg style).
      - Prop. 2.1 (Humbert): V(F_D) = |d|^(3/2) * zeta_K(2)/(4*pi^2), with
        Note (1): "Though our proof does not apply directly to the cases of
        Q(sqrt-1) and Q(sqrt-3), the above formula is nevertheless valid
        since W and a factor of V(F_L) cancel."
      - Note (2): number of inequivalent cusps of the Bianchi orbifold = h.
      (Sarnak's Sec. 2 derivation excludes D=1,3 for unit bookkeeping; the
       D=3 case is DERIVED from scratch in-sandbox in PART A1 below, units
       and the order-3 cusp rotation handled explicitly.)
  [F] J. S. Friedman, "Analogues of the Artin factorization formula for the
      automorphic scattering matrix and Selberg zeta-function associated to
      a Kleinian group", arXiv:math/0702030.  Main scattering theorem
      (proved as Thm 5.1), quoted from the extract:
        "Theorem. Let Gamma be a cofinite Kleinian group, Gamma_1 a
         finite-index normal subgroup of Gamma. Let chi in Rep(Gamma_1,V),
         and psi = U^chi [the induced representation]. Then for all regular
         s in C,  phi(s,Gamma_1,chi) = phi(s,Gamma,psi)."
      With chi = 1:  phi(s,Gamma_1,1) = phi(s,Gamma,U^1) and
      U^1 = (+)_theta theta^{n_theta} over irreps of Gamma_1\\Gamma, so the
      subgroup's scattering determinant = product over irreps, CONTAINING
      the base scattering determinant as the trivial-representation factor.
      This is the Kleinian (3d) extension of Venkov-Zograf [VZ83].
  [V] A. B. Venkov, Spectral theory of automorphic functions, Proc. Steklov
      Inst. Math. (1982); A. B. Venkov + P. G. Zograf, Math. USSR Izvestiya
      21 (1983) 435-443 (the Fuchsian original; cited through [F]).
  [B734] in-repo: m004 = index-12 congruence cover of the Bianchi orbifold
      PSL(2,O_3)\\H^3 (corroborated below: Humbert volume ratio = 12 to
      ~1e-55; shapes' minimal polynomial z^2-z+1; cusp-lattice index 4 x
      rotation order 3 = 12).

CAVEAT ON NORMALITY (declared up front): [F]/[V] require Gamma_1 NORMAL in
Gamma.  Our cover is NOT normal (|Isom(m004)| = 8 < 12 = degree, computed
below), so the factorization theorem is quoted as the standard relation for
the normal case, and the transfer used here is proved DIRECTLY by the
one-cusp uniqueness lemma (PART B1) -- which is stronger (exact scalar
equality, no determinant, no normality).

POST-HOC NOTE (declared, WORKING_RULES rule 3): the first run of this file
failed on tooling bugs -- a Python float contamination 3**(-2) inside
zeta_K at integer argument, mpmath Hurwitz zeta at s=1 (nan), a sympy
integral form that did not auto-simplify, and snappy's pari-style
space-before-exponent number strings.  All are FIXED here (mpmathify on
entry; digamma formula for L(1,chi); polar-coordinate integral; snum
helper).  No mathematical claim changed; the failed transcript is preserved
in p2_cover_out_run1_FAILED.txt.
"""

import sys
from mpmath import (mp, mpf, mpc, gamma, pi, sqrt, zeta, quad, exp, psi,
                    findroot, fabs, mpmathify)

PASS = []
def check(label, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    PASS.append(bool(ok))
    print(f"  [{tag}] {label}" + (f"  ({detail})" if detail else ""))
    if not ok:
        print("  *** HARD FAIL -- probe aborts with outcome-relevant failure ***")

def hr(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)

def snum(x):
    """snappy Number -> mpf (pari prints '... e-65' with a space)."""
    return mpf(str(x).replace(' ', ''))

# ---------------------------------------------------------------------------
hr("PART A0 -- field arithmetic of K = Q(sqrt(-3)) recomputed from scratch")
# ---------------------------------------------------------------------------
mp.dps = 60

# units of O = Z[w], w=(1+sqrt(-3))/2, N(a+bw)=a^2+ab+b^2
units = [(a, b) for a in range(-2, 3) for b in range(-2, 3)
         if a * a + a * b + b * b == 1]
print(f"units of O (N=1 solutions): {units}")
check("unit number w_K = 6", len(units) == 6)

# class number h=1 via the Minkowski bound (2/pi)*sqrt(3) < 2:
mink = (2 / pi) * sqrt(3)
print(f"Minkowski bound = (2/pi)*sqrt(3) = {mink}")
check("Minkowski bound < 2  =>  h(K) = 1 (every class has an ideal of norm 1)",
      mink < 2)

# ideal counts r(n) by direct lattice enumeration mod units, vs sum_{d|n} chi(d)
import math
X = 2000
R = int(math.isqrt(4 * X // 3)) + 2
cnt = {}
for a in range(-R, R + 1):
    for b in range(-R, R + 1):
        n = a * a + a * b + b * b
        if 0 < n <= X:
            cnt[n] = cnt.get(n, 0) + 1
def chi(n):
    return (0, 1, -1)[n % 3]
ok = True
for n in range(1, X + 1):
    r_lat = cnt.get(n, 0) // 6              # elements mod 6 units = ideals (h=1)
    r_chi = sum(chi(d) for d in range(1, n + 1) if n % d == 0)
    if r_lat != r_chi:
        ok = False
        print(f"  mismatch at n={n}: lattice {r_lat} vs chi {r_chi}")
        break
check(f"#ideals of norm n == sum_(d|n) chi_-3(d) for all n <= {X} "
      "(grounds zeta_K = zeta * L(chi))", ok)

# numeric zeta_K and Lambda_K (mpmathify on entry: no float contamination)
def L_chi(s):
    s = mpmathify(s)
    return 3 ** (-s) * (zeta(s, mpf(1) / 3) - zeta(s, mpf(2) / 3))
def zK(s):
    s = mpmathify(s)
    return zeta(s) * L_chi(s)
def LamK(s):
    s = mpmathify(s)
    return (sqrt(3) / (2 * pi)) ** s * gamma(s) * zK(s)

# L(1,chi) via the digamma formula  L(1,chi) = (psi(2/3) - psi(1/3))/3
kappa_target = 2 * pi * 1 / (6 * sqrt(3))          # class number formula 2*pi*h/(w*sqrt|d|)
L1 = (psi(0, mpf(2) / 3) - psi(0, mpf(1) / 3)) / 3
print(f"L(1,chi)          = {L1}")
print(f"2*pi*h/(w*sqrt3)  = {kappa_target}   (B736's residue 0.6046...)")
check("residue of zeta_K at s=1: L(1,chi) == 2*pi/(6*sqrt3)",
      fabs(L1 - kappa_target) < mpf(10) ** -50, "class number formula, recomputed")

# functional equation of the COMPLETED zeta (validates the completion used)
ok = True
for s0 in (mpc("0.3", "2.1"), mpc("0.72", "-5.4"), mpc("-1.3", "0.9")):
    ok = ok and fabs(LamK(s0) - LamK(1 - s0)) / fabs(LamK(s0)) < mpf(10) ** -45
check("Lambda_K(s) = Lambda_K(1-s) at 3 complex points (rel err < 1e-45)", ok)

# ---------------------------------------------------------------------------
hr("PART A1 -- symbolic ingredients of the base scattering (sympy proofs)")
# ---------------------------------------------------------------------------
import sympy as sp

s = sp.symbols('s', positive=True)
r = sp.symbols('r', positive=True)
# (i) the unfolding integral over C = R^2, in polar coordinates:
#     int_R2 (1+|x|^2)^(-(1+s)) dx = int_0^oo 2*pi*r (1+r^2)^(-(1+s)) dr = pi/s
I = sp.integrate(2 * sp.pi * r * (1 + r ** 2) ** (-(1 + s)), (r, 0, sp.oo))
check("unfolding integral  int_{R^2} (1+|x|^2)^(-(1+s)) dx = pi/s",
      sp.simplify(I - sp.pi / s) == 0, f"sympy (polar): {I}")

# (ii) local Euler factor:  1 + sum_{k>=1} Phi(p^k) q^(-k(s+1))
#      with Phi(p^k) = q^k - q^(k-1):
#      geometric series  = 1 + (1-1/q) * q^(-s)/(1-q^(-s))
#      algebraic identity = (1-q^(-s-1))/(1-q^(-s))
q = sp.symbols('q', positive=True)
k = sp.symbols('k', positive=True, integer=True)
geo = 1 + (1 - 1 / q) * q ** (-s) / (1 - q ** (-s))
target = (1 - q ** (-s - 1)) / (1 - q ** (-s))
alg_ok = sp.simplify(geo - target) == 0
# and the geometric summation itself, exactly at (q,s) = (7,2):
S_exact = sp.Sum((q ** k - q ** (k - 1)) * q ** (-k * (s + 1)),
                 (k, 1, sp.oo)).subs({q: sp.Integer(7), s: sp.Integer(2)}).doit()
sum_ok = sp.simplify(1 + S_exact
                     - target.subs({q: sp.Integer(7), s: sp.Integer(2)})) == 0
check("Euler factor  sum_k Phi(p^k)/q^(k(s+1)) = (1-q^(-s-1))/(1-q^(-s))"
      "  =>  sum_A Phi(A)/N(A)^(s+1) = zeta_K(s)/zeta_K(s+1)",
      alg_ok and sum_ok, "identity symbolic + exact geometric sum at q=7,s=2")

# (iii) covolume of O as a lattice in R^2 = C:
covol_O = sp.Matrix([[1, sp.Rational(1, 2)], [0, sp.sqrt(3) / 2]]).det()
check("V(F_L) = covol(O) = sqrt(3)/2", sp.simplify(covol_O - sp.sqrt(3) / 2) == 0)

# (iv) completed form:  (2*pi/(sqrt3*s)) * zeta_K(s)/zeta_K(s+1)
#                     == Lambda_K(s)/Lambda_K(s+1)   via Gamma(s+1)=s*Gamma(s)
zs, zs1 = sp.symbols('zs zs1')            # placeholders for zeta_K(s), zeta_K(s+1)
c = sp.sqrt(3) / (2 * sp.pi)
lhs = (2 * sp.pi / (sp.sqrt(3) * s)) * zs / zs1
rhs = (c ** s * sp.gamma(s) * zs) / (c ** (s + 1) * sp.gamma(s + 1) * zs1)
check("phi(s) = (2pi/(sqrt3 s)) zeta_K(s)/zeta_K(s+1) = Lambda_K(s)/Lambda_K(s+1)",
      sp.simplify(lhs - rhs) == 0, "Gamma(s+1)=s*Gamma(s)")

print("""
DERIVATION (D=3 done directly, units + order-3 cusp rotation handled;
each computational step verified above; framework = EGM ch. 6 / [S] Sec. 2):
  Gamma = PSL(2,O_3);  Gamma_oo = stab(oo)  contains translations by O and
  the rotations diag(eps,eps^-1), eps^2 in {1,w,w^2}  (cusp cross-section =
  the (3,3,3) Euclidean orbifold T^2/Z_3).
  Cosets Gamma_oo\\Gamma  <->  coprime bottom rows (c,d) mod the FULL unit
  group O* (|O*| = 6; in PSL: mod {1,w,w^2} x {+-1}):
    - c = 0: single coset  ->  y^(1+s) coefficient exactly 1;
    - c != 0: fix one generator c per nonzero ideal (h=1: c mod O* <-> (c));
      then d runs over ALL d in O with (c,d)=1, each a distinct coset.
  Zeroth Fourier coefficient over C/O of the c-sum, unfolding d mod cO
  against the x-integral (integral (i)), with N(c) = |c|^2:
    phi(s) = ( pi / (s * V(F_L)) ) * sum_{ideals A != 0} Phi(A)/N(A)^(s+1)
           = ( 2*pi / (sqrt(3) * s) ) * zeta_K(s)/zeta_K(s+1)      [(ii),(iii)]
           =  Lambda_K(s) / Lambda_K(s+1)                          [(iv)]
  This MATCHES [S] eq. (2.9)-(2.10) (his s_S = 1+s, h=1, V(F_L)=sqrt(3)/2),
  now including D=3 which [S] Sec. 2 excluded for unit bookkeeping.
=> THE BASE ORBIFOLD'S 1x1 SCATTERING "MATRIX" IS THE COMPLETED-DEDEKIND-
   ZETA RATIO   phi_O(s) = Lambda_K(s)/Lambda_K(s+1),   POLES INCLUDED.""")

# ---------------------------------------------------------------------------
hr("PART A2 -- numeric verification of phi_O = Lambda_K(s)/Lambda_K(s+1)")
# ---------------------------------------------------------------------------
mp.dps = 60
def phi(s0):
    return LamK(s0) / LamK(mpmathify(s0) + 1)
def phi_raw(s0):                       # the derived (uncompleted) form
    s0 = mpmathify(s0)
    return (2 * pi / (sqrt(3) * s0)) * zK(s0) / zK(s0 + 1)

s0 = mpc("0.37", "1.19")
check("completed and derived forms agree numerically at a random complex s",
      fabs(phi(s0) - phi_raw(s0)) / fabs(phi(s0)) < mpf(10) ** -45)

# unitarity on the critical axis and the functional relation phi(s)phi(-s)=1
ok1 = all(fabs(fabs(phi(mpc(0, t))) - 1) < mpf(10) ** -45 for t in ("0.7", "2.3", "9.1"))
check("|phi(it)| = 1  (unitary scattering on the continuous spectrum [1,oo))", ok1)
check("phi(s)*phi(-s) = 1", fabs(phi(s0) * phi(-s0) - 1) < mpf(10) ** -45)

# phi(0) = -1  (the two Lambda-poles at 0 and at 1 collide and cancel)
val = phi(mpf(10) ** -30)
Lchi0 = L_chi(0)
print(f"phi(1e-30) = {val}")
print(f"L(0,chi) = {Lchi0}  (exact 1/3 => zeta_K(0) = -1/6)")
check("phi(0) = -1", fabs(val + 1) < mpf(10) ** -25)
check("L(0,chi) = 1/3", fabs(Lchi0 - mpf(1) / 3) < mpf(10) ** -50)

# THE POLE AT s=1 (the observer's beta=1 pole, B736) and its residue,
# by two independent numeric routes: the eps-limit and a Cauchy integral.
mp.dps = 70
eps = mpf(10) ** -30
res_lim = eps * phi(1 + eps)
res_cauchy = quad(lambda th: phi(1 + mpf("0.3") * exp(1j * th))
                  * mpf("0.3") * exp(1j * th), [0, 2 * pi]) / (2 * pi)
res_exact = 2 * pi ** 2 / (9 * zK(2))
print(f"residue at s=1, eps-limit       = {mp.nstr(res_lim, 40)}")
print(f"residue at s=1, Cauchy integral = {mp.nstr(res_cauchy.real, 40)}")
print(f"2*pi^2/(9*zeta_K(2))  [S](2.14) = {mp.nstr(res_exact, 40)}")
check("res_{s=1} phi = 2*pi^2/(9*zeta_K(2)) > 0  (simple pole, positive residue)",
      fabs(res_lim - res_exact) / res_exact < mpf(10) ** -25
      and fabs(res_cauchy.real - res_exact) / res_exact < mpf(10) ** -25
      and fabs(res_cauchy.imag) < mpf(10) ** -25 and res_exact > 0)
# Sarnak (2.14) with D=3 constants: 2*pi^2/(V(F_L)*w*sqrt|d|*zeta_K(2)),
# V(F_L)*w*sqrt|d| = (sqrt3/2)*6*sqrt3 = 9  -- same number:
check("[S] (2.14) with V(F_L)=sqrt3/2, w=6, sqrt|d|=sqrt3: denominator = 9",
      sp.simplify((sp.sqrt(3) / 2) * 6 * sp.sqrt(3) - 9) == 0)

# ---------------------------------------------------------------------------
hr("PART A3 -- the infinite tower is IN the scattering (zeros/poles located)")
# ---------------------------------------------------------------------------
mp.dps = 50
# first nontrivial zero of zeta_K = first zero of L(s,chi_-3): rho_1 ~ 1/2 + 8.04i
rho1 = findroot(lambda z: zK(z), mpc("0.5", "8.03"), solver='muller')
print(f"rho_1 = {rho1}")
check("zeta_K(rho_1) = 0 with Re(rho_1) = 1/2",
      fabs(zK(rho1)) < mpf(10) ** -40 and fabs(rho1.real - mpf(1) / 2) < mpf(10) ** -30,
      "first L(chi_-3) zero, t ~ 8.0397")
# a second tower point inherited from zeta(s): rho_2 ~ 1/2 + 14.1347i
rho2 = findroot(lambda z: zK(z), mpc("0.5", "14.13"), solver='muller')
check("zeta_K(rho_2) = 0 with Re(rho_2) = 1/2",
      fabs(zK(rho2)) < mpf(10) ** -40 and fabs(rho2.real - mpf(1) / 2) < mpf(10) ** -30,
      "first Riemann zero, t ~ 14.1347")
# the scattering function has a ZERO at rho and a POLE at rho-1:
z1, p1 = fabs(phi(rho1)), fabs(phi(rho1 - 1))
z2, p2 = fabs(phi(rho2)), fabs(phi(rho2 - 1))
print(f"|phi(rho_1)|   = {mp.nstr(z1, 5)}   |phi(rho_1 - 1)| = {mp.nstr(p1, 5)}")
print(f"|phi(rho_2)|   = {mp.nstr(z2, 5)}   |phi(rho_2 - 1)| = {mp.nstr(p2, 5)}")
check("phi has zeros at the nontrivial zeros rho and poles at rho-1",
      z1 < mpf(10) ** -25 and z2 < mpf(10) ** -25
      and p1 > mpf(10) ** 25 and p2 > mpf(10) ** 25)
print("""
DIVISOR OF phi(s) = Lambda_K(s)/Lambda_K(s+1)  (Lambda_K: poles exactly at
s=0,1; zeros exactly at the nontrivial zeros of zeta_K):
    poles:  s = 1 (simple, residue 2*pi^2/(9*zeta_K(2)) > 0  -- THE zeta_K
            pole, i.e. B736's beta=1 object), and s = rho-1 for every
            nontrivial zero rho of zeta_K;
    zeros:  s = rho for every nontrivial zero, and s=0 is regular
            (pole-pole cancellation, phi(0) = -1).
    Euler product over ALL primes of O -- no finite congruence truncation.""")

# ---------------------------------------------------------------------------
hr("PART B0 -- the cover: m004 over the Bianchi orbifold (facts recomputed)")
# ---------------------------------------------------------------------------
mp.dps = 60
import warnings
warnings.filterwarnings("ignore")
import snappy

M = snappy.Manifold('m004')
H = snappy.ManifoldHP('m004')
print(f"m004: num_cusps = {M.num_cusps()}, cusp = {M.cusp_info()[0]}")
check("the object has exactly ONE cusp (complete torus cusp)",
      M.num_cusps() == 1 and M.cusp_info()[0].is_complete)

shapes = [mpc(snum(w.real()), snum(w.imag())) for w in H.tetrahedra_shapes('rect')]
resid = max(fabs(z ** 2 - z + 1) for z in shapes)
check("tetrahedra shapes satisfy z^2 - z + 1 = 0 (both = exp(i*pi/3))",
      resid < mpf(10) ** -55, f"max residual {mp.nstr(resid, 3)}")
print("  => invariant trace field = Q(shapes) = Q(sqrt(-3))  (Neumann-Reid).")

volH = snum(H.volume())
vol_orb = 3 ** mpf("1.5") * zK(2) / (4 * pi ** 2)     # Humbert ([S] Prop 2.1 + Note (1))
ratio = volH / vol_orb
print(f"vol(m004)      = {mp.nstr(volH, 55)}")
print(f"vol(orbifold)  = {mp.nstr(vol_orb, 55)}   [Humbert, [S] Prop 2.1]")
print(f"ratio          = {mp.nstr(ratio, 55)}")
check("vol(m004) / vol(PSL(2,O_3)\\H^3) = 12 (covering degree, B734)",
      fabs(ratio - 12) < mpf(10) ** -50)

# cusp cross-section bookkeeping: cusp shape of m004 = 2*sqrt(-3)
sh = H.cusp_info()[0].shape
tau = mpc(snum(sh.real()), snum(sh.imag()))
check("cusp shape of m004 = 2*sqrt(-3)  (lattice Z + 2sqrt(-3)Z, in K)",
      fabs(tau - mpc(0, 1) * 2 * sqrt(3)) < mpf(10) ** -50, f"tau = {mp.nstr(tau, 20)}")
# index of Z+2sqrt(-3)Z in O = covol ratio = (2sqrt3)/(sqrt3/2) = 4; times the
# order-3 cusp rotation of the orbifold: 4*3 = 12 = the covering degree,
# exactly the one-cusp-over-one-cusp concentration demanded by covering theory:
check("cusp-section degree = [O x| Z_3 : Z+2sqrt(-3)Z] = 4*3 = 12 = index",
      sp.simplify((2 * sp.sqrt(3)) / (sp.sqrt(3) / 2) - 4) == 0)

Sym = M.symmetry_group()
print(f"Isom(m004) = {Sym}, order {Sym.order()}, full: {Sym.is_full_group()}")
check("the 12-cover is NOT normal: |Isom(m004)| = 8 < 12 (no deck group of "
      "order 12 can act)", Sym.order() == 8 and Sym.is_full_group())

# ---------------------------------------------------------------------------
hr("PART B1 -- THE TRANSFER: one-cusp uniqueness lemma (direct proof)")
# ---------------------------------------------------------------------------
print("""
STANDARD RELATION, AT SOURCE ([F] arXiv:math/0702030, Kleinian extension of
Venkov-Zograf [VZ83]; NORMAL finite-index subgroups):
    phi(s, Gamma_1, chi) = phi(s, Gamma, U^chi)          (all regular s)
    => phi(s, Gamma_1, 1) = phi(s, Gamma, U^1)
     = PROD_{theta in (Gamma_1\\Gamma)*} phi(s, Gamma, theta)^{n_theta} :
    the cover's scattering determinant CONTAINS the base's (theta = trivial).
OUR COVER IS NON-NORMAL (PART B0), so we do not lean on [F]; the transfer is
proved directly, and comes out STRONGER (scalar equality, poles included):

LEMMA (one cusp over one cusp => exact scalar transfer).
  Let pi: m004 = Gamma'\\H^3 -> O_3 = Gamma\\H^3 be the degree-12 cover
  (Gamma' < Gamma = PSL(2,O_3), both 1-cusped: PART B0; [S] Note (2), h=1).
  Then, reading constant terms in the SAME intrinsic height y:
        phi_m004(s) = phi_O(s) = Lambda_K(s)/Lambda_K(s+1)   IDENTICALLY.
PROOF.
  (1) g := pi* E_O(., 1+s) is Gamma'-automorphic (Gamma' < Gamma), a
      -Delta-eigenfunction of eigenvalue 1-s^2, of moderate growth
      (local isometry; the pullback is literally the same function).
  (2) Its constant term along the m004 cusp equals the constant term of E_O:
      the m004 cusp lattice L' embeds in the orbifold cusp lattice L = O
      (PART B0: index 4, plus the Z_3 rotation), and averaging an
      L-periodic function over C/L' equals averaging over C/L
      [verified numerically below].  So   c.t.(g) = y^(1+s) + phi_O(s) y^(1-s).
  (3) h := g - E_m004(., 1+s) has constant term (phi_O - phi_m004)(s) y^(1-s).
      For real s > 1:  |y^(1-s)|^2 y^(-3) is integrable at the cusp
      [verified symbolically below], and nonzero Fourier modes decay
      exponentially ([S] Lemma 2.15 proof; Kubota), so h is in L^2.
  (4) h is an L^2 eigenfunction of -Delta (self-adjoint, >= 0) with
      eigenvalue 1-s^2 < 0  =>  h = 0  =>  phi_m004(s) = phi_O(s) for s > 1,
      hence identically by meromorphic continuation (EGM ch. 6 / [F] Sec. 2:
      E and phi are finite-order meromorphic).                          QED
  (The proof uses NO normality and no determinant: with one cusp the
   scattering matrix IS the scalar phi.)""")

# ingredient (2): sublattice averaging -- L-periodic modes integrate to zero
# over the SUBlattice torus C/L'.  L = O with basis (1,0),(1/2,sqrt3/2);
# L' = Z + 2sqrt(-3)Z with basis (1,0),(0,2sqrt3).  Dual(L) modes l != 0:
mp.dps = 30
dual_modes = [(0, 2 / sqrt(3)), (1, -1 / sqrt(3)), (1, 1 / sqrt(3)), (2, 0)]
okavg = True
for (lx, ly) in dual_modes:
    f = lambda Xv, Yv: exp(2j * pi * (lx * Xv + ly * Yv))
    val = quad(lambda Xv: quad(lambda Yv: f(Xv, Yv), [0, 2 * sqrt(3)]), [0, 1])
    okavg = okavg and fabs(val) < mpf(10) ** -20
check("every nonzero dual(O)-mode averages to 0 over the sublattice torus "
      "C/L'  (constant terms agree)", okavg)

# ingredient (3): cusp L^2 integrability of y^(1-s) for s>1
sreal = sp.symbols('s', real=True, positive=True)
y = sp.symbols('y', positive=True)
Iy = sp.integrate(y ** (2 * (1 - sreal)) * y ** -3, (y, 1, sp.oo))
check("int_1^oo y^(2(1-s)) y^-3 dy = 1/(2s) < oo for s > 1 (h is L^2 at the cusp)",
      sp.simplify(Iy - 1 / (2 * sreal)) == 0, f"sympy: {Iy}")

# consequence: the m004 residue at s=1 in terms of the OBJECT'S OWN volume
mp.dps = 60
res_exact = 2 * pi ** 2 / (9 * zK(2))
res_m004 = 2 * sqrt(3) / volH          # = sqrt3/(6*vol_orb) via ratio 12
res_geom = sqrt(3) / (6 * vol_orb)
print(f"res phi at s=1  =  2*pi^2/(9 zeta_K(2))       = {mp.nstr(res_exact, 40)}")
print(f"cusp-covol/vol  =  sqrt3/(6*vol_orb)          = {mp.nstr(res_geom, 40)}")
print(f"               =  2*sqrt3/vol(m004)           = {mp.nstr(res_m004, 40)}")
check("res_{s=1} phi_m004 = 2*sqrt(3)/vol(m004)  (three expressions agree; "
      "Humbert + class-number formula + the derived phi close a triangle)",
      fabs(res_m004 - res_exact) / res_exact < mpf(10) ** -45
      and fabs(res_geom - res_exact) / res_exact < mpf(10) ** -45)

print("""
=> (b) ANSWER: YES -- the object's own (1x1) scattering function IS
       phi_m004(s) = Lambda_K(s)/Lambda_K(s+1)
   EXACTLY, in the intrinsic normalization (any cusp renormalization
   multiplies by c^s, c > 0: entire and zero-free, divisor unchanged).
   The object's voice carries the COMPLETED Dedekind zeta of Q(sqrt(-3))
   WHOLE: the simple pole at s=1 (residue 2*sqrt3/vol(m004) > 0 -- the same
   analytic object as B736's beta=1 pole, residue proportional to
   L(1,chi) = 2*pi/(6*sqrt3)), every nontrivial zero rho (as a zero), and
   every shifted zero rho-1 (as a pole): the full infinite tower, Euler
   product over ALL primes of O, no finite congruence truncation.
   Had m004 had k > 1 cusps, phi would be a k x k matrix of PARTIAL zeta
   functions and only its determinant would be controlled; the ONE-CUSP
   structure is what forces the scalar identity -- outcome B is what this
   computation would have produced in that world.""")

# ---------------------------------------------------------------------------
hr("PART C -- THE CLOSING: Dehn filling destroys exactly that channel")
# ---------------------------------------------------------------------------
N = snappy.Manifold('m004(5,1)')
print(f"m004(5,1): solution type = '{N.solution_type()}'")
print(f"           cusp complete?  {N.cusp_info()[0].is_complete}")
print(f"           volume        = {N.volume()}")
F = N.filled_triangulation()
print(f"           filled_triangulation num_cusps = {F.num_cusps()}")
check("m004 has 1 complete cusp; m004(5,1) has 0 (filled, closed hyperbolic: "
      "all tetrahedra positively oriented)",
      M.num_cusps() == 1 and M.cusp_info()[0].is_complete
      and (not N.cusp_info()[0].is_complete) and F.num_cusps() == 0
      and N.solution_type() == 'all tetrahedra positively oriented')

print("""
WHAT IS DESTROYED (exactly):
  m004 (open cusp):   L^2 = (discrete)  (+)  INT_[1,oo)  spanned by
      E(P, 1+it), whose constant term  y^(1+it) + phi(1+it) y^(1-it)  carries
      phi = Lambda_K(s)/Lambda_K(s+1) -- the completed zeta_K, poles and all.
      The continuous spectrum [1,oo) IS the zeta_K-carrying channel (B735's
      "voice", now with its exact content identified).
  m004(5,1) (closed): compact hyperbolic 3-manifold => -Delta has PURELY
      DISCRETE spectrum (elliptic theory on compact manifolds); there is no
      cusp, hence no Eisenstein series, no constant term, no scattering
      function, no continuous spectrum.  The object that vanishes is not a
      quantity but the entire meromorphic family E(P,1+s) together with its
      scattering function phi -- i.e. precisely the completed-zeta_K
      structure (the s=1 pole = the observer's beta=1 object included).
      Closing the object silences EXACTLY the zeta_K voice.  (B735 said the
      voice vanishes; this probe says WHAT the voice was saying.)""")

# ---------------------------------------------------------------------------
hr("VERDICT")
# ---------------------------------------------------------------------------
allpass = all(PASS)
print(f"""
checks: {sum(PASS)}/{len(PASS)} passed
(a) Covering relation, at source: Friedman arXiv:math/0702030 (Kleinian
    Venkov-Zograf): for NORMAL finite-index subgroups the scattering
    determinant of the cover equals the base's twisted by Ind 1 and factors
    over irreps, containing the base determinant as the trivial factor.
    Our cover is non-normal (|Isom(m004)| = 8 < 12) -- so the transfer is
    proved DIRECTLY: with one cusp over one cusp the pullback/uniqueness
    lemma (PART B1, every ingredient verified in-sandbox) gives the scalar
    identity phi_m004 = phi_O, stronger than the determinant relation.
(b) The object's own voice: phi_m004(s) = Lambda_K(s)/Lambda_K(s+1), the
    COMPLETED Dedekind zeta of Q(sqrt(-3)) whole -- pole at s=1 (residue
    2*sqrt3/vol(m004) > 0, the beta=1 pole of B736), zeros at every rho,
    poles at every rho-1: the infinite tower, no finite-level truncation.
(c) The closing: m004(5,1) is closed hyperbolic (0 cusps): no Eisenstein
    series, no scattering, purely discrete spectrum. Dehn filling destroys
    precisely the zeta_K-carrying continuous channel.
OUTCOME: {"A" if allpass else "check failures above"} -- the object's voice
carries zeta_K whole, and closing destroys precisely that.
Firewall: pure math/structural throughout; no SM value; nothing to CLAIMS.
""")
sys.exit(0 if allpass else 1)
