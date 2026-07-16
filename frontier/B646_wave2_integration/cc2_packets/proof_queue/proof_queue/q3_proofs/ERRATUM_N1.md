# ERRATUM to the delivered N1 packet (OA_CC2_next_queue_2026-07-16.zip, sha 52005c8c)
# — the generic-rung law as stated there is WRONG; corrected form below.
# (cc2, 2026-07-16; caught by this seat's own Q3 proof attempt, before any
# conformal-block measurement relied on it.)

STATED (n1_counting/FINDINGS_CC2.md + PACKET_README.md): "GENERIC-RUNG LAW
(theorem-candidate): kappa coprime to {2,3,5,7,11,19} => Z = +1. Confirmed at 23."

WRONG. The Weyl-class sum splits into two half-weight character sectors (Q3, L2):
a trivial sector and a sector twisting by the Legendre symbol (r|5) — the ten classes
whose fixed-point group has an ODD number of odd-exponent 5-divisors. Every generic
rung available in the packet's range (13, 17, 23) happens to satisfy (kappa|5) = -1,
which masked the twist. Decisive new rungs (q3_decider, exact pipeline, class-function
checked): Z(29) = 0, Z(31) = 0 [both (kappa|5) = +1]; Z(37) = +1 [(37|5) = -1].

**CORRECTED GENERIC-RUNG LAW: for gcd(kappa, 2*3*5*7*11*19) = 1:
  Z(kappa) = (1 - (kappa|5)) / 2  in {0, 1} — silent on quadratic residues mod 5,
  unit on non-residues.** Structural reading: 5 = disc(A1) (tr^2 - 4 det = 9 - 4);
the twist character is (kappa | disc A1) — the object's generic silence pattern is
the quadratic character of its own monodromy discriminant.

RETRO-CHECK against every banked rung (all consistent): 13, 17, 18 non-residues ->
baseline 1 + zero resonance = 1; 14, 16, 19 residues -> baseline 0, plus resonances
+1 (7^2-class at 14), 0 (dyadic interference at 16), +2 (Phi_9-class at 19): the
banked Z_7 = 2 is PURE SURPLUS over a SILENT baseline, not 1 + 1.

WHAT STANDS UNCHANGED from the packet: the six-rung prediction bank Z_8..Z_13 =
1,1,2,1,2,0 (direct exact computations, not law-derived — and Z_8 = +1 has since been
CONFIRMED by the Q1 level-8 build); the interference mechanism at 16; the single-class
surplus mechanism at 19; the per-class jump behavior (now upgraded to the uniform
elementary-divisor form, Q3 L3, 300/300); the D1 characters; the clock-law material
(N2) is untouched.

Half of all generic rungs are silent. The abelian/Funar heuristic ("unimodular =>
unit") holds only on the non-residue half; the residue half's vanishing is a genuinely
nonabelian sector cancellation.
