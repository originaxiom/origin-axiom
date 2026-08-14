# B910 — L3: the Kummer class of the compact-pencil cubic κ — [α_κ] = [α_μ]: the compact wall-cubic is the SAME Knus–Paques element as the charge cubic

**Date:** 2026-08-05 · **Seat:** computation subagent (for cc banking) · **Status:** BANKED — exact (six symbolic cube certificates + exact non-cube witnesses); local scans as discovery only

## The question (register item L3)

The solo seat's compact campaign produced a fourth cubic with resolvent
ℚ(√77): κ, the compact-pencil wall cubic (ν(s) = c·κ(s)⁶, constant term
−19³, disc kernel {7,11}), whose field is the SAME cubic field K = ℚ[ρ]/μ
as the charge cubic (the One-Field theorem, κ splits [1,2] over K). B902
placed the three noncompact cubics in the Knus–Paques group of cubic
algebras with resolvent ℚ(√77): [α_gen] = [α_μ], [α_vac] = [α_μ]⁻¹. L3
asks: where does κ sit, and what is the full multiplication table of the
four classes in F*/(F*)³, F = ℚ(√77, √−3)?

Same field forces [α_κ] ∈ {[α_μ], [α_μ]⁻¹} — but which branch, under the
one fixed convention (positive s = √(disc/77), α = (−27q + 3s√−231)/2), is
a genuine computation: it decides whether the compact wall-triple carries
the charge orientation or the vacuum orientation.

## The rebuild (verified from scratch, exact)

From B854's exact e6 machinery: the compact pair's pencil g14 + s·g22 on
the 18-dim core/floor quotient (core 30, floor 12, quotient 18 — asserted);
ν(s) = det, 20-point exact interpolation (degree 18 = 18 asserted, the §LV
aliasing lesson honored); primitive factorization gives ν = c·κ⁶ exactly,

- **κ(s) = 2771822592000·s³ + 3033676800·s² − 56402640·s − 6859**,
  irreducible over ℚ (the exact rational scalar c is recorded in
  `results.json` under `kappa.nu_scalar_c`; ν = c·κ⁶ asserted by exact
  expansion),
- constant term **−6859 = −19³** ✓, disc = 2²⁸·3¹⁰·5⁶·7³·11·19¹²,
  squarefree kernel **{7,11}** ✓ (resolvent ℚ(√77), the six-cubic law),
- **[1,2] split over K certified exactly**: the root
  s\*(ρ) = −4997/1257360 − (198911/68107)ρ + (560387520/885391)ρ²
  satisfies κ(s\*(ρ)) ≡ 0 mod μ(ρ) (polynomial remainder, exact).

## The Kummer elements (B902 construction, regenerated + new)

α = (−27q + 3s√−231)/2 from the monic depressed cubic; 4-vector arithmetic
over (1, √77, √−3, √−231):

| cubic | α | note |
|---|---|---|
| μ | 13⁶·(1/25443808051200 + √−231/299873452032000) | regenerated = B902 |
| generic | (4933932225386250240000 + 418636673669136384000·√−231)/13³ | regenerated = B902 |
| vacuum | (−39471457803090001920000 + 3349093389353091072000·√−231)/13³ | regenerated = B902 |
| **κ** | **19⁶·(−1/690594465792000 + √−231/1470297894912000)** | NEW |

The numerator law transfers: α_μ carries 13⁶ (noncompact prime), α_κ
carries 19⁶ (compact prime).

## The theorem (exact certificates)

Local scans (8 clean primes p ≡ 1 mod 3, 77 and −3 QRs, coprime to all
denominators; all four embeddings; twist set ζ₆ᵃε₇₇ᵇ) for discovery; every
positive is proved by symbolic cubing, every negative by an explicit
χ₃-witness at a split prime (a ring-hom certificate: cubes land on cubes).

1. **α_μ / α_κ = γ₃³** with
   **γ₃ = (1+√−3)·(5239/48013 − (5239/192052)·√−231)**
   (5239 = 13²·31, 48013 = 7·19³) — verified by exact symbolic cubing.
2. **α_vac · α_κ = γ₄³** with
   **γ₄ = (1+√−3)·(−1247616/403 − (311904/403)·√−231)** (403 = 13·31) —
   verified likewise.
3. **α_gen / α_κ = γ₅³** with
   **γ₅ = (1+√−3)·(2217458073600/89167 − (554364518400/89167)·√−231)**
   (89167 = 13·19³) — found by direct reconstruction AND equal, as an
   exact 4-vector, to the composition γ₂γ₃/γ₁ from the regenerated B902
   certificates γ₁ (α_μ·α_vac), γ₂ (α_gen·α_vac) — a cross-check that the
   certificate system is internally consistent.
4. Control, regenerated + upgraded: **α_μ / α_gen = (2197/500716339200)³**
   — the direct certificate B902's reconstruction missed is the plain
   rational **const(μ)/lead(μ)** (13³ over μ's leading coefficient);
   α_μ·α_vac = γ₁³, α_gen·α_vac = γ₂³ reproduce B902 digit-for-digit.
5. α_μ·α_κ, α_gen·α_κ, α_vac/α_κ: **non-cubes at all 9 twists** (exact
   χ₃-witnesses recorded per twist in `results.json`), and each α
   individually is a non-cube at all 9 twists — no class is trivial.

> **[α_κ] = [α_μ] in F*/(F*)³, with NO unit twist — under the one fixed
> sign convention the compact wall-cubic sits in exactly the charge
> cubic's Kummer class, not the vacuum's. The One-Field theorem sharpens
> to a one-CLASS theorem: compact and noncompact walls are the same
> element of the Knus–Paques group, same orientation. Consequently
> vacuum ⊕ κ = split — the vacuum field annihilates the compact cubic
> exactly as it annihilates the charge cubic.**

### The multiplication table of the four classes (C := [α_μ], group ℤ/3)

Assignments: [α_μ] = [α_gen] = [α_κ] = C, [α_vac] = C² = C⁻¹, C ≠ 1.

| · | α_μ | α_gen | α_vac | α_κ |
|---|---|---|---|---|
| **α_μ** | C² | C² | 1 | C² |
| **α_gen** | C² | C² | 1 | C² |
| **α_vac** | 1 | 1 | C | 1 |
| **α_κ** | C² | C² | 1 | C² |

Every off-diagonal entry is certified (cube certificate where 1, exact
non-cube witness where C or C²); the table is asserted consistent with
every scan in the script.

### Structural note on the certificates

Every certificate is ζ₆-twisted-Kummer: γ = ζ₆ᵉ·(element of ℚ(√−231)),
e ∈ {0,1}. The same-orientation ratio μ/gen is untwisted and rational
(e = 0); the annihilations (μ·vac, gen·vac) are 2ζ₆·rational (B902); the
cross-pencil certificates (μ/κ, gen/κ, vac·κ) are 2ζ₆ times an
IRRATIONAL element of ℚ(√−231) — the compact/noncompact identification
is witnessed one level deeper in the Kummer quadratic, never needing
√77 alone. The prime 31 — present in κ's leading coefficient
2¹⁴·3⁴·5³·7²·11·31 and absent from μ's — appears in every κ-certificate
(5239 = 13²·31, 403 = 13·31, 2217458073600 = 2¹⁶·3⁴·5²·7²·11·31).

### Methodological note

B902's `cube_reconstruct` rationalized through float64 with denominator
cap 96; the κ certificates have denominators 7·19³ and 13·19³, invisible
at that precision (this is why B902 recorded the μ/gen ratio survivor
with no direct certificate). B910 reconstructs at 80 dps via
`limit_denominator(10⁹)`: all six cubes now carry DIRECT certificates.
Every positive remains gated on exact symbolic cubing, so the change
widens discovery only, never proof. Scans: 32 clean embedding-tests per
pair (8 primes × 4 embeddings), runtime 86 s total.

## Files

- `kappa_class.py` → `results.json` (the rebuild, the split certificate,
  alphas, scans with witnesses, the six cube certificates, the table)
- `independent_check.py` — re-verifies γ₃, γ₄ and one non-cube witness
  through sympy radical arithmetic (no shared code with the 4-vector
  algebra of `kappa_class.py`)

## Depends on

B854 (exact e6 + ADS), B866 (μ), B888 (the two weight cubics), B902 (the
construction + γ₁, γ₂, regenerated here), solo ledger §LV–LVI (κ, the
One-Field theorem — both re-verified from scratch here).

## Registered follow-up

The Galois bijection ρᵢ ↔ s\*ᵢ (exact s\*(ρ) now in hand) against the
class identity: does the wall-to-wall matching preserve the Kummer
orientation (the triality-echo question from ledger §LVI GEO)?


## Banking-seat verification (cc, 2026-08-05)

The agent's independent check path (`independent_check.py` — sympy radical
arithmetic sharing no code with the 4-vector algebra) re-run at banking:
γ₃³·α_κ = α_μ TRUE, γ₄³ = α_vac·α_κ TRUE, the p = 37 χ₃ witness confirmed.
results.json regenerated clean (the exec-contamination of run 1 diagnosed by
the agent itself and fixed). The One-Class theorem stands:
**[α_μ] = [α_gen] = [α_κ] = C, [α_vac] = C⁻¹** — and the numerator law
(13⁶ on the noncompact side, 19⁶ on the compact side) is banked as structure.
