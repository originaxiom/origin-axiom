# 196 — R6′ DISCHARGED: the forced half of the sealed edge prediction is testable at 21 sites

**Date** 2026-09-10 · **Lane** outside bench · **Branch** `<seat>/outside-bench`
**Certificate** `certificates/edge_minimum_chain.py` · **Output** `outputs/edge_minimum_chain_out.txt`
**Instrument** the SEALED one, verbatim · **Gate 5 untouched**

**Occasion:** the owner — *"go for it, do it, advance #1"*, #1 being Tier-INTERFACE.

---

## 0. FIRST, A CORRECTION I OWE THE OWNER

I reported that Tier-INTERFACE was *"owner-pending on the L173 aperiodic-design unseal decision"*
and that it **"needs your word."** **It does not, and has not for twenty days.**

> **L173 — SEALED 2026-08-21 (B1106).** `docs/EDGE_PREREG_SPEC.md`, digest in `SEAL_LEDGER`,
> *"the owner's D-2/D-3 executed — **the aperiodic unseal RESOLVED**"*, C-GEN run and passed
> **before** the seal, differential-first per R12, three kill conditions, NEGATIVE banks if any fires.

`WHAT_WOULD_COUNT` §4A.2 was written **2026-08-20, one day before the seal**, and its status line
has never been updated. I read the status line instead of the state and relayed a decision the owner
had already made back to them as one they owed. Same failure class as this session's stale-tree
readings, and the third instance of it: **a status line is a claim about the record and must be
checked against the record.**

## 1. What is actually open, and it is exact

The addendum-beside (B1171, from cc3's B8146) re-posed R6 as a **commissioned observable**:

> **R6′** — the number of boundary-capable edge modes in a *labelled* Fibonacci gap, as a function of
> the scanned phason ρ, **on a chain long enough to separate a 5-count from a 6-count** at the
> preregistered windows.

**Nobody computed how long "long enough" is.** The banked verifications are at N = 987 and 2584. The
anchor apparatus (Verbin–Zilberberg–Kraus, arXiv 1403.7124 = PRB 91 064201) has **13–28 waveguides**.
The whole question of whether this prediction is testable on apparatus that exists lives in that gap.

## 2. The instrument is the sealed one, and the positive controls reproduce

Convention pinned by `EDGE_PREREG_SPEC` §3 and `B1106/b1106_gen_control.py`: `b_n = ⌊(n+1)a+ρ⌋ −
⌊na+ρ⌋` at `a = 2−φ = 1/φ²`, `ρ = a`; right hand `(b₀…b_{N−1})`, left hand read outward
`(b₋₁, b₋₂, …)`. Hamiltonian, detector and threshold from `tests/test_b1095_mirror_isospectral.py`
verbatim: on-site potential `w_n = b_n`, uniform hopping 1, tridiagonal; boundary weight on the
**first 20 sites**, boundary-capable above 0.5.

B1106's seal records that **two of that bench's own attempts failed the positive control first**.
Both reproduce here before anything else is read:

* **C1, N = 987:** word diffs `[]`, isospectrality **1.332×10⁻¹⁵**, split **(5, 6)**. PASS.
* **C2, N = 1597:** odd-index breakage at **exactly `[0, 1]`**, the two cut-adjacent letters. PASS.

## 3. The answer

| idx | N | parity | word diffs | isospectrality | split (R,L) | 20 sites / N |
|---|---|---|---|---|---|---|
| 7 | **13** | odd | `[0,1]` | 1.93×10⁻¹ | (13,13) | 154% |
| 8 | **21** | even | `[]` | **1.33×10⁻¹⁵** | (21,21) | 95% |
| 9 | **34** | odd | `[0,1]` | 1.51×10⁻¹ | (22,22) | 59% |
| 10 | 55 | even | `[]` | 8.88×10⁻¹⁶ | (17,14) | 36% |
| 11 | 89 | odd | `[0,1]` | 1.47×10⁻¹ | (7,6) | 22% |
| 12 | **144** | even | `[]` | 7.77×10⁻¹⁶ | **(5,6)** | 14% |
| 13 | 233 | odd | `[0,1]` | 1.47×10⁻¹ | (5,6) | 8.6% |
| 14 | **377** | even | `[]` | 1.33×10⁻¹⁵ | (5,6) | 5.3% |
| 16 | 987 | even | `[]` | 1.33×10⁻¹⁵ | (5,6) | 2.0% |

**The sealed prediction splits in two by apparatus cost, and nobody knew:**

**The FORCED half is testable at 21 sites — inside the anchor's existing range.**
The word closes at **N = F₈ = 21** and isospectrality holds there to **1.33×10⁻¹⁵**, machine
precision. This is not a numerical accident and it needed no large chain: once the word closes,
`J·H_R·J = H_L` letter-for-letter and the spectra are *equal by conjugation*, at any size. And the
odd-index control breaks at **N = 13 and 34** with gaps of **0.19 and 0.15** — macroscopic, and also
inside or beside the anchor's range.

> **K1 and K3 — the two forced kill conditions — are testable on arrays of the size that have
> already been fabricated.** 13, 21 and 34 waveguides. The anchor built 13 to 28.

**The FREE half needs a longer chain.** The (5,6) split first appears at **N = 144** and is stable
upward. But the sealed detector's boundary window is an **absolute 20 sites**: it reads 95% of a
21-chain and 59% of a 34-chain. At those sizes the "boundary" is the whole object and the counts
`(21,21)`, `(22,22)` are not boundary measurements at all. On a ≤10%-of-chain criterion the count
needs **N = 377**.

> **K2 — the complementary localization split — needs N ≈ 144 at the earliest and N ≈ 377 for a
> clean boundary read.** Beyond the anchor, but 144 is a plausible fabrication run rather than an
> impossible one.

## 4. What this changes for R6′

R6′ asked to commission *a* mode count. The honest answer is that **the sealed prediction is two
experiments, not one**, and they have very different prices:

1. **The two-hand degeneracy and its parity breakage** — K1 and K3 — at **13/21/34 sites**, needing
   a spectral comparison of two fabricated hands and no mode counting at all. The differential here
   is a *presence/absence of exact degeneracy*, and it is 10¹⁵ apart from its odd-index control.
2. **The complementary count** — K2 — at **144–377 sites**, needing the mode count R6′ commissions.

The first was invisible while the banked windows started at 987. It is the cheaper experiment by two
orders of magnitude in array size and it tests the two *forced* clauses of the prediction.

## 5. Named, not done

**The sealed detector has an absolute scale.** Its 20-site window is fixed in the sealed instrument,
and that — not the physics — is what puts the count's floor at 144–377. A fraction-of-chain detector
would lower it. **This bench does not change the sealed quantity**; the observation is registered so
that whoever writes the next addendum-beside can decide, per the seal's own amendment rule.

**And §4A.2's status line should be corrected on main** from *"SPEC ONLY, OWNER-PENDING"* to
*"SEALED 2026-08-21 (B1106); the live item is R6′'s commissioned observable."* That is main's edit,
not this bench's.

*Gate 5 untouched: no measured physical value is used or named. Nothing promotes to `CLAIMS.md`.
The prediction's content is unchanged — this memo prices its apparatus, and prices nothing else.*
