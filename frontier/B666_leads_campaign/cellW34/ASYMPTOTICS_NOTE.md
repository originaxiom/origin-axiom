# THE ASYMPTOTICS DERIVATION NOTE (B666 cell F', re-scoped per
# ADDENDUM_1 amendment / B668; executed by cell W3-4, 2026-07-17)

Classification of the banked observable families by GENUINE large-k
behavior, with the exact growth exponents derived and verified
(f_prime_asymptotics.py; full output in cellW34_output.txt), and the
legal-target list for any future resurgence attempt.  This note is the
execution of B668's ruling: the original F' ("resurgent S2 from the
ladder") died against the melody theorem; what follows is what large-k
content actually exists.

## CLASS P — PERIODIC: zero asymptotic content

| family | fact | source |
|---|---|---|
| the Z-ladder Z(kappa) | exactly periodic; N0 = 2^6 3^3 5^4 7^2 11^2 19^2; EXACT minimal period P = 175560 = 2^3*3*5*7*11*19 | melody theorem (B651), B662/G |
| every metallic-word certificate ladder Z_t(kappa), t = 3,4,5,6 | finite exact q-support => exactly periodic => bounded; WORD-UNIVERSAL (not an amphichirality property) | B669 |
| the generic subsequence | minimal period 5 = disc(A1) | B656/G2 |

A periodic sequence has NO 1/k asymptotic series: Z ~ exp(k S0 + S1 +
S2/k + ...) is a type error on this class.  Every currently banked
k-indexed trace observable is in this class.  ILLEGAL as a resurgence
target, permanently.

## CLASS G1 — POWER-LAW GROWTH, CONVERGENT CORRECTIONS
## (legal expansions, zero resurgent content)

All from the Kac-Peterson formulas; kappa = k + h_vee; simply-laced
normalization (theta,theta) = 2; all identities below verified exactly
(sympy) and all exponents verified numerically (40-digit mpmath) with
banked anchors: SU(2) closed form (B238 su2_data), SU(3) Weyl sum at
k=2 (B238 su3_data, modulus — their S00 carries the (-i)^{|D+|}
Weyl-denominator phase), E6 Weyl sum at k=2 rebuilt by the banked B570
method (|W| = 51840).

**S00(kappa) = kappa^{-r/2} (det A)^{-1/2} prod_{a>0} 2 sin(pi ht(a)/kappa)**
=> exact growth law

    S00 ~ C_g kappa^{-dim(g)/2},   C_g = (det A)^{-1/2} prod_{a>0} 2 pi ht(a)

(from r/2 + |D+| = dim/2 and (rho,a) = ht(a), both verified exactly):

| stage | r | \|D+\| | dim | EXPONENT of S00 | verified slope |
|---|---|---|---|---|---|
| SU(2) | 1 | 1 | 3 | **-3/2** | -1.499999 |
| SU(3) | 2 | 3 | 8 | **-4** | -3.999996 |
| E6 | 6 | 36 | 78 | **-39** | -38.999338 |

Constant checks S00*kappa^{dim/2}/C_g -> 1 at kappa = 1e5 (all three).
Every FIXED-label S-entry has the same exponent (S_{lm}/S00 ->
dim(l)*dim(m); A1 witness computed).  The global dimension 1/S00 grows
as kappa^{+dim/2}.

**Fixed-rep quantum dimensions** (the "S2-coefficient" of this class,
derived in closed form):

    d_lambda(kappa) = dim V_lambda * (1 - pi^2 h_vee C2(lambda) / (6 kappa^2) + O(kappa^-4))

with C2(lambda) = (lambda, lambda+2rho) — the second asymptotic
coefficient IS the Casimir.  Derivation from the exact matrix identity
sum_{a>0} c_a c_a^T = h_vee A^{-1} (i.e. sum_{a>0} (mu,a)(nu,a) =
h_vee (mu,nu)), verified as an exact sympy identity for A1/A2/E6.
Numerical Richardson fits match to <= 5e-9 relative on all six banked
reps: A1 fund (C2=3/2), A1 adj (4), SU(3) fund (8/3, == the banked
su32_wrt header formula), SU(3) adj (6), E6 27 (52/3), E6 78 (24 =
2h_vee).

**Alcove-interior quantum dimensions** grow as kappa^{|D+|} =
kappa^{(dim-r)/2}: verified slopes 1.0000 / 2.9977 / 35.9996 for
SU(2)/SU(3)/E6.  **T-entries**: h_lambda = C2/(2 kappa) -> 0 and
c(kappa) -> dim g, both convergent 1/kappa series => bounded
oscillatory.

All class-G1 expansions are CONVERGENT (finite products of functions
analytic in 1/kappa) => Borel-trivial: no Stokes data, no
nonperturbative ambiguity, nothing for resurgence to reconstruct.  The
coefficient ladder exists (and is derivable in closed form, as above);
the resurgent ladder is empty.

## CLASS G2 — THE TORSION TOWERS: q-GEVREY (theta-class) GROWTH

From cellB2's banked exact landscape (B617 closed form; 78 entries,
m in {1,4,5,7,8,11}, tr = 3..15).  New exact form, verified against
ALL 78 banked integers:

    |tau_m(tr)| = prod_{j=1..m} (beta^j - beta^-j)^2,
    beta = (tr + sqrt(tr^2-4))/2

equivalently THE BIGROWTH LAW (30-digit spot checks, exact identity):

    log|tau_m(tr)| = m(m+1) log beta + 2 log (q;q)_m,   q = beta^-2

- **m-direction (fixed tr):** |tau_m| = (q;q)_inf^2 * beta^{m(m+1)} *
  (1 + eps), |eps_m| < 3 q^{m+1} (verified for the whole tr=3 column;
  at tr=3, 2 log(q;q)_inf = -0.365723620).  log|tau_m| ~ m^2 log beta:
  SUPER-FACTORIAL (q-Gevrey / theta class).  Classical Borel-GMP
  resurgence is a type error on this growth; the only machinery that
  types is q-Borel-Laplace / quantum-modular analysis, with the
  natural degeneration wall q -> 1 (tr -> 2, the parabolic limit).
- **tr-direction (fixed m):** exponent m(m+1) exactly —
  |tau_m(tr)|/tr^{m(m+1)} -> 1 monotonically (0.857 -> 0.906 across
  tr=12..15 at m=4), with CONVERGENT 1/tr corrections => G1-type.

One exponent, m(m+1), governs both directions of the tower, on the
fundamental eigenvalue beta(tr).

## THE LEGAL-TARGET LIST (for any future resurgence attempt)

1. **ILLEGAL:** any 1/k expansion of any banked trace ladder (class P).
   The melody theorem + B669's word-universality close this
   permanently; "S2 from the ladder" stays dead (B668's ruling — this
   note is its execution).
2. **LEGAL BUT TRIVIAL:** class G1 (S-entries, quantum dimensions,
   T-entries).  Expansions exist and are here derived in closed form
   (exponents -dim/2, +(dim-r)/2; the Casimir 1/kappa^2 coefficient);
   convergence => zero resurgent content.  An "extraction" here can
   only re-derive known closed forms.
3. **LEGAL, NON-CLASSICAL (the one honest direction):** the torsion
   tower in m (class G2) — the unique banked family with
   more-than-power growth.  A future attempt must use q-calculus
   (q-Borel) machinery; the target is the q -> 1 (tr -> 2) behavior of
   (q;q)_inf at q = beta^-2 — quantum-modular territory, flagged as
   research-grade.  NOT claimed to be feasible; claimed to be the only
   banked family where the question types.
4. **THE HONEST STATEMENT (B668's second outcome, delivered jointly
   with the table):** NO banked observable carries extractable
   CLASSICAL resurgent (divergent-factorial) content.  Any genuine
   GMP-style program would first have to construct a new observable
   with an honestly divergent perturbative expansion; no trace ladder
   can supply one (the class-P argument is word-universal), and the
   stage families cannot either (convergent).

## Firewall

B669's ruling stands verbatim: wall 10 (dimensionful quantities
untypeable) + R5 (k <-> scale untyped).  Nothing in this note licenses
any vacuum-energy, scale, or cosmology reading; all labels here are
mathematical.  Novelty of the closed forms NEEDS-SPECIALIST as always
(the KP formulas and q-Pochhammer asymptotics are cited-standard; the
tower's bigrowth law is a restatement of B617's banked theorem in
beta-product form).
