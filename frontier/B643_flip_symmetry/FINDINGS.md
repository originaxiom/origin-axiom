# B643 — L93: the flip obstruction (honest negative; the candidate refined)

**Date: 2026-07-16. Prereg 76d64ba0 (sealed first). Gate F1 FIRED.**

The amphichiral flip (a↦a, b↦baB with the certified U_φ companion),
acting per-side with either antilinear J-convention (±), does NOT
preserve the cocycle space of the weld double — the naive flip is not
a symmetry of the coupled local system as posed.

**The diagnosis (registered, unproven):** φ preserves the meridian but
maps the longitude only to a CONJUGATE of λ⁻¹-type words; the weld's
peripheral identification is therefore twisted by the conjugator, and
the flip's action on the double requires composing with the
corresponding INNER automorphism (conjugation by ρ of the conjugating
word) — absent from both tested conventions.

**The refined L93 candidate:** τ* = (the flip) ∘ (the inner correction
by the φ(λ)-conjugator), companion J adjusted accordingly; same gates
F1–F4. Registered as the L93 continuation; the 24ζ₆ row of the LAW MAP
stays **LAW** with the upgrade path updated.

**What this negative teaches:** the chord's symmetry group is smaller
than naively expected — the swap acts (B638), the naive flip does not.
The chord remembers which of its symmetries survive the coupling; that
selectivity is itself structure.

---

## Steps 2–4 (2026-07-16): THE FLIP-BREAKING VERDICT (final)

**Step 1 (`b643_refined.py`):** φ(LONG) = LONG⁻¹ EXACTLY with the EMPTY
conjugator, and φ(μ) = μ — the a-family flip is peripherally clean, and
since it inverts the longitude while the deck swap does too, the
geometrically correct candidate on the double is the SIDE-EXCHANGING
flip Φ = swap ∘ φ (orientation-preserving, LINEAR companion).

**Step 2 (`b643_swapflip.py`):** the derived pullback convention
(W = V⁻¹ per side, V₁ = U₂₇·conj(U_φ), V₂ = U_φ·U₂₇⁻¹) is the only one
of three that acts on rep0 — but NOT on all five modes. The SL(2)
diagnostic identifies why: Q = U_φ⁻¹·u·conj(u_φ)·u = [[1, √−3],[0,1]]
≠ ±I — **no global SL(2) companion exists**; the two per-side
companions differ by a genuine unipotent.

**Step 3 (`b643_companion.py`):** at the 27 level the commutant is
3-dimensional (block scalars on Sym¹⁶⊕Sym⁸⊕Sym⁰), so a corrected
global companion T = V·D could still exist. The exact linear system
(172 nontrivial off-diagonal conditions, 3 unknowns) has solution
space of dimension 1 — and it is SINGULAR: **d = (0, 0, 1)**.

**Step 4 (`b643_bfamily.py`):** the φ(a)=b involution class (B605
family 3; peripheral conjugator w = aBAb found exactly, μ ↦ μ,
λ ↦ λ⁻¹; U_φb normalized into SL(2) by ζ₃⁻¹) gives THE SAME verdict:
solution dimension 1, **d = (0, 0, 1)**, no invertible member.

Inner corrections cannot rescue either class: composing Φ with Ad(w)
multiplies the intertwiner space by ρ(w), which preserves
(non)invertibility — the obstruction covers the full outer classes.

### The theorem-shaped statement

> **The chord breaks both amphichiral flip classes.** For each of the
> two orientation-reversing involution families of the object, the
> side-exchanging flip on the weld double admits exactly ONE partial
> intertwiner of the 27 local system, supported on the Sym⁰ block
> alone — the flip survives only on the invariant line (h⁰), where
> nothing dynamical lives, and is broken on Sym¹⁶ and Sym⁸ (the θ-odd
> exponent modes). The only symmetry of the double's 27-cohomology
> that survives is the deck swap σ* (B638, antilinear).

### What this does to L93 and the 24ζ₆ mechanism

L93 CLOSES as resolved-negative with an exact obstruction witness. The
LAW OF THE CHORD'S CORE (Y[023] = 24ζ₆·Y[123], 9/9) is therefore NOT
forced by a flip symmetry — consistent with B638's honest closure (the
swap law alone leaves a 10-dimensional residual). The magnitude's
mechanism must be non-symmetry (cochain-level structure); the
spontaneous breaking itself is the finding: the object is amphichiral,
its chord is not — **coupling breaks the mirror down to the swap.**

Residual (registered, not run): the two order-4 orientation-reversing
families (φ(a)=A, φ(a)=B; squares = the half-longitude isometry) were
not probed; the same pipeline applies if wanted.

Outputs: `b643_output.txt` (all four steps, appended in run order).
