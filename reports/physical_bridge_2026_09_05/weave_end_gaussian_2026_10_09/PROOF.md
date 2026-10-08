# The normal Gaussian retains the end Weyl factor

Conditional construction on the actual horizontal normal operator.
It is a local free five-dimensional Gaussian, not yet a full
six-dimensional boundary action or a mirror-free quantum completion.

## The operator and radial Hamiltonian

The physical dictionary identifies M=partial_t+C from left coefficients
to the right coefficients conjugate to existing opposite-charge left
fields. With gamma5=+1 on the source, the five-dimensional Gaussian
operator is

    D5=gamma5 partial_t+Dslash4+C.

Its diagonal chiral mass entries are partial_t+C and -partial_t+C,
the actual M and Mdagger normal entries. Dslash4 is anti-Hermitian,
anticommutes with gamma5 and commutes with C on parallel backgrounds.
Writing the action as barPsi gamma5 (partial_t+H) Psi gives

    H=gamma5(Dslash4+C), Hdagger=H,
    H^2=-Dslash4^2+C^2.

This derives the radial Hamiltonian from the same normal kinetic map.
The radial variable is Euclidean evolution, not an extra physical
time. Each eigenvalue mu of C and external chiral singular pair has

    H_mu=[[mu,conjugate(z)],[z,-mu]], E=sqrt(mu^2+|z|^2).

Here z is the corresponding entry of gamma5 Dslash4; a constant
minus sign relative to a convention for the Weyl map changes no
chirality. Quantization gives H_F=sum a_i dagger H_ij a_j.
Its four occupation-state energies are0,0,+E,-E. The unique ground
state is the occupied negative eigenspinor. Subtracting its energy,
exp[-L(H_F+E)] tends to its rank-one projector; the other sectors
are suppressed by exp(-LE) and exp(-2LE). Both endpoints of a
finite Gaussian amplitude remain as bra and ket.

For m>0 and E=sqrt(m^2+|z|^2), choose negative eigenvectors anchored
to the negative-energy mass-limit basis at +m and -m:

    v_plus=(-conjugate(z),E+m)/sqrt(2E(E+m)),
    v_minus=(E+m,-z)/sqrt(2E(E+m)).

Direct multiplication gives

    v_plus dagger v_minus=-z/E.

The same-sign overlap is1. The opposite-sign overlap has magnitude
|z|/E and the phase of -z. For an invertible external Weyl matrix K,
singular-value decomposition proves that the corresponding determinant
overlap has phase det(-K)/|det K| and modulus
product lambda/sqrt(lambda^2+m^2), with matched frame conventions.
This is an exact finite-cutoff Gaussian identity. It retains one
Weyl factor, not a nonchiral squared factor or an invisible pure phase.

As z tends to zero, this overlap vanishes; dividing by its magnitude
is singular there. A gapped small external-field chart can temporarily
avoid these zeros, but cannot justify discarding the Weyl factor from
the physical theory. No ultraviolet convergence, phase trivialization
over all backgrounds or complete cusp determinant is proved here.

The quantization framework is the state-overlap construction of
Witten--Yonekura, https://arxiv.org/html/1909.08775, section2.3.
The matrices above retain a complex z and the actual normal source
orientation; the independent executable route uses the full finite
Fock space. A reference used to define a phase is not automatically
an additional physical field, as also distinguished in the earlier
R23/R25 work and Choi--Ohmori, https://arxiv.org/html/2205.02188.

## A local boundary realization in the normal model

Take t<=T, increasing outward. Impose gamma5 Psi=sigma Psi at T,
sigma=+1 or-1. For a tangential zero mode the normal equation gives

    f(t)=exp[-sigma*mu*(t-T)].

It decays into the interior t->-infinity exactly when sigma*mu<0.
Its four-dimensional chirality is sigma. This sign is derived from
M and Mdagger; the decaying cusp direction t->+infinity in the original
complete problem is the opposite direction.

In this five-dimensional normal theory the projector is a local
elliptic boundary condition. At nonzero tangential momentum the
decaying principal solution is an eigenspinor of gamma5 Dslash4,
which anticommutes with gamma5, so it cannot lie in a single gamma5
eigenspace. This checks the complementing condition. In Lorentzian
signature gamma0 anticommutes with gamma5, so the normal Hamiltonian
boundary form vanishes on the half-dimensional allowed space.
The Euclidean first-order boundary operator need not be self-adjoint.

For mu<0 with sigma=+1, the lower-component boundary bra applied
to the negative-energy spinor has a single Weyl zero. The opposite
sigma choice exchanges chirality and complex-conjugates the chiral
factor. This connects the normal solution and Gaussian overlap,
not just their dimensions. Pauli-Villars masses, if used with that
boundary, must have sigma*mu_PV>0 to avoid regulator surface modes.
This sign condition does not by itself regulate all infinite products.

## The declared balanced reference and the charged count

Use the actual C blocks from weave_cusp_anomaly. Each coupled2x2
block has eigenvalues+/-sqrt(delta^2+b^2). Choose sigma to be its
eigenvalue sign, so these two channels have no surface mode.
The two remaining extremes in each module have opposite signs at
zero flux; choose sigma on each to be THAT zero-flux sign.

This reference is balanced in each V_j module: sum sigma=0.
It is an input on the normal channel space, not selected by genesis
or asserted local on the full cusp circle. For every channel,

    end_index_channel=sigma*(1-sigma*sign(mu))/2.

Consequently the net normal boundary index is

    sum end_index_channel=-signature(C)/2=-ind M.

The actual coupled pairs and both extrema are retained. The independently
counted uncoupled spin-line reference is also balanced and gives this
same net index. Its extra vectorlike pairs can differ; net agreement
does not identify the two boundary conditions.

Applying the full physical gauge trace therefore yields the negative
of the earlier five-component anomaly vector, on the declared normal
boundary realization. This is perturbative representation accounting,
not a computed global eta invariant. Its coefficients can cancel the
old interior coefficients only if this boundary contribution and its
associated charged modes are actually retained. It is not evidence
for cancellation in the original complete-domain theory without that
added boundary prescription.

At n=1 the charge-one endpoint remains zero; zero flux has zero NET;
negative flux reverses the answer. Complete E8 root and independent
tensor reconstructions retain exotics and conjugates. No new three-
generation spectrum is inferred.

## Gauge coupling and the full-parent lifting duty

Writing s=T-t and a=|mu|, the normalized model profile is
sqrt(2a) exp(-a s) on s>=0. In cusp measure ell exp(-t)dt its
original coefficient is ell^(-1/2) exp(t/2) times that profile.
The constant normalized gauge field thus has matrix element
g6/sqrt(Area) times its representation generator. The area and g6
remain the old supplied quantities. Moving the profile does not
remove that charge. A collar of width L loses exp(-2aL) norm; the
infinite normal problem is not an exact finite-core kernel count.

Finally the horizontal projection is an angular Fourier projection.
Already [P0,exp(i theta)] is nonzero: it sends the constant to a
nonzero first Fourier mode with a minus sign. Such a projection is
not pointwise local. A reference defined only on its range is not
automatically a local boundary condition for the six-dimensional
operator. The five-dimensional ellipticity test above does not test
that missing full symbol.

The next admission test is the full boundary lift with all angular
channels, physical bundles, adjoint conditions and both end factors.
If a proposed pure relative phase avoids a physical wall, its
reference transformation, locality and behavior at zeros must instead
be shown. This packet does not rule out those other possibilities.
The earlier saddles and all source/silver alternatives remain; a
stable chiral vacuum, full SM and TOE have not been derived.
