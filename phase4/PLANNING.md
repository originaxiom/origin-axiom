# Phase 4 Planning (Vacuum → FRW / Scale Sanity)

Status: **Planning / design note, non-binding.**

This document collects the design intent for Phase 4 in light of:

- the canonical θ & A architecture described in `docs/THETA_ARCHITECTURE.md`;
- the existing Phase 0 contract and corridor/ledger structure;
- the Phase 1–3 history (toy interference, toy vacuum residue, and the
  Phase 3 mechanism vacuum model with binding regime).

Nothing in this file is a claim about nature; binding contracts and claims
must live in Phase 0 and in co-located `CLAIMS.md` / `CLAIMS_TABLE.md`
documents once Phase 4 is formally scoped.

---

## 1. Working title and mission

**Working title:** Phase 4 – Vacuum-to-FRW Consistency & Scale Sanity

**Mission (draft):**

> Starting from the Phase 3 mechanism vacuum model and its canonical
> global amplitude A(θ), Phase 4 explores whether there exists a
> structurally reasonable mapping from A(θ) to FRW-like cosmological
> behaviour (and rough vacuum-energy scales) that yields a non-empty,
> non-pathological θ-corridor.

In other words: Phase 4 is the first phase whose *primary job* is to test the
vacuum mechanism against cosmology-like structure, not just to demonstrate a
mechanism in isolation.

---

## 2. Inputs and outputs (conceptual)

**Inputs (conceptual):**

- From Phase 3 (mechanism):
  - Canonical θ in [0, 2π).
  - A_0(θ): unconstrained global amplitude.
  - A(θ) with a non-cancellation floor; binding diagnostics.
- From Phase 0:
  - Corridor/ledger semantics.
  - Binding-certificate pattern.
- From Phase 2 (toy FRW), as *design inspiration*:
  - Experience embedding a vacuum-residue proxy into FRW equations.
  - Numerical considerations and pitfalls.

**Outputs (conceptual, not yet formalised):**

- One or more **mappings** from A(θ) (or a derived residue) into:
  - a toy FRW module, or
  - a vacuum-energy-like scalar observable.
- A clearly defined **Phase 4 θ-filter** (even if broad), or a record that
  all reasonable mappings investigated lead to empty or pathological corridors.
- A Phase 4 paper that:
  - states a narrow, honest scope;
  - documents the mappings, diagnostics, and corridor behaviour;
  - connects back to the Phase 3 mechanism architecture.

---

## 3. Relationship to earlier phases

- **Phase 1:** remains a conceptual and numerical precursor, not a source
  of binding θ-constraints, unless we later define an explicit mapping to
  canonical θ and re-audit it.
- **Phase 2:** its FRW embedding is treated as a *prototype*. Phase 4
  should:
  - reuse lessons (e.g. stability, normalisation choices),
  - but not be constrained by any specific Phase 2 numerics.
- **Phase 3 (mechanism):** is the *anchor* for θ and A. Phase 4 must
  respect the canonical definitions from the mechanism.

---

## 4. Open design questions (to be resolved before a Phase 4 contract)

1. What precise mathematical form should the mapping
   A(θ) → (vacuum-energy proxy, FRW parameters) take?
2. How do we normalise any vacuum-energy-like quantity so that “scale sanity”
   tests are meaningful but do not overclaim?
3. What diagnostics best capture “non-pathological FRW behaviour” in a way
   that can be turned into a corridor or filter on θ?
4. How do we ensure that Phase 4’s θ-filter is compatible with the Phase 0
   ledger and can be cleanly intersected with any future filters?
5. What does a minimal, publishable Phase 4 paper look like, in terms of:
   - sections (introduction, mechanism recap, mapping definition,
     diagnostics, corridor behaviour, limitations);
   - tables and figures;
   - explicit non-claims?

---

## 5. Next concrete steps (before coding)

1. Refine `docs/THETA_ARCHITECTURE.md` as needed while reading this file.
2. Draft a **Phase 4 contract skeleton** (SCOPE/CLAIMS/NON_CLAIMS) that
   mirrors the style of Phases 0–3 but with a deliberately narrow mission.
3. Only then define:
   - the Phase 4 directory structure (src, paper, workflow, outputs);
   - any Snakemake gate scripts;
   - initial toy mappings and diagnostics.

Once these steps are done and the contract is locked, Phase 4 can proceed in
rung-style increments as with the new Phase 3 mechanism.

