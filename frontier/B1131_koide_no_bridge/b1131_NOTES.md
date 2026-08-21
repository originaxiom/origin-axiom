# P-KOIDE — NOTES: the verdict and why (sealed probe, executed against PRECOMMIT.md)

## VERDICT: NO-BRIDGE

`det φ = −2/3` (B904) and Koide's `Q = 2/3` are a coincidence. B1129's dismissal
STANDS and is now sharpened: the missing instrument this cell was commissioned
to build (or prove unbuildable) was built — four pre-committed routes, all
failing — and the gap B1129 flagged is now closed by a negative result, not by
an unexamined absence. No cc3 3rd opinion is triggered (that gate is for
BRIDGE-FOUND only).

## det φ's exact meaning (STEP 0 — the headline finding of this probe)

`det φ` is the determinant of an explicit 78×78 rational change-of-basis
matrix between two independently-built concrete bases of the (unique) 78-dim
split E₆ Lie algebra: the octonionic Barton–Sudbery/triality construction
(B904) and "the build" (B854's Chevalley-Serre construction). Re-loading the
banked artifact (`frontier/B904_barton_sudbery/stage4c_phi.pkl`) and
recomputing independently in-sandbox (sympy exact rationals, this probe):

- `det φ = −2/3` confirmed exactly.
- **New structural fact, established here**: φ is EXACTLY block-diagonal.
  Grouping BS-native coordinates into {6 torus, 72 root} and build-native
  coordinates into {6 Cartan (h₁..h₆), 72 root}, the two off-diagonal blocks
  are the zero matrix on every entry (checked exhaustively). The 72×72
  root-space block is a **signed permutation matrix, det = +1 exactly** — it
  contributes nothing. **The entire −2/3 lives in the 6×6 block** mapping the
  object's own geometric torus (4 triality-diagonal directions inside so(8) +
  the 2-dim tri(ℂ′)) to the textbook combinatorial simple-coroot basis
  {h₁,...,h₆}. Its characteristic polynomial (`6x⁶−11x⁵−8x⁴+5x³+10x²−2x−4`) is
  irreducible-looking with irrational roots; its singular values (≈0.50, 0.61,
  0.63, 0.82, 1.09, 3.83) were checked adversarially against cos45°=1/√2≈0.7071
  — nearest is 0.630, gap 0.077, not close.

**Reading:** det φ is provably a fact about **comparing two bases of E₆'s
rank-6 Cartan subalgebra** — a lattice/root-system basis-change determinant.
It contains no 3-dimensional real vector anywhere in its derivation, no inner
product with a democratic direction, no cosine, no angle. The small
denominators (2, 3) are not mysterious: E₆'s own arithmetic is saturated with
exactly these primes (`|Z(E₆_sc)|=3`, Coxeter number `h=12=2²·3`,
`|W(E₆)|=2⁷·3⁴·5`, `dim=78=2·3·13`, `27=3³`). This is the single strongest
piece of evidence in this probe: det φ is categorically the wrong KIND of
object (a 6-dim lattice basis-change scalar) to encode Koide's kind of content
(a 3-dim vector's direction cosine). No amount of further searching inside
det φ's own structure will find an angle, because none exists there — checked,
not assumed.

## The Koide side (STEP 1 — verified, standard)

PDG central values (`m_e=0.51099895000`, `m_μ=105.6583755`, `m_τ=1776.86` MeV,
as already banked in `B703_koide_sigma_distance/koide_q3.py`):
`Q = 0.666660511...` (2/3 to 5 sig figs), `α = 44.9997°` (45° to 4 sig figs),
`cos²α = 0.500004616...` (1/2 to 5 sig figs). The identity `Q = 1/(3cos²α)`
verified to 1e-41 (mpmath, dps=40). **The STRUCTURAL content any bridge must
derive is α=45° (cos²α=1/2) — the geometric fact that the standard-rep
component of the √m vector has EXACTLY the same magnitude as its democratic
component** (derived here: writing `√m_k = M(1+c·cos(θ+2πk/3))`, the
democratic magnitude is always `M`, the orthogonal magnitude is
`cM√(3/2)`, and their equality — the 45° condition — forces `c=√2` exactly,
which is B686's already-banked "parametrization tautology," restated
geometrically). This is the target; the bare number 2/3 is not.

## Why each pre-committed route fails

**(a) The trit (B897/B1030 three 9-blocks, triality-cyclic order 3).** The
only natural 3-vector this structure supplies without any further choice is
the block-dimension vector (9,9,9). Computed: `α=0°` exactly, hence `Q=1/3`
exactly — the **minimum** of Koide's Q (Q ∈ [1/3,1) for positive reals), the
**antipode** of Koide's 45° point on the same circle, not a step toward it. A
bare ℤ/3 permutation symmetry, with no further input, forces the fully
democratic point — this is the generic, structurally-forced consequence of
symmetry alone, and it is the opposite of what a bridge would need. No second
natural 3-vector exists in the banked data: the su(2)′ refinement (3+6 split)
applies to only 2 of the 3 blocks (the third, (3_c,3_f), is single-valued —
not a well-defined third component), and the Casimirs (C_c=C_f=4/9 on color
vs. flavor, C_w=3/8 on the weak-doublet pieces) are cross-SECTOR invariants,
not a 3-tuple indexed by the three generation-blocks. Route (a) has no
candidate that is not either trivially antipodal or simply not a 3-vector.

**(b) det φ = 1/(3cos²α) read backward.** Solving for α given |det φ|=2/3
gives cos²α=1/2 by pure arithmetic — true for *any* quantity equal to 2/3,
with zero dependence on what det φ actually is. Computationally demonstrated
with a reductio: substituting an intentionally unrelated quantity that also
equals 2/3 (e.g. a 3-sided die's `P(roll>1)=2/3`) produces the identical
"α=45°." This is precisely the bare equality the seal disqualifies
(`det φ = 2/3 = Q` — already dismissed by B1129). Confirmed here computationally,
not just asserted: the substitution has no discriminating power at all.

**(c) v0, the sealed rank-3 exceptional-Jordan-algebra element (B663/B670 arc
A1) — the one forced, unfitted rank-3 object on record** (`N(v0,v0,v0)=−6≠0`,
`sharp(v0) ∝ v0`, invertible). Its banked support vector is `(1,−1,1)` at
27-indices `(12,13,14)`. Computed angle to `(1,1,1)`: **70.53°**
(`arccos(1/3)`), `cos²α = 1/9` — not 45°, not close. Flagged before computing
(PRECOMMIT.md): the comparison itself is likely not even principled, since
`(12,13,14)` are raw basis-coordinate slots in the 27's chosen indexing, not a
verified Peirce/eigenvalue decomposition of v0 (that needs v0's trace and
quadratic-invariant functionals — `T2_v0_v0` is explicitly `null` in
`a1_results.json`, i.e. genuinely not computed anywhere in the record). This is
a double failure: not principled, and numerically wrong regardless.
**Named uncomputed datum** (the NEEDS-STRUCTURE-shaped remainder): v0's actual
Peirce eigenvalue triple. It does **not** upgrade the verdict, for a stated
reason: nothing in the record motivates expecting those eigenvalues (once
computed) to sit at 45° rather than anywhere else on the circle — there is no
forcing argument, only an absence of data. Per the sealed default (NO-BRIDGE
unless forced), an unexplored possibility with no positive indication and no
motivating mechanism does not keep the verdict open; it is recorded honestly
as a boundary of this probe, not chased as a fishing expedition (the seal's
own non-fishing commitment, and the repo's standing
`BASE_RATE_PRINCIPLE.md` rule against "any natural algebraic operation"
Koide fishing).

**(c′) φ's own eigen/singular structure.** Folded into STEP 0 above: the only
non-trivial (6×6) block of φ has no eigenvalue or singular value near
cos45°=1/√2. Checked adversarially, closed.

## Coincidence probability (STEP 3.iii)

Among reduced fractions `p/q` with `1≤p<q≤30` (277 total), the `{2,3}`-smooth
ones (both numerator and denominator built only from primes 2 and 3) number 23
— density **8.3%**, i.e. roughly 1-in-12 for a "generic small ratio to be this
kind of clean." 2/3 itself (`p+q=5`, `p·q=6`) is among the smallest-height
fractions possible, tied for 2nd/3rd simplest non-trivial rational after 1/2.
This is not a formal p-value (no pre-registered menu/null model was run in the
style of B615/B655's comparison campaign — that would be a separate, larger
design); it is the illustrative base-rate calibration the seal asked for, and
it is consistent with the repo's own `BASE_RATE_PRINCIPLE.md`. Combined with
the mechanistic point that E₆'s own group theory (order, Coxeter number,
center, dimension) is pervasively 2,3-smooth, **both 2/3's are independently
"cheap" outputs of highly-2,3-smooth constructions (E₆ arithmetic on one side,
3-generation democratic geometry on the other) — no causal link required to
explain either.**

## Gate 5 compliance

Lepton masses entered ONLY in STEP 1 (the Koide-side target: α=45°,
cos²α=1/2). They were never used in, or fed back into, any object-side
construction (det φ / the trit / v0). Verified by inspection of `koide.py`:
the three PDG constants (`ME`, `MMU`, `MTAU`) appear exactly once, confined to
the `step1_koide_classical` block, and are absent from every route (a)/(b)/(c)
computation.

## What this probe adds to the record

1. A precise, independently-verified characterization of det φ (the 6×6
   Cartan-block localization) that was not previously stated at this level of
   detail in B904's own FINDINGS.md — worth a LAW_MAP amendment note if this
   arc is banked, since it sharpens what "det φ = −2/3" actually means for any
   future probe tempted to reuse that number.
2. A closed, four-route, pre-committed negative on the specific det-φ↔Koide
   coincidence, discharging the gap B1129 left open.
3. One named uncomputed datum (v0's Peirce eigenvalues) recorded for the
   record, explicitly not chased, with the reasoning for why not stated.

## Recommendation

Bank as a clean terminal negative (NO-BRIDGE). Suggested one-line LAW_MAP-style
entry if promoted: "det φ (B904, the rank-6 E₆ Cartan-basis-change
determinant) is structurally unrelated to Koide's 45° mass-vector geometry —
four pre-committed bridge routes fail; B1129's dismissal sharpened, the gap
closed (P-KOIDE)." No physics claim, no CLAIMS.md entry (Gate 5 — this is a
negative about a NON-bridge, not a value crossing).
