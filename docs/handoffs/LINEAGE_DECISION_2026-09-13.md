# THE LINEAGE DECISION — make the historical line canonical, by FAST-FORWARD

*Written 2026-09-13 for whoever banks next. **This is a recommendation with its evidence, not an
action taken:** `main` is untouched and this bench did not move it.*

**The short version: `main` can be fast-forwarded onto the historical line. Nothing is lost, the
history is recovered, no force-push is involved, and it fixes known-red tests. Do that rather than
harvest.**

---

## 1. What actually happened — it was not drift

`main` and the historical line **never shared a root to drift apart from.**

| | commits | root | span |
|---|---|---|---|
| `main` | **50** | `72f1f7fb` (2026-09-06) | 2026-09-06 → 09-09 |
| the historical line | **3135** | `517783f2` (2026-05-22) *"Initialize the Origin Axiom canonical repository"* | 2026-05-22 → 09-10 |

**`main`'s root commit landed 9400 files in one commit**, and its message is not an announcement — it
is an ordinary arc write-up ("THE JOIN CLOSES…"). A working tree was committed into a fresh
repository and work continued from there. **This happened more than once:** the historical line
contains **three** root commits — `517783f2` (05-22), `5e421117` (08-30) and `72f1f7fb` (09-06) — so
the tree was re-founded at least twice and the lane absorbed each new root.

**And the mechanism is stated in the repo's own commit messages.** The lane kept itself current with
`main`, one-directionally:

> `a2d4fc19` — *"Merge origin/main into the outside bench lane so fixes apply against current main"*
> `2a3ac6ce` — *"Keep the lane current: merge main (2 commits…)"*
> `e7d62df7` — *"Keep the lane current: merge main again (11 commits)"*

**The lane consumed `main` and never published back.** That is the whole of it. Not an accident, not
neglect — a deliberate one-way discipline that nobody ever closed the loop on.

## 2. Why the "3085 commits ahead" number is misleading

`git log main..outside-bench` = **3085**, which reads like an enormous backlog. It is not.
**3061 of those are pre-snapshot history** that `main` cannot reach because `main` was re-founded
rather than grown. **The genuinely unlanded recent work is 24 commits** (23 non-merge), dated after
the 2026-09-09 fork point.

## 3. THE DECIDING FACT — it is a fast-forward

```
git merge-base --is-ancestor origin/main <historical tip>   →   TRUE
```

**`main`'s tip `b94ed03a` is already an ancestor of the historical tip `940b24fb`.** So:

* **no rewrite, no force-push, no history surgery** — `main` simply moves forward;
* **`main` loses nothing**, because all 50 of its commits are already contained;
* **the paper-verification branch still merges as an ordinary branch** afterwards, its base
  `b94ed03a` being in that history.

This is the unusual case where the big-sounding option is the **safe** one.

## 4. What the tree gains, measured

`git diff origin/main <historical tip>` → **673 files changed, 84 482 insertions, 255 deletions.**

The 255 are **edits, not removals**: all 42 files that lose a line gain more than they lose. And the
gains are not inert — **the historical line already fixes tests that are red here**, better than this
bench would have written them. The clearest example, `test_b565_realform::test_snappy_gate`:

> *"The holonomy is a PSL(2,C) representation; an SL(2,C) lift is only defined up to a sign character
> χ: H₁ → {±1} … SnapPy 3.3.2 returns the lift with χ(a) = −1, so tr(a), tr(aB) and tr(ABB) all come
> back negated and a literal comparison fails while the representation is unchanged."*

Their repair requires **exactly one** sign character to reproduce **all three** pinned traces — which
is *stronger* than a per-word "match up to sign", because per-word matching would pass for a
representation that is not the holonomy. `test_b616_heldout` and B511's `d3_wild_access.py` have
comparable treatment. **This bench spent today re-deriving one such fix (the B1062 logs) before
finding it already existed.**

## 5. FAST-FORWARD, NOT HARVEST — and why the distinction matters here

**Harvest is the wrong instrument.** Re-deriving findings instead of moving commits is *precisely the
habit that produced this split*. And the entire reason to prefer the historical line is that it
**keeps the provenance** — which harvesting discards. Harvest is for another seat's *conclusions*;
this is our own history.

## 6. THE ONE DUE-DILIGENCE STEP, not yet done

**The fast-forward is verified possible; the historical tip is NOT verified healthy.** Before
flipping canonical, at that tip: run the full suite, run `scripts/gates/gates.py`, and check the
arc-verdict/id integrity gates. **Do not skip this** — a fast-forward is safe for *history* and says
nothing about *content*.

## 7. THE ROOT-CAUSE FIX, which matters more than the merge

Moving the pointer fixes today. It does not fix the pattern, and **the pattern has cost real work at
least three times this week**:

1. the B1062/B1137 evidence fix, re-derived here before being found already done (L210);
2. B1400 — a seat correctly audited `origin/main`, reported 16 literature terms absent, and **8 of
   them already existed** on this branch;
3. **E77** — both narrative logs frozen for 25 arcs while the gate stayed green, because it enforces
   that two files move *together*, not that either moves *at all*.

**The common cause: seats hand each other findings, not commits.** That is excellent for
verification — independent re-derivation is the method, and it works — and it is silent about
integration. Whatever is decided about the lineage, **one of these needs to become mechanical**:

* a **merge lane that runs both ways**, not only main → lane; or
* a **liveness check** — fail when a branch holding banked work has not landed in N days, the same
  shape as `doc-currency`'s declared debts, which are noisy *on purpose*; or
* simply **one lane**, which is what §3 makes cheap.

## 8. Status at the time of writing

`main` untouched at `b94ed03a`. Paper-verification branch at `44ca6c35`, 70 commits, all pushed,
31 of 32 gates passing, 7 suite failures — **none of them this bench's**, and several of which §4
suggests the historical line has already fixed.
