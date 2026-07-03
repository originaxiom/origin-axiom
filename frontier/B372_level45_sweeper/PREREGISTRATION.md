# B372 (W2.7) — the level-45 sweeper: PRE-REGISTRATION (committed before computation)

**Campaign W2.7 (task #161). The robustness question: is the seam a level-15 accident or a
level-family phenomenon? Two-outcome per cell; nulls written below before any run.**

## Construction (declared)

Level N = 45 (= 9·5; odd ⇒ a genuine SL(2,ℤ/45) Weil representation, no metaplectic cover).
Theta-lift conventions transported verbatim from the banked level-15 model (P56/P57 lineage):
`D = diag e₄₅(j(j−1)/2)`, `WR = F·D⁻¹·F⁻¹` (raw DFT conjugation, normalization-free),
`W_m = WR^m·D^m`, `Par: f(x) ↦ f(−x)`; pair observable `tr(Par·P_a(W_{m₁})·Q_b(W_{m₂}))`,
H-projected. **Engine: CRT/F_p** (toolbox row 6 — the B80 method): all matrix arithmetic mod
several primes `p ≡ 1 (mod 180)` with ζ₁₈₀ realized as a power of a primitive root; the readout
traces reconstructed exactly by CRT + rational reconstruction, then solved in the declared
subfield basis. Exactness tier: exact (integer arithmetic + reconstruction with cross-prime
agreement mandatory), not floating point.

## The conventions gate (hard-blocks everything downstream)

The identical pipeline run at level 15 must reproduce the banked flagship exactly:
`tr(Par·P₀Q₄) = −1/48 − (1/80)√5 − (1/48)√−3 + (1/48)√−15` (P19/E1), and a second banked cell.
Any mismatch ⇒ stop, fix conventions, re-gate. No level-45 number is read before this passes.

## The declared readout basis and the questions

At level 45 the relevant quadratic subfields of ℚ(ζ₁₈₀) declared for the solve:
`{1, √5, √−3, √−15}` (the level-15 set) ∪ `{√−35?—no: declared exactly the products of
{√5, √−3} as before}` plus the real-cubic trace pieces of ℚ(ζ₉)⁺ (basis `{1, c₁, c₂}` with
`cₖ = ζ₉^k + ζ₉^{−k}`), i.e. the solve space is the 12-dim ℚ-span of
`{1, c₁, c₂} ⊗ {1, √5, √−3, √−15}`. A residual outside this span is itself a reportable
finding (the value left the declared home), not a failure.

- **Q1 (singles wall):** every single-seed readout `tr(Par·P_a(W_m))`, m ∈ {1,2}, lies in the
  REAL part of the span (zero √−3 and √−15 components). NULL: the wall persists at 45.
- **Q2 (the seam question):** the pair (1,2) cells — the full a-grid against the first two
  b-clusters, plus any cell flagged by Q1 structure. PRE-REGISTERED NULL: at level 45 every
  pair value lies in ℚ(√5) ⊗ ℚ(ζ₉)⁺ (NO imaginary component — the seam does NOT persist,
  consistent with the real Gauss sum g(45) = 3√5 since 45 ≡ 1 mod 4).
  ALTERNATIVE (the seam persists): nonzero √−3 / √−15 components appear in pair cells.
  Either verdict banks; a third outcome (values outside the declared span) banks as its own
  finding with the residual exhibited.
- **Q3 (data, no prediction):** the orders and eigenvalue-exponent supports of W₁, W₂ at 45.

## Guards

Cross-prime agreement on every reconstructed value (≥3 primes; a disagreement kills the cell,
never averaged). The level-15 gate above (MB12-style positive control: the pipeline must SEE
the known seam before being trusted to report absence). Runtime is sized by Q3 first (the
order computation, cheap mod p); if the DFT-over-powers cost at 45 exceeds the session budget,
the declared fallback is a partial a-grid — reported as coverage, never silently truncated.
