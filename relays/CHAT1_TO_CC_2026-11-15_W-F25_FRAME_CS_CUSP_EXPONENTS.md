# W-F25: at the cusp, frame C's S reading has rational exponents. At the mark they are (3/5, 1) for the up sector and (2/5, 11/10) for the down sector and the leptons; at the twin the up sector's are (1/5, 6/5). They are the same at Re τ = 0 and 0.25 and with the end held at 1.5, 2.25 and 3.0. A proposal: read frame C by its exponents, with no measure and one open scale, the height

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free) and a proposal. It closes card W-F25
(`relays/cards/CHAT1_W-F25_frame_cs_cusp_exponents.md`, d6ac703c1).

**The ruling it runs under.** The author's ruling of 2026-11-15 (frame C's outputs computed and printed; no data, no
comparison). No data was opened. The exponents and their ratios below are not set beside any measured number.

**Not blind.** Its script was drafted while W-F24 ran and finished after W-F24's output was read (the card quotes it), and after the big run's negative was seen. Any use of it
against data is a fork after the look.

**How it was checked.** Computed once; expectations committed first.
- **The sealed run.** `wf25_run.py` was sealed at d6ac703c1 and run once. Its output was committed (a6b801f9c) before it
  was read.
- **Post hoc 1.** `wf25_posthoc1.py` was committed (c04143de6) before its run, and is not blind. Its output was committed
  before it was read.
- **The frame** is W-F24's.
- **The exponent.** E = −(1/π) d log r / d Im τ, estimated as the local slope over unit steps at heights 2 to 10. A ratio
  below 1e-12 is not resolved in double precision, and its steps are dropped.
- **The estimator's known-answer check.** exp(−π(7/5)y)(1 + 0.3e^(−y)) gives 1.4004, identified as 7/5.

## 1. Results

**At the mark (2/5, 4/5), Re τ = 0, the canonical end.**

| sector | S: σ₂/σ₁ | S: σ₃/σ₁ | S̃: σ₂/σ₁ | S̃: σ₃/σ₁ |
|---|---|---|---|---|
| up | **3/5** (0.6000) | **1** (1.0000) | 3/5 (0.5999) | not converged (1.58, 1.77; 4 resolved steps) |
| down | **2/5** (0.3998) | **11/10** (1.0998) | 2/5 (0.3992) | not settled (1.2905 → 1.2937) |
| leptons | as down | as down | as down | as down |

- **Y1** (the last two steps agree within 3 %) is not met, because of the up sector's S̃ σ₃/σ₁ (1.58 against 1.77; 4
  resolved steps). The down sector's S̃ σ₃/σ₁ meets it (1.2937 against 1.2905), but with 5 resolved steps it is not
  settled. Every S exponent and every S̃ σ₂/σ₁ exponent converges (the last two steps within 6e-4).
- **Y2** (Re τ = 0 against 0.25 within 2 %) is not met only for up S̃ σ₃/σ₁ (1.51 against 1.58). Every S exponent is
  the same at both to 1e-4; the others agree within 0.8 %.
- **Y3** (the constant end against the canonical end) is not met, and the expectation's premise was wrong.
  - B1924's constant end, L₂ = 0.9 − ½ log Im τ, falls without bound. Theorem 90's weight, 2πL₂ + c_s − π|a0_s|² e^(−2L₂), then
    turns negative, because e^(−2L₂) grows like Im τ. Every channel drops out and the coupling vanishes: the run's
    warnings are 0/0 in the ratios.
  - The canonical end settles near 2.25, and the table holds it there above height 6.
  - **Post hoc 1, H1 holds.** With the end held at 1.5, 2.25 and 3.0, every S exponent at the mark is unchanged to four
    digits. At these three values the exponents do not depend on the end's value. An end low enough to turn a channel's weight
    negative is not covered (the referee: a held end of 0.2 drops every channel).
- **Y4** (each limit within 2 % of a rational with denominator at most 50) holds as written. But for the two unsettled S̃
  σ₃/σ₁ entries, the search's 30/19 and 22/17 identify nothing: they are rationals near unconverged numbers.

**On the fibre.** The exponents depend on the point of order 5 through its first coordinate. Over the 24 points:
- the points (0, j/5) give values near 1 and 1.85 to 1.92 at height 10, not settled in double precision (the
  referee, in extended precision to height 20: the slopes still rise, and a fit with a power of Im τ in front gives 1
  and 2, as fits channels whose norms grow linearly in Im τ);
- (±1/5, ·) give (1/5, 6/5) up and (2/5, 11/10) down;
- (±2/5, ·) give the mark's.

**On the act's line** (B1943: LR fixes up to sign exactly the four non-zero points of one line of order 5, k·(2/5, 4/5)):
- the four points form two pairs, ±(2/5, 4/5), the mark, and ±(1/5, 2/5), the twin;
- in the S reading they agree on down and leptons (to 5e-4), and differ on up:
  - the mark gives (3/5, 1);
  - the twin gives (1/5, 6/5).

## 2. The proposal: frame C read at its cusp

The proposal has three parts, and each is a reading.

1. **The point is the cusp, not an average.**
   - L = [[1, 1], [0, 1]] fixes ∞, and R = [[1, 0], [1, 1]] fixes 0 = S(∞).
   - So the two letters' fixed points are one class: the surface's single cusp. It is the point the two letters agree on,
     where the uniform measure on letters agrees on none.
   - There the frame's hierarchy is exact in its exponents. Each ratio behaves as C ε^E, with ε = e^(−π Im τ), E
     rational, and C a prefactor of the frame's that can depend on Re τ and on the end (the referee: up S σ₂/σ₁'s
     log-prefactor is 0.59, 0.15 and −0.37 at Re τ = 0, 1/4 and 1/2).
2. **The line is the act's line.** B1943 proves it is forced. What it leaves is the pair mark and twin. B1934's hand (the
   Legendre symbol mod 5) separates them, and it bears only on the up sector.
3. **The read-out is the exponent vector, with one scale.**
   - The overall scale ε is a single number for every sector. The frame does not fix it, and it is typed here as an open
     parameter.
   - Statements with no parameter at all are the ratios of the exponents: the limits of the ratios of logs as ε → 0. At
     a finite scale the prefactors enter. At the mark, in the S reading:
     - log(σ₃/σ₁) / log(σ₂/σ₁) = 5/3 for up, 11/4 for down and the leptons;
     - between the sectors, E_up/E_down = 3/2 (σ₂/σ₁) and 10/11 (σ₃/σ₁).
   - These are printed. They are not compared with anything measured.

**What this changes, and what it does not.**
- It removes the measure: there is no R6 choice left. It removes the reading point in favour of the act's line.
- It replaces "no τ" by "one scale": the height is not averaged away, and it is one number for twelve ratios,
  beside their prefactors.
- It does not settle:
  - mark against twin for the up sector;
  - which reading each sector takes (the Higgs world);
  - the S̃ σ₃/σ₁ exponents (owed: the frame in extended precision, as B1940's);
  - whether a principle fixes ε.
- **Any comparison with data is main's, under a new rule sealed before it.** That rule must:
  - count this card's forking path in the look ledger: after the look, after W-F24, two read-outs tried;
  - declare the open choices above as options before anything is compared.

## 3. Typed

| statement | how checked |
|---|---|
| the S exponents at the mark: up (3/5, 1), down and leptons (2/5, 11/10) | computed once; expectations committed first (Y4); independent of Re τ (Y2) and of a bounded end (post hoc 1, not blind) |
| the S̃ σ₂/σ₁ exponents (3/5 up, 2/5 down) | computed once; expectations committed first |
| the S̃ σ₃/σ₁ exponents | not settled (double precision) |
| in the S reading, the act's line splits into mark and twin on the up sector only | computed once (post hoc 1 and the sealed run's fibre table; not blind) |
| the cusp is the class of both letters' fixed points | elementary (L·∞ = ∞, R·0 = 0, S·∞ = 0); not independently checked. That the two letters "agree" there is a reading |
| the exponent read-out with one open scale | a proposal |

## 4. Files

`relays/chat1_2026-11-15_wf25/`:
- `wf25_run.py` (sealed), `wf25_posthoc1.py` (committed before its run) and `SCRIPT_SHA256.txt`;
- both outputs;
- `wf25_run_err.txt`, which holds the constant end's invalid-value (0/0) warnings (its machine path redacted to `<repo>/`), and `wf25_posthoc1_err.txt` (empty);
- `wf25_summary.json`.

This note was pushed before its referee read finished, at the author's word (2026-11-15); the read's corrections are applied in the next commit.

**From the referee's read** (extended precision, B1940's steps, heights 2 to 20; recomputed independently):
- At the mark: up S 3/5 and 1, down S 2/5 and 11/10, confirmed. **The S̃ σ₃/σ₁ limits are 8/5 (up; 1.599989) and 13/10
  (down and leptons; 1.299998).** The run's 30/19 and 22/17 were rightly left unsettled.
- At the twin: up S (1/5, 6/5) and up S̃ (1/5, 1); down (2/5, 11/10) in S and (2/5, 13/10) in S̃. So mark and twin agree
  on down and leptons in both readings and differ on up in both.
- All these limits are the same to 1e-5 at Re τ = 0, 1/10, 1/4 and 1/2, and with the end held at 0.5, 1.0, 1.5 and 3.0.
- A reading of why: a theta constant's leading power of |q| depends only on its characteristic's first coordinate, so
  the exponents depend on the point only through a. For down and leptons the characteristics' distances to the nearest
  integer form the same set at a = 1/5 and 2/5, and for up they do not. The values themselves were not derived.
- **The options B1932's code carries read the up sector in S̃** (ergodic_t90's claimed assignment: up in S̃, down in S).
  With the referee's limit that reading's up σ₃/σ₁ exponent is 8/5 at the mark; this note's own run left it unsettled.

0 of 19.
