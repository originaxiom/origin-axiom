# B447 — PREREGISTRATION: the m-scan harness (Thermodynamic Campaign, D2)

**Committed BEFORE computation. Firewalled; nothing to `CLAIMS.md`. Campaign: docs/OPEN_LEADS.md
§"The thermodynamic campaign"; frame: speculations/S054.**

## The question (blind)

Is the golden member (m=1) of the metallic family **thermodynamically exceptional** — beyond the
three whitelisted mechanisms — or is every warm observable a smooth function of the class
parameter? Prior probes compared golden to silver/bronze pointwise (a 2–3-point scan that cannot
distinguish a smooth trend from an exception). This harness computes five warm observables across
**m = 1..6** and classifies each as smooth-in-m vs exceptional-at-m=1.

The metallic chain: substitution `a → aᵐb, b → a` (incidence `[[m,1],[1,0]]`, PF eigenvalue
`λ_m = (m+√(m²+4))/2`); diagonal tight-binding model, onsite `±V` by letter, hopping 1;
periodic-approximant words of length ~1500.

## The observables (all functionals of the object-as-quasicrystal)

1. **C(T)** — specific heat from the single-particle spectrum (canonical). **B181 pre-kill
   honored:** the chain is permanently critical, there is NO intrinsic T_c — C(T) is read as
   critical-at-all-T structure (multi-peak/log-periodic, the known Cantor-spectrum behavior),
   never as a transition hunt. This also computes, from scratch and in-repo, what Chat-2's
   "Direction 0" claimed in chat only (its numbers never landed in the repo).
2. **β(V)** — the anomalous transport exponent: `⟨x²(t)⟩ ~ t^{2β}`, wave-packet spreading with
   boundary guard, V ∈ {0.5, 1, 2, 4}.
3. **f(α)/D_q** — multifractal dimensions of the spectrum at matched resolution
   (box-counting D_q, q ∈ {−2..4}). **In-repo anchor (gate):** B163's matched-depth
   D₀ ≈ 0.91 (golden), 0.77 (silver) must reproduce.
4. **Gap-label realization table** — realized labels `(p,q)` in `ℤ + ℤθ_m` sorted by gap width.
   **The θ_m module trap (documented in the plan):** θ_m = the b-letter frequency
   `= 1/(1+λ_m)`, NOT `(√(m²+4)−m)/2` — the wrong generator manufactures fake asymmetries.
5. **γ(E)** — transfer-matrix Lyapunov on/off spectrum (B181's observable, extended across m):
   expected ≈ 0 on-spectrum for all m (permanent criticality is class-wide).

## The stratification guard (pre-registered trap)

`m²+4` = 5, 8, 13, 20, 29, 40 → squarefree kernels 5, 2, 13, **5**, 29, 10. **m=4 shares
golden's field ℚ(√5)** — the same-field control inside the scan: an m=1 exception caused by the
5-ramification/field mechanism must reappear at m=4; an exception at m=1 ONLY is either
CF/Hurwitz-extremality or the Jones wall (both whitelisted, must be traced explicitly) or
genuinely new (escalate). Prime-vs-composite `m²+4` accidents are read against this
stratification, not as m=1 magic.

## Registered outcome split (three bins, fixed now)

1. **LAUNDERS** — every observable is smooth in m (monotone/interpolable in λ_m), or its m=1
   behavior is explicitly traced to a whitelisted mechanism {Jones wall λ₁<2 (B218), CF/Hurwitz
   extremality (B176/B181), 5-ramification (B446's S₅ mechanism)} with the m=4 field-partner
   check applied.
2. **NEW-MATH** — a sharp, previously-unstated law of the m-family (e.g. a closed form for
   β(V,m) or D₀(V,m)) that is real but class-level mathematics.
3. **H1-candidate** — an m=1 exceptionality NOT reducible to the whitelist under the
   burden-inversion rule (one session to exhibit F, out-of-sample at a second V and the m=4
   partner) → B398 discipline before voicing.

**Prediction (stated for honesty):** LAUNDERS. All five observables smooth in m; D₀ and β
decrease with m at fixed V (stronger effective coupling); C(T) multi-peak for ALL m
(class-generic hierarchical spectrum, matching the known log-periodic literature); γ≈0 on
spectrum for all m. The only m=1 flags expected are the whitelisted three.

## Controls (fixed now, computed alongside)

- **Simpler-system:** periodic chain (β=1 ballistic, trivial C(T) with a single Schottky-like
  peak family, D₀=1, empty gap-label table) and random chain (β≈0 localized) — the three-regime
  gate.
- **Same-class:** the m-scan IS the class control; m=4 is the same-field partner.

## Reproduce-gates (known numbers first)

- Three-regime transport: periodic β=1.00 (±0.05), random β≈0 (<0.15), Fibonacci strictly
  between — the Damanik–Tcheremchantsev regime structure (anomalous, sub-ballistic,
  V-decreasing).
- B163 anchor: D₀(golden) ≈ 0.91, D₀(silver) ≈ 0.77 at matched depth.
- Gap labels land on `ℤ + ℤθ_m` with residual ≤ 1e-3 (the module check).

## Lit-gate (mandatory line)

Nearest published: the Fibonacci multifractal spectrum is **classic 1986–89 literature**
(Kohmoto–Kadanoff–Tang lineage; Fujiwara–Kohmoto–Tokihiro; rigorous dimensions
Damanik–Gorodetski); anomalous transport bounds are Damanik–Tcheremchantsev; Cantor-spectrum
specific heat with log-periodic oscillations is published (Tsallis-school and successors,
Carlos/Vallejos-type analyses). **Our delta: the systematic m-scan of the metallic family with
the exceptionality classifier and the m=4 same-field control — the family-level question, not
the single-chain facts.** No "first f(α)" claim.

## MB-guards

MB12 (vacuity): the classifier can fire (a non-whitelisted m=1 exception) and can fail (all
smooth) — both outcomes bank. MB7/MB8: no value-matching against physical constants; B218
calibrates what a *launderable* m=1 exception looks like. The B181 no-T_c pre-kill is honored;
any apparent "transition" in C(T) is artifact-suspect first (finite-size Schottky structure).

## Machinery

numpy exact diagonalization (N≈1500 approximants; O(N³) trivial); time evolution via
eigendecomposition with edge-occupation guard <1e-8; float64 with a spot mpmath cross-check on
one m if any rank/threshold decision arises. Everything scripted in this directory;
FINDINGS.md + test lock on bank.
