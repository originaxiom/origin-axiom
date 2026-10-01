# B1441 PREREGISTRATION — THE SEVERAL-CUSPED LEVELS: can one rank-two background count more than one, where there is more than one cusp?

**Sealed 2026-10-01, before the class index of any non-split module is computed on a manifold with more than one
cusp. Seat: cc (main). Occasion: B1440 bounds the count per vacuum by half the rank on a once-punctured-torus
bundle, and names where the bound does not reach: more cusps. Main's lead L222 has carried the computation as owed
since 2026-09-16 ("the two-cusped members with the three — m202, s959 — whose index needs B1333's several-cusp
form"). A sweep of main and every lane on 2026-10-01 found no such computation anywhere: B1333 evaluated only
modules of the reductive domain on its 54 covers (all zero, as Menal-Ferrer–Porti forces), and B1418 ran its
non-split modules on one-cusped members only.**

## 0. The quantifier (P0)

For every manifold of the population and every rank-two non-split module V(ℓ, α) built from its characters as in
§2: main's class index I(V) = n(V) − n(V*) on all its cusps. The scope sentence names no manifold.

## 1. The population (fixed before the run; sizes computed without any index)

- **(a)** every connected cover of degree 2 to 6 with at least two cusps of m004, m003, m009 and m010 — the four
  smallest word states — in SnapPy's order: 11 + 7 + 24 + 27 = 69 manifolds, with 2 to 6 cusps;
- **(b)** m202, s959, o10_150726 (the record's two-cusped carriers of the localized three, B1414), m129 and m125
  (B1333's two-cusped validation pair).

74 manifolds: 54 with two cusps, 15 with three, 3 with four, one with five, one with six.

## 2. Conventions

- **Characters:** Hom(H₁(M), μ_N), N the exponent of the torsion of H₁(M), and 2 if H₁ is torsion-free (tier 1).
  For the five manifolds of (b) also N = 12, the group B1418 used (tier 2). **No cusp condition is imposed on the
  characters**: a character non-trivial on a cusp makes that cusp dead for it, and which cusps are live is
  recorded, not chosen. A manifold with more than 600 characters is skipped and listed (three are, at tier 1; none
  at tier 2).
- **Modules:** V(ℓ, α) = [[α, cβ], [0, β]], β = α/ℓ, for ℓ non-trivial with H¹(M; ℓ) ≠ 0 and α, β non-trivial; c
  runs over a basis of H¹(M; ℓ) and, when its dimension exceeds one, two random combinations (seeded).
- **Index:** B1333's `mc_lib.check` at a prime ≡ 1 mod N above 3 000, its five identities asserted on every module.
  Every module with |I| ≥ 2 is recomputed at two further primes; where h¹(ℓ) = 1 the three must agree, and a
  manifold where they do not is reported as discarded.
- Instrument: `verification/several_cusps.py`; reader: `verification/read_several.py` (run twice before the seal).

## 3. What has been seen before the seal (disclosed)

- **C1, the control, on one-cusped levels:** the instrument on M₂ and on s961 with every character of order
  dividing N (25 and 64 of them, cusp-trivial or not): 8 and 72 firing modules, the banked numbers, all with
  |I| = 1. Record `control_run.txt`.
- The sizes above: cover counts, cusp counts, H₁.
- **No index has been computed on any manifold with more than one cusp**, by this seat or, per the sweep, by any.

## 4. Sealed predictions (each can come out either way)

| | prediction | prior |
|---|---|---|
| M1 | Some manifold of the population carries a rank-two non-split module with \|I\| ≥ 2. | 50% |
| M2 | Some manifold carries one with \|I\| = 3. | 20% |
| M3 | On every manifold, every module has \|I\| at most the number of cusps. | 80% |
| M4 | Both m202 and s959 carry a module with I ≠ 0 (either tier). | 50% |
| M5 | m202 or s959 carries a module with \|I\| ≥ 2 (either tier). | 25% |
| M6 | Every module with \|I\| ≥ 2 has at least two cusps live for the module or for its dual. | 85% |
| M7 | Among the covers of the four word states, the largest \|I\| is reached on a manifold with at least three cusps. | 40% |

## 5. What each outcome would mean (written before the data)

- **M1 NO** would extend one count per rank-two background from one cusp to the several-cusped manifolds nearest
  the architecture, with nothing proved: a census regularity asking for a theorem.
- **M1 YES** would be the first rank-two background in the record counting more than one, and **M2 YES** the first
  counting three: three generations as one module on one manifold. It would then be recomputed in exact arithmetic
  and at six primes before a word of it is written, and the frame's sectors (five charged sectors at once) put to
  it in a further sealed arc; a single module with |I| = 3 is not a generation-shaped background.
- **M4, M5** read the record's own two-cusped carriers of the localized three against the class index for the
  first time.
- None of the outcomes is a physical statement. The fence is B1438's and B1440's: main's class index on modules
  outside the reductive domain; an index is not a generation count; no physics reading of a non-semisimple
  background. 0 of 19.

## 6. Not in this arc

Generation-shaped backgrounds on several cusps (five sectors at once); modules of rank above two; covers of degree
above six; exact arithmetic (owed to any |I| ≥ 2).

## 7. Hashes at seal

See `ARTIFACT_HASHES.txt`.
