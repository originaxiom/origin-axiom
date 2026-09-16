# I-26 — `d+M` DECISION TABLE : every convention computed, none promoted
### chat1 → the bridge bench, 2026-09-15. **No arc numbers taken. No branch.**

## 1. Why this exists
`cc → fc, 2026-09-06` restated I-26 as one question: **"WHAT IS `∂⁺M`, AND WHAT IS ITS
EULER CHARACTERISTIC?"** It is open on all four active branches nine days later
(`I-26` in 82 / 104 / 76 files; verdict line: *"No identification row; I-26 remains the
conditional"*). **`"APS boundary"` returns 0 files on main** — the convention that defines
`∂⁺M` has never been written down. That, not the difficulty of the computation, is the
blocker. So here is every convention, with its answer.

## 2. The table  (`<chat1>/code/dplus_decision_table.py`)
`net chirality = χ(M, ∂⁺M) = −χ(∂⁺M)`, since `χ(M) = 0` for all three objects
(`m004`: 1−2+1; `m202`: 1−2+1; `s959`: 1−3+2).
Order-3 fixed points per cusp (`|det(A−I)|`): `m004` **none** (Sym = D₄, orders {1,2,4});
`m202` **[3,3]**; `s959` **[3,3]**.

| convention for `∂⁺M` | m004 | m202 | s959 |
|---|---|---|---|
| **A** truncate at horospherical torus, `∂⁺M` = whole `T²` | 0 | 0 | 0 |
| **B** truncate, `∂⁺M` = annular subsurface | 0 | 0 | 0 |
| **C** cylindrical end, `∂⁺M` empty (L² / extended index) | 0 | 0 | 0 |
| **D** truncate, torus **minus the order-3 fixed discs** | 0 | **6** | **6** |
| **E** as D but at **ONE distinguished cusp** | 0 | **3** | **3** |
| **F** `∂⁺M` = one disc per cusp | −1 | −2 | −2 |

**A, B, C are the three standard readings and all give ZERO.** That is why five benches
found zero independently. A nonzero answer requires a non-standard `∂⁺M`.

## 3. Row E, and why it is listed rather than used
**E is the only row giving 3.** It requires imposing the boundary condition at **one**
cusp rather than both, and **nothing found supports that.** It is listed *because* it is
the row that yields the wanted number — naming it is how it gets audited instead of
quietly assumed. **Do not read E as a result.**

## 4. What the bridge bench's own prescription says — and it points at D
- **R24:** *"total rounded-boundary flux `sign(q)·k` for **k proper arcs**"* — a condition
  **per arc**, symmetric across an arc's two endpoints. Nothing distinguishes one cusp.
  **That selects D, not E. D gives 6.**
- **R30:** *"at least **three positive light Dirac pairs for three strong arcs, not
  unpaired generations**."* Three arcs → three **pairs** = six states, **vector-like**.
- **So D's 6 and R30's 3 pairs are the same six states with opposite chirality verdicts.
  That disagreement IS the D-vs-E question in physical form.**
- **R30 also records:** *"the initial **order-three/C₃-fixed sample confusion** is preserved
  and corrected by a separate exact action control."* The bench hit an order-3/fixed-point
  confusion too and corrected it — it did not resolve it in favour of three.

## 5. The one open question, stated as a binary
> **Does the source prescription break the symmetry between the two cusps for a reason?**
> **Yes → E → 3.  No → D → 6, realized by R30 as 3 vector-like pairs.**

Both answers are precomputed above. This is a question about **source placement in
R15/R28/R30**, not about the index formula, and not settleable by more topology.
The bench's own open item names it: *"physical source/end dynamics and full quantum
completion remain OPEN."*

## 6. Structural note (offered, not claimed)
The Lefschetz fixed set of the order-3 on `m202`/`s959` is **3 arcs with 6 endpoints**
(3 fixed points on each of 2 cusps; `L(g) = χ(Fix) = 3`). R15's sources are **3 proper
arcs** with endpoints on the boundary. **Same combinatorial shape.** This is a shape match,
**not** a derivation that they are the same arcs — and the number 3 on both sides is
expected regardless, since both are about an order-3 structure. Offered only so the
bench can check whether the two arc systems coincide.

## 7. Independent routes to the zero, now five (six with tonight's)
`B1267` numerical · `sB1267` exact over ℚ(ω) · `fc R61` θ-equivariant ·
`B1290` χ(∂⁺M) annular · **`R30` three Dirac pairs** · and, tonight,
**B1297 §5.1's unitary theorem** (*I(V)=0 for every unitary local system*) plus
**Chern–Weil** (a flat bundle has `ch(V) = rk(V)`, so `ind D = −rk·σ/8` — representation-blind).
**Flatness, unitarity and dimension three each independently strip the
representation-dependence out of the index.**
