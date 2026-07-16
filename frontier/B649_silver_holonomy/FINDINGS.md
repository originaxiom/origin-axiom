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

---

## Stage 3a (prereg 9db17956) — THE SILVER DOUBLE'S DIMENSIONS: THE 3/5/1 GRAMMAR REPRODUCES

**All three gates PASS, and the discovery is the pattern:**

- **S3a-G1** — the weld intertwiner EXISTS over L (16-dim rational
  solution space; invertible element found; U₂₇ lifted).
- **S3a-G2** — the mirror side's relators = I₂₇ exactly (the
  conjugate-conjugated construction is consistent over L).
- **S3a-G3** — exact dimensions by pure-L elimination (162-dim system,
  ~200 s):

| quantity | silver (m136, disc 32) | fig-8 (disc 5, banked) |
|---|---|---|
| solo h⁰(M; 27) | **1** | 1 |
| solo h¹(M; 27) | **3** | 3 |
| double h⁰(D; 27) | **1** | 1 |
| double h¹(D; 27) | **5** | 5 |

**THE DIMENSION GRAMMAR (3 solo modes / 5 double modes / 1 invariant
section) IS OBJECT-INDEPENDENT across the two computed objects** — the
prereg sealed NO prediction (the values were the discovery), and the
silver, with different trace field, different discriminant, different
presentation rank, lands exactly on the fig-8's numbers. The natural
mechanism candidate: the principal-sl₂ block structure
27 = V(16)⊕V(8)⊕V(0) drives the count (the same blocks on both
objects); registered for the mechanism queue, not asserted.

**Campaign §B2 routing:** this is the first FORM-level reproduction row
for the grammar table — the dimension grammar moves to
witnessed-on-two-objects. h¹ = 5 ≥ 3 ⇒ **stage 3b opens: the silver
Y-tensor** (the certificate machinery over L; the core-law SHAPE, the
cross-ratio, the swap structure — each checked at form level with the
silver's own arithmetic).

---

## Stage 3b-i (prereg 3d0d45f7) — THE SILVER SWAP STRUCTURE REPRODUCES; the invariant sharpened

**Gates: G1–G3 all PASS exactly; G4 delivered with a run-2 correction.**

- **G1** — U₂₇·conj(U₂₇) = +1·I exactly: **J² = +1 reproduces** on the
  silver (the fig-8's sign, not assumed).
- **G2/G3** — σ* maps all five H¹ classes to cocycles; σ*² = id mod
  B¹ (5/5): the antilinear involution (real structure) on H¹(D; 27)
  is OBJECT-INDEPENDENT across the two computed objects.
- **G4 (run 2 — the honest coordinate solve; run 1's
  echelon-coefficient shortcut was frame-mangled and its own G3-proven
  constraint |d| = 1 was the tell, preserved in
  `b649_stage3b_swap_run1_output.txt`)**: the exact 5×5 matrix C with
  **C·conj(C) = I exactly**, lower-triangular in the computed basis,
  diagonal (d₀, d₁, 1, −1, 1) with d₀, d₁ norm-1 elements of ℚ(i) —
  and the headline structural fact: **C is entirely s-free — the
  σ*-matrix is defined over ℚ(i)**, the silver's imaginary quadratic
  subfield (the fig-8's matrix was defined over ℚ(√−3), ITS imaginary
  quadratic field).

**The invariant, sharpened (a precision note that applies to the
fig-8's banked phrasing too):** by Hilbert 90, every norm-1 element of
an imaginary quadratic field is conj(c)/c — so the DIAGONAL entries of
an antilinear involution's matrix are basis-gauge-variant, and
"unit-diagonal" statements (including B638's banked "Eisenstein-unit
spectrum" wording) carry gauge slack. The gauge-INVARIANT content is:
(i) the real structure itself (J² = +1, C·conj(C) = I), and (ii) the
FIELD OF DEFINITION of the matrix — ℚ(ζ₆)-side ℚ(√−3) for the fig-8,
ℚ(ζ₄) = ℚ(i) for the silver. The K020 reading at form level: the real
structure is forced; the imaginary quadratic field is object-chosen.
Routed: a dated precision note for the B638 row (grammar-table
accuracy), NOT a retraction — B638's theorem content (J² = +1, the
law Y∘σ* = conj Y, the phase geometry via the law) is basis-free and
untouched.

**§B2 scorecard so far:** dimension grammar 3/5/1 ✓ reproduced; swap
real structure ✓ reproduced (with the field-of-definition refinement).
Remaining silver input: the Y-tensor (stage 3b-ii, certificates).

---

## Stage 3b-ii (prereg 5dd14ee0) — THE SILVER Y-TENSOR: the §B2 scorecard completes

**G1 (machinery):** the multi-relator certificate engine validated —
δS = ω EXACT on both sides including the certificate paths; **the
silver peripheral commutator has van Kampen AREA 4** (the fig-8's was
2). **G2:** all 10 triples exact (~75 min total; `silver_Y_L.json`).
**G3 verdicts (each a grammar-table entry):**

| form-level row | verdict |
|---|---|
| zero law shape: Y[01k] ≡ 0 | **REPRODUCES** (3/3 zero slots) |
| the Y-tensor's field of definition | **REPRODUCES the subfield law: every Y ∈ ℚ(i)** (s-free), as the σ*-matrix — the chord data lives in the object's imaginary quadratic subfield on BOTH objects |
| σ*-law Y∘σ* = conj(Y) | **REPRODUCES exactly** (spot triples (0,2,3), (2,3,4) with the banked matrix) |
| lit/silent classification | EXISTS on both objects; the silver's unbent weld is **LIT** (Y[024] ≠ 0) where the fig-8's unbent was silent — WHICH class is object-dependent |
| the single-unit core ratio (the fig-8's 24ζ₆) | **DOES NOT reproduce as a universal law** — the three spectator ratios differ (cross-ratios ≠ 1); the crisp ratio is a fig-8-silent-class phenomenon. SCOPE REFINEMENT, not a K3 event: the banked row was always fig-8-scoped ("all nine computed doubles" of THAT object) |
| lit-class deviation structure | the cross-ratio deviations are STRUCTURED: all four deviation numerators share **211**; both components of the first carry **13** (the fig-8's dial prime!); denominators 13- and 211-free — an exact adic statement, silver edition |

**The campaign §B2 silver-control conclusion (GATE B's input, complete):**
the FORM rows — dimension grammar 3/5/1, the swap real structure
(J² = +1, antilinear involution), the zero law's shape, the σ*-law,
and the imaginary-quadratic field-of-definition law — reproduce on the
second object and are candidate FORCED rows for the grammar table. The
VALUE rows — which units, which class (lit/silent), the deviation
primes (13 vs 211-and-13) — are object-chosen: K020 at the chord
level, now witnessed end-to-end on two objects.

HINT rows (recorded, not judged): area 2 → 4 (fig-8 → silver, the
commutator's van Kampen area doubles with disc 5 → 32?); 211 (silver)
vs 13 (fig-8) as dial primes — 13 split in ℚ(√−3), 211 ≡ 3 mod 4 inert
in ℚ(i): the split-prime reading does NOT generalize naively; recorded.


---

## ERRATA (2026-07-16, from the cc2 receipts P0/F4 — verify-don't-trust reciprocal; all verified here before filing)

1. **Stage 1, false witness sentence:** "the ratio of the two exact
   traces gives i" is WRONG — tr(abc)/tr(ac) = 1 + i (verified from
   entries_L.json exactly). The correct clean witness (cc2's, verified
   here): **tr(a²)/tr(b) = i**. The conclusion ℚ(ζ₈) ⊆ trace field is
   UNAFFECTED (1 + i = √2·ζ₈ also generates it with √2 present).
2. **Stage 1, residual summary:** "residuals ≤ 8e-63" understated the
   quartic relation's residual (4.69e-62; still under both sealed
   thresholds — verdict unaffected, summary corrected).
3. **Stage 1, stale prose in a sealed artifact:** the sealed output's
   printed header says "mpmath.pslq minimal polynomials" but the final
   script uses direct relation checks (the pslq text is a stale draft
   line baked into the seal). The artifact's mathematics stands; the
   prose is flagged, not silently rewritten.
4. **Stage 2a, stale comment block:** the script's run-2 comment still
   describes the (superseded) "projective/det-nontrivial" diagnosis
   while its own output shows det ≡ 1 — same stale-prose class.
5. **Stage 2a, rescoping note:** stage 1's deferred "primitive-element
   minimal polynomial" was discharged in stage 2a as product-basis
   ℚ(s, i) identification — mathematically equivalent for every use
   made of it; the substitution is hereby reconciled explicitly.

Practice adopted (routed to the error ledger as the STALE-ARTIFACT-TEXT
class): pre-seal grep of prints/comments against the method actually
executed.
