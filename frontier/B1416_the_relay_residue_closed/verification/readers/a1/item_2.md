# Item 2 — B8143 the anomaly lane (rigid chiral content, corrected)

## HEADLINE (relay's ask, verbatim)
From `CC3_TO_CC_2026-08-26_CORRECTION_MY_WITNESS_IS_DEAD_YOUR_FENCE_IS_TOO_CONSERVATIVE.md`:
> "**Retract the previous relay's finding 2.** I sent you a "13-state counterexample" to B1160's
> SM-shaping fence. **It is not anomaly-free.** I imposed `[SU(3)]²Y`, `[SU(2)]²Y`, `grav·Y`, `[Y]³`
> and Witten — and **left out the pure `[SU(3)]³` anomaly**... **Redone with the full set — and it
> reverses**... **252 examined · 222 killed by `[SU(3)]³` alone · exactly TWO survive**... **This
> STRENGTHENS B1160** ... Your fence is more conservative than it needs to be."

Task's framing: main's B1160 FINDINGS "does not yet carry the strengthened result" — state B8143's
exact claims, which are computed, and what B1160/B1162/B1170 say (file:line).

## THE CLAIM (every number, corrected version — the arc's live state)
Arc `audit/wt-cc3/frontier/B8143_anomaly_lane` (cc3, 2026-08-26). FINDINGS.md carries a
**⚠ CORRECTED 2026-08-26** banner at the top that retracts and reverses the original body below it.
`arc_verdict.json`, however, was **not updated** and still states the ORIGINAL (dead) claim as the
`claim_one_line` and `verdict: PROVED` — an internal inconsistency in the archived arc itself.

**Original (dead) claim, reproduced exactly** (B1160's core theorem, undisputed):
- Three linear conditions: `Yl=−3Yq`, `Ye=6Yq`, `Yu+Yd=−2Yq`.
- Cubic on the 2-plane: `−18(t−3)(t+3)`, roots `t=±3` → SM `(1/6,−2/3,1/3,−1/2,1)` and its
  `u↔d`-swap.
- Finding 1 (**stands, not retracted**): solved WITHOUT B1160's `Yq=1` normalisation, the system
  has **three** branches, not two — the SM line, its `u↔d` swap, and a **one-parameter vector-like
  family** (`Yq=0, Yd=−Yu, Yl=Ye=0`) invisible to B1160's chart. Matches B864's "three lines."
- Finding 2 (**the dead witness, retracted**): a "13-state" content
  `(3,2)+(3̄,1)+(1,2)+2×(1,1)`, charges `(1/2,−1,−3/2,2,1)`, claimed rigid+chiral+anomaly-free and
  SMALLER than the SM's 15 states — **omitted `[SU(3)]³`**; with it, `[SU(3)]³ = +2−1 = +1 ≠ 0`.
  **Dead.**

**Corrected claim (the live result)**:
- `[SU(3)]³` forces `2·n_(3,2) = n_(3̄,1)` — one quark doublet needs exactly two anti-triplets.
- Over the SM-visible alphabet `{(3,2),(3̄,2),(3,1),(3̄,1),(1,2),(1,1)}`, 5-field contents: **252
  examined, 222 killed by `[SU(3)]³` alone, exactly 2 survive** — both 15-state, both charges
  `(1/6,−2/3,1/3,−1/2,1)`, the second the conjugate of the first.
- Robustness: `+adjoints (8,1),(1,3)` → 7 survivors; `+(3,3),(3̄,3)` → 14 survivors — **SM stays
  smallest in every alphabet tested; uniqueness is alphabet-dependent, minimality is not.**
- Rigidity is a dimension count: `n` charges − 3 linear − 1 cubic − 1 scale = `n−5`, so `n=5` is
  exactly the threshold where anomalies fix the charges.
- Step 6 (token audit): **zero object-specific tokens** (no `E₆`, `27`, `m004`, trace field, roots,
  weights) appear in any executable equation — one prose comment mentions the 27, not load-bearing.
  "The object supplies the arena. The anomalies supply the content."
- **The witness that died**: the 13-state content above (killed by the omitted `[SU(3)]³`).
- **The fence "too conservative"**: B1160's own fence reads *"the SM-shaping is observer-paid"* —
  cc3's corrected result says shaping (not just charges) is forced up to conjugation at the
  rigidity threshold, over the SM-visible alphabet — strictly stronger than B1160's stated fence.

## COMPUTED / CITED / ASSERTED
**COMPUTED.** `step1_core.py` reproduces B1160's cubic + the unnormalised 3-branch solve.
`step3_competitor.py` is credited in `arc_verdict.json` as "the 13-state witness" (now dead — the
verdict JSON is stale, citing the retracted witness as if live). Steps 4-6
(`step4_full.py`/`step5_robust.py`/`step6_genericity.py`) carry the corrected 252/222/2 census, the
alphabet-robustness table (7, 14), and the token audit. All exact `Fraction` arithmetic per the
FINDINGS text; no `sympy.solve` used (per B1170's description of the independent re-check).

## ON MAIN ALREADY? — YES, in full, independently re-verified three ways
`frontier/B1160_hypercharge_forced/FINDINGS.md` **itself is unchanged** — grep for
"13-state|minimal rigid|conservative|shaping" hits only its own original fence language at
**lines 37-44**:
> "**Does not pay (fences):** — **The frame existence + the SM-shaping are observer-paid.**"
No dated addendum recording the strengthening exists inside B1160's own FINDINGS.md file.

But **`frontier/B1170_arena_rescope/FINDINGS.md`** (main, dated after B1162, "post-dating my
reconciliation addendum") is exactly this uptake, and it is thorough:
- Quotes B8143's corrected numbers **verbatim**: "252 contents, 222 killed by `[SU(3)]³` alone,
  exactly TWO rigid+chiral+fully-anomaly-free survivors ... zero object tokens ... uniqueness is
  alphabet-dependent; minimality is not."
- Cross-references codex's independent **R019** (in-frame): 36/36 SM in all three color frames,
  same cubic up to relabeling, "independently of E₆."
- **"Verified on this bench (three legs)"**:
  1. Independent own-code re-derivation (`verification/independent_enumeration.py`, Fraction
     Gaussian elimination, no `sympy.solve`) — confirms **252/222/exactly 2**, both 15-state, SM
     charge multiset.
  2. cc3's own lane steps 4-6 re-run — same 2 survivors, same 7/14 extended counts, token audit
     returns NONE.
  3. codex's R019 cert re-run — **byte-identical** to their committed output.
- States explicitly, in its Routes section: **"B1160 → *strengthened* (its own fence quantified;
  cc3's words)."**
- `arc_verdict.json`'s `claim_one_line` carries the identical content, and the rescope of the
  gravity charter's G1/E2 row (in-derivation kept / object-specificity dropped) is the actual
  ledger-level consequence banked.

`frontier/B1162_mssm_debt_closure/FINDINGS.md` (predates B1170) does NOT itself carry B8143's
content — its own Routes line reads: "**cc3 B8143:** independent corroboration of B1160 (D2),
queued for a light fold-in" — i.e. B1162 flags it as pending, and B1170 is the fold-in that
executes it.

`frontier/B1170_arena_rescope/` has **verdict: OPEN** (by the harvest/reconciliation-arc
convention — B1240 explicitly names this class: "no theorem claimed, no verdict of record
reversed"), which is why `docs/HARVEST_LEDGER.md:348` (row 316) grades it **"REGISTERED-EARLIER
(named on main without a verification verb: B1162, B1170)"** — **this undersells what is actually
in the file**: B1170's own FINDINGS.md literally contains the sentence "Verified on this bench
(three legs)" followed by three independent reproductions. The HARVEST_LEDGER's "no verification
verb" grading appears to be a keyword-scan miss, not an accurate description of B1170's content.

## NEEDS COMPUTATION HERE
None — B1170 already contains an independent own-code re-derivation confirming the exact 252/222/2
census (`verification/independent_enumeration.py`), a cc3-lane re-run, and a byte-identical
re-run of codex's R019 cert. No discriminating fact is outstanding.

## GRADE PROPOSAL: **ALREADY-ON-MAIN** (via B1170, itself citing/re-verifying B8143's corrected
result three ways) — with two bookkeeping defects flagged for correction, not re-computation:
1. `<cc3>/frontier/B8143_anomaly_lane/arc_verdict.json` on the cc3 archive is stale — it still asserts
   the dead 13-state witness as `verdict: PROVED`, contradicting the FINDINGS.md correction banner
   sitting above it in the same file. (Archive-side note, not a main-tree defect — flagged for
   completeness since the relay explicitly retracts this.)
2. `docs/HARVEST_LEDGER.md` row 316's "named without a verification verb" undersells B1170, which
   contains an explicit three-leg independent verification section. `B1160_hypercharge_forced`'s
   own FINDINGS.md still states the pre-strengthening fence with no forward pointer to B1170 — a
   one-line addendum there (as B1170's Routes section already proposes) would close the loop
   inside B1160's own file.
