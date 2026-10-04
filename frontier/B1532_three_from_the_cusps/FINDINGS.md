# B1532 — THREE FROM THE CUSPS: no finite abelian cover of m004's levels M₂–M₆ carries even one generation of sm:B1515's frame at a λ = 1 pulled-back member, at any class; three does not occur

cc (the SM-derivation seat), 2026-10-04. Sealed at `97fdce6d` before any twisted term was read (`PREREGISTRATION.md`,
sha-256 `f7ff13be…`, SEAL_LEDGER).
- **The run.**
  - **Part 0, the banked identity,** came first in each route: all 507 χ = 1 terms equal sm:B1515's banked census rows, in I
    and in every B1297 dimension, in route T and in route L.
  - **Route L** (`run_terms.py`, sm:B1515's route L unchanged) read all 507 members at every χ and every class in one
    session of 13,060 s, finishing on 2026-10-03 at 23:15Z.
  - **Route T** read in two sessions. The first read 200 members (3,307 s). It was restarted with four workers at 20:34Z
    (resume-safe output; Part 0 passed again, 507 of 507) and read the other 307 in 21,071 s, finishing at 02:25:28Z on
    2026-10-04.
  - **The read-out** (`read_out.py`) ran as sealed at 02:28Z. Route C runs after it (the seal's §4), so its P1 read "route C
    missing" (`read_out_first_run.txt`).
  - **Route C** (`run_route_c.py`) read its sealed sample from 02:30Z for 841.6 s: 264 readings, all equal to route T's sums.
  - **The read-out ran again at 02:45Z** with route C's result (`read_out.json`, `read_out_log.txt`). The two printouts
    differ only in P1 (now true) and the timing (33.2 s, 33.8 s).
  - **No adjudication was needed:** D5 found no term on which the routes differ, so `adjudicate.py` did not run.
- **Verdict: NEGATIVE** (the seal's §9: both routes agree on every term, no count is unresolved, and no count is three).
  - **No finite abelian cover of M₂–M₆ carries a generation-shaped count of sm:B1515's frame at a λ = 1 pulled-back
    member, at any class, in either order.** Not three, and not one.
  - The census reads 68,596 counts in each route (every member, every class, every subgroup B of every level). The two
    routes' censuses are identical count for count (D5 = 0 term by term; the histograms were compared again at banking),
    and their list of generation-shaped counts is empty.
  - **Why: the 10̄′ side never goes below −1, and where it reaches −1 the 5̄′ side is at least two.** Every W count is ≥ −1.
    It is −1 at 1,344 counts, all at the interior class of M₆'s 120 two-class members, on covers containing χ = ν⁴. Every
    one of them has I(Λ²) = −2 (720) or −4 (624). No Λ² count is positive.
  - **The 5̄′ side is not small on M₆.** Its counts reach −28. On M₂–M₅ every Λ² term is 0.
- **As sealed: 5 of 9 predictions held** (P1, P2, P3, P7, P8). P4, P5, P6 and P9 fail. The priors expected 5.89.
- **Disclosed, not sealed: sm:B1535's blind prediction.** Theorem C was committed at `5c6a4225` before this read-out ran
  (`frontier/B1535_the_cap/PREDICTION_FOR_B1532.md`). Its prediction holds at all 163,507 readings of each route:
  - Λ² terms 0 on M₂–M₅;
  - on M₆, Λ² terms non-zero only at twists with n(ν⁻³χ ⊗ ρ) ≥ 1, never below −n;
  - every W term ≥ −1, and −1 only at χ = ν⁴.
- **After the run (disclosed; §4): the members at the twists κ⁵ = 1.** `post_run_twists.py` reads them on every finite
  abelian cover from the sealed terms: 110,956 counts per route, on M₂, M₄ and M₆. None is generation-shaped, and the routes
  agree.
- **A correction carried.** The seal quoted a design-time bound: the silver squares' covers trivial on the cusp carry "at
  most two" generations. That bound is one-sided and was withdrawn at sm:B1530's bank (ERROR_LEDGER, E9 instance). The
  silver squares' covers were read exactly by sm:B1534 and are bounded by proof in sm:B1535 (Theorem C, sealed).
- **What it is, and what it is not** (§5). It answers the owner's "continue with the next arc" for m004's own levels: the
  pullback of the frame to any finite abelian cover of a level carries no generation at λ = 1. It says nothing about:
  - the covers' own members (characters and classes not pulled back);
  - non-abelian covers;
  - members at other twists, beyond the κ⁵ = 1 check after the run (sm:B1535's Theorem C bounds every finite-order twist
    at one generation; its run is pending);
  - other states, or anything off the hyperbolic point;
  - which cover, if any, is physical (sL-5's one bit);
  - I-26 or the experiential question.
  **0 of 19 stays 0.**

## 0. What was found

**The census** (`read_out.json`; route T, identical in route L). A count is S(ν, c, B) = (I(p*W₁), I(Λ²p*W₁)) on the cover
cut out by B, at a member ν and a class c.

| level | ∣T_n∣ | subgroups B | counts | W counts | Λ² counts | generation-shaped |
|---|---|---|---|---|---|---|
| M₂ | 5 | 2 | 10 | 0 | 0 | none |
| M₃ | 16 | 15 | 240 | 0 … 5 | 0 | none |
| M₄ | 45 | 12 | 540 | 0 … 7 | 0 | none |
| M₅ | 121 | 14 | 1,694 | 0 … 20 | 0 | none |
| M₆ | 320 | 74 | 66,112 | −1 … 83 | −28 … 0 | none |

- **The subgroups** are found by closure. Their numbers, 2, 15, 12, 14 and 74, equal Tóth's s(1, 5), s(4, 4), s(3, 15),
  s(11, 11) and s(8, 40).
- **On M₂–M₅** every Λ² term is 0 at every class, so a count is (w, 0) with w ≥ 0: one or more 10̄′ with no 5̄′, never a
  generation.
- **On M₆** (66,112 counts over the one-class members' class, the two-class members' interior and generic classes, and
  every special class):
  - the W count is −1 at 1,344 counts, all at the interior class of the 120 two-class members (864 at the 96 of order 40,
    480 at the 24 of order 8), on covers containing χ = ν⁴. There I(Λ²) is −2 (720 counts) or −4 (624);
  - every other W count is ≥ 0, and every Λ² count is ≤ 0.
  So a generation-shaped count, I(W) = I(Λ²) ≠ 0, would have to be (−1, −1), and it does not occur.
- **The base itself (B = 1).** M₆'s 24 two-class members of order 8 read (0, −1) at the interior class and (1, −1) at the
  generic class. The 96 of order 40 read (0, 0) at both (at the interior class, as Corollary I requires). So P6 fails: none
  is generation-shaped on M₆ itself.
- **The degree law** S(ν, c, B) = |B|·T(ν, 1, c) holds at 10,465 of the 68,596 counts and fails at 58,131 (P9 fails).

## Seen first (the repo, then the literature)

**At the seal** (PREREGISTRATION §0, the PRIOR ART section). The sweep was `git fetch --all`, then
`scripts/checks/prior_work.py` and `git grep` on every head with eleven terms. Nothing read F-HE on any cover of a level;
"covers of M6" and "fibre covers" were absent on every head. sm:B1506 T2 and main's T-THE-LEVEL concern the level tower's
twists, which Lemma Z covers.

**Refreshed at banking** (2026-10-04, after `git fetch --all`). Main moved to `98714379` (S52, B1469: the sep16 lane rowed);
the other heads are as at sm:B1535's seal. The sweep ran again with eight post-run terms: "three from the cusps", "covers of
M6", "case (b) twist", "kappa^5", "shifted coset", "W = -1 only", "5bar' count", "generation-shaped".
- **"three from the cusps":** this seat's own records, and main's HARVEST_LEDGER row 837, which registers sm:B1532 as
  sealed and unbanked.
- **"covers of M6":** this arc only.
- **"shifted coset":** main's B933 design note (a spin structure's coset, another usage).
- **"case (b) twist" and "W = -1 only":** absent.
- **"kappa^5":** sm:B1534's Lemma Q (`members_every_twist.py` and its SEAL_LEDGER row) and sm:B1530's read-out, which bear
  on §4.
- **"5bar' count" and "generation-shaped":** the frame's own record (sm:B1509, sm:B1511, sm:B1515, sm:B1530, sm:B1534) and
  its harvests. The files that also name an abelian cover are this seat's ledgers and relays for sm:B1530 and sm:B1534,
  main's HARVEST_LEDGER, and sm:B1515's FINDINGS, whose cover sentence is about the four's interior classes (the seal's §0).
  None reads the frame's count on a cover of a level.

**The literature.** At the seal: Shapiro's lemma (Kedlaya, *Notes on class field theory*, Lemma 3.2.3) and the subgroup
count of ℤ/m × ℤ/n (Tóth, arXiv:1312.1485, Theorem 4.1), both read at source; Menal-Ferrer–Porti through sm:B1515's
Lemma 3. At banking nothing more was needed. The reading uses no external result beyond these. sm:B1535's Theorem C (which
cites Garland–Raghunathan through Monroe, arXiv:2604.22004 §6.1) is cited in §5 for what lies beyond this arc's scope; it is
not used in the verdict.

## 1. The run (as sealed)

### 1.1 The banked identity (Part 0)

`run_terms.py` repeats K1 in each route before any term is read. In both routes all 507 χ = 1 terms of M₂–M₆ equal
sm:B1515's census rows, in I and in every B1297 dimension of W₁ and Λ²W₁, the two-class members at their generic class
(`part0_T.json`, `part0_L.json`). Route T passed it again when it was restarted.

### 1.2 The terms (routes T and L)

- **Route T** (`cover_lib_t.py`): route T's own presentation, classes, pencils and special points, at the levels' first
  primes above 2²³.
- **Route L** (`cover_lib_l.py`): sm:B1515's route L unchanged, with its own presentation, classes and pencils, below 2²².
- Both read every term T(ν, χ, c) = (I(W₁(c) ⊗ χ), I(Λ²W₁(c) ⊗ χ)) of the population: 119,347 terms (ν, χ), and at every
  class 163,507 readings in each route.
- The terms themselves (`terms_T.jsonl`, `terms_L.jsonl`, 22 MB each) are kept compressed as `terms_T.jsonl.gz` and
  `terms_L.jsonl.gz`; their sha-256 before compression is in §7.

### 1.3 The checks

| check | what it reads | failures |
|---|---|---|
| D1 | Part 0 in both routes | 0 |
| D2 | the four pencils predict h¹ of E, E*, Λ²E, (Λ²E)* at every generic class | 0 |
| D3 | at every rational special point the flagged family's h¹ is above its generic value | 0 |
| D4 | gen2 = gen wherever gen2 was read | 0 |
| D5 | route T = route L term by term (terms, pencils, the multiset of special readings) | 0 |
| D6 | conjugation (Lemma D): T(ν̄, χ̄) = T(ν, χ) at the one-class, interior and generic classes | 0 |
| D7 | the design-time bounds and Corollary I, term by term | 0 |

The coincidence structure of the special classes (which (χ, family) share a class) is the same in both routes at every
two-class member.

### 1.4 Route C

`run_route_c.py` reads Lemma S's middle term directly: I(E ⊗ ℂ[A]) with ℂ[A] the permutation module, never split into
characters. Its sealed sample is eight members per level (M₂'s five) at every |B| ≤ 5, at the one class or at the interior
and generic classes, plus one subgroup of order 11 on M₅ for two members. The sample's hit list was empty, since no count is
generation-shaped.
- **Read:** 264 readings (M₂ 10, M₃ 88, M₄ 48, M₅ 10, M₆ 108; |B| = 1, 2, 3, 4, 5 and 11), all equal to route T's sums.
- The counts read whole include (1, 0), (3, 0), (3, −2), (2, −1), (1, −1) and (0, −1).

### 1.5 The read-out

`read_out.py` read the predictions as the seal's §7 states them. Its verdict rule is §9: both routes agree (D5 = 0, P2), no
count is unresolved, and no count is three, so the arc is NEGATIVE within its scope.

## 2. The theorems (as sealed), and what the run supplies

- **Lemma S** (the count is a sum of twisted terms) and **Lemma Z** (twists non-trivial on the cusp count 0) make every
  finite abelian cover's count a subgroup sum of the λ = 1 terms. Route C confirms Lemma S numerically in 264 readings of
  covers read whole (P1).
- **Lemma D:** the dual order counts the opposite at the conjugate class. D6 holds at every term, so only W₁ is read.
- **Lemma J and Proposition H:** special points only where νχ or ν⁻³χ is non-simple, in the families E and (Λ²E)*. P7
  holds: no other family has one.
- **Corollary I:** at the interior class every simple twisted term is (0, 0). D7 holds at every term.
- **The design-time bound** allowed counts down to (−4, −4) on M₆ from |B| = 4, so three was not excluded at the seal. The
  run reads W ≥ −1 everywhere; the bound was far from sharp on the W side.

## 3. The predictions

| | prediction | prior | read |
|---|---|---|---|
| P1 | route C equals route T's sum on every (ν, c, B) it reads | 97% | **holds** (264 of 264) |
| P2 | no D5 disagreement left after adjudication | 90% | **holds** (D5 = 0) |
| P3 | no generation-shaped count on any cover of M₂–M₅ | 85% | **holds** |
| P4 | some cover of M₆ carries a generation-shaped count at some class | 60% | **fails** |
| P5 | some cover of M₆ carries ∣N∣ = 3 | 30% | **fails** |
| P6 | an order-8 two-class member is generation-shaped on M₆ itself at its interior class | 40% | **fails**: (0, −1) |
| P7 | special points only at E with νχ ∈ NS and (Λ²E)* with ν⁻³χ ∈ NS | 92% | **holds** |
| P8 | every Λ² term at a simple ν⁻³χ is 0 at a non-interior class | 85% | **holds** |
| P9 | the degree law at every (ν, c, B) | 10% | **fails** (10,465 of 68,596) |

Five of nine held against priors summing to 5.89. G (golden) was stated as not informative here and not read: every level of
m004 is golden.

## 4. Post-run check: the members at κ⁵ = 1 (written after the run; disclosed)

sm:B1534's seal found its own population lacked its twist scope (ERROR_LEDGER, E9 instance) and noted that this arc's
population had the same open question. It is answered here from the sealed terms (`post_run_twists.py`, 94 s).
- **The members.** A member ν = ν₀ε with ν₀ a λ = 1 member and ε trivial on the fibre, ε(tₙ) = κ, κ⁵ = 1, κ ≠ 1, has the
  same V_η (ν⁵ = ν₀⁵). Since ε⁻⁴ = ε, W₁(ν, c) = W₁(ν₀, c) ⊗ ε and Λ²W₁(ν, c) = Λ²W₁(ν₀, c) ⊗ ε².
- **The counts.** On a cover with deck characters B′ its W terms are ν₀'s at εχ and its Λ² terms ν₀'s at ε²χ; by Lemma Z
  only twists trivial on the cusp count. With B₀ = B′ ∩ T_n^:
  - if B′ has no χ with χ(tₙ) = κ⁻¹ (equivalently κ⁻²), the count is (0, 0);
  - otherwise the count is (Σ_{y ∈ x₁+B₀} T_W(ν₀, y, c), Σ_{y ∈ 2x₁+B₀} T_Λ(ν₀, y, c)), with x₁ = εχ₁ ∈ T_n^, and the pairs
    (B₀, x₁ + B₀) that occur are exactly those with 5x₁ ∈ B₀.
  - x₁ ∈ B₀ gives ν₀'s own count (ε ∈ B′), already in the census. On M₃ and M₅ multiplication by 5 is invertible on T_n,
    so nothing new occurs; on M₂, M₄ and M₆ the shifted cosets are new: 4, 24 and 148 pairs (B₀, x₁ + B₀).
- **The check of the code.** The same code at x₁ = 0 reproduces the sealed census exactly, in both routes.
- **Read:** 110,956 counts per route (M₂ 20, M₄ 1,080, M₆ 109,856). None is generation-shaped. Every W count is ≥ −1 and
  every Λ² count lies in [−24, 0]. The routes agree.
- **Other twists.** A member whose κ is not a root of unity counts (0, 0) on every finite cover: a term needs a piece trivial
  on the cusp, which makes κ a root of unity (sm:B1534's Lemma Q argument). Members at roots of unity with κ⁵ ≠ 1, if any,
  are not read here. sm:B1535's Theorem C, with its Lemma W on the levels, bounds every finite-order member on every finite
  cover at one generation; that is sm:B1535's claim, sealed and pending its run, not this arc's.

## 5. What the reading means

### 5.1 The owner's arc, for m004's own levels

The arc asked whether a finite abelian cover of a level can carry three generations of the frame. The answer at λ = 1 is
no, and more: none carries one. The levels' covers carry 10̄′ alone (on M₂–M₅, and the positive W counts on M₆), or 5̄′
with fewer or no 10̄′ (on M₆). The two never meet at one value.

### 5.2 Why the sides never meet

The run's shape is what sm:B1535's Theorem C states, which was proved after this arc's seal and committed as a blind
prediction before its read-out:
- **The 10̄′ side is capped by b0 + n(ν⁴).** On a once-punctured-torus bundle every finite-order character is trivial on the
  puncture loop, so the line has no interior class (sm:B1535's Lemma W). A term's cap is then b0 = [χ = ν⁴], and a count's
  is the number of χ ∈ B equal to ν⁴, at most 1. That is the W ≥ −1 read here, with −1 only at χ = ν⁴.
- **The 5̄′ side is capped by the four's interior supply.** n(ν⁻³χ ⊗ ρ) is 0 on M₂–M₅ and non-zero on M₆ only at sm:B1515's
  28 characters. So Λ² is 0 on M₂–M₅ and reaches −28 on M₆'s large covers.
- **Where W = −1, the cover contains χ = ν⁴, hence the whole group ⟨ν⁴⟩:** order 2 at the 24 members of order 8, order 10
  at the 96 of order 40. Read at banking from the sealed terms: at the interior class ⟨ν⁴⟩ carries exactly two Λ² terms of
  −1 at every one of the 120 (at the order-8 members they are at χ = 1 and χ = ν⁴), so its count is (−1, −2). A larger cover
  adds only W terms ≥ 0 and Λ² terms ≤ 0. That is why (−1, −1) never occurs.

### 5.3 What this does not touch

- **The covers' own members** (sL-10 item 14): characters of π_A not pulled back, and the other Shapiro summands of
  H¹(M_A; p*V_η). sm:B1535 reads the second (the covers' own classes) under Theorem C; its §10 registers the first, the
  puncture characters.
- **Non-abelian covers,** where Mackey gives induced modules of dimension > 1 and the four's cuspidal supply can grow
  (bending; sm:B1535 Corollary C3).
- **Selection.** A count on a cover-state of X_gen is a count, not a held vacuum (R76), and which cover is physical stays
  open (sL-5).

## 6. Prior work and standing

- **EXTENDS** sm:B1515 (the frame, the members, routes T and L, the census as the banked identity) to every finite abelian
  cover of the levels, at every class.
- **sm:B1534** carried this arc's method to the silver squares (with Lemma S freed of ψ(P) = 1) and was banked first.
- **sm:B1535** (sealed at `b410afeb`) proves the cap that explains the census; its prediction for this arc was blind.
- New as swept: F-HE read on any cover of a level.

## 7. Errors in this arc, and the record

- **Before the seal:** a recall slip (Tóth's arXiv number) and a read-out crash caught by the dry run (ERROR_LEDGER rows of
  2026-10-03).
- **The withdrawn bound** quoted in the seal's source paragraph and §10 (the silver squares' covers "bounded by two") is an
  E9 instance, withdrawn at sm:B1530's bank. The sealed text is not edited.
- **The run:** no instrument was changed after the seal. Route T's restart was resume-safe and repeated Part 0.
- **The terms' sha-256** (before compression): `terms_T.jsonl` and `terms_L.jsonl`, recorded in `verification/terms_sha256.txt`.

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt`: the seal.
- `verification/run_terms.py`, `cover_lib_t.py`, `cover_lib_l.py`: the sealed run (routes T and L).
- `verification/terms_T.jsonl.gz`, `terms_L.jsonl.gz`, `terms_sha256.txt`, `terms_T_log.txt`, `terms_L_log.txt`,
  `part0_T.json`, `part0_L.json`: the terms and the run's logs.
- `verification/read_out.py`, `read_out.json`, `read_out_log.txt`, `read_out_first_run.txt`: the read-out.
- `verification/route_c.py`, `run_route_c.py`, `route_c_run.json`: route C.
- `verification/d5_failures.json`: D5's list (empty); `adjudicate.py`, not needed.
- `verification/post_run_twists.py`, `post_run_twists.json`: §4, after the run.
- `verification/controls.py`, `controls.json`, `controls_run.txt`, `dry_run*.py`, `dry_run*_log.txt`: before the seal.
- The blind prediction: `frontier/B1535_the_cap/PREDICTION_FOR_B1532.md` and `frontier/B1535_the_cap/verification/check_b1532.json`.
- `arc_verdict.json`; the lock `tests/test_b1532_three_from_the_cusps.py`.
