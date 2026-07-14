# P1 ERRATUM (2026-07-15) — the longitude frame error, and its scope

**What was wrong:** P1's first bank (#943) evaluated ξ on "baBA" (the
fiber-frame commutator) labeled as "the longitude, B67 convention." In
B575's meridian presentation ⟨a, b | aWb⁻¹W⁻¹⟩, W = bABa, that word is
NONPERIPHERAL (commutes with neither meridian). The same wrong word was
given to chat-2 as their item-5 input (corrected on the record, B599
FINDINGS).

**How it was caught:** P2's Gate A (the ℤ²-cocycle compatibility
(ρ(μ)−I)ξ(λ) = (ρ(λ)−I)ξ(μ), left-cocycle convention) failed at ALL SIX
blocks. The original failing output is preserved and hashed
(`p2_original_gateA_failure.txt`, `ARTIFACT_HASHES.txt`).

**The correction:** the zero-framed longitude for μ = a is bABaaBAb (seat
4's canonical form); the word used in the regenerated table, "abABaaBAbA" =
a·(bABaaBAb)·a⁻¹, is GROUP-EQUAL to it (cocycle values on group-equal words
coincide once the cocycle condition holds — it does, solved from the
relator). The peripheral certificate: `peripheral_certificate.py` (the
SL(2)-level checks: the word commutes with a; exponent sum 0; its image is
−[[1, 2√3·i],[0,1]] — the off-diagonal equals the banked cusp shape).

**Scope of what is now certified (per seat 4's discipline):** Gate A green
= compatibility with the tested commuting pair, NOT an independent proof of
the longitude's topology/framing/orientation, and NOT gauge-independence of
the table. The table's vectors are REPRESENTATIVES in a fixed gauge
(coboundary-gauge and scale convention: leading ξ(μ)-coordinate = 1); they
are basis/gauge-dependent data. The gauge-invariant object (the class in
H¹(T²; V_m)) and its invariant pairing await the J-intertwiner cell (below).

**Unaffected by the erratum:** the ξ(μ) column, the dim H¹ = 1 gates, the
regular-unipotency gates, P0, and every bank outside the campaign.

## AMENDMENT (2026-07-15, seat-4 audit adopted) — my item-6 adjudication was WRONG

The earlier ITEM6 adjudication claimed "B582's certificate is a direct
finite-t computation (dimension-78 certificate, locked)." **Reading the
actual lock refutes this:** `test_b582_chiral_play.py` locks (1) the 27's
complexity (a weight-orbit fact), (2) the ARITHMETIC statement
dim e₆ = 72 + 6 = 78, deferring the closure dimension to "the G1-computed
dial map" — whose code was NEVER COMMITTED (the ROUND1_TRANSCRIPT bank has a
provenance hole; this is why chat-2 had to ask for its longitude
convention), and (3) the rank-≥2 hypothesis fact. **The finite-t existence
of the chiral play is NOT independently certified in-repo** — consistent
with L79's own open sub-item (the t ∈ {2, ω} sweep incomplete). Seat 4's
conditional blocker is adopted verbatim: B582's finite-t certificate is
mandatory before any claim that the mirror-double exists at finite
deformation; until then all such statements are FORMAL/JET-LEVEL. The
G1-recomputation (in-repo, committed code, with the certified longitude) is
registered as a mandatory campaign cell.
