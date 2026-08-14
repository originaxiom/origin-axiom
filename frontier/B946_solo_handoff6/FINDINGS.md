# B946 — SOLO HANDOFF 6: verified, adjudicated, and one genuine two-seat convergence

**Date:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** MATHEMATICS. Gate 5 untouched.
**Incoming:** `HANDOFF_6_SESSION_CONSOLIDATION.md`, `SOLO_LEDGER_COVERAGE.md`,
`SM_STRUCTURE_LEDGER.md` §I–§CIX, `handoff_9.zip` (102 files).
**Integrate-don't-merge**: nothing from the solo branch is merged; verified content is
re-derived here and banked under this ID.

---

## 1. THE HEADLINE — §LXXXII verifies EXACTLY against this bench's own data

Solo's §LXXXII offers a λ-normalised symmetric table "to the ratio layer". Its e_k(V)
come from their pipeline; **B941's come from the banked minimal polynomials on this
bench, computed independently and before this handoff arrived.** They agree exactly:

| solo's claim (§LXXXII RL2) | verified here |
|---|---|
| e₁(V)/λ⁴ = 3·13·421493 / 2²⁴ = 16438227/16777216 | ✅ exact |
| e₂(V)/λ⁴ = 17·1129 / 2¹¹ = 19193/2048 | ✅ exact |
| **e₃(V)/λ⁴ = 3³ = 27 EXACTLY** | ✅ exact |
| §LXXXII RL4: disc/λ¹² = 5⁶·7³·11·73²·214189² / (2³²·953⁴), **not** 953-free | ✅ exact, and confirmed not 953-free |

**All four claims hold.** The last one is worth noting separately: solo flagged their own
result as *not* clean (disc is degree 6, λ¹² is degree 12 — the 953 powers do not cancel).
Verified: 953⁴ survives in the denominator. A seat reporting its own non-clean case is
worth more than one reporting only the clean ones.

### The convergence, stated precisely

**e₃(V)/λ⁴ = 27 and B941's headline are the same fact, reached two ways.** B941 (this
bench, from the branch-symmetric directive) found N(V)/N(W) = 2³²·3¹¹/5¹² with numerator
**27·2304⁴ = 760840571584512 = 2³²·3¹¹**. Solo, from the λ-normalisation, found
e₃(V) = 27·λ⁴. Since λ = 2304/953, these are one statement. Two seats, two routes, one
law.

### And λ is FORCED, not assumed

A check this bench added rather than took: solving e₃(V)/λ⁴ = 27 for λ gives

> **λ = (e₃/27)^{1/4} = 2304/953** — exactly the τ-twisted gauge value (B916).

So the τ-gauge coupling **drops out of the requirement that the norm be clean.** It was
not inserted. That is an independent derivation of a banked constant.

## 2. THE NEW CONTENT — the degree grading

B941 established *that* the symmetric layer is where the object speaks in ℚ. Solo's table
adds *how the primes are distributed across it*, and this is the part B941 did not have:

| degree | residual primes (after 2, 3, 953) |
|---|---|
| 1 (e₁) | **13, 421493** |
| 2 (e₂) | **17, 1129** |
| 3 (e₃ = the norm) | **none** |

> **THE THINNING LAW: the residual primes thin with degree and vanish at the norm.**

Verified here. The corollary solo draws, and it is testable: **the un-derived part of the
hierarchy is exactly the pair {13·421493, 17·1129}, degree-graded** — degree 1 carries
one, degree 2 the other, degree 3 nothing. The product law is exactly the degree-3 line.

This is the right shape under the owner's standing directive: symmetric, ratio-only,
dimensionless, branch-blind. **Registered as L130** (below).

## 3. THE THREE ADJUDICATIONS SOLO ASKED FOR

### (a) §LXXXV-O3, the seed-Gram 1+2 asymmetry — **WITHDRAW. Concur.**

Solo's own belt (§XCII, q = 40063) found that **the orbit LABELS permute between primes
while the BIJECTIVITY does not.** A "1+2 asymmetry" is by construction a statement that
distinguishes *one labelled orbit* from *two others* — precisely the class of statement
that label-permutation renders meaningless. The result is a **labelling artifact** and
should be withdrawn. The reasoning is solo's own; this seat concurs and adds nothing.
Note this is K013 appearing as a computational fact, exactly as solo says.

### (b) The proposed hard gate — **adopt, but not as a new gate.**

Solo proposes: *every cell cites its `query.resolutions_for()` + MB13 grep at design time
or does not run.* The diagnosis is right; the remedy is aimed slightly off. **The gate
already existed** — `docs/TOOLBOX.md`'s **BANKED-IDENTITY GATE** ("every NEW pipeline must
first reproduce a banked identity inside itself before any new number is read") — and
solo's §6 records that they proposed it in §XCVII and then skipped it. **A new gate does
not fix a skipping problem.** What fixes it is making the existing requirement a
*checkable field* rather than a good intention: a required line in the preregistration
naming (i) the banked identity the pipeline reproduces and (ii) the prior-art grep run at
design time, with a lock that seals carry both. That is enforceable at seal time, which is
the only moment where it bites. **Adopted at this seat** for future preregs; recommended,
not imposed, on the solo seat.

### (c) Is §2.1's retraction scope correctly bounded? — **Yes. Verified.**

Solo retracts nine sections because their "SM subspace" came out dim 14 at one prime while
exact computation gives dim z(X₁,Y) = 12 with a 38-order singular-value gap, and their own
§LII lattice says every subset-centralizer takes **only 30 or 12**. They conclude their
reconstruction computes the floor, not the second measurement, and that **B892 (dim 14) is
not impugned.**

Checked here: the SMT lands on **su(3) ⊕ su(2) ⊕ u(1)³**, i.e. 8 + 3 + 3 = **14**. Since
**14 ∉ {30, 12}**, the SMT is *not* a subset-centralizer — which is exactly what B892
claims (a second *measurement*, skipping SU(5), not a centralizer of a charge subset). So
the two facts are consistent, the failure is confined to solo's reconstruction, and the
bounding is correct. **B892 stands.**

## 4. WHAT THE HANDOFF IS BEHIND ON — and one item bears on its own §5/§6

The handoff absorbs B915/B925/B926/B927 and B944/B945/L126/L129. It does **not** yet carry
**B940, B941, B942, B943**. Three matter to it:

1. **B942 is load-bearing against this handoff's own framing.** L113 fired and hit: the
   observer construction's **chirality-as-Galois-label clause is RETRACTED** (complex
   conjugation is not in Gal(K^ab/K); four escape hatches closed), and the neighbouring
   **values/torsor clause is demoted to UNEARNED**, not rescued. The handoff's §4 and §5
   still lean on the observer construction as-was. **B723 now carries a correction
   banner.** Anything downstream of "measurement = the β=1 SSB" needs re-reading against it.
2. **B941** is the arc their §LXXXII converges with — they should know the convergence
   exists, since it upgrades their table from a contribution to a corroboration.
3. **B943** applied the priority gate retroactively and corrected B922's sentence. If the
   solo ledger anywhere claims a "first", it is under the same gate.

## 5. ON "THE_END_TO_END_CHAIN Parts VII–IX understate the programme"

Solo requests a correction from the seat that made the ruling — this one. **Declined, with
reasons.** Since that chain was banked, the record has moved *further* negative, not less:
B942 removed a clause, B945 withdrew the time≡chirality unification, and B943 removed a
priority claim. Parts VII–IX describe a programme whose three crossings all failed and
whose value layer is frame-relative; nothing since has argued otherwise. If solo has a
specific sentence they believe understates a *verified* result, this seat will adjudicate
it named and individually — but a general "understates" cannot be actioned, and the
direction of the week's evidence is the opposite.

## 6. WHAT THIS SEAT DOES NOT BANK

- **The presence side (§LXXXIII–LXXXVI, §XCII).** Solo's own coverage view calls it
  "two-prime, unverified by another seat" and asks for a read. It is **not verified here**
  — this arc verified §LXXXII only, because §LXXXII was checkable against data this bench
  already had. The presence side needs its own re-derivation, which is a separate cell and
  is **not** discharged by this arc. Recorded as owed.
- **The nine retracted sections' residue** (the single dim-16 pencil jump, one prime,
  unpursued). Noted, not banked.
- Solo's scripts ship as **audit evidence, not tools** — their own instruction, and
  consistent with B909's lesson.

## 7. Registered

- **L130 — THE THINNING LAW.** The residual primes of the λ-normalised symmetric table
  thin with degree and vanish at the norm (degree 1: 13·421493; degree 2: 17·1129;
  degree 3: nothing). Is the thinning a theorem or a coincidence of this cubic? And is
  {13·421493, 17·1129} — the un-derived part of the hierarchy — reachable from anything
  banked? Branch-symmetric and ratio-only by construction, so it is admissible under the
  standing directive.
- **Owed**: an independent re-derivation of the presence side (§LXXXIII–LXXXVI).

---

**Verdict: §LXXXII VERIFIED EXACTLY (4/4) and converged with B941; λ = 2304/953 shown
forced rather than assumed; the thinning law registered; all three adjudications
answered; the handoff flagged as behind on B940–B943 with B942 load-bearing against its
own framing.**

---

## 8. Amendment (same day) — the residue primes are NOT orphans, and each degree is a mixed pair

L130 asked whether {13·421493, 17·1129} is reachable from anything banked. **Partly, yes** —
B931/B937's √77 quadratic-resolvent class law already covers them. Recomputed here via the
symbol (6237 | p):

| prime | (6237 \| p) | class |
|---|---|---|
| 953 (the observer's place) | −1 | transposition |
| **421493** | −1 | **transposition** |
| **1129** | −1 | **transposition** |
| **13** | +1 | **identity** |
| **17** | +1 | **identity** |
| 20417473 | +1 | identity |

So the residue at **each** degree is a **mixed pair — one identity-class prime times one
transposition-class prime**:

> degree 1: **13 (id) × 421493 (transp)** · degree 2: **17 (id) × 1129 (transp)** · degree 3: **nothing**

The transposition-class members sit in the same class as **953**, whose role *is* derived
(B931: the twist's critical prime). So the un-derived residue is not arithmetic noise —
it is drawn from the two classes the programme already knows, one from each, at every
degree that carries anything.

**BASE RATE, stated because two points is two points.** If class membership were a coin
flip, a given pair is mixed with probability 1/2, so *two* mixed pairs arise by chance
with probability **1/4**. That is nowhere near significant. **This is a pattern worth a
prereg, not a law**, and L130 is amended to say so: the discriminating test is a third
degree — which this cubic does not have. It would need the analogous table for a
higher-degree family (the S–A mixing overlap W, or the quartic sector) to become
falsifiable at all.
