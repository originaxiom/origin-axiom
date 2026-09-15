# Reader r2 — Memo 229 (THE_MIRROR_AND_THE_BULK.md)

## 1. HEADLINE
"THE MIRROR AND THE BULK: both riddles are literal, both have answers, and the rest is the tower."
Cells 1–4 = A/A/A/A, C1–C4 pass. No explicit date in the memo body; `INDEX.md` banks it "1B,
2026-09-14".

## 2. CLAIMS
1. **CELL 1 = A (the bulk is inert)**: `m004` filled at 8 hyperbolic slopes `(5,1)...(10,3)` gives
   invariant-trace-field degrees 4,7,4,8,8,7,8,8 — `ℚ(√−3)` contained in **NONE**. m004's own
   (unfilled) invariant trace field: `x²+x+7`, degree 2, disc `−27 = ℚ(√−3)` (the control). Grade:
   PROVED — "independently reproducing C8's banked census over 78 slopes."
2. **CELL 2 = A (the mirror is an automorphism)**: `m004 → mirror` has **8 isometries**, cusp-map
   determinants `{−1,+1}`, symmetry group **D₄**; the `+1` one is an **orientation-reversing
   self-map**. Conclusion: there is no second manifold, "the other half" is the object itself, an
   identification, not a partner. Grade: PROVED (computed isometry group).
3. Price statement: axiom 5 (orientation) **provably** yields an amphichiral object (250/250
   orientation double covers amphichiral, cited from "memo 196's addendum") — "the bit is spent by
   the axiom, not withheld by the arithmetic." Grade: cited from elsewhere, not re-derived here.
4. **CELL 3 = A (the tower breaks the mirror)**: covering-tower census to degree 7 — degree
   2–4: 4 covers, 0 chiral; degree 5: 4 covers, **2 chiral** (first chirality, 2 cusps,
   `H₁=ℤ/2⊕ℤ⊕ℤ`); degree 6: 11 covers, 8 chiral; degree 7: 9 covers, 8 chiral; total ≤7: 28 covers,
   18 chiral. Cites B1324's own degree-10 census: 66/87 chiral, "every cover keeps the invariant
   trace field" — answering FRESH_EYES Q15 (a carrier keeping the atom and remembering the bit)
   YES. Grade: PROVED to degree 7 here; degree 8–10 figures are **cited from B1324**, not re-derived
   in this memo.
5. **CELL 4 = A (and still gives index 0)**: on chiral one-cusped covers, the torsion is
   meridian-generated, leaving 2 cusp-trivial unprotected sectors, **both index 0**, plus 136
   control sectors at 0. The 54 multi-cusped chiral covers (**B1333**, computed on
   `<remote>/paper-verification-ufp0zn`, **explicitly cited as branch work and NOT re-run here**):
   38,070 sectors at three primes over all 54 covers, 1841 with ≥2 live cusps, **index ZERO in
   every one**. Grade: the one-cusped part (2 sectors + 136 controls) is presented as computed on
   this bench; the 54-cover multi-cusped part (38,070 sectors) is an **explicit citation of another
   branch's work**, not independently reproduced by this memo.
6. Interpretive synthesis: complement/mirror/shadow are three "prices" (C8, axiom 5, C4
   respectively), not three symptoms of a missing whole; the object "sits exactly at the corner
   where the atom and the bit trade against each other," and the covering tower is the one place
   both are held at once, "and even there the index is 0." Grade: interpretive, labelled as such.
7. **"THE LIVE FRONTIER, named"**: both censuses (B1324, B1333) stop at degree 10; past degree 10
   is "**the one place this question still has a computable rather than a banked answer**." States
   in advance: nonzero index higher up would be the first object-native chirality; continued zero
   would make "the tower is vector-like" much stronger than two censuses currently support. Grade:
   forward-looking claim, explicitly hedged both ways — **but see §6, this specific framing was
   later called "TOO STRONG" by memo 230.**
8. Operational controls: **C1** — `is_isometric_to(M, mirror)` **ignores orientation** (returns
   True for chiral `m015`); a first sweep using it wrongly reported 38/38 covers amphichiral to
   degree 8, caught only by comparison with B1324's banked census, not by the instrument itself.
   **C2** — SnapPy's **double-precision** trace-field routine returned **degree 11 garbage** for
   m004's actual degree-2 field, caught by its own positive control, fixed with `ManifoldHP`. Both
   failure modes are reproduced inside the certificate. Grade: both are genuine instrument-failure
   findings, computed and shown, not just claimed.

## 3. CERTIFICATE
- **Seal:** `outside_bench/seals/THE_MIRROR_AND_THE_BULK_PREREG.md` — **exists**. Memo states sha256
  `f1e065d38d1a04938b42bf20ed3e29ee237afa60af4a2e8ae5537081e635ba50`. **Computed live
  `shasum -a 256` on the current tree: `3a98f2c2a05d547cc3d0258e95081b46cc46b44ec09111814fc985d1e1166632`
  — DOES NOT MATCH.** Traced the discrepancy via `git log -p`: the seal was committed at
  `b3c32df2` matching the memo's stated hash exactly (`git show b3c32df2:<path> | shasum -a 256` →
  `f1e065d3...`, confirmed), then **modified during the later merge commit `4e21000f`**
  ("Merge paper-s9-second-pass into main"), which rewrote one line for vendor-name redaction:
  `` `<vendor>/paper-verification-ufp0zn` `` → `` `<remote>/paper-verification-ufp0zn` `` (per the
  repo's own attribution/privacy policy — `docs/SEAT_REGISTER.md`'s merge-hygiene note confirms
  "eighteen files carried the cloud tool's branch-name prefix (rewritten to `<remote>/`...")). **So
  the mismatch is explained and benign**: the seal's scientific content (fences, cell definitions,
  controls) is byte-identical apart from that one redaction; the hash drift is a housekeeping
  side-effect of the merge, not evidence of post-hoc tampering with the preregistration. A future
  reader recomputing this hash should compare against the pre-merge commit `b3c32df2`, not HEAD, or
  else expect exactly this one-line diff.
- **Certificate:** `outside_bench/certificates/the_mirror_and_the_bulk.py` — **exists**.
- **Output:** `outside_bench/outputs/the_mirror_and_the_bulk.txt` — **exists**. Tail:
  `CELL 1 (the bulk is inert): A`, `CELL 2 (the mirror is an automorphism): A`,
  `CELL 3 (the tower breaks the mirror): A`, `CELL 4 (and still gives index 0): A`,
  `C1...PASS`, `C2...PASS`, `C3 CS declared one-sided: stated`, `C4 record quoted: PASS` — **agrees
  exactly** with the memo's stated outcomes (claims 1–5, 8).

## 4. ON MAIN ALREADY?
1. **C8's banked filling census (Cell 1) and B1324's covering-tower census (Cell 3):** **(a)
   already on main**, cited by the memo itself as the pre-existing record this cell reproduces —
   confirmed these are real frontier arcs (B1324 is directly discussed in the MEMORY context and in
   `outside_bench/INDEX.md` row 229's own text as a prior banked arc).
2. **The 54-multi-cusped-cover, 38,070-sector, index-0 result (Cell 4, claim 5):** **(a) already on
   main, cited with matching numbers.** `docs/TOE_REQUIREMENTS_LEDGER.md` row "2 chirality" (dated
   2026-09-15, i.e. one day after this memo) states: *"Phase 2's chiral-cover test has now been RUN
   and returned zero: the multi-cusp index derived and verified (B1333), 38 070 sectors on all 54
   chiral covers to degree ten all zero, and the first proof of I = 0 on a stated domain
   (B1334)."* — **numbers match exactly** (38,070 sectors, 54 covers, all zero).
3. **The "live frontier past degree 10" framing (claim 7):** **(d)-adjacent: partially contradicted
   / overtaken by a sibling memo, not by main directly.** `outside_bench/INDEX.md` row 230
   (`THE_TOWER_PAST_TEN.md`, same date 2026-09-14) explicitly says: *"memo 229 called the tower past
   degree 10 'the one place the question still has a computable answer' AND THAT WAS TOO STRONG."*
   Memo 230 ran the actual scan (18 in-domain sectors at degrees 11–14, all index 0) and found the
   index instrument **has never returned a nonzero on any real manifold in characteristic zero**
   (citing B1297's own MB12: "LIVE NON-VACUITY NOT ESTABLISHED" and B1335's char-0 refutation), so a
   further null there "cannot distinguish 'the covers are vector-like' from 'this index never fires
   on real manifolds.'" **`docs/TOE_REQUIREMENTS_LEDGER.md`'s current row 33 (2026-09-15) does NOT
   carry memo 230's caveat** — it states flatly that the test "has now been RUN and returned zero"
   without qualifying that the instrument's own live-positive status in char-0 is unestablished.
   This is not a direct contradiction of memo 229's *computed facts* (Cells 1–4 are not disputed),
   but it is a live gap: the doc that inherited memo 229's numbers is currently **more confident
   than memo 229's own sibling memo (230) says is warranted**.
4. **Axiom 5 / "orientation provably yields amphichiral, 250/250" (claim 3):** cited from "memo
   196's addendum," itself an outside_bench artifact — (c) not independently found cited by number
   in `docs/`, though the general amphichirality-of-m004 fact is consistent with
   `docs/TOE_REQUIREMENTS_LEDGER.md`'s chirality row.

## 5. NEEDS COMPUTATION HERE
- **Cell 1 (filling census):** for each of the 8 listed slopes, run SnapPy `M.dehn_fill((p,q))`
  then `M.invariant_trace_field_degree()` (or `ManifoldHP` per the memo's own C2 control fix) and
  confirm degrees `4,7,4,8,8,7,8,8` and that none contains `√−3` (check via `M.trace_field()`'s
  minimal polynomial discriminant, not just degree, to rule out `√−3` appearing as a subfield of a
  higher-degree field by coincidence).
- **Cell 2 (mirror isometry):** `M.symmetry_group()` and `M.is_isometric_to(M.mirrored(),
  return_isometries=True)` on `m004`, filtering by **cusp-map determinant** (not the naive
  orientation-blind `is_isometric_to` flagged by C1) — expected 8 isometries, group D₄, at least one
  det=+1 orientation-reversing self-map.
- **Cell 4 (the discriminating fact for the whole memo):** the single most important number to
  re-check independently is **whether the chirality index has EVER returned nonzero on any real
  (non-synthetic) manifold in characteristic zero** — per memo 230's finding, it has not. A verifier
  should re-run B1297's own positive-control population (the "60 census manifolds, 12 sectors, all
  zero" cited in memo 230) and confirm this remains the state of the art; until a live positive
  exists, claim 5's "index zero in every one" and claim 7's framing both need that caveat attached.
- **The seal hash (documentary):** `git show b3c32df2:outside_bench/seals/THE_MIRROR_AND_THE_BULK_PREREG.md
  | shasum -a 256` should reproduce `f1e065d3...` exactly, confirming the mismatch's explanation.

## 6. SUPERSESSION
- **Claim 7 (the "live frontier past degree 10" framing) is explicitly called "TOO STRONG" by memo
  230** (`THE_TOWER_PAST_TEN.md`, banked 2026-09-14, same day), which ran the actual scan and found
  the deeper problem: the index instrument has no demonstrated live positive in characteristic zero
  anywhere in the record, so nulls at any depth (10, 14, or beyond) cannot discriminate "vector-like"
  from "instrument never fires." Memo 230's own words: *"THE FRONTIER MOVES RATHER THAN CLOSES: the
  live question is no longer 'is there a nonzero index higher up the tower?' but 'CAN THIS INDEX
  FIRE ON ANY REAL MANIFOLD IN CHARACTERISTIC ZERO AT ALL?'"*
- **Cells 1–4's actual computed content is NOT contradicted or withdrawn by memo 230 or anything
  else found** — only the specific rhetorical framing of what "the live frontier" is has been
  corrected.
- Current main (`docs/TOE_REQUIREMENTS_LEDGER.md`, dated one day after both memos) has **not yet
  absorbed memo 230's correction** — it restates memo 229's Cell 4 numbers without memo 230's
  caveat. This is a documentation-currency gap a future harvester should close.

## 7. GRADE PROPOSAL
**DISPUTED** (narrowly, and importantly, per the PROMPT's instruction never to bury this class).
Not because Cells 1–4's computations are wrong — they check out, the certificate matches, and
Cell 4's headline number (38,070 sectors, all zero) is already correctly cited on main
(`docs/TOE_REQUIREMENTS_LEDGER.md`). The dispute is specifically about **claim 7**: memo 229's own
framing of "the live frontier" was flagged as **too strong** by its own sibling memo (230) within
the same banking session, on the grounds that the underlying instrument has never demonstrated a
live positive in characteristic zero — and **main's current ledger row inherited memo 229's
confident framing without memo 230's correction**, so as of this reading, a reader of
`docs/TOE_REQUIREMENTS_LEDGER.md` alone would come away more confident about "the tower is
vector-like" than the record's own most careful memo license. This should be flagged for
harvesting: propagate memo 230's caveat into the TOE ledger row wherever memo 229's/B1333's numbers
are cited.
