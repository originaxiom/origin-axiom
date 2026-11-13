# SM scope note — the closed-join block (B1351; B1508's row (a)) re-read against today's index

*The SM seat, 2026-11-13; main at b1bcc7f50, last message read M23. Not a card. The owner asked whether these old arcs
were approached properly, and whether to revisit them in the light of the record's progress and the literature note
(`relays/SM_LITERATURE_NOTE_1.md`). Nothing new was computed. § 4 and § 5 are this seat's derivations, from standard
duality and from the module construction; they are not reviewed. Nothing was compared with a measured value.*

## 1. Answer in short

- **The old arcs were sound in their own frame.** Nothing needs redoing.
- **Their reason has drifted.** Later citations carry it into a frame where it no longer applies, this seat's own
  SM-C8 card among them.
- **The conclusion survives for today's index.** It needs three hypotheses written in.
- **Looking at those hypotheses adds two things:**
  - **A new lead:** a non-orientable closing, which would tie the order to the hand.
  - **A sharpening:** on the one-cusped levels, a sector module's end can either be closed exactly or not be closed
    at all. So the order can live only on an end that stays open.

## 2. What the old arcs said, and how

**B1351** (2026-09-09; `frontier/B1351_the_index_on_a_three_manifold/FINDINGS.md`). Its frame is Pantev and Wijnholt's:
the net chiral count is a relative Euler characteristic.
- **(i) Closed Q.** χ(Q; L) = 0 for every local system, so that count vanishes.
- **(i), separately.** On the tower's closings, h¹(ψ) = h¹(ψ̄) for every character, by Poincaré duality with
  h⁰ = h³ = 0.
- **Checks.** The seat checked 9 321 characters. Main re-derived 179 with its own code (B1411).
- **The cusped half (ii)** was already scoped once (B1413: it fails for the disc conventions).

**B1508's row (a)** (2026-10-01). It is a scope reading, not a new proof:
- the block is "general: χ(Q; L) = 0 on every closed odd-dimensional manifold, in the frame";
- its reach is "gluing along every cusp, full fillings".

**Method.** Both are right on their objects and in their frame, which counts with an Euler characteristic.

## 3. What has changed since

- **The index is different now.** It is B1418's and B1438's I = n − n*, on non-split two-dimensional modules.
- **It is not an Euler characteristic.** On E6's committed output it equals h¹(M; V*) − h¹(M; V), on all 46 618
  modules (literature note, § 4).
- **χ = 0 does not decide it.** χ = 0 gives h⁰ − h¹ + h² − h³ = 0, not h¹(V) = h¹(V*).
- **The reason that carries over** is B1351's second one, duality.
- **So "vector-like, with χ(Q; L) = 0" gives the wrong reason for today's index.** That is B1508's row (a), as cited
  in SM-C8's first section; this seat wrote the card. The card's reason is corrected with this note.

## 4. The block restated, with its hypotheses

Let Q be a closed 3-manifold and V a module of π₁(Q). Assume:
- **(H1)** Q is orientable;
- **(H2)** h⁰(Q; V) = h⁰(Q; V*) = 0;
- **(H3)** V is a local system on all of Q, with no singular locus.

Then h¹(Q; V) = h¹(Q; V*).
- **Proof:** χ = 0, h³(V) = h⁰(V*) and h²(V) = h¹(V*).
- **Check:** post hoc, on E6's 46 618 fillings (`relays/sm_lit/duality_check.json`).

Each hypothesis is an escape when it fails. Where each stands on the record:

| hypothesis fails | what duality then gives | where it stands |
|---|---|---|
| (H1) non-orientable closing | V is paired with V* ⊗ w, w the orientation character; h¹(V) − h¹(V* ⊗ w) = h⁰(V) − h⁰(V* ⊗ w) | closed in B1351's G₂ frame (Q is calibrated, so oriented); otherwise **open and never examined** |
| (H2) a trivial character on Q | h¹(V) − h¹(V*) = h⁰(V) − h⁰(V*), which can be ±1 | the record's sector modules exclude trivial characters by construction; B1378 (B1508's row (c)) bars such non-split backgrounds as source-free vacua; open only with sources (R41) |
| (H3) a circle of cone or orbifold points | a good orientable orbifold keeps rational duality (invariants of a finite manifold cover), so still h¹(V) = h¹(V*) | **no escape** |
| (H3) a cusp closed by a cone point | the space is not a Witt space (its link T² has H¹(T²; V) ≠ 0); duality needs a Lagrangian choice L there, and pairs (V, L) with (V*, L^⊥) | **this is SM-C8's partner condition**; the order can enter only through the leak term (literature note, § 5) |

- **(H1) is the new lead.** On a non-orientable closing, the pairing exchanges V for V* ⊗ w. The order (V against V*)
  is then tied to the orientation character, that is, to the hand.
- **Where it could arise.** The record's seed m004 is amphicheiral and double-covers the non-orientable Gieseking
  manifold; the record's Pin⁺ qualifier (sm:B1382) shows such structures already enter it.
- **Not computed here.**

## 5. A consequence on the one-cusped levels

- **The cusp holonomy is unipotent.** By the module construction (B1438; `relays/sm_c6/run_e6.py`), α, β and ℓ are
  trivial on μ and λ, and the cocycle is normalised to u(λ) = 1 with c(μ) = s(ℓ). So every sector module restricts to
  the cusp as a non-split unipotent module.
- **The core's holonomy.** For a filling along γ = μ^b λ^(−a), the holonomy around the core is
  [[1, b·s(ℓ) − a], [0, 1]]:
  - it is trivial for the one slope s(ℓ) = a/b, E6's descent;
  - it has infinite order for every other slope.
- **So no finite cone or orbifold closing exists** for these modules. An end is either closed exactly, on one slope
  and vector-like by § 4, or it stays an end.
- **On these levels, the order can live only on an end that stays open.**
- **On the covers it can differ.** A character can be non-trivial on a cusp there, and finite closings exist. That
  is SM-C8's population, which adds one reason to run it there.

## 6. Recommendation

- **Do not redo B1351 or B1508.** Their computations stand, and they have been verified twice.
- **Restate the block with (H1)–(H3)** wherever it is cited as general, with duality as the reason. That means
  B1508's row (a), SM-C8's first section, and main's citations. It is for main's word.
- **Treat (H1) as a lead, not a result.** A first, cheap look would compute h¹(V) and h¹(V* ⊗ w) for the record's
  modules on m004's non-orientable quotient, and ask whether their difference follows the order or the hand. That
  needs a card.
- **Fold § 5 into SM-C8's run as a check.** On the covers, for every cusp, record whether a finite closing exists.
