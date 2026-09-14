# B1408 — L216 ANSWERED BEFORE THE WINDOW WAS SPENT, AND THE
# OBSTRUCTION QUANTIFIED (2026-09-14)

## 0. THE ONE-SENTENCE RESULT

The θ-odd sector carries **exactly one number**, and at the object's own word
that number is `1/(2φ)` — **the value B856 already benched and could not
discriminate**. So **L216 closes negative with no window spent.** And the
obstruction is now measured rather than asserted: **the value channel needs
relative precision ~`10⁻²`–`10⁻³`; an index channel needs ~`10⁻¹`; B856's bench
had ~`10⁻¹`.** 12/12 checks.

**This arc also corrects its own author's hypothesis** — §3.

## 1. THE ODD SECTOR CARRIES ONE NUMBER

Computed at B1349's exactness on the 2-dimensional θ-odd sector (Gram
`diag(2,2)`), over the complete period:

- **ear-independent for ALL 15 words.** Unlike the even sector — where only the
  7 non-units are — the odd readout has **zero ear anchor by construction, at
  every word**.
- **`dim_ℝ span{Q_m} = 1`** of an ambient 3. Singular values
  `[6.3705…, 0, 0]`. The sector carries **one number, scaled**. Its output
  ceiling is `1`, never `4`.
- its whole value set over the period is **three** numbers:
  `{−1, −1/2, +1/(2φ)}`.

## 2. AND AT THE OBJECT'S WORD IT IS THE ALREADY-BENCHED VALUE

    m = 1:   odd readout  λ = (√5−1)/4 = 1/(2φ) = 0.309016994375…

which is exactly what `KIND_TABLE` records as *"the `1/(2φ)` that B856 already
took to a bench and could not discriminate."*

**And the two halves of the mirror agree.** For the ten words with `3 ∤ m` —
precisely those where B1406 found the even sector's graded trace vanishes — the
odd ear-independent readout and B1406's normalised graded trace are **the same
number**, verified exactly:

    agree on m ∈ {1,2,4,5,7,8,10,11,13,14}   =   {m : 3 ∤ m}

> **So the mirror sector's reading at the object's own word is ONE number,
> `1/(2φ)`, reached by two independent routes. The sector is now closed
> entire.** L216 needed no window: the odd row would have delivered the value
> already known to fail.

## 3. THE CORRECTION — AND IT IS THIS BENCH'S OWN HYPOTHESIS THAT FALLS

Going in, the working hypothesis was that *the crowding is a property of the
field*: that `ℚ(√5)` values of small height are dense enough in any window that
**no** such reading could ever discriminate. That would have been a structural
no-go for the entire coupling channel.

**Measured, it is false.** Counting height-bounded `(p+q√5)/r` in a window of
relative half-width `ε` around each of C6's values:

| target | `ε=10⁻¹` | `ε=10⁻²` | `ε=10⁻³` | `ε=10⁻⁴` |
|---|---|---|---|---|
| `1/(2φ)` | 198 | 18 | **1** | **1** |
| `1/2` | 317 | 25 | **1** | **1** |
| `1` | 633 | 54 | 4 | **1** |
| `φ/2` | 513 | 51 | 4 | **1** |
| `1/4` | 155 | 12 | **1** | **1** |
| `φ/4` | 257 | 27 | **1** | **1** |
| `1/(4φ)` | 96 | 7 | **1** | **1** |

*(height ≤ 20, 28 001 candidates; a strict **lower bound** on "natural
candidates" — it excludes `π`, `e`, and everything outside `ℚ(√5)`.)*

Two readings, both important:

1. **At `ε ≈ 10⁻¹` every window is crowded** — tens to hundreds of candidates.
   At height ≤ 12 the count at `1/(2φ)` is **43**, which reproduces B856's
   *"≥17 natural candidates"* as a **generic** fact about that precision, not a
   fact about that value. B856 was not unlucky.
2. **At `ε ≈ 10⁻³` the windows are essentially unique** — one candidate, at
   most four even at height 20; at `10⁻⁴`, exactly one everywhere.

> **So the value channel is NOT dead in principle. It is dead at the precision
> that was available.** The hypothesis that the field forbids discrimination is
> **withdrawn**; what the arithmetic actually says is a *requirement*.

## 4. THE REQUIREMENT, AND THE CHEAPER CHANNEL

| channel | what it must beat | needed relative precision |
|---|---|---|
| **value** (a `ℚ(√5)` reading) | the height-bounded candidates in the window | **`10⁻²` (conservative) to `10⁻³` (generous)** |
| **index** (an integer `n`) | the next integer, at distance `1/\|n\|` | **`10⁻¹`** for `\|n\| ≤ 2` |
| *available* (B856's bench) | — | *`10⁻¹`* |

An integer observable of size 1 or 2 needs **50–100 %** precision to be
confusable. The programme already has such quantities — B1406's graded index
`tr(C) = 2`, and B1335's `I = ±1`.

> ### At the precision the programme can reach, only DISCRETE observables can discriminate. That is two to three orders of magnitude of slack, and it is where a contact row has to be built.

This is not a claim that any particular index *is* a physical observable.
It is a statement about what a contact row must be made of if it is to survive
a bench at achievable precision.

## 5. WHAT THIS SETTLES, AND WHAT IT DOES NOT

**Settles:**
- **L216 CLOSED, negative.** The θ-odd sector carries one number and it is the
  failed one. No window spent — which is the whole point of posing
  discrimination first (B1407's rule, applied immediately).
- **The mirror sector is closed entire.** Both halves, one value, at the
  object's own word.
- **B856's failure was structural, not unlucky** — and so was the even row's.
  Three windows of accounting work were spent on a channel whose binding
  constraint was a factor of `10²` in precision.

**Does not settle:**
- whether any *specific* discrete quantity of this object is a physical
  observable — that is exactly the gate B856 lost on, and nothing here touches
  it;
- whether some higher-precision measurement exists for a quantity of this kind;
  the table gives the threshold, not a survey of benches.

## 6. FENCES

- No value is compared to any measurement. §3's `ε` is a **parameter**, and
  B856's outcome is **cited from `KIND_TABLE`** as already recorded.
- The candidate count is a strict **lower bound** (`ℚ(√5)` only, height ≤ 20).
  A more generous candidate set makes the value channel's requirement
  *stricter*, never looser — so the conclusion is robust in the safe direction.
- The odd-sector computation is exact in `ℚ(ζ₆₀)`; the rank is taken over **ℝ**
  (E73) and the value set reported exactly.
- Nothing here reaches `CLAIMS.md`, F2 or Gate 5.

Artifacts: `b1408_precision.py` (12/12). Locks: `tests/test_b1408_precision.py`.
