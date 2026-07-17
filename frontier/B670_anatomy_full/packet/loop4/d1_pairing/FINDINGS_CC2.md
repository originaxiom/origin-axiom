# D1 — BANKED: THE PAIRING FILLS THE OBSTRUCTION SPACE (cc2 + subagent,
# 2026-07-17; prereg 8ffb0eb6; ALL GATES PASS, exit 0)

THE STRUCTURE OF THE FULL 5x5 VECTOR PAIRING [u_i cup_x u_j] in H^2(D;27-bar):
1. h^2(D; 27-bar) = 5 (Euler-forced, gated). RANK of span{[c_ij] : i<j} = 5.
   **THE VECTOR CUP CLASSES SPAN ALL OF H^2 — the supra-class coupling is
   SURJECTIVE onto the obstruction space.** (Pivots in the 31-dim ambient:
   cols 0,1,16,25,30; all 25 classes have zero residual in the 5-dim basis.)
2. THE BLOCK TABLE: [c_01] (boundary-boundary) = ZERO — the two boundary-born
   classes do not couple. ALL six boundary-solo pairs NONZERO — THE FIRST
   BOUNDARY SUPRA-COUPLING (the boundary talks to the generations at the
   vector level). All three solo-solo pairs NONZERO (C1 reproduced exactly).
3. THE SOLO RELATION: the three solo classes span only rank 2 — ONE exact
   linear relation binds [c_23], [c_24], [c_34] (frontier feed: extract its
   coefficients; a candidate "generation sum rule").
4. THE CUBIC-VISIBILITY MAP: all 9 nonzero classes are CUBIC-VISIBLE — for
   every nonzero [c_ij] some k has Y[ijk] != 0 (checked against the banked
   B637 unbent table; Y[023] = C1's witness exactly, cross-check True).

CORRECTION TO LOOP 3 (C1 FINDINGS, synthesis 2 — MB14, owned): the phrase
"the vector theory carries couplings the cubic CANNOT SEE" was overstated.
TRUE and banked: Y[024] = 0 while [c_24] != 0 — a SINGLE contraction can
vanish while the class lives (slot-wise blindness). FALSE as generalized:
no class is invisible to ALL contractions (global cubic-blindness does not
occur). The corrected synthesis: the cubic table IS the full contraction
data of the vector pairing (Y[ijk] = the u_k-contraction of [c_ij]); the
pairing is the finer object; its slot-wise zeros are basis-artifacts of
contraction, not missing couplings.
Controls: solo witnesses reproduce C1 exactly; Koszul antisymmetry 25/25;
coboundary-shift invariance; diagonal zero; zero floats. Artifacts:
d1_pairing.py, d1_results.json, d1_run.log. Repo untouched.
