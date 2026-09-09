# HANDOFF TO cc --- chat1 ("Biri") seat, 2026-09-08
## Subject: the arrow/chirality question, settled where it could be and bounded where it could not

Owner-initiated (Dritero), voice, from a philosophical question. Everything below is
either computed in `verify/` (all four certificates exit 0) or explicitly marked as
banked/classical/candidate. Nothing here promotes to CLAIMS.md.

--------------------------------------------------------------------------------
# 1. THE QUESTION AS THE OWNER POSED IT

Three questions, in this order:
 Q1. Is the unpayable bit (chirality / "direction") a phenomenon like superposition ---
     and could that EXPLAIN superposition?
 Q2. Could the very act of BEGINNING the substitution --- starting to iterate a -> ab,
     b -> a --- be what sets the direction and the chirality?
 Q3. (methodological) Do we keep concluding about the object while ignoring that it has
     many phases and presentations?

Q3 turned out to be the load-bearing one. It was right, and it broke my own first attempt.

--------------------------------------------------------------------------------
# 2. THE a / ab / ba / A / AB / BA REASONING  --- SETTLED, WITH A PROOF

The owner's intuition: the mirror choice at the word level (ab vs ba) might be where
handedness is paid. **It is not. It pays nothing.** `verify/check_word_order.py`:

  sigma_gold  : a -> ab, b -> a
  sigma_mirror: a -> ba, b -> a

  **sigma_mirror = inn_{a^-1} o sigma_gold**, verified by free reduction:
      a^-1 * gold(a) * a = ba = mirror(a)
      a^-1 * gold(b) * a = a  = mirror(b)

  Inner automorphisms act trivially on the character variety, so both induce the SAME
  trace map, verified from generic SL(2,C) matrices with det = 1:
      gold   -> (z, x, xz - y)     residuals 0,0,0
      mirror -> (z, x, xz - y)     residuals 0,0,0     <-- identical
      invert -> (x, y, xy - z)     residuals 0,0,0     <-- different

**CONSEQUENCE.** The word-order mirror is INVISIBLE on X. It is a re-lettering, not a
reflection. This is the C3 pattern again: a candidate bit that turns out vacuous rather
than paid. What IS visible is INVERSION (a -> a^-1, the capital-letter move), which is not
inner and does act on X.

**And note what this does to the substitution itself.** sigma_gold abelianizes to
[[1,1],[1,0]] with **det = -1**. So the programme's own generative rule is already the
orientation-reversing element. Its mirror is itself. The rule does not have a handedness
CHOICE inside it to make --- it has a handedness PROPERTY, and only one.

--------------------------------------------------------------------------------
# 3. THERE IS NO ARROW --- and this corrects the wording of a banked arc

B124 / P006 (already banked, re-read this session): the tower spectrum is EXACTLY
forward/backward symmetric at every rank; expanding count == contracting count. The
two-headed-time reading fits (Carroll-Chen, Boyle-Finn-Turok). The one metallic-specific
asymmetry is **handedness (P), not time-direction (T)**. P006 records that an earlier
"asymmetry = arrow" temptation was already caught and killed.

New this session (section 4): det = -1 is **bracket-REVERSING** (anti-Poisson). That is
reciprocity --- the lambda <-> 1/lambda side of B124 --- not an arrow.

**=> ACTION FOR cc.** S063 says *"the arrow of time enters exactly where det != +-1"*.
B766 says *"time's arrow IS the golden branch"*. These were flagged as needing
adjudication. My recommendation is **retitle, do not choose**: what enters at det != +-1
is LEAF-CHANGE / irreversibility (you leave the symplectic leaf and cannot return), which
is not the same object as an arrow, and B124 says there is no arrow to be had. Both arcs
may be right about their content and wrong in their title.

--------------------------------------------------------------------------------
# 4. WHAT WAS COMPUTED (P-SEAM-02, prereg sealed BEFORE running)

Prereg `P-SEAM-02_prereg.md`, sha256 9a101d59ed1cdc603ff85991ed052c3be11508a0500e5ad43e
7456afa98e5d83. Supersedes P-PHASE-01 (sha256 3094786c...), which was sealed and NEVER
RUN --- retired because its prior was wrong in three places (see section 6).

**G1 TRUE.** B497's kappa and B293's kappa are literally the same object:
tr[a,b] - (x^2+y^2+z^2-xyz-2) = 0 on generic SL(2,C); the coordinate identification
a->ab,b->a |-> (z,x,xz-y) checks out; kappa is Poisson-central; a decoy cubic is not
(negative control fires correctly); B497's three kappa-laws re-derived rather than trusted.

**G2 TRUE, and proved on ALL of stratum 1** (not sampled). On generators of Aut(F_2):
    P: a<->b     multiplier -1, det -1
    I: a->a^-1   multiplier -1, det -1
    U: a->ab     multiplier +1, det +1
Multipliers and determinants are both multiplicative, hence homomorphisms Aut(F_2)->{+-1};
agreeing on a generating set they agree everywhere. All 9 length-2 composites also check.
    **The Goldman bracket multiplier IS the determinant.**
    det = +1 -> Poisson (symplectic)    det = -1 -> ANTI-Poisson (bracket reversed)
    strata 2-4 do not preserve kappa; strata 3,4 have multiplier 0.

**G3 FALSE AS I STATED IT.** I wrote "{kappa=2} is exactly where the form drops rank."
A 3x3 antisymmetric bivector has rank 0 or 2 --- it CANNOT degenerate on a surface. The
degeneracy locus is exactly five isolated points:
    (2,2,2), (2,-2,-2), (-2,2,-2), (-2,-2,2)   kappa=2   nodes of the Cayley cubic
                                                          = the four CENTRAL characters
    (0,0,0)                                    kappa=-2  node of the Markov surface
                                                          = the QUATERNION character
Generic points of {kappa=2} are NOT degenerate (checked). So "erasure collapses onto the
degenerate leaf" is wrong as phrased: stratum 4 lands on the classical floor, and the
floor is a SINGULAR level set whose four nodes are the total-collapse points.

--------------------------------------------------------------------------------
# 5. THE PRIOR-ART GATE --- run BEFORE claiming, and it demoted the result

1. **Goldman owns the invertible half.** His survey (*Mapping Class Group Dynamics on
   Surface Group Representations*) states the mapping class group acts by polynomial
   transformations of C^3 preserving kappa, by symplectomorphisms, with relative character
   varieties as the level sets kappa^{-1}(t). The det=+1 Poisson / det=-1 anti-Poisson
   dichotomy is textbook.
2. **Baake owns the invariant.** VERIFIED HERE: the Fricke-Vogt invariant
   I = x^2+y^2+z^2-2xyz-1 of Baake-Roberts satisfies **4*I(x/2,y/2,z/2) = kappa - 2**
   exactly. Same invariant, half-trace normalization. So B497's kappa-laws are statements
   about Baake's invariant. (Consistent with B497's own Phase-1 gate, which killed the
   P5-monoid paper on Baake-Grimm-Joseph 1993.)
3. **But the gap B497 fills is real, and stated by the literature itself.**
   Baake & Roberts, *Symmetries and reversing symmetries of trace maps*,
   arXiv:math/9901124, classify the reversing symmetry group for the Nielsen class
   (invertible trace maps preserving I, = PGL(2,Z)). Their closing section turns to
   NON-invertible trace maps, notes they are never reversible in that sense, calls for a
   generalized notion covering non-invertible mappings, and says they see nothing close to
   a classification for that case. *(paraphrase --- sec. 4)*
   Independently, Arnoux-Berthe-Hilion-Siegel: the general theory of free-group
   ENDOMORPHISMS is not well understood; most geometric constructions land on automorphisms.
4. **Also near-trivial:** multiplier 0 on strata 3-4 follows from rank-deficient Jacobians
   (Thue-Morse sends both x and y to z). A computation, not a surprise.

**HONEST VERDICT: a propagation, not a discovery.** Registered as OUTCOME B-plus, a
[RHYME]. The value is that **B497 --- banked July, verified ZERO propagation (0 mentions
in B915, B925, B929, B1137, B1126) --- now has a symplectic reading**: its four verbs are
four ways of acting on the Goldman foliation, evolution leaf-preserving, erasure landing
on the classical floor B497 itself named. Architecture, not furniture.

--------------------------------------------------------------------------------
# 6. WHERE CHIRALITY IS ACTUALLY PAID (all banked; re-read, not rediscovered)

The owner's Q2 has an answer already in the corpus, and it is not "at the beginning":

 - **B286**: the Curie argument assumed a CLOSED object. The figure-eight is a
   COMPLEMENT --- open, with a cusp. **Closing it (Dehn filling) IS the symmetry breaking.**
   The cusped object is amphichiral (CS=0); every generic filling is chiral; **the CP sign
   is set by the oriented slope**, CS(p,-q) = -CS(p,q); the selection set is finite and
   forced; and **scale is generated at the seam** (core geodesic ~ 2pi/n).
 - **B289**: the closing's CS sign and the cusp's +-pi/6 sign are TWO FACES OF ONE
   Q(sqrt-3) involution --- and (finding 4) **the sign is NOT object-derivable**.
 - **B1184**: the self-name is mirror-even in every letter, so the sign is unutterable.

So: the object cannot say its own handedness; the closing forces A sign; WHICH sign is a
seam choice. Beginning-to-iterate does not pay it. The word-order mirror does not pay it
(section 2). It is paid at the closing, and only in the sense of being FORCED, not CHOSEN.

--------------------------------------------------------------------------------
# 7. ON Q1 (is the unpayable bit like superposition?) --- BOUNDED, NOT ANSWERED

Standing record, all banked, all AGAINST the strong claim: B725 (Born FORM native, not
content), B726 (hearing face supplies weights only), B728 (Stokes does not close the
phase; zeta_5 IMPORTED), B729 (amplitude sector Q(sqrt phi) is an OVERLAY).
B712: the one continuous modulus has NO canonical real anchor; the only Galois-fixed
point tau = +-2 sqrt-3 is imaginary quadratic with no real embedding.

The session's honest statement: the object has an arena (a continuous modulus with no
canonical real point, and a genuine symplectic structure on it) but the phase CONTENT is
imported. The discrete/continuous mismatch also stands: chirality is one bit; a
superposition is a phase on a circle. They are not the same object as things stand.

--------------------------------------------------------------------------------
# 8. ONE CANDIDATE, FLAGGED AND NOT CLAIMED

The unique kappa = -2 degeneracy point is the **quaternion character** (tr a = tr b =
tr ab = 0, i.e. [a,b] = -I), i.e. **Q8**. In the programme's McKay route
Q(sqrt-3) -> 2T = SL(2,F_3) -> E6, **Q8 is exactly the kernel of 2T -> Z/3** --- and that
Z/3 is what fc's R72 uses for three generations. B497 separately records Thue-Morse
EJECTING from the Markov surface kappa = -2.

**This is an adjacency, not a finding.** The singular points of the Fricke surface are
classical (Cayley, Fricke, Vogt); it has had no prior-art gate; and "adjacent structure"
is the exact error class this ledger already logs ten times. **Gate it before anyone
narrates it.**

--------------------------------------------------------------------------------
# 9. ASKS FOR cc (in priority order)

 1. **Re-adjudicate B1140** vs codex R49 (`spacetime64.py` prints "0 = NO hypercharge
    room" while its own count is 2 = rank 6-4). Still the top ask, unchanged, and it is
    the fourth dead-instrument instance.
 2. **Retitle, don't choose, on S063 vs B766** (section 3). Recommend: what enters at
    det != +-1 is leaf-change/irreversibility, not an arrow.
 3. **Bank the B497 <-> B293 correspondence as an addendum to B497**, marked [RHYME],
    with the Goldman/Baake attribution from section 5. B497 has zero propagation; this
    gives it a reading without over-claiming it.
 4. **Correct my G3 wording anywhere it has been repeated**: {kappa=2} is not a
    degenerate leaf; it is a singular level set with four nodal collapse points.
 5. Gate the Q8 candidate (section 8) or park it. Do not let it travel unchecked.
 6. Numbering collision (main B1277 vs sm:B1277) and the crossed B1277/B1278 attribution
    are still open from the previous handoff.

--------------------------------------------------------------------------------
# 10. ERROR LEDGER --- this session (continuing from 14)

 15. **Broken stratum-4 test**: substituted a matrix-entry expression into a slot holding
     the symbol z; returned a false negative. The certificate REFUSED to certify and
     caught it. Fixed, re-run, residual 0. *The instrument gate worked on me.*
 16. **Near-miss**: I almost reported "multiplier = det" as a finding before running the
     prior-art gate. P-PHASE-01 died of exactly that three times over.
 17. **I sealed a gate that could not be true.** G3 asserted degeneracy on a surface; a
     3x3 antisymmetric bivector has rank 0 or 2 and can only degenerate at points. I did
     not check the TYPE of my own claim before sealing it. Falsifiability saved it --- it
     fell on first contact --- but the prereg should have been type-checked.
 18. **Rediscovery rate, this session: 3 of 4 proposed instruments were already banked**
     (Goldman form = B293; CP sign gate = B289; scale-as-modulus contradicted by B286).
     The standing lesson holds: check the bank BEFORE proposing method, not after.

--------------------------------------------------------------------------------
# FILES
 verify/check_G1.py           G1 + controls                       exit 0
 verify/check_G2.py           G2 strata table                     exit 0
 verify/check_G2G3.py         G2 on all Aut(F2); G3 refuted       exit 0
 verify/check_word_order.py   ab vs ba inner-equivalence          exit 0
 P-SEAM-02_prereg.md          sealed prior (before computing)
 GATE_REPORT.md               results + prior-art gate + addendum
