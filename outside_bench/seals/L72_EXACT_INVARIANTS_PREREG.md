# SEAL — L72: the level-2 invariants exactly, and what the uniqueness residual actually gates

**Sealed before the certificate was written. No prototype run. No priors declared except
where stated.**

Memo 211 left L72 with one residual, the cell's own words:
*"uniqueness-up-to-gauge of the level-2 F-symbols (constructed + verified, **not
classified**)."* Memo 211 closed the **Galois** half of it. This seal asks two things the
bench can settle without the literature: **what the residual actually gates**, and **what
the cell's reported invariants are exactly.**

## The object

`P2W5-L72`'s section [D] reports the E₆ level-2 colored invariants of 4₁ as floats:
`N=1 → 1.0`, `N=3 → 2.0881460000204`, `N=5 → −0.6920214716301`, computed by Habiro's closed
form at `q = ζ₇`:

> `J_N(q) = 1 + Σ_{k≥1} Π_{j=1}^{k} ( q^N + q^{−N} − q^j − q^{−j} )`

(the cell's loop runs to `k = N`; the `j = N` factor is identically zero, so the tail
vanishes and the sum is the standard one — asserted as a control below).

## CELL 1 — the exact values

**Observed:** `J_N(ζ₇)` for `N = 1, 3, 5` as **exact** elements of `ℤ[ζ₇] = ℤ[x]/Φ₇(x)`,
each one's minimal polynomial over ℚ, and the degree of the field it generates.

- **Outcome A:** all three lie in the **real subfield** `ℚ(ζ₇)⁺`, degree 3 over ℚ.
- **Outcome B:** at least one does not.

## CELL 2 — do the exact values match the cell's floats?

**Observed:** the numeric evaluation of the exact values against
`1.0`, `2.0881460000204`, `−0.6920214716301`.

- **Outcome A:** agreement to the printed precision.
- **Outcome B:** disagreement.

## CELL 3 — does the uniqueness residual reach any reported number?

**Observed:** whether `J_fig8` consumes any F-symbol or associator input, and whether any
other quantity stored in the cell's `results.json` is computed from the constructed 6j
rather than from the modular data `(S, T)`.

- **Outcome A:** no reported number depends on the F-symbols — the residual is real as a
  *categorical* statement and **inert** for everything the cell reports.
- **Outcome B:** at least one reported number depends on them, and the residual bites it.

## CELL 4 — is `ℚ(ζ₇)⁺` the object's own charge field `K`?

`K = ℚ[x]/(x³ − 12x − 5)` is the field memo 204 identified as the object's trialitarian `L`.
A reader may hope the level-2 invariants land in it.

**Observed:** the discriminant and Galois type of each field — for `K`, `disc = 6237` with
squarefree part `77` (non-square ⇒ `S₃`); for `ℚ(ζ₇)⁺`, computed here.

- **Outcome A:** the two are **not** isomorphic, and the Galois type is the obstruction.
- **Outcome B:** they are isomorphic.

**Declared prior for CELL 4 only: Outcome A** — memo 204 established `K` is non-cyclic with
`|Aut(K/ℚ)| = 1`, and a real cyclotomic field is cyclic; the cell exists to compute both
sides rather than assert the mismatch.

## Controls

- **C1** — Habiro's form must reproduce the **Jones polynomial of 4₁** at `N = 2`:
  `q² − q + 1 − q⁻¹ + q⁻²`, exactly, in `ℤ[q, q⁻¹]` (the cell ran this control numerically at
  a generic value; it is run **exactly** here).
- **C2** — the tail-vanishing claim: the `j = N` factor of Habiro's product is identically
  zero, so extending the sum past `k = N − 1` changes nothing. Asserted exactly.
- **C3 — MB12.** The minimal-polynomial routine must be able to return a degree **other
  than 3**: run on `ζ₇` itself it must return **6**, and on a rational it must return **1**.
  If it cannot, CELL 1 may not be read (memo 164).

## Interpretation is not preregistered

Per bench rule #21 the outcomes state only what is observed.
