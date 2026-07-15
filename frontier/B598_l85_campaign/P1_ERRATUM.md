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

## SECOND AMENDMENT (2026-07-15, the freshness addendum D1–D10 adopted)

- **D2 RETRACTION:** the "quadratic-arrow verdict" ("the arrow is quadratic;
  P3 matches at order two; B599 is the classical side of P3") is RETRACTED
  as a banked claim — no map was constructed to have an order; it survives
  only as a heuristic expectation. Every ledger surface carrying it is
  superseded by this note (PROGRESS_LOG is append-only; the supersession
  entry is authoritative).
- **D1:** the banked "P2" is renamed **P2-preflight** (gates + data; the
  quantization map does not yet exist).
- **D3:** the P2 script's "PREREGISTERED" docstring label was not a
  pre-result timestamp (source + output + verdict shipped together in #945);
  relabeled RETROSPECTIVELY REGISTERED; the failed odd-trace prediction
  stands permanently as an exploratory failure.
- **D6:** the peripheral certificate is NUMERICAL evidence in one
  representation; group equality requires the faithfulness of the geometric
  rep (Thurston — cited, not re-proven here), and primitivity, preferred
  framing, and cusp ORIENTATION (the certificate checked |Im| only) are not
  yet certified. **Readiness step 1 is PROVISIONAL** pending the exact
  algebraic peripheral derivation (seat 4's adjudication §3–4 is the
  blueprint to port in-repo).
- **D7:** Gate B covers one vector per block and the letter 'a' only — an
  implementation spot-check, not the full intertwining claim; full-basis ×
  both-generators coverage is a chain sub-item.
- **D8:** the P2 and word-independence scripts were print-only; both are now
  failure-enforcing (asserts added).
- **D9:** the six-block word-independence run is an exact INTERNAL
  consistency check (same pipeline), relabeled as such.
- **D4 (refinement):** the invariant ratio (I_λ : I_μ) of step 3 removes
  gauge AND scale within a block; what it does not supply is the
  CROSS-DOMAIN normalization (classical scale ↔ stage scale) — that is
  step-4's explicit obligation.
