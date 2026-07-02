# B367 (W2.3) — the value-map s(m₁,m₂): step 0 — the exact six-pair matrices

**Status: banked COMPLETE (frontier). Step 0 (the exact six-pair matrices) passed every pre-registered
check and refuted the B361 local law; the V3 hypothesis stage ran exactly as pre-registered and returned
outcome (B): NO uniform CRT-local product formula at the declared complexity — the exact table + the graded
obstruction bank as the channel's exhibit. Pre-registration: `PREREGISTRATION.md` (PR #442, committed before
any computation). Firewalled; nothing to `CLAIMS.md`.**

## What step 0 computed

All six pair s-matrices for seeds m ∈ {1,2,3,4}, fully identified — every entry an exact element of
H = ℚ(√5, √−3), no PSLQ, no floats (`step0_exact_matrices.py`; tables in `step0_tables.json`). The
theta-lift Weil matrices are rebuilt from scratch (W_m = WR^m·D^m in the B358 ℚ(ζ₆₀) engine); labels are
raw eigenvalue exponents. Gates all passed: orders (20, 12, 6, 20 for m = 1,2,3,4), ΣP_a = I and
idempotence exact, single-seed controls clean (the seam remains pair-exclusive), and every row and column
of every s-matrix sums to 0 exactly (the forced ΣQ = I sum rule — S0.1).

## The pre-registered checks (S0.2–S0.7): all passed

- **S0.2** — the eight previously PSLQ-identified (1,2) entries reproduce exactly (relayed independent
  computation, cross-session): (0,4) = +1/48 … (15,11) = −1/480, at the index↔exponent dictionary recorded
  in the module.
- **S0.6** — the relayed full 11×11 (1,2) matrix reproduces **entry-by-entry**; its structure claims are
  now exact: **rank 4**; **Coxeter-oddness** `s(a, 12−b) = −s(a,b)` for all (a,b); the {4,8}-support
  sector is exactly the rows {0,4} and is disjoint from the rest.
- **S0.3** — the six ±1/144 entries of (2,3) reproduce; **the pre-registered prediction hit**: the full
  value set is {±1/144, **±1/288**} — the ±1/288 entries are precisely what the height-blocked partial
  identification could not see.
- **S0.4** — the (1,3) and (1,4) zeros upgrade to **exact tier**: every entry of both tables has √−15
  coefficient exactly 0, at full identification (the √−3 component is present in pair traces generally;
  the zero statement is the seam coefficient).
- **S0.5** — first complete (2,4) and (3,4) tables: value sets {±1/120, ±1/240, ±1/480} and
  {±1/48, **±1/96**} (the ±1/96 values are new).
- **S0.7** — the exact aggregates Σs² (supersede all partial-coverage values):

  | pair | (1,2) | (3,4) | (2,4) | (2,3) | (1,3) | (1,4) |
  |---|---|---|---|---|---|---|
  | Σs² | **43/7200** | **1/192** | **3/3200** | **1/2304** | **0** | **0** |

  Ordering: (1,2) > (3,4) > (2,4) > (2,3) > 0 = 0, a ~14× spread of exact rationals with two exact zeros.

- **V1 (denominator hypothesis) holds on all data**: every |s| ∈ {1/48, 1/96, 1/120, 1/144, 1/160, 1/240,
  1/288, 1/480} is 2^a·3^b·5^c with a ≤ 5, b ≤ 2, c ≤ 1.

## Step 0's own discovery: the local law (B361) is REFUTED at pair (3,4)

The banked selection rule — *bright ⇔ the pair contains a seed elliptic at both primes* (11 pairs, 0
counterexamples) — **fails on the twelfth pair**: (3,4) contains no such seed (m=3 is 3-trivial, elliptic
only at 5; m=4 is 5-parabolic, elliptic only at 3) yet is **bright**, with the second-largest aggregate
(1/192) — confirmed by two independent computations (this table; the relayed partial ±1/48 entries). The
minimal repair ("each prime covered by some seed of the pair") is refuted in the same table: (1,3) has the
identical covering pattern and is **exactly dark**. Since W₁ and W₄ have identical level-15 spectra, the
discordant pair {(1,3) dark, (3,4) bright} shows **the support pattern is strictly finer than spectra +
local ellipticity types** — the finer-than-spectrum phenomenon, previously seen in the values, now
operates at the support level. (The V3 search is *not* pre-refuted: its declared inputs are m mod 3 and
m mod 5, and 1 ≢ 4 mod 5 — what died is the coarser type-level law.)

## The V3 verdict (outcome B): no local-symbol product formula at declared complexity

The pre-registered model — `s = X3[e₃a, e₃b, m₁%3, m₂%3] · X5[e₅a, e₅b, m₁%5, m₂%5] · X4[e₄a, e₄b]`,
solved by exact multiplicative tensor completion over ℚ (`v3_search.py`) — **fails on the true data**
(`true_pass: False`) while **0 of 200** support/sign/denominator-matched random tables pass, so the test
has teeth and the failure is informative, not vacuous. The diagnosis is sharply graded:

- **Per-pair:** (2,4) and (2,3) *do* factor into the CRT-local form individually; **(1,2) and (3,4) do
  not** — the rank-4 pair and the law-breaking pair are exactly the locally-unfactorable ones.
- **Uniformity:** every two-pair joint is inconsistent — including (2,3)+(2,4), which share seed 2. No two
  pairs admit common local tables.
- **Exact ranks** of the bright s-matrices: (1,2) = 4, (2,3) = 2, (2,4) = 1, (3,4) = 2. Rank alone does
  not decide local factorability ((2,3) factors at rank 2; (3,4) fails at rank 2).

Together with the law refutation above, the conclusion of the probe: **the value map is not a function of
CRT-local data at level 15** — neither its support (the law) nor its values (V3) factor through
(m mod 3, m mod 5, CRT labels). The seam form is an eigenbasis-geometry invariant in a strong sense: any
closed form must use data finer than everything local tried here (candidate finer inputs, for a FUTURE
pre-registration only: the seeds' fixed-point quadratic forms — disc 5 vs 20 distinguishes m=1 from m=4 —
or Galois-cocycle data of the eigenbases). Per the pre-registration, the lead closes **at this complexity
budget** (label: open at higher complexity, not "impossible"); the exact six-pair table is the exhibit.

## What this changes

The reconciliation substrate is complete: three independent computations (two relayed cross-session, one
this probe — different machinery, different conventions) now agree on every comparable entry, and the
remaining disagreements were all coverage artifacts, resolved in this table's favor. The value-map hunt
(the V3 local-symbol search, the 200-random-table null, the held-out pairs (2,7)/(3,7) and the exact
zeros) runs next, exactly as pre-registered — nothing in this step licenses a formula claim yet.

**Provenance.** B358 (engine + flagship), B359/B360 (partial tables, superseded by this exact set),
B361/B362 (the local law — REFUTED above at (3,4); its 11 confirming pairs stand as data), B366 (why the
theta lift is the forced object to compute in). Reproducer: `step0_exact_matrices.py` (~13 min, pure Fractions); locks:
`tests/test_b367_step0.py` (5 always-on from the banked tables + 1 OA_SLOW regeneration).
