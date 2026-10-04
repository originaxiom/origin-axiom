# B1534 — THE SILVER COVERS: no finite abelian cover of m135 or m136 carries three generations at a pulled-back member of sm:B1515's frame, in either order; the 5̄′ side is capped at two

cc (the SM-derivation seat), 2026-10-04. Sealed at `1f58d161` before `run_terms.py` read any twisted term
(`PREREGISTRATION.md`, sha-256 `0423e1f1…`, SEAL_LEDGER).
- **The run.**
  - The banked identity came first. `controls.py` and `members_every_twist.py` were re-run unchanged from 23:35:13Z to
    23:39:34Z. `identity.py` finds them identical to the sealed outputs in every field but the timings, and all twelve
    sealed hashes check. This was committed at `2729f761` before any term was read.
  - `run_terms.py` read every term of every member at every class in routes E (exact over ℚ(ζ₂₄)) and N (60 digits), from
    23:39:55Z to 23:53:55Z (840 s). It used one worker, no error.
  - `run_route_c.py` read route C, the permutation module never split into characters, on each member's order-4 cover,
    from 23:54:12Z (2906 s). It agrees with route E's sums on all 16 readings.
  - `read_out.py` read the sealed predictions (`read_out.json`, `read_out_run.txt`).
- **Verdict: NEGATIVE** (the seal's §9: P7 holds, so the routes agree, and P4 holds).
  - **No finite abelian cover of m135 = −LLRR or m136 = +LLRR carries three generations at a pulled-back member of
    sm:B1515's frame at the hyperbolic point, in either order.** The scope is every member at every twist (Lemma Q), every
    class, and every subgroup of every contributing group.
  - **The only generation-shaped count that occurs is (−1, −1):** one generation, as at the base, in W₁'s order; (+1, +1)
    in the dual order (Lemma D). It occurs in two places:
    - at m135's interior class, on every cover whose deck group meets C_ν in one of the 3 subgroups (of 8) that miss the
      character (½, ½);
    - at m136's κ = −1 members, on every cover whose deck group meets C_ν in one of the 11 subgroups (of 16) that miss
      (½, ½; 0). The common double cover is one of them.
  - **Why three cannot occur: the 5̄′ side is capped at two.** Of the 144 terms, a Λ² term is non-zero only at the
    non-simple members (m135's u₁, u₂; m136's κ = −1 members), at the two twists χ with νχ non-simple. There it is −1 (0 at
    the special class). Every simple twist reads Λ² = 0 (P5), and so do the simple members at every twist. So on any cover,
    I(Λ²p*W₁) ∈ {0, −1, −2}, and a generation-shaped count has |a| ≤ 2.
  - **The 10′ side is not capped.** At m135's four members of order 4, the W term is +1 at five of the eight twists and the
    Λ² term is 0. So covers count (1, 0), (3, 0) and (5, 0): one, three or five 10̄′ with no 5̄′, anomalous by
    I(Λ²W) − I(W) = −1, −3, −5. In B1509's dictionary these are not generations.
- **As sealed: 7 of 8 predictions held** (P1, P3–P8). P2 fails: the (½, ½) term at m135's interior class is (0, −1), not
  (0, 0), so covers that contain (½, ½) count (−1, −2) there. The priors expected 6.64.
- **After the run (disclosed; §4).** `post_run_s.py` reads every term and count again on SnapPy's own presentation, cusp and
  polished holonomy, with its own members, classes, pencils and special classes. It agrees with route E on both states:
  every member, every profile of terms, every special class and every subgroup count (712 s).
- **What it is, and what it is not** (§5). It answers the owner's question of 2026-10-03 ("are u sure about the math behind
  your negative conclusions about three generatiosn, sure sure sure?") for the silver squares: the withdrawn one-sided bound
  is replaced by the exact readings, both signs and every class. It says nothing about:
  - the covers' own members (characters and classes not pulled back);
  - non-abelian covers;
  - other states, or anything off the hyperbolic point;
  - which cover, if any, is physical;
  - I-26 or the experiential question.
  **0 of 19 stays 0.**

## 0. What was found

The population (§5 of the seal) is every member at every twist, by Lemma Q. Its counts are those of the fourteen members
listed in the seal's §2:
- **m135:** eight members at κ = 1, each with C_ν ≅ ℤ/4 × ℤ/2 and 8 subgroups.
- **m136:** four members at κ = 1 with C_ν ≅ (ℤ/2)² and 5 subgroups, and two at κ = −1 with C_ν ≅ (ℤ/2)³ and 16 subgroups.

Characters are written as fibre part and t′-turn, (w₀, w₁; k).

**The terms T(ν, χ, c) = (I(W₁(c) ⊗ χ), I(Λ²W₁(c) ⊗ χ))** (`terms.json`). There are 144 in each route, and the routes agree
on every one. W = +1 occurs at 24 terms, all at simple members.

| state | member | class | terms (all other χ ∈ C_ν read (0, 0)) |
|---|---|---|---|
| m135 | u = (0, 0), (½, ½) (simple) | the class | (1, 0) at χ = (½, ½) |
| m135 | the four of order 4 (simple) | the class | (1, 0) at the five χ ∉ {1, ν, ν⁻¹} |
| m135 | u₁ = (0, ½), u₂ = (½, 0) | c_int | (−1, −1) at χ = 1; (0, −1) at χ = (½, ½) |
| m135 | u₁, u₂ | every generic class | (0, −1) at χ = 1 and at χ = (½, ½) |
| m135 | u₁, u₂ | the special class s = ∓√2/30 | (0, 0) at all eight |
| m136 | u = (0, 0), (½, ½), κ = 1 | the class | (1, 0) at χ = (½, ½; 0) |
| m136 | u = (0, ½), (½, 0), κ = 1 | the class | (0, 0) at all four |
| m136 | u₁, u₂, κ = −1 | the class | (−1, −1) at χ = 1; (0, −1) at χ = (½, ½; 0) |

- **The special classes** (route E's pencils, all 64; route N's own pencils find the same special points, within the run's
  10⁻²⁵ criterion, and the same generic ranks).
  - Only the (Λ²E)* pencil drops rank, and only at χ = 1 and χ = (½, ½) of m135's two members.
  - Both drop at one point, s = −√2/30 at u₁ and s = +√2/30 at u₂ (c_s = c_b + s·c_int in route E's basis). That point lies
    in K, so no conjugate pair occurs.
  - Every other pencil (E, E*, Λ²E at every χ; (Λ²E)* at the six other χ) has no special point.
  - At the special class every term is (0, 0). There the Λ² term rises from −1 to 0 at both χ = 1 and χ = (½, ½). Read
    through sm:B1530's Lemma D, this is the one class, up to scale, where bit = 1 (an inference, §5.3).
- **The counts.** Over every member, class and subgroup (164 rows, the two generic classes counted separately), the counts
  that occur are:
  - (−1, −1), 28 times;
  - (−1, −2), 20 times;
  - (0, −1), 12 times;
  - (0, −2), 20 times;
  - (0, 0), 42 times;
  - (1, 0), 30 times;
  - (3, 0), 8 times;
  - (5, 0), 4 times.
  - No other count occurs. In particular there is no (a, a) with |a| ≥ 2, and no |I(Λ²)| ≥ 3.
- **By member.**
  - m135's interior classes count (−1, −1) on {1}, {1, (0, ½)} and {1, (½, 0)}, and (−1, −2) on the five subgroups that
    contain (½, ½).
  - m135's generic classes count (0, −1) and (0, −2) the same way, and the special class counts (0, 0) everywhere.
  - The order-4 members count (0, 0) on {1}, (1, 0) on four subgroups, (3, 0) on two, and (5, 0) on the whole group.
  - m136's κ = −1 members count (−1, −1) on 11 of their 16 subgroups and (−1, −2) on the 5 that contain (½, ½; 0).

## Seen first (the repo, then the literature)

**At the seal** (PREREGISTRATION §0, the PRIOR ART section). The sweep was `git fetch --all`, then
`scripts/checks/prior_work.py` over seven heads with twelve terms. It found sm:B1532 (the method), sm:B1530 (the members and
routes), sm:B1515, sm:B1509, main's B1297 and B1466, and sm:B1506 T2 with main's T-THE-LEVEL. Nothing reads F-HE on a
cover of m135 or m136 beyond sm:B1530's common double cover.

**Refreshed at banking** (2026-10-04, after `git fetch --all`). Every head is as at the seal: main `d295fc5d`, the audit lane
`c7aa3a29`, and the other seats as listed there. The sweep ran again with eight post-run terms: "silver covers", "special
class", "anomalous count", "10bar-only", "three 10", "sqrt2/30", "bit = 1", "order-4 member".
- **sm:B1511 (the projective tower) bears on §5.2.** On m004's levels its 10′ count reaches three (s961, one per background
  of a deck orbit), while Λ²W is boundary-acyclic, so there is no 5̄′ on any level. The silver covers show the same split:
  here the 5̄′ side is non-zero, but capped at two.
- **"silver covers":** B129 and B771 (SL(3) trace fields on the silver bundle's cyclic covers, another frame), sm:B1530 and
  this arc.
- **"special class":** main's B1442 ("a special class of a several-dimensional H¹(ℓ)", another usage) and sm:B1532's seal.
  Nothing reads a special class of the four's extension on m135 or m136.
- **"anomalous count":** sm:B1397 (the flux caps' anomaly), THE_SM_VERDICT and the kill graph, in another frame.
- **"three 10":** sm:B1511's s961 row (above) and the negatives' synthesis that cites it.
- **"10bar-only" and "sqrt2/30":** absent.
- **"bit = 1":** sm:B1530's seal (its Lemma D) and an unrelated script of B766.
- **"order-4 member":** this arc only. sm:B1372 and sm:B1373's "order-4 points" are another usage.

**The literature.** At the seal: Shapiro's lemma (Kedlaya, *Notes on class field theory*, Lemma 3.2.3) and the subgroup
count of ℤ/m × ℤ/n (L. Tóth, arXiv:1312.1485, Theorem 4.1), both read at source for sm:B1532. At banking nothing more was
needed: the reading uses no external result beyond those and sm:B1515's Lemma 3 (Menal-Ferrer–Porti, arXiv:1001.2242). Not
found in the sources read: any reading of a rank-five extension of a twisted four on a cover of a punctured-torus bundle.

## 1. The run (as sealed)

### 1.1 The banked identity

`identity.py` compares `controls_rerun.json` with `controls.json` and `members_every_twist_rerun.json` with
`members_every_twist.json`. Both are identical but for the timings. K0–K10 hold again:
- the relators and cusp of the exact holonomies;
- every banked member and χ = 1 term of sm:B1530;
- Lemma Z′ on 28 characters off the population;
- the subgroup counts;
- the pencils at χ = 1;
- route C on the two banked covers;
- route N's own pencils;
- the fibre operator's eigenvalues on both states.

### 1.2 The terms (routes E and N)

- **Route E.** sm:B1530's exact_lib reads every term over ℚ(ζ₂₄). class_index asserts B1297's identity, the annihilator
  identity and Lemma E at each of the 288 indices (144 terms, two modules each).
- **Route N.** It reads the same terms at 60 digits on its own numerical four, with route E's classes carried by the
  conjugator. The conjugator's relative singular values are 1.05 × 10⁻⁶¹ against 0.031 (m135) and 6.02 × 10⁻⁶¹ against
  0.055 (m136).
  - Every identity held.
  - The smallest kept singular value was 1.16 × 10⁻⁵ (relative), and the largest dropped 1.29 × 10⁻⁵⁷.
  - The routes agree on all 144 terms.
- **Route N's pencils.** Route N reads every term at route E's classes, carried, the special classes included. Its own
  pencils (64, from its own Fox kernels and cokernels) found the same generic ranks and the same special points as route
  E's, within the run's criterion of 10⁻²⁵: one point per two-class member, at χ = 1 and χ = (½, ½) alike.

### 1.3 Route C

`run_route_c.py` reads Lemma S's middle term directly: I(W₁ ⊗ ℂ[A]) and I(Λ²W₁ ⊗ ℂ[A]), with ℂ[A] the permutation module
of A = H₄^, never split into characters. It ran from 23:54:12Z for 2906 s.
- **Which covers.** H₄ is each member's first subgroup of order four in the instrument's order. The modules have rank 20
  and 40 over ℚ(ζ₂₄).
- **Which classes.** It reads the interior class (or the one class) and c_g1: 16 readings.
- **Read.** All 16 equal the sum of route E's terms over H₄. The counts read whole were (−1, −2), (−1, −1), (0, −2), (0, 0),
  (1, 0) and (3, 0). Among them are the order-4 members' (3, 0) and the interior class's (−1, −2).
- **The controls had already checked it on two banked covers (K7):** the 3-fold cyclic cover along t at m135's interior
  class, and the common double cover at m136's κ = −1 member.

### 1.4 The read-out

`read_out.py` reads terms.json and route_c.json, and its verdict rule is the seal's §9.
- P1, P3, P4, P5, P6, P7 and P8 hold; P2 fails.
- P7 holds, so the verdict is not withheld.
- P4 holds: no (state, member, class, subgroup) has a count (a, a) with |a| = 3.
- **Verdict: NEGATIVE.** No finite abelian cover of m135 or m136 carries three generations at a pulled-back member of
  sm:B1515's frame, in either order.
- The generation-shaped counts by |a| are |a| = 1 only.
- `read_out_run.txt` is its printed output.

## 2. The theorems (as sealed), and what the run supplies

- **Lemma S** (every finite regular abelian cover) and **Lemma Z′** turn every cover's count into a subgroup sum of the 144
  terms. Route C reads the cover whole on the order-4 covers and agrees (all 16 readings).
- **Lemma Q**, with K10, carries every member at every twist onto the fourteen. Members at κ ∈ μ₁₀ are the listed ones
  twisted by ε of order 5: their counts are a listed member's on the same cover when ε ∈ B, and (0, 0) when it is not.
  Members at other twists count (0, 0) on every finite cover.
- **Lemma D:** the dual order's counts are minus these at the conjugate member. So the dual order's only generation-shaped
  count is (+1, +1).
- **Proposition H′** holds as read (P3): the special classes lie at χ ∈ {1, (½, ½)} only.
- **Corollary I′** holds as read (P1): at m135's interior class every term with νχ simple is (0, 0), and every count lies
  in {(−1, −1), (−1, −2)}. That is two of the four values the corollary allows.
- **The boundary-type ranges.** At simple twists they allowed W = 1 − δ_χ ∈ {0, 1} and Λ² = bit_χ ∈ {0, 1}. At non-simple
  twists they allowed W ∈ {0, 1, 2} and Λ² ∈ {−1, 0, 1}. The run reads:
  - W ∈ {0, 1} and Λ² = 0 at every twist of every simple member, non-simple twists included; W = 1 at 24 terms;
  - bit_χ = 0 at every simple twist;
  - W = 0 and Λ² ∈ {−1, 0} at the non-simple twists of the non-simple members' boundary-type classes.

## 3. The predictions

| | prediction | prior | read |
|---|---|---|---|
| P1 | Corollary I′ at m135's interior class | 97% | **holds** |
| P2 | the (½, ½) term at c_int is (0, 0) | 50% | **fails**: (0, −1) |
| P3 | special classes only at χ ∈ {1, (½, ½)} | 95% | **holds** |
| P4 | **the question:** no three on any abelian cover, either order | 85% | **holds** |
| P5 | every Λ² term at a simple twist at a boundary-type class is 0 | 85% | **holds** |
| P6 | every generation-shaped count has ∣a∣ = 1 | 60% | **holds** |
| P7 | the routes agree (E and N on every term and special point; C on every cover read) | 95% | **holds** |
| P8 | conjugate members of m135 carry the same multisets of terms | 97% | **holds** |

The priors sum to 6.64; seven held.

## 4. Post-run check S (written after the run; disclosed)

`post_run_s.py` was written after `run_terms.py` had read its outcome. It is disclosed here and is not sealed.

**Why.** Routes E and N share three inputs that one slip would reach alike: the group (family_lib's bundle presentation
⟨a, b, t⟩ with cusp words abAB and t′ = t or abt), the coordinates (u, κ), and the class basis (route N reads route E's
classes, carried by the conjugator). Route S shares none of these. Its group, cusp and point come from SnapPy:
- b+−LLRR, identified as m135(0,0): generators a, b, c; relators accBab and aabCBC; cusp abcacB and abc. The four's
  relator residual is 5.8 × 10⁻⁵⁹.
- b++LLRR, identified as m136(0,0): relators abAccB and aacbCB; cusp ACac and b. Residual 2.3 × 10⁻⁵⁹.
These come through sm:B1530's loader, unchanged.

Route S finds the rest itself:
- its members, as every character of order dividing 4 with h¹(ν ⊗ ρ) ≥ 1;
- its contributing characters, by Lemma Z′ read on SnapPy's peripheral curves;
- its classes, from an interior basis and a boundary-type class of its own;
- its own pencils and special points, at all eight (or four) χ and all four modules.

It reads every term at the interior class, at two generic classes and at every special class it finds, and then every
subgroup's count. It shares route N's class-index code (sm:B1527's cusp_lib) and nothing with route E's exact_lib.

**Read.**
- **m135:** 8 members (h¹ 1 or 2, as route E). The two two-class members each have one special class, found by route S's
  own pencils. The profiles (the sorted terms per class kind, the number of special classes, and the (order, count)
  multisets) equal route E's on all 8.
- **m136:** 6 members, four at κ = 1 with |C_ν| = 4 and two at κ = −1 with |C_ν| = 8. The profiles equal route E's on all 6.
- Every identity check held. Lemma Z′ read off C_ν gave (0, 0) at the two characters checked per member.
- The generation-shaped counts are (−1, −1) only, and no count is three.

## 5. What the reading means

### 5.1 The owner's question, for the silver squares

The question of 2026-10-03 was whether the negative conclusions about three generations were sure. On the silver squares:
- the design note's bound ("at most two") was one-sided and is withdrawn (sm:B1530 §7; ERROR_LEDGER, E9);
- this arc replaces it with the exact readings.

On every finite abelian cover of m135 and m136, at every pulled-back member of sm:B1515's frame at the hyperbolic point,
the count is one of eight values, and none is three generations in either order.

The negative is stated with its population: frame F-HE, the hyperbolic point, m135 and m136, every finite regular abelian
cover, every pulled-back member at every twist and every class. It stands on two sealed routes that agree on every term
(one exact), route C reading the covers whole, and a third route on SnapPy's presentation after the run. It does not
reach:
- the covers' own members;
- non-abelian covers;
- any other state.

### 5.2 Where the count comes from, and why it stops at one

- **The 5̄′ side.** A Λ² term is non-zero only at the non-simple members, at their two non-simple twists:
  - χ = 1 and χ = (½, ½) at m135's u₁ and u₂;
  - χ = 1 and χ = (½, ½; 0) at m136's κ = −1 members.
  Each is −1, or 0 at the special class. So a cover carries at most two 5̄′. The simple twists' bit_χ is 0 everywhere,
  which is sm:B1530's Part C (Λ_A ∩ π_A = 0) here read at non-square χ too.
- **The 10′ side.** The interior class gives −1, at χ = 1 only. The simple members give W = +1 at 24 terms. So W₁'s 10′
  count on a cover is at most one, and its 10̄′ count reaches five.
- **The two sides meet only at (−1, −1).** I(W) ≥ −1 on every cover, and I(Λ²) ∈ {0, −1, −2}, so a non-zero agreement is
  (−1, −1). That is the interior class's −1 at χ = 1, on covers whose deck group misses the other non-simple twist: the
  base's one generation, pulled back.

### 5.3 The special class

- At s = ∓√2/30 the extension is still non-split. But every twisted term vanishes there, the base's (0, −1) included.
- It is the one boundary-type class, up to scale, where the Λ² term vanishes. Read through sm:B1530's Lemma D
  (I(Λ²W₁) = bit − 1 at a boundary-type class), it is where e ∧ c_P lies in Λ_A (bit = 1). That is an inference: bit
  itself was not computed at the special class.
- sm:B1530 read c_b, c_b ± c_int and c_b + 2c_int, none of them special, so it did not see this class.
- The class adds no count. It is a fact about the moduli of W₁: the boundary-type line of classes carries one point where
  the 5̄′ count switches off.

### 5.4 Where three could still be

- **The covers' own members.** These are characters and classes on a cover that are not pulled back from the base. By
  Shapiro, H¹(M_A; p*V_η) = ⊕_{χ∈B} H¹(M; V_η ⊗ χ), and the pulled-back classes are the χ = 1 summand. The other summands
  are new classes, and nothing here reads them (§10 of the seal; registered as sL-10 item 14).
- **Non-abelian covers** (Mackey gives induced modules of dimension > 1).
- **Off the hyperbolic point, other states, other frames.**
- **A coupling between the sides.** The 10̄′-only counts (3, 0) and (5, 0) are anomalous in B1509's dictionary. A frame
  that supplied 5̄′ from another sector would read them differently. None is on the record.

## 6. Prior work and standing

- **EXTENDS** sm:B1530 (the members, the routes, the common double cover) and sm:B1532 (the method on m004's levels, which
  is running). It answers sL-10 item 11.
- It replaces the design note's one-sided bound (ERROR_LEDGER, E9 instance) and closes the scoping slip found at the seal
  (Lemma Q; ERROR_LEDGER, E9 instance).
- No external source reads a rank-five extension of the twisted four on a cover of a punctured-torus bundle (§ Seen
  first). B1515's frame exists only in this repository.

## 7. What this arc does not decide (the next questions)

- **The covers' own members** (sL-10 item 14), on the smallest abelian covers of m135 and m136, by Shapiro's
  decomposition: H¹ of the twisted four on the cover, summand by summand, with every class's count. A class in a single
  χ summand is the pullback of the base module ν ⊗ [[ρ, c], [0, η⁻¹]], with η = ν⁵χ and c ∈ H¹(η ⊗ ρ), so those classes
  reduce to finitely many base readings. Classes mixing summands need a pencil over the summands, and characters of the
  cover that are not pulled back need the cover's own group.
- **sm:B1532's levels of m004.** It is running, and its correction is due in its FINDINGS. The same twist question stands
  for its population beyond λ = 1, to be stated in its FINDINGS.
- **The order-4 members' 10̄′ counts** of 3 and 5 with no 5̄′: whether any frame pairs them.
- **sL-10 items 12 and 13:** the fused module at m135, and what holds the member.

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt` — the seal.
- `verification/silver_lib.py`, `silver_n.py` — routes E and N.
- `verification/controls.py`, `controls.json`, `controls_run.txt` — K0–K9.
- `verification/members_every_twist.py`, `.json`, `_log.txt` — K10.
- `verification/identity.py`, `controls_rerun.*`, `members_every_twist_rerun*` — the banked identity.
- `verification/run_terms.py` → `terms.json`, `run_log.txt` — the sealed run.
- `verification/run_route_c.py` → `route_c.json`, `route_c_log.txt` — route C.
- `verification/read_out.py` → `read_out.json`, `read_out_run.txt` — the predictions.
- `verification/post_run_s.py` → `post_run_s.json`, `post_run_s_log.txt` — route S, after the run.
- `arc_verdict.json`; the lock `tests/test_b1534_the_silver_covers.py`.
