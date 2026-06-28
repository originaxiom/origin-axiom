# B259 — the gravity brick (what the object *does* supply) + an honest theorem-vs-gap map of the five walls

**Status: banked observation (frontier). The MATH (Mostow metric solves 3d Einstein; action = complex CS) is
firewall-clean differential geometry; the PHYSICS reading (3d quantum gravity, `G·Λ`, simplicity constraints, DESI)
is FIREWALLED → `speculations/S043`. Nothing to `CLAIMS.md`.** Built in response to "stop grading, lay the first
stone." Two digests (chat2: *tighten* the headline; chat1: I *over-firewalled*) are both partly right — this probe
records the resolution.

## The three ingredients that exist
1. **Metric (Mostow).** The figure-eight complement has a *unique* complete hyperbolic metric (Mostow rigidity) →
   a canonical frame field. **STONE 1, verified (sympy):** a constant-curvature(−1) metric has `Ric = −2g`, `R = −6`,
   and **solves 3d vacuum Einstein** `R_ij − ½R g_ij + Λg_ij = 0` with **`Λ = −1` exactly**. Hyperbolic ⟺ Einstein
   with Λ<0; the Mostow metric *is* a 3d Einstein solution (Witten 1988). The object genuinely supplies the metric
   input — that part of chat1's "brick" is real.
2. **Action (Witten–Gukov).** 3d gravity with Λ<0 = `SL(2,ℂ)` Chern–Simons; the action on the hyperbolic structure
   = the **complex volume** `Vol + iCS = 2.0299 + 0i` (B250). Real, banked.
3. **Level (golden).** `k=3`; via Smolin/Kodama `k = 6π/(GΛ)` → `GΛ = 2π`. Real arithmetic — but firewalled and
   caveated (4d combo; `k` vs `k+2=5`; **Planck-scale**, see the magnitude gap and S043).

## The join — and why it is the wall, not an available calculation
The simplicity constraint `B = e∧e` (Plebanski → GR from BF) is a **4D** construction: it needs a 4D tetrad `e^I`
(`I=0..3`). Mostow supplies a **3D dreibein** (a metric on a 3-*manifold*). So:
- **in 3D the pipeline closes trivially** — hyperbolic = Einstein, and 3d gravity is *topological* (no local d.o.f.,
  no simplicity constraint needed). Nothing new closes; it's the definition.
- **in 4D the pipeline is the 3d→4d lift** (class S / a 4-manifold), which the object does *not* supply (B253).

So "do the Mostow tetrad + `k=3` + `GΛ` close into 4D Einstein?" = exactly **wall #4**. The ingredients are real; the
join is the wall. Chat1's build question is well-posed and the inputs exist — but the missing step is the one the
program already located, not a calculation with available ingredients.

## The five walls — honest classification (the real deliverable)
After verifying both digests' load-bearing claims, the summary "walled by theorem" was **too strong** (chat1's
correction lands), *and* "the quantum face reaches the SM skeleton" was **too loose** (chat2's correction lands).
The honest map is **one theorem + one quantitative gap + three open gaps**:

| # | wall | status | why |
|---|---|---|---|
| 1 | `SL(2,ℂ)` holonomy vs **compact** E₆ | **THEOREM** | `SL(2,ℂ)` has no nontrivial finite-dim unitary rep → no nontrivial hom into compact E₆ (B247); the *holonomy-breaking* bridge can't start. *But:* the `SL(2,ℂ)` character variety **is** the Coulomb branch of `T[4₁]` — as a Coulomb coordinate (not a gauge holonomy) it is **not** walled by compactness. (OPEN reframing) |
| 2 | McKay-E₆ vs a dynamical gauge group | **OPEN** | `T[4₁; E₆]` (type-E₆ 3d-3d) is uncomputed (DGG) — a real gap. *Hidden step:* the input-E₆ (choice of 6d theory) is **not** the output McKay-E₆ (from `ℚ(√−3)→2T→E₆`); computing it wouldn't by itself link them — the link is the open question (same letters, different categories). |
| 3 | chirality / amphicheiral `τ` | **OPEN** | object is CP-symmetric, `78` real (B252); but **SSB of `τ` could source chirality** — a sharp, well-posed question needing external dynamics (B253). Hard ≠ impossible; object-undecidable ≠ undecidable. |
| 4 | 3d (`T[4₁]`) vs 4d (SM) | **OPEN** | `T[4₁]` is 3d (3d-3d, K006); the class-S 4d lift exists as a framework but is uncomputed for this object. |
| 5 | scale / DESI (topological Λ) | **QGAP + HOOK** | `GΛ` is provably dimensionless (scale-free). Golden `k=3 → GΛ=2π` is a **Planck-scale** Λ; observed dark energy needs `k ~ 10¹²⁴` (the c.c. problem). The topological-Λ idea (`k` counts transitions → stepwise Λ → evolving DE, cf. DESI 2.5–4.2σ) is a firewalled hook (S043) — but `k=3` is **122 orders** from observation, so it is *not* the DESI dark energy. |

**Net.** Exactly **one** wall is a theorem (#1, and only for the holonomy-breaking framing); the rest are uncomputed
gaps, each with a published framework (Coulomb branch, 3d-3d `T[4₁;E₆]`, SSB dynamics, class-S lift) — *and* a
122-order quantitative obstruction on #5. "The gap is structure, not ignorance" remains the honest headline for #1
and the scale-freeness; for #2–#4 the honest word is **uncomputed**, not **impossible**.

## Side-fix (chat correction, verified)
`4 ≠ Fibonacci`: SU(2)₃ has **4 primaries** {0,½,1,3/2}; **Fibonacci is the 2-object** integer-spin subcategory
{1,τ}. (Repo grep: not banked wrong anywhere — the conflation was only in the chat draft. B254 already states the
coset is a *CFT coset, not a gauge group*.)

Anchors: B247 (compact-E₆ theorem), B250 (complex volume), B252/B253 (CP-symmetry / 3d-not-4d), B254 (coset, not
gauge group), K006/K018 (3d-3d / scale-free). Lit: Witten 1988 (2+1 gravity = CS); Gukov (complex CS = complex
volume); Dimofte–Gaiotto–Gukov (3d-3d); Smolin/Kodama (`k=6π/GΛ`); DESI DR2 2025 (evolving-DE hints).
