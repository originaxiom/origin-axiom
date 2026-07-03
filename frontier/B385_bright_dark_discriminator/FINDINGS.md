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
