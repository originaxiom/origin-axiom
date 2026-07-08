# B485 — the metallic A-polynomial family (forcing edges #2/#3, task #201): the Alexander law CLOSED

**Owner directive (2026-07-08): compute the living object to its fullest. Target: the metallic
A-polynomial family + the m=3 genus (two open edges of the K024 forcing map). This session
CLOSES the Alexander (abelian) half exactly and anchors the SL(2,ℂ) genus; the full-m A-poly
elimination runs as the continuing heavy computation.**

## CLOSED — the Alexander family law (exact, verified m = 1…5)
The metallic bundle A_m = R^m L^m (m=1 → 4₁, m=2 → m136, m=3 → s464, m=4/5 built from the word)
has Alexander polynomial
  **Δ_m(a) = a² − (m²+2)·a + 1**
verified in sage/snappy for m = 1,2,3,4,5 (a²−3a+1, a²−6a+1, a²−11a+1, a²−18a+1, a²−27a+1).
This is exactly the CHARACTERISTIC POLYNOMIAL of the monodromy A_m (det(aI − A_m), since
tr A_m = m²+2, det A_m = 1) — as it must be for a fibered 3-manifold (the Alexander polynomial
of a mapping torus is the char poly of the monodromy on H₁ of the fiber). So the abelian/Alexander
half of the metallic A-poly family is a one-line closed form: **the family's Alexander invariant
is its monodromy trace m²+2**, the same m²+2 that runs through the whole program (the metallic
trace, the seam, the breath). Forcing edge #2, Alexander level: CLOSED.

## ANCHORED — the SL(2,ℂ) A-polynomial genus (m=1)
The figure-eight A-polynomial (geometric component) M⁴L² − (M⁸−M⁶−2M⁴−M²+1)L + M⁴ defines a
curve of **geometric genus 3** (sage Curve.genus()); its Newton polygon has 7 interior lattice
points (the genus upper bound; the drop 7→3 is the curve's singularities). This is the m=1 anchor
for the genus-family question ("m=3 genus, genus-2 generality").

## CONTINUING — the full SL(2,ℂ) A-polynomial for m ≥ 2 (the genuinely open edge)
snappy has no direct A-polynomial for m136/s464; the SL(2,ℂ) A-polynomial requires the
character-variety elimination (symbolic SL(2,ℂ) rep of π₁(bundle) + peripheral holonomy +
Groebner elimination of the trace coordinates keeping meridian M and longitude L). This is heavy
(the reason edge #2/#3 is open) and is launched as a background computation; the genus family
(does genus grow with m? is m=3 genus 2, per "genus-2 generality"?) is read off when it lands.
Reproducers: `apoly_sage.py` (Alexander law + genus anchor), `apoly_elim.py` (the elimination).

## Session close — what computed, and the honest boundary (proper-research discipline)
COMPUTED and BANKED this session:
1. **The Alexander family law CLOSED**: Δ_m(a) = a² − (m²+2)a + 1, verified m = 1…5 (sage/snappy).
   = char poly of the monodromy; the family's Alexander invariant is the metallic trace m²+2.
2. **Geometry characterized**: the metallic bundles have RECTANGULAR cusps (purely imaginary
   cusp shape: m=1 → 3.464i = 2√3 i, m=2 → 2.000i, m=3 → 1.662i, m=4 → 1.600i → decreasing).
   A real geometric fact (meridian ⊥ longitude on the cusp torus, consistent with the
   amphichiral symmetry).
3. **Genus anchor**: figure-eight (m=1) SL(2,ℂ) A-polynomial curve has geometric genus 3 (sage).

NAMED COMPUTATIONAL BOUNDARY (the genuinely open part of edges #2/#3):
The full SL(2,ℂ) A-polynomial for m ≥ 2 via direct symbolic elimination is an 11-variable
lex Gröbner (rep params + conjugator + peripheral eigenvalues) that does NOT converge
in-session — this is exactly why the edge is open. **Priced next step** (for the continuing
computation): either (a) resultant-based elimination (eliminate the 4 conjugator params by
resultants, then the 5 rep params — degree-by-degree, avoiding the full lex GB), or
(b) numerical A-polynomial by sampling the character variety at many (M,L) and fitting the
Newton polygon, from which the genus family reads off directly. The genus question
("m=3 genus, genus-2 generality") is then a Newton-polygon computation per m.

**Net**: one of the four open forcing edges had its abelian half CLOSED (the Alexander law)
and its geometry characterized (rectangular cusps, genus-3 anchor); the SL(2,ℂ) genus family
is a well-priced continuing computation, not a mystery. Honest partial close of task #201.
