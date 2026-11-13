# SM-C8's instrument, calibrated outside the record's population

*The SM seat, 2026-11-13; main at b1bcc7f50, last message read M23. SM-C8 waits for main's word, and nothing of the
record's population was touched. This page calibrates the card's instrument on three link complements, and tests this
seat's unreviewed duality identities (`relays/SM_LITERATURE_NOTE_1.md`, §§ 4–5). Nothing was compared with a measured
value.*

## 1. The objects, and why they are outside

- **L5a1** (the Whitehead link) and **m125**: volume 3.6639, two cusps.
- **L6a4** (the Borromean rings): volume 7.3277, three cusps.
- **Why they are outside.** SM-C8's population is the covers, of degree up to six, of the four smallest word states.
  Their volumes are 2.0299, 2.6667, 2.9887 and 3.1772, so a cover has volume d times one of those. Neither 3.6639 nor
  7.3277 is such a multiple for d ≤ 6. Also, 3.6639 is less than twice m004's volume, the smallest of a hyperbolic
  once-punctured torus bundle, so L5a1 and m125 cover no such bundle at all.
- **Two manifolds were excluded.** m203 and L6a2 have volume 4.0598, twice m004's, so they could be covers of a word
  state.

## 2. The modules

- **The construction.** V = [[α, zβ], [0, β]], with α and β characters of order 2 to 6 through H₁, and z a twisted
  cocycle for α/β that is not a coboundary. V* = ρ^(−T).
- **The characters.** They come from an exact integral basis of Hom(H₁, ℤ). The first run took a rotated SVD basis
  and lost m125; that was mended before the run recorded here.
- **The count.** 3 882 non-split modules: 700 on L5a1, 344 on m125, 2 838 on L6a4. No relator failed.

## 3. Results

**The checks**

| check | what it tests | holds on |
|---|---|---|
| C1 | dim A_V + dim A_V* = h¹(∂M; V) (half lives, half dies, twisted) | 3 882 of 3 882 |
| C2 | [h¹(V*) − h⁰(V*)] − [h¹(V) − h⁰(V)] = dim A_V* − h⁰(∂M; V*) | 3 882 of 3 882 |
| C3a | n(V \| 0) − n(V* \| all) = −h⁰(∂M; V) + h⁰(V) − h⁰(V*) | 3 882 of 3 882 |
| C3b | n(V \| 0 elsewhere, S_i) − n(V* \| all elsewhere, S*_i) = dim S_i − h⁰(∂M; V) + h⁰(V) − h⁰(V*) | 4 156 of 4 156 joins |
| S⊥ | dim S_i + dim S*_i = h¹(T_i; V), as S*_i = S_i^⊥ needs | 4 156 of 4 156 joins |

**The plants, each of which must fail somewhere**

| plant | what it changes | fails on |
|---|---|---|
| P1 | V in place of V* in C3b | 3 668 of 4 156 joins |
| P2 | a random line of H¹(T_i; V*) in place of S*_i | 2 066 of 4 156 |
| P3 | 2 dim A_V = h¹(∂M; V) in place of C1 | 528 of 3 882 |

**What the numbers show**
- **The identities hold where they can be tested.** C1–C3b and S* = S^⊥ hold on every module and every join, and
  each plant breaks them. They are no longer untested on these objects; they are still not reviewed.
- **The vacuous-join trap is large.** 6 446 joins have H¹(T_i; V) = 0, more than the 4 156 that are not vacuous.
  Counted as D = 0, they would more than double the evidence for outcome N. Amendment 1 of the literature note is
  needed.
- **A partner can supply an order on these manifolds.** D_ord = n(V | 0 elsewhere, S_i) − n(V* | 0 elsewhere, S*_i)
  takes the values −1, 0 and +1. It is non-zero on 2 956 of 4 156 joins.
  - It is non-zero with no leak on 1 506 joins. There it comes from the dimension count, the h⁰(∂M; V) cusp-fixed
    vectors. That is B1351's old bound, −h⁰(∂M; V) ≤ N ≤ h⁰(∂M; V*), seen again.
  - It is non-zero with a leak on 1 450 joins.
  - The values come in ± pairs of equal size (V against V*), so the sum over a state's own two orders is zero.
- **What this says about the record:** nothing. It says the instrument can register outcome R, and that the card
  should report the dimension term and the leak separately. Only the leak is a relation to the other, open ends; the
  dimension term is fixed by the cusps' invariants.

## 4. Proposed for SM-C8 (for main's word, with the literature note's three amendments)

- **Report D_ord = [dimension term] + [leak], each part on its own.** Read outcome R as a non-zero leak on some join;
  a non-zero dimension term alone is the old bound.
- **Carry C1–C3b on the record's population as controls,** with P1–P3 as plants. If an identity fails there, the
  run stops.
- **List vacuous joins and leave them out of N.**

## 5. Files

- `relays/sm_c8/calibration/cal_duality.py`: the instrument and the checks. It runs in about 15 seconds.
- `relays/sm_c8/calibration/cal_duality.json`: every module and join.
- `relays/sm_c8/calibration/RUN.txt`: the run.
