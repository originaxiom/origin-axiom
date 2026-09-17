# xB020 — THE MECHANISM IS COMPLEX CONJUGATION: xB019 corrected against xB012, B1224 derived, and L194's data at 5× the slice

**Seat `xb`, `sep16-branch`, 2026-09-17. PREREGISTRATION sealed `1ece78f6…` and PUSHED at `8583810`
before `verification/` existed, axes declared. Verdict: PROVED.**

Gate 5 absolute: no value, no generation count, no physics reading, nothing to `CLAIMS.md`.

---

## 1. H1 — the correction, and it is to an arc from this same session

xB019 named the mechanism as *"a non-orientable manifold's holonomy lands in `PGL(2,ℂ)`, outside the
`SL(2,ℂ)` theory."* **That is wrong — and this session had already banked the refuting fact.**

**xB012's V2: `PGL(2,ℂ) ≅ PSL(2,ℂ)`.** Over an algebraically closed field every element has a square
root, so any `A ∈ GL(2,ℂ)` is scaled to determinant 1 by `1/√det A` — hence `SL(2,ℂ) ↠ PGL(2,ℂ)` and
`PGL(2,ℂ) = SL(2,ℂ)/{±I} = PSL(2,ℂ)`. Verified symbolically. **`PGL(2,ℂ)` is not a larger group, so
it cannot be the mechanism.**

*(The same computation shows exactly why the two arcs differ: the isomorphism **fails** over `ℝ` and
over `𝔽_q`, where not every element is a square — which is precisely why `PGL(2,O₃) ≠ PSL(2,O₃)` in
xB017 but `PGL(2,ℂ) = PSL(2,ℂ)` here. **The same symbol, two different facts, one arc apart.**)*

> **THE REAL MECHANISM: `Isom(H³) = PSL(2,ℂ) ⋊ ℤ/2`, where the extra factor is COMPLEX CONJUGATION —
> anti-holomorphic, and in no `PGL` at all.** xB019's sentence is **withdrawn**.

## 2. H2 — B1224 DERIVED, not observed

Orientation reversal acts on the holonomy by **complex conjugation**, so the complex volume
`Vol + i·CS` is conjugated to `Vol − i·CS`. Volume is unchanged (it is positive), so **`CS ↦ −CS`.**

An **amphichiral** manifold admits an orientation-reversing **self**-isometry, so

> **`CS = −CS` ⟹ `2·CS = 0` ⟹ `CS ∈ {0, ¼}` mod ½.**

**That is B1224 — which banked it as a census observation (6 of 6). Here it is a consequence of the
mechanism.** And the check: over `OrientableCuspedCensus[:400]`, **6 amphichiral manifolds, 0
escapees** — `m004, m136, m206` at `0`; `m003, m135, m207` at `¼`.

## 3. H3 — L194 at five times B1235's slice (the blind cell)

B1235 cell 2 registered **L194** — *free deck ⟹ `CS ≡ 0`?* — on **40** orientation double covers, all
at zero, against a **36 %** quarter-rate among amphichiral manifolds generally. It marked the row
**"Data, not theorem."**

| orientation double covers tested | `CS = 0` | `CS = ¼` | other | errors |
|---|---|---|---|---|
| **200** | **200** | **0** | **0** | **0** |

> **Unchanged at 5× the slice.** Against the 36 % quarter-rate, `P ≈ 0.64²⁰⁰ ≈ 1.7 × 10⁻³⁹`.

## 4. H4 — what the mechanism explains, and what it does not

**EXPLAINS — the 2-torsion.** Conjugation gives `CS = −CS` for any manifold with an
orientation-reversing self-isometry. An orientation **double cover** always has one — its deck
transformation — so **its `CS` is 2-torsion by construction.** That is **B1234's cell 1 (40 of 40
amphichiral, against a 3.0 % base rate) with a reason under it.**

**DOES NOT EXPLAIN — the selection of `0` over `¼`.** Conjugation is **blind to which** of the two
2-torsion classes you land in. L194's hypothesis is that **freeness** of the deck involution does the
selecting — and **nothing in this arc derives that.**

> **H3 is data at a larger slice. It is not a proof, and this arc does not let the data imply the
> theorem.**

## 5. H5 — verdict

**(1)** xB019's mechanism sentence is **withdrawn**; the mechanism is **complex conjugation**.
**(2)** **B1224 is upgraded from OBSERVED to DERIVED**, with no census escapees.
**(3)** **L194 is sharpened, not closed**: the 2-torsion half is now explained; **exactly the
selection half remains open**, with its evidence strengthened from 40 to 200.

**AXES HELD FIXED, named as the rule requires:** **cusped** manifolds only — the closed case is not
touched · SnapPy's `cs` normalisation (mod ½) throughout · the non-orientable census slice is a
**prefix, not a random sample** · **freeness of the deck involution is CITED from B605, not
re-verified here.**

## 6. What this arc does NOT claim

Not that L194 is proved by data · not that the tools' breaking in xB019 is evidence for A6 · no
identification (E82/I-10) · no physics reading · nothing to `CLAIMS.md`.

**Locks / artifacts:** `verification/conjugation.py` (H1–H5), `verification/conjugation.json`,
`verification/conjugation.out`.
