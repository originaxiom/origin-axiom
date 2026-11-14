# B1926 — At an odd number of ticks the class-index frame's matter exists only twisted by the orientation: the tick inverts the scar

**Verdict: PROVED** (a short proof; main's own Fox-calculus computation on the tick's levels 1 to 8; the web seat's
sealed run of W-C8 part 2a, computed independently, agrees on every count). cc (main), 2026-11-14 (S306p). Data-free;
exact arithmetic over a prime field. Nothing is measured, and no count is given a physical meaning. **0 of 19.**

## 1. The answer first

- **The question** (register row P-846; the author: compute the one object the selection rule picks that no frame had
  computed). The web seat built the Gieseking manifold m000 from its tick and ran it, with the tick's levels, in the
  free-cusp and class-index frames (W-C8 part 2a, sealed, `73a60b519` and `e37753fd7`).
  - **The free-cusp frame:** every level n = 1 to 8 has b₁ = 1 and cusp rank 1. Each is closed, like m004.
  - **The class-index frame:** at the odd levels (1, 3, 5, 7), which are non-orientable, there are fibre-torsion
    characters (3, 10 and 28 of them at levels 3, 5 and 7) but **no sector module at all**. At the even levels there are
    sector modules (12, 210 and 1 892 at levels 4, 6 and 8).
- **Why, in general (main's proof).** At level n the bundle group is G_n = ⟨a, b, t ∣ t x t⁻¹ = σⁿ(x)⟩, with σ the
  tick (a ↦ ab, b ↦ a; abelianisation LP, det −1).
  - σ sends the scar λ = [a, b] to a conjugate of λ⁻¹: σ(λ) = a λ⁻¹ a⁻¹. So σⁿ(λ) = g λ^((−1)ⁿ) g⁻¹, and the meridian
    μ = g⁻¹t satisfies μ λ μ⁻¹ = λ^((−1)ⁿ). The cusp is a torus for even n and a Klein bottle for odd n.
  - Take a character l with l(μ) = 1 (the record's fibre-torsion characters are so defined, B1438) and a cocycle c,
    so that c(xy) = c(x) + l(x) c(y). Since l(λ) = 1, c(μ λ μ⁻¹) = c(λ), while c(λ⁻¹) = −c(λ).
  - **So at odd n, c(λ) = −c(λ), and c(λ) = 0 for every such class** (in characteristic ≠ 2). A sector module
    V(l, α) needs a class normalised by c(λ) = 1 (B1438), and so **none exists on any non-orientable bundle**. This
    holds for every determinant −1 act, not only the golden tick.
  - **The other half:** for a character with l(μ) = −1, the fibre characters times the orientation character w
    (w(t) = −1, w = 1 on the fibre), the same algebra gives c(λ) = c(λ) with no constraint. So the twisted classes are
    free to be non-zero on the scar. They give non-split modules [[α, cβ], [0, β]] whose diagonal characters differ
    by the orientation character, α/β = l·w. These are not B1438's sector modules, whose three characters are all
    trivial on μ.
  - **The web seat's post hoc 1** (`4345829aa`, its output in `f181d5f8d`): at the odd levels the twisted duality
    h²(V) = h¹_rel(V* ⊗ w) holds on every character and the untwisted one fails, and non-zero gaps h¹(χ) − h¹(χ* ⊗ w)
    (±1, in equal numbers: 4, 11 and 29 of each sign at levels 3, 5 and 7) occur only at the odd levels. This is read
    on main, not recomputed.
- **Main's own computation** (`verification/odd_ticks_no_modules.py`; Fox calculus over F₁₉₁₄₁, the characters through
  a root of unity of the torsion's exponent; no code of the seat's):

  | level n | orientable | fibre-torsion characters with l(μ) = 1 | of them with a class non-zero on λ | with l(μ) = −1 (twisted): non-zero on λ |
  |---|---|---|---|---|
  | 1, 2 | no, yes | 0 | — | — |
  | 3 | no | 3 | **0** | 3 of 3 |
  | 4 | yes | 4 | 4 | — |
  | 5 | no | 10 | **0** | 10 of 10 |
  | 6 | yes | 15 | 15 | — |
  | 7 | no | 28 | **0** | — |
  | 8 | yes | 44 | 44 | — |

  The character counts are the web seat's (3, 10, 28; 4, 15, 44), found by a different code on two other primes.
- **So, on the record's definition, the class-index frame's matter exists only at an even number of ticks. At an odd
  number it exists only in the form twisted by the orientation character.**

## 2. What this means, and what it does not

- **It bears on the even-tick condition** (the author's ruling of 2026-11-11: "only even ticks are observed" is a
  condition the weight must deliver). The frame does part of the work: whatever weight a history with an odd number of
  ticks carries, it carries no sector module of the record's kind. Whether the twisted modules, which do exist there,
  count as the frame's matter is a definition. The record has made it only implicitly (B1438's l(μ) = 1). It is now a
  stated choice, and it decides whether the frame delivers the condition outright. It is entered as such
  (register row P-846), not decided here.
- **It sharpens the hand.** At odd ticks, matter can exist only twisted by the orientation character. The hand enters
  the frame's matter exactly through the tick's parity. This is the twisted duality the SM seat proposed, met at its
  root.
- **Main's expectation of 2026-11-13** (that the gap between h¹(V) and h¹(V* ⊗ w) follows the tick parity) is moot on
  the odd levels for the untwisted modules, as the web seat said. For the twisted modules it is the web seat's post hoc
  1 and the SM seat's SM-C10, both pending.
- **Not shown:** the frames F-HE and F-AP on m000 (W-C8, later parts); the twisted modules' counts and duality; the
  metallic rivals' ticks (W-C8 part 5). The physical reading of any of it is not given.

## 3. Mistakes made on the way and mended (disclosed)

- **Main's first control was mis-designed.** It took t's value from 1 to 40 and found no non-zero class, but the proof
  says the twisted value l(μ) = −1 is the only one that frees c(λ), and the sample missed it. The control was replaced
  by exactly that value before the result was used, and it then finds every class non-zero.
- **Main's first message to the author overstated the result.** It said odd-tick histories carry nothing the frame
  can count. They carry no untwisted sector module, and twisted ones exist. The correction was told the same night.

## 1a. Seen first

`VERDICT topic-sweep /non.orientable|Klein bottle|Gieseking|m000|orientation.twisted|odd tick/: 25 of 1664 arcs on
main match (OPEN 3, PROVED 22); 3 register rows match (QUEUED 3)`. None states this result. Read for this arc:
- B469: every metallic bundle double-covers a non-orientable bundle.
- B1234: the squaring buys orientability and costs every value.
- B1239: a free orientation-reversing deck gives CS = 0.
- B1328: extension over m000 selects, one mechanism, a relation.
- B1607 and B1871: the tick at the common point; one tick or two acts.
- B1438: the slope law and the sector modules' definition.
- GENESIS T-ROOT and its table of frames, whose m000 row this fills for two frames.

**Literature:** Fox calculus; the cohomology of a group with coefficients in a character (standard).

## Files

- `verification/odd_ticks_no_modules.py` → `odd_ticks_no_modules.json`, `odd_ticks_no_modules_run.txt` (seconds).
- `verification/web_seat_part2a_out_e37753fd7.txt`: the web seat's sealed run's output, copied unchanged from its
  branch at `e37753fd7`.
- The lock: `verification/test_b1926_odd_ticks.py`. Its planted cases: the twisted characters must free c(λ); a
  conjugator with the wrong sign must be refused; the orientable levels must carry classes.

## Reproduce

```
cd frontier/B1926_at_odd_ticks_the_frames_matter_exists_only_twisted_by_the_orientation_the_tick_inverts_the_scar/verification
python3 -B odd_ticks_no_modules.py && python3 -m pytest -q .
```
