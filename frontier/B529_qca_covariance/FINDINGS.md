# B529 — The QCA covariance make-or-break: verified, and it does NOT pass as a selection

**What arrived.** The exploration seat's "make-or-break" QCA computation (the LOCALITY gate named by B527 and
the physics-crossing document): a 1D coined quantum walk on the substitution chain, with a "spectral nesting
cost" = mean-squared distance from each level-n eigenphase to its nearest level-(n+1) eigenphase. Claim: the
identity coin is *worst*, the max-mixing coin **iσ_y** is *exact* (cost ~10⁻³²), "the substitution covariance
SELECTS a parameter-free local unitary — the make-or-break is PASSED." Verified independently; the decisive
control the seat itself flagged as unrun (§5c) was run here. Firewalled; nothing to `CLAIMS.md`.

## Reproduced (the handoff's golden table is real)
With a proper (non-degenerate) moving shift, my from-scratch walk reproduces the golden numbers:
| coin | handoff | this trunk (golden, N 66→243) |
|---|---|---|
| identity | 5.6e-5 (worst) | **5.6e-5** ✓ |
| Hadamard | 4.7e-6 | **4.0e-6** ✓ |
| iσ_y | ~10⁻³² (exact) | **0.0** ✓ |
| golden-angle (π/5, 2π/5) | 4.3e-9 | **4.3e-9** ✓ |
So §2's measurements are correct and reproducible — not disputed.

## The decisive control (run here; the seat skipped it) — BOTH candidate coins fail as selections
- **iσ_y's "exactness" is spectral degeneracy + self-similarity, NOT a golden dynamical selection.** The
  iσ_y walk collapses to only **6 distinct eigenphases** (of hundreds) for *any* substitution — a degeneracy
  artifact — and those 6 points are fixed by the *stationary letter-frequencies*. Golden reaches cost **0 at
  every level** because it is exactly self-similar (frequencies identical at all levels); a *random*
  substitution's cost is nonzero at small size (e.g. 3.7e-4 at level 2→3) and drops to **0 by level 3→4** as
  its frequencies stationarize (`qca_controls.py`: golden=0, tetranacci=0, random=0 at matched size 243/256).
  So the coin is **generic** — it collapses every substitution to its stationary 6-point spectrum; golden is
  exact-at-finite-level only by self-similarity, which *any* substitution achieves asymptotically. The
  physics-crossing kill-rule ("controls reproduce the signal") fires. **The "parameter-free iσ_y coin
  *selected by covariance*" claim is refuted — iσ_y selects self-similarity, not the golden object.**
- **The golden-angle coin is NOT robustly special either.** It *embeds* φ (cos π/5 = φ/2) and looked like a
  genuine selection on the first two controls (golden 4.3e-9 vs tetranacci 1.4e-4, random 2.0e-6). But over
  **10 random controls at matched size** (`golden_angle_robustness.py`), golden beats **8/10 and loses to 2**
  (two random substitutions nest *better* than golden). So golden sits in the good tail, but the effect is
  **not golden-exclusive** — by the strict kill-rule (controls must not reproduce), it does not pass as a
  clean selection. *(A weak affinity is real — golden is better than ~80% of randoms with the φ-embedding
  coin — but it is a good-tail effect, not a decisive selection; firewalled, not a crossing.)*

## Verdict: the make-or-break LOCALITY gate is NOT passed
Neither candidate coin is a genuine golden-specific parameter-free local unitary: **iσ_y is generic** (a
spectral-degeneracy triviality), and the **golden-angle coin is a non-robust good-tail effect** (2/10 controls
beat it). Covariance-as-spectral-nesting does **not** select a golden-specific coin. The physics-crossing
route's LOCALITY gate — "a parameter-free or finitely-selected local unitary picked out by the object" — is
**not** cleared by this computation. (The seat's "PASSED" was premature: it rested on the iσ_y exactness
without the control, which shows the exactness is generic.)

## Method note (the discipline cut both ways this time)
Given the standing "serial false killer" caution, I did **not** dismiss the handoff — I reproduced its golden
table, and I chased the golden-angle coin as a *possible real selection* rather than killing it with the iσ_y
refutation. But I also almost **false-positived** it: two controls looked like a clean selection; ten controls
showed it is not. The rule held in both directions — **compute the discriminating fact (here: enough controls
to see the tail), don't stop at the first flattering or damning one.**

Consistent with PHYS-REFUTED and the K025 metric-cone finding (the object does not *select* — here it does not
select the local unitary either). Locks: `tests/test_b529.py`. Reproducers: `qca_controls.py`,
`golden_angle_robustness.py`. Cross-refs: [[B527]] (metric cone; LOCALITY was the named next gate), [[B525]]
(the discriminating-fact rule), docs/CLOSURE_2026-07-11 (PHYS-REFUTED).
