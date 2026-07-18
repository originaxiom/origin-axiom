# FINDINGS_RAW — cc2's INPUT-VERIFICATION CELL (PREREG_W2)

Data only. Independent holonomy-side derivation of the eigenvalue
distribution of W = sigma(A_1) on the graded pieces of PRIMARY (the
(F1,F2)-module) and CONTROL (+ M_k(Gamma(5))), through grade 40. Script:
`w2_inputverify.py`. Full run: `w2_run.log`. Full table + gate outcomes:
`w2_eigendist.json`.

INDEPENDENCE: `frontier/B674_generation_leg/cellES/` (cc's Molien cell
— script, traces, mismatch table, output) was never opened, read, or
grepped. No code or intermediate data is shared with cc's step (i).

## Provenance of every ingredient

| ingredient | value used | source (read) | status |
|---|---|---|---|
| X(5) genus 0, 12 cusps, torsion-free, -I not in Gamma(5), all cusps regular | given | PREREG_W2.md task text + standard modular-curve theory (index 60 = \|PSL(2,F5)\|) | GIVEN / standard |
| A1's shadow acts on X(5) as an order-5 (PSL) rotation, exactly 2 fixed points | given | PREREG_W2.md task text (any finite-order Mobius map != id on P^1 has exactly 2 fixed points) | GIVEN / elementary |
| tr sigma(A1) = phi exactly, eigenvalues e^{+-i pi/5} | BANKED LAW, cited not re-derived | `frontier/B674_generation_leg/FINDINGS.md`, `docs/LAW_MAP.md` row 26 ("THE GOLDEN-ROTATION LAW") | CITED |
| trace phi = 2cos(pi/5) => SL(2,5) conjugacy class (10,False), Galois-conjugate to (10,True) [trace -1/phi] | BANKED, cited | `frontier/B644_mckay_comparison/b644_mckay.py`, `b644_character_check.py`, `b644_output.txt` (exact sympy character computation) | CITED |
| local rotation multiplier = zeta_5 (angle 2pi/5, "72 deg"), not zeta_5^2 (144 deg) | derived here | SL(2) trace 2cos(theta) <=> local Mobius multiplier e^{2i theta} (standard elliptic-element fact); theta=pi/5 => multiplier e^{2 pi i/5} | DERIVED |
| deg(omega) = g-1+c/2 = 5, deg(omega^k) = 5k for **every** integer k>=0 (no parity split) | derived here | Riemann-Roch on X(5)=P^1: omega^2 = Omega^1(cusps), deg=2g-2+c=10 (no elliptic-point terms, torsion-free); "all cusps regular" is exactly what removes the usual odd/even-k case split | DERIVED |
| dim M_k(Gamma(5)) = 5k+1, all k>=0 | derived here | h^0(P^1,O(5k)) = 5k+1; cross-checked against public classical fact dim M_1(Gamma(5))=6 (Klein icosahedral weight-1 forms) | DERIVED + sanity-checked |
| closed form: eigenvalues on H^0(O(d)) = chi_0 * zeta^m, m=0..d | derived here | equivariant line-bundle theory (monomial basis is a zeta-rotation eigenbasis) | DERIVED |
| chi_inf = chi_0 * zeta^d, and the holomorphic-Lefschetz identity chi_0/(1-zeta)+chi_inf/(1-zeta^-1) = Sum chi_0 zeta^m | derived here, verified symbolically for d=0..6 | Atiyah-Bott holomorphic Lefschetz fixed-point formula | DERIVED + symbolically verified in-script |
| chi_0(k) = (-1)^k = zeta_10^{5k} (CONTROL fiber-character law) | derived **under a flagged convention** | exponential-in-weight ansatz + anchor at the banked (F1,F2) grade | **FLAGGED CONVENTION** |
| PRIMARY grade n = tensor of CONTROL grade n with the banked doublet {zeta_10^{+-1}} | derived here | task's own step-4 prescription ("(F1,F2)-multiples of M_k pieces") | DERIVED, under a flagged freeness assumption |

## The shape of the distribution

**CONTROL** M_k(Gamma(5)), dimension 5k+1: eigenvalues are
{(-1)^k * zeta_5^m : m = 0..5k} where zeta_5 = zeta_10^2. Concretely, for k EVEN the
5k+1 eigenvalues are the even powers zeta_10^{2m mod 10} (only even
exponents 0,2,4,6,8 occur); for k ODD they are the odd powers
zeta_10^{(5+2m) mod 10} (only odd exponents occur). Within a grade, the
5k+1 total splits over the 5 available residues (mod-5 cycling of m)
so that exactly ONE residue gets multiplicity k+1 and the other four
get k — CONTROL grade k's multiplicity vector always has exactly one
entry equal to k+1 and four entries equal to k, at the 5 exponents of
one fixed parity (even for k even, odd for k odd); the complementary 5
exponents of the other parity are 0. (Directly verified in the table:
e.g. grade 10 -> mult [11,0,10,0,10,0,10,0,10,0]; grade 11 ->
[0,11,0,11,0,12,0,11,0,11].)

**PRIMARY** V_n = F1*M_n (+) F2*M_n, dimension 2(5n+1): eigenvalues are
CONTROL grade n's list shifted by +1 (the F1 branch) union shifted by
-1 (the F2 branch). Since CONTROL grade n occupies only one parity
class (5 residues), shifting by +-1 moves it to residues of the
**opposite** parity — so PRIMARY grade n is supported ENTIRELY on the
parity-class opposite to CONTROL grade n's (odd residues when n is
even, even residues when n is odd), and the +-1 shift symmetry
interleaves the two F1/F2 branches onto the same 5 residues, doubling
each count and splitting the "+1 extra" between two adjacent residues.
Concretely the PRIMARY multiplicity vector at grade n has exactly two
entries (adjacent, both of the surviving parity) equal to (2n+1) and
three entries equal to 2n, occupying the 5 residues of parity opposite
n, with the other parity's 5 entries identically 0. (E.g. grade 20 ->
[0,41,0,40,0,40,0,40,0,41]: entries 41 at residues 1,9 and 40 at
3,5,7 — 2n+1=41, 2n=40, n=20 even => odd residues populated.)

Both towers are supported on only 5 of the 10 possible zeta_10-exponents
per grade, alternating parity as the grade advances by 1 — a direct
consequence of the base rotation being order-5 (not order-10) at the
level of the underlying P^1 automorphism, with the extra factor of 2
(order 10 overall) entering only through the global chi_0(k)=(-1)^k sign
(CONTROL) resp. the extra +-1 doublet shift (PRIMARY).

## Gate outcomes (grades 0..40, both towers)

- **GATE 1 (dimension sums = Riemann-Roch count, every grade):
  PASS.** CONTROL sums to 5k+1, PRIMARY to 2(5k+1), at all 41 grades.
- **GATE 2 (trace, two independent ways — direct eigenvalue sum vs.
  the holomorphic-Lefschetz closed form chi_0/(1-zeta)+chi_inf/(1-zeta^-1),
  reduced exactly via sympy): PASS** at all 41 grades (both formulas
  agree exactly, symbolically, not just numerically).
- **GATE 3 (W^5 acts as one global scalar per grade — the "multiplier
  sign" fact): PASS.** For every grade (CONTROL and PRIMARY), all
  stored eigenvalues raised to the 5th power collapse to a single
  common value, confirming W^5 genuinely covers the identity on the
  base P^1 (a structural necessity, not fitted).
- **GATE 4 (Galois consistency — sqrt5 -> -sqrt5 [sigma_3: j -> 3j mod 10]
  applied to the whole table must equal the table built from the OTHER
  ("(10,True)") SL(2,5) class): PASS after one correction** (see
  self-correction log below) — at all 41 grades, both towers.
- **Supplementary (not an official gate): non-centrality of W on V** —
  confirmed directly; already CONTROL grade 1 (dim 6) has eigenvalue
  multiset {-1(x2), zeta_5, zeta_5^2, zeta_5^3, zeta_5^4*(-1)}, i.e. is
  manifestly not scalar. Consistent with the sealed vacuity gate's
  non-abort condition (this is a supplementary cross-check from this
  cell, not a re-run of the sealed vacuity gate itself).

**ALL 4 OFFICIAL GATES PASS at every grade 0 through 40, both PRIMARY
and CONTROL.**

## Self-correction log (in the interest of showing the gate is live)

The first run of `w2_inputverify.py` FAILED gate 4 for PRIMARY at
every single grade (CONTROL passed cleanly). Diagnosis: the
"Galois-conjugate" PRIMARY construction had been coded to flip only
the base-rotation exponent (zeta_5 -> zeta_5^-1) while silently leaving
the (F1,F2) doublet's own eigenvalues zeta_10^{+-1} unchanged. That is
wrong: those eigenvalues are themselves elements of Q(zeta_10) and
transform under the SAME Galois automorphism sigma_3 (j -> 3j) as
everything else — sigma_3(zeta_10^{+-1}) = zeta_10^{+-3}, exactly
matching sigma_3(phi) = -1/phi = 2cos(3pi/5). Once the conjugate
doublet shift was corrected from +-1 to +-3, gate 4 passed at every
grade. This is reported as data: it shows gate 4 is doing real,
falsifiable work rather than being tautological.

## Flagged conventions / residual ambiguities (NOT resolved silently)

1. **chi_0(k) = (-1)^k for CONTROL (the fiber-character law).**
   Dimension-count and the abstract group-structure constraints (W^10=1,
   W^5=global scalar) are satisfied by **any** 10th root of unity as
   chi_0(1) — they do not pin it. The value used here comes from an
   additional ASSUMPTION: that the fiber character is exponential in
   the (possibly fractional) weight parameter, chi_0(w) = e^{i w pi s}
   for a single fixed real number s, anchored at the banked doublet's
   grade-1/5 eigenvalue e^{i pi/5}. This anchoring turns out to pin
   s = 1 with NO branch ambiguity (multiplying back through by 5 kills
   the mod-2pi/5 freedom). This assumption cannot be checked
   independently from the holonomy side alone without the actual
   cocycle used to define sigma on integer-weight forms — which lives
   inside route 1's machinery (cellES), deliberately not read by this
   cell. **This is the single most important place where cc's
   Molien-cell number could legitimately disagree with this cell's
   CONTROL table**: if it does, the disagreement is expected to be
   explainable exactly by a different (but equally group-theoretically
   valid) choice of chi_0(1) in mu_10, not by an error in either
   derivation — diagnose there first per the PREREG's disagreement
   protocol.
2. **Freeness of the (F1,F2) module.** PRIMARY V_n is assumed to be
   FREE of rank 2 over M_n(Gamma(5)) through grade 40 (no linear
   relations between the F1- and F2-multiples of M_n forms). This is
   the natural reading of "the graded module generated by (F1,F2)" and
   is consistent with F1, F2 being algebraically independent generators
   at low weight, but is not proved here.
3. **Which fixed point is "0."** The convention zeta_5 = zeta_10^2
   (rather than zeta_10^-2) for the "trace-phi" class is a labeling
   choice; verified NOT to affect any reported multiplicity (the
   tables are symmetric under complex conjugation j -> -j at every
   grade, checked in-script).

## What this cell does NOT do

Per PREREG_W2, cc2's cell stops at the eigenvalue-distribution gate.
The support pre-test (step ii, the eta-dressing / {2/5,3/5} mod-1 check)
and the coefficient comparison (step iii) are cc's Molien-cell
territory and are out of scope here; this cell's sole deliverable is
the table above and its gate outcomes, to be checked for EXACT
agreement against cc's step (i) before (iii) is allowed to run.
