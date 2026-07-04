# B425 — the GEOMETRIC Reidemeister torsion at ρ_geo (vs B423's dynamical zeta) — PRE-REGISTRATION

**Committed before the exact computation. Provenance: a cross-chat catch (2026-07-04). B423
computed τ_m = det(I − Sym^{2m}(A)) with A = [[2,1],[1,1]] — but that A is the figure-eight's
HOMOLOGICAL MONODROMY (the golden cat map), NOT the hyperbolic holonomy ρ_geo. So B423 computed
the DYNAMICAL zeta (golden by construction: A has eigenvalues φ²,φ⁻²), which is a legitimate
Reidemeister torsion of the mapping torus w.r.t. the homological representation — but it is not
the GEOMETRIC (holonomy) torsion its prereg claimed ("the torsion at the holonomy / at the
parabolic/geometric point"). This bud computes the geometric torsion — the object B423 named
but did not compute — and adjudicates whether the object is "golden through and through" or
carries Eisenstein (√−3) structure on the geometric side.**

## The computation (blind, exact)

The discrete faithful holonomy of 4₁: ρ(a)=[[1,1],[0,1]], ρ(b)=[[1,0],[−u,1]], with ρ(relator)=I
FORCING u²+u+1=0, i.e. u = ω (primitive cube root of unity; trace field ℚ(√−3), the Eisenstein
field). At this ρ_geo, compute the twisted Alexander polynomial (Wada invariant, via Fox
calculus) in Sym^{2m} for the E₆ exponents {1,4,5,7,8,11}, exactly:
- EXACT arithmetic via CRT over primes p ≡ 1 mod 3 (where ω ∈ 𝔽_p); reconstruct over ℚ.
- SANITY: the trivial rep must reproduce the ordinary Alexander polynomial of 4₁ = t²−3t+1.
- Read: (i) are the torsion coefficients rational (does √−3 cancel in the determinant)?
  (ii) the canonical adjoint (m=1) regularized torsion at t=1.
- Cross-check the Fox MATRIX itself (mpmath, 120 digits): does √−3 survive in its trace/
  eigenvalues (is the Eisenstein content present in the rep, even if it cancels in the det)?

## THE REGISTERED READ (two-outcome, before computing)

- **GOLDEN (B423's implicit claim stands):** the geometric torsion is ALSO golden — √5 in its
  coefficients/values, no √−3 content ⇒ the object is golden on both the dynamical and the
  geometric side; B423's label was harmless; the wall holds "golden through and through";
  write the papers as-is.
- **EISENSTEIN (the catch is real):** the geometric torsion is NOT golden — its arithmetic is
  governed by √−3 / rational (Eisenstein), distinct from the dynamical golden zeta ⇒ B423
  conflated two DISTINCT torsions; the object carries BOTH (dynamical-golden + geometric-
  Eisenstein) = the two double-uniqueness cornerstone sides; correct the label; the papers get
  a more precise (and richer) central identity.

## The emergence bar (four-part, campaign-standard — binds this destination too)

If the geometric torsion carries any forced invariant that is (i) forced (ii) unsought (iii) an
EXACT SM structure (gauge-rank / generation count / anomaly lattice) (iv) survives a control —
it clears the bar → escalation. Eisenstein/rational arithmetic (√−3, the Hilbert-class-field
companion of the golden √5) is NAMED MATHEMATICS, not an SM structure → named negative, wall
holds. The registered question for the bar: does the "door on the √−3 side" lead to physics, or
to the object's own second cornerstone face (ℚ(√−3), Reid's arithmetic-knot field)?

## Cross-validation target (must reproduce)

The figure-eight's geometric ADJOINT torsion is already banked: **V30** (normal Reidemeister
torsion at the discrete-faithful κ=−2 root: τ₁ = −3, trace field ℚ(√−3), |τ|=3=|disc|) and
**V31** (structurally identified as Porti's adjoint torsion FORM, Fried–Milnor). This bud's
Fox/Wada adjoint MUST reproduce −3 (a third independent method) or the discrepancy must be
explained before banking.

## Machinery
Exact CRT (𝔽_p, p≡1 mod 3) + rational reconstruction; gcd-reduction of the rational function
mod p before CRT (keeps coefficients small); mpmath 120-digit for the Fox-matrix trace + relator
error. Locks from geometric_torsion.json. Firewall: name the output as math; no physics to CLAIMS.
