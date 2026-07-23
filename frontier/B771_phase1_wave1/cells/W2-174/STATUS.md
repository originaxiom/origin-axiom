# W2-174 (H104) cell status

**VERDICT: RESOLVED-A** — omega-window assemblies are realized in E6 for **both**
window groups (2T and A4), by explicit exhibited classes.

## Evidence (all computed in-cell)

- `compute.py` (main, symbolic-first): gates **A1–C6 all PASS** (exact): 2T rebuilt
  from Hurwitz units, exact character table gated; rho3 = 1'+2' in SU(3) exact;
  R = SO(3) rep with ker = {±1} exact; **I3-invariance proven SYMBOLICALLY** for the
  untwisted generators, the central scalar w·Id (w³=1), and both twisted witnesses
  directly. Parts D–E (numeric matrix build) are slow in sympy; at status-writing
  time the run was still completing — `output.txt` accumulates it. Every fact that
  Parts D–E gate was independently computed by `aux_numeric.py` (below).
- `aux_numeric.py` / `aux_output.txt` (fast numeric, complete): **N1–N11 all PASS**:
  - both witnesses are homomorphisms (all 576 pairs, <1e-10) and injective
    (2T faithful; A4 kernel exactly {±1});
  - characters: **9w at an order-3 class for both** (non-real ⇒ 27-restriction not
    self-conjugate ⇒ chiral / non-sigma-stable class);
  - decompositions (exact-integer snapped):
    27|W2T = 3·1 + 9·1' + 3·1'' + 3·2 + 3·2'' — (n1,n2) = (9,0);
    27|WA4 = 9·1' + 6·3;
  - (Sym³V)^G and (Sym³V*)^G ≥ 1 for both (invariant cubic at character level);
  - **I3 nondegenerate: dim Stab_{gl(27,C)}(I3) = 78 = dim e6**, seeds 0 and 1,
    gap ratios 1.32e14 / 1.34e14 (well-conditioned);
  - I3 numerically invariant under both witnesses at random points, both seeds.

## The witnesses

- 2T: g ↦ w^{eps(g)} · P(rho3(g), I, I) (center-twisted single-factor trinification)
  — independently confirms wave-1 OI-173's candidate end-to-end.
- A4: g ↦ w^{eps(g)} · P(R(g), I, I) (SO(3) route; descends to a faithful A4)
  — **new in this cell**: the OTHER window group is realized by the same mechanism.

## Mechanism (one line)

Z/3 abelianization of the group composed with the mu_3 center of E6 = the Eisenstein
omega twist; exactly the groups B356's window permits (A4, 2T) are exactly the groups
where the twist is available. B356's character-level window is not vacuous: it is
REALIZED, at both of its groups.

Firewall: structural only (which embeddings exist in Stab(I3)); no SM values;
nothing to CLAIMS.
