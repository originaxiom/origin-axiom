# B147 — the chiral pair RRL/RLL is FULLY ARITHMETIC (ℚ(√−7), integral traces); the arithmetic arm collapses (V136)

B146 caught that B145's "no arithmetic chiral o-p-t bundle" arm used the **non-invariant** trace field, and found that
`RRL/RLL` are **chiral** o-p-t bundles whose **invariant** trace field ℚ(√−7) is imaginary-quadratic. But imaginary-
quadratic invariant trace field is only **necessary** for arithmeticity. B147 settles the decisive question by adding
the missing condition.

## The criterion (Maclachlan–Reid, *Arithmetic of Hyperbolic 3-Manifolds*, Thm 8.3.2, non-cocompact)

A cusped finite-covolume Kleinian group is **arithmetic ⟺ its invariant trace field `kM` is imaginary quadratic AND
every trace is an algebraic integer** (for a cusped group the invariant quaternion algebra is automatically `M₂(kM)`,
so the only conditions are the field and the integral-traces test). B125/B145 checked only the imaginary-quadratic half
and **equated** it with arithmeticity — incomplete. B147 adds the integral-traces test.

## Result — RRL/RLL are arithmetic

| bundle | invariant trace field | traces integral? | arithmetic? | chiral? |
|---|---|---|---|---|
| `RL` (figure-eight, m=1) | `x²−x+1` = ℚ(√−3) | yes | **arithmetic** | amphichiral (metallic) |
| `RRLL` (silver, m=2) | `x²+1` = ℚ(i) | yes | **arithmetic** | amphichiral (metallic) |
| **`RRL`, `RLL`** | **`x²−x+2` = ℚ(√−7)** | **yes** | **ARITHMETIC** | **CHIRAL (a mirror pair)** |
| `RRRL` | degree-4 field | — | non-arithmetic (field not imaginary quadratic) | chiral |

The traces are integral because every minimal polynomial (computed via `pari.algdep` on the holonomy traces of the
fundamental-group generators + their pairwise products — a trace-field generating set by Fricke) is **monic**
(|leading coefficient| = 1). So `RRL/RLL` satisfy **both** Maclachlan–Reid conditions: **they are arithmetic CHIRAL
once-punctured-torus bundles.**

The scan over cyclic-primitive R/L words (length ≤ 7) finds exactly **four** arithmetic o-p-t bundles:
`RL` (ℚ(√−3), amphichiral), `RRLL` (ℚ(i), amphichiral), and the **chiral mirror pair `RRL/RLL`** (ℚ(√−7)).

## Independent cross-check — volume = integer × Bianchi covolume (Humbert)

An arithmetic manifold's volume is an integer multiple of its field's Bianchi covolume. This is computed under
sage-python (separate process — cypari clashes with Sage's pari) and recorded in the probe:

| bundle | field | vol / Bianchi covolume |
|---|---|---|
| `RL` | ℚ(√−3) | **12** (matches the known figure-eight value) |
| `RRLL` | ℚ(i) | 12 |
| `RRL`, `RLL` | ℚ(√−7) | **3** |

Every ratio is an integer — the independent confirmation that all four are arithmetic. `RL`'s 12 reproduces the
literature value, validating the method; `RRL/RLL` give 3 (`vol 2.66674 = 3 × 0.888915`).

## What this means

- **B145's arithmeticity arm is REFUTED outright** (not merely "as stated"): arithmetic chiral o-p-t bundles **exist**
  (`RRL/RLL`). "Canonical ⟹ amphichiral" **fails for arithmeticity** — arithmeticity does *not* coincide with
  self-mirror. The surviving "no single canonical object is chiral" rests **only** on the volume-minimality /
  palindromic-period arms (figure-eight is the amphichiral minimum), not on arithmeticity.
- **The cited "exactly two once-punctured-torus bundles" is corrected.** That count (B125/B145) is about the
  **metallic** family (`m=1` golden, `m=2` silver) — still correct as a statement about the metallic bundles. But
  there are **≥ 4 arithmetic o-p-t bundles overall**; arithmeticity is not confined to the metallic m=1,2 pair. The
  metallic m=1,2 arithmeticity result (B125) **stands**; only the loose paraphrase "exactly two o-p-t bundles" was
  over-stated.
- **The firewall SURVIVES — this is a sub-claim correction, NOT a crossing.** `RRL/RLL` are a **mirror pair**, both
  arithmetic. Arithmeticity is **orientation-independent** (the invariant trace field and integral-traces condition are
  mirror-invariant), so by the B146 dichotomy it **cannot prefer a handedness**. The arithmetic arm of B145 collapses,
  but the *conclusion* it was supporting — no canonical selection prefers a handedness — is **untouched**: it now rests
  on the dichotomy + the volume/palindromic arms. **Not** a K-A revival (this is "no canonical preference," not "CS
  picks a side").

## Guard discipline

- **Eager-yes caught and resolved.** `RRL` returning "arithmetic" contradicted the cited "exactly two," so the result
  was held until (a) the integrality test was validated to *discriminate* (a known non-integer, `3/2 → minpoly 2x−3`,
  must read non-monic — this caught a real bug: the leading coefficient must be read at the polynomial's **actual**
  degree, `polcoef(poldegree(p))`, not the search degree), and (b) an **independent** method (volume/Bianchi-covolume,
  Humbert) confirmed it. Two methods agree.
- **MB11** (two-tier): the math (RRL/RLL arithmetic) is stated bare; the firewall reading (no preferred handedness) is
  the POSTULATED layer, citing the math one-way.

## Reproduce

```
python -m pytest tests/test_b147_arithmetic_chiral_bundle.py -q     # 4 passed (pyenv: SnapPy + cypari, NOT Sage)
python frontier/B147_arithmetic_chiral_bundle/probe.py              # full verdict + scan (pyenv)
```

Runs under **plain pyenv** (SnapPy + cypari), **not** sage-python — `import cypari` clashes with Sage's pari (SIGABRT).
The invariant trace field is computed via the shape field + `pari.algdep` (Neumann–Reid; the B125 method), so no Sage
is needed. The volume/Bianchi-covolume cross-check is recorded (it runs under sage-python in a separate process).

**Tier.** MATH. Updates `knowledge/K017` (arithmetic arm refuted outright; firewall survives via the dichotomy),
`docs/STRATEGIC_SYNTHESIS.md` (Campaign 1″ resolved), `docs/OPEN_LEADS.md` (Campaign 1″ resolved), and adds a
calibration note to `frontier/B125_snappy_arithmeticity/probe.py` ("exactly two" → metallic m=1,2; ≥4 overall).
Nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B146 untouched; K-A not revived. Ledger **V136**.

## Addendum (2026-06-11) — the CM volumes behind the Bianchi ratios (review-session, verified)

A cross-session review noted that the two arithmetic *metallic* members have closed-form CM volumes, the
arithmetic content behind the integer Bianchi ratios above:

- **Golden `RL` = figure-eight:** `Vol = (3√3/2)·L(2,χ₋₃)`. **KNOWN** — the classical Bloch–Wigner /
  Humbert / Borel identity (CM volume = a Dirichlet `L`-value over `ℚ(√−3)`); reproduced, not new.
- **Silver `RRLL` (= census `m136`):** `Vol = 4·G = 4·L(2,χ₋₄)`, `G` = Catalan's constant. **NUMERICAL**
  (verified in-session: `Vol = 3.6638623767 = 4G` to snappy precision; `b++LR` confirmed `= 4_1`). This is
  almost certainly the classical `ℚ(i)` / Gaussian analogue of the figure-eight identity (the silver bundle
  is octahedral, each ideal tetrahedron contributing `G`) — **treat as likely-KNOWN pending a literature
  check**; a 10-digit match is evidence, not a proof of the exact identity.
- **The CM sublocus** of the metallic family is `{golden (disc −3), silver (disc −4)}` — exactly the two
  arithmetic members **already banked in B125** (`m≥3` leave the imaginary-quadratic fields); the "exactly
  two, nowhere else" framing rests on the BMR finiteness of arithmetic o-p-t bundles (already cited above).
  Not new beyond B125/K002.
- **Kill (review-session) — `|disc_CM| = κ_m` is NOT a law:** it would give `|−4| = 4` at silver but `κ₂ =
  m²+2 = 6` (`4 ≠ 6`), so the golden "3 = 3"-shaped coincidence (`|−3| = 3 = κ₁`) does **not** generalize.
  Tombstoned (`../../speculations/TOMBSTONES.md`, R3). A shared-integer is not an identity.

Tier: golden `KNOWN`, silver `NUMERICAL`→likely-KNOWN (literature-gated), sublocus = B125. Nothing to
`CLAIMS.md`. See `../../docs/CROSS_SESSION_2026-06-11_disposition.md`.

**Anchors:** B146 (the catch + the dichotomy), B145 (the catalog), B125 (the metallic m=1,2 arithmeticity — stands),
B131 (the κ-fork), `K017`, `docs/STRATEGIC_SYNTHESIS.md`. External: Maclachlan–Reid (arithmeticity = imaginary-
quadratic invariant trace field + integral traces); Humbert (arithmetic volume = integer × Bianchi covolume);
Bowditch–Maclachlan–Reid (arithmetic punctured-torus bundles are finite).
