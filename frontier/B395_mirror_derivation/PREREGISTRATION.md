# B395 (Closure II / M3) — PRE-REGISTRATION: derive the mirror law from the trace formula

**Committed before computation. Target: upgrade P61's mirror law t(a,−b) = τ₃(t(a,b))
from verified to DERIVED. Time-box: 1 session.**

## The route (the character-identity reduction)

Reindexing the DFT gives: mirror ⟺ a statement about C[j,−l] vs C[j,l]. On the formula's
domain (P64), C[j,l] = ζ₆⁻¹·χ(j,l)·ζ₁₅^{Q_{jl}} with χ = tr(W₁ʲW₂ˡJ⁻¹). τ₃ restricted to
ℚ(ζ₁₅) is the Galois element σ₁₁ (11 ≡ 1 mod 5, ≡ −1 mod 3). REGISTERED CLAIM (the lemma
that would constitute the derivation):

    C[j, −l] = σ₁₁( C[j, l] )   for ALL (j,l)  — cell-wise, in ℚ(ζ₁₅)

(equivalently χ(j,−l)ζ^{Q_{j,−l}} = σ₁₁(χ(j,l)ζ^{Q_{jl}}), including the boundary cells —
stated directly on C to avoid domain bookkeeping). If the cell-wise law holds, the mirror
follows by exact summation: t(a,−b) = Σ ζ₂₀^{−ja}ζ₁₂^{−lb}·σ₁₁(C[j,l])/240, and since σ₁₁
fixes ζ₂₀-windows? — NO: σ₁₁ on ζ₂₀: 11 mod 20 = 11 ≠ 1 — the window bookkeeping must be
carried exactly: the summation step is part of the verification (engine-exact, not
hand-waved; the standing Π_H hazard applies). The registered final gate: reproduce
t(a,−b) = τ₃(t(a,b)) on the full banked table FROM the cell-wise law + exact summation
alone (no direct use of the banked mirror).

KILL: the cell-wise law fails — bank the failing cells and their pattern (the mirror then
has NO cell-local origin, itself a sharp structural fact echoing B389's twist-blocked
inversion).

Machinery: the exact ζ₆₀ engine + banked pow-caches. Locks from output JSON. Firewalled.
