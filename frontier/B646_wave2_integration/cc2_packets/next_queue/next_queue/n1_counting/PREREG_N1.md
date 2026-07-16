# N1 — THE COUNTING CELL (sealed prereg; cc2, 2026-07-16)

**The question (from R1's residual-hint):** what does Z_k = Tr ρ_k(A₁) COUNT? The record
already frames Z_k as the Sol mapping-torus WRT invariant (L24(b), Jeffrey 1992) with
Funar's abelian |Z| = |H¹|^(1/2). Here det(A₁ − I) = −1 is unimodular ⇒ the abelian
count is 1 at every level ⇒ **the ladder's 0 (k=4) and 2 (k=7) are intrinsically
nonabelian deviations.** This cell decomposes them.

**Data to bank blind (before reading against predictions):**
D1. The exact CHARACTER of ρ(A₁) per parity sector, k=1..7: eigenvalue = root-of-unity
    multiplicity vectors via power traces Tr(B^j), j = 0..ord−1, DFT at dps 50 with
    integrality certificates (round-error < 1e-30; checks Σm = dim, Σ m ζ^r = Z_sector,
    m ≥ 0). Machinery: level_ladder engine rebuilds; locked word T²ST.
D2. The Jeffrey decomposition PER WEYL TERM, k=1..7: the B600 Jeffrey pipeline
    (coroot-lattice Gauss sums, exact sympy) instrumented to emit each Weyl-element
    class's contribution separately, not just the sum.

**Sealed falsifiable predictions:**
P-N1-a (the zero is interference): at k=4 (κ=16) the total vanishes while AT LEAST ONE
    individual Weyl term is nonzero. Falsifier: every term is individually zero
    (termwise death, not interference).
P-N1-b (the surplus is new support): at k=7 (κ=19, split) the set of Weyl classes with
    nonzero contribution is STRICTLY LARGER than at the inert rungs k=3 (κ=15) and
    k=5 (κ=17). Falsifier: identical support with only magnitude changes.
P-N1-c (sector correlate — comparison list sealed for look-elsewhere honesty): the
    sector pattern (O,O,E,N,E,O,B) across κ=13..19 is tested against EXACTLY these
    classifiers: κ mod 3, κ mod 4, κ mod 5, v₂(κ), v₃(κ), ℚ(√−3)-splitting of odd p|κ,
    ℚ(√5)-splitting of odd p|κ, κ prime?. Outcome banked with denominator 8; with 7
    rungs, any hit is NOTICED at most — no promotion from this cell.

**Interpretive target (exploratory, labeled as such):** identify Z_k as a signed count
over A₁-twisted W-sectors (Lefschetz-flavored: which w have fixed points on the κ-torsion
of the coweight torus) and name what jumps at the split prime. Any identity found gets a
NOTICED entry + an exact-check script; promotion requires a fresh-rung prediction (k=8)
in a FUTURE cell, not this one.

**Gates:** k ≤ 6 ladder reproduction in-run (hard stop); Jeffrey totals must equal the
banked Z_k per level (the R1/B600 cross-pipeline identity) before per-term data is read.
