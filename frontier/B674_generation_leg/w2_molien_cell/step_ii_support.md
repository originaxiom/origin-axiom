# STEP (ii) -- THE SUPPORT PRE-TEST (first falsifier) -- PASS
# prereg b4c9a6bb; formed symbolically from the step-(i) data; no coefficient
# expanded beyond the two grade-0 constants; no comparison against any target stream.

## The object

Molien series, one per Galois conjugate over Q(sqrt5):
  M(q)  = phi^2 * prod_{k>=1} prod_{t} (1 - zeta10^t q^k)^{-m_k(t)}      [trace-phi seed, zeta10^{+-1}]
  M'(q) = (1-phi)^2 * prod_{k>=1} prod_{t} (1 - zeta10^t q^k)^{-m'_k(t)}  [conjugate seed, zeta10^{+-3}]
with m_k the step-(i) gate distribution and m'_k its Galois conjugate (t -> 3t).
The grade-0 piece contributes the exact CONSTANTS 1/(2-phi) = phi^2 and its
conjugate (1-phi)^2 (no q-dependence; the product is well-defined since m_0(0) = 0).

## Which side of the convention every object is on

- The Molien product (weight-step grading) has INTEGER q-support: it lives on the
  REDUCED side of the Yang-Lee convention (the side of the banked reduced integer
  streams).
- The sealed per-component eta-dressing (banked, B672 recognition) maps the reduced
  side to the dressed side: comp_a = q^{nu_a} * eta^{48/5}_reduced * (reduced series),
  nu = (0, 1/5) read from sigma(T) = diag(1, zeta5) (the f1/f2 T-exponents).
- eta^{48/5} carries exactly q^{2/5} (48/5 * 1/24 = 2/5, exact Fraction arithmetic).

## The tests (all exact; each could have failed)

- [PASS] (ii-a) m_0(0) = 0: no unit eigenvalue at grade 0 => the Molien product is well-defined
- [PASS] (ii-a) grade-0 factor EXACT: det(I - W|V_0) = 2-phi and 1/(2-phi) = 1+phi = phi^2 -- M(0) = phi^2; conjugate M'(0) = 2-phi = (1-phi)^2
- [PASS] (ii-a) doublet non-collapse witness at grade 0: M(0) - M'(0) = sqrt5 != 0
- [PASS] (ii-b) Molien q-support is INTEGER (weight-step grading; the reduced side of the convention) -- support classes mod 1 of the undressed product: {0}
- [PASS] (ii-c) eta^{48/5} prefactor carries q^{2/5} exactly (48/5 * 1/24 = 2/5)
- [PASS] (ii-c) per-component intrinsic exponents nu = (0, 1/5) read from sigma(T) = diag(1, zeta5)
- [PASS] (ii-c) target class gap 3/5 - 2/5 = 1/5 == the vvmf T-exponent gap (could have failed)
- [PASS] (ii-c) REQUIRED LANDING: dressed support classes mod 1 = {2/5, 3/5} -- dressed = (2/5 + 0, 2/5 + 1/5) = (2/5, 3/5); each component single-class
- [PASS] (ii-c) both classes ATTAINED (grade-0 constants phi^2, (1-phi)^2 nonzero)
- [PASS] (ii-d) conj(distribution) == conjugate-seed distribution via t -> 3t (all k <= 40)
- [PASS] (ii-d) lift-independence: t -> 7t gives the same multisets (m_k(t) = m_k(-t))
- [PASS] (ii-d) doublet genuinely TWO-element: conjugate distribution differs -- witness k=0: classes [1, 9] vs [3, 7]; grade-0 values phi^2 vs (1-phi)^2, gap sqrt5
- [PASS] (ii-d) involution: swap^2 = id (3*3 = 9 = -1 mod 10 and m_k(-t) = m_k(t))
- [PASS] (ii-d) swap map compatible with the per-component classes 2/5 <-> 3/5

## Verdict

REQUIRED: dressed q-support classes mod 1 land in {2/5, 3/5}: MET -- the two dressed components have single-class support 2/5 and 3/5
REQUIRED: the component-swap map reproduced by the Molien doublet: MET -- Galois conjugation sqrt5 -> -sqrt5 exchanges the two conjugate series (involution; genuinely two-element, grade-0 gap sqrt5; classes 2/5 <-> 3/5 exchange
 matching the banked comp1 <-> comp2 = Yang-Lee <-> Fibonacci convention swap,
 trace phi <-> 1-phi).

Teeth (how this could have killed): (alpha) m_0(0) != 0 would make the product
divergent (DESIGN defect); (beta) a T-exponent gap != 1/5 in the block would land
the dressed classes outside {2/5, 3/5}; (gamma) a conj-unstable distribution or a
collapsed doublet (M = M') could not reproduce the two-component swap; (delta) a
fractional-support grading (weight instead of weight-step) would smear the support
over all five classes mod 1. Each was computed, none occurred.

The orientation (which Galois conjugate is comp1) is NOT fixed here: that is a
step-(iii) coefficient question and step (iii) is LOCKED pending the cc2 gate.
Structural note (no stream loaded): the trace-phi side's grade-0 value is phi^2 --
the same landscape value the banked Galois-partner doublet carries (W32).

