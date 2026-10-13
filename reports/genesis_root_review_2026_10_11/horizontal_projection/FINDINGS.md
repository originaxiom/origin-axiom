# Horizontal coupling and cusp confinement of the projected modes

The supplied semi-flat geometry now has an authored controlled projection onto its three vertical zero modes, for either extreme puncture condition. The projected modes do not decouple exactly. Their coupling to the complement is bounded, and their projected cusp operator is confining. These conclusions concern the specified mathematical operator; neither a full total-space index nor a physical generation spectrum follows yet.

## What is derived in the fixed problem

The preceding vertical gap and the explicit cylinder profiles give exponentially accurate finite-fibre quasimodes. A neck deformation which is fixed near the puncture permits differentiation of their spectral projections on a common graph domain. Returning to the actual metric coordinates gives bounded horizontal derivatives and hence a bounded off-diagonal total coupling. This is an analytic argument in PROOF.md, not a consequence of the finite test count.

The fibre normalization, profile integrals and full mixed spin connection together give

    D_P = [c1(y partial_x+i gamma/4-6in)
           +c2(y partial_y-1/2)]/ell + exponentially small remainder.

Here gamma is the vertical chirality and n remains the supplied admitted cusp-line parameter. The leading geometric connection is i gamma dx/(4y), the unitary Chern connection of the previously recorded half-Hodge metric y^(-gamma/2). This is an explicit leading-connection calculation, not an exact global Berry connection or an identification of a mathematical kernel with particles. Dropping the mixed spin term gives the wrong coefficient.

The supplied based cusp lift uses the inverse move T^-1. On the actual coefficient eigenspaces its phases are {1,5,7}/8 for gamma=+1 and {1,3,7}/8 for gamma=-1. Both overall spin signs keep every phase at least1/8 from an integer. These phases, transported through the equivariant kernel-frame construction, imply the radial squared-operator potential bound

    mu^2-|mu'| >= pi^2 y^2/64-(gamma/4-6n)^2-1.

Consequently the projected block has compact resolvent on the prescribed complete base, by the authored tail estimate and local elliptic compactness. The fixed area, base scale, extending spin, coefficient, globally compatible lifts, extreme domain and n are retained inputs.

## Why the full operator still requires work

The limiting coupling is (c2-i gamma c1)g_gamma/ell, where g_gamma=(s partial_s+1/2)f_gamma/||f_gamma||. It is nonzero and rank one in the horizontal spin factor. Its fibre profile is L2, but its vertical Dirac derivative is not L2: the latter has a critical local term of order r^(-3/2). Bounded coupling on the total domain therefore does not mean invariance of the vertical graph domain.

This prevents using an unqualified formal square or substituting the inverse of D_V for the inverse of QDQ. It does not exclude a valid total complementary estimate. The next task is to prove that estimate on the already constructed closed domain, then make the total Fredholm and index comparison. Independent specialist review remains owed for the analytic arguments throughout this chain.

The controls distinguish the hypotheses. With zero cusp phase the radial potential is only constant and does not confine. A rank-one projection rotating by y^2 can coexist with a complement gap sqrt(y), while its horizontal derivative grows as2y^2. Thus the actual transition phases and the differentiated neck construction do real work; neither rank three nor a growing vertical gap is sufficient alone.

## Verification

The first pushed seal 041b69a1b879a020cf974b29218a2fd88e9ed841 produced an exact-root classification exception before a complete verdict. Its raw failure is preserved. Expanding exact complex radicals, with the same expected values and no tolerance, was resealed and pushed at026fde3fdb6809c8c23a5178d3d802e060719e81 before execution. The second run passed all66 finite exact safeguards in3.719945934 seconds and all seven tests in4.73 pytest seconds (5.287122242 seconds including capture). Both stderr logs are empty. All fifteen pins matched the repaired seal and remained unchanged.

These checks test identities, transitions, inequalities and countercontrols. They do not machine-certify the projection regularity or compact-resolvent theorem. No new shared bank number, canonical genesis promotion, empirical parameter, physical action or full-theory claim is made. The latest other-seat publication and the governance outcome are recorded separately in PUBLICATION_NOTES.md.
