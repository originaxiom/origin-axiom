# xB032 — THE THERMODYNAMIC SIDE: the torsion growth rate IS the monodromy's topological entropy, and the step B803 named in 2026 and never took turns out to be blocked by the same wall as everything else

**Seat `xb`, `sep16-branch`, 2026-09-18. PREREGISTRATION sealed at `988ca30d` before any cell existed.**
**Owner's direction: *"the object had a thermodynamical side we never account for, which plays a
crucial role for physics ambitions."***

**Reconnaissance first, and it constrains what this arc may claim.** The record is **not** innocent of
this vocabulary — 199 files mention entropy, 66 Ruelle, 52 Fried, 41 dilatation. It already holds the
dilatation `φ²` and its **minimality** (xB014 ADDENDUM 1: *"extremal three ways"*, `1 of 40` on
`log λ` and on volume, the minimum **forced** because *"trace 3 is the smallest possible for a
pseudo-Anosov in `SL(2,ℤ)`"*), and **B803 already named the missing step and filed it under "Not
verified here"**: *"The analytic-torsion join (needs the cusped Cheeger–Müller/**Fried** literature
step first — a literature step, not a computation)."*

**So the gap was never the vocabulary. It was the JOIN — and a step written down as owed and never
taken.**

---

## T1 — THE SIXTH NAME, AND IT IS THERMODYNAMIC

m004 is the once-punctured-torus bundle with monodromy `RL`:

| | |
|---|---|
| `RL = [[1,1],[0,1]]·[[1,0],[1,1]]` | **`[[2,1],[1,1]]`**, trace **3**, det **1** |
| characteristic polynomial | **`t² − 3t + 1`** |
| Alexander polynomial of `4₁` | **`t² − 3t + 1` — IDENTICAL** |
| dilatation `λ` = spectral radius | **`(3+√5)/2 = α = φ²`** |
| **topological entropy `h_top = log λ`** | **`0.9624236501` = `2 log φ`** |
| xB029's **measured** tower torsion growth per level (re-read from `g2_mssm.json`, not recalled) | **`0.9624236501`** |

> **`log|Tor H₁(Xₙ)| = n · h_top(monodromy) + o(1)`.**
>
> **The tower's torsion homology is an ENTROPY, growing at exactly the entropy rate of the object's
> own monodromy. So Friedmann–Witten's `T_O` term — `P_eff = log|Tor H₁(Q̂)|`, the quantity Acharya
> et al. need to reach 84 — is on this tower `n · h_top`.**

**FENCE, in the seal and repeated:** for a **fibred** knot the Alexander polynomial **is** the
characteristic polynomial of the monodromy. That is **classical**. **The content is that three arcs
carried the same number without the join** — xB030 found five names for `α`; this is the sixth, and
it is the one that makes the other five mean something physical.

---

## T2 — THE EXTREMALITY, JOINED: the object is the SLOWEST TORSION PRODUCER in its class

| word | trace | dilatation | `h = log λ` | volume | measured `log\|Tor\|/n` at `n = 60` | match |
|---|---|---|---|---|---|---|
| **RL** | 3 | **2.61803399** | **0.96242365** | **2.029883** | **0.9624236501** | ✓ |
| RRL | 4 | 3.73205081 | 1.31695790 | 2.666745 | 1.3169578969 | ✓ |
| RLL | 4 | 3.73205081 | 1.31695790 | 2.666745 | 1.3169578969 | ✓ |
| RRRL | 5 | 4.79128785 | 1.56679924 | 2.989120 | 1.5667992370 | ✓ |
| RRLL | 6 | 5.82842712 | 1.76274717 | 3.663862 | 1.7627471740 | ✓ |
| RLRL | 7 | 6.85410197 | 1.92484730 | 4.059766 | 1.9248473002 | ✓ |
| RLRRL / RRLRL | 10 | 9.89897949 | 2.29243167 | 4.751702 | 2.2924316696 | ✓ |

**8 of 8, at 6 distinct dilatations — the binding control (≥ 4 distinct values, so the agreement is
not an artefact of testing only the minimum) is satisfied.** Minimum entropy at `RL`; minimum volume
at `RL`.

> **The dilatation column and the torsion-growth column are THE SAME COLUMN.** So xB014's *"extremal
> three ways"* says something it did not say: **the object minimises the entropy — it is the slowest
> torsion producer in its class.**

**FENCE:** minimal dilatation is a **known theorem**; minimal volume is **Cao–Meyerhoff**. **Nothing
here is new mathematics. The join is the content.**

---

## T3 — THE STEP B803 NAMED AND NEVER TOOK, AND IT LANDS ON THE SAME WALL

**Obtained at source: N. V. Dang, C. Guillarmou, G. Rivière, S. Shen, *The Fried conjecture in small
dimensions*, arXiv:1807.01189v3 (Invent. Math.).** **Fried himself is NOT read here** — his theorem is
quoted **through** DGRS, so **Fried's row stays CITED-UNREAD** and **DGRS becomes READ-AT-SOURCE**.

> **Definition, verbatim:** *"We say that the complex (or `ρ`) is **acyclic** if `H^k(M; ρ) = 0` for
> each `k`."*
>
> **Fried's formula, verbatim (their eq. 1.2, `dim(M) = 2n₀+1`):** *"`|ζ_{X,ρ}(0)^{(−1)^{n₀}}| =
> τ_ρ(M)`, where `ρ` is the lift to `π₁(M)` of an **acyclic and unitary** representation
> `ρ₀ : π₁(M) → U(ℂʳ)`."*

**The sealed prediction was that Fried requires ACYCLICITY — the same `h¹ = 0` that Friedmann–Witten
buy with finite `π₁`. It holds, and it is STRONGER than sealed: there is a SECOND hypothesis,
UNITARITY, which the seal did not name.**

**And the record's own objects were measured against both:**

| | |
|---|---|
| reducible non-split loci examined (`t12835` over `ℚ(ζ₁₂)`, plus m004) | **56** |
| satisfying **ACYCLIC** | **0** — `nonsplit_cocycle()` returns a cocycle **only** when `h¹(χ²) > 0`, so every locus has `h¹ ≥ 1` **by construction** |
| satisfying **UNITARY** | **0** — a unitary rep is completely reducible; these are reducible **non-split**, hence not semisimple, hence not unitary. B1418 says so itself: *"not the geometric holonomy, not unitary"* |

**Independent corroboration from the record's own numbers:** `I^ss = 0` **everywhere** in B1418's
table. The semisimplification — which is what a unitary representation would be — gives index zero at
every locus. **The index exists only off the semisimple set.**

> **ONE WALL, THREE COATS.**
> **Friedmann–Witten** need no zero modes (`h¹ = 0`), bought with **finite `π₁`**.
> **Fried** needs **acyclic AND unitary**.
> **The record's chirality index** is *defined* on the locus `h¹ ≠ 0` and fires *only* on
> **non-semisimple** modules.
>
> **The thermodynamic route does not go around the wall. It requires STRICTLY MORE than the
> topological one.** B803's *"literature step, not a computation"* is now taken far enough to know
> that **obtaining Fried's own paper would not change the outcome** — the step fails on hypotheses,
> not on access.

---

## T4 — THE HONEST READING, AND ITS LIMITS

**(a)** `P_eff` is an **entropy**. FW/Acharya's condition `P_eff = 84` is an **entropy requirement on
the three-cycle** — 84 nats, `n = 88` levels of this tower — and the cosmological-constant tuning is
an **entropy-matching** condition rather than a geometric one. **THIS IS A REFRAMING. It changes no
number and derives nothing.**

**(b)** It does **not** make a hyperbolic `Q̂` admissible. **xB029 Addendum 1 stands**: FW assume
finite `π₁`, and the zero modes are real on three of six members.

**(c) DO NOT SLIDE BETWEEN THE TWO ENTROPIES.** `h_top` of the **geodesic flow** of *any* hyperbolic
3-manifold is **2**, universally — it discriminates nothing. The entropy that carries information here
is the **monodromy's**, `log λ`, which is a **fibration** datum, not a metric one. **An argument that
moves from one to the other is wrong.**

**(d)** It does not cross B1012's wall. xB014 ADDENDUM 1 already recorded that a ladder supplies a
**dimensionless index** where the wall needs a **dimensionful** quantity, and an entropy is still
dimensionless.

---

## THE VERDICT

**T1** `α`'s sixth name is `exp(h_top)` — the tower's torsion is the monodromy's entropy, and
`P_eff` is therefore an entropy. **T2** the dilatation column and the torsion-growth column are one
column, at 6 distinct values, so the object **minimises the entropy** as well as the volume.
**T3** the never-taken Fried step is **blocked by acyclicity AND unitarity**, both of which the
record's mechanism violates **by construction** — 0 of 56 loci satisfy either. **T4** a reframing,
declared as one.

**Prior scored: T1 correct · T2 correct with the control satisfied · T3 correct AND the seal
understated it (unitarity was not predicted) · T4 held to.**

**Gate 5 absolute. No value. Nothing to `CLAIMS.md`. The record now carries one number under SIX
names instead of six numbers.**
