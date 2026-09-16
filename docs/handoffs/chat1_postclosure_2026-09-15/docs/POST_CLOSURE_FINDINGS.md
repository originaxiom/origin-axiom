# POST-CLOSURE FINDINGS — everything since `CLOSURE_HANDOFF`, 2026-09-15
*(Corrections live in `ADDENDUM2_2026-09-15.md`; read that first.)*

## A. I-26: THE `d+M` DECISION TABLE  (`<chat1>/docs/I26_DECISION_TABLE.md`, `<chat1>/code/dplus_decision_table.py`)
`cc→fc 2026-09-06` reduced I-26 to: **"WHAT IS `∂⁺M`, AND WHAT IS ITS EULER
CHARACTERISTIC?"** Open on all four branches nine days later (82/104/76 files;
*"No identification row; I-26 remains the conditional"*). **`"APS boundary"` = 0 files on
main** — the defining convention has never been written down. That is the blocker.

Six conventions, every cell computed, **none promoted**. Net chirality `= −χ(∂⁺M)`:

| convention | m004 | m202 | s959 |
|---|---|---|---|
| A whole cusp torus | 0 | 0 | 0 |
| B annular subsurface | 0 | 0 | 0 |
| C cylindrical end / L² | 0 | 0 | 0 |
| D torus minus order-3 fixed discs | 0 | **6** | **6** |
| E as D, ONE distinguished cusp | 0 | **3** | **3** |
| F one disc per cusp | −1 | −2 | −2 |

**A, B, C are the standard readings and all give zero** — which is why five benches found
zero. **Row E is the only 3 and it is unmotivated.** R24's flux is `sign(q)·k` **per proper
arc**, symmetric across endpoints → selects **D**. **R30**: *"three positive light Dirac
**pairs** for three strong arcs, **not unpaired generations**"* — D's 6 and R30's 3 pairs
are the same six states with opposite chirality verdicts. **That disagreement IS the
D-vs-E question in physical form.** And `<chat1>/code/03` now closes E geometrically: the two
cusps are swapped by an isometry and have identical shape `e^{iπ/3}`.

## B. B1297 §5.1's PARENTHETICAL IS THE GENERAL OBSTRUCTION — already banked
> *"the index vanishes for every **UNITARY** local system: `V* ≅ V̄` and conjugation
> preserves ranks."*

**unitary ⇒ completely reducible ⇒ `V* ≅ V̄` ⇒ `I(V) = 0`.** No finiteness, no rationality,
no characteristic needed. **My `Z/3`-rationality argument was a special case of this, and
my Maschke argument was the wrong category.** Both superseded by one sentence on main
since 2026-09-08. A nonzero index requires a **non-unitary** local system — and
`U(t) = [[1,t],[0,1]]` is non-unitary and not completely reducible (`<chat1>/code/07`).

## C. FLATNESS KILLS IT INDEPENDENTLY — Chern–Weil
Chern classes are polynomials in `F`. A **flat** bundle has `F = 0`, so all rational Chern
classes vanish and `ch(V) = rk(V)` **exactly**. Atiyah–Singer on a spin 4-manifold then
gives `ind D = −rk(V)·σ/8`: **representation-blind.** 27 and 27bar have equal rank, so
equal index — **vector-like for any flat bundle on any spin 4-manifold, always.**
The SM's chirality lives in `∫ch₂(V)` (instanton number), quadratic in `F`.
**The programme's entire apparatus — character varieties, holonomy, trace fields, the 2T
door, twisted cohomology — is the theory of flat connections.**

## D. WHAT THE SM EQUATIONS REQUIRE vs WHAT EXISTS
| requirement | status |
|---|---|
| 4-manifold (Euclidean for the index) | MISSING |
| spin structure | **HAVE** (all orientable 3-mflds are spin; `Ω₃^Spin = 0`) |
| `G`-bundle, `G` compact | PARTIAL (flat local systems) |
| connection with **curvature** `F ≠ 0` | **MISSING** |
| spinor bundles `S^±` (needs `γ₅`, even dim) | MISSING |
| Dirac operator | **PARTIAL** — main has a **certified** one on m004, `λ₁ = 2.974550580` |
| `ind D = ∫ Âch(V)` | MISSING (bulk integral never computed) |
| anomaly cancellation | **HAVE** (verified on 3×27 trinification) |
| Yukawas → masses | out of scope (moduli, banked) |

## E. CORPUS ABSENCES (word-boundary, `origin/main`, `*.md`)
**0 files:** Chern class · Chern–Weil · Chern character · Pontryagin · Atiyah–Singer ·
second Chern · **APS boundary** · positive part · nonsemisimple.
**Present:** curvature 63 · flat connection 60 · Dirac operator 18 · instanton 13 ·
index theorem 11 · signature 388 · quadratic form 46 · Markov 159.
**The characteristic-class machinery is absent; the 3-manifold vocabulary is rich.**
And **B1290 already frames the index better than I did**: `net chirality = χ(M, ∂⁺M)`,
with torus/annulus → 0 and **disc → −1, pair of pants → +1**.

## F. THE BIANCHI PICTURE, and what it is NOT
Humbert: `vol(H³/PSL(2,O₃)) = 0.169156934`. **m004 = index 12, m202 = 24, s959 = 36,
v3551 = 42, s596 = 30.** **Index 12 contains exactly two manifolds: m003 and m004** — the
twins are that whole level.
**But:** the levels are *not* a ladder (index 24 has **7** members, 36 has **12**), the
indices are not multiples of 12 (28, 30, 35 occur), and **there are no inclusions among
m004/m202/s959** — verified by exhaustive low-degree cover enumeration (`<chat1>/code/04`).
**Torsion precision:** a hyperbolic manifold group is torsion-free, so **no** manifold here
contains 3-torsion — m202 and s959 included. The order-3 is in the **normaliser**
(`Sym = D₆`, outer). *"The class has the 3-torsion"* means **the orbifolds above them do.*

## G. THE FOUR-PROPERTY TABLE — nothing has all four
| | forced | chiral | 2T door | order-3 |
|---|---|---|---|---|
| m004 | yes | **no** | 48 | **0** |
| **Weeks** `m003(-3,1)` | yes | yes | **0** | 2 |
| m129 / m125 | yes | yes | 192 | **0** |
| m202 / s959 | **no** | yes | 96 / 576 | 2 |

Weeks is the **unique min-volume closed orientable hyperbolic 3-manifold** (GMM 2009),
**forced and CHIRAL** — which killed my *"forced ⇒ mirror-even"* law. It has
`H₁ = (Z/5)²` — the prime 5 twice — and **still zero** surjections onto `2I = SL(2,F₅)`:
**having the prime in homology does not open the door.** Its trace field is cubic.

## H. HOMOLOGY LADDER (combinatorial; valid on exceptional fillings)
`m004(p,1)`, `p = 0..6` → `Z, 0, Z/2, Z/3, Z/4, Z/5, Z/6`. **`p=0` is the only infinite
one.** The first genuinely **hyperbolic** filling is **`p = 5`** (vol 0.9813688);
`p = 0..4` are all exceptional, so neither hyperbolic tools nor `cs` apply to them.
