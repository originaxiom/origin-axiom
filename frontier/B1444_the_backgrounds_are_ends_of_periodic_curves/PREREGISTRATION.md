# B1444 PREREGISTRATION — THE TORSION LAW ON UNTOUCHED LEVELS: is the banked coupling the first-order torsion of the sector along the periodic curve through the background?

**Sealed 2026-10-01, before any periodic curve is followed on any level of the population below. Seat: cc (main).
Occasion: lead L235 (what fixes the Higgs values) and the owner's instruction of 2026-10-01 to carry a chain to its
last computation. A sweep of main and every lane on 2026-10-01 found the periodic-orbit fields of the trace map on
κ = −2 (B448) and the slope defined as a cusp shape (B1438), and found no statement that a periodic curve passes
through the torsion points on κ = 2, and nothing linking the frame's backgrounds to such curves.**

## 0. The quantifier (P0)

For every level of the population, and every extension character ℓ selected in §2: the curve of solutions of
T(p) = σ·p through the torsion point of ℓ on κ = 2, and on it every rank-two sector module ρ ⊗ a (β running over all
characters of the level with α = ℓβ and β non-trivial). The scope sentence names no level.

## 1. The objects

- T is the trace map of the level's monodromy Φ on (X, Y, Z) = (tr x, tr y, tr xy), κ = X² + Y² + Z² − XYZ − 2.
- A character ℓ of the level of order above two has a square root v on the fibre; diag(v, v⁻¹) is a smooth point p₀
  of κ = 2 with T(p₀) = σ·p₀ for a sign twist σ. dT at p₀ has eigenvalues λ, λ⁻¹ on the surface and 1 across it, so
  exactly one smooth curve of solutions passes through p₀, transverse to κ = 2. Its points off κ = 2 are
  representations of the level into PSL(2, ℂ), irreducible on the fibre; the meridian is the intertwiner T (det 1,
  T → 1 at p₀).
- The sector with quotient character β is the module x ↦ (vβ)(x)ρ(x), y ↦ (vβ)(y)ρ(y), t ↦ T. At p₀ it is α ⊕ β with
  α = ℓβ: the frame's sector module (B1432) with its extension class switched on is the first-order germ.
- Its torsion is τ = det(1 − Φ* | H¹(F; V)), computed on cocycles modulo coboundaries.
- e = 2 − κ is the parameter along the curve at p₀.

## 2. The population (fixed before the run; sizes computed without following any curve)

27 levels: −LLR 1, −LLR 2, −LRR 1, +LRR 2, −LRR 2, +LLLR 1, +LLLR 2, −LLLR 1, −LLLR 2, −LLRR 1, +LLRR 2, −LLRR 2,
+LLRLR 1, +LLLRR 1, −LLLRR 1, +LRLRR 1, −LRLRR 1, +LLLLR 1, −LLLLR 1, +LLLLR 2, +LLRLRR 1, −LLRLRR 1, +LLLRLR 1,
−LLLRLR 1, +LLRRLR 1, +LLLRRR 1, −LLLRRR 1 — every level from a list of 34 short word states with fibre torsion
between 3 and 32 and at least two extension characters of order above two, none of which has been run. On each
level up to six extension characters, spread evenly over the characters of order above two in their fixed order.

Instrument `verification/law_population.py` on `verification/curve_engine.py`; reader `verification/read_law.py`
(run twice on the control before the seal, identical output).

## 3. What has been seen before the seal (disclosed in full)

Everything below was found by exploration on 2026-10-01 and is the reason for the predictions. It is not evidence
for them; the population is.

- **The curves of the root, exactly** (primary decomposition over ℚ): level one, a conic through the two order-5
  torsion points and the geometric representation; level two, lines; level three, on each sign twist a line and
  two rational quartics, with κ − 2 = w(w − 1) and m + 1/m − 2 = −w(w² − w + 4), w = u − 1/u, u = X + 1.
- **The exploratory census:** 11 levels (+LR 2, 3, 4; −LR 1, 2, 3; −LLRLR 1; +LLR 2; −LLLR 3; +LRR 3;
  +LLRLRRLR 1), 56 backgrounds, 1 265 sectors: 932 of 932 unmatched sectors have first-order coefficient
  (s(α) − s(ℓ))(s(β⁻¹) − s(ℓ)); every matched sector has order at least two; 80 matched sectors are identically
  zero; the cusp shape tends to |s(ℓ)| on 56 of 56; identically zero ⟺ meridian = ±(longitude)^±s on 56 of 56.
- **A guess that failed and is not predicted:** "order = 1 + number of matches". Ten doubly matched sectors have
  order two.
- **The control** (`control_run.txt`, levels +LR 2 and +LR 3 through the sealed instrument and reader): P1 40 of
  40, P2 56 of 56, P3 10 of 10, P4 10 of 10.
- Per-sector tables of the frame's backgrounds on +LR 3, +LR 4, −LR 3, −LR 4, +LLR 3, −LLLR 3, +LLRLRRLR 1.
- **No curve has been followed on any level of §2.**

## 4. Sealed predictions (each can come out either way)

| | prediction | prior |
|---|---|---|
| P1 | Every unmatched sector (s(α) ≠ s(ℓ) and s(β⁻¹) ≠ s(ℓ)) has torsion of order one in e with coefficient (s(α) − s(ℓ))(s(β⁻¹) − s(ℓ)), to relative 10⁻⁶. | 85% |
| P2 | Every matched sector has order at least two or vanishes identically; no unmatched sector vanishes identically. | 85% |
| P3 | On every background the cusp shape log M / log l of the curve tends to \|s(ℓ)\| at the reducible end, to relative 10⁻⁶. | 90% |
| P4 | On every background: some matched sector vanishes identically ⟺ the meridian equals ±(longitude)^±s along the curve. | 65% |
| P5 | The population contains backgrounds of both kinds (filling type and not). | 80% |

A background whose curve the instrument cannot follow (branch point before e = 0.02, or a failed Newton step) is
reported and counted, not dropped silently; for P4 it is untested.

## 5. What each outcome would mean (written before the data)

- **P1, P3 YES** would make the slope law (B1438) a statement about actual flat connections: the slope is the cusp
  shape at the end of a curve of irreducible representations, and the coupling s(ℓ) − s(η) is the first-order
  term of the sector's torsion along it. **P1 NO** on even one sector would mean the eleven exploratory levels were
  special and the statement is withdrawn to them.
- **P2** is the firing law seen from the curve: a slope match is the vanishing of the first-order term.
- **P4 YES** would split the backgrounds into two kinds by a topological criterion (the curve lies in a Dehn
  filling); **P4 NO** would leave the identically vanishing torsion unexplained.
- None of the outcomes is a physical statement. Off the end κ = 2 the cusp holonomy has no invariant vector in a
  doublet, so the class index is zero there by B1297's identity: the index of the frame is a property of the
  reducible end. Torsion is not a mass. 0 of 19.

## 6. Not in this arc

A proof of P1–P4; the second-order coefficients as a closed formula; levels with fibre torsion above 32; the curves
through the order-two characters (nodes of κ = 2); the direction of the Higgs character η.

## 7. Hashes at seal

See `ARTIFACT_HASHES.txt`.
