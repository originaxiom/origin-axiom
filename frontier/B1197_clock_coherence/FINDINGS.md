# B1197 — THE CLOCK-COHERENCE RUN (route B4, the D2 gate): SPLIT — the named ladder passes, the census fails globally

**Status: banked (frontier). Verdict PROVED** (the coherence measurement, with two positive controls
and a bite control). Executed the moment 5A returned, per the owner's standing instruction.
`verification/` carries both scripts + both result sets. Gate 5 clean (geometry only).

## The condition under test (cloud's weld-book addendum 2, verbatim scope)

Paying **LEAP-1** (CS-time conjugate to Λ, Alexander–Magueijo–Smolin) and **W1** (4-volume-time
conjugate to Λ, Hartle–Thorne) TOGETHER requires CS-time and volume-time to be **the same clock up
to monotone reparameterization** — two variables conjugate to the same Λ must agree up to canonical
transformation. Testable: **along the (1,n) ladder CS must be monotone in Vol**, with the full check
across **B289's banked 78-closing census** (|p|,|q| ≤ 8, gcd = 1). Cloud's declared two-outcome:
monotone ⇒ jointly payable (LEAP-1's price unchanged); non-monotone ⇒ the joint package is refuted
and the choice becomes AMS-clock XOR HT-clock.

## Two catches before any verdict (narrated, both mine)

1. **WRONG CENSUS, caught by re-reading the source.** The first run swept the **112-member
   shape-field family** (B1186) — a set of distinct manifolds — when the condition is about the
   **Dehn-filling closings of m004**. Different objects entirely; that run's non-monotone output is
   discarded as off-target, not reported.
2. **VACUITY TRAP, caught by my own counters.** The corrected run's first pass returned an **empty**
   census (0 closings) because SnapPy's CS fudge must be primed on the *unfilled* manifold before
   filling (B289's instrument does exactly this: `_ = float(M.chern_simons())` then `dehn_fill`).
   With an empty sequence `all(...)` returns True — the run printed "MONOTONE: True" over nothing.
   Caught because the census size was printed alongside; a **vacuity guard** (assert ≥ 10 rungs) is
   now in the committed script. The MB12 class, self-caught pre-bank.

## The instrument, controlled two-sidedly

- **Positive control 1**: the corrected sweep finds **exactly 78** distinct hyperbolic closings up to
  (p,q) ~ (−p,−q) — B289's banked census size, reproduced independently.
- **Positive control 2**: B289's banked sign law **CS(p,−q) = −CS(p,q)** holds **156/156** on the
  mirror pairs — the banked positive reproduces.
- **Bite control**: shuffling |CS| against the same volume order yields **36 violations** — the
  monotonicity detector demonstrably fires when the structure is absent.

## THE RESULT — a split, with exact witnesses

**The named primary test PASSES.** The **(1,n) ladder**, extended to n = 2…30 (29 rungs): Vol
strictly increasing 1.398508884 → 2.026719753 (→ Vol_cusp = 2.029883212819), |CS| strictly
decreasing 0.246607253 → 0.016665127 (→ 0). Monotone in both, no exceptions. The p = 1 family in the
census (14 members) is likewise monotone.

**The full census check FAILS.** Globally across the 78 closings sorted by volume, |CS| is **not**
non-increasing: **15 violations**. And **every family p ≥ 2 carries a within-family violation**, each
exhibited:

| family | witness (|CS| rises as Vol rises) |
|---|---|
| p=2 | (2,−3) V=1.737124 \|CS\|=0.169123 → (2,5) V=1.919520 \|CS\|=0.200608 |
| p=3 | (3,4) V=1.863443 \|CS\|=0.126674 → (3,5) V=1.921027 \|CS\|=0.199099 |
| p=4 | (4,−5) V=1.923087 \|CS\|=0.101181 → (4,−7) V=1.973762 \|CS\|=0.142402 |
| p=5 | (5,−1) V=0.981369 \|CS\|=0.077038 → (5,−2) V=1.529477 \|CS\|=0.234622 |
| p=6 | (6,−1) V=1.284485 \|CS\|=0.067932 → (6,5) V=1.928668 \|CS\|=0.098310 |
| p=7 | (7,−1) V=1.463777 \|CS\|=0.060617 → (7,2) V=1.649610 \|CS\|=0.231986 |
| p=8 | (8,1) V=1.583167 \|CS\|=0.054637 → (8,3) V=1.824344 \|CS\|=0.174195 |

Structural observation (interpretive, labeled): the families sit at **different |CS| scales** — the
(p,±1) closings carry small |CS| at low volume while the (1,n) and (p,±2..) closings carry large
|CS| — so the global failure is a *family-stratification* effect, not noise.

## What this does to D2 (the routed consequence)

**Neither of cloud's two declared outcomes fires cleanly.** The coherence condition holds exactly
where the record's asymptotics pointed (the cusp-approaching (1,n) ladder — the trajectory
B289/B303 single out, |CS| → 0 with Vol ↗ Vol_cusp toward the amphichiral origin) and fails
everywhere else. So **D2 sharpens from a computation to a scope question, and it is the owner's**:

- **If the physical clock is a single realized trajectory** (one path through time — and the (1,n)
  ladder is the record's own distinguished path), the joint LEAP-1+W1 package **survives its test**
  and is payable at the price cloud stated.
- **If coherence must hold across the whole closing census** (all slopes simultaneously — the
  stronger reading of "the same clock up to monotone reparameterization", which is a statement about
  the two *variables*, not one path), the joint package is **refuted**, and the choice becomes
  AMS-clock XOR HT-clock exactly as cloud specified.

Both readings are defensible; the run cannot choose between them, and saying so is the honest
verdict. The measurement is now banked so the decision is made on data rather than in advance.

## Fences

CS is SnapPy's `chern_simons()` (mod 1), reduced to [−1/2, 1/2) and taken in absolute value; B289
established that this agrees with Im(complex_volume)/(2π²) mod 1/2 across the same census, and this
run reproduces B289's sign law as its control. The ladder extension beyond the |q| ≤ 8 box (n up to
30) is outside B289's banked census box and is reported as such (its monotonicity is this arc's own
computation). "Monotone reparameterization" is interpreted as a monotone relation between the two
quantities; the trajectory-vs-variable scope distinction is exactly the open half handed to the
owner. No firewall crossing; no measured value.
