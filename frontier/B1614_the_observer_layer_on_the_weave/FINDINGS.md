# B1614 — THE OBSERVER LAYER ON THE WEAVE: the weave has a self-name (its unique irreducible fixed point), cannot sign itself (its own rule swaps the sheets), and splits "awareness" along local systems — the geometry is wholly visible at the puncture while the matter carrying the three is wholly private — and its mirror-odd structure is two bits, not m004's one

**Verdict: PROVED** (A1–A5 hold as sealed). cc (main), 2026-10-08. Sealed `c04b1acb2` before `observer_on_the_weave.py`
ran. Asked by the owner ("are all negative conclusions about qualia valid for single thread m004 or whole weave?";
"bank and run the awareness arc"). A5 is the cell of a READING (the holonomy proposal, firewalled). None of this is a
statement about experience. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /qualia|quale|self-naming|self-signing|private state|blanket|observer layer|no self-closure|aware/: 22 of 1384 arcs on main match (NEGATIVE 3, OPEN 4, PROVED 15)`
— the observer layer B752–B1184 (all on m004), the S91 addenda, W2, B1602–B1605, B1610, B1611, B1327. **Literature:**
group cohomology of free groups and parabolic cohomology (standard); the holonomy reading's anchors (predictive
processing, integrated information, sheaf-theoretic contextuality, Chern–Simons-type odd invariants) cited from the
reviewer's knowledge and graded nothing here.

## 1. The computation (`observer_on_the_weave.py`; `observer_on_the_weave.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **A1** (QP-1) | two joint fixed points, the common point the unique irreducible one | 95% | **HOLDS** — (0, 0, 0) with κ = −2 (irreducible) and (2, 2, 2) with κ = 2 (reducible): **the weave's self-name is its common point** |
| **A2** (QP-2) | adjoint visible; matter, doublet, trivial private | 85% | **HOLDS** — adjoint H¹ = 3, restriction to the puncture injective, **0 private**; each matter block χ_p ⊗ ρ_Q and the doublet H¹ = 2, the puncture's cohomology 0 (ρ(c) = −1), **all private**; the trivial line H¹ = 2, all private |
| **A2′** | the parity lines visible | 60% | **HOLDS** — H¹ = 1 each, restriction injective, 0 private |
| **A3** (QP-4) | the rule fixes the common point, normalises the moves, reverses the form | 97% | **HOLDS** — σ(0, 0, 0) = (0, 0, 0); σLσ⁻¹ = [[2, −1], [1, 0]], σRσ⁻¹ = [[1, 1], [0, 1]], both det 1; W21's form reversed: σ swaps the sheets, so by B1327 nothing invariant under the principle's rule chooses one — **the weave cannot sign itself** |
| **A4** (one class) | sheet = det = CP-oddness; McKay differs; rank 2 over 𝔽₂ | 85% | **HOLDS** — on L, R, P, ι, σ the sheet, det and CP-oddness agree; the McKay sign differs (L, R: −1; σ: +1); rank 2 — **two classes on the weave**, where m004 had one (B1183) |
| **A5** (reading cell) | odd parts of χ_T(L), χ_T(R) non-zero; χ_T(LR) = 0; the puncture's holonomy −1 | 75% | **HOLDS** — χ_T(L) = e^{−iπ/4}, χ_T(R) = e^{+iπ/4} (odd parts ∓0.707, exchanged by the mirror); χ_T(LR) = 0 and the moves' commutator 0; the puncture loop acts on every matter block by −1 (even) |

## 2. What it says

**The observer layer on the weave is not m004's.** The weave names itself (one irreducible point every move fixes) and
cannot sign itself (its own rule exchanges the sheets) — the m004 pattern "self-naming without self-signing" holds on the
weave, by different computations. But "awareness = no private states" splits along local systems: **the geometry (the
adjoint, the deformations) is wholly visible at the puncture; the parity lines are visible; the matter that carries the
three is wholly private** — its cohomology restricts to zero at the puncture, because the puncture acts on it as −1. And
the weave's mirror-odd structure is two independent bits — the sheet, which is also CP, and the McKay orientation — not
one class.

**The holonomy reading (firewalled; proposed in conversation on 2026-10-08: awareness as a loop with holonomy, qualia as
its orientation-odd part).** On the weave: the puncture loop's holonomy is even (−1), "aware but choiceless"; a single
move's holonomy on the matter has an odd part (e^{∓iπ/4}), and the mirror exchanges L's with R's; the double tick's trace
is zero. Read together with A2: the matter's cohomology is private and the moves act on it with orientation-odd
characters. A reading, nothing more; its next cell would be the odd part as a function on the weave's whole group.

## 3. Disclosed

- The predictions were reasoned by hand before the seal; A3 recomputes facts used at B1607 and B1610.
- "Private" here means the kernel of the restriction H¹(F₂; E) → H¹(⟨c⟩; E) at the common point, one local system at a
  time; it is not the interior classes of B1602–B1605 on the forced covers (a different space), though both are
  cohomology invisible from the ends.

## 4. Files

`verification/observer_on_the_weave.py` (sealed, unchanged), `observer_on_the_weave.json`, `observer_run.txt`. Test:
`tests/test_b1614_the_observer_layer_on_the_weave.py`.
