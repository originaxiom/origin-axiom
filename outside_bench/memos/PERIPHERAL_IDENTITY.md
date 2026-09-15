# THE PERIPHERAL IDENTITY AND THE FULL FIXED LOCUS — tr(ab⁻¹) = gal(κ) is the Riley relation in disguise, exact on the parabolic character scheme with defect exactly (tr a)²−4 off it; and the trace map's whole fixed locus is the κ-pair plus one non-reduced, mirror-fixed origin
## (outside bench, 2026-08-26; fifty-fourth memo; closes codex OA-C1083 and completes OA-C1082; executes memo 43's own named follow-up; one extraction error machine-caught in-run and fixed before any claim)

### The two questions
Codex Wave-3 left one new OPEN row on this lane's work and one counterexample:
- **OA-C1083 (OPEN):** is tr(ab⁻¹) = gal(κ) an identity on the character
  component, or only an equality at the selected Riley point? (= memo 43's own
  named one-line follow-up.)
- **OA-C1082 (REFUTED):** memo 43's "the fixed locus is a conjugate pair"
  overclaimed — (0,0,0) is another fixed point. What is the *whole* locus?

### PART I — the identity (`certificates/peripheral_identity.py`, sympy exact)
Component-level, gal(κ) := 3−κ (the involution of κ's quadratic X²−3X+3, root
sum 3), so the question is whether **tr(ab⁻¹) + tr[a,b] = 3** identically.
With x = tr a = tr b, z = tr ab: S(x,z) = tr(ab⁻¹)+κ = 3x²+z²−x²z−z−2.
- **FACT 1.** The nonabelian trace relation of m004 is **derived in-run** from
  the relator: the component factor is extracted as the gcd of all four
  matrix-entry conditions, anchored at s=1 to the banked Riley quadratic
  t²−t+1, and verified by rebuilding representations at sample roots and
  checking the relator vanishes. Converted to trace coordinates:
  **P(x,z) = z² − x²z + 2x² − z − 1.**
- **FACT 2 (anchor).** P(2,z) = z²−5z+7 — the parabolic slice is exactly the
  two Galois-conjugate geometric characters.
- **FACT 3 (the answer).** Dividing: **S − 3 = P + (x² − 4)**, with quotient
  exactly 1. So on the nonabelian component (P = 0):
  **tr(ab⁻¹) + κ = 3 + (tr a − 2)(tr a + 2).**
  The identity tr(ab⁻¹) = gal(κ) holds **precisely where the meridian is
  parabolic**, and there it holds scheme-theoretically (S−3 ≡ 0 in
  ℚ[z]/(z²−5z+7), verified — both geometric characters at once). Off the
  parabolic slice it fails with defect **exactly x²−4**, the parabolicity
  measure. **OA-C1083 closes: a PERIPHERAL identity — it is the Riley
  relation in disguise, and its "3" is the cusp condition, not an accident
  of the point.**

### PART II — the full fixed locus (OA-C1082 completed)
The memo-43 substitution's trace map is computed as the unique polynomials in
(x,y,z) (exact interpolation over the 84-monomial basis from 140 exact SL2(ℚ)
samples, then verified on 40 fresh samples):
x′ = y, y′ = xy³−2xy−y²z+z, z′ = xy⁴−3xy²+x−y³z+2yz.
- **FACT 4.** Gröbner elimination of the fixed-point system on the cusped
  surface x²+y²+z²−xyz = 0 gives elimination polynomial **z²(z²+12)**: the
  full fixed locus is **exactly three points** —
  | point | type |
  |---|---|
  | (2−q, 2−q, 2−4q) = (3/2−√3i/2, ·, −2√3i) | simple; coordinates gal(κ) |
  | (1+q, 1+q, −2+4q) = (3/2+√3i/2, ·, +2√3i) | simple; coordinates κ |
  | (0, 0, 0) — codex's point | **non-reduced (multiplicity 2)** |
  and nothing else. The scheme has length 4 = 1+1+2.
- **FACT 5.** Conjugation (the beat's field action) **swaps the κ-pair and
  fixes the origin**: the mirror-moved part of the fixed locus is exactly
  memo 43's conjugate pair; the remainder is the single mirror-fixed fat
  point.

> **The two ends of the codex exchange, answered with one certificate: the
> identity behind memo 43's coordinates is peripheral — exact on the
> parabolic character scheme, where it IS the Riley relation, with defect
> (tr a)²−4 off it — and the fixed locus memo 43 under-counted is now
> complete: the κ-pair the mirror exchanges, plus one degenerate point the
> mirror cannot move. The mirror's free orbit on the fixed locus is still
> exactly the κ-pair.**

### Error filed (in-run, machine-caught before any claim)
The first extraction of the component factor took a non-common factor of one
matrix entry (the (0,1) entry carries a spurious cofactor t²+t+1 at s=1); the
preregistered verification step (rebuild representations, check the relator)
refused it. Root cause: the component factor must be common to **all four**
entry conditions; fixed by extracting the gcd and anchoring at s=1 to the
banked t²−t+1. The failed candidate never reached a claim — the in-cert gate
did its job.

### What this feeds
- The Riley relation P(2,z) = z²−5z+7 rewrites as κ + tr(ab⁻¹) = 3: the
  parabolic representation condition is itself a trace-3 statement — a fourth
  appearance of the TRACE THREE motif (memo 49), now as the defining equation
  of the geometric characters.
- The origin's non-reducedness (multiplicity 2) and mirror-fixedness are new
  exact facts available to the atlas's fixed-locus row; the level-0 surface's
  singular point is the degenerate fixed point.
- Codex rows OA-C1082/OA-C1083 can move: 1082's counterexample is adopted and
  completed (the locus is exactly 3 points); 1083 closes with the sharp
  peripheral statement.

### Fences
All of Part I is rational polynomial algebra (no algebraic numbers touched:
symmetric functions of the Riley roots are rational). Part II's trace map is
interpolation-plus-verification — exactness rests on the classical fact that
traces are polynomial coordinates on X(F₂) (CITED-standard) plus the 40-sample
exact verification; the Gröbner computation is over ℚ. "The beat's field
action" = complex conjugation on characters, as in memo 43. Gate 5 untouched.

### Certificates
`certificates/peripheral_identity.py` (sympy); output
`outputs/peripheral_identity_out.txt` (vendored copy re-run in-lane,
byte-identical).

### One sentence for the ledger
The equality that labeled the fixed points by κ's conjugates is the cusp
speaking — exact wherever the meridian is parabolic, failing by exactly
(tr a)²−4 elsewhere — and the fixed locus it labels is now complete: two
simple points the mirror exchanges, one fat point it cannot move.
