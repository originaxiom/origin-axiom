# TERMINOLOGY POLICY — binding on the paper's drafting; source for Appendix C

**Owner-approved 2026-08-14.** Governs every section of the genesis-first paper.
**Enforced by `check_terminology.py`.** Nothing here changes the corpus — the internal
names remain the working vocabulary; **the paper uses standard terminology and ships the
translation.**

---

## The principle

> ## **A term earns its place in the paper by naming a mathematical object. If a standard name exists, the paper uses the standard name.**

**And the argument is the paper's own scope, not taste.** `TERMINOLOGY.md` defines the
worst offender against itself:

> *"**being** = the holonomy/geometry side… **hearing** = the monodromy side. **Named for
> the observer-coupling reading**; **the mathematics is the bifocal two-ended structure.**"*

**The paper disclaims the observer-coupling reading** (Gate 5; no physics identification in
the body). ## **Keeping names coined for a reading the paper disclaims would contradict its own scope statement.** The rename is required by consistency, not by fashion.

---

## TIER 1 — RENAME (internal → paper)

| internal | ## **paper** | note |
|---|---|---|
| **being face** | ## **the Kleinian trace-field side** (ℚ(√−3); prime 3; 2T; E₆) | also resolves collision **T7** |
| **hearing face** | ## **the fiber-field side** (ℚ(√5); prime 5; 2I; E₈) | also resolves collision **T7** |
| the two hands | **the bifocal pair** / the two arithmetic ends | |
| deaf | ## **non-CM** | the corpus already glosses it exactly so |
| the voice | **the continuous-spectrum channel** | per B737/B739 |
| the chord | **the θ-equivariant fixed line of the trace map** | |
| the seam | **the interface locus** | |
| the child | **the orientation double cover's quotient** | C5's own gloss |
| the observer's place | **the distinguished basepoint** | |
| H-EAR · the Listening Protocol · the audibility law | ## **do not appear** | interpretive; no paper content depends on them |
| the incompleteness / the closing | **the residual freedom / its fixing** | |
| the Born ledger | ## **do not appear** | |

## TIER 2 — KEEP, GLOSSED AT FIRST USE (physics word ⟶ math object, same sentence)

**The model is the corpus's own best gloss:** ***"measurement = fiber functor."*** Every
Tier-2 term must be pinned like that, in its first sentence.

| term | required gloss |
|---|---|
| measurement | **= the fiber functor** (equivalently: successive centralizers of the charge torus) |
| native gauge | **= complex Chern–Simons** |
| multiplicity | **= the covering degree** |
| flavor atoms · generation · matter · vacuum · colour · charge | **names of `𝔢₆`/27 sub-objects**; each pinned to its subspace at first use, per `SKELETON.md` App. C |

## TIER 3 — THE COLLISIONS (one referent per symbol; bare use FORBIDDEN)

**These are correctness, not style. A referee who finds one symbol meaning two things has found an inconsistency.**

| symbol | referents | ## paper's required forms |
|---|---|---|
| **conductor** | cusp order's conductor (golden 4) · word's shadow modulus `m²+4` (golden 5) | **`cusp conductor`** · **`shadow modulus m²+4`** |
| ## **level** | congruence level of the Bianchi group · **Chern–Simons level `k`** | ## **`congruence level`** · **`Chern–Simons level k`** — ⚠ **cc3 wrote a bare "level 15" into a banked relay; it is the collision that bit hardest** |
| **θ-even** | the `F₄` exponent set {1,5,7,11} · B1011 C6's mirror **value** set | **`θ-even exponents`** · **`θ-even value set`** |
| **σ** | gravitational `σ = ℓ/4G` · the stage pin in `c = 6σ` · B945's R↔L swap | **`σ_grav`** · **`σ_stage`** · **`the R↔L swap`** |
| ## **π/6** | `arg κ = ∓π/6` — a **conjugation-invariant trace** · `arg Y[134] = π/6` — **proved pipeline GAUGE** | ## **opposite type.** Always written with its object: **`arg κ`** vs **`arg Y[134]`** |
| **c** | `c((E₆)₁) = 6` (Sugawara) · `c_BH = 6σ` (Brown–Henneaux) · the cusp-torus theory's `c` · B559's `c = 1` | **subscript all four**; bare `c` forbidden |
| **trace field** | fiber/eigenvalue field `ℚ(√(m²+4))` · the **Kleinian** trace field | **`fiber field`** · **`Kleinian trace field`** |
| **P** | the conjugating element (A7's bit) · the substrate exchange-symmetry operation (B16) | **`P_conj`** · **`the exchange-symmetry operation`** |

**Also**: bare arc IDs in `B1025–B1044` name two arcs each — **the paper cites arcs by ID *and* title**, never by bare number.

---

## Why this ordering

1. ## **Collisions first — they cause REFUTATION.** Poetry gets a paper dismissed; an inconsistent symbol gets it killed. cc3 hit two of these in one day (the fork-label collision, the four `c`s) and one nearly became a false finding.
2. **Tier 1 second — it causes DISMISSAL.** A referee meeting *"the being face ℚ(√−3)"* on page 8 stops reading, and the content lost by renaming is zero.
3. **Tier 2 last — the skeleton's plan already works** for these; they only need discipline.

## Bonus: the rename repairs a real sentence

*"The being(3) and hearing(5) faces interfere at congruence level 15"* is opaque.
## **"The Kleinian trace-field and fiber-field sides interfere at congruence level 15"** is a legible mathematical claim a referee can engage with — **and it is the same statement.**

## Declared

- **The Tier-1 targets are cc3's proposals**; several (`the chord`, `the seam`, `the child`,
  `the observer's place`) are **cc3's readings of their internal definitions and should be
  checked against their arcs before drafting.**
- **`TERMINOLOGY.md` has 70 entries; this policy covers the ~30 that reach the paper.**
  The remainder are corpus-internal and out of scope.
- **The collision list is the corpus's own** — every row is a hazard the corpus registered
  itself. **cc3 added no collisions; cc3 only transcribed and assigned paper forms.**
