# THE BANKING PROTOCOL — what must be true before an arc is banked, and what must be current after

**Standing and binding for every seat.** Owner directive, 2026-08-09: *"should we have a banking
protocol so we make sure all these get updated after all new findings, and the protocol makes sure
— and maybe hires an independent agent to make sure the update happens. Every decadal review should
make sure no single md document is outdated and doesn't represent the current state."*

**Companions:** `COMPUTE_THE_PROGRAM.md` (the pre-compute protocol P0–P6) · `THE_LADDER.md` (what
we lack) · `THE_FRAMEWORK.md` (what we have) · `WORKING_RULES.md` §0 (the binding pointer).

---

## PART I — THE BANKING CHECKLIST

Every banked arc, no exceptions. `scripts/gates/gates.py` enforces the mechanical rows; the
judgement rows are enforced by the independent verification in Part II.

### A. The arc itself
1. **`FINDINGS.md`** — the write-up. *The filename matters:* `scripts/forcing/build.py` ingests
   only files named exactly `FINDINGS.md`, and **45 arcs were never ingested** because they used
   another name (B1–B5 among them). If the substance lives elsewhere, `FINDINGS.md` must exist and
   point at it.
2. **`arc_verdict.json`** — `id`, `verdict`, `instrument`, `claim_one_line`, `depends_on`,
   `supersedes`/`superseded_by`, `authored_by`, **`creates_law` (bool; REQUIRED from B1103
   on — a `true` demands a `THEOREM_REGISTRY.md` row in the SAME PR; the
   `theorem-registry` gate reads it, the schema lock enforces it — R48-F4)**.
3. **The verdict must be the right *kind*.** An arc that establishes *another* arc's claim fails is
   an **auditor doing positive work** — `PROVED`, never `RETRACTED`. `RETRACTED` is reserved for an
   arc withdrawing **its own** headline (B818; caught two mislabels on 2026-08-08).
4. **Locks** — `tests/test_b<NNN>_*.py`, asserting the arc's load-bearing facts, not its prose.
5. **If sealed: report the result.** A sealed prereg with no report is a file-drawer entry
   (B837, B982). If it will never fire, record a **disposition**, not silence.

### B. The three ledgers, same or next PR
6. **`CHANGELOG.md`** — top. 7. **`PROGRESS_LOG.md`** — append. 8. **`docs/CAMPAIGN_STATUS.md`** —
`LATEST`.

### C. The surfaces a reader forms their picture from
9. **`docs/LAW_MAP.md`** — required for every substantial arc (claim ≥ 500 chars, non-instrument);
   gated by `representation-sweep`. **Carry the scope with the claim** — `lawmap-scope` exists
   because compression dropped it.
10. **`docs/THE_LADDER.md`** — if the arc moves a rung, move it. **BLIND never becomes BOUNDED in
    one step.**
11. **`docs/THE_FRAMEWORK.md`** — if the arc changes what the programme *has*.
12. **`docs/OPEN_LEADS.md`** — closures quote **the closing sentence and its path**. A closure whose
    scope sentence **names a manifold** is suspect by construction.
13. **`docs/RETRACTED_PHRASES.md`** — a retraction is not complete until its phrase is registered
    and the sweep is clean. *Retracting a claim does not retract its instances.*
14. **Kill graph** — every `NEGATIVE` arc routed, with `kill_form`, `hatch`, `revival_score`.
15. **`CLAIMS.md`** — only if it passes Gate 5. Structure, never SM values.

### D. Regenerate and verify
16. `python3 scripts/atlas/atlas.py` · `python3 scripts/views/generate.py`
17. `python3 scripts/gates/gates.py` — **all green**, including `doc-currency`.
18. **Full `pytest`** — green *before* commit, and **do not touch the tree while it runs** (a
    mid-run regeneration invalidated a 58-minute run on 2026-08-08).
19. Feature branch → PR → squash-merge → push **origin *and* codeberg**.

---

## PART II — INDEPENDENT VERIFICATION (the owner's "hire an agent")

**The author of an arc is the worst auditor of whether its surfaces were updated**, because the
same picture that produced the omission produces the check. So:

> **A banking pass is not complete until an agent that did not write the arc confirms the
> checklist, reading the repository rather than the conversation.**

**What the verifier is given:** the arc ID and one instruction — *verify Part I against the working
tree; report each row PASS / FAIL / N-A with the file and line that discharges it.*

**What the verifier is NOT given:** the author's reasoning, or the claim to be confirmed. It checks
**presence and currency**, not correctness — correctness is the locks' job.

**Escalation.** Any FAIL blocks the merge. A verifier that reports all-PASS on a checklist with a
missing row is itself a finding, and gets recorded like any other.

**Why this rather than trust:** on 2026-08-08 one seat produced five omissions of this exact class;
the audit seat committed the same error *inside the audit built to catch it*; and B982 found it
*inside a governance gate*. **The failure is structural — a 949-arc corpus queried from memory —
so the check must come from outside the memory that failed.**

---

## PART III — THE DECADAL REVIEW: NO DOCUMENT MISREPRESENTS THE STATE

Every review additionally certifies **document currency across the whole repository**, not just the
arcs.

**Mechanically** — `doc-currency` (B984) measures, for each registered living document, the newest
arc it cites against the newest arc that exists, and fails past a per-document tolerance. A
document may be `frozen` (a *visible* opt-out, reported every run) or carry a **DECLARED DEBT**
naming what is owed and when it was declared. **A debt is not an exemption**: it prints on every
run and the lock fails if the set grows. *(B982: seven gate exemptions rested on an audit that
never named them. Never again a silent pass-through.)*

**By reading** — the review reads every room and asks one question of each: *does this still
describe the programme?*

| room | files | the question |
|---|---|---|
| **claims** | `CLAIMS.md`, `THEOREM_LEDGER.md`, `LAW_MAP.md` | is anything here superseded, retracted, or scoped wider than its arc proved? |
| **the chain** | `THE_FRAMEWORK.md`, `UNIQUENESS_THEOREM.md`, `THE_SM_VERDICT.md` | can a reader follow **philosophy → aAbB → the object → its faces and family → the algebra → the cascade → symmetry breaking and gauge groups** without a gap? |
| **the negatives** | `THE_LADDER.md`, the kill graph, `RETRACTED_PHRASES.md` | is every "we don't have X" still a **claim with a citation**, not an impression? |
| **method** | `WORKING_RULES.md`, `PRACTICES.md`, `TOOLBOX.md`, `METHOD.md` | do these describe how we **actually** seal, verify and certify **today**? |
| **speculation & philosophy** | `speculations/`, `philosophy/`, `story/`, `knowledge/` | is the firewall still one-way, and does the motivation still match the mathematics? |
| **logs & easy-read** | `CHANGELOG.md`, `PROGRESS_LOG.md`, `CAMPAIGN_STATUS.md`, `INDEX.md` | can a new reader — human or agent — reconstruct the work from these alone? |

**The standard:** *whoever opens this repository, human reviewer or AI seat, should be able to
follow the complete chain of work and arrive at the current state without being misled by any
document in it.*

---

## PART IV — THE CHAIN THAT MUST STAY LEGIBLE

The named waypoints, each of which must be findable and current. Where a link is **thin**, the
ladder rung is given — thinness is a fact to record, not to hide.

**philosophy / the four incompletenesses** → **aAbB** (A1–A7; one bit; φ) → **the object m004** —
monodromy, cusp, torus bundle, puncture → **its two ends** (E₆ hyperbolic ↔ E₈ spherical) → **its
class and family** (sisters, both rows, the child) → **the seam** → **metallic families and the
SL(n) towers** → **the algebra** (McKay E₆, M(𝕆,ℂ), the 27) → **the measurement cascade** →
**symmetry breaking and the gauge groups** → **the boundary** (rank, chirality, scale, time).

**Thin links, recorded honestly (checked 2026-08-09):**
- **Markov blanket — 0 arcs, in no document.** Genuinely absent. **Conflation hazard:** the corpus
  is full of **Markov *triples* / the Markov cubic**, a *different object*; a grep for "Markov"
  will read as covered when it is not. Ladder rung **X31, BLIND**.
- **Feedback mechanism — 2 arcs.** Named by the owner as very important; effectively unbuilt.
  Ladder rung **X32, BLIND**.
