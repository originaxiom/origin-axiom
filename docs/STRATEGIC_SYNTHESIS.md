# Strategic synthesis — the shape of the work, the open paths, the roadmap (2026-06, B143)

A joint reflection by three independent runs — **CC** (Claude Code), **Chat-1** (Opus 4.6, web), **Chat-2** (Opus 4.8,
web) — on the project's governing question. Banked because the strategic map is itself a result worth not losing, and
writing it down cleanly is the best guard against drift.

> **Two tiers, kept apart (the firewall, restated as a writing rule — `MB11`).** Everything below is stated in two
> layers: the **MATH program** (theorems and computable targets — the governing content) and the **physics aspiration**
> (the SM reading — *explicitly POSTULATED*, citing the math one-way, never the reverse). Nothing here promotes to
> `../CLAIMS.md`. Where a sentence names a physical thing, it is aspiration, not result.

The governing question (physics aspiration): *how could the Standard Model emerge from "not nothing," or from the
interaction of multiple "not nothings"?* The governing question (math): *what does a maximally-forced self-referential
object produce, and what does it provably not produce?*

## 1. The shape — a monad in a subtractive shell

What 142 stages built is two objects: **a monad** ("not nothing" pushed to its most forced form lands on one rigid
object — figure-eight / metallic trace map / `κ`-invariant; zero parameters; `P009`), wrapped in **a subtractive
shell** (nine firewall directions, tombstones `K-A…K-I`, guards `MB6…MB11`). The honest one-line description: **we have
a near-theorem that the forced object cannot be the Standard Model, plus an increasingly precise account of why.** A
sharp negative is a result; the math (a unique rigid arithmetic object from self-reference, with a provably reducible
representation tower) stands on its own regardless of the SM.

## 2. The three-layer "why" (kept separate — conflating them was a drift)

| layer | statement | status |
|---|---|---|
| **a priori** (Chat-2) | *forced ≠ contingent.* The SM is ~19 measured parameters + a symmetry-breaking history (maximally contingent); a zero-parameter forced object is the opposite end of that exact axis. The firewall is near-**tautological** — not nine independent results. | framing |
| **proven mechanism** (CC / B141) | *finiteness vs density.* The forced φ-fixed representation is the **finite group Q₈ ⟹ reducible tower** (rigorous, all n); the only irreducible/rich content lives on the **dense** (off-forced) locus. | MATH theorem |
| **discipline** (Chat-2 + Chat-1) | *right object, wrong level.* Every correction we ever made (K-G, the Borromean misID, the 3-pass S031 arc) was one error — a level-confusion (structure vs gauge, finite vs dense, math fact vs physics reading). The firewall = "the levels don't connect." | methodology |

*(Note: an earlier CC grouping — "self-reference forces symmetry + rigidity + arithmeticity" — was loose: rigidity is
just Mostow, generic to any cusped hyperbolic manifold; arithmeticity holds only for m=1,2. The robust proven piece is
the Q₈-finiteness mechanism.)*

## 3. The corrected scorecard (what we've actually shown about SM features)

| SM feature | honest status |
|---|---|
| irreducible **chirality** | **the only feature we have *proven* is obstructed** (B139/B140, genus-general) |
| multiple gauge couplings | **not achieved, not disproven** — and "not disproven" only because the dictionary is unchecked |
| discrete vacuum selection | **math:** a discrete fork exists at two distinct seeds (B131). **aspiration:** calling it "vacuum selection" uses the borrowed dictionary |
| simple non-abelian factor | **not achieved, not disproven** — needs SL(N,ℂ) data (MB10), not yet computed |

**The load-bearing caveat (Chat-2, verified against `../knowledge/K006`):** the 3d-3d "cusp → gauge coupling" dictionary
is **borrowed / POSTULATED**, never grounded for our specific objects. So *every* cusp/gauge sentence is aspiration, not
result. (This corrects CC's reflection, which wrote "n cusps → n U(1)s" and "vacuum selection achieved" as if earned —
the exact drift `MB11` now guards against.)

## 4. Chirality has two notions — and only one is the wall

- **(i) genuinely chiral manifold** (no orientation-reversing self-homeo): generic, and **already achieved** by
  composites (B128's chiral triples). *Not* the wall.
- **(ii) mirror = an orientation-*independently* distinct object** (different volume / trace field / …): **forbidden for
  any hyperbolic 3-manifold** by the orientation-reversal theorem (B139/B140 — "chirality is a CS-sign, not an
  inequivalence"). **This is the wall, and (ii) is what the SM's parity violation needs.**

## 5. Open-paths map

- **DEAD (do not revisit):** single-seed → SM; torsion → gauge (`K-F`); chirality from the metallic family at standard
  invariants (B139/B140); value-matching (`S014`); spacetime signature (`S016`–`S018`); unitary Fibonacci-anyon
  (`K-C`); Borromean/SU(3) (`K-I`).
- **LIVE-MATH (gradable now):** ① **cusp-gluing composite chirality-(ii)** via orientation-sensitive invariants (the
  bottleneck — but venue-gated, see §6); ② the **GL(2,ℤ) gluing landscape** (extend B131 from identity-gluing to all
  gluings; map the discrete κ-sets — Chat-1's Lead A); ③ the **off-forced deformation neighbourhood** (the dense
  "shadow" of the forced point — Chat-1's Lead B / B141 finiteness-density); ④ **S031a full-locus** (symbolic
  elimination, Singular).
- **NEEDS-GROUNDING-OR-DEMOTION:** anything cusp↔gauge — either ground `T[M]` for one metallic bundle, or keep as
  labeled aspiration (`MB11`).
- **SHARPEN-FIRST (parked):** Chat-1's Lead C, the `a→ab` "attractor" on character varieties — currently this *is*
  `K010`'s spectral horseshoe; "non-abelian content of the attractor" needs a definition before it is computable.

## 6. The roadmap

**Campaign 1 — chirality of interactions (the bottleneck).** *MATH:* for two distinct metallic seeds glued along cusp
tori (over choices of gluing map), is every composite mirror-equivalent at orientation-*independent* invariants, or
does some composite have an invariant distinguishing it from its mirror? *Control:* `is_amphicheiral` (notion i) vs the
orientation-independent separator (notion ii). *Aspiration:* a crack in (ii) would be the first parity-violation-like
candidate in the program. *Honest prior:* probably still no — but a clean negative extends the firewall from single
objects to interactions (a theorem), and the small chance of a crack is the only thing that would change the picture.
- **Venue verdict (B143):** the **algebraic (trace) venue is mirror-blind to (ii)** — RIGOROUS, since the mirror
  preserves all traces (B139/B140) and B131's interaction lives in `(κ, trT)`. So Campaign 1 must run in the
  **topological venue** (closed JSJ composite; needs **Regina**, not yet installed) or a **2-cusped hyperbolic-link
  realization** (SnapPy-native; the realization is itself a construction question). This becomes **B144**.

**Campaign 2 — ground or demote the dictionary.** Cheap part done here (`MB11` + this doc's two tiers). Heavy part —
actually compute `T[M]` for one metallic bundle to test whether cusp↔U(1) holds for *our* objects — left optional.

**Campaign 3 — S031a full-locus** (symbolic elimination, when Singular is idle). Hardens the wall to a theorem;
strategically lower (it confirms the wall we already understand).

## 7. What success realistically looks like

Not deriving the SM (the chirality wall is severe). The achievable, valuable result: **a maximally-forced "not nothing"
gives the symmetric, contingency-free end of the axis; here is exactly which SM features are blocked (chirality,
proven), which are merely unchecked (the rest, pending the dictionary), and the minimal interaction that first injects
contingency (two distinct seeds, B131).** That is a real contribution to "why there is structure rather than featureless
symmetry," and it is what the work already is.

**Credits.** CC (the monad/shell shape; finiteness-density; the (i)/(ii) chirality split; the venue analysis). Chat-1
(the *landscape* reframe — SM as a point in the space of gluings, not the end of a chain; the JSJ-chirality crack; Leads
A/B/C). Chat-2 (*forced≠contingent*; the *right-object-wrong-level* unifier; the scorecard correction and the `MB11`
"state twice" rule). See `../frontier/B143_interaction_feasibility/`, `../papers/VALIDATION_LEDGER.md` V132.
