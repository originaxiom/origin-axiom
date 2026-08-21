# Blind arcs — the triage registry

**Generated-adjacent but HAND-MAINTAINED. The `atlas-lexicon-current` gate reads this file.**

A *blind* arc is one whose `FINDINGS.md` matches none of the atlas lexicon's motifs. B821 showed
that a raw blind **count** conflates three unlike things, and B822 showed that capping it with a
threshold is self-referential — the arc documenting the gate incremented the very count it was
fixing. So there is **no ceiling**. Instead every substantial blind arc (`FINDINGS.md` ≥ 2000 bytes)
must appear below with a disposition, and the gate fails **only on untriaged arcs**.

Thin arcs (< 2000 bytes) are excluded from the metric entirely — an arc reading *"Logged
observation, not a claim."* cannot match any lexicon and none should try.

## Dispositions

- **`GAP`** — a real object topic the lexicon does not cover. **This is open instrument work.**
- **`INSTRUMENT`** — an arc about the programme's own machinery, with no object content. An
  **object** atlas is *correct* to miss it. Not a defect, and not to be closed by adding a motif:
  B821 proved that a motif for the meta-layer matches 46 % of the corpus, because self-audit
  vocabulary is the house method's ambient register, not a distinguishing topic.

**Adding a row is a judgement, and it is recorded here rather than absorbed into a number.** The
honest failure mode of this design is labelling everything `INSTRUMENT`; that is visible and
auditable in a way a passing threshold never was.

| arc | disposition | why |
|---|---|---|
| `B1018` | INSTRUMENT | The suite's parallel qualification (xdist, the arbiter rule) — about **our own test infrastructure**, not an object topic; an OBJECT atlas is correct to miss it. |
| `B977` | INSTRUMENT | The representation-sweep gate — about **our own claim hygiene**, not an object topic. |
| `B966` | INSTRUMENT | The `lawmap-scope` gate — about **our own claim hygiene**, not an object topic. |
| `B965` | INSTRUMENT | The LAW_MAP scope audit — about **our own claim hygiene**, not an object topic; an OBJECT atlas is correct to miss it. |
| `B961` | INSTRUMENT | The frame instrument (`frame.py`) — exact Killing form, centralizer, Killing-perp, derived algebra on e₆. About **our own machinery**, not an object topic; an OBJECT atlas is correct to miss it. |
| `B679` | INSTRUMENT | An `engine_v7` gate-report patch, prepared and verified but not deployed; explicitly about a seat conduit that is not a repo-tracked file. |
| `B770` | INSTRUMENT | The closure census — Phase 0 bookkeeping over the programme's own arcs. |
| `B793` | INSTRUMENT | Gate 8R2-A, blocked on an **architectural finding about the B788 solver**. About the apparatus, not the object. |
| `B798` | INSTRUMENT | The algebraicity falsifier's power box — discharges review actions R32-4/R32-5 by pricing a `(d, H)` test budget. It **governs** an object claim without making one. *(Borderline: the falsifier it prices is load-bearing for B796, so if the lexicon ever gains a motif for falsifier design, revisit.)* |
| `B818` | INSTRUMENT | The verdict-vocabulary errors and the `RETRACTED` disambiguation. |
| `B819` | INSTRUMENT | The coverage-frame correction to B817. |
| `B827` | INSTRUMENT | The shadow-progress-log recovery and the fail-open-by-drift gate fix. About the repository's own bookkeeping; an object atlas is correct to miss it. |
| `B833` | INSTRUMENT | The negative-routing measurement and the arc-register vs kill-register unit mismatch. About the repository's own bookkeeping; an object atlas is correct to miss it. |
| `B836` | INSTRUMENT | Routing the negative backlog into the kill graph. About the repository's own bookkeeping; an object atlas is correct to miss it. |
| `B837` | INSTRUMENT | The file-drawer audit of sealed-but-unreported preregs. About the repository's own reporting discipline; an object atlas is correct to miss it. |
| `B899` | GAP | The hierarchy-source check (an earned negative): the sealed cells' deviation magnitudes vs mu's root geometry. Object-level topic (root spacings, leakage magnitudes) the lexicon does not yet carry a motif for; the negative verdict does not make it instrumental. |
| `B935` | GAP | The composition hunt: forced compositions of the object's cascade classes and the rank-2 degeneracy of the register overlap. Object-level geometry (overlap matrices, singular structure) the lexicon carries no motif for; the negative verdict does not make it instrumental. |
| `B986` | GAP | The B500 depth-5 reopen: eliminants of depth-5 trace-map words over GF(p), and whether the child field K = Q[t]/(t^4-t-1) occurs as a root field. Object-level arithmetic (the child, the F/M/D word grammar, resultant eliminants) the lexicon carries no motif for. The NEGATIVE verdict is about this seat's own *method* being vacuous, but the arc's subject is the object, so it is a GAP and not an INSTRUMENT. |
| `B998` | INSTRUMENT | The axiom chain's lock audit: which forks `test_b749_genesis_forks.py` actually tests versus which `THEOREM_LEDGER.md` cites. About the repository's own verification discipline — an object atlas is correct to miss it. |
| `B1065` | INSTRUMENT | the three amendment controls for B1024's SAME — equivariance/base-rate/joint-rank checks on the programme's own class-map machinery; an OBJECT atlas is correct to miss it |
| `B8087` | GAP | The neutrino selector: stabilisers of pure vs generic spinors in `so(10)` acting on the **16**, and the rank 5→4 drop. Object-level topic — spinor orbits, pure-spinor cones, the spinor variety `S₁₀` — that the lexicon carries **no motif for at all**, which is itself the finding: the atlas has motifs for roots, Levis and charges but none for the *spinor* side of the same algebra, so an entire half of the breaking chain (`⟨1⟩` reaches SO(10) by roots, `⟨ν^c⟩` leaves it by spinors) is invisible to it. Not instrumental — no repository machinery appears in the arc. |
| `B8090` | INSTRUMENT | Cold-audit finding on another seat's **summary layer**: a banked claim calling `sign(λ²)` a character when it is `−1` at the identity. The subject is the repository's own record-keeping and the group-theoretic type of a claim, not the object — **an object atlas is correct to miss it**. The only mathematics involved is the Klein group's multiplication table. |
| `B8092` | INSTRUMENT | The design audit: whether another seat's orchestration **prompts** could structurally exclude a positive. Its subject is the repository's own experimental design — guard wording, bite-witness placement, the grade enum — and contains no object mathematics at all. **An object atlas is correct to miss it**, and this is the clearest INSTRUMENT case in the register. |
| `B8096` | GAP | Re-running a residue hunt with a prompt guard relaxed to the banked condition it cites. The mathematics is object-level — Klein-orbit invariants of the λ family, and a resolvent-divisibility candidate killed by vacuity — but the lexicon carries no motif for the **coboundary/gauge-coset** layer, the same named miss B1076's own triage row records. Not instrumental: the guard-relaxation is the *occasion*, the invariants are the *subject*. |
| `B8105` | INSTRUMENT | R48 phase 1: a currency audit of the repository's own **synthesis surfaces**, and a registry found violating its own same-PR rule. The subject is the corpus's **document hygiene and gate coverage** — there is no object mathematics in it at all. **An object atlas is correct to miss it**, and the arc's own finding is that *no gate reads* the rule in question, which is the same class of blindness this register exists to record. |
| `B8107` | INSTRUMENT | R48 verification: checking that two review fixes actually landed, and finding the fix reproduced the pattern it fixed. Subject is the repository's **gates, protocol checklist and registry** — no object mathematics. **An object atlas is correct to miss it.** |
| `B8108` | INSTRUMENT | R48 phase 3: triaging the corpus's own synthesis surfaces by supersession banner. Subject is **document hygiene and the reviewer's own instrument**, with no object mathematics. **An object atlas is correct to miss it.** |
| `B8109` | INSTRUMENT | R48's closing report: which review instruments worked, which did not, and the positive-control principle for document scans. **Pure methodology**, no object mathematics — an object atlas is correct to miss it. |

**Open `GAP` count: 2** (`B899`, `B935` — leakage/deviation magnitudes and root-spacing geometry await a lexicon motif). `B537` was closed by B825's `markov_cubic` motif.

> **Zero open gaps means "no known uncovered object topic among substantial blind arcs" — NOT "the
> lexicon is complete."** The 18+1 motifs remain grounded in K001–K022 and unrevisited since
> 2026-07-01; B806's call for a full re-grounding is untouched.

**Known false-positive mode of `markov_cubic` (B825):** B821/B822/B823 dropped off this registry not
because they are about the Markov cubic but because they **quote** it while discussing the gap. A
regex motif matches *mentions*, not *subjects*. Recorded rather than filtered, because filtering
would mean classifying by topic — the thing B822 refused.
