# W-F25: at the cusp, frame C's S reading has rational exponents. At the mark they are (3/5, 1) for the up sector and (2/5, 11/10) for the down sector and the leptons; at the twin the up sector's are (1/5, 6/5). They do not depend on Re τ or on the end's value, so frame C has a read-out with no τ and no measure: its exponents, with one overall scale left open

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free) and a proposal. It closes card W-F25
(`relays/cards/CHAT1_W-F25_frame_cs_cusp_exponents.md`, d6ac703c1).

**The ruling it runs under.** The author's ruling of 2026-11-15 (frame C's outputs computed and printed; no data, no
comparison). No data was opened. The exponents and their ratios below are not set beside any measured number.

**Not blind.** It was designed after W-F24's output was read, and after the big run's negative was seen. Any use of it
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

- **Y1** (the last two steps agree within 3 %) is not met, because of the S̃ σ₃/σ₁ column. Every S exponent and every S̃
  σ₂/σ₁ exponent converges, to 1e-3 or better.
- **Y2** (Re τ = 0 against 0.25 within 2 %) is not met only for up S̃ σ₃/σ₁ (1.51 against 1.58). Every other exponent is
  the same at both.
- **Y3** (the constant end against the canonical end) is not met, and the expectation's premise was wrong.
  - B1924's constant end, L₂ = 0.9 − ½ log Im τ, falls without bound. At the cusp 2πL₂ + c_s turns negative, and the frame's
    channels drop out: the run's warnings show all singular values zero.
  - The canonical end settles near 2.25, and the table holds it there above height 6.
  - **Post hoc 1, H1 holds.** With the end held at 1.5, 2.25 and 3.0, every S exponent at the mark is unchanged to four
    digits. The exponents do not depend on the end's value, as long as the end stays bounded.
- **Y4** (each limit within 2 % of a rational with denominator at most 50) holds as written. But for the two unsettled S̃
  σ₃/σ₁ entries, the search's 30/19 and 22/17 identify nothing: they are rationals near unconverged numbers.

**On the fibre.** The exponents depend on the point of order 5 through its first coordinate. Over the 24 points:
- the points (0, j/5) give non-rational values near 1 and 1.85 to 1.92;
- (±1/5, ·) give (1/5, 6/5) up and (2/5, 11/10) down;
- (±2/5, ·) give the mark's.

**On the act's line** (B1943: LR fixes up to sign exactly the four non-zero points of one line of order 5, k·(2/5, 4/5)):
- the four points form two pairs, ±(2/5, 4/5), the mark, and ±(1/5, 2/5), the twin;
- they agree on down and leptons, and differ on up:
  - the mark gives (3/5, 1);
  - the twin gives (1/5, 6/5).

## 2. The proposal: frame C read at its cusp

The proposal has three parts, and each is a reading.

1. **The point is the cusp, not an average.**
   - L = [[1, 1], [0, 1]] fixes ∞, and R = [[1, 0], [1, 1]] fixes 0 = S(∞).
   - So the two letters' fixed points are one class: the surface's single cusp. It is the point the two letters agree on,
     where the uniform measure on letters agrees on none.
   - There the frame's hierarchy is exact. Each ratio is ε^E, with ε = e^(−π Im τ) and E rational.
2. **The line is the act's line.** B1943 proves it is forced. What it leaves is the pair mark and twin. B1934's hand (the
   Legendre symbol mod 5) separates them, and it bears only on the up sector.
3. **The read-out is the exponent vector, with one scale.**
   - The overall scale ε is a single number for every sector. The frame does not fix it, and it is typed here as an open
     parameter.
   - Statements with no parameter at all are the ratios of logs. At the mark, in the S reading:
     - log(σ₃/σ₁) / log(σ₂/σ₁) = 5/3 for up, 11/4 for down and the leptons;
     - between the sectors, E_up/E_down = 3/2 (σ₂/σ₁) and 10/11 (σ₃/σ₁).
   - These are printed. They are not compared with anything measured.

**What this changes, and what it does not.**
- It removes the measure: there is no R6 choice left. It removes the reading point in favour of the act's line.
- It replaces "no τ" by "one scale": the height is not averaged away, and it is one number for twelve ratios.
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
| the act's line splits into mark and twin on the up sector only | computed once (post hoc 1 and the sealed run's fibre table; not blind) |
| the cusp is the class of both letters' fixed points | a reading (elementary) |
| the exponent read-out with one open scale | a proposal |

## 4. Files

`relays/chat1_2026-11-15_wf25/`:
- `wf25_run.py` (sealed), `wf25_posthoc1.py` (committed before its run) and `SCRIPT_SHA256.txt`;
- both outputs;
- `wf25_run_err.txt`, which holds the constant end's divide-by-zero warnings, and `wf25_posthoc1_err.txt` (empty);
- `wf25_summary.json`.

This note was pushed before its referee read finished, at the author's word (2026-11-15). The read's corrections follow in a later commit.

0 of 19.
