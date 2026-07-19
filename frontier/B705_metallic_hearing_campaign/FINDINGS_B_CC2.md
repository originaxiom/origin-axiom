# FINDINGS — CELL B: can a NON-BUNDLE hear? (Whitehead link colored-Jones test)

*Seat cc2, read-only/advisory. Sealed prereg: MASTERPLAN_AND_PREREG.md,
sha256 = a06a1b074f22548d5d875baa8845914ca98bb007e5f789d6190df216d24cf6b6
(verified by independent `sha256sum` this run, matches SEALS.txt). Repo
untouched; this file written directly via shell redirection into the
campaign directory, no git operations performed. All algebra below is
either (a) computed from scratch with exact sympy rational/Laurent-polynomial
arithmetic and independently cross-validated against SageMath 10.9 /
SnapPy 3.3.2's `Link.jones_polynomial()`, or (b) explicitly marked as an
honest-flagged, unverified attempt. Nothing below is fabricated or quoted
from unchecked memory of a paper's formula without an independent numeric
gate.*

## VERDICT: **SILENT** (at the level actually computed — N=2 colored Jones,
i.e. the ordinary Jones polynomial, evaluated at the golden root q=e^{2pi i/5}).
No real golden/metallic tone appears in the Whitehead link's own invariant
at this level; the calibration figure-eight's tone is real and cleanly
golden-shaped, the Whitehead's is not even real. **N=3 (the literal
SU(2)_3/Fibonacci color) is INCONCLUSIVE-FLAGGED for the Whitehead link
specifically** — see part 3 for exactly what broke and why no number is
reported for it.

---

## 1. Objects and method

- **Figure-eight knot 4_1** (calibration/bundle object): SnapPy braid word
  `[1,-2,1,-2]` on 3 strands, writhe 0, 1 component. Volume 2.02988321...
  (standard).
- **Whitehead link L5a1 = 5^2_1** (test object): SnapPy braid word
  `[-1,2,-1,-1,2]` on 3 strands, writhe -1, PD code
  `[(4,0,5,3),(0,4,1,9),(6,1,7,2),(2,7,3,8),(8,5,9,6)]`, 2 components.
  Component structure (computed from the braid permutation, not assumed):
  strands {0,1} (0-indexed) merge into one continuous component (self-writhe
  -1), strand {2} is the other component alone (self-writhe 0); the other
  3 crossings are genuine inter-component crossings.

**Method (N=2, i.e. the ordinary/fundamental colored Jones = Kauffman
bracket / Jones polynomial):** built the Temperley-Lieb representation of
the braid group from scratch (rho(sigma_i) = A*1 + A^{-1} e_i, diagrams as
exact matchings composed via union-find loop-counting, all arithmetic exact
sympy Laurent polynomials in A), closed up the braid, applied the standard
writhe correction V_L(t) = (-A)^{-3w(D)} <D> with t = A^{-4}. Cross-checked
against Sage 10.9 / SnapPy's independent `Link.jones_polynomial()` for both
objects: **exact match for the figure-eight** (no ambiguity, single
component); **exact match for the Whitehead link up to a constant overall
sign** that is fully explained and not a discrepancy: SnapPy's "new
convention" for links explicitly drops the (-1)^(c-1) factor that the
classical/Lickorish-Millett-style Jones convention (c = #components) carries
for even c (confirmed directly from the docstring's own unlink formula,
"(q+q^-1)^(n-1)" vs. the classical "(-q-q^-1)^(n-1)"); with that sign
accounted for, the two independent computations agree on every coefficient.
This is a genuine, non-trivial independent verification, not a
self-consistency tautology.

## 2. Exact polynomials and the golden-root evaluation

**Figure-eight**, classical convention (integer powers of t):
V_{4_1}(t) = t^2 - t + 1 - t^-1 + t^-2

**Whitehead link**, classical convention, in q := t^{1/2} (2 components,
even, so half-integer powers of t are expected and correct — Whitehead has
linking number 0, matches):
V_W(t) = q^-7 - 2q^-5 + q^-3 - 2q^-1 + q - q^3

The golden root used, per the prereg (SU(2)_3 / Fibonacci level, k=3,
level root q_level = e^{2pi i/(k+2)} = e^{2pi i/5}): evaluate the
figure-eight at t = zeta5 = e^{2 pi i/5}, and the Whitehead at
q = zeta10 = e^{i pi/5} (so that t = zeta10^2 = zeta5, the SAME root,
consistent with the natural half-integer-power variable the Whitehead's
own polynomial is written in).

**Figure-eight at the golden root** (exact, reduced mod the 5th cyclotomic
polynomial Phi_5(y) = y^4+y^3+y^2+y+1, y = zeta5):

  V_{4_1}(zeta5) = 2y^3 + 2y^2 + 2  =  1 - sqrt(5)  =  **-2/phi**

This is REAL (verified exactly: value is fixed by the field automorphism
y -> y^-1, i.e. complex conjugation on the unit circle), lies in the real
quadratic field Q(sqrt(5)), and is a clean rational multiple of 1/phi. This
independently reproduces the campaign's own banked calibration figure
(PAPER.md section 4.5 / banked B242: "SU(2)_3 = SU(3)_2 = -2/phi, the
reduced colored-Jones value of the knot 4_1"). Good cross-check: computed
here from scratch, matches the banked value exactly.

**Whitehead link at the golden root** (exact, reduced mod the 10th
cyclotomic polynomial Phi_10(x) = x^4-x^3+x^2-x+1, x = zeta10):

  V_W(zeta10) = 2x^3 - 3x^2 + 3x

Applying complex conjugation (x -> x^-1, computed exactly in the ring
Q[x]/(Phi_10(x))) sends this to x^2 - 3x + 3, which is **NOT equal** to
2x^3-3x^2+3x, and also not its negative. **The value is a genuine, non-real
complex number.** High-precision numeric cross-check (independent of the
ring-arithmetic reduction): value = 0.881966011250105... +
0.812299240582266...i, matching the exact ring computation to 50 digits.

Exact decomposition:
- Re(V_W(zeta10)) = (4 - sqrt(5))/2 = 5/2 - phi  (in Q(sqrt(5)), but note:
  NOT a clean rational multiple of phi or 1/phi the way the fig-8 value is —
  it is a rational-plus-phi combination, i.e. even taken alone the real part
  does not have the fig-8's clean "metallic ratio" shape).
- Im(V_W(zeta10))^2 = 25/4 - (5/2) sqrt(5)  — this forces a further
  quadratic extension beyond Q(sqrt(5)); the full value lives genuinely in
  the degree-4 field Q(zeta10), not in the degree-2 real subfield Q(sqrt5).

**Why it isn't forced real:** the figure-eight's amphichirality forces
V(t) = V(1/t) as Laurent polynomials, which is why its root-of-unity value
must be real. The Whitehead link is also amphichiral as an unoriented link,
but this does NOT force V_W(t) = V_W(1/t) — checked directly and it is
neither symmetric nor antisymmetric under t -> 1/t. (Mechanically: the
Whitehead link's positive-amphichiral symmetry requires reversing the
orientation of one component, which changes effective crossing signs
between components and breaks the naive V(t)=V(1/t) relation that holds
for amphichiral knots.) This is a real, structural difference between the
link and the knot case, not an artifact.

## 3. N=3 (spin-1 / literal Fibonacci color): calibration succeeded, Whitehead honest-flagged

Built a from-scratch Jones-Wenzl f_2 = id - delta^-1 * e_1 projector
insertion via 2-cabling of the braid word (block-swap pattern for cabling a
single crossing into 4; framing correction using the ribbon twist
mu_2 = A^8; reduced normalization = raw bracket / (quantum dimension
Delta_2 = A^4+1+A^-4), once per component that is disjoint from the rest).

**Validated on single-component (knot) cases:**
- Sanity check: a 0-framed unknot with f_2 inserted reduces to exactly 1
  (required for any "reduced" colored invariant) — passes.
- Figure-eight, N=3, computed via this from-scratch cabling: reproduces
  Habiro's well-known cyclotomic-expansion closed form for 4_1's colored
  Jones **exactly as a full Laurent polynomial** (not just at one root):
  t^6-t^5-t^4+2t^3-t^2-t+3-t^-1-t^-2+2t^-3-t^-4-t^-5+t^-6. Independently
  re-derived on a SECOND, Markov-stabilized diagram of the same knot
  (different braid, writhe 1 instead of 0) and got the identical answer —
  confirms both the cabling machinery and the total-writhe framing
  correction are diagram-independent (a genuine invariant), for the
  single-component case.
- At q=zeta5, this N=3 fig-8 value equals **exactly the same** -2/phi as
  N=2. This is not a coincidence or a bug: Habiro's cyclotomic expansion has
  a term that contains the factor (q^{5/2}-q^{-5/2}), which is EXACTLY zero
  when q=zeta5 (since q^{5/2}=e^{i pi}=-1=q^{-5/2}) — all higher terms
  (k>=2) vanish identically at this specific root, leaving only the N=2
  piece. (Checked further: N=4 collapses this same mechanism one term
  earlier and gives exactly 1 — fully trivial — at zeta5.)

**Whitehead link, N=3: NOT reported, honestly.** The identical method,
applied to a genuinely 2-component link with real inter-component crossings
(tested first as a control on the plain positive Hopf link, braid closure
of sigma_1^2, both components colored N=3), produces a result that
**does not reduce to a self-consistent Laurent polynomial**: dividing the
raw bracket by Delta_2 once per component (the convention validated above
for split/disjoint unions, where it correctly reproduces the required
multiplicativity J'(K1 unlink K2) = J'(K1)*J'(K2)) leaves a genuine
non-polynomial remainder for the Hopf link, and the identical failure mode
recurs on the Whitehead link itself. Diagnostics performed: confirmed the
core cabling+composition machinery is linear and bug-free by an independent
identity check (id = f_2 + g_2 decomposition verified to hold exactly);
confirmed no choice of writhe-correction exponent (tried five values)
turns the Hopf-link result into a clean polynomial, ruling out a simple
framing-exponent error; the discrepancy is therefore a genuine unresolved
issue in extending the per-component reduced-normalization convention to
linked (non-split) multi-component colored invariants, not found and fixed
within this session's budget. **No Whitehead N=3 numeric value is reported
— reporting one would risk fabrication.** This is exactly the situation the
prereg's honest-flag clause anticipates.

## 4. Base-rate / honesty test (as required by the prereg)

Any knot or link's ordinary Jones polynomial has integer Laurent
coefficients; evaluating it at ANY 5th or 10th root of unity therefore
lands, for every knot/link without exception (including the unknot, whose
Jones polynomial is the constant 1), inside the cyclotomic field Q(zeta5)
[deg 4/Q], whose real subfield is Q(sqrt5). **That much is true regardless
of which object you plug in — it is a fact about the evaluation point, not
about the object, and by itself proves nothing about "hearing."** The
content-bearing, object-specific questions are: (i) does the value actually
land in the REAL subfield Q(sqrt5) (not automatic — depends on the
object's own symmetry, e.g. amphichirality), and (ii) if real, is it a
clean rational multiple of phi/1-over-phi (a "metallic ratio" shape) rather
than a generic real quadratic surd.

- Figure-eight (WELD/bundle object): passes BOTH bars. Real (forced by
  amphichirality + verified), and exactly -2/phi (both at N=2 and N=3).
- Whitehead (non-bundle, no monodromy): **fails bar (i) outright** — the
  N=2 value is not even real, let alone golden-ratio-shaped. Its
  amphichirality does not force reality the way the knot's does (Section 2).

## 5. Verdict

**SILENT**, at the level rigorously computed (N=2 colored Jones = ordinary
Jones polynomial, evaluated at the golden/SU(2)_3 root, cross-validated
against an independent tool). The Whitehead link's own invariant carries no
real golden tone here — consistent with, and an independent piece of
support for, the banked B699 conclusion that golden hearing is a
bundle/monodromy phenomenon, not something a generic (non-fibered) hyperbolic
object picks up just by virtue of being evaluated at a golden root. The N=3
(literal Fibonacci/SU(2)_3-color) computation for the Whitehead link is
INCONCLUSIVE-FLAGGED, not SILENT-by-computation: the method was validated
exactly (matching Habiro's trusted closed form) for single-component
objects but hit a genuine, unresolved technical obstruction extending to
this link, honestly reported rather than papered over. A follow-up cell
with more budget to fix the multi-component colored-Jones normalization (or
access to a dedicated colored-Jones/quantum-invariant package) could
close this gap; SnapPy 3.3.2 and Sage 10.9 as used here have no built-in
colored (N>2) Jones polynomial routine, only the ordinary (N=2) one.

## 6. Reproducibility

Scratch scripts used (not part of the repo, cc2 scratchpad only):
`kauffman.py` (from-scratch TL-algebra Kauffman bracket, N=2, cross-validated
vs Sage), `colored_jones2.py` (N=3 cabling + Jones-Wenzl projector, validated
on knots, honest-flagged on links), plus one-off Sage scripts used only to
call SnapPy/Sage's independent `Link.jones_polynomial()` for cross-checking.
No repo files touched; no git operations performed.
