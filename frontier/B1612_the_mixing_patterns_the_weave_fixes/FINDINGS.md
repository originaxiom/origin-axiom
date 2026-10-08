# B1612 — THE MIXING PATTERNS THE WEAVE FIXES: the weave's group fixes six full mixing patterns and none lies inside the data — not for the leptons (0 of 216 trials) and not for the quarks (the closest is the identity, 331σ off in |V_us|); it fixes two one-column relations that survive at 3σ, TM1 and TM2, and against NuFIT 6.1's θ₁₂ only TM1 stands (sin²θ₁₂ = 0.318, +1.5σ; TM2 +4.9σ) — a one-parameter relation the chiral weave allows without the swap, not a parameter-free value

**Verdict: PROVED** (M1–M4 and D1–D3 hold as sealed; one deviation in the data source and two post-seal computations,
disclosed). cc (main), 2026-10-08. Sealed `f008c0424` before any cell was computed and before any data was read. **The
first value contact under the owner's reopening of 2026-10-08.** No parameter of the nineteen derived. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /PMNS|tri-?bimaximal|TM1|TM2|CKM|Cabibbo|NuFIT|residual symmetr|mixing pattern/: 21 of 1383 arcs on main match (NEGATIVE 8, PROVED 13)`
— the thread-level mixing results on m004 (B342, B343, B467, B631, B861), the value campaign's NEGATIVEs (B398,
B1063, B1066), the SM seat's §3 reading (TM1 from the swap), B1611, W33. **Literature:** Lam (2008); the classical
patterns — cited from the reviewer's knowledge.

## 1. The patterns (`mixing_on_the_weave.py`; `mixing_on_the_weave.json`; no data)

| | sealed prediction | prior | result |
|---|---|---|---|
| **M1** | G faithful on T | 70% | **HOLDS** — the image on T has order 96; 56 elements have three distinct eigenvalues |
| **M2–M3** | finitely many fully fixed patterns, TBM among them | 75% | **HOLDS** — 11 eigenbases give **six** patterns: bimaximal (L against R), TBM (RL against ⟨RR, rLL⟩), democratic, a trimaximal one with \|U_e3\|² = (2 − √3)/6 ≈ 0.0447 (L against RL), one with a single maximal angle, and a circulant (1/9, 4/9, 4/9) |
| **M4** | the TM2 column (⅓, ⅓, ⅓) | 70% | **HOLDS** (the RL basis against RR's eigenline) |
| **M4′** | the TM1 column (⅔, ⅙, ⅙) | 50% | **HOLDS** (the RL basis against RRL's eigenline) — **without the swap**: the seat's §3 TM1 survives on the chiral weave |
| M5 | the look-elsewhere count | — | 216 full-pattern trials (6 × 36); the comparison script tried each of the 5 columns in 18 placements (90) |

## 2. The contact (`compare.py`, sealed; `data.json`; `comparison.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **D1** | no full pattern inside NuFIT's 3σ \|U\| ranges | 85% | **HOLDS** — 0 of 216, both orderings |
| **D2** | none, nor the identity, within 3σ of PDG's \|V_ij\| | 97% | **HOLDS** — 0 of 252; the closest is the identity, 331σ off (\|V_us\|) |
| **D3** | some fixed column inside NuFIT's ranges | 60% | **HOLDS** — two of 90: TM1 as U's first column (\|U_e1\| = 0.816) and TM2 as U's second (\|U_e2\| = 0.577, near the top of 0.519–0.580) |

**Post-seal (disclosed; `post_seal_tm_sum_rules.py`).** Each surviving column is a one-parameter relation: with θ₁₃
measured, TM1 gives sin²θ₁₂ = 1 − 2/(3 cos²θ₁₃) and TM2 gives 1/(3 cos²θ₁₃). Against the record's NuFIT 6.1 values
(B1066's log; a secondary source): **TM1 0.318, +1.5σ; TM2 0.341, +4.9σ** in both orderings (the θ₁₃ spread ≤ 0.0004).
TM2 is excluded by the newer fit, as B342 found for m004's ℤ/3; TM1 stands.

## 3. What it says

**The weave's group does not fix the mixings.** Of its six fully fixed patterns none fits the leptons and none fits the
quarks, so no mixing angle is a parameter-free group-theoretic number of the weave — the angles, like the CP phase
(B1611), live in the couplings. **What the weave allows is one viable relation:** the TM1 column, |U_e1|² = ⅔,
|U_μ1|² = |U_τ1|² = ⅙, from the root's double tick RL (the charged-lepton residual symmetry) and RRL (the neutrinos'),
with no swap. It is a one-parameter family, not a value, and it is a READING twice over: which sector is the leptons is
FK11's unearned dictionary, and which subgroup each sector keeps is a selection the weave allows and does not force. The
quark sector gets nothing from the group: the Cabibbo angle is not a residual-symmetry number here.

**For the goal.** 0 of 19: the CKM moduli are not fixed; the PMNS (outside the nineteen) gets one allowed relation. The
next sharper test of the TM1 reading is its correlation of θ₂₃ with δ_CP (|U_μ1| = |U_τ1|), a near-term experimental
target; and the parameters themselves need the couplings.

## 4. Disclosed

- **The data source deviates from the seal.** The seal named NuFIT's newest release on nu-fit.org (6.1 or later). The
  site was unreachable on 2026-10-08 (expired TLS certificate) and no primary 6.1 |U| table could be fetched; the
  comparison used NuFIT 6.0's |U| 3σ table (arXiv:2410.05380v2, variant "IC24 with SK-atm", stated as the global
  minimum over both orderings, so NO and IO carry the same table). The 6.1 numbers enter only post-seal, from the
  record's B1066 (a secondary source, angle fits).
- PDG 2025 (section 12, dated 1 December 2025, eq. 12.27); asymmetric uncertainties symmetrised to the larger side.
- The comparison script tried 18 placements per column (3 columns × 6 orders), so the column look-elsewhere count is
  90, not the instrument's 45; stated as computed.
- The imported expectation was stated in the seal: the measured mixings were known to the reviewer.

## 5. Files

`verification/mixing_on_the_weave.py` and `compare.py` (sealed, unchanged), `mixing_on_the_weave.json`, `mixing_run.txt`,
`data.json` (with sources), `comparison.json`, `compare_run.txt`; `post_seal_tm_sum_rules.py` →
`post_seal_tm_sum_rules.json`. Test: `tests/test_b1612_the_mixing_patterns_the_weave_fixes.py`.
