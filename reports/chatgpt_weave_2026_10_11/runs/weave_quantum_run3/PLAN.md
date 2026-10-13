# Run 3: fixed Gaussian realization and determinant multiplier

Date: 2026-10-10. This plan was written after source reading and exploratory
algebra/numerics, before the formal verification scripts. It is NOT a blind or
externally timestamped preregistration.

## Scope and fixed inputs
- Compare against Phi=eta^21(theta2^2,theta3^2,theta4^2).
- Fix one massless complex rank-two chiral fermion (four real chiral fermions),
  c=2, in the flat Q8 background on C/(Z+tau Z) minus its origin.
- Use the odd base spin structure and the extension permitting the minimal
  z^(-1/2) pole (the E-plus domain from Run 2). Its conjugate can be included
  for a nonchiral, nonanomalous full local theory; only its chiral block is
  calculated here.
- Fix coordinate-flat local metric and the usual conformal/oscillator trace
  normal ordering and prime-form OPE normalization. No spectator sector,
  eta prefactor selected from the target, arbitrary flat-line twist, or
  Standard Model input is allowed.
- Abelianize this SAME monomial representation on the unramified index-two
  cover with periods (1,2 tau), two lifted punctures at 0,tau, two charge
  -1/2 twist insertions, and a charge +1 fermion insertion at z.
- The cover is a computational choice of polarization, not a preferred word.

## Derived expectations to test (not blind predictions)
1. s(z)= (theta3(z|2tau),theta2(z|2tau))/sqrt(theta1(z|tau)) is the
   unique vector zero mode, up to scale, for the stated extension.
2. Its Wronskian is -pi eta(tau)^3; its components solve the n=1/2,
   accessory-B=0 Lame equation.
3. The complete oscillator-normalized, zero-mode-saturated Gaussian chiral
   amplitude, computed by the charge trace and prime forms on the cover,
   is a tau-independent constant times eta(tau)*s(z).
4. The constant in one explicitly continued branch is
   (2*pi)^(3/4)*exp(i*pi/8). Other constant cocycle/field phases do not affect
   the multiplier comparison.
5. Its puncture residue vector is proportional to
   (theta3(2tau),theta2(2tau))/sqrt(eta(tau)).
6. The three quadratic components K=(theta2^2,theta3^2,theta4^2)/eta
   have scalar character chi_eta^5 relative to the rotation representation,
   NOT chi_eta^3. The discrepancy is chi_eta^2, order twelve.
7. Test the discrepancy on both L and R and on all positive words through
   length eight. The balanced Fibonacci word LR is blind to it; L^3 R is not.
8. Distinguish the geometric Wronskian and zero-mode normalization from the
   infinite-dimensional fermion measure. A constant rephasing cannot repair
   the T-spectrum mismatch.

## Verification methods
- Exact symbolic matrices and cyclotomic monomial group enumeration.
- Rational q-series identities and Bernoulli/Hurwitz ground-energy check.
- Direct theta series versus independent oscillator-product formulas.
- Analytic derivations for all-domain claims, numerical checks at 80/100 dps
  at nonspecial moduli and insertion points. No interval bounds are claimed.
- Elementary OPE degeneration/factorization checks, NOT all-genus sewing.

## Explicit limits
The calculation provides holomorphic chiral amplitude multipliers in a fixed
CFT determinant trivialization. It does not separately compute a singular
Dirac spectral zeta function, the full Quillen metric/connection and its
Bismut-Freed parallel transport, a general nonabelian defect category, or a
four-dimensional/gravitational completion. A match of a Wronskian alone is
not a quantum determinant match.
