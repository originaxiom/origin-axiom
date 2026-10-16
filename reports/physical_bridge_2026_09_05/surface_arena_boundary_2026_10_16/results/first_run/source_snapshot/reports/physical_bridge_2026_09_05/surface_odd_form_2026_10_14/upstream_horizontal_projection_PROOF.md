# Controlled horizontal transport and the projected cusp operator

Authored analytic argument, requiring independent specialist review. All statements retain the supplied metric, field and global lift data. The two extreme puncture conditions remain choices, not derived physical laws.

## From cylinder quasimodes to differentiated finite fibre kernels

Use Euclidean long-cylinder coordinates z=r+is from vertical_cusp_gap. Its normalized three-dimensional limiting kernel is f(z) times the appropriate coefficient eigenspace, or its antiholomorphic conjugate. Let Q_tau be these three profiles cut off to one on |s|<=y/8 and zero for |s|>=y/4. They extend by zero to the actual finite punctured torus. Their error under Dhat_tau and their Gram error are bounded by C y^m exp(-b y) for some b>0 and finite m; this follows directly from the profile's exponential tails and the cutoff derivative. Throughout this proof E(y) denotes such an error, allowing its constants and finite power to change.

Let P_tau be the exact vertical kernel projection and R_tau the inverse of Dhat_tau on its orthogonal complement. The preceding uniform vertical estimate gives ||R_tau||<=C. Thus

    (I-P_tau)Q_tau=R_tau Dhat_tau Q_tau=O(E(y))

in L2 and in graph norm. Since both spaces have dimension three, P_tau Q_tau is a basis for large y. Normalize it by its positive Gram inverse square root to obtain an orthonormal frame F_tau. This is a constructed frame, not a claim that arbitrary choices of zero modes converge.

To differentiate, first use a different, local parameter trivialization which is exactly the identity near the puncture and on |s|<=y/4. At a reference parameter, choose a smooth function beta(s/y) equal to zero on |s/y|<=1/4 and equal to s/y near the seam |s/y|=1/2. Infinitesimal changes of x and y are implemented by the vector fields beta(s/y) partial_r and beta(s/y) partial_s, respectively, with the corresponding unitary density/spin identifications. At the two ends their difference is exactly the required displacement or length change. They respect the fixed unitary coefficient gluing. The perturbation of the pulled-back operator is supported away from the puncture. Its first-order coefficients are O(1/y), and its zeroth-order coefficients are O(1/y^2). Domains near the puncture are unchanged.

Ordinary flat elliptic estimates with bounded-overlap unit charts on this neck give, uniformly,

    ||dot Dhat psi|| <= (C/y)(||Dhat psi||+||psi||).

This is a common-graph-domain differentiable family. The fixed spectral gap permits differentiating the resolvent around a circle of radius less than that gap. The elementary inverse identity gives dot R(z)=-R(z) dot Dhat R(z), and contour integration gives dot P. Differentiating Dhat P=0 and P^2=P gives

    (I-P) dot P P = -R_tau dot Dhat P,
    P dot P P=0,
    dot P=(I-P)dot P P + ((I-P)dot P P)^*.

The first identity has the complementary inverse, not the singular full inverse. These identities and the graph estimate justify differentiation; finite matrices alone would not.

The exact kernel has exponentially small norm on the support of dot Dhat: F_tau differs from Q_tau by E(y). Its derivatives on that puncture-free region are also E(y), by the local elliptic estimate and Dhat F_tau=0. Consequently y dot Dhat P and y dot P are E(y). Derivatives of Q_tau's cutoff and of its Gram normalization have the same error. Therefore F_tau and its first parameter derivatives converge, in this neck trivialization, to the fixed cylinder frame at that rate.

For weighted spatial derivatives needed below, use graph regularity near the puncture for vector fields vanishing there, and ordinary elliptic estimates elsewhere. The coefficients s partial_r and s partial_s vanish linearly at the puncture and have size at most O(y) on the finite strip. Graph error E(y) therefore remains E(y) after these derivatives. No assertion that unweighted Cartesian derivatives of a critical half-pole are L2 is made.

The resolvent/projection method agrees with the local common-domain perturbation discussion in Simon, section 2, steps 3--6 and equations (2.8)--(2.15): https://link.springer.com/article/10.1007/s13373-018-0118-0. Here the needed differentiability follows from the displayed smooth neck deformation and inverse identity; an analytic-family theorem is not asserted for a merely smooth cutoff family.

## Return to the actual horizontal derivative

At fixed original fibre coordinates u,v, set r=u+xv and s=yv. On the central cylinder,

    y partial_x = y partial_x|_(r,s) + s partial_r,
    y partial_y = y partial_y|_(r,s) + s partial_s.

The area-A fibre norm of an orthonormal spin-component function is (A/y) times its Euclidean norm. A normalized physical frame is therefore Psi_tau=sqrt(y/A) F_tau. Its y derivative adds 1/2. The neck trivialization agrees with the central coordinates and differs elsewhere by vector fields of size O(y); their effect on the exponentially small tails is still E(y). Thus

    y partial_x Psi_tau = sqrt(y/A)[s partial_r F_infty + E(y)],
    y partial_y Psi_tau = sqrt(y/A)[(s partial_s+1/2) F_infty + E(y)].

These identities imply uniformly bounded physical horizontal derivatives of the projection, with the factor 1/ell for orthonormal base directions. On compact base subsets the prior smooth graph-family construction gives boundedness; the cusp estimate supplies the uniform bound at infinity.

Let P act fibrewise, with both horizontal spin components retained, and Q=I-P. It commutes with c1,c2 and GammaV, and D_V P=P D_V=0 on the fibre domains. The full expression is

    D=D_V+[c1 y partial_x+c2(y partial_y-1/2)-i GammaV c1/4]/ell,

with -6in c1/ell added for the prescribed line. Hence [D,P] is a bounded zeroth-order operator on the base Hilbert bundle. Smooth compact-base core sections are mapped into the admitted total domain; closure using the bounded commutator extends this to Dom(D). The off-diagonal B=QDP and its adjoint are bounded, of order 1/ell, not growing with y. Subtracting B+B* from the selfadjoint total operator gives a selfadjoint block-diagonal operator on the same domain. This establishes legitimate closed diagonal blocks; it does not establish the complementary block's spectral coercivity.

## The projected connection is determined by the profile

Normalize f by N=||f||, whose finite positive value need not be evaluated. The cylinder holomorphic profile obeys partial_s f=i partial_r f. Its norm is periodic in r and decays at both infinite ends. Integrating partial_s(s |f|^2) gives

    Re <f,s partial_s f>/N^2=-1/2.

The imaginary part is zero: the Cauchy--Riemann equation turns it into one half of the integral of s partial_r |f|^2, which vanishes around each periodic circle. The excised puncture-circle term tends to zero, since |f|^2=O(1/|z|), while the vector-field coefficient and boundary length each contribute one power of |z|. Thus the integration by parts respects the singular trace.

For either vertical chirality gamma=+1,-1,

    <f_gamma,s partial_s f_gamma>/N^2=-1/2,
    <f_gamma,s partial_r f_gamma>/N^2=i gamma/2.

The physical normalization's +1/2 and the full operator's -c2/(2ell) must both be included. So must its mixed term -i gamma c1/(4ell). In the normalized kernel frame the projected block is, with an exponentially small bounded matrix remainder,

    D_P = [c1(y partial_x+i gamma/4-6in)
          +c2(y partial_y-1/2)]/ell + E(y)/ell.

The geometric connection i gamma dx/(4y) is the Chern connection of the Hodge metric y^(-gamma/2). This matches the previously stated vertical factors lambda^(-1/2) for the plus kernel and lambda^(1/2) for the negative kernel. The computation derives their LEADING OPERATOR CONNECTION from this metric; it does not claim an exact global Berry connection or select the physical twist n. Dropping the mixed spin term would incorrectly replace the quarter coefficient by one half.

## The mixing is finite and is not vertical domain invariance

Put g_gamma=(s partial_s+1/2)f_gamma/N. It is perpendicular to the limiting kernel, belongs to L2, and is nonzero: at s=0 away from the puncture it equals f_gamma/(2N). Its companion is Q(s partial_r f_gamma/N)=-i gamma g_gamma. Therefore the limiting off-diagonal map is

    B_infty=(c2-i gamma c1) g_gamma/ell.

This horizontal Clifford combination has rank one on the two-dimensional horizontal spin factor. The coupling is not identically zero, although one horizontal polarization is annihilated. Uniform first-derivative convergence above transports boundedness and this nonzero limiting map to the actual finite fibres.

There is an important stronger claim which fails. For gamma=+1, near the puncture f~C z^(-1/2), and

    g ~ (C/(4N))[z^(-1/2)+bar z z^(-3/2)],
    partial_bar_z g ~ C z^(-3/2)/(4N).

Thus g is L2 but D_V g is not L2: its squared radial integral behaves like integral r^(-2) dr. The conjugate calculation applies to gamma=-1. A naive anticommutator or squared-operator manipulation which assumes B_infty maps into Dom(D_V) would be invalid. This does not invalidate bounded off-diagonal decomposition on the TOTAL closed domain, and it is not a no-go for the complementary total block.

## The actual cusp transition and the projected spectral conclusion

Use the supplied based inverse-move lift for the deck transformation (x,y,u,v)->(x+1,y,u-v,v). It leaves z and the coframe unchanged. The right-move matrix T satisfies T A0 T^-1=A0 and T B0 T^-1=A0 B0. Therefore Z=T^-1 satisfies Z B0 Z^-1=A0^-1 B0, as required by this inverse based action. The based lift is retained input; the coordinate matrix alone would determine it only up to additional based information. This is the right/left convention already distinguished by W45, not a new choice of monodromy.

For gamma=+1, restrict Z to the A0=i eigenspace selected by the holomorphic cylinder profile. Its phases are {1,5,7}/8. For gamma=-1, the A0=-i eigenspace gives {1,3,7}/8. An overall minus spin lift shifts them by 1/2; none becomes integral. The cutoff, exact projection and Gram normalization can be chosen equivariantly, so these are the actual transition matrices of this constructed kernel frame, not merely a limit of unordered eigenvalues. No extra flat character is introduced.

After the base radial unitary transformation t=log y, the leading operator in a cusp Fourier mode is

    D_k = [c2 partial_t+i c1 mu(t)]/ell,
    mu=2 pi (k+alpha)e^t+beta, beta=gamma/4-6n.

For every allowed alpha and integer k, |2 pi(k+alpha)|>=pi/4. Its square is

    ell^2 D_k^2=-partial_t^2+mu^2+i c2 c1 mu'.

Since i c2 c1 is a Hermitian involution, its potential is bounded below by mu^2-|mu'|. With q=|2 pi(k+alpha)|e^t,

    mu^2-|mu'| >= q^2/4-beta^2-1
                   >= pi^2 y^2/64-beta^2-1.

The first bound uses (a+beta)^2>=a^2/2-beta^2 and a^2/4-|a|>=-1. It holds for either sign of k+alpha and every fixed admitted n. The exponentially small remainder is bounded and symmetric in the full projected operator. The tail estimate plus local elliptic compactness on the finite-rank base bundle gives compact graph embedding and compact resolvent for D_P on the prescribed complete base. Cutoffs can be placed before any artificial finite-height seam; no independent boundary condition is being invented there.

This is a genuine spectral result for the projected harmonic block, not yet for D. A zero-phase comparator instead has a radial free channel (or only a constant mass), so its potential does not grow; the conclusion uses the actual phase information, not only rank three.

## Remaining duties

The projection has controlled horizontal derivatives, the total off-diagonal coupling is bounded, the limiting connection agrees with the prior Hodge weights, and the projected harmonic block is confined at the cusp. The complementary TOTAL block QDQ still requires an estimate respecting the puncture domain. The growing vertical gap alone is not its inverse, and the failure of vertical-domain invariance above prevents treating a formal product square as a proof. Once that block is controlled, the total Fredholm/index comparison must still be made on the actual global domain. None of this supplies the same-field physical action, selects Lambda or n, normalizes observables, or derives a complete physical theory.
