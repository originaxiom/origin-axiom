# B1514 — THE DECOUPLING LAW: through level 6, no chiral state of the harmonic tower couples to a Higgs class of its background. The opposite-sign 10̄′ lives in the sub-bundle, and all its couplings pass through a twisted Higgs bulk that has no cohomology.

**Date:** 2026-10-02 · **Seat:** cc (the SM-derivation branch) · **Verdict:** PROVED.
**Sealed** at a0badfa3 (PREREGISTRATION.md, sha256 `12aa1edd7819cf9d7848d2b34e55420d631e11825c890cbf626848651e08c014`), before any
Higgs class, coupling or joining form at a case-(b) member was computed.
**Run as sealed by two independent routes that share no code** (the owner's rule NO NEGATIVE FROM A BUG). They agree group by group
on every dimension, every zero and every non-zero:
- route T, `verification/census.py --record`: 2 479 s, 1 120 readings, nine primes;
- route L, `verification/independent_route.py --record`: 2 196 s, 1 672 readings, nineteen other primes *[the readings' primes; recounted 2026-10-02 from `verification/independent_route_run.txt`, where each Part A block names its prime in the field `arithmetic` ("GF(p), q = r"): 19 distinct, none of route T's 9 (`census_run.txt`, the same field); Part 0 adds 7 more and Part B none. Main's B1453 reader counted the `p` fields, which hold Parts 0 and B, 13. B1514's lock has counted the nineteen since the bank: `tests/test_b1514_the_decoupling_law.py`, test_the_routes_agree_on_disjoint_primes]*.

**Price:** unchanged, 0 of 19.

## 0. Seen from above

**The question** (B1513 leads 1 and 2). B1513 found that the projective triplet's chiral 10′ does not couple to its own Higgs class.
Is "a chiral state does not couple to a Higgs class of its background" a law of B1509's harmonic frame? The tower has a second
chiral mechanism, B1511's case (b): one 10̄′ per member, in orbits of four on M₄, five on M₅ and six on M₆, at every real point of
B1512's table. This arc read all of them:
- 18 (level, class, λ) groups and 184 members per prime-root;
- M₄ exactly, by both routes;
- every group at every root of its factor modulo five primes of its own, two in route T and three in route L (28 distinct
  primes in all, none shared between the routes).

**Proved at the seal.**
- **The 10̄′ lives in the sub.** At a firing member, every 10̄′ class has a representative with values in the sub-bundle V (Lemma 2).
- **The sub-wedge lemma.** So every 10̄′·10̄′·5̄′_H coupling is the image of a class in H²(Λ²V), where Λ²V = ν² ⊗ Λ²ρ_q is the twisted
  Higgs bulk (Lemma 3).
- **The Higgs filtration.** Λ²W₁ sits between Λ²V and V ⊗ L, and V ⊗ L = ν⁻³ ⊗ ρ_q is acyclic on M₄, the background's own V_η ∋ c on
  M₆, and a deck-and-ι image of V on M₅ (Lemma 4).

**The answer (both routes).**
- **The twisted Higgs bulk is acyclic at every member** (P1 YES). So, by the sub-wedge lemma, the chiral 10̄′ cannot couple.
- **The Higgs sector is as Lemma 4 reads** (P2 YES):
  - **M₄** has no Higgs class at all;
  - **M₆** has one, the lift of the background's own class c;
  - **M₅** has one, two at its double point w = 7. These come from V ⊗ L, a deck-and-ι image of the member's V, not from the
    member's own c.
- **The chiral 10̄′ couples to none of them** (P3 YES). [a ∧ a′] = 0 in H²(Λ²W₁) for every pair of 10̄′ classes (route L), and
  ⟨h̄ ∪ a ∪ a′⟩ = 0 for every 5̄′_H (route T), at every member, prime and root.
- **No form joins two members of an orbit** (P5 NO). The 184 own triples carry exactly one form, the wedge form; all 5 400 cross
  triples carry none, although every orbit has cross triples that pass the character test. So the induced background on m004 has no
  cross coupling (P6, vacuous).
- **The non-chiral sector does couple** (P4 YES).
  - The 10′ classes of W₁ couple to the 5′_H on every M₅ and M₆ member.
  - At simple points those 10′ classes are not interior, so they are not normalizable zero modes.
  - At M₅'s double point one of them is interior: the vector-like partner of one of the two 10̄′. It couples to itself,
    B(f_int, f_int) ≠ 0 against both 5′_H classes (post-run (a), both routes).
- **The other order decouples too.** W₂, whose chiral state is a 10′, does not couple it to W₂'s Higgs classes (post-run (c), both
  routes).
- **Positive controls fired everywhere.**
  - x ∪ c ≠ 0 (route L) and ⟨y ∪ x ∪ c⟩ ≠ 0 (route T) at every reading.
  - B1513's banked zero and non-zero were reproduced through the generalised code (K5).
  - The joining-form code found the wedge form in every own triple.

**Reading.**
- **The law, through level 6.** Read with B1513, every chiral state of the harmonic tower has zero tree-level coupling to every
  Higgs class of its own background and of its orbit's induced background. That covers case (a)'s 10′ through a Jordan block (B1513
  on levels 1 and 3; its pullbacks to every level through 6 read here, post-run (e)) and case (b)'s 10̄′ through the sub-bundle
  (here, in both extension orders).
- **Chirality and coupling exclude each other.** The couplings that exist belong to non-chiral states.
- **The mass reading.** In main's frame a coupling is the coefficient of a mass term on actual flat connections (B1445
  Theorem C). Read the same way here (the analogue in this frame is not proved), the chiral matter gets no tree-level mass from
  its background's Higgs directions.
- **I-26 stays UNEARNED. 0 of 19.**

## 1. Setting

As sealed (PREREGISTRATION §1).
- **The frame.** B1509's E₈ ⊃ (SU(5) × SU(5)′)/ℤ₅. The 10̄′ comes with W, the 10′ with W*, the 5′_H with Λ²W, the 5̄′_H with Λ²W*.
- **A member.** ν = (ν_F, λ), V = ν ⊗ ρ_q, L = ν⁻⁴, V_η = ν⁵ ⊗ ρ_q, c ∈ H¹(V_η), and W₁ = [[V, cL], [0, L]].
- **The populations** (B1511 C1, B1512 D; data):
  - M₄: two orbits at w = 7, λ = 1;
  - M₅: four orbits at λ = 1 (w = 7, a double point), λ = ±i and λ = −1 (a Jordan point);
  - M₆: eight orbits at λ = ±1.
- **Arithmetic.**
  - Route T: B1513's relative triple product (`law_lib.py` on `higgs_lib.py`) over ℚ(ζ₁₂)[q]/(q² − 7q + 1) and GF(p), with roots
    found by flint.
  - Route L: the lifting criterion (`lift_route.py` on B1513's `independent_audit.py`) over ℚ(√5, √−3) and GF(p).

## 2. The lemmas (proved at the seal; PREREGISTRATION §3)

- **Lemma 1 (the cusp).** Every module that carries a Higgs slot is acyclic on the cusp, so duality turns each coupling into a class
  of H². This was checked at every reading (D3).
- **Lemma 2 (the 10̄′ lives in the sub).** H⁰(L) = 0 and x ∪ c ≠ 0 make H¹(V) → H¹(W₁) an isomorphism. Checked directly at every
  group (post-run (b)).
- **Lemma 3 (the sub-wedge lemma).** For a, a′ ∈ H¹(W₁), [a ∧ a′] is the image of [a_V ∧ a′_V] ∈ H²(Λ²V). So **if Λ²V is acyclic,
  every 10̄′·10̄′·5̄′_H coupling vanishes.** The dual statement holds for W₂, whose 10′ lives in its sub V*.
- **Lemma 4 (the Higgs filtration).**
  - M₄: V ⊗ L = ρ_q, acyclic because B1509's Q at μ⁴ = 1 has numerators 5q, −27q, −7q on q² − 7q + 1 = 0.
  - M₆: V ⊗ L = V_η, which carries c.
  - M₅: V ⊗ L is a deck-and-ι image of V.
  - This was checked at every reading (D6).
- **Lemma 5 (the deck and ι).** Every member of a group reads the same (D8, both routes).
- **Lemma 6 (the sector count).** n(W₁) = h¹(V) and n(W₁) − n(W₁*) = +1 (D4, both routes).

## 3. The sealed run

**Part 0, the banked identity,** passed first in both routes at all 18 groups: the banked h¹(L), h¹(V), h¹(V_η) and h¹(W₁), and
x ∪ c ≠ 0.

**Part A, the census.** The two routes give the same reading at every member of each group:

| group | h*(Λ²V) | h¹(V ⊗ L) | 5′_H = 5̄′_H | 10̄′ classes (interior) | 10′ classes (interior) | 10̄′ coupling | 10′ coupling |
|---|---|---|---|---|---|---|---|
| M₄, both orbits (exact and mod p) | 0 | 0 | 0 | 1 (1) | 2 (0) | — (no Higgs) | — (no Higgs) |
| M₅, λ = 1 (w = 7), c = c₁, c₂, c₁ + c₂ | 0 | 2 | 2 | 2 (2) | 3 (1) | **0** | ≠ 0 |
| M₅, λ = ±i and λ = −1 (the Jordan point) | 0 | 1 | 1 | 1 (1) | 2 (0) | **0** | ≠ 0 |
| M₆, all eight orbits, λ = ±1 | 0 | 1 | 1 | 1 (1) | 2 (0) | **0** | ≠ 0 |

All 1 120 route-T readings and all 1 672 route-L readings fall on these rows. The positive control fired at every one of them.

**Part B, the joining forms** (the first prime-root of every group, both routes). The 184 own triples carry exactly one form, the
wedge form; all 5 400 cross triples carry none. So no cross coupling exists to compute.

**Part C, the checks.** D1–D8 (route T) and D1–D9 (route L) all hold. Route L's comparison with route T's record passes on all 18
groups, and the predictions agree.

## 4. The predictions, read

| | prediction (prior) | result |
|---|---|---|
| P1 | the twisted Higgs bulk Λ²V is acyclic at every member (80%) | **YES**, every member, both routes |
| P2 | the Higgs content as Lemma 4 reads (75%) | **YES**: none on M₄; h¹(V) on M₅ (2 at w = 7, for every c); one on M₆ |
| P3 | **the law, own coupling:** the 10̄′ coupling to every 5̄′_H vanishes (85%) | **YES**, every member, prime and root, both routes |
| P4 | the 10′ coupling is non-zero at some member with a 5′_H (40%) | **YES**: at every M₅ and M₆ member |
| P5 | some cross triple carries a joining form (50%) | **NO**: 0 of 5 400 |
| P6 | every cross coupling through a joining form vanishes (80%) | **YES**, vacuously |
| P7 | **the law across the record**, with B1513 (75%) | **YES** |

## 5. Post-run checks (`verification/post_run_checks.py`, record `post_run_checks_run.txt`; not predictions)

- **(a) The interior 10′ at M₅'s double point.** n(W₁*) = 1 there: a vector-like partner of one of the two interior 10̄′. In both
  λ = 1 classes of M₅ its coupling is **non-zero**, by both routes:
  - B(f_int, f) ≠ 0 for some 10′ class f;
  - the self-coupling B(f_int, f_int) ≠ 0 against each of the two 5′_H basis classes (route T), and [f_int ∧ f_int] ≠ 0 in
    H²(Λ²W₁*) (route L).

  With B1513 (where an interior 10′ exists only where the coupling vanishes), this is the only coupling among normalizable zero
  modes in the record. It belongs to the vector-like pair, not to the chiral excess.
- **(b) Lemma 2 directly.** The image of H¹(V) in H¹(W₁) has rank h¹(W₁) at every group.
- **(c) The other order.** W₂ = [[L, δV], [0, V]], with δ a class of Hom(V, L) = V_η*, has a chiral 10′ (B1511's I(W₂) = −1).
  - Its 10′ classes number 1 at simple points and 2 at w = 7.
  - Its 5′_H classes number 0 on M₄, 1 on M₅ and M₆, and 2 at w = 7.
  - Its 10′ coupling is **zero** at every group, by both routes. This is the dual sub-wedge argument: W₂'s 10′ lives in its sub V*,
    and Λ²V* is acyclic.
- **(d) Where the non-zero 10′ couplings sit.**
  - On M₄ there is no Higgs class.
  - On every M₅ and M₆ group the coupling is non-zero. At simple points it involves only non-interior classes; at w = 7 it involves
    one interior class.
- **(e) Case (a) through level 6** (`verification/case_a_levels.py`, record `case_a_levels_run.txt`; added at the bank). The sealed
  text says B1513 read case (a). B1513 computed the join on m004 and the triplet on s961, so the other levels are read here
  directly, by both routes. That covers B1509's join pulled back to M₁–M₆, and the triplet pulled back to M₆. Each route used two
  primes per configuration and every root: 36 readings per route, on 22 primes in all, none shared.
  - At every reading: one 5′_H, Λ²V acyclic, h¹(W*) = 2 with one interior 10′, and the 10′ coupling **zero** on all of H¹(W*).
    Route L also finds the μ-type pairing and the cross terms [a_i ∧ e f₀] zero.
  - The positive control is **non-zero** by both routes: B1510's ±i point pulled back to M₅.
  - Transfer predicts this. At the join's q, Q = −q(s + 1)²(s² − 10s + 1) has no root on the unit circle other than −1, so every
    deck-twisted part upstairs is acyclic and every class is a pulled-back class. The same holds for the triplet with q³ for q.

## 6. The physical reading

**What holds.**
- **The law.** Through level 6 the harmonic tower has two chiral mechanisms:
  - case (a): B1509's 10′ through a Jordan block, on the pullback and the projective triplet;
  - case (b): the opposite-sign 10̄′, through x ∪ c ≠ 0, in orbits of four, five and six.
  In both, the chiral state has zero tree-level coupling to every Higgs class of its background (B1513 for case (a); here for case
  (b), in both extension orders). No form joins two members of an orbit, so the induced background on m004 has no cross coupling
  either.
- **The case-(b) mechanism is structural:**
  - the chiral state sits in the sub-bundle (Lemma 2);
  - its wedge lands in the twisted Higgs bulk (Lemma 3);
  - that bulk has no cohomology at any point read (P1).
- **The Higgs fields exist on M₅ and M₆.**
  - M₆: one 5′_H/5̄′_H pair, the background's own class lifted, as in case (a).
  - M₅: one pair (two at w = 7), from the member's image under the hyperelliptic involution and the deck.
  - M₄'s opposite-sign backgrounds have none.
- **Couplings exist, but only for non-chiral states.** The 10′ sector of W₁ couples to the 5′_H on every M₅ and M₆ member. At M₅'s
  double point that includes an interior 10′, the vector-like partner, which couples to itself.

**What it means.** Read with main's B1445 (in main's frame a coupling is the coefficient of a mass term on actual flat
connections, Theorem C; the analogue in this frame is not proved here):
- the harmonic frame gives its chiral matter **no tree-level mass from its own background's Higgs directions**, anywhere in the
  record through level 6;
- the only coupling among normalizable zero modes in the record is the self-coupling of the vector-like 10′ at M₅'s double point;
- an up-type Yukawa for chiral matter must come from outside the background's own Higgs sector.

**What it is not.**
- Not a statement about non-perturbative couplings (membrane instantons; the record computes none).
- Not about Higgs classes from another background, another state, or an end or apex inflow (B1509 lead 2).
- Not beyond level 6. The case-(b) mechanism is a theorem wherever the twisted bulk is acyclic, and acyclicity was computed only at
  these points.
- Not a mass or a ratio, and not a selection of any background, level or q.

**I-26 stays UNEARNED. 0 of 19.**

## 7. Record and disclosures

- **Order.**
  - PREREGISTRATION.md (sha256 12aa1edd…) was committed and pushed at a0badfa3. With it went both routes' code, the controls (K1–K6,
    126 s) and both routes' Part 0 run on banked data.
  - Route T ran first (2 479 s), then route L (2 196 s). Neither file was edited between the seal and the runs.
- **Before the seal (in the sealed text):**
  - a draft printed h¹(W₁*) at four M₅/M₆ members. It follows from banked data, and nothing depended on it.
  - A design slip, n(W₁*) = 0 at every member, was caught before the seal: at M₅'s double point n(W₁*) = 1 (ERROR_LEDGER).
- **One instrument change before the seal.** B1511's `gf_roots` is a brute force over GF(p) and too slow at p ≈ 8 × 10⁶. Route T
  finds roots with flint's `nmod_poly.roots`, as the sealed text says.
- **The sealed text's "B1513 read it" (case (a)).** B1513 computed levels 1 and 3. Post-run (e) reads the pullbacks to every level
  through 6 and the triplet on M₆, by both routes, before P7 is read through level 6.
- **A bug in post-run (e), caught before banking.** Its first run reported the route-L cross terms non-zero at every level, B1513's
  banked level 1 included. The check compared ModP's integer 0 with the string "0", so it could not pass. Fixed and rerun; the
  instruments were not involved (ERROR_LEDGER).
- **Post-run check (a) extended after its first run.** Its first version recorded only that some B(f_int, f) is non-zero. It now
  also records the self-coupling B(f_int, f_int) per 5′_H (route T) and [f_int ∧ f_int] (route L). Checks (b)–(d) reproduced
  unchanged.
- **The c-choice at M₅'s double point.** The two routes take c₁, c₂ and c₁ + c₂ in their own bases. Every reading was the same for
  every c in both routes, so the comparison needed no alignment.
- **Read at the seal for overlap:** main's S33 (357b7c98: B1445, B1446) and the audit lane's R76 (b2925dac). There is none
  (RELAY_LEDGER). B1445's Theorem C is cited in §6 as a reading, not used for a claim.
- **Read at the bank:** main moved to S34 (b08f76f7: B1447, the branch off one member's Higgs curve, in main's frame). There is no
  overlap with this arc's result; B1447 is cited in lead 3. The audit lane has not moved since R76.
- **Built on:** B1509, B1511, B1512 and B1513 (its instrument, its independent audit's method, and its case-(a) result).

## 8. Leads (registered, not run; each sealed before computing)

1. **The twisted bulk theorem.** Is ν² ⊗ Λ²ρ_q acyclic for every unitary fibre character ν and every q > 0, q ≠ 1, on every level?
   That would extend T-HIGGS-BULK-ACYCLIC to twisted bulks, and make the case-(b) decoupling a theorem on every level.
2. **Case (a)'s zero, proved** (B1513 lead 1, open). Case (b) now has a structural reason. Case (a)'s Jordan zero is still only
   computed.
3. **The vector-like pair at M₅'s double point.** Its 10′ couples to itself through both 5′_H (post-run (a)). Read with B1445,
   switching on a 5′_H direction would give that 10′ a mass term. Does that deformation exist in this frame, and what does it lift?
   Main's B1447 (S34, read at the bank) builds the analogous branch in its own frame: a family of flat connections leaving one
   member's Higgs curve.
4. **A Higgs from outside the background:** another state on the level, an end or apex inflow, or a non-perturbative coupling (B1513
   lead 3). The record now closes the inside door for every chiral state through level 6.
5. **The 5̄′** (unchanged, decisive).

> **Lead 5 taken (2026-10-02, B1515; PROVED by the sealed rule).** At q = 1, the one point of the family where Λ²W meets the cusp,
> two routes that share no code read every λ = 1 member of M₁–M₆. The 5̄′ count is zero at the 384 simple members. At 24 order-8
> members of M₆, through interior classes of ν ⊗ ρ₁, W₁ carries a 10̄′ and a 5̄′ (I = +1 and −1, anomaly −2): the wrong partner. No
> member through level 6 is generation-shaped. `frontier/B1515_the_hyperbolic_point`.

## Verification

- `verification/law_lib.py`: route T's members, couplings, joining forms and populations, on B1513's `higgs_lib.py`.
- `verification/lift_route.py`: route L, the lifting criterion on B1513's `independent_audit.py`. It shares no code with route T.
- `verification/controls.py` → `controls_run.txt`: K1–K6, run before the seal.
- `verification/census.py` → `census_run.txt`, `census_log.txt`: route T, the sealed run.
- `verification/independent_route.py` → `independent_route_run.txt`: route L, the sealed run, with the comparison.
- `verification/post_run_checks.py` → `post_run_checks_run.txt`: post-run checks (a)–(d), both routes.
- `verification/case_a_levels.py` → `case_a_levels_run.txt`: post-run check (e), case (a) through level 6, both routes.
- `tests/test_b1514_the_decoupling_law.py`: the lock.
