# Reader r1 — Memo 200 (THE_Z2_SLOTS_ARE_FULL.md)

## 1. HEADLINE
"THE ℤ/2 CENSUS HAS ONE KIND IN IT, AND THAT KIND'S SLOTS ARE FULL" — CELL 1/2/3 = B/B/B,
four controls all passing. Date **2026-09-11**.

## 2. CLAIMS
1. The existing census (B1174 NEGATIVE, B1276 PROVED, B1041 PROVED) is **sound and not
   rebuilt** — reproduced "as far as it is used." Grade: **reproduced, not new**.
2. `Hom(V₄, ℤ/2)` enumerated by brute force = **4 elements, 3 non-trivial** (control C1).
   Grade: **PROVED (trivial group-theory fact, exact)**.
3. B730/B1174's three named Galois legs (being=c/ℚ(√−3), hearing/ℚ(√5), meeting/ℚ(√−15))
   are exhibited AS exactly those 3 non-trivial homomorphisms of the meeting V₄ =
   Gal(ℚ(√−3,√5)/ℚ) — i.e. **that kind's slots are FULL, by counting**. Grade: **B (exact)**.
4. Parity law (`c` acts on a quadratic field iff imaginary) reproduced **4/4** on all three
   faces plus B1276's off-face control ℚ(√−7) (control C2). Grade: **reproduced**.
5. §8's relational bit `D=(2−κ)/g²` runs over `{-181,-29,-19,-1,+1,5,11}` with B1248's `A_OBJ`
   fixed — **a bit ONLY on the sub-locus |D|=1**; off it, a torsor with no distinguished pair.
   Control C3 confirms the classifier can return a genuine ℤ/2. Grade: **NEGATIVE / exact
   scoping, not a refutation of §8** (memo says §8 itself "does not overclaim").
6. The Chern–Simons bit `A[2]={0,¼}⊂ℝ/½ℤ` is genuinely two-valued and **independent of `c`**:
   m003 and m004 are both amphichiral, equal volume (2.029883213), yet sit at CS=¼ vs 0.
   Across L192's banked census (203,122 manifolds, control C4): **181 amphichiral, 106 at 0,
   75 at ¼**. Grade: **B (exact); "amphichirality forces membership in A[2], not which
   element"**.
7. Synthesis: the record carries **at least three KINDS** of ℤ/2 — (a) Galois legs (3 slots,
   full), (b) square classes of a pair (2-valued only on a sub-locus), (c) value-group torsion
   (2-valued, independent of (a)). Grade: **REGISTER (typing claim, no new number)**.
8. Explicitly stated non-claims: does not move any freedom-ledger row; does not claim the
   list of kinds is complete (only "at least three, exhibited"); does not weaken B1174/
   B1276/B1041. Grade: **documentary scope statement**.

## 3. CERTIFICATE
- `certificates/the_z2_slots_are_full.py` — **EXISTS**.
- `outputs/the_z2_slots_are_full_out.txt` — **EXISTS**. Tail matches the memo's own closing
  paragraphs near-verbatim, including the three-kinds table and "Gate 5 untouched. No
  measured value is used or named," agreeing with the headline.
- No seal named for this memo.

## 4. ON MAIN ALREADY?
- **(a) already on main**: B1174 (the ℤ/2-identification NEGATIVE), B1276 (PROVED, legs=faces
  + parity law) and B1041 (PROVED, one cube at direction level) all exist on main
  (`frontier/B1174*`, `frontier/B1276*`, `frontier/B1041*` — confirmed present in repo tree
  structure referenced throughout `frontier/`); memo 200 explicitly reproduces these rather
  than claiming them new.
- **(c) NOT on main**: the explicit three-kind typology (Galois leg / square class / value-
  group torsion) and the specific claim "that kind's slots are FULL by counting" — grep for
  "three kinds ... Z/2", "kinds of Z/2" and similar across `docs/` and `frontier/*/FINDINGS.md`
  returns no hits outside `outside_bench/`.
- B1327 (`frontier/B1327_relation_not_observer/FINDINGS.md`), the memo's stated occasion, IS
  on main — but the typing answer memo 200 supplies to B1327's worry is not.
- The m003/m004 Chern–Simons datum (CS = ¼ vs 0, equal volume 2.029883213, both amphichiral)
  and the L192 census split (181 amphichiral: 106 at 0 / 75 at ¼) were not found cited
  verbatim outside `outside_bench/` in this search; likely computed fresh from the bench's own
  L192 census (an outside-bench artifact) rather than reproduced from a main arc.
- No contradiction with main found.

## 5. NEEDS COMPUTATION HERE
1. Claim 2 (`Hom(V₄,ℤ/2)` = 4, 3 non-trivial): trivial GAP/sympy group-theory enumeration —
   DOCUMENTARY-adjacent but a one-line check; expected 4/3.
2. Claim 6 (CS(m003)=¼, CS(m004)=0, equal volume): `snappy.Manifold('m003').chern_simons()`
   and `.volume()`, likewise for `m004`; expected CS m003 ≈ 0.25 (mod ½), m004 ≈ 0, volumes
   equal to ~10 digits (2.029883213).
3. Claim 6's census split (181 amphichiral in L192's 203,122-manifold sample, 106 at CS=0,
   75 at CS=¼): re-run L192's own census script (owned by this bench, cited as "banked") over
   the same population and recount the CS(2) split; expected 106/75 exactly if reproducing the
   same fixed population, otherwise DOCUMENTARY (population-dependent, needs the L192 seed).
4. Claim 5 (D-torsor values `{-181,-29,-19,-1,+1,5,11}`): recompute `D=(2−κ)/g²` over B1248's
   named partner set with `A_OBJ` fixed; DOCUMENTARY unless the exact generating set of
   partners is reproduced from B1248 — recipe: pull B1248's partner list and re-evaluate D.

## 6. SUPERSESSION
No later INDEX.md row or owner-register addendum found that withdraws or supersedes memo
200's headline. It explicitly states it does not retract any of B1174/B1276/B1041, and no
arc on main is found to contradict or supersede its typology claim.

## 7. GRADE PROPOSAL
**REGISTER** — this is chiefly a documentary/typing memo (no new headline number; its two
"new" numeric facts, the D-torsor set and the CS(2) 106/75 split, both reproduce this bench's
own prior censuses rather than compute anything fresh). Worth a ledger row citing the
three-kind typology, but not itself a computation needing independent re-verification beyond
the cheap sanity checks in §5.
