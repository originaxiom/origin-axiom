# P-SEAM-02 --- RESULTS: G1, G2, and the PRIOR-ART GATE
seat chat1 ("Biri"), 2026-09-08.  Prereg sealed BEFORE computing:
  P-SEAM-02  sha256 9a101d59ed1cdc603ff85991ed052c3be11508a0500e5ad43e7456afa98e5d83
  (supersedes P-PHASE-01 sha256 3094786c..., sealed and never run)

## VERDICTS

  G1  IDENTITY .............. TRUE   (controls pass)
  G2  POISSON ACTION ........ TRUE   (controls pass) -- but see the gate below
  G3  DEGENERACY ............ NOT RUN
  PRIOR-ART GATE ............ **DEMOTES G2.** Mechanism is classical.

## G1 --- computed, not asserted
  tr[a,b] - (x^2+y^2+z^2-xyz-2)          residual = 0   (generic SL(2,C), det=1 imposed)
  B497 coords == B293 coords              a->ab,b->a induces (z, x, xz-y): residual 0 x3
  {kappa,x} = {kappa,y} = {kappa,z} = 0   (Casimir reproduced from Goldman relations)
  decoy cubic x^2y+z^3-3xz                NOT central (C-null correctly fails)
  B497 kappa-laws S1,S2,S3 re-derived     residual 0 (not trusted from the table)
  S4 image in {kappa=2}                   TRUE (after fixing MY bug -- see ledger)

## G2 --- the computed law
  | stratum                  | kappa      | Goldman multiplier |
  |--------------------------|------------|--------------------|
  | 1  gold      (det = -1)  | preserved  | -1  (ANTI-Poisson) |
  | 1  gold^2    (det = +1)  | preserved  | +1  (Poisson)      |
  | 2  doubling  (det =  4)  | NOT presd  | none               |
  | 3  Thue-Morse(det =  0)  | NOT presd  |  0                 |
  | 4  rank 1                | NOT presd  |  0                 |
  Identity multiplier +1 (C-alive). Not every map preserves kappa (C-vacuity does not fire).
  **Statement: on stratum 1 the bracket multiplier IS the determinant.**

## PRIOR-ART GATE --- run BEFORE claiming anything (the v1 lesson)

1. **The invertible half is Goldman's.** Goldman's own survey (*Mapping Class Group
   Dynamics on Surface Group Representations*, math.umd.edu/~wmg/mcgdynamics.pdf):
   the mapping class group acts by polynomial transformations of C^3 **preserving kappa**,
   and acts by symplectomorphisms; the relative character varieties are the level sets
   kappa^{-1}(t). Orientation-reversing classes being anti-symplectic is standard.
   => "det = +1 Poisson / det = -1 anti-Poisson" is TEXTBOOK, not ours.

2. **The invariant is Baake's.** VERIFIED HERE: Baake-Roberts's Fricke-Vogt invariant
   I = x^2+y^2+z^2-2xyz-1 satisfies **4*I(x/2,y/2,z/2) = kappa - 2** exactly. Same
   invariant, half-trace normalization. So B497's kappa-laws are statements about the
   Fricke-Vogt invariant -- squarely inside Baake-Grimm-Roberts territory. (Consistent
   with B497's own Phase-1 gate, which killed the P5-monoid paper on Baake-Grimm-Joseph
   1993 containing its spine verbatim.)

3. **Baake-Roberts, arXiv:math/9901124** (*Symmetries and reversing symmetries of trace
   maps*, Baake & Roberts 1999) classify the reversing symmetry group for the **Nielsen
   class** = invertible trace maps preserving I, isomorphic to PGL(2,Z). Their closing
   section turns to non-Nielsen (non-invertible) trace maps, notes they are never
   reversible in that sense, calls for a generalized notion covering non-invertible
   mappings, and states plainly that they see **nothing close to a classification** for
   that case. *(paraphrase; the sentence is in sec. 4 of the arXiv text)*

4. **Independent confirmation of the gap.** Arnoux-Berthe-Hilion-Siegel: any substitution
   extends to a free-group endomorphism, and the general theory of **endomorphisms** is
   not yet well understood -- most geometric constructions land on automorphisms.

## HONEST VERDICT (what today actually bought)

**Not a discovery. A propagation.**
 - The det = +-1 half of G2 is classical (Goldman) and its invariant is Baake's.
 - Multiplier 0 on strata 3-4 is **near-trivial**: those maps have rank-deficient
   Jacobians (Thue-Morse sends x,y both to z; rank-1 collapses further), so the pulled-
   back bivector degenerates for elementary reasons. It is a computation, not a surprise.
 - The residue that is genuinely NOT in the literature is the **frame**: a four-stratum
   classification of the NON-INVERTIBLE sector, which is exactly what Baake-Roberts say
   is missing and exactly what B497 already banked in July 2026.
 => So the value is that **B497 (verified zero propagation: 0 mentions in B915, B925,
    B929, B1137, B1126) now has a symplectic reading**: its four verbs are four ways of
    acting on the Goldman foliation, with evolution leaf-preserving and erasure landing
    on the degenerate leaf {kappa=2} that B497 itself calls "the classical floor."
    Architecture, not furniture. Nothing promotes to CLAIMS.md.

## REGISTERED OUTCOME
Per the sealed prereg this is **OUTCOME B-plus**: G1 and G2 true, but the mechanism is
classical, so the correspondence is a **[RHYME]** in the P000 sense -- files to
philosophy/ or as a B497 addendum, promotes nothing. Outcome A is NOT claimed.

## STILL OPEN
 - G3: is {kappa=2} exactly where the Goldman form drops rank? (predicted yes: the
   reducible locus; classical, should be checked not assumed)
 - G4: S063 ("arrow enters where det != +-1") vs B766 ("arrow IS the golden branch").
   NOTE: G2 sharpens this -- det = -1 is anti-Poisson, i.e. bracket-REVERSING, which is
   the reciprocity/time-reversal side of B124/P006, NOT an arrow. B124 says there is no
   arrow. So S063's "arrow" wording is suspect and the adjudication should probably
   retitle rather than choose.
 - the general claim "multiplier == det on ALL of stratum 1" is tested on TWO citizens
   only. Two instances are not Aut(F_2).

## ERROR LEDGER (this run)
 15. **My stratum-4 test was broken**: I substituted a matrix-entry expression (trace of
     a product in a1..b3) into a slot holding the SYMBOL z. It returned S4 FALSE. The
     certificate refused to certify -- controls caught my bug, as designed. Fixed, re-run,
     residual 0. *A false negative from a broken instrument, caught by the instrument gate.*
 16. Near-miss: I nearly reported "multiplier = det" as a finding before running the
     prior-art gate. v1 died of exactly that three times. The gate demoted it.

================================================================================
## ADDENDUM (same session) --- G2 UPGRADED, G3 REFUTED AS STATED

### G2 is now proved on all of stratum 1, not sampled
The two-citizen caveat is closed by an argument, not more samples. On generators of
Aut(F_2):
   P: a<->b        multiplier -1   det -1
   I: a->a^-1      multiplier -1   det -1
   U: a->ab        multiplier +1   det +1
Pullback multipliers compose multiplicatively and so do abelianization determinants, so
both are homomorphisms Aut(F_2) -> {+-1}. Agreeing on a generating set, they agree
everywhere. Verified additionally on all 9 length-2 composites. **The law
"Goldman multiplier = det" holds on ALL of stratum 1.** (Still classical -- this is the
orientation-reversing/anti-symplectic dichotomy, now merely made explicit in coordinates.)

### G3 IS FALSE AS I STATED IT
I wrote: "{kappa=2} is exactly where the Goldman form drops rank." **It is not.**
The bivector is 3x3 antisymmetric, so its rank is 0 or 2 -- it can only degenerate at
points, never on a surface. Solving {x,y}={y,z}={z,x}=0 gives **exactly five points**:

   (2,2,2), (2,-2,-2), (-2,2,-2), (-2,-2,2)   kappa = 2   -- nodes of the Cayley cubic
   (0,0,0)                                     kappa = -2  -- node of the Markov surface

Generic points of {kappa=2} (e.g. (1,1,-1), (1,1,2)) are NOT degenerate: checked.

**Corrected statement.** The classical floor {kappa=2} is the Cayley cubic
x^2+y^2+z^2-xyz-4=0; its four nodes are the four CENTRAL characters (each generator
|-> +-I). The Markov surface {kappa=-2} (x^2+y^2+z^2=xyz) has its node at the origin,
which is the QUATERNION character (tr a = tr b = tr ab = 0, i.e. [a,b] = -I).
Degeneracy sits at the singular points of the two special level sets -- not on a floor.

So "erasure = collapse onto the degenerate leaf" is WRONG as phrased. What is true:
stratum 4 lands on the classical floor {kappa=2}; the floor is a symplectic-leaf level
set that happens to be SINGULAR, and full rank-0 collapse happens only at its 4 nodes.

### ONE CANDIDATE FLAGGED, NOT CLAIMED
The kappa = -2 degeneracy point is the **quaternion character**, i.e. Q8. In the
programme's own McKay route (Q(sqrt-3) -> 2T = SL(2,F_3) -> E6), **Q8 is exactly the
kernel of 2T -> Z/3**, and that Z/3 is the element fc's R72 uses for three generations.
Also B497 records that Thue-Morse EJECTS from the Markov surface kappa=-2.
=> Candidate adjacency: the unique irreducible Poisson-degenerate point is the kernel of
the map whose quotient counts generations. **NOT a finding.** It has not had a prior-art
gate (the Fricke-surface singular points are classical -- Cayley, Fricke, Vogt), and
"adjacent structure" is precisely the error class this ledger already logs ten times.
Register it, gate it, do not narrate it.

### LEDGER
 17. **I stated G3 in a form that cannot be true.** A 3x3 antisymmetric bivector has rank
     0 or 2; "degenerates on a surface" is impossible by linear algebra alone. I sealed
     that gate without checking its type. The prereg was right to make it falsifiable;
     it fell on the first contact.
