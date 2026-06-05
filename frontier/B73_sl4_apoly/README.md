# B73 — SL(4) figure-eight A-variety from the trace map (rank-4 B71)

The B71 pipeline (`realize → monodromy → eigenvalue ratios`) at rank 4: the monodromy `t` is the null
vector of the **32×16 Kronecker** system, and the genuine meridian `μ = w⁻¹t = A⁻¹t` uses the same
rank-independent conjugator `w=a` (V46).

**Established (exact-ish, numerical):**
- The **32×16 Kronecker monodromy** solves (residual ~1e-10), and the **V46 meridian fix is
  rank-independent**: `μ = A⁻¹t` commutes with the longitude `[A,B]` (~1e-10), `eig(μ)=eig(t)`.
- The **geometric branch via `Sym³: SL(2)→SL(4)`** of the figure-eight holonomy reproduces `Sym³` of the
  SL(2) monodromy exactly: `eig(t4) = (4th root of unity)·{μ³, μ, μ⁻¹, μ⁻³}` to ~1e-12 — the Sym³
  **shadow** of the Cooper–Long figure-eight A-polynomial (the rank-degree eigenvalue pattern,
  exponents ±3, ±1).

**Honest boundary (deferred):** a genuine SL(4) *Dehn-filling* component (the analogue of SL(3)'s
W1/W2 = ±3 fillings, where the predicted **degree-4 relation `L⁴=M`** and a possible link to the SL(2)
spectral-curve **`j=1728`** would be tested) requires the SL(4) character-variety **fixed locus**, i.e.
the SL(4) trace map (B48 is SL(3) only). A direct numerical fixed-locus search at candidate
root-of-unity A-spectra found **no** SL(4) bundle reps — the right Dehn-filling spectra aren't known a
priori without that machinery. So the **degree-4 / `j=1728` hypotheses are untested here** (recorded
open, not claimed). The Sym³ geometric branch is the validated higher-rank content.

- `probe.py` — `sym_power`, `monodromy` (general `n`), `meridian`, the Sym³ shadow check.
- Tests: `tests/test_b73_sl4_apoly.py`. Ledger row **V50**.

Standalone character-variety mathematics; no physics, no Origin claim. Proven core P1–P16 untouched.
