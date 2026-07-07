# B465 — INTAKE + reading rules: the "8×4×3 two-generator monodromy" handoff (2026-07-07)

**Committed before the exact runs. Firewalled. Incoming from the FINAL INTEGRATED HANDOFF
(Chat-1 floating-point + Chat-2 exact-claimed); the standing rule applies: verify every
cross-chat claim before banking; burden-inversion on every structure.**

## Provenance note (recorded, firewalled)

The owner notes the exploration route ran through narrative/mythological material (the
speculation lane). Per the standing architecture (`speculations/`, motivation-required):
the motivation is recorded, the mathematics stands or falls by computation alone.

## The construction (pinned from Chat-2's seam package, `chat2_seam_package_20260702.zip`)

N = 15; z = ζ₁₅; D = diag(z^{j(j−1)/2}); F = DFT/√15; Wl = D; Wr = (F·D·F†)†;
W₁ = quantize('RL') (order-20 exponents K1, banked B376); W₂ = quantize('RRLL')
(order-12, K2); Par: j → −j. The handoff's objects: U = Par·W₁; **M(l) = Par·W₁·W₂^l**
(reconstruction validated: l=1 reproduces the claimed 8-4-3 order multiset exactly in
float; exact verification below). Galois twists: z → z^c, √15 → (c|15)√15 (Gauss sum;
Chat-2's stage-2 convention), c ∈ (ℤ/15)*; QR class {1,4}.

## Claims table (verify → adjudicate)

| # | claim | source tier | verification route |
|---|---|---|---|
| C1 | M(1) has 15 modes splitting 8/4/3 by rotation period 60/15/30 | Chat-2 "exact" | F_p (p ≡ 1 mod 60, two primes): eigenvalue orders + multiplicities |
| C2 | l-sweep: 15 singletons at l=0; 8-4-3 at l=1,4; "11-fold" at l=2,3; "period 3 in l" | Chat-2 | exact l = 0..11 + the classical-shadow test (below) |
| C3 | U = Par·W₁ has order 60, 15 modes, 3-6-3-3 bands | Chat-2 | exact spectrum |
| C4 | QR c gives 15 modes, NQR c gives 9 | Chat-2 | exact c-scan of distinct-eigenvalue counts |
| C5 | non-abelian monodromy (32 loops, 0/36 commuting), cycle structure 8×4×3 | Chat-1 float | **construction not shared** — what is determinate: the exact spectra constrain any tracking; bin UNVERIFIABLE-UNTIL-SHARED otherwise |
| C6 | all 8 c-values have distinct eigenvalue spectra; max\|tr\| = √5 (c=1) vs √15 (others) | Chat-1 float | exact char-poly distinctness; the trace bound with an MB12 vacuity check (√15 = the trivial Gauss/Parseval ceiling?) |
| C7 | dark points carry more distinct eigenphases (12.2 vs 8.2; 42 dark-only) | Chat-1 float | reconstruct per-address operator if determinate; else bin |
| C8 | "8 = SU(3) octet", "15 = SU(4)/SO(6) adjoint", "4 = 3̄+1 ⇒ Pati–Salam" | naming | **HELD(value-matching) from birth** (B452 frozen rule: structural predicates cannot fire alone); adjudicated at the eigenspace level |
| C9 | 15/9 ↔ V₁₇/V₉ of 27 = V₁₇+V₉+V₁ | naming | dimension check first (17 ≠ 15 on its face); HELD |

## Reading rules (fixed now)

- **The float reconnaissance already found the parsimonious structure the handoff
  missed**: spec(M(1)) = ζ₆₀⁸·{1, i, −1, −i} with eigenspace dims (4,4,3,4) — i.e.
  M(1)⁴ = ζ₆₀³²·I (scalar). If exact: the "octet" is 4⊕4 (two DISTINCT eigenvalues), the
  8/4/3 split is the arithmetic of which scalar-dressed 4th-roots are primitive 60th
  roots — and the SU(4)→SU(3) branching reading (8+3+3̄+1, needing an irreducible 8) is
  **REFUTED at the eigenspace level**, not merely unmatched.
- **The classical-shadow launder test (the decisive bin)**: M(l) quantizes
  −A₁A₂^l ∈ SL(2,ℤ/15) (exact Egorov, banked B376 mechanism). If the spectral structure
  of M(l) is a function of the classical conjugacy data (order, trace) of −A₁A₂^l mod 15
  across the whole l-sweep and c-scan, the entire phenomenon is the Weil functor reading
  SL(2,ℤ/15) class arithmetic — **LAUNDERS** (class data, not object dynamics). Metallic
  m-control: the same test at a second word pair where feasible.
- Any residual structure not so derived → burden-inversion; H1 only via B398 (owner
  present).
- C5/C7 floating-point items without shared constructions get the standing prior: recorded,
  burden-inversion applies on arrival of the construction.
