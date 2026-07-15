# B608 — THE ROSETTA TABLE (mixed form): the mixing goes down to the roots

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities —
math-tier subsystem/coset/charge census; the gauge/matter reading stays
firewalled as interpretation. The Listening Campaign's Phase-1 remainder;
gate G1 opens on this bank. Lock `tests/test_b608_rosetta_gsm.py`
(OA_SLOW). Run: `OA_SLOW=1 python3 rosetta_gsm.py`.**

## The declared chain (all nodes computed from the adjacency)

E₆ ⊃ D₅×U(1)₁ (delete endP) ⊃ A₄×U(1)₂ (delete short_end) ⊃
su(3)+su(2)+U(1)_Y (delete branch; su(3) = {midQ, endQ}, su(2) = {midP}).
Every root is labeled by its charge triple q = (n_endP, n_shortend,
n_branch); the q = 0 class splits into su(3)-roots and su(2)-roots.

## The controls (all green, failure-enforcing)

- **C2:** 36 positive roots census exactly into 12 classes; su(3) = 3
  positive roots, su(2) = 1; every charged class has size ∈ {1,2,3,6}
  (color×weak product consistency).
- **C3:** the odd 26 = 12 pair-combos ×2 signs + 2 Cartan. **NINE of the
  twelve pair-combos are CLASS-MIXED at the root level** — the θ-fold
  welds roots from different G_SM classes into single odd directions,
  including one su3-root|su2-root weld and two su3-root|charged-multiplet
  welds. Only three combos are class-pure. (One accounting iteration is
  in the git history: the first C3 draft double-counted pair members.)
- **C1:** every positive-weight θ-even block line expands exactly in the
  θ-even root combinations at its height.

## THE ROSETTA TABLE (the deliverable; full table in the output file)

Per odd-block line, the exact integer coefficients over the pair-combos
with full G_SM class labels. Highlights:
- **V₈'s tips (wt ±16) are class-PURE in q = (1,1,2)** — refining B607's
  (1,1) bicharge purity: the only G_SM-gradable lines in the hearing
  sector sit in a single charged class.
- **The shallowest lines (wt ±2, both blocks) touch the su(3)-root and
  su(2)-root welds directly** — color and weak content enter the hearing
  sector at its lowest principal depth, already mixed.
- Every non-tip line touches ≥ 2 G_SM classes; the middle lines touch
  three.

## What this settles for the campaign

The Rosetta Stone exists only in MIXED form, at three simultaneous
levels: the fold welds G_SM classes into pairs (9/12 mixed), the
principal strings mix the pairs (B604), and the lines mix the bicharges
(B607). Phase 2 (the sealed value extraction) proceeds on the mixed
table per the campaign's stopping rule; any coupling-like functional is
a combination across classes, with the (1,1,2) tips as the unique pure
anchors.
