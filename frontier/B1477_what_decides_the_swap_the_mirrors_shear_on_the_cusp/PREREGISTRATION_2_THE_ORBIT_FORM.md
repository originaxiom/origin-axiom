# B1477 — SECOND SEAL: the orbit form of the shear law, on a range not yet opened

**Sealed before `orbit_form.py` runs on anything but o10_150729 and the two controls.** cc (main), 2026-10-06, the same
day as the first seal (`673e52be5`, sha256 31acad53), after cell C1 of that seal completed.

## 0. Seen first

- **C1 is complete and P1 FAILED AS SEALED.** 212,641 manifolds; 283 amphichiral (181 one-cusped, 102 multi-cusped). On
  the one-cusped members the sealed law holds on 181 of 181 (75 at ¼, all rhombic; 106 at 0, all rectangular). On the
  multi-cusped it holds on 101 of 102. **The registered kill fired on one manifold: o10_150729** (five cusps, CS ¼), on
  which the reversing isometries disagree — invariant-cusp counts (invariant, rhombic) = (1, 1), (3, 3) **and (0, 0)**.
- **Why, read off that one manifold.** The isometry with no invariant cusp permutes the cusps in a 2-cycle and a
  3-cycle. Its cube is orientation-reversing and preserves the three cusps of the 3-cycle, rhombically. The sealed
  sentence counted only cusps fixed by f itself; it was wrong for an f that moves cusps in an odd cycle. (B1239's swap
  corollary carries the same hidden hypothesis — "fill each swapped pair" — and its bucket A is not contradicted only
  because no manifold of its range has such an isometry with CS ¼; that sentence is owed an addendum.)
- `orbit_form.py` was run on **o10_150729** (orbit parity 1 for all three cycle types (1,1,1,2), (1,4), (2,3); law holds)
  and on **m004, m003** (single orbits; unchanged). On nothing else.
- Of the other 282 amphichiral census members I know their sealed-form counts (C1's output) and not whether any has an
  odd orbit longer than one. Of the fresh range below I have opened only its sizes (77,331 two-cusped, 34,590
  three-cusped, 7,463 four-cusped, 1,101 five-cusped link exteriors) and timed `chern_simons()` on the first forty
  three-component links without reading a value.

## 1. The statement

For an orientation-reversing isometry f of a cusped hyperbolic manifold, and an orbit O of f on the cusps of odd length
ℓ, the power f^ℓ is orientation-reversing and preserves each cusp of O; on H₁ of one of them it acts by the product of
f's cusp maps around the cycle, an involution of determinant −1 — rectangular or rhombic, the same on every cusp of O.
Let n(f) be the number of odd orbits on which it is rhombic. **The orbit form: CS(M) ≡ n(f)/4 (mod ½), for every
reversing f.** Orbits of even length contribute nothing. On a one-cusped manifold it is the sealed law.

## 2. Cells and predictions

- **Q1 — the census again** (`orbit_form.py census`): the 283 amphichiral members of C1. Prediction: the orbit form holds
  on 283 of 283, no MIXED. **Prior 90%.** *Post-hoc for the 282 where the two forms coincide; the content is o10_150729
  and any other member with an odd orbit longer than one.*
- **Q2 — a fresh range** (`orbit_form.py links`): every exterior in SnapPy's `HTLinkExteriors` with two or more cusps
  (links to fourteen crossings; about 120,000), CS prefilter as in C1. Prediction: the orbit form holds on every
  amphichiral one, no MIXED. **Prior 80%.** Not fresh where a link exterior is isometric to a census manifold already
  read; reported.
- The instrument validates its own composition order: the product around an odd cycle must square to the identity as
  an integer matrix; an INVALID is reported, never folded.

**Kill.** One amphichiral manifold in either range with orbit parity ≠ the CS class, or one MIXED, or one INVALID.
**Reading.** Holds on both ranges: the shear law stands in its orbit form as a census law (conjectural beyond), and the
first seal's P1 is recorded as *failed as sealed, by a mis-stated clause, on one manifold*. Fails: the law is dead beyond
one cusp and the page says so; the one-cusped statement (181 of 181) and Theorem A are untouched either way.

## 3. Disclosed

- This statement was written after seeing the first seal's result and because of it. It is not a prediction of the
  first seal and is not graded as one.
- Instrument at this seal (sha256, first 16): `orbit_form.py` 79ca6e98057a287c.
- No cited result is load-bearing (the owner's rule of 2026-10-06). SnapPy's isometry list is taken as complete; its
  cusp-map convention is validated by the involution check rather than assumed.

## 4. Scope

Frame F-CI. Objects: the 283 amphichiral members of the installed cusped census; the multi-component link exteriors of
HTLinkExteriors. Reach: class (a census law). No physical quantity. 0 of 19 before and after.
