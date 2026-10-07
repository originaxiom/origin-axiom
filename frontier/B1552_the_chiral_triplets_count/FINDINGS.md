# B1552 — THE CHIRAL TRIPLET'S COUNT: NEGATIVE as sealed — F-HE's count at the weave's own spin vacuum is (0, 0) at every reading: the weave's chiral triplet carries no generation in the frame's dictionary there; after the read-out, sm:B1509's T2 and T3 prove the zero at every class on every thread at every tick

cc (the SM-derivation seat), 2026-10-07. **Verdict: NEGATIVE, by the seal's §7** (P5 holds on no chiral twin in either
module, with P1–P4 holding on a complete record).
- **The seal.** `c9d03b92` (sha256 556910b6…), on the owner's ruling "Seal and run now", ahead of main's requested
  review.
- **The identity.** It held at 18:24:35–18:24:42Z (`verification/identity.json`).
- **The run.** 18:24:54Z to 20:09:36Z, rc 0, three workers, one start each and no stop.
- **The record.** It was committed unread at `69a357a3`.
- **The read-out.** `read_out.py` ran once, at 20:10:05Z.
- **The price is unchanged:** 0 of 19.

## Seen first

- **The repo sweep at the seal** (the seal's §0). Twelve terms over every head, fetched 2026-10-07 at 18:12:57Z.
  - "complex triplet" is on no head.
  - "spin doublet", "chiral triplet", "common point" and "spin vacuum" are only in this branch's weave dossier (W8–W10).
  - Main's B1600 and B1601 and this branch's sm:B1550, sm:B1530 and the held sm:B1551 were read for their bearing.
- **The literature leg** (abstract level, 2026-10-07):
  - Biswas, Gupta, Mj and Whang (arXiv:1707.00071), finite mapping-class orbits at genus one;
  - Looijenga's Prym representations (abelian covers, arithmetic images);
  - Korinman (arXiv:1412.2671), the punctured tori's quantum representations;
  - Daly (arXiv:2411.04431), twisted Alexander polynomials of punctured-torus bundles;
  - the A₄ and Δ(27) flavour literature (complex triplets put in by hand).
- **The standing is EXTENDS.** Nothing found reads the frame's count at the common point.

## 1. The question and the design (the seal's §1–§5)

**The question.** The weave dossier's W10 has, from the joint action of L and R with no thread chosen:
- a chiral triplet T, and its conjugate T̄, on the three parity-twisted spin doublets of the common point;
- three alike interior classes at one vacuum character on exactly one sign twin of every odd-trace word, at tick 3.

**The arc asks whether each of those classes carries one generation in the frame's count.** The count is
(I(W₁), I(Λ²W₁)), with W₁ = [[A, c], [0, 1]] and c a generic interior class, read with F-HE's dictionary unchanged.

**The modules.** Two candidates:
- (a) λ ⊗ (ρ_Q ⊕ ρ_Q);
- (b) λ ρ_Q ⊕ λ̄ ρ_Q.

**The population.** The twelve odd-trace states to length 6 at tick 3: both lifts, both modules, the three parities,
every κ ∈ μ₈ with n > 0, and two draws. That is 432 readings per route.

**Two routes.**
- Route 1: the tick's route-P presentation with sm:B1549's banked cohomology at 50 digits.
- Route 2: the deck-compatible presentation with the arc's own numpy Fox calculus.

**The controls.** The pre-seal controls, outside the population and disclosed, read (0, 0).

## 2. The read-out (`verification/read_out.json`, `read_out_log.txt`)

| prediction | held? |
|---|---|
| the record complete (12 of 12 states in each route) | yes |
| P1, the two routes give the same multiset of counts per (state, module, lift) | yes |
| P2, the two draws agree at every reading | yes |
| P3, the three parities agree at each (state, module, lift, κ) | yes |
| P4, every route-2 gap ≥ 10⁶ | yes |
| P5, (−1, −1) at the three parities on a chiral twin | **no, on all six twins in both modules** |

**The verdict rule gives NEGATIVE as sealed.**

## 3. The counts

**All 864 readings read (0, 0):** 432 in each route, on all twelve states, both modules, both lifts, every κ and both
draws. The six vector-like twins read (0, 0) too, which is P6, recorded.

**The interior dimensions behind the zero** (the record's `reads`, the same in both routes):

| module | states | readings per route | n(A) | (h⁰, h¹, r¹, n) of W₁ ∣ W₁* | of Λ²W₁ ∣ Λ²W₁* |
|---|---|---|---|---|---|
| (a) | chiral twins | 144 | 2 | (0, 1, 0, 1) ∣ (1, 3, 2, 1) | (0, 2, 0, 2) ∣ (0, 2, 0, 2) |
| (a) | vector-like twins | 72 | 4 | (0, 3, 0, 3) ∣ (1, 5, 2, 3) | (3, 10, 9, 1) ∣ (0, 4, 3, 1) |
| (b) | chiral twins | 144 | 2 | (0, 1, 0, 1) ∣ (1, 3, 2, 1) | (1, 6, 5, 1) ∣ (0, 4, 3, 1) |
| (b) | vector-like twins | 72 | 4 | (0, 3, 0, 3) ∣ (1, 5, 2, 3) | (3, 10, 9, 1) ∣ (0, 4, 3, 1) |

The extension lowers the interior dimension of W₁ and of W₁* alike, and of Λ²W₁ and Λ²W₁* alike, so I = 0 at every
reading.

## 4. After the read-out: the zero is a theorem the record already had (PROVED; missed at design time)

**The theorem.** At the weave's spin vacuum, I(W₁) = 0 for every non-zero class c. This holds on every state at every
tick, at every κ, in both modules and in any sum of twists λ ρ_Q. It is sm:B1509's T2 and T3 (this seat, 2026-10-01)
read at the common point. Its check is the weave dossier's W11 (`the_spin_zero.py`).

**The proof.**
- **No cusp cohomology.** The puncture loop acts on A by λ([a, b]) ρ_Q([a, b]) = −1. So the peripheral torus fixes no
  vector, and H*(T; A) = 0 by the Koszul complex.
- **No fibre invariants.** Q₈ fixes no vector of ℂ², so H⁰(F; A) = 0 and H⁰(A) = H⁰(A*) = 0.
- **sm:B1509's T2 gives I(W₁) = −r₁, with r₁ = 1 exactly when e ∪ c = 0** (e the fibration class).
  - T2's proof does not use its hypothesis h¹(A) = 1.
  - The classes from H¹(M; A) restrict into H¹(T; A) = 0. So the restriction of W₁'s classes still factors through
    H¹(M; 1) = ℂe.
- **sm:B1509's T3: e ∪ c is the image of c under the natural map ker(S_A − 1) → coker(S_A − 1).** S_A is the stable
  letter's action on H¹(F; A).
- **At the weave's vacuum S_A is semisimple.** It is κ times an element of a finite group: W10's group of order 96 on the
  parity-twisted doublets, or W9's ℤ/8 on the doublet. So the map is injective, e ∪ c ≠ 0, r₁ = 0 and I(W₁) = 0.

**What follows.**
- **No generation shape here.** F-HE's (−1, −1) needs I(W₁) = −1. So the weave's spin vacuum carries no generation and no
  anti-generation in this frame, on any thread at any tick, in any rank.
- **The record is the case.** At all 864 readings, r₁(W₁) = 0, h⁰(W₁*) = 1 and r₁(W₁*) = 2, as T2 says (the table, and
  W11's check (1)).
- **Λ²W₁ is not needed.** It reads 0 as well (the table).

**What the arc got wrong.**
- The answer could be read at design time. The seal's sweep (§0) named the vacuum, not the mechanism, so it did not reach
  this seat's own sm:B1509.
- The run, 2 h 39 min, confirms the theorem on twelve states. It was not needed to learn the answer.
- This is recorded for the reconciliation with main.

**Where a count can live (the same two theorems, read as a rule).** An extension's index needs either:
- cusp cohomology of A: a puncture that fixes a vector, as the hyperbolic vacuum's parabolic does (sm:B1530, sm:B1550);
- or a Jordan block of S_A at eigenvalue 1, as sm:B1509 found at q = 17 ± 12√2.

The weave's spin vacuum has neither, at any tick.

## 5. What it means

- **The weave's own vacuum gives no generation content in the frame.**
  - The weave's chain from the principle stands: non-cancellation and the joint action force the vacuum (W2), the
    records give three parities (W1), and the vacuum's spin part gives them as a chiral triplet with interior room (W9,
    W10).
  - F-HE's count reads that triplet as (0, 0) everywhere: no generation and no anti-generation, in either candidate
    module.
- **So the content of a generation is not the weave's alone.** In the record it appears only at a thread's own
  hyperbolic geometry. On the forced A₄ cover that is on +LR alone (sm:B1550; W6, twelve of twelve).
- **This fits main's B1601 disclosure,** "meeting the common point does not give content", now in the frame's own
  count.
- **For the owner's goal:**
  - derived from the weave: the three, alike, separate at the third tick, with a hand;
  - not derived: that each of the three carries a generation, which this frame does not give at the weave's vacuum.
- **The closest whole picture is two-sided:** the weave's three with +LR's content (sm:B1550). By the owner's rule that
  is a thread result.
- **By §4, this holds beyond the population.** The frame reads no generation at the weave's spin vacuum on any thread at
  any tick (WEAVE + WAVE, proof).

## 6. What this arc does not decide

- **Other frames or dictionaries** at the weave's vacuum (GENESIS FK11).
- **A vacuum combining a thread's geometry with the weave's spin part.** One candidate is λ ⊗ ρ_hyp ⊗ ρ_Q, a natural
  rank four. It is not read here; it is the hatch.
  - §4's rule allows content there: on the puncture, ρ_hyp ⊗ ρ_Q acts as (−U) ⊗ (−1) = U, with U unipotent, so it fixes
    a vector.
- **Vacua outside §4's theorem.** States beyond length 6, other ticks and other κ at the spin vacuum are decided by §4.
  Characters of other kinds (not twists of ρ_Q) are not.
- **Whether the third tick counts (GENESIS FK7), and the swap (GENESIS GM5c).**

## Files

- `PREREGISTRATION.md`: the seal.
- `verification/`:
  - `chiral_lib.py` (both routes);
  - `identity.py` → `identity.json`;
  - `pre_seal_controls.json`;
  - `run.py` → `run_1.jsonl.gz`, `run_2.jsonl.gz` (`run_sha256.txt`);
  - `read_out.py` → `read_out.json`, `read_out_log.txt`;
  - `run_notes.md`.
- `ARTIFACT_HASHES.txt`.
- After the read-out: the weave dossier's W11, `docs/dossiers/the_weave_2026-10-07/the_spin_zero.py` →
  `the_spin_zero.json` (§4's theorem checked on this record and its hypothesis on every state to length 12).
