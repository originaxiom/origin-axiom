# MEMO 161 — THE STABILIZER IS so(8), COMPUTED — AND WHAT THAT MEANS FOR THE SM

**Banked 2026-08-30.** Seal `seals/Q7_STABILIZER_ID_PREREG.md`, pushed before computing.
Certificate `certificates/q7_stabilizer_id.py`; output vendored.

**`SUMMARY: S1-28 | S2-RANK4 | S3-SIMPLE`** — all three as the declared prior said.

---

## 1. WHAT WAS COMPUTED

Memo 160 said *"a dimension count is evidence, not an identification"* and left the stabilizer
unverified. It is now computed, exactly, in the object's own trace field ℚ(√−3) — no floating point.

| | |
|---|---|
| **S-1** | `dim 𝔰 = 28`, as an **exact nullspace** inside `B575`'s banked e₆-in-gl(27) basis — **by construction**, where memo 160 had it by subtraction. A **second independent pair** also gives 28, so 28 is generic, not an artefact of one choice. |
| **closure** | all **784** brackets solved in 𝔰's own basis and **verified on all 729 coordinates** — 𝔰 is a subalgebra, checked rather than assumed |
| **S-2** | **rank 4** (centraliser dimension of a generic element) |
| **S-3** | **SIMPLE** — centraliser dimensions across the basis are **min 4, max 4**; elements with centraliser ≥ 14 (which a whole 𝔤₂ factor would force): **0** |

**Dimension 28 with rank 4 does not settle the type** — both `𝔰𝔬(8)` and `𝔤₂ ⊕ 𝔤₂` have dimension
28, rank 4, and 24 roots. **Simplicity separates them, and 𝔰 is simple.** So:

> **The generic stabilizer of a pair (27, 27̄) in e₆ is 𝔰𝔬(8) — type D₄. Identified, not guessed.**

That closes **hypothesis 1 of five**, and it is the one memo 160 flagged hardest.

## 2. WHAT IT DOES *NOT* CLOSE — the fence, held

- **A Lie algebra is not a group scheme.** `𝔰𝔬(8)` is compatible with **Spin(8), SO(8) and PGO(8)**,
  and **only the simply connected Spin(8) gives strong approximation.** That is now the sharpest
  remaining unknown, and it is sharper than before precisely because the algebra is settled.
- **Hypothesis 5 is untouched** — that the orbit count equals the stabilizer's class set (the
  Borel–Serre / Bhargava bijection, needing `G(ℤ)` class number one and a coherent integral model).
- **S-4 is UNPINNED, as predicted.** This is the **generic** pair. Whether the object's own pair is
  generic — lies in the open orbit — was not established here, and must not be quietly widened.
- **`B990`'s declared UNFAVOURABLE prior stands unrepudiated.** **Route A has not been shown to
  cross.**

---

## 3. WHAT IT MEANS FOR THE STANDARD MODEL — the owner's question, answered narrowly

**Directly: nothing. Not one measured number moves.** No value, no mass, no mixing, no generation
count. This is not a physics result and must not be filed as one.

**What it bears on is the *input ledger*, and one specific row.** `B990`'s gap is that an orbit
invariant cannot pick a point — and *"a VEV is only ever defined up to the unbroken group,"* so a
canonical **integral** orbit would **be** a canonical VEV direction. `B1017` names exactly this:

> **"THE RECOUNT: FIVE RESOURCES, AND THE RANK CLOSING IS UNSOURCED."**

The fifth of five resources — the **rank-closing VEV direction** — is the interface's single
remaining un-derived slot. **If Route A crossed, the programme would stop *supplying* it and start
*deriving* it from the arithmetic of a totally-real S₃ cubic field.** One input moves out of the
"had to hand in" column.

**And even then it is a direction, never a number.** `B991` proved the hypercharge normalisation is
not derivable *in principle* — the anomaly conditions are homogeneous, so they fix a direction and
never a scale. **A crossing gives the direction and cannot give the value.** The SM's numbers stay
exactly where nine proved value-crossing negatives put them.

**And it changes nothing about the rest of the wall:** `λ` still has no acceptance criterion;
`ℙ(B₀)` is still one condition short; there is still **no equation of motion anywhere**, and the one
route probed came back **generic to every finite-volume hyperbolic 3-manifold**; generations are
closed on the commensurator route and **sector-complete negative** on the cohomological one.

> **The honest ceiling of this whole line, if every remaining hypothesis holds: one supplied input
> becomes a derived one, and it is a direction rather than a value. That is ledger work, not
> physics.** It is worth doing because the ledger is the paper's spine and `B1017` calls this row
> the sharpest open item on the board — not because it moves the Standard Model.

## 4. GATE 5 AND FENCES

No measured value entered. Exact linear algebra over ℚ(√−3) throughout. The optimisation that made
the run feasible (inverting one independent coordinate block once, instead of a 729-row elimination
per bracket) **preserved the full-span verification** — every bracket is still checked on all 729
coordinates, so closure is proved and not assumed.

---

## ADDENDUM (2026-08-31) — `S3-SIMPLE` WAS A NECESSARY CONDITION, NOT A SIMPLICITY PROOF

**Marked in place, not rewritten.** This memo reports the stabilizer **SIMPLE**. The test behind that
word is: no basis element has centraliser dimension ≥ 14, *"which a whole `g₂` factor would force"* —
a **necessary condition against one named alternative** (`𝔤₂ ⊕ 𝔤₂` over the same field), not a proof
that the algebra has no proper ideal. The certificate's inline comment scopes it correctly; the
verdict label and this memo's prose do not. **Bench error #19.**

**The alternative the test cannot see:** for `L/F` quadratic, `Res_{L/F}(𝔤₂)` has `F`-dimension **28**
and generic centraliser `F`-dimension **4** — it reproduces *every number measured here*. The test was
built against a direct sum **over F**, where one whole factor centralises another; a Weil restriction
has no such F-factor, so the premise does not apply to it and it was never excluded.

**The conclusion was true and is now proved.** Memo 167 computes the **centroid**: dimension **1** at
`p = 100003` and `p = 1000003`, with the **Killing form rank 28 of 28** exactly. Semisimple with
trivial centroid ⟹ **central simple**; central simple of dimension 28 ⟹ **type D₄ uniquely**, since
no other simple Lie algebra has dimension 28. So `S3-SIMPLE`'s verdict **stands**, `S1-28` and
`S2-RANK4` are **reproduced** (same seed, dim 28, all 378 brackets re-verified on all 729
coordinates), and the identification is upgraded from *consistent with D₄* to **forced**.
