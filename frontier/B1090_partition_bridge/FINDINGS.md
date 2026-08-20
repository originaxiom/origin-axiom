# B1090 — THE PARTITION-FUNCTION BRIDGE (C2 of L174): the quantum theory exists, its saddle is ω, and its b=1 value is reproduced here

**Date:** 2026-08-20 · **Verdict: PROVED (typed bridge + two exact identities + a numeric reproduction; every literature item CITED with its equation number)**

## 1. The quantum theory exists with our exact ingredients (CITED, typed)

Andersen–Kashaev's TQFT (arXiv 1109.6295) evaluates the figure-eight complement in
§11.4: at the completely balanced hyperbolic point (a± = b± = c± = 1/6), the
renormalized partition function is

  Z̃_ℏ(X) = e^{−iπ/12}/ν(c_b) · χ_{4₁}(0),  χ_{4₁}(x) = ∫_{ℝ−i0} dy (Φ_b(x−y)/Φ_b(y)) e^{2πix(2y−x)}  (their eq. 38)

— ONE integration variable, a RATIO of two Faddeev quantum dilogarithms: the two ideal
tetrahedra, one positive one negative — **the amphichirality is visible in the
formula's shape**. Equivalently (their §12) χ_{4₁}(0) = g₂(ℏ) with the Gaussian-dressed
Φ_b^{−2} integral; in Garoufalidis–Kashaev's normalization (arXiv 1411.6062, eq. 1)
the same object is 𝓘_{1,2}(b) = ∫_{ℝ+iε} Φ_b(x)² e^{−πix²} dx up to their dictionary.

## 2. THE ω-SADDLE (new observation; exact on this bench)

The steepest-descent potential is v₂(z) = −2Li₂(−e^z) − z²/2 (AK eq. 40–41). The saddle
equation v₂′(z) = 2log(1+e^z) − z = 0 is EXACTLY (1+u)² = u for u = e^z, i.e.

  **u² + u + 1 = 0  —  e^z = ω.**

**The critical point of the object's own quantum-gravity partition function is the
programme's founding field generator.** Verified symbolically; the saddle equation
vanishes to 5×10⁻⁵¹ at z = ±2πi/3.

## 3. The two floors share one number (exact, 50 digits)

At the saddle, v₂(−2πi/3) = **π²/6 − i·Vol** — the exact complex conjugate of B1088's
classical Rogers value 2R(e^{iπ/3}) = π²/6 + i·Vol. The classical action card and the
quantum saddle are the same special value seen from the theory's two sides. And AK's
Theorem 5 part (3) (their §12, proven, CITED) gives lim_{ℏ→0} 2πℏ log|g₂(ℏ)| =
Im v₂(z₂) = −Vol(S³∖4₁): **B1088's action card is the PROVEN classical limit of a
defined quantum partition function.**

## 4. The b=1 value reproduced in-sandbox (DECIDABLE-HERE demonstrated)

GK eq. (2): 𝓘_{1,2}(1) = (e^{iπ/6}/√3)(e^{V/2π} − e^{−V/2π}), V = Vol. This bench
evaluated the state integral DIRECTLY from Faddeev's integral definition (AK eq. 42;
contour Im w = 0.7; outer contour ℝ + 0.25i; convergence per AK eq. 46 asymptotics;
the inversion relation eq. 47 used as the implementation's sanity gate):

  numeric 0.32871516886 + 0.189783865438i vs closed 0.328715166319 + 0.189783789761i
  → **|Δ| = 7.6×10⁻⁸** (fast quadrature; agreement at the quadrature's own precision).

## 5. Ties and residuals (typed)

- **Path A (the metallic WRT tower)**: GK's machinery IS the rational-points/roots-of-
  unity layer of this same function family — the tower and the state integral are one
  object at two parameter faces. (The Andersen–Hansen asymptotics and the quantum-
  modularity layer are in cc3's owner-routed websearch package, lane 4.)
- **L154 (σ ↔ the stage's σ)**: the b-parameter/level question SHARPENED not decided —
  the σ-identification remains L154's own lead; nothing here consumes it.
- **C5**: the arithmetic-CS question inherits the quantum side's shape — GK's cyclic
  quantum dilogarithm at roots of unity is exactly the layer an arithmetic analogue of
  the σ/volume term would live in (their reading note is lane 5 of the package).
- **The Hilbert space on T²**: typed as the standard quantum-Teichmüller/AK module —
  the named remaining assembly for the campaign's quantization side.

**Locks:** tests/test_b1090_partition_bridge.py (the ω-saddle polynomial exactly; the
saddle value π²/6 − i·Vol at 40 digits; the GK closed-form value's self-consistency).
The numeric run's record: `b1090_state_integral.py` (the fast-quadrature version as
executed; the b=1 evaluation is reproducible in ~minutes).
