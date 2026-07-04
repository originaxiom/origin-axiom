# B406 — BANKED: the two-conductor bridge, verified then deflated by torsion

**Status: complete. Firewalled. (The E-section of the final Chat-1 handoff; Sections A–D
were processed in B398/B403/B405.)**

- **VERIFIED:** the Hecke pattern is exactly as claimed — agreement at {13,17,19,29},
  disagreement at {7,11,23,31,37,41,43} (the conductor-40 model y² = x³−7x−6 = 
  (x+1)(x+2)(x−3) reproduces it); LCM(40,15) = 120 is exact arithmetic (and nothing more);
  their self-corrections check out (47 not supersingular; their supersingular list
  {7,23,31,79} matches our banked sentinels).
- **THE CONGRUENCE ARC (new, both halves ours):** a_p(15a1) ≡ a_p(40a1) (mod 4) at EVERY
  good prime < 200 (zero violations) — but the congruence is FORCED BY TORSION: 8 divides
  #15a1(F_p) (ℤ/8 rational torsion) and 4 divides #40a1(F_p) (full rational 2-torsion),
  so both a_p ≡ p+1 to the relevant modulus. Mod 8 the differences are {0,4} — nothing
  survives beyond torsion. **The "modular correspondence = quantization map" lead is dead
  at the congruence level**; the two curves are genuinely different forms sharing only
  conductor-arithmetic trivia.
- **THE 31-COLLISION (registered tension):** their E2 row claims split-PRINCIPAL primes
  are "absent from the program" (19, 31, 61, 79, …) — but 31 and 79 are supersingular
  sentinels for 15a1 (banked B405). If the 1215-triple identification surfaces 31, their
  two hypotheses collide: the sentinel fires AND the "principal absent" row dies. Filed.
- **Agreement primes < 200 banked as data:** {13,17,19,29,59,61,79,89,101,109,179,181}
  (no dressing; 79 noted as also-supersingular, uninterpreted).
- **Hooks to the ledger:** the moonshine mapping (χ's ↔ moonshine groups) — HOOK, no
  computation defined; "Gate B in minutes" — pending THEIR exact inputs (the B347
  geometric holonomy rerun is not specified to reproducibility); E5 tensor hypothesis —
  remains NEEDS-FORMULATION (no map from rational seam entries to integer Hecke data).

**Provenance.** bridge_check.py, the mod-4 extension → bridge.json, mod4_extension.json;
locks tests/test_b406_bridge.py.
