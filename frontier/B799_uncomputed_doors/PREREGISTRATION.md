# B799 — PREREGISTRATION: the twelve uncomputed doors (Compaction W0)

**Sealed before any computation.** cc banking seat, 2026-07-29. Owner directive: green light on the
Compaction Masterplan, whose **W0** was resequenced to first at review — a known violation of the
programme's own standing rule must not wait behind an infrastructure programme.

**Scope: repository-quality and mathematics only. No physics reading. Nothing to `CLAIMS.md`.**

---

## 1. The object

`frontier/B738_pathfinder_compiler/kill_graph.json` carries **217 classified negatives**. Exactly
**12** carry `fact_computed: false` — closures where the discriminating fact was, by the compiler's
own classification, never computed in-sandbox.

The programme's standing rule (B525 audit; memory-anchored): *a negative is only as sound as the
in-sandbox computation of its **discriminating** fact — never asserted, cited, or proxied.* Twelve
banked closures do not meet it. This arc resolves each one, in one of four ways, **declared here
before looking**.

The twelve: **B140, B332, B412, B433, B435, B579, B668, B685, B720, B731, W7-rebase,
S019-Fisher-metric**.

## 2. The four permitted outcomes (declared before compute)

Every door lands in exactly one. **No fifth outcome is available**, and in particular there is no
"looks fine on reading" disposition.

| outcome | meaning | what it requires |
|---|---|---|
| **COMPUTED** | the discriminating fact is computed in-sandbox, here, and the closure **stands** | exact computation + a test lock |
| **COMPUTED-OVERTURNS** | the fact is computed and the closure **does not survive it** | exact computation + retraction of the kill |
| **IN-REPO-CITED** | the fact is genuinely computed and **locked in another arc of this repo** | the cited arc's lock must be named AND observed to pass |
| **HONEST-DOWNGRADE** | the fact cannot be computed in-sandbox now | relabel the closure as *uncomputed*, with the reason; `NEEDS-SPECIALIST` only if the in-sandbox route is **exhausted**, never merely long |

## 3. Two-outcome criteria, per door class

**IN-REPO-CITED is not a free pass.** It is granted only if the cited arc's discriminating
computation exists AND its test lock is executed and observed to pass *in this arc's run*. A citation
to an unlocked or absent computation **fails** to IN-REPO-CITED and falls to HONEST-DOWNGRADE. This
is the criterion that can fail, and it is the point of the arc: `IN-REPO-CITED` must not become the
new proxy.

**COMPUTED requires the fact that discriminates**, not a fact adjacent to it. For each door the
prereg names below what would count; anything else is HONEST-DOWNGRADE.

| door | the discriminating fact that must be computed | falls to |
|---|---|---|
| **B140** | that no non-principal φ-fixed point carries ℚ(√−3) (the retracted "~35" claim), and that orientation-reversal is genus-independent at the level used | HONEST-DOWNGRADE |
| **B332** | `det(A − I) = −1` for the deck element, forcing hyperbolic (⟹ g is not the generation-cycling deck element) | HONEST-DOWNGRADE |
| **W7-rebase** | the E₆ centre acts on the **27** as the scalar ω (hence splits nothing) | HONEST-DOWNGRADE |
| **B412, B433, B435, B668** | the cited in-repo arc (B408, B426, B437, B662 respectively) contains the computation **and its lock passes here** | HONEST-DOWNGRADE |
| **B731** | *already retracted by B734 (E22)*: verify the retraction is banked, then relabel — this record is stale, not merely uncomputed | HONEST-DOWNGRADE |
| **B685, B720, B579, S019** | expected HONEST-DOWNGRADE (external-source integrality; literature classification; a proxy kill resting on the seat's own failed derivations; a claim never well-posed) | — |

## 4. What would make this arc a failure

- Any door dispositioned **IN-REPO-CITED without running the cited lock**.
- Any door marked **COMPUTED** on a fact that does not discriminate the closure.
- Any use of **NEEDS-SPECIALIST** before the in-sandbox route is exhausted.
- Reporting fewer than 12 dispositions.

## 5. Pre-stated expectation (so the result can disappoint it)

I expect roughly: 3 COMPUTED, 4–5 IN-REPO-CITED, 4–5 HONEST-DOWNGRADE, 0–1 COMPUTED-OVERTURNS.
**If every door lands COMPUTED or IN-REPO-CITED, that is a warning sign, not a success** — it would
mean the compiler's `fact_computed: false` flag carries no information, and the flag itself would
then need auditing.

## 6. Deliverables

- `FINDINGS.md` — 12 dispositions, one per door, each naming its discriminating fact.
- `doors.py` — the in-sandbox computations for the COMPUTED class.
- `kill_graph_patch.json` — the corrected records (the original file is **not** rewritten in place;
  B738's artifact keeps its provenance).
- `tests/test_b799_doors.py` — locks for every COMPUTED fact, and an executable assertion that each
  IN-REPO-CITED door's cited lock exists.

## 7. Firewall

Mathematics and repository quality only. No physics claim, no value comparison, no Gate 5 surface,
nothing to `CLAIMS.md`. Where a door's subject matter is physics-adjacent (B433's 3d-3d, B579's
values package), this arc adjudicates **only** whether the discriminating fact was computed — never
whether the physics reading is true.
