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

**The degree=rank tower law — CONFIRMED at SL(4) (Path A, `dehn_filling.py`, V54).** The earlier P4
deferral is resolved: a smarter targeted search (sweep finite-order A-spectra, solve the bundle
condition for `B`) **does** find SL(4) Dehn-filling bundle reps, and the predicted relation lands:
- **A-spectrum `{1,1,ω,ω²}`** (`ω=e^{2πi/3}`, `char (z−1)²(z²+z+1)`, **`tr A=tr A⁻¹=1`** — the direct
  analogue of SL(3)'s W1 spectrum `{1,i,−i}`): the scalar criterion **`[A,B]=c·μ⁴` ⟺ `M⁴=L`** holds —
  **degree = rank**. Confirmed to **~9e-39** at high precision (`dehn_filling_highprec.py`; controls
  k=3,5 are O(1)); median ~5e-13 over a 15-rep family.
- **A-spectrum `{primitive 8th roots, char z⁴+1}`** (`tr A=0`): a SECOND Dehn-filling component giving
  **`M³=L`** (a different degree).

So the **degree=rank law** — on the SL(n) figure-eight bundle's principal Dehn-filling component
`{tr A=tr A⁻¹=1}`, the longitude is the meridian's n-th power `Mⁿ=L` — is confirmed for **n=3 (V47)**
and **n=4** (here). Honest caveat: SL(4) has *more than one* Dehn-filling component (the `{z⁴+1}` one
gives `M³=L`), so the rank-th power lives specifically on the `{tr=1}` component; degree=rank is the
relation on that principal component, not the only one. The **SL(2) end is degenerate** (A0,
`test_b73_dehn_filling`): `Fix(T_1²)` is a single geometric component, no Dehn-filling component,
`L=M^k` not on Cooper–Long. The **`j=1728` link remains a separate, untested hypothesis** (and Path B,
V53, independently confirms j=1728 is an isolated symmetry-forced point with no Coulomb structure).
Label: high-precision-numerical (~1e-39), not yet symbolic-exact.

- `probe.py` — `sym_power`, `monodromy` (general `n`), `meridian`, the Sym³ shadow check.
- `dehn_filling.py` — `realize_bundle_rep`, the degree=rank test; `dehn_filling_highprec.py` — the
  ~1e-39 mpmath confirmation.
- Tests: `tests/test_b73_sl4_apoly.py`, `tests/test_b73_dehn_filling.py`. Ledger rows **V50**, **V54**.

Standalone character-variety mathematics; no physics, no Origin claim. Proven core P1–P16 untouched.
