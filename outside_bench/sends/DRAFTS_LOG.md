# THE SEND LOG — what has actually left, and what is sitting in drafts

**Standing instruction, 2026-08-31 (supersedes the send in row R71):**
> *"all aproved, just dont send them, leave in drafts ready to be sent."*

**So: compose and CREATE DRAFTS. Do not transmit.** Note for any later seat — the Gmail connector's
`send_message` **transmits immediately, with no draft step**; `create_draft` is the separate tool and
is the only one to use under this instruction.

---

## HOUSE STYLE (owner's instruction, 2026-08-31)

> *"make the emails seam wrriten by human, not ai"*

**All seven drafts were rewritten as letters.** What was cut and why — the tells were real:

- **ALL-CAPS section headers** (`THE SETUP`, `WHAT WE DO NOT CLAIM`) — nobody writes a cold email
  to a colleague with headers. Gone; the same content is now prose.
- **Identical architecture across all seven.** This was the worst of it: mathematicians in adjacent
  fields talk, and seven letters with the same skeleton would read as generated the moment any two
  were compared. **Each letter now has its own shape and length** — Andersen's is short because he
  wrote the thing being asked about; Gannon's leads with the striking fact; Thorne's opens by
  admitting it's a cold email.
- **The tidy symmetric "why either answer pays" block.** Real people say *"that would suit me as well
  as a positive one"* in passing, mid-paragraph.
- **The quarantined `WHAT WE DO NOT CLAIM` section.** **Every fence is still there** — it is now said
  the way a person says it (*"I should be honest that I don't expect the count to be 1"*,
  *"that's a guess from the shape of the problem rather than anything I derived"*, *"I'd very likely
  get it wrong"*). **Nothing was softened to sound casual.**
- **Corporate "we"** where one person is writing. Now first-person singular throughout.

**`Q11` to Dimofte went out in the old style and cannot be recalled.** Noted so a later seat does not
wonder why one sent letter reads differently from the seven drafts.

---

## SENT (one item, before the draft-only instruction)

| item | to | when | id |
|---|---|---|---|
| **Q11 — the σ bridge** | **Tudor Dimofte**, `tudor.dimofte@ed.ac.uk` (verified: Professor & Personal Chair of Geometry and Physics, Edinburgh; Higgs Centre) | 2026-08-31, on *"ok, i aprove"* | msg `1a05a10d88d4971a` |

Verbatim record: `outside_bench/sends/Q11_DIMOFTE_READY.txt`.

---

## IN DRAFTS — composed, **awaiting the owner's send**

**Address verified** (checked this session against the person's own institution/department page):

| item | to | draft id | msg id |
|---|---|---|---|
| **Q7 — Route A / integral orbits** | **Jack Thorne**, `thorne@dpmms.cam.ac.uk` — Kuwait Professor of Number Theory & Algebra, DPMMS Cambridge | `r667423517285828338` | `1a05b8467c156de0` |
| **Q1 — SEAM-A Gate 2** | **Jørgen Ellegaard Andersen**, `jea@sdu.dk` — Professor, Head of the Centre for Quantum Mathematics, SDU. **He is the "A" in Andersen–Hansen: the ask goes to its own author.** | `r1656145960915783272` | `1a05b8d197101f18` |

**Address needs YOUR confirmation before sending** — one candidate, not certain:

| item | to | why flagged | draft id | msg id |
|---|---|---|---|---|
| **Q3 — the B491 seam form** | **Terry Gannon**, `tjgannon@ualberta.ca` | **two addresses surface** — this one and an older `tgannon@math.ualberta.ca`. Drafted to the current-looking one. **Confirm on his department page.** | `r-8184297143157010156` | `1a05b84baf477cd5` |

**Recipient field deliberately left EMPTY** — the person is identified in the draft's own opening
block, but **no address was confirmable from this machine** (public search did not return one and the
egress proxy blocks the department pages). **I did not guess an address for a real person.** Each
draft opens with a bracketed block naming the intended recipient and why; **delete that block before
sending.**

| item | intended recipient (named in the draft) | draft id | msg id |
|---|---|---|---|
| **Q8 — Gate B, the `T[4₁;E₆]` crux** | a 3d-3d specialist **other than Dimofte**, who already has Q11 — the brief names **Gukov's group** and the **Gang–Yamazaki / Terashima–Yamazaki** lineage | `r7373359908195091086` | `1a05b8d60d710cba` |
| **Q2 — J₃(𝕆) Beilinson regulators** | **Alexander Goncharov** (Yale) — polylogarithms, regulators, Arakelov motivic complexes | `r1866070633817661341` | `1a05b8db68ff2aa4` |
| **Q4 — Cappell–Miller order of vanishing** | **Werner Müller** (Bonn) — his GAFA 2020 and J. Geom. Anal. 2021 papers are exactly the cusped setting | `r7865600470961527096` | `1a05b8dffb97fc33` |
| **Q5 — complexified hyperbolicity** | the **Cantat–Loray** lineage (IRMAR / Rennes) — both have written on dynamics on character varieties of the once-punctured torus | `r8928946916564439964` | `1a05b8e40f419c51` |

### What each draft carries

Every one is written to memo 140's standard — **tell the specialist what we closed ourselves**, so
nobody spends an hour on a route we already killed:

- **Q7** — `h(K) = 1` with the Minkowski work explicit; determinant 5 squarefree via Krutelevich Cor
  16; the stabilizer **identified** (dim 28 by construction; centroid 1 + Killing rank 28 ⟹ central
  simple ⟹ **D₄ forced**, which also excludes `Res_{L/F}(𝔤₂)`; commutant 12 not 18 ⟹ **simply
  connected**; the object's own pair regular). Asks **only the fifth hypothesis**. `B990`'s
  unfavourable prior is stated in the email **with its reason**.
- **Q1** — Lee's Thm 2 read on-bench, not cited second-hand; **`|a₁| = 1` at all four ideal points**
  re-derived from our own A-polynomial, so the tangential-base-point torsor is trivial and gives
  nothing; the CS = 0 contact closed too. Says plainly that Lee's Conj. 7.4.2 is still a conjecture.
- **Q3** — states the object in native language with the exact witness
  `t(0,4) = −1/48 − (1/80)√5 − (1/48)√−3 + (1/48)√−15`, then **asks whether it is known**. Novelty is
  the question, not the claim.
- **Q8** — reports our own **refutation** of the "three breaking scales" reading relayed to us
  (`dim H¹ = 6 = rank E₆`, uniform — that spectrum was G₂⊕A₂, not E₆) and two sub-paths we closed
  negative. Says the fold is forced but **the chain stops at F₄**.
- **Q2** — states our **negative** result first (216-cell exact grid, 18 targets sealed by hash
  before the search, extended basis, no hit) and asks **only** the exceptional tier.
- **Q4** — asks three sharp questions and admits the cusp-correction shape is **our guess, not a
  derivation**, and that we do not have the analytic machinery in-house.
- **Q5** — asks only whether the off-axis question is **decidable**, so we know whether to pursue it;
  Q6 rides along in one sentence as explicitly *not worth your time on its own*.

**Fences held in all seven:** no Standard-Model claim; no physics claim; each states what we do
**not** assert; each offers the exact working and code on request; each says a negative answer is as
useful as a positive one. **Gate 5 clean — no measured value in any of them.**

---

## NOT DRAFTED

- **Q6** — a rider on Q3/Q5 by the queue's own design, folded into Q5's closing line. Not a send.
- **Q9** — **withdrawn by this bench** pending a rewrite around the live mechanism. Sending it as
  written would put a question to a specialist that our own `B632`/`B1036`/`B1039` work has moved
  past.
