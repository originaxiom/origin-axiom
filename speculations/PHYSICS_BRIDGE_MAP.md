# The physics-bridge map — every fork, classified (so we don't give up by missing the terrain)

Firewalled; not a claim. This is the **complete terrain** of bridges from the metallic trace-map / SL(n) tower to
physics — what is **DEAD** (do not revive), what is **LIVE & computable**, and what is **HEAVY/deferred**. The point
is honesty at scale: "don't give up on physics" means *knowing where it is already dead* and computing the few
genuinely-open forks to exhaustion. Nothing here promotes to `../CLAIMS.md`; the physics chapter stays CLOSED;
P1–P16 untouched.

## DEAD — do not revive (each killed by computation; kills in `../docs/atlas/FAILURE_ATLAS.md` + `TOMBSTONES.md`)

| bridge | why it is dead | kill |
|---|---|---|
| tower eigenvalues = masses / operator dimensions | one golden scale (moduli monodromy), not a fluctuation Hessian | B107 / V94 (S015) |
| torsion = masses | same category error | B107 / V94 |
| `Λ = Λ_Planck·φ⁻²ᴺ` (cosmological constant) | null hypothesis + circular | CLAIMS D1–D3 (S014) |
| Lorentzian spacetime from the Goldman/volume Hessian | computed **(2,0) Riemannian** | B96 / V80 (S016) |
| spacetime "climbs the ranks" | Lorentzian only at `k=2` | B101 R2 (S018) |
| 3+1D at SL(3) (dim count) | count is arithmetic; metric Riemannian | B101 (S017) |
| 3+1D from Cartan geometry | 3d→4d **type-mismatch wall** | S020 (WALLED) |
| entanglement = holographic | **log** entanglement = generic 1D-CFT; geometry AdS-like but generic | V37 (S021) |
| Seiberg–Witten / spectral-curve **family** in m | genus locked to 1; forced j=1728 CM coincidence; zero moduli | `spectral_curve_gate1/2`, V32–34 |
| Fibonacci-anyon **family** (silver/bronze TQC) | only m=1 (golden) categorifies (Ostrik); no unitary pentagon for m≥2 | `metallic_anyon_probe` |
| **SL(n≥3)** Hermitian quasicrystal chain | self-adjoint 1D transfer ⇒ symplectic; `SL(n)=Sp` only at n=2; n≥3 non-Hermitian | `sln_multichannel_probe` |
| tower = the Kostant **principal**-sl(2) adjoint decomposition | `⊕Sym^{2i}` ≠ the two-sequence (differ ∀n≥3) | B89-T / B98 |
| Bell/CHSH on the classical Fricke surface | `z=f(x,y)` deterministic ⇒ CHSH ≤ 2 | S006 / B108 |

## LIVE & COMPUTABLE — the genuinely-open forks (this sweep)

| # | fork | concrete computation | status |
|---|---|---|---|
| **Phase 1 / S023** | the **metallic-mean quasicrystals** are distinct real materials | gap-label field `ℚ(√(m²+4))`, RG scale `φ_m`, spectral dim — per m (SL(2), Hermitian) | **TESTED-POSITIVE** (`metallic_spectra.py`) — distinct fields `{√5,√2,√13}`; the algebra is m-universal (B120), the physics is not |
| **Phase 2 / S024** | the **monodromy sl(2) grading** of the adjoint + the Hitchin relation | the tower = the **external `det=−1` `GL(2,ℤ)`-action**; inequivalent to the principal/Kostant (Hitchin/Fuchsian, B101) for n≥3 by the `det=−1` parity (odd `Sym^d`) | **DONE (B121/V109)** — positive characterization; Hitchin reading firewalled (S024) |
| **S007** | the SL(n) operator gap-labeling | SL(2)/metallic-m part now computed (S023); the SL(n≥3) part is blocked (non-Hermitian) | POSTULATED → partially advanced |

## HEAVY / DEFERRED — mapped + feasibility-probed (Phase 3)

| # | fork | concrete computation | obstruction |
|---|---|---|---|
| **S025** | off-principal **irreducible** sector at higher rank (S011 continuation) | does independent spectral content exist off-locus at SL(4)/SL(5) or another knot? | no SL(4) char-variety classification (B115); EMPTY for 4₁/SL(3) (B110) |
| **S026** | the `T[4₁]` **state-integral / 3d index** at fixed knot, varying rank n | does the SL(n) A-variety (B71/B83) organize a tower of partition functions? | quantum-dilogarithm machinery cost; only the moduli level is citable (K006) |
| **S027** | **quantum modularity** of the metallic Kashaev invariants | the `GL(2,ℤ)` modular cocycle of `J_N` for metallic knots | the *continuous* family-in-m is dead (Gate 1); target the arithmetic/cocycle only |

## THE LADDER (B126) — how far does the rigidity propagate, and where exactly does it stop?

The deepest honest result (a five-agent literature survey + computation; full citations in `LADDER_LITERATURE.md`,
synthesis in `../frontier/B126_ladder_to_physics/FINDINGS.md`, reframe in `../philosophy/P007`). The question is not
"is there a bridge?" but **"how far up the ladder (quantize → 3d `T[M]` → 4d → particle content) does the object's
classical rigidity propagate?"** Answer: **exactly two floors, provably, then a nameable wall.**

| floor | does rigidity propagate? | status |
|---|---|---|
| **1 — arithmetic → quantization** | YES: the trace field determines the **field** of the perturbative quantum series | **THEOREM**, proven for our family (Yoon arXiv:2110.11003; DG 1202.6268) |
| **2 — Mostow → `T[M]` rigidity** | YES: no marginal couplings; `M` selects the SUSY phase (`4₁`→unbroken, gapped); `H₁` torsion → one-form symmetry | **ESTABLISHED** (Cho–Gang–Kim 2007.01532; DGG; ASvT) |
| **3 — 3d → 4d** | **NO**: the 4d theory is data of the 2d **boundary** `∂M`, not `M` | wall; ceiling **N=4 SYM / N=2\*** (Gaiotto; Kapustin–Witten) |
| **4 — SUSY scale / masses** | **NO**: orthogonal input; no manifold mechanism | wall (Douglas landscape) |

**So we lack no concept** — we lack what no 3-manifold can carry (the 2d-boundary data fixing the 4d theory, and the
SUSY-breaking scale). The new in-house structural fact at Floor 2 is `H₁(M_m)=ℤ⊕(ℤ/m)²` (the metallic `m` = the
torsion order, B126); its center-symmetry reading is `S029` (POSTULATED, five kills). The one genuinely-untested door
is whether the `K₃`/Bloch grading of the quantization is special on `ℚ(√−3)`/`ℚ(i)` (DORMANT, `S027`-adjacent).

## The discipline (why this is brave AND honest)

The framework is *a theory of the architecture of the possible, not the furniture of the actual*. The dead column is
not failure — it is the **shape**, mapped (`P003`). The live column is where computation can still teach us
something real: the metallic quasicrystals are **buildable materials** with distinct, measurable, field-theoretic
fingerprints; the 3d-3d correspondence is a **real QFT duality**. Bravery is computing those to exhaustion, each
with a kill condition — not reviving the dead. Every fork's status is a ledger fact; nothing crosses to
`../CLAIMS.md`.
