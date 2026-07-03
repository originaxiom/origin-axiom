# B405 — BANKED: the supersingular package verified, deflated, and converted to sentinels

**Status: complete. Firewalled.**

- **VERIFIED:** a₇ = a₂₃ = 0 for the conductor-15 curve (15a1) — the program's two
  exceptional Gram primes are exactly the two supersingular primes below 30
  (counts_15a1.json). An exact, post-hoc, 2-for-2 alignment — banked as a datum.
- **DEFLATED (three ways):** (i) "#E = |2T|, |Q₈|" is automatic (#E = p+1 at any
  supersingular prime; the binary orders are prime+1 coincidences; the dictionary cannot
  be stated for 2I since 119 is composite); (ii) the CONTROLS kill "every program prime's
  count means something" — p = 11, 13, 17, 19 ALL give 16 (equally dressable ⇒
  unfalsifiable, the S5 pattern); (iii) Lead 1 is the THIRD return of the killed prime
  filter (B403) without addressing the kill — flagged.
- **Lead 3 ("seam = f₁₅ ⊗ Weil(15), entries are Hecke eigenvalues"): NEEDS-FORMULATION** —
  seam entries are rationals (±1/48-family); Hecke eigenvalues are the integers a_p; no
  map was proposed. Not testable as stated.
- **THE SENTINEL CONVERSION (the honest falsifiable core):** the supersingular list of
  15a1 below 200 is banked (sentinels.json). REGISTERED HOOK: if a future exceptional
  prime in higher-level Gram spectra (e.g. the 1215 identifications) lands on this list,
  it becomes an immediate registered test with real content — the same protocol as the
  17/19 sentinels (B403).

**Provenance.** verify_15a1.py, the sentinel extension → two JSONs; locks
tests/test_b405_supersingular.py.
