# W18 — a prediction, recorded before the test

The SM-derivation seat, 2026-10-08. Committed before the run it predicts. Nothing here is a result.

## What was seen before this was written

- **W17.** The weave's five on the thread itself, W(ν, c) = [[Dν³, c·Pν⁻²], [0, Pν⁻²]] (D = ρ_Q, P = Ad ρ_Q), reads
  F-HE's pair (1, 1) on the vector-like twin of every word with φ³ ≢ ±I (mod 16). It reads (0, 1) on the chiral twin and
  (0, 0) on the mod-16 words. 32 of 32 states to length 8.
- **A scratch probe.** The same five on the forced A₄ cover, by Shapiro. It used one reading per state: lift 0, the
  first ν with a class, and the first basis class. The cover's count splits over A₄'s irreducibles R ∈ {1, ω, ω², P},
  where ω is the deck character and P the triplet, with weights dim R. Each sector's pair is (I(W⊗R), I(Λ²W⊗R)).
  - +LR and −LLLR: 1: (1, 1); ω: (0, 1); ω²: (0, 1); P: (1, 1). The cover's total is (4, 6).
  - −LR and +LLLR: 1, ω and ω²: (0, 1) each; P: (0, 2). The total is (0, 9).
  - +LLRLRR: (0, 0) in every sector.
- **A structural check (no index read).** On all 32 states the parity lines of W8 have value 1 on the stable letter
  at tick 3 (B_p(t³) = 1). The cusp-trivial lines B_p are therefore exactly the A₄ triplet's three characters
  restricted to the resolving tick.

## The quantity

At the resolving tick, M₃ (the thread's third tick), each non-zero parity has its line B_p, a character of π₁(M₃).
The five carried by that line is W|M₃ ⊗ B_p.
- **Its pair** is (I(W|M₃ ⊗ B_p), I(Λ²W|M₃ ⊗ B_p)). This is the B_p-part of the counts that the forced cover's five
  gives in F-HE's dictionary.
- **Summed over the three parities,** it is the five valued in the weave's triplet, (W ⊗ P)|M₃.
- **By Shapiro,** each parity's part equals the tick-1 pair (I(W⊗P), I(Λ²W⊗P)).
- **The zero parity's part** is W|M₃ itself. By Shapiro it is the sum of the sectors 1, ω and ω² at tick 1.

## The rule (named before the run; the trial budget is this list)

- **Population and readings:** every odd-trace state of GENESIS to length 8 (32 states). Both lifts of t. Every 24th
  root of unity ν at which the gluing group is non-zero. Every basis class and one generic combination. These are
  W17's 480 readings.
- **Route A (tick 1, every reading):** for each R ∈ {1, ω, ω², P}, the pair (I(W⊗R), I(Λ²W⊗R)), and the same for
  the dual W*.
- **Route B (tick 3, direct):** on the twelve states to length 6, both lifts, every ν with a class, and the first basis
  class. For each parity q ∈ {0, p1, p2, p3}, the pair (I(W|M₃ ⊗ B_q), I(Λ²W|M₃ ⊗ B_q)), with B_0 trivial. Length 8
  is left out: its tick-3 relators run to 71 404 letters, too long for the rank-ten module on this engine.
- **The checks:**
  - route B's non-zero parities equal route A's P-sector;
  - route B's zero parity equals the sum of route A's 1, ω and ω²;
  - the three parities agree with each other (Theorem G).
- **The engine:** sm:B1374's, over GF(p) with p ≡ 1 (mod 24), as in W17.

## The predictions

1. **The carriers.** These are the vector-like twins of the words with φ³ ≢ ±I (mod 16), 14 states. Every reading's
   P-sector is (1, 1). So each parity line carries exactly one generation of the weave's five, and the five valued
   in the triplet reads (3, 3) at the resolving tick.
2. **The chiral twins** (14 states): the P-sector is (0, 2).
3. **The mod-16 words** (±LLRLRR and ±LLLLLRRR): (0, 0) in every sector.
4. **The singlet sectors:** (1, 1), (0, 1) and (0, 1) on the carriers, and (0, 1) each on the chiral twins. So the
   zero parity's part is (1, 3) on the carriers, which is anomalous, and the forced cover's total is (4, 6).
5. **The two routes** agree at every reading they share.

**What each outcome would mean.**
- **If (1) holds,** each of the three parity lines carries exactly one generation of the weave's own five at the
  resolving tick, on every carrier thread. That is three sectors of index one, distinguished by the parity characters
  and cycled by the deck: main's orbifold standard, met by law on the weave's own modules.
  - The three sectors together are anomaly-free, (3, 3).
  - The zero parity's part, (1, 3), is not, and neither is the forced cover's total, (4, 6).
- **If some carrier's P-sector reads otherwise,** the probe's (1, 1) on +LR and −LLLR was a coincidence, and the
  parity lines do not carry one generation each by law.

Either way the count is read in F-HE's dictionary (GENESIS FK11, I-26, unearned). Reading the three sectors as three
generations of one world needs the third tick kept (GENESIS FK7).
