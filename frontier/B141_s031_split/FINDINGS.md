# B141 — split S031: the φ-fixed tower is REDUCIBLE (Q₈ finiteness), the φ²-geometric tower is IRREDUCIBLE (V130)

Third reconciliation pass on S031, one layer past B140, and a substantive correction to B140's reframe. The
conceptual root of the φ-vs-φ² distinction is **finiteness vs density of the SL(2) image.** All re-derived
in-sandbox (sympy-exact + a numeric search). MATH tier; firewalled; nothing to `CLAIMS.md`; P1–P16, B85, the merged
B124–B140 untouched. **B129's banked conclusions are preserved** — a framing / object-identity correction.

## Item 1 (RIGOROUS, all n) — the principal φ-fixed point is REDUCIBLE at every SL(n), n≥3

The unique **irreducible** SL(2) φ-fixed point is `(0,0,0)` (κ = tr[A,B] = −2 ≠ 2; the other fixed point `(2,2,2)`
is reducible). Its representation is the **quaternion group Q₈**: `A = diag(i,−i)`, `B = [[0,1],[−1,0]]` ⟹
`A² = B² = −I`, `AB = −BA` (verified; the group generated has **order 8**). Q₈ is **finite** with irrep dims
`{1,1,1,1,2}` (Σ dim² = 8), **max irrep dim 2**. So the principal `Sym^{n−1}` image (dim n) is **reducible for all
n ≥ 3**. Verified algebra-dim table (`⟨Sym^{n−1}A, Sym^{n−1}B⟩` vs n²):

| n | Sym^{n−1} | alg dim | n² | |
|---|---|---|---|---|
| 2 | Sym¹ | 4 | 4 | **irreducible** |
| 3 | Sym² | 3 | 9 | reducible (`χ_a⊕χ_b⊕χ_c`) |
| 4 | Sym³ | 4 | 16 | reducible |
| 5 | Sym⁴ | 4 | 25 | reducible |
| 6 | Sym⁵ | 4 | 36 | reducible |
| 7 | Sym⁶ | 4 | 49 | reducible |

Character cross-check: `χ_{Sym²V} = (3,3,−1,−1,−1) = χ_a + χ_b + χ_c` on classes `(1,−1,i,j,k)` (verified). **So
there is no irreducible principal φ-fixed point anywhere in the tower (n≥3)** — SL(2) is the only level where it is
irreducible. *This corrects B140's "rigidity of the principal irreducible fixed point": there is nothing irreducible
to be rigid about.*

## Item 2 (RIGOROUS, all n) — the φ²-geometric tower is IRREDUCIBLE at every SL(n), in ℚ(√−3)

The figure-eight φ²-geometric holonomy (B129's S1a object, `principal_sl3_rep()`): `A = [[1,1],[0,1]]`,
`B = [[1,0],[−ω,1]]`, `ω = ½ + ½√−3` — **Zariski-dense** in SL(2,ℂ). `Sym^{n−1}` stays irreducible: verified
**alg dim = n² for n = 2..5**, all word-traces in ℚ(√−3).

## Item 3 (SOLID) — the structural key: finiteness vs density

The Q₈ image is **finite** (order 8); the fig-8 image is **infinite** (`A^k = [[1,k],[0,1]]`, unbounded). **Finite
image ⟹ reducible tower; dense image ⟹ irreducible tower.** This is the conceptual root of the φ-vs-φ² distinction —
the same split as `det = −1` (φ, discrete fixed points) vs `det = +1` (φ² = RᵐLᵐ, hyperbolic bundle), one level
down. S031's original clause "fixes only the `Sym^{n−1}` image, trace field ℚ(√−3)" took *irreducibility + ℚ(√−3)*
from the φ² (dense) object and *"fixed point"* from the φ (finite) object — **no single object has both.**

## Item 4 (STRONG EVIDENCE / CONJECTURE, open n≥4) — the SL(3) φ-fixed locus appears entirely reducible

Item 1 kills the *principal* irreducible φ-fixed point; the remaining question is whether any **non-principal**
irreducible φ-fixed point exists. An intertwiner search (converges, unlike B129's saddle-flee): the φ-fixed
condition `gAg⁻¹ = AB, gBg⁻¹ = A` reduces to `A g⁻¹ A g = g A g⁻¹` with `B = g⁻¹ A g`; fix `A = diag(1,−1,−1)`,
solve for `g`, classify `⟨A,B⟩` by algebra dim. **Result: 60/60 converged, 0 irreducible** (this probe) — consistent
with the handoff's 150/150. **Conjecture:** the SL(3) φ-fixed locus is entirely reducible (no irreducible φ-fixed
point, principal or not). Item 1 is rigorous; "entirely" is **strong evidence, finite-sample, not a proof**, open
n≥4. Necessary condition at any φ-fixed point: `A ~ B ~ AB` (mutually conjugate; SL(2) analogue `x=y=z`). The
rigorous path is symbolic elimination of the φ-fixed system (the same target as the SL(4) elimination route).

## The split (what S031 becomes)

- **S031a (φ-fixed / trace-map automorphism):** the φ-fixed tower is **reducible** — principal reducible ∀n≥3
  (rigorous, Q₈ finiteness); full SL(3) locus **entirely reducible** (conjecture, open n≥4). Firewall-aligned:
  **reducible × discrete** (tighter than B140's "rational").
- **S031b (φ²-geometric):** `Sym^{n−1}` of the figure-eight holonomy — **irreducible ∀n, in ℚ(√−3)** (rigorous,
  dense image; = B129's S1a; the HMP-adjacent object, 1505.04451).

**B129 preserved:** "0 escapes from ℚ(√−3)" holds (φ-fixed traces rational ⊂ ℚ(√−3); S1a's φ² Sym² in ℚ(√−3)).

## Reproduce

```
python frontier/B141_s031_split/probe.py
python -m pytest tests/test_b141_s031_split.py -q
```

Items 1–3 are sympy-exact (rigorous, unconditional); Item 4 is a seeded numeric search (no Sage).

**Tier.** MATH. Splits `speculations/S031` (S031a φ-reducible / S031b φ²-irreducible), calibrates `knowledge/K012`,
adjusts `frontier/B140` FINDINGS. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B140 untouched; B129's conclusions
stand. Ledger **V130**.

**Anchors:** B140 (the reframe this adjusts), B129/`K012` (S1a = the φ²-object; the m=1 sealing), B138 (the principal
Sym lemma; `sym_power`), B71 (the φ² geometric components), `K003`/`K005` (the principal Sym tower). External:
quaternion group Q₈ character table; Heusener–Muñoz–Porti 1505.04451 (the SL(3) figure-eight character variety).
