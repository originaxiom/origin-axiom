# B1293 — SEAT HARVEST 2026-09-06: the SM group is reached, I-14 collapses to a point, and my B1290 was second

**Verdict: PROVED** for what is re-computed here; the rest is fenced as **harvest, not verification**.
Owner's instruction was to fetch codex — codex's head is **R040 (2026-09-02), already harvested at
B1238/B1239, nothing new**. Two *other* seats pushed the same day, and both land on the main goal.

## 1. Confirmed on this bench, from structure alone

| claim | seat | checked here |
|---|---|---|
| E₆ has **120** A₂ subsystems and **40** A₂³ subsystems | fc R65/R68 | ✓ built from E₈ roots; matches `51840/1296 = 40` |
| labelling `c = (1,0,2,2,0,2)` grades the 27 as **9+9+9**, and so does its θ-flip | fc R68 | ✓ |
| `z_L` is an **A₁A₅ involution** of E₆ splitting the 27 as **15 + 12** | SM seat B1277 | ✓ a ℤ/2 grading with that split has centralizer **dim 38 = 3 + 35**, and `27|SU(2)×SU(6) = (2,6̄)⊕(1,15) = 12+15`; `78 = 38 + 40` |
| `π₁(m004)` has **48** surjections onto 2T | banked | ✓ reproduced (used as the method control in B1292) |

## 2. The calibration that changes how R68 should be cited

**9+9+9 occurs in 178 of 728 nonzero labellings — 24.5%, the *most common* grading shape, not a rare
one.** So R68's content is **not** the partition. It is the **two-sided ℤ[g]-stability** that cuts
**40 → 4 → 1**. *Anyone citing "9+9+9" as the discovery is citing the wrong number.* Recorded because
that is exactly the misreading this corpus has been burned by (E61/E63: right arithmetic, wrong
attribution).

## 3. The two results main did not have

**(a) The first vacuum with the Standard-Model group — SM seat B1277.** The closing's own sign
character composed with the SU(2)_L centre, `W = z_L ∘ χ_j`, together with `⟨N_g⟩, ⟨ν^c_g⟩`, leaves
**su(3) ⊕ su(2) ⊕ u(1)_Y** unbroken. Their words: *"the first vacuum of the programme with the
Standard-Model group."* **Its A₁A₅ step is confirmed above; the stabiliser computation itself is
harvest.**

**(b) I-14 collapses to a point — fc R68.** Of E₆'s 40 trinification A₂³ subsystems, **exactly one**
is stable under the founding ratio from *both* sides, and it is **mirror-invariant**. `85 → 40 → 4 →
1`. Third H5 multiplicity to become a point, and the largest. **fc's own fence, which main must carry:**
*"what is not exhibited: that the physical trinification the record's chain uses **is** this subsystem
rather than one of the other 39."*

## 4. The obstruction that came with them

**Theorem (SM seat B1277): every vacuum with three generations of Q, u^c, e^c keeps SU(5) unbroken.**
So on Y₃ you cannot have the SM group *and* three generations — *"two generations of Q and L is the
closing's Standard Model."* **Their own scoping, carried verbatim:** this is a property of **the
closed closing**, *"which is vector-like anyway,"* and *"the chiral closing named in the destination
ledger is still the object to construct."* **Harvest, not verified here.**

## 5. Priority, stated plainly

**fc's R56 derived `net chirality = χ(M, ∂⁺M)` — with *"zero on any closed 3-manifold, zero for a
knot"* and *"the record's seven chirality walls are one theorem"* — before main's B1290.** B1290 and
B1291 are **independent confirmation and extension**, not discovery. B1291 *does* go strictly further
on one point: B1277 §4 enumerates *"every candidate ∂⁺ ⊆ T² (empty, an annulus, the torus)"* — three
cases — where B1291 proves the **general criterion** (χ ≠ 0 **iff** the dividing set has a
null-homotopic component), classifies **all 54** involutions, and adds the **parity theorem**.

## 6. One distinction I nearly conflated, recorded so nobody else does

fc's **R61** says *"θ is a real structure on the **fibre**"* with `Fix(θ)` two arcs; **R62** says
*"θ = −I"* on the **cusp torus**. **Different spaces — not a contradiction.** On the *closed* cusp
torus `−I` has **exactly 4 isolated fixed points** (B1291's rank-2 case), never arcs, because a closed
surface has no boundary for an arc to end on. Arcs live on the *quotient*.

## Fences

1. **NOT verified here:** R68's icosian `4 → 1` collapse (needs their rebuilt icosian E₈ and the
   founding ratio's two-sided action); the SM seat's vacuum-manifold scan, its Wilson-line stabiliser,
   and its SU(5) theorem. All carried as **harvest with attribution**.
2. **No ledger row moves.** I-14 stays as fc leaves it — the listener-map half is unchanged. I-26
   untouched.
3. **Arc-ID collision discipline holds:** the SM seat's arcs are cited as `sB1272…sB1277` per
   `docs/SM_SEAT_ALIAS_TABLE.md`; main's B1272–B1277 are different arcs.

*Scope addendum 2026-09-08 (E53, B1303; the point was chat1's, HARVEST_LEDGER row 20): the headline's "the SM group is reached" is
the GAUGE ALGEBRA at the Wilson-line step (sm:B1278, re-run B1294). The seat's own next arc, sm:B1283 — verified on this bench in
B1303 with independent code — computes the tree-level vacuum of that closing and finds that every SM-preserving flat direction
leaves ONE extra U(1) unbroken: at tree level the unbroken group is **SU(3) × SU(2) × U(1)_Y × U(1)_Z′ (rank 5)**, with a
family-non-universal Z′ of computed charges. The headline stands for what it says (the algebra); the vacuum's rank is 5, not 4.*
