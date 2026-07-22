# S16 REVIEW 2 — B749 genesis forks (v2 re-seal)

NONCE: B749R2-LIVE-8c2d5e41
DATE: 2026-07-21
REVIEWER: fresh, non-authoring §16 seat (audit seat, ~/oa-audit-seat)
SCOPE: narrow — verify the remedy for review 1's single STOP premise (MEASUREMENTS.md F7
falsely asserted "quadratic slopes = exactly the metallic family"; witness √3−1) and check
for regressions. All other review-1 premises were PASS and are re-checked only for
byte-stability, not re-litigated.

## FINDINGS

### CHECK 1 — The F7 correction: PASS
Structure: MEASUREMENTS.md v2 F7 (lines 48-61) now carries the three-strata form exactly as
required: F7a = non-quadratic slope, no self-similar generator via Lagrange, verified on a
transcendental-slope witness by CF non-periodicity, with its correct assertive claim "(the
self-similarity locus is exactly the QUADRATIC class, not the metallic family)"; F7b = the
quadratic-non-metallic stratum with the √3−1 witness (CF period (1,2)) and its OWN verdict
criteria — ROBUST = F7b carriers lack the anatomy, FRAGILE = an F7b carrier matches the
interface (T4's extremality then priced as load-bearing) — both outcomes stated, both
reachable, so MB12 holds for the new stratum (reachability is concrete: the period-(1,2)
composite abelianization is [[1,1],[1,0]]·[[2,1],[1,0]] = [[3,1],[2,1]], trace 4, det 1 —
Anosov, so a genuine hyperbolic mapping torus exists to measure; recomputed here). F7c =
cross-reference to F3 for the metallic stratum itself, no duplicate measurement.
False universal GONE: grep over the arc + P019 finds "exactly the metallic family" only (i)
inside F7's header QUOTING the v1 sentence explicitly marked FALSE, and (ii) inside the P019
erratum quoting it as the caught error — no assertive use anywhere. The v1 ROBUST-language
echo "(the family is the self-similarity locus)" survives only inside S16_REVIEW_1.md's own
quotations; absent from all sealed design text.
Mathematics recomputed independently in this seat (sympy 1.x, mpmath, 40 dps):
- CF(√3−1) = [0;1,2,1,2,…], purely periodic, period (1,2) — computed by iterator AND by
  sympy's continued_fraction_periodic(-1,1,3) = [0,[1,2]].
- Minimal polynomial x²+2x−2, degree 2 — quadratic, as sealed.
- Not metallic for ANY m (stronger than review 1's m=1..5 spot check): if √3−1 = [0;m,m,…]
  it would satisfy x²+mx−1=0; subtracting the minimal polynomial gives (m−2)x+1=0, i.e.
  x = 1/(2−m) rational — contradiction; sp.solve confirms no solution; empirical check
  m=1..7 all False. Metallic values are (√(m²+4)−m)/2, minpoly constant −1 ≠ −2.
- Sturm-number condition (strict substitution-invariance): conjugate −1−√3 ∉ (0,1) — holds.
- "Metallicity = the all-equal-digits subfamily selected by T4's extremality" is CORRECT:
  (i) [0;m,m,…] all-equal-digits ⟺ x = 1/(m+x) ⟺ the metallic means, by definition/
  computation; (ii) it is a PROPER subfamily of the quadratic class (the witness); (iii) the
  witness is self-similar yet fails the extremality selector: its Lagrange number, computed
  here from λ_n = [a_{n+1};…] + [0;a_n,a_{n-1},…] over both positions of the bi-infinite
  (1,2)-word, is max(√3, 2√3) = 2√3 ≈ 3.4641 > √5 = L(φ) (Hurwitz bottom of the spectrum,
  = T4's extremality as P019 states it). So self-similarity (Lagrange/quadratic) and
  extremality (T4) are genuinely different selectors and the corrected attribution is right.

### CHECK 2 — The v2 seal: PASS
All five sha-256 lines of the v2 block recomputed from the working tree; ALL FIVE MATCH:
- fbabd790…f65b63a  PREREGISTRATION.md — IDENTICAL to the v1 line (unchanged since the
  base commit, re-verified against git show 1e432778: same digest), so no prereg drift.
- dbf7e40c…40d81e5d MEASUREMENTS.md — changed (the F7 correction + executor-warnings
  addendum; delta audited in Check 5).
- ae2b8921…b932c3ad EXECUTION_NOTES.md — NEW at v2 (confirmed absent from commit
  1e432778: "exists on disk, but not in '1e432778'").
- 9fab1ea1…e2f1b32d P019_the_genesis_axiom_chain.md — changed by the erratum only
  (byte-audit in Check 4).
- cdde0698…f63f5c9  reviews/S16_REVIEW_1.md — pinned; digest matches the file on disk,
  whose content records the STOP this v2 remedies (nonce B749R1-LIVE-3f7a1c88 intact).
v1 block preserved: the entire v1-commit ARTIFACT_HASHES.txt is byte-identical to the first
five lines of the current file (diff clean), and the three v1 digests recomputed from git
show 1e432778:<path> all reproduce the recorded v1 lines. Working tree clean at e5e482ff
("B749 v2 re-seal"), which sits directly on the v1 seal commit 1e432778.

### CHECK 3 — EXECUTION_NOTES.md vs cc's relay: PASS
Compared point-by-point against <cc2-seat>/seat-work/relay/
CC_TO_CC3_2026-07-21_b749_execution_notes.md. All three strengthenings carried faithfully:
1. ROBUST-earning + contra-prior skeptic — relay's "a ROBUST verdict states WHICH invariants
   were checked and why absence there is informative" + "any contra-prior ROBUST (F5 or F3)
   gets one skeptic of its own" maps exactly onto NOTES item 1 (same B742 false-ROBUST-class
   rationale, same F5/F3 enumeration, "despite the verdict direction").
2. F8 pre-execution vacuity — relay's "write down concretely what GEOMETRY-REDUNDANT would
   look like (which combinatorial invariant COULD in principle encode √−3), so the criterion
   demonstrably can fail" + the §16-checks-information-beyond-B746 duty map onto NOTES item 2.
   The NOTES add two "e.g." candidate invariants (order-unit trace pairing in a quadratic
   imaginary extension; gap-labeling outside ℚ(√5)) — illustrative, non-binding elaboration,
   not a weakening or a criterion change.
3. F5 dual-route — relay's census/isometry AND explicit-construction (det −1 bundle →
   orientation double cover → verify ≅ m004) routes with field/degree cross-checks and the
   no-single-isometry-call rule map onto NOTES item 3 verbatim in substance.
Verification-side only, as claimed: none of the three alters any fork's discriminating
measurement (F2–F8 criteria audited in Checks 1/5) or any prior — the priors live in
PREREGISTRATION.md, whose digest fbabd790… is unchanged v1→v2, exactly the seal the relay
says "stands". The additions only ADD verification duties (an extra skeptic; a pre-execution
writedown; a second identification route) — strengthenings in the permitted direction.

### CHECK 4 — The P019 erratum: PASS
Byte-stability of the approved text: git show ced69b62:philosophy/P019_the_genesis_axiom_chain.md
is 9514 bytes; diff against the first 9514 bytes of the current file is CLEAN — the owner-
approved red-penned text is byte-unchanged (and that blob's digest reproduces the v1 sealed
line efb3a40a…, closing the loop). Everything after byte 9514 is exactly the erratum block.
Form: the erratum is appended after the approved text (line 62's soft version is corrected
by annotation, not edited — the right choice for byte-stability), clearly dated 2026-07-21,
and its heading marks it "for owner + cc sign-off at the merge gate" as required.
Mathematics: the telescoping "aperiodic → Sturmian (T3) → self-similar = quadratic
(Lagrange) → metallic (T4's extremality) → golden (T4's fixed point)" is correct, each
inclusion strict with a witness: Sturmian ⊊ aperiodic (Morse–Hedlund: Sturmian = minimal
complexity p(n)=n+1; Thue–Morse is aperiodic non-Sturmian); quadratic-slope ⊊ Sturmian
(transcendental slopes — F7a's witness class); metallic ⊊ quadratic (√3−1, verified in
Check 1); golden ⊊ metallic (silver, m=2). Attribution per arrow is right: T3 = Morse–
Hedlund, quadratic ⟺ eventually-periodic CF = Lagrange, all-equal-digits = extremality
selection (Check 1 shows the F7b witness fails it, L = 2√3 > √5), golden = the m=1 fixed
point at the Hurwitz bottom. The rewritten soft sentence ("…yields the SELF-SIMILAR
(quadratic-slope) class, within which the metallic family is the all-equal-digits subfamily
that T4's extremality alone selects") is exactly the corrected statement verified in Check 1,
and the erratum's claim that F7b measures the exposed in-between stratum matches
MEASUREMENTS.md v2.

### CHECK 5 — No regressions: PASS
Full diff of git show 1e432778:MEASUREMENTS.md (the v1-sealed bytes) against the v2 working
tree shows EXACTLY two hunks and nothing else:
(1) the F7 block replacement (v1 lines 48-55 → v2 lines 48-61, audited in Check 1);
(2) a five-line executor-warnings addendum appended to the cross-fork instrument rules.
The header, F2, F3, F4, F5, F6, F8 blocks and the original cross-fork rules text are
byte-unchanged. The addendum's content matches review 1's recorded findings item for item:
'b++RL' = m004 (review 1 Check 6, vol 2.02988321282, isometry-confirmed); m000 = the
Gieseking, vol 1.0149416064, orientation_cover ≅ m004 (review 1 Check 4/F5, run live there);
the 'b-+RL'/'b--RL' trap — a different non-orientable manifold of vol 2·Catalan (recomputed
here: 2·Catalan = 1.83193118835444, matching review 1's 1.8319311884); and F2's det=−1
scope caveat "as recorded in the review". All are executor warnings — none alters a
measurement criterion or a prior.
The v2 re-seal commit e5e482ff touches exactly five files: ARTIFACT_HASHES.txt (+7, the v2
block), EXECUTION_NOTES.md (new), MEASUREMENTS.md (the two hunks), reviews/S16_REVIEW_1.md
(the pinned review entering git), P019 (+11, the erratum) — nothing else in the repo.
Directory sweep (ls -laR incl. hidden; git ls-files; git status --ignored): the arc contains
exactly the four sealed files + reviews/ holding S16_REVIEW_1.md (tracked, digest-pinned)
and this review's own channel S16_REVIEW_2.md (untracked, as review 1's was during its run).
No hidden, ignored, or stray files.

### CHECK 6 — Independent anchor: PASS
ANCHOR (this review, distinct from review 1's m015 anchor): live clock `date +%s` ->
1784670246 (2026-07-21, ~8 min after review 1's anchor 1784669758 — consistent forward
wall-clock), paired with an independent live computation `snappy.Manifold('m022').volume()`
-> 2.9891202829 (a census manifold uninvolved in B749). Verified by grep that neither
'm022', nor 2.9891202…, nor 1784670246 appears anywhere in the arc directory or P019
(absence exit = 1). Not derivable from any sealed file.

---
## SUMMARY
1 F7 correction (three strata; false universal gone; math verified) ... PASS
2 v2 seal (all five digests recomputed; v1 block preserved) ........... PASS
3 EXECUTION_NOTES faithful to cc relay; verification-side only ....... PASS
4 P019 erratum (approved text byte-stable; dated; gated; correct) .... PASS
5 No regressions (two-hunk delta only; warnings match review 1) ...... PASS
6 Independent anchor ................................................. PASS

Review 1's single STOP premise is remedied exactly and minimally: the false identity
"quadratic slopes = exactly the metallic family" is gone from all assertive text, replaced
by the correct three-strata design whose new F7b stratum (witness √3−1, quadratic,
self-similar, non-metallic — every property recomputed in this seat, including the
extremality separation L(√3−1) = 2√3 > √5) turns the caught error into a measured object.
All other v1-PASS premises are byte-stable or strengthened in the permitted
verification-side direction, and the v2 seal is arithmetically exact.

VERDICT: SEAL-READY
