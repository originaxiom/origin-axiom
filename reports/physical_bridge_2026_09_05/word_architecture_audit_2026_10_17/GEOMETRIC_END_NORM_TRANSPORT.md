# Transporting the geometric end norm without choosing an end

October 18, 2026. Analytical companion to
[the theta-field transport](GEOMETRIC_THETA_REGISTER.md).
The actual Szego kernels determine how their cutoff norms and finite
parts transform. The common subtraction ambiguity cancels from the
paper's defect, but covariance leaves a family of admissible geometric
cuts. This distinguishes a coordinate mismatch from an undetermined
physical end law. No numerical experiment is performed here.

## Existing fields and prior results

Use periods 1,tau and B1654's kernels and residues

    S_r(z,tau)=theta_r(z,tau) d(tau)/[theta_r(0,tau)theta_1(z,tau)],
    d=partial_z theta_1(0,tau), r=2,4,3,
    R=(-theta_2(0)^2,-theta_4(0)^2,i theta_3(0)^2)/d.

Source pin: main `2e5716bd9bea013d69f3cd733f083b61a6f59dbd`.
B1654's complete producer already establishes the norm asymptotic,
common-log cancellation and a channel-dependent-cutoff control.
B1657/W87 already give a closed form for the defect; its defining
source formulas and S0/S1 comparison were read, not replayed.
B1666 and the paper's Lemma 25 already prove its automorphy law.
Those results are reused, not presented as newly discovered.

For a small embedded coordinate disc at the puncture, define

    N_r(tau,epsilon)=integral_(E_tau minus disc_epsilon) |S_r|^2 d^2z,
    c_r(tau)=lim_(epsilon->0)[N_r-2 pi log(1/epsilon)].

Although S_r changes sign around some periods, |S_r|^2 is periodic;
the norm is independent of the choice of fundamental parallelogram.
Near zero S_r=1/z+O(z), so the subtracted remainder is locally
integrable. In particular the finite part exists and

    N_r=2 pi log(1/epsilon)+c_r+o(1).

The finite part, the asymptotic renormalized norm, and the norm at a
finite physical cut are three different objects. The last equality is
not an exact formula at arbitrary nonzero epsilon.

## Exact kernel law and transport of the cut

For gamma=[[A,B],[C,D]], let J=C tau+D, tau'=gamma tau, z'=z/J.
The theta laws give a permutation sigma of the three even channels
such that

    S_r(z',tau')=J S_(sigma(r))(z,tau).             (1)

This is exact, including its scalar: normalization to residue one
cancels the theta multipliers. For L, sigma exchanges 3 and 4 and
J=1. For S0:tau->-1/tau, it exchanges 2 and 4 and J=tau.
The generator identities follow by substitution in
[DLMF 20.7.26--33](https://dlmf.nist.gov/20.7#viii); their composition
gives (1). In particular, a minus sign from -I agrees with the oddness
of each kernel. Period translations contribute only signs, which
drop from this norm.

Since d^2z'=|J|^-2 d^2z, the integrand measure is invariant. The
same geometric cut has coordinate radius

    epsilon'=epsilon/|J|,
    N_r(tau',epsilon')=N_(sigma(r))(tau,epsilon).   (2)

This equality is exact for sufficiently small embedded discs. It
does not assert that the same numerical epsilon in two coordinates
describes the same cut.

Inserting the finite-part definition into (2) yields

    c_r(tau')=c_(sigma(r))(tau)-2 pi log|J|.        (3)

The sign is fixed by log(1/epsilon')=log(1/epsilon)+log|J|. It can
also be checked from the equivalent exact relation
N_r(tau',epsilon)=N_(sigma(r))(tau,|J|epsilon).
The additive shift is common to all three channels. Their differences
therefore transform by permutation alone.

If y=Im tau, then y'=y/|J|^2. Hence

    c_hat_r=c_r-pi log y

also transforms by permutation. This is the finite part relative to
the unit-area flat metric: its disc radius is delta=epsilon/sqrt(y),
and 2 pi log(1/epsilon)+c_r=2 pi log(1/delta)+c_hat_r.
Adopting that reference metric is not selecting a physical boundary.

## Recovering the defect law without suppressing the end data

For a ruled lift e, the companion note proves

    R(tau')=q_e Q_e R(tau),
    q_e=mu(e)/j_e(tau), j_e^2=J,

where Q_e is a real signed permutation. Its unsigned permutation
agrees with (1). Jacobi's identity gives sum R_r^2=0. Thus

    D(tau)=sum_r c_r(tau) R_r(tau)^2

obeys

    D(tau')=q_e^2 [D(tau)-2 pi log|J| sum_r R_r^2]
            =mu(e)^2 J^-1 D(tau).                 (4)

On L, mu^2=i; on S0, mu^2=i. These are exactly the existing eta-six
character and weight minus one of the paper's Lemma 25. The derivation
here shows how it arises from transport of the underlying norms, not
only from the closed formula for D. Also

    ||R(tau')||^2=|J|^-1 ||R(tau)||^2,

so |D|/||R||^2 is invariant, as already recorded.

A common change c_r->c_r+k(tau) leaves D unchanged. A channel-dependent
change does not: replacing epsilon_r by lambda_r epsilon gives the
finite shift

    D -> D-2 pi sum_r log(lambda_r) R_r^2.

This is B1654's existing N4 distinction. It must not be promoted to
independence of every regulator or boundary prescription.

For the paper's equal-canonical-amplitude ansatz, define
u_r=sqrt(N_r) R_r at a finite cut, using positive norms. Transporting
the cut as in (2) gives u'=q_e Q_e u exactly. The same holds for the
asymptotic model N_r^ren=2 pi E+c_r on its positive domain, with

    E'=E+log|J|.

If E is incorrectly held fixed, the renormalized norms instead acquire
the common additive shift (3), and u does not generally transform by
q_e Q_e. Such a mismatch is not evidence of a physical difference
between the same transported configuration. The vanishing of the
common-log contribution to u.u does not remove this norm dependence
from other observables.

## Covariance does not choose the end radius

There is an explicit family of cuts satisfying (2). Let

    ell(tau)=min {|m+n tau| : (m,n) in Z^2 minus {(0,0)}}.

Lattice transport gives ell(gamma tau)=ell(tau)/|C tau+D|.
For every constant t in (0,1), set

    epsilon_t(tau)=t ell(tau)/4.                  (5)

These discs are embedded, since the flat injectivity radius is
ell(tau)/2, and all choices obey the identical modular covariance
law. They are continuous; differentiability at changes of the shortest
lattice vector is not asserted or needed for this counterfamily.
The point is not that (5) is the right end prescription. It is that
the specified flat geometry and covariance do not uniquely select t.

Distinct t give distinct norms: increasing epsilon removes an annulus
on which |S_r|^2 has a positive integral. This is genuine remaining
cut dependence, not a failure to transport coordinates. The asymptotic
defect is protected against its common logarithmic part; the exact
finite-cut combination need not equal that limiting defect.

Additional requirements such as a derived variational boundary law,
the full hyperbolic geometry, or a smooth family of physical domains
may restrict these candidates. None is inferred from the modular
transformation alone. B1667's two hyperbolic horocycle prescriptions
and its scoped numerical conclusions are neither replaced nor
recertified by this flat-coordinate counterfamily.

## Consequence for the joining problem

The paper's pairing, scalar phase, kernel and cutoff can be transported
consistently together. That is a positive compatibility result within
the supplied field model. It prevents both discarding a needed line
factor and treating a coordinate-cut mismatch as a physical negative.
It also leaves explicit freedom: compatible end data are not unique.

The next physical obligation is to derive an end response on the same
field system, rather than select one member of (5) for its spectrum.
No stationary boundary, physical fermion operator, three-generation
count, vacuum selection or observer is constructed here.

This analytical checkpoint awaits separate non-authoring review. A
sealed successor needs kernel laws at generic moduli and points,
transported-disc and deliberately fixed-disc controls, the sign of (3),
common versus channel-specific shifts, finite-cut versus finite-part
comparisons, and compatibility with the actual Higgs and kinetic terms.
No frozen verification package or historical result is changed.
