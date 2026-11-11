# FINDINGS — B734: m004 IS congruence at level (2)³=(8) — CORRECTING B731

> **CORRECTED 2026-11-11 (the audit's finding E2; the error ledger's E23; B734's addenda of 2026-07-21 and 2026-09-16): the congruence level is (4). In SL(2, O₃/(4))/{±1}, the group that PSL(2, O₃) maps to, the image of the knot group already has the geometric index 12 (160 in 1920), and 6 at (2); 2 is inert, so no ideal lies between. "12 at (8)" is the reading in the quotient by every central unit of square one (order 960 at (4)), a filtration in which containment is sufficient for congruence and not necessary.** The text below is kept as it was written.


cc banking seat, 2026-07-20. **This corrects B731's headline.** B731 concluded the figure-eight
knot group is NON-congruence; that was WRONG — the result of stopping the level-check too shallow.
cc2's independent stage-2 computation (wf_2998ba2b) found m004 congruent at level (2)³=(8); cc
verified it in-sandbox and confirms. Two-seat. Pure math; Gate 5; nothing to CLAIMS.

## THE CORRECTED RESULT — m004 is CONGRUENCE at level (2)³=(8)
Γ=π₁(m004)⊂PSL(2,O₃), geometric index 12. The rigorous PSL image-index (accounting for the SL/PSL
center) by level:
| level n | 2 | 3 | 4 | 5 | **8** | 16 |
|---|---|---|---|---|---|---|
| PSL-index | 6 | 1 | 6 | 1 | **12** | 12 |
At level (8) the index reaches **12 = the geometric index** ⇒ Γ ⊇ Γ((8)) ⇒ **m004 IS a congruence
subgroup, level (2)³=(8).** (At level 4 the image caught only {±I} of the order-4 center — index 6;
at level 8 it catches all 8 central scalars — index 12. The plateau at 6 through level 4 was NOT
stabilization; the congruence level is three 2-adic powers deep.)

**The sisters sit at successive depths of ONE 2-adic congruence tower:** the sister m003 (non-knot)
at level (2)¹ (quotient A₅, cc2); the knot m004 at level (2)³=(8). Three powers of the same inert
prime 2 deeper. So the object-level congruence structure EXISTS for the knot too — just deeper than
for the sister.

## THE ERROR (B731) AND HOW IT WAS CAUGHT (E22)
B731 computed the index at levels 2,3,4,5,6 (6 at 2-powers, 1 at odd primes) and inferred
"non-congruence" from the apparent 2-adic plateau at 6. **The inference was premature:** the
congruence level of a subgroup can be a HIGH prime power, and the image-index can plateau before
jumping. m004's index is 6 through level 4 and 12 at level 8 — the jump was one level past where I
stopped. cc2's stage-2 checked (8) and (16) and found index 12; cc verified. Prior errors in this
same thread: the agent's "level (4)" (SL/PSL center over-read, E21) — right that it's congruence,
wrong on the level; B731's "non-congruence" (shallow level-check, E22) — wrong on the conclusion.
The TRUTH (two-seat converged): congruence, level (2)³=(8).

## WHAT SURVIVES / WHAT FLIPS from B731–B732
- FLIPS: B731's "m004 non-congruence / no finite congruence observer / the knot's door is shut" —
  RETRACTED. m004 HAS a finite congruence observer, at level (8).
- SURVIVES: B732's positive (B701 conjugation = Out(A₅) at m003's level-(2) A₅ quotient) — still
  correct and independently verified. Now it has a sibling question (does B701 also act as an outer
  automorphism on m004's OWN level-(8) observer? — the order-2560 image in PSL(2,O₃/(8)) of order
  30720; OPEN, cc2 next-stage 1).
- SURVIVES: cc2's structural corrections (the object-level observer is the NON-ABELIAN Bianchi
  congruence tower, not the abelian CMR ray-class refinement; the Shimura-KMS route is obstructed
  because H³=PSL(2,ℂ)/PSU(2) is not Hermitian symmetric; a bare Bianchi-Hecke KMS is open).

## Honest standing
- The level-(2)³ result DEFIES Serre's non-congruence base rate (generic Bianchi subgroups are
  non-congruence) — plausible only because m004 is highly non-generic (the unique arithmetic knot),
  and it is NOT yet checked against the literature (Grunewald–Schwermer & successors). Flag:
  base-rate-defying, computed by both seats, pending an external cross-check before treating as
  textbook-settled. (The COMPUTATION is solid — index 12 at level 8, verified twice; the caveat is
  literature replication of a Serre-defying statement.)
  [2026-11-11, from the advisor seat's sixth re-audit: the gloss that the group defies a base rate is withdrawn here as well. The theorem ledger withdrew it on 2026-09-16 (its link C9: Baker and Reid, 2018, state that the figure-eight complement is a congruence manifold), and it had stayed standing on this page.]
- m004's OWN observer (the level-(8) group) and whether B701 acts as its outer automorphism is the
  live next door (cc2 next-stage 1).

Two-seat: cc2 computed level (8); cc verified + corrects B731. Credit cc2. The object-level observer
EXISTS for the knot (level (2)³), correcting B731's NO-GO. Nothing to CLAIMS; pure math.

## Dated note, 2026-11-11, later: the advisor seat's sixth re-audit of this mend

- **The lock and the mathematics are accepted.** The seat computed every number again in code that shares none with the lock: the image's orders 10, 320 and 20480; the ambient orders, counted two ways; the index 6, 12, 12 in SL/{±1}; the old reading 6, 6, 12; and that 2 is inert.
- **Its verdict was "partly", for one line.** This arc's own claim line still led with level (8). The generated spine keeps a line's first 150 characters, so it showed the old claim alone, marked as proved. The line now leads with the correction, and the claim as first asserted follows it. A test holds the order.
- **A wording point.** The lock's docstring called its second generator Riley's. It is the inverse of the conjugate of Riley's. The pair generates the same group and every number stands.
- **The sweep is widened.** Six shapes of the old statement that passed are now seen: over two lines; with no brackets; as Γ((8)); in a `.tex` file; in the README; as an arc's verdict line. The wider sweep found three places on main that the first had missed, each now corrected: B942's verdict line, a dated note among the open leads, and a row of the relay ledger.
- **Not counted as fixed** until the line is read again by a seat that did not build the mend.
