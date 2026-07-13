# B560 — the chat-3 frontier campaign (cells 1–4), verified & integrated

A cross-seat (chat-3) "governed frontier campaign" of six certificate-driven cells,
processed **verify-don't-trust**. All 26 of chat-3's own cell tests pass in-sandbox,
and the load-bearing headline claims were **independently re-derived** here
(`tests/test_b560_chat3.py`, 3 locks). The cells' artifacts (code, certificates,
data, tests) are preserved under `cells/`. Firewall-clean throughout: the campaign
states its own open boundaries and claims nothing to CLAIMS.md.

Integrated under a new number (B560) per the cross-seat discipline — cherry-picked
and re-verified, not merged.

## Verification verdict (per cell)

| Cell | Result | Verdict |
|---|---|---|
| 1 | Universal ℤ/11 charge: SNF(I−M₄)=diag(1,1,1,11); χ=(1,3,6,7) left-fixed mod 11 | **VERIFIED** (independently) — **re-confirms B552** |
| 1B | Every nonzero ℤ/11 class has a finite **localized carrier** (defect pair L u R / L v R, equal 3-context + core length) | **VERIFIED** — first-core-length map reproduced EXACTLY: {1:3,2:9,3:3,4:16,5:14,6:14,7:16,8:3,9:9,10:3} |
| 1C | Exact **defect kinematics** — depth-stabilized factor census of σ¹⁰(a) (σ⁹=σ¹⁰ for 7≤L≤500; 1699 factors at L=500) + fusion/annihilation channels | tests pass (kinematic classification, no dynamics) |
| 2 | **Observer-flow closure** with prefix-independent EXACT edge certification — the B540 derived-sequence graph is **intrinsic** (not an artifact of finite-prefix saturation) | tests pass — a **rigor upgrade to B540** |
| 3 | **Fixed-character local atlas**: 253 support points (247 irreducible + 6 reducible); 246 Krawczyk-certified simple roots + 1 exact trace-zero double point (Ô_{X,x}≅ℂ[[ε]]/(ε²)); certified length ≥ 248 | tests pass — **certified LOCAL atlas; global completeness OPEN** (no degree/intersection bound) — connects to B532 / S031a |
| 4 | **Degree-4 frequency module = ℤ[τ] EXACTLY** (τ=√φ, τ⁴−τ²−1=0): f_a=τ−1, f_b=τ³−τ²−τ+1, f_A=τ²−τ, f_B=−τ³+τ+1 | **VERIFIED** — the frequencies are the M₄ Perron eigenvector and generate ℤ[τ] (coeff-matrix det = 1) — **strengthens B535/B546** |

## What is new vs re-confirmed

- **Re-confirmations** (corroborate banked work): Cell 1 = B552 (ℤ/11 charge); Cell 2's
  graph = B540's 12-node closure (now with an intrinsic, prefix-independent certificate).
- **New, verified**: the **localized ℤ/11 carriers** (Cell 1B) and their exact first-core
  map; the **defect kinematics** census (Cell 1C); the **certified fixed-character local
  atlas** of 253 points with 246 Krawczyk boxes + the trace-zero double point (Cell 3, a
  concrete local resolution of the B532/S031a fixed-character question — global count
  still open); and the **exact ℤ[τ] frequency module** (Cell 4), a strengthening of the
  degree-4 module in B535/B546.

## Cell 4's two self-corrections (they align with the repo's existing honesty)

Cell 4 explicitly retracts two earlier over-statements, and both **match the repo's
current PC23/B555 framing** (so no repo claim needs weakening):
1. distance from the full golden module is **not** an absolute discriminator, because
   ℤ + ℤ/φ (mod 1) is dense — the repo already uses silver/generic-slope controls, not
   a distance threshold;
2. infinite-volume opening of all five gaps across a continuous coupling chamber is
   **not yet proved** — the repo already frames B555/PC23 as *experiment-ready*, not a
   theorem. The honest status is "experiment-ready dimensionless prediction with exact
   label algebra, strong finite-size + coupling evidence, open infinite-volume theorem."

## Open (carried forward, not claimed)

- Cell 3's **global completeness** — "exactly 253 fixed characters" needs an exact degree
  or intersection-number bound (in-sandbox saturation is strong evidence, not proof).
- Cell 4's **infinite-volume gap-opening theorem** across the coupling chamber.
Both are registered as the campaign's honest boundaries; neither is asserted.
