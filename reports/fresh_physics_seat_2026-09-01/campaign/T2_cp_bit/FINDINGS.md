# T2_cp_bit — L192's object side computed; the sealed comparison written and HELD

**Outside evaluation seat, campaign cell T2, 2026-09-01. Verdict: DESIGN-SEALED.**

> **DISPOSITION (owner election, 2026-09-01, later): HOLD-CLOSED — not fired; licensed row
> retained unspent; L192 closed in `docs/OPEN_LEADS.md` as already answered (B303, negative)
> with B1234's mechanism attached. The sealed design below is a record, not a queue item.
> Re-ask only under the five-line template in `../../CAMPAIGN_TYPE_MATCHED.md`.**
**Gate 5: no measured Standard Model value appears anywhere in this cell** — scripts, results,
design, or this file. The comparison in `SEALED_DESIGN.md` is written and **HELD**, never executed.

## Conventions (stated per E23 discipline)

- **CS normalization:** SnapPy's `Manifold.chern_simons()`, the Riemannian Chern–Simons invariant
  normalized so it is defined **mod ½** for orientable cusped manifolds. **Value group:
  `ℝ/(½)ℤ`**, representatives reduced to `[0, ½)`. This is the convention in which the repo's
  banked statements read exactly: 2-torsion elements of `ℝ/(½)ℤ` are `{0, ¼}`; `CS(m004) = 0`
  and `CS(m003) = ¼` (B1224). Reconciliation is therefore direct — our raw SnapPy outputs
  (`1.35e-16` for m004, `0.25000000` for m003) reduce to exactly those elements; no unit
  conversion (no `π²` factor, which belongs to the complex-volume normalization `ℂ/π²iℤ` of
  B813 Cell 0, **not** used here) was applied or needed.
- **Orientation:** census orientation as loaded by `snappy.Manifold(name)`; no reorientation.
  CS is orientation-odd, but `{0, ¼}` is fixed pointwise under negation mod ½
  (`−¼ ≡ ¼`), so the **bit is orientation-independent** — no orientation choice can flip it.
- **Amphichirality test:** `symmetry_group().is_amphicheiral()` — the authoritative call per
  B1226's recorded catch (`is_isometric_to(mirror)` finds orientation-reversing isometries and is
  not a chirality test).
- **Precision:** every CS value computed at standard double precision AND on the
  `high_precision()` manifold; agreement required (tolerance `1e-6`; the separation to resolve is
  `¼`, six orders larger). Guarded against B1226's second catch (`str()` display artifact) by
  using `float()` throughout.
- **Basis/tolerance:** TOL = `1e-6` on the `[0, ½)` representative, frozen in the script before
  any control was run.

## HALF 1 — the object side, computed (`compute_cp_bit.py` → `results.json`)

**Bit-reading procedure** (frozen): for amphichiral M, `CS mod ½` ≡ 0 → **CP-EVEN**;
≡ ¼ → **CP-ODD**; else **NOT-2-TORSION** (failure). For non-amphichiral M: **UNDEFINED-CHIRAL**
— the ℤ/2 is symmetry-given (B1224) and does not exist without the symmetry.

| manifold | CS (raw, std) | mod ½ | amphichiral | bit |
|---|---|---|---|---|
| **m004** | +1.3e−16 | **0.000000000** | True | **CP-EVEN** |
| **m003** | +0.25000000 | **0.250000000** | True | **CP-ODD** |
| m136 | −0.00000000 | 0.000000000 | True | CP-EVEN |
| m135 | +0.25000000 | 0.250000000 | True | CP-ODD |
| m206 | +0.00000000 | 0.000000000 | True | CP-EVEN |
| m207 | +0.25000000 | 0.250000000 | True | CP-ODD |
| **m208** | +0.00000000 | 0.000000000 | **False** | **UNDEFINED-CHIRAL** |

High precision agrees with standard on all 19 manifolds computed (`precision_agreement_everywhere:
True`).

**Chiral controls — generic CS is NOT in {0, ¼}:** twelve chiral orientable census manifolds
(m006, m007, m009, m010, m011, m015, m016, m017, m019, m022, m023, m026); mod-½ representatives
0.386, 0.364, 0.479, 0.229, 0.308, 0.347, 0.263, 0.097, 0.352, 0.287, 0.037, 0.422 —
**0 of 12 within 1e-6 of {0, ¼}**. The 2-torsion set is special, not generic; the exhibits'
landing exactly on it is the amphichirality theorem at work, not a census artifact.

**m208 reconciled with its banked status:** CS ≡ 0 (as banked) **and** chiral — so it carries no
bit under this procedure. This is the design's guard against reading `CS = 0` alone as CP-even:
the bit is the element of a *forced* ℤ/2, and only amphichirality forces it.

**MB12 bite (named, RUN):** the bit-reading procedure applied to m003 outputs **CP-ODD** —
`MB12_bite_m003_cp_odd: True`. The reading is non-vacuous: it produced the other element on the
sibling, and it produced failure outcomes (UNDEFINED-CHIRAL ×13) on every control where the bit
is not defined.

> **OBJECT-SIDE OUTPUT (one bit): m004 sits at the CP-EVEN element of the ℤ/2.**
> The discriminating pair m003 sits at CP-ODD. Contingent datum, tier (ii) of B1226's form:
> amphichirality forces the ℤ/2; m004's own geometry selects the identity.

HALF-1 checks: 9/9 PASS (see `results.json` → `checks`).

## HALF 2 — the sealed design (`SEALED_DESIGN.md`, HELD)

Written, sealed, **not executed**. Contents, per the L192 licence:

- **Prediction P:** bit(object) = **CP-EVEN** (copied from HALF 1, computed before sealing).
- **Two-outcome criterion:** measured CP-sector configuration classified per channel as
  `CONSISTENT-WITH-CP-EVEN-POINT` (→ CP-EVEN) / `EXCLUDES-ALL-CP-EVEN-POINTS` at a frozen
  `Z* = 5` (→ CP-ODD) / `UNRESOLVED` (→ VOID). Both bit outcomes reachable; primary channel
  designated on type grounds only (the gauge-topological channel, via B813 Cell 0's legitimate
  CS-functional bridge), frozen before any measured status is consulted.
- **B813 clause:** no value crosses (a ℤ/2 element is compared to a ℤ/2 element; a MATCH implies
  no coupling value — `CS ≡ 0` maps to a *set* of CP-even points, not a number); no
  PSL(2,ℂ)→SU(3) map is invoked; the coefficient slot is never written to. The refuted value
  dictionary is not re-entered; B813 stands as the governing theorem.
- **Gate 5 clause:** execution only on the owner's election, by a reader seat; label assignment
  from measurement *is* execution and is outside this cell; post-hoc changes void the execution.
- **Bite control (named, RUN):** `bite_control_design.py` — a hypothetical object at `CS = ¼`
  reads **CP-ODD** (PASS), both reader labels reach their bits, the abstain path works, and both
  MATCH and MISMATCH are expressible. 9/9 PASS.

## Why this cell does not repeat B1027/B1137/B813's error

All three prior box-D probes demanded a continuous value from a bit-valued channel (B1226 Cell 3:
"3/3 asked for a value; 0/3 asked the bit"). This cell's object-side output is cardinality 2 and
its sealed comparison consumes cardinality 2. Nothing in this cell can emit, and the design
cannot consume, a phase magnitude.

## Files

- `compute_cp_bit.py` — HALF 1 computation (snappy); exits 0 on all checks passing.
- `results.json` — full per-manifold data and the 9 named checks.
- `bite_control_design.py` — HALF 2 bite controls on hypotheticals; exits 0 on pass.
- `SEALED_DESIGN.md` — the held design.

## Verdict

**DESIGN-SEALED.** Both halves done; all controls pass (HALF 1: 9/9 including the MB12 bite on
m003; HALF 2: 9/9 including the named CS = ¼ hypothetical). Nothing banked to the repo record;
nothing outside this cell directory touched.
