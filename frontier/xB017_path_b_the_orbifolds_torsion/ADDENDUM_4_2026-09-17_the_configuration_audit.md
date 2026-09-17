# xB017 — ADDENDUM 4: the CONFIGURATION AUDIT — three axes never varied, two of them move the answer

**2026-09-17. `PREREGISTRATION.md` untouched (`82134f36…`); cells E1–E4.**

The owner defined what he means by *verify*: **"to see whether you're properly informed for the task,
and all the configurations around it."** That reframes this arc's corrections — **each was a negative
given while under-informed about one configuration**, not a computational error. So this addendum
enumerates Path B's configuration **axes** and varies the ones xB017 never varied.

| axis | configurations | xB017 |
|---|---|---|
| the field `d` | all imaginary quadratic | **varied** (base rate) |
| cover level | `(√−3), (2), (3), (4), (8)` | **varied** |
| the cover | full vs maximal regular intermediate | varied **only in Addendum 3** |
| **ambient group** | `SL` / `PSL` / **`PGL`** | **NOT varied** |
| **torsion order** | `{2,3}` in PSL / **`{2,3,6}` in PGL** | **NOT varied** |
| **the object** | m004 / **m003** | **NOT varied** |

---

## E1 — the ambient group: the deck group is ℤ/4, not ℤ/2

xB017 worked in `PSL(2,O₃)`. **But the programme's own tower uses `PGL(2,O₃)` as the base** — `v₀` is
its covolume, and the 1 : 12 : 24 tower is measured against it.

**A first test here was inconclusive and is recorded:** it conjugated by the single element
`diag(ζ₆,1)`, found it does **not** normalise `Γ`, and would have concluded "PGL adds nothing." **That
is one representative of the coset, not the coset.** Corrected — testing all **12** classes of `Γ` in
the non-PSL coset: **2 normalise**, and the first passes the full check over all **20 480** elements.

> **`|N_PGL(Γ)/Γ| = 2 (PSL) + 2 (coset) = 4 = |Isom⁺(m004)|`.**

**And a theorem confirms it independently of the search:** for an **arithmetic** manifold
`Isom⁺(M) = N_{Comm(Γ)}(Γ)/Γ`, and the commensurator is the maximal group of the class — `PGL(2,O₃)`,
since `h = 1`.

> **Addendum 3's ℤ/2 was itself under-stated.** In the ambient group the programme actually uses, the
> deck group is **ℤ/4 — all of m004's orientation-preserving symmetry.**

## E2 — the torsion order: the base orbifold's cusp torsion is ℤ/6

`diag(ζ₆,1)` acts as `z ↦ ζ₆z`, of **order 6** in PGL. PSL sees the same cusp rotation as order 3,
because it quotients by the units' squares.

| d | \|O^×\| | PGL cusp rotation |
|---|---|---|
| **3** | **6** | **order 6 ← extra** |
| 1 | 4 | order 4 ← extra |
| 2, 5, 7, 11, 15, 163, … | 2 | order 2 |

> **xB017's N2 — "orders {2,3}" — is correct and PSL-SCOPED.** The programme's base orbifold is the
> **PGL** one, whose cusp torsion is **ℤ/6** — and **6 is the largest torsion order of any Bianchi
> PGL group.** A sharper `d = 3` selector than anything xB017 measured.

## E3 — the object: m003 and m004 are indistinguishable by everything this arc used

| | PSL-index | \|Isom\| | \|Isom⁺\| | amphichiral | H₁ |
|---|---|---|---|---|---|
| m004 | 12 | 8 | 4 | yes | ℤ |
| m003 | 12 | 8 | 4 | yes | ℤ/5 ⊕ ℤ |

**Identical on every invariant Path B used.** What separates them is **H₁** and the **congruence
level** — m003 at `(2)¹` with quotient `A₅`, m004 at `(2)³ = (8)` (B734).

> **Path B's machinery does not separate the sisters; the congruence level does. That is the handle
> Path C needs, and it was sitting in this arc's own dependency, unused.**

---

## E4 — what the audit changes, and the method lesson

**Path B's standing, strengthened:** **both** torsion orders **positive** — the ℤ/2 part is really
**ℤ/4** in the right ambient group, the ℤ/3 part really **ℤ/6** there. **Negative only** that the full
cover is regular. **Fences unchanged:** the cusp rotation does not descend to m004 (`|Isom⁺| = 4`, no
order-3 or order-6 symmetry).

> **THREE OF THIS ARC'S FOUR ERRORS WERE UNVARIED CONFIGURATIONS, NOT WRONG ARITHMETIC.** A negative
> is only as wide as the configuration space actually swept — **and the sweep must be written down
> before the headline. Not the cells alone: the AXES.**

**This is now a standing rule** (`WORKING_RULES` / `docs/PRACTICES.md`): **a preregistration declares
its CONFIGURATION AXES and which values of each it will vary; a negative is reported as scoped to the
swept region, and any unvaried axis is named in the verdict.**

**Artifacts:** `verification/addendum4_configuration_audit.py` (E1–E4), `verification/addendum4.json`,
`verification/addendum4.out`.
