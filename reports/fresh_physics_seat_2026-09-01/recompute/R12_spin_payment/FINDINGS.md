# R12 — B1141 THE SPIN PAYMENT — recomputation (Ring R2, third independent engine)

**VERDICT: MATCH** (every banked number reproduced exactly; plus one new independent leg the
arc did not run — the beat derived from m000's own holonomy — which returns the identical
selection).

## Blind-first discipline record

**Read BEFORE computing:** `frontier/B1141_spin_payment/FINDINGS.md` lines 1-60 only (the claim
statement and banked numbers: A, B, omega, relator `abABaBAbaB`, beat words, census signs,
rank 3 / nullspace 1, W0-closure signs, |lambda|^2 = -1, chi-parity, beat^2 = conj-by-a).
Nothing else of the arc.

**Read AFTER my own code ran and passed:** `frontier/B1141_spin_payment/b1141_results.json`,
`arc_verdict.json`, `verification/verify_spin_payment.py` (Parts 1-5),
`tests/test_b1141_spin_payment.py`, and codex R021's banked leg
(`frontier/B1208_cross_seat_harvest/FINDINGS.md` LEG 7).

## My own computation (files in this dir)

- `blind_recompute.py` / `.out` — exact sympy over Q(omega), all my own linear algebra.
- `snappy_check.py` / `.out` — SnapPy cross-identification (own word-search code).
- `beat_derivation.py` / `.out` — NEW LEG: the beat derived from m000's actual holonomy.
- `derived_beat_exact.py` / `.out` — exact selection re-run with the derived beat.

### Diff against banked numbers — all MATCH

| item | banked | mine (exact) |
|---|---|---|
| relator R(A,B) | +I | +I |
| census R(-A,-B) / R(-A,B) / R(A,-B) | +I / -I / -I | +I / -I / -I (=> exactly two lifts, chi(a)=chi(b)=-1) |
| abelianized relator | H1 = Z | 1*a - 1*b = 0 => Z |
| beat respects relator; beat^2 | yes; conj-by-a | R(beat(a),beat(b)) = +I exactly; beat^2(g) = a g a^-1 on both generators |
| intertwiner system | 8x4, rank 3, nullspace 1 | rank 3, nullspace 1 (exact Gaussian elimination over Q(omega)) |
| W0 | closes all four eqs with sign +, det 1 | W0 = [[1, -omega],[0,1]] (= [[1, 1/2 - sqrt(3)i/2],[0,1]]), det 1; W0 conj(A) W0^-1 = +A, W0 conj(B) W0^-1 = +rho(beat(b)), W0 conj(W0) = **+A** |
| twisted lift | needs \|lambda\|^2 = -1, impossible | same: twisted intertwiner space is the SAME line lambda*W0 (rank 3, nullspace 1, proportional), and (lambda W0)conj(lambda W0) = \|lambda\|^2 A => \|lambda\|^2 = -1 |
| chi beat-invariance | lengths 1 and 5 odd; general parity | confirmed; 50/50 random free words preserve length parity |
| SnapPy m004 | Vol 2.02988..., H1 = Z | 2.0298832128, Z, orientable; my (A,B) identified inside SnapPy's holonomy (word pair ('ab','ba') matches the trace triple (2, 2, 2.5-0.866i) up to PSL sign, and the banked relator holds on that pair) |
| SnapPy m000 | Gieseking side | nonorientable, Vol = Vol(m004)/2 exactly (1.01494...), orientation cover isometric to m004, unique orientable degree-2 cover |

The arc's own verification (read after) sets up the *identical* 8x4 system with the identical
conventions (their (p,q,r,s) = my (w11,w12,w21,w22); their Ab, Bb = my rho(beat(a)),
rho(beat(b))) — no convention mismatch to resolve (E23 check done); this bench is a genuinely
third run of the same mathematical content with independently written code.

### Planted-positive controls (the claim is an exclusion)

1. **Rank falsifiability:** replacing the beat by the identity automorphism gives exact rank 4,
   nullspace 0 — the rank-3/nullspace-1 result could have failed.
2. **Sign falsifiability:** W = [[0,1],[-1,0]] has W conj(W) = -I — a "-" self-consistent square
   is achievable in general, so m004's "+A" is a fact of this manifold, not a tautology of the
   setup. (The sign of W0 conj(W0) is scaling-invariant on the ray: only |lambda|^2 > 0 can
   multiply it.)
3. **Decision symmetry:** my single decision procedure run on both lifts returns
   (+,+) -> EXTENDS (|lambda|^2 = 1) and (-,-) -> KILLED (|lambda|^2 = -1); had the banked claim
   been inverted, the same code would have said so.

### NEW LEG the arc did not run: the beat derived from m000 itself

The arc (and the banked claim) *assumes* the beat words beat(a)=a, beat(b)=b^-1 a b a^-1 b. I
derived the Gieseking gluing independently from SnapPy's m000 holonomy:
pi1(m000) = <a0,b0 | a0 a0 b0 b0 A0 B0>, both generators orientation-reversing (det O31 = -1);
SnapPy's SL2C on an odd word returns the matrix part of the antiholomorphic action (verified:
SL2C(a0 a0) = +-SL2C(a0) conj(SL2C(a0)) to 2.6e-17). The even subgroup <x = a0^2, z = a0 b0>
maps onto m004's group: (x, x z^-1) matches my (A,B) exactly (conjugacy residual 2.5e-15), and
the transported odd element W' = P M_{a0} conj(P)^-1 gives the beat representative
**beat'(a) = a, beat'(b) = b a b^-1**, with sigma'^2 = a and W' conj(W') = +A.

Re-running the full selection **exactly** with beat' (`derived_beat_exact.py`): rank 3,
nullspace 1, W0' = [[1, -conj(omega)],[0,1]], square = +A => untwisted EXTENDS, twisted KILLED
(|lambda|^2 = -1). **Identical verdict — the selection is representative-independent.**

**Honest note (not a discrepancy):** the banked beat and the m000-derived beat differ by
composition with Q = conj(W0^-1 W') = +-[[1, sqrt(3) i],[0,1]], a parabolic translation by
sqrt(3) i. The cusp lattice of Gamma in these coordinates is <1, 2 sqrt(3) i> (verified by
scanning all upper-triangular parabolic words to length 10), so Q is NOT in Gamma: Q is a
*half-longitude cusp symmetry* of m004, i.e. the two beat representatives differ by an outer
symmetry of m004, not merely an inner automorphism. Both extensions are Gieseking gluings
(Mostow + minimal-volume uniqueness) and both select the same lift, so the banked claim's
substance is unaffected; but a maximally pedantic restatement is "a/the Gieseking beat" — the
specific representative in the banked words is the m000 gluing up to a symmetry of m004.
Verdict stays MATCH.

### Cross-check with codex R021 (read after my computation)

R021 (B1208 LEG 7): the restriction of m000's two Pin^- structures to m004 is **constant**
because p*: H^1(N;F2) -> H^1(M;F2) is zero (H1(N) = Z, cover generators land in 2Z). Consistent
with my run: exactly one m004 spin structure is Gieseking-compatible, and both of my
independent beat representatives select the *same* one (the untwisted lift in the (A,B) basis)
— which is exactly the "constant, unnamed image" of R021; B1141/this cell names it. My snappy
leg independently re-verified R021's ingredients: pi1(m000) presentation <a,b|aabbAB>, H1 = Z,
both generators orientation-reversing, orientation cover = m004.

### Vacuity checks

- The census result is *forced* by letter parity (5 a-letters, 5 b-letters in the relator), so
  the census per se could not have come out otherwise **given** R(A,B) = +I — but R(A,B) = +I
  itself is contentful (a PSL relator need only close to +-I), and the rank/sign results are
  contentful (controls 1-2). Not vacuous.

Gate 5: n/a — pure topology/algebra, no measured SM value used anywhere in this cell.
