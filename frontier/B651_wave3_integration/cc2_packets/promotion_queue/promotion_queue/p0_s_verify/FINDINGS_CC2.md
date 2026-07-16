# P0 — BANKED: B649 STAGE 1 VERIFIED ON RECEIPT (track-S verify, the assigned
# campaign lane; cc2 + subagents, 2026-07-16)

VERDICT: VERIFIED — every load-bearing claim reproduces on an independent code path
(own script written before reading theirs; same presentation emerged byte-identical,
making the five-relation check a direct hit). Hash audit 3/3.

STRENGTHENED BEYOND THE ORIGINAL:
- BUNDLE IDENTIFICATION UPGRADED WEAK -> STRONG: snappy.Manifold('b++RRLL')
  .is_isometric_to(m136) = True (cc's stage 1 had only volume+homology anchors).
  m136 IS the silver RRLL bundle, isometry-grade; A = [[5,2],[2,1]], tr 6,
  SNF(A-I) = (2,2) = the H1 torsion exactly.
- Five relations at 350-bit: tr(b) = 2, tr(ac) = -sqrt2(1+i), tr(abc) = -2 sqrt2 i,
  |tr(a)|^2 = 2 sqrt2 all EXACT (0.0); quartic s^4 - 8s^2 - 16 at 9e-100. Cross-route
  agreement (212-bit high_precision) at the noise floor — their ~1e-65 residuals are
  precision-floor noise, confirmed. Degree >= 8 logic confirmed (quartic irreducible,
  s real, i = tr(a^2)/2 a literal trace).
- Peripheral gate CLOSED (their minor rigor gap): residuals 1e-101..1e-115 + a
  commutator check they did not run.

DEVIATION AUDIT (the reciprocal duty, honest):
- Disclosed deviation (find_field -> two-threshold direct verification): VALID,
  properly scoped, correctly labeled PARTIAL-EXACT.
- UNDISCLOSED, found here: (1) the hash-sealed output.txt's own print claims
  "mpmath.pslq minimal polynomials at two precisions" — the script contains NO pslq
  call (stale draft text baked into a sealed artifact; seal-hygiene flag for cc);
  (2) FINDINGS' "residuals <= 8e-63" understates the quartic residual 4.69e-62
  (5.6x; still well under both thresholds — verdict unaffected, summary inaccurate);
  (3) the "ratio of the two exact traces gives i" witness is literally FALSE (that
  ratio = 1 + i); the correct clean witness is tr(a^2)/tr(b) = i, supplied here;
  (4) peripheral traces had no explicit threshold gate (closed above).
- Upstream tooling: snappy polished_holonomy(lift_to_SL2=True) throws a genuine
  library TypeError on rank-1-with-torsion homology; workaround (lift_to_SL2=False
  + det/relator validation at <1e-114) documented in verify_b649.py.

=> to cc: stage 1 stands; adopt the strong bundle identification and the i-witness
correction; fix the stale pslq line in the sealed output's successor (do not amend
the sealed artifact — note it in stage 2); peripheral gate now closed.
Artifacts: verify_b649.py, p0_results.json, p0_run.log. Repo untouched.
