# Cross-session processing — disposition ledger (2026-06-11)

Processing record for two parallel review sessions (B = pairing/CFT/arithmetic; C = scrutiny) plus a
fresh-clone external audit. Default per item: **check against the live repo; bank only what my own
verification confirms is new + correct, at the supported tier; dedup / tombstone / discard the rest.**
The dedup *is* the deliverable; the bankable residue is thin (as the brief predicted). Nothing here
promotes to `../CLAIMS.md`; the proven core P1–P16 is untouched. The originating sessions are
AI-assistant instances sharing priors — their self-checks count for nothing; this ledger records *my* dispositions.

The C1/C2/C3 CFT handoff (a third document) was already shipped (PR #173) and is **not** reprocessed
here; `R1`/`R4` below are explicitly **not** double-counted against that L16/S023 RM material.

## Verified this session (independent)
- The audit's three "red" tests (`test_b101_hitchin_reframing::test_v0_anosov_hallmark`,
  `test_b106_dehn_filling_anatomy` ×2) **pass at HEAD in the canonical env** (`6 passed`); the audit saw
  them red at the older `19c2f25` with a different numpy → env-sensitivity, not a live failure.
- **F4** reproduced in full (and a modulo-sign bug in my own probe caught + fixed) → banked as **B152**.
- **R2b** silver volume = 4·Catalan verified numerically; `b++LR` = figure-eight confirmed.

## Deliverable 1 (F1–F4)

| item | verdict | disposition |
|---|---|---|
| **F1** λ*=1 / I=1/4 via "dictionary D" | = **B26 / C5** (dedup) | confirming re-derivation only; not banked. A third selector converging on B26/C5, same epistemic rank as C5's T1. |
| **F2** λ*=1 spectral fingerprint numbers | partial-new numbers, KNOWN arena (B25) | **banked NUMERICAL** as a refined experimental-target card in `../frontier/B25_fibonacci_spectrum_anchor/README.md` (band counts F_k thru F=610, decay 0.8711(4), gaps {m/φ}, D₀≈0.86 unconverged). |
| **F3** centralizer = S(∏GL(mᵢ)) reading | new framing of B121/B122, not new math | **banked STRUCTURAL framing note** in `../knowledge/K008_tower_determined_by_seed.md` (a centralizer reading of the banked multiplicities; pointer, no claim). |
| **F4** CS 240-census, m208 converse | **NEW, verified** | **banked as probe B152** (`../frontier/B152_cs_amphichirality_census/`, V141): 7 amphichiral, 0 necessity violations, m208 the unique converse counterexample (chiral, CS=0) → CS-2-torsion necessary not sufficient. NUMERICAL/census, extends B128/B136. |

## Deliverable 2 (R1–R5; R6 not present in the brief)

| item | verdict | disposition |
|---|---|---|
| **R1** congruence truncation | Ng–Schauenburg already cited (NOVELTY_AUDIT R3 / K015) | **framing**: the *mechanism* (rational-CFT data factor through finite congruence quotients ⟹ golden content invisible there) is the complementary **face** to L16/S023's *location* (the real-quadratic axis). One boundary, two faces. Noted on `../docs/OPEN_LEADS.md` L16. **Not merged, not double-counted.** |
| **R2a** fig-8 Vol=(3√3/2)L(2,χ₋₃) | KNOWN-classical (new-to-repo) | **banked KNOWN** in `../frontier/B147_arithmetic_chiral_bundle/FINDINGS.md` (CM-volume addendum); classical Bloch–Wigner/Humbert. |
| **R2b** silver Vol=4·Catalan=4·L(2,χ₋₄) | NUMERICAL, expected-known (Gaussian analogue) | **banked NUMERICAL→likely-KNOWN** (B147 addendum), literature-gated; verified to snappy precision, not proven; do not pitch as new. |
| **R2-family** CM sublocus = {golden,silver} | mostly = **B125 / K002** | one-line sharpening (B147 addendum) citing B125 + BMR finiteness; not new. |
| **R3** \|disc\|=κ kill at silver | a kill (negative) | **TOMBSTONE K-N** (`../speculations/TOMBSTONES.md`): \|−4\|=4 ≠ 6=κ₂; the golden 3=3 does not generalize. |
| **R4** junction unit-group algebra | mostly = **P12**; new bits elementary | pointer to P12; the Cayley–Hamilton / ramified-prime additions are standard number theory, not banked as new. |
| **R5** golden "leak" tr=−1/φ | resolved **NO SIGNAL** | **TOMBSTONE K-O** (TOMBSTONES): the seed's SU(2)₃ trace is golden & nonzero, but its class is one of ~47% nonzero / ~13% golden-magnitude in the order-2880 image — populated, not distinguished. Field-forcing stands (trivially); "distinguished" does not. |
| **convergence note** (A & B same boundary) | corroboration, NOT external review | **banked WITH caveat** in `../docs/STRATEGIC_SYNTHESIS.md` §8b (independent legs = literature anchors; one-specialist review still unmet). |

## External audit (Doc 2)

| item | verdict | disposition |
|---|---|---|
| **F-1** three "red" tests | pass at HEAD in my env | noted above (not reproduced); the env-sensitivity residue is what CI guards. |
| **F-2** no CI | real | **prepared**: `.github/workflows/core.yml` written + verified green locally (proven-core locking tests, sympy+numpy; full suite stays local for SnapPy/Sage). **Not yet pushed** — the push token lacks the GitHub `workflow` scope; enable with `gh auth refresh -h github.com -s workflow` (or add the file via the GitHub UI), then push. |
| **F-3** CLAIMS.md header drift | real | **fixed**: `../CLAIMS.md` freshness line updated (B1–B152; "B69–B152 produced zero promotions"). Header only — no claim changed. |
| **F-4** discoverability / re-derivation tax | partial (atlas exists; method-bugs not surfaced from README) | **fixed**: `../README.md` "Before you compute anything new" pointer (grep OPEN_LEADS; MB6–MB12; atlas). |
| **F-5** single maintainer, no external eyes | standing, not actionable | noted in STRATEGIC_SYNTHESIS §8b (B150 = the citable artifact; review unmet). |
| audit **§3a/b/c** | = F4 / F2 / F3 | covered above. |
| audit **§3d** (commuting⟹trace-2⟹entropy⟹excluded; tr=3 quantized) | fragmented, not cleanly banked | **OPEN_LEADS L17** (not banked; check vs B128/K013; the entropy step unbanked). |
| audit **ToE verdict** | consistent with firewall (B151) | noted in STRATEGIC_SYNTHESIS §8b (external audit independently reached the firewall / ToE-refusal read). |
| audit **recs 1–7** | 1=F-1/F-2, 2=F-3, 3=F-4, 4=live frontier (in ROADMAP/OPEN_LEADS), 5=F-5, 6=F2 card, 7=§3 residue | all covered above; recs 4/5 are standing notes. |

## Doc 3 (C1/C2/C3)
**DONE — PR #173** (S023 Pell + L16, K001 cusp, B85 constraint, TOMBSTONES K-J…K-M). Not reprocessed.

## Bottom line
Exhaustive treatment, thin bank: the one real new result is **B152** (the CS census + m208). **R2b** is a
likely-known numerical identity behind a literature gate. Everything else is dedup, framing, tombstone,
or maintenance. The maintenance fixes (CI, CLAIMS freshness, README nav) are the audit's genuine value.
The standing recommendation — one external specialist (B150 the artifact) — survives, unmet.
