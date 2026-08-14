# B811 — the promotion gate run: two legal kills, one promotion, and a mis-specified null

cc banking seat, 2026-07-30. **Prereg `6fa4c2c6fa027b44`, sealed and committed at `20170b02`
BEFORE any computation. Gate 5 held throughout — no SM value reaches `CLAIMS.md` under any
outcome of this arc.**

## Why it ran

`METHOD.md`'s lifecycle: **CHECKED** may *"set a diagnostic flag only; route to DORMANT, **never
KILLED**"*; **KILLED** is *"**only** via the full promotion gate → tombstone + residual-hint."*
**B580 Round 1 was a check and it issued KILLED** on H128–H130 — a stage violation, with the ledger
rows still reading `[NOTICED]` above their own kill verdicts. This arc ran the gate that was owed.

## Result against the sealed criteria

Family: `(a·φⁿ + c)/(b·φᵐ + d)`, sealed in advance and **verified to contain all three hinted
forms** — **28,957** distinct values.

| hint | target | σ | `N_hit` | sealed verdict |
|---|---|---|---|---|
| **H128** | α_s(M_Z) = 0.1180 ± 0.0009 | 0.8 % | **37** | **KILLED (legal)** |
| **H129** | sin²θ₁₃ = 0.0220 ± 0.0007 | 3 % | **208** | **KILLED (legal)** |
| **H130** | Koide Q = 2/3 ± 2×10⁻⁵ | 0.003 % | **1** | **PROMOTED** |

**My pre-stated expectation was refuted.** The prereg said I expected KILLED for all three and that
a promotion *"must be reported plainly rather than finding a reason to discount it."* H130 promoted.
Reported.

## H128 — killed on structure, independently of the base rate

α_s(M_Z) is a **running** coupling. Computed here at one loop, n_f = 5:

```
alpha_s(M_Z/2) = 0.13108     alpha_s(M_Z) = 0.11800     alpha_s(10 M_Z) = 0.08862
```

Its value exists **only relative to a chosen scale**. The object is **proved scale-free** (S3/B615).
**A quantity defined only against a scale choice is not the kind of thing a scale-free structure can
emit** — so H128 fails on *kind*, before any counting. The base rate (37 hits) corroborates; it is
not the reason.

## H130 — the promotion is real, and my null was the wrong instrument for it

The single family member inside H130's window **is 2/3 itself** — `(2φ⁰+0)/(3φ⁰+0)`.

The null asked *"how rare is 2/3 among **φ-expressions**?"* But 2/3 is a **simple rational**, and the
window is 3×10⁻⁵ relative. **A φ-family cannot populate that window at all**, because φ is
irrational — only the degenerate `n = m = 0` members are rational. The test could only ever return
1. It measured nothing.

**The hint is a coincidence between two rationals** (Koide's Q and h(27)), so the correct null is a
**simple-fraction family**, which this arc did not seal. That is a **design flaw in my test**,
identified the same way the face classifier (precision 0.45) and the lexicon extractor (process
vocabulary) were — by checking the instrument against what it was actually asked to measure.

**This is not a rescue, and the distinction matters:** I am not discounting the *result*, I am
reporting that the *instrument* was inapplicable. The sealed verdict stands as **PROMOTED**.

**And promotion is the right action anyway** — `PROMOTED` means *a decision to run*, and what must
be run is exactly the properly-specified null. The promotion and the correction are the same act.

**What promotion does NOT mean.** Two independent structural findings stand and neither is touched
by this arc: **B580** — the channel carrying h(27) is **proven information-free** (the level-1 chord
is identical for 4₁, 5₂ **and the unknot**); **B686** — Q = 2/3 is a 120°-parametrisation
statement. A channel that cannot distinguish the object from the unknot cannot carry its physics,
whatever the base rate of 2/3 turns out to be.

## H131 — unchanged

An already-computed **NULL**: no log-periodic golden modulation in Planck 2018 TT residuals, with
the initial 7× excess honestly diagnosed as a Gaussian-smoothing artifact. Nothing to promote.

## Dispositions to apply

- **H128 → KILLED (legal)** — tombstone + residual-hint; kill earned on the level check.
- **H129 → KILLED (legal)** — tombstone + residual-hint; 208 hits and B580's blind check.
- **H130 → PROMOTED** to `OPEN_LEADS` as a **decision to run the correctly-specified null**, with
  B580's and B686's structural findings recorded alongside as the standing obstruction.
- **H131 → NULL**, unchanged.
- The `[NOTICED]` labels on all four rows are wrong and are corrected to their true lifecycle state.

`gate.py` · lock `tests/test_b811_gate.py`
