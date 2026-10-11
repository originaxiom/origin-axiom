# Scoped lemmas for review

These are standard geometric facts rederived for the current dependency, not originality claims. Proposed rows preserve their hypotheses before normal banking; they do not edit the canonical LAW_MAP.

| Lemma | Exact scope | Proof and safeguards |
|---|---|---|
| The weight-12n Hodge metric realizes effective flux n | Effective PSL(2,Z) modular base with curvature minus one, metric y^(12n), integer n; F=-6in dA, flux n, finite energy 6pi n²/g² | PROOF.md curvature section; verify.py area, descent, curvature and energy checks |
| Fixed flux admits a constant-curvature energy minimizer | Abelian two-dimensional Yang–Mills functional with square-integrable curvature and fixed flux; nonzero flux is not selected against zero | PROOF.md square identity and boundary scope; verify.py symbolic bound and zero control |
| Open smoothness and finite action do not quantize this flux | Given HDelta, the trivial open line admits metrics (y^12 |Delta|²)^s for all real s; this does not define an integral compactified extension for noninteger s | PROOF.md global frame and Stokes calculation; verify.py real-s curvature and boundary orientation |
| The pole prescription has an exact twisted norm realization | Given HDelta and specified tensor/end metric, the norm of Fmod/Delta^n is the weight-shifted norm of Fmod; no full Dirac index asserted | PROOF.md norm section; verify.py norm and two-sided cusp decay controls |
| Trivial elliptic isotropy first occurs at positive weight 12 | Integral automorphic-weight family on this base; conditions 4 divides k and 6 divides k; not a physical necessity of that family | PROOF.md stabilizer argument; verify.py exact algebraic phases for negative, zero and positive controls |

Open item carried forward: derive or recover the explicit physical coupling/end rule that would make the required nonzero integral sector follow from earlier premises. No additional flux census is proposed. A four-dimensional lift is not inferred from a base-area calculation.
