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
> and P15-P16; the current suite is 66 passed, 1 skipped.

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

Across Phase B the pattern is consistent: the well-defined content is exact or
numerically reproducible, but each physical or semantic bridge stalls at an
inserted dictionary, carrier, coupling, unit, selector, or observable.

**Standing gate:** nothing here is promoted without the `conditional → proven` gate. Exact
*algebra* surfaced by a probe may be promoted (e.g. P11–P13, promoted from the B1/session-3
material); speculative *physics* may not.

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
