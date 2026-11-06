"""R76-1, the OPEN_LEADS half of P-617 (S306j, 2026-11-06): Review 74's reader proposed closing 73 of the 77 open
leads in docs/OPEN_LEADS.md (41 answered with pointers, 32 carried in full by register rows). Each proposal was checked
against its pointers; every quote behind a decision was found verbatim at its path (checks.json). A confirmed lead's
first heading gains 'CLOSED 2026-11-06 (R76-1, B1850: ...)'; an unconfirmed one keeps its heading and gains a dated
note under it saying what is answered or carried and what is not. Run from the repository root."""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[3]
LEADS = ROOT / "docs" / "OPEN_LEADS.md"

CLOSE = {
    "L149": "answered by B1019 (DIVERGES: the siblings have no door)",
    "L151": "carried in full by P-328 (its MATCH/MISMATCH test, after the e20c J rule is verified on main)",
    "L154": "carried in full by P-137 (the bridge posed on the weave's sector), with P-138 and P-318",
    "L158": "answered by B1040 (the field owns V's structure, the object its instantiation) and B1041; a one-line TERMINOLOGY note remains",
    "L165": "a duplicate of L176, both carried by P-332",
    "L166": "answered by B1070 and B1071 (Λ constructed), with B1072 and B1073; the spec's gaps G5–G9 lie outside the lead's closing criterion",
    "L174": "answered: C1–C4 banked as B1088–B1091, C5 NEGATIVE in B1108",
    "L175": "answered by B1110's F5 (the h = 0 locus is a word property)",
    "L176": "carried in full by P-332 (the Eichler route, the explicit automorphisms, B1121's search box)",
    "L177": "answered by B1104 (NO-SECTION)",
    "L184": "answered by B1178 (collection 178 s to 15 s); the later regression is P-322's",
    "L188": "answered by B1199's GC-31",
    "L191": "carried in full by P-334 (B502 dead at depth 4)",
    "L196": "answered in B1235's addendum (the five verdicts written)",
    "L202": "answered by B1413 (zero on every geometric sector, by theorem) and B1324; (a) superseded by B1604",
    "L204": "answered by B1322 (N(27) = 0 on every direction)",
    "L206": "answered by main's check (B1850's l206_generating_pair.py: w = b to 8.5e-15 in the faithful holonomy, so (ABABB, a) generates π₁(m003)); P-334's dated note on B1401 still owed",
    "L217": "answered by B1409 (all three rows); the residue is P-328",
    "L220": "answered: R57-3, 12 of 12 adjudicated",
    "L222": "answered by B1438, B1444, B1470, B1441 and B1442, with FK13 in GENESIS",
    "L232": "carried in full by P-426 (the five living documents)",
    "L234": "answered by B1442 ((a) NEGATIVE) and P-309 ((e) answered, (b)–(d) retired)",
    "L248": "§ 8 carried in full by P-667; the rest answered (P-335)",
    "L249": "carried in full by P-429 (its six cells)",
}
KEEP = {
    # proposed "carried in full"
    "L145": "P-322 carries the REVIVABLE view. Not carried: L145a's B500 reopen (35 unchecked words) and its score correction, and L145c's composite-id hazard.",
    "L148": "Neither P-322 nor P-291 carries the widen-or-declare decision or the B806/B1008 re-derivation.",
    "L152": "P-291 is a math-integrity check and states no relay-content gate; no row carries this lead.",
    "L161": "P0-0, the genericity control, lives only here. P-335 declined an experiment and kept L161 at P0-0; Phase 1b is P-331, under P-033.",
    "L162": "P-332 carries the transitivity proof route. Not carried: the THE_CLAIM input-#5 and B962 Q4 amendments it gates.",
    "L183": "P-322 does not carry the census of arcs banked without a runnable reproducer, and no other row does.",
    "L198": "P-322 carries the CANNOT_RUN count and the vendoring of R020–R022. Not carried: the fc R46 certificates, the six PINS-TEXT runners and the reproduce_belt walk.",
    "L213": "No row carries the canonicity classification of the banked triangulation uses.",
    "L214": "P-322 carries only the homonym table. Not carried: re-running NOVELTY_AUDIT and the NEEDS-LIT rows through it.",
    "L193": "P-334's answer is on 1490 word states, not on the 112-family. The finer invariant is not carried.",
    "L207": "P-334 carries the depth-one result. Not carried: Nielsen-inequivalent pairs at depth two and beyond (m009, for one).",
    "L192": "P-323 carries the θ̄ question. Not carried: the same CP bit for δ_CKM and δ_PMNS, and the link to B303.",
    "L197": "P-319 (the P9 and GENESIS tier) and P-589 (LAW_MAP) carry parts. Not carried: the corpus-wide walk of the superseded_by candidates, and REVIEWER.md's lock_kind column.",
    "L205": "Answered FAIL (B1321, B1414), and P-333 carries the weave-level successor. Not carried: the golden test of the eleven ten-tetrahedra members.",
    "L211": "P-318 carries the dated corrections. Not stated anywhere: the stratum-law question itself, or its retirement as defined by the instrument.",
    "L218": "No row carries the enumeration of the object's integer invariants.",
    "L221": "P-326 carries only (d). The 27̄ remedy and its pairing spectrum are carried by no row.",
    "L231": "P-427, P-317 (b), P-318 and P-289 carry most items. Not carried: the withdrawn 16σ phrase, the sealed-crossings count, and B1141/B1145's 'no Dirac operator'.",
    "L239": "P-321 carries (a) and P-428 carries (c). (b) and (d)–(g) are carried by no row.",
    "L240": "P-428 carries (c) and (f), and P-092 the THE_CLAIM line. (a), (d), (e) and (g)–(i) are not carried by name.",
    "L242": "P-428 names both counts as proposed RETIRED, not yet confirmed. The ε-sign formula is in no row.",
    "L243": "P-428 carries (c) and (d). Not carried: (e), R69's −3, and (f), the child lane's decisions.",
    "L247": "P-571 and P-589 (a) carry parts. Not carried: the other 31 member-scope kills, and CLOSED_DOORS's member-scope column.",
    # proposed "answered"
    "L144": "B1096 shuts door 5 (the anomaly layer vanishes identically). Doors 1–4 are untouched.",
    "L146": "B1600 and B1601 answer the hypothesis on its false side (2T on every odd trace). Still open: what singles out ±LR. The own-conductor test for m ≥ 4 is not run.",
    "L147": "B1021 itself says the ask (λ₂ to 50 digits) is not discharged.",
    "L157": "Hooks 1, 2 and 4 are computed (B1039, B1042, B1043), and hook 3 is L154. Forbid 1 (seam-locality) is recorded as untested.",
    "L159": "B1248 and B125 do not address the gerbe, and the Deligne–Milne gate never ran.",
    "L163": "B866 and B978 rebuild the pencil. Still open: char-0 exactification over K. L142's re-pose was closed only by a reading.",
    "L182": "SEAM-B and SEAM-Y are resolved (B1146, B1154). SEAM-A is open in B1156, and B1159 calls it a wall only in substance.",
    "L185": "The disposition table is only in a gitignored audit draft, and the row it promises does not exist.",
    "L189": "The eight dispositions are only in the audit room (P-656). Item (1) is P-638, still open.",
    "L190": "B1188 corrects only the direction word. The reach-deficit law and its richer null are not computed.",
    "L194": "B1477 makes it a census law on 1,205 manifolds, 'not a proof'. The proof obligation stands.",
    "L200": "P-318 lists only B1295's PSLQ domain. The proof and c₀ are not derived.",
    "L201": "B1641 and B1674 compute neither the F₄ chamber faces' SU(3)³ anomaly nor any closing.",
    "L203": "(i) is generalised by B1733, and B1722 is negative. (ii) on Y12's order-16 lines is not computed. The selection is open (P-139, P-373).",
    "L212": "B1702 does not test the cusp field against the end invariant, and the probe is not run.",
    "L215": "B1406 still says observed, not derived, and P-334's note has not landed.",
    "L219": "B1410 reframes it. Whether the boundary-unipotent selector applies in the tower's room is not computed.",
    "L223": "B1700 and B1795 (P-325) pay the split. The closing's own existence has no pointer.",
    "L229": "P-309 retires (i)–(ii) and answers (iii). (iv) is open (FK9), and (v) is carried nowhere.",
    "L233": "Closed: (a) and (f) (B1438, B1440), and (b) (B1737); (d) is retired. (c)'s cocycle is owed (B1737 § 3), and (e) is carried nowhere.",
    "L235": "(a) is closed (B1444), (b) goes into P-294, and (c) is answered. The core question and (d) remain.",
    "L236": "Answered: (b) and (g) (B1445, B1444); (d) is withdrawn; (a), (c) and (f) are retired by P-309. (e), the complete-cusp point's volume and CS, is not computed.",
    "L237": "(a) and (b) are answered (B1447, B1736), and (c), (d) and (f) retired. (e)'s leftovers are open (B1451).",
    "L245": "B1469–B1472 decide about a dozen claims. The rest are checked only in the audit room, and xB014's B207 note is unrowed.",
    "L246": "Phase 1 and Phase 2's first cell are paid (B1474–B1481). Not carried: Phase 3, Phase 2's number-field question, and the unexplained residue.",
}


def main():
    lines = LEADS.read_text(encoding="utf-8").split("\n")
    first = {}
    for i, ln in enumerate(lines):
        m = re.match(r"#{2,3} (L\d+)\b", ln)
        if m and m.group(1) not in first:
            first[m.group(1)] = i
    assert not (set(CLOSE) & set(KEEP))
    for L in list(CLOSE) + list(KEEP):
        assert L in first, L
        # the lead-debt gate's own closure pattern (a status word after "**", "— ", "- " or the id; a title's "CLOSED FORM" is not one)
        assert not re.search(r"(?:\*\*|— |- |L\d+[a-z]? )(?:CLOSED|DISCHARGED|WITHDRAWN)\b", lines[first[L]]), (L, lines[first[L]][:120])
    for L, why in CLOSE.items():
        lines[first[L]] += " — CLOSED 2026-11-06 (R76-1, B1850: %s)" % why
    for L in sorted(KEEP, key=lambda x: -first[x]):      # insert bottom-up so earlier indices hold
        note = ("> *2026-11-06 (R76-1, B1850): Review 74's reader proposed closing this lead; main's check did not confirm it."
                " %s The lead stays open.*" % KEEP[L])
        lines[first[L] + 1:first[L] + 1] = ["", note]
    LEADS.write_text("\n".join(lines), encoding="utf-8")
    print("closed %d, kept %d with notes" % (len(CLOSE), len(KEEP)))


if __name__ == "__main__":
    main()
