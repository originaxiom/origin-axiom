# B892 — the SECOND MEASUREMENT THEOREM verified: two charges take E₆ to the SM algebra — and the wall is a COMPLEX point of the split frame; B874 amended

> ## ⚠ SENTENCE CORRECTED BY B950 (2026-08-08) — the mathematics is untouched
>
> This arc's computation is right and is not disturbed: **dim z(x₁,y*) = 14, derived 11,
> centre 3**, i.e. **su(3) ⊕ su(2) ⊕ u(1)³**, locked in `tests/test_b892_smt.py`.
> **But su(3)⊕su(2)⊕u(1)³ is 14-dimensional and the Standard Model gauge algebra is
> 12-dimensional** — su(3)⊕su(2)⊕u(1), **one** abelian factor, not three. So the phrase
> *"take E₆ to the Standard Model algebra"* below **overstates by two abelian factors**.
> Not a refutation — extra U(1)s are standard in GUT descent (SO(10) → SM leaves
> U(1)_{B−L}), and rank-6 E₆ reaching rank-4 must shed rank somewhere — but the chain is
> **two steps from the SM, not zero**: (i) which u(1) combination is hypercharge, (ii)
> what breaks the other two. See `docs/SM_SPECIFICATION_LEDGER.md` and B950 (L132).


cc banking seat, 2026-08-04/05 night. S1 verification of the solo seat's SMT (their queue #1),
plus the amendment this seat owes its own B874. Mathematics scope; nothing to `CLAIMS.md`;
Gate 5 untouched.

## 1. The theorem, verified on this build (their exact route, end to end)

The solo seat's tower (sm_exact.py → sm_closer.py, foreign paths patched, the q-clobber
red-herring diagnosed): the block-12 pencil over F = ℚ[ρ]/μ; the **perfect-square gate
C₂² − 4C₀ = 0 exact**; γ² = −C₂/2 with the +γ eigenspace 2-dim; the traceless 2×2 giving
a² = −det₁₄ ∈ F(γ), det₁₄ ≠ 0 (gate); λ₊(y*) = 0 by construction; and the squeeze —
**dim z(x₁, y*) = 14** (≥ by construction: kernel-12 + two antipodal lines; ≤ by the tower
prime), **derived = 11** (≥ by the prime; ≤ by the wall-centrality argument), center ≥ 3 ⟹

> **z(x₁, y*) = su(3) ⊕ su(2) ⊕ u(1)³ EXACTLY. Two measurements of the object's own
> superselection charges take E₆ to the Standard Model algebra**, skipping SU(5).

(γ_q = 13410, a_q = 2675 at 40123 — matching their §XXII digits.)

## 2. This seat's two independent facts: the wall is COMPLEX in the split frame

- **Sign, computed**: det₁₄ evaluates to +2.79×10⁹ at the real root (γ-part exactly 0) ⟹
  a² < 0 ⟹ **a is imaginary**: y* = γx₁₄ − a·x₁₆ is not a real point of the split torus.
- **The real-line scan** (120-point + golden-section, 30 digits): on the real (x₁₄,x₁₆)
  projective line the ONLY jump is the known plane stratum (nullity 30 at pure x₁₆); **no
  real nullity-14 point exists there** — consistent, and now a fact, not an absence.
  > **CORRECTED 2026-11-11 (the audit's finding E5; main).** The scan did not show this. Its golden-section step sits
  > under `if not found:`, the 120-point grid always finds the plane stratum, and so the refinement never ran. A
  > 120-point grid cannot exclude a point between its nodes, and "now a fact" was too strong for it. **What does show
  > it** is `verification/walls_on_the_line.py`: s₁, x₁₄, x₁₆ and x₂₂ commute and diagonalise together, so the joint
  > nullity at every point of the line, real or complex, is read off their joint weights. On z(s₁), of dimension 46,
  > 12 weights vanish on x₁₄ and x₁₆ (the generic nullity) and 30 on x₁₆ (the plane stratum). The nullity jumps at
  > finite t only at four points, all purely imaginary: 14 at t = ±0.0515261607 i and 18 at t = ±0.0464130116 i, in
  > the normalisation y = x₁₄ + t x₁₆ of B854's invariants. **So on the real line the nullity is 12 at every point but
  > pure x₁₆.** A direct rank computation agrees at the four walls, beside them, and at six real points. It also
  > verifies on main the mechanism B874's addendum records as the solo seat's: the 34 active weights fall into seven
  > proportionality classes of sizes 2, 2, 6, 6, 6, 6, 6, three real and four in two conjugate pairs. Main's first
  > attempt at a mend, a finer scan with a bound between grid points, failed its own checks: the matrices are scaled
  > over fourteen orders of magnitude, and a scan is the wrong instrument here.
  >
  > **Dated note, 2026-11-11, later: the advisor seat's sixth re-audit accepts this mend, and main ran what it noted.**
  > - **Accepted.** The seat computed the claim again by another route: the six brackets of the four elements vanish
  >   exactly over the rationals; the counts 30 and 12 are exact ranks; at 60 digits one basis diagonalises all four to
  >   9e-41; the four walls are main's to 40 digits; a control finds a real wall where one is known.
  > - **The other two roots.** Main's instrument took s₁ at the smallest of the cubic's three real roots, and the
  >   structure paper's skeleton says the same of all three. Whether a wall is real has to be computed at each. Main ran
  >   its instrument at all three (`verification/walls_at_the_three_roots.py`, expectations written first, not blind):
  >   at each root the counts are 46, 30 and 12 and the finite walls are four purely imaginary points, ±0.0464130116 i
  >   and ±0.0515261607 i; ±0.0339621153 i and ±0.0304159681 i; ±0.0057855638 i and ±0.2158521452 i (nullity 18 and 14
  >   in each pair). They are the seat's values to nine digits. **So at no Galois root is there a real point of nullity
  >   14 on the line.**
  > - **Figures that are not the same from run to run.** The landing's message and the script's header quoted a
  >   condition number of 12 and an off-diagonal part of 3.5e-14; the run first committed printed 30.8 and 2.1e-14. Main
  >   ran the file twice more on the same machine: once it gave the committed figures byte for byte, once the others.
  >   Inside an eigenspace of dimension above one the basis is the solver's choice. Nothing rests on those figures; the
  >   counts and the walls, to nine digits, are what the lock holds. The run committed now is the last one made.
  > - **The slow lane.** Three of the lock's four first tests read the committed run; the recomputation is in the slow
  >   lane, where it took about 80 seconds on main's machine and 38 on the seat's. It stays there, and the lock says so.
- Reading, fenced: the second measurement's charge lives in the complexification; its real
  avatar belongs to the compact-direction story (layer 8) — connecting the SMT directly to
  W7's signature question. Whether a real wall point exists elsewhere in C: open.

## 3. THE B874 AMENDMENT (this seat's own correction, logged)

B874's addendum claimed *"the complete ladder is {78, 46, 30, 12}; the torus does not supply
the step-2 charge."* **The second clause was an overgeneralization and is corrected**: the
coordinate-direction tests (x₁₄, x₂₂ → 12) were right in scope, but the torus's *algebraic*
wall point y* supplies exactly the step-2 charge and lands on the SM. The within-C ladder
includes **{18, 14}** (their §XXI strata; 14 verified here). What survives of B874's negative:
SU(5)×U(1) (26) is still not reached by these charges — **the second measurement skips SU(5)
over ℝ** *(scope added 2026-08-18: over the algebraic closure the 26/A₄ stratum is attained at
four non-real points; the skip is a reality phenomenon — see B874's 2026-08-18 addendum)*;
the fused principle's step-2 role reduces to naming the wall. Correction credited to the solo
seat's evidence-first relay; B874's FINDINGS gains a pointer to this arc.

## 4. Also verified this session (the S1 queue advancing)

- **The hypercharge fit reproduces on this build** (hyper.py): rank 3 for exactly the
  conjugation pair of assignments; the 14 mixed assignments fail at rank 4 (exact direction).
- **The across-breakings suite verifies here too**: G₂₀ closes in one round (dim 20,
  derived 19 with derived² = 19, center 1, generic-C centralizer 12) ⟹ su(3)_c ⊕ su(3)′ ⊕
  su(2)′ ⊕ u(1) by their color-ideal argument; and the commutation-law scan reproduces the
  **ℤ₂ obstruction** exactly (the s_is_j = c_ij pattern with ∏c = −1 across the
  configurations — no configuration lets all three perspectives commute).
- Cross-confirmations already in hand: their 11-term texture = B884's 11 cells; their
  wall-route family table = B876's grading; their two-cubics note = B886/B888; their floor
  = B874's Cent(C), third way.

`tests/test_b892_smt.py`
