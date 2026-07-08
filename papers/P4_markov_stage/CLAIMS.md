# Paper 4 — the claims inventory (assembled from the registry; re-verification column live)

| # | claim | bank | reproducer | lock | lit-status |
|---|---|---|---|---|---|
| 1 | tr[A_m,A_n] = 2 − (mn(n−m))² (symbolic identity via Fricke + the B467 product-trace) | B471 | chain_verify.py | test_b471 ✓ | NEEDS-LIT (the gate: Aigner ch.2–3, Reutenauer Fricke/Cohn chs., Cusick–Flahive ch.2) |
| 2 | (1,2) is the unique parabolic pair (mn(n−m) = 2 unique in m<n) | B471 | chain_verify.py | test_b471 ✓ | with #1 |
| 3 | A₁ = g₁; ⟨A₁,A₂⟩ = ⟨g₁,g₂⟩ = [PSL₂ℤ, PSL₂ℤ] (Nielsen + balanced-word kernel) | B471 | chain_verify.py | test_b471 ✓ | Cohn 1955 KNOWN core; metallic reading NEEDS-LIT |
| 4 | the chain conserves the Markov cubic; /3 walks the spine; every renormalized pair parabolic | B471 | chain_verify.py | test_b471 ✓ | Fricke/Markov classical; framing NEEDS-LIT |
| 5 | N(λ_m) = −1 = det X_m (companion); frozen through φ-power degeneracy; impossible in imaginary fields | B469 | br_n_norm.py | test_b469 ✓ | DERIVABLE; identification program's own |
| 6 | breathability: integer det −1 root ⟺ tr − 2 = t² AND t \| (B−I); the family = the root locus; chain rootless beyond letters (2–200 certified) | B469/B470 | hierarchy_verify.py | test_b469/70 ✓ | NEEDS-LIT (SL(2,ℤ) square roots) |
| 7 | the breath hierarchy root ⟹ mirror ⟹ balanced ⟹ frozen; strictness witnessed exactly (the (ℤ/12)² pair; RRRLLRLL) | B470 | hierarchy_verify.py | test_b469/70 ✓ | components DERIVABLE; frame program's own |
| 8 | body-chain amphichiral at every rung (palindromic-alphabet theorem); letter-tower chiral iff imbalanced (unified with the Pisano residue) | B470 | rf1/rf3 + hierarchy | test_b470 ✓ | NEEDS-LIT (amphichirality criteria) |
| 9 | THE CLOSURE THEOREM [W₁²,W₂³] = I; κ_q(1,1) = −1 ≠ −2; the exact 25-entry table (3 lifts) | B472 | kq_verify.py | test_b472 ✓ | seam-level κ_q framing NEEDS-LIT |
| 10 | mod-3 image = Q₈; mod-5 image = SL(2,5); closure ⟺ CRT centrality | B472 | kq_verify.py | test_b472 ✓ | classical groups (cite); the occurrence is the result |
| 11 | THE MASTER THEOREM: κ_q = ε(jl)·χ₅ (two characters) and both κ_q and the tier factor through (gcd(x,20), gcd(y,12)) — 36 divisor cells | B474 | cross_table.py + master table | test_b474 ✓ | program's own; NEEDS-LIT (divisor-lattice selection rules) |
| 12 | the seam faces: tr(Par W₁W₂) = ζ₆₀⁸, tr(Par W₂W₁) = ζ₆₀⁴ — ratio ζ₁₅ (three lifts) | B472 add. | session locks | test_b472 ✓ | program's own |
| 13 | context (cited, not claimed): Markov 1879; Cohn 1955; Hurwitz; Aigner 2013; Reutenauer 2018; Guéritaud volumes; Pandey–Wong (BWY for the LR bundle) | — | — | — | KNOWN |

**Re-verification pass (the writing pass reruns all locks):** pending — first act of draft v1.
**Constants appearing:** λ_chain (25 digits, non-algebraic ≤ 8), c (28 digits, PSLQ-negative) — quoted as data with their certificates.
**Explicitly NOT in this paper:** any physics naming (the firewall in prose); the criticality frame beyond one scoped remark (B473 is open work); the towers-as-one-object metaphor (S-room, HELD).
