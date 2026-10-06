# PREREGISTRATION 2 — sealed 2026-10-06 by the web seat BEFORE computing. Follows PREREG 1 (85df26a8).
## R1 — the exploratory spin-bit identification, sealed and made robust
Re-run P2 with the OTHER transversal (t = b instead of a). Predicted: the same counts (24 extend, 24 sign-obstructed,
0 outer) and m004's Z/2 character moves 48 of 48 to the other half. KILL: any other number.
## R2 — the register is complex conjugation c, visible prime by prime
Riley: pi1(4_1) -> SL(2, Z[omega]), x -> [[1,1],[0,1]], y -> [[1,0],[-omega,1]]. The deck acts as rho -> rhobar (c).
Predicted, at each prime p <= 31 (reduce mod a prime over p):
  - p = 3 (ramified): rho and rhobar reduce to the SAME representation (omega = omegabar = 1 in F3).
  - p = 2 mod 3 (inert): rho and rhobar are NOT conjugate over F_{p^2}; they differ by Frobenius (traces 2-omega vs 2-omega^p).
  - p = 1 mod 3 (split): rho mod pi and rhobar mod pi are two non-conjugate representations over F_p (c swaps pi, pibar).
  KILL: any p != 3 where rho and rhobar have equal traces on the test words.
  Controls: the Riley relation holds mod p at every p; tr(xy) = 2 - omega is not in Z.
## R3 — the paper's Scope 7.2 ("pi1(4_1) surjects onto neither 2I nor A5"), checked two ways
(i) direct enumeration of surjections of SnapPy's pi1(m004) onto A5; (ii) the order of the image of Riley mod 2 in
SL(2,F4) = A5. Predicted (if the paper is right): 0 surjections, and the Riley mod-2 image is a PROPER subgroup.
No prediction is preferred; the paper's statement is what is tested. Either outcome is reported.
