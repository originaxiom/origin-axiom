# B1948 — The relations the record holds among the Standard Model's parameters, typed: one live, the frame-wide ones refuted, each refutation naming a requirement

**Verdict: OPEN** (an inventory: step 1 of the goal P-862). Main, 2026-11-15. It reads the record's governing tables;
no measured number is newly compared, and every data status is the record's own. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /relation among|relations among|universal relation|sum rule|Georgi|Koide|TM1|minimal SU\(5\)/: 47 of 1689 arcs on main match (NEGATIVE 13, OPEN 3, PROVED 31); 26 register rows match (DONE 18, QUEUED 8)`.
- **What was read.** `verification/extract_candidates.py` pulls the 242 rows of LAW_MAP, FALSIFIER_REGISTER,
  THEOREM_REGISTRY, THE_CLAIM and GENESIS that tie physical parameters together (`verification/candidates.txt`). Main
  read them and the arcs named below.
- **The literature:** minimal SU(5)'s Y_e = Y_dᵀ and its failure on the lepton–down split, and the Georgi–Jarlskog
  factor (standard). The trimaximal TM1 and TM2 patterns are common to many discrete flavour models (standard).

## The types

- **U:** holds in every allowed history, given only the shared structure: the root, the orientation, and the
  dictionary Λ as tagged.
- **F:** holds at every point, line and τ of a frame, given that frame's dictionary. It needs no selection inside the
  frame.
- **S:** holds only at a selection inside a frame: a τ, a line, a residual or a reading.

## The inventory

| # | relation | arcs | type | status in the record | what it teaches |
|---|---|---|---|---|---|
| 1 | charge quantisation, t/3 + d/2 + Y ∈ ℤ | P2; B1080 | U | **CONFIRMED** (no violating state) | generic to any SU(5)-embeddable theory, so not specific |
| 2 | the global form (SU(3)×SU(2)×U(1))/ℤ₆ | P3; T-GLOBALFORM | U | untested (needs a monopole) | a genuine claim, not testable now |
| 3 | level 5's Weil representation lies in SU(3) × SU(2) | B1934 | U | structure, not a parameter relation | the act's prime carries the gauge pattern |
| 4 | sin²θ_W = 3/8 at unification | B909, B919 | U, given the SU(5)/E₆ embedding | standard; the object supplies no scale; with one input and a desert the crossing missed at 16σ (LAW_MAP, THE CROSSING) | a relation that needs a scale the programme lacks |
| 5 | the exotics' quantum numbers | P6 | U, given the 27 | untested | conditional and clean |
| 6 | a rank-5 vacuum with a family-non-universal Z′ | P9 | F (the closing's vacuum) | untested | as 5 |
| 7 | the hypercharge normalisation | B991 | U | **not derivable** (homogeneity) | a no-go |
| 8 | Y_e = Y_dᵀ on every line of order dividing 5, so m_e/m_μ = m_d/m_s and m_μ/m_τ = m_s/m_b | B1698, B1934 | F | **REFUTED** (the data's lepton–down split; minimal SU(5)'s known failure) | the leptons need a level with another prime (P-845) |
| 9 | under E₆'s cubic, lepton and down singular values equal for every 27 vev (D = 1) | B1738 | F | **REFUTED** as 8 | the lepton factor needs a source outside the 27s' cubic |
| 10 | a flavour-blind Higgs gives m₂/m₃ ≥ 1/3 in every sector | B1727 | F | **REFUTED** (the data lie far below) | the Higgs must be flavoured |
| 11 | one covariant Higgs splits the sectors' m₂/m₃ by at most 4 (point coupling) | B1692, B1693 | F | the up–lepton pair **excluded** at M_Z (B1693); the bound fails at the canonical end (B1693's correction) | in the point coupling the up quarks need a Higgs of their own |
| 12 | the hierarchy–alignment dichotomy: no zero-free Higgs on record carries both | B1739, B1740; B1946 | F | sealed (B1740). Frame C's cusp mixing aligns only with one reading (B1946) | hierarchy and mixing pull against each other in this coupling |
| 13 | the cusp exponents e(m₂/m₃) = ½ − (‖2q_Lα‖ + ‖2q_Rα‖)/2 and the tropical rule | B1788, B1945 | F, per line | the up/down 3:2 is the measured ratio restated, not derived (B1788); the averaged pattern is untested (P-859, with main's disclosed foreknowledge) | exponent ratios are free of τ: a form a relation can take |
| 14 | m₁m₃ = m₂² at the coincident point N = S | B1659 | S (a point) | not tested as a relation | — |
| 15 | the weave's symmetry reduces none of the 13 flavour parameters, on any of its 68 subgroups | B1620 | U | a **no-go** | there is no symmetry relation among the quark masses and mixings |
| 16 | **TM1:** sin²θ₁₂ = 1 − 2/(3 cos²θ₁₃) ≈ 0.318, and δ_CP in 252.7°–292.9° (or its mirror) | P10; B1612, B1613 | S (a residual pair; one τ cannot give both on the ruled branch, B1640) | **LIVE:** 2.28σ on JUNO's second release, against a kill line of 3σ | the record's one live relation, and it needs a selection |
| 17 | TM2: sin²θ₁₂ = 1/(3 cos²θ₁₃) | P10′ | S | **FALSIFIED** at 5.82σ (B1756) | — |
| 18 | the CP sign is the CS sign, and CS = 0 exactly when amphichiral: CP violation allowed, not forced | B303, B1611 | U | no number | — |
| 19 | θ_QCD = 0 | P1 | — | **WITHDRAWN** (B1009) | — |
| 20 | three as a count: vector-like at the root; the flavour three derived, the gauge three a selection; chirality a bit | B713, B1290, B1604, B1606, B1466 | U | structure | no parameter relation |
| 21 | the Dirac L ν^c's det M vanishes exactly where −3w has order 4 | B1799 | F, per line | not tested as a relation | — |

## What it says

- **One live relation, and it needs a selection.** The record holds exactly one live forward relation among the
  Standard Model's free parameters: TM1 (16). It is at 2.28σ, and it rests on a residual pair the principle does not
  select. Its sibling TM2 is falsified.
- **Every frame-wide flavour relation is refuted** (8 to 12). Each refutation names a requirement:
  - the leptons need a level with a prime other than 5;
  - the lepton factor needs a source outside E₆'s cubic;
  - the Higgs must be flavoured;
  - hierarchy and alignment must not exclude each other.

  These are structural lessons, not near misses.
- **The weave's own symmetry gives no quark relation** (15). So any universal quark relation must come from the
  coupling's structure, not from its symmetry.
- **The universal structural relations are generic or untestable now.** Charge quantisation (1) is generic. The global
  form, the exotics and the Z′ (2, 5, 6) are untested. sin²θ_W = 3/8 (4) needs a scale.

## For step 2 (what the inventory points to)

- **Exponent relations are free of τ** (13). Within a frame they are the natural carriers of universal relations.
  - P-845's level decides which lepton relation holds.
  - At order 10 the lepton rows are the down rows with the doublet's twist negated (SM-C13b). That is a relation of
    form, derivable without data.
  - At order 15 the leptons keep the order-5 rows (B1942).
- **A data-free derivation of the lepton–down exponent relation at each candidate level** is therefore the first new
  relation to derive. It is to be sealed before any comparison, and the look ledger's history, with main's foreknowledge
  of the lepton–down split, counts it.

## Not claimed

- That the inventory is complete beyond the record's governing tables and the arcs named.
- Any new comparison with data.
