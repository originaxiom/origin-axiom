# PREREGISTRATION --- P-SEAM-02
## Are the four verbs (B497) the action on the Goldman symplectic foliation (B293)?
### i.e. is unitary evolution leaf-preserving, and is "collapse" the degenerate leaf?

seat: chat1 ("Biri"), 2026-09-08. Owner-initiated (Dritero), voice.
SUPERSEDES: P-PHASE-01, sha256 3094786ce532aa7141e4f383ea701c657cce9ad168465e0a059df85403c0de47
   (v1 stays sealed on the record, unamended and unrun. It is superseded because its
    prior was wrong in three places -- see section 1. No result was computed under it.)
firewall: rung-1 only. No SM value fit in the critical path.

--------------------------------------------------------------------------
## 0. WHY v1 WAS RETIRED (three refutations from the initial work)

Reading philosophy/P000-P021 and the seam arc B286-B297 broke v1's prior:

 (i)  **v1 assumed an arrow to pay for.** B124 / P006: the tower spectrum is EXACTLY
      forward/backward symmetric at every rank -- expanding count == contracting count.
      THERE IS NO ARROW. The one metallic-specific asymmetry is HANDEDNESS (P), not
      time-direction (T). v1's T4 was built from the wrong end.
 (ii) **v1's T1 instrument is banked.** B293 already has the Goldman bracket on X(4_1),
      {x,y}=2z-xy etc., kappa = x^2+y^2+z^2-xyz-2 as the CASIMIR, symplectic leaves
      {kappa=const}, peripheral (mu,lambda) a canonical conjugate pair, cross-verified
      against the Neumann-Zagier frame (B263). Proposing it as method was rediscovery.
 (iii)**v1's chirality gate is banked.** B289: all 78 hyperbolic closings chiral,
      CS(p,-q) = -CS(p,q) exactly, and the closing's CS sign and the cusp's +-pi/6 sign
      are TWO FACES OF ONE Q(sqrt-3) involution. Also: the sign is NOT object-derivable
      (finding 4). The gate I wrote already has its answer.
 Also contested: v1 sec.2 lists R_+ (scale) as a free continuous modulus; B286 finds
      SCALE IS GENERATED AT THE SEAM (core geodesic ~ 2pi/n). v1 is wrong, not B286.

--------------------------------------------------------------------------
## 1. THE CLAIM UNDER TEST (the one thing NOT banked)

B497 (PROVED, banked July, **verified zero propagation** -- 0 mentions in B915, B925,
B929, B1137, B1126) stratifies End(F_2) into four verbs by determinant:

  1. Aut, det +-1        "evolution"        kappa' = kappa                (kappa PRESERVED)
  2. inj, |det| >= 2     "renormalization"  kappa'-2 = (kappa-2)x^2y^2
  3. inj, det 0          "decoherence"      Thue-Morse, singular on every abelian shadow
  4. non-inj             "erasure"          image contained in {kappa = 2}
  universal: kappa=2 invariant under every endo; (kappa-2) | (kappa'-2) always.

B293 (PROVED, independently) shows that on X(4_1) the SAME kappa = tr[a,b] is the
**Casimir of the Goldman bracket**, so {kappa = const} are exactly the SYMPLECTIC LEAVES.

**THE CLAIM:** these are one structure, not two. The four verbs are the four ways an
endomorphism can act on the symplectic foliation:
  - stratum 1 (det +-1) is LEAF-PRESERVING -- a Poisson map -- i.e. the structural
    analogue of unitary/Hamiltonian evolution;
  - strata 2-3 MOVE the leaf;
  - stratum 4 collapses onto {kappa = 2}, and {kappa=2} is conjectured to be exactly
    where the Goldman form DEGENERATES -- the structural analogue of collapse.

If true, the quantum-phase question the owner asked ("is superposition native?") has a
native answer in the object's OWN banked material: unitarity = staying on a leaf,
measurement = leaving it -- with no imported constant, hence untouched by B728/B729's
"phase is imported" verdict, which was about zeta_5 and Q(sqrt phi), NOT about kappa.

--------------------------------------------------------------------------
## 2. GATES (declared before computing)

 G1 IDENTITY. B497's kappa and B293's kappa are the SAME polynomial
    x^2+y^2+z^2-xyz-2 = tr[a,b] on the F_2 character variety. Verify as an identity,
    not a resemblance. If they differ, this is a NAME COLLISION and the probe dies here.
 G2 POISSON. Stratum 1 (det +-1) acts on X(4_1) preserving the Goldman bracket
    (a Poisson/symplectomorphism action); strata 2-4 do NOT. Test both directions --
    a positive on stratum 1 with no negative on strata 2-4 is NOT a pass.
 G3 DEGENERACY. {kappa = 2} is exactly the locus where the Goldman form drops rank
    (the degenerate leaf / the reducible or binary-dihedral locus). Stratum 4's image
    lands there. Compute the rank of the bracket matrix on and off kappa=2.
 G4 ADJUDICATION. Two banked accounts of the same bit, no cross-citation:
    S063 "the arrow of time enters exactly where det != +-1"  vs
    B766 "time's arrow IS the golden branch" (gamma_5, (1-phi)^2 = phi^-2).
    Under G2 these unify iff leaving the leaf first happens at the golden branch.
    Registered: this may resolve as TWO DIFFERENT BITS. Do not force a unification --
    the arrow/CP unification was already killed once (three independent regimes).

TRUE requires G1 AND G2 AND G3. G4 is reported either way, never used to rescue G2.

--------------------------------------------------------------------------
## 3. CONTROLS (a negative from an uncontrolled instrument is not a negative)

 C-alive   : recompute {kappa, x} = {kappa, y} = {kappa, z} = 0 symbolically from the
             Goldman relations. MUST reproduce B293's Casimir. If it fails, every null
             below is VOID.
 C-null    : a random degree-3 polynomial in (x,y,z) of comparable shape must NOT be
             Poisson-central. If it "is", the algebra is being computed wrong.
 C-vacuity : if EVERY endomorphism preserves kappa (not just stratum 1), G2 is vacuous
             -- report FALSE-BY-VACUITY, do not dress it as a pass. (This is the C3
             failure mode: an involution that made the choice vacuous rather than paid.)
 C-collision: G1 must compare polynomials, not names. B497's kappa is defined on F_2;
             B293's on the once-punctured-torus character variety. Same object requires
             the same generators -- check the identification explicitly.

Certificate exits 0 only if C-alive PASSES, C-null FAILS, C-vacuity does not fire, and
the G-verdicts are mutually consistent. No unconditional success line may be printed.

--------------------------------------------------------------------------
## 4. REGISTERED OUTCOMES / STOPPING RULE

 A (structural): G1+G2+G3 all true. The four verbs ARE the symplectic dynamics;
   leaf-preserving = the unitary sector; {kappa=2} = the collapse locus. This would be
   genuinely new (B497 has provably never propagated) and MUST be re-derived a second
   independent way before it leaves the seat.
 B (arithmetic only): G1 true, G2 false. The monoid is an arithmetic stratification that
   does not respect the Poisson structure. The correspondence is a [RHYME], filed to
   philosophy/, promoted nowhere.
 C (collision): G1 false. Two different kappas. Dead, recorded, one line.

PRE-COMMITTED PRIOR: G1 very likely TRUE (both are tr[a,b] on the F_2 character
variety). G2 is the real risk and the honest coin-flip. G3 is the one I expect to be
messiest -- "degenerate leaf" may be several strata, not one.
Most likely outcome: **B**. Outcome A is the only one worth a second instrument.

--------------------------------------------------------------------------
## 5. WHAT THIS PROBE DOES NOT CLAIM

No physical time (P006/P011: iteration-count is not cosmic time; the firewall stands).
No arrow derived (B124: there isn't one). No chosen sign (B289 finding 4: the closing
forces A sign, which sign is the seam choice). No Born CONTENT (B725/B726 stand: form
yes, content no). No SM value. If A holds, the result is a STRUCTURAL correspondence
between a banked monoid and a banked foliation -- an architecture claim, not furniture.

--------------------------------------------------------------------------
## 6. ERROR-LEDGER DISCIPLINE (carried)

 - any quoted arc string is grepped before it ships (anti-fabrication rule, error 12).
 - `git grep --all` is BANNED: it parses as --all-match and silently searches nothing
   (error 14, produced 14 false ABSENT verdicts).
 - the pass line is computed from the controls, never hardcoded (error 11).
 - a null from a control-failing instrument is reported VOID, not as a null.
 - "already banked" is checked BEFORE proposing method (this prereg exists because
   v1 failed that check three times).

sha256(body-above) = 9a101d59ed1cdc603ff85991ed052c3be11508a0500e5ad43e7456afa98e5d83
sealed_utc = 2026-09-08T19:49:19.111609+00:00Z
