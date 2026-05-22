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

## Phase A — Tested Foundation · **complete — gate passed 2026-05-22**

> Gate passed: `origin_axiom` package built, suite green (33 passed, 1 optional
> skip), all ten P-claims locked. Tagged `phaseA-foundation-freeze`.

**Scope:** lock every `proven` claim (P1–P10 in `CLAIMS.md`) behind an automated test, in a
clean Python package. Reproduce — not extend — the verified core.

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

**Gate:** the full test suite is green; every P-claim in `CLAIMS.md` has a passing test;
a freeze tag `phaseA-foundation-freeze` is created (`REPRODUCIBILITY.md`).

---

## Phase B — Frontier · **in progress**

**Scope:** attempt the `open` items (O1–O9) under quarantine in `frontier/`. Every attempt
is explicitly labelled speculative. Nothing enters the `proven` core without passing the
`conditional → proven` gate in `GOVERNANCE.md` §5.

**Non-claims:** until a gate is passed, no frontier result is a claim — only a logged
observation.

**Probes run so far** (each is a logged observation, not a claim):

| Probe | Question | Outcome |
|---|---|---|
| B1 | Gluing identity ↔ discrete Chern–Simons flatness? | Qualified yes at the holonomy level; no CS action / level `k`. |
| B2 | Monodromy action on the moduli space? | Linear action on `(log M,log L)`; falsified the handoff's A-polynomial-curve claim. |
| B3 | 4D Regge complex (handoff "Step 5A")? | 3D triangulation exact; the "4D stacking" is not a defined construction. |
| B4 | BKL billiard / Gutzwiller / golden Kasner? | Figure-eight = shortest billiard orbit (exact); leading Gutzwiller term (37.8%, modest); golden Kasner exponents. Heavily caveated. |
| B5 | Wheeler-DeWitt constraint / a Λ estimate? | Reproduces known structure; the `Λ` estimate is dead-adjacent (cf. D1, D2). Documentary only. |

Across B1–B5 the pattern is consistent: the well-defined content is exact, but the bridge
to 3+1 gravity rests, in every probe, on a step asserted but not constructed.

**Standing gate:** nothing here is promoted without the `conditional → proven` gate. Exact
*algebra* surfaced by a probe may be promoted (e.g. P11–P13, promoted from the B1/session-3
material); speculative *physics* may not.

---

## Standing rules

- A rung does not start until the previous rung's gate passes.
- Dead claims (`docs/ARCHIVE.md`) are never revisited.
- Every rung completion is logged in `PROGRESS_LOG.md` and reflected in `CLAIMS.md`.
