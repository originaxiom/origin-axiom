# Exact hand checks supporting the source review

2026-11-09. Personal algebra and change-of-variable derivations.
No scientific program was run. These supplement the existing W f1
Clifford derivation, which remains in the preceding intake document.

## The physical S4 cusp norm

Let w=r exp(i theta) be the puncture coordinate and
Omega=ell/(r log(1/r)). Ignoring the fixed positive scale/angular factors,
the physical S^a norm of a trivial-periphery Laurent section w^-m is

    integral Omega^(2-a) r^(1-2m) dr.

For a=4 this is

    I_m = integral r^(3-2m) [log(1/r)]^2 dr.

With u=log(1/r), dr=-r du, the same norm is

    I_m = integral u^2 exp[-2(2-m)u] du.               (1)

Equivalently the physical coefficient is r^(2-m)u^2 and the area element
is du/u^2. The variable T=log y used in the source barrier argument is
a different cusp coordinate, with u proportional to y and T=log y.
It must not be substituted for u without its Jacobian and measure.

Equation(1) converges at infinity for m=1 and diverges for m=2. Thus the
strict simple-pole allowance survives the external quadrature's measure
error. On the external interval u in[2,40] the corrected values, up to
the same fixed factors, have exact expressions

    I_1 = (13/4) exp(-4) - (3281/4) exp(-80),
    I_2 = (40^3-2^3)/3.

These follow from the antiderivatives
-exp(-2u)(u^2/2+u/2+1/4) and u^3/3. The delivered quadrature instead
integrates (1)/(log u)^2. No numerical execution is needed to identify
the discrepancy. Its own earlier radial quadrature is an available
independent recovery control after an admitted repair.

## Four-cycle potential and its exact limit

For arbitrary complex p,r,f, put

    Q = p e12 + r e23 + p e34 + f e41.

Its rows and columns each have one nonzero entry, so

    QQ† = diag(|p|^2,|r|^2,|p|^2,|f|^2),
    Q†Q = diag(|f|^2,|p|^2,|r|^2,|p|^2),
    {Q,Q†} = diag(A,B,B,A),
    A=|p|^2+|f|^2, B=|p|^2+|r|^2.                   (2)

This commutes with reversal P4. For independent plus and minus factors,
the two selected weight planes have the identical diagonal compression

    diag(A_plus+B_minus, B_plus+A_minus).

Equation(2) proves the polynomial identity underlying the finite random
tests. Equality of these compressions alone is not equality of full
spectra. The actual cyclic family's Cartan connection, flat gluing and
Theta map are the separate, load-bearing global argument in
CARTAN_CYCLIC_VECTOR_PAIRING_AND_PHYSICAL_CURRENT_RESPONSE_2026_11_09.md.
Its hypotheses must travel with the pairing conclusion.

## Nonautonomous RGE stage coordinates

If v=s tau and dy/dv=v, the chain rule gives dy/dtau=s^2 tau.
Starting at0, y(1)-y(0)=s^2/2. The delivered RGE loop evaluates
s*rhs(tau,y), giving s/2 instead. At s=2 these are2 and1.
Autonomous equations do not detect this omitted argument conversion.
An initial v0 also has to be included whenever the RHS uses absolute v.
