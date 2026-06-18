# B164 — the 4-punctured-sphere Fricke cubic + the metallic monodromy (P1 of Masterplan II, PR1)

**Date:** 2026-06-18. **Status:** the first artifact of P1 (Betti→Hitchin / isomonodromy, `OPEN_LEADS` H5-c):
the **(0,4) Jimbo–Fricke cubic** built explicitly, its **Painlevé-VI / MCG dynamics** (the three Vieta
involutions) exhibited, **bridged** to the once-punctured-torus (OPT) cubic at the void fiber, and the **metallic
degrees** placed on the realization. Standalone character-variety / dynamics mathematics; **no Origin-core claim,
no physics**; P1–P16 frozen; nothing to `../../CLAIMS.md`. Ledger V159. Reproducer `cubic04.py`. **The
OPT↔(0,4) cover dictionary, the isomonodromy *flow*, and the firewall-relocation verdict are DEFERRED to PR2.**

## Why the 4-punctured sphere

The seed's Betti object is the OPT `(1,1)` character variety (a dim-2 Fricke cubic). The **only other** dim-2
Fricke cubic is the **4-punctured sphere `(0,4)`** (`dim = 6g−6+2n = 2` only at `(1,1)` and `(0,4)`) — and it is
the **Painlevé-VI / class-S monodromy manifold** (Cantat–Loray, Iwasaki, Boalch; cited in B150). P010/§8c
identified it as the seed's natural composition partner and the gateway to the Hitchin/Higgs (dynamical,
scale-carrying) side. This stage builds it.

## Results

- **C1 [exact] — the cubic + its MCG dynamics.** The Jimbo–Fricke cubic
  `Φ = x²+y²+z²+xyz − p_x x − p_y y − p_z z − p_0` (with `p_x=t₁t₂+t₃t₄`, `p_y=t₁t₄+t₂t₃`, `p_z=t₁t₃+t₂t₄`,
  `p_0=4−Σtᵢ²−t₁t₂t₃t₄`; `tᵢ` the four boundary traces, `x,y,z` the channel traces). Its three **Vieta
  involutions** `s_x: x↦p_x−yz−x` (and cyclically) are each an **involution** and **preserve Φ** (symbolic). These
  generate the `(0,4)` mapping-class / **Painlevé-VI** action — *the dynamics exists on our object.*
- **C2 [exact] — the bridge to the OPT cubic.** At `tᵢ=0`, `Φ` becomes `x²+y²+z²+xyz−4`; under `z↦−z` this is
  `x²+y²+z²−xyz−4`, i.e. the **OPT Fricke cubic at `κ=2`** (the void / cancellation fiber, B161). So the `(0,4)`
  void fiber **is** the OPT `κ=2` fiber — a concrete OPT↔(0,4) link at a special fiber.
- **C3 [exact] — the metallic degrees.** `M_m=[[m,1],[1,0]]` has eigenvalue `λ_m=(m+√(m²+4))/2`, **dynamical
  degree `λ_m²`** (the trace-map / character-variety degree), and trace field `ℚ(√(m²+4))` — verified m=1,2,3
  (`ℚ(√5), ℚ(√8), ℚ(√13)`). These are the degrees the metallic monodromy contributes to the realization.
- **C4 [num] — the (0,4) dynamics is genuinely hyperbolic.** The composite `s_x∘s_y` is **loxodromic** — generic
  on-surface orbits grow geometrically (positive per-step log-growth), not periodic — with an MB-style **control**:
  a single Vieta involution is period-2 (bounded), so "loxodromic" is a real, falsifiable property. *Hyperbolic
  (positive-entropy) dynamics lives on the (0,4) cubic.*

## Honest scope — what is DEFERRED (PR2), and one corrected over-reach

- An initial draft claimed `s_x∘s_y` has dynamical degree exactly `φ²=λ_1²`; the numerics **refuted** it
  (point-orbit norm-growth tracks the *naive* degree, not the cancellation-reduced dynamical degree, and
  `s_x∘s_y` is not the figure-eight element). **Corrected:** C4 now claims only that the dynamics is loxodromic.
- The **OPT↔(0,4) double-cover dictionary** — so that the metallic `M_m` maps to a *specific* `(0,4)` word whose
  dynamical degree is `λ_m²` — needs the cover + a Pic-action degree computation (not orbit-norm growth). **PR2.**
- The **isomonodromy (Painlevé-VI) FLOW** as a genuine continuous "time" (a Schlesinger integrator on 4 Fuchsian
  points) and the **firewall-relocation verdict** (does the scale stay external — the Higgs field's, P010/§8c?
  expected YES) — **PR2.** This stage builds the static object; the flow is the next leg.

## Firewall
Standalone character-variety / dynamics mathematics. No scale, no Λ, no crossing; the Painlevé "time" (PR2) is
expected to be a dimensionless modulus (P006), and the scale external (P010/§8c) — to be tested, not assumed.
Nothing to `CLAIMS.md`; P1–P16 untouched.

## Anchors
B150/V139 (the class-S / Cantat–Loray / Painlevé citations), K001 (the OPT Fricke cubic + trace map), B161
(the κ=2 void/cancellation fiber), B67/B69 (the Fricke-cubic machinery mirrored here), P010 + `STRATEGIC_SYNTHESIS`
§8c (the Betti↔Hitchin hypothesis this tests), `speculations/S024` (the Hitchin side), `OPEN_LEADS` H5-c. Ledger
V159. External: Jimbo–Fricke / Iwasaki (the (0,4) cubic); Cantat–Loray (the dynamics, dynamical degree); Boalch /
Jimbo–Miwa (Painlevé VI as isomonodromy).

## Reproduction
`python frontier/B164_isomonodromy_04cubic/cubic04.py` — C1 (cubic + 3 Vieta involutions preserve it), C2 (the
void-fiber bridge), C3 (metallic degrees m=1,2,3), C4 (loxodromic witness + control). Prints `ALL CHECKS PASS`.
