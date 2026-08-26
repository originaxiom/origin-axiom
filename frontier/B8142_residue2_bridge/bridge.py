"""B8142 -- does R_{rho(m)}(s) = prod_{j=-m}^{m} R(s-j, sigma_j) hold on m004?

Residue 2 (B8133) asks for a relation between the twisted Ruelle family's value at 0
(Fried's point) and its values at the positive integers (Pfaff's and the graviton's).
The candidate bridge is the eigenvalue decomposition of rho(m) = Sym^{2m} C^2:

    rho(m)(gamma) has eigenvalues e^{jL},  j = -m..m,  L = l + i*theta
    e^{jL} e^{-s l} = e^{i j theta} e^{-(s-j) l}
    =>  R_{rho(m)}(s) = prod_{j=-m}^{m} R(s-j, sigma_j)

Tested here at s > 2 + m, where EVERY factor's Euler product converges absolutely, so
both sides are computed directly with no analytic continuation.

CONTROLS, all able to fail:
  - a WRONG j-range (-m..m-1) must MISMATCH, else the test is insensitive to the claim
  - a WRONG shift (s+j instead of s-j) must MISMATCH
  - the m=0 case must be the trivial identity R(s,sigma_0) = R(s,sigma_0)
  - increasing the geodesic cutoff must make agreement BETTER, not worse
"""
import cmath
import math
import sys

try:
    import snappy
except ImportError:
    print("SKIP: snappy not available")
    sys.exit(0)

FAIL = []


def check(name, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


M = snappy.Manifold("m004")


def geos(cut):
    return [(complex(g.length), g.multiplicity) for g in M.length_spectrum(cut)]


def log_R(s, k, cut):
    """log R(s, sigma_k) = sum_gamma mult * log(1 - e^{i k theta} e^{-s l}).  Complex."""
    tot = 0j
    for L, mult in geos(cut):
        l, th = L.real, L.imag
        z = cmath.exp(1j * k * th) * math.exp(-s * l)
        tot += mult * cmath.log(1 - z)
    return tot


def log_R_rho(m, s, cut):
    """log of prod_gamma det(1 - rho(m)(gamma) e^{-s l}), via the explicit eigenvalues."""
    tot = 0j
    for L, mult in geos(cut):
        l = L.real
        for j in range(-m, m + 1):
            z = cmath.exp(j * L) * math.exp(-s * l)
            tot += mult * cmath.log(1 - z)
    return tot


def log_rhs(m, s, cut, jrange=None, twist=lambda j: j, shift=0.0):
    js = jrange if jrange is not None else range(-m, m + 1)
    return sum(log_R(s - j + shift, twist(j), cut) for j in js)


print("A  the identity, at s > 2 + m where every factor converges absolutely")
CUT = 5.5
for m, s in ((0, 6.0), (1, 6.0), (2, 6.0), (3, 8.0), (4, 9.0)):
    lhs = log_R_rho(m, s, CUT)
    rhs = log_rhs(m, s, CUT)
    d = abs(lhs - rhs)
    check("m=%d, s=%.1f :  R_rho(m)(s) == prod_j R(s-j, sigma_j)" % (m, s), d < 1e-12,
          "|diff| = %.2e" % d)

print("\nB  controls -- each must FAIL to match, or the test is insensitive")
m, s = 2, 6.0
lhs = log_R_rho(m, s, CUT)
d_bad_range = abs(lhs - log_rhs(m, s, CUT, jrange=range(-m, m)))
check("CONTROL truncated j-range (-m..m-1) MISMATCHES", d_bad_range > 1e-6,
      "|diff| = %.2e" % d_bad_range)
# NOTE: an earlier "control" here used s+j instead of s-j. It is VACUOUS -- over the
# symmetric range j = -m..m the substitution j -> -j maps {R(s-j, sigma_j)} onto itself,
# so s+j is an IDENTITY, not an error, and the check could never fail. Replaced by two
# perturbations that genuinely break the claim.
d_bad_twist = abs(lhs - log_rhs(m, s, CUT, twist=lambda j: 2 * j))
check("CONTROL wrong twist (sigma_{2j}) MISMATCHES", d_bad_twist > 1e-6,
      "|diff| = %.2e" % d_bad_twist)
d_bad_shift = abs(lhs - log_rhs(m, s, CUT, shift=0.05))
check("CONTROL perturbed shift (s-j+0.05) MISMATCHES", d_bad_shift > 1e-6,
      "|diff| = %.2e" % d_bad_shift)
d_sym = abs(lhs - sum(log_R(s + j, j, CUT) for j in range(-m, m + 1)))
check("recorded: s+j is a SYMMETRY (j -> -j), not a control -- it matches", d_sym < 1e-12,
      "|diff| = %.2e" % d_sym)

print("\nC  cutoff behaviour -- agreement must improve, not degrade")
ds = []
for c in (4.0, 4.5, 5.0, 5.5):
    ds.append(abs(log_R_rho(2, 6.0, c) - log_rhs(2, 6.0, c)))
print("     cutoffs 4.0/4.5/5.0/5.5 -> " + "  ".join("%.1e" % x for x in ds))
check("agreement holds at every cutoff (it is an identity, term by term)",
      all(x < 1e-12 for x in ds))

print("\nD  what sits at Fried's point")
m = 3
print("     R_rho(%d)(0) = prod_{j=-%d}^{%d} R(-j, sigma_j)" % (m, m, m))
print("     j < 0 half  ->  conj R(i, sigma_i), i = 1..%d   <-- the GRAVITON's own factors" % m)
print("     j = 0       ->  R(0, sigma_0)")
print("     j > 0 half  ->  R(-j, sigma_j), j = 1..%d       <-- reflected, needs continuation" % m)
for i in (3, 4, 5):
    v = log_R(float(i), i, CUT)
    print("     |R(%d, sigma_%d)| = %.10f   (converges: %d > 2)" % (i, i, math.exp(v.real), i))

print("\n%d/%d checks passed" % (10 - len(FAIL), 10))
sys.exit(1 if FAIL else 0)
