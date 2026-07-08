# Paper 1 — "The Seam Form" · claims inventory (content assembly, 2026-07-08)

**Per the charter: registry-driven claims table with per-claim bank / reproducer / lit-status.
Every row is re-verified at draft time (promotion-time re-verification). P1 is the full
treatment of the interaction form (the "seam") that P4 §4 references as a worked instance.**

| # | claim (as it will appear) | bank | reproducer | lit-status |
|---|---|---|---|---|
| S1 | The seam form: the interaction (a,b) ↦ tr(Par·P_a·Q_b) of the critical pair at level 15 takes **44 distinct values, all in ℚ(√5,√−3)** | L-SEAM (B358–B367) | seam value generator | program's own; Weil-rep values cite |
| S2 | **Spectral theorem**: the seam operator's spectral invariants σ₁ = σ₂ = 1/24 (the framing/central-charge fingerprint) | L-SEAM | (B358–B367 reproducer) | c/24 framing — Hannay–Berry/Kurlberg–Rudnick |
| S3 | **The cornerstone**: the seam field's distinguished quadratic subfield is ℚ(√−15) — the seam level 15's own field; √−15 "dies first" in the vanishing order | L-SEAM | seam value generator | program's own |
| S4 | **The exchange identity**: Par-conjugation / the σ-exchange W₁ ↔ W₂ acts on the seam values by a specific involution | L-SEAM + T-SIGMA (B466) | `sigma_action.py` | Gieseking deck action, thin lit |
| S5 | **The channel-vanishing lemma** (the opening): a Galois channel vanishes ⟺ its cyclotomic support is empty — vanishing is forced by the character's support, not fitted | L-KLEIN (B459/B468) | `verify_patterns.py` | equivariance DERIVABLE (Coste–Gannon/Serre); counts = data |
| S6 | **Selection rules**: exactly **5 vanishing patterns** occur (none / {√−3,√−15} / {√5,√−15} / {√5,√−3,√−15} / all), realizing the **subfield lattice** of ℚ(√5,√−3); counts 120/20/20/10/70 | L-KLEIN | `verify_patterns.py` | Klein-four subfield lattice; classical-anchored |
| S7 | **The dark locus**: 70 points are dark (all four channels vanish); **54 of the 70 sit at quantum closure** ([W₁ʲ,W₂ˡ]=I) — darkness concentrates at closure | L-KLEIN + T-KQ (B472) | `kq_verify.py`, `verify_patterns.py` | program's own |
| S8 | **Par is the orientation involution**: det(Par) = −1, Par = Weil image of −I; the whole seam is "watched through Par" | T-2REG/T-PQB (B469/B470) | `br1_br2.py`, `rf3_quantum.py` | DERIVABLE (Jacobi symbol) |
| S9 | **The master theorem**: both the commutator trace κ_q = ε(jl)·χ₅ AND the seam tier factor through the divisor pair (gcd(x,20), gcd(y,12)) — the entire selection architecture is two functions on the **36-cell divisor lattice** of the two clock orders | T-MASTER (B474) | `cross_table.py` + master table | co-factorization program's own; divisor-lattice selection NEEDS-LIT (the P1 spine) |
| S10 | **The magnitude law**: \|κ_q(j,l)\|² = #Fix([A₁ʲ,A₂ˡ] on (ℤ/15)²) (Howe), verified 25/25 — the divisors of 15 are Howe's formula at level 15 | T-KQ (B472) | `kq_verify.py` | Howe/Thomas (cited) |
| S11 | **The conductor law**: seam level 15 = conductor of the compositum(geometry field, dynamics field); the level's arithmetic drives the whole seam | L-COND (B449) | (B449 reproducer) | classical-anchored; seam framing program's own |
| S12 | **The two-register breath**: det(Par@N) = sign(σ on (ℤ/N)²) = (−1)^{(N−1)/2}, the quantum and classical orientation breathe together (levels 15/45/75/225) | T-2REG (B469 BR1) | `br1_br2.py` | DERIVABLE (Jacobi) |

## Open / suspended (must NOT be claimed until closed)
- The **cyclotomic-support step of the master theorem** (deriving each cell's tier from its
  cyclotomic support) is verified-on-240 but not proven per-channel — stated as the paper's
  own open problem (same status as P4 Theorem G(ii)).
- The **6b power-set magnitude law** (composite-N generalization of S10) is NOT confirmed
  (B486 SIXB_VERDICT) — excluded from P1 until an exact definition reproduces it.

## Re-verification note
S6/S7 (`verify_patterns.py`), S9/S10 (`kq_verify.py`, `cross_table.py`), S8/S12 (`br1_br2.py`)
re-run clean this session. S1–S4/S11 (the B358–B367/B449 seam bank) to be re-run at draft v1.
