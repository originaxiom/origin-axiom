# xB017 — ADDENDUM 3: "still negative both paths on B?" — No. NEITHER torsion order is negative.

**2026-09-17. `PREREGISTRATION.md` untouched (`82134f36…`); new cells D1–D4 in
`verification/addendum3_the_z2_is_deck_data.py`. The THIRD correction to this arc, and the second
produced by an owner question rather than by the arc's own checking.**

The question was a status check. **Checking instead of answering turned up a third correction.**

---

## The claim that was too strong

N5(b) concluded: *"`Γ` is not normal, the cover is irregular, **there is no deck group at all**."*
**The last clause is too strong.**

**True:** the **full** index-12 cover `m004 → H³/PSL(2,O₃)` is irregular, so the orbifold's torsion
is not the deck group **of that cover**.

**Also true, and this arc never looked:** the **maximal regular intermediate cover**
`m004 → H³/N(Γ)` has deck group **ℤ/2** — and **its nontrivial class is represented by genuine
2-torsion of the Bianchi orbifold.**

## D2/D3 — the witness, and the two bugs caught before the verdict

Enumerating **exact** order-2 elements of `PSL(2,O₃)` (trace 0, `det = 1` in `ℤ[ω]`) with entries in
`[−6,6]²`: **1738 found. 590 of them normalise `Γ` and lie outside it.**

**Control:** **0 of the 1738 lie inside `Γ`** — as required, since `Γ` is a knot group and
torsion-free. A nonzero count would have meant the reduction or the membership test was broken.

**The first witness, verified four ways:**

1. **Full conjugation** over all **20 480** elements of `Γ mod 8`, not just the two generators:
   `g H g⁻¹ = H`. ✓
2. **Exact over `ℤ[ω]`:** `det = 1`, `trace = 0`, `g² = −I` — **order 2 in PSL, i.e. genuine
   orbifold 2-torsion.** ✓
3. **All 590 witnesses lie in ONE coset of `Γ`** — consistent with `N(Γ)/Γ ≅ ℤ/2`: a single
   nontrivial class, **and it is represented by 2-torsion.** ✓
4. **Geometric:** `|Isom(m004)| = 8`, orientation-preserving part `ℤ/4`, which has a **unique**
   element of order 2 — exactly what the deck ℤ/2 must be. ✓

**Two bugs of this seat's own, caught inside the cell before any verdict, and recorded because the
verdict rests on the corrected hunt:**

* **Bug 1 — the wrong level.** A first normalisation test worked **mod 4**. `Γ` does **not** contain
  `Γ(4)` — the PSL-index at level 4 is **6**, not 12 — so the test was at the wrong level and its
  answer (`N/H = 1`) was **void**.
* **Bug 2 — `det ≡ 1 mod 8` instead of `det = 1` exactly.** A first hunt accepted matrices whose
  determinant was 1 *modulo 8*. **Those live in `SL(2,O₃/8)` and are not in the Bianchi group at
  all**, and they produced **1260 spurious "witnesses"** — an 18 % hit rate against a chance
  expectation of 0.7 %, which is what exposed it.

---

## D4 — Path B, fully re-aimed

| | role | verdict |
|---|---|---|
| the orbifold's **ℤ/3** | **covering** data — the cusp cross-section `S²(3,3,3)`, `d = 3`'s alone among all imaginary quadratic fields | **POSITIVE** |
| the orbifold's **ℤ/2** | **deck** data — it realises the deck involution of the maximal regular intermediate cover | **POSITIVE** |
| the **full** index-12 cover | is it regular? | **NEGATIVE** |

> **Neither torsion order is negative. What was negative was this seat's framing — three times over.**

**And the fences stay, which is where the actual content is.** The ℤ/3 does **not** descend to m004
(B486's rectangular cusp; m004 has no order-3 symmetry), while the ℤ/2 **does** act on m004. **So the
two orders behave differently, and that asymmetry is the finding:**

> **The ℤ/2 acts on the object. The ℤ/3 does not.**

**Not claimed:** any mechanism, any physics reading, any identification of either torsion with a
trinification ℤ/3, `2T/Q₈` or `Z(E₆)` (E82/I-10; xB005 priced that family at **0.58 bits**).

---

## The pattern, stated because it is now threefold

| challenge | what it overturned |
|---|---|
| *"u sure about extremality"* | xB014's kill — wrong sort direction, wrong rank convention |
| *"are u sure about b"* | xB017's headline — a kill aimed at one half of a two-clause question |
| *"still negative both paths on B?"* | xB017's N5(b) — *"no deck group at all"*, when a regular intermediate cover has one |

**Three times the error was the same shape: a negative stated more broadly than what was actually
tested.** The rule xB017 Addendum 2 earned — *a kill must say which clause it kills* — is now
extended by this one:

> **A kill must also say at which LEVEL it holds.** *"No deck group"* was true of the full cover and
> false of the intermediate one, and the arc never distinguished them. **When a cover is irregular,
> the next question is not "so there is no deck data" — it is "what is the maximal regular
> intermediate cover, and what is ITS deck group?"**

**Artifacts:** `verification/addendum3_the_z2_is_deck_data.py` (D1–D4),
`verification/addendum3.json`, `verification/addendum3.out`.
