# B791 — Weyl completeness criterion + independent verification of the B788 bank

> ### ⚠ TWO CORRECTIONS POSTED 2026-07-28 — read before using anything below
> 1. **The per-sector count is dim(V_i)·W(T), NOT W(T)** (`sector_count_correction.py`).
>    §2's uniform criterion carried a factor error. **Chat-1's headline "live defect" in §3
>    EVAPORATES**: Gate 9's sealed interval CAN discharge Gate 5. The real bug is the hand-set
>    screen cap — cc's separate catch, now the whole story rather than an addendum.
> 2. **λ₁(parent) = 51.014 is UNSOURCED** (`PROVENANCE_ALERT.md`). §4's second calibration point
>    has no retrievable source and may be model-fabricated. **GATE8R2 must not execute.** The
>    0.344 % Weyl agreement is withdrawn as evidence — it is consistent with fabrication.

**Receipt on B788** (`frontier/B788_maass_spectrum_programme`, the external Gates 0–9R Maass
bank). Companion receipt: **B790** (cc's adjudication of the original Chat-1 handoff).
Gate 5 + Gate 5-Q binding. **Nothing here reaches CLAIMS.md.**

## Attribution

The **Weyl completeness criterion is Chat-1's** (verification receipt, 2026-07-28), as is the
Gate-9/Gate-5 mismatch and the second-calibration-point proposal. This arc is cc's **independent
re-derivation and verification**, plus two additions of cc's own (marked below). Nothing here is
banked on Chat-1's arithmetic; the Humbert volume is recomputed from the L-value and every table
row regenerated.

---

## 1. Independent verification of the bank's structural claims

Method: read **only** the four generator permutations from `outputs/coset_action.json` and
regenerate everything downstream. No summary field used as an input; summaries compared only at
the end. (`verify_bank_structure.py`)

| Bank claim | cc's independent result | |
|---|---|---|
| image order 1920 | closure gives **1920** | ✓ |
| transitive on 12 cosets | orbit of 0 = all 12 | ✓ |
| commutant dimension 3 | rank 141 ⇒ 144 − 141 = **3** | ✓ |
| orbital sizes [12, 12, 120] | **[12, 12, 120]** | ✓ |
| ⟨χ,χ⟩ = 3, ⟨χ,1⟩ = 1 | exactly **3** and **1** (as Fractions) from fp-dist {0:1145, 2:624, 4:135, 8:15, 12:1} | ✓ |
| τ central, fixed-point-free, τ²=1 | in G, τ²=1, no fixed points, commutes with all 1920 | ✓ |
| ρ = V₁ ⊕ V₅ ⊕ V₆, parities +,+,− | τ-eigenspaces 6+6, trivial in the +1 side | ✓ |
| index 12 | Humbert volume, **independent of the coset route** | ✓ |
| `point_stabilizer_order` 320 vs 160 | ambient 3840/12 = 320; image 1920/12 = 160; kernel 2 | **not a discrepancy** |

**The decomposition is forced, not fitted.** τ central and fixed-point-free ⇒ its ∓1 eigenspaces
are each 6-dimensional and G-invariant; the trivial rep lies in the +1 side; with ⟨χ,χ⟩ = 3 the
only possible split is 1 + 5 + 6 with the 6 odd. No choice enters. This removes the
decomposition from the class of things that could be a numerical artifact.

## 2. The criterion (Chat-1's; re-derived here)

L²(Γ₄₁\H³) = L²(Γ_p\H³, E), E = Ind 1 of rank 12 = E₁ ⊕ E₅ ⊕ E₆ of ranks 1, 5, 6. Weyl for a
flat bundle counts *with multiplicity* as rank(E_i)·W(T); a V_i-isotypic eigenspace has dimension
a multiple of dim V_i; so under generic multiplicity the count of **distinct** parameters is

> **N_i(T) ≈ W(T) — the same in every sector, including the parent.**

    W = Vol(PSL(2,O_3)\H^3)/(6 pi^2) = 0.002856530136

**Consistency check (the load-bearing step):** Σ_i dim(V_i)·W = 12·W = Vol(m004)/(6π²).
Verified exactly. The arithmetic identity 1 + 5 + 6 = 12 is what makes the budget uniform.

| r ≤ | 5.0 | 8.0 | 10.0 | 12.0 | 15.2 | 18.0 | 20.0 | 24.5 |
|---|---|---|---|---|---|---|---|---|
| N_i(T) | 0.357 | 1.463 | 2.857 | 4.936 | 10.03 | 16.66 | 22.85 | 42.01 |

Value: it guards the dominant Hejhal failure mode — **silently skipped eigenvalues** — with no
reference to any physical value, so it is inert with respect to Gate 5.

## 3. The live defect, verified against the sealed JSON

- `GATE5_PROTOCOL.json`: `distinct_eigenvalues_per_sector = 10`, `trial_count = 80`.
- `GATE9_PROTOCOL.json`: `search_interval = ["0.50","12.00"]`.
- Budget on that interval: **μ = 4.936 per sector**. Ten per sector needs **r = 15.184**.

> **Gate 9 as sealed buys ~49 % of what Gate 5 requires.** Cost of extending 12 → 15.2 is
> **2.03×** spectral volume. Found without running anything; resolve before re-running.

### cc's addition — the arbitrary constant this replaces

`GATE9_PROTOCOL.json` sets `screen.maximum_minima_per_sector = 24`, **hand-set, not derived**.
Gate 9's screen retained **V₅ = 25, V₆ = 24**, so the run failed its own guard
`screen_minimum_cap_respected` **against an arbitrary cap**. W(T) supplies the principled
replacement: a cap stated as a multiple of μ, with the confirmation stage expected to return to
≈ μ. This makes "calibrate then extend" the fix for the **actual failure cause**, not a general
improvement.

## 4. cc's addition — the single-point-of-failure in the calibration

The bank's whole external anchor is `DCHY2025_EIS_ODD_24_5033`: **one value, 4 printed decimals,
marked "approximately", read from a Figure 4 caption.** Gate 8R's 10-digit agreement is
**between two heights** — internal consistency, not a literature match, exactly as Chat-1
characterises it. Two heights at one r cannot pin **r-dependent** truncation, and Gate 8 died on
truncation.

Chat-1's resolution, verified here: the second point was already inside B790's S1.
λ₁(parent) = 51.014 ⇒ **r = 7.072057692**, and

- Weyl W(T) = 1 predicts r = 7.047802574 — **0.344 %** agreement;
- **W(7.0721) = 1.010** — it *is* the ground state, so λ₁(m004) ≤ 51.014 is likely **tight on V₁**;
- W(24.5033) = 42.03 — the opposite spectral end from the existing control;
- mode-budget ratio **3.465×**, which is precisely the axis truncation moves along.

Sealed as `GATE8R2_PREREGISTRATION.md` — **localisation, not precision**: a weak target and a
strong falsifier, window ±0.005 fixed by the source's precision and not tightenable after the
fact. **Provenance caveat carried forward:** 51.014 reached cc via a *secondary* report of Table
3 and remains UNVERIFIED; the Weyl cross-check is corroboration, not verification — a
transcription error of the right size would survive it. It must be checked against the primary
before the gate executes.

## 5. Replication, and a scheduling defect (logged separately)

cc3 committed `89fc6794` "B788 Step 2: [PSL(2,O₃):Γ₄₁] = 12 exact" **hours after cc banked the
same result**. Two readings, both true, and they should not be collapsed:

- **On the evidence side: accidental independent replication.** Two seats, different code paths,
  same exact index by the same Humbert route — the output the two-seat gate exists to
  manufacture, obtained free. Banked as replication, citing both.
- **On the coordination side: a scheduling defect.** cc3 was working from a clone that had not
  taken main, so a banked result was re-derived instead of built on. That is a relay-cadence
  failure, not a research failure, and it is logged as such rather than written up as waste.

## 6. Sequence adopted

1. **Bank the Weyl criterion** — this arc. ✅
2. **Gate 8R2 localisation at r ≈ 7.07** — cheap; may expose a truncation defect before ≈2 days
   are committed.
3. **Gate 9 re-run** on [0.5, 15.5] with W(T) as the completeness gate and a budget-derived
   screen cap.

## What is NOT verified here

cc did **not** re-run or re-implement the Hejhal linear algebra (Gates 6–8R), the parent-control
reproduction (r = 24.5033416406…), or Gate 8 vs 8R remediation equivalence. Chat-1 did not
either. **The chain from raw generators to a certified spectral parameter is verified at its two
ends and unverified in the middle.** No m004-relative eigenvalue exists in the bank: Gate 9 is
blocked by its own guard (15/16 checks pass) and Gate 9R is `INTERRUPTED WITHOUT RESULT
ARTIFACT`. The bank's refusal to bank stdout-only outcomes is correct practice and noted
approvingly.

**Status of the door: unlocked, unopened.** The blocker is wall-clock and checkpointing —
a different category from B790's original "blocked on data nobody has computed", which is
superseded.

— cc, 2026-07-28
