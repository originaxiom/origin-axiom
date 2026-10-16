# Critical fundamental solutions and the interacting boundary response

Authored before execution. This is a conditional local theorem for the
SAME supplied source, root and background as surface_root_gauge_sector.
It is not foundational selection, all-angular ellipticity, full curved
SUSY/source boundary dynamics or a physical SM spectrum.

## 1 Exact complete zero momentum fundamental matrices

Set x=g sqrt(r), s=1-x^2. The saved equation becomes

 f_x+[C0/x+x D/s+Y/s+beta x A]f=0, beta=rho/g^2.

At j=etaR/4 all4blocks are isometric to the following canonical models.
The complete coefficient identities, including A and normal current,
are checked; negative angular/module sectors are not inferred by name.
With coordinates(1,4) and(2,3), K0 splits as Kplus and -Kplus,

 Kplus(doublet)=[[1/x-x/s,2/s],[2/s,-x/s]],
 Kplus(triplet)=[[1/x,2sqrt2/s],[2sqrt2/s,-2x/s]].

In the positive subspace a bounded critical vector v is respectively

 v_d=(-x,1)/s^(3/2), v_t=(-sqrt2 x,1+x^2)/s^2.

Define w=x s(v2,-v1). It is the regular negative-subspace solution.
A second negative-subspace solution L is

 L_d=(2x log(x)-x^3, 1-2x^2+2x^2 log(x))/sqrt(s),
 L_t=(2sqrt2 x(1+x^2)log(x)-4sqrt2 x^3,
      1-4x^2-x^4+4x^2 log(x))/s.

Reference derives these by L=w u+(0,x s/w1), where
u'=Kplus12 x s/w1^2. The primitives are 2log(x)-x^2 and
2sqrt2(log(x)-2x^2/(1+x^2)). An additive constant is a regular seed,
not a different critical trace law. Directly det(w,L)=x s, v.w=0,
v.L=1. Thus u_bad=(L2,-L1)/(x s) is the other positive solution.

Embed columns in order bad,critical-plus,regular,critical-minus:

 F0=[(u1,0,0,u2),(v1,0,0,v2),(0,w1,w2,0),(0,L1,L2,0)].

Check F0'+K0 F0=0 and its full nondegenerate constant Green Gram.
It pairs bad with regular and critical-plus with critical-minus.
The bad column grows as1/x and is not in L2(x dx); the other three
are bounded, regular is O(x), and the minus branch has x log(x).
For sigma+ the Cauchy plane is span(v,regular); for sigma- it is
span(L,regular). Both are rank2 Green-null, NOT particle counts.

At zero momentum the sigma+ orthogonal projector has the two lines
(-x,0,0,1),(0,1,x,0) for the doublet, and
(-sqrt2 x,0,0,1+x^2),(0,1+x^2,sqrt2 x,0) for the triplet.
Their squared norms are1+x^2 and1+4x^2+x^4. Sigma- is the entire
(2,3) plane, but excluding its logarithmic solution would incorrectly
shrink its solution space. Replacing log(x) by log(x/kappa) adds
-2ell log(kappa)w (ell=1,sqrt2): the same plane and critical pairing.
The sigma+ projector varies with background/cutoff; P P' P=0 and
the differentiated Green identity must accompany field variations.

For a singleton2block, C0=diag(d,-d), D=diag(bh,-bh), Y=0, with
d in{0,+1,-1} and |h|<=2. F0=diag(x^(-d) s^(bh/2),
x^d s^(-bh/2)) solves the full equation, including Cartan response.
At d=0 both modes are bounded and sigma selects one; at |d|=1
exactly one is regular O(x), the other non-L2. Singlets recover the
old free response, not an additional interacting family count.

## 2 Controlled finite momentum construction

For each coupled4block choose0<a<=1/4. Euclidean column bounds are

 ||bad||<=16/x, ||v||<=4, ||regular||<=4x, ||L||<=8.

These follow by the triangle inequality from the displayed formulas,
s>=15/16, sqrt2<=2, x|log(x)|<=1. The last inequality follows by
maximizing -x log(x) on(0,1); no numeric grid is used. The complete
Green Gram gives inverse row bounds4x,8,16/x,4 respectively. Hence

 ||F0(x)F0(y)^(-1)||<=64(y/x+1+x/y), 0<y<=x<=a.

||A||=2. Define on bounded continuous functions with a limit at0

 Vf(x)=-beta F0(x) integral_0^x F0(y)^(-1)y A f(y)dy.

The estimate integrates to (704/3)|beta|x^2<256|beta|x^2.
Thus q=256|beta|a^2<1 makes f=sum_n V^n f_seed convergent for
each bounded seed, with remainder<=q^(n+1)||f_seed||/(1-q).
This is a constructive exact response at every finite beta; choose
a sufficiently small, then continue uniquely across any closed
annulus up to x<1 by the iterated-integral series bounded by exp(M L).
No uniform fixed-cutoff high-frequency angle follows from that step.
The singleton estimates are smaller and use the same256constant.

Running-supremum bounds give Vf=O(x^2) for a bounded seed and
Vf=O(x^3) for a regular O(x) seed. Thus leading critical and regular
coefficients, and the required resonant logarithmic dressing, remain.
Green conservation transports each chosen plane to every finite cut.
Its limiting current is zero, so it remains maximal Green-null.
The finite-momentum response is this convergent integral construction,
not an interval-evaluated numeric matrix or uniform symbol theorem.

Completeness is also controlled. The three bounded solutions stay
independent by their distinct leading critical/regular coefficients.
Trace K=0, so the Wronskian of any four independent solutions is a
nonzero constant. Hadamard's bound applied to these three columns,
whose norm product is O(x), forces every fourth independent solution
to have norm>=c/x. It is non-L2(x dx). Consequently the bounded
three span ALL L2 solutions; each sigma condition selects exactly two.
For singleton |d|=1 the same constant-Wronskian argument with its
regular O(x) column excludes a second L2 solution; d=0 is a regular
ODE with two bounded solutions. These are finite-block local statements,
not an unjustified completeness claim over untested angular integers.

## 3 Full actual nonlinear BPS tangent control

Differentiate the SAME root background with respect to g, including
connection and scalar components, not merely the leading half-pole.
In normalized root coordinates(E+,-H/sqrt2,E-), its components are

 a2=(0,i sqrt2 g sin(theta)/s^2,0),
 a3=(0,-i sqrt2 g cos(theta)/s^2,0),
 a4=(q/2,0,q*/2), a5=(q/(2i),0,-q*/(2i)),
 q=exp(-i theta/2)(1+x^2)/(sqrt(r)s^2).

Using the earned source lambda projector, psi=-sum_a v_a P_lambda
tensor a_a. Undo the SAME spin and scalar frames and set f=sqrt(r)psi.
The full angular identity is f(theta)=exp(i theta etaR/4)f(0), Jf=etaR f,
and its actual full48component radial residual is zero. The leading
critical sign is sigma+, but the bounded connection component is
essential. Recover its entire triplet-v profile in every actual source
spin block, both W signs and both degeneracies. Full source Majorana
pairing is verified, not assigned to an isolated pseudoreal4block.

This is an important known-positive control and local tangent, not a
global admitted zero mode, selected physical fermion or all nonlinear
boundary superpartners. Full boundary variation must also differentiate
its field-dependent response. Parent/root/action/metric/holonomy and
critical choice remain supplied. All angular integers, curved normal,
both ends, common boson/auxiliary/source/SUSY boundary action, global
stationarity and whole normalized charged spectrum/anomalies/extra
field fate, foundational SM/three/parameters and gravity remain duties.
