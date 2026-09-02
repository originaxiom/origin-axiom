# R48 — B511/D3.3 "wild-register accessibility": the committed dynamics does not reproduce, and the corrected dynamics reverses the verdict

**Banked (B511_physics_verdict/D3_FINDINGS.md, D3.3):** "P(κ ≈ 2 classical) ≥ 0.84; P(wild-accessible κ) ≤ 0.10 across
all mixes" — read there as "wild arithmetic is DYNAMICALLY SUPPRESSED: a typical history classicalizes (κ → 2)", and
D3.1: "stationary measure concentrates on κ = 2 … median 2.0 across seeds/sizes". Script: `d3_wild_access.py`
(41 lines): n Haar-random SU(2) pairs (A,B), 3000 steps of F: (A,B) → (AB, A) (80 %), M: (A,B) → (A, BA), D: (A,B) →
(A², B²), matrices rescaled by √|det| every 20 steps, then κ = x²+y²+z²−xyz−2 from the traces.

**(a) Verbatim rerun (Phase C agent, then the seat; numpy 2.4.6):** every history goes to NaN within 500 steps; the
script prints `classical=0.000 wild-accessible=0.000` for all three mixes. Mechanism: floating-point det drift is
amplified by the doubling move (det(A²) = det(A)²), the entries leave SU(2) exponentially, and rescaling by √|det|
cannot bring them back (`r48_output.txt`, part (a): 1000/1000 NaN for every mix and seed).

**(b) What the moves do to κ (exact to 3e−15):** F and M are Nielsen moves and preserve the Fricke invariant κ exactly;
only D changes it. So the "stationary measure" is driven entirely by the doubling events; nothing in F/M can move κ
toward 2.

**(c) Same dynamics with the matrices kept on SU(2) (polar re-projection every 20 steps):** across the three mixes and
three seeds (n = 1000, 3000 steps) P(classical) = 0.03–0.09, P(wild-accessible) = 0.73–0.76, median κ = 0.56–0.69
(Haar initial pairs: median 0.62, P(classical) = 0.02, P(wild) = 0.79). The measure stays wild; it does not
classicalize.

**Verdict: DIFFERS.** The banked numbers 0.84 / 0.10 / median 2.0 are not produced by the committed script on this bench
(it produces NaN), and a version of the same dynamics that keeps the matrices on the group gives the opposite
conclusion. Since F and M preserve κ exactly, a concentration on κ = 2 could only come from the doubling map
x → x² − 2 on traces, which is chaotic on SU(2) (angle doubling), not contracting to θ = 0. B511's D3 headline
("DYNAMICALLY SUPPRESSED … classicalization restated at the field level") therefore rests on a run whose numbers this
seat cannot reproduce and whose corrected form says the reverse. The B511 physics verdict itself is already negative
("no structure beyond B506/B507; T-SCALE fails"), so nothing downstream flips sign; but the D3.3 sentence should not be
cited as a result, and B506/B507's "classicalization" — which D3 says it restates — deserves the same rerun.

Files: `r48.py` (takes the committed script path as argument), `r48_output.txt`.
