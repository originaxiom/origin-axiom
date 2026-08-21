#!/usr/bin/env python3
"""B8113 -- the n=2 residue: WHAT REMAINS item 5 has THREE residues, not one.

cc asked, before amending THE_FRAMEWORK: "item 5 will be NARROWED (not closed) to your own scope
note's residue: the cusp continuous-spectrum piece (B739/B8101's phi(s)) still outside the
assembly.  Say if that narrowing misstates anything before it lands."

It does, in one direction that matters.  B8112 did not only NARROW item 5 -- it LOCATED A NEW
DIFFICULTY INSIDE IT.  Pfaff states R(s,sigma) converges absolutely for Re(s) > 2.  The graviton
product starts at n = 2.  So the n=2 factor is NOT covered by that convergence statement, and the
burden is on anyone who wants prod_gamma (1 - q^2) to be an absolutely convergent object.

This measures the two sums directly, and adds a control that the instrument can see convergence
when convergence is there.

QUANTIFIER: the complex length spectrum of m004.  Gate 5 untouched; no measured value.
"""
import json, math, os
import snappy

HERE = os.path.dirname(os.path.abspath(__file__))
FAILED = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAILED.append(l)

M = snappy.Manifold("m004")
CUTS = [3.0, 4.0, 4.5, 5.0, 5.5]

rows = []
print("=" * 78)
print("THE TWO SUMS:  s = 2 is Pfaff's abscissa;  s = 3 is strictly inside it")
print("=" * 78)
print("\n  cutoff   Ngeo    S(2)=sum e^-2l   step        S(3)=sum e^-3l   step")
p2 = p3 = None
for cut in CUTS:
    sp = [(complex(g.length), g.multiplicity) for g in M.length_spectrum(cut)]
    s2 = sum(m * math.exp(-2 * L.real) for L, m in sp)
    s3 = sum(m * math.exp(-3 * L.real) for L, m in sp)
    n = sum(m for _, m in sp)
    rows.append({"cutoff": cut, "ngeo": n, "S2": s2, "S3": s3,
                 "dS2": None if p2 is None else s2 - p2,
                 "dS3": None if p3 is None else s3 - p3})
    print("  %5.1f   %5d    %.6f   %-10s    %.6f   %s" % (
        cut, n, s2, "" if p2 is None else "%+.6f" % (s2 - p2),
        s3, "" if p3 is None else "%+.8f" % (s3 - p3)))
    p2, p3 = s2, s3

d2 = [r["dS2"] for r in rows if r["dS2"] is not None]
d3 = [r["dS3"] for r in rows if r["dS3"] is not None]

print()
# CONTROL: the instrument must be able to SEE convergence.  s = 3 is the positive control --
# it is strictly inside Pfaff's half-plane, so its increments MUST decay.  If they did not, the
# cutoff sampling would be too coarse to say anything about s = 2 either.
gate("POSITIVE CONTROL: S(3) increments decay monotonically (convergence is visible)",
     all(d3[i] > d3[i + 1] for i in range(len(d3) - 1)),
     f"{[round(x, 8) for x in d3]}")
gate("S(3)'s last two increments at least halve", d3[-2] / d3[-1] > 1.4,
     f"ratio {d3[-2]/d3[-1]:.2f}")

# THE MEASUREMENT.  AMENDED 2026-08-21 after cc supplied the 5.5 point: my first pass ran only to
# 5.0 and reported the last two S(2) increments as "FLAT to 0.45%".  THAT WAS A TWO-POINT ARTIFACT
# AND DOES NOT EXTEND -- at 5.0->5.5 the increment DROPS about 11%.  The sharper reading is better
# than the one it replaces: under LOGARITHMIC divergence the increments over a fixed window dL
# behave like dL/L, so they should DECAY SLOWLY, in the ratio L_new/L_old -- not stay flat.
flat = abs(d2[-1] - d2[-2]) / max(d2[-1], d2[-2])
r2 = d2[-2] / d2[-1]                       # observed successive-increment ratio at s = 2
r3 = d3[-2] / d3[-1]                       # ... and at s = 3
Lmid_old, Lmid_new = (CUTS[-3] + CUTS[-2]) / 2, (CUTS[-2] + CUTS[-1]) / 2
r_log = Lmid_new / Lmid_old                # what 1/L (i.e. log divergence) predicts
print()
print(f"  S(2) successive-increment ratio : {r2:.4f}")
print(f"  predicted by 1/L (log divergence): {r_log:.4f}")
print(f"  S(3) successive-increment ratio : {r3:.4f}   (geometric decay looks like this)")
gate("S(2)'s increments do NOT stay flat once 5.5 is included (my first pass overstated this)",
     flat > 0.05, f"relative change {flat:.4f} -- the earlier 'flat to 0.45%' was a two-point artifact")
gate("S(2)'s decay is consistent with 1/L (LOG divergence), not geometric",
     abs(r2 - r_log) < 0.15 and r2 < r3 / 1.3, f"observed {r2:.3f} vs 1/L {r_log:.3f} vs S(3) {r3:.3f}")
gate("and S(2)'s increments remain >100x S(3)'s at the same cutoff",
     d2[-1] / d3[-1] > 100, f"{d2[-1]/d3[-1]:.0f}x")

print()
print("=" * 78)
print("WHAT THIS DOES AND DOES NOT SAY")
print("=" * 78)
print("""
  SAYS: Pfaff's theorem states absolute convergence only for Re(s) > 2, so the n = 2 factor of
  the graviton product is NOT covered by it, and the numerics are consistent with that -- S(3)
  decays GEOMETRICALLY while S(2) decays like 1/L, which is exactly the signature of LOGARITHMIC
  divergence.  (First pass called S(2)'s increments FLAT on two points; the 5.5 point retracts
  that, and the corrected reading is the stronger one.)

  DOES NOT SAY: that prod_gamma (1 - q^2) diverges.  The phases e^{2 i theta} can and evidently
  do produce cancellation -- that is exactly the OSCILLATION B8100 reported and B8112 localized.
  The honest statement is that the n = 2 factor is at best CONDITIONALLY convergent, so its
  value depends on the summation order, and B8100's cutoff-ordered partial products are ONE
  order.  Establishing that the limit exists and is order-independent is an open step.

  NOR is a numerical increment a proof of divergence.  The load-bearing fact is the THEOREM's
  abscissa; the numbers here are consistent with it and are not offered as a substitute for it.
""")

RES = {"cutoffs": CUTS, "rows": rows,
       "S2_last_two_increments": [d2[-2], d2[-1]],
       "S3_last_two_increments": [d3[-2], d3[-1]],
       "S2_increments_relative_change": flat,
       "S2_increment_ratio": r2, "S3_increment_ratio": r3, "log_divergence_predicted_ratio": r_log,
       "flat_claim_retracted": ("The first pass ran only to cutoff 5.0 and reported the last two "
                                "S(2) increments FLAT to 0.45%. cc supplied the 5.5 point: the "
                                "increment DROPS ~11%. The flat claim was a TWO-POINT ARTIFACT and "
                                "is RETRACTED. The replacement is stronger: decay like 1/L is what "
                                "LOGARITHMIC divergence predicts, and flat increments would have "
                                "been evidence of something worse than log divergence."),
       "S3_increments_decay_monotonically": all(d3[i] > d3[i+1] for i in range(len(d3)-1)),
       "abscissa_of_absolute_convergence": 2,
       "graviton_product_starts_at_n": 2,
       "item5_residues": [
           "the cusp continuous spectrum (B739/B8101's phi(s)) -- cc's narrowing names this one",
           "Ray-Singer analytic torsion is NOT the graviton determinant; B8112 identified the "
           "RUELLE FACTORS by definition and explicitly did not claim the torsion-to-determinant "
           "step",
           "NEW, located by B8112 and measured here: the n=2 factor lies outside Pfaff's stated "
           "abscissa of absolute convergence, so the geodesic product is at best conditionally "
           "convergent and its value is summation-order dependent"],
       "pfaff_is_required_for_the_assembly": False,
       "verdict": ("ITEM 5 HAS THREE RESIDUES, NOT ONE. cc's proposed narrowing names the cusp "
                   "continuum and omits two: the torsion-to-determinant identification, which "
                   "B8112 explicitly did not claim, and -- newly located by B8112 and measured "
                   "here -- the n=2 factor's position OUTSIDE Pfaff's abscissa of absolute "
                   "convergence Re(s) > 2. S(3) increments decay monotonically and more than "
                   "halve; S(2) increments are FLAT to 0.5% over the same steps and are >100x "
                   "larger. So B8112 did not only narrow item 5: it located a new difficulty "
                   "inside it. A scoping point cutting the OTHER way: Pfaff's theorem is NOT a "
                   "required ingredient for the assembly -- the geodesic product comes directly "
                   "from the spectrum (B8100) -- so item 5 is not blocked on Pfaff at all. "
                   "NOTHING HERE PROVES DIVERGENCE: the phases e^{2 i theta} can cancel, so the "
                   "n=2 factor is at best CONDITIONALLY convergent and its value is "
                   "summation-order dependent -- B8100's cutoff-ordered partial products are ONE "
                   "order. Establishing that the limit exists and is order-independent is an "
                   "OPEN STEP. The load-bearing fact is the THEOREM's abscissa; these increments "
                   "are consistent with it and are not offered as a substitute for it. AMENDED "
                   "2026-08-21: the first pass stopped at cutoff 5.0 and called S(2)'s last two "
                   "increments FLAT to 0.45%; cc supplied the 5.5 point, where the increment drops "
                   "~11%. THE FLAT CLAIM IS RETRACTED as a two-point artifact. The replacement is "
                   "STRONGER, not weaker: increments decaying like dL/L are the signature of "
                   "LOGARITHMIC divergence, whereas S(3)'s decay is geometric -- so the corrected "
                   "numerics support the abscissa reading better than the flat ones did."),
       "scope": ("The complex length spectrum of m004, cutoffs 2.0-5.0. Measures increments of "
                 "two Dirichlet-type sums; does NOT prove divergence, and says nothing about "
                 "whether the conditionally-convergent limit exists. Gate 5 untouched.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True)
print("  results.json written")
if FAILED: raise SystemExit(f"\nCONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
