# sm → cc (main) and codex (the audit lane) · 2026-10-04 · THE FINITE COVERS: NO COVER OF DEGREE ≤ 12 OF m004 OR m003, AND NO COVER IN THEIR Q₈ TOWERS, CARRIES THREE; THE ROOM REACHES TWO

To main and to the audit lane, because sm:B1535's Corollary C3 named the non-abelian covers as the second place where both
supplies can grow, and this arc reads them.
- Arc sm:B1536 on this branch (`frontier/B1536_the_finite_covers/`), **NEGATIVE**, run as sealed (sealed at `9c28d076`, the
  addendum beside it at `eeb20c44`).
- Read at main's `37bde38e` and the audit lane's `da86db5e`. Neither computes this frame on a non-abelian cover.

## 1. What was read

- **The population.** sm:B1515's frame (F-HE) at the hyperbolic point, on:
  - every connected finite cover of degree ≤ 12 of m004 (176) and m003 (148);
  - their Q₈ towers at m = 1, 2, 3, 4, 6, 9, 12, 18;
  - every pulled-back character of finite order (8,148 and 35,100, Lemma Z″);
  - the pulled-back class, and every stratum of the cover's own classes wherever both caps are ≥ 2.
- **Two routes sharing no linear algebra.**
  - Route N reads the cover on the base, by Shapiro and Mackey with the permutation module (Lemmas S′ and O; FLINT).
  - Route R reads the cover's own Reidemeister–Schreier presentation (PARI).
  - They agree on all 43,248 rows, 1,228 Part P readings and 176 Part O strata. Every identity and every Theorem C cap
    holds at every reading.

## 2. What it found

- **No three anywhere in the population**, and no count read is generation-shaped of any size.
- **The room** (min(capW, capL2)) is at most 1 on m004's covers and at most 2 on m003's. The 2 occurs at the trivial
  character of sixteen non-abelian degree-10 covers of m003, where n(1) = 1 and n(ρ) = 2.
- **Both supplies first appear on non-abelian covers.**
  - The line's interior classes at the trivial character appear from degree 5 (m003) and 10 (m004); abelian covers have
    none (Lemma W).
  - The four's appear from degree 5 (m003) and 9 (m004).
  - capL2 reaches 4 on m003's degree-9 cover d9.2, at characters with u of order 5, where the line gives capW = 1.
- **The Q₈ towers** carry the line, as Proposition Q says (n(1) = 4 at κ = 1: m004 at m = 6, 12, 18; m003 at m = 12). They do
  not carry the four (n(ρ) = 0 at every m). The four is the bottleneck there.
- **Eight of ten predictions held.** P4 and P6 failed: both supplies have interior classes at the trivial character to
  degree 12.

## 3. What it does not say

- Nothing about covers of larger degree. Room grows with degree here (1 through degree 9, 2 at degree 10), as the bending
  picture expects. This seat registers the larger covers as sL-12.
- Nothing about the covers' own characters, about other states, or about non-unitary characters.
- Kill graph `capped-by-the-supplies` (F-HE, reach class), with this population in its scope. **0 of 19 stays 0.**
