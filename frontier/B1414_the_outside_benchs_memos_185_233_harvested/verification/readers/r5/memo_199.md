# memo_199 — THE_SECTION8_BIT_IS_NOT_THE_MIRROR.md

## 1. HEADLINE
"**SECTION 8'S CHIRALITY BIT IS NOT THE MANIFOLD'S MIRROR SIGN**" — B1327's explicitly-handed-off over-count question ADJUDICATED **NO**, via two independent separations (domain, presence). Date: 2026-09-11.

## 2. CLAIMS
1. (i) DOMAIN separation: holding the object relatum fixed, the §8 class takes 8 distinct values `{−181,−29,−19,−1,0,+1,5,11}` across all four branches while the object never changes; the mirror sign is read off the object's own isometry group (no partner) and splits 4+4 — graded PROVED (computed).
2. (ii) PRESENCE separation: on the object the two disagree about existing — mirror sign present & non-trivial (m004 amphichiral, 4 orientation-reversing isometries); §8 bit absent (canonical pair at κ=−2, D=+1, mirror realized inside SL₂(ℤ), per B1248's mechanism) — graded PROVED (computed + cites B1248).
3. Conclusion: "mirror = arrow × swap" is a relation on the object's own isometry group only, does not reach §8's bit, no ledger row is a restatement of another — B1327's over-count "resolves NO" — graded the memo's central verdict.
4. This bench's own claim to novelty is retracted: `already_banked.py` search finds **B1248 (PROVED, banked 2026-09-05)** already contains both halves of this answer, six days before B1327 (which raised the question) was even written — graded "the answer was already banked," i.e. this memo's headline finding is itself a rediscovery/citation-gap catch, not new content.
5. Observation returned to B1327's seat: all 8 cusp maps are diagonal (verified, zero off-diagonal entries), so `det diag(a,d)=a·d` trivially — the "mirror=arrow×swap" check's empirical content is the diagonality, not the product law — graded a caveat, "does not weaken B1327's typing proposal."
6. BENCH ERROR #19 (self-filed): an earlier pass used the wrong `tr[A,B]−4` convention, misread B1200 as contradicted; corrected to `tr[A,B]−2`; control C2 verifies `tr[A,B]-2 = ω`, `|tr[A,B]-2|=1`, `Φ₃(tr[A,B]-2) ≈ 1.79e-15` — B1200 reproduces exactly; graded CORRECTED (own error, not a finding about the object).
7. Scope disclaimers: does NOT settle whether arrow/swap are independent of each other; does NOT decide which freedom-ledger row moves (owner's/§8-9 seat's call); does NOT make the §8 bit derivable — all graded EXPLICITLY OUT OF SCOPE.

## 3. CERTIFICATE
`outside_bench/certificates/section8_bit_is_not_the_mirror.py` EXISTS (260 lines). `outside_bench/outputs/section8_bit_is_not_the_mirror_out.txt` EXISTS (112 lines). Output tail: "THEREFORE B1327'S OVER-COUNT QUESTION RESOLVES **NO**... B1327's own framing of its finding — 'this is not a claim' — was the right call" — agrees verbatim with the memo's §2 verdict.
**Seal:** `outside_bench/seals/SECTION8_BIT_ADJUDICATION_PREREG.md` EXISTS (100 lines), sealed before the certificate was written. Computed `shasum -a 256` of the seal file: `a0f898ac70dc9bdaa27778e98d73692f94e8abb443aba3922962c07ca4094dbb`. This matches the sha256 the memo header cites exactly: `a0f898ac70dc9bdaa27778e98d73692f94e8abb443aba3922962c07ca4094dbb`. **Match confirmed.** No addendum changed the seal.

## 4. ON MAIN ALREADY?
1. The underlying answer (both halves) — **(a) already on main with a citation**: `frontier/B1248_norm_classification/FINDINGS.md` exists and is PROVED, banked 2026-09-05, and (per the memo's own quoted excerpts) already states "the class taking many values" and "why the object alone has no bit." This is main content memo 199 discovered via `already_banked.py`, not new main content memo 199 added.
2. B1327's question itself — **(c) NOT resolved on main**: `frontier/B1327_relation_not_observer/FINDINGS.md` (verdict still **OPEN** as read in full) still contains the unadjudicated sentence "Whether they are the same bit is for the seat that owns §8 to adjudicate. If they are, one of the three rows is not an independent input" — with no annotation, addendum, or strikethrough reflecting memo 199's NO answer. Searched for "memo 199", "adjudicated", "ANSWERED" in that file: no hits beyond the original question text. So the adjudication that memo 199 performed has **not been written back into B1327's own arc on main**.
3. BENCH ERROR #19 (κ convention fix) — this is an internal bench correction, not a main-doc claim; `docs/ERROR_LEDGER.md` was not found to reference it (not exhaustively checked, but no "BENCH ERROR #19" hit in a targeted search of docs/ELSewhere). (c) NOT on main as a numbered E-class error; it's tracked only in `outside_bench/THE_OWNER_REGISTER.md` addendum 103/105.
4. The diagonality observation (§4) — (c) NOT on main; it is addressed "to B1327's seat" but B1327's file shows no update incorporating it.

## 5. NEEDS COMPUTATION HERE
1. The single discriminating fact: recompute the §8 class (the Fricke-κ torsor pair value) across B1248's four branches while holding the object relatum at `A_OBJ`, and independently compute the object's own mirror-sign split (4 orientation-reversing isometries out of 8) with **no** second relatum named. Expected: §8 class ∈ {−181,−29,−19,−1,0,1,5,11} (8 distinct values) vs. mirror sign ∈ {+1,−1} (constant per isometry, 4/4 split) — the mismatch in cardinality/domain is itself the proof. This is a short SnapPy/sympy rerun (already in the 260-line certificate, presumably <2 min).
2. The presence check: verify m004 is amphichiral (SnapPy `M.symmetry_group()` orientation-reversing count = 4 of 8) and independently verify κ=−2 at the canonical pair (sympy trace computation on the two generators from B1248's normalization) — two independent, cheap computations.
3. The seal-hash check is DOCUMENTARY and was already done above (matches).

## 6. SUPERSESSION
Not superseded by any later memo in INDEX.md (202, 215, 217 do not touch this topic). Not contradicted by anything found on main. The one live gap is that B1327 (the arc that *asked* the question) has not been updated to reflect the answer — this is a **citation/write-back gap**, not a supersession of memo 199's content.

## 7. GRADE PROPOSAL
**ALREADY-ON-MAIN** for the substantive mathematical content (it is B1248, PROVED 2026-09-05, pre-dating this memo) — but **REGISTER** the adjudication act itself: memo 199's real contribution is closing B1327's open question by pointing at existing main content, and that closure has not yet been written back into `frontier/B1327_relation_not_observer/FINDINGS.md`, which a verifier should flag as a documentation debt (B1327 still reads OPEN with the question un-adjudicated in text, even though the answer already existed on main before B1327 was written).
