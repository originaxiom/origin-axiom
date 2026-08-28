# B1205 — THE CUBIC CELL RUN: the cubic exists and is failable, but it cuts one dimension of three — the missing ingredient is the LINEAR cuts, and GC-25 already proved they are absent

**Status: banked (frontier). Verdict NEGATIVE** for the proposal as posed (B1204's cubic route
cannot force the ℙ³), **with a sharper positive residue**: the requirement is now located exactly,
and its absence is a *proved* fact rather than a gap in the search.
`verification/reproduce.sh` → `REPRODUCES`. Gate 5 clean.

## What was proposed, and what was run

B1204 read the record's one continuum-to-points forcing (B1160's hypercharge) and prescribed:
*seek a failable condition, nonlinear in its decisive step*, naming the object's own cubic at the
coupling as the candidate home. **The cell ran that.**

**Good news first — the cubic is real.** The down block is a 3×3×4 tensor (B1185), so
**Y_d(h) = Σ_k h_k T[:,:,k]** is linear in the Higgs direction h ∈ ℙ³, and therefore
**det Y_d(h) is a genuine cubic form on the ℙ³** — degree 3, not identically zero, and **failable**
(a generic h has det ≠ 0). Exactly the shape B1204 asked for, and it exists at exactly the place
row E1 says the values live.

**Then the counting kills it.** One polynomial equation cuts exactly one dimension:

- **{det Y_d = 0}** is a cubic **surface** in ℙ³ — dim 3 → 2. Not points.
- Its **singular locus is empty** (grad = 0 has no nontrivial solution; 5/5 random samples smooth —
  and classically a generic determinantal cubic surface *is* smooth), so "h is a singular point"
  selects nothing.
- The **rank ≤ 1** locus has codimension (3−1)² = 4 inside a 3-dimensional space: **empty by count**.

## THE DIMENSION LEDGER — why B1160's recipe does not transfer

| | starting space | linear conditions | after linear | the cubic | result |
|---|---|---|---|---|---|
| **B1160 (worked)** | 5-dim charge space | **three, and they do FOUR dimensions of work** | a **LINE** (dim 1) | cuts 1 | **POINTS** |
| **the ℙ³ (here)** | dim 3 | **NONE — proved absent** | still dim 3 | cuts 1 | a **surface** (dim 2) |

**In B1160 the cubic was decisive only because the linear conditions had already done the dimensional
work.** The cubic did one dimension; the anomaly linears did four. On the Higgs line there are no
linear conditions at all — and that is not an oversight, it is **B1195/GC-25's proved result**: every
banked symmetry acts *trivially* on B₀, which is exactly why the ℙ³ row was typed
PERMANENT-AT-CURRENT-KNOWLEDGE.

**So the two results lock together, and the conclusion inverts the prescription**:

> **The missing ingredient for forcing the ℙ³ is not the nonlinear condition — the nonlinear
> condition exists. It is the LINEAR cuts, and the record has already proved that no banked symmetry
> supplies them.**

## What this changes

- **B1204's prescription is amended, not discarded**: "failable, nonlinear in its decisive step" is
  right about the *last* step and silent about the *first*. The full recipe is
  **linear conditions to cut dimension, then one nonlinear condition to cut to points** — and the
  program currently has the second half and not the first.
- **The requirement is now exactly stated**: forcing the Higgs line needs **three independent
  conditions linear in h** (or two linear plus the cubic). Since no symmetry provides them
  (GC-25) they would have to come from a *consistency* requirement linear in the closer's data —
  an anomaly-type constraint on the coupling, not a symmetry of it.
- **GC-25's permanence result is upgraded in meaning**: it is not merely "the floor carries three
  continuous parameters"; it is **the proof that a B1160-style forcing cannot reach them.**

## Fences

The tensor entries are not banked (the 𝒯 char-0 evaluator remains commissioned to codex, R023), so
the computation is over the *shape* — a generic 3×3×4 tensor — not the object's specific T. That is
sufficient for the dimension ledger, which is a codimension count and cannot be improved by knowing
the entries: **a single equation cuts one dimension whatever its coefficients.** It is *not*
sufficient to rule out the object's own T being non-generic in some *other* useful way (e.g. its
determinant vanishing identically, which the banked SKEW ZERO and the rank-2 family law make worth
checking when 𝒯 lands) — that check is named, not run. The smoothness claim is sampled (5/5) plus
the classical fact, not proved for the object's T. Nothing here weakens V-3.
