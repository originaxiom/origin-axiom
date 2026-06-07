# S023 — the metallic means are genuinely distinct real quasicrystals (m-universal algebra, m-distinct physics)

**Status: `TESTED-POSITIVE`.** Firewalled; not a claim; 1D condensed matter, **not** fundamental physics. Phase 1 of
the physics-bridge sweep. Cites the mathematics one-way; nothing promotes to `../CLAIMS.md`; the physics chapter
stays CLOSED.

**Structural fact (cited, external + repo).** The SL(2), Hermitian, single-channel tight-binding chain on the
metallic substitution `a → aᵐb, b → a` is a **genuine, buildable quasicrystal** (golden m=1 = Fibonacci; silver m=2
= Pell/octonacci; bronze m=3) — studied in photonic lattices, cold atoms, polariton condensates. The trace map of
this chain **is** the Kohmoto–Kadanoff–Tang map (B107/K007); its spectrum is a zero-measure Cantor set whose gaps
obey the gap-labeling theorem (Bellissard, external). The m=1 case is textbook (1992).

**[MATH] (the sharp hinge, computed — `metallic_spectra.py`).** B120 proved the trace-map **algebra** — the Sym
two-sequence `μ_d` — is **m-universal** (it depends only on `(n, det)`, never on the seed `m`). The **physics** is
not: the metallic means are **arithmetically distinct materials**.
- **Gap-labeling field.** The IDOS gap labels live in `ℤ + ℤα_m` with `α_m = φ_m/(φ_m+1) ∈ ℚ(√(m²+4))`; the
  squarefree discriminants are `{5, 2, 13}` for m=1,2,3 → **three distinct quadratic fields** `ℚ(√5), ℚ(√2),
  ℚ(√13)`. (Verified: 10/10, 12/12, 12/12 of the largest gaps land on the predicted lattice.)
- **RG length-scale.** The renormalization (decimation) scaling is `φ_m = (m+√(m²+4))/2` — distinct per m
  (`1.618, 2.414, 3.303`).
- **Spectral fractal dimension.** The box-counting dimension of the spectrum differs per m (`≈0.628, 0.636, 0.650`;
  **numerical / finite-size — supporting, not load-bearing**). The dimensions are computed **in-house** on the actual
  silver/bronze chains (not extrapolated from the golden-case literature), but the values are close and finite-size,
  so this is a *supporting* signal, not the keeper.

**What `TESTED-POSITIVE` rests on (the scope, sharpened).** The load-bearing claim is the **arithmetic
field-distinctness** (`ℚ(√5),ℚ(√2),ℚ(√13)` — exact) and the **distinct RG scale `φ_m`** (exact). The spectral
box-dimension is a *supporting, finite-size* dynamical observation, not the foundation of the result — the metallic
means are distinct because they live in **different quadratic fields**, which is exact arithmetic regardless of any
dynamical sub-claim.

**[LEAP] (kept separate).** "The algebra is **one** object (m-universal, B120); the physics is a **family of
distinct materials**." The connection-to-reality your intuition senses is real and computable — it is the
**spectral theory of buildable quasicrystals** (silver/bronze are realizable), each with its own quadratic-field
fingerprint — not masses, Λ, or spacetime (all DEAD; see `../docs/atlas/FAILURE_ATLAS.md`).

**HONEST SCOPE (what is identification vs. new).** The gap-labeling *technology* and the m=1 case are textbook;
what is **new** here is the **systematic metallic-m family** computed in one place, and the explicit
**algebra-universal / physics-distinct contrast** against B120 — a genuine, falsifiable statement about a family of
real materials. It is **1D condensed matter**, not cosmology. The **SL(n≥3)** extension is blocked: the multichannel
chain is non-Hermitian (no quantum Hamiltonian; `sln_multichannel_probe`, S007), so this distinctness result is an
**SL(2)** statement.

**Kill condition (passed).** Had the metallic spectra been affinely equivalent (one field, one dimension), this
would be `TESTED-NEGATIVE` ("same material rescaled"). They are not — the fields are distinct → first-class
positive.

Related: `S007` (the SL(n) gap-labeling hook — its SL(2)/m-family part is now computed here; the SL(n≥3) part stays
blocked), `K007` (the KKT/quasicrystal anchor), `../frontier/physics_probes/metallic_spectra.py`, B107, **B120**
(the m-universal algebra this contrasts against).
