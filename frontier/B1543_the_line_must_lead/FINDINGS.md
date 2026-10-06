# B1543 — THE LINE MUST LEAD: a count (−g, −g) of sm:B1515's frame needs the cup map y ↦ c ∪ y on the line's classes to drop rank; at maximal rank, three needs 3 ≤ n(ν³ ⊗ ρ) and n(ν ⊗ ρ) ≤ b0 + n(ν⁴) − 3, at the trivial character 3 ≤ n(ρ) ≤ n(1) − 2; no cover the banked rows fix meets it

cc (the SM-derivation seat), 2026-10-06. **Not sealed: a corollary of a banked theorem, checked on the banked record, and a
census of banked data. No count is read.** Verdict: PROVED (the corollaries hold at every banked reading, and the census is
complete).

- **Corollary C′** (§1). From sm:B1535's Theorem C (ii), exactly: I(W₁) ≥ rk δ¹_W − b0 − n(ν⁴). Here δ¹_W : H¹(N; L) → H²(N; V),
  y ↦ c ∪ y, is the connecting map of 0 → V → W₁ → L → 0. A count (−g, −g) therefore needs rk δ¹_W ≤ b0 + n(ν⁴) − g.
- **Checked on the record** (§2). The bound holds at every one of the 5,204 banked readings that carry rk δ¹_W, with no
  violation: sm:B1541's 380, sm:B1536's 3,160 (Parts P and O, both routes) and sm:B1542's 1,664 (after its read-out). It is
  an equality at 189 and 1,576 of the first two, and at none of sm:B1542's.
- **The floor, observed and not proved** (§2). At all 6,756 banked readings that carry the count, I(W) ≥ −b0. That includes the
  2,828 readings where the line has interior classes and Theorem C (ii) would allow I(W) to reach −b0 − n(ν⁴). By the identity
  every reading checks, the floor means the boundary image of H¹(N; W) is no larger than W*'s boundary invariants. If it is a
  theorem, the frame's W count is at most one generation at every class, and three is out of this frame's reach. If it
  fails, it fails where that boundary image is large. It is the next question.
- **Why N₄₅'s generic stratum classes fail** (§3). On N₄₅ (sm:B1541) rk δ¹_W = 9 = h¹(N₄₅; ℂ) at every generic class of
  every cusp stratum: the cup map is injective, so I(W) ≥ 9 − 1 − 4 = 4 there. It is 8 on the deck group's twisted
  eigenspaces, 4 on the classes from d9.2, and 0 at the class pulled back from m003.
- **Corollary C″, the maximal rank** (§1). rk δ¹_W ≤ min(h¹(N; L), n(ν ⊗ ρ)). At a class where it is maximal, a count (−g, −g)
  with g > b0 needs n(ν ⊗ ρ) < h¹(N; L) and n(ν ⊗ ρ) ≤ b0 + n(ν⁴) − g. With Theorem C (i), three at maximal rank needs:
  - at a member ν: n(ν³ ⊗ ρ) ≥ 3 and n(ν ⊗ ρ) ≤ b0 + n(ν⁴) − 3;
  - at the trivial character: **3 ≤ n(ρ) ≤ n(1) − 2. The line must lead the four by two.**
- **The census** (§4). Of the 117 cyclic covers whose supplies sm:B1536's banked rows fix by Lemma A (sm:B1540's
  construction), none meets 3 ≤ n(ρ) ≤ n(1) − 2. The line's supply n(1) never exceeds 4 there, and the largest n(1) − n(ρ)
  is 2, at n(ρ) = 1. N₄₅ has (4, 18) and the degree-60 covers (3, 3) and (3, 7): the four leads, not the line. All 117 were
  also read directly, without Lemma A, in two routes and by integer homology; every one agrees.
- **The deck grading** (§1, §4). On a cyclic cover the deck group grades the cup map, so an eigenspace's classes have their own,
  smaller maximal rank B_j. Of the 585 eigenspaces of the 117 census covers, the graded criterion for three holds at 16, and
  every one of them carries no class of the four. So on these covers three needs a class below its graded maximal rank.
- **What it changes.** Room for three, min(1 + n(1), n(ρ)) ≥ 3, is necessary and was the census's criterion (sm:B1540). It is
  not sufficient. At a class whose cup map reaches its maximal rank, the line must lead: by two at the trivial character,
  and by the graded bound on an eigenspace. Whether a subspace's generic classes reach that rank is a fact of the cup product,
  read in the record, not of the dimensions alone. N₄₅'s strata reach the global bound, 9. Its eigenspaces do not: they reach
  4 and 8 against a graded bound of 9. So the search needs covers where the line leads, or classes whose cup rank is low.
  §5 names both, and two more places.

**0 of 19 stays 0.**

## 1. The corollaries

**Theorem C (ii)** (sm:B1535, proved at design time; its identities are checked at every reading of sm:B1535, sm:B1536, sm:B1541
and sm:B1542):

I(W₁) = dim(⟨c_i⟩ ∩ Λ(V)) − b0 + rk δ¹_W − dim(im δ¹_{W*} ∩ K_L),

with c_i the restrictions of c to the cusps where ν is trivial, Λ(V) the restriction image of H¹(N; V), b0 = [ν⁴ = 1], and K_L
the interior part of H²(N; L*), of dimension n(L*) = n(ν⁴).

**Corollary C′.** I(W₁) ≥ rk δ¹_W − b0 − n(ν⁴). So a count (−g, −g) needs rk δ¹_W ≤ b0 + n(ν⁴) − g.
- *Proof.* The first term is ≥ 0, and dim(im δ¹_{W*} ∩ K_L) ≤ dim K_L = n(ν⁴). □

**Corollary C″.** rk δ¹_W ≤ min(h¹(N; L), n(ν ⊗ ρ)), since im δ¹_W lies in K_V, the interior part of H²(N; V), of dimension
n(V) = n(ν ⊗ ρ) (Theorem C's proof, "δ¹_W"). Write h¹(N; L) = n(L) + p(L), p(L) being the dimension of the restriction image of
H¹(N; L) at the cusps, and note n(L) = n(ν⁻⁴) = n(ν⁴) (ν is unitary of finite order, and ν⁻⁴ is the conjugate of ν⁴). At a
class where rk δ¹_W = min(h¹(N; L), n(ν ⊗ ρ)):
- if h¹(L) ≤ n(V), Corollary C′ needs p(L) ≤ b0 − g, impossible for g > b0. At the trivial character p(1) is the number of
  cusps (half of H¹ of the boundary lives), so an injective cup map gives I(W₁) ≥ #cusps − 1;
- if n(V) < h¹(L), Corollary C′ needs n(ν ⊗ ρ) ≤ b0 + n(ν⁴) − g.

With Theorem C (i) (n(ν³ ⊗ ρ) ≥ g), three at maximal rank needs n(ν³ ⊗ ρ) ≥ 3 and n(ν ⊗ ρ) ≤ b0 + n(ν⁴) − 3. The condition
n(ν ⊗ ρ) < h¹(L) then holds by itself, since h¹(L) ≥ b0 + n(ν⁴). At the trivial character ν = ν³ = 1 and b0 = 1:
3 ≤ n(ρ) ≤ n(1) − 2. □
- When n(ν ⊗ ρ) = 0, δ¹_W = 0 at every class and the obstruction is absent (§5, item 3).
- A class below maximal rank (a special class) escapes C″ but not C′.

**The deck grading.** Let N_c be the k-fold cyclic cover of N along c. Shapiro grades the two sides:
H¹(N_c; ℂ) = ⊕_m H¹(N; c^m) and H¹(N_c; ρ) = ⊕_j H¹(N; c^j ⊗ ρ). The cup product and the interior part of H² respect
(j, m) ↦ j + m. So at the trivial character of N_c, a class c′ in the c^j eigenspace of the deck group has

rk δ¹_W(c′) ≤ B_j = Σ_m min(h¹(N; c^m), n(c^{j+m} ⊗ ρ)),

which can be smaller than the global bound min(h¹(N_c; ℂ), n(ρ)). At a class of the c^j eigenspace at its graded bound, three
needs B_j ≤ n(1) − 2, with n(ρ) ≥ 3. Classes that mix the eigenspaces, such as generic classes of H¹, are bounded only by the
global bound and can reach it.

Half lives for unitary characters gives:
- h¹(N; c^m) = n(c^m) + #{cusps of N where c^m is trivial};
- the four's h¹(N; c^j ⊗ ρ) = n(c^j ⊗ ρ) + #{cusps of N where c^j is trivial}.

A cusp torus carries H¹ of dimension 2 for the line and for the four when the character is trivial on it (the four of a
parabolic group fixes one line of Hermitian matrices), and 0 otherwise. The four's formula agrees with sm:B1542's control K2 on
all four of its covers and with sm:B1541's on N₄₅, each read directly in two routes (§4).

## 2. The check on the record

`verification/corollary_check.py`, record `verification/corollary_check.json` (banked data only).

| record | readings | C′ violated | C′ an equality | rk δ¹_W > n(V) | Theorem C (i) violated |
|---|---|---|---|---|---|
| sm:B1541 (all routes) | 380 | 0 | 189 | 0 | 0 |
| sm:B1536, Parts P and O, both routes | 3,160 | 0 | 1,576 | 0 | 0 |
| sm:B1542 (all routes; after its read-out) | 1,664 | 0 | 0 | 0 | 0 |

The two facts C′ and C″ rest on are re-read from the same records: im δ¹_W ⊂ K_V (rk δ¹_W ≤ n(ν ⊗ ρ)), and Theorem C (i)
(−n(ν³ ⊗ ρ) ≤ I(Λ²W) ≤ 0). Neither fails at any reading.

**The deck grading on sm:B1542's record** (`verification/b1542_check.json`). At all 216 eigenspace readings rk δ¹_W ≤ B_j, and at
all 1,664 readings rk δ¹_W ≤ the global bound. The ranks lie well below both. At the interior classes of d10.13's and d10.36's
covers rk δ¹_W = 0, yet the count is (−1, −3): C′ allows −4, and the W count stays at −1.

**The floor (an observation, not a theorem).** The banked identity route_r checks at every reading is
I(E) = h⁰(N; E) − h⁰(N; E*) + h⁰(∂N; E*) − r¹(E), with r¹ the rank of the restriction to the boundary. For the frame's W
(c ≠ 0, V without invariants) it reads I(W) = −b0 + h⁰(∂N; W*) − r¹(W). Tallied over every banked reading that carries the
count:

| record | readings | I(W) = −b0 | I(W) < −b0 | readings with n(ν⁴) ≥ 1 |
|---|---|---|---|---|
| sm:B1535's Part M, both primes | 1,552 | 288 | 0 | 0 |
| sm:B1536, Parts P and O, both routes | 3,160 | 1,728 | 0 | 784 |
| sm:B1541 | 380 | 9 | 0 | 380 |
| sm:B1542 | 1,664 | 666 | 0 | 1,664 |

So r¹(W) ≤ h⁰(∂N; W*) at every reading: the boundary image of H¹(N; W) never exceeds W*'s boundary invariants. sm:B1532's
163,507 terms per route also hold I(W) ≥ −b0 (sm:B1535's check), but there n(ν⁴) = 0, so they do not test the floor.

Half lives gives r¹(W) + r¹(W*) = h¹(∂N; W) = h⁰(∂N; W) + h⁰(∂N; W*). At an interior class on the trivial character
(c zero on every cusp, so h⁰(T; W) = h⁰(T; W*) = 2 on each cusp torus T) this makes I(W) = −1 + (r¹(W*) − r¹(W))/2. Three
would need r¹(W) − r¹(W*) = 4. On the record the difference is at most 0 at every interior class: N₄₅'s interior class has
r¹(W*) − r¹(W) = 10 (I(W) = 4), and the degree-60 covers' interior classes have 0 (I(W) = −1).

At such a class the boundary image of H¹(N; W) is made of two parts:
- H¹(N; V)'s image;
- the boundary values of lifts of line classes y with c ∪ y = 0.

A lift over an interior y restricts to the line's part as zero. Its part in H¹(∂N; V) is a secondary, Massey-type invariant of
(c, y) at the cusps. An excess of r¹(W) needs that invariant to leave H¹(N; V)'s image. Proving the floor, or finding a class
that breaks it, decides whether this frame can host three at all.

## 3. N₄₅'s cup ranks (sm:B1541's record)

| subspace | rk δ¹_W | count |
|---|---|---|
| every cusp stratum (0 to 5 free cusps) | 9 | (4, −10), (5, −7), (5, −6), (5, −5) |
| the deck group's eigenspaces ζ¹–ζ⁴, and their interiors | 8 | (5, −5); (3, −10) |
| ζ⁰ (the classes from d9.2), and its interior | 4 | (0, −5); (−1, −10) |
| the class pulled back from m003 | 0 | (0, 0) |

h¹(N₄₅; ℂ) = 9 = n(1) + #cusps = 4 + 5 (sm:B1540's Smith form gives H₁(N₄₅) = ℤ⁹ ⊕ (ℤ/2)², and route F reads n(1) = 4 at
three primes). Every generic stratum class has an injective cup map. Corollary C′ is an equality at 189 readings:
- on the strata with at most two free cusps, I(W) = 9 − 1 − 4 = 4;
- on every eigenspace's interior part: 4 − 1 − 4 = −1 on ζ⁰'s, 8 − 1 − 4 = 3 on the others'.

The two subspaces where the cup map drops (ζ⁰ and the pulled-back class) are the two where I(W) ≤ 0. They are the classes
that come from below.

The deck grading does not explain the drop on N₄₅. Its base character ε is trivial on d9.2's only cusp, so the graded bound is
9 on every eigenspace (§4's graded census), while the generic classes reach 8 on ζ¹–ζ⁴ and 4 on ζ⁰. The cup product itself is
degenerate there, beyond what the dimensions force.

## 4. The census

The 117 cyclic covers N_c of sm:B1536's thirty room covers whose every power has the line and the four fixed by the banked rows
(sm:B1540's construction, loaded by path), with (n(1), n(ρ)) at the trivial character by Lemma A:

| (n(1), n(ρ)) | covers | | (n(1), n(ρ)) | covers |
|---|---|---|---|---|
| (0, 2) | 2 | | (1, 11) | 6 |
| (1, 1) | 16 | | (3, 1) | 4 |
| (1, 2) | 28 | | (3, 2) | 2 |
| (1, 3) | 6 | | (3, 3) | 4 |
| (1, 5) | 14 | | (3, 7) | 2 |
| (1, 6) | 8 | | (4, 18) | 1 |
| (1, 10) | 24 | | | |

None meets 3 ≤ n(ρ) ≤ n(1) − 2. The line's supply is at most 4, and n(1) − n(ρ) is at most 2 (at (3, 1)). The four leads on
every cover with room ≥ 3: the seven are N₄₅ (4, 18) and the six degree-60 covers (3, 3) and (3, 7).

**The census read directly** (`verification/census_direct.json`, 446 s). Every one of the 117 covers was built from its
character and read at its trivial character without Lemma A:
- route N, Shapiro on the state with the cover's own permutation module (p = 16773481, 16775281 or 16776961);
- route R, the cover's own presentation, at another prime (p = 2147482801 or 2147482921);
- H₁ by PARI's Smith form.

All 117 agree with Lemma A's sums in both routes, and b1 − cusps = n(1) on every one. The degrees run from 10 to 100.
N₄₅'s supplies were also read by route F (sm:B1541), and four of the six degree-60 covers' by sm:B1542's control K1.

**The graded census** (`verification/graded_census.json`). Every eigenspace of every census cover's deck group was checked, 585
in all, with its graded bound B_j and the four's h¹ there.
- The per-power supplies are the banked rows'.
- The cusps where c^m is trivial are read off N_c itself: a cusp of N on which c has order o has k / o cusps of N_c above it.

The graded criterion (B_j ≤ n(1) − 2 with n(ρ) ≥ 3) holds at 16 eigenspaces: j = 1, 2, 4, 5 on the 6-fold covers of d10.13,
d10.14, d10.36 and d10.38. All 16 are empty. There n(ψ^j ⊗ ρ) = 0 and ψ^j is non-trivial on every cusp, so the four's h¹ is 0.

The four's h¹ per eigenspace agrees with the controls that read it directly in two routes:
- sm:B1542's K2: (5, 0, 0, 4, 0, 0) on d10.13's and d10.36's covers, (5, 0, 2, 2, 2, 0) on d10.16's and d10.40's;
- sm:B1541's K2: (3, 5, 5, 5, 5) on N₄₅.

On the non-empty eigenspaces of the degree-60 covers, B_j is 3 or 4, so I(W) ≥ −1 there at the graded bound. (−3, −3) needs
rank ≤ 1.

d10.13's and d10.14's 6-fold covers are one cover of m003 up to conjugacy (sm:B1540), and so are d10.36's and d10.38's. Each such
cover therefore carries two deck structures. Their eigenspaces are different subspaces of the same H¹(N; ρ), with different
line gradings: (4, 0, 1, 3, 1, 0) and (5, 1, 0, 2, 0, 1).

## 5. Where three can live

Corollary C′ is necessary for every count; C″ only for classes of maximal rank. So three can live:
1. **At special classes**, where the cup map drops below its maximal rank, global or graded. On N₄₅ they are the classes that
   come from below (the ζ⁰ eigenspace and the pulled-back class). By C′, three on N₄₅ needs rk δ¹_W ≤ 2; on the degree-60
   covers it needs rank ≤ 1.
2. **On covers where the line leads.** Cyclic covers along a character with a large line supply qualify: by Lemma A, n(1) on
   N_χ is the sum of n(χʲ) over the powers, so a Galois orbit of puncture characters with n(χ) = 3 (sm:B1538's Part L)
   multiplies the line. The four's supply there is the open structure question (a census after sm:B1538's records are
   regenerated).
3. **At members where n(ν ⊗ ρ) = 0**, where δ¹_W = 0 at every class. There I(W) = dim(⟨c_i⟩ ∩ Λ(V)) − b0 −
   dim(im δ¹_{W*} ∩ K_L), so I(W) = −3 needs rk δ¹_{W*} ≥ 3 − b0, and h¹(N; ν⁻¹ ⊗ ρ) ≥ 3 − b0.
   - If ν is non-trivial on every cusp, that h¹ is 0: n(ν⁻¹ ⊗ ρ) = n(ν ⊗ ρ) = 0, and the cusp cohomology vanishes (a cusp
     element with ν ≠ 1 acts by ν times a unipotent). Then I(W) = −b0. When b0 = 1, ν³ = ν⁻¹ and n(ν³ ⊗ ρ) = 0, so
     I(Λ²W) = 0. No count there is generation-shaped.
   - So cusps where ν is trivial are needed.
4. **By the golden lift** (sm:B1534's Lemma Q, sm:B1541 §5.2). On a 5-fold cyclic cover along a golden character, a generic
   pulled-back class counts Y + 4X: the trivial member's count plus four times a golden member's. The four golden members'
   generic counts agree by Galois invariance (Lemma C) when ℚ(ζ₅) is disjoint from the holonomy's field; a sealed reading
   would read all four.
   - Theorem C (i) makes both Λ² terms ≤ 0, so a total −3 needs Y_Λ = −3 and X_Λ = 0.
   - The base must saturate C (i) at its trivial character (n(ρ) ≥ 3), and X_W = −1 needs the line at the golden character.
   - N₄₅'s generic classes cannot (their Λ² counts are −5 to −10). sm:B1542's d10.13 and d10.36 covers, with n(ρ) = 3, are in
     range.

**A prediction for sm:B1542, registered before its read-out**
(`docs/dossiers/the_line_must_lead_2026-10-06/PREDICTION_FOR_B1542_BEFORE_ITS_READ_OUT.md`, commit 646a4fc4; not part of its
seal):
- no class on its four covers counts (−3, −3);
- any generation-shaped count is (−1, −1), on d10.13's or d10.36's cover;
- on d10.16's and d10.40's covers I(W) ≥ 3 at every class of maximal rank.

## Seen first (the repo sweep and the literature)

- **The repo sweep.** `git fetch --all` first, then `scripts/checks/prior_work.py` over every head with twelve terms:
  "Corollary C'", "rk d1(E)", "cup map", "connecting map", "maximal rank", "line must lead", "the line leads",
  "injective cup", "delta1_W", "rk delta", "interior supply", "n(nu x rho)".
  - It first ran at 13:55Z (this seat at dedd2a9b, main at 88ed6981). It was run again at 15:00Z over every head then present,
    with main at 0b4b4786 and a new web seat's branch at 2579ca01. The second run found new hits only in this seat's own files
    of the afternoon: the kill-graph entry of sm:B1541, its view, and the registered prediction. The new web seat's branch has
    no hit for any of the distinctive terms.
  - "line must lead" and "injective cup" are absent everywhere; "n(nu x rho)" too. "the line leads" and "delta1_W" appear
    only in this seat's own kill-graph entry for sm:B1541 (written today, citing this arc) and its view.
  - "rk d1(E)" appears only in the instruments that compute it (sm:B1535, sm:B1536).
  - "Corollary C'" names other corollaries (B1509's C) apart from that kill-graph entry.
  - "cup map" appears once outside this seat: the audit lane's silver cyclic transfer design (2026-10-06). It names cup maps
    and a cup annihilator on the cusp torus of its fixed silver member, a local boundary construction. It has no rank bound
    for δ¹_W.
  - "connecting map" and "maximal rank" are common in other senses.
  - The bearing source is this seat's sm:B1535 (Theorem C, whose (ii) is the corollary's premise), with sm:B1536 and sm:B1541's
    records.
- **The literature.** Two queries: the "half lives, half dies" lemma for the boundary of a 3-manifold; and Menal-Ferrer and
  Porti's twisted cohomology of cusped hyperbolic 3-manifolds and the restriction to the boundary. Both sources were read in
  full text today.
  - A. Putman, "Half lives, half dies and the signatures of boundaries" (note, dated 1 November 2022), Theorem 0.4 with
    Corollary 0.3. For a compact oriented (2n+1)-manifold with boundary and a field of characteristic ≠ 2, the kernel of
    H_n(∂M) → H_n(M) is a Lagrangian, so half-dimensional. For n = 1 and torus cusps, the restriction H¹(M; ℂ) → H¹(∂M; ℂ),
    its dual, has rank #cusps. That is p(1) = #cusps, used in C″. It is also re-derived on the instances: sm:B1540's Smith
    forms give b1 − cusps = n(1) on N₄₅ and the six degree-60 covers.
  - P. Menal-Ferrer and J. Porti, "Twisted cohomology for hyperbolic three manifolds", Osaka J. Math. 49(3) (2012),
    arXiv:1001.2242v2, Theorem 0.1. For the holomorphic irreducible representations V_n, n ≥ 2, composed with a lift of the
    holonomy, H¹(M; E_ρn) injects into H¹(∂M; E_ρn) with half its dimension: no interior classes. The paper treats
    holomorphic representations only. The four (the action on Hermitian matrices, V₂ ⊗ V̄₂) is not one, and this seat's banked
    interior supplies of it are positive (18 on N₄₅).
  - No source read bounds this frame's count by a cup rank. The frame is this seat's (sm:B1515), and the corollary is two lines
    from Theorem C (ii).
- **Standing: EXTENDS** (sm:B1535's Theorem C).

## Disclosures

- An earlier draft of this file lost its paths to a shell substitution: it was written with an unquoted heredoc, so the shell
  ran the backticked strings. One of them was `git fetch --all`, which advanced the seat's view of main to 0b4b4786 and showed
  the new web seat's branch. The others failed harmlessly. The text was rewritten, the sweep re-run over every head after the
  fetch, and the slip logged in ERROR_LEDGER. No banked file was touched.
- The prediction of §5 was written after sm:B1542's seal, while its run was at task 325 of 556, before any of its rows was read.

## Files

- `verification/corollary_check.py`, record `verification/corollary_check.json`: the check on the record and the census.
- `verification/census_direct.json` (`corollary_check.py --direct --record`): the census read directly.
- `verification/graded_census.json` (`corollary_check.py --graded --record`): the deck grading on every census cover.
- `verification/b1542_check.json` (`corollary_check.py --b1542 --record`): C′ and the gradings on sm:B1542's record.
- `verification/floor.json` (`corollary_check.py --floor --record`): the floor's tally over every banked reading.
- `tests/test_b1543_the_line_must_lead.py`: the lock.
