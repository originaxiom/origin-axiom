# B1615 — THE COUPLINGS THE WEAVE ALLOWS: the weave's group leaves the masses free (three per sector at TM1's symmetry), forbids every bilinear and trilinear of the matter alone, gives degenerate masses with a singlet Higgs, and with vacua along its own residual subgroups gives rigid spectra (0, 1, 1), (½, ½, 1) or one family with the exact sum rule m₁ + m₂ = m₃ — the charged leptons' hierarchy is out of reach; the sealed bound "no ratio below 0.1" is refuted by that family

**Verdict: NEGATIVE as sealed** (C1, C2, C3, C5 hold; C4's first clause fails, its second holds after a disclosed
post-seal scan). cc (main), 2026-10-08. Sealed `c5d30c59a` before `couplings_on_the_weave.py` ran (the seal's push
carried five LAW_MAP rows to clear the doc-currency gate, commit `2c968525d`, disclosed). The masses are nine of the
nineteen. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /Yukawa|mass matrix|mass hierarch|mass ratio|Schur|couplings|Clebsch|charged lepton/: 57 of 1386 arcs on main match (NEGATIVE 3, OPEN 8, PROVED 46)`
— B1611, B1612, B1606, the SM seat's §1, B1126; the seat's W34 and W35 (lane `eb4e97801`). **Literature:** Schur's
lemma, Clebsch–Gordan decomposition, the residual-symmetry approach (Lam) — standard.

## 1. The computation (`couplings_on_the_weave.py`; `couplings_on_the_weave.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **C1** | (T ⊗ T̄)^G = 1; no G-invariant bilinear of T alone; (T ⊗ T ⊗ T)^G ≤ 1 | 80% | **HOLDS** — 1; T ⊗ T, Sym² T, Λ² T: 0; T ⊗ T ⊗ T and T ⊗ T ⊗ T̄: 0 |
| **C2** | one coupling per Higgs representation | 90% | **HOLDS** — T̄ ⊗ T = 3 + 3 + 2 + 1, each once |
| **C3** | a singlet Higgs gives three equal masses | 99% | **HOLDS** — (1, 1, 1) |
| **C4** | no residual-aligned vacuum gives a ratio below 0.1, and none the charged leptons' (2.9 × 10⁻⁴, 0.059) | 85% | **FAILS on its first clause.** One-dimensional fixed spaces give rigid spectra: (0, 1, 1) in the first triplet (along RL, L, R, RRL), (½, ½, 1) in the second triplet along RL and in the doublet along L, R, RRL. The second triplet along RRL has a two-dimensional fixed space — a one-parameter family whose sampled m₁/m₃ reached 0.084. **The second clause holds** (post-seal scan below) |
| **C5** | at RL the masses are three free parameters | 95% | **HOLDS** — RL has three distinct eigenvalues on T |

**Post-seal (disclosed; `post_seal_family_scan.py`, 519 841 points of the family).** The family obeys the exact sum rule
**m₁ + m₂ = m₃** (to 10⁻¹⁵); m₁/m₃ runs over [0, ½] and m₂/m₃ over [½, 1]. The charged leptons' m_μ/m_τ = 0.059 is
unreachable (m₂ ≥ m₃/2); the closest approach is a factor of about 17 (log₁₀ distance 1.23).

## 2. What it says

The weave's group does not fix the masses: at TM1's charged-lepton symmetry they are three free parameters; a singlet
Higgs makes them degenerate; no invariant bilinear or trilinear of the matter alone exists (no Majorana-type mass, no
cubic coupling, for T by itself). With vacua along the weave's own residual subgroups the spectra are rigid — one
massless and two degenerate, or (½, ½, 1) — or, in one family, constrained by m₁ + m₂ = m₃, which allows one small ratio
but never a second: the observed charged-lepton hierarchy is out of reach. The masses, like the phase (B1611) and the
angles (B1612), are not in the weave's group. The sealed bound was too strong (the family's m₁/m₃ reaches zero); the
reading's substance stands.

**A lead, not a claim.** RRL is TM1's neutrino-side symmetry (B1612). Were the sum rule m₁ + m₂ = m₃ to hold for the
neutrino masses, normal ordering would force m₁ ≈ 28 meV and Σm ≈ 0.115 eV — in tension with the cosmological bound.
The neutrino masses need the Majorana analysis (T ⊗ T ⊗ H), which this arc did not do; registered for a sealed arc.

## 3. Disclosed

- C4's sampling (25 points) could not settle its second clause; the dense scan is post-seal.
- The seal's push was blocked by the doc-currency gate (LAW_MAP lagging 11 arcs); five LAW_MAP rows rode with it as a
  separate commit.
- The measured charged-lepton ratios were known (stated in the seal).

## 4. Files

`verification/couplings_on_the_weave.py` (sealed, unchanged), `couplings_on_the_weave.json`, `couplings_run.txt`;
`post_seal_family_scan.py` → `post_seal_family_scan.json`. Test: `tests/test_b1615_the_couplings_the_weave_allows.py`.
Kill-graph entry B1615.
