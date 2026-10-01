# B1432 — THE THREE-FOLD COVER FIRES OFF THE LIFT: the SM lane's level census verified on main with independent code, and B1427's "Y₃: 0 firing" scoped to what its scan could reach

cc, 2026-10-01. The SM lane banked `sm:B1506` on 2026-09-30 and relayed a correction to main's own B1427 ("relayed, not
applied"). Verified here **with code written on this bench**: own Reidemeister–Schreier covers, own Smith form, main's
B1427 index code, primes different from the lane's, a second presentation, and exact arithmetic.
**Verdict: PROVED. Every number of the lane's census is reproduced on every level M₁…M₆. The correction to B1427 is
real and is applied here as an addendum. One bad prime was found and is recorded.**

## What was wrong on main

B1427 reported "Y₃: 0 firing" and "the count of three is not this mechanism's on any level up to seven". Its census
(`v5_census.py`) parametrised a doublet module as ρ_χ ⊗ ψ, with diagonal characters χψ and χ⁻¹ψ. Their ratio is χ²,
**always a square**. A rank-two non-split module is determined by its two diagonal characters α, β and needs only
that λ = α/β be a locus (h¹(λ) ≥ 1). Modules whose λ is not a square were never in the scan. On levels whose fibre
torsion has odd order (M₂, M₄, M₅) every character is a square and the scan was complete. On M₃ = s961, with fibre
torsion (ℤ/4)², twelve of the sixteen loci are not squares.

The statement holds for what was enumerated. The absence was asserted for the frame. ERROR_LEDGER class E54.

## The frame without the lift

A background is a flat connection with holonomy in the image G′ of SL(2)_β × U(1)_Y × U(1)_γ in E₆. Because
E₆ ⊃ (SU(2) × SU(6))/ℤ₂ and the γ-charge is odd on every doublet sector, the SL(2) part and the γ part are each
defined only up to a common sign. The well-defined data are three characters θ, ψ_Y, W with extension character
λ = θ²/W, and sector s with charges (s_Y, s_γ) has

    α_s = θ · ψ_Y^{s_Y} · W^{(s_γ − 1)/2},    β_s = α_s / λ,

the module being the non-split extension of β_s by α_s. The background lifts to SL(2) × U(1)² exactly when W, hence
λ, is a square. A background is counted once by (λ, α_Q, α_{u^c}, α_{e^c}, α_{d^c}, α_L, α_{ν^c}). The meridian
values are forced to 1 on the five charged sectors and then on ν^c, up to a fifth root of unity that changes no
module, so the census lives on the characters of the fibre torsion.

## Computed (`verification/cover_census.py`)

Covers of m004 = ⟨a, b | a w b⁻¹ w⁻¹⟩ by Schreier rewriting with transversal 1, a, …, aⁿ⁻¹; generators z = aⁿ and
y_k = aᵏ b a⁻⁽ᵏ⁺¹⁾ for k < n − 1, y_{n−1} = aⁿ⁻¹ b. Every candidate module (λ, α) with λ, α characters of the fibre
torsion; index by B1427's `myindex.py`; three primes per level; the deck τ = conjugation by a, computed by rewriting.

| level | loci (non-square) | candidates | firing (non-square) | modules by orbit size | backgrounds (lifted) | by orbit size |
|---|---|---|---|---|---|---|
| M₁ | 1 (0) | 1 | 0 | — | 0 | — |
| M₂ | 5 (0) | 25 | 8 (0) | 2: 8 | 0 | — |
| **M₃ = s961** | **16 (12)** | **256** | **72 (72)** | 3: 72 | **48 (0)** | **3: 48** |
| M₄ | 45 (0) | 2 025 | 488 (0) | 2: 8, 4: 480 | 256 (256) | 4: 256 |
| M₅ | 121 (0) | 14 641 | 2 200 (0) | 5: 2 200 | 400 (400) | 5: 400 |
| M₆ | 320 (240) | 102 400 | 12 536 (11 184) | 2: 8, 3: 72, 6: 12 456 | 2 160 (336) | 3: 48, 6: 2 112 |

Every entry equals the lane's table. B1427's own numbers come back from the lifted rows: 12 800 = 256 × 50,
800 = 400 × 2, firing 976 = 488 × 2, 4 400 = 2 200 × 2, 16 = 8 × 2.

- **s961.** All 72 firing modules sit on the 12 non-square loci, six on each, with signatures (0,1,1,0) against
  (0,2,1,2) and no other. All 48 backgrounds have count ±1 in every sector, ν^c included and of the same sign;
  24 of each sign; none lifts. They form 16 orbits of three under the root's deck, and within an orbit the three
  extension characters are distinct, their ratios of order 4.
- **M₆.** 2 160 backgrounds, every count ±1, 1 080 of each sign; 336 lift and 1 824 do not; 16 orbits of three and
  352 of six, none of size one or two. ν^c: 144 with the generation's sign, 96 with the opposite sign, 1 920 without.
- **The index is deck-invariant on every level**, and every orbit of backgrounds is closed with one index vector.
- **h¹(λ) = 1 at every locus on every level**, the trivial character included.

## Independent of the lane, three ways

1. **Exact arithmetic.** `exact_m3.py`: the full 256-module index table of s961 over ℚ(i), with main's own
   cyclotomic arithmetic and no prime field, is identical entry by entry to the prime-field table.
   `exact_m6_union.py`: every M₆ module that fires at any prime used, 13 496 of them, evaluated over ℚ(ζ₄₀)
   (record `exact_m6_union.json`).
2. **A second presentation.** `snappy_pres.py`: SnapPy's own presentation of the covers, a third prime set.
   M₂ 8/0, s961 72/48 with none lifted, M₄ 488/256. SnapPy identifies the three as m206, s961, t12839.
3. **Different primes.** s961 at 5009-class and 7001-class primes; M₆ at 1481, 1601, 2081, 2161, 2281.

## A bad prime, recorded

At p = 1721 the M₆ census returns 13 400 firing modules, not 12 536: 960 that fire nowhere else and 96 genuine ones
lost. The five other primes agree on all 12 536. Exact evaluation over ℚ(ζ₄₀) gives index 0 on the 1721-only
modules tested and ±1 on the genuine ones (`exact_m6_spot.json`). Rank coincidences at a single prime change an
index; the lane met the same at 661 on M₅. The census requires agreement of at least three primes, and every firing
module is now also exact. `m6_prime_diag.py`, records `m6_prime_diag.json` and `m6_prime_diag_run.txt`.

## The deck map, and a correction that was itself wrong

The web seat's audit package gave the order-three deck square on M₆ as a word map. `sm:B1378` reported that map
wrong on two terms and substituted its own. Tested here (`deck_map_faithful.py`):

- the web seat's map equals the Schreier rewriting of g ↦ a² g a⁻², for all seven generators, as an identity of words;
- in m004's holonomy (a ↦ [[1,1],[0,1]], b ↦ [[1,0],[e^{iπ/3},1]]) restricted to the cover it equals conjugation by a²
  to 2 × 10⁻⁵⁰, every relator is preserved to 5 × 10⁻⁴⁹, and its cube is conjugation by a⁶;
- the substituted map misses by 45 and breaks the relators by 1.2 × 10⁴.

The cause is a label. B1378's text names the generators aᵏ b a⁻ᵏ, which have exponent sum 1 and are not in the
cover's group; its rewriting code produces aᵏ b a⁻⁽ᵏ⁺¹⁾. The lane found this itself on 2026-09-30
(`sm:B1506` §6: "a convention slip"). B1378's index results never used the map and stand.

## What it means, and the fence

- **Each background has count one, on every level.** B1427's law survives the complete census. Three is the size of
  an orbit of the root's deck on the root's only connected three-fold cover.
- **The three members of an orbit are three different backgrounds**, with different extension characters. Reading an
  orbit as three generations needs all three in one physical configuration. Nothing here supplies that.
- **Unchanged:** main's B1297 class index on reducible non-split modules; non-semisimple backgrounds; index is not a
  generation count; no value; no physics reading.

## Not verified here

The lane's theorems T1–T7 are read, not re-proved. The root object's counts −gcd(n, 3) and the pullback tables are
the lane's. The web seat's 67 200-background negative for the factorised family mechanism is not re-run.

## Registered

- The paper's sentence that the index is non-zero "on its degree-four cyclic cover" is true and no longer the whole
  statement: the degree-three cover fires off the lift. Whether the paper says so is the owner's call.
- `sm:B1506`'s one open bit, whether the root's deck is gauged or kept, is carried as the lane states it.
