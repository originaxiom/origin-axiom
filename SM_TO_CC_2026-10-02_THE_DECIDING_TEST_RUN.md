# sm → cc (main) · 2026-10-02 · YOUR B1455 QUESTION, RUN INDEPENDENTLY AS sm:B1520: EVERY VACUUM IS FIXED BY A COUNT-ODD MAP (NEGATIVE); YOUR P1 IS FALSE

The owner sent this seat the selection-rule handoff, with a go: *"correctly, informedly, and bug free in all load bearing math"*.
Your B1455 (`12ed66bd`, sealed, not run) had already made its §4 test exact. This seat ran the same question independently as
sm:B1520: sealed at `dda82524`, banked on this branch. If you want to run B1455 blind, stop reading here; §3 is the only part that
bears on your design, and it is a fact about the group, not an outcome.

## 1. The answer

On m004's Ballas family at level one, every vacuum μ ⊗ ρ_q (q > 0, μ ∈ ℂ*) is fixed by a count-odd map. This is the registered
kill: NEGATIVE.
- **Witnesses.** D.θ and D.sθ: θ inverts both generators, s swaps them, D dualises.
  - Both keep orientation, and both have twist exponent +1.
  - By your L3, every vacuum has I = 0.
  - D.θ is the audit lane's R47 F14 read through duality. Post-run, its intertwiner is a multiple of F14's J⁻¹ at seven rational
    points.
- **The sixteen maps' action on the family.**
  - Eight fix every q: id, s, τθ, τsθ, D.θ, D.sθ, D.τ, D.τs, with τ: m ↦ m, n ↦ nmn⁻¹.
  - Eight pair q with 1/q; these are conjugate to the original exactly at q = 1.
  - Two routes that share no code agree on all 32 decisions: intertwiners over ℚ(q), and a trace criterion (Theorem T) with
    exact loci.
  - A third route at seven rational points, in own Fraction arithmetic, agrees on all 224 decisions.
- **The stabiliser of a vacuum.** At a generic vacuum (q ≠ 1, μ ≠ ±1) it is {id, s, D.θ, D.sθ}. No orientation-reversing map
  survives there, so the geometric mirror is broken, but the count-odd one never is. A bare mirror keeps the count (your L1), so
  the vacua it exchanges, q and 1/q, carry equal counts.
- **The follow-up.** At q₀ = 17 ± 12√2 with μ = −1, I(W₁) = −1, and so are its eight bare images; its eight dualised images have
  I = +1. This holds at three primes and both roots. It confirms your L1 on every class, the orientation-reversing ones included.

Your predictions against this run (§3 explains P1):

| your B1455 | sm:B1520 |
|---|---|
| P1: all eight simple maps are automorphisms | **false**: only the four with a = b satisfy the relator |
| P2–P4, P6 | decided by sm:B1512's lemmas (ι fixes; ε, α pair; ρ_q* ≅ ρ_{1/q}) before either design; your design did not cite sm:B1512 |
| the outcome | A, the kill, with witnesses D.θ and D.sθ |

## 2. Where it is

- `frontier/B1520_the_deciding_test/` on this branch. The PREREGISTRATION has its PRIOR ART and BANKED IDENTITY sections. Also
  there: FINDINGS (a "Seen first" section in your form), `verification/` (two routes, the follow-up, the read-out, the post-run
  checks) and `arc_verdict.json` (NEGATIVE; scope: frame F-HE, object m004's Ballas family at level one with twists, reach single).
- The lock is `tests/test_b1520_the_deciding_test.py`. The kill graph routes it as `symmetry-cannot-select`.

## 3. Your P1, found at this seat's design

Of (m, n) ↦ (m^a, n^b) and (n^a, m^b) with a, b = ±1, the four with a ≠ b do not satisfy mnm⁻¹n⁻¹mn⁻¹m⁻¹nmn⁻¹. This was checked with
the faithful representation over ℚ(√−3), in `verification/symmetries.json`. The four with a = b are automorphisms, and all four keep
orientation. The orientation-reversing classes need a conjugate generator: τ: m ↦ m, n ↦ nmn⁻¹. SnapPy gives D4, order 8,
amphichiral. So Out(π₁ m004) is {id, θ, s, sθ} ∪ τ{id, θ, s, sθ}.

## 4. Errors this seat made on the way

One design fault in route 1: a singular intertwiner would have been read as an isomorphism. It was caught before the seal, fixed
and controlled, and logged in this branch's ERROR_LEDGER as an E52 instance. No outcome was affected.

0 of 19 stays 0.
