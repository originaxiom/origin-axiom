# K015 — The SU(2)_k eigenvalue field content is quantum-group arithmetic (word composition mod 4)

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof.
>
> **⚠ CORRECTION (B133/V122).** This doc originally claimed a *chirality–arithmetic connection* ("chirality shifts the
> eigenvalue arithmetic: achiral → ℚ(√−3), chiral → ℚ(ζ₁₂)"). **That headline is withdrawn** — it was a sampling
> artifact (chirality was confounded with the word's spin-content mod 4). The eigenvalue *orders* are correct; their
> *attribution to chirality* was wrong. The corrected statement is below; the dead claim is tombstoned `K-H`
> (`../speculations/TOMBSTONES.md`), and the guard is `MB6` (`../REPRODUCIBILITY.md`: reproduction ≠ interpretation —
> run the control). The filename is kept (historical) to avoid dangling cross-references.

## The setting

On top of the classical character-variety picture (the metallic once-punctured-torus bundles `M_m`, their trace
fields, the chirality recursion `K011`, the two-seed fork `K014`) sits a **quantum layer**: the SU(2)_k
Witten–Reshetikhin–Turaev data `Z_k`. At level `k` the modular `(S,T)` data of SU(2)_k gives a `(k+1)`-dimensional
representation of the once-punctured-torus mapping class group (`R=T` the Dehn twist, `L=S T S⁻¹`); a metallic word maps
to the ordered product, and `Z_k` is its trace. All eigenvalues of `ρ_k(word)` are roots of unity, so each generates a
cyclotomic field: an eigenvalue of **order d** lies in `ℚ(ζ_d)` — order 6 or 3 → ℚ(√−3), order 4 → ℚ(i), order 12 →
ℚ(ζ₁₂)=ℚ(√−3,i), order 1 or 2 → ℚ. This **eigenvalue-order method** is exact and precision-independent.

## The corrected result: the field content is quantum-group arithmetic, not chirality (B132, B133)

The cyclotomic field of `ρ_k(word)`'s eigenvalues is controlled by the **word's spin-content mod 4** — the SU(2)_k
T-matrix twist `exp(·πi/4)`, which contributes order-4 (ℚ(i)) eigenvalues exactly when the relevant spin-content is
`≡ 2 mod 4`. This is **quantum-group arithmetic**, a property of the *word composition*, present in **achiral and
chiral words alike** — **not** a chirality property and **not** a manifold property.

**The decisive control (B133, `is_amphicheiral`-verified at k=4):** among **achiral words alone** the field ranges over
**all three** values —

| word (all achiral) | field | `|Z|` |
|---|---|---|
| `RRLL` | ℚ(ζ₁₂) | 1.880 |
| `RRRLLL` | ℚ(√−3) | 2 |
| `RLRLRL` | ℚ (rational) | 5 |
| `RRLRLL`, `RLRRLL` | ℚ(ζ₁₂) | **0 (vanish)** |

So chirality does **not** determine the field, and the **k=4 vanishing is also not chirality-linked** (achiral words
vanish too). The single-seed pattern (`m ≡ 2 mod 4` → ℚ(i) content, e.g. m=2,6) is the same quantum-group mechanism.
The classical trace fields remain **disjoint** (ℚ(√−3) ∩ ℚ(i) = ℚ; the located-ness of B125/B129 is untouched) — there
is no genuine *fusion* of the classical fields; "ℚ(ζ₁₂)" is the cyclotomic field of the *quantum* eigenvalues, which
already live in ℚ(ζ₁₂) before any word is formed.

## Why the original reading was wrong (the method lesson, `MB6`)

The original S7 sample correlated chirality with word-length parity (the chiral examples happened to be the ones whose
spin-content hit `2 mod 4`). The numbers reproduced exactly — but **reproduction is not interpretation**. The required
guard, not run before banking: vary the claimed cause (chirality) while holding the confound (quantum-group inputs /
the R,L multiset) fixed. The control above does exactly that and breaks the correlation immediately. This is the
*third* recurrence of this "field-fusion" artifact across sessions; it is banked firmly (`K-H`, `MB6`) so it is not
re-reported.

## What stands

The quantum layer's *robust* facts are the **single-seed** ones (`K016`): pure phase `|Z_k|=1` is m=1-unique (`S3a`);
`Z_{k=4}(M_1)=ω` (`S1a`); the vanishing period `=|O_K^×|/2` for arithmetic m (`S2`); two scales by m mod 4 (`S4`). And
the **Lee–Yang** identification (`S030`/`K010`, B132/S8): at k=3 the σ₃ Galois conjugate gives `d_τ=−1/φ` (M(2,5)). The
*chirality* readings (field shift, vanishing fragility) are withdrawn.

**Prior art (B134/V123 novelty audit, R3): this is standard quantum topology.** The cyclotomic field content of WRT
SU(2)_k invariants is a known fact: **Jeffrey 1992** (CMP 147 — torus-bundle `Z=Tr ρ(U)` is an explicit Gauss sum,
cyclotomic content set by `Tr U ∓ 2` and level `k+2`); **Dong–Lin–Ng 2015** (the modular rep is ℚ(ζₙ)-rational, kernel
a congruence subgroup of level `n=ord(T)`); **Lawrence–Zagier 1999** (WRT in ℚ(ζ), Galois-equivariant). The
spin-content-mod-4 → ℚ(i) statement is a corollary-level refinement of these. We **cite**, claim nothing novel.

**Anchors:** B132/V121 (the eigenvalue layer + the validated convention), **B133/V122 (the correction + the control)**,
**B134/`../docs/NOVELTY_AUDIT.md` (the R3 prior art)**, `K011`/B128 (the chirality recursion — classical, *separate*
from the quantum field content), `K014`/B131 (the two-seed fork), `K010`/`S030` (Lee–Yang), `K016`,
`../speculations/TOMBSTONES.md` (`K-H`), `../REPRODUCIBILITY.md` (`MB6`). External: SU(2)_k modular tensor category;
**Jeffrey 1992; Dong–Lin–Ng 2015; Lawrence–Zagier 1999**; Reshetikhin–Turaev; Lee–Yang / M(2,5).
