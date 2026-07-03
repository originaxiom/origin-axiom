# The toolbox — reusable engines and lemmas, indexed by "applies when"

*(Added 2026-07-03. This is the REUSE view: CLAIMS.md says what is true; the atlas says what
pattern recurred; this says what to call. One line each: applies-when → tool → entry point.
Curated at the audit; extend when a probe builds something a future probe will want.)*

## Engines (code you call)

| applies when | tool | entry point |
|---|---|---|
| exact arithmetic in ℚ(ζ₆₀) / level-15 Weil representations | the cyclotomic engine (Fraction vectors mod Φ₆₀; exact T, S, Gauss sums, √5/√−3/√−15 constants) | `frontier/B358_seam_certification/cyclo_engine.py` |
| identifying a cyclotomic quantity exactly in H = ℚ(√5,√−3) | Galois H-average + exact 4-basis solve | `seam_certification.py::H_avg, solve_H` |
| any seam readout (pair or single; any seeds, words, covers) | theta-lift matrices `W_m = WR^m·D^m`, DFT eigenprojectors, fast Par-trace | `frontier/B367_value_map/step0_exact_matrices.py` |
| 𝔢₆ cohomology on the figure-eight (any Sym-block computation) | the two-basis architecture: exact root brackets + block-diagonal action + **INTERTWINERS** (chain ↔ symrep crossings — two runs died for missing this), Fox blocks, H¹/H² extractors, exact-Gram ad-solve | `frontier/B352_cup_product_obstruction/cup_product.py` |
| higher-order deformation obstructions / boundary data at depth ≥ 2 | the jet method (no BCH transcription; self-gating P₁/P₂/P₃), blockwise z₂ solve, word jets | `frontier/B370_massey_depth2/massey.py, massey_legB.py` |
| a symbolic-in-m matrix identity that direct symbolics can't reach | the CRT/F_p symbolic-m reconstruction with an exact factorization as final certificate | `frontier/B80_sl4_adproof/` (method), `sln_toolkit.py` (B153 helpers) |
| testing a product-factorization hypothesis on an exact table with zeros | multiplicative tensor completion over ℚ (gauge-fixed propagation; zero-cell logic) | `frontier/B367_value_map/v3_search.py::solve_model` |
| "has anyone hit this obstacle / built this before?" | the recurrence atlas (motifs, obstacle→resolution oracle) + the repo gates | `scripts/atlas/query.py card` · `scripts/gates/gates.py` |

## Lemmas & decision procedures (results you cite — ledger IDs where promoted)

| applies when | fact | where |
|---|---|---|
| transporting seam/spectral data across covers or matrix powers | `P_a(W^k) = P_{k⁻¹a mod ord}(W)` for gcd(k, ord) = 1 | P17 (B368) |
| sanity-gating any pair table | row/column sums = the single-seed value (from ΣQ_b = I); seam slot sums to exactly 0 | E1/E2 provenance (B358/B367) |
| deciding amphichirality of a punctured-torus bundle from its word | the cyclic-palindrome / block-pair criterion | P34/P35 (B134/B136) |
| excluding trace fields / exceptional ends | unimodular disc floor (only ℚ(i), ℚ(√−3)); Niven forces E₆+E₈, excludes E₇; no C₃ trace fields | P48 (B239) · P49 (B249) · P54 (B307) |
| chirality-window questions on finite subgroups | the det-lemma: trivial det character ⇔ FS = −1; the ℤ/3-abelianization window | B356 |
| WRT/level arithmetic of the family | the level-period law + squarefree(m²+4) | P40/P41 (B204/B208) |

## Design patterns (method-level; the expensive lessons)

- **The banked-identity gate:** every NEW pipeline must first reproduce a banked identity inside
  itself before any new number is read (leg B's τ-gate rejected two convention-artifact "results";
  B355's conventions gate caught the CRT twist). Never read verdicts past a failed gate.
- **Derivation-first:** derive the transformation on paper before fitting anything (B366's three
  failed ansätze vs the one clean Jacobi inversion).
- **The order-1-identity trick:** an identity that holds at first order makes its second-order
  defect invariant under the first-order indeterminacy (the δ = φ_λ − τ·φ_µ construction, B370-B).
- **Complete the table before trusting the rule:** the B361 "local law" survived 11 pairs and died
  on the 12th (B367). Empirical selection rules are conjectures until their domain is exhausted.
- Numerics hygiene: PSLQ needs ≥30 digits; mpf/mpc reject format specs (use float()/nstr); double
  precision is structurally insufficient for Sym-block ranges; Euclidean normalization is not an
  invariant scaling; validate exploratory numerics at ≥2 seeds and ≥2 word sets.
