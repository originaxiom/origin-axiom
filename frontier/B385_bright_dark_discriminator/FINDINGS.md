# B385 — T1 BANKED: both cheap layers KILLED — the discriminator is character-level

**Status: T1 kill banked (twice over); the character-level continuation derived and named.
Pre-registration: PREREGISTRATION.md (committed first). Firewalled.**

## Kill 1 (the registered bet): darkness is NOT γ-group-theoretic

The full invariant table of G = ⟨γ_{m₁}, γ_{m₂}⟩ ≤ SL(2,ℤ/15) (orders, CRT images, −I
membership, det-class multisets, trace sets mod 5) separates NOTHING: bright (2,3) and dark
(1,3) have IDENTICAL profiles (|G₁₅|=480, |G₃|=4, |G₅|=120, −I ∈ both, same traces). No
tabulated invariant is disjoint across the 12 pairs (group_hunt.json).

## Kill 2 (the word-map layer): the (j,l)-grid det-class distribution fails on the riddle pair

Per-pair det-class counts over the word grid (ords: W₁:20, W₂:12, W₃:6, W₄:20, W₅:4, W₇:12):
**(3,4) bright and (1,3) dark have the SAME distribution {1: 63, 3: 21, 5: 27, 15: 9}/120** —
the riddle pair defeats word statistics too (class_counts.json). Corollary worth keeping:
(1,2) and (2,4) share {142, 26, 68, 4}/240 — the B382 class profile is a two-pair profile.

## The derived next layer (named, not yet run)

`D·C⁻¹ = Z^{−8}` EXACTLY (diag ζ^{j(j−1)/2 − 8j²} = diag ζ^{−8j}) — the theta lift is the
canonical lift times a Heisenberg insertion. Hence every theta word factorizes as
(standard lift of γ′) × T(v_word) × phase, with v_word(j,l) the γ-transported accumulation of
(0,−8)-vectors — pure 2-vector arithmetic. By P64, the pair table is then the standard
character times ζ^{Q_{γ′}(v_word)}: **the bright/dark difference must live in the word-shift
map v_word — the twist's accumulated characteristic — not in γ.** Registered continuation:
compute v_word for the riddle pair, find the invariant of its 5-part that separates, then
verify on all 12.

**Provenance.** group_hunt.py, class_counts.py (seconds each); locks
tests/test_b385_discriminator.py.

---

# T2-partial BANKED: the v_word map SEES the riddle — first layer that separates

The accumulated word-shift map v_word(j,l) (from the derived factorization
W-word = U_std(γ′)·T(v_word)·phase, with insertions X⁻⁸ per WR_c-step and Z⁻⁸ per C-step;
γ-sanity verified for all six seeds): the 5-part support profiles across all 12 pairs give

- scalar stats FAIL (support sizes bright {6,12,18,20} vs dark {6,10,18,22} overlap;
  zero-cell counts overlap) — consistent with the two banked kills;
- **the support SETS are disjoint bright-vs-dark (no collision), and the riddle pair
  separates for the first time: (3,4) has 12 support vectors, (1,3) has 18, different sets**
  (vword.json). Adjacent hint: (2,7)-bright and (3,5)-dark share the symmetric core
  {(0,0),(1,3),(3,1),(4,4)} and differ by coordinate-SWAPPED extras ((0,3),(4,1) vs
  (3,0),(1,4)) — a reflection-parity flavor, not yet a criterion.

**Registered next step:** the systematic property scan on the banked supports (swap-closure,
negation, QR-multiplier orbits, ω-pairing multisets, joint (γ′, v_word) anti-content) to
extract the STATED criterion; then re-verify 12/12 + the out-of-sample prediction.

---

# T2b BANKED: darkness is SPECTRUM-cancellation, not cell-vanishing (+ 3 scan nulls)

**The correction (exhibit: the riddle pair, exact).** The dark pair (1,3) has **44/120
anti-carrying raw cells — the same count as bright (3,4)**. Dark ≠ anti-free cells; dark =
every DFT window kills a nonzero anti-table (the H-average does not commute with ζ-multiplication,
so cell-level anti-content coexists with a fully real projected t-table). This is the P65
row-16 mechanism at whole-pair scale — darkness is a complete spectral null of the anti-table.

**Scan nulls (3, banked):** closure properties (swap/neg/dbl/swap-neg) all fail on all 12
supports; diagonal and antidiagonal contents overlap across bright/dark ((2,4)-bright shares
its full diagonal with dark pairs); scalar stats already dead (T2-partial).

**Label-exclusion data (riddle):** bright (3,4)'s anti-cells occupy 12 joint labels
(cls, v_word mod 5); the dark grid visits 8 of them; **4 labels are bright-exclusive:
(1,(0,2)), (1,(2,1)), (1,(2,3)), (1,(4,2))** — all with a ±2 coordinate; with v₃ refinement,
all bright-exclusive labels have v₃ ∈ {(1,0),(1,2)} (anti_correlation.json).

**The named next question (the criterion's true form):** prove the window-cancellation
identity for dark pairs — why every ζ-window annihilates (1,3)'s 44-cell anti-table (the
per-pair analog of the P65 ζ₅-spectrum argument). The criterion, once stated, is a property
of the (γ′, v_word)-labelled character sums, not of any support set alone.
