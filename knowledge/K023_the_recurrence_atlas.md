# K023 — The Recurrence Atlas: recurrence as the fingerprint of one object, made usable

**Textbook layer (`knowledge/`): a self-contained explainer, firewalled, citing its provenance. Introduces no new
*result* — it names a re-runnable **instrument** (`scripts/atlas/`) and the reading behind it.** Nothing here promotes to
`CLAIMS.md`; the atlas is a *meta-tool about the structure of the work*, not a physics claim.

## 0. In one sentence

A *tiny* set of objects resolves the *majority* of the ~420 frontier probes — the trace-map words, the metallic tower,
the figure-eight, the two arithmetic ends, and the one conserved trace `κ`. The **Recurrence Atlas** mines that fact into
a queryable graph so we can (i) **re-orient fast**, (ii) **re-use** what has historically resolved an obstacle, and
(iii) tell **genuine unity** (a conserved quantity that *must* recur) apart from **the hammer** (our method, which recurs
by selection). It is the owner's observation — *"dead ends get solved by re-using the same object"* — turned into a tool.

## 1. Why recurrence ≈ unity — the conservation argument

Recurrence, by itself, is not evidence of anything: if you only own a hammer, everything recurs as a nail. The atlas is
built to **separate the forced recurrence from the selection effect**, along one honest axis — the motif's
*conserved-status*:

- **First integral (forced ⇒ genuine unity).** `κ = tr[a,b] = x²+y²+z²−xyz−2` is **conserved by the trace map for every
  `m`** (K001/K007; = the Goldman-symplectic Casimir, B293). A first integral *must* reappear on every fibre of the
  problem — its recurrence (in ~29% of probes) is **forced by a conservation law**, not chosen by us. This is the one
  place where "the same object keeps coming back" is a theorem, not a habit.
- **Structural invariant (recurs as an invariant of the transform).** The two arithmetic ends (`ℚ(√5)/E₈` and
  `ℚ(√−3)/E₆`), the Eisenstein `ω`, the Dickson `det=−1` parity, the `ℤ/3` deck — these recur because they are
  *invariants of the object's own maps* (K020/K021). Forced-ish, structural, bankable as **form**.
- **Tool (recurs by selection — the hammer).** The **trace map** itself appears in ~58% of probes. That is *because it is
  our method*. Its recurrence is a **selection effect and is NOT evidence of unity.** The atlas reports it — and quarantines
  it — on purpose.

So the honest headline the atlas prints is: *the recurrence that means something is the **conserved** recurrence (`κ`, the
two ends), and the atlas keeps it visibly separate from the tool-reuse.* That discipline — **verify-don't-trust, applied to
our own favourite objects** — is the point of the instrument, not an afterthought.

## 2. The seven uses (what it is *for*)

1. **Re-orient fast.** `query.context_card()` — the conserved quantities, the corpus status, the top motifs, the honest
   split, the meeting-point candidates, in one screen. For a returning session or a fresh seat.
2. **Obstacle → resolution oracle.** `query.resolutions_for(type)` — "stuck at obstacle *X* → which conserved motif has
   historically resolved *X*?" The *cycle*, made queryable (obstacle-types from `docs/atlas/FAILURE_ATLAS.md`).
3. **Motif → recurrence trace.** `query.motif_trace(m)` — every probe a motif touches, cross-domain appearances flagged.
4. **Dead-end / DORMANT revival.** `query.revive(B###)` — the owner's move: given a stalled lead, the conserved motifs
   that resolved *the same obstacle-type* elsewhere **but were not yet tried here**.
5. **Genuine-unity detector.** `query.meeting_points()` — ranked **candidates** for cross-domain re-surfacing (§3).
6. **Gap finder.** `query.gaps()` — obstacle-types with few banked resolutions (the open frontier); motif pairs that
   avoid each other (a structural gap).
7. **Self-consistency + discipline.** The recurrence graph *is* the "one object seen from N angles" argument, made
   auditable — and it guards against selling the hammer as unity.

## 3. The genuine-unity detector — and its honest limits

The detector scores each probe by **domain breadth** plus the repo's **documented unity-patterns** — co-occurrence
signatures seeded from the *known* cross-structure identifications:

| pattern | the documented meeting it encodes |
|---|---|
| `two_ends` | the two arithmetic ends identified as one object — K021/B332/B261 |
| `object=dynamics` | the carrier knot realized as the trace-map fixed locus / its conserved trace — B67/K007 |
| `physics_bridge` | a conserved structure carried across the topology/arithmetic → physics bridge — B121 |
| `quantum_meeting` | the WRT/AJ quantum invariant meeting the arithmetic ends — B261 |
| `symplectic_casimir` | `κ` realized as the Goldman symplectic Casimir — B293 |

**The honest caveat (binding).** These are **candidates for human judgement, never proof**:

- **Co-occurrence ≠ meeting.** A probe can name-check figure-eight *and* the trace map without *proving* they are the same
  object (B67 does; most do not). The detector reads *lexical* signatures; the *meeting* is semantic. Confirm by reading.
- **The corpus is saturated.** `object=dynamics` fires in ~41% of probes, `two_ends` in ~32%. Cross-domain co-occurrence
  is the **norm** here — which is *itself* the "one object" fingerprint, but it means the famous meetings (B67, B261) land
  in the **top tier**, not necessarily the top five, and the detector cannot single them out lexically. That is a feature
  reported honestly, not a bug hidden.
- **Breadth under-ranks depth.** A narrow-but-deep *identity* (e.g. the founding `g = −R·L⁻¹`, B332 — an arithmetic-only
  meeting) scores *low* on a breadth detector. The tool measures *breadth of meeting*; a deep two-line identity will be
  under-ranked. Know this when reading the ranking.

## 4. How it is built (re-runnable)

```
python scripts/atlas/atlas.py     # mine frontier/ -> scripts/atlas/atlas_data.json (the graph)
python scripts/atlas/render.py    # regenerate docs/RECURRENCE_ATLAS.md (the map — GENERATED, do not hand-edit)
python scripts/atlas/query.py card | motif <m> | obstacle <t> | revive <B###> | gaps | meet
```

- `atlas.py` — the **motif lexicon** (each motif: `kind`, `conserved`, `home-domain`, `patterns`, `gloss`) + the miner
  (parses every `frontier/B###/FINDINGS.md` for motif hits, `B/K/S/L###` edges, status, and a keyword-matched
  obstacle-type) + the analysis + the detector.
- `docs/RECURRENCE_ATLAS.md` — the **generated** map (stays current by regeneration).
- This note — the **stable** vision (hand-written; the map is derived).

The lexicon and the unity-patterns are the *judgement* in the tool; they are meant to be **edited and re-run** as the
corpus grows. Grounded in the repo's own vocabulary (K001/K007 `κ`; K020/K021 the two ends and the structural theorem;
`docs/atlas/FAILURE_ATLAS.md` the obstacle taxonomy; `docs/HINT_LEDGER.md` H2/H4 the recurrence-hints).

## 5. Firewall status

The atlas is a **meta-tool about the structure of the work**. It makes **no physics claim** and promotes **nothing to
`CLAIMS.md`**. The one thing it *asserts* is methodological: **conserved recurrence is meaningful, tool-reuse is not, and
the two must be kept visibly apart** — the same discipline (K020's firewall; verify-don't-trust) turned on our own most
beloved objects. Motif frequencies and meeting-point ranks are **navigation, not results**.

**Provenance.** `κ` first integral: K001/K007, B293. Two ends / structural theorem: K020, K021, B261, B332. Object =
trace-map locus: B67. Physics bridge: B121. Obstacle taxonomy: `docs/atlas/FAILURE_ATLAS.md`. Recurrence-hints: H2/H4
(`docs/HINT_LEDGER.md`). Instrument: `scripts/atlas/`. Reframe it serves: K022 (the symmetric centre).
