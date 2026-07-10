# B498 — The Interaction Campaign: mixed words in the monoid (banking-seat verification)

**The exploration-seat handoff (2026-07-10, companion to B497) independently re-derived. C1 exact;
Q1a PROVED by hand; Q1b verified to 26 digits (conjecture); C2 depth-2 exact with TWO corrections to
the handoff; C3 E-data reproduced at 2 seeds. Q2 (depth-3, the decisive monopoly test) running —
verdict appended when it lands. Firewalled; physics reading → speculations only. Nothing to CLAIMS.md.**

## C1 — chirality of mixed words (EXACT; `verify_mixed.py`)
With S(x,y,z)=(y,x,z): **24 of 39** words (length ≤3) are chiral; every F-containing word is chiral
**except exactly MFM**. Mechanism lemma (one line, verified): **M∘S = M** — M is symmetric in its
first two arguments, hence parity-blind; the outer M-sandwich erases the enclosed evolution's
handedness. **Artifact flag honored:** the mirror of an F-word is the word with F→F′=S∘F∘S (the
mirror Fibonacci a→ba, b→a, not in the alphabet); verified exactly — with F′ adjoined the monoid is
mirror-closed. BANKED: the F-chiral/M,D-achiral split + the MFM mechanism. NOT banked: "mixing
creates unpaired chirality" (the artifact).

## Q1a — E_Haar[log mult_D] = −2: **PROVED** (hand proof, banked)
Per factor: E[log(4cos²t)] under the Haar angle density (2/π)sin²t. Proof: log|2cos t| =
Σ_{k≥1}(−1)^{k+1}cos(2kt)/k (classical Fourier series); sin²t=(1−cos2t)/2; the k≥1 terms kill
∫log|2cos t|=0 and the k=1 coefficient gives ∫cos2t·log|2cos t| = +π/2; hence E = (2/π)(0−π/2) = −1.
mult_D = x²y² has two independent factors ⟹ **E[log mult_D] = −2. QED.** (mpmath 15-digit check ✓.)
**Decimation contracts the quantum deviation at the universal rate e⁻² per event — exact.**

## Q1b — E_Haar[log mult_M] = 0: **PROVED** (hand proof, 2026-07-10)
The exact u-reduction (new lemma, verified symbolically): with x=2cos a, y=2cos b, z=2(cos a cos b −
sin a sin b·u), u~U[−1,1]: mult_M = A+Bu with **A+B = 4sin²(a+b), A−B = 4sin²(a−b)** — i.e.
mult_M is the **convex combination 4sin²(a+b)·(1+u)/2 + 4sin²(a−b)·(1−u)/2**. The u-integral is then
exact, and in (σ,δ)=(a+b, a−b) coordinates (log-singularities grid-aligned) high-precision quadrature
gives E[log mult_M] = −4.5×10⁻²⁷ (zero to 26 digits), and the reduction closes into a HAND PROOF:
(3) the Haar weight collapses, sin²a·sin²b/(sin2a·sin2b) = tan(a)tan(b)/4; (4) the Fourier series
g(t) = sin²t·ln(4sin²t) = 1/2 − (3/4)cos2t + Σ_{n≥2} cos(2nt)/(n(n²−1)), and the cosine difference
gives −2Σcₙ sin(2na)sin(2nb); (5) Iₙ = ∫₀^π tan(a)sin(2na)da = π(−1)ⁿ⁺¹ (regular at π/2, recursion
via tan·sin2a = 1−cos2a); (6) E+1 = −2Σcₙ = −2(−(3/4)+1/4) = 1, hence **E[log mult_M] = 0. QED.**
(Every step numerically checked; `q1b_hand_proof_steps` in the reproducer.)
**TM/decoherence is critical — now a THEOREM: log|κ−2| is a driftless multiplicative random walk.**

## C2 — the golden monopoly at depth ≤ 2 (EXACT) + two corrections
All isolated fixed points of all 12 words of length ≤2: **every coordinate in ℚ or ℚ(√5)** ✓. The D
fixed **line** (−1,−1,z) ✓ — transverse to the κ-foliation; trace −1 = the order-3 locus (the ℤ/3
resonance recorded as a HOOK, not promoted). **Corrections to the handoff (both verified):**
1. the quadratic x²+3x−9 (disc 45) lives at **MD**, not DM (composition-order attribution);
2. the κ-level list is incomplete: **DD** fixed points carry κ = **(1±3√5)/8** — in ℚ(√5) but **NOT
   in ℤ[φ]** (quarter-denominators). The handoff's "all levels in ℤ[φ]" is FALSE as stated; the
   correct statement is levels ⊂ ℚ(√5). The FIELD monopoly is unaffected; the RING refinement dies.

## C3 — the drift table (E-data; `c3_orbits.py`, 200×300, seeds {11,42})
Reproduces the handoff's table directionally at both seeds (units: median +0.15/+0.07, **0.000**
classicalized — the control is clean; F80/M20: −2.12/−2.13; F80/D20: −5.26/−4.66 (the strongest);
F80/M10/D10 between). Magnitudes slightly milder than the handoff's 500×400 run — consistent with
the shorter time horizon; ordering identical. BANKED as E-data with protocol+seeds.

## The drift ledger (the campaign's structural yield, tiered)
| verb | drift E[log mult] | status |
|---|---|---|
| evolution (units) | 0 — κ conserved exactly | banked (U-stratum law) |
| decoherence (M) | **0 — critical** (driftless walk) | **PROVED** (2026-07-10) |
| decimation (D) | **−2 exactly** (contracts e⁻² per event) | **PROVED** |
| the classical boundary | both verbs exactly marginal (log-sine) | classical, cite (Lewin) |

Physics reading (classicality = attractor of the measure dynamics, not of any map; decoherence alone
critical/never sufficient; coarse-graining the true classicalizer) → speculations/S063 addendum,
one-way, firewalled.

## Pending
**Q2 depth-3 + period-2 (the decisive monopoly test)** — computing; verdict appended on landing (any
non-ℚ(√5) field refutes; survival names the conjecture). Q3–Q5 queued. Lit-gates (Cantat–Dujardin;
Axel–Peyrière) blocked until the research window (~Jul 14).

## Reproduce
```
python3 verify_mixed.py     # C1 + Q1a + Q1b + C2(depth 2) + corrections
python3 c3_orbits.py        # the drift table (bounded, 2 seeds)
pytest ../../tests/test_b498_mixed.py
```

---

## Q2 verdict (2026-07-10, census in progress) + the abelian/wild dichotomy

**THE GOLDEN MONOPOLY IS REFUTED AT DEPTH 3** — triple-verified (exact solve; symbolic substitution;
**matrix-level**: Fricke lift → the word as a substitution on SL(2,ℂ) matrices → trace residuals 0.0
at 40 digits; inheritance check: fixed by NO shorter word). The newborn fields on the solved census
(13/30 words at this writing; heptagonal reappears across the M-family):
- **ℚ(√3)** (FFD-type words; e.g. (1/2−√3/2, −√3−1, 2+√3/2), convention-proof endo φ(a)=a²b²a², φ(b)=a²b²),
- **ℚ(√−3)** (Eisenstein — the object's own trace field, born at an interaction fixed point),
- **ℚ(ζ₇)⁺** (the heptagonal cubic x³+x²−2x−1, disc 49): fixed points = **the cyclic arrangements of
  (2cos 2π/7, 2cos 4π/7, 2cos 6π/7)** — the full Galois orbit, cyclically permuted.

**The dichotomy test (the follow-up verdict question, run 2026-07-10):** every newborn field so far is
**ABELIAN** (quadratics; the C3 cubic with square discriminant — cyclotomic-contained by
Kronecker–Weber), and torsion-shaped (orders 3, 7, 12). **The cyclotomic-tameness candidate law:** the
interaction algebra births only abelian/torsion arithmetic. If it holds, the grammar can NEVER birth
the object's own non-abelian geometric fields (x³−x−1 disc −23 S₃; x⁴−x−1 disc −283 S₄) — interaction
fixed points and hyperbolic geometry would be arithmetically disjoint. **Named boundary:** the D-heavy
timeout words (FDM/FDD/MFD) have hundreds of numerically-genuine fixed points (analytic-Jacobian
Newton, residual <1e−28) whose minimal polynomials exceed degree-6/height-10⁵ identification — the
abelian-or-wild question THERE needs exact elimination or deep PSLQ (priced). Any non-abelian find
refutes tameness and makes the B398 value-question live.
