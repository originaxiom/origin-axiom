# K021 — The founding identity: `g = −R·L⁻¹`, the two ends, and where the values are (and are not)

**Textbook layer (`knowledge/`): a self-contained explainer, firewalled, citing its `B`/`V` provenance. It introduces
no new result — it ties the 2026-07-01 arc into one narrative a reader outside the program can follow.** Nothing here
promotes to `CLAIMS.md`; the physics dictionary is **postulated**, not derived; the mathematics is exact and
independently checkable.

---

## 0. One-paragraph statement

A single substitution `σ` builds two `2×2` integer matrices `R, L` (the generators of `SL(2,ℤ)`). Their **product** and
their **ratio** are the two arithmetic ends of the whole program: `RL` (trace 3) generates `ℚ(√5)` → E₈ (the golden /
monodromy end), and `−R·L⁻¹` — which **equals** the order-3 element `g` that permutes the three matter generations —
generates `ℚ(√−3)` → E₆ (the Eisenstein / gauge-and-generation end). The object forces all the dimensionless
**structure** (the gauge group E₆, the 27, three generations, a democratic Yukawa) but leaves the **values** (the mass
hierarchy, the CP sign) behind a wall. This document shows what that wall is *made of*: the two ends live in two
quadratic fields that share only `ℚ`; a value would be an element of their compositum `ℚ(√5,√−3)`; and while that
compositum is exactly the **Hilbert class field of the seam `ℚ(√−15)`** (so the object completes its own seam), the
seam's arithmetic is generic and carries no value. The value is the product of a real-transcendental magnitude (a
volume) and a finite-complex phase (a congruence torsion) — a product the single object never takes.

---

## 1. From the axiom to two letters

The program's premise (`philosophy/P000`–`P005`) is "not nothing → distinction". The minimal formal carrier is a
substitution `σ` on a two-letter alphabet, whose incidence/​twist matrices are

```
R = [[1,1],[0,1]]     L = [[1,0],[1,1]]      (⟨R,L⟩ = SL(2,ℤ))
```

The metallic once-punctured-torus bundles have monodromy `RᵐLᵐ`; `m=1` is the **figure-eight knot complement** (K010),
the object the program is *about*.

---

## 2. The founding identity  `g = −R·L⁻¹`  (B332)

Let `g = [[0,−1],[1,−1]]` — the order-3 element (`g³ = I`) that cyclically permutes the three Eisenstein-conjugate
Riley generators, i.e. the ℤ/3 that permutes generations (B324/B326). Then, exactly:

```
g = −R·L⁻¹        and       g⁻¹·R = −L .
```

So the generation element is the **signed ratio** of the two letters, just as the monodromy `A = RL` is their
**product**. The two simplest length-2 words in `R, L` are the two ends:

| combination | matrix | trace | disc(charpoly) | field | end |
|---|---|---|---|---|---|
| **product** `R·L` | `[[2,1],[1,1]]` | 3 | **5** | `ℚ(√5)` | golden → 2I → **E₈** (monodromy/ambient) |
| **ratio** `−R·L⁻¹ = g` | `[[0,−1],[1,−1]]` | −1 | **−3** | `ℚ(√−3)` | Eisenstein → 2T → **E₆** (gauge + generations) |

*(Provenance:* B332; the two-ended structure is B248/​[[two-ended-unification-and-wall-map]]; the McKay assignments
`√5→2I→E₈`, `√−3→2T→E₆` are standard, B315/​B266.) The E₆ end (the ratio) internally carries **both** the gauge center
`ℤ/3` (Level 3) and the commensurator generation `ℤ/3` (Level 4); both are Eisenstein.

---

## 3. The four levels (K020, recalled)

| Level | locus | symmetry | ℤ/3? | determines |
|---|---|---|---|---|
| 1 | object (the complement) | `D₄`, order 8 | no | the amphichiral `ℤ/2` (CP-sign existence) |
| 2 | seam (cusp torus) | `ℤ/2 × ℤ/2` | no | two internal values (CP sign, scale `k=3`) |
| 3 | E₆ character variety | E₆ center `ℤ/3` | **yes** | democratic Yukawa, the cascade |
| 4 | commensurator `PGL(2,𝒪₋₃)` | Eisenstein-unit `ℤ/3` | **yes** | generation multiplicity |

The gauge structure (Level 3) and the generation count (Level 4) both flow from the `√−3` end = the ratio `g`.

---

## 4. The 27, the generations, and the democratic Yukawa

At E₆ the matter multiplet is the **27**. Under the arithmetic `2T ↪ E₆` (B329):

- **`27|₂T = 3·1 ⊕ 3·1′ ⊕ 3·1″ ⊕ 6·3`** (principal / quaternionic embedding) — it factors through `2T/{±1} = A₄`.
- The generation ℤ/3 mixes the three copies by an **ω-circulant** `M = α·J + ω·P` with `β−α = ω` exactly (B324) —
  eigenvalues `(2√13, 1, ω²)`: **one heavy, two light of equal magnitude** (the "democratic Yukawa": `|1| = |ω²| = 1`).

The two light generations are **degenerate in magnitude but differ in phase** (`arg 1 ≠ arg ω²`). Whether that phase
degeneracy can be lifted at E₆ — i.e. whether the mass **hierarchy** is computable from the character variety alone — is
the wall.

---

## 5. Why the hierarchy is Level 4 (the phase cannot be split)  `n₁ = n₂`

Write the ω- and ω²-multiplicities of the 27 at the generation element as `n₁, n₂`. The hierarchy splits (Level 3) iff
`n₁ ≠ n₂`; it stays degenerate (Level 4) iff `n₁ = n₂`. The verified chain:

1. **B327/B329.** For the natural embeddings — quaternionic `SU(2)` *and* complex `SU(3)` (trinification) — `n₁ = n₂`.
   (Trinification looks like it could split, but the 27's balanced `3/3̄` pairing restores reality; non-vacuity: the
   `SU(3)` `3`|₂T is genuinely complex, `−1±√3i`.)
2. **B331 (the clean reason).** The generation element `g` is **elliptic and ambivalent**: eigenvalues `{ω,ω²}` are
   inverse-closed, so `g ~ g⁻¹`, so `χ₂₇(g)` is **real in every representation** — compact *or* holomorphic. The
   proposed `SL(2,ℂ)` (non-self-dual/holomorphic) escape **fails at its root**: holomorphicity is invisible at a
   finite-order element (the holomorphic and compact characters of `g` coincide, both `0`); it only distinguishes
   *loxodromic* (infinite-order) elements — which carry volume/CS, i.e. **structure**, not the finite ℤ/3 that would
   split the **phase**.
3. **B326.** The generation ℤ/3-breaking datum is **finite congruence torsion** `H₁(3-fold cover of 4₁) = ℤ ⊕ (ℤ/4)²`,
   with the deck ℤ/3 acting irreducibly (char poly `Φ₃ = Δ mod 4`, since `−3 ≡ 1 mod 4`). Finite/abelian data gives
   **texture** (selection rules), never a continuous **magnitude**.

So the mass hierarchy is **not** in the single object's E₆ data. It is a Level-4 (commensurator) datum. This is a
theorem-shaped conclusion, not a limitation: the finite generation symmetry is the wrong (elliptic) kind of complex.

---

## 6. What the wall is made of — the seam `ℚ(√−15)`  (B332–B334)

The two ends live in `ℚ(√5)` and `ℚ(√−3)`, which share only `ℚ`. A physical **value** would be an element of their
compositum `ℚ(√5,√−3)` — biquadratic, `Gal = ℤ/2×ℤ/2`, with three quadratic subfields `ℚ(√5)`, `ℚ(√−3)`, and the
**seam** `ℚ(√−15)` (`√5·√−3 = √−15`, ramified at `15 = 3·5`, the two ends' own primes).

- **B334 (a theorem, verified).** `H(ℚ(√−15)) = ℚ(√5,√−3)`: the seam's **Hilbert class field is the two-ended
  compositum**. The seam has class number 2 (arithmetic *incomplete*); its completion — where every ideal becomes
  principal — *is* the two ends. **The object completes its own seam.** (Verified by the splitting law: a split prime is
  principal ⟺ `p ≡ 1,4 mod 15`, non-principal ⟺ `p ≡ 2,8 mod 15`; cross-checked against the form `x²+xy+4y²`.)
- **B333 (the null test).** Yet the seam's **intrinsic** arithmetic is **generic**: `h(−15)=2` is shared by 14 fields to
  `−400`, units `{±1}`, ramification tautological. So `ℚ(√−15)` is distinguished **relationally** (its HCF is the two
  ends) but generic **intrinsically** — **no value falls out of it.** The tempting `137 ≡ 2 (mod 15)` (non-principal)
  observation is **dead**: `≈ 0.556` of split primes are non-principal (that is what `h=2` means) — a coin flip.

**The synthesis.** `ℚ(√5,√−3)` is *abelian* over `ℚ`, hence class-field-theoretic, hence **finite congruence data** —
the same finite data B326 found as `(ℤ/4)²`. Finite/abelian arithmetic gives **texture, never magnitude**. A magnitude
(the hierarchy) is real and **transcendental** — it lives in the object's *volume*, on the structure side. **The value is
the product of a real-transcendental magnitude and a finite-complex phase — an operation the single object declines to
perform.** That product is the Level-4 relation, external to the object.

---

## 6a. The symmetry-broken sector — structure ⊕ value, and the flow  (B336–B338)

The single object is *symmetric* (amphichiral ℤ/2, generation ℤ/3), which forces the structure and forbids the value.
We probed the **symmetry-broken** sector directly:
- **The value's home is doubly separated (B336).** The value would live in the imaginary seam `ℚ(√−15)`; the amphichiral
  object is real (`J_N(4₁;ζ₁₅)` is real → zero `√−15`), and the chiral routes to `√−15` are *provably closed* — the
  monodromy discs `{t²−4}` never hit `−15`, and every commensurable neighbour shares `ℚ(√−3)` (Bianchi `O₋₃`) while
  `√−15` is a *different* Bianchi group `O₋₁₅`. With B333 (`√−15` arithmetically generic), `√−15` is *generic in
  arithmetic and not a geometric invariant* — it is only the abstract compositum (B334).
- **Structure ⊕ ordering (B337).** A symmetric configuration (shared `ℚ(√−3)`, ℤ/3) gives E₆ + a **democratic**
  spectrum `{52,1,1}`; distinct seeds (`m=1,2,3`, fields `ℚ(√−3), ℚ(i), deg≥4`) give an **ordered** spectrum
  `{10.2,−4,−0.2}` but **no shared E₆**, and `{1,2,3}` is not even forced (arithmeticity selects `{1,2}`). The **same**
  symmetry that forces the structure forbids the ordering: **no static configuration has both.**
- **The bridge is a flow, externally parametrized (B338).** The object *contains* a flow — Dehn filling `(1,n)` from the
  symmetric cusp (`CS=0`, amphichiral) to broken/chiral configs, chiral order parameter **`CS ~ −1/(2n)`** — but the
  flow's *parameter* (the slope = the vacuum) is external. So structure⊕value is *bridged* by a flow the object contains,
  yet the value is **selected** (by the filling choice), **not forced**. (Reunification reading, firewalled:
  `../speculations/S047`.)

The upshot: the firewall holds not by our stopping but by *theorem* — the object is the moduli space of symmetry-
breakings; which breaking (which value) is realized is the external, physical selection.

## 7. The firewall, stated exactly

*The object forces the **form** of physics and never its **values**.* Mechanized as a Galois theorem (K020): every
discrete invariant examined is a symmetrizable Galois orbit or a canonical object (B330, five classes sealed,
conditional). Confirmed empirically by a null test (B322, `p≈0.5`). This document adds the arithmetic anatomy: **the two
ends never take their product; the seam that would hold the product is generic; the value lives only in the relation.**
Nothing here crosses to `CLAIMS.md`.

---

## 8. What a specialist would need (the open gates)

The remaining gates are in `docs/OPEN_PROBLEMS.md`:
- **B — the CRUX `T[4₁;E₆]`** and its hierarchy sub-atom: the Level-4 commensurator geometry (the `(ℤ/4)²` torsion +
  the volume) is where the value would be assembled; needs the exceptional 3d-3d state integral and the Bianchi-group
  computation. (The overlap index `[Γ:Γ∩gΓg⁻¹]`, reported as 3, is **not yet verified** — B332.)
- **A — S032-A**: the all-invariants no-forced-choice theorem (B330 is the conditional five-class version).
- **C — multiplicity → generations**; **D — the non-Hermitian Damanik–Gorodetski spectral theorem.**

**Provenance index.** Axiom→letters: P000–P005, K010. Identity: **B332**. Two ends: B248, B315, B266. Levels: **K020**.
27/circulant: **B324**, **B329**. Hierarchy = Level 4: **B326**, **B327**, **B329**, **B331**. Seam: **B332**, **B333**,
**B334**. Firewall: **B322**, **B330**, K020. Meditation: `speculations/S046`.
