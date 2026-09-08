# B1302 — THE SIBLING m202, WHERE THREE APPEARS: its flat E₆ sector is vector-like by the same conjugation (exact), it has no cusp-trivial twist at all, its three lines are PW's localized count under two named choices, and its price is the golden face — the whole case for re-pricing D3, recorded for the owner's decision

*MASTERPLAN v3.1 Phase 1, third harvest arc. DESIGN sealed before evaluation (`DESIGN.sha256`, `811873b0…`). Sources read in
full: sm:B1282 + addendum (@ 87a9004a), fc R72 §4–§6 + R72b/c/d (@ 659487bb), audit R12/R15/R18 (@ 82cd8aaf), main's
B1291/B1292, the chat1 relay §2–§3. Every seat script re-run in its pinned worktree (five receipts); every claim re-derived here
with an EXACT holonomy of m202 in SL(2, ℤ[ω]) and the B1297 engine extended to two cusps. HARVEST_LEDGER rows 21–27. Date 2026-09-08.*

## The sentence

**Three seats converged on m202 without citing each other, and all three are right about their own quantity.** fc: the
order-3 isometry of the sibling fixes three lines, and with equal charges on them the singular-frame count is 3 × (16 ⊕ 10 ⊕ 1)
— verified here as geometry (cusp maps: orders 6, 3, 2 fix (1,1), (3,3), (4,4) points per cusp; chat1's law det(A − I) = 2 − tr A
on every map), fenced as fc fences it (PW's localized count, I-26, two choices). The SM seat: the flat E₆ sector near the geometric
point is vector-like because the inversion acts as θ on the whole 12-dimensional tangent space — verified exactly: h¹(m202; Sym^k)
= 2 for every even k ≤ 22, the inversion the scalar (−1)^{k/2+1} on every slot, the order-3 rotation (ω, ω̄) on k ≡ 2 (mod 6) and
trivial on k ≡ 4; and the golden face is absent (Δ_{m202} has seven ±1 monomials, no specialisation divisible by t² − 3t + 1).
The audit seat: three proper arcs joining the cusps, the parity argument retained (its "net three" is conditional and stays its
own). **New here:** the two cusps' peripheral classes generate H₁ = ℤ², so m202 has NO non-trivial cusp-trivial character — the
descent's twist mechanism (B1297) has no sector on the sibling; its flat sector is untwistable as well as vector-like (T-ONE-CUSP-
INDEX extended to two tori: r₁ = t₀ = 2 on the untwisted Sym², index 0, every identity). **So the sibling passes both of chat1's
tests where the object fails both (order 3 ⇒ three lines; gcd(3, |Out E₆|) = 1 ⇒ inner lift), its flat sector is dead by the
same conjugation as everywhere else, and the 3 lives only in the singular frame at the price of the golden face.** v3 called D3
drift; this arc makes no decision and hands the priced case to the owner.

## 0. Pre-registration and outcome (DESIGN §2)

| prediction | outcome |
|---|---|
| Q1 h¹ = 2; inversion (−1)^{k/2+1}; order-3 (ω,ω̄) / (1,1) | **PASS**, exact (`b1302_signs.py`, holonomy `A = [[−2ζ², −1−ζ²],[ζ², ζ²]]`, `B = [[−ζ², ζ²],[−1+ζ², 0]]`, ζ = ζ₁₂; tr a = tr b = ω̄, tr ab = √−3, both cusps trace +2) |
| Q2 two-cusp index over the cusp-trivial twists: all zero | **PASS, and sharper than predicted**: the peripheral sublattice has index 1 — there are no non-trivial cusp-trivial characters; the one sector (ψ = 1, Sym²) has a = (0,2,2), t = (2,4,2), r₁ = r₁* = 2, I = 0; the k = 0 control r₁ = t₀ = 2 (`b1302_index.py`, `d2multi.py`) |
| Q3 cusp maps (1,3,4) per cusp for orders (6,3,2); the law det(A−I) = 2 − tr A | **PASS** (`b1302_cuspmaps.py`; SnapPy's `isomorphisms_to` returned the 6 cusp-preserving isometries here while `symmetry_group()` reports 12 — the group-side census gives all 12 classes, 6 swapping the cusps) |
| Q4 the golden face absent | **PASS** verbatim (`b1302_faces.py`: 7 monomials, coefficients ±1, 48 primitive classes / 45 monic / 0 divisible, Δ(t,t) = −(2t²+3t+2)) |
| Q5 dispositions | as §4; the D3 case in §3 |

## 1. The exact germ (Q1) and the census
The automorphism census on SnapPy's holonomy (`m202_census.py`): 180 word pairs of length ≤ 5, 12 distinct H₁-actions — the
identity, −I, the swap and its negative, four reflections, two rotations of order 3, two of order 6 (D₆ acting faithfully on
H₁ = ℤ²); fc's R72b and sm:B1282's §1 exactly. The SM seat's own `sibling_germ.py` asserts on this bench at its step (1)
(62/4): a script environment sensitivity, recorded and reported; the claim stands on three benches. The action table (exact):

| k | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| h¹ | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| inversion | −1 | +1 | −1 | +1 | −1 | +1 | −1 | +1 | −1 | +1 | −1 | +1 |
| order-3 rotation | (ω,ω̄) | (ω,ω̄) | (1,1) | (ω,ω̄) | (ω,ω̄) | (1,1) | (ω,ω̄) | (ω,ω̄) | (1,1) | (ω,ω̄) | (ω,ω̄) | (1,1) |

On e₆'s six slots {2, 8, 10, 14, 16, 22} the inversion reads (+,−,+,+,−,+) = θ_D, hence θρ ≅ ι*ρ on the germ (sm:B1282's
linearisation step, adopted as cited) and N(27) = 0 there; h¹(m202; 27) = 6 at the geometric point.

## 2. What is new: no twist can enter (Q2)
Cusp classes in H₁ = ℤ² (a, b basis): cusp 0 (m, l) = ((−2, 3), (1, 2)), cusp 1 ((−1, 3), (−3, 2)); elementary divisors of the
peripheral sublattice (1, 1). Every character of π₁(m202) that is trivial on both peripheral subgroups is trivial. Compare the
object's covers (B1297: 16 and 45 cusp-trivial torsion twists, all inverted by the period-2): on the sibling the question does
not arise. Registered as H-B1302-NOTWIST.

## 3. The D3 case, priced (no decision here)
For: m202 is in the object's commensurability class (B1292); it has the order-3 isometry with three fixed lines that B1291's
parity forbids on one cusp; the lift of an order-3 symmetry is forced inner (gcd(3, 2) = 1), so the outer-lift vector-like
theorem cannot apply; three seats' quantities agree. Against: the 3 is a singular-frame PW count needing two of fc's named
choices (equal signs on the three lines; the manifold within the class — 7 of 72 tetrahedral manifolds to 12 tetrahedra carry a
three-line ℤ/3) and I-26; the flat sector is vector-like and untwistable (§1–§2); the golden face — the E₈/icosian face and its
family triplet (B1270/B1271) — is not carried by the sibling (Q4); "leave the knot, keep the field" keeps ℚ(√−3) and 2T only.
v3 §2 priced D3 as drift ("outside the object"); B1292 said the hatch was mis-scoped (flatness, not parity, is the binding
obstruction — and flatness is cusp-count-independent, so the flat sector's death here is B1292's prediction confirmed).

## 4. Seat credits (the seat speaks first) — HARVEST_LEDGER rows 21–27
sm:B1282 VERIFIED (exact), its script VERIFIED-DIFFERS (environment), its addendum VERIFIED; fc R72 §4–§5 VERIFIED (geometry;
the spectrum recorded as fc records it), R72/R72b/R72d scripts re-run PASS ×3; audit R12 AGREES, R15/R18 REGISTERED as
conditional (to B1304); chat1 §2 CONFIRMATION (the law on every cusp map), §3 REGISTERED (H-CHAT1-THREE).

## 5. Fences
No count of generations is asserted: fc's 3 × (16 ⊕ 10 ⊕ 1) is I-26- and PW-conditional and rests on two named choices. The
inner lift is I-28. The linearisation from tangent to germ is cited (sm:B1280 §3(a)). The sibling's E₆ must come from ℚ(√−3)
and 2T alone (B727's route). Nothing here is a value.

## 6. Reproduction
`verification/`: `m202_setup.py` (facts), `m202_exact.py` (the exact holonomy), `m202_census.py`, `b1302_signs.py` (~10 min,
exact), `d2multi.py` + `b1302_index.py`, `b1302_cuspmaps.py`, `b1302_faces.py`; receipts `sm_b1282_*_rerun.txt`, `fc_r72*_rerun.txt`;
`tests/test_b1302_the_sibling_m202.py` runs the fast scripts in a scratch cwd and pins the signs table from its JSON.
