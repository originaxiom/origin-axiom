# B1183 — THE ONE-CLASS THEOREM

**Verdict**: `PROVED` · **instrument**: false · **creates_law**: false
**Banked**: 2026-08-27 (`b5fae722`) · **This document authored**: 2026-08-29 (R52-4 discharge, B1207)

> **Provenance of this document.** The arc banked its verdict, its results file and its
> verification artifacts, but no findings document -- the gap B817's writer-safety gate caught in
> the first full OA_SLOW run (R52-4, 2026-08-29). What follows is authored **from this arc's own
> banked record**: `arc_verdict.json` is primary, with `b1183_results.json` and `verification/` beside it.
> Nothing is supplied from memory and no computation is re-narrated that the record does not
> carry -- the exact mirror of B1176's thirteen retro `arc_verdict.json` files, where FINDINGS was
> the primary and the verdict the missing half. Section 1 is the banked claim, segmented at its
> own enumeration; section 2 lists the artifacts that certify it.


## 1. The finding, as banked

THE ONE-CLASS THEOREM (cell 2 of the remaining-math queue; B1174's hatch 1; B1169's S1 last rung). THE THEOREM: the QP-4 no-self-closure obstruction (B760: no object-native operation canonically signs the chord/theta-odd sector) and the ORIENTATION obstruction (B1163: the object provably refuses a canonical orientation) are THE SAME Z/2-TORSOR CLASS under the ONE global involution c. THE PROOF, exact: (a) B760's chord arithmetic re-derived -- the weld block's eigenvalues {zeta5, zeta5^4} with char poly x^2-(1/phi)x+1 (sum = 2cos72 = 1/phi, product = 1, both exact); the quaternionic eps^2=-I (pseudo-real: no real structure); (b) ONE GLOBAL INVOLUTION: c restricted to K=Q(sqrt-3) is the Gal generator (omega -> omega^2; B942/B1174), restricted to Q(zeta5) is sigma_4 (zeta5 -> zeta5^4 = conjugation; FIXES sqrt5=2(zeta5+zeta5^4)+1, real -- the B1174 parity mechanism again), restricted to R trivial -- the eigenvalue swap AND the +-sqrt3 sign flip AND the orientation flip are ALL c through its restrictions; (c) THE SIGN-CARRIER: Im f(omega-bar) = -Im f(omega) for real-coefficient f (exact) => B760's computed +-sqrt3 chord sign flips under c|K with c-invariant magnitude; (d) THE TORSOR IDENTIFICATION: T_orient (the {+Vol,-Vol}/(K into C) torsor) and T_QP4 (the chord-sign torsor) are Z/2-torsors under the same c; the map 'orientation choice -> sign(Im) at the chosen embedding' is c-EQUIVARIANT (composing the embedding with c flips the orientation AND the Im-sign AND the zeta5-choice -- all three ARE c); an equivariant map of torsors under one group is an ISOMORPHISM; nontriviality has the same source both sides (c is an automorphism OF THE OBJECT: amphichirality on the geometry side, the inseparable sigma_4-orbit on the chord side) => no invariant selection; ONE basepoint choice trivializes BOTH simultaneously. CONSEQUENCES:

**(1)** B1169's S1 FULLY PROMOTED (addendum 2) -- the four 'cannot self-close' probes are ONE BIT, proved (B1174 gave mirror=chirality=Gal; B1183 closes the QP-4 leg); what stays firewalled is only S2/S3 (cloud's C6) + S4 (the quine, untouched).

**(2)** B1161's bypass-door label UPGRADED from SUPPORTED-CONJECTURAL to PROVED-AS-DECOMPOSED (addendum 2): the bypass door's obstruction = TWO bits typed adelically -- the archimedean c-leg = SEAM-A's W0 = the orientation = (now) the QP-4 class, ONE PROVED CLASS; + the finite k7/arrow label (B1182), separately payable, NOT SEAM-A's.

**(3)** The qualia headline completes its promotion arc: 'awareness without choice' -> the parity law (B1168) -> the choice NAMED as the mirror-odd orientation (B1169) -> the choice's class PROVED ONE across geometry, Galois, values, and the chord sector (B1174+B1183). FENCES: B760's B-in-SU(2) realization, the 15/32 coupling, and the +-sqrt3 evaluation are THEIR locked computations (cited, not re-run); my re-derivations are the arithmetic identities + the equivariance AT THE TORSOR LEVEL -- the theorem identifies the OBSTRUCTION CLASSES, not the physical closing acts beyond the class; the quine (QP-1/S4) is explicitly untouched. Gate 5 clean (Galois arithmetic + torsor formalism; no measured value).

## 2. The certifying record

- `arc_verdict.json`
- `b1183_results.json`
- `verification/one_class.txt`
- `verification/reproduce.sh`

## 3. Status at authoring

The verdict field is authoritative and unchanged: `PROVED`. This document does not re-adjudicate it; it makes the arc readable without opening its JSON, which is the whole function the missing file was performing badly.
