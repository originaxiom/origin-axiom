# B585 — the listener's law: the two lifts, the two tones, and a refuted mechanism

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; no SM quantities
(the B580 binding rule); firewall intact. Preregistered (PREREGISTRATION.md);
laws verified on held-out levels; the mechanism candidate REFUTED by its own
preregistered prediction. Locks: `tests/test_b585_listener_law.py`.**
Run: `python3 listener_law.py` (pyenv, ~2 min; reuses B238's `su3_data(k)`).

## N1 — the naming theorem (verified, matrix-level, 4 words)

On the stage `S² = −C` (exact); in SL(2,ℤ) `S² = −I`. Hence, exactly:
> `tr(C ρ(W)) = −tr ρ(S²W)` — the C-twist inserts the central element, i.e.
> **the mirror-twisted play is (up to the central sign) the play of the OTHER
> SL(2,ℤ) lift −M of the object's PSL(2,ℤ) monodromy** — the (−A₁)-bundle,
> trace −3, a genuinely different Sol manifold (traces 3 ≠ −3, not conjugate).
The channel identities follow and are verified on RL, RRLL, RRRLLL, RRL:
> `tr_odd = ½(Z(W) + Z(S²W))`, `tr_even = ½(Z(W) − Z(S²W))`.
**The θ-odd (chiral) channel is what the two lifts agree on; the θ-even channel
is the lift-dependence.** (Adjacent banked fact, cited: B279 — τ fixes both spin
structures of the complement; this is the closed-bundle lift bit, a distinct object.)

## K1 — LAW-O, the two-tone law (blind table k=1..12; held-out k=13..17: 5/5 HITS)

For the figure-eight play (RL) on SU(3)_k, κ = k+3, over the full range κ = 4..26:
> **tr_odd(κ) = 1·[4|κ] − (1/φ)·[5|κ], additively.**
The κ=20 collision (first 4|κ ∧ 5|κ) was the sharpest held-out test: predicted
1 − 1/φ = 1/φ², measured +0.381966 = 1/φ². **HIT.** The chiral channel of the
object on the SU(3) tower is a chord of exactly two constant tones: a unit
4-tone and a golden 5-tone of amplitude −1/φ. At κ=5 the 5-tone plays alone —
that is B584's "the golden amplitude is entirely θ-odd."

**LAW-E (the even channel) FAILED its hold-out** (κ=17 predicted 0, measured +1;
κ=18 predicted −1, measured 0). The even channel's law is OPEN — banked as a
guess that died, per the null discipline.

## The clock table (data; no law claimed)

Odd-block clock orders k=1..12: `1, 10, 12, 8, 12, 36, 60, 20, 12, 28, 24, 60`.
No simple function of κ found (honest). **L77's 60 surfaces**: the golden-voiced
stages beyond κ=5 (κ=10, 15) both tick at order 60; the pure-golden stage κ=5
ticks at 10. Curiosity recorded, not claimed: at κ=11 the odd-block eigenvalue
denominators are {4,5,20} — the stage's own κ never appears.

## M1 — the mechanism candidate REFUTED (its own preregistered prediction)

The candidate: "5|κ" = `√5 ∈ ℚ(ζ_κ)` — the tone fires when the stage's field
contains the WORD'S trace field. Preregistered consequence: silver RRLL
(ℚ(√2)) fires iff 8|κ; bronze RRRLLL (ℚ(√13)) iff 13|κ; RRL (ℚ(√3)) iff 12|κ.
**Measured (κ = 4..26): REFUTED.**
- silver fires on multiples of {4, 5, 7} (e.g. κ=10: +1 with 8∤10; κ=16 value
  −1.8284 = non-constant), not on an 8-locus;
- bronze fires at κ ∈ {5,15,25} but is SILENT at κ=10 — tones interfere
  destructively; its values on the 5-multiples are non-constant (+1, +2, −1);
- 13|κ does fire for bronze (13, 26) but as one voice among many (11, 19, 6, 7…).
So field containment as stated is dead. What survives: **only the figure-eight
has the clean constant two-tone additive law** — the golden/minimal word is
special again (cf. B238's level-rank coincidence, B233/B234). The true mechanism
(likely a signed fixed-point count of ±W on the level-κ weight torus mod Weyl)
is registered as **L82**.

## Reading (firewalled)

The listener's law, as far as it is proven: chirality is lift-agreement — the
θ-odd voice is the part of the play on which the two SL(2,ℤ) lifts of the
object's monodromy cannot disagree. On the SU(3) tower the object's chiral
voice is a two-tone chord (4-tone, golden 5-tone) with exact additivity, and
that clean law is figure-eight-specific: heavier words splinter into
interfering, non-constant tones. The stage's arithmetic (κ) gates which tones
sound; the object's word decides whether the chord is clean.

## Gates and discipline

k=2 reproduces B584 exactly (tr_even = 0, tr_odd = −1/φ, clock 10); modular
gate green at every k used; C central at every k; N1 identities exact at 1e-9.
Blind/hold-out protocol followed; the failed LAW-E and the refuted M1 mechanism
are banked as negatives with their discriminating facts in-sandbox. MB13 sweep
in PREREGISTRATION.md.

## Anchors

B584 (Round 3), B238 (stage + su3_data(k)), B570-C3/B569 (E₆ rows), B279
(complement spin bit), L77 (the 60), B233/B234/B238 (golden-is-special), L81
(parent lead), L82 (the fixed-point mechanism, new).
