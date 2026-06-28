# NOVELTY — the E₆-bridge arc (B262–B277), adversarial prior-art assessment (R6, 2026-06-28)

Deep-research adversarial prior-art pass (workflow `wa2zghuze`; ~30 search/verify agents). Verdict enum: KNOWN /
PARTIALLY-KNOWN / APPEARS-NOVEL / NEEDS-SPECIALIST. Confidence: medium (absence of found prior art ≠ absence of prior
art). **This pass DOWNGRADED the load-bearing existence claim to a known framework — recorded honestly.**

## CLAIM 1 — E₆ character variety: dim H¹ = rank, ρ_prin a smooth point (B264 / B273 / B274 / B275)
**Verdict: KNOWN (framework). The in-sandbox contribution is a worked E₆ instance + explicit computation, NOT a new
theorem.**
- **Falbel–Guilloux 2015** ("Dimension of character varieties for 3-manifolds", arXiv:1510.00567): for a *general
  reductive* `G` (incl. exceptional, so E₆), an irreducible component of the character variety of a `t`-cusped
  3-manifold has `dim ≥ t·rank(G) − dim(G)·χ(M)`; for hyperbolic `M` (`χ=0`), `dim ≥ cusps·rank(G)` — **exactly the
  "dim H¹ = rank" count**, already covering E₆.
- **Menal-Ferrer–Porti** (Osaka 2012 twisted cohomology; J. Topology 2014 torsion; arXiv:1111.4338 local coordinates
  for SL(n,C)): the "principal-`sl₂`-composed holonomy is a **smooth point**, cohomology pinned to the cusp by the
  half-lives-half-dies injection `H¹(M)↪H¹(∂M)`" mechanism. Since `Ad∘(principal sl₂→e₆)=⊕Sym^{2mᵢ}` (Kostant
  exponents), the MFP vanishing applies **termwise** → the E₆ `H¹` is the sum over exponents `= rank`. **The B274
  smoothness IS MFP applied to E₆** (as B274 already states: the criterion is cited, not re-derived).
- **Falbel–FGKRT 2016** (Exper. Math.) and **Heusener–Muñoz–Porti 2016** (Illinois J. Math.): the explicit
  higher-rank figure-eight program — full `SL(3,C)` character variety, the distinguished `Sym²`-principal component.
  The "go beyond SL(2)" program exists; it **stops at SL(3)**, never reaching E₆/principal-`sl₂→e₆`.
- **Genuinely in-sandbox (verification, not new theorem):** the explicit exact (mod-p) `e₆` cup-product computation
  (B273), the exponent-graded packaging, the explicit witness (B275). Honest label: a **worked exceptional-group
  instance** of the Falbel–Guilloux dimension theorem + the MFP smoothness mechanism.

## CLAIM 2 — arithmetic selects E₆ via the ramified prime → 2T → McKay (B266)
**Verdict: PARTIALLY-KNOWN — pieces standard; the SELECTION-RULE overlay APPEARS-NOVEL (NEEDS-SPECIALIST).**
- Reduction `knot group → SL(2, residue field of a trace-field prime)` is **standard**: **Long–Reid 1998** (simple
  quotients; split primes), **Chinburg–Reid–Stover 2011** (explicit *ramified*-prime reductions), **Şengün 2012**
  (Bianchi-group reductions; `O_{−3}=ℤ[ω]`), **Riley** (`4₁ ↠ PSL(2,𝔽₃)` is classical).
- McKay `2T↔E₆, 2I↔E₈, 2O↔E₇` is **textbook** (**Dechant 2016**).
- **Not found in any reference:** the *arithmetic selection rule* combining them — ramified prime 3 → 𝔽₃ → 2T → E₆;
  `det=5` → 𝔽₅ → 2I → E₈; **E₇ "homeless" because 2O is never `SL(2,q)`**. This synthesis is the candidate-novel
  kernel — **APPEARS-NOVEL but modest** (a re-synthesis of standard pieces); **NEEDS-SPECIALIST** to confirm.
- **Verified asymmetry (R6 addendum):** Stuebner 2025 (arXiv:2502.06488) + in-sandbox GAP `GQuotients` (`2T`→2,
  `A_5`→0, `2I`→0) show the two ends are **group-asymmetric**: the E₆ end is a genuine `pi_1(4_1)` surjection onto
  2T; the E₈ end (`ℚ(√5)`, prime 5) is **field-level only** — the spherical companion's field, not a 4₁ surjection.

## CLAIM 3 — quantum invariant arithmetic at trace-field roots (B276)
**Verdict: KNOWN (phenomenon); the specific ζ₃-residue framing is a minor observation (matches B276's "PARTIAL").**
- Quantum modularity of the `4₁` colored Jones is **proven and active**: **Garoufalidis–Zagier** (figure-eight),
  **Bettin–Drappeau** (≤7 crossings). The **Habiro/Le cyclotomic expansion** of `J_N(4₁)` and the volume from
  `Li₂(e^{±iπ/3})` (`ζ₆` generates `ℚ(√−3)`) are standard. The canonical arithmetic framework is
  **Garoufalidis–Scholze–Wheeler–Zagier 2024** ("The Habiro ring of a number field", arXiv:2412.04241; `K_3`-graded,
  Frobenius-glued, Bloch-group modules) — exactly CLAIM 3's setting. The arithmetic of WRT special values (Habiro ring,
  Coste–Gannon Galois action, quantum modular forms) is established. B276's `ζ₃,ζ₆∈ℤ[ζ₃]` degeneration is a small,
  honest observation within this known framework — consistent with its self-labelled PARTIAL/coherence status.

## CLAIM 4 — amphichirality realized as the E₆ outer automorphism (B271)
**Verdict: NEEDS-SPECIALIST — both halves standard; the IDENTIFICATION is uninvestigated (zero verified prior art —
an absence of coverage, not confirmed novelty).**
- A knot symmetry **acting on a (higher-rank) character variety** is standard: **Heusener–Muñoz–Porti** (the `D₄`
  action on the SL(3) variety of `4₁`), **Paoluzzi–Porti** (invariant character varieties of symmetric knots).
- The `E₆` **outer automorphism** with fixed subalgebra `F₄` and the `(E₆,F₄)` symmetric pair (EIV) is **textbook**.
- **Not found:** realizing a knot's *amphichirality* **as** the `E₆` outer automorphism (chirality locus = the
  `26 = e₆/f₄`). **APPEARS-NOVEL as a framing**; modest; **NEEDS-SPECIALIST**.

## Net
The **load-bearing existence math (CLAIM 1) is essentially KNOWN** — Falbel–Guilloux (dimension, general reductive
incl. E₆) + Menal-Ferrer–Porti (smoothness/cohomology); B264/B273/B274/B275 are a **worked E₆ instance with explicit
computation**, not a new theorem (B274 already cites the criterion). The two **candidate-novel** kernels are both
**modest and NEEDS-SPECIALIST**: the arithmetic-selection overlay (CLAIM 2: ramified-prime → binary-polyhedral →
McKay-ADE *as a selection rule*, with E₇ homeless) and the amphichirality-as-E₆-outer-automorphism framing (CLAIM 4).
CLAIM 3 is KNOWN. **Honest framing going forward: cite Falbel–Guilloux / Menal-Ferrer–Porti / Falbel-FGKRT /
Heusener–Muñoz–Porti / Long–Reid / Chinburg–Reid–Stover / Dechant / Garoufalidis–Zagier; do not claim novelty for the
existence/dimension/smoothness; reserve any novelty claim for the CLAIM-2 selection overlay and the CLAIM-4 framing,
both pending a specialist close.** Nothing changes in `CLAIMS.md` (the arc was never promoted).
