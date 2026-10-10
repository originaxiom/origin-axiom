# Auxiliary elimination with the actual compact boundary

Authored before execution; conditional analytic result with finite exact
controls. Non-author analytic review is owed. All assumptions/costs are
in DESIGN. The full silver/E8 coefficient is unchanged, not re-enumerated.

## 1. Canonical expansion, no component-table shortcut

Use the canonical exterior/measure convention in DESIGN. Actual adjoint
reverses odd products and exchanges t with b, so (theta2)^dagger=bartheta2
and u^dagger=u. Write the static chiral fields as

    Phi_i=phi_i+theta2 F_i, phi_i=A_i+i B_i,
    barPhi_i=phi_i^dagger+bartheta2 F_i^dagger,
    V=u D/2, G=1+u D, G^-1=1-u D.

These nilpotent exponentials are exact. Direct multiplication yields

    Z_i=2 B_i-i theta2 F_i+i bartheta2 F_i^dagger
            +u (partial_i D+i[phi_i^dagger,D]).

For an orthonormal frame, direct Berezin extraction gives

    (1/4) int d4theta Tr Z_i Z_i
       =Tr(B_i D_A,i D)+(1/2)Tr(F_i F_i^dagger).

Here D_A=d+i[A, .]. The additional trace Tr B_i[B_i,D] is zero by
cyclicity, not because matrices commute. Thus the canonical coefficient
is 1/2, not 2, for THIS declared field and measure. Left differentiation
of G in W gives W_alpha=2 theta_lower,alpha D; raising with eps^12=-1
gives W^alpha W_alpha=4 theta2 D^2. The gauge piece plus its actual
conjugate consequently contributes Tr D^2/2.

This resolves the previous recorded 4.10/4.14 mismatch in favor of
4.14 for the declared action. It does not establish a universal erratum
or invalidate the parent. The earlier projected-response computation
used invertibly rescaled fields, not these canonical kinetic coefficients.

## 2. Holomorphic source, relative term and two retained surfaces

Let H=dphi+i phi wedge phi, so H_jk=partial_j phi_k-partial_k phi_j
+i[phi_j,phi_k]. Define c_i=epsilon_ijk H_jk=2(*H)_i. With the fixed
flat reference, the relative functional is

    W_Phi,rel=integral Tr(a D_star a+2i a^3/3), a=Phi-Phi_star.

It includes the preceding packet's affine surface counterterm. In this
convention the theta2 coefficient is

    2 integral Tr(F wedge H)-integral_Sigma Tr(a wedge F).

The last term vanishes because BOTH a_t and F_t belong to the bilinearly
isotropic A1. This is integrated isotropy; pointwise wedge products need
not vanish. Locally the unmodified CS expansion retains the divergence
partial_j epsilon_ijk Tr(phi_i F_k). A nonzero control detects its omission.
After the relative cancellation, S_W supplies

    (1/4)Tr(F_i c_i+c_i^dagger F_i^dagger).

Integration by parts of the real kinetic piece on the core is instead

    integral Tr B_i D_A^i D
       =-integral Tr D mu + integral_Sigma Tr B_n D,
    mu=div_A B (with the actual volume form).

Do not drop that surface using closed-space identities. D's essential
boundary trace is INTERNALLY PARALLEL in k, while the response's lowest
slot is Pi_k B_n=0. Those two conditions make this integral zero. A
zero-mean k-valued B_n need not be pointwise zero; if D varies internally
the cancellation can fail. A structure-valued nonzero B_n is orthogonal
to k and is NOT erased. Orthogonality in full E8 follows from invariance,
k=[k,k] and [k,s]=0, not from a tensor-model dimensional match.

## 3. Eliminate the actual real/complex auxiliaries

Before imposing its vanishing boundary term, the static auxiliary action is

    L_aux=integral Tr( D^2/2-D mu+F_i F_i^dagger/2
                     +(F_i c_i+c_i^dagger F_i^dagger)/4 )
             +integral_Sigma Tr B_n D.

Vary the real D and real/imaginary coordinates of the complex F. In the
bulk their unique algebraic solutions are

    D=mu, F_i=-c_i^dagger/2, F_i^dagger=-c_i/2.

The conjugate in F is necessary: differentiating with respect to F_i^dagger
gives F_i/2+c_i^dagger/4. A non-real curvature is an opposing control
against replacing F by -c/2. The source's displayed F equation therefore
cannot be copied without an explicit symbol/conjugation dictionary; Braun
B.14 also distinguishes curvature and conjugate curvature. We make no
claim that its H auxiliary is numerically identical to this F.

Completion of squares gives L_aux,on=-V for the admitted zero-surface
domain, with EXACT static potential

    V=(1/2)||mu||^2+(1/8)||c||^2
      =(1/2)||mu||^2+(1/2)||H||^2_two-form.

Norms use the supplied positive metric/compact trace; the two-form norm
counts j<k. No Bochner rearrangement is used and no structure flag flux
is reinterpreted as this energy. The curvature contains the full bracket,
so cubic/quartic interactions remain; the moment term retains i[A_i,B_i].

## 4. The induced domain is not free after elimination

Keeping the static part of the WHOLE superspace response also requires

    Pi_k B_n=0, Pi_k F_n=Pi_k F_n^dagger=0,
    Pi_k(D_A,n D+[B_n,D])=0.

Essential traces remain D|Sigma in parallel k and F_t in A1 (with its
actual conjugate). Substitution gives the genuine scalar derivative laws

    mu|Sigma in parallel k,
    (*H^dagger)_t in A1,
    Pi_k(*H^dagger)_n=0,
    Pi_k D_A,n mu=0.

For the last equation the commutator projects to zero: for c,D in parallel
k, the pairing with [B_n,D] is that with [D,c] and Pi_k B_n=0. Flat
reference plus a_t in A1 makes H_t=D_star a_t+i a_t^2 belong to A2,
whose k pairing vanishes; its actual adjoint has the same zero pairing.
Thus the projected normal-F law follows from the strict tangential
subalgebra; the tangential-F and mu derivative laws are NOT automatic
off shell. These restrictions must enter the future physical domain.

The existing harmonic structure background has H=mu=0. It satisfies
all these conditions and Pi_k B_n=0, with the same fixed boundary metric.
This is inherited analytic admission, not a new numerical PDE solve.

## 5. A conditional static minimum, not a physical-kernel certificate

The exact positive functional on the declared smooth domain obeys V>=0;
the admitted reference has V=0. For every smooth admitted real tangent
variation its second variation is

    delta^2 V=||delta mu||^2+||D_star delta phi||^2 >=0,
    delta mu=div_A delta B+i[delta A_i,B^i].

At zero residuals no second-order field terms survive. This all-direction
argument is stronger than a finite Hessian sample; samples test signs and
nontriviality only. A compact infinitesimal gauge parameter lambda gives
delta phi=d lambda+i[phi,lambda], delta A=D_A lambda,
delta B=i[B,lambda], delta H=i[H,lambda], delta mu=i[mu,lambda].
Hence admitted gauge tangent directions lie in the null space at the reference.
The finite point-jet control can be realized by a parameter supported in
the interior, so it does not presume arbitrary boundary gauge values.
Nonzero derivative jets must cancel; setting them to zero is not a test.

We have NOT proved an isolated/gapped minimum, positivity of the complete
Hamiltonian, well-posed time evolution, a complete gauge quotient, quantum
stability or equality with the mathematical Hodge kernel. Static A_mu=0
and fermions=0 is a priced sector. Physical Weyl phases/adjoint/maximal
domains, supersymmetric nonlinear completion, anomaly/inflow and vacuum
selection still matter. All 35 harmonic choices remain, not 35 selected
vacua and not three physical families. The complete SM/TOE is unachieved.

Primary sources read personally: [Luedeling](https://arxiv.org/html/1102.0285v1)
4.1-4.2, typeset pages9-10; [Braun et al.](https://arxiv.org/html/1812.06072v2)
B.1. Their closed-space component simplifications do not replace the
relative compact-boundary calculation above.
