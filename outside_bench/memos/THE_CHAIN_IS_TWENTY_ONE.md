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

---

# ADDENDUM 1 — THE PRICING WAS THE SMALL FINDING. THE LARGE ONE POINTS THE OTHER WAY.

**2026-09-11.** Owner: *"what does this mean? why it feels like youre not reporting properlu/downplaying"*.

The instinct was right, and for a worse reason than tone. The body of this memo priced the
apparatus and led with the cheap number. I had not finished asking **what the sealed clauses
depend on.** Having asked, the answer runs against the body's framing.

## 1. All three sealed clauses are functions of the word

At every window where the word closes, `H_L` **is** `H_R` read backwards — not similar to it, the
same matrix under the reversal permutation, verified elementwise:

    N =   21  even   H_L == J·H_R·J : True    isospectrality 1.33e-15
    N =  144  even   H_L == J·H_R·J : True    isospectrality 7.77e-16
    N =  987  even   H_L == J·H_R·J : True    isospectrality 1.33e-15
    N =   34  odd    H_L == J·H_R·J : False   isospectrality 1.51e-01
    N = 1597  odd    H_L == J·H_R·J : False   isospectrality 1.47e-01

* **Clause 1** (isospectrality at even index) holds exactly where the word closes — and there it is
  a **relabelling**. Two orderings of one matrix have the same eigenvalues. The `1.3×10⁻¹⁵` is
  floating-point error in diagonalising the same matrix twice.
* **Clause 3** (breakage at odd index) is the complement of the same word fact.
* **Clause 2** (the 5/6 split) is the one I expected to be free, and it is not. Under `J` a
  right-hand eigenvector carrying weight on the **first** 20 sites maps to a left-hand eigenvector
  carrying weight on the **last** 20. So the left count is forced to be the right chain's *far-end*
  count. **Computed: the J-forced left count equals the measured left count at every closed window.**
  The "complementary split between two hands" is **(near-end, far-end) counts of one chain.**

The word is a function of `(ρ, N)`, both fixed in the seal. **So all three clauses are computable on
paper, and none is contingent on a measurement.**

## 2. What this is NOT

**It is not an error in B1095, and B1095 does not hide it.** Its own sentence: *"the left hand's word
is EXACTLY the reversal of the right hand's word … so the two half-line Hamiltonians are conjugate
by the exchange matrix (J·H_R·J = H_L) and the spectra coincide."* The mechanism is stated. The spec
labels clause 1 **(forced)**. And *"P-equivariant (free)"* means **not invariant** — which is true:
the split does change under P. Nobody claimed it was undetermined. **No retraction is asked of
anyone.**

## 3. What it is

A question about the **prereg as a falsifier**, and the record's own rule answers it.

> **MB12/E2**, `WHAT_WOULD_COUNT` §4A.0's own citation: *"a preregistered test must be able to both
> pass and fail"* … *"**cannot-fail and cannot-pass are the two faces of one defect (E2/MB12): both
> settle the outcome before the test runs, so neither is a test.**"*

If the prediction is an identity of its own model, then **given the model it cannot fail.** What a
measurement could still refute is that a fabricated array *realises* the intended word and the
tight-binding model. That is a real and worthwhile experiment — it tests fabrication and the
platform's reciprocity — but it is a test of the apparatus, not of the object.

And the reciprocity half is not even contingent: *any* chain read backwards has the same spectrum.
So the empirical residue of clause 1 is **"is the left-going word the reverse of the right-going
word"** — combinatorics — **plus "is the photonic platform reciprocal"** — known physics.

§4A.0 applied MB12 to a whole success *tier*, and wrote that doing so was the larger application of
a rule previously used on single criteria. **This is the same rule applied to a sealed prereg.**

## 4. The limit of this finding, stated rather than left for a reader to find

This analyses the **sealed §1 windows, at ρ = α**. B1085's object is the **function ρ ↦ edge
content**, banked over a 144-point sweep (`rho_sweep_counts.json`). **Whether that function carries
contingent content is not addressed here**, and it is the obvious next cell. If it does, the lab
lane's falsifier should be re-posed on the function rather than on the α windows — which is a thing
the seal's own addendum-beside rule permits.

## 5. What survives of the body of this memo

The pricing stands and is still useful, but as **calibration, not as the experiment**: the word
closes at N = 21 and breaks at 13/34 with macroscopic gaps, so a fabricator can verify that an array
realises the intended cut phase on 13–34 waveguides before committing to a 144+ array. That is worth
having. It is not a test of the programme.

**And the honest consequence for the goal: Tier-INTERFACE is weaker than §4A.2 presents it.** That
does not make the programme worse — it makes the ledger true. It does re-rank what is left: if the
lab lane tests a model identity, then K3 (the crossings sort) and the three 4A.3 doors carry the
weight.

*Nothing is retracted from any other arc. Gate 5 untouched.*
