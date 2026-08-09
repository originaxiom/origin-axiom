# B1006 — PREREGISTRATION: is the object's own spectral value algebraic?

**SEALED BEFORE COMPUTE. 2026-08-09.** Nothing below written after seeing a result.

## P0 — the quantifier

Computes over **m004's own second Maass cusp-form spectral parameter**, `r`, banked to **25 decimal
places** by B922. **B922 states it is NOT INHERITED from the parent Bianchi group** — so this is an
**object-level** quantity, which is the address **B993** left open when it showed the trace-field
route is class-level.

## Why now, and why this was never a real test before

**B798** established the exclusion law: PSLQ needs **N ≈ 1.43·d·log₁₀(H)** digits. The programme's
earlier spectral test ran at **8 digits**, which B798 says *"excludes essentially nothing"* — so its
"51st percentile of random spectra" was **absence of evidence, not evidence of absence.** The
instrument had no power.

**B922 delivered 25 digits.** The envelope that precision supports, computed from B798's law and
**fixed here before any run**:

| height bound H | max degree d testable at 25 digits |
|---|---|
| 10² | **d ≤ 8** |
| 10³ | **d ≤ 5** |
| 10⁵ | **d ≤ 3** |
| 10⁷ | **d ≤ 2** |

**No cell may exceed its row.** Exceeding it manufactures spurious relations from noise, which is
precisely the failure B798 named.

## The values (banked, B922)

    r      = 4.9000853730625213014795758        (25 dp)
    lambda = 1 + r^2 = 25.0108366633012685587659

## The cells — fixed here

- **A — r over ℚ.** Integer relation among 1, r, …, r^d within the envelope.
- **B — λ over ℚ.** Same, on λ = 1 + r².
- **C — r over the object's own fields.** Relations with **φ**, **√5** (hearing) and **√3**
  (the real trace of the being field), within the envelope.
- **D — r against the object's canonical constants.** Relations with **Vol(4₁) = 2.029883212819307…**
  and **π**, within the envelope.

## THE CONTROL — run FIRST, and the cell is void without it

**MB12, and B798's lesson made mechanical.** At the *same* precision and envelope:

1. **Positive control** — run on **φ** and **√5**, which *are* algebraic of degree 2. **The
   instrument must FIND them.** If it does not, it has no power and every null is meaningless.
2. **Negative control** — run on **π** and **e**, not algebraic of low degree. **The instrument must
   find NOTHING.** If it "finds" a relation, the envelope is too loose and the run is void.

**Both controls must pass before any cell result is read.**

## The two outcomes

- **OUTCOME A — a relation fires and survives the controls.** The object's own spectral value is
  algebraic over something nameable. **That is a number, it is object-level, and a shared
  classification cannot produce it.** *It is NOT thereby an SM ratio — it is a mathematical fact
  about the object, and the arc will say so.*
- **OUTCOME B — nothing fires and the controls pass.** **The first INFORMATIVE null in the value
  layer.** Every previous one was underpowered. A genuine exclusion at d ≤ 8, H ≤ 10² is a
  structural fact: the object's own spectral value is **not** low-degree algebraic.

**Both are results. There is no null-of-the-null.**

## THE DECLARED PRIOR

> **OUTCOME B is expected.** Maass eigenvalues are conjecturally transcendental and no arithmetic
> reason is known for r to be algebraic. **This cell is expected to produce an informative negative,
> not a discovery.** Recorded so that an Outcome A, if it comes, is worth something.

## What would make this cell INVALID

- exceeding the declared degree/height envelope for the precision · running a cell before the
  controls pass · adding a constant to cells C/D after seeing a near-miss · reporting a relation
  whose residual is not below the precision floor · treating a found relation as an SM claim.
