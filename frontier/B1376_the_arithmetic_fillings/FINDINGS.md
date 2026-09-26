# B1376 — THE ARITHMETIC FILLINGS: the record's clause "none of the 78 closed hyperbolic fillings of m004 is arithmetic" (B288, carried into main's paper) is false and is withdrawn — B288 tested arithmeticity with the imaginary-quadratic criterion, which decides it only for cusped groups; under the cocompact criterion (Maclachlan–Reid 8.3.2) exactly three of the grid's fillings are arithmetic up to orientation, m004(5,1) the Meyerhoff manifold (Chinburg 1987; invariant trace field of discriminant −283), m004(6,1) (−59) and m004(8,1) (−31), six slopes of the 78 with their mirrors — as B718 had computed in July and the record never propagated; re-decided here slope by slope with an instrument of this seat's own (polished holonomy, integer relations, the Hilbert symbol at each real place, no Sage): the exhaustive re-check of the full grid was attempted and abandoned: it reproduced B718's six slopes on the first 46 of 87 cases in minutes, then stalled for over twenty minutes on one non-integral high-degree field (past m004(-8,5)) without a result, a genuine cost of the algdep/lindep route at high degree without Sage's field machinery; the exhaustive claim is B718's own (dual-method: Hilbert symbol and the independent bounded-conjugate cross-check), cited rather than re-derived — **exactly 3 arithmetic fillings up to orientation over the box it scanned (integral p = 5..40, non-integral q = 2..12, p ≤ 25), all three integral, {5,6,8}**, with 14 non-integral one-complex-place negatives and 14 higher-degree cases left unresolved by its own tool ceiling, never folded into a negative. The other half of B288 stands: no filling's field contains ℚ(√−3), and none of the three can, a field with a real place containing no imaginary quadratic subfield — so the E₆-selecting arithmetic remains an open-object property; what changes is the sentence, the lock, and one inference: a closing can be arithmetic without carrying the selecting field

> **Note (2026-09-26, after fetching main @ `987c0c8f`): main made this correction first.** Main's B1419 (2026-09-16, prompted by
> the same question from the owner and, the same hour, by two opponent reviews of the paper) decided the whole |p|, q ≤ 8 grid —
> six arithmetic slopes, (±5,1), (±6,1), (±8,1), discriminants −283, −59, −31 — minted **E82** (the WRONG-DOMAIN CRITERION
> class) and corrected the paper's C46 sentence. This arc is an independent agreement from this branch, which forked on
> 2026-09-06 and did not carry B1419: its three slopes up to orientation are main's six. This branch's E71 is main's E82
> (seat label sm:E71); the paper relay in §3 had already been applied on main (E54 on this seat's side: no sweep of main
> before banking).

**Date:** 2026-09-16 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's question ("none of the 78 fillings is arithmetic is wrong — m004(5,1) is the Meyerhoff manifold, proven arithmetic by Chinburg in 1987") · **Status:** CORRECTION OF RECORD (B288's clause withdrawn; the true count computed) + PROVED (the three arithmetic fillings, verified with own code) · **Price: unchanged** · **Numbering:** B1376.

## 0. Seen from above

The owner is right. The sentence lives in three places: B288's FINDINGS ("0 are arithmetic (none is imaginary-quadratic, degree 2)"),
B288's lock (`N_ARITHMETIC == 0`, "none imaginary-quadratic; arithmeticity lost on closing"), and main's paper (§ the seam: "of the
grid's 78 closed hyperbolic fillings, zero keep ℚ(√−3) and zero are arithmetic"; the chain table's seam row, "settled & lock"). The
criterion B288 used — arithmetic iff the invariant trace field is imaginary quadratic (with integral traces) — is the criterion for a
**non-cocompact** Kleinian group (Maclachlan–Reid 8.2.3): it decides arithmeticity for the cusped object and for nothing closed. A
Dehn filling is closed, and the cocompact criterion (8.3.2) has three conditions: exactly one complex place, integral traces, and the
invariant quaternion algebra ramified at every real place. B718 (2026-07-19, "corrected re-run") applied it under Sage and found in a
box larger than the grid exactly three arithmetic fillings up to orientation, all integral: (5,1), (6,1), (8,1), with invariant trace
fields of discriminants −283, −59, −31 — the first being the Meyerhoff manifold, whose arithmeticity is Chinburg's 1987 theorem. B718's
lock asserts this. B740 (2026-07-21) recomputed B288's other clause on all 78 fillings — no field contains ℚ(√−3) — and its verdict
line says only that; the paper's row re-attached B288's clause. The record thus held two contradictory statements for two months, and
the false one reached the paper.

This arc re-decides the seven controls with an instrument written here, without Sage — SnapPy's polished holonomy at 1 000–4 000 bits,
the invariant trace field k = ℚ(tr²a, tr²b, tr a tr b tr ab) recognised by integer relations (a joint real–imaginary PSLQ), its
signature from the real roots, the integrality of the traces of Γ⁽²⁾ from monic minimal polynomials, and the invariant quaternion
algebra (tr²g − 4, tr[g,h] − 2 / k), g = a², h = b², evaluated at each real place. Controls first: the Weeks manifold m003(−3,1)
arithmetic (disc −23), the Meyerhoff manifold arithmetic (a quartic field of signature (2,1) and discriminant −283, both real places
ramified), m004(6,1) and m004(8,1) arithmetic (cubic fields (1,1), −59 and −31), m004(7,1) not (two complex places), m004(4,3) and
m004(1,2) not (one complex place, the algebra split at a real place) — B718's verdicts, each reproduced. Then the grid: the seven controls (own code, matching B718's slopes and the Weeks manifold exactly); the exhaustive grid claim is B718's own, cited.

What stands: no closed filling's field contains ℚ(√−3) (B288/B740's other clause, and the three arithmetic fields cannot contain it —
a field with a real embedding has no imaginary quadratic subfield, and a cubic field has no quadratic subfield at all). So the
E₆-selecting arithmetic — ℚ(√−3) → 3 → SL(2,𝔽₃) = 2T → E₆ — is still an open-object property, and the seam's fork keeps its shape.
What changes: the sentence "none is arithmetic" is withdrawn wherever it appears; "no closing is arithmetically distinguished" must read
"no closing carries the selecting field"; and the record already contains the arithmetic closing as an object of study — the Child
Program's forced child is the Meyerhoff manifold (B434–B437, B718, B944's row "new arithmetic, disc −283") — so the substance was never
lost, only the clause. Main's paper needs the correction before deposit; the exact replacement is in §3.

## 1. Computed

`verification/arithmetic_fillings.py` (own code; records `arithmetic_fillings_controls_run.txt`, `arithmetic_fillings_grid_run.txt`).

| item | result |
|---|---|
| the criterion implemented | Maclachlan–Reid 8.3.2 (cocompact): k has exactly one complex place; every trace an algebraic integer; A₀ = (tr²g − 4, tr[g,h] − 2 / k) with g = a², h = b² ramified at every real place (σ_v of both entries negative) |
| controls | m003(−3,1) ARITHMETIC (cubic, (1,1), disc −23); m004(5,1) ARITHMETIC (quartic, (2,1), disc −283, ramified at both real places); m004(6,1) ARITHMETIC (cubic, (1,1), −59); m004(8,1) ARITHMETIC (cubic, (1,1), −31); m004(7,1) NON-ARITHMETIC (sextic, (2,2): two complex places); m004(4,3) NON-ARITHMETIC (quintic, (3,1), split at the third real place); m004(1,2) NON-ARITHMETIC (septic, (5,1), split at the fifth real place) — B718's seven verdicts, reproduced |
| the fields, by discriminant | the primitive elements found here generate the same fields as B718's: polynomial discriminants −71²·283, −13²·59, −11²·31 (squarefree parts −283, −59, −31); the Weeks control −23 |
| the grid \|p\| ≤ 8, 1 ≤ q ≤ 8, gcd 1 (87 slopes, 9 exceptional, 78 hyperbolic) | the exhaustive re-check of the full grid was attempted and abandoned: it reproduced B718's six slopes on the first 46 of 87 cases in minutes, then stalled for over twenty minutes on one non-integral high-degree field (past m004(-8,5)) without a result, a genuine cost of the algdep/lindep route at high degree without Sage's field machinery; the exhaustive claim is B718's own (dual-method: Hilbert symbol and the independent bounded-conjugate cross-check), cited rather than re-derived — **exactly 3 arithmetic fillings up to orientation over the box it scanned (integral p = 5..40, non-integral q = 2..12, p ≤ 25), all three integral, {5,6,8}**, with 14 non-integral one-complex-place negatives and 14 higher-degree cases left unresolved by its own tool ceiling, never folded into a negative |

## 2. What it means

1. **B288's clause is withdrawn.** "0 are arithmetic (none is imaginary-quadratic, degree 2)" conflated two statements: none is
   imaginary-quadratic (true, and irrelevant to a closed manifold's arithmeticity) and none is arithmetic (false). The lock encoded the
   conflation; it is repaired here (`N_IMAGINARY_QUADRATIC = 0`, `N_ARITHMETIC_COCOMPACT = 3` with the slopes and discriminants).
2. **The seam's fork keeps its shape.** The load-bearing statement is about ℚ(√−3), and it is proved rather than merely counted for the
   three arithmetic fillings. "The open object carries the arithmetic that selects the exceptional algebra and no closing" remains
   true with "the arithmetic" read, as the paper reads it, as the selecting field.
3. **One inference is corrected.** B288's "no closing is arithmetically distinguished toward E₆" is right; its implicit "no closing is
   arithmetic" is not: the Meyerhoff filling is arithmetic, its field is a quartic of discriminant −283, and B434's "forced child" is
   exactly this manifold. Arithmeticity and the selecting field are different properties; closing loses the second and can keep the
   first.
4. **The error class.** A criterion valid for one class of objects (cusped groups) applied to another (closed fillings) — E71, with the
   standing rule that an arithmeticity test on a closed manifold must run the cocompact criterion and print which of its three
   conditions fails; "imaginary quadratic" is never a test for a closed manifold.
5. **Two-bench state.** B718's Sage computation and this seat's Sage-free instrument agree on every case both decided; the grid's
   tally is the seven controls (own code, matching B718's slopes and the Weeks manifold exactly); the exhaustive grid claim is B718's own, cited.

## 3. For main, before the deposit

The paper (papers/P3_THE_PAPER/main.tex) states the clause twice. Replacement for the seam paragraph: "of the grid's 78 closed
hyperbolic fillings, zero keep ℚ(√−3) (54 in the first census, completed to 78 of 78 on re-computation); three, up to orientation, are
arithmetic with other fields — the Meyerhoff manifold (5,1) [Chinburg 1987], (6,1) and (8,1), of discriminants −283, −59, −31 — and none
of those fields can contain ℚ(√−3)". Replacement for the chain table's seam row: "of the grid's 78 closed hyperbolic fillings none
keeps Q(sqrt-3); three up to orientation are arithmetic with other fields (the Meyerhoff manifold (5,1), (6,1), (8,1)) & settled & lock".
The B288 lock on main needs the same repair as here. Nothing else in the seam's argument moves.

## 4. Caveats

1. The instrument is numerical with exact recognition: integer relations at 1 000–4 000 bits, verified on the real and the imaginary
   parts separately; the field's degree is the degree of the recognised minimal polynomial and could in principle be under-recognised
   if the true degree exceeded the ceiling (then the case is reported UNRESOLVED, never as a negative). The three positives and the
   controls are at low degree and unambiguous; B718's independent Sage run agrees.
2. The primitive element is a small integer combination of the three generators; that each generator lies in ℚ(θ) is verified by an
   integer relation, so the recognised field is the invariant trace field and not a proper subfield.
3. Ramification at a real place is decided by the sign of the two Hilbert-symbol entries under that embedding; a zero entry would be
   reported (none occurred).

## 5. Registered

E71 (ERROR_LEDGER); a RETRACTIONS row for B288's clause; the phrase "none is arithmetic" in RETRACTED_PHRASES; the correction relayed
to main (the letter's thirty-sixth note). Nothing on the destination ledger.

## Verification

`verification/arithmetic_fillings.py controls | grid | p,q` (`grid` reproduces 46 of 87 slopes reliably and then meets a field the
algdep/lindep route cannot resolve in reasonable time without Sage; kept as a script for future use, not under a lock). Lock:
`tests/test_b1376_the_arithmetic_fillings.py` (the seven controls). The repaired B288 lock `tests/test_b288_arithmetic_filling_census.py`.

**Sources.** Maclachlan–Reid, *The Arithmetic of Hyperbolic 3-Manifolds*, Theorems 8.2.3 and 8.3.2 (the two criteria) and 3.6.2 (the
Hilbert symbol); Chinburg, "A small arithmetic hyperbolic three-manifold", Proc. AMS 100 (1987) (the Meyerhoff manifold); this
record's B288, B740 (the ℚ(√−3) census), B718 (the cocompact-criterion census under Sage), B434–B437 (the child).
