# R37 — spectra and symmetry rows: B790, B777, B850, B894 (SnapPy + PARI, no Sage)

| row | claim | R37 | verdict |
|---|---|---|---|
| B790 L1 | m004 and m003 are not isospectral despite equal volume | length spectra to Re ℓ ≤ 5: 134 vs 150 geodesic classes; 70 vs 77 distinct real lengths, 43 shared; trace-norm multisets differ | MATCH |
| B790 L2 | every geodesic trace 2cosh(ℓ/2) (134 for m004, 150 for m003) lies in ℤ[ω], worst deviation 2.6e−15 | counts 134 / 150 exactly; worst deviation 1.8e−11 with SnapPy's double-precision lengths (the bank's 40-dps figure is the same statement at higher precision) | MATCH |
| B777 (cc verification of cc3's V4 genericity) | m004 D4 amphicheiral; m003 ℤ/2+ℤ/4 amphicheiral; m025 ℤ/6 amphicheiral; m009, m010 ℤ/2+ℤ/2 not amphicheiral | all five rows reproduced exactly (symmetry group and amphicheirality) | MATCH. Recorded: the silver bundle b++RRLL = m136 is D4 and amphicheiral like m004; m015/m016 (5₂ and its sister) are not. |
| B850 | length-spectrum "multiplicity" maxima m004 4, m003 3, m136 4, m009 8, m015 2 (holonomy-word counts at 40 dps) | SnapPy complex-length classes to Re ℓ ≤ 4: max multiplicity m004 12, m003 12, m136 11, m009 11, m015 6 (means 4.58, 4.02, 3.92, 3.89, 2.35) | the bank's numbers are word-count artefacts of its own enumeration, not geometric multiplicities (B850 itself later called Cell 4 "an artifact"); the qualitative ordering arithmetic (≈11–12) > non-arithmetic (6) survives, the specific "m009 = 8 exceeds m004 = 4" comparison does not (both ≈ 11–12) |
| B894 | K = ℚ[x]/(x³−12x−5): disc 6237 = 3⁴·7·11, monogenic, 5 unramified, S₃ closure | poldisc = nfdisc = 6237 = 3⁴·7·11 (index 1), Galois S₃, signature (3,0), 5 = 𝔭₁𝔭₂ with e = 1 | MATCH |

**Physics content:** none. "No observable content."
