# Reader r6 — memo 225 (outside_bench/memos/THE_JORGENSEN_NUMBER.md, incl. ADDENDUM 1)

## 1. HEADLINE
"JØRGENSEN: the theorem the owner meant, and it is stronger than the one I found." Banked
2026-09-13 (INDEX.md). **ADDENDUM 1 (same date, filed as memo 226): "§4's AXIOM CONCLUSION IS
WITHDRAWN."** The headline's central number (J(m004)=1) survives; the axiom-discharge conclusion
built on it does not.

## 2. CLAIMS
1. Correction to memo 224: the owner's "theorem about figure 8 being only with cusp that fixes
   first axiom" is Jørgensen's inequality (1976) + Callahan (2009) Cor. 2.4, banked on a branch as
   arc **B1345** (`<remote>/paper-verification-ufp0zn`, dated 2026-09-12) — not fork F9/B1323 as
   memo 224 first guessed — grade: CORRECTION, memo 224's own findings otherwise stand.
2. J(m004) = 1 **exactly, with no search**: relator `aWb⁻¹W⁻¹` (W=ba⁻¹b⁻¹a) verified = +I, `tr a`=2
   (parabolic ⇒ `|tr²a−4|`=0 exactly), κ=tr[a,b]=u²+2, κ−2=u² a primitive cube root of unity,
   `|κ−2|`=1 exactly ⇒ J≤1 (upper bound from the pair) and J≥1 (Jørgensen's inequality) ⇒ J=1 —
   grade: **exact computation**, not disputed by the addendum.
3. The record already banked `|κ−2|=1` under the name "the unit obstruction" (HINT_LEDGER H96;
   B1200) without knowing it was the saturation of Jørgensen's 1976 bound — grade: reproduced
   finding (credited to B1345), not re-derived independently here.
4. §4 (**WITHDRAWN by ADDENDUM 1**): the theorem discharges UNIQUENESS_THEOREM's A1, A2, A4, A5,
   A6, leaving only orientation — grade: **WITHDRAWN**. The corrected accounting (ADDENDUM 1,
   filed as BENCH ERROR #32): a Jørgensen group is by definition **two-generator**, so the theorem
   *assumes* A1 (and A2/A3 via the PSL(2,ℂ) hypothesis) rather than deriving it; only A4, A5, A6
   are genuinely discharged — **three of six, not five**.
5. J=1 selects the pair {m000, m004} (m000 = the Gieseking manifold, non-orientable); orientation
   picks m004 out of the pair — the same fork memo 224 found from the GL(2,ℤ) monoid side
   (M=L·S, M²=A, mapping torus m000) — grade: reproduced/cross-checked finding, unaffected by the
   addendum's withdrawal.
6. Scope stated: Callahan cited not re-proved; m000's J=1 is inherited from B1345, not recomputed
   here (m000's holonomy is not in PSL(2,ℂ)); whether {m000,m004} is the *complete* J=1 set is not
   established — grade: explicit non-claims.
7. **ADDENDUM 1's own positive re-verification**: J(m004)=1 reproduced a *second, independent* way
   from SnapPy's own (non-parabolic-generator) holonomy, minimised over Nielsen-move pairs, giving
   1.000000000000; and **323 two-generator census manifolds scanned, exactly one (m004) reaches
   1** (m009 at √2, m129/Whitehead link at exactly 2) — grade: **independently verified**,
   uniqueness now tested rather than only cited from B1345.

## 3. CERTIFICATE
- `certificates/the_jorgensen_number.py` exists; `outputs/the_jorgensen_number.txt` exists (both
  confirmed).
- No seal (the memo states this explicitly: "exact arithmetic in ℤ[ζ₆]... plus one literature
  theorem cited and labelled as cited") — no seal file to check.
- Output tail: "kappa - 2 = u^2, a primitive cube root of unity, |kappa - 2| = 1 : exact / J(m004)
  = 1, from the pair (a,b) plus Jorgensen's inequality : exact + cited / the record banked this
  number as 'the unit obstruction' : verified on main / the uniqueness theorem needs ORIENTABLE,
  and m000 also has J = 1 : cited/inherited / C1 non-vacuity : PASS" — **AGREES** with the memo's
  §2–§5 exactly; the output itself does not print an axiom-count line, consistent with §4 having
  been the interpretive layer that ADDENDUM 1 later withdrew (the output was never wrong; the
  memo's prose conclusion was).

## 4. ON MAIN ALREADY?
- **(a) ALREADY ON MAIN, and more current than the memo believed.** `frontier/B1345_the_jorgensen_number/`
  exists and is committed to main (`git log`: commit `83cb185a`, 2026-09-12; confirmed
  `git merge-base --is-ancestor` of current HEAD `3857877d`, 2026-09-15 — **it IS on origin/main
  now**, even though this outside-bench memo describes it as living only on
  `<remote>/paper-verification-ufp0zn`). This is a currency gap, not a contradiction: B1345 landed
  on main the day after this memo's original body was written (2026-09-12→2026-09-13) or shortly
  after; a re-reader of this memo today should know B1345 no longer needs branch-fetching.
  - `frontier/B1345_the_jorgensen_number/FINDINGS.md:29`: "J(m004) = 1.000000000000000, attained
    at (ab, ba)..." — matches claim 2 exactly.
  - `FINDINGS.md:103`: "Nine of eleven reproduce exactly: m000 1, m004 1, m009 √2, m136 2√2,
    m003 4..." — matches claim 5's slack-table quote exactly.
  - `FINDINGS.md:116-117`: "m000 at J = 1 is not a counterexample to uniqueness — it is the
    hypothesis working. m000 is the Gieseking manifold: non-orientable..." — matches claim 5.
  - Checked directly: B1345's FINDINGS.md does **not** itself claim the A1/A2/A4/A5/A6
    axiom-discharge overreach that this memo's original §4 made and later withdrew (grep for
    "A1", "A2", "A4", "A5", "A6", "discharge" in B1345's FINDINGS.md returns no such claim) — so
    main's own B1345 was already more careful than this memo's first pass, and there is **no
    dispute** here, only an outside-bench self-correction that converges with what main already
    had right.
- `docs/UNIQUENESS_THEOREM.md` exists on main and defines A1–A6; not independently re-read here
  line-by-line, but its existence confirms the axiom labels (A1, A2, A4, A5, A6) used by both the
  memo and B1345 refer to a real, checkable main document.
- `docs/HINT_LEDGER.md` H96 and `frontier/B1200_one_polynomial/FINDINGS.md:17` both confirmed on
  main with the "unit obstruction" / `|κ−2|=1` language quoted — **(a) exact match**.

## 5. NEEDS COMPUTATION HERE
- Claim 2 (J(m004)=1 exact): recompute the relator check (`aWb⁻¹W⁻¹ = I` with `ρ(a)=[[1,1],[0,1]]`,
  `ρ(b)=[[1,0],[u,1]]`, u=ζ₆) and the exact value `κ−2=u²`, `|κ−2|=1` in `ℤ[ζ₆]` — pure symbolic
  arithmetic, no search, cheap and exact.
- Claim 7 (uniqueness among two-generator census manifolds): recompute J via SnapPy holonomy +
  Nielsen-move minimisation over the (up to) 323 two-generator manifolds in
  `OrientableCuspedCensus`, confirming exactly one (m004) attains 1.000000000000, with m009→√2 and
  m129→2 as the next-smallest. This is the discriminating fact for the uniqueness claim and is the
  one worth independently re-running given it replaces a citation with a computation.
- Claim 4 (withdrawn axiom count): DOCUMENTARY — the correct count (A4,A5,A6 discharged; A1,A2/A3
  assumed) is a hypothesis-reading exercise against Callahan's stated theorem, not a number to
  recompute; a verifier should simply re-read Callahan's definition of "Jørgensen group" (two
  generators, by definition) against `docs/UNIQUENESS_THEOREM.md`'s A1 statement to confirm the
  logical containment.

## 6. SUPERSESSION
**Superseded in part by its own ADDENDUM 1 (= memo 226, `JORGENSEN_IS_IT_RIGHT.md`)**, which
withdraws §4's axiom-discharge conclusion (BENCH ERROR #32) while leaving §§1–3,5–6 and the
addendum's own re-verification intact. Memo 226 was read in full as part of this review (it is the
direct successor memo; INDEX.md row 226 confirms "ADDENDUM 1 to memos/THE_JORGENSEN_NUMBER.md
(memo 225 §4 WITHDRAWN)"). No further memo after 226 revisits this. Not superseded by anything
independent on main, since main's own B1345 already agreed with the corrected (weaker) reading.

## 7. GRADE PROPOSAL
**REPRODUCE-AND-BANK** — the surviving content (J(m004)=1 exact, the independent SnapPy
re-verification, the 323-manifold uniqueness scan, and the {m000,m004} pair/fork
cross-confirmation) is a clean discriminating computation that upgrades B1345 from
cited-Callahan-theorem to independently-tested-uniqueness, and is worth a small follow-on arc or
an addendum to B1345 itself recording the Nielsen-pair reproduction and the two-generator census
scan. The withdrawn §4 axiom-count claim should NOT be banked in any form; note for the record
that main's B1345 never made that overclaim in the first place, so no correction to main is owed
there — only the addition of the new positive material.
