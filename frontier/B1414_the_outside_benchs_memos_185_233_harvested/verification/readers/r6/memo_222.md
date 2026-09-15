# Reader r6 — memo 222 (outside_bench/memos/KMRT_ARRIVES.md)

## 1. HEADLINE
"KMRT ARRIVES: the record's most load-bearing unverified claim HOLDS, and the object's algebra is
SPLIT." Banked 2026-09-13 (INDEX.md). No addendum to this memo itself.

## 2. CLAIMS
1. CELL 1: KMRT §43.C's own definition types the object's cubic K=ℚ[x]/(x³−12x−5) as **⁶D₄**
   exactly (fails ¹D₄, ²D₄, ³D₄ clauses; satisfies only the ⁶D₄ clause via K⊗Δ = degree-6,
   6-automorphism, non-abelian ≅ S₃) — grade: **A**. This directly **REFUTES B882's ³D₄ naming**
   by definition, not by a search summary.
2. CELL 2: no cyclic-composition generator ρ exists over K (#Aut(K/ℚ)=1); KMRT §36.C's descent
   construction Γ(C,L) is the correct replacement — grade: **A**.
3. CELL 3: memo 204's pinned commutant "(77,b)_K, b unknown" is fixed by KMRT Thm 43.8/Prop 43.9
   as Q=(a,77)_K with a∈K×, N_{K/ℚ}(a)=1 — grade: **A**.
4. CELL 4: exhaustive search over 342 admissible a=x³/N(x) found 0 non-split (a,77)_K — grade:
   **B**, explicitly labelled "NOT-FOUND over a stated family, never a proof of nonexistence."
5. CELL 6 (NOT preregistered, filed post-hoc under seal ADDENDUM 1 per standing rule R121): n_p
   (primes above p where 77 is a non-square in K_w) is exactly ≤1 for every rational prime,
   because K(√77) is K's own Galois closure; combined with KMRT Prop 43.6 (corestriction-additivity
   forcing an even ramification count) this **proves E is SPLIT** — grade: **A**, and flagged as
   THE RESULT.
6. Control C6: replacing 77 by generic b (5,13,33,−1,3) reaches the theoretical max n_p=3 in every
   case, showing n_p≤1 is a property of 77-as-discriminant-square-free-part, not the instrument —
   grade: PASS, interpretive conclusion labelled as such.
7. CELL 5: BENCH ERROR #29 — the standing citation "KMRT Ch. VII §43/§44.B" has the wrong chapter
   number (actually Ch. X for §43/44, Ch. VIII for §36); section numbers were right — grade:
   logged error, does not affect downstream use.
8. Operational: 4 silent GP/PARI subprocess failures (all exit 0) caught, one only because it
   contradicted Chebotarev — grade: process note, RULE ADDED (#25).

## 3. CERTIFICATE
- `certificates/kmrt_arrives.py` exists; `outputs/kmrt_arrives.txt` exists (both confirmed).
- Seal `seals/KMRT_ARRIVES_PREREG.md` exists; `shasum -a 256` =
  `8a936c7709deed8892998a1acd5f62cb892dff944fe227aa74f6c3ce49833dba`, matching the memo's declared
  post-ADDENDUM-1 hash exactly — **MATCH**.
- Output's tail: "CELL 1 (KMRT types the object 6D4): A / CELL 2 (no cyclic composition over K): A
  / CELL 3 (memo 204's pin is the normal form): A / CELL 4 (classification decides E?): B /
  CELL 5 (the bench's citation): A / CELL 6 (could it have differed?) NOT PREREG: A" plus "C1–C7"
  all PASS/N/A — **AGREES** with the memo's own cell table verbatim.
- The source PDF (KMRT draft, sha256 `e3d1e114...ddf`) is not committed to the repository; its
  hash is stated in the memo but not independently re-verifiable from this bench without the file.

## 4. ON MAIN ALREADY?
- **(d) DISPUTED — this is the important one.** `frontier/B1077_intrinsic_split/FINDINGS.md`
  (verdict PROVED, dated 2026-08-19, still the live verdict — `superseded_by: null` in its
  `arc_verdict.json`) states, in its own "FLOOR-LIFT" section: *"ℚ(√77) can only enter through the
  twisted **³D₄** form, where the cubic étale algebra is a field... B882's conjecture is therefore
  stateable in KMRT's own language: the dressed datum is the **³D₄** twist of the split triple by
  K."* Memo 222 CELL 1, reading the actual primary source verbatim, proves this naming is wrong:
  K is non-cyclic (fails the ³D₄ clause, which requires a cyclic cubic) and the correct type is
  **⁶D₄**. Main's B1077 (PROVED, unretracted) and this memo directly contradict each other on the
  D₄-type label. `grep -rl "6D4|⁶D₄"` over frontier/docs/papers returns **zero hits** — the
  correction has not propagated to main at all.
  - Note: `frontier/B1413_.../DOC_RELAY_TRIAGE_2026_09_12.md:18` records that a *different*
    outside-bench memo (204, `THE_OBJECT_IS_6D4.md`) "explicitly reproduces B1077 and withdraws
    the apparent conflict: the bare octonion norm and the dressed centralizer are different
    objects" — i.e. B1077's *intrinsic-layer* split-triple theorem is not in conflict with the
    *dressed* object being ⁶D₄. But B1077's own text still names the dressed twist "³D₄", which is
    the specific label memo 222 shows is wrong. The reconciliation-of-scope is on main; the
    corrected label is not.
- B882 (`frontier/B882_magic_square_naming/`, verdict PROVED) does not itself state a D₄ type in
  its FINDINGS.md/arc_verdict.json (checked directly — no "D4" string present); the ³D₄ naming
  that memo 222 refutes lives specifically in B1077's floor-lift addendum, not in B882's own text.
  So "B882's ³D₄ naming is refuted" (memo 222's own phrasing, inherited from memo 204) is more
  precisely a correction to **B1077**, not to B882 itself.
- Memo 204 (`THE_OBJECT_IS_6D4.md`, the outside-bench predecessor this memo verifies) is not a
  B-arc and is not on main; only its downstream effect (the DOC_RELAY_TRIAGE note above) is
  referenced from a main-tracked file.
- CELL 5's chapter-number fix and CELL 4's not-found search are (c) NOT ON MAIN (no chapter-number
  citation of KMRT exists on main to correct, and the 342-sample search itself is bench-internal).

## 5. NEEDS COMPUTATION HERE
- Claim 1 (the ⁶D₄ typing — the discriminating fact for the DISPUTE): recompute, from K's minimal
  polynomial x³−12x−5, that (i) it is irreducible over ℚ, (ii) disc(K) (=6237, per the memo) is
  not a perfect square (so #Aut(K/ℚ)=1, K non-cyclic — refuting ³D₄), and (iii) the resolvent
  sextic K⊗Δ = x⁶−30x⁴+225x²−308 has Galois group of order 6 and is non-abelian (i.e. ≅ S₃, hence
  ⁶D₄ under KMRT §43.C's own clause). All three are one-liners in sympy/PARI-gp and do not require
  the KMRT PDF itself — only its quoted definition, which is reproduced verbatim in the memo. This
  is the fact a verifier should recompute to adjudicate the B1077-vs-memo-222 dispute.
- Claim 5 (E is split): recompute disc(K(√77)) = 3⁸·7³·11³ and confirm ramification only at 3,7,11
  (each n_p=1); recompute the Frobenius-class/n_p table for p<500 and confirm n_p≤1 always; this
  is a from-scratch PARI/sympy number-field computation, independent of the KMRT source.
- Claim 6 (control C6): recompute n_p for b∈{5,13,33,−1,3} and confirm each reaches max 3 — cheap,
  discriminating (shows 77 is special because it IS disc(K)'s squarefree part).
- Claim 4: DOCUMENTARY-adjacent (a negative search result); recomputing the 342-sample sweep is
  optional confirmation, not required since it is explicitly not claimed as a proof.

## 6. SUPERSESSION
No later outside-bench memo revisits KMRT/⁶D₄/memo 222 by name (INDEX rows 223–233 and owner
register scanned; the register's own hits at lines 4079/4159/4170/4175/4203 all *cite* memo 222
approvingly as the closing word on the KMRT question — "there is no outstanding literature ask on
this bench" — none retract it). Not superseded on main, since main has not yet incorporated the
correction at all (see §4 DISPUTED).

## 7. GRADE PROPOSAL
**DISPUTED** — main's `frontier/B1077_intrinsic_split/FINDINGS.md` (PROVED, unretracted) names the
dressed object's twist type "³D₄"; this memo, reading the primary source (Book of Involutions
§43.C) verbatim, computes that K is non-cyclic and the correct KMRT type is "⁶D₄", making B1077's
label wrong on its own terms. This should not be buried: B1077 needs either an ADDENDUM correcting
"³D₄"→"⁶D₄" throughout its floor-lift section, or an explicit adjudication of why the outside
bench's primary-source reading doesn't apply. The memo's harder result (E is split, CELL 6) is a
clean, independent, reproduce-and-bank-worthy number-theory computation that does not depend on
resolving the naming dispute.
