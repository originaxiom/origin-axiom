# B425 — the object has TWO torsions: dynamical (golden) + geometric (Eisenstein) = the two cornerstone sides

**Status: banked — an exact result + an honest correction of a merged overclaim. The cross-chat
catch was RIGHT. Firewalled: named mathematics, no physics; the emergence bar is NOT cleared.**

## The catch (verified)

B423 computed τ_m = det(I − Sym^{2m}(A)) with **A = [[2,1],[1,1]]** — the figure-eight's
HOMOLOGICAL MONODROMY (the golden cat map, eigenvalues φ²,φ⁻²). That is the **dynamical zeta /
Milnor–Fried torsion** of the mapping torus w.r.t. the homological representation — **golden BY
CONSTRUCTION** — and it is a legitimate invariant. But B423's prereg called it "the torsion at
the holonomy / at the parabolic/geometric point." **It is not.** The holonomy is ρ_geo, the
discrete faithful SL(2,ℂ) rep, whose entries carry ω (Eisenstein). The geometric torsion is a
DIFFERENT object, computed here for the first time in the E₆ grading.

## The geometric torsion (exact, blind, validated)

At ρ_geo — ρ(a)=[[1,1],[0,1]], ρ(b)=[[1,0],[−u,1]], with **ρ(relator)=I forcing u²+u+1=0**
(so u=ω; trace field ℚ(√−3)) — the twisted Alexander polynomial in Sym^{2m} at the E₆ exponents
{1,4,5,7,8,11}, exact via CRT (p ≡ 1 mod 3), **validated** by the trivial rep reproducing the
ordinary Alexander polynomial of 4₁, t²−3t+1:

| | dynamical zeta (B423, monodromy A) | GEOMETRIC torsion (ρ_geo, holonomy) |
|---|---|---|
| adjoint m=1 | **−5** = disc ℚ(√5) (golden) | **−3** = disc ℚ(√−3) (Eisenstein) |
| field of the invariant | golden, ℚ(√5); Fibonacci apparition primes | **rational** — √−3 CANCELS in every determinant |
| adjoint polynomial | — | (t−1)(t²−5t+1)/t³, roots in ℚ(√21) (3-governed) |
| Sym¹ (holonomy) | — | (t²−4t+1)/t², roots in ℚ(√3) |

**Every geometric twisted-Alexander coefficient is a rational integer** (√−3 cancels in the
determinant) — for all six exponents. The geometric torsion is NOT golden.

## Where √−3 lives, and where it cancels (the seam, made concrete)

The √−3 is genuinely PRESENT in the geometric rep — it does not vanish from the object, only from
the invariant:
- **Fox MATRIX trace** (m=1) = **2 + 3√3·i** — complex; Im(trace) ≠ 0 at ALL six exponents
  (mpmath, 120 digits). The Eisenstein content is in the matrix (its entries, trace, eigenvalues).
- **Fox matrix DETERMINANT** = the torsion = (t−1)⁴(t²−5t+1)/t³ — **rational**; √−3 cancels.

So the geometric side sees √−3 (in the rep) but its canonical invariant (the determinant/torsion)
descends to ℚ with a 3-governed (Eisenstein) signature — while the dynamical side sees √5 (golden).
√5 · √−3 = √−15 = the seam field. The two torsions ARE the two double-uniqueness cornerstone
sides: golden cat map (dynamics → ℚ(√5)) and unique arithmetic knot (holonomy → ℚ(√−3)).

## Cross-validation (three independent methods agree on −3)

The figure-eight geometric ADJOINT torsion = −3 was already banked twice: **V30** (normal
Reidemeister torsion at the discrete-faithful κ=−2 root: τ₁=−3, ℚ(√−3), |τ|=3=|disc|) and **V31**
(identified as Porti's adjoint torsion FORM, Fried–Milnor). This bud's Fox/Wada adjoint at ρ_geo
reproduces **−3** — a third route. B423's −5 was a genuinely different object (the dynamical zeta),
and the −3 geometric value was on record in this repo since June; B423 did not cross-reference it.

## The cross-chat's precision worry, resolved

The reported blow-up (relator error 10⁻¹³ at m=1 → 10²⁹ at m=11) is a **double-precision
artifact**: at 120 digits the relator error is ~10⁻¹¹⁵ at every exponent. The qualitative finding
(Fox eigenvalues complex / Eisenstein present) survives and is confirmed exactly.

## Guard: the raw Fox eigenvalue-product (−25−13ω, "prime 67") is NOT an invariant

A cross-chat follow-up computed the PRODUCT of the two nonzero eigenvalues of the (un-normalized)
Fox matrix Φ(∂r/∂b) at ρ_geo, m=1, and found the Eisenstein integer **−25−13ω** (norm 469 = 7·67),
reading the 67 as a "new prime." **This is a presentation artifact, not a knot invariant** — three
exact controls kill it:
1. **It varies with t.** That eigenvalue-product is e₂(t) = 3t²−15t+5√3·i·t+21−9√3·i−15/t+5√3·i/t+3/t²
   — different at every t (−3+√3·i at t=1; −25−13ω only at one particular irrational t). An invariant
   cannot depend on t.
2. **It is rational for the other Fox derivative.** The same eigenvalue-product for Φ(∂r/∂**a**) is
   purely rational at every t (−3 at t=1, −15/4 at t=2, …) — **no √−3, no 67.** The Eisenstein content
   is an artifact of choosing the b-generator; the a-generator gives ℚ.
3. **The invariant is the NORMALIZED determinant, which is −3.** det(Φ(∂r/∂b))/det(ρ(a)t−I) =
   (t−1)(t²−5t+1)/t³ → −3 (rational, t-independent as a normalized object). The 67 does not appear.

So the √−3 IS in the Fox matrix (its entries/eigenvalues, and the b-derivative eigenvalue-product) —
which is the correct qualitative point — but the specific number −25−13ω and its prime 67 are not
invariants (they fail the ∂r/∂a control and the t-invariance test). The genuine invariant is −3.

## The emergence bar (iii fails) — the door on the √−3 side

(i) forced ✓ (Mostow rigidity: ρ_geo is unique). (ii) unsought ✓ (blind knot theory). (iii) EXACT
SM structure? **NO** — √−3 / rational arithmetic is the Eisenstein field ℚ(√−3), the class-field
companion of the golden √5 (they meet at ℚ(√−15)); it is not a gauge-rank pattern, a generation
count, or an anomaly lattice. (iv) n/a. **Named negative.** The "door on the √−3 side" is real —
the geometric torsion is Eisenstein, not golden — but it opens onto the object's OWN second
cornerstone face (Reid's arithmetic-knot field), not onto physics. **The wall holds.**

## Consequence for the papers (a correction that TIGHTENS the central identity)

B423's identity "E₆ torsion = the cat map's periodic-orbit product 5F₂ⱼ²=#Fix(A²ʲ)" is CORRECT
as stated for the **dynamical zeta** (and only mislabeled). The precise, corrected central
identity of Paper 2 is stronger: **the object carries two Reidemeister-type torsions, one per
cornerstone field — the dynamical zeta (golden, ℚ(√5), periodic orbits of the monodromy) and the
geometric Porti torsion (Eisenstein, ℚ(√−3), the holonomy) — and √5·√−3 = √−15 is the seam where
they meet.** The double uniqueness is no longer just two theorems pointing at two fields; it is two
literally-computed torsions carrying the two discriminants (5 and −3).

**Provenance.** geometric_torsion.py → geometric_torsion.json; lock tests/test_b425_geometric_torsion.py.
Cross-refs V30/V31 (Porti adjoint torsion = −3), B347 (E₆ = ⊕Sym^{2m_i}), B423 (dynamical zeta).
