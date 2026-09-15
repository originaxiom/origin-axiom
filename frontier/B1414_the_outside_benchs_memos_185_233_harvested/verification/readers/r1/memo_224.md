# Reader r1 — Memo 224 (THE_FIRST_AXIOM.md, + Addendum 1)

## 1. HEADLINE
"THE FIRST AXIOM: THE THEOREM IS REAL, IT IS ON MAIN, IT PRICES RATHER THAN DISCHARGES — AND
A3 IS EXACTLY THE SQUARING." CELL 1=A, CELL 2=A, CELL 3=A, CELL 4=A; C1–C4 all PASS. Date
**2026-09-13**; Addendum 1 dated **2026-09-13** (same day, later).

## 2. CLAIMS
1. CELL 1: the owner's remembered "figure-8-only-with-cusp" theorem = fork F9 / **B1323**,
   banked on `origin/main` **2026-09-09**. Grade: **A** — but see §6, **SUPERSEDED by
   Addendum 1**: this identification is **WRONG**.
2. F9's discriminator table: 2 records→`ℤ²`→**m004**, ONE cusp, ℚ(√−3); 3 records
   (surface)→**Whitehead link (m129)**, TWO cusps, ℚ(i); 3 records (toral)→no hyperbolic
   structure (χ=0 for T³-bundles vs χ=3Vol/4π²>0 for hyperbolic). Grade: **quoted from B1323,
   accurate**.
3. CELL 2: F9 **PRICES** A1, does not discharge it — B1323's own fence quoted verbatim ("A1–A7
   are not derived from anything weaker"; reach = "words of length 3"). Grade: **A — axiom
   count stays 4, price stays 12**.
4. §3: an unmerged branch (`physics-seat-evaluation-8dkbrl`, cell T5_a6_audit) proposes
   re-typing orientation as "closing #0," which would move the count 4→3 (price 12→11);
   its one recorded missing datum: "A1,A2,A4–A6 WITHOUT A3 force M up to the swap... NOT
   computed anywhere in the record." Grade: **DOCUMENTARY report of a branch finding,
   proposed only, not landed**.
5. CELL 3: enumerating `{L,R,S}` (det ±1) to length 4: with A3 (det+1) global min `|trace|=3`
   at `A=LR=[[2,1],[1,1]]`, dilatation φ²; **without A3** (det±1) global min is `|trace|=1` at
   **det=−1**, attained by `M=L·S=[[1,1],[1,0]]`, one class up to the A7 swap, `M²=LR=A`
   exactly, `char(M)=t²−t−1` (golden ratio). Grade: **A — "A3's entire matrix-level content
   is that it replaces the golden matrix by its square."**
6. CELL 4 (control): the same enumerator restricted to det=+1 reproduces UNIQUENESS_THEOREM
   §3's banked `A=LR`, `|trace|=3` first, before trusting CELL 3. Grade: **A, control**.
7. Controls C1 (Anosov test bites both ways at det=−1, correctly), C2 (torsion-formula
   144-point grid reproduced with zero mismatches), C3 (manifold ID — M's mapping torus is
   Gieseking m000 — explicitly **INHERITED**, not recomputed, no SnapPy claim made), C4 (all
   quotations located; one typographic-quote bug caught and recorded, not silently fixed).
8. §6: two things flagged from the branch sweep — (a) `codex/seat-r001`'s **OA-C1103
   REFUTED** (H₁=ℤ does not uniquely isolate m004 in the corrected 112-member ℚ(√−3) cusped
   family; `o10_150700` is a counterexample) and **OA-C1134 OPEN** (two numerical near-ties on
   cusp shape, awaiting an exact certificate); (b) F9's registered successor, FRESH_EYES **Q15**
   ("is there a carrier that keeps the atom and remembers the bit?" — none found).
9. Addendum 1: §1's identification is **SUPERSEDED** — the owner's theorem is actually
   **Jørgensen's inequality (1976) + Callahan (2009) Cor. 2.4**, memo 225, on arc **B1345**
   (dated 2026-09-12), which the addendum describes as "on a branch"
   (`<remote>/paper-verification-ufp0zn`). "Everything else in this memo stands." A second,
   independent confirmation of CELL 3 is claimed: dropping A3 gives `M`, mapping torus **m000**,
   and memo 225 finds `J=1` holds for **both** m000 and m004 — "a GL(2,ℤ) monoid enumeration
   and a 1976 discreteness bound select the same pair {m000,m004}." What changes about the
   axioms: Jørgensen+Callahan discharge A1,A2,A4,A5,A6 given orientability — "far more than
   F9's pricing of A1" — but leave orientation (and memo 223's price of 12) untouched.

## 3. CERTIFICATE
- `certificates/the_first_axiom.py` + `outputs/the_first_axiom.txt` — **both EXIST**. Tail
  matches headline exactly: "THE AXIOM COUNT IS UNCHANGED BY THIS CERTIFICATE: 4 axioms, price
  12," all four CELL outcomes = A, all four controls PASS, including the C3 "labelled
  INHERITED, no SnapPy identification claimed" language reproduced near-verbatim.
- Seal: `seals/THE_FIRST_AXIOM_PREREG.md`, sha256 quoted in the memo as
  `f44223389d9f09861ed61cad19168e6f5149797f42652920c2f67f9f0b4da250` — **matches** `shasum -a
  256` of the actual seal file exactly (verified: identical 64-hex-char string), and the memo
  states it was "COMMITTED BEFORE THE CERTIFICATE WAS WRITTEN." No addendum changed this seal.

## 4. ON MAIN ALREADY?
- **(a) already on main**: B1323 (`frontier/B1323_the_genesis_upgrades/FINDINGS.md`, banked
  2026-09-09) is exactly as described — F9 "ROBUST twice," the substrate-count discriminator
  table, and the explicit fence "A1–A7 are not derived from anything weaker... words of length
  3." `docs/UNIQUENESS_THEOREM.md:25` carries A1 verbatim ("Two-record substrate... Not one;
  not three."). `docs/THEOREM_LEDGER.md:64` already carries a dated 2026-09-09 addendum
  crediting B1323 with the dictionary lemma.
- **Important nuance — CELL 3's "NOT computed anywhere in the record" claim is questionable**:
  `frontier/B1323_the_genesis_upgrades/FINDINGS.md:75` (same arc, same date, **on main four
  days before this memo**) already states: *"the Fibonacci morphism a↦ab, b↦a has matrix
  [[1,1],[1,0]] = L·P (det −1: A2 without A3); orientation (C5≡A3) forces the square:
  (LP)²=LR=A ... PLP=R"* — this is the **identical matrix** (memo 224 calls the swap `S`
  where B1323 calls it `P`) and the **identical squaring identity** `M²=LR=A` that memo 224's
  CELL 3 presents as new. What CELL 3 actually adds beyond B1323 is the **exhaustive
  minimality argument** (that this class is the forced GLOBAL MINIMUM `|trace|` over ALL
  `{L,R,S}` words at det=±1, not merely an exhibited example via the Fibonacci-morphism
  route) plus the bidirectional Anosov control. The T5-audit's claim (quoted at face value in
  §3) that this datum is "NOT computed anywhere in the record" is **only true of the
  minimality/uniqueness framing**, not of the underlying matrix identity, which was already
  on main. This is not a contradiction of memo 224's result, but the memo's own characterization
  of the gap somewhat overstates novelty; a verifier should not read CELL 3 as discovering
  `M²=A` for the first time.
- **(c) NOT on main / STALE at time of writing**: the T5_a6_audit branch content itself
  (`physics-seat-evaluation-8dkbrl`) — grep for `T5_a6_audit` or "A6 RELABELING" outside
  `outside_bench/` returns no hits; it remains unmerged, exactly as the memo states.
- **(d)/corrected — Addendum 1's own branch attribution is STALE**: `frontier/
  B1345_the_jorgensen_number/FINDINGS.md` **is on `origin/main`**, landed by commit `83cb185a`
  dated **2026-09-12** — i.e. **one day before** Addendum 1 (2026-09-13) was written
  describing it as "on a branch" (`<remote>/paper-verification-ufp0zn`). By the time this
  reader checked (repo HEAD, 2026-09-16), B1345's content (Jørgensen J(m004)=1, Callahan Cor.
  2.4, the m000/m004 Gieseking-double-cover relationship, the slack table) is fully present on
  main, seat "cc," and matches Addendum 1's description closely (including the m000/m004
  volume-doubling and orientability point). **This is not a contradiction of memo 224's
  math, only of its "on a branch" framing** — worth flagging so a later reader doesn't
  re-search branches for something already on main.
- CELL 4's control (reproducing UNIQUENESS_THEOREM §3's `A=LR`, trace 3) matches
  `docs/UNIQUENESS_THEOREM.md`'s own banked content exactly.
- The paper sentence quoted in C3 ("The squaring is not cosmetic: it is the orientation
  axiom...") is confirmed present verbatim at `papers/P3_THE_PAPER/main.tex:391`.
- `docs/THE_SM_VERDICT.md:62-76` already carries the "4 axioms + 14 unearned = 18 rows...
  4+8=12 irreducible... 0 of 19" figures this memo's §1 (per the owner-register R133-1 entry)
  describes fixing — **confirmed on main**, credited there to **memo 223**, not memo 224.

## 5. NEEDS COMPUTATION HERE
1. Claim 5 (CELL 3, the without-A3 enumeration): re-run a finite word enumeration over
   `{L,R,S}` (det ±1) to length 4, apply the torsion-free-closure test `|det(B−I)|=1` and
   minimal-`|trace|` selection; expect global minimum `|trace|=1` at det=−1, exactly two
   matrices, conjugate by `S` (the A7 swap), and `M²=LR=A` exactly. This is the one item on
   main that should be spot-checked against B1323's `verification/u3_dictionary.py` (which
   has the same `L·P` identity) to confirm they agree.
2. Claim 6 (CELL 4 control): same enumerator, restricted to det=+1; expect `A=LR`, `|trace|=3`,
   reproducing `docs/UNIQUENESS_THEOREM.md` §3 exactly.
3. Claim 9 (Addendum 1, J=1 for both m000 and m004): recompute Jørgensen's number
   `J = |tr²A−4| + |tr[A,B]−2|` minimized over SnapPy geometric holonomy word pairs for m000
   and m004; expect J=1 for both (per B1345's own computation, already on main —
   `frontier/B1345_the_jorgensen_number/verification/b1345_j_of_m004.py`).
4. Seal check (already done above): `shasum -a 256 outside_bench/seals/THE_FIRST_AXIOM_PREREG.md`
   — CONFIRMED to match the memo's quoted hash exactly.

## 6. SUPERSESSION
- Memo 224's own §1 identification (that F9/B1323 is the owner's remembered theorem) is
  **explicitly SUPERSEDED by its own Addendum 1** (same day, 2026-09-13; memo 225 makes the
  correct identification: Jørgensen + Callahan, arc B1345). The memo itself states "Everything
  else in this memo stands" — CELL 3's computation and its conclusion (A3 = squaring) are
  **not** retracted by the addendum, only reinforced with a second independent route.
- No later INDEX.md row (through 224, the end of r1's assignment) or owner-register entry
  retracts CELL 3's computation itself.
- Owner register `R133` (`outside_bench/THE_OWNER_REGISTER.md:4326`) records the same content
  as the base memo verbatim, confirming provenance.

## 7. GRADE PROPOSAL
**REGISTER**, with one **DISPUTED-adjacent flag, not a true dispute**: the memo's headline
computation (CELL 3, "A3 is exactly the squaring") is sound and cheap to reproduce
(finite word enumeration), but (i) its claim that the underlying `M²=A` identity was "NOT
computed anywhere in the record" is contradicted in substance (not conclusion) by
`frontier/B1323_the_genesis_upgrades/FINDINGS.md:75`, already on main four days earlier with
the identical matrix and identity under different names (`P` vs `S`); and (ii) Addendum 1's
"on a branch" attribution of the Jørgensen/Callahan theorem (B1345) is now stale — B1345 has
been on `origin/main` since 2026-09-12, predating even the addendum that called it unmerged.
Neither issue changes the arithmetic; both are provenance/currency corrections a harvest pass
should make when citing this memo.
