# B1253 — THE GEOMETRY OF THE FOREIGN 16s IS RIGID — AND IT IS *NOT* A GENERATION COUNT

**Status: banked (frontier). Verdict PROVED, at a scope this arc's own first draft got WRONG.**
`verification/sm_sector.py`, selftest green (rc captured directly, E39). Gate 5 clean.

## 0. THE HEADLINE THIS ARC ALMOST CARRIED, AND WHY IT IS DEAD

A first draft claimed **"the generation count is forced at three."** **It is refuted**, by a test the
record itself supplied. `docs/OPEN_PROBLEMS.md` §C — *"Multiplicity → the generation count"* — was
**CLOSED on 2026-08-30** because **B324** showed the candidate three there were **g-conjugates**,
hence **sharing one character**, hence tautological. The same objection applies here, and the check
is one computation:

> **All 15 sixteen-blocks lie in a SINGLE Weyl orbit** (the orbit has 27 members; all 15 are in it).
> So the three 16s in every triple are **W(E₆)-conjugates**. They share one character.
> **"Three" counts CONJUGATES, not species. This is not a generation count.**

The draft was corrected **before** the claim reached `THE_SM_VERDICT.md` — a patch to that file was
written on the dead basis and **reverted**. Recorded as **E63** below.

## 1. WHAT IS REAL — the W6 layer B891 named on 2026-08-04 and nobody ran

B891 registered *"the next W6 layer is structural: the pairwise geometry of the three 16s"* and it
went **unrun for thirteen months of arcs** (the B1247 retrieval failure, recurring). Computed here on
B1250's construction — each mod-2 weight-character with `so(10)` stabiliser cuts a 16-block from the
27; there are **15**, all **distinct**, and the geometry is **rigid**:

| | |
|---|---|
| pairwise `\|A∩B\|` | exactly **TWO** values: **8** (45 pairs), **10** (60 pairs) |
| empty triple intersections | exactly **11** of 455 |
| each of those 11 | `\|A∩B\| = \|A∩C\| = \|B∩C\| = 8`, `\|A∪B∪C\| = 24` of 27, residue **3** |
| max mutually-independent family | **3** — no fourth |

**Two-sided control**, 300 random collections of 15 random 16-subsets of a 27-set: max family 2 in
288 cases and 3 in only 12 (~**4%**); distinct pairwise-overlap values 5–9, **never 2** (**0/300**).
**The rigidity is real and non-generic.** What it is *not* is a count of species.

## 2. EACH 16 IS A COMPLETE SM GENERATION (a check on B1252's derivation)

On the hypercharge **derived** at B1252: **all six anomalies cancel** (control: shifting Y(e^c) by
1/6 breaks Y³ and Y·grav²); **hypercharge conserved on ALL 45 cubic terms**; `Y` on the 16 is exactly
the SM set, on the **10** exactly **two Higgs doublets + the colour-triplet pair** (not assumed), on
the 1 exactly `{0}`, traceless overall; and the **full SM Yukawa sector** is present in the 40
`10·16·16` terms — up, down, charged-lepton, Dirac-neutrino, plus the 24 expected GUT proton-decay
operators. **Scope:** a 16 of SO(10) is anomaly-free by construction and the Yukawa structure is
standard, so these are **consistency verifications**, valuable because a wrong Y would have failed
them on any of 45 terms.

## 3. THE PRINCIPAL DECOMPOSITION, computed not cited

`27 = Sym¹⁶ + Sym⁸ + Sym⁰ = 17 + 9 + 1` from the weights with B1252's exact metric, so B632's
`h¹ = 3` splits as **1 (trivial, abelian) + 1 (Sym⁸) + 1 (Sym¹⁶)**.

## 4. E63 — THE ERROR, recorded because it nearly reached a canonical surface

**Class: a rigid structure mistaken for a species count, because the equivalence was never quotiented
out.** The geometry (15 blocks, two-valued overlaps, max family 3) is real and non-generic — and
**every element of it is Weyl-equivalent to every other**, so none of it distinguishes species. The
control I ran (against *random* subsets) tested **rigidity**, not **inequivalence**, and rigidity was
never the question. **Rule:** before a multiplicity is read as a count of things, **quotient by the
symmetry that acts on them** — and note that `OPEN_PROBLEMS` §C had already closed this exact route
on 2026-08-30, so a sweep of the open-problems file would have supplied the test before the claim.

## 5. WHAT THIS DOES AND DOES NOT CHANGE

**Unchanged:** the generation **COUNT** stays on the **open-inputs** side, where `THE_SM_VERDICT.md`
and **B1033** put it. **B714's** "generation COUNT 3, object-forced" is untouched by this arc (it
rests on the rungs, not on these blocks). B891's *"mechanism-hood: not decided"* stands.

**Added:** the pairwise geometry B891 asked for, computed and rigid; the anomaly/Yukawa verification
of B1252's derived hypercharge; the principal decomposition computed rather than cited; and a
recorded refutation of the reading those facts invite.

## Dependencies

B891 (the layer), B1250 (the blocks), B1252 (the metric and Y), B632 (h¹ = 3),
B324 / `docs/OPEN_PROBLEMS.md` §C (the conjugacy objection that decides it), B1033, B714.
