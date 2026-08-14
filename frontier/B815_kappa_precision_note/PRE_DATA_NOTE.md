# B815 — the calibration gate's own precision, recorded BEFORE the ratings arrive

cc banking seat, 2026-07-30. **Written and committed while the wave-2 workflow is still running
and no rating has been seen.** That timing is the whole point: a precision caveat discovered after
a borderline result is indistinguishable from an excuse.

## What was measured

The Fleiss' κ instrument (`scripts/checks/fleiss_kappa.py`) was built and verified against Fleiss'
published worked example — **10 subjects × 14 raters × 5 categories, κ = 0.210, reproduced exactly**
(`tests/test_fleiss_kappa.py`, 12 locks). It was then run on *synthetic* data shaped exactly like
wave 2's calibration block: **12 raters × 15 items × 4 categories**, with each rater agreeing with
a latent ground truth **85 %** of the time.

| quantity | value |
|---|---|
| per-rater fidelity to latent truth | **0.85** (by construction) |
| Fleiss' κ | **0.7695** |
| bootstrap 95 % CI over items | **[0.6549, 0.8471]** |
| sealed gate | **κ ≥ 0.75** |

## Two facts that follow, and neither is about our data

1. **The 0.75 gate is a demanding bar.** Raters who individually agree with the truth 85 % of the
   time land at κ ≈ 0.77 — *just* over. The sealed threshold is not a formality; it corresponds to
   roughly 85 %+ per-rater fidelity across a 4-category vocabulary.
2. **Fifteen items cannot resolve the gate to better than about ±0.10.** The CI on a κ of 0.77
   spans 0.65 → 0.85 and **straddles the threshold**. A point estimate near 0.75 is therefore
   compatible with a true κ on either side of it.

## The rule this fixes in advance

**The sealed gate is NOT loosened.** It stays exactly as sealed: **κ ≥ 0.75 to write, below to
hold.** Changing a threshold after building the instrument that measures it would be the same
error as moving a falsifier, and it is refused here.

**What is added is a reporting obligation, and adding it can only make the result more honest:**

> Whenever the point estimate passes but the CI's lower bound falls below the gate, the pass is
> reported as **PASS (marginal — the 15-item block cannot resolve the gate to better than ±0.10)**,
> with the interval printed alongside. The verdicts are written, because the sealed rule says so —
> but nobody later reads that κ as settled when it was not.

Symmetrically: a **FAIL** whose CI's *upper* bound sits above the gate is reported as
**HOLD (marginal)** — held, per the sealed rule, but not as a finding that the panel definitely
disagrees.

## Why record it separately rather than fold it into the wave-2 arc

Because the credibility of the caveat depends entirely on its timestamp. Committed now, it
constrains how the result may be read no matter which way it lands. Committed afterwards, it would
be worth nothing — and would look like exactly what it was not.

**Nothing here is a result about the object.** It is a measurement of the measuring instrument.
Gate 5 untouched.
