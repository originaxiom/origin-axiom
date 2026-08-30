# THE PUBLICATION CAMPAIGN — the six things between here and publication-ready

**Opened 2026-08-30 (owner-directed, after Review 53). Expectations are pre-registered below,
before any cell runs, because the last campaign's pre-registration was wrong in an instructive
way (B1216: *"the one cell predicted least likely to produce forward motion is the only one that
did"*) and that is only visible if the prediction is on the record first.**

## 0. Why the order is what it is — and it is not a preference

Twice on 2026-08-30 this bench asserted something was open that was already banked:

- six "remains open" claims made without running `already_banked.py`, of which **three were
  closed** (the A2 stratum, the hypercharge direction, the spin lift);
- and, *on the same day the E53 class was minted*, the relayed claim that **B632's cell 2 is
  "queued and unrun"** was propagated into four surfaces before checking. **Cell 2 ran
  2026-07-15**, under a sealed prereg, verdict PROVED — and the canonical `PROGRESS_LOG.md` had
  carried the entry since the day it happened.

So the campaign's first cell is not a math cell. **Nothing in this campaign may be called open
until Cell 0 has run on its terms.** A campaign that skips this spends its budget re-deriving
its own record.

---

## Cell 0 — THE REVERSE SWEEP (discharges R53-3) · runs FIRST, gates Cells 1–3

**The gap.** `open_claim_sweep.py` runs **surfaces → arcs**: it takes a claim of openness and asks
whether a settled arc already decided it. That direction cannot see a banked result that *no
surface mentions at all* — there is no claim to match. B1188 measured that population at **132
PROVED on-theme arcs absent from every live surface**, and B985 measured the bias that produces
it: object-faces recover at 79–100%, **relation-faces at 6–19%**.

**The computation.** The other direction: **arcs → surfaces.** For each settled arc, take its
claim's distinctive terms and ask whether *any* live surface carries the result. Rank the misses
by on-theme weight. Output: a triaged list — SURFACE-IT (a result that belongs on a named
surface), SUPERSEDED (a later arc owns it), or INTERNAL (an instrument arc an object-facing
surface is right to omit).

**MB12 / bite control, both directions, mandatory before any output is read.**
*Positive*: B1188's five sharpest off-surface arcs (B279, B769, B786, B293, B552) must be flagged.
*Negative*: arcs that are demonstrably well-surfaced (B1141 and B1170, both now cited on multiple
surfaces) must **not** be flagged. If either control fails, the run is void.

**Pre-registered expectation (this bench, before running).** 40–90 of the 132 genuinely
off-surface; **at least one bearing directly on Cells 1–3.** Stated because it is falsifiable: if
Cell 0 returns fewer than ten, E53 was over-diagnosed and this campaign should say so.

**Falsifier for the instrument itself.** If the reverse sweep flags results the surfaces *do*
carry — i.e. it cannot distinguish absence from paraphrase — it is measuring vocabulary, not
propagation, and must be withdrawn rather than tuned until it looks right.

---

## Cell 1 — λ's ACCEPTANCE GATE (not λ's value)

**The gap, stated exactly.** λ is the ledger's weakest row and the reason is sharper than "we
have not derived it": **no criterion exists by which it could be derived or refused.** A row that
cannot pass and cannot fail is an MB12 vacuity sitting inside our own freedom ledger. The
deliverable of this cell is therefore **a gate, not a number.**

**What λ is.** The object's own algebra is the timeless tracial II₁ factor; an **external weight**
completes it to type III_λ, and the closer's clock enters exactly there (B723).

**The template that exists.** σ's row is *not* closed either, but it is **gated**, and the gate is
an *identification*: c_BH = 6σ and c((E₆)₁) = 78/13 = 6, so proving the boundary theory is (E₆)₁
**is** σ = 1. λ needs its structural analogue.

**The computation.** Write the criterion in the form: *λ is accepted iff there is a canonical
weight on the object's algebra whose Connes modular spectrum is S(M) = {λⁿ} ∪ {0} with λ fixed by
an invariant already banked.* Then enumerate the candidate invariants the corpus actually owns —
the fundamental unit at the golden end, exp(−Vol), the Ruelle/Selberg data, and the
basepoint-free tower growth-rate channel (B1116) — and state for each whether it *could* supply λ
and what would refute it.

**MB12 gate on the gate — the cell fails without this.** The criterion must be shown to
**reject** at least one concrete candidate weight. A criterion that accepts everything offered is
the vacuity we are trying to remove, relocated.

**Pre-registered expectation.** Writing a *failable* gate: likely. λ *closing*: **not expected
this campaign**, and the cell will say so rather than reach.

---

## Cell 2 — THE ℙ³'s SECOND CONDITION, decided by exhaustion

**Where it stands.** The cubic supplies one nonlinear condition and the coupling one canonical
linear functional: 3 → 2 → 1. A point set needs 0. B1206 found the mechanism: a cubic term
C(X, Y, ·) becomes a **linear functional** on B₀ as soon as its other two legs are pinned to
unique states. H_u is 1-dimensional (sector table Q/dc/Hd/Hu = 3/3/4/1), so it pins
automatically; of the 27's two neutrals only N₁ gives a nonzero row.

**The computation.** Enumerate **every** cubic term of the invariant and **every** multiplicity-1
sector, and decide by exhaustion whether a *second* independent pinning exists.

**Why this is worth running even though the expected answer is no.** If exhaustion returns none,
the ℙ³ row converts from *"an open continuous row"* to **a proven no-go: the construction is one
condition short and cannot be completed from inside.** That is a result, and a publishable one —
it changes the ledger row's type rather than leaving it hanging.

**Bite control.** The enumerator must **recover the known pinning** (the 1·10·10 term via H_u).
An enumerator that finds nothing including the thing we already have is broken, not decisive.

**Pre-registered expectation.** **No second condition** — because the sector table has exactly one
multiplicity-1 entry. Recorded now so that finding one counts as a genuine surprise.

**Consequence already registered in the paper, before the run.** Should the row close, the result
is a **finite point set, not a unique prediction** — the row converts to a finite label. That
sentence is already in §7 precisely so it cannot be added afterwards.

---

## Cell 3 — B632 CELL 3: the symmetric texture on the double

**The correction that produced this cell.** Cells 1 and 2 are **done and PROVED**. Cell 2 ran
2026-07-15: the cubic invariant C is exactly unique in B575's basis (45 zero-weight-sum triples;
a 180-equation invariance system with a 1-dimensional solution space; all 45 coefficients
nonzero); the forced vev couples to **all three** generation slots, B_C block-diagonal (the sl₂
prediction **verified**) with c₀, c₄, c₈ all nonzero; the component census reproduces the triangle
rules exactly; and Ω: Λ²H¹(27) → H²(M;27*) is nonzero on all three pairs, so **no generation-pair
decouples**. The cell-1 "three diagonal values" prediction resolved **DISSOLVED-BY-OBSTRUCTION**.

**What is actually unrun.** **Cell 3, registered with its own prereg**: the *symmetric* texture on
the **double**, via Mayer–Vietoris from banked pieces. The solo object carries the antisymmetric
half; the symmetric half is not on the solo object at all. The double is where h¹(M;27) = **5**,
not 3.

**This is the live generation computation on the record** — and it is the one cell in this
campaign whose outcome this bench genuinely cannot predict, which is exactly why it has the most
information in it.

**Discipline, non-negotiable.** The existing sealed prereg governs; it is not rewritten to suit
the run. **No SM comparison anywhere** — that is a separate sealed round under the owner's
standing directive, and Gate 5 holds throughout.

**Pre-registered expectation.** None offered. Declining to guess is the honest state here, and a
guess entered now would only contaminate the reading.

---

## Cell 4 — THE REFEREE-FACING VERIFICATION APPENDIX

**The deliverable.** Every load-bearing claim in the paper mapped to the arc that establishes it,
that arc's `verification/reproduce.sh`, and its test lock — so a referee can re-run the paper
rather than believe it.

**The falsifier, and it is the point.** Any paper sentence that cannot be traced to a
reproducible arc is either **repaired or deleted**. The appendix is built to find those, not to
decorate the ones that pass.

**Bite control.** The generator must be shown to **fail on a deliberately unsupported sentence**
inserted for the test. An appendix that certifies whatever it is given certifies nothing.

**Depends on:** Cells 0–3 landing, since each may change what the paper claims.

---

## Cell 5 — THE HOSTILE READ OF §3, from both directions

**Runs last, on the final text.** The new chain section has had **no** adversarial pass; the rest
of the paper has had five.

**Both instruments, because this window proved they are not substitutes.** The cloud seat's line
is the finding: *"five adversarial passes caught every defect on the page and none of the one that
required reading the record."* So §3 gets **a page read** (is the argument sound as written?) and
**a record read** (does the corpus actually say this?) — and the record read is the one this
programme has been under-investing in.

**Specific exposures to attack, named in advance so the pass cannot be graded on softballs:** the
43-link count and its type breakdown; the claim that C6–C17 contains no axiom; the assertion that
M² = RL *is* the orientation axiom rather than merely illustrating it; the four-route failure and
whether "bought at geometrization and nowhere earlier" overstates it; and whether the McKay
doorway is stated in the form that survives, given a weaker version was retracted.

---

## Sequencing, stop rules, and what would end this campaign early

```
Cell 0  (the reverse sweep)         ──►  gates 1, 2, 3
                                          │
              ┌───────────────────────────┼───────────────────────────┐
              ▼                           ▼                           ▼
        Cell 1 (λ's gate)          Cell 2 (ℙ³ exhaustion)      Cell 3 (B632 cell 3)
              └───────────────────────────┼───────────────────────────┘
                                          ▼
                                  Cell 4 (referee appendix)
                                          ▼
                                  Cell 5 (hostile read, both directions)
```

**Stop rules.**
1. **Cell 0 gates everything.** If it finds banked work bearing on Cells 1–3, those cells are
   redesigned before they run, not after.
2. **No cell reports a positive without its bite control passing first.** A control that fires
   only after the result is known is not a control.
3. **A cell that cannot state what would refute it does not run.** Cell 3 is exempt from
   pre-registered *expectation* but not from its prereg's falsifiers, which are already sealed.
4. **Gate 5 holds throughout.** No measured physical value enters the paper or any cell's output.
5. **The suite certifies the exact tree before any push** (E39), and no tree mutation during a
   certifying run (E46). Both were violated once each today; both are now in the review.

**What this campaign does NOT promise.** It does not close λ. It does not make the construction
parameter-free — the four axioms are structural and named, and no cell here removes one. What it
promises is that **every remaining row is either closed, converted to a proven no-go, or given a
criterion by which it could fail** — and that the paper's claims are reproducible by a stranger.
