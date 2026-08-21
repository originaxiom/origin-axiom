# B1114 verification bench — LORENTZ ON THE DOUBLE

Verifies `breakthrough_memos/LORENTZ_ON_THE_DOUBLE.md` (outside bench, 2026-08-21) with
fresh, own-authored code against the same e6 Chevalley basis B1098/B1102 use. All work
in `b1114_staging/`; the repo was read-only throughout. Script: `b1114_verify.py`.
Machine results: `b1114_results.json`. Runtime: **5.8s**, all four layers **CONFIRMED**.

## Overall verdict: CONFIRMED

Joint centralizer is exactly 8-dimensional, center 0, rank 2 → the unique rank-2
dim-8 semisimple type, A2 = su(3). The bi-weight multiset matches the memo's claim
exactly. The control (B1098's dim_c = 16) reproduces. One caveat is flagged below
(a mis-sourced citation inside the memo, not a wrong number and not a wrong
conclusion — see "the 36 note").

## The A2+A2 subsystem construction (the canonical method, own re-implementation)

1. Load the stored hatch triple (`frontier/B1098_nonabelian_hatch/b1098_a2_triple.json`,
   `dim_c: 16`). Verify `[X,Y]=H`, `[H,X]=2X`, `[H,Y]=-2Y` exactly, then *identify* (not
   assume) which simple roots it sits on by direct search: `X = e_{α0} + e_{α2}` —
   confirms it is B1098's `Levi(0,2)-regular`, matching B1102's own provenance chase.
2. **CONTROL** (required before trusting anything downstream): compute
   `z_e6(X,H,Y)` as the exact nullspace of the stacked 234×78 `ad`-matrix, own code,
   independent of B1098's/B1102's centralizer routines. Got **16**, matching the stored
   `dim_c` and B1098's `a2+a2` table row. Cross-checked mod two large primes
   (1000003, 1000033) both ways throughout the script, not just here.
3. Roots orthogonal to the A2 (i.e. orthogonal to both `α0` and `α2` under the exact
   root inner product `ip`): **12**, exactly as claimed. Split into connected components
   under "linked iff `ip(r,s)≠0`": **[6, 6]**, with the two components mutually
   orthogonal on *all* 36 cross pairs (not just the adjacency-derived ones — checked
   directly). This is the A2+A2 subsystem.
4. Each 6-root component + the two coroots of a "simple pair" within it (`ip(r1,r2)=-1`,
   `r1+r2` also in the component) gives an 8-dimensional ideal: **I1** (simple pair
   `(0,0,0,0,-1,-1),(0,0,0,0,0,1)`) and **I2** (simple pair
   `(-1,-2,-2,-3,-2,-1),(0,1,0,0,0,0)`). Both dimension 8 (rank of the spanning set,
   not assumed). `[I1,I2]=0` on all 64 cross pairs; both commute with the *stored* hatch
   triple element-wise (9 brackets zero, not just "being in the nullspace").
5. `rank(I1 ∪ I2) = 16`, which — combined with both being independently confirmed
   inside the nullspace-computed centralizer — proves `I1 ⊕ I2 = z_e6(hatch triple)`
   exactly. This is the CONTROL closing the loop: two independently-built objects
   (brute-force nullspace vs. root-orthogonality) agree on the nose.
6. I1's own principal (regular) nilpotent `e2 = e_{r1}+e_{r2}` (its own simple pair) is
   solved into a full JM triple `(e2,h2,f2)` by the same general `ad²`-solve method
   B1098 uses (ported fresh, own implementation, with the same kernel-correction
   fallback — not needed on this run). Exact triple relations verified; commutes with
   the stored hatch triple on all 9 brackets.
7. **Same-class check, done the way B1098 actually keys classes** (dim of the reductive
   triple-centralizer + the exact ad(h) eigenvalue multiset over all 78 dimensions),
   not by eyeballing a single number: `dim z_e6(e2,h2,f2) = 16` (matches), and
   `ad(H)`'s spectrum equals `ad(h2)`'s spectrum exactly (both: eigenvalue `-4` ×1,
   `-2` ×20, `0` ×36, `2` ×20, `4` ×1, summing to 78 — counted precisely from the run
   log). Both match → same class by B1098's own invariant, independently reproduced.
8. **Layer 2d, the crux.** `z_e6(X,H,Y,e2,h2,f2)` (six stacked `ad`-matrices, own
   nullspace code, mod-p cross-checked): **dimension 8**. A structural theorem confirms
   this *must* equal I2 exactly, independent of the nullspace computation: the reductive
   centralizer of a simple algebra's own *principal* sl2, taken *within that algebra*, is
   always trivial (0-dimensional — the standard fact that also shows up as B1098's own
   `Levi(0,1,2,3,4,5)-regular` [principal of the whole e6] row having `dim_c=0`). Since
   I1 and I2 commute entirely, `z_{I1⊕I2}(I1's triple) = z_{I1}(triple) ⊕ z_{I2}(triple)
   = 0 ⊕ I2 = I2`. Checked computationally: `rank(joint_basis ∪ I2_basis) = 8`, proving
   the two independently-derived 8-dimensional spaces coincide exactly. The joint
   centralizer closes under bracket (28/28 pairs land back in span), has center
   dimension **0**, and reductive rank **2** (generic-element method, 6 trials, min) —
   dim 8 + center 0 + rank 2 has exactly one solution among simple Lie algebras: **A2 =
   su(3)**. So `E6 ⊇ (I1's triple) ⊕ (hatch's triple) ⊕ su(3)`, realified:
   `so(3,1) ⊕ su(3)`.

## The failed-method-avoided note

`lorentz_double2_out.txt` (kept for the error ledger, not reproduced) took a different
route: rather than building I1/I2 directly from root-system orthogonality, it appears to
have primary-decomposed a *generic element* of the already-computed 16-dim centralizer
(no synthetic pre-flight validation, unlike B1102's later, validated `split_ideals`).
Its printed numbers are internally inconsistent and were not caught in that run:
`components: 4 6 6` (three pieces, not the correct two — a spurious extra split) and
`ideal dims after closure: 8 9`, which **sum to 17, exceeding the known-correct total of
16** — the "closure" step leaked outside the centralizer entirely. That inconsistency
(`rank(I1)=1, rank(I2)=3` instead of `2,2` — no valid rank-1 or rank-3-with-dim-9 simple
factor of this shape exists as a clean sl3 pair) would have been caught immediately by
the `rank(I1 ∪ I2) == 16` cross-check this bench runs as a matter of course (step 5
above). The canonical method (root-orthogonality, this memo's and this bench's) sidesteps
the fragility of generic-element primary decomposition entirely by building I1, I2 from
root-system combinatorics that are exact and checkable at every step.

## Layer-by-layer verdicts

- **Layer 1 (the one-line lemma):** CONFIRMED. Real form `g0` of complex `g` contains no
  nonzero complex subalgebra — one line: a complex subspace `s ⊆ g0` satisfies `s = i·s
  ⊆ g0 ∩ i·g0 = 0`. **Fence, stated plainly:** the *density* premise (the object's
  hyperbolic holonomy is Zariski-dense in `SL(2,C)`, `tr[A,B] = 3/2+(√3/2)i ≠ 2`) is
  CITED from B1086/B1098 and is **not** re-derived here — it concerns a hyperbolic
  3-manifold representation, outside this Lie-algebra sandbox's data. What this bench
  *does* verify is the piece the lemma consumes: `span_C(X,H,Y)` is confirmed (rank 3,
  exact relations) to be a genuine complex 3-dimensional `sl2(C)` inside `e6(C)` — so
  *given* the cited density, the deduction that no real form of E6 hosts it goes through.
- **Layer 2 (the algebra):** CONFIRMED, including the CONTROL. See above.
- **Layer 3 (signature/rationality):** CONFIRMED. I1, I2 individually have
  all-Fraction (Q-rational) bases; `dim(I1 ∩ I2) = 8+8-16 = 0` (a genuine direct sum).
  The "fixes, doesn't swap" conclusion is then a clean formal argument (given in full in
  the script and JSON), not a further computation: a Q-rational, non-trivial direct-sum
  decomposition cannot be permuted by any automorphism of C/Q, because such an
  automorphism fixes every Q-rational vector pointwise. No explicit "q ↦ 1−q" map needed
  to be constructed to reach this conclusion — rationality of each factor is the whole
  content, and that *is* computed, not assumed.
- **Layer 4 (the 27's bi-weights):** CONFIRMED, exactly (Fraction throughout, no floats
  used anywhere in this layer either — the task's float-rounding allowance was not
  needed). Own crystal-of-ω1 construction of the 27 (27 states, standard minuscule-weight
  BFS), independently certified as a genuine e6-representation on **all 3003** Chevalley
  basis pairs (not a sample). `rho27(H)` and `rho27(h2)` are diagonal (both pure-Cartan
  elements); the bi-weight multiset is
  **`{(±2,±2):1, (±2,0):4, (0,±2):4, (0,0):7}`** on the nose, all bi-weights even.
  **Bonus** (beyond what the task strictly required, using the fact that layer 2d proved
  the joint centralizer *is* I2, so I2's own clean root-derived coroots serve directly as
  the su(3)-color Cartan): within each of the `(±2,0)`/`(0,±2)` blocks there is exactly
  one color-singlet state plus a 3-state color-nonsinglet "triangle"; the four pure
  `(±2,±2)` corners are purely color-singlet; the same 3_c weight-triangle appears
  identically at `h1=+2` and `h1=-2`, the same 3̄_c triangle at `h2=±2`, and the 3_c and
  3̄_c triangles are exact weight-negatives of each other — an exact, computed
  confirmation of the claimed `(1,1)⊗1_c ⊕ (1,0)⊗3_c ⊕ (0,1)⊗3̄_c` decomposition, not
  merely a dimension-count coincidence.

## The one flagged caveat ("the 36 note")

The memo's canonical output (`lorentz_double3_out.txt`) prints `dim z_{e6}(e2) = 36 (A2
class <=> 36)`, and the task brief cites this as "per B1098's dim-c table." **Checked
programmatically**: B1098's own `b1098_results.json` has no `dim_c` entry equal to 36 at
all — its `dim_c` column is the *reductive centralizer of the whole triple* (max value
35, the minimal/A1 orbit's `a5` row), a different invariant from `dim z_g(nilpositive
alone)`. This bench independently computed **both** invariants for **both** X (hatch) and
e2 (I1's principal): the correct B1098-style invariant (`dim_c=16` + the full 78-entry
`ad(h)`-spectrum) matches exactly between the two, which is the properly-sourced
"same-class" proof; **and** `dim z_e6(nilpositive alone)` is 36 for *both* X and e2 (also
matching, a second independent confirmation) — so **36 is a real, correct, verifiable
number**, just attributed to the wrong table in the memo's own citation. This is a
documentation/sourcing slip in the memo, not a computational error and not a wrong
conclusion: the "same nilpotent class" claim it was meant to support holds, confirmed
here by the properly-sourced invariant. Flagged per "report faithfully" rather than
silently corrected or allowed to inflate false doubt about an otherwise-clean CONFIRMED
result.

## Other honest fences

- The I1 / I2 labeling (which of the two size-6 orthogonal components is "the one whose
  principal triple we build") is an arbitrary, immaterial choice — the construction is
  symmetric in the two components; this bench picked `comps[0]` as I1 without loss of
  generality (swapping the labels swaps which factor ends up "double-duty" vs. "the
  joint centralizer," not any verified number).
- Layer 1 and layer 3's *logical* content (the lemma's proof; the no-swap argument) are
  stated as prose arguments resting on computed premises, not as further numerical
  computation — this is the correct division of labor (the task itself frames layer 1
  this way: "it needs no computation, just a correct proof paragraph") and is flagged
  explicitly rather than dressed up as more computation than it is.
- Exactness: every load-bearing number in every layer, including the bonus, is exact
  (Python `Fraction` / `sympy.Rational`, plus modular cross-checks at two large primes
  for every nullspace/rank computation). The task's allowance for float-rounded integer
  weights in layer 4 was not needed — the own-built representation is exact throughout.

## Runtime

5.8s total (rep-certification over all 3003 Chevalley pairs is the dominant cost, ~4.2s;
everything else is sub-second). Comfortably inside the ~3 hour budget.
