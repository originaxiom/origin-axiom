# Which flat puncture deformations survive the return?

19 November 2026. Author hand proof for independent review. This continues the isolated-fibre control in d1807cb0f and the matched peripheral pair in 09f0c2617. B67 on main already gives the fixed trace curve. The question here is what happens at two compact gauge backgrounds, with the exact same marked boundary holonomies at the comparison point.

## Identity handles are locally rigid even with a moving base

Use B67's figure-eight return on the free punctured-torus generators: a maps to a²b and b maps to ab. A flat history is a pair of handle holonomies A,D and a base holonomy g such that gAg⁻¹=A²D and gDg⁻¹=AD. The following bound holds for any compact Lie group with an invariant positive inner product. Write X=log A, Z=log D in a sufficiently small identity chart. Put H=(X,Z) in the product norm. Equivariance of exponential and local logarithm gives the left sides of the log equations exactly as (Ad_g X, Ad_g Z). Their right sides are (2X+Z,X+Z)+R(H), with ||R(H)|| at most C||H||² by smoothness of the two product logarithms. The radius and C are independent of g.

The real symmetric exponent matrix M has eigenvalues (3±sqrt(5))/2. Orthogonally resolving the two handle indices into its eigenlines commutes with the coefficient action Ad_g. On an eigenline with eigenvalue λ the reverse triangle inequality bounds ||Ad_g v − λv|| below by |1−λ| ||v||. Summing the squared bounds gives

    ((sqrt(5)−1)/2) ||H|| ≤ ||(diag(Ad_g,Ad_g)−M)H|| ≤ C||H||²

at every exact solution in the chart. In a smaller common neighborhood this forces H=0. The base may still vary. In particular the square-root handle path available on the isolated fibre cannot be completed to a nearby flat history with this return. The proof allows nondifferentiable paths and E8 conjugators. Its ingredient is hyperbolicity on the two handle indices versus isometry on the coefficients. It also works for an individual hyperbolic return diagonalizable over the reals by using the eigenbasis norm on the handle indices and the gap to the unit circle. The allowable neighborhood can depend on the return word.

## A compact family through the parity background

In SU(2) take x=tr A, y=tr D and z=tr AD. B67's fixed curve has y=z=x/(x−1). One can check it by substituting in the returned traces (xz−y,z,xz²−x−yz), obtained using the determinant-one trace identity. Real traces alone would not establish compactness or an actual extension. The following construction gives both near x=0.

Write the unit quaternions as A=u+v and D=w+d with scalar parts u=x/2 and w=y/2. Set |v|²=1−u², |d|²=1−w² and v·d=uw−z/2. These prescribe a real independent vector pair for all sufficiently small real x, since its Gram matrix is the identity at zero. Choose a smooth realization beginning with v=i,d=j. Quaternion multiplication gives exactly the three required traces. The returned pair has the same three traces, hence its imaginary vectors have the same Gram matrix. The unique proper rotation taking one ordered vector pair and its cross product into the other is smooth near zero. Lifting the rotation locally to a unit quaternion gives the exact simultaneous conjugator g. This argument avoids any assumption about reducible complex characters.

Pass to the spin-one representation SU(2) → SO(3) in the defining SU(3), and then to the same E6 × SU(3) embedding used in c86f37bd6. At zero the two handles are half turns about perpendicular axes and generate the Klein four group. The returned quaternion pair is (−j,k), so the base cycles the three axes up to signs and the image is the tetrahedral rotation group. This is the parity history up to a simultaneous choice of axes and signs. The marked boundary uses c=[a,b] and b_per=a⁻¹t for the return generator t. Indeed the given return sends c to aca⁻¹. Thus c and b_per commute throughout. At zero the same peripheral pair (I,B), B the image of b_per, is obtained by a separate identity-fibre history as in 09f0c2617.

The determinant-one commutator identity gives κ=tr[A,D]=x²+y²+z²−xyz−2, hence

    κ+2 = x²(x²−3x+3)/(x−1)².

For every sufficiently small nonzero real x this lies strictly between 0 and 4. The commutator survives projection to SO(3). Its rotation angle near the identity in SO(3) is 2 arccos(−κ/2)=2 sqrt(3)|x|+O(x²). The smooth commutator therefore has nonzero derivative at zero. Differentiating peripheral commutativity puts this derivative in the B-fixed tangent space. It lies inside the embedded su(3) and in the 56-dimensional complement identified in 09f0c2617: in su(3) the fibre-invariant diagonal has no traceless B-fixed vector because B cycles its entries. We have integrated at least one distinguishing direction. The other period b_per is allowed to vary along the family. Prescribing both periods independently would be a different extension problem.

## Does the other boundary holonomy stay fixed?

There is an exact answer on this family, independent of the numerical base-trace check in B67. Write n=v×d. The rotation R of the base sends d to d′=wv+ud+n and v to v′=x d′−d, using A²=xA−I. It sends n to v′×d′=d′×d=−|d|²v+(v·d)d+w n. Reading the diagonal in the basis (v,d,n) gives

    tr_SO(3) R = xw+u+w = x²/(x−1).

The peripheral base element a⁻¹t is conjugate to t by b since tbt⁻¹=ab. It has this same trace. This also recovers B67's base-trace-squared formula upstairs because the spin-one trace is the square of the SU(2) trace minus one. At x=0 the rotation angle is 2π/3 and its trace is zero. Its angle has zero first derivative but changes at second order. One may choose a smooth simultaneous frame keeping its rotation axis fixed, so the base has zero first-order motion in that frame. After embedding in E8 its adjoint trace is 77+54τ+τ² for real defining trace τ. This differs from 77 for small nonzero τ=x²/(x−1). Thus **even up to E8 conjugacy the exhibited family cannot realize a nonzero puncture displacement with the base boundary holonomy held exactly at B**. To first order it can. This second-order obstruction concerns the exhibited curve, and leaves other curves open. It matters when specifying which boundary data a physical source is allowed to change.

## Control with one tick

For the one-step substitution a → ab, b → a (interchanging ab and ba changes no handle trace here), exact return would require the two handles to be conjugate. In spin one their defining SU(3) traces are x²−1 and y²−1. Even an E8 conjugator requires equality: on the chosen SU(3) the E8 adjoint trace of a spin-one element with SU(2) trace s is 78 + ((s²−1)²−1) + 54(s²−1) = 24+52s²+s⁴. This is strictly increasing in s²≥0. Equality therefore requires x²=y². Along this curve it forces x=0 or 2. Every sufficiently small nonzero member fails the one-tick condition, although each returns exactly after two ticks. This tests one explicit family. Other compact gauge families and other generated returns have their own equations.

## Physical reading and outstanding premise

The identity and parity histories have the same undisturbed boundary holonomies. Only the latter of this pair supports an arbitrarily small, nonzero flat puncture deformation with the two-tick return. This is local existence versus local rigidity, a stronger conclusion than the earlier tangent-space count. A free seam at quadratic order in the supplied two-dimensional curvature action still sets the period to zero. The nonzero derivative above also has divergent unweighted kinetic norm as a flat variation on the complete cusp by 09f0c2617. A finite cut or external boundary source would be an additional choice. This calculation supplies neither that choice nor a preference between the two undisturbed energies.

Inputs are the marked return, compact gauge law, flat sector and, for the positive example, the spin-one embedding, parity background and permission for the peripheral base holonomy to move. The real parameter x labels solutions. No action coefficient, measured datum, family multiplicity or vacuum probability is read from x. The outstanding physical dependency is a stationary source or end equation in a common admitted domain that can actually access the distinction. A local exclusion at the identity is no exclusion of the full relational architecture.

Review the uniform log estimate, smooth compact extension, peripheral marking and one-tick character test. This is a hand derivation shared for review. No new scientific execution or banking.
