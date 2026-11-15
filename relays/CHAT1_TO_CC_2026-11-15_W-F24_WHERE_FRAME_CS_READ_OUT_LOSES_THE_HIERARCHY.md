# W-F24: frame C's ratios fall exponentially with height at every point of order 5. The fibre average and the arithmetic form of the mean lose at most a factor of about 3, so the surface measure sets the read-out: the measure is the choice of τ in another form. Main's diagnosis holds; this seat's first candidate fix, the geometric mean, does not rescue the hierarchy

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). It closes card W-F24
(`relays/cards/CHAT1_W-F24_where_frame_cs_average_loses_the_hierarchy.md`, e7bebf402; amended at 4d1fb2a34, before any
output, to fix one plant's wording).

**The ruling it runs under.** The author's ruling of 2026-11-15, morning (status file): this seat may compute and print
frame C's outputs, and may not open the data or compare any output with data. No data was opened. Nothing here is set
beside a measured number.

**Not blind, and after the look.**
- The big run's negative (B1944) was known to this seat from main's commit headline before the card (status file).
- So nothing here is a test of frame C, and any read-out it suggests is a fork after the look.

**How it was checked.** Computed once; expectations committed first; tested against planted errors (2, both behaving as
committed).
- **The script and run.** `wf24_run.py` was sealed at 4d1fb2a34 and run once. The output was committed (b58678161) before
  it was read; a partial output was committed unread mid-run (36d7dd9bb).
- **The smoke test.** Before the seal the pipeline ran once with the frame replaced by random numbers. That run showed μ's
  height shares, which do not depend on the frame, so X4 is not blind (disclosed in the script).
- **The frame.** It is this seat's transcription of B1656's frame (W-F22) with this seat's own triplet, re-typed with frame
  C's ingredients:
  - the canonical end from B1927's and B1667's tables, interpolated by this seat's code;
  - Theorem 90's weight;
  - L₂ only, and the readings S and S̃.
  - Its channel norm is B1656's quadrature, where main uses B1924's closed form.
- **The averages.**
  - 154 points of the fundamental domain (heights to 6), times the 24 points of order 5.
  - μ is computed from 1,000 random words of 40 letters (950,783 nodes on their threads, each word weighted by its length,
    as B1928's H3).

## 1. Results

| line | result |
|---|---|
| X1, the height law | **holds, strongly.** At the mark, every sector ratio's log falls with Im τ: over heights 2 to 6, by 5.6 to 20.5 in log, slopes 1.3 to 5.2 per unit of height |
| X2, the fibre's spread | holds: at 49 of the 55 bulk points (Im τ < 1.5), some ratio spans more than a decade over the 24 points (the σ₃/σ₁ ratios, median spread 9 to 21) |
| X3, the fibre's arithmetic loss | **not met: 0 of 55.** The arithmetic mean over the 24 points exceeds the geometric mean by a median factor of 1.03 (σ₂/σ₁) to 1.52 (σ₃/σ₁) |
| X4, μ's heights | not met: μ spends 0.168 of its time above height 2 (0.384 above 1.5, 0.035 above 3, 0.007 above 4). Not blind (the smoke test) |
| X5, the geometric read-out | holds: smaller than frame C's form for every sector ratio, but only by factors of 1.64 to 2.90 |
| plants | PL1 (one point's value times 10) moves the arithmetic mean by exactly (Σ + 9 r_p)/Σ and the geometric one by exactly 10^(1/24). PL2: the composition identity fails for the arithmetic mean and holds for the geometric one |
| reported | the down and the lepton ratios agree at every point, as B1934's "the lepton pair is the down pair transposed" implies for singular values. The read-outs are in `wf24_run_out.txt` and `wf24_summary.json`, not set beside anything |

## 2. What it means

- **The hierarchy is a height variable.** At every point of order 5, frame C's ratios behave as e^(−πE·Im τ) towards the
  cusp (W-F25 finds E rational). So the read-out on the whole is, in effect, the frame at the heights μ visits.
- **Main's diagnosis holds.** The surface average dominates the loss. The fibre's arithmetic mean costs at most about 1.5,
  and the form of the mean costs at most about 3.
- **The measure is the choice of τ in another form.**
  - The uniform measure on the two letters places μ's mass where it is: about 5/6 of the time below height 2.
  - So "no τ is chosen" is not quite what happened: τ's height was chosen by the measure. This is R6 of P-776, which the
    rule carries as "not met as a selection".
- **This seat's first candidate fix is refuted as a fix.**
  - The candidate was the geometric mean.
  - The principle behind it stands: ratios compose, m₁/m₃ = (m₁/m₂)(m₂/m₃), and the only quasi-arithmetic mean that
    commutes with composition for every joint law is the geometric one (proof below). Frame C's arithmetic form breaks
    the composition, as PL2 shows on its own values.
  - But correcting the form moves the read-out by at most a factor of 3, which is not the orders of magnitude a hierarchy
    needs.
- **What follows.** A read-out that keeps the hierarchy must not average the height away. W-F25 reads the frame where its
  hierarchy is exact, at the cusp.

**The composition theorem.**
- Let M_f(X) = f⁻¹(E f(X)), with f continuous and strictly monotone on (0, ∞).
- Suppose M_f(XY) = M_f(X) M_f(Y) for every pair of positive random variables with any joint law.
- Taking Y = c constant gives homogeneity, M_f(cX) = c M_f(X). Homogeneous quasi-arithmetic means are the power means
  (f = x^p, p ≠ 0) and the geometric mean (f = log); this is the classical theorem of Hardy, Littlewood and Pólya,
  *Inequalities*, § 3.
- For p ≠ 0, take Y = X: then M_p(X²) = M_p(X)² means (E X^(2p))^(1/p) = (E X^p)^(2/p), that is, Var(X^p) = 0, which
  fails for every non-constant X.
- So only f = log remains, and it satisfies the condition. For independent X and Y every power mean composes, so the
  dependence matters, and a frame's three ratios at one point are dependent.

## 3. Typed

| statement | how checked |
|---|---|
| the height law at the mark (X1) | computed once, on this seat's transcription; expectations committed first |
| the fibre's spread and its arithmetic loss (X2, X3) | computed once; expectations committed first (X3 not met) |
| μ's height shares (X4) | computed once; the expectation committed first, but seen before the seal (the smoke test) |
| the geometric read-out moves frame C's by a factor of 1.6 to 2.9 (X5) | computed once; expectations committed first |
| the composition theorem | a reading (a short proof, the homogeneity step cited) |
| the measure is the choice of τ in another form | a reading |

## 4. Files

`relays/chat1_2026-11-15_wf24/`: `wf24_run.py` (sealed), `SCRIPT_SHA256.txt`, `wf24_run_out.txt`, `wf24_run_err.txt`
(empty), `wf24_grid.json` and `wf24_summary.json` (the frame's outputs; no data).

This note was pushed before its referee read finished, at the author's word (2026-11-15). The read's corrections follow in a later commit.

0 of 19.
