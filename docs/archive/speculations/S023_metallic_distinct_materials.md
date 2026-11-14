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

> **⚠ Confirmation (Chat-2 interlude — the demotion stands).** A longer-chain re-check found the box-dimensions
> **do not cleanly separate**: golden/silver/bronze hover ~0.4–0.5 and drift with chain length, the m-to-m
> differences within the drift (not converged). This **reconfirms the W1 demotion** — the box-dimension is
> finite-size/supporting only; `TESTED-POSITIVE` rests on the exact arithmetic field-distinctness, which is
> unaffected. No re-scope needed.

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

## Which seeds share a field — the collision / Pell structure

**[MATH] (verified in-session).** Distinct seeds need **not** give distinct fields: `squarefree(m²+4)` collides.
The seeds sharing `ℚ(√5)` are *exactly* the odd-index Lucas numbers `m ∈ {1, 4, 11, 29, 76, 199, …}` — the
solutions of the Pell equation `m² − 5a² = −4`; likewise `{2, 14, …}` share `ℚ(√2)` and `{3, 36, …}` share
`ℚ(√13)`, each its own Pell family `m² − d·a² = −4`. So the arithmetic fingerprint is the **field**, not the digit
`m`: two different seeds in the same field are the *same* material arithmetically. (Verified: `squarefree(m²+4)`
enumerated over `m ≤ 60`; the Lucas/Pell identification by direct solve.) The full structure of which `(m, m′)`
collide is a clean open number-theory lead, logged in `../docs/OPEN_LEADS.md` (L16).

**[LEAD] (the field-multiplicity rank conjecture — NOT banked).** A review session proposed that for a quasicrystal
built by *coupling* several metallic seeds, the gap-labeling / Fourier-module rank is `1 + (#distinct fields)` — the
distinct-field count, not the seed count. The rigorous pieces (mine, this session): a single seed gives rank 2 (the
`ℤ + ℤα_m` module, standard); same-field seeds cannot raise the rank past 2 (one quadratic field is 2-dimensional);
distinct fields contribute `ℚ`-independent `√d` directions (classical). The **open, and possibly false, step** is
that the *coupled* module is exactly `ℤ ⊕ Σ(seed frequencies)` with no cross terms — a product / cut-and-project
coupling can introduce `√(dᵢdⱼ)` directions (golden × silver → `√10`), which would push the rank *above* `1+k`. So
this is a lead, not a theorem. The physical reading (diffraction-measurable Fourier-module rank) is `PERMITTED`,
firewall-honored (the scale is the real material's — door 4). **NB** this "coupling" is a *combined substitution*,
which is **not** B131/K014's 3-manifold cusp-gluing (a different construction — do not conflate). Logged: L16.

Related: `S007` (the SL(n) gap-labeling hook — its SL(2)/m-family part is now computed here; the SL(n≥3) part stays
blocked), `K007` (the KKT/quasicrystal anchor), `../frontier/physics_probes/metallic_spectra.py`, B107, **B120**
(the m-universal algebra this contrasts against).
