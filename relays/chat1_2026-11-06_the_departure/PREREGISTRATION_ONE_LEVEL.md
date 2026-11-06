# ONE PROCESS, ONE LEVEL — pre-registration (the web seat, 2026-11-06)

**For:** the owner's goal, with the scale kept. The owner, 08:21: "we should seek it." This answers P-721's lead
("which conductor the 4D couplings are heard at — a criterion in object terms … stated before any value") and
P-719's ("state a level-fixing principle in object terms (data-free)").

**Kind:** data-free. SL(2, ℤ/N) arithmetic only.
- **Firewall (P-719, P-721, P-722):** no scale ratio and no coupling value is computed from any level, here or in the
  check. No held-out quantity appears, and nothing is compared with data.
- **Written before** `one_level_check.py` is run.

## The principle

**(K) One process, one level.** The goal asks for one process that places τ, the line and the scale. P-719 places the
scale through a level k (Z ∼ exp(i·Vol_ℂ/ℏ), with ħ fixed by k; P-722). So k must be the level at which the same
process places τ and the line.

That process runs as follows:
- **The line** is the golden monodromy's twisted periodic orbit, v ≡ −LR·v (P-718, P-721). It exists at level N iff
  det(LR + I) = 5 is not a unit mod N.
- **The departure** is the one invisible to the level-N rung (reading (ii)): a single run of n with L^{n−1} ≡ ±I
  mod N, i.e. n = N + 1. Its apex is i(N + √5)/2.
- **The rung is a finite one,** Γ/⟨⟨Tᴺ⟩⟩. P-717's ladder ends at A₅: Γ/⟨⟨Tᴺ⟩⟩ is the (2, 3, N) triangle group,
  finite iff N ≤ 5.

**What follows for P-721's three candidates:**
- **Level 3:** 5 is a unit mod 3, so the dynamics has no nonzero twisted periodic orbit and there is no line. A level-3
  process would place a τ (run 4, apex iφ²) but no line.
- **Level 15:** not a finite rung, since (2, 3, 15) is hyperbolic. Its invisible departure is a run of 16 (apex
  i(15 + √5)/2), which is a different τ from the line's own level.
- **Level 5:** the minimal level holding the line; the last finite rung; the level of the run-6 departure and τ*₆.

**So (K) gives k = 5.** The map from k to ħ, and to any ratio, is P-722's convention, and is to be fixed by main before
any value.

## Predictions for the check (hand-derived)

- **Twisted fixed points** (LR + I)v ≡ 0 mod N, nonzero:
  - N = 2: 0;
  - N = 3: 0;
  - N = 4: 0;
  - N = 5: 4 (the pair);
  - N = 15: 4, the same pair, embedded by v ↦ 3v.
- **Untwisted ones** (LR − I)v ≡ 0: none at any N.
- **The order of LR in PSL(2, ℤ/N):**
  - N = 2: 3;
  - N = 3: 2 (LR² ≡ −I mod 3);
  - N = 4: 3 (LR³ ≡ I mod 4);
  - N = 5: 5;
  - N = 15: 20 (the signs mod 3 and mod 5 agree first at 20).
- **The minimal single-run departure invisible at level N:** n = N + 1. A run of n is invisible iff N ∣ n − 1. Apex
  Im (N + √5)/2.
- **|PSL(2, ℤ/N)| for N = 2, 3, 4, 5:** 6, 12, 24, 60, equal to the (2, 3, N) triangle groups.
  - The classical fact that ⟨⟨Tᴺ⟩⟩ = Γ(N) for N ≤ 5, and has infinite index for N ≥ 6, is cited, not computed.

**What would refute:** a nonzero twisted fixed point at N = 3; a different invisible run at N = 5 or 15; or the pair
failing to embed at N = 15.

0 of 19.
