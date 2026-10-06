# LP01 — THE COMMON COVER: m004 and m202 share a cover of degree 24 (12 over m202). It is chiral, and it has no three. The same holds for s959 (degree 36) and o10_150726 (degree 20). Chirality reaches the tower above the root; the count of three does not.

Seat LP, own numbering, for main to harvest. 2026-10-06. Sealed `PREREGISTRATION.md` (sha256 117ab6e4), committed and
pushed at 3a802c0d2 before any target ran. Frame F-CI, reach the class, no physical claim. 0 of 19.

## The sentence

The figure-eight group is a congruence subgroup of level 4 in PSL(2, ℤ[ω]). So every manifold of its class whose
holonomy sits in PSL(2, ℤ[ω]) has an exact common cover with m004, read off a 12-point coset action. For the three
two-cusped members where B1418 found chirality, the door and the three together, these common covers are:

- **m202:** degree 24 over m004, 12 over m202;
- **s959:** degree 36 over m004, 12 over s959;
- **o10_150726:** degree 20 over m004, 4 over o10_150726.

**Each is chiral, and none has the three.** Every cusp-fixing isometry has |det(X − I)| ∈ {0, 4}, which is m004's own
pattern, not m202's {0, 1, 3, 4}.

## 1. What ran

**The sealed instrument** (`verification/common_cover.py`, 6ec81e44, SnapPy 3.3.2):
- **Controls,** before the seal: m206 was found at degrees (2, 1); m003 at (2, 2), with the common cover m206.
- **m202:** searched through every degree-pair to degree 20 over m004 (1,445 × 514 covers at the last step). **No common
  cover at degree ≤ 20.** The run was stopped by the session's time limit during degree 22 (`common_cover_all.out`). On
  this instrument, s959 and o10_150726 were not reached in that run.
- **o10_150726:** run separately to its bound of 20 as a cross-check of §2 (`common_cover_o10_sealed.out`). Its result
  is in §4.

**The exact instrument** (`verification/exact/`, built after the seal when the brute force proved too slow; disclosed as
a second instrument):

1. **Exact holonomies in SL(2, ℤ[ω]).**
   - SnapPy's holonomy was normalised so that a cusp's meridian is a unit translation, then each entry was recognised
     as x + yω (`exact.py`, `reps.txt`).
   - m004: a = [[ω, 1], [−1−ω, −1]], b = [[1, 2], [−1−ω, −1−2ω]]. The relator aaabABBAb evaluates to −I, which is
     the identity in PSL(2).
   - m202: B1302's representation, with relator aabbAbAABBaB = I. A second normalisation was also found.
   - s959 and o10_150726: also found, with integral entries and determinant 1.
2. **Level 4** (`cong3.py`; `cong3_run.out`).
   - The image of π₁(m004) in PSL(2, ℤ[ω]/4), a group of order 1,920, has index **12**.
   - m004 has index 12 in PSL(2, ℤ[ω]). This follows from the volumes: vol(m004)/12 = 0.16916 = V_tet/6, the
     covolume of the Bianchi group.
   - So Γ₁ = π₁(m004) is the full preimage of its image mod 4.
   - Every other modulus tried (2, 3, 5, 7, 11, 13, 19, 31, 6, 8, 9, 12) gives index 1 for m202. B1302's
     representation of m202 is not detected as congruence at those levels.
3. **The common cover** (`build2.py`; `build2_run.out`, `exact_results.json`).
   - π₁(target) acts on the 12 cosets of Γ₁ by reduction mod 4. The stabiliser of a coset is exactly Γ₁ ∩ π₁(target),
     so each orbit gives a common cover. SnapPy builds it from the permutations.
   - Conjugates by the diagonal units of PGL(2, ℤ[ω]) and by complex conjugation were also run. They give no other
     cover up to isometry signature.

## 2. The covers

| target | degree over target | degree over m004 | cusps | H₁ | volume | |Sym| | chiral | three | cusp det values |
|---|---|---|---|---|---|---|---|---|---|
| m202 | 12 | 24 | 6 | ℤ⁸ | 48.7172 | 12 (ℤ/2 × ℤ/6) | yes | **no** | {0, 4} |
| s959 | 12 | 36 | 6 | ℤ/3 ⊕ ℤ⁶ | 73.0758 | 12 | yes | **no** | {0, 4} |
| o10_150726 | 4 | 20 | 6 | ℤ/4 ⊕ ℤ⁶ | 40.5977 | 16 | yes | **no** | {0, 4} |

- **Targets, measured on the same instrument:** m202 is chiral and has the three, {0, 1, 3, 4}, door 96. m004 is
  amphichiral, with {0, 4} and door 48.
- **The door is not computed on the covers.** π₁ has 7–8 generators there, and the instrument computes it only up to
  four (disclosed in §5 of the preregistration).
- **Cusp shapes of the m202 cover:** 2√3·i (three cusps) and (2/√3)·i (three cusps). All are rectangular; the
  hexagonal shape ω of m202's cusps is gone.

## 3. Against the predictions

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | a common cover of m004 and m202 within degree 24 over m004 | 75% | **PASS**, at exactly 24, found by the exact instrument. The sealed instrument certifies none at ≤ 20; 22 is excluded for every conjugate inside PGL(2, ℤ[ω]) (the action is transitive), not for conjugates outside it. |
| P2 | every minimal common cover is chiral | 40% | **PASS** for the one found (the only one up to PGL(2, ℤ[ω])-conjugation) |
| P3 | some minimal common cover has the three | 45% | **FAIL** |
| P4 | chirality, three and door together on a minimal common cover | 25% | **FAIL** (the three is absent) |
| P5 | the minimal common cover is not a regular cover of m004 | 60% | **PASS**: \|Sym\| = 12 < 24, so no deck group of order 24 |
| P6 | common covers found for s959 (≤ 24) and o10_150726 (≤ 20) | 60% | **split.** o10_150726: degree 20 (see §4 for the sealed instrument's own result). s959: degree **36**, beyond its bound, so P6 as sealed FAILS for s959. |

## 4. The sealed cross-check on o10_150726

*(Filled in from `common_cover_o10_sealed.out` when the run ended; see the line below.)*

## 5. Reading (the sealed rule)

P1 holds and P4 fails. **The three belongs to m202, not to the tower above the root:** "pass to the class" is an
input. One more thing comes out that the rule did not anticipate:

- **Chirality does reach the tower above the root.** The common covers are finite covers of m004 (degrees 20, 24, 36),
  and every one is chiral. So chirality needs no step outside m004's covers; the amphichiral root has chiral covers.
- **The three is what does not survive.** It lives in m202's hexagonal cusps. In every common cover with m004, the
  cusps are rectangular, carrying m004's pattern {0, 4}.
- The gap between the root and the matter content is therefore narrower than "chirality and three". **It is the count of
  three alone.** By L0 it needs at least two cusps, and on the covers built here it is not inherited.
- A common cover is not native reachability (the audit lane's rule, adopted at the seal). The covers here are general
  finite covers of m004, a move GENESIS lists under commensurability, not one it derives.

## 6. What this does not show

- Minimality is not proved over all conjugates in the commensurator. It is shown for degree ≤ 20 (all conjugates, by
  the sealed search) and for degree 22 within PGL(2, ℤ[ω]).
- Larger common covers may carry the three: a rectangular cusp lattice has hexagonal sublattices. Nothing here
  excludes that.
- The door on the covers is not computed.
- Chirality here means no orientation-reversing isometry, and the three is B1418's cusp count. Neither is a fermion
  count.
