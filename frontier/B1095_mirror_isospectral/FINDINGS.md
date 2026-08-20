# B1095 — THE MIRROR-ISOSPECTRAL SPLIT: the two hands share their spectrum exactly, and the hand is only WHERE states live (both audit-seat checks answered)

**Date:** 2026-08-20 · **Verdict: PROVED (own-code exact/machine-precision computation; answers the audit seat's two B1085 checks; corrects B1085's and B1091's phrasing at the named rows)**
**Trigger:** the audit seat's two questions (the one-state question; the gap-labeling
differential) — both flagged as questions-not-defects, both requiring in-sandbox
computation only. Both computed here; both answers are sharper than either reading
the questions anticipated.

## 1. THE MAIN FINDING: exact isospectrality at reversal-closed windows

At the cut phase ρ = α, for window sizes N = F₁₆ = 987 and F₁₈ = 2584 (even Fibonacci
index): **the left hand's word is EXACTLY the reversal of the right hand's word**
(letter-for-letter, verified), so the two half-line Hamiltonians are conjugate by the
exchange matrix (J·H_R·J = H_L) and **the spectra coincide to machine precision — max
difference 1.3×10⁻¹⁵ across all 2584 eigenvalues.** The hand is not "IDS-blind to ≤1
state": at these windows it is spectrally INVISIBLE — exactly zero.

At N = F₁₇ = 1597 and F₁₉ = 4181 (odd index), the reversal identity fails at exactly
the TWO cut-adjacent letters, and isospectrality breaks macroscopically (max spectral
difference 0.147). **The Fibonacci-index parity decides whether the palindrome closes
around the cut — the tick-parity (Breath ℤ/2, B1083's M vs M²) surfacing at the
spectral level.**

## 2. The answer to the one-state question (the audit seat's check 2)

Sharper than either alternative offered. At reversal-closed windows, **all eleven
boundary-capable energies are SHARED between the hands** (every left edge energy is a
right bulk eigenvalue and vice versa, at ≤ 1.3×10⁻¹⁵), and the hands localize them
COMPLEMENTARILY: the right hand binds five to the cut, the left hand binds the other
six. **The 6 − 5 = 1 is a parity remainder: a shared family of ODD size cannot split
evenly.** So: not "the same one state" (no single state carries the difference), and
not "independent" either — an eleven-state shared family with a hand-dependent
complementary split. The "density vs count" reading is the right direction, and the
exact statement is stronger: **the energies are P-invariant (forced); the localization
is P-equivariant (free).** The origin torsor's P-bit (B1083: reversal = parity, not
arrow) is physically realized as WHICH shared states bind — the forced/free ontology
instantiated in one computation.

## 3. The answer to the gap-labeling differential (the audit seat's check 1)

- **Gap labeling VERIFIED on this bench**: every spectral gap's IDS plateau equals
  frac(m·α) to ~10⁻⁴ (finite-size) with integer labels m ∈ [−12, 12]; every edge state
  sits in a labeled gap (right hand: m ∈ {+1,+2,+3,+4,+6}; left hand: m ∈
  {−5,−2,+1,+4,−3,+5}-family, per the banked energies).
- **The counts are STANDARD pumping content IN KIND, and the sweep is honest about
  its own detector**: the 144-point ρ-sweep shows strongly ρ-dependent edge counts
  (pumping — the standard picture), and the (5,6) pair occurs at seven OTHER grid
  points besides α — **the pair is not golden-unique**, which is the modest form of
  the B724 defusal this sweep supports. What the sweep does NOT cleanly certify is
  the fine window structure: the 0.5-boundary-weight detector is volatile near
  transitions (a grid point 2×10⁻⁵ from α reads (5,9) while α reads (5,6) — states
  mid-pump carry intermediate localization and flip a global threshold). A per-gap
  occupancy detector (gap-interior energy + localization length) is the named
  instrument upgrade before any window-measure claim. Sweep record in the arc dir.
- **THE DIFFERENTIAL, stated**: what gap labeling + bulk–boundary FORCE is the per-gap
  occupancy windows — they speak per gap, per hand. **What they do NOT speak of is the
  cross-hand structure: the exact mirror-isospectrality at reversal-closed windows, the
  complementary split of one shared odd family, and its Fibonacci-parity breaking.**
  That layer is B1085's honest headline after this arc; the 5-vs-6 counts are its
  standard-physics shadow. B1085's FINDINGS and B1091's card row are corrected
  accordingly (same bank).

## 4. Corrections applied (dated, in place)

- **B1085**: the phrase "the free half is edge-observable, and ONLY edge-observable"
  gains its precise form: *the free half is spectrally invisible (exactly, at
  reversal-closed windows) and localization-visible at the cut; the counts are
  standard bulk–boundary content; the novel layer is the mirror-isospectral
  complementary split.* Gap-labeling context added (the grep the audit seat ran now
  finds it).
- **B1091**: the hand row now reads "spectrally invisible, localization-visible" in
  place of the count-blindness phrasing, and cites this arc.
- **L173**: the prereg spec's first paragraph now REQUIRES the gap-labeling
  differential before any comparison (the audit seat's warning, adopted verbatim as
  discipline).

**Locks:** tests/test_b1095_mirror_isospectral.py — the reversal identity at N = 987
(exact), isospectrality ≤ 10⁻¹² at N = 987, the reversal failure at N = 1597 sites
{0,1}, the eleven-energy cross-appearance, and the odd-family parity statement.
