# B366 — the invariant spin sector + the S-closure dichotomy (the L57 verdict)

**Status: banked (frontier), COMPLETE in two installments. (1) The gate's skeleton, EXACT (two elementary
lemmas + the identification). (2) The derived level-15 S-transformation (two exact closed formulas, verified
to 7e−12 / 1e−10, no fits): the seam-bearing class is S-closed at fixed modulus; the canonical class exits to
modulus τ/4. The pre-registered naive mixing pattern FAILED and is superseded by the derived dichotomy —
within the stated quantization premise the lift is not a choice. Campaign W2.2. Firewalled; nothing to
`CLAIMS.md`.**

## The two lemmas (exact)

1. **The puncture lemma.** `SL(2,ℤ)` acting on the 2-torsion of the fiber torus fixes **only the origin**;
   the three nonzero half-periods form a single orbit (`SL(2,ℤ/2) ≅ S₃`). The puncture is the unique
   MCG-invariant point.
2. **The spin lemma.** Under the classical action on theta characteristics, the odd `[½,½]` is **fixed by
   both generators**; the three even characteristics form one orbit (`T` swaps `[0,0]↔[0,½]` fixing `[½,0]`;
   `S` swaps `[0,½]↔[½,0]` fixing `[0,0]`).

## The identification and the forcing-shaped corollary

With B364/B365: `T+ = triangular = [½,0]` (its T-multiplier verified in B364 — and indeed `T` fixes `[½,0]` ✓,
an independent consistency hit); `T− = triangular×(−1)ⁿ = [½,½]` (**the odd one**); `S+ = square = [0,0]`;
`S− = [0,½]`. Hence, exactly:

> **The seam-bearing (a=½, triangular/theta-lift) class contains the unique invariant spin sector `[½,½]`;
> the canonical (a=0) class contains none.**

Combined with lemma 1, the gate's argument has its shape: an MCG-equivariant quantization of the *punctured*
fiber (the unique invariant point) that selects a single spin sector can only select the invariant one — which
lives in the seam-bearing class. B365's vanishing signature (one distinguished half-period zero for the
triangular family; the parity-central label `j=8`) is the same structure seen from the divisor side.

## The pre-registered prediction — FAILED, and superseded (the 4th productive failure)

The classical action predicted the S-mixing pattern of the four families: **`T− → T−`, `S+ → S+`, `T+ ↔ S−`.**
Three quick ansatz attempts to verify it failed for three different recorded reasons (a degenerate large-`c`
strip that fit anything; a mis-derived `j`-dependent prefactor; a growth-measurement that conflates prefactor
and theta growth). The derivation-first redo (part 2, below) settles it: **the prediction was wrong** — the
naive characteristic action `[a,b] ↦ [b,a]`-style is *not* how the geometric `S` acts on the level-15
families. Like the arc's three previous failed predictions, the failure bought a sharper statement than the
prediction would have: the forcing comes *directly* from S-closure, with no family-permutation step at all.

## Part 2 — the derived S-transformation: the closure dichotomy (the verdict)

One Jacobi inversion per family (Poisson summation on `n = 15m + j`; every step classical; full derivation in
the module docstring). With `e(x) = e^{2πix}` and `S : (z,τ) ↦ (z/τ, −1/τ)`, **exactly**:

**Triangular (seam-bearing, `a=½`)** — the `j`-dependence in the prefactor cancels identically
(`−4j(j−1) + (2j−1)² = 1`):

> `f_j(z/τ, −1/τ) = (−iτ/15)^{1/2} · e((30z+1)²/120τ) · Σ_r e(−r(2j−1)/30 − r/30) · f_r(z + (τ+1)/30, τ)`

The image is the **same family, same modulus**, at the finitely-translated argument `z + (τ+1)/30` — a
30-torsion Heisenberg translation — with a `ζ₃₀` kernel. **The class is S-closed at fixed τ.** (The raw
Poisson output is sign-twisted at `z + τ/30`; the twist collapses via the exact elementary identity
`f̃_r(w) = e(−r/30)·f_r(w + 1/30)` — the "sign twist" is a real `1/30` shift.)

**Square (canonical, `a=0`)** — prefactor `j`-dependence also cancels:

> `g_j(z/τ, −1/τ) = (−iτ/30)^{1/2} · e(15z²/4τ) · Σ_r ζ₁₅^{−rj} · g_r(z/2, τ/4)`

The image lives at **modulus τ/4 with argument z/2** — a rescaling, *not* a Heisenberg operation. **The class
exits the fixed-τ level-15 space entirely** (B365's metaplectic doubling, now seen from the S side).

Verification (no fits, no free parameters; `s_transformation.py`): triangular worst relative deviation
**7.1e−12** (4 residues × 3 arguments), square **1.2e−10**, the twist-shift identity **1.1e−15**, half-`K`
stability 5e−13. The metaplectic eighth-root is fixed by the principal square-root branch at the test modulus
(verified numerically, not re-derived globally — a convention, not a claim).

**Two exact remarks (convention bridges).** (i) *Normalization:* the triangular family is literally the
half-characteristic quadratic form — exactly `f_j(z,τ) = e(−τ/120 + z/2) · Σ_{n′ ≡ j−½ (15)} e(n′²τ/30 + n′z)`
(from `n(n−1) = (n−½)² − ¼`; verified 1.2e−15). An implementation built directly on the `(n′)²/30`
normalization must carry the `e(−τ/120 + z/2)` bridge factor (and the coupling `e(n′z)`, not `e(2n′z)`), or
the S-identity fails at O(1) — a conventions trap, not a mathematics gap. (ii) *Kernel ↔ finite-Weil:* the
geometric kernel factors exactly as `e(−r(2j−1)/30) = ζ₁₅^{−rj} · ζ₃₀^{r}` (the integer identity
`−r(2j−1) = −2rj + r`): the finite Weil S-kernel composed with a metaplectic half-shift diagonal — the
explicit form of how the finite representation layer (B355/B358) sits inside the geometric transformation,
and a named hook for identifying the `ζ₃₀`-diagonal with the Heisenberg-lift half-shift (`X¹Z²`) already on
the ledger.

## What the dichotomy forces (the gate's verdict, with its named premise)

**Premise (named, standing):** pair states are level-15 theta functions on the fiber torus, carrying the
standard Heisenberg/metaplectic action — the modeling premise the whole seam arc computes in.

Within that premise: a modular-invariant quantization needs an `S`-action **on the state space at the given
modulus**. The derived dichotomy says the seam-bearing class *has* one (closure up to a finite Heisenberg
translation, which is internal structure) and the canonical class **does not** — its geometric `S` leaves the
space. The canonical Weil representation of `SL(2,ℤ/15)` (B355, exact) still exists as a finite-dimensional
representation; the dichotomy shows it is **not realized by the geometric theta transformation at level 15**.
Combined with part 1 (the unique invariant spin sector lives in the seam-bearing class; the canonical class
contains none), the two independent selectors agree:

> **Within the stated premise, the theta lift is forced — not a choice. The seam form `s(m₁,m₂)` is an
> invariant of the geometrically-quantized pair at this tier.**

The arc's probation condition is discharged in the forced direction *at the geometric tier*; the premise
itself remains a named modeling assumption, and nothing here promotes. Scope honestly stated: what is proved
is a dichotomy between the two polarization conventions at level 15, plus the spin-sector lemmas — a
specialist would phrase it as "the half-characteristic polarization is the unique level-15 `S`-closed one."

**Provenance.** B364 (the two polarizations), B365 (the vanishing signature; the doubling), the seam arc
B358–B363 (what this forces). Reproducers: `invariant_spin.py` (part 1, exact), `s_transformation.py`
(part 2, derived formulas + verification); tests: `tests/test_b366_invariant_spin_sector.py` (3, exact),
`tests/test_b366_s_transformation.py` (3, numeric locks).
