# B451 — thermo D4 / Relation R5: the trace-map Ruelle resonances — the gate caught a banked-number bias, the leading eigenvalue is now three-method-certified, the subleading spectrum is a named boundary

**Status: banked (frontier). Firewalled. Prereg: `PREREGISTRATION.md` (PR #611, before
computation). Verdict: the cycle-expansion machinery is VALIDATED at the leading
eigenvalue after an honest convention catch — the prereg's literal gate value (the banked
γ = 0.51) turned out to be a finite-time artifact of B186's estimator, discovered and
corrected here (B186's FINDINGS carry a dated correction note; its certification verdict
is untouched). The subleading resonances did not stabilize within the session budget —
named, quantified boundary. No H1.**

## The gate story (the honest chronicle — the B355 lesson again: conventions/windows)

1. Cycle expansion (orbits to N = 6–8, survivor-seeded Newton, two-grid checks) gave
   γ = 0.44–0.47 — REFUSING the prereg's literal gate (banked γ = 0.51). No resonance was
   read.
2. Adversarial cross-check #1: an independent DIRECT estimator (2D surface sampling,
   400k points, asymptotic windows) gave **γ = 0.443 ± 0.002** — agreeing with the cycle
   expansion, not the banked number.
3. Adversarial cross-check #2: **B186's exact code verbatim reproduces its banked value
   (0.509)** — so the banked number is real, but it is the **early-window value of the
   1D Schrödinger-line survival** (400 points, fit window 0.001 < f < 0.5, transient-
   inclusive). The same line data with dense sampling (200k points) and asymptotic
   windows converges to **0.451 ± 0.005**.
4. **Corrected ground truth: γ(λ=3) = 0.445 ± 0.006** — three independent estimators
   (cycle expansion 0.445, direct surface 0.443, dense-line asymptotic 0.451). The
   prereg gate, read against the corrected ground truth: **PASS** (the leading zeta zero
   IS the escape rate). B186's banked 0.51 was the same decay read too early; its
   certification verdict (γ > 0 ⟺ exponential escape ⟺ hyperbolicity signature) is
   completely unaffected — the correction is to the quoted VALUE's precision, recorded
   in B186's FINDINGS with a dated note.

## What is banked as data

- **The stable primitive-orbit table at λ = 3** (identical across every seeding
  configuration — grids 44–150, survivor depths 5–8): periods (1,2,3,4,5,6) have
  (0, 2, 0, 1, 2, 2) primitive orbits. The absence of fixed points and period-3 orbits
  on the surface is real (T's only ℝ³ fixed points, (0,0,0) and (1,1,1), lie off-surface)
  — the horseshoe's symbolic grammar is NOT the full 2-shift (the prereg's
  grammar-as-input discipline did its job; "expect 2^n" appears in the code as the
  refuted straw model).
- **The leading transfer-operator eigenvalue = the escape rate**, now certified by
  method-agreement (0.5% between cycle expansion and direct simulation) — the
  Bowen–Ruelle identity exhibited concretely on the object's own dynamics.
- κ-scan (stable-truncation, same caveats): γ(κ=2.5) ≈ 0.11, γ(κ=3) ≈ 0.15,
  γ(κ=4) ≈ 0.21 — monotone in κ as expected (faster escape at stronger coupling).

## The named boundary (what did NOT stabilize)

The **subleading zeros** (the resonances proper) vary with the orbit sets at n = 7, 8
(counts 2→4→5 across seedings — enumeration incomplete): second-resonance rate lands in
[0.64, 0.88] across enumerations. Two honest statements survive: (i) **a spectral gap
exists** — every enumeration puts the second resonance ≥ 0.19 above the leading rate;
(ii) the resonance VALUES are uncertified. The concrete unblocking requirement (priced):
certified-complete period-n enumeration for n ≥ 7 — exact Groebner/resultant per degree
(degree-2ⁿ systems; feasible n ≲ 8 with effort) or interval-arithmetic-verified Newton
with the DG symbolic dynamics. The m-control (silver word map) waits on the same
certification — running it with an uncertified enumerator would manufacture comparisons.

## Bins

Leading eigenvalue: LAUNDERS into classical thermodynamic formalism (Bowen–Ruelle),
as the prereg anticipated — the value is the object's escape rate, now measured
consistently. The banked-number correction: process win for verify-don't-trust (the
gate refused, and the refusal was information). Subleading spectrum: UNDECIDED-AT-DEPTH
(the licensed bin) — named boundary above. Lit-gate (cycle expansions for Fibonacci
trace maps, Cvitanović-school): pending; the spectral-gap observation is
NEEDS-LIT before any novelty word.

## Reproduce
```
python3 resonances.py 6          # grid-Newton version (the gate chronicle's step 1)
python3 survivor_enum2.py 8 3.0  # the stable-count + two-grid stability run
pytest ../../tests/test_b451.py  # locks: B186 reproduction, corrected gamma, stable counts
```

## Addendum (2026-07-08): the named boundary COMPUTED — the certified resonance spectrum at N = 8

The certification hybrid (exact algebraic counts + numeric points): sage Groebner on the
FULL fixed-point system (all three components + surface — the first attempt with two
components overcounted with spurious points, caught and corrected in-session) gives the
EXACT period-n point counts at λ = 3: n = 1..8 → ∅, 4, ∅, 8, 10, 22, 28, 48 — **all real,
all simple** (complex count = real count = squarefree at every n). The heavy numeric
enumeration matched everywhere EXCEPT n = 6 (16 of 22): **one primitive 6-orbit was
missing — recovered exactly from the algebraic variety — with |Λ| = 914.7**, a huge
multiplier and hence a vanishing Newton basin (why every seeding missed it; its 1/|Λ|
weight ≈ 0.001 is also why the leading eigenvalue was barely affected). Verify-don't-trust
at the orbit level: the algebra audited the numerics and found the one hole.

**The certified primitive table (n ≤ 8): {2: 2, 4: 1, 5: 2, 6: 3, 7: 4, 8: 5}** —
multipliers in `orbits_certified.json`. The certified cycle expansion:

| truncation | leading (escape rate) | 2nd resonance | 3rd (complex pair) |
|---|---|---|---|
| N = 7 | 0.4458 | −2.195 → rate 0.786 | rate 0.860 |
| N = 8 | **0.4415** | −2.024 → rate **0.705** | rate 0.890 |

- The leading zero is CONVERGED against the direct estimator (0.443(2)) ✓ — the gate holds.
- **The second Ruelle resonance is REAL NEGATIVE with rate 0.70(8)** (the N-drift is the
  quoted uncertainty) — a period-2-modulated decay channel; spectral gap ≈ 0.26.
- The third is a complex pair near rate 0.89.
- The path to more digits is now mechanical: the same certification at n = 9, 10 (the
  n = 8 Groebner ran inside its cap). Bins: the spectrum values = the campaign's residual
  NEW-MATH-eligible data (lit-gate: Cvitanović-school cycle expansions for Fibonacci
  trace maps — pending); no whitelist form suggests itself at this precision — recorded,
  not scanned (the F1 lesson).
