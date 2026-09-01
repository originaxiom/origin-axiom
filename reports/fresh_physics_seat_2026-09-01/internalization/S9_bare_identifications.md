# S9 — THE BARE IDENTIFICATION CANDIDATES (internalization sweep digest)

Seat: internalization sweep reader, 2026-09-01. I digest and flag; I judge nothing dead or proved.

## 0. Provenance of the candidate list — NOT COMMITTED, but deterministically regenerable

The B1231 arc directory (`frontier/B1231_identification_discipline/`) contains only three files:
`FINDINGS.md`, `arc_verdict.json`, `CITATION_VERIFICATION_2026-09-01.md`. **The sweep's candidate
list (the "61 candidates, 52 BARE" of phases A+B) is not committed as an artifact anywhere I could
find** (searched `frontier/B1231_*`, `docs/`, `scripts/checks/`, repo-wide filename and content
grep). It is, however, a pure function of the committed `arc_verdict.json` corpus via
`scripts/checks/identification_audit.py --extract/--triage`, so **I regenerated it on this bench**
(imported the module, dumped all hits untruncated to 220 chars — the script itself caps stored
sentences at 220 chars and prints only 25/15 samples).

**Regenerated counts: 63 total — 3 MAP-language, 6 TYPING-language, 54 BARE.** The banked claim is
61/3/6/52. The discrepancy is exactly accounted for: **B1231's and B1232's own `claim_one_line`
fields postdate the sweep and both land in the BARE pile** (B1231's hit is its quotation of the I-6
error; B1232's is the methodological verb "identify the raw choice space"). 63−2 = 61, 54−2 = 52.
The banked numbers were honest at sweep time; the pile grows with the corpus by design.

Instrument caveats the evaluator must carry (asserted in the tool's own selftest, verified passing
on this bench): the net catches only explicit correspondence constructs ("identified with",
"the same", "dictionary", "coincides with", "≡", …) inside `claim_one_line` **only** — it reads
no FINDINGS.md, no docs. **It misses bare "X IS Y"** (the C-5b phrasing) and anything living
outside the one-line claim. So this pile is a lossy sample, not coverage; B1231 says so itself.

## 1. The ledger itself (`docs/IDENTIFICATION_LEDGER.md`, 7 rows, read in full — 37 lines)

- **I-1 EARNED** — 2T ↔ affine E₆ Dynkin (McKay). A theorem: the rep graph *is* the diagram (B266/B727).
- **I-2 EARNED** — the object's SL(2,ℤ) trace-map action ↔ N=2\* class-S S-duality (B150), literature-confirmed.
- **I-3 EARNED** — Vol(m004) = (3√3/2)·L(χ₋₃,2) (B680), a 40-digit identity.
- **I-4 REFUTED** — CS(m004) ↔ θ_QCD (B813): dead on type, a functional value cannot fill a coefficient slot.
- **I-5 REFUTED** — V₄⋊S₃ ↔ D₄ triality (B1223): the template — map existed, action trivial.
- **I-6 UNEARNED** — π₁(m004)↠2T ≡ the transverse ALE Γ (B1228): two different 2T's; earn = one construction where the same 2T plays both roles.
- **I-7 UNEARNED** — the object's ℤ/3 ≡ the boundary CFT's |P/Q| module group (B1230 C-5b); earn = show the trinification/Galois ℤ/3 *is* the group permuting {1,27,27̄}. **B1232 sharpened it**: Gal(ℚ(ζ₃)/ℚ) is order **2**, so part of the claim conflated a ℤ/2 with a ℤ/3.

Baseline (`docs/IDENTIFICATION_BASELINE.json`): unearned = 2, rows I-6/I-7, total_rows 7. The gate
is a ratchet (UNEARNED may not increase), deliberately not a hard block. B1232's verdict declares
I-7 (status UNEARNED, sharpened note) — the declaration mechanism is being used post-B1231.

## 2. The BARE pile, grouped by downstream load (all 54, 1–3 sentences each)

Method note (coverage honesty): for each candidate I had the flagged sentence + arc verdict + the
live board; I read full `claim_one_line` for six load-bearing arcs (B964, B267, B260, B1012, B1089,
B1000) and did **not** open the other arcs' FINDINGS or trace per-arc downstream citations
exhaustively. Tier placement is my read of the live board (CAMPAIGN_STATUS B1216–B1232 era), not a
verdict.

### TIER 1 — load-bearing on the live chain (σ headline, E₆ chain, parameter count)

- **B1034 (PROVED)** — the stage CFT ≡ the AdS₃ boundary CFT of the object's own quotient (L154).
  The single biggest bare identification in the record: everything holographic (c = 6σ, the σ menu,
  B1229/B1230's whole consistency campaign) routes through it. Honestly carried as NO-EXHIBIT /
  UNDECIDED, re-affirmed by B1231's net. Earn: exhibit the duality map (quotient gravity ↔ stage
  CFT) and show it acts — e.g. on characters/partition function — not just matched central charges.
- **B1012 (PROVED)** — the CS normalisation dictionary: Brown–Henneaux c = 3l/2G + σ = l/4G + the
  on-shell action close exactly, "c = 6σ FORCED NOT ASSUMED." The closure is internally exact, but
  the whole dictionary presupposes B1034's unexhibited holographic identification — c = 6σ is
  forced *inside AdS₃/CFT*, and whether the object IS that is the L154 debt. Note also: **B1226
  refuted B1012's part (1) chain** (blind-to-k ⟺ CS = 0 ⟺ amphichiral broken at the second link,
  both directions; corrected to blind-to-k ⟺ complex volume real) — the arc still reads PROVED;
  the evaluator should check whether B1012's own surfaces carry the B1226 correction.
- **B267 (PROVED)** — "the arithmetically-selected E₆ and the character-variety E₆ are the same Lie
  object, the McKay exponent set **matching** the tangent-space grading." Evidence type is exactly
  what the B1231 rule disallows (matching exponent sets). This is the coherence node gluing the two
  E₆ appearances the whole chain leans on — and B1228's σ = 1 retraction already showed the two
  E₆-sources (McKay-on-2T vs geometric CS boundary, which is A₁) can come apart. I-6's exact
  species, one floor up. Earn: a map carrying one E₆ to the other with a faithful action.
- **B260 (PROVED)** — the SL(2,ℂ) character variety ≡ the Coulomb branch of T[4₁], "A-polynomial
  verified, dissolving wall #1." Downstream: the entire class-S frame (and the context of EARNED
  I-2). The A-polynomial equality is a real computed invariant check but is still number-matching
  under the strict rule; the DGG-type map exists in literature. Earn: cite/exhibit that map and
  its action, upgrading the check from invariant-match to map-and-action.
- **B964 (RETRACTED) + B1000/B978/B990 downstream** — "'adjoint VEV' and 'measurement/centralizer'
  are THE SAME OPERATION." Stabilizer-of-adjoint-vector = centralizer is standard Lie theory; the
  bare half is the *physics* glue (the object's measurement operation ≡ a GUT adjoint VEV). Note
  carefully: B964's verdict is RETRACTED but the retraction is of two *earlier* claims — this
  identification is asserted **as the correction inside the retraction arc**, and it is used
  downstream (B990 "the same operation as L133/L134/L138", B1000's charge-sector closings, B978's
  mass mechanism). Earn: a map from the measurement/centralizer datum to a VEV in a specified
  representation, acting on the breaking pattern, not the slogan.
- **B1089 (PROVED) + B1139 (PROVED)** — the h¹-to-mode identification "is the CS/AW dictionary
  (CITED not proven)"; B1139's state-name likewise "labels a CITED dictionary on exact rows." The
  matter-card synthesis (27-cohomology IS the matter content) rests on a literature dictionary
  imported, self-fenced as cited. Earn: verify the CS/AW correspondence for this instance, or price
  it as an explicit external input on the ledger.
- **B1145 (PROVED)** — "'the generation's seat closes on-object' is the programme's THESIS reading
  (the object's-geometry → physics identification the programme is trying to earn), NOT a theorem."
  This is the global bare identification, self-declared as thesis — the honest umbrella over the
  whole pile. Nothing to earn locally; it is the programme's endpoint.
- **B1182 (PROVED)** — the arrow ≡ r (the B716/B721-era reversal element as the arrow's algebraic
  seat). Downstream: every arrow-of-time/orientation statement (B1183, B1163 era). Carries its own
  guard ("if the arrow is ever re-identified with a different ℤ/2 the instrument re-runs") but the
  identification itself is conventional, not mapped. Earn: show the dynamical arrow's action and
  r's action agree equivariantly, not that both are order 2.

### TIER 2 — mid-load: banked spine pieces, pattern-level glues, deferred identifications

- **B1114 (PROVED)** — I1's principal JM triple "commutes with the hatch triple and is the SAME
  class" at the A₂ landing; the joint-centralizer crux follows. If "same class" was computed
  (conjugacy exhibited) it is earned in-arc; if read off matching labels it is I-5's species.
  Evaluator: check the arc's computation.
- **B1120 (PROVED)** — C₀ = 3^{−1/4} = |disc|^{−1/4} as "the k = 0 instance of a genuine arithmetic
  pattern continuing at k = 1,2 — the adelic dictionary is a THEOREM-GENERATOR." A three-point
  pattern promoted to a dictionary. Downstream: the tower arithmetic story (B1130/B1133 single-end).
  Earn: a proof that C_k equals the adelic expression for all k, or an explicit fence at k ≤ 2.
- **B1134 (PROVED)** — "B1114's 'signature is the observer's' and B1127's 'compact color is the
  observer's' are the SAME single closing." Glues two closings into one; if leaned on for the input
  count, the common mechanism needs exhibiting, not the shared slogan.
- **B271 (PROVED)** — the amphicheiral τ-breaking locus identified with the E₆-irreducibility locus
  ("the 26 = e₆/f₄, exponents {4,8}"). Number-flavored evidence on a wall-#4-adjacent claim; earn:
  the locus equality as sets/schemes with the map exhibited.
- **B348 (PROVED)** — at the Eisenstein point the duality involution z↦1−z "coincides with" Galois
  conjugation, so amphichirality "self-identifies." A pointwise computed coincidence carrying an
  identification-shaped conclusion; earn: the intertwining map on more than the fixed point.
- **B601 (PROVED)** — the odd trace law "coincides with B587's LAW-O" — agreement on 14 κ-points
  including 2 registered predictions. Strong for a numeric law; still agreement-of-values, not an
  identity proof. Earn: closed-form derivation of one law from the other.
- **B236 (PROVED)** — ordinary and super TCI cosets "are literally the same coset," sweep-confirmed
  unique. Computed-in-arc; low residual risk; kept here because "literally the same" carried by a
  sweep is enumeration, not a map.
- **B74 (PROVED)** — the W_N charge-conjugation grading and the Dickson P-grading "are literally the
  same involution −w₀." This one names its map (−w₀) inside the sentence — arguably the closest to
  EARNED in the whole BARE pile; a Phase-C quick win.
- **B962 (PROVED)** — "it is THE SAME GAP EVERY GUT HAS." A literature-comparative identification
  used to reframe the 27-half shortfall as generic. Earn: a cited/verified statement that standard
  E₆ GUTs face the type-identical gap (partially touched by B964's own correction).
- **B1175 (OPEN)** — explicitly "NOT yet identified with B1141's beat-selected sign lift" — a
  *deferred* identification, queued to the spin thread. Model discipline; no debt yet, listed so
  Phase C finds it when the spin thread lands.
- **B1000 (PROVED)** — flagged sentence carries "B990 showing it is the same operation as
  L133/L134/L138" — the measurement≡VEV glue again (see B964 above); the charge-sector
  two-closings count leans on it.
- **B978 (PROVED)** — the adjoint-half/27-half statement "now also a statement about MASS" — an
  extension of the B964-species identification into the mass mechanism.

### TIER 3 — internal consolidations and computed identities (low glue risk: both sides live in the same structure, or the equality was computed in-arc)

- **B1033** — the 6+2+8 cross-cut "is the same fact from the so(10) side" (branching recomputation).
- **B1074 (OPEN)** — the frame-blind vacuum block is "literally the same rational matrix" across frames — a computed matrix equality.
- **B1181 (OPEN)** — "the retraction and the confirmation are the same computation pointed in opposite directions" — rhetoric about one computation.
- **B1183 / B1191 (PROVED)** — the no-self-closure and orientation obstructions unified; B1191 calls it "a proved finite-case correspondence" — proved in-arc.
- **B1199 (PROVED)** — R8 "the same shape at different levels," self-typed as *pattern-level* — honest labeling; becomes a debt only if later cited as more than pattern.
- **B1208 / B1212 (OPEN)** — entry-for-entry confirmation of Memo 123; codex certificate "REPRODUCES, output identical" — verification claims, computed.
- **B1218 (PROVED)** — "the SAME lock on a SECOND surface" — doc-maintenance.
- **B1227 (PROVED)** — B1224 and B1225's keystone "the same statement in different value groups" — the arc's own theorem, and B1231 itself classifies B1227 as a *typing* success.
- **B534** — a proved biconditional (dark-hyperbola theorem).
- **B543 / B546** — measured IDS gap labels reproduce the internal degree-4 / ℚ(√φ) dictionary at stated precision — computed reproductions of an in-house dictionary.
- **B595** — the seven-row dictionary with two confirmed blind predictions — has discriminating tests.
- **B624** — the odd hearing trace "is the same twelve-term Weil coset Gauss assembly," zero exceptions κ = 4..24 — computed on the stated range.
- **B705** — metallic-tone audibility iff the weld field is real — computed criterion.
- **B889 / B896** — the across-breakings dictionary dissolving into Π-blocks; Hungarian-aligned frames — in-arc computations on one object.
- **B946** — e₃(V)/λ⁴ = 27 and B941's headline "THE SAME FACT reached two ways" — exact integer agreement of two computations.
- **B956** — quotes B582's own proof to locate a tension — reading, not gluing.
- **B976** — "the same leak one level up" — meta-claim about summarization.
- **B255** — uniqueness sweep over regular simplices, riding the McKay theorem (I-1).

### TIER 4 — no live debt: banked negatives, refuted dictionaries, or false-positive hits

- **B145, B411, B52, B541, B558, B1096 (all NEGATIVE)** — dictionaries tested and killed (γ′-field, PC12, 17-component, three-level SM-absence) or structurally unanswerable; these are the discipline working, banked.
- **B23 (OPEN)** — "no BKL/Misner dictionary is derived" — an explicit non-claim.
- **B1226 (PROVED)** — hit is its reference to B813's refutation standing — no new identification.
- **B1155 (OPEN)** — hit is a citation of B682's Vol dictionary = **EARNED I-3**.
- **B1231 / B1232** — post-sweep self-hits: B1231 quoting I-6, B1232's closure-test verb. Already ledgered/declared.

## 3. The u-map (listener) case, in detail

B1231's sharpest structural claim: **the listener map u IS an identification map, performed
implicitly and for free for two years; pricing it is the crossing cell.** The record around it:

- **What u is** (`docs/LISTENER_MAP_SPEC.md`, L166): the hearing instrument evaluates
  h(g) = u†M_odd(g)u on C²_odd ⊂ C⁶ (SU(3)-level-2 weight space, ⟨R,L⟩ ≅ 2T×2I, order 2880).
  Every hearing result (B593/B856/B1011 and the whole tone corpus) was taken at exactly two
  vectors u₃, u₆ — and the spec states in caps: **"THIS CHOICE IS GIVEN, NOT DERIVED"** (B1011 C5
  excludes deriving it; B1066 names the gap: "which physical apparatus is which listener state u
  remains unconstructed").
- **What has been earned**: the *classifier* Λ (which u's are admissible from field data alone) was
  posed (L166, AC4 demoted / AC4′ discrimination installed by the bench repair) and then
  constructed and sealed — GRAND_COMPUTATION_LEDGER I1: **Λ = "the minimal exceptional orbit's
  Galois-fixed directions" → exactly {u₃, u₆}, PROVED, three independent re-implementations,
  AC1–AC6 closed on the odd channel (B1070–B1073)**. So the two-year convention is now
  field-licensed *as a menu*.
- **What remains bare**: the second half — physical apparatus ≡ listener state u — is exactly the
  cross-structure glue the ledger's rule governs, explicitly not licensed by the spec (F1/F7, G9).
  The one *value-level* attempt at it is closed **null**: B1128 P-INSTRUMENT (the listener-map
  coupling predicts |U_e1|/|U_e2| = φ, misses ~5σ) and B1132 (null on the whole ℂP¹_odd; the
  instrument route "exhaustively closed"), with the exact golden-meridian law h(R²L²,u) =
  −φ·h(RL,u) − iφ·n_y(u) as the side-yield.
- **The ledger gap (red flag below)**: despite B1231's own FINDINGS elevating u to "an
  identification map performed for free," **u has no row in the IDENTIFICATION_LEDGER** — the
  ledger stops at I-7. An UNEARNED u-row would raise the count to 3 and red the ratchet at
  creation; the baseline's own note says new UNEARNED rows *should* red at creation. As written,
  the programme's self-named largest unpriced identification is tracked in prose, not in the
  register built for it.

## 4. Red flags (for the evaluating seat; I judge none of them)

1. **The sweep candidate list is not committed** — the banked "61 candidates / 52 BARE" is
   reproducible only by re-running the instrument (I did; it reproduces modulo the two post-sweep
   arcs). A one-file JSON dump would make the phase-A/B result auditable without execution.
2. **The u-map has no ledger row** despite B1231's FINDINGS declaring it *the* identification map
   performed for free — the register's founding arc exempted its own largest example, and adding it
   now would trip the very ratchet B1231 installed (baseline unearned = 2).
3. **B267's earned-by-matching phrasing** ("McKay exponent set matching the tangent-space grading")
   sits at PROVED while being the rule's textbook disallowed evidence — and B1228's σ = 1
   retraction already demonstrated the two E₆-sources can come apart. Phase C should hit this row
   first.
4. **B1012 reads PROVED end-to-end while B1226 refuted its part-(1) equivalence chain** at the
   second link (live board, 2026-08-31); and its part-(2) "c = 6σ forced" is forced only inside
   the holographic identification B1034 leaves NO-EXHIBIT. Check B1012's surfaces carry the fence.
5. **B964's identification lives inside a RETRACTED-verdict arc as the correction** — the
   "adjoint VEV ≡ measurement/centralizer" glue is downstream-active (B990/B1000/B978) but its home
   arc's verdict string is RETRACTED, which any verdict-level reader will misfile in either
   direction.
6. **The instrument's blind spot is load-bearing for this very digest**: BARE-pile membership is
   claim_one_line-only and misses bare "X IS Y" phrasings — the pile above is a floor, not a census
   (B1231 says this itself; repeated here so S9 is not read as coverage).

## Coverage modulus (exact)

READ IN FULL: `docs/IDENTIFICATION_LEDGER.md` (37 lines, whole file);
`frontier/B1231_identification_discipline/FINDINGS.md` and `arc_verdict.json` (whole);
`scripts/checks/identification_audit.py` (whole, 206 lines); `docs/IDENTIFICATION_BASELINE.json`
(whole); `docs/CAMPAIGN_STATUS.md` lines 1–120 (B1225–B1232 entries); `docs/LISTENER_MAP_SPEC.md`
lines 1–60 plus its §1.1 statement block; WORKING_RULES.md lines 233–239 (the Identification
Rule); full `claim_one_line` for B964, B267, B260, B1012, B1089, B1000; B1232's `identifications`
field; grep hits on "listener" across docs/ (CAMPAIGN_STATUS 1054/1595/2628/2632/2634,
GRAND_COMPUTATION_LEDGER I1 line, CROSSING_REQUIREMENTS 111–129, FIELD_EXPLORATION_REPORT 21–89).

REGENERATED: the full 63-hit sweep (sentences stored at ≤220 chars by the script itself — I saw
each hit's flagged sentence to that cap, printed at 200).

NOT READ / SKIPPED: `frontier/B1231_.../CITATION_VERIFICATION_2026-09-01.md` (its content is
summarized in FINDINGS' citation-debt section, which I did read — the MMS/Anderson-Moore detail
here is second-hand from FINDINGS); the FINDINGS.md of the other 53 BARE-pile arcs (tier placement
for those rests on flagged sentence + verdict + live board only); per-arc downstream citation
tracing (not done except where the live board or the six full claims state it); the P3 paper
itself; `docs/RETRACTIONS.md` beyond the B964 header line; the rest of CAMPAIGN_STATUS (>120);
`tests/test_b1231_identification.py`. The selftest was run: CONTROLS PASS, blind-spot control
included.
