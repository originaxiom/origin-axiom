# Origin Axiom — Roadmap

> ## STATE AT REVIEW 42 (2026-08-09) — stepping back: what the whole body of work is actually saying
>
> **1. The object gives STRUCTURE and withholds VALUES, and the withholding has a mechanism every
> time.** Tier 0 is done (the object is forced up to one bit; A7 *is* that bit, and B979 showed it is
> where φ enters). Tier 1 is substantially done and contains every positive result: the **global ℤ₆
> form DERIVED** (B862 — *the SM itself cannot fix it*), the **hypercharge direction DERIVED** (B864),
> **u(1)³ = span(Y, χ, ψ) COMPUTED** (B992, no longer inferred), the algebra, the generation count.
> **Tier 2 has zero results and, since B1005, no live candidate.** The three sealed crossings failed
> by three *different* named mechanisms, and the obstructions are theorems, not bad luck: values are
> **frame-relative** (B936), centralizers **preserve rank** (B952), chirality is **not self-supplied**
> (B713/B760).
>
> **2. The gaps are not a list — they are a BUDGET.** B1000 measured the external inputs: **five
> closings over four incompletenesses**, with **charge taking two** (a chirality sign *and* a
> rank-reducing VEV). **B963 then proved those two COMPETE**: τ ≠ id *is* the 27's complexity **and**
> τ is the only rank-reducing involution — **spend it on rank and you lose the chirality.** Two
> resources, one budget. This is the sharpest structural fact the programme holds about its own
> incompleteness, and it is why the missing pieces cannot be closed one at a time.
>
> **3. The reframe that lands this window, and it changes what confirmation could even mean.**
> **B996: reaching E₆ is GENERIC** — five of seven metallic grammars surject onto 2T, two-thirds of
> the family — and the arc states the consequence in its own words: this **"REMOVES THE ENDPOINT'S
> POWER TO CONFIRM THE BEGINNING."** **B997/B1002: the golden is the UNIQUE metallic grammar whose
> own-conductor shadow is a McKay group.** Put together:
>
> > ### Reaching E₆ is generic. Being the golden is unique. The object's specialness lives in its GRAMMAR, not its DESTINATION.
>
> **Therefore matching the Standard Model could never have confirmed the axioms — even if it had
> worked.** The programme spent three campaigns aiming at the endpoint for validation while the
> uniqueness sat at the beginning. **That is a strategic correction, and it is banked, not felt.**
>
> **4. The crux, stated so it can be held honestly.** The observer-coupling reorientation says values
> live in the **observer–object coupling**, not in the object. If that is right, the object *should
> not* emit values — so **Tier 2's emptiness is exactly what our own framework predicts.** That is
> either the deepest thing here or the most sophisticated way of being unfalsifiable, and
> `WHAT_WOULD_COUNT` says Tier 2 is what decides whether this is physics at all. **The constructive
> resolution follows from the statement itself: a theory whose values are coupling artifacts must
> predict THE COUPLING, not the values.** Notably, that target sits **outside B687's atlas and
> outside B743's tower** — precisely the bar B1005 sets for a fourth crossing. **The negative points
> at where to look.**
>
> **5. What the practice keeps discovering about itself.** The recurring error of 2026-08-09 — nine
> instances — was never a wrong computation. It was **mistaking an instrument's blindness for the
> object's absence**: B1007 rebuilt a solver that existed, B1006 re-ran a check that existed, two
> ladder rungs graded BLIND had computed arcs behind them, and **B1008 measured the atlas as unable
> to see the very layer the programme now works in** (14 of 14 recent concepts have no word in it).
> *A suggestive parallel with the object's own observer/observed structure is noted and **explicitly
> not claimed as evidence** — it is a methodological rhyme, and the firewall applies to it as to
> anything else.* **What it does earn is the owner's standing rule, now operative: "we don't have X"
> is a hypothesis requiring a search, never a conclusion.**


> **This is the PHASE LADDER** — Phase 0/A/B/C, cadences and standing rules — and the file the
> `views-fresh` gate tracks. Its companion is the **TIER MAP** (*from the object to the goal*,
> Tier 0 → Tier 4) at `docs/ROADMAP.md`. **They are different documents, not copies**: verified in
> B830, they share **zero** headings. Review 35 mislabelled the companion a stale fork; that was
> wrong and is corrected.

Governed by `GOVERNANCE.md`. This file is the phase ladder. It stays in sync with
`CLAIMS.md` and `PROGRESS_LOG.md`. Each rung has a scope, explicit non-claims, and a gate
that must pass before the next rung begins.

---

## Phase 0 — Governance & Specification · **locked**

**Scope:** the constitution and scaffolding. No physics claims.

**Artifacts:** `GOVERNANCE.md`, `CLAIMS.md`, `ROADMAP.md`, `PROGRESS_LOG.md`,
`CHANGELOG.md`, `REPRODUCIBILITY.md`, `docs/ARCHIVE.md`, `AUDIT_REPORT.md`, `PROVENANCE.md`.

**Gate (passed 2026-05-22):** the audit is complete, the claim ledger exists, and the
framing is locked to the V4 / Reality-Check line.

---

## Phase A — Tested Foundation · **complete — current core P1-P16**

> Initial gate passed 2026-05-22: `origin_axiom` package built, suite green
> (33 passed, 1 optional skip), all ten initial P-claims locked. Tagged
> `phaseA-foundation-freeze`. Later exact-algebra integrations promoted P11-P13
> and P15-P16. The `P1–P16` core remains locked and untouched; the **full repo
> suite** (core + the frontier `B`-probe locks) now spans **~1228 test functions across
> 331 files** as of the B352 frontier (the proven core is unchanged; all growth is
> frontier `B`-probe locks).

**Scope:** lock every `proven` claim (currently P1-P16, with P14 unused) behind
an automated test, in a clean Python package. Reproduce — not inflate — the
verified core.

**Non-claims:** Phase A makes no new claims. It does not touch `open` items. It does not
promote anything.

**Rungs:**

| Rung | Work |
|---|---|
| A1 | Repo skeleton: `src/origin_axiom/`, `tests/`, `requirements.txt` / packaging, `.gitignore`. |
| A2 | `algebra` module — `L, R, A`, eigenvalues, `χ_A`; Fibonacci fusion identity; preserved form `G`. Locks P1, P2, P6. |
| A3 | `statistics` module — Ising and Zimm–Bragg transfer-matrix realizations; word-ensemble thermodynamics. Locks P3, P4, P5. |
| A4 | `gluing` module — the variational gluing identity (Sympy). Locks P7. |
| A5 | `topology` module — mapping-torus torsion; figure-eight / sister SnapPy data; the five-filter sieve. Locks P8, P9, P10. |
| A6 | Reconcile `conditional` claims C1–C4: each documented with its named assumption and a test that checks the *conditional* statement, not more. |
| A7 | Session-3 exact-algebra integrations: `log A` decomposition, gluing-equation factorization, isospectrality, Mobius vector field, derived cubic potential. Locks P11-P13 and P15-P16. |

**Gate:** the full test suite is green; every P-claim in `CLAIMS.md` has a passing test;
a freeze tag `phaseA-foundation-freeze` is created (`REPRODUCIBILITY.md`).

---

## Phase B — Frontier · **in progress**

> **State at Review 37 (2026-08-03).** The SM-structure window closed: the selection spine
> (repair → fused principle → termination → anomaly split → registerability keystone → menu
> gate) carries **zero load-bearing imports**; the **First Measurement Theorem** (the object's
> superselection charges stratify e₆; three Galois-conjugate first breakings; triality tiling
> with a cyclic law; matter = the two foreign sectors) is a **two-seat theorem**; **THE
> DESCENT** shows each breaking's matter is exactly one SM generation's multiplet pattern while
> the triple lives *across* the three breakings, not within one. Structure only — no values,
> no generations mechanism, Gate 5 untouched. Ledger: `docs/progress/REVIEWS.md` Review 37.


**Scope:** attempt the `open` items (O1–O9) under quarantine in `frontier/`. Every attempt
is explicitly labelled speculative. Nothing enters the `proven` core without passing the
`conditional → proven` gate in `GOVERNANCE.md` §5.

**Non-claims:** until a gate is passed, no frontier result is a claim — only a logged
observation.

**Probe clusters run so far** (each is a logged observation, not a claim):

| Probe(s) | Question | Outcome |
|---|---|---|
| B1-B5 | Topology/CS/moduli/Regge/BKL/Wheeler-DeWitt bridges? | Exact local structures found; no constructed 3+1 gravity bridge. |
| B6-B9 | Field-theoretic lift of P15/P16? | Potential is derived as algebra; kinetic term, carrier, particle and fusion interpretations remain frontier. |
| B13-B16 | Trace-map character variety, half-step, invariant controls, record swap? | Half-step trace lift contains the `A` sector; exchange/half-step symmetry is still an added condition. |
| B17-B24 | Half-step kernel campaign: functoriality, awareness, spacetime, spectrum, BKL, anyon bridges? | Trace lift is canonical; semantic/physical dictionaries remain stalled. |
| B25 | Fibonacci spectrum anchor at `lambda=1`? | Strong finite-approximant numerical anchor if `lambda=1` is accepted; coupling is motivated, not derived. |
| B33–B71 | The `SL(n)` trace-map **tower** + figure-eight A-polynomials/character variety? | Exact math: the Dickson tower (`knowledge/K003`), the A-polynomial / degree=rank `Mⁿ=L` family, the `SL(3)` A-variety (B67/B71). |
| B80–B106 | Prove the tower; classify the fixed points; geometry/physics audit? | `M⁴=L` symbolic-exact (B89); tower exact `n≤4` (B80); `char(ρ_n)` a **class function** (B103); three fixed-point classes (B106); Riemannian (not Lorentzian) signature, physics chapter **CLOSED** (B96/B101/B107). |
| B107–B124 | Consolidate the representation; bank the firewalled asides? | The **sign half proved all `n`** (B112); the tower = **`Sym^n(W)`, `W=V⊕1`** the external `det=−1` fundamental (B121/B122); the `(n;trace,det)` determination (B120); `m=1` arithmeticity (B123); reciprocity/time-reversal (B124). The standing prize: a **functorial `Sym(W)→trace-ring`** construction. |
| B128–B151 | The closing arc: chirality, completeness, the symmetry, and the physics boundary. | **Chirality axis CLOSED** — forced+generic but always self-mirror or mirror-paired ⟹ no preferred handedness; arithmeticity arm refuted outright (B144–B147). **Degree=rank COMPLETE on the irreducible locus** — B89's family is the whole component, `M⁴=L` unconditional (B149). **The unit's symmetry FORCED-identified** with the `N=2*` class-S S-duality mapping-class action (B148/B150, literature-confirmed). **Firewall CONFIRMED** — the complex volume is dimensionless (`ℂ/4π²ℤ`), carries no physical scale (B151). **The physics arc is CLOSED at the firewall** — a real bridge (symmetry) + a confirmed wall (no scale); cosmological-constant question on the far side. A POSTULATED structural reading of the wall: `STRATEGIC_SYNTHESIS.md` §8a. |
| B152–B217 | The object's faces: arithmetic, geometry, character-variety, dual McKay. | **The four-faces object** — the metallic bundle `RᵐLᵐ` mapped through trace-map / hyperbolic-geometry / character-variety / quantum-topology lenses (`papers/metallic_one_object/SYNTHESIS.md`). The WRT **period law** `P(γ)=lcm(t−2,t+2)/content`, `content=m` (B204/B208/B214/B219, correcting the B216 genus reading); the figure-eight character variety **is the elliptic curve `40a1`** (conductor `2³·5`, non-CM, B211); the **dual McKay** `E₈`(`ℚ(√5)`) + `E₆`(`ℚ(√−3)`), **`E₇` excluded** (B210); a hyperbolicity-divide separating two faces (B217). All firewalled. |
| B218–B230 | Emergent supersymmetry from golden multiplicity. | The golden Fibonacci-anyon / `SU(2)₃` chain flows to **tricritical Ising `c=7/10` = the first `N=1` superconformal minimal model** (B218–B224), via the *unique* ordinary↔super coset coincidence at `SU(2)₃` (B228); golden is **uniquely SUSY** among metallic chains, robust AFM/FM (B224/B230); explicit metallic/super Seifert duals `S²(m²+4,m²+3,3)` (B227/B229). Emergent, not lattice (B223). All firewalled. The framework search (`speculations/S041`): every external-framework overlap is a **rhyme, no crossing** — firewall holds a 5th time. |
| B231–B314 | The structural-theorem arc: the object forces form, not values. | The **two-ended object** (`E₆`/`ℚ(√−3)` ↔ `E₈`/`ℚ(√5)`, `E₇` excluded by Niven; B248/B258/B261); the **arithmetic atom** `4₁→ℚ(√−3)→2T→McKay Ê₆` + the `E₆` character variety (B264/B266/B282); the **cascade** = standard Slansky Lie theory + the Eisenstein `ω` (B305/B306/B310/B311); **Face IV houses the *form*** (CIZ `SU(2)₁₀`; B312/B313); the **four faces of one `κ`** (B309). **The firewall is a Galois theorem** — every discrete invariant is a Galois orbit of the object's own arithmetic (B285/B314). *The object forces the form of physics, never its values.* All firewalled; `knowledge/K020`, `philosophy/P013`. |
| B315–B325 | The specialist handoff + the value hunt. | Forgotten leads + cross-chat handoffs run to conclusion; the frontier mapped to four gates (`docs/OPEN_PROBLEMS.md`). E₇-exclusion contains heterotic's (pseudoreal root, B315); `√−7` = the chirality field (B316); the object is a **transcendental** Painlevé-VI solution (B317); amphichirality = the geometric firewall (B318); **the value hunt, run — the object's invariants match the SM at chance (`p≈0.5`, null test): the firewall confirmed empirically** (B322); the **four-level framework** (B323); the ω-circulant generation matrix exact in `ℤ[ω]` = structure not values (B324); the "ℤ/3-protection" obstruction refuted, CRUX stays Level 3 (B325). All firewalled. |

Across Phase B the pattern is consistent: the well-defined content is exact or
numerically reproducible, but each physical or semantic bridge stalls at an
inserted dictionary, carrier, coupling, unit, selector, or observable — and the
**physics arc is now closed at the firewall** (a real symmetry bridge, a confirmed
scale wall). The remaining open frontier is **mathematics**: the functorial
`Sym(W)→trace-ring` wall (`ρ_n`; `knowledge/K008`, `story/09`), the `GL(2,ℤ)`
gluing landscape (H5), and the arithmetic-minimality question (H4). Since B151 the
frontier has mapped the **one object through four faces** (B152–B230): the elliptic
curve `40a1`, the dual McKay `E₈`+`E₆`, and an emergent `N=1` superconformal
(`c=7/10`) symmetry — every cross-face link a verified *rhyme* at the Betti /
rep-theory / dimensionless level, the firewall reconfirmed throughout. Since then the
**structural-theorem arc (B231–B314)** sharpened this into one proven statement — *the
object forces form, not values*, the firewall as a Galois theorem — and the
**specialist-handoff arc (B315–B325)** mapped the frontier to four gates and confirmed
the value-firewall empirically (the value-hunt null test). Ledger through `V238`, probes
`B1–B370+`; recent probes in `CHANGELOG.md`; the current frontier in `docs/OPEN_PROBLEMS.md`; the promoted tier in `CLAIMS.md` (2026-07-03 audit).

**Standing gate:** nothing here is promoted without the `conditional → proven` gate. Exact
*algebra* surfaced by a probe may be promoted (e.g. P11–P13, promoted from the B1/session-3
material); speculative *physics* may not. All physics readings stay quarantined in
`speculations/` + `philosophy/`; the physics chapter is CLOSED (`knowledge/K006`).

---

## Phase C — Exhaustive survey of emergence-paths · **in progress**

**Scope:** rather than push the single Origin Axiom mechanism deeper, *systematically
enumerate* the mechanisms by which "nothing being unstable" could produce reality,
probe each until it carries a definite verdict, and treat the resulting map as the
deliverable. See `paths/README.md`, `paths/PATHS.md`, `paths/MECHANISM_CLASSES.md`.

**Non-claims:** Phase C probes are observations, not claims. Same gate as Phase B.

**Path-space:** 20 mathematizable paths (E1–E20) across 11 mechanism classes, plus
5 philosophical paths (P1–P5) in a separate register.

**First batch:**

| Probe | Question | Class |
|---|---|---|
| E14 | Is "nothing" even formally well-defined? | F — categorical / formal |
| E11 | Does counting alone force something? | E — statistical / informational |
| E5 | Does mainstream physics already have a working mechanism (Vilenkin)? | B — quantum zero-point |

Each probe ends with exactly one verdict: `PRODUCES-OBSERVABLE`, `STALLED`, `DEAD`,
`NEEDS-EXPERTISE` (see `paths/README.md`). No "interesting, continue."

**Expected outcome:** most paths will `STALLED` at the same wall the Phase B probes
hit (well-defined content, unconstructed bridge to an observable). The map of
failure modes is itself the contribution.

**Re-plan checkpoint:** after the first batch's three verdicts, the next batch of
~3 is selected on the basis of what was learned, not the current ranking.

---

## Standing rules

- A rung does not start until the previous rung's gate passes.
- Dead claims (`docs/ARCHIVE.md`) are never revisited.
- Every rung completion is logged in `PROGRESS_LOG.md` and reflected in `CLAIMS.md`.
- **WIDEN cadence** (every ~10 banked results; governed by `METHOD.md`): cross-finding synthesis — every banked
  result since the last WIDEN gets a touchpoint in `docs/STRATEGIC_SYNTHESIS.md` / the relevant `SYNTHESIS.md`;
  resurface dropped patterns (the L37 audit, made standing); a **mandatory DORMANT sweep** of `docs/HINT_LEDGER.md`;
  and the **standing physics-parallels prompt** ("which verified results have known parallels in frameworks we
  haven't examined?" — keeps the framework search L46/S041 live). *Zero new NOTICED hints since the last WIDEN is
  the rut-alarm.*
- **QUESTION cadence** (same trigger): run the completeness-critic prompt-set ("what modality/connection haven't we
  tried? the adjacent unasked question to each banked result? what would a skeptic say is missing?") → new
  `QUESTION`-type rows in `docs/HINT_LEDGER.md`. (Internalizes the chat1/chat2 cross-check so new questions don't
  depend on it.)

---

## ⟳ VIEW REFRESH — 2026-07-29 (Review 32)

*Navigation view, regenerated at each decadal review; freshness enforced by the `views-fresh`
gate (GOVERNANCE §12: "freeze the substrate; generate the views").*

**Where the phase ladder actually stands.** Phase 0 locked; Phase A complete; **Phase B is the
live frontier**; Phase C in progress. The operative planning document is no longer this file but
`docs/CLOSURE_MASTERPLAN.md` (Phase 2 structural sweep → Phase 3 correspondence enumeration →
Phase 4 walls → an unreached Phase 5 capstone), with `docs/THEOREM_LEDGER.md` (C1–C23) as the
forced-core ledger it feeds.

**Cadences — status.** The WIDEN / QUESTION cadences remain standing. The **law-harvest** (a
standing item since Review 31) ran twice: 6 buried laws recovered at Review 31, and **4 more at
Review 32** from a 33-arc pre-B788 backlog filter (B471, B534, B533, B120). The **decadal review**
fires every ~20 merges and now additionally **must refresh every navigation view** — enforced, not
remembered.

**Live gates on any physics reading:** Gate 5 (no SM quantities to CLAIMS), Gate 5-Q
(phenomenology firewall), and **L91** — the typed-functor obligation that `WORKING_RULES` rule 6
names as the thing physics readings wait on. L91 obligations (1)–(3) are open.

> **Review 33 (2026-07-29)** — the compaction campaign is CLOSED (W0–W5 + residuals B800/B801/B802). Next load-bearing work is authoring: **701 of 731 arcs still need verdicts** (the generated ledger projects 4.1 %), and **~111 negatives are unregistered** in the kill graph (B801, measured, CI 55–168).

> **Review 34 (2026-07-30)** — next: **wave 2** (425 arcs, **overlapping** slices so the reader-conservatism offset is measured rather than confounded), a **random-sampled** re-audit of wave 1, and the stale WHAT axis. The forcing graph has **317 nodes and ~47 edges** — coverage is a precondition, not the goal.

> **Review 35 (2026-07-30)** — next: **the third verdict wave** — 229 arc ids were never assigned to
> any reader and **116 of them carry a `FINDINGS.md`** (B819), so the residue is a *coverage-frame
> gap, not a data gap*. Its calibration block must exercise **all four** verdict categories, checked
> **before** the run: wave 2's exercised two while licensing four, and **2 of the 11
> untested-category writes were wrong** (B818). Also open and unscheduled: **the lexicon's full
> re-grounding** (B806) — B825 closed only the one *known* gap, and `docs/atlas/BLIND_ARCS.md` says
> in place that an empty `GAP` column is not a finished instrument.

> **Review 36 (2026-08-01)** — next: **P5 Phase 2**, the table-first draft, carrying Phase 1's four
> reshaped claims and the **Q2 two-cell row**. Highest-value instrument task: **re-ask "could this
> gate still fail?" across all 19 gates** — three were found fail-open by drift in one window, none
> by the standing audit.


*Review 38 (2026-08-05): window B890–B906 reviewed — the M(𝕆,ℂ) isomorphism, the sealed generation-shaped verdict, the flavor arc with I = −1, the Kim lit-gate; five promotion candidates listed; next sealed cell: the real-form selector (B907). See docs/progress/REVIEWS.md.*


*Mid-window update (2026-08-05, post-crossing): B907–B917 — e₆(2) selected; the norm/signature; I = −1 exact; the one-number table; THE CROSSING (MISS 16σ, the desert dead, R4b registered); the value-arc convergence with the solo seat. See CAMPAIGN_STATUS and the masterplan v5.*


*Review 39 (2026-08-05): window B907–B919 + the register loop + THE CROSSING reviewed; suite green after hygiene; candidates listed (B908, the value-layer cluster, B912, B914 + R38 leftovers); next sealed: R4b. See docs/progress/REVIEWS.md.*

*Review 40 (2026-08-07): window B909, B914–B941 reviewed — the three crossings all negative, D₂ decoded as the hierarchy's carrier, the value layer proved value-invisible, two precedent numbers banked (the Maass and Dirac eigenvalues), and the branch-symmetric ratio-only phrasing registered as binding on any future crossing. Three real discipline failures caught by the anti-burial locks and fixed; the priority-language asymmetry flagged (B922's unqualified claim predates the O3 gate — panel dispatched). See docs/progress/REVIEWS.md.*

> **Review 41 — 2026-08-09.** `docs/ROADMAP_TOE.md` is **superseded** by `docs/THE_FRAMEWORK.md`; the execution order now lives in `docs/THE_CAMPAIGN.md` (Wave 1 repairs, **4 of 6 done** → Wave 2 holes → Wave 3 live surfaces → Wave 4 blind, **ledger first**). Rungs and their grades are in `docs/THE_LADDER.md`.
>
> **Navigation note found by this review:** there are **two roadmap files** — this one (the gated navigation view) and `docs/ROADMAP.md`. The gate tracks **this** one. Worth consolidating; recorded rather than silently left.
