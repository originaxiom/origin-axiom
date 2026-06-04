# Physics-probe map — which framework→physics crossings are real, which are shut

**Date:** 2026-06-04. **Status:** exploratory, **uncommitted** (review pending). Proven core
P1–P16 untouched. Probes from the physics-probe planning pass (`PHYSICS_COMPUTATION_PLAN.md`),
**independently re-run and verified here**; the verdicts and caveats below are this session's
verification, not the plan's self-report.

## One-line map

The trace-map framework crosses into **real but established 1D condensed-matter physics at SL(2)**,
and **nowhere else**: the most thesis-aligned probe (emergent geometry) came back **no**, and the
SL(n≥3) tower has **no physical (transfer-matrix) realization** for a structural reason. No probe
reaches the founding thesis. That map — including the shut doors — is the deliverable.

## TIER 1 — verified (re-run this session)

| probe | result | verdict | what it actually is |
|---|---|---|---|
| **Path 1** (`path1_quasicrystal.py`) | trace map from physical transfer matrices, viol 3e-15; Fricke–Vogt `I=(δ/2)²` exact, E-independent (spread ~1e-16); Cantor spectrum | **VERIFIED** | the **standard Fibonacci quasicrystal** (Kohmoto–Kadanoff–Tang 1983). Real, *known*. |
| **Path 1b** (`path1b_gaplabeling.py` + `path1b_control.py`) | 12/12 gaps on `{nω mod 1}`, 8/12 at err<0.001 (median 0.0000); control: periodic/random have no gaps to label, random baseline ~0.4 hits | **VERIFIED & significant** | the **gap-labeling theorem** (Bellissard). Real topology→physics, *known*. |
| **Path 7** (`path7_emergent.py`) | (B) factor complexity `p(k)=k+1` exact (Sturmian, zero entropy) → linear counting; (A) EE log-slopes q=0.184/per=0.159/rand=0.102 | **NEGATIVE (via B)** | emergent-geometry precondition: the natural counting is the **wrong kind**. |

### Two caveats found in verification (not in the plan's self-report)

1. **Path 7(A) is not well-calibrated and does not carry the result.** Its own printed slopes have
   *periodic* at 0.159, but periodic should be `1/3` if (A) were certifying "c=1 critical" — so (A)
   cannot cleanly certify the quasicrystal as critical (the slopes are finite-size-contaminated and
   barely separated). **The Path 7 negative rests entirely on (B)** — the exact, un-fakeable linear
   complexity `p(k)=k+1` and the tower entropy `n·log μ` — which is solid. The writeup's claim that
   (A) "clears the necessary precondition" is overstated; treat (A) as inconclusive.
2. **Path 1b's lattice search has an inert parameter and shipped without its control.** In
   `(m+nω) mod 1`, the integer `m` is inert (`m mod 1 = 0`), so the real search is `{nω mod 1}`,
   `n∈[−8,8]` (17 values); the reported `m=−8` is meaningless. The promised periodic/random control
   was **missing from the script** — added in `path1b_control.py`. With it the result holds and is
   significant (8 hits at err<0.001 vs a ~0.4 random baseline; periodic/random have no gaps at all).

**Honest scope of TIER 1:** Path 1 and 1b are *correct* and *real*, but they are **rediscoveries of
textbook quasicrystal physics**, not new results — cite KKT/Bellissard, do not claim. They are "1D
condensed matter, not the thesis," exactly as the plan says.

## Path 1-SL(n) — the "one live target" — is NEGATIVE, structurally (no big probe needed)

The plan's one genuinely-novel TIER-1 question: does an `n`-channel chain realize the **SL(n)** trace
map, so the tower's `a_d` control a real spectrum? **Answer: no, for a structural reason already
evidenced in the repo (B52).**

- A 1D `n`-orbital tight-binding chain has `2n×2n` transfer matrices that preserve the
  Wronskian/current symplectic form ⇒ they live in **`Sp(2n,ℝ)`**, not `SL(n)`.
- The coincidence **`Sp(2)=SL(2)`** is *exactly why* the single-channel case (Path 1) realizes the
  SL(2) trace map — and it is the **only** `n` where the groups coincide. For `n≥2` channels,
  `Sp(2n) ≠ SL(n)`.
- **B52** (`frontier/B52_multichannel_fibonacci_bridge_control/`, Ledger) already verified this for
  `n=3`: the naive 3-channel model gives `6×6` **symplectic** transfer matrices with a **sixth**-order
  trace recursion — not SL(3)'s third-order Cayley–Hamilton recursion.

**Conclusion:** the SL(n≥3) tower is a pure-math object — `Out(F₂)`-dynamics on the `SL(n,C)`
character variety of `F₂` — with **no natural 1D-Hamiltonian (transfer-matrix) realization**. This
is recorded as a NEGATIVE; it closes the "live" TIER-1 target at the cost of a structural argument
(not a multi-session model search). Scope note: this rules out the *natural transfer-matrix*
realization; it does not (and cannot) prove no exotic physical system anywhere realizes `SL(n)`.

## The full map (TIER 2–4, not run — by the plan's own ratings, low marginal value)

- **TIER 2** (Path 4 adjoint torsion, Path 3 A-polynomial prep): topological cross-checks /
  object-prep for a future expert. Real but do **not** cross to dynamics. Path 3 (extend B67's
  A-polynomial to the metallic mapping tori) is the genuinely expert-worthy *object* — worth building
  only if/when an expert is engaged.
- **TIER 3** (Path 5 gauge, Path 6 cosmological constant): thesis-relevant but blocked. Path 5 is
  numerology-risk (expect "only resembles"); Path 6 is already a repo kill — do not refit.

## Bottom line

Both independent sweeps — the math line (`a_d`, Phase A) and this physics line — converge: the work
is real, honest, and modest, and **the founding thesis is not being approached by either**. The
genuinely new things to bank are **B67** (figure-eight A-polynomial from the trace map) and the
**candidate `a_d` formula** (`B58_phaseA/CANDIDATE_A_D.md`); the quasicrystal/gap-labeling crossings
are real but textbook. The most valuable next moves are an **expert read** (B67 + PC12 + candidate)
and settling `a_d` via the **smooth fixed-line point** computation — not grinding TIER 2–4.

## References (the textbook physics that Path 1/1b reproduce)

- M. Kohmoto, L. P. Kadanoff, C. Tang, *Localization Problem in One Dimension: Mapping and Escape*,
  Phys. Rev. Lett. **50**, 1870 (1983) — the Fibonacci trace map.
- S. Ostlund, R. Pandit, D. Rand, H. J. Schellnhuber, E. D. Siggia, Phys. Rev. Lett. **50**, 1873
  (1983) — companion (almost-periodic Schrödinger).
- A. Sütő, *The spectrum of a quasiperiodic Schrödinger operator*, Commun. Math. Phys. **111**, 409
  (1987); J. Stat. Phys. **56**, 525 (1989) — singular-continuous / zero-Lebesgue (Cantor) spectrum.
- J. Bellissard, *Gap labelling theorems for Schrödinger operators*, in *From Number Theory to
  Physics* (Springer, 1992) — the IDOS-in-`Z+Zω` labels.
- (Sturmian complexity `p(k)=k+1`: Morse–Hedlund; the Fibonacci word is the canonical Sturmian word.)
