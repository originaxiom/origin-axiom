# B1419 — THE ARITHMETIC FILLINGS, CORRECTED: six of the 78 closed hyperbolic fillings of m004 in the |p|,q ≤ 8 grid are arithmetic (the Meyerhoff manifold among them); B288's "zero" applied the cusped criterion to closed manifolds

cc, 2026-09-16. Prompted by the owner ("m004(5,1) is the Meyerhoff manifold, proven arithmetic by Chinburg in 1987, no?") and,
the same hour, by two independent opponent reviews of the paper that found the same row. **Verdict: B288/B740's "0 are
arithmetic" is REFUTED; "0 keep ℚ(√−3)" STANDS.** Error class E82 minted. Pure math; the paper's C46 sentence corrected.

## What was wrong
`B288/arithmetic_census.py` line 60 counts `n_arith = #{fields of degree 2}` and its FINDINGS says "0 are arithmetic
(none is imaginary-quadratic, degree 2)". An imaginary quadratic invariant trace field is the criterion for a **non-cocompact**
arithmetic Kleinian group. For a **closed** hyperbolic 3-manifold H³/Γ the criterion (Maclachlan–Reid, Thm 8.3.2) is:
(1) the invariant trace field k has exactly one complex place; (2) all traces are algebraic integers; (3) the invariant
quaternion algebra A = ((tr²g − 4, tr[g,h] − 2)/k), ⟨g,h⟩ ⊂ Γ⁽²⁾ irreducible, is ramified at every real place of k
(both Hilbert-symbol entries negative there). A closed manifold's invariant trace field is never imaginary quadratic with
integral traces (that would make Γ commensurable with a Bianchi group, hence non-cocompact), so the old test could only
ever return "0" on a closed census: **a criterion that cannot fail on its domain** (the MB12 vacuity rule, violated).

## The corrected census (`verification/arithmetic_census_closed.py`, sage-python; `.jsonl` one row per slope)
Grid |p| ≤ 8, 1 ≤ q ≤ 8, gcd = 1: 87 slopes, 9 exceptional, **78 closed hyperbolic** (as B740). For each: invariant trace
field by SnapPy/Sage `find_field` (degree ≤ 24 at ≤ 800 bits; two slopes needed 1 200 bits, `stragglers_recheck.py`; the
seven deepest at degree ≤ 32 / 2 000 bits, `deep_stragglers.py`, with the mirror isometry m004(p,q) ≅ m004(−p,q) —
B740's shortcut, re-verified here by `is_isometric_to` for all ten pairs used — carrying the field to the mirror slope);
signature; trace-field integrality; the Hilbert symbol at each real place from the 1 000-bit polished holonomy, its entries
recognised in k by PSLQ against the field's complex root and checked to 10⁻¹⁵⁰.

| slope | inv. trace field | disc | signature | traces integral | ramified at real places | **arithmetic** |
|---|---|---|---|---|---|---|
| (±5,1) — the Meyerhoff manifold, vol 0.98137, H₁ = ℤ/5 | x⁴ − x − 1 | −283 | (2,1) | yes | yes, yes | **YES** (Chinburg 1987, reproduced) |
| (±6,1) | x³ + 2x − 1 | −59 | (1,1) | yes | yes | **YES** |
| (±8,1) | x³ + x − 1 | −31 | (1,1) | yes | yes | **YES** |
| 14 slopes: (±8,3), (±7,2), (±5,2), (±4,3), (±3,2), (±2,3), (±1,2) | degrees 5–7, one complex place | | (n−2,1) | yes | **no** at a real place | no |
| 52 slopes | degrees 6–31 | | ≥ 2 complex places | | | no |
| 6 arithmetic · 72 not · 0 undetermined | | | | | | |

The Hilbert symbols for the six: (5,1): a = −15z³−7z²+20z+12, b = 4z³−9z²+6 in ℚ[z]/(z⁴−z−1) (σ(a),σ(b)) = (−0.46,−0.25),
(−1.30,−0.14) at the two real places; (−5,1): a = 3z³−3z²−z−2, b = 2z³−4z²+z+1, (−3.99,−2.59), (−2.23,−0.10). The cubic
cases have one real place each; entries in the `.jsonl`.

## What it changes, and what it does not
- **The paper (C46's sentence)**: "zero keep ℚ(√−3) and zero are arithmetic" → "zero keep ℚ(√−3) and six are arithmetic
  (Meyerhoff among them), the other seventy-two are not". The **conclusion drawn from it survives in corrected form**: no
  closing re-sees the object's own arithmetic; the arithmetic a closing carries (disc −283, −59, −31) is a different
  arithmetic, and it selects no exceptional algebra by the McKay door (none of the three fields is imaginary quadratic,
  so none reaches SL(2,𝔽₃) as the object does). "The two cannot be held at once" stands as *the object's arithmetic and a
  closing cannot be held at once*; the slogan "a closed object carries no arithmetic" is withdrawn.
- **B434 already knew**: B434 (2026-07) banked "the Meyerhoff manifold — new arithmetic (disc −283), not golden". The repo
  held B288's "zero arithmetic" and B434's "Meyerhoff is arithmetic" side by side for two months; nobody joined them.
  That is a second instance of the E54 absence-rule failure (a sweep would have found B434) on top of the E82 criterion error.
- **B747 (0/78 invariant trace fields contain √5)** is a different claim and is untouched.
- **Literature** (cited, not read in full): Chinburg, *A small arithmetic hyperbolic three-manifold*, Proc. AMS 100 (1987)
  140–144, proves m004(5,1) arithmetic with this field. Whether (±6,1) and (±8,1) appear in the literature as arithmetic
  fillings of the figure-eight is not checked here; the computation stands on its own criterion and is re-runnable.

## Locks
`tests/test_b1419_arithmetic_fillings.py`: the census file has 78 hyperbolic rows and 87 slopes; exactly the six slopes above
are arithmetic; every row is decided; the Meyerhoff field, discriminant and signature; live SnapPy checks of the volume,
H₁ and the ten mirror isometries. Related: B288 (addendum), B740 (addendum), B434, E82.

## Two more computations made on the same pass (the paper's hostile-review items, S12)
- `verification/congruence_levels.py` (+ `.out.txt`): in Riley's representation the image of π₁(m004) in PSL(2,O/I) :=
  SL(2,O/I)/{±1} has index 1 at (√−3) and (3), 6 at (2), **12 at (4)** and at (8) ⇒ the group contains Γ((4)); its level is
  (4) (B734 addendum; B734's (8) is a deeper level where containment also holds). Γ(√−3), of the same index 12, has four
  cusps, so m004 is not a principal congruence manifold. Baker–Reid (2018) state the figure-eight complement is congruence.
- `verification/quotients_gap.out.txt`: GAP `GQuotients` on SnapPy's presentation — surjections up to Aut: 2T: **2**,
  2O: **0**, 2I: **0** (A₄ 1, S₄ 0, A₅ 0, PSL(2,7) 4, SL(2,7) 8). The paper's "short catalogue" paragraph now rests on this
  quotient count, not on the subgroup-of-SL(2,K) trace remark. Also recorded there: the B1170 content-census ablation
  (no content isolated by the linear conditions alone; the cubic makes the five linear survivors rigid).
