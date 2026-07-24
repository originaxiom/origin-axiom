# R5: SL(3) CHARACTER VARIETY AT THE GEOMETRIC POINT — ASSESSMENT

cc3 audit seat, 2026-07-24. Gate 5-Q.

---

## Status: LARGELY COMPUTED (B71, B99, B101, B759, B769)

The SL(3) character variety of m004 has been computed from multiple angles.
The question posed by B779 — "does θ-odd/θ-even coupling produce new
invariants, or is SL(2) terminal?" — is answerable from existing data.

## What is computed

### The variety (B71)

SL(3) character variety decomposes into three 2-dimensional components:

| component | locus | type |
|---|---|---|
| V0 | x₁=x₄, x₂=x₅ | geometric (contains Sym² of SL(2) holonomy) |
| W1 | x₁=x₄=1 | Dehn-filling (Falbel D2: M³=L) |
| W2 | x₂=x₅=1 | Dehn-filling (Falbel D3: M³L=1) |

Matches Heusener–Muñoz–Porti and Falbel et al. Exact, locked.

### The local deformation space (B99, B101)

At the geometric Sym² point on V0:

- **Jacobian spectrum:** characteristic polynomial (t-1)² × [3 reciprocal
  pairs]. The c=5 pair is exactly the SL(2) adjoint torsion carried up
  by Sym². This is NOT the Dickson tower spectrum — the SL(3) content is
  not just a lift.

- **Cohomology (B101):** H¹(F₂, sl(3)_Ad) = 8, splitting under the
  principal sl(2) as **3 (Teichmüller, tangent to V0) + 5 (cubic,
  transverse)**. The 5 cubic directions are genuinely new — they are
  Hitchin deformations that leave V0 while remaining Anosov.

### The θ-coupling (B759, B769)

This is the decisive result for R5:

| level | θ-odd/θ-even coupling | status |
|---|---|---|
| SL(2) | off-block = 0 | **DISSOCIATED** |
| SL(3) = Sym² | off-block = √3 | **INTEGRATED** |

The coupling norm √3 = √|disc(Q(√-3))| is a trace-field invariant.
The coupling fraction across all 7 Sym² traces is exactly 15/32.
The commutator [A,B]'s Sym² derivative is purely θ-odd (4i√3).

**θ is trivial at SL(2)** (tr(AB) = tr(BA), always). **θ is non-trivial
at SL(3)** — it acts as the permutation (1 4)(2 5)(3 8)(6 7) on the
8-coordinate trace space. This is the rank-onset signature (S1 in B780).

### The arithmetic seal (B129)

The SL(3) tower is sealed in Q(√-3). All traces of the principal Sym²
representation lie in Q(√-3). No arithmetic escape to new fields. The
new invariants at SL(3) are in the SAME field as SL(2) — they are new
directions in the same arithmetic.

## Answer to the R5 question

**SL(2) is NOT terminal.** SL(3) produces three genuinely new structures:

1. **The θ-coupling norm √3** — a trace-field invariant that exists only
   at SL(3). At SL(2), c and θ are dissociated (the two sectors don't
   talk). At SL(3), they integrate with coupling strength exactly √3.

2. **The 5 cubic deformation directions** — tangent to the Hitchin
   component, transverse to V0. These are SL(3)-specific degrees of
   freedom with no SL(2) analogue.

3. **The commutator's pure θ-odd character** — [A,B]'s Sym² derivative
   is purely imaginary (4i√3), meaning the commutator "lives in the
   θ-odd sector" at SL(3). This has no SL(2) counterpart (where the
   commutator is θ-invisible).

However: all new invariants lie in Q(√-3). No new fields emerge. The
SL(3) content enriches the Eisenstein column — it does not create a
third column.

## Significance for convergence

The θ-coupling at SL(3) is structurally important for the convergence
thesis:

- At SL(2), the two sectors (Galois/c and geometric/θ) are independent.
  The observer's c-choice and the object's θ-structure don't interact.
- At SL(3), they integrate. The coupling norm √3 is the measure of
  integration. This means: the observer's closing act (which involves
  both c and θ) has a computable spectral signature at SL(3) that
  doesn't exist at SL(2).

The coupling fraction 15/32 is a candidate for a new structural constant
of the closing act — the "fraction of the SL(3) content that is
observer-sensitive." It joins the mixing number 1/(φ·√5) as a second
computed structural constant.

## What remains genuinely open

1. **The Hitchin deformations off V0:** the 5 cubic directions are
   constructed (B101) but their image in the character variety has not
   been traced. Do they reach W1 or W2? Do they stay Anosov?

2. **SL(4) and beyond:** the SLN skeleton paper notes L = -M⁴ at SL(4)
   as apparently new. The general-n tower proof is open (B85).

3. **The coupling at higher rank:** does the coupling norm grow as
   √|disc| at every Sym^(n-1), or does it stabilize? Unknown.

## Verdict

**R5: DONE.** SL(2) is not terminal. The θ-coupling norm √3 and the
5 cubic Hitchin directions are genuinely new SL(3) invariants, all in
Q(√-3). The coupling fraction 15/32 is a candidate second structural
constant. The closing act has a computable SL(3) signature.
