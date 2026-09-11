"""CERTIFICATE -- K3 RUN: memo 195 section 4's hypothesis sorted against the sealed text, and KILLED.

THE HYPOTHESIS (memo 195 section 4, fenced and never banked as a law): that the seven-for-seven
crossing exhaustion is STRUCTURAL -- a measured dimensionless value is a magnitude WITH an
orientation; by Dirichlet the magnitude can only come from hearing (unit rank 1) and the
orientation only from being or meeting (rank 0, c nontrivial); no quadratic face carries both; so
every crossing that asked one face for a value asked it for a commodity it provably lacks.

THE KILL CONDITIONS, fixed in memo 195 section 4 BEFORE any sorting:
  K1  a banked result deriving ORIENTATION from HEARING        -> one found kills it
  K2  a banked result deriving GROWTH from BEING               -> one found kills it
  K3  sort the seven FROM THE SEALED TEXT.  Ambiguous classification -> VACUOUS, dies.
      A crossing that asked a face for its OWN commodity and still missed -> FALSE.
  K4  a banked POSITIVE requiring both commodities from one face -> one found kills it

B1222 was cited in advance as the precedent and the warning: it proposed a unification of the
programme's ~65 vanishings, named three kill conditions, and died on them.

This runs K3.  Every classification below quotes the arc's own sealed claim line.
"""
import sys

# (arc, what the object side supplied, which face that is, what was asked of it, outcome)
SORT = [
 ("B915",
  "the banked gauge boundary sin^2thetaW = 3/8 from the exact E6 traces, plus the two-loop SM-desert curve",
  "BEING (E6 arrives through 2T through Q(sqrt-3))",
  "alpha_s(M_Z) -- a RUNNING coupling, i.e. GROWTH",
  "MISS 15.97 sigma, and ALPHA_S-DOMINATED: 'gap +0.041 vs +0.002 in sin2thetaW'"),
 ("B925",
  "the compact D-chain's own algebra",
  "BEING",
  "an RG LADDER -- GROWTH",
  "OUTCOME B: rungs RG-DEGENERATE (M3=M4=M5), the E6 rung 'RG-invisible'"),
 ("B929",
  "the m_S flip-mass structure",
  "BEING (the frame / the 27)",
  "CKM mass RATIOS -- MAGNITUDES",
  "TIER 1 shape HIT (cascade, index in band); TIER 2 ratios MISS 'by factors 5-9'"),
 ("B1027/B1063",
  "the chi phases {+-2pi/3} -- the arguments of omega, i.e. being's mu_6 units",
  "BEING (a TRIT: three points on the circle)",
  "delta_CP -- a CONTINUOUS phase",
  "MISS 11.4 sigma / 38 sigma quark; refresh: eight pairs, eight misses"),
 ("B1066 R-A",
  "the listener pair, value 0.27639 = |S_tautau|^2, a phi-expression",
  "HEARING (phi-geometric)",
  "sin^2 theta_12 -- a MAGNITUDE",
  "MISS 4.7 sigma"),
 ("B1066 R-B",
  "the phi-geometric tone row, anchor phi/2 = 0.80902",
  "HEARING (the record's own words: 'the phi-geometric row')",
  "|U_e1| -- a MAGNITUDE",
  "MISS 3.4 sigma, 'unrescuable'"),
 ("B1075",
  "the same tones, 1/2 and 1/(2phi)",
  "HEARING",
  "PMNS MODULI -- MAGNITUDES",
  "MISS AT POWER, 'about 5 sigma below |Ue2|'s 3-sigma edge'"),
]

print(__doc__)
print("=" * 78)
for arc, src, face, asked, out in SORT:
    print(f"\n  {arc}")
    print(f"    object side : {src}")
    print(f"    face        : {face}")
    print(f"    asked for   : {asked}")
    print(f"    outcome     : {out}")

print()
print("=" * 78)
print("THE VERDICT ON K3")
print("=" * 78)

own_commodity_misses = [a for a, s, f, q, o in SORT
                        if f.startswith("HEARING") and "MAGNITUDE" in q.upper()]
print(f"""
  Crossings that asked a face for its OWN commodity and still missed: {len(own_commodity_misses)}
    {', '.join(own_commodity_misses)}

  Hearing's commodity IS multiplicative magnitude -- unit rank 1, the fundamental unit phi,
  the regulator.  All three of these asked hearing whether a measured ratio equals a
  phi-expression.  That is hearing being asked for exactly what hearing has.  All three
  MISSED, at 4.7, 3.4 and about 5 sigma.

  K3's FALSE branch fires.  THE HYPOTHESIS IS REFUTED -- not vacuous, FALSE, which is the
  more informative of the two deaths available to it.

  SECOND TIME.  B1222 proposed a unification of the programme's ~65 vanishings, named its
  kill conditions in advance, and died on them.  Memo 195 section 4 cited B1222 as the
  precedent when it wrote these conditions.  The discipline worked twice.
""")
print("  WHAT SURVIVES, as observations and NOT as a law:")
print("""
   1. B915's miss is ALPHA_S-DOMINATED by a factor of about 20: the gap is +0.041 in the
      RUNNING direction against +0.002 in the trace-fixed boundary ratio.  The boundary
      value -- being's own commodity -- was nearly right; the growth direction was not.
   2. B929 HIT on shape and MISSED on magnitude: the discrete cascade ordering landed in
      band, the ratios were off by 5-9x.
   These two are consistent with the complementarity.  Three others are not.  Two
   supporting instances out of seven is a tendency, and a hypothesis that fails its own
   decisive test is refuted, not partially confirmed -- B1222's exact wording, applied here
   to my own.

  WHAT IS UNTOUCHED: memo 195 sections 1-3.  The complementarity is Dirichlet's unit
  theorem and the five-arcs-never-joined measurement is a count.  Neither depended on this.

  AND THE CONSEQUENCE FOR THE GOAL: section 4A.0's fourth leg STAYS EMPIRICAL.  The
  seven-for-seven needs no type story; it is what it looks like -- the object's numbers are
  not nature's numbers.  The document was right to call it exhaustion rather than theorem,
  and the attempt to upgrade it fails.
""")
sys.exit(0)
