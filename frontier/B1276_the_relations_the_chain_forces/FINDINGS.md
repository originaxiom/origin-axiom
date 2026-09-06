# B1276 — THE RELATIONS THE CHAIN FORCES AMONG THE 19: every operator of the E₆ cubic on the 27, labelled by the descent, carries the same coupling — one Yukawa for up, down, lepton and Dirac-neutrino, the same for the μ-term and the exotic mass, the same on the 24 colour-triplet operators

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (exact: B1275's tensor read through B1252/B1253's labels) · **Price: unchanged**

## Why

The owner asked what exactly completes the 19. Before the destination can be stated, the relations the chain
*already* imposes among them must be computed rather than recalled from GUT lore. B1275 made the cubic explicit;
B1252/B1253 label every weight of the 27 by its Standard-Model quantum numbers. Reading one through the other gives
the complete tree-level superpotential of the E₆ theory on one 27, with coefficients.

## 1. The 45 operators ((`verification/relations.py`), exact)

The 27 by label: Q (6), u^c (3), d^c (3), L (2), e^c (1), ν^c (1) — the 16; H_u (2), H_d (2), D (3), D̄ (3) — the 10;
S — the 1. The 45 zero-sum triples, by operator and coefficient:

| operator | component triples | d-values |
|---|---|---|
| H_u Q u^c | 6 | ±1 |
| H_d Q d^c | 6 | ±1 |
| H_d L e^c | 2 | ±1 |
| H_u L ν^c | 2 | ±1 |
| S H_u H_d (the μ-term) | 2 | ±1 |
| S D D̄ (the exotic mass) | 3 | ±1 |
| D Q Q, D̄ d^c u^c (diquark) | 6 + 6 | ±1 |
| D̄ L Q, D e^c u^c, D d^c ν^c (leptoquark) | 6 + 3 + 3 | ±1 |

**Every coefficient is ±1: the E₆ theory on the 27 has exactly one coupling λ.** With the three generations of the
object's closing (B1273) the cubic is λ d_abc |ε_ijk| 27^a_i 27^b_j 27^c_k, so the same λ multiplies every entry.

## 2. The relations, stated exactly (at the object's scale, tree level)

1. **Yukawa unification of each generation's four Yukawas:** y_u = y_d = y_e = y_ν = λ. Hence with the same Higgs
   VEVs **m_b = m_τ, m_s = m_μ, m_d = m_e** and **m_t : m_b = v_u : v_d = tan β**, and the Dirac neutrino mass equals
   the up-type mass of its generation.
2. **μ = m_D = λ⟨S⟩:** the Higgs doublets' mass and the exotic colour-triplets' mass come from the same singlet with
   the same coupling. A light doublet (⟨S⟩ ~ v) makes the exotics light; heavy exotics (⟨S⟩ ≳ 10¹⁵ GeV, see 3.)
   make the doublets heavy: **the doublet–triplet splitting is forced against the chain at tree level.**
3. **Both diquark and leptoquark couplings of D are present with |λ| = 1**, so D exchange mediates proton decay at
   tree level; the observed lifetime then requires m_D = λ⟨S⟩ ≳ 10¹⁵ GeV — the singlet VEV at the unification
   scale, which is where B1271 §3's rank reduction puts it.
4. **The down–lepton splitting has a carrier:** D d^c ν^c with ⟨ν^c⟩ ≠ 0 (the other rank-reducing VEV, B1271 §3) mixes
   the exotic D with the down quarks and moves m_d, m_s off m_e, m_μ — the standard E₆ mechanism, present in the
   object's own operator list.
5. **No Majorana mass anywhere** (B1271 (d)): with the 27̄s of the closing pairing ν^c through the flavons (B1273 §3),
   the light neutrino is exactly massless at tree level (lepton number unbroken), or Dirac at the up-quark scale
   without that pairing.

## 3. Against the data (the running is an accepted-physics input; no crossing sealed)

| relation | low-energy ratio | at the object's scale the chain says |
|---|---|---|
| m_b / m_τ | 2.35 | 1 — known to hold within tens of percent after running (the classic b–τ) |
| m_s / m_μ | 0.88 | 1 — fails by ~3 after running (the classic; item 4 is the carrier of the fix) |
| m_d / m_e | 9.1 | 1 — fails by ~3–9 (same) |
| m_t / m_b | 41 | tan β — free, from the VEV data |
| m₁ ≤ m₂ + m₃ per sector | violated by 17–136 | the zero-diagonal texture (B1273): the diagonal source is missing |

## 4. What this fixes in the destination (`docs/THE_DESTINATION_LEDGER_2026-09-06.md`)

The Yukawa block (9 charged masses, 3 Dirac neutrino masses, μ, m_D, the 24 exotic couplings) collapses to **one
number λ times the VEV data**, with four exact relations and two tree-level tensions (the splitting, the neutrino).
Everything that is not a ratio the chain fixes is a VEV or a non-tree-level term.

## Controls (MB12)

- The labels are B1252's derived hypercharges through B1250's blocks, not assigned by hand; the operator counts
  6 + 6 + 2 + 2 / 2 / 3 / 24 = 45 reproduce B1253's 40 + B1271's 5.
- The coefficients are read from the solved tensor (B1275); a non-unit value anywhere would break "one coupling".

## Verification

`verification/relations.py` (exact; ~2 min; `SELFTEST: PASS`), run record `verification/relations_run.txt`.
Lock: `tests/test_b1276_the_relations_the_chain_forces.py`. Feeds on B1275, B1252, B1253, B1250, B1271, B1273.
Registers no identification change.
