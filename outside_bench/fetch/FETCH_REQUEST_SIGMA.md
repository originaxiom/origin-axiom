# FETCH LIST — what this bench cannot reach, and exactly what is needed from each

**2026-09-07.** The owner offered to download what the egress proxy blocks. **Verified blocked from
this machine:** `arxiv.org`, `export.arxiv.org`, `ar5iv.labs.arxiv.org`, `web.stanford.edu`,
`people.mpim-bonn.mpg.de`, `semanticscholar.org`, `inspirehep.net` — via **both** `curl` and
`WebFetch`. So everything below is genuinely unreachable, not merely awkward.

**Purpose:** finish memo 171 §5 — the four-step computation that decides σ.

**How to hand it back:** paste the relevant passage into chat, or drop the PDFs/text into
`outside_bench/fetch/` on any branch and push; I will pull and read.

---

## PRIORITY 1 — the decisive one. If you fetch only one, fetch this.

**arXiv:1904.06057** — Gukov & Manolescu, *A two-variable series for knot complements*
*(also at `web.stanford.edu/~cm5/surgeries.pdf`)*

> **NEEDED: the explicit `F_K(x,q)` series for the FIGURE-EIGHT KNOT `4₁` — as many terms as
> printed, exactly, with the section/equation number.**

**Why it is decisive:** this is the object itself. `B1191`/GC-12 typed the missing piece as *"a
genuine boundary character no banked artifact supplies"* — **this is that character, for our knot.**
With the coefficients in hand I can run **GC-6's own `c_eff_series` estimator** on the object for the
first time, instead of on the `η⁻¹` free-boson substitute it has been using. That is steps 2–4 of
memo 171 §5, executable same-day on this bench.

---

## PRIORITY 2 — the relation memo 171 rests on, currently CITED/UNVERIFIED

**arXiv:2508.10112** — *`c_eff` from Resurgence at the Stokes Line*
**arXiv:2508.10087** — Harichurn, *`c_eff` from Surgery and Modularity* (DIAS-STP-25-20)

> **NEEDED: (a) the precise definition of `c_eff`; (b) the exact statement relating it to the
> Virasoro `c` — I have it from search snippets as `c_eff = c − 24·min(h_i)`, and need it verbatim;
> (c) whether either paper computes `c_eff` for any HYPERBOLIC knot complement, especially `4₁`.**

**Why:** memo 171's entire §2–§3 — the claim that GC-6 compared a Virasoro `c` against a unitary
substitute's `c_eff` — **depends on this relation being stated as I have it.** If the relation is
different, the type-error finding weakens or dies. **This is the one that could refute me.**

---

## PRIORITY 3 — does our object even have such a character?

**arXiv:1909.13002** — *Higher rank `Ẑ` and `F_K`*

> **NEEDED: is `F_K`/`Ẑ` defined for HYPERBOLIC knot complements (as opposed to negative-definite
> plumbings / torus knots), and is `4₁` treated? Any statement about existence or obstruction.**

**Why:** this is `Q11`'s actual question, the one already sent to Dimofte. If the literature already
answers it, the letter's ask narrows before he replies.

---

## PRIORITY 4 — the blocker memo 171 did NOT move

> **NEEDED: anything on whether `Ẑ`/`F_K` or its log-VOA character is sensitive to `CS = 0`, or to
> the manifold being AMPHICHIRAL.**

**Why:** `B1064`'s obstruction — amphichirality deletes the quantized sector — is **untouched** by
memo 171. Re-typing the count does not restore a deleted attachment. **Two blockers; only one has
moved.** Any statement bearing on this is worth as much as Priority 1.

---

## ALSO USEFUL, LOWER PRIORITY

- Zagier, *Knots, perturbative series and quantum modularity*
  (`people.mpim-bonn.mpg.de/zagier/files/preprints/KnotsAndQuantumModularity.pdf`) — the quantum
  modularity of `4₁` specifically; the corpus's `B1120`/`B1124` Kashaev-tower arithmetic lives next
  door to this and has never been checked against it.
- **arXiv:2604.16077** — *Volume Conjecture and quantum hyperbolic invariants: the figure eight knot
  complement* — recent and squarely on our object.

---

## THE ONE-LINE VERSION

**`F_K(4₁)`'s explicit series + the exact `c_eff`/`c` relation = everything I need to run memo 171
§5 to a verdict on σ.** Everything else sharpens or refutes; those two finish the computation.
