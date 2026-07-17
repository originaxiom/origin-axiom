# B657 — THE INVARIANT-LINE CAMPAIGN: cc2's packet verified and banked
# (main seat, 2026-07-17; packet seals 8/8; W0a/W0b/W2a reproduced on
# this machine; W1's sealed matrix re-derived independently)

cc2's corrected probe of what a relay had mislabeled "the dark sector"
(prereg 9d8aa8ff, sealed with hard gates and outcome vocabularies
before compute; W1 addendum sealed before the portal run). Verdicts:

## W0a — CONFLATION-REFUTED (reproduced bit-identically here)

The holonomy-invariant line v₀ of the 27 (joint nullspace, hard gate
dim = 1 = the banked h⁰) is **NOT the Spin(10) gauge singlet**:
- v₀ is supported on exactly THREE weights with coefficients (1, −1, 1),
  all h_pr-null (h_pr·v₀ = 0 exact);
- both valid Spin(10)×U(1) branchings (nodes 1 and 6; multiplicities
  16/10/1, charge ratio 1:−2:4) put the GUT singlet at the E₆
  highest/lowest weight — h_pr eigenvalue **±16**, the extreme of the
  principal grading;
- v₀'s coefficient at the singlet weight: **exactly zero**, both
  branchings.

The relayed "h⁰ section = gauge singlet = dark matter candidate" was a
conflation of two decompositions of the 27 (GUT branching vs principal
SL(2)). The label never entered the repo; it dies here in the packet.
House name: **THE INVARIANT LINE.** This seat's reproduction: the
patched script run on the banked B575 apparatus produces a
**bit-identical w0a_v0.json**.

## W0b — ONE-PER-BLOCK (reproduced identically here, up to runtime)

27 = V17 ⊕ V9 ⊕ V1 under the holonomy — **exactly block-diagonal** —
and the per-block cohomology is (h⁰, h¹) = (0,1) / (0,1) / (1,1):
sums reproduce the banked (1, 3); the V1 (trivial) block's h¹ = b₁ = 1,
so **the invariant-line H¹ class IS the Betti class**, and each
principal block carries exactly one H¹ class. This upgrades the
dimension-grammar mechanism candidate (the principal-sl₂ blocks drive
the count) from a numerology to a computed refinement — and it is the
block-level face of B656/G5's (i₁, i₂) reduction. Reproduction:
w0b_blocks.json identical except the runtime field.

## W1 — THE PORTAL IS A SECTOR-RESPECTING RANK-5 ISOMORPHISM

P(u) = [v₀ × u] (Jordan cross product 27 ⊗ 27 → 27̄, the banked cubic's
polarization; ρ-invariance a hard gate): **P: H¹(D; 27) → H¹(D; 27̄)
has rank 5, kernel 0** — an isomorphism — and is **exactly
block-diagonal** on B637's boundary-born {0,1} / solo-inherited
{2,3,4} split: an invertible upper-triangular 2×2 boundary block and
an antidiagonal-type 3×3 solo block with corners (1, −2) and middle
−15/11. ZERO-PORTAL is refuted: the invariant line couples to the
entire cohomology, bijectively, without mixing the sectors.

This seat's verification: the sealed portal_matrix.json re-derived
with independent exact linear algebra (verify_w1_matrix.py — rank,
det ≠ 0, the zero blocks, the quoted entries: all confirmed). The
portal PIPELINE's end-to-end independent run on this machine is the
silver control below (their pkl cache is seat-local; the golden
pipeline rerun is priced, not claimed — their own verify-note states
the same deviation).

## W2a — THE SILVER CONTROL: FORM-MATCH DEEP (re-run end-to-end here)

19/19 hard gates, exact in L = ℚ(s, i):
- the 3/5/1 grammar reproduces; the one-per-block table reproduces
  **entry for entry** ((0,1)/(0,1)/(1,1) on block dims 17/9/1);
- **v₀_silver has the SAME shape as golden's invariant line — three
  basis terms, coefficients (1, −1, 1), all h_pr-null** (the invariant
  line's form proposes as metallic-universal; NOTICED, two objects);
- the portal is again a **rank-5 isomorphism with kernel 0**.

FORM-MISMATCH, flagged honestly (adopted as flagged): golden's portal
is block-diagonal on the boundary/solo split; silver's is exactly
upper-triangular with no analogous zero block — but the silver class
basis has no canonical alignment with golden's provenance labels, so
the mismatch may be basis choice. Consequence (theirs, adopted): the
ISOMORPHISM property proposes as FORCED (two objects, two fields);
the SECTOR-RESPECTING property does NOT (yet) — deciding needs a
canonical boundary-restriction decomposition on the silver double
(priced, one cell → L102).

## W2b — the repair note (relayed onward)

The packet includes REPAIR_NOTE_CHAT1.md for the originating seat:
what their instinct got right (one-per-block, the portal's reality),
the identification that died (W0a), the two category errors (stage vs
classical — the B650 equivariance wall), and their "dark ladder"
redirected to the banked mirror/sector laws. The design-adversary lane
(L99's spirit) working as adopted post-JUNO.

## Grammar-row adjudication (their proposals, this seat's verdicts)

- **The portal-isomorphism law** — BANKED as LAW (two objects, exact;
  FORCED-candidate pending a third object).
- **The one-per-block refinement** — BANKED as LAW (two objects,
  exact; the mechanism face of the dimension grammar's reduction).
- **v₀'s universal (1, −1, 1) h_pr-null shape** — NOTICED (two
  objects; no mechanism yet).
- **The block-structure question** (sector-respecting: geometry or
  basis?) — OPEN, priced as L102.

## Ledger deltas

LAW_MAP: the portal law row (new); the dimension-grammar row gains the
one-per-block refinement. OPEN_LEADS: L102 opened (the canonical
silver decomposition). Locks: tests/test_b657_invariant_line.py (4).
Privacy patches + originals' hashes: ORIGINALS_MANIFEST.txt.
Reproduction artifacts: verify_w1_matrix.py + verify_w1_out.txt;
reproduction evidence quoted above (w0a bit-identical; w0b identical
mod runtime; w2a re-run — see rerun_notes.txt).
