# B649 — TRACK S WAVE 1 BANKED: the silver holonomy, stage 1

**Prereg 429a344c (sealed first, under the campaign seal a463c6aa).
One disclosed method deviation: the prereg named SnapPy's Sage-gated
`find_field`; the conventions block says pyenv-only — substituted with
direct exact-relation verification at two thresholds (the gate
CRITERION unchanged); the full primitive-element minimal polynomial is
deferred to stage 2 under G4's deferral clause (obstruction named:
complex-pslq tooling).**

## Gates

- **S1-G1 PASS.** m136: volume 3.6638623767, homology ℤ/2+ℤ/2+ℤ =
  ℤ ⊕ coker(A−I) for A = RRLL exactly (det(A−I) = −4, SNF (2,2)).
  Presentation ⟨a,b,c | aBAbcc, aaCbcB⟩; peripheral (CCB, caCA).
- **S1-G2 PARTIAL-EXACT PASS** (five relations, residuals ≤ 8e-63 vs
  thresholds 1e-40 and 1e-55): tr(b) = 2; **tr(ac) = −√2 − √2·i;
  tr(abc) = −2√2·i**; s = 2Re tr(a) satisfies s⁴ − 8s² − 16 = 0;
  |tr(a)|² = 2√2. Consequences: **the trace field contains
  ℚ(ζ₈) = ℚ(i, √2)** (the ratio of the two exact traces gives i), and
  s has degree 4 ⇒ the trace field has degree ≥ 8. The prereg's
  disc-32 → √2 expectation: CONFIRMED — and sharpened: the silver's
  arithmetic is mod-8 (ζ₈) from the first computation, exactly the
  2-adic dependence the campaign's B2 hazard note pre-labeled.
- **S1-G3 PASS.** Holonomy generators at ~64 digits; max relator
  residual 8.5e-64 (up to ±I); peripheral traces μ = 2, λ = −2
  (parabolic cusp ✓).
- **S1-G4 DEFERRED** per the clause: exact entry identification +
  the primitive minimal polynomial = stage 2 (complex-pslq / resultant
  tooling; the real quartic s⁴−8s²−16 and ℚ(ζ₈) are the anchors).

## Campaign routing

Stage 2 (registered): the exact field build (a ℚ(ζ₈)-tower or degree-8
field class), the Sym-lift to 27, the E₆ exec-prefix over the silver's
field, peripheral certification — then the silver chord (B648 §B2).
The ζ₈ finding routes to the grammar table NOW: the silver's silence
character runs through mod-8 arithmetic, so the (κ|disc) law's 2-adic
sector is load-bearing for the control, as pre-labeled.

One in-run precision-path bug (double-precision collapse through
python complex) was caught by the two-threshold gate itself and fixed
— the E5 class, caught by design.

---

## Stage 2a (prereg 4dc3eacd) — THE EXACT SILVER HOLONOMY OVER L (G4 closed)

**Result: the m136 holonomy generators are EXACT elements of
SL₂(L), L = ℚ(s, i) with s⁴ = 8s² + 16 ([L:ℚ] = 8, ζ₈ ∈ L):**

- **S2a-G1 PASS** — all 12 entries identified DIRECTLY (no
  normalization needed) from the polished representation at 1200 bits;
  acceptance residual 1e-250 (fitting freedom ~50 digits — spurious
  relations excluded by two orders of magnitude); exact table in
  `entries_L.json`.
- **S2a-G2 PASS (better than the gate)** — both relators evaluate to
  **+I exactly** in L (the gate allowed ±I); det(a) = det(b) =
  det(c) = 1 exactly: an honest SL₂(L) representation, not merely
  projective.
- **S2a-G3 PASS** — all five stage-1 trace relations now SYMBOLIC
  (tr(μ)² = 4, tr(λ)² = 4, tr(b)² = 4, tr(ac)² and tr(abc)² against
  the exact ζ₈-targets, all via the scale-free tr²/det form).

The in-trail record (three runs, each failure caught by an exact
gate): run 1 — 64-digit source left ~40 digits of pslq fitting freedom
and the EXACT det gate caught spurious identifications (preserved as
`b649_stage2a_run1_FAILED.txt`); run 2 — the quotient-ring reduction
carried a sign error (s⁴ = −8s²−16 instead of +8s²+16), caught by the
same det gate (generator b, untouched by s², passed — the E2-adjacent
tell); run 3 — all gates pass. Upstream note: snappy's
`lift_to_SL2C` crashes on multi-torsion H₁ (ℤ/2+ℤ/2+ℤ) — worked
around via `lift_to_SL2=False`; the polished PSL matrices turned out
to BE the SL₂ lift.

**Stage 2b opens:** the 27-lift Sym¹⁶⊕Sym⁸⊕Sym⁰ over L (even Sym
powers — works for any det-1 source directly) and the E₆ exec-prefix
over L; then the silver chord (campaign §B2).

---

## Stage 2b (prereg 34f851b1) — THE SILVER 27-LETTERS EXACT OVER L

**Foundation fact (sealed in the prereg): B575's E₆ apparatus is
RATIONAL** — the cubic's 270 entries are ±1, the principal sl₂ has
rational entries — dumped once to `e6_principal_rational.json` /
`cubic_rational.json` (the silver track is now decoupled from the
fig-8 prefix build). Consequence: the silver chord runs over
L = ℚ(s, i) alone.

**All three gates PASS (exact):**
- **S2b-G1** — both silver relators evaluate to I₂₇ EXACTLY in
  GL₂₇(L) on the Bruhat-lifted letters (6 lifts, ~1.5 s each; the
  relator products ~5 s — the sparse-skip multiplication made the
  degree-8 arithmetic cheap).
- **S2b-G2** — cubic preservation C(gx,gy,gz) = C(x,y,z) exactly on
  all 25 declared sample triples (seed 649): the lift lands in E₆.
- **S2b-G3** — tr₂₇(μ) = tr₂₇(λ) = 27 exactly (parabolic sources ⇒
  unipotent 27-images; the sign dies in even Sym powers).

The lifted letters persist in `letters27_L.json` (the stage-3 input).

**Stage 3 opens (the campaign GATE B's blocker, now in reach):** the
silver double — the gluing/weld solve over L, h¹(D_silver; 27) by
amalgam-Fox (SIX generators: the silver presentation has three), and
the Y-tensor with the FORM-level law checks (the campaign §B2's
form-level reproduction: the core-law shape, the cross-ratio, the
silence character with disc 32).
