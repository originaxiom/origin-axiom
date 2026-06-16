"""PHASE 2 / ROUTE R1 -- FINAL consolidated results (this session). All VERIFIED.

=========================================================================================
A. NEW EXACT SYMBOLIC PROOF -- figure-eight (m=1), SL(3), {1,i,-i} (o=4):
     [A,B] = c * mu^3  identically over Q(i),  with c * det(t) = 1  (so c=1 on SL(3)).
     => k=3, non-vacuous (3 irreducible reps, ||.||~1e-15). Matches k=4-m(o-3)=3.
     scripts: r1_fig_sl3_o4_proof.py (proof), r1_fig_sl3_o4_verify.py (c*det=1 + irreducible)
     Mechanism: k = smallest j with [A,B]*mu^-j scalar (r3_k_mechanism.py).

B. THE o=4/SL(4) BLOCKER RESOLVED -- {1,1,i,-i} figure-eight SL(4) irreducible locus is EMPTY:
     LEMMA 1 (EXACT, Q(i)): det(UR)*det(LL) IN the bundle ideal (reduces to 0 mod GB) =>
              every rep has a singular coupling block UR=t[0:2,2:4] or LL=t[2:4,0:2].
     LEMMA 2 (numeric, structured): the only branch carrying nondegenerate reps (t22=i*t33) has
              Burnside dim = 13 < 16 at 2 seeds (6 reps each) -- all reducible.
     CONTROL: {1,1,w,w^2} (o=3) same construction => Burnside 16 (irreducibles exist).
     => the law's predicted (m=1,o=4,n=4)->k=3 point DOES NOT EXIST. Consistent with order-based
        rigidity: o=4 admits irreducibles only at n=3 (n=5 also found none, suggestive).
     scripts: r1_fig_sl4_o4_prove_empty.py (Lemma1 sat=unit), r1_fig_sl4_o4_final.py (Lemma1 membership),
              r1_o4_consolidated.py (Lemma1 exact + Branch-B Burnside=13 + o=3 control).

C. SILVER (m=2) UPGRADED to 50-digit matrix identity (was float 1e-12 in B154):
     o=3 {1,w,w^2}: [A,B] = -mu^4  (k=4), 2 seeds, ||.||~1e-53.
     o=4 {1,i,-i}:  [A,B] = -mu^2  (k=2), confirmed 4 independent reps (float) + 50-digit (1 rep).
     scripts: r2_silver_polish.py, r2_silver_o4_robust.py

D. THE CLOSED FORM k=4-m(o-3) IS REFUTED (confirms a prior-session bronze finding, re-verified here
   by an INDEPENDENT full-relation Newton path, 4 reps/cell, 2 seed streams):
     VERIFIED k(m,o) at SL(3):
                o=3      o=4      o=6
        m=1     4        3        -
        m=2     4        2        -
        m=3     1*       3        1
     (*) m=3,o=3 is DEGENERATE: o|m => A^m=I => mu=A^-3 t = t exactly (||mu-t||~1e-15); the "k=1" is the
         meridian-collapse regime, NOT a metallic point -- EXCLUDE it.
     Genuine refutation: (m=3,o=4)->3 [formula predicts 1] and (m=3,o=6)->1 [formula predicts -5]. WRONG.
     => k=4-m(o-3) was an artifact of m in {1,2}. The "order-not-rank" qualitative finding STANDS
        (o=3 => k=4 at n=3 AND n=4 for m=1,2); the 2-parameter closed form does not.
     scripts: r5_bronze_verify.py, r6_find_law.py, r7_m3o3_degeneracy.py

OBSTRUCTION to a uniform (m,o) derivation:
  - higher m (m>=4) reps are hard to reach by Newton (more nonlinear); o>=5 needs n>=5 for a primitive
    spectrum; data is sparse beyond the 3x2 grid.
  - the exponent is k = min j: [A,B]*mu^-j scalar (a per-spectrum ideal fact), but its value as a function
    of (m,o) has no 2-parameter closed form consistent with the bronze row; likely needs m mod o + a
    metallic-A-polynomial-slope computation (the full B67/B71/B89 program generalized to phi_m), not a fit.
=========================================================================================
"""
print(__doc__)
