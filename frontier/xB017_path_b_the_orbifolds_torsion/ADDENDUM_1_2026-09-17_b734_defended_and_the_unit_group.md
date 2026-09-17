# xB017 — ADDENDUM 1: a banked result DEFENDED against an outside check, and the invariant this arc missed

**2026-09-17. `PREREGISTRATION.md` untouched (`82134f36…`); new cells A1–A4 in
`verification/addendum_checks.py`.**

The literature sweep xB017 commissioned returned **after** the arc banked. It **confirms** N1–N5's
conclusions and supplies citations for what the arc had computed — **and it does two other things:
it challenges a banked repo result, and it names an invariant this arc never tested.**

---

## A1 — the challenge, adjudicated BY COMPUTATION, and the banked result wins

The sweep scored B734's congruence level as **wrong**, claiming `π₁(4₁)` is congruence at level
`⟨4⟩` rather than `⟨8⟩`, on a table showing "index 12" at `⟨4⟩`.

**Adjudicated on this bench rather than by choosing a report:**

| level | \|SL(2,O₃/n)\| | \|image\| | \|centre\| | \|img ∩ Z\| | **SL**-index | **PSL**-index |
|---|---|---|---|---|---|---|
| (2) | 60 | 10 | 1 | 1 | 6 | **6** |
| (4) | 3 840 | 320 | 4 | 2 | **12** | **6** |
| (8) | 245 760 | 20 480 | 8 | 8 | 12 | **12** |

The geometric index is **12 in PSL**, so the congruence level is the smallest ideal whose **PSL**
index reaches 12 — **`⟨8⟩`, not `⟨4⟩`. B734 is right.**

> **And the challenge's "12" at level `⟨4⟩` is the SL index, read as a PSL index.** That is **E21**,
> already in this repo's error ledger — minted in July 2026 when a research agent made the **same
> slip on the same group**: *"a congruence/index conclusion over PSL(2,·) must quotient by the FULL
> centre of SL(2,O/I) … not read the SL image index."* The centre at level `⟨4⟩` has order **4** and
> the image meets it in **2**, exactly as E21 describes.

**A banked, two-seat result defended against an outside check by the repo's own bookkeeping rule.**
The error ledger did not just classify the failure after the fact — **it predicted the failure mode
of an independent check made fourteen months later.**

## A2 — Γ(√−3) is not even a manifold group (N5(a) strengthened)

The sweep supplied an explicit element of `Γ(√−3)`; verified here exactly:
`M = [[−4−4ω, −3], [−1+4ω, 3+4ω]]` has `det = 1`, `trace = −1`, `M³ = I`, and `M ≡ I (mod √−3)`.

> **`Γ(√−3)` contains 3-torsion**, so `H³/Γ(√−3)` is an **orbifold, not a manifold.** N5(a) showed
> `Γ = π₁(m004)` is *not* that group; this shows it **could not have been.** *(The sweep also
> computes 4 cusps for it — not re-verified here, flagged.)*

## A3 — 2T is a congruence QUOTIENT, never a stabiliser

`|SL(2,𝔽₃)| = 24 = |2T|`, `|PSL(2,𝔽₃)| = 12 = |A₄|`. The deck group of
`H³/Γ(√−3) → H³/PSL(2,O₃)` acts **faithfully** on `H³`, and the **centre of `SL(2,𝔽₃)` acts
trivially** there — so the deck group is **A₄**, not 2T. And by **Klein's theorem (1875)** the finite
subgroups of `PSL(2,O_d)` are exactly `1, ℤ/2, ℤ/3, D₂, D₃, A₄` — **no binary polyhedral group
embeds in a Bianchi group at all.**

> **2T occurs as a congruence quotient and never as an isotropy group.** xB017's N1 said *"onto"*,
> which is correct; this fixes the word that would have been wrong next. **The record should not read
> the spine's 24 as a symmetry *of* the orbifold — it is the order of a quotient.**

## A4 — the invariant this arc never tested, and it DOES single out d = 3

The cusp stabiliser in `PSL(2,O_d)` is `O_d ⋊ (O_d^×/{±1})`, so the cusp cross-section is
`T² / (O_d^×/{±1})`. And `O_d^× = {±1}` for **every** `d` except two:

| d | \|O_d^×\| | `O^×/{±1}` | cusp cross-section |
|---|---|---|---|
| 1 | 4 (`μ₄`) | ℤ/2 | `S²(2,2,2,2)` |
| **3** | **6 (`μ₆`)** | **ℤ/3** | **`S²(3,3,3)`** |
| 2, 5, 6, 7, 11, 15, 19, 23, 31, 43, 67, 163, … | 2 | trivial | `T²` |

> **The cusp is a torus for every imaginary quadratic field but two, and `d = 3` is the only one with
> a ℤ/3 there.** `μ₆` is also the **largest unit group** of any imaginary quadratic field.

**xB017's N2 is SCOPED, not overturned.** The torsion **orders** `{2,3}` are generic, exactly as N2
proved — that argument stands. **But the cusp's ℤ/3 is not generic**: it is `d = 3`'s alone, and it
comes from the **unit group**, which is *neither* the torsion orders N2 tested *nor* the ramification
N3/N4 tested.

> **The honest answer to "what distinguishes `d = 3`" is its unit group `μ₆`** — and this arc missed
> it because it tested exactly the two invariants it had named in its own seal. **A preregistration
> fixes what you will test; it does not tell you what you failed to think of.** That is the limit of
> the method, stated plainly, and it took an outside sweep to show it.

**Does this rescue Path B's frame? No.** N5(b) stands untouched: `Γ` is not normal, the cover is
irregular, there is **no deck group**. The cusp ℤ/3 is an invariant of the **orbifold**, not deck data
for m004 over it. **Path B's verdict is unchanged; its base-rate finding gains a genuine exception,
and the exception is not the one the path was built on.**

---

## What the sweep confirmed, with citations the arc had computed rather than cited

Torsion `{2,3}` for every `d` — **Klein 1875**, *Math. Ann.* **9**, 183–208 (finite subgroups of
`PSL₂(O)` are `1, ℤ/2, ℤ/3, D₂, D₃, A₄`) · `SL(2,𝔽₃) ≅ 2T`, `SL(2,𝔽₅) ≅ 2I`, and **only** these ·
`SL(2,𝔽₂) ≅ S₃`, `SL(2,𝔽₄) ≅ A₅` (**not** binary) · norm-3 ramification exactly when `3 | D` ·
`D = −3` the unique discriminant ramified only at 3, with `|D|` minimal · `v₀ = 0.0845784672008…`
correct to 13 digits, via **Humbert's formula** · `[PSL(2,O₃) : Γ₈] = 12` — **Riley 1975**,
*Math. Proc. Camb. Phil. Soc.* **77**, 281–288 · `Γ₈` non-normal with `N(Γ₈)/Γ₈ ≅ ℤ/2`, agreeing with
N5(b)'s isometry-count argument · `PGL(2,O₃) = [3,3,6]⁺`, the cleanest structural reading of the 24.

**Carried caveats, not dropped:** the sweep could **not** verify theorem numbers in Fine or in
Elstrodt–Grunewald–Mennicke and says not to quote them; and it flags an unverified "≈0.0408" for the
minimal cusped orbifold volume circulating in search results, which matches nothing in this
commensurability class. **Neither is used here.**

**Artifacts:** `verification/addendum_checks.py` (A1–A4), `verification/addendum_checks.json`,
`verification/addendum_checks.out`.
