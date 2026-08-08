# CC3 → CC — UNEXPLORED LEADS: the sweep outside `OPEN_LEADS.md`

cc3 audit seat, 2026-08-09. Gate 5-Q. Nothing promotes. **No ledger, register
or `kill_graph.json` was edited — this proposes.**

The owner asked whether there are leads not explored, on the ledger or
elsewhere. Answer: **yes, and the largest reservoir is not a ledger at all.**
It is the kill-graph's revival structure — 132 killed claims that each carry an
explicit, pre-analysed route back, with a numeric score saying how promising
that route is — and **no register indexes it.** You cannot ask any ledger
"what are the most revivable kills"; that query exists only inside a JSON file.

Reported below with the nulls included, because three of the five things I
checked came back empty and saying so is the point.

---

## 1. WHAT I CHECKED, INCLUDING THE NULLS

| channel | result |
|---|---|
| `docs/LEAD_REGISTER.md` — a **second register** | **REAL, and outside your ask.** 185 lines, names 77 arcs; a re-score of the whole non-banked corpus (133 probes) against *today's* toolset, updated at Review 37. Your triage covered `OPEN_LEADS` only. |
| in-arc `[NEW OPEN Nx]` registrations | **NULL — channel is clean.** 2 arcs, 8 markers, **all registered.** |
| arcs with unrun-work markers but no register mention | **NULL — base rate.** 58 of 172 such arcs (34%) are unregistered, against a corpus baseline of **36%** (342 of 941 arcs are named in no register). Being unregistered does not correlate with having unrun work. No signal; do not spend on it. |
| `docs/TOMBSTONES.md`, `docs/FAILURE_ATLAS.md` | **MISSING from `origin/main`.** `LEAD_REGISTER.md` names five registers it swept; two of them do not exist at those paths. Either they were renamed and the citation rotted, or that sweep's coverage claim is overstated. Worth one minute of yours. |
| **`kill_graph.json` revival structure** | **THE FINDING — see §2.** |

---

## 2. THE RESERVOIR

`frontier/B738_pathfinder_compiler/kill_graph.json`, 741 entries, carries three
fields no register surfaces:

- **`hatch`** — a named escape route for a killed claim. **231 entries have one**;
  **132** use one of seven short route names (`deepen-past-plateau`,
  `native-continuous-channel`, `route-through-atom`, `nonlinear-transport`,
  `enumerate-landing-sites`, `infinite-tower`, `recompute-cited`); the rest
  carry a full prose hatch.
- **`revival_score`** — 0–6, present on **220** entries. Distribution:
  `{0:9, 1:66, 2:67, 3:49, 4:19, 5:9, 6:1}`. **28 score ≥ 4.**
- **`priority`** — and **167 entries are `UNTRIAGED`**, with **no hatch and no
  revival score at all**. Nearly a quarter of the graph was never assessed for
  revivability in the first place.

Of the 132 short-hatch entries, **57 are named in no register**; of the 27
scoring ≥ 4, **10 are named in no register**. Note honestly: at a 36% corpus
baseline those rates (43%, 37%) are **unremarkable**. The finding is not that
these are anomalously lost — it is that a whole indexed lead structure exists
that no ledger can be queried against, so its top items surface only by
accident.

---

## 3. THE TEN UNREGISTERED HIGH-REVIVAL KILLS

Ranked by the graph's own score. **B500 was verified end-to-end on this seat;
the other nine are the graph's annotations, read but not independently
re-derived — labelled as such.**

### B500 — score **6**, the highest in the graph — `deepen-past-plateau` — **VERIFIED**

A kill that its own arc says is **not a kill**. Checked in both source files:

- `frontier/B500_child_hunt/FINDINGS.md`: *"## Depth 5 — the KILL is
  PROVISIONAL"* … *"**35 words remain UNCHECKED** (26 timeouts + 9
  never-reached)"* … *"strongly suggestive (0/115) but **not the complete
  depth-5 exhaustion** the prereg's KILL requires."*
- `frontier/B525_are_you_sure/FINDINGS.md`: *"**CHILD-NOTSHORT → KILL
  downgraded to PROVISIONAL.** Only **115 of 150** words were actually analyzed
  … **35 unchecked**, not 9 … **reopen = re-run the 35** (𝔽_p Gröbner or longer
  timeout)."*
- kill-graph note: *"The atlas marks this dead, but the FINDINGS text itself
  downgrades the depth-5 kill to PROVISIONAL and issues an explicit REOPEN
  action"*, and *"the kill must NOT be cited as complete alongside Gate C/B519."*

So: the question *"is the child (x⁴−x−1, d_K = −283) a short word?"* is **open at
23% unchecked**, the reopen action is written down, the arithmetic is specified
(eliminants of degree ~3000–9280 — 𝔽_p Gröbner or a targeted d_K = −283 factor
test), and it appears in **no register**. This is the single most concrete
unexplored lead the sweep found.

### The other nine (graph annotation, unverified here)

| arc | score | hatch | what is still live |
|---|---|---|---|
| **B111** | 5 | nonlinear-transport | the s_n↔c bridge; graph calls the c-into-θ carrying question *"the live crux of the two-chiralities program"* and says the hatch *"is actively being walked at a deeper level"* |
| **B477** | 5 | deepen-past-plateau | universal sterility law refuted by s776's count, but *"the L6a4 pairing hint survives unexplained"*; the fresh read used a **truncated** cocycle window (7 of ~30 sign entries) |
| **B712** | 5 | native-continuous-channel | the real-anchor probe consulted **only** the A-polynomial curve as "the object's one continuous modulus"; the graph's own pressure: the **emittance** face supplies canonical choice-free continuous *real* data that was never consulted |
| **B374** | 4 | deepen-past-plateau | sector exists on prime-power towers, dies at mixed levels; *"the phase-map riddle … registered and uncracked"* |
| **B394** | 4 | infinite-tower | the kill's reward is live structure: the **unified singles law**, Σ_support = 1 frozen across all levels, c walking down the cyclotomic tower |
| **B706** | 4 | native-continuous-channel | the SM-flavour kill; rung 2 died on a **kind** mismatch (discrete bits vs ~19–26 continuous reals) — directly adjacent to Cell 9 |
| **W10-B660/B666** | 4 | native-continuous-channel | composite id; not a plain arc — needs a name before it can be registered |
| **W11-B706** | 4 | native-continuous-channel | composite id, as above |
| **P21 — the framework search** | 4 | enumerate-landing-sites | not an arc id at all; a *campaign-level* entry sitting in an arc-keyed graph |

Those last three are worth a second look for a different reason: **the graph's
`id` field is not uniformly an arc id.** Anything keyed on it — including my own
sweep and any future attachment pass — silently mis-handles them.

---

## 4. WHAT I RECOMMEND

1. **Register B500's reopen.** It is verified, concrete, costed, and its own
   arc forbids citing the kill as complete. Cheapest real lead in the repo.
2. **Index `revival_score` somewhere queryable.** One generated table —
   `docs/REVIVABLE.md`, built by script from `kill_graph.json`, sorted by score
   — turns 220 scored hatches from a JSON field into a frontier. This is the
   structural fix; the ten arcs above are just what it surfaces first.
3. **Triage the 167 `UNTRIAGED`.** A quarter of the kill graph has no hatch and
   no score. Until they do, "revivable kills" is a statement about the 574 that
   were assessed, not about the graph.
4. **Resolve `TOMBSTONES.md` / `FAILURE_ATLAS.md`** — restore, redirect, or
   correct `LEAD_REGISTER.md`'s coverage claim.
5. **Normalise the `id` field** (or document that it is mixed), before anything
   else keys on it.
6. **Do not spend on the "unregistered arcs" angle.** I checked; it is the base
   rate. Recorded so nobody re-runs it.

---

## 5. RELATION TO TODAY'S OTHER RELAYS

This is the same shape a fourth time, and it is getting hard to call a
coincidence. The lead ledger indexes *leads*. The forcing graph indexes *arcs*.
The face taxonomy indexes *kills*. Each is a well-built instrument, and the
thing that falls between them — a killed claim that carries its own route back —
belongs to none of them, so nothing surfaces it. **Our instruments hold
objects, and relations fall through.** A revival hatch is a relation between a
dead claim and a live method.

— cc3
