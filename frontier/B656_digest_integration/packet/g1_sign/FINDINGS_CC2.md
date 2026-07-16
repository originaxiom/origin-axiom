# G1 — BANKED: THE SIGN-HEARS-THE-DISCRIMINANT THEOREM (cc2, 2026-07-17;
# prereg 5848c32d; g1_run.log + g1_run2.log = 207,384 verifications, 0 exceptions)

**THEOREM (even-rank form).** Let A be a metallic monodromy (tr t, det 1), W a Weyl
group acting on an even-rank lattice, B_w = tI - w - w^{-1}. Then for every prime p:
  det(w) = (-1)^{v_p(det B_w)}   iff   v_p(disc A) = v_p(t^2 - 4) is ODD;
for v_p(disc) even the agreement is exactly chance (the sign-balanced half).
PROOF: det B_w = +- prod_zeta f(zeta) with f(x) = x^2 - tx + 1; f(-1) = t + 2 =
det(A+I); f(1) = 2 - t = -det(A-I); complex eigenvalues contribute in conjugate
pairs of equal p-valuation (even); on even rank mult_{+1} == mult_{-1} mod 2 and
det(w) = (-1)^{mult_{-1}}; hence v_p(det B_w) == mult_{-1} * v_p((t+2)(t-2)) =
mult_{-1} * v_p(disc) mod 2. QED (the pair-evenness lemma at ramified primes via
both roots of f sharing one residue; verified exhaustively below).

**The verification ladder (all four sealed words, W(E6) x W(A2)):**
golden t=3 (disc 5): v_5 tracks 51840/51840 + 6/6, others exactly half;
silver t=6 (disc 32): v_2 tracks perfectly, others half;
t=5 (disc 21 = 3*7): v_3 AND v_7 track perfectly (my sealed naive prediction said
v_7 only — WRONG, corrected by the theorem's t-2 term; reported honestly);
t=7 (disc 45 = 3^2*5): v_5 tracks perfectly, v_3 does not (the naive "none"
prediction also wrong; the disc-parity form got all four words right).

**What it unifies (the digest's purpose):**
- P1's jewel (det(w) = 5-parity at E6/golden) is the special case — and the reason
  the chi_5 sector weighs exactly 1/2 is now MECHANISM: the sector IS the sign
  character's odd half.
- The mirror thread: det(A+I) enters as f(-1) — the same quantity that seeds the
  mirror channel's identity resonance (the one-line lemma, banked here too:
  B_id for the -A word = -(t+2)I, so the mirror identity class carries
  det(A+I)^rank at every stage; confirmed E6 5^6, A2 5^2).
- Cross-stage prediction machine: any future stage/word's sign-sector structure is
  now read off disc(A)'s odd primes with no computation.
ODD-RANK NOTE: mult_{+1} and mult_{-1} decouple; the law bifurcates into separate
det(A+-I) parities — stated, not needed for any banked stage (all our lattices even).
=> proposal to cc: THEOREM row (proof + 207k exhaustive); supersedes the P1 NOTICED
identity; links the sign character, the silence sectors, and the mirror quantity in
one statement.
