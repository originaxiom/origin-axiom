# B1490 — PREREGISTRATION: THE COMMON COVER VERIFIED — the LP seat's LP01 built and measured by main's own code, and what it says for the ends fork

cc (main), 2026-10-07. Review 60's R60-3. The owner's new seat LP (hired 2026-10-07 "for fresh approach") sealed and
ran LP01 THE COMMON COVER: the figure-eight group is a congruence subgroup of level 4 in PSL(2, ℤ[ω]), so the class
members with holonomy in PSL(2, ℤ[ω]) have exact common covers with m004 read off a 12-point coset action; for the three
two-cusped members where B1418 found chirality, the door and three together, the covers have degree 24 (m202), 36
(s959), 20 (o10_150726) over m004, each chiral, none with the three. **Sealed before any cover is built or measured
on this bench.** No physical quantity is predicted. 0 of 19.

## 1. What is verified, and how

The seat's data are taken as input: its exact holonomies of the targets in SL(2, ℤ[ω]) (`lp_reps.txt`, from its
`exact/reps.txt`) and its m004 (a = [[ω, 1], [−1−ω, −1]], b = [[1, 2], [−1−ω, −1−2ω]]). Everything else is main's code
(`common_cover_main.py`): the arithmetic in ℤ[ω] and ℤ[ω]/4, the image of the figure-eight group mod 4, the twelve
cosets, the action of π₁(target) on them, the orbit of the coset of K and its stabiliser, the cover built in SnapPy
from the permutation representation, and B1418's measures on it — cusps, H₁, volume, |Sym|, chirality (an
orientation-reversing isometry), and the cusp counts |det(X − I)| over the cusp-fixing orientation-preserving
isometries (the "three" is a value 3).

## 2. Seen first

`VERDICT topic-sweep /common cover|congruence|coset action|covers both/: 21 of 1362 arcs on main match (NEGATIVE 4, PROVED 16, RETRACTED 1)`
— read at the level of the verdict lines: **B731 (RETRACTED, 2026-07-20)** withdrew an earlier "non-congruence"
headline and recorded m004 as congruence *at level 8*, with PSL-index 6 at levels 2 and 4; B1201 (a harvest), B1349,
B1488 and the rest use the words otherwise. B1418 (the three on m202, s959, o10_150726; the covers of m004 inside the
112 do not attain three), B1291 (three excluded on one cusp; the escape is ≥ 2 cusps), B1333 (the index on several
boundary tori) are the F-CI priors. **Literature:** Riley's representation and the index 12 of the figure-eight group
in PSL(2, ℤ[ω]) are classical and are checked here by the volume ratio and the mod-4 count, not assumed.

**Seen before the seal — the controls (`controls.json`, `congruence_level.json`, `level_recount.json`).** The seat's
reps of o10_150726, m202 and s959 have determinant one, send every relator of SnapPy's presentation to ±I, and their
trace squares agree with SnapPy's holonomy; its m004 satisfies aaabABBAb = −I; |PSL(2, ℤ[ω]/4)| = 1920 by closure;
the images of Riley's K and the seat's K mod 4 both have order 160 (index 12) and are conjugate in PSL(2, ℤ[ω]/4).
**And a correction found by the control:** recounted in SL and in PSL, the PSL-index of π₁(m004)'s image is 6 at level
2, **12 at level 4**, 12 at level 8. B731's level-4 index of 6 was wrong; m004 is congruence at level 4, as LP01 says,
not only at level 8. **No cover has been built or measured here.**

## 3. Disclosed

Not blind: main read LP01's FINDINGS (its table of covers and measures) before writing this. The seat's exact
representations are inputs (checked as above); the m004 representation is the seat's, with Riley's as the alternative
(`--riley`). SnapPy's `cover` from a permutation representation is used with the convention tested by the volume ratio
(the cover's volume must be the orbit size times the target's). The cusp-count instrument is rewritten here, not the
seat's and not B1418's file; B1418's definition is used (values of |det(X − I)|).

## 4. Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **C1** | π₁(o10_150726) acting on the 12 cosets of K has an orbit of size 4 through the coset of K; the cover built from it has volume 20·vol(m004) = 4·vol(o10_150726), 6 cusps, H₁ = ℤ/4 ⊕ ℤ⁶ | 85% |
| **C2** | that cover has 16 isometries, is chiral, and its cusp-fixing orientation-preserving isometries have |det(X − I)| ∈ {0, 4} only — no three | 80% |
| **C3** | π₁(m202) has an orbit of size 12; the cover has volume 24·vol(m004), 6 cusps, H₁ = ℤ⁸, 12 isometries, chiral, no three | 75% |
| **C4** | every cusp of both covers is rectangular (2·Re(shape) ≡ 0 mod 2 in a reduced basis): the hexagonal cusps of the targets do not lift | 65% |

**Reading rules.** VERIFIED iff C1 and C2 hold (the sealed cross-check cover of LP01's §4); C3 and C4 are reported as
they come. Any difference from LP01's table is recorded on main and relayed to the seat before anything is built on
either. The correction to B731 lands with this arc as an addendum on B731 and a row in RETRACTIONS, whatever C1–C4 do.

## 5. What this arc will say about the ends (a reading, stated before the run so it cannot be fitted)

In frame F-CI the three is the fixed-point count 3 of an orientation-preserving isometry of order three on a cusp
(B1291: det(A − I) = 3 exactly for the order-3 rotation), which needs a hexagonal cusp lattice; and B1291's parity says
its fixed lines must run between two different cusps. So in F-CI **a generation-count of three is three lines of an
order-3 symmetry running between two hexagonal ends.** If C4 holds, the covers lose the hexagonal cusps and with them
the three — the count does not lift because the symmetry does not. That is the same lesson as THE ENDS (B1487) for the
harmonic frame, in a different frame: the count lives at ends with a structure the generated states do not have.

## 6. Instruments

`verification/common_cover_main.py`, `verification/lp_reps.txt` (the seat's data), `verification/congruence_level.py`,
`verification/level_recount.py` and their outputs; hashes in `ARTIFACT_HASHES.txt`.
