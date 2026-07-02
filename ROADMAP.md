# Origin Axiom — Roadmap

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
> suite** (core + the frontier `B`-probe locks) now spans **~1211 test functions across
> 328 files** as of the B350 frontier (the proven core is unchanged; all growth is
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
`B1–B350`; recent probes in `CHANGELOG.md`; the current frontier in `docs/OPEN_PROBLEMS.md`.

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
