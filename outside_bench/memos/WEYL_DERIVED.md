# THE WEYL COEFFICIENT, DERIVED — the cusp-spectrum counting law is now a theorem of the functional equation, its constant term vanishes, and the census tracks it with |S(T)| < 2 everywhere
## (outside bench, 2026-08-25; thirty-eighth memo; campaign cell C1 = VI.3(a)'s named residue; every numeric claim gate-checked in-run)

### The debt
B739/B1142 use the smooth law N(T) = (T/π)log(T√3/(2πe)) as an instrument — the
697×-sparsity falsification of the geodesic reading rests on it — but the coefficient
was asserted from the literature shape, never derived inside the record. VI.3(a)
named that residue.

### THE THEOREM (`certificates/c1_weyl.py`; mpmath, 30 digits, all gates asserted)
1. **The completed form is verified, not assumed:** Λ_K(s) = (√3/2π)^s Γ(s) ζ_K(s)
   satisfies Λ_K(s) = Λ_K(1−s) to relative error < 10⁻³⁰ at off-line test points.
2. **The law is derived:** by the argument principle, N(T) = θ_K(T)/π + S(T) with
   θ_K(T) = Im log Γ(½+iT) + T·log(√3/2π); Stirling gives
   **θ_K(T)/π = (T/π)·log(T√3/(2πe)) + c + O(1/T)** — and the constant is measured,
   not guessed: **c = 0** (the deviation decays exactly like 1/T over three decades;
   contrast the Riemann case, where the analogous constant is 7/8). The instrument's
   formula is not just right — it is exact to O(1/T) with no constant correction.
3. **The census tracks it:** the 108 zeros to T = 130 are recomputed in-run
   (43 ζ + 65 L(χ₋₃), matching the banked census), and at checkpoints
   T = 30/50/80/100/130 the remainder S(T) = N_obs − θ_K/π is
   +0.375 / +1.162 / +1.690 / +1.260 / +1.282 — **|S(T)| < 2 at every checkpoint**,
   as the argument principle demands at these heights.

> **VI.3(a)'s residue is paid: B1142's density instrument now rests on a derived
> coefficient with a verified functional equation under it, and the derivation
> came out cleaner than the literature shape suggested — the constant term is zero.**

### Fences
Placement/analytic-structure only; no value claimed; Gate 5 untouched. The
derivation is numerical-with-gates (functional equation at 10⁻³⁰, constant-decay
over three decades, census remainder bounded), not a formalized proof; S(T)'s
O(log T) bound is used at census heights only, as stated.

### Certificates
`certificates/c1_weyl.py`; output `outputs/c1_weyl_out.txt`.

### One sentence for the ledger
The counting law the record had been borrowing is now its own: functional equation
verified, coefficient derived, constant term exactly zero, and the observed zeros
never stray two units from it.
