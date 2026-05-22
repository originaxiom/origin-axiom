# Origin Axiom — Governance (Phase 0)

**Status:** Phase 0 — locked. Amendments require a logged entry in `PROGRESS_LOG.md`.
**Last updated:** 2026-05-22

This file is the **constitution** of the consolidated Origin Axiom repository. It exists for
one reason: the project has a documented history of generating a small, genuine mathematical
core and then over-narrating it as physics. Governance is the mechanism that keeps the two
apart. Every other file in this repo is subordinate to the rules here.

---

## 1. Purpose

To investigate the Origin Axiom — *existence as a frustrated cancellation* — as a
**claim-bounded, reproducible, falsifiable** research program, in which:

- what is proven is locked behind tests and cannot silently regress;
- what is speculative is quarantined and clearly labelled;
- what has been killed stays killed;
- and every claim is traceable to code, a test, and a document.

The goal is **not** a theory of everything. The goal is a body of work an external expert
could clone, run, audit, and trust.

---

## 2. The framing lock

The project produced two contemporaneous self-assessments on 2026-05-21 (see
`AUDIT_REPORT.md` §3): an optimistic one (`handoff.md`) and a disciplined one
(`ORIGIN_AXIOM_REALITY_CHECK_v1.md` + the V4 paper).

**This repository is bound to the disciplined framing.** The strongest label the project may
apply to itself is:

> a candidate classical/statistical transfer-matrix framework with topological and
> Lorentzian *mathematical* structure — **not** a theory of spacetime, gravity, matter,
> or cosmology.

The handoff document is retained in `legacy/` as a historical record of the exploration. It
is **not** a source of claims.

---

## 3. Claim status labels

Every claim in `CLAIMS.md` carries exactly one label:

| Label | Meaning |
|---|---|
| `proven` | Exact, independently checkable, and backed by a passing test. Safe to build on. |
| `conditional` | True *given assumptions that were chosen, not forced*. The assumptions must be named. |
| `open` | A research target. Not a partial result. Lives in `frontier/`. |
| `dead` | Tested and falsified, or shown circular/numerological. Permanent. See `docs/ARCHIVE.md`. |

A claim with no label does not exist. Prose anywhere in the repo must not assert anything
stronger than the label of the claim it rests on.

---

## 4. What counts as a claim

A statement is a **claim** only if it is backed by all three of:

1. **Code** — a script or module in `src/` (or `frontier/` for open work) that computes it;
2. **A test** — an assertion in `tests/` that fails if the result changes;
3. **A document** — an entry in `CLAIMS.md` with an ID, the statement, the label, and the
   evidence pointer.

"Interesting patterns" without all three are not claims. They may be noted in
`PROGRESS_LOG.md` as observations, never asserted as results.

---

## 5. Promotion and demotion gates

Status changes are **gated** and must be logged in `PROGRESS_LOG.md`:

- **`open` → `conditional`** — a derivation exists, but rests on named assumptions.
  Requires: code + test + the assumptions written explicitly in `CLAIMS.md`.
- **`conditional` → `proven`** — the assumptions are eliminated or shown forced.
  Requires: a proof or an exhaustive check, plus a test, plus reviewer-style scrutiny
  recorded in the log.
- **anything → `dead`** — a falsification or a demonstration of circularity. Requires:
  the reproducing code/test and an entry in `docs/ARCHIVE.md` explaining *why* it died.
- **`dead` → anything** — **forbidden.** A dead claim is permanent. A genuinely new idea
  that resembles a dead one is a *new* claim with a new ID.

Nothing moves out of `frontier/` into the proven core without passing the
`conditional → proven` gate.

---

## 6. The red-team lens

Before any claim is labelled `proven`, ask the skeptic's questions and record the answers:

1. Were the axioms/parameters chosen to produce this result? (If yes → at most `conditional`.)
2. Is this a definition presented as a discovery?
3. Does the result survive if a different but equally natural choice is made?
4. Is a number being matched to a "famous constant" after the fact? (If yes → `dead`.)
5. Does the wording claim physics where only mathematics was shown?

The project's credibility is the honesty of these answers, not the size of the claims.

---

## 7. Phase structure

| Phase | Scope | Status |
|---|---|---|
| **Phase 0** | Governance, specification, claim ledger, repo scaffolding. | locked |
| **Phase A** | The tested foundation: lock every `proven` result behind a test. | active |
| **Phase B** | The frontier: attempt `open` items in `frontier/`, quarantined, gated. | not started |

Phase B may not begin until Phase A's test suite is green. See `ROADMAP.md`.

---

## 8. Anti-overclaim glossary

Recurring wording corrections. The left column is **forbidden**; use the right.

| Do not write | Write instead |
|---|---|
| "the gluing creates causal structure / spacetime" | "the composition preserves a Lorentzian form in *phase space*" |
| "φ explains the cosmological constant" | (nothing — this is `dead`, see D1–D3) |
| "the universe is a figure-eight knot" | "`A` is the figure-eight knot monodromy" |
| "we derived Einstein's equations" | "the BKL connection identifies one Kasner solution among infinitely many" |
| "Fibonacci anyon physics" | "an exact Fibonacci *fusion-count* dictionary" |
| "proven" (for a chosen-axiom result) | "conditional, given axioms A1–A6" |

---

## 9. Process

- **`PROGRESS_LOG.md`** — append-only, chronological. Every working session adds a dated
  entry. Never edit past entries. When it grows large, roll older entries into
  `docs/progress/` by quarter.
- **`CHANGELOG.md`** — human-facing, versioned (Keep a Changelog format), updated at releases.
- **`CLAIMS.md`** — the living ledger. Updated in the same commit as any result it describes.
- **Freezes** — stable states are git-tagged (see `REPRODUCIBILITY.md`).
- **`legacy/`** — frozen prior history. Never edited, never a source of claims.
- **`docs/ARCHIVE.md`** — the register of dead ideas and why they died.

---

## 10. Amending this constitution

Phase 0 is locked. Amendments are allowed only when they improve *legibility or discipline*
without weakening any rule, and must be recorded in `PROGRESS_LOG.md` with a rationale.
Loosening a rule to admit a claim that would otherwise fail is explicitly forbidden.
