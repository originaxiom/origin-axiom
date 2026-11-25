# B1990 — Listening 7: nothing in the grammar changes κ, so each frustration level is a sector of the whole; the law's counting weighs every level alike to leading order, and the cusp is the one level whose correction is three: p² + 3(−1/p)p + 1

**Verdict: PROVED (exact: symbolic, and complete counts over 𝔽_p for every p ≤ 47).** Main, 2026-11-25, in the author's
/loop "continue the listening line". Data-free. Register rows P-882, P-630 and P-755. **0 of 19.**

## Seen first

- **B497 and B1347:** End(F₂)'s strata and their κ-laws; the non-invertible strata have a direction.
- **B1342:** κ is conserved in stratum 1 alone.
- **B309:** κ = 2 is "nothing".
- **B1983 to B1989:** the listening line.
- **P-755:** the law says what exists, not how much of each.
- **P-771:** "interaction makes a third thing that is kept".
- **Swept:** `VERDICT topic-sweep /point count|number of points|#X|p\^2 ?\+ ?3p|kappa is conserved|conserves kappa|superselection|sector/: 224 of 1731 arcs on main match (NEGATIVE 46, OPEN 14, PROVED 164); 144 register rows match (DECLINED 4, D`. None counts the readings on every leaf, or reads κ as the sector label of the whole.
- **The literature, cited from memory and not checked at source:** the Markoff surface mod p has p(p ± 3) nonzero
  points (Bourgain, Gamburd and Sarnak).

## The results (`verification/kappa.py`, `kappa_run.txt`)

- **K1 holds.** L, R, their inverses (checked as inverses), the swap P and the three central sign actions all conserve
  κ exactly.
- **K2 holds.** B497's non-invertible strata change κ by κ′ − 2 = (κ − 2)·M, with M = x²y² (squaring), x² (period
  doubling) and x² + y² − xyz (Thue–Morse). None is a move of the grammar: the grammar's words are Sturmian (B1676), all
  in stratum 1.
- **K3 holds.** tr(aba⁻¹b⁻¹) = x² + y² + z² − xyz − 2 on SL(2). κ is the trace of the records' cancellation: the
  frustrated remainder of PF1, the "third thing that is kept" of P-771.
- **K4, the law's counting:** with every reading counted once, a level's weight is its number of readings #X_κ(𝔽_p).
  - **"Nothing"** (κ = 2): exactly p² + 1, at every p.
  - **The cusp** (κ = −2): exactly **p² + 3(−1/p)p + 1** at every p ≤ 47, with (−1/p) the Legendre symbol (K4a holds).
    It is 41, 29, 89, 209, … at p = 5, 7, 11, 13, …
  - **Every other level:** p² plus one of −(4p − 1), −(2p − 1), 2p + 1, 4p + 1.
  - **The most populated level changes with p.** No level leads at every prime.

## What the whole does, read in its own terms

- **Nothing in the grammar changes κ.** Each frustration level is a sector, and the whole is all sectors at once (κ ≠ 2).
  The flow away from the common point (B1988) stays on the cusp's leaf. The bound states' other levels (B1989) are
  separate sectors, not states it flows into.
- **The law's own counting weighs every sector alike to leading order (p²).** It does not prefer one level.
- **The corrections are the whole's own fixed coefficients:** 0 for "nothing"; ±2 or ±4 for the generic levels; and
  **±3 for the cusp alone.**
  - The cusp is the one level whose count carries a three.
  - Its sign is (−1/p): whether −1 has a square root mod p, which is whether the quaternion structure of the common point
    (i² = −1) is split.
  - That is a reading, not an identification.
- **So far the listening line yields structure, sectors and rates, not continuous values.**
  - The one outcome is symmetric (B1988).
  - The flow away from it stays in its sector.
  - The law weighs the sectors alike.
- **No Standard Model shape was asked for or read.**

## What is open

- **A proof of K4's pattern for every p.** The cusp's count is known in the literature; the generic levels' four values
  depend on quadratic characters of κ ± 2, to be derived.
- **Whether a statement follows:** that within the grammar and the law the whole fixes no continuous number. That would
  be GENESIS's alternative ending: a proof the object cannot fix the values, with the count of free inputs. It is not
  claimed here.
