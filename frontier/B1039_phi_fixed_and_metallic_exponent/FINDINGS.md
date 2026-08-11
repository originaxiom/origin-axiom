# B1039 — two clusters restored, and **re-verifying them found two defects in what was about to be restored**

**Date:** 2026-08-11 · **Lane:** the consolidation refresh, campaign **step 5** (*"restorations bank
as arcs — re-verify the identities before restoring, **never restore from memory**"*). Gate 5
untouched; zero anchors; nothing to `CLAIMS.md`.
**Files:** `verify.py` → `results.json` (34 checks) · lock
`tests/test_b1039_phi_fixed_and_metallic_exponent.py` (12).

Restores two of B1037's seven clusters — **four debt rows, two laws** — chosen not by size but by
**what this sandbox can honestly redo**. `snappy`, `cypari`, `cypari2`, `sage` and `flint` are all
absent here, so restoring an arc on citation alone would *be* restoring from memory.

---

## 1. THE HEADLINE IS NOT THE RESTORATION — IT IS WHAT THE RESTORATION CAUGHT

Both laws survive. **Both arrived carrying a defect that a citation-level restoration would have
propagated onto a curated surface**, and in one case the defect is a **false statement**.

### DEFECT 1 — *"finite image ⟹ reducible tower"* is **false**, and the counterexample is small

`B141` Item 3 states the conceptual root of the whole split:

> *"**Finite image ⟹ reducible tower; dense image ⟹ irreducible tower.** This is the conceptual
> root of the φ-vs-φ² distinction."*

**The first half is false as a general implication.** Computed here, from scratch:

| group | order | `Sym²` algebra dim | verdict at `n = 3` |
|---|---|---|---|
| `Q₈` | 8 | **3** of 9 | reducible |
| **`SL(2,3)`** (binary tetrahedral) | **24** | **9** of 9 | **IRREDUCIBLE** |

`SL(2,3)` is **finite** and its `Sym²` is **irreducible**. The bound is not finiteness — it is the
**maximal irrep dimension `d`**, which gives reducibility for every `n > d`. That is **2** for `Q₈`
and **3** for `SL(2,3)`, and *the two groups sit on opposite sides of their own bound at exactly
`n = 3`* — so the bound is **sharp**, and finiteness alone is not the reason.

> **B141's conclusion survives untouched; only its stated mechanism was too strong.** The tower over
> `Q₈` really is reducible for all `n ≥ 3`, and the reason really is a dimension inequality —
> `dim Sym^{n−1} = n > 2` — it is just not the inequality the slogan names. **Restored in the
> narrowed form.**

### DEFECT 2 — the Klein-4 chain has an **unstated hypothesis**

`B142`'s one-line proof opens: *"principal eigenvalues `{1,−1,−1}` ⟹ `A² = I`."* That step needs
**`A` semisimple**. The Jordan matrix `diag(1) ⊕ [[−1,1],[0,−1]]` has the **same spectrum** and
**det 1**, and is **not** an involution — verified here. The hypothesis *does* hold at a φ-fixed
point (`A` is conjugate to `diag(1,−1,−1)` by fiat), so **the proof is sound**; it was simply never
written down, and a restoration that copies the chain verbatim copies the gap.

**And B142's probe never verified its own lemma.** `klein4_lemma_symbolic()` exhibits **one**
commuting pair and checks the identities on it. The universally quantified statement — *two
involutions whose product is an involution commute* — is verified here for the first time, as a
group identity: `⟨a,b | a², b², (ab)²⟩` has **order 4** and **trivial commutator**.

---

## 2. THE φ-FIXED LAW, RE-DERIVED

**The split is a determinant sign, visible before any representation is built.** The φ-map
`A ↦ AB, B ↦ A` abelianises to `[[1,1],[1,0]]` — **det −1**, trace 1, golden. The bundle monodromy
`σ_R∘σ_L` abelianises to `[[2,1],[1,1]]` — **det +1**, trace 3 — *which is the object's own
`A = LR`*.

**And the bridge equation does the selecting.** The induced trace map is **derived**, not quoted:
`tr(ABA) = tr(A²B) = xz − y` by Cayley–Hamilton on generic det-1 matrices, giving
`(x,y,z) ↦ (z, x, xz−y)`. Its fixed points are **exactly two**:

| fixed point | `κ = x²+y²+z²−xyz−2` | |
|---|---|---|
| `(2,2,2)` | **`κ = 2`** | the cancellation completes — ***nothing*** — reducible |
| `(0,0,0)` | `κ = −2` | **the unique irreducible φ-fixed point** |

> **The founding sentence is the selection principle here.** *"κ = 2 ⟺ nothing"* is not decoration
> on this cluster — it is what leaves exactly one candidate standing, and that candidate is `Q₈`.

`(0,0,0)` forces `tr A = tr B = tr AB = 0`, hence `A² = B² = −I` and `AB = −BA`; the group closes
at **order 8**. Its **five** conjugacy classes force five irreps, and `Σd² = 8` over five parts has
the **unique** solution `1+1+1+1+2` — so **max irrep dim 2 is derived here, not quoted from a
character table**. The algebra-dimension table reproduces B141 exactly:

| n | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| alg dim | **4** | 3 | 4 | 4 | 4 | 4 |
| `n²` | 4 | 9 | 16 | 25 | 36 | 49 |

**Irreducible at `n = 2` only.** The other side re-verifies too: the φ²-geometric holonomy has
`alg dim = n²` for `n = 2..5` with all word-traces in `ℚ(√−3)`, and `A^k = [[1,k],[0,1]]` is
unbounded — **infinite image**.

## 3. THE METALLIC EXPONENT, RE-DERIVED — and the meridian is **forced**

The load-bearing object is an **exact free-group identity**:

> `φ_m([A,B]) = Aᵐ[A,B]A⁻ᵐ` — verified by word reduction for **m = 1..10**. *(B154 verified
> `m = 1, 2`; the induction for general `m` was never written down, and that gap is **carried**,
> not closed.)*

From it, `µ = A⁻ᵐt` is peripheral in one line — `µ[A,B]µ⁻¹ = A⁻ᵐφ_m([A,B])Aᵐ = [A,B]` — given only
the mapping-torus relation `tXt⁻¹ = φ(X)`, which *defines* the bundle.

**And the exponent in the meridian is forced, not fitted.** `A⁻ᵏt` is peripheral **only** at
`k = m` — checked for `m = 1,2,3` across `k = 0..6`, unique every time, because in a free group
`A^j` commutes with `[A,B]` only at `j = 0`. Abelianisation confirms the family:
`ab(φ_m) = M_m²` with trace `m²+2`, for `m = 1..7`.

**B198's SL(5) result is re-checked against its banked certificate, not re-searched** — the right
move for a claim whose evidence *is* a certificate:

| | measured here (dps 40) | B198 quotes |
|---|---|---|
| `‖[A,B] − µ²‖` | **1.55 × 10⁻¹⁹** | 1.5e−23 (at dps 60) |
| `‖[A,B] − µ¹‖` | **3.878** | 3.9 |
| `‖[A,B] − µ³‖` | **8.230** | 8.2 |
| `‖µ − t‖` | **2.1876** | 2.19 |
| Burnside rank | **25 of 25** | full |
| `order(µ)` | **INFINITE**, loxodromic | geometric component |

**The counterexample that kills every closed form was re-run in-sandbox**, by invoking B198's own
reproducer rather than reimplementing it (the B1033 pattern): on the `order(µ) = ∞` stratum,
**`o = 4` and `o = 8` both give `k = 3`**, 8/8 reps each. `k = 7−o` predicts **3 and −1**;
`k = 4−m(o−3)` likewise. **Both refuted, measured rather than remembered.**

## 4. THE TWO SCOPE QUALIFIERS THAT TRAVEL WITH THE ROW, OR IT IS AN OVERCLAIM

1. **B199's sublocus.** *"`[A,B] = µ²` **on the geometric component**"* over-states it. The rigid
   identity holds on a **dim-2 sublocus — ~1 % of irreducible loxodromic reps** (8/887, 24/3486).
   **The `err < 1e-6` filter *selected* that sublocus**, so *"305/305 unanimous"* was a **filter
   artifact**. Read `k = 2` **at the complete cusped rep**. *(At SL(3) it does hold component-wide;
   the sublocus phenomenon emerges with rank.)*
2. **Every closed form is refuted** — including the one still printed above B154's own correction
   banner. Restoring that line without the banner would restore a refuted claim, which is the one
   outcome a consolidation pass must never produce — **the same trap B1037 caught at B123.**

## 5. WHAT IS CARRIED BY CITATION — named, not implied

**B142's `s776` cartography** (SnapPy + PARI: the magic-manifold identification, volumes, symmetry
orders, trace fields) — a **tombstone K-I plus guard MB10, not a positive result**, and not part of
the restored law. **The all-`n` density step** (standard theorem; `n = 2..5` computed here).
**B154's *"exactly 2 components"*** — primary decomposition, which sympy cannot do. **B198's exact
SL(3) cells** — Sage/Singular ideal membership; no CAS here finishes that Gröbner computation,
*which was B157's premise in the first place*. **B141 Item 4** — *"the SL(3) φ-fixed locus is
entirely reducible"* — is a **CONJECTURE** in its own arc (a 60/60 numerical search) and is
restored as one.

---

**Verdict: PROVED.** 34 checks. **Four debt rows retired into two curated laws**: the band
B100–B199 goes **27 → 23** and the corpus **221 → 217**, *exactly the four rows, no drift*.
**Both figures are dated** — the 27/221 are measured with rows written by B1039 and later
removed, so the arc that retires rows does not also move the number it publishes.

**Self-correction — a NEW failure mode, not another instance of the running one.**
The self-measurement hazard is present as usual and was handled the usual way (both band figures
dated, this arc's rows excluded from the 27/221). **This is a different thing: the instrument
itself was wrong, and only its control knew.** `sym_power` built by substituting coordinates directly is an
**anti**-homomorphism (`Sym^d(MN) = Sym^d(N)Sym^d(M)`), and the control — functoriality plus
`det Sym^d = (det)^{d(d+1)/2}`, B1038's identity reused — **failed on the first run**. Every
downstream number was unaffected (an algebra's opposite has the same dimension, a group's opposite
the same irrep dimensions), **so nothing would have looked wrong**. It is fixed by acting through
`Mᵀ`. *This is precisely the contravariance bug-class B154 records catching with its own
figure-eight control* — *"a control that must reproduce a known answer is the cheapest guard"* —
found the same way, in the arc that restores it.
