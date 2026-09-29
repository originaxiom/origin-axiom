# xB034 — THE CROSS-BRANCH AUDIT: four of this seat's own claims corrected, one strengthened, and the physics map redrawn around a route this seat did not know existed

**Seat `xb`, `sep16-branch`, 2026-09-29. Not a sealed prediction — see `PREREGISTRATION.md`.**

## 0. WHAT WAS READ

Seven remote branches; full history after unshallowing. **121 commits since this seat last synced
(2026-09-18)** across five of them:

| branch | not in `sep16-branch` | of which since 09-18 | merge-base |
|---|---|---|---|
| `main` | 16 | 7 | `c052c857` 09-16 |
| `<remote>/standard-model-derivation-0qt6ao` (the SM seat) | 132 | 40 | `44c75c36` 09-06 |
| `audit/physical-bridge-2026-09-05` | 166 | 56 | `8f83b5c8` 09-05 |
| `<remote>/outside-bench` | 25 | 16 | `c052c857` 09-16 |
| `<remote>/paper-review-verification-kaz3f5` | 26 | 2 | `c052c857` 09-16 |
| `<remote>/physics-seat-evaluation-8dkbrl` | 165 | 0 | `a5138424` 09-01 |

**The SM seat advanced while the fetch was running** (`ac4f8a82 → 6fe28a6b`). The lanes are live.

---

## 1. CORRECTIONS TO THIS SEAT'S OWN BANKED CLAIMS

### 1.1 xB030 U1 / xB032 T1 — *"none of which saw the other two"* is FALSE

xB030 wrote that the Alexander root, the locus where the chirality index can fire, and the tower's
torsion growth rate *"are ONE algebraic number, named three ways in three arcs, **none of which saw the
other two**."* **B1260 (2026-09-06, in this seat's own tree) had made the central join twelve days
earlier**, verbatim:

> *"**Δ(t) = t² − 3t + 1**, roots **φ²** and **φ⁻²**, product **1**"* · *"the Alexander root where
> h¹ jumps"* · *"(Note the object's own golden pair appearing unbidden: the Alexander roots are
> φ^{±2}.)"*

**What xB030/xB032 actually added is narrower:** the **torsion-growth** edge (`log α` = the measured
growth constant) and the **entropy** name. **The Alexander-root/golden-locus join was B1260's.** This
is the **third** instance in the session of claiming novelty for something already in the tree.

### 1.2 xB030 U4 — *"cannot simply be composed"* is INCOMPLETE, and the correction points forward

xB030 U4 said the literature takes chirality from **conical singularities** and requires the
three-cycle to be cohomologically silent, while *"the record takes chirality from `h¹` OF the
three-cycle"* — *"opposite demands on one quantity … the two programmes cannot simply be composed."*

**That describes only one of the record's two chirality routes.** **B1355** (SM branch only — **not on
main, not in this seat's tree**) builds **the literature's own mechanism for E₆**:

> *"the destination's local model is the G₂ cone over CP³/2T … Its E₆ locus and an A₁ locus meet only
> at a curved, non-orbifold apex … by Witten's inflow the apex must carry chiral E₆-charged matter with
> U(1) charge: **the E₆ analogue of Acharya–Witten's U(N) point**."* — **PROVED for the geometry,
> CITED for the physics**; *"one 27 per point"* is the literature's rule, not re-derived.

And the outside bench, reading the same paper as xB029 **on the same day, independently**, made the
link this seat missed (memo 234 ADDENDUM 4): *"**Assumption 2 is B1355's open problem, assumed**"* —
the G₂-MSSM's granted *"conical singularities at which chiral matter is supported"* is exactly what
B1355 constructs. **So the programmes CAN be composed — along B1355.** *"Cannot be composed"* holds only
for the `h¹`-index route.

### 1.3 xB030 / xB031 — *"both routes to an index of 3 are shut"* sits UNDER stronger theorems, and does NOT cover the apex route

Correct as a statement about the **index**, but it is an empirical corroboration beneath theorems
already banked:

- **B307** (in this tree): *"no hyperbolic knot can have a cyclic-cubic (C₃) trace field"* — three
  *interchangeable* generations are impossible, **by a theorem**, not a scan.
- **B1381** (SM branch, **PROVED**): *"no cyclic cover Mₙ of m004 has a rank-one character with
  h¹ = 2, for any n … because Mⁿ is never scalar"* — **xB030's empirical cap, as a theorem, on every
  level.**
- **B1398** (SM branch): *"Every completion on the record's menu … gives an **even** number of
  generations … which is zero for a bulk flux."*

**And it does not reach the apex route.** B1355's *"one 27 per point"* makes three generations a
question of **three apexes**, which is a different mechanism with a different obstruction (L221:
*"the three-apex design is excluded **as it stands**"* — no seesaw — with a 27̄ sector as the seat's
remedy). **The index route is exhausted; the apex route is open and conditional.**

### 1.4 xB021 — the bits are the KERNEL, not a stabiliser; and twelve is a group of six

Main's **S24 / B1429** verified xB021 on its own bench and **sharpened it against its own mechanism**:

> *"On the circle the invariant lives on, the map x ↦ −x is fixed exactly where twice the value
> vanishes — **which is exactly the two-element sister orbit**. So the orientation and order bits …
> act trivially on the **whole** orbit. They are the **kernel** of the action, not a point stabiliser.
> **Moving from the object to its sibling buys nothing for these two bits.**"*

And the normalisation: *"for a cusped manifold the invariant is defined modulo a half, so values in
twelfths form a group of **six**, not twelve"* — xB021's *"the family realises all twelve"* reads
**all six classes**. **This agrees with xB033**, which found the `0`/`¼` dichotomy is the modulus: on
`ℝ/½ℤ`, negation fixes exactly `{0, ¼}` — the same fact, seen from the group side.

---

## 2. TWO CELLS, COMPUTED — both run from this arc against banked artefacts

### C1 — the generation cap and the thermodynamic side share a root: POSITIVE ENTROPY

B1381's mechanism is that `Mⁿ` is never scalar. `entropy_and_the_cap.py`:

| monodromy | type | `h_top` | first scalar power, `n ≤ 40` |
|---|---|---|---|
| `RL` = m004, and 7 more hyperbolic words | hyperbolic | 0.962 … 2.292 | **NEVER** |
| `R` | parabolic | 0 | NEVER |
| order 4, 6, 3 | elliptic | 0 | **`n = 2, 3, 3`: ±I** |

**Positive entropy is SUFFICIENT for B1381's non-scalarity** — the elliptic control fires, so the
test discriminates — **and NOT necessary** (parabolic is entropy-zero and never scalar). **So the
generation cap and xB032's thermodynamic side have one root: the monodromy is pseudo-Anosov.** It is
the **positivity** of the entropy that does the work — **not** its golden value, **not** its minimality:
every hyperbolic word caps too. *Stating this as an equivalence would be wrong, and it is not stated.*

### C2 — E65 confirmed on xB031's banked modules, and it explains what xB031 left bare

E65 / B1260: *"every Sym^n of SL(2) is self-dual, so net chirality is identically zero."* Any SL(2)
representation preserves the symplectic form, **so `ρ_χ` is self-dual even though it is non-split**;
then `V = Sym^m(ρ_χ) ⊗ ψ` has `V* ≅ Sym^m(ρ_χ) ⊗ ψ⁻¹`, and **`ψ² = 1` forces `I = 0`.**

| | `ψ² = 1` (self-dual) | `ψ² ≠ 1` |
|---|---|---|
| X2 (`m ≤ 3`, 6 435 modules) | **771, all `I = 0`** | 432 with `I ≠ 0` |
| X3 (`m = 4…6`, 2 808 modules) | **288, all `I = 0`** | 144 with `I ≠ 0` |

**Kill (a self-dual module with `I ≠ 0`) fired 0 times on 1 059. All 576 nonzero modules carry
`ψ² ≠ 1`.** **So xB031's index is a TWIST effect, not a `Sym^m` effect:** untwisted `Sym^m` is always
zero, and the `ψ` twist is the only thing breaking self-duality. xB031's *"higher-`Sym` route"* was
really the *"ψ-twisted higher-`Sym` route"*, and E65 had already closed the untwisted one.

---

## 3. RECONCILIATIONS AND SCOPE NOTES

- **The referee's `max h¹ ≤ b₁`** (paper-review round 3 §7) is a **cusped, deficiency-one** statement;
  xB030's closed data — `h¹ = 1` with `b₁ = 0` on **506** manifolds — show it does not extend to closed
  manifolds. **Not a contradiction of the referee**, who scoped it to *"everything scanned"*; B1260 §1
  explains why it doesn't matter there: on a closed manifold `h¹(V) = h¹(V*)` identically, so `h¹ = 1`
  carries no net chirality.
- **The referee's own §9** withdrew most of §§7–8 as re-derivations of B1260, B307, B1161, B850 and
  E65. **This seat read §9 before leaning on §7.**
- **`already_banked.py` does not read `papers/`** (outside bench memo 236, bench error #40). A real gap
  — **but it did not cause xB033**: the tool reads `docs/*.md` (`--wide`) and every `FINDINGS.md`, so
  it would have found B1239. **xB033's failure was not running it.**

---

## 4. INTEGRATION HAZARDS — for the owner, because they need a scheme decision

### 4.1 Lead numbers collide, and main already has internal duplicates

`OPEN_LEADS.md` has **no uniqueness check** on either branch.

| | main | `sep16-branch` |
|---|---|---|
| duplicated numbers | **L160, L222, L223, L224** | L160, L220 |
| L222 | E83 residue **and** *The family as the object* | *The family as the object* |
| L223 | *Silent receipts* **and** *Level mismatch* (renumbered from the fork's duplicate L220) | *k-coupling normalisation* (xB016) |
| L224 | *Harvest gate is blind* — **the same entry twice** | *Amphichiral knot `cs ≡ 0`* (xB023) |
| L225 | *3D index under Dehn filling* (B1428) | *Ray–Singer torsion term of `P_eff`* (xB029) |

**On merge, L223 would exist three times, L224 three times, L225 twice** — and every arc, log and
changelog line that cites them would point at the wrong lead. **Main's own attempt to fix the fork's
duplicate L220 (by renumbering it to L223) created a new collision.**

**Not renumbered here**: the durable fix is a scheme — seat-namespaced leads (as `xB` already
namespaces this seat's arcs), or a reservation plus a uniqueness gate like the one `relay-debt` now
has — and it binds every seat. **That is the owner's decision.** Rewriting this seat's historical log
lines would also violate their append-only rule.

### 4.2 Error-class numbers diverge

Main is at **E83** (*hash-order-dependent verification*), this branch at **E82**; both carry a
duplicated **E58**. **R58-1's class must be minted as E84 or higher**, not E83. Main has **no**
mismatched-hypothesis class, so R58-1 is still needed.

### 4.3 The same result banked twice under different numbers

B288's *"no arithmetic filling"* was withdrawn as **B1419** on main and as **B1376** on the SM seat.

---

## 5. WHAT THIS DOES TO THE ROADMAP

- **R58-3 — RESOLVED BY PORT.** Main repaired `test_b288` on **2026-09-16 (S12), one commit after this
  branch forked**; the SM seat removed it too. This branch still asserted the falsehood. **Ported
  byte-identically from main; 4 passed.** *R58-3 was a debt already paid the day it was filed.*
- **R58-1 / R58-2 — UNBLOCKED.** B1376 has landed. **Mint as E84/E85**, after syncing with main.
- **The physics priority is reordered.** The `h¹`-index route is **structurally exhausted** — B307,
  B1381, B1398, E65, xB030, xB031. **The live bridge to the literature is B1355's apex route**, where
  three generations means **three apexes** and the open problem is L221's 27̄ sector. **xB031's
  declared remainder (31 loci, `m > 6`, `t12833`) is demoted accordingly** — C2 shows the index there
  is a twist effect that E65 already bounds.
- **`cs(M*) = −cs(M)` stays the cheapest load-bearing literature debt** — and main's S24 leans on it too
  (*"both are fixed by the mirror"*), so it is now load-bearing on two branches.
- **Integration needs the lead-number scheme decided first** (§4.1).

**Gate 5 absolute. No value. Nothing to `CLAIMS.md`.**
