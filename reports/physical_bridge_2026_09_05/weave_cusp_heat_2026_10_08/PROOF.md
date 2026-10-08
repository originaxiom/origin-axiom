# The continuum heat contribution in the actual cusp operator

Authored conditional derivation in the pinned supplied parent and
complete graph domain. This computes the spatial-cutoff heat-current
diagnostic for internally parallel unbroken gauge fields. It does not
construct a consistent determinant phase, renormalized full quantum
action or stable vacuum. All former parent/metric/spin/selection inputs
remain supplied. The magnetic stationary family remains unstable.

## The operator and the cutoff current

The previous physical dictionary identifies M with the actual four
left-Weyl mass map, not an auxiliary bosonic map. After its bundle
isometries and constant unitary row phases, a horizontal end channel
has M=partial_t+C with C Hermitian. Define

    D = [[0,Mdagger],[M,0]], Gamma=diag(1,-1),
    J = [[0,-1],[1,0]], D_end=J partial_t+sigma1 C.

Here each scalar entry is tensored with the end-channel space. D is
self-adjoint on the doubled complete graph domain. Its square has
Mdagger M and M Mdagger as its two diagonal blocks. Gamma records
source minus target, hence the previously identified physical index.
Neither the gaugino nor opposite-charge cokernel is deleted.

Choose smooth scalar chi_T equal to1 below T and0 above T+1, with
uniformly bounded derivatives. For s>0,

    S_T(s)=Tr(Gamma chi_T exp(-s D^2)).

The insertion has compact internal support, so the smoothing traces
and differentiated products are legitimate. Graded cyclicity applied
WITH that insertion gives

    dS_T/ds = (1/2) Str([D,chi_T] D exp(-s D^2)).

Indeed the supertrace of [D,chi_T D exp(-sD^2)]_super vanishes;
expanding it leaves twice the chi_T D^2 term plus the displayed
commutator. Omitting [D,chi_T] before taking the limit is precisely
the invalid cyclic cancellation the preceding packet warned against.

At the limiting end [D,chi_T]=J chi_T'. On a scalar mass mu,

    tr(Gamma J (J i*p+sigma1*mu)) = -2mu,
    integral(dp/(2pi))*exp(-s*(p^2+mu^2))
        =exp(-s*mu^2)/sqrt(4pi*s).

Since integral chi_T' dt=-1, the outward sign is positive:

    dS/ds=tr(C exp(-s C^2))/sqrt(4pi*s).                 (1)

No sign or coefficient is imported from a different inward-normal
eta convention. A wrong sign changes the continuum contribution.

## Why the complete cusp gives this limit

At c=d=0 the actual cusp Fourier decomposition has finitely many
zero-angular channels, with the coupled C matrices already derived.
Their heat normal kernel is the free radial Gaussian times exp(-sC^2).
The compact core changes its fixed-s limit at t to infinity only by
a term tending to zero. All nonzero angular channels have confining
frequency-square*exp(2t) leading potentials and at most linear-exp(t)
lower terms. Completing the square bounds them below by a positive
frequency-square*exp(2t) term minus a constant for fixed n.

Consequently the heat operator restricted to that nonzero-angular
sector on a far half-cusp is trace-class at fixed s: Dirichlet bracketing
and the one-dimensional heat bound reduce the bound to
integral dt sum_{frequency!=0} exp(-c_s*frequency^2*exp(2t)), which
converges. A cutoff separating the core introduces only compactly
supported commutators. Heat off-diagonal estimates make their far-end
contribution tend to zero, as do the differentiated kernels in(1).
No uniform interchange of the cusp limit with s to zero is assumed.

For finite c,d, their physical coefficients and derivatives decay
as polynomials in y times exp(-pi*y/ell). Duhamel expansion with this
short-range perturbation leaves the fixed-s normal kernel unchanged.
The two horizontal diagonal heat kernels have the same leading term,
so their difference has a convergent cutoff integral, although their
individual traces have linear length divergences. Thus S(s)=lim S_T(s)
exists, is differentiable for s on compact subsets of(0,infinity),
and obeys(1). These are analytic heat estimates, not certified by the
finite algebra checks. Outside analytic review remains owed.

The prior Fredholm proof gives a nonzero essential gap and finite
kernel. Positive discrete modes pair through M/sqrt(E); they cancel
in the supertrace. The open horizontal channels have short-range
scattering off the compact core, while nonzero angular channels are
closed at infinity. The scattering derivation below gives the complete
remaining relative density and its exponentially decaying large-s
contribution. It therefore also fixes lim_{s->infinity}S(s)=ind M,
without assuming that a non-trace-class ordinary heat trace is cyclic.

Albin--Rochon [section1.4](https://arxiv.org/html/0801.1969v2) gives
the corresponding renormalized-trace structure for cusp Dirac operators.
Here the stated Fourier, cutoff and short-range arguments identify its
end contribution for the supplied operator; no uncomputed families
eta form or determinant phase is borrowed.

## Scattering fixes the continuum normalization separately

Diagonalize C. For a mass mu and energy E=p^2+mu^2, p>0, use incoming
wave exp(-ipt) and outgoing wave exp(ipt). Applying M/sqrt(E) multiplies
their amplitudes by(mu-ip)/sqrt(E) and(mu+ip)/sqrt(E), respectively.
Thus the partner scattering matrices obey

    S_minus=D_out S_plus D_in^(-1),
    det(S_plus)/det(S_minus)=product (mu-ip)/(mu+ip).

The determinant relation holds even when the core mixes open channels.
At a common energy each open channel has its own p=sqrt(E-mu^2).
Positive embedded/discrete states are paired by the same invertible
map; threshold resonances at E>0 cannot add an unpaired zero state.

With a common spatial cutoff, the box quantization condition is
2pT+arg(S)=2pi*k plus a shared end phase. Its leading T/pi densities
cancel between partners. Differentiating the scattering phase gives,
per channel in the p measure,

    rho_plus-rho_minus
        =(1/(2pi*i))*partial_p log[(mu-ip)/(mu+ip)]
        =-mu/(pi*(p^2+mu^2)).

Therefore its continuum heat contribution is

    integral_0^infinity dp (rho_plus-rho_minus) exp(-s*(p^2+mu^2))
        =-sign(mu)*erfc(abs(mu)*sqrt(s))/2.              (2)

The identity follows by a Gaussian Laplace integral, or by
differentiating in s and fixing the zero limit at infinity. It is
not a fit to the previous index. Half-line boundary conditions used
to derive a box density cancel between partners; no reflecting wall
is being added to the physical complete surface.

Dabholkar--Jain--Rudra [section3](https://arxiv.org/html/1905.05207)
uses partner scattering to expose continuum contributions in a
noncompact index. Our mass, momentum, normal orientation and density
normalization are fixed independently above, then checked against(1).
Its cylinder is not asserted to be this whole cusp geometry.

The spectral decomposition with(2) now gives

    S(s)=ind M-(1/2)sum_mu sign(mu)*erfc(abs(mu)*sqrt(s)).

The prior global index, independently established from complete
Dolbeault kernels, is ind M=(1/2)sum sign(mu). Hence

    S(s)=(1/2)sum_mu erf(mu*sqrt(s)),
    S(0+)=0, S(infinity)=ind M.                         (3)

This limit takes the common spatial cutoff away at fixed s BEFORE
the ultraviolet limit. A zero-mode truncation instead returns ind M
for every s and is not the same regulator. Equation(3) does not
identify the ultraviolet and infrared physics. It retains their
nonzero difference, supplied by the actual continuum relative density.

## Coupled modules and the full charged coefficient

Every paired horizontal C has eigenvalues plus/minus
sqrt(delta^2+tau^2*b^2). Their contributions to(1)--(3) cancel for
every tau. The unpaired extreme masses are independent of tau.
For V_j with k=nq, the full internal heat supertrace per gauge weight is

    S_j(k;s)=-[erf((k+(j+1)/2)*sqrt(s))
               +erf((k-(j+1)/2)*sqrt(s))]/2, j even;
    S_j(k;s)= [erf((k+j/2)*sqrt(s))
               +erf((k-j/2)*sqrt(s))]/2, j odd.

Finite neutral c,d leave this character unchanged. The independent
zero-Higgs route has two masses -(beta+1)/2 and-(beta-1)/2 for even
beta, or two masses beta/2 for odd beta. Here beta=m+2nq. All four
physical slots are included, and their full tensor-weight odd mass
character agrees with the coupled extreme route.

Apply the previous physical gauge traces to S_R(s). At infinity this
recovers ALL five old anomaly coefficients and the n=1 endpoint; at
zero they all vanish. This is not a claim that the finite-s coefficients
are integer generation counts or consistent anomalies. The SU3 cubic
coefficient provides a nontrivial intermediate control. With
P_r(n)=sum_R A3(R) sum_mu mu^r (one conjugate representative), direct
use of the complete roster gives

    P_1=0, P_3=48n*(7n^2-2),
    A3_heat(n;s)=-16n*(7n^2-2)*s^(3/2)/sqrt(pi)+O(s^(5/2)).

It is not identically zero as a function of finite s for nonzero integer
n; the expansion proves this near zero, not the absence of every
possible finite-s root. No sector was dropped. Its IR limits are -1 at n=1 and -3 at
n>=2, with opposite signs at negative n. At n=0 all odd mass
characters vanish. Color-preserving graph-compact deformations retain
the net index; this computation neither contradicts nor circumvents
that theorem by changing an interior condensate.

## The physical product regulator and its precise limit

For an internally parallel unbroken external gauge field, the gauge
representation acts on the gauge factor and commutes with M and its
domain. Let D4[A] be its Euclidean spacetime Dirac operator. The
physical left/right pair from the prior trace-dual dictionary is the
appropriate chiral subspace of

    Dtot=D4[A] tensor1 + gamma5 tensor D,
    Gamma_tot=gamma5 tensor Gamma.

This is the doubled representation of the existing kinetic and mass
action. Restrict to one conjugate-charge representative, or include
the factor one-half when tracing the full charge-conjugate roster;
the doubling does not authorize extra Weyl species. The total grading anticommutes with Dtot, and
Dtot^2=D4[A]^2 tensor1 +1 tensor D^2. Both kinetic operators and the
gauge curvature term remain, so the heat kernel factorizes. Inserting
a compact-spacetime gauge parameter and chi_T gives the standard
four-dimensional covariant chiral heat coefficient times S_R(s).
Sending T to infinity at fixed s, then s to0, gives ZERO for this
projected covariant heat-current coefficient. The continuum part tends
to minus the known zero-mode coefficient. No desired counterterm or
additional representation has been inserted to obtain this difference.

This is a regulated current diagnostic, NOT yet the consistent gauge
variation of an effective action. Bilal [section3.4 and section4.2](https://arxiv.org/html/0802.0634v1)
explains why the regulator must use the actual gauge-dependent fermion
operator and why a covariant current is not automatically the derivative
of an effective action. The same warning applies to the spatial trace
prescription here. No commutation of limits, arbitrary internal gauge
parameter, determinant phase or Wess-Zumino integrability is proved.
The outer-end current in the full Ward identity must still be kept.

Finally, the UNGRADED horizontal heat density is positive:
2*tr(exp(-sC^2))/sqrt(4pi*s) per unit radial length. Inserting a
nonzero unbroken color generator squared retains a positive density.
Its integral diverges linearly with the cutoff even at fixed s. The
finite supertrace does not define the parity-even determinant or its
coupling renormalization. This is not a computation of the complete
boson/ghost/fermion loop combination, which might have further
cancellations. It is a concrete additional duty, not a parent no-go.

The next gate is one common regulator/relative subtraction for the
effective action and propagators, its end terms and integrable gauge
variation. A vanishing heat coefficient alone cannot replace that
construction. Stability, global anomalies, three physical families,
genesis-to-parent selection, observer/qualia and gravity remain open.
