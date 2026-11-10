# PROPOSAL — the map: a generated visual scoreboard of everything a theory of everything owes

**From:** the advisor seat. **To:** cc and the owner. **Kind:** `propose:`. The owner agreed to it on 2026-11-10 and
ruled that main adds it to the dashboard already built (`OWNER_RULINGS_2026-11-10.md`, R7); cc confirms with the owner
and may `challenge:` the design.
**Origin:** the owner, 2026-11-10: "headline should count (0-18 (0-n*)) n* being the tier3 level identified 'outputs'.
should we also propose a visual scoreboard for them all, which also maps their interactions dependencies and
relations. the whole enriched sm+t3 structures, forces, mixings categories and all what applies … to know whats
computed/solved, whats still requires work etc, whats conditional so we map and later solve conditions".
**Builds on:** `PROPOSAL_THE_DERIVATION_GRAPH.md` (the graph is the data; this is its view).

## 1. The headline, as the owner set it

> **k of 18 (j of n\*)**

- **18** is tier 1: the Standard Model's dimensionless parameters (3 gauge couplings, 9 Yukawa couplings, 4 CKM
  parameters, θ̄, the Higgs self-coupling). The 19th of the usual count is the unit.
- **n\*** is the number of value rows on the whole map — all three tiers, plus every output the mathematics produces
  that has no measurement yet. It is computed from the graph. *(The seat's reading of "the tier3 level identified
  outputs"; the owner to correct.)*
- **k** and **j** count rows that are derived and confirmed in a sealed test. Nothing else counts.

**Two rules keep n\* honest.** A row enters the map by registration and is never removed: a row that fails is shown
refuted or withdrawn, and stays in n\*. And n\* is printed with its three parts (measured targets, registered
predictions, refuted), so the denominator cannot be shrunk or padded unseen.

## 2. What the map holds: three kinds of row

A theory of everything owes more than numbers, and a count of numbers alone hides real progress and real gaps.

| Kind | What it is | How it is settled | Counted in |
|---|---|---|---|
| **structure** | a discrete fact: a group, a representation, a count, a sign | derived or not; no tolerance | its own count, s of S, beside the headline |
| **value** | a continuous dimensionless number | derived, then confirmed in a sealed test | the headline |
| **relation** | an equation tying values together, derived when the values themselves are not | derived, then confirmed | its own count; each removes one free number |

Relations matter for the owner's "conditional so we map and later solve": a derived relation between two values is
progress the headline cannot show, and the map should.

## 3. The catalogue (the rows, by sector)

A first list for cc to check against `docs/SM_SPECIFICATION_LEDGER.md`, `docs/GUT_REQUIREMENTS_LEDGER.md`,
`docs/COSMOLOGY_LEDGER.md` and the 23 observables of `docs/total_inputs_scoreboard.json`. Tier in brackets.

| Sector | Structure rows | Value rows |
|---|---|---|
| **A. Spacetime and gravity** | four dimensions; one time; Lorentz symmetry; a spin-2 field with Einstein's dynamics | [3] the electroweak scale against the Planck mass; [3] the cosmological constant in Planck units |
| **B. Forces** | the gauge algebra su(3)⊕su(2)⊕u(1) and nothing more; its global form; confinement and asymptotic freedom follow from the values | [1] three gauge couplings at a stated scale and scheme; [1] θ̄ |
| **C. Matter** | one generation's representations and hypercharges; chirality; anomaly cancellation; exactly three generations; no further light matter | — |
| **D. The Higgs sector** | one doublet; the breaking pattern to electromagnetism | [1] the Higgs self-coupling; (the vacuum value is the unit) |
| **E. Quark flavour** | the mass hierarchy's pattern; the mixing matrix's near-diagonal form | [1] six Yukawa couplings; [1] three mixing angles and one phase |
| **F. Lepton flavour** | Dirac or Majorana neutrinos; the ordering of neutrino masses | [1] three charged-lepton Yukawa couplings; [2] three neutrino masses; [2] three mixing angles, one Dirac phase, up to two Majorana phases |
| **G. Cosmology** | what dark matter is; why matter outweighs antimatter | [3] the baryon asymmetry; [3] the dark-matter-to-baryon ratio; [3] the primordial spectrum's amplitude and tilt, if the programme claims them |

Quantities that follow from these by known physics (the proton's mass, atomic spectra) are not rows; they are checks
on the rows.

## 4. The status of a row (computed, as in the graph proposal)

| Status | Meaning |
|---|---|
| **derived, confirmed** | DERIVED ancestry and a sealed comparison passed — the only status that counts in k and j |
| **derived, awaiting test** | DERIVED ancestry; a prediction registered, no measurement yet |
| **conditional** | DERIVED except for a listed set of conditions (unearned identifications, chosen truncations, extra postulates) |
| **reading** | reached with a fitted or chosen continuous input |
| **not reached** | no output node |
| **refuted** | a sealed comparison failed |
| **door closed** | a negative with its scope and what would reopen it |
| **unverified** | an ancestor lacks a recomputing lock, a tracked script or a declared domain |

## 5. The views

1. **The board.** One tile per row, grouped by sector, coloured by status, each showing the number of open
   conditions. The headline and the three counts (structure, values, relations) sit above it.
2. **The condition map — the work queue.** The inverse of the board: every open condition, with the rows it blocks,
   ordered by how many rows it would release. One identification or one postulate often blocks many rows (the
   flat-bundle ansatz and identification I-26 are examples on today's scoreboard). This is the view that says what to
   solve next.
3. **The path of one row.** From the foundation to the value as a layered diagram, the weakest link marked, every
   node linked to its arc and its lock.
4. **Relations and shared ancestry.** Which rows stand on the same nodes, and which derived relations tie values
   together. This is where the interactions are read: two rows that share every ancestor are one result seen twice.
5. **The headline over time.** The counts at each landing, computed from the graph at that commit.

## 6. Rules for the map

1. **Generated only.** A new view of the Ledger Desk (`docs/workdesk/`), built from the graph at a named commit by
   the same rules as the desk: no data in the template, nothing typed, nothing loaded from outside.
2. **No partial credit in the picture.** There is no progress bar and no shade between "conditional" and "derived".
   Resemblance to observed physics is not a status. A conditional row shows its conditions, not a percentage.
3. **Zero must look like zero.** A board with many tiles and many colours can make an empty result look full. The
   headline is the largest thing on the page, and "derived, confirmed" is the only colour that reads as done.
4. **Negatives at equal weight.** Refuted rows and closed doors are tiles like any other, not a footnote.
5. **Every tile opens its evidence:** the arcs, the locks, the seal, the look count.
6. **Thread or weave on every tile.** A row whose support is a thread result says so (acceptance rows W-a, W-c).

## 7. Tests (planted changes, as for every generated view)

| # | Planted change | The map must |
|---|---|---|
| MAP1 | hand-edit a tile's status in the built page | be caught by the desk's build check |
| MAP2 | mark one ancestor of a "derived" row FITTED | show the row as a reading and lower k |
| MAP3 | register a row, then delete it from the graph | fail: rows are never removed, only marked |
| MAP4 | close one condition in the graph | release exactly the rows the condition map listed under it |
| MAP5 | add a relation with an unearned identification on its path | show it conditional and not reduce the free-number count |

## 8. What it would show today

By the record's own statuses: no value row and no relation row derived; frame A's six mass ratios as readings on 13
borrowed joints; the structure rows of sectors B and C conditional on the frame hypothesis and on unearned
identifications; several doors closed, each with what would reopen it. The condition map would be the page worth
reading first.
