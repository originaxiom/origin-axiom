# Memo 211 — L72's FLAGGED ISSUE, LOCATED: the cell's machine-readable artifact records a failed run of older code

**Seal:** `outside_bench/seals/L72_PHASE2_AUDIT_PREREG.md`, sha256
`0daa7ada95b244277c404027c03f0eb34424910fcdd3598c9ab14033dd0545cb`, committed before the
certificate was written.
**Certificate:** `outside_bench/certificates/l72_phase2_audit.py` ·
**Output:** `outside_bench/outputs/l72_phase2_audit.txt`
**Outcomes: CELL 1 = B · CELL 2 = A · CELL 3 = A.** Controls C1–C3 all pass.

---

## 0. What was owed

`frontier/B775_phase2_wave1/FINDINGS_WAVE5.md:22`: *"E6 modular data at k=1,2 independently
confirmed consistent … **but the cell's Phase-2 closure claim carries an issue the verifier
flagged. Carry with the issue named.**"* **The issue is named nowhere in the arc.** Memo 210
left it as L72's live remainder.

## 1. CELL 1 — the cell's two committed artifacts disagree. OUTCOME B.

| | `output.txt` | `results.json` |
|---|---|---|
| verdict | **`RESOLVED-A`** | **`UNRESOLVED`** |
| `wall` / `W_computed_wall` | True | **False** |
| `deformation` / `deformation_ok` | True | **False** |
| `theta_odd_directions_exist` | *(not printed)* | **False** |

## 2. And SnapPy is on this box, so the disagreement is settled by running, not by reading

The cell's **unmodified** `compute.py` was copied to an isolated tree with only B581's JSON
beside it and re-run. **20.0 s.**

> **`output.txt` reproduces.** Byte-identical apart from three things: the position of a
> `tkinter` warning line, the runtime stamp (24.8 s → 20.0 s), and one SnapPy
> Chern–Simons value at the 1e-15 level (`-2.22e-15` vs `-1.77e-15`, both zero).
>
> **`results.json` does not.** **51 fields differ**, and it is missing the `gate5` key
> entirely.

**What the stale JSON actually records.** Not a cosmetic drift — a *different, failed*
computation:

| field | committed `results.json` | what the committed code produces |
|---|---|---|
| `G_deformation/per_exponent/{1,4,5,7,8,11}/h1` | **0** for all six | **1** for all six |
| …`/rel_ok` | **False** for all six | **True** for all six |
| …`/exact_Qzeta6` | **absent** | present, `{rel_ok: True, h0: 0, h1: 1, periph_inv: 1}` |
| `G_deformation/lagrangian` | **False** | **True** |
| `B_level1/associator_class` | **absent** | `TRIVIAL` |
| `G_deformation/B581_sign_law_reverified` | **absent** | `True` |

> **The committed machine-readable artifact says the object has `dim H¹ = 0` in every E₆
> exponent block.** That contradicts B581, B575's G4 gates, the cell's own printed output,
> and memo 210's CELL 1 — where the order of vanishing of Δ_E6 at t = 1 came out **exactly
> 6**, one simple zero per exponent, which *is* the six one-dimensional H¹'s.

The JSON is an artifact of an **earlier version of the code**, whose relator check failed
(`rel_ok: False`) and whose H¹ therefore came out zero everywhere; `UNRESOLVED` is the
downstream consequence. **It was never regenerated after the code was fixed.**

**Fence:** the arc never names its flagged issue, so this memo cannot claim to have found
*the* one. It has found **an** issue, it is decisive, and it is reproducible in twenty
seconds.

## 3. CELL 2 — the Deligne splitting rebuilds independently. OUTCOME A.

From an E₆ level-2 stage rebuilt here from the Cartan matrix (the memo-206 instrument; all
stage gates pass, `C = S²` asserted equal to the diagram flip):

| | this bench | P2W5-L72 |
|---|---|---|
| simple currents (qdim 1) | `000000, 000002, 200000` | **same three** |
| closed under fusion | True, cyclic ℤ/3 | ℤ/3 |
| \|det S\| on the pointed part | **0.0352828005** | 0.03528 |
| Müger centraliser | `000000, 010000, 100001`, rank 3 | **same three** |
| centraliser qdims | 1, 1.801938, 2.24698 | same |
| centraliser h mod 1 | 0, 2/7, 6/7 | 0, 6/7, 9/7 → **same mod 1** |

Worst entrywise error of `S^{E6₂} − S^{pointed} ⊗ S^{centraliser}`: **6.229e−15**; for T,
**1.601e−15**. **The splitting is real and independently confirmed.**

## 4. CELL 3 — the Galois ambiguity is removed. OUTCOME A.

The cell identifies the rank-3 factor by matching S and T *entry-by-entry* to SU(2)₅-even at
`q = exp(iπ/7)`. **Modular data does not determine a modular tensor category in general**, so
the whole Galois orbit was swept: `S^{(k')}_{jl} ∝ sin(πk'(2j+1)(2l+1)/7)`, `h^{(k')} = k'·h`.

| k′ | quantum dims | worst \|ΔS\| | worst \|ΔT\| | |
|---|---|---|---|---|
| **1** | 1, 1.801938, 2.24698 | **1.110e−15** | **2.734e−16** | **MATCH** |
| 2 | −1.24698, 0.554958, 1 | 7.667e−01 | 1.564e+00 | reject |
| 3 | −0.801938, 0.445042, 1 | 6.824e−01 | 1.564e+00 | reject |
| 4 | −0.801938, 0.445042, 1 | 7.667e−01 | 1.950e+00 | reject |
| 5 | −1.24698, 0.554958, 1 | 8.510e−01 | 1.950e+00 | reject |
| **6** | **1, 1.801938, 2.24698** | 8.427e−02 | 8.678e−01 | **reject** |

> **k′ = 6 has the SAME quantum dimensions and is still rejected** — on S at 8.4e−2 and on T
> at 8.7e−1. So the quantum dimensions alone do **not** identify the factor, and the cell's
> entry-by-entry S-and-T test was the right instrument, not a loose one. Exactly one
> conjugate survives, and five are rejected (C3, MB12: the sweep discriminates).

## 5. What this leaves

> **INTERPRETIVE.** P2W5-L72's **mathematics is right**, and is now reproduced on an
> independent bench: the splitting, the centraliser, and the identification all hold, with
> the Galois ambiguity — the plausible failure mode behind *"modular data does not determine
> a category"* — explicitly closed. What is broken is the **record**: the one artifact a
> ledger or a sweep would read says `UNRESOLVED` and `h¹ = 0` everywhere.

This is the audit lane's own subject arriving inside a mathematics cell. Memos 207–209
found status lines that disagreed with arcs. **Here a committed JSON disagrees with the
committed code that allegedly produced it**, and the disagreement is not a label but a
failed computation preserved as if it were a result.

**Two actions, neither of them this bench's to take on main:**

1. **Regenerate `frontier/B775_phase2_wave1/cells/P2W5-L72/results.json`** from the
   committed `compute.py`. Twenty seconds, SnapPy present. Until then any consumer of that
   file reads a failed run.
2. **The cell's own remaining residual stands and is narrowed, not discharged:**
   *"uniqueness-up-to-gauge of the level-2 F-symbols (constructed + verified, not
   classified)."* CELL 3 removes the Galois ambiguity. **Classification still requires the
   rank ≤ 4 classification of modular tensor categories from the literature, which this
   bench has not read and does not cite.**

## 6. L72's status after this memo

| | |
|---|---|
| phase 1 (the principal torsion) | **DONE** — memo 210 |
| phase 2 (the 6j at levels 1–2) | **mathematically sound and independently reproduced**; its committed JSON is stale and must be regenerated |
| phase 2's uniqueness residual | **narrowed** (Galois closed), **not discharged** (classification unread) |
| phase 3 (CS along the θ-odd direction) | **WALLED, EXTERNAL** by the cell's own computation: 8112-variable PGL(27,ℂ) Ptolemy, or an extended-Bloch/CCS class for E₆ |
