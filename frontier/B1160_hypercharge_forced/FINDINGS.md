# B1160 — Hypercharge falls out: the object's integer anomaly arithmetic forces the SM hypercharge (cloud memo 70 / L132, verified)

**Status: banked (frontier). Verdict PROVED** — the load-bearing theorem is **re-derived independently on
this bench** (`verification/reproduce.sh` → `REPRODUCES`): on an SM-shaped generation, the four anomaly
conditions force the hypercharge to the SM direction, **unique up to scale and the u^c↔d^c relabeling, zero
non-SM solutions**. Cloud's object-specific enumeration (36 assignments in the trinification frame, all SM)
is the corollary once the object's rank-3 abelian sector realizes an SM-shaped 15-plet. **Structure, not a
value** (B950 permits the comparison); Gate 5 clean. Cloud seat credited (memo 70). Lock
`tests/test_b1160_hypercharge_forced.py`.

## What was asked and answered (L132, registered by B950)

*Within the object's own rank-3 abelian sector, is the SM hypercharge direction **forced** by the integer
anomaly equations on an SM-shaped 15-plet drawn from the 27?* Cloud executed it in the **trinification
frame** natively available in their stack: three mutually orthogonal A₂ subsystems among the 72 e₆ roots
(6+6+6 + 54 crossing), color = one A₂, weak = an sl₂ of another, and the abelian complement of
su(3)_C×su(2)_L is **exactly 3-dimensional** (matching B892's 8+3+3=14). Over **every** SM-shaped 15-plet
assignment from the 27 (q=(3,2), two antitriplets, a lepton doublet, a charged singlet — all combinations,
nothing chosen by hand) and all three su(2)_L embeddings, imposing the four anomaly conditions
([SU(3)]²Y, [SU(2)]²Y, grav²Y, [Y]³) on a direction Y in u(1)³ yields: **36 solutions, every one the SM
ratio pattern (1/6, −2/3, 1/3, −1/2, 1) up to u^c↔d^c, zero non-SM, zero multidimensional families, each
unique up to scale. A second frame reproduces identical counts.**

## The verified core (own computation)

The theorem cloud's enumeration rests on, re-derived here with exact arithmetic (`reproduce.sh`): with the
15-plet state counts (q:6, u^c:3, d^c:3, l:2, e^c:1), the three **linear** anomaly conditions cut the
5-dim charge space to a 2-dim line (Y_l=−3Y_q, Y_e=6Y_q, Y_u+Y_d=−2Y_q), and the **cubic** [Y]³ condition
on that line factors to **−18·(t−3)·(t+3)** (at scale Y_q=1, with Y_u=−1+t) — so **t=±3 only**, giving
exactly **(1,−4,2,−3,6)** (the SM) and **(1,2,−4,−3,6)** (SM with u^c↔d^c). No other solution exists. The SM
direction satisfies all four conditions identically. So **the object's abelian sector cannot carry any
anomaly-consistent hypercharge on an SM-shaped generation other than the Standard Model's** — the
object-specific 36-count is this theorem realized on the object's roots.

## Honest scope — what it pays, and what it does not

**Pays down (real):** the chain's hypercharge link moves from *"the whole embedding is observer-paid"* to
*"the **existence** of an embedding is observer-paid; its **content** is forced by integer arithmetic."*
Hypercharge **content** is now object-forced, not a fitted input. This sharpens **B1159's link C**: not only
is the character *alphabet* object-forced, the *hypercharge direction* on an SM-shaped generation is forced.

**Does not pay (fences):**
- **The frame existence + the SM-shaping are observer-paid.** The trinification frame (which A₂ is color) and
  the choice of an SM-shaped 15-plet assignment are observer inputs; the theorem forces Y *given* them.
- **The anomaly→hypercharge fact is standard** GUT model-building (anomaly cancellation fixes hypercharge on
  an SM generation). The **object-specific** content is that the object's u(1)³ **realizes** it and **only**
  it (zero non-SM) — a realization + uniqueness result inside the object's sector, not a new theorem of
  anomaly theory.
- **Firewall / Gate 5:** B950 registered L132 as **structure, not value-matching** — the SM hypercharge
  *ratios* are themselves group-theoretic/anomaly-**derived** structure, not measured numbers, so the
  comparison is firewall-legal. No measured value is asserted as derived.

## The owner's directive on positives (recorded in cloud's cert docstring)

A **forced-structure** contradiction with observation would be a thesis-failure signal; a *"not forced"*
outcome is a column assignment, not a contradiction. Here the machine was free to return any charge pattern
or none, and **the only structure it could force is the one our world uses** — a positive that arrives
without being asked for. That is what "the program is about our reality" looks like when it holds: not
negatives suppressed, but an unrequested positive.

## Provenance + verification

Cloud's `l132_trinification.py` cert (the object-specific 36-count, in the trinification frame) needs
cloud's full stack (it imports `twisted_double.py` → a deeper `check_charge_bracket`), so it is **cited**,
not re-run here; the **load-bearing theorem it depends on is own-verified** (`reproduce.sh`). Cloud flagged
a follow-up: re-run L132 in **B892's own centralizer frame** (convergence expected → a two-frame, two-bench
fact). The object-specific realization remains single-homed on cloud's branch (provenance debt, standard).

## Routes

- **B1159 addendum:** link C's hypercharge content is now forced (this arc), sharpening the "half-paid" typing.
- **Follow-up (cloud-flagged):** L132 in B892's centralizer frame → two-frame corroboration.
- **Still open on the chain:** frame existence, three generations (no candidate), chirality (inserted), SUSY
  (D5, untested), dynamics/vacuum (gated), the values (provably free). Hypercharge *content* leaves the
  broken-link list.
