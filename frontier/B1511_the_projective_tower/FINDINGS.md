# B1511 — THE PROJECTIVE TOWER: on s961 the three order-2 characters carry B1509's 10′ each, a projective triplet; M₄ carries the opposite sign in orbits of four; no level carries a 5̄′

**Date:** 2026-10-01 · **Seat:** cc (the SM-derivation branch) · **Verdict:** PROVED.
- The theorems were proved at the seal, except one sentence of Theorem F, which is corrected here (§7).
- The sealed run reads D1–D7 as decided, P1–P6 and P8 YES, and P7 NO.
- 32 pairs are UNRESOLVED and registered as the next arc.

· **Price:** unchanged, 0 of 19 · **Seal:** `PREREGISTRATION.md`
(sha256 b5fbd35930882eacb5e1ba8d01203c2520dce8da1de81cd04142eeb1d575e8d7), committed and pushed at 49baea7d before the run.

## 0. Seen from above

B1509 found one 10′ on m004. On the audit lane's harmonic vacuum A ⊕ 1, A = μρ_q, the extension W₁ = [[A, c], [0, 1]] counts −1 at
q = 17 ± 12√2 with μ = −1, where the fibre monodromy has a Jordan block. This arc carried that construction to m004's cyclic covers
M₁–M₆ in B1506's frame. Backgrounds are ν ⊗ ρ_q for every character ν of the level, and the root's deck acts on them. The census read
every level by deck orbit.

1. **The pullback counts one on every level** (Theorem D). B1509's W₁ pulls back to −1 on every Mₙ at q = 17 ± 12√2, with
   λ = (−1)ⁿ. Its deck orbit has size one.
2. **s961 carries a projective triplet** (P2 YES). The deck orbit of T₃ = (ℤ/4)²'s three characters of order 2 is exceptional at
   q³ = 17 ± 12√2, with λ₃ = ν(m³) = −1.
   - There the fibre monodromy has a Jordan block: kernel dimensions 1, 2, 2, 2 on H¹.
   - Each of the three backgrounds has I(W₁) = −1 and I(W₂) = +1, with data (0, 1, 1, 1), exactly B1509's.
   - This was found exactly over ℚ(i)[q]/(q⁶ − 34q³ + 1) and at 10 prime–root pairs. Λ²W counts 0.
   - That is three 10′ on s961, one per background. Pulled back to M₆ (λ₆ = 1) it is still three (Part B; Shapiro holds). By the
     level law the root object counts gcd(n, 3): 1, 1, 3, 1, 1, 3 on levels 1–6.
   - **The mechanism is exact:** the orbit's twisted Alexander polynomial is B1509's at q³, P_{O₂}(q, s) = Q(q³, s) (post-run (a)).
     The triplet is B1509's Jordan block met at the cube root of B1509's q.
3. **The order-4 orbits do not fire** (P3 YES, P4 YES). All four are exceptional:
   - at q² − 11q + 1 = 0 with λ₃ = 1;
   - at the palindromic sextic q⁶ − 12q⁵ + 20q⁴ + 14q³ + 20q² − 12q + 1 = 0 with λ₃ = −1.

   Every root is simple (kernel dimensions 1, 1, 1, 1), so every count is 0.
4. **M₄ carries the opposite sign in orbits of four** (P6 YES). This is case (b): the line ν⁻⁴ is non-trivial on the fibre and trivial
   on the cusp.
   - M₄'s two orbits of 3-torsion characters are exceptional at q² − 7q + 1 = 0, that is q = φ^{±4} with φ the golden ratio, at λ = 1.
   - There each of their 8 members has I(W₁) = +1 and I(W₂) = −1, exactly and over GF(p); Λ²W counts 0.
   - Read in B1509's dictionary that is one 10̄′ per member: four per orbit on M₄. The level law gives gcd(n, 4) = 1, 2, 1, 4, 1, 2.
5. **No level carries a 5̄′** (Theorem A(vi)). Λ²W is boundary-acyclic for every rank-five extension of a character by any twisted
   ρ_q on any level. So I(Λ²W) = 0 everywhere, confirmed at every point read. The tower adds 10′s, or 10̄′s, never the 5̄′ that
   would cancel them.
6. **What stays open** (P7 NO). Part C2 found a common root at all three primes in 102 of its 356 pairs.
   - In 70 of them the common factor is q² + q + 1 (post-run (b)), whose roots are not positive.
   - The other 32 are M₅'s four eigenline orbits at every λ and M₆'s eight order-8 orbits at λ = ±1. Their twisted polynomials are
     real (post-run (c)) and their coincidence is automatic, so case (b) can fire there at generic real q.
   - Theorem F's last sentence said it could not, which was a design-time error (§7).
   - Under the sealed reading rule these 32 are UNRESOLVED, counted neither way, and are the next arc's question (§8).

**Reading.**
- Three is reached in this family exactly as B1506 found it in the Standard-Model frame: as a deck orbit of three backgrounds on s961,
  m004's only 3-fold cover.
- Here each background is an honest harmonic vacuum: R42's metric on the cover, tensored with a unitary character.
- Each carries B1509's chiral 10′.
- But they are three distinct vacua (B1506's fence), each anomalous alone (no 5̄′), at a q no dynamics has selected.
- **I-26 stays UNEARNED. 0 of 19.**

## 1. Setting

As sealed (PREREGISTRATION §1).
- Mₙ = F ⋊ ⟨mⁿ⟩, with Tₙ = coker(Φⁿ − 1) of orders 1, 5, 16, 45, 121, 320.
- Characters ν = (ν_F, λ). The deck acts by (a, b) ↦ (b, 3b − a).
- The background is V = ν ⊗ ρ_q, and W₁ = [[V, c·L], [0, L]] with L = ν⁻⁴ and c ∈ H¹(ν⁵ ⊗ ρ_q). W₂ is the opposite order.
- The twisted fibre monodromy is S_ν = [[0, A₁], [−αA₂, A₁ + αA₂ + βA₃]], and S⁽ⁿ⁾ is the product around the level.
- P_ν(q, s) is its characteristic polynomial on H¹(F; ν_F ⊗ ρ_q).
- Main's index I = n(V) − n(V*) is read on B1506's Reidemeister–Schreier presentation of each level:
  - exactly over ℚ(i)[q]/(g) and ℚ(ζ₁₂)[q]/(g);
  - over GF(p) through B1374's index_lib, at three primes and every root.

## 2. The theorems (proved at the seal; proofs in PREREGISTRATION §3)

- **Theorem A (the count's shapes, every level).**
  - V is boundary-acyclic. ℓ is a commutator in F, so every character is trivial on it, and ρ_q(ℓ) has eigenvalues q, q, q, q⁻³.
  - Case (a), L = 1: I(W₁) = −r1 ∈ {0, −1}, and −1 iff e ∪ c = 0.
  - Case (b), L ≠ 1 but trivial on the cusp: I(W₁) = 1 − r1 ∈ {0, +1}, and +1 iff x ∪ c ≠ 0, with x generating H¹(Mₙ; L). It needs
    h¹(ν ⊗ ρ_q) ≥ 1 and h¹(ν⁵ ⊗ ρ_q) ≥ 1 at the same q.
  - Λ²W counts 0 always, and |I| ≤ 1.
- **Theorem B (Wang on the covers).** H¹ = ker(λ⁻¹S⁽ⁿ⁾ − 1) and H² = coker(λ⁻¹S⁽ⁿ⁾ − 1). In case (a), I(W₁) = −1 iff c lies in the
  Jordan part. P_ν is an invariant of the deck orbit.
- **Theorem C (which case on which level).** Case (a) occurs on levels 1–6 only for the trivial character and T₃'s sixteen (levels 3
  and 6).
- **Theorem D (the pullback).** −1 on every level at q = 17 ± 12√2 with λ = (−1)ⁿ, deck orbit of size one, and 0 at every other point,
  including every h¹ = 2 point.
- **Theorem E (three).** An honest three needs an orbit of size three, and those are T₃'s characters, case (a). So s961's five orbits
  decide three on every M_{3j}.
- **Theorem F (case (b)'s automatic coincidence).** ν⁵ lies in ν's deck orbit exactly for M₄'s 3-torsion, M₅'s eigenline and M₆'s
  order-8 characters (C10).
  - Its last sentence claimed that real roots are generic only on M₄'s 3-torsion orbits. **That is withdrawn** (§7): every twisted
    polynomial is real (post-run (c)).
  - Corrected: case (b) can fire at generic real q on all three families of self-coincident orbits.
    - On M₄'s it does (Part C1).
    - On M₅'s and M₆'s it is UNRESOLVED (P7, §8).

## 3. The sealed run (`verification/tower_census.py`, record `tower_census_run.txt`, 21 minutes)

**The banked identity** passed inside the run: B1509's Q at level one, and B1509's first row (I(W₁) = −1, I(W₂) = +1, I(Λ²W₁) = 0) on
this arc's index.

**Part A — s961's five orbits of size three** (exact over ℚ(i)(q); every point exact and over GF(p) at every root):

| orbit | P(q, s) | λ₃ | real exceptional locus | positive roots | ker dims of (S − λ)ʲ | counts W₁ / W₂ / Λ² |
|---|---|---|---|---|---|---|
| O₂ = {(0,2), (2,2), (2,0)} (order 2) | Q(q³, s), palindromic | −1 | q⁶ − 34q³ + 1 | 0.30877, 3.23868 | **1, 2, 2, 2 (Jordan)** | **−1 / +1 / 0, each member** |
| | | ±i | q⁶ − 14q³ + 1 | 0.41562, 2.40602 | 1, 1, 1, 1 | 0 / 0 / 0 |
| | | 1 | (q − 1)²(q² + q + 1)² | none | — | — |
| O_A, Ō_A (order 4) | real, not palindromic, equal | 1 | q² − 11q + 1 (and q − 1, q² + q + 1) | 0.09167, 10.9083 | 1, 1, 1, 1 | 0 / 0 / 0 |
| | | −1 | q⁶ − 12q⁵ + 20q⁴ + 14q³ + 20q² − 12q + 1 | 0.10213, 0.34039, 2.93780, 9.79134 | 1, 1, 1, 1 | 0 / 0 / 0 |
| | | ±i | none | — | — | — |
| O_B, Ō_B (order 4) | real, not palindromic, equal | as O_A | as O_A | as O_A | 1, 1, 1, 1 | 0 / 0 / 0 |

- Every orbit's three members have the same polynomial (D1).
- At every point: rank B = 4, so H⁰(F) = 0. The direct h¹ equals the fibre's kernel dimension at every member, exactly and at every
  prime–root pair (D2).
- Every count lies in Theorem A's range, with both identities asserted (D3). Λ²W counts 0 everywhere (D4).
- I(W₁) = −1 exactly at the Jordan point (D5).
- No P(q, λ) vanishes identically (P8).

**Part B — M₆** (the first member pulled back, λ₆ = λ₃², over GF(p) at every root; D6, post-run (d)):
- At the triplet's point (λ₆ = 1): h¹ = 1, and I(W₁) = −1, I(W₂) = +1.
- At O₂'s ±i points (λ₆ = −1): h¹ = 2, because λ₃ = i and −i are both exceptional there. Every class counts 0.
- At the order-4 points: h¹ = 1 and the count is 0.
- Shapiro's h¹(λ₃) + h¹(−λ₃) and its count hold at all eleven points.

**Part C1 — M₄'s two 3-torsion orbits at λ = ±1.** Their P is exact over ℚ(ζ₁₂)(q), and f is rational.
- **λ = 1:** f = (q − 1)⁴(q² − 7q + 1)(q² + q + 1). At q² − 7q + 1 = 0 (q = φ^{±4} = 6.85410, 0.14590) the fibre root is simple
  (1, 1, 1, 1), with h¹(L) = h¹(V_ν) = h¹(V_{ν⁵}) = 1.
  - **Every member of both orbits has I(W₁) = +1 (data (0, 1, 1, 0): r1 = 0, so x ∪ c ≠ 0), I(W₂) = −1 and I(Λ²W) = 0.**
  - This holds exactly over ℚ(ζ₁₂)[q]/(q² − 7q + 1) and at 6 prime–root pairs per orbit.
- **λ = −1:** an octic with no positive root.

**Part C2 — the GF(p) gcd test on every other pair** (levels 2, 4, 5, 6; three primes each):

| level | pairs | no common root but 0, 1 | UNRESOLVED | of which the factor is q² + q + 1 (post-run (b)) | self-coincident, real (post-run (c)) |
|---|---|---|---|---|---|
| M₂ | 8 | 8 | 0 | — | — |
| M₄ | 44 | 36 | 8 (λ = 1) | 8 | 0 |
| M₅ | 96 | 60 | 36 | 20 (λ = 1) | 16 (four eigenline orbits × four λ) |
| M₆ | 208 | 150 | 58 | 42 (λ = 1) | 16 (eight order-8 orbits × λ = ±1) |

C10's classification was reproduced inside the run (D7).

**Part D — the per-level table** (families with a non-zero count at some positive q ≠ 1, λ ∈ μ₄; W₁-type count per member):

| level | pullback (Theorem D) | orbits of three (Part A, Shapiro) | case (b) (Part C) | UNRESOLVED |
|---|---|---|---|---|
| m004 | −1 at q = 17 ± 12√2 | — | — | — |
| M₂ | −1 | — | none | — |
| s961 | −1 | **O₂: three × (−1) at q³ = 17 ± 12√2, λ₃ = −1** | — | — |
| M₄ | −1 | — | **two orbits of four × (+1) at q = φ^{±4}, λ = 1** | — |
| M₅ | −1 | — | none among the resolved | 4 eigenline orbits of five (16 pairs) |
| M₆ | −1 | **O₂ pulled back: three × (−1), λ₆ = 1** | none among the resolved | 8 order-8 orbits of six (16 pairs) |

The pullback and the triplet never fire at the same q, so no single background configuration on s961 counts four.

## 4. The predictions, read

| | prediction (prior) | outcome |
|---|---|---|
| P1 | O₂'s polynomial is palindromic (~80%) | **YES**: it is Q(q³, s) |
| P2 | O₂ fires: a projective triplet on s961 (~40%) | **YES**: at q³ = 17 ± 12√2, λ₃ = −1; each member −1 (W₁), +1 (W₂); exact and 10 prime–root pairs |
| P3 | no order-4 orbit fires on s961 (~85%) | **YES**: every root simple. Its stated reason, "their polynomials are complex", was wrong; they are real (§7) |
| P4 | some order-4 orbit is exceptional at a positive q ≠ 1 (~60%) | **YES**: all four, at q² − 11q + 1 (λ₃ = 1) and the sextic (λ₃ = −1) |
| P5 | Shapiro on M₆ (~97%) | **YES**: all eleven points |
| P6 | case (b) fires on M₄ (~35%) | **YES**: both 3-torsion orbits, every member +1, at q = φ^{±4}, λ = 1 |
| P7 | Part C2 finds no coincidence (~85%) | **NO**: 102 pairs UNRESOLVED at all three primes. Post-run, 70 are q² + q + 1; 32 are real self-coincident pairs |
| P8 | no s961 orbit is identically exceptional (~90%) | **YES** |

## 5. Post-run checks (`verification/post_run_checks.py`, record `post_run_checks_run.txt`; not predictions)

- **(a) The triplet is B1509 at q³.** P_{O₂}(q, s) = Q_monic(q³, s) exactly, read from the record and checked symbolically. So O₂'s
  exceptional loci are B1509's with q ↦ q³:
  - q⁶ − 34q³ + 1 at −1;
  - q⁶ − 14q³ + 1 at ±i;
  - (q³ − 1)² at 1.
  The Jordan block sits where B1509's does. Why an order-2 twist on the 3-fold cover reproduces the base at q³ is not explained here
  (lead).
- **(b) The λ = 1 coincidences are q² + q + 1.** The 70 UNRESOLVED pairs that are not self-coincident (8 on M₄, 20 on M₅, 42 on M₆) were
  recomputed. After q and q − 1, the common factor is exactly q² + q + 1 at every prime. It also divides every λ = 1 polynomial seen in
  Parts A and C1. Its roots are the primitive cube roots of unity, so none of these pairs coincides at a positive q.
- **(c) Every twisted polynomial is real.** P_ν(q, s) = P_{ν⁻¹}(q, s) identically over GF(p), at all 32n + 1 interpolation points, for
  every character at levels 2–6. That is 2, 6, 22, 60 and 158 pairs, none differing.
  - Since ρ_q is real, P_{ν⁻¹} = P_ν̄ is the conjugate polynomial, so each P_ν is real.
  - The likely mechanism is the fibre's hyperelliptic involution: −1 on H₁(F), central in the punctured torus's mapping class group,
    which carries ν to ν⁻¹ and presumably fixes ρ_q. This is not proved here (lead).
  - It is why s961's four order-4 orbits share two real polynomials, and why the 32 self-coincident pairs came out UNRESOLVED.
- **(d) The triplet and Shapiro.** All three members of O₂ give (−1, +1, 0, data (0, 1, 1, 1)) exactly and at all 10 prime–root
  pairs. Every Part-B row agrees with Shapiro.

## 6. The physical reading

**Three, from the harmonic family.**
- B1506 found three on s961 as an orbit of the root's deck, in the Standard-Model frame (rank-two doublet modules).
- This arc finds three there in the audit lane's harmonic family, with B1509's mechanism. Each of the three backgrounds
  ν ⊗ (μρ_q ⊕ 1) is a harmonic vacuum: R42's complete Blaschke metric on the cover, tensored with a flat unitary character. Each carries
  one chiral 10′ of SU(5)′ through the Jordan block of its twisted fibre monodromy.
- The number three is again the degree of m004's only 3-fold cover. Its three order-2 characters are permuted by the root's deck.

**What it is not.**
- **Not a generation.** There is no 5̄′, on s961 or any level (Theorem A(vi)), so each background's count is anomalous on its own.
- **Not three families of one vacuum.** The three backgrounds are distinct flat bundles, whose characters differ by order-2 characters
  (B1506's fence). Reading them as three families needs the whole orbit in one configuration, which the record does not derive.
- **Not selected.**
  - q = (17 ± 12√2)^{1/3} is not chosen by any dynamics here.
  - The end condition is main's interior one (B1509 Proposition E: the 10′ count runs over 0, 1, 2 with the end).
  - Whether the deck is gauged (one) or kept (three) is B1506's open bit.
- **The opposite sign exists.** On M₄, at q = φ^{±4}, a different mechanism (case (b), x ∪ c ≠ 0) gives 10̄′ in orbits of four. The
  tower does not fix a sign by itself.

**I-26 stays UNEARNED. 0 of 19.**

## 7. Record and disclosures

- **Order.** PREREGISTRATION.md (sha256 b5fbd359…e8d7) was committed and pushed at 49baea7d with the instrument and the controls
  (C1–C10), before any twisted polynomial of a non-trivial character was computed. The run is `tower_census.py --record`, 21 minutes.
- **Theorem F's last sentence is withdrawn (a design-time reasoning slip; ERROR_LEDGER).**
  - The seal argued that a self-coincident orbit not closed under inversion has a complex polynomial, so its real roots are
    non-generic. On that basis it called M₄'s 3-torsion orbits the only place case (b) could fire at generic real q.
  - The premise is false. Every twisted polynomial is real (post-run (c)), so M₅'s eigenline and M₆'s order-8 orbits qualify too.
  - The sealed run is unaffected. It sent those pairs to the gcd test with their inverse orbits, as sealed, and reported them
    UNRESOLVED, as the sealed rule requires.
  - P3's stated reason ("their polynomials are complex") was wrong for the same cause. Its outcome is unaffected.
  - The corrected statement is in §2.
- **P7 is NO under the sealed rule.** The post-run identification of q² + q + 1 in 70 pairs is labelled post-run. It removes them from
  physical relevance, but it does not convert them to a sealed YES.
- **The 32 self-coincident pairs** are UNRESOLVED and counted neither way, as sealed. Their roots and counts are a new open outcome,
  sealed as the next arc (§8).
- **Harvested by citation:**
  - main's S30/B1441 (several-cusped, rank two: none counts three), B1442 (sealed), L234 and B1440;
  - the audit lane's R42 (the background on covers), R54–R56, R69 and R74, and its records that the cover counts are owed;
  - B1506's frame and level law.

## 8. Leads (registered, not run; each sealed before computing)

1. **The 32 self-coincident pairs** (M₅'s four eigenline orbits at every λ; M₆'s eight order-8 orbits at λ = ±1). Their polynomials are
   real and their coincidence automatic. Find their positive roots and the case-(b) counts. Prior: they fire like M₄'s. If they do,
   M₅ carries orbits of five and M₆ orbits of six with the opposite sign.
2. **Why Q(q³).** Explain P_{O₂}(q, s) = Q(q³, s): the order-2 twist on the 3-fold cover reproduces the base family at q³. Is there a
   cover or isogeny carrying (s961, ν, ρ_q) to (m004, ρ_{q³}) on the fibre's twisted cohomology?
3. **The reality symmetry.** Prove P_ν = P_ν̄ for every character: the hyperelliptic involution, and ρ_q's invariance under it.
4. **The 5̄′ is still missing on every level.** It needs a building block whose Λ² is not boundary-acyclic (B1509 §5), or the end.
5. **One configuration.** Can the triplet's three vacua be one background? This is B1506's fence, now in the harmonic frame.

## Verification

- `verification/tower_lib.py`: the twisted fibre monodromy, the cover presentations, and the index exactly and over GF(p).
- `verification/controls.py` → `controls_run.txt`: C1–C10, run before the seal.
- `verification/tower_census.py` → `tower_census_run.txt`: the sealed run, Parts A–D.
- `verification/post_run_checks.py` → `post_run_checks_run.txt`: post-run checks (a)–(d).
- `tests/test_b1511_the_projective_tower.py`: the lock.

> **Read against main's S31 (2026-10-01, later the same day; main dfe08803 and d88c220e).**
> - **Main's B1443** (PROVED) computed the orbit's coupling tensor in the Standard-Model frame. Each member of a deck orbit couples
>   only to its own Higgs class, with one strength for the orbit: Y(i, j; k) = y·[i = j]·[η_i = η_k]. So a mass matrix is y·diag(v_k)
>   and members do not mix. On s961 all 16 of B1506's orbits have three distinct Higgs classes for every coupling.
> - **Two corrections by the owner are recorded there.** Copies along a deck orbit are not a blocker; that was an imported expectation.
>   And what fixes the Higgs values is uncomputed, not excluded (main's lead L235).
> - **Applied to §6 above.** "Not three families of one vacuum" and "the three backgrounds are distinct flat bundles" describe what is
>   open: the deck kept (B1506's bit), the 5̄′, and the Higgs values. They are not a limit on the triplet.
> - **Checked here** (own code): on the root's tower the characters of every deck orbit at levels 2–6 multiply to the trivial
>   character. This includes the triplet's three order-2 twists, (2,0) + (0,2) + (2,2) ≡ 0. So a term joining the triplet's three
>   members is allowed by the characters, as main found for the Higgs characters of B1506's orbits. Whether it is non-zero is not
>   computed.
> - **Main's B1444** (sealed, not run) uses the same fibre object as this arc's instrument, the torsion det(1 − Φ* on H¹(F; V)), in rank
>   two along the trace map's curves. It does not overlap this arc's claims.
> - New lead: does each member of the projective triplet couple to its own Higgs class? (OPEN_LEADS, B1511 lead 6).
>
> **Currency (2026-10-01, at B1513's seal).** Main closed L235(a) in S32 (B1444). In main's frame the cubic joining an orbit's
> three Higgs classes has no group to live in: h²(M; k) = 0 on a level, and the pairwise products vanish. The "term joining the
> triplet's three members" above is therefore not a bulk cup product there. Lead 6 is taken by B1513, whose P5 asks whether any
> up-type form joins two members in the harmonic frame. `frontier/B1513_the_triplets_higgs_sector`.

> **Leads 1 and 3 taken (2026-10-01, B1512).** Lead 3: the fibre's hyperelliptic involution fixes ρ_q, so P_ν = P_{ν⁻¹} on every level
> (a theorem now; post-run (c) was its observation). Lead 1: all 32 self-coincident pairs fire, M₅ in four orbits of five and M₆ in
> eight orbits of six, +1 per member at every real exceptional point. Part D's table is complete through level 6 (B1512 §3). Also
> there: the dual family is the family at 1/q, and the strong inversion and the amphichiral map send q to 1/q. This explains §3's
> O_A/Ō_B relation ("as O_A") and M₄'s two classes (class 10 is class 1 at 1/q). `frontier/B1512_the_self_coincident_orbits`.
