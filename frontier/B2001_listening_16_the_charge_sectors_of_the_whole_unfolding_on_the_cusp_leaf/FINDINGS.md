# B2001 — Listening 16: across the whole cusp leaf the neutral sector holds what persists and the charged pair fades about twice as fast, with the two charged members identical; on the whole's own prime 3 the charged spectrum is exactly half the neutral one; and the covariant unfolding is the symmetric walk on three pairs of moves

**Verdict: PROVED (exact commutation and symmetry; spectra by dense eigensolvers on orbits up to 5,832 points; the halving to
12 digits, post hoc).** Main, 2026-11-25, in the author's /loop "continue the listening line". Data-free. Register row
P-882. **0 of 19.**

## Seen first

- **B1995:** at the common point the linearised unfolding treats ω's three members alike.
- **B2000:** at (3,3,3) the covariant linearisation separates them 14 : 5, with the pair locked. That result is local.
- **B1996 and B1997:** the 3-tower's settled rate λ*/2 for W₊, over ℚ(cos 2π/9).
- **B1983:** the leaf mod p is connected.
- **Swept:** `VERDICT topic-sweep /charge sector|neutral sector|charged pair|time-reversal|symmetric walk|Vieta/: 8 of 1742 arcs on main match (PROVED 8); 3 register rows match (QUEUED 3)`. No arc decomposes the unfolding on the leaf by ω's charge.
- **The literature (standard):** the Markoff graphs mod p, with their three Vieta moves, are studied as expanders
  (Bourgain–Gamburd–Sarnak). Nothing here depends on that work.

## The results (`verification/sectors.py`, `sectors_run.txt`)

The table gives each sector's slowest decay per move: the largest modulus below the top, divided by 6 for W₆. W₁₂ gives the
same ratios.

| leaf | points | neutral (q = 0) | charged (q = 1 and 2) |
|---|---|---|---|
| mod 5 | 40 | 0.901106 | 0.449077 |
| mod 7 | 28 | 0.885952 | 0.469678 |
| mod 11 | 88 | 0.957678 | 0.458730 |
| mod 13 | 208 | 0.967655 | 0.469856 |
| mod 27, orbit of (3,3,3) | 72 | 0.881917 | 0.440959 |
| mod 81 | 648 | 0.986507 | 0.493254 |
| mod 243 | 5,832 | 0.986507 | 0.493254 |

- **G1 holds:** W₆ and W₁₂ commute exactly with C's permutation on every orbit.
- **G2 holds:** the two charged sectors have the same spectrum, to 10⁻⁶ by the general solver and exactly by the symmetric
  one (post hoc, below).
- **G3 holds:** at every level the neutral sector's slowest decay (0.88 to 0.99 per move) differs from the charged pair's
  (0.44 to 0.49).
  - The constant, the one undamped mode, lives in the neutral sector.
  - The charged sectors' strongest mode is at most half the top.
- **G4 holds:** on the 3-tower both sectors settle, unchanged from mod 81 to mod 243: neutral 0.986507, charged 0.493254.

## Post hoc, labelled (`halving_posthoc.py`, `halving_posthoc_run.txt`; written after the run was read)

- **(a) Exact (sympy): the six conjugated moves are closed under inversion.**
  - L⁻¹ = CRC⁻¹ and R⁻¹ = C²LC⁻².
  - The third move X = CLC⁻¹ = (y, yz − x, z) has X⁻¹ = C²RC⁻².
  - So the C-covariant unfolding is the symmetric walk on the three pairs L^±, R^±, X^±. It is time-reversal symmetric
    (W₆ = W₆ᵀ on every orbit), and W₁₂ = 2W₆.
- **(b) On the 3-tower the charged spectrum is exactly half the neutral one below the top.**
  - Neutral slowest over charged top is 2.000000000000 at mod 27 and at mod 81. At mod 5, 7, 11 and 13 the ratio is 2.0066,
    1.8863, 2.0877 and 2.0595.
  - The leading eigenvalues pair as μ and μ/2:
    - mod 27: 2√7 and √7;
    - mod 81: 5.919044005 and 2.959522002, then 5.758770483 and 2.879385242.

    2.879385242 agrees with 1 + 2cos(π/9) to nine digits, the ninth-root field of B1997. These are numerical
    identifications; the halving's reason is open.

## What the whole does, read in its own terms

- **Taken over the whole leaf, the 1 + 2 split is a split in persistence.**
  - The neutral sector carries the constant and the slowest forgetting, 0.99 per move at the whole's prime.
  - The charged pair is forgotten roughly twice as fast, 0.49 per move.
  - The two charged members never differ.

  The local 14 : 5 at (3,3,3) (B2000) is therefore not local only: across the leaf, the neutral member is what the whole
  remembers.
- **The whole, made covariant under ω's own symmetry, has no arrow of time.** It is exactly the symmetric walk on three
  Vieta-type moves. B2000's and this arc's splits are not produced by any asymmetry between a move and its inverse.
- **At the whole's own prime the relation between the two sectors is exact,** a factor of 2 in the spectrum. At other primes
  it is close to 2, not equal.
- **No rate is read as physical, and nothing is compared with data.**

## What is open

- **Why the charged spectrum is exactly half the neutral one on the 3-tower:** the structure behind it, perhaps the three
  C-fixed points there against one at mod p.
- **The exact fields** of 0.986507 and 0.493254 (√7 at mod 27; 1 + 2cos(π/9) appears at mod 81).
- **Whether anything in the whole breaks the reflection** that keeps the charged pair locked (agy-exp's NI-4, not checked).
