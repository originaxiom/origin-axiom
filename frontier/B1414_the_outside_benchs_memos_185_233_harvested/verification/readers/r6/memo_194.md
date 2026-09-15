# Reader r6 — memo 194 (outside_bench/memos/THE_BIT_ASKED.md)

## 1. HEADLINE
"THE BIT, ASKED AT LAST: the object is at zero, and the sister that shares its atom is not."
Dated 2026-09-10. ADDENDUM 1 (same date, owner correction): "ure refering to the object, not the
faces interactions relations and the shadow" — restates the finding at the shadow/face level
rather than the single-manifold level.

## 2. CLAIMS
1. L192 (docs/OPEN_LEADS.md, registered 2026-08-31 by B1226) is answered: the object's CS-mod-½
   channel is bit-valued and every prior probe (B1027, B1137, B813) asked it for a continuous
   value instead — grade: DIAGNOSIS, cited from L192's own text.
2. CELL 1 (non-vacuity): 203,122 one-cusped census manifolds classified; amphichiral manifolds
   land in A[2]={0,¼} at worst distance 2.6e-15 (tol 1e-9); 106 at 0, 75 at ¼ — grade: **B**
   (outcome letter, PASS on all 4 controls C1–C4).
3. CELL 2: m004 sits at CS = 1.35e-16, class 0 — grade: **B**.
4. CELL 3: 59 of the 99 volumes among amphichiral manifolds carry both bit-elements — grade: **B**
   (volume does not predict the bit).
5. CELL 4 / THE FINDING: m003 and m004 are commensurable (index 12, B993), share volume
   2.029883, invariant trace field ℚ(√−3), and V₄ — yet sit at opposite bit-elements — grade:
   **B**, explicitly flagged "this is the finding."
6. Three old box-D negatives (B1027, B1137, B813) are RE-TYPED (not overturned) as asking a
   bit-valued channel for a real number — grade: re-typing, not a new refutation.
7. **ADDENDUM 1 restatement:** across all 181 amphichiral one-cusped manifolds, neither volume
   (59/99 split) nor H₁ abelianization (26/62 types split) nor both jointly (two explicit witness
   pairs: t12062/t12063 same vol+H₁ opposite bit; o10_132112/o10_132113 same vol+H₁ opposite bit)
   determines the bit — grade: **NO** on all three sub-tests, computed exhaustively over the 181.
8. Addendum's tension, explicitly REGISTERED NOT RESOLVED: whether the CS bit is the meeting-leg
   (ℚ(√−15)), a fourth ℤ/2 outside B1276's V₄ indexing, or requires amending B1276's indexing —
   grade: OPEN QUESTION, not answered.

## 3. CERTIFICATE
- `certificates/l192_the_bit.py` exists; `outputs/l192_the_bit_out.txt` exists (both confirmed
  present in `outside_bench/`).
- Seal `seals/L192_THE_BIT_PREREG.md` exists; `shasum -a 256` of that file =
  `969d8bd175b46ae83e22ba6a6d90a515c9d6d73c40fe21ef4bad1fd37a6973b7`, which matches the memo's
  declared sealed hash `969d8bd1` (first 8 hex chars) exactly — **MATCH**.
- Output's tail: "WHAT IS ESTABLISHED. The bit is well defined (C1, worst distance 2.6e-15 over
  181 amphichiral manifolds), non-vacuous (75 of them carry the other element)... not a
  commensurability-class invariant (m003). The object sits at the identity." — this **AGREES**
  with the memo's headline and §4 finding verbatim in substance.
- No separate certificate/output file is named for ADDENDUM 1's follow-on computation (the 181×
  volume/H₁ cross-tabulation) beyond the same certificate+output pair; the numbers quoted in the
  addendum (99 volumes, 62 H₁ types, the two named witness pairs) are not separately re-verified
  against a distinct output file here — this is a gap in the paper trail worth flagging, not a
  contradiction.

## 4. ON MAIN ALREADY?
- L192 itself: (c) NOT ON MAIN as answered. `docs/OPEN_LEADS.md` L192 entry (line 2187) is still
  the original 2026-08-31 registration text with no "CLOSED"/"RUN" annotation; the review-currency
  lines above it (Review 50–52) still read "Next lead: L192" and nothing later marks it resolved.
- Underlying facts cited as background are (a) already on main with citation:
  - B993 commensurability/index-12 finding — `frontier/B993_cornerstone_verified/` exists.
  - B781 "m003 shares trace field ℚ(√−3), volume 2.029883, and V4" — `frontier/B781_m003_sister/`
    exists.
  - B1224 (amphichirality forces CS∈{0,¼}) — `frontier/B1224_amphichiral_cs_torsion/` exists.
  - B1226 (the β-odd box typing) — `frontier/B1226_the_beta_odd_box/` exists.
  - B1027, B1137, B813 (the three re-typed negatives) — `frontier/B1027_fourth_crossing/`,
    `frontier/B1137_regulator_probe/`, `frontier/B813_cs_theta_type_audit/` all exist.
  - B1276 (the three forced V₄ faces: being/hearing/meeting) — `frontier/B1276_legs_are_faces/`
    exists; B730 (`frontier/B730_forced_faces_and_cosmos/`) exists.
  - B1108 (finite-shadow CS claim) — `frontier/B1108_c5_archimedean/` exists.
  - B803 (the commensurability-class typing rule) — `frontier/B803_commensurability_audit/`
    exists.
- The specific NEW claim of this memo — that the 2-torsion CS *bit itself*, asked as a bit rather
  than a value, separates m003/m004 below the commensurability class, and that neither volume nor
  H₁ determines it — is (c) NOT ON MAIN. No frontier arc or docs file was found (grep for
  "l192_the_bit", "A\[2\]", "203 122", "203,122", "t12062", "o10_132112" all zero-hit outside
  `outside_bench/`) that banks this as a B-arc.

## 5. NEEDS COMPUTATION HERE
- Claim 2/C1: recompute over SnapPy's `OrientableCuspedCensus` (one-cusped subset, 203,122
  manifolds) the amphichirality flag and `CS mod ½`; verify every amphichiral manifold's distance
  to {0,¼} is < 1e-9. Expected: worst distance ~2.6e-15, 106 at 0 / 75 at ¼.
- Claim 5 (the finding): recompute CS(m003) and CS(m004) directly in SnapPy/verified-numeric CS,
  confirm m004 → class 0, m003 → class ¼ (or vice versa — the memo doesn't print m003's own class
  value, only "opposite"), and independently confirm commensurability index 12 and shared
  invariant trace field ℚ(√−3) via `snappy.Manifold.invariant_trace_field_gens` or the bench's own
  arithmetic-invariants routine.
- Claim 7 (addendum): recompute the volume-vs-bit and H₁-vs-bit cross-tabulations over all 181
  amphichiral one-cusped manifolds and confirm the two named witness pairs (t12062/t12063 and
  o10_132112/o10_132113) independently — this is the single most load-bearing discriminating fact
  in the addendum (it is what kills "volume+H₁ ⇒ bit" as a complete story).
- Claim 8: DOCUMENTARY (an open question, not a number).

## 6. SUPERSESSION
Not withdrawn by a later outside-bench memo — no memo 195–233 references "memo 194", "L192", or
"the bit" (INDEX.md and owner-register grep both checked; the one register hit, R-line "the
natural successor to memo 194," at THE_OWNER_REGISTER.md:2166, *extends* rather than withdraws it,
naming box D's dictionary question as memo 194's open successor). Not superseded by anything on
main since L192 remains open there. The memo's own ADDENDUM 1 is a self-correction of *framing*
(object-level → face/shadow-level), not a retraction of the §2–§4 numbers, which the addendum
explicitly says stand ("§4 is not withdrawn — it is true and was aimed one level too low").

## 7. GRADE PROPOSAL
**REPRODUCE-AND-BANK** — this is exactly the kind of clean, cheap (SnapPy census sweep),
falsifiable computation the standing rules ask for: it answers a starred (★★★) registered lead
with a non-vacuous, converse-tested finding (47 chiral manifolds at CS=0 kill "bit = chirality
detector"), and the addendum's witness pairs are a sharp, checkable discriminating fact. It should
be banked as a B-arc, L192 marked CLOSED/RUN in `docs/OPEN_LEADS.md` with the finding and its
explicit non-claims (no CP-odd phase value follows; B813 still governs), and the open tension
(§4 addendum, three-way disjunction on which ℤ/2 the bit is) registered as the successor lead
rather than left implicit in an outside-bench file only.
