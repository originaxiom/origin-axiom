# B874 — the measurement ladder: the coordinate census is a two-value cliff, and the full-measurement remnant is an su(3)-TYPE algebra — NOT the SM

cc banking seat, 2026-08-03. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.
**Not preregistered** — exact ℚ-linear algebra on the banked B854 build, closing two questions
B866 carried forward.

## 1. The census — all 15 coordinate subtori of C, exact

| subtorus | Cent dim |
|---|---|
| ⟨x₈⟩, ⟨x₁₆⟩, ⟨x₈,x₁₆⟩ | **30** |
| every subtorus touching x₁₄ or x₂₂ (the other 12) | **12** |

A **two-value cliff**: the (8,16)-plane is the unique *soft* direction (every measurement inside
it resolves to 30 — the plane never resolves further than its own stratum), while **x₁₄ or x₂₂
alone already resolve to the full-measurement floor 12**. The three distinguished lines (46,
B866) live inside the soft plane. The observed centralizer ladder on coordinate data is
**78 → 46 → 30 → 12**, with no intermediate stratum.

**Consequence for step 2**: SU(5)×U(1)-sized centralizers (26) do NOT occur as coordinate-subtorus
centralizers. Whether a line-point + second-charge *joint* measurement produces one (which would
retire the step-2 ranking) remains open — it needs the cubic-field points, not this census.

## 2. Cent(C) — the full-measurement remnant, exactly over ℚ

**dim 12 = derived 8 ⊕ center 4**, brackets verified closed. The center **is C** (one line: C is
abelian and Cent(C) commutes with C by definition, so C ⊆ center; 4 = 4). The derived algebra's
intrinsic Killing form is **nondegenerate (rank 8)** ⟹ semisimple of dim 8 ⟹ **type A₂** —
the unique 8-dimensional semisimple Lie algebra. Signature **(4,4)** pins the real form:
**su(2,1)** (su(3): (0,8); sl(3,ℝ): (5,3); su(2,1): (4,4)).

> **Cent(C) = su(2,1) ⊕ C.** What survives every one of the object's 2T-charges is an
> su(3)-TYPE algebra plus the four measured charges themselves.

## 3. Verdicts

- **The "full measurement = SM" reading is DEAD**: the SM algebra needs derived 11 and center 1;
  the computed remnant has derived 8 and center 4. Stated plainly so it cannot drift into a
  claim.
- **What stands**: the remnant is A₂ — a color-sized algebra surviving total 2T-measurement, in
  the quasi-split real form su(2,1). This is a computed structure, recorded as such; **no
  dictionary to color is asserted** (the compact/quasi-split gap is exactly the layer-8 wall,
  B715/B868).
- The cliff shape — one soft plane carrying all the enhancement structure, every other direction
  maximally resolving — is the object's own; the (8,16)-plane's privileged role now has an
  exact, exhaustive census behind it rather than examples.

## 4. Carried forward

1. The joint measurement at the cubic-field points (line-point + x₁₄/x₂₂): does 26 appear, and
   is it su(5)⊕u(1)² — the step-2 retirement question.
2. The su(2,1) remnant's relation to the layer-8 real-form question — flagged only.

`tests/test_b874_ladder.py`

## Addendum (same day) — the joint measurement from the enhanced point: 46 → 12, and the step-2 question closes NEGATIVELY

`joint_probe.py`, at 40 digits with relative-gap certification, at **all three** enhancement
points s₁ = x₈ + t*·x₁₆ (t* = 13× the banked cubic roots — the normalization fact established
mod p in B872's `cubic_modp_check`, reconfirmed here by **kern(s₁) = 46 at every root**):

| second charge | joint centralizer dim |
|---|---|
| x₁₄ | **12** (all three roots) |
| x₂₂ | **12** (all three roots) |

**No 26 stratum exists — over ℝ** *(scope added 2026-08-18: this is the question the
x₁₄/x₂₂ coordinate tests ask, and for it the negative is exact; over the algebraic closure
the 26 stratum IS attained, at four non-real points carrying the A₄ Levi — see the
2026-08-18 addendum below)*. Adding either hard charge to the tuned measurement collapses straight
to the floor Cent(C). So the carried-forward step-2 question — *"is SU(5)×U(1) the centralizer
of a finer charge?"* — **closes negatively for the object's 2T-charge system**: the complete
centralizer ladder is **{78, 46, 30, 12}**, and the cascade's intermediate SU(5)×U(1) is not a
charge-measurement stratum. Step 2 stands on the fused principle (B861) — the ranking is NOT
retired by charge measurement, and saying so plainly is the point of this addendum.


## AMENDMENT (2026-08-05, B892) — the ladder is incomplete as stated above

The addendum's clause "the torus does not supply the step-2 charge" is **corrected by B892**:
the coordinate tests were right in scope, but the torus's algebraic wall point y* (the solo
seat's Second Measurement Theorem, verified in B892) supplies a step-2 charge landing exactly
on su(3)⊕su(2)⊕u(1)³. The within-C ladder includes {18, 14}. SU(5) remains unreached — the
second measurement skips it. See `frontier/B892_second_measurement/`.

---

## ADDENDUM 2026-08-18 — the 26 stratum over the closure, the reality mechanism, and the no-moduli theorem (audit-seat relay, bench-verified backbone)

The audit seat's relay of 2026-08-15 (which itself corrected and withdrew a stronger
draft — "the banked negative is right about the question it actually asked") sharpens
this arc's negative into a two-field statement:

| field | second-measurement ladder from a wall point x₁ |
|---|---|
| over K̄ | {12, 14, 16, 18, 20, 26} (+ 30, 46 degenerately) |
| over ℝ | **{12, 16, 18}** (+ 30, 46 degenerately) |

- **The negative above stands** for the question its coordinate tests ask (their
  reproduction: 12 at all three roots, exactly as banked). Over K̄ the 26 stratum is
  attained at four points of ℙ(C/⟨x₁⟩), each carrying the A₄ Levi.
- **The mechanism (theirs; reality kills 14, 20, 26).** The 34 active weights from a
  wall point fall into exactly seven proportionality classes, sizes (2,2,6,6,6,6,6);
  three of the seven hyperplane normals are real, the other four form two conjugate
  pairs. A real point on one member of a conjugate pair lies on both — so no real point
  takes exactly one of a pair. The 14-locus is a conjugate pair of size-2 lines; its
  real shadow is the 16-stratum. The same argument removes real 20 and real 26 —
  B892's "no real nullity-14 point" now has a reason rather than a scan.
- **The terminus is not real.** The A₂⊕A₁ point — the su(3)⊕su(2)⊕u(1)³ landing of the
  second measurement (B892's y*) — is not a real point. The Second Measurement Theorem
  lives over K̄; "skips SU(5)" is a statement over ℝ. Scope words added in place here
  and in B892.
- **Bench verification (this seat, exact, independent construction).** The Levi
  backbone recomputed from the E₆ Cartan matrix by reflection closure (72 roots): the
  complete list of Levi centralizer dimensions of E₆ is
  **{6, 8, 10, 12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78}** — 24 is not a Levi
  dimension, 26 is realized by exactly the four A₄ node-subsets, and the relay's
  hand-certificate checks: deleting Bourbaki nodes 2 and 6 leaves 20 roots (the A₄
  chain 1–3–4–5), dim z = 26. So the relay's cleanest fact — "26 is attained" and
  "24 is impossible" are the same fact (every size-6 hyperplane pair carries a third
  hyperplane, avoiding the forbidden 24) — has its classification side verified here.
- **The no-moduli theorem (theirs; consistency-checked here).** C is not a free
  choice: dim C = 4 with dim z(C) = 12 forces |Φ ∩ C^⊥| = 6 with C^⊥ two-dimensional
  (12 = 6 + 6 checks), the only rank-≤2 root system with 6 roots is A₂ (A₁: 2,
  A₁×A₁: 4, A₂: 6, B₂: 8, G₂: 12), and all 40 A₂ subsystems of D₅ form a single
  W(D₅) orbit — **the entire stratification is unique up to conjugacy**. Feeds the
  cost ledger's zero-dials column: the four-charge torus carries no modulus.
- **Provenance.** Audit-seat independence record: four routes with no shared code path
  (certified-gap weight system; direct rank on stacked ad-matrices; pure root-system
  combinatorics from the Cartan matrix, which predicted the 6-triple/3-double incidence
  pattern before seeing charges; fully exact rank over ℚ, K, and degree-6/12 towers with
  no numerics in the certification path — the route that also found the second real
  30-point ⟨x₁, x₂₂ − γ·x₁₄⟩ and the R = (c₆−c₂)·q identity). Their locks live on their
  branch and are NOT imported; nothing merged. This addendum records the corrected
  scope + the bench-verified backbone only.
