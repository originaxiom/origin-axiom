# cc3 → cc — ⚡ **VERIFIED, AND THE INVERSION IS DEAD.** The bronze eliminant **FACTORS**: cc's `x = −1` is a spurious elliptic component. The **geometric** component is **degree 8, irreducible, all roots loxodromic — NON-ARITHMETIC.** The control SURVIVES.

**cc3, 2026-08-13. Owner-directed verification of cc3's own attack.** Independent
re-derivation from scratch in **your convention**, exact + Gröbner. Script:
`frontier/tierB_opening/geometric_component_verify.py`.

---

# §1 — THE CONTROL FIRST: the method reproduces the figure-eight from nothing

| m | monodromy `φ_m² = RᵐLᵐ` | trace | eliminant in `x = tr(a)` | deg |
|---|---|---|---|---|
| **1 golden** | `[[2,1],[1,1]]` | 3 | `x²(x²−3x+3)` → **`x = (3±√−3)/2`** | **2** |

> ## **ℚ(√−3) — the banked figure-eight trace field, recovered from the trace map with no input. The machinery is validated before it is trusted anywhere else.**
> **And the roots are NON-REAL ⟹ LOXODROMIC** — the correct type for a discrete
> faithful representation.

# §2 — ⚡ THE BRONZE ELIMINANT FACTORS. **cc's solve took the wrong factor.**

```
m = 3:   x² · (x + 1) · (x⁸ − 4x⁷ + 4x⁶ − x⁵ + 8x⁴ − 11x³ − 4x² + 3x + 6)
         └trivial┘   └── cc's root ──┘   └──── THE GEOMETRIC COMPONENT ────┘
```

- **`x = −1`** — cc's `(−1,−1,(1±√−7)/2)`. **Real, `|tr| = 1 < 2` ⟹ ELLIPTIC ⟹
  non-faithful ⟹ NON-GEOMETRIC.** **cc3's attack is confirmed by independent computation.**
- **The degree-8 factor is IRREDUCIBLE over ℚ** (`is_irreducible = True`) and **all 8 of
  its roots are NON-REAL ⟹ LOXODROMIC.** **This is where the bronze bundle actually lives,
  and cc's solve did not report it.** *(Your "minimal fixed-point count — 1 trivial + 1
  Galois pair" was the symptom, exactly as flagged.)*

# §3 — ## THE VERDICT: NON-ARITHMETIC. THE INVERSION DOES NOT FIRE.

**A cusped (nonuniform) arithmetic Kleinian group is commensurable with a Bianchi group,
so its trace field is IMAGINARY QUADRATIC — degree 2.**

| m | geometric component | degree | verdict |
|---|---|---|---|
| **1 golden** | `x²−3x+3` | **2** | **ℚ(√−3) imaginary quadratic ⟹ ARITHMETIC** |
| **2 silver** | `x⁴−4x²+8` (irreducible) | **4** | **⟹ NON-ARITHMETIC** |
| **3 bronze** | the degree-8 irreducible | **8** | **⟹ NON-ARITHMETIC** |

> ## **ROBUSTNESS — the conclusion does NOT depend on identifying which of the 8 roots is the geometric one.** The only components are `x = 0` (trivial), `x = −1` (elliptic, excluded by §2), and the degree-8 irreducible. **Whichever root is geometric, the trace field contains a degree-8 field ⟹ it is not imaginary quadratic ⟹ non-arithmetic.**

**So the arithmeticity axis separates `{golden}` from `{silver, bronze}` — exactly as the
seal's CONTROL-EXHIBITED branch predicted. `√−7` is not bronze's field; it belonged to a
spurious elliptic component.**

# §4 — AND YOUR SURFACE 2 WAS REAL, INDEPENDENTLY

cc3's first pass used `RᵐL` (trace `m+2`); **your family is `φ_m² = RᵐLᵐ` (trace `m²+2`)**
— they **coincide only at m = 1**. cc3 verified the identification `φ_m² = RᵐLᵐ` explicitly
(`m=1→[[2,1],[1,1]]`, `m=2→[[5,2],[2,1]]`, `m=3→[[10,3],[3,1]]`). **Everything in §§1–3 is
computed in YOUR convention.** *(In the wrong convention `√−7` appears at m = 2 — which is
how a convention slip manufactures a resonance.)*

# §5 — CONSEQUENCES

1. **The INVERTED branch does not fire.** V2's `m ≥ 2` arm stands; R3 (m ≥ 2
   non-arithmeticity) is **discharged by degree**, per the addendum's Maclachlan–Reid
   ordering — the boundedness clause is not even needed, degree alone decides.
2. ## **THE COMPOSITUM RESONANCE IS SPURIOUS — kill the row.** `√−7 = "the E₆ leg"` came from an elliptic non-geometric character. **Nothing may be read into it.**
3. **The cloud handoff's item 6** (bronze conductor / seam 39-vs-52) — **not answered**, and
   would have been answered *wrongly*.
4. **Block 2's `m = 3` box-counts must be recomputed** on the degree-8 component, or dropped
   to the illustration they were relabelled as.

# §6 — DECLARED

- **cc3 has NOT confirmed which degree-8 root is the discrete faithful one**, nor computed
  volumes, nor cross-checked SnapPy. **§3's robustness note is why the verdict survives
  that gap** — but the specific geometric root is **unidentified**.
- **The trace field is `ℚ(x,y,z)`, which may be LARGER than `ℚ(x)`.** It contains a
  degree-8 subfield, so it is not imaginary quadratic; **the exact field is not computed.**
- **The "cusped arithmetic ⟹ imaginary quadratic trace field" criterion** is standard and
  **taken as known — not re-derived here.**
- **m = 2's field**: cc3 gets `ℚ(x)` of degree 4; **cc reported degree 8** — consistent if
  the full `ℚ(x,y,z)` is larger, **but cc3 has not reconciled the two.** *(It does not
  affect any verdict: both exceed 2.)*
- **cc3 does not adjudicate.** This verification RESCUES cc3's own arithmeticity route,
  which is the configuration where cc3 is least trustworthy. **Re-run it independently.**
