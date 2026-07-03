# B379 (D3(b) opener / W2.11 core) — the reduction theorem + the closed form: a table becomes one number

**Status: banked (frontier) + P60 promoted at banking (two independent exact computations — the
relayed one and this repo's re-verification, which independently hit and fixed the same
real-subfield trap in its first checker; all locks green). The remaining gap to "the first value
forced by symmetry alone" is now ONE number (the 1/12) plus ONE reality proof (row 16).
Provenance: the owner directed the relayed seat to hunt this target; adjudication and banking
here. Firewalled.**

## T1 — the reduction theorem (verified 13/13 cells, component-exact)

For a cluster a with mult-1 occupancy inside an invariant parity block, the banked pair kernel
is pure eigenframe geometry inside the block:
    t(a,b) = ⟨v_a|u_b⟩⟨u_b|Par|v_a⟩ / (‖v_a‖²‖u_b‖²),
verified against the banked (1,2) table on all four slot cells {6,14}×{2,10} and all nine
3-block cells {0,4,16}×{0,4,8} — including the silent row 16 and the mirror column b = 0 —
with exact ℚ(ζ₆₀) field inversion (the norms live in the larger real subfield; both seats'
first checkers stumbled exactly there, and both caught it). **Corollary, now derived:** the
support pattern — t(a,b) = 0 whenever ζ₁₂^b does not occur in a's block.

## T2 — the closed form (verified exact): one number, two golden faces

With the helicity gradings H₁ = P₊ − P₋, H₂ = Q₊ − Q₋ inside a rigid sector:
    Π_H tr(Par·H₁·H₂) = −(φ/6)·√−3      (slot; components (0,0,−1/12,−1/12))
    Π_H tr(Par·H₁′·H₂′) = +(1/(6φ))·√−3  (3-block; components (0,0,−1/12,+1/12))
— exact σ_√5 Galois conjugates of one another. The cell values follow from the rank-1 sign
pattern: **±1/48 = (±1)·(1/4)·(1/12)** — the 1/4 is the helicity-grid average, the 1/12 the
seam part of the golden-unit constant. Via P57 (Par = J⁻¹·ζ₆⁻¹·XZ) and J acting as a SCALAR on
each rigid block (verified exactly here): each constant is ζ₆⁻¹μ⁻¹·tr(XZ·H₁H₂) — a trace of
the elementary Weyl step against the two gradings.

## Row 16 — the mechanism candidate upgraded (banked-data-exact)

The relayed frame-alignment bet died; the truth found is stronger: **row 16 is ℚ(√5)-dark** —
t(16,0) = (1/24, 1/120, 0, 0), t(16,4) = t(16,8) = (5/48, −1/240, 0, 0): the entire row's
kernel is real-quadratic (verified by direct lookup in the banked exact table). Same darkness
type as pair (1,4), at single-row resolution inside a bright pair; σ₄₉ pairs rows 4 ↔ 16
exactly (4·49 ≡ 16, 16·49 ≡ 4 mod 20) — Galois-partner rows, one bright, one dark.

## The two named residues (the entire remaining W2.11 gap)

1. **Why 1/12** — derive the golden-unit constant's normalization from symmetry (candidate
   mechanisms on record: the Haar(2T×ℤ/2) = 1/48 reading relayed earlier; the Weyl-step trace).
2. **Prove t(16,·) ∈ ℚ(√5)** (the τ₃-invariance of the 16-line pairing); with the banked mirror
   law this completes the row-16 silence as a two-mechanism theorem (Galois reality + mirror).

**Provenance.** The relayed pre-registration + handoff (verified item-by-item; H2/H3 kills
recorded there); P56/P57 (the machinery), the banked step0 tables (the comparison target).
Reproducer: `reduction_verification.py`; locks: `tests/test_b379_selection_rule.py`.
