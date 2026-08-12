# SUPERSESSIONS — the arc graph does not carry what the bodies know

> **Why this exists (B1046).** Two defects, one shape.
>
> **(A) The supersession graph is one-way.** **42 arcs declare `supersedes`; 5 carry the
> back-link.** A reader of `Y.superseded_by` cannot tell a live arc from one its successor refuted.
> **B1037 caught B123 by reading a body; B1043 missed B564 because no body said so** — and the
> graph is the thing that should have said so.
>
> **(B) Self-correcting arcs are unregistered.** **35** `FINDINGS.md` carry a
> `CORRECTION`/`REFUTED`/`WITHDRAWN` banner **below their own headline**; **31** have no
> `docs/RETRACTIONS.md` row, against that file's own rule — *"every future retraction adds its row
> in the PR that banks the correction."* The banners sit at **25–74 %** of the file: **the refuted
> headline is always on top**, and a body-reading pass meets it first.
>
> **The instrument:** `scripts/checks/supersession.py`, gated as **`supersession`**, fail-closed.
> **Triaged, not capped** (B821/B823): it fails only on **untriaged LOAD-BEARING** items — a
> superseded arc still **cited on a curated surface**, or a self-correction whose **verdict is not
> PROVED**. Triaging all 72 would mean writing 72 judgements without reading 72 bodies, which is
> the claim-line sin this instrument exists to name.
>
> **Deliberately NOT automated: the back-links are not written.** `supersedes` conflates
> **REPLACES** with **EXTENDS** — **B142 "supersedes" B141 and B1039 correctly restored both** — so
> auto-filling `superseded_by` would mark live arcs dead.

**Dispositions.** `REPLACES` → the successor invalidates it; **restoring it would re-import a
refuted claim**. `EXTENDS` → both live. `SELF-LABELLED` → the headline already carries its own
withdrawal, so no reader is misled.

## A. One-way links whose target is still cited on a curated surface

*Basis for each judgement is stated. Where it is the successor's own claim line, that is the
successor **asserting the relationship**, which is stronger than a keyword match — but it is not a
body read, and it says so.*

| arc | superseded by | disposition | judgement |
|---|---|---|---|
| `B13` | B14 | **EXTENDS** | B13 is the trace-map linearization's A-sector lattice block; B14 is the uniqueness of `F = LP` as a `GL(2,ℤ)` square root. Different statements. *(claim lines)* |
| `B65` | B80 | **EXTENDS** | B80 *"established from first principles"* what B65 computed — a stronger derivation of the same `J(m)` char-poly factorisation, not a refutation. *(claim lines)* |
| `B111` | B117 | **REPLACES** | B117: *"the 'promotion' is really a Sym-1 absence"* — it dissolves the object B111 counts. **B1037 independently dispositioned B111 ⊂ B117 as SUBSUMED, from the bodies.** |
| `B123` | B125 | **REPLACES** | **The worked case.** B125 *"overturn[s]"* B123's arithmeticity reading; **B1037 read both bodies** and recorded *"DECLINE — RETRACTION, NOT RESTORATION"*, the error being Reid's **knot** theorem applied to **bundles**. |
| `B162` | B163 | **EXTENDS** | B162 fixes `κ = 2` as the unique positive-measure fibre; B163 characterises the `κ < 2` spectrum as Cantor. Complementary. *(claim lines)* |
| `B210` | B212 | **EXTENDS, with a corrected sub-part** | B212 *"correct[s] the assum[ption]"* about `RᵐLᵐ ≡ I mod p` but does not touch B210's McKay-group statement. *(claim lines — the corrected sub-part is not identified here and would need a body read.)* |
| `B259` | B268 | **REPLACES** *(the map, not the theorem)* | B268 is *"wall map v2 — wall #1 dissolved, wall #2 reduced"*. B259's **five-wall map** is superseded; its Mostow/Einstein theorem is not. *(claim lines)* |
| `B273` | B274 | **EXTENDS** | B274 builds on B273's vanishing cup product to conclude smoothness at `ρ_prin`. *(claim lines)* |
| `B496` | B497 | **EXTENDS** | B497 generalises B496's single Thue–Morse trace map to four strata with exact κ-laws. *(claim lines)* |
| `B731` | B734 **and** B794 | **SELF-LABELLED** | B731's own claim line **opens with the withdrawal** — *"The 'figure-eight knot group is non-congruence' headline is withdrawn"*. **Note the two successors disagree on the level** — B734 says `(8)`, B794 says *"exactly `(4)`"* — which is **not a contradiction but the registered `E23` level-convention ambiguity** (SL-kernel vs mod-centre filtration). Both live. |
| `B361` | B367 | **REPLACES** *(the law; not the data)* | **Added B1047, and the gate demanded it the moment B1047's `LAW_MAP` row named B361.** B367's body: *"the local law (B361) is **REFUTED** at pair (3,4) … **fails on the twelfth pair**"* — (3,4) contains no doubly-elliptic seed yet is bright, and the minimal repair dies in the same table because (1,3) has the identical covering pattern and is exactly dark. **B362 is the same law's confirmations and falls with it** (it is not itself a supersession target, so it has no row here — its disposition is in `DEBT_LEDGER` §B300–B499). **The retraction takes the LAW, not the DATA:** B367 says *"its 11 confirming pairs stand as data"*. **Bodies read at B1047.** |
| `B766` | B786 | **REPLACES** *(the third generator)* | B786: *"the third generator is inversion ι, **not** reversal θ (trace-trivial at every rank)"* — it names and replaces B766's third generator. The rank-3 result survives; the generator does not. *(claim lines)* |

### The five this refresh's own restorations put on curated surfaces

**The instrument caught me.** B1039, B1040 and B1044 cited these onto `LAW_MAP`, and every one is
a superseded target — so the gate demanded a judgement. **I have it, because those arcs' bodies
were read at restoration time**, and in each case the successor *extends*:

| arc | superseded by | disposition | judgement |
|---|---|---|---|
| `B141` | B142 | **EXTENDS** | **The worked example for why back-links must not be auto-written.** B142 upgrades B141's *principal* case to a Klein-4 proof; **B141's Item 1 (Q₈ finiteness, rigorous for all n ≥ 3) is untouched**, and B1039 restored **both**, carrying B141's Item-3 slogan correction and B142's missing semisimplicity hypothesis. Auto-filling `superseded_by` here would have marked a live, correct arc dead. |
| `B154` | B157 | **EXTENDS, with a refuted sub-part** | B157 refutes the closed form `k = 4 − m(o−3)` via bronze; **B154's `µ = A⁻ᵐt` derivation and the order-not-rank conclusion survive** and are what B1039 restored. **B154's own body already carries the CORRECTION banner** — it is honest at the site. |
| `B157` | B198 | **EXTENDS** | B198 breaches B157's *"NEEDS-SPECIALIST / needs a real CAS"* wall at SL(5) o=5 — it **removes a limitation**, it does not refute a result. B157's refutation of the closed form stands and B1039 carries it. |
| `B164` | B169 | **EXTENDS, with a corrected sub-part** | B169's P1 corrects **B164's C4** (a point-orbit-norm proxy tracked the naive rather than the dynamical degree). **B1040 restored B169's corrected form explicitly** and said so in its row; B164's C1–C3 (the cubic, the Vieta involutions, the `κ = 2` bridge) are untouched. |
| `B95` | B153 | **EXTENDS** | Already registered in `ERROR_LEDGER` E-adjacent form: B153 found B95's *"forced"* is **conditional on the mult-(n−2) ansatz**, and that non-semisimple irreducibles exist. A scope narrowing, not a refutation. |

> **This is the instrument's first real catch, and it caught its author.** Five superseded arcs
> reached curated surfaces through *this refresh's own restorations*. **All five are genuinely
> EXTENDS** — which is the outcome that vindicates *not* auto-writing back-links, since a
> mechanical rule would have marked all five dead and B141's live Item 1 with them.

## B. Self-corrections whose verdict is not PROVED

*These are the ones where the headline is the first thing a body-reading pass meets and the arc
itself concluded against it.*

| arc | verdict | disposition | judgement |
|---|---|---|---|
| `B408` | NEGATIVE | **REPLACES — and this is the worst case in the corpus** | The body opens *"**THE SEAM DOES NOT CONTRACT — the one scale lever stands** … Ratio ≈ 1.2170 > 1: PERSISTENCE/EXPANSION … the object's single **scale-lever candidate**"* and 27 lines later kills it: *"**CORRECTION** (adversarial panel): the seam **CONTRACTS** — persistence was an artifact … max over embeddings **is biased by embedding count** … NORMALIZED RATIO = **0.7649 < 1** … the object has **NO scale lever in any tested channel**."* **A scale-lever claim is the most firewall-sensitive object in the programme.** The `arc_verdict` is correctly NEGATIVE; **`RETRACTIONS.md` has no row**. **B426 upgrades the correction to a theorem** — survivor and trap sit side by side. **Nothing may restore the 1.217 reading; B408's own gate also voids its 135-level scout numbers (0.02495 / 0.02103 / 0.02135).** |
| `B702` | RETRACTED | **REPLACES** | Headline states *"THE METALLIC-HEARING BIFOCAL LAW: hearing ⇔ real-quadratic swap field"* as a law, with verdict RETRACTED. **Already registered as `E17`** (swap/weld conflation) in `ERROR_LEDGER.md` — so the lesson is carried; **the headline is not.** |
| `B437` | RETRACTED | **SELF-LABELLED** | The headline itself carries *"[RETRACTED AS INHERIT…]"*. No reader is misled. |
| `B385` | NEGATIVE | **SELF-LABELLED** | *"both cheap layers **KILLED**"* is in the headline. |
| `B812` | NEGATIVE | **SELF-LABELLED** | *"**NO PATH**, and the blocking wall is not the one anyone assumed"*. |
| `B331` | NEGATIVE | **SELF-LABELLED** | *"the 'complex escape' is **closed** at its root"*. |
| `B558` | NEGATIVE | **SELF-LABELLED** | *"The three-level **negative**, verified (+ one correction + a named landmine)"*. |
| `B489` | NEGATIVE | **EXTENDS** | *"verified arithmetic, SM …"* — the arithmetic stands; the negative is about the SM reading. Body read not performed; flagged rather than resolved. |
| `B26` | NEGATIVE | **UNINFORMATIVE HEADLINE** | The headline is literally `# B26 -- Findings`. Not misleading, but it tells a reader nothing — a **different, weaker defect**, recorded so it is not re-raised as this one. |

## The backlog, measured and not hidden

> ### ⚠ CORRECTED AT B1047 — this paragraph's own numbers were wrong when B1046 published them.
>
> It read *"72 candidates total; **21** are load-bearing … the remaining **51**"*. **The instrument
> said 26 and 46 on the same tree.** Nothing above changed and no disposition moves; what was wrong
> was the arithmetic *about* the table, published one paragraph below a table that already had
> **25 rows**. **B1046's locks pinned the dispositions and not the counts, so nothing caught it** —
> the next arc's sweep did, which is the same way B1039's B564 miss surfaced. **Recorded rather
> than silently edited:** this is `E37` (self-measurement) in its cheapest form, and the repair is
> the general one — *a number a script can produce should be checked against the script.*

**70 candidates total; 25 are load-bearing** (the gate's scope — **25 findings over 24 distinct
arcs**, B731 appearing twice because two successors supersede it) and all 24 are dispositioned
above. The remaining **45** — one-way links whose target is cited on **no** curated surface, and
self-corrections on **PROVED** arcs — are real but not currently misleading anyone. **They are not
triaged, and the gate does not fail on them.** Recorded here so the number is public rather than
implied.

> **B1048 MOVED IT AGAIN, DOWNWARD, AND THAT DIRECTION IS THE POINT.** Candidates fell **72 → 70**
> and load-bearing **27 → 25** because **B408 and B426 now carry correction banners and
> `RETRACTIONS.md` rows** — so they are no longer *unregistered* self-corrections. **Two of the 31
> this file measured are paid**, by body reads rather than by bulk-writing rows, which is the
> refusal B1046 recorded. The unregistered count is now **29**.
>
> **This number MOVES WHEN THE CORPUS IS CONSOLIDATED, and B1047 moved it in the same commit that
> corrected it.** B1046's instrument reported **26** on its own tree; B1047's `LAW_MAP` row named
> **B361**, which put a superseded arc on a curated surface and took the count to **27** —
> **the gate fired, and the row above is the judgement it demanded.** That is the instrument
> working, not drift: *consolidating a cluster is exactly the act that makes its superseded members
> load-bearing.* The count is now **locked against the instrument** rather than typed
> (`tests/test_b1047_seam_cluster.py`), so it cannot go stale again.

**Maintenance.** A new `supersedes` declaration, or a new self-correction banner, adds its row here
in the same PR — the rule `RETRACTIONS.md` already states and which **31 arcs did not follow**.
