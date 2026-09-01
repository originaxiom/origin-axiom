# PROPOSAL (2026-09-01, fresh physics seat; a filing act — owner / banking seat decides, nothing changed here) — B964 is mislabelled RETRACTED; under PRACTICES (B818, Boundary rule 1) it is PROVED with `supersedes` populated

**Status of this file.** A proposal only. Re-filing a verdict and regenerating VERDICT_LEDGER
are owner/banking-seat acts. Original files unedited.

**What B964 does.** It withdraws two claims of *other* arcs — (1) "27-VEV route stops one step
short" (B962) and (2) "the object does not supply a VEV" (B952, B959, B960; echoed by B962) —
and proves a positive reframing: the measurement cascade *is* an adjoint Higgs mechanism, and
only the rank-reducing 27 VEV is missing. FINDINGS l.91 reads `**Verdict: CORRECTION.**`, which
is not a vocabulary value; `arc_verdict.json` carries `"verdict": "RETRACTED"`,
`"supersedes": null`, which places the arc under VERDICT_LEDGER `## RETRACTED (10)` (l.1167).

**The rule.** `docs/PRACTICES.md` ~l.115 (B818): *"RETRACTED applies only when the arc
withdraws **its own** headline. … Mislabelling an auditor as RETRACTED makes the ledger say the
audit is untrustworthy"*; ~l.120 (Boundary rule 1): *"a correction that also proves is PROVED …
the withdrawal is recorded in supersedes"*. B964 withdraws nothing of its own.

**Propagation gap (cause).** B967's retraction sweep matched the registered phrase exactly;
B952/B959/B960 paraphrase it and so carry no pointer. Only B962 does (l.5 `## ⚠ PARTIALLY
RETRACTED BY B964`). Unpointed sites (Ring R3 HELD re-read H2,
`reports/fresh_physics_seat_2026-09-01/recompute/H2_b964_filing/`): B952 l.47–49; B959 l.88;
B960 l.55; `docs/LAW_MAP.md` l.269 (B952 row, pre-B964 wording; l.230–233 are correct).
`RETRACTIONS.md` and `RETRACTED_PHRASES.md` are correct; `docs/CLAIMS.md` does not exist.

**Proposed worklist** (for the owner to accept, edit or reject):

1. `arc_verdict.json`: `"verdict": "PROVED"`, `"supersedes": ["B962 (27-VEV one step short)",
   "B952/B959/B960 (object supplies no VEV)"]`, dated in-place note.
2. Dated addenda-beside on B952, B959, B960 pointing at B964.
3. `docs/LAW_MAP.md` l.269: NB "superseded by B964 (2026-08-08): the cascade is an adjoint
   Higgs mechanism; the missing datum is the rank-reducing 27 VEV only".
4. Regenerate VERDICT_LEDGER (B964 leaves `## RETRACTED`).

Filed as R3_REPORT **F1**. No computation is involved; nothing in B964's content is disputed.

## CORRECTION (2026-09-01, later the same day; owner's rule "sweep the repo before concluding we don't have something")

*"`docs/CLAIMS.md` does not exist"* (propagation-gap paragraph) was written without a sweep.
Sweep (all seven remote heads, filename regex `CLAIMS`): `docs/CLAIMS.md` indeed exists on no
head, **but the claims registry is the root `CLAIMS.md`** (231 lines; also `core/claims/{D4,
P12, P15}.md`, `papers/P1_seam_form/CLAIMS.md`, `papers/P4_markov_stage/CLAIMS.md`). Those
were then swept for B964 / B962 / B952 / B959 / B960 / "VEV": no hit in any of them, so the
unpointed-site list above is unchanged — the root registry simply carries no VEV claim. The
sentence should read: *"the claims registry (root `CLAIMS.md`, core/claims, papers/*/CLAIMS.md)
carries no VEV claim, so it needs no pointer."*
