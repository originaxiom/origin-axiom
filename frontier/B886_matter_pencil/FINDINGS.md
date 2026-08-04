# B886 — THE MATTER PENCIL: P(x,λ) = F₁¹·F₂⁸ exactly; six Π-weights in two Galois orbits; the B885 laws are now THEOREMS; a second cubic field enters

cc banking seat, 2026-08-04. The masterplan's W1, executed inline-deep. Everything exact —
nothing in this arc floats. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.

## 1. The pencil and its factorization (stage 1, exact over ℚ)

ρ(x₈), ρ(x₁₆) — exact rational 27×27 matrices on the B883 build — **commute exactly**, and the
bivariate charpoly (28-point exact interpolation) factors over ℚ as

**P(x, λ) = det(x·I − ρ(x₈) − λ·ρ(x₁₆)) = F₁(x,λ)¹ · F₂(x,λ)⁸,  both cubic in x.**

So **the 27 carries exactly SIX joint Π-weights in two size-3 Galois orbits**: the F₁-orbit
{w₀,w₁,w₂} (multiplicity 1 each) and the F₂-orbit {u₀,u₁,u₂} (multiplicity 8 each) — 3 + 24 = 27.
At each root of μ the specialization has factor structure **[(1,1), (10,1), (16,1)]** (exact,
over the algebraic field): the branches COLLIDE as 1 = lone w, 10 = w+w+u, 16 = u+u. **The
cubic μ is the matter pencil's branch-collision locus — its third independent appearance.**

## 2. The collision design is S₃-equivariant (stage 2, exact)

| root | 10-collision | lone w (the singlet) | the 16 |
|---|---|---|---|
| r₀ | w₀, w₁ + u₀ | **w₂** | u₁ + u₂ |
| r₁ | w₀, w₂ + u₁ | **w₁** | u₀ + u₂ |
| r₂ | w₁, w₂ + u₂ | **w₀** | u₀ + u₁ |

A Latin-square-like equivariant design: at root i, the participating u is uᵢ and the lone w is
w_{2−i}. All collision identities decided by exact minimal-polynomial zero-tests.

## 3. The two B885 laws — now theorems

For every ordered pair i ≠ j (all six), exactly:
- **LAW 1**: the frame-i singlet weight evaluated at r_j **equals e₁₀(r_j)** — TRUE, 6/6. Each
  frame's vacuum axis is a 10-block direction of every other frame — no longer 10⁻²⁶ numerics.
- **LAW 2**: it **never equals e₁(r_j)** — TRUE, 6/6.
(The one-line LAW 0 from the design note: the singlet is automatically a joint Π-weight vector,
since ρ(x₁₆) preserves the 1-dim ρ(sᵢ)-eigenspace.)

## 4. The new object: a SECOND cubic field

Field identification (sympy `field_isomorphism`, exact): **the mult-8 weight orbit's field is
isomorphic to K = ℚ[ρ]/μ** — the generic matter weights live in the charge field itself. **The
mult-1 orbit's field is NOT isomorphic to K** — the singlet/vacuum weights live in a *different*
cubic field. The object's matter sector carries **two distinct cubic fields**, coupled by the
collision design. The second field's invariants (discriminant, Galois closure's relation to
K's, ramification) are the named follow-up — it is a brand-new arithmetic invariant of the
object, first seen tonight.

## 5. Scope

- Everything here is exact; the laws' earlier numeric form (B885) is superseded in strength.
- The multiplicity-8 uniformity (all 24 generic weights in 8-fold degenerate triples) is the
  pencil-level restatement of the 𝕆⊗ℂ structure — the 8 is the octonion dimension appearing as
  exact weight multiplicity.
- No physics reading; the vacuum-to-Higgs law's fenced framing stays as in B885.

`tests/test_b886_matter_pencil.py`
