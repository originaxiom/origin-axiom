# B971 — L132 (amended): the NON-VACUITY prerequisite CANNOT be met. L132 CLOSED as VACUOUS.

**Date:** 2026-08-08 · **Lane:** MATHEMATICS. Gate 5 untouched. Nothing to `CLAIMS.md`.
**Task:** establish whether L132's non-vacuity prerequisite (B951's amendment) can be met at
all, before any anomaly cell is allowed to run.

---

## THE VERDICT

> **VACUOUS — and the vacuity is now a computed uniqueness, not an expectation.**
>
> Of the **2047** non-empty sub-multiplet sets of the **27** under the object's own landing
> site, **exactly one** has a fully anomaly-free abelian sector — and it is the **complete
> 27**. Every decomposition of the 27 the record contains is *exhaustive*: the object's
> operations act **on** the 27, they never delete from it. The one incomplete spectrum in the
> corpus (B864's re-anchored **16**) is an **imported truncation that B864 itself declares
> underived**.

**And a second finding that must be banked with the first: L132's headline question has
already been run.** `B864` (2026-08-03) computed the anomaly ledger over the E₆ chain and
banked *"hypercharge is the unique gaugeable U(1) in the chain's abelian sector"*. B951's
literature panel did not surface it — a **prior-art miss inside the programme's own corpus**.
L132 as posed would have rediscovered B864 five days later.

---

## 1. (a) HOW THE RECORD SPECIFIES THE SPECTRUM — it is specified, and it is COMPLETE

The record never states "the spectrum is complete 27s" in those words. It does something
stronger and checkable: **every decomposition of the 27 anywhere in the corpus sums back to
27.** Four independent ones, from four different instruments:

| where | decomposition | sum | status here |
|---|---|---|---|
| the **holonomy** (ρ = principal ∘ ρ_geo) — B575/B632 | 27 = V(16) ⊕ V(8) ⊕ V(0), dims **17 + 9 + 1** | **27** | **re-derived in-sandbox** from the Cartan matrix alone (`holonomy_probe.py`) |
| the **joint charge operators** ρ(x₈), ρ(x₁₆) — B886 | two Galois orbits, mult 1 and mult 8: **3·1 + 3·8** | **27** | read from B886 (exact over ℚ there) |
| the **cascade's Levi** A₂+A₁ — B892 | 11 Levi irreps: 6+3+3+3+3+2+2+2+1+1+1 | **27** | **computed here** as W_S-orbits (`vacuity_probe.py`) |
| **G₂₀** — B897 | block table tiles **9 + 9 + 9** | **27** | read from B897 |

The Levi decomposition computed here is, state for state, **16 + 10 + 1** in SM shape —
(3,2) + 4×(3,1) + 3×(1,2) + 3×(1,1) — which is exactly the content L134 calls "the twelve
exotics". **The exotics are still there.** Nothing in the record removes them.

**A targeted sweep for a truncation found exactly one**, and it is not the object's:

> **B863 §Carried-forward / B864 §1:** *"over the full **27** nothing is anomalous, so anomaly
> alone does not force keeping only the chiral core."*

The truncation ("re-anchoring") is a rule of the **cascade** (B860/B861), applied to the 27;
B864 explicitly declines to derive it. So the record contains an incomplete spectrum **as an
input**, never as an object-supplied fact.

**One further reading checked and closed.** In the cohomological ("heterotic-style") reading
the matter would be `H¹(M; 27_ρ) = 3` rather than the module. That reading does not rescue
non-vacuity, for two computed reasons:

- B632's own **binding correction**: the three classes are *"three inequivalent local-system
  modes… three copies of one representation is exactly what this is **NOT**"*. A Betti number
  is not a list of states.
- **Computed here:** the centralizer of the principal sl(2) in e₆ is **0-dimensional** (the
  adjoint contains no V(0); exponents derived as 1,4,5,7,8,11). So the commutant of the
  object's holonomy carries **no continuous gauge group at all** — there are no gauge-anomaly
  conditions to write in that reading, vacuously or otherwise.

## 2. (b) THE CHECK CANNOT FAIL — computed, with a live control

All of the following are exact, symbolic, and computed in-sandbox from the E₆ Cartan matrix.
Nothing is cited.

**The one fact everything reduces to.** For a *generic* Cartan element H = Σᵢ hᵢ αᵢ^∨:

> **Σ_{λ ∈ 27} λ(H) ≡ 0** and **Σ_{λ ∈ 27} λ(H)³ ≡ 0**, identically in all six hᵢ.

Every U(1)³, [SU(3)]²U(1), [SU(2)]²U(1) and U(1)-gravitational condition is a **coefficient**
of these two polynomials, so this single identity carries all of them at once. (This is E₆'s
vanishing symmetric third-order Casimir — **derived here, not cited to Okubo.**) The same
holds for the **27̄**, whose weight set is verified *different* from the 27's — the 27 is
complex, computed, not assumed.

**On the object's own landing site** (A₂+A₁ Levi, node set {1,3,6}; dim 14, centre 3 — all
re-derived), with the abelian direction left **generic across the entire 3-dimensional
centre** (t₁,t₂,t₃ free, so all three u(1)s simultaneously):

| condition | value on the complete 27 |
|---|---|
| U(1)³ | **0** |
| U(1)-gravitational | **0** |
| [SU(3)]² U(1) | **0** |
| [SU(2)]² U(1) | **0** |
| [SU(3)]³ | **0** |
| Witten SU(2) parity | **6 doublets — even** |

*(The doublet count reproduces B951's "6 doublets, even" independently.)*

**MB12, both halves, discharged:**

- **Can the criterion pass?** Yes — trivially, above.
- **Can the criterion fail?** **Yes — the instrument is real.** Controls: su(5)'s **10** and
  su(3)'s **3** both give **nonzero** cubics under the identical code path. And on the 27
  itself, **dropping any one of the 11 Levi irreps makes U(1)³ and the gravitational condition
  nonzero in all 11 cases**; dropping a single weight also does.

> **So the vacuity is a property of the INPUT, not a defect of the test.** That distinction is
> what MB12 asks for, and it now has a computation behind it.

**The uniqueness of the vacuity — the sharpest single number in this cell.** Enumerating all
**2047** non-empty subsets of the 11 Levi irreps and solving exactly for the anomaly-free
abelian directions:

| anomaly-free abelian solution space | # of sub-multiplet sets |
|---|---|
| **3-dimensional (every direction works ⇒ VACUOUS)** | **1 — and it is the complete 27** |
| 2-dimensional | 48 |
| 1-dimensional (the check *selects* a u(1)) | 156 |

**Vacuity holds on exactly one spectrum out of 2047, and it is precisely the one the object
supplies.**

## 3. (c) WHAT NON-VACUITY WOULD REQUIRE — four things; the record supplies one

| # | requirement | supplied? |
|---|---|---|
| 1 | an unbroken gauge group with a non-vanishing cubic | **partly** — the Levi supplies it in the cascade reading; the **holonomy reading supplies none** (0-dim commutant, computed) |
| 2 | a list of **states** — not a module, not a Betti number | **NO.** The record has the 27 (a module) and h¹ = 3 (a multiplicity, explicitly corrected away from "three copies") |
| 3 | a **handedness** assignment per state | **NO.** Computed: a vector-like subset has vanishing cubic *regardless of completeness*. Without handedness the functional is undefined; with a vector-like one it is identically zero. Banked position: chirality is not self-supplied |
| 4 | **incompleteness** — some state deleted | **NO**, and this is theorem-grade already: knot groups have cyclic abelianization, so π₁(m004) cannot surject onto ℤ₃×ℤ₃ or the Heisenberg group (B955 §3); abelian holonomy only (B955 §1); finite images A₄/D₅/S₅ are toral (B959). **No orbifold projection, no quotient, no boundary-condition truncation exists here.** |

> **The object's operations are centralizers, holonomies and gradings. They *act on* the 27
> and *decompose* it. Nothing in the kit *deletes* from it — which is why all four
> decompositions in §1 sum to 27.**

This is the same single cause as the SM verdict, seen on a second face. It is **not** the
claim that incompleteness requires rank reduction — it does not (a rank-preserving Wilson line
on an orbifold splits multiplets happily). It is the weaker and correct claim that
incompleteness requires a **deletion operation**, and the object has none.

**Pre-empting the obvious revival.** Suppose a truncation were imported anyway. **Anomaly
cancellation still would not select the Standard Model.** Of the 2047 sets, **156** admit a
*unique* anomaly-free u(1) — spread over 5 to 22 states, including **18** sixteen-state sets
and **15** fifteen-state sets, one of which is exactly SM-generation-shaped
((3,2)+2×(3,1)+(1,2)+(1,1) = 15). The counts run in multiples of 3, suggesting a residual ℤ/3
this cell did **not** compute the equivalence classes of; even quotienting by it the 16-state
count is **6, not 1**. **Choosing the truncation is the entire content, and the object
supplies no truncation.**

## 4. (d) LITERATURE — where anomalies DO constrain an incomplete E₆ multiplet

**Honest limit, stated first: no live search was reachable from this cell** (the session's
web-search budget was exhausted before it began). What follows is (i) in-repo prior art from a
sweep that *did* reach INSPIRE, and (ii) recalled settings, flagged as such. **The null is not
certified.**

**(i) In-repo, from B951's INSPIRE-reached sweep — carried, not re-verified here:**

> anomalies become nontrivial *"only when the spectrum is **NOT** complete 27s — incomplete
> multiplets, projected-out exotics, string constructions. Anomalous U(1)′ in string
> constructions handled by **Green–Schwarz**"* (Langacker §III.6.3).

So the answer to (d) is **yes, such settings exist** — and they are exactly the
projection-bearing constructions the object lacks.

**(ii) Recalled settings — RECALLED, UNVERIFIED IN THIS CELL, listed as pointers for a future
verified sweep, not as support for any claim:**

- **Heterotic Wilson-line / free-quotient compactifications** — split multiplets are generic;
  an anomalous U(1) typically survives and is cancelled by Green–Schwarz (Dine–Seiberg–Witten).
- **Orbifold GUTs** — brane-localized fields are incomplete multiplets and *localized* anomaly
  cancellation is a genuine constraint (Arkani-Hamed–Cohen–Georgi; Scrucca–Serone–Silvestrini–
  Zwirner; Asaka–Buchmüller–Covi).
- **F-theory GUTs with hypercharge flux** — flux breaking produces incomplete multiplets.
- **E₆-inspired phenomenology (E₆SSM and relatives)** — complete **27**s are retained in the
  low-energy spectrum *precisely because* anomaly cancellation would otherwise fail. **That is
  this cell's result read backwards**, and it is the sharpest literature statement available:
  in the one place the constraint bites, its role is to *force* completeness.

## 5. WHAT THIS CELL DOES NOT ESTABLISH

- **It does not refute anything.** B864's ledger stands exactly as banked; this cell reproduced
  its arithmetic (ψ over the full 27: 16−20+4 = 0 and 16−80+64 = 0; over the 16 alone: 16 and
  16; χ over the full 16: 0 and 0; over 10+5̄: 5 and 125 — **all reproduced**).
- **It does not certify a literature null** (§4).
- **The 2047-subset enumeration is scoped**: it treats the 11 Levi irreps as atoms (correct for
  a gauge-invariant spectrum), assumes multiplicity one, and takes the A₂+A₁ Levi as
  colour+isospin — which is itself B892's identification, not an independent fact.
- **It says nothing about values, generations, the real form, or spacetime.**

## 6. THE RECOMMENDATION

1. **CLOSE L132 as VACUOUS.** The non-vacuity prerequisite fails at three of four requirements,
   and the one requirement that *is* met is met only in a reading whose commutant is empty.
2. **Record B864 as L132's true prior art** — inside the corpus, five days earlier. Any future
   anomaly cell must cite it or it is a rediscovery.
3. **Scope-note B864's headline** (not a retraction): its uniqueness result is uniqueness of
   the anomaly-free abelian direction **over an imported chiral truncation**. This cell's map
   shows 156 different truncations of the 27 each have such a unique direction, so the
   selective power lives in the truncation, not in the anomaly conditions.

---

**Reproduce:** `python vacuity_probe.py`, `python holonomy_probe.py`, `python nonvacuity_map.py`
(sympy, exact throughout; outputs `*_out.json` alongside).
