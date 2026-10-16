# Full decaying zero-energy space, not a transverse chirality verdict

Authored BEFORE execution. Same supplied local end/operator/dictionary;
global core/domain/quantum admission are separate. Finite exact controls
verify implementation, not nonauthor acceptance. All statements below are
per one fixed Fourier/coefficient channel, not a complete universe census.

## 1. Retain the whole first-order equation

Use the prior verified Q=D+D* with masks(0,r,X,rX,Y,rY,XY,rXY).
For K>0 rotate tangent axes so momentum is along X. Write a=ell exp(-r/ell),
L=K/a, W=mu exp(2r/ell) and

    A0=partial_r+W+1/ell,
    A1=partial_r+W,
    A2=partial_r+W-1/ell.

Adjoints are -partial_r plus the same multiplication term in flat L2.
The actual equation splits into FOUR2-component FIRST-ORDER systems:

    (scalar,rX): [[A0,iL],[iL,A1*]],
    (r,X):      [[A0*,-iL],[-iL,A1]],
    (rY,XY):    [[A1*,-iL],[-iL,A2]],
    (Y,rXY):    [[A1,iL],[iL,A2*]].

The first/third inputs are even forms, the second/fourth odd. These
systems—not a separate scalar transverse Schrödinger equation—determine
zero-energy Q data. D+D* can cancel across adjacent degrees. A sum of
pure-degree closed/coclosed spaces need not be the full first-order kernel.

## 2. One scalar function supplies ALL four decaying channels

Let phi be the positive normalized decaying solution of

    H0phi=0, H0=-partial_r2+W2+ell^-2+L2, phi(0)=1.

Each2-system reduces exactly to this scalar equation by eliminating one
component using L!=0. Set c=A0phi and d=A2*phi. The four columns are

    b0=phi scalar + i c/L rX,
    b1=c r + i L phi X,
    b2=i L phi rY + d XY,
    b3=i d/L Y + phi rXY.

Direct full8x8 substitution uses phi''=(W2+ell^-2+L2)phi. It tests every
component, not only the one used to eliminate. Conversely every solution
of each2-system reconstructs phi from its scalar, X, rY or top component.
If the original vector is L2, that scalar is L2: the only divisions are by
L, which is bounded below and grows. Thus there is no hidden second L2
scalar branch. The four supports are disjoint, hence independent.

For beta=|mu|>0, x=beta ell exp(2r/ell), delta=K2/(4 beta ell),

    phi proportional to x^(-1/2) W_(-delta,1/2)(x).

Its Tricomi representation has positive parameter1+delta and positive
Euler integrand for x>0. It never vanishes. The decaying asymptotic is
exp(-x/2)x^(-delta-1/2); multiplying by W,L or1/L still leaves an L2
function. A second independent scalar solution is phi int phi^-2 dr;
the same asymptotic makes it grow like exp(+x/2), not L2. This proves
completeness, not stabilization of a finite sample.

For mu=0,K>0, the same scalar function is K_1(K exp(r/ell)); direct
substitution and its decaying positive asymptotic give the analogous
unique L2 scalar branch. See the personally checked primary definitions
[Whittaker](https://dlmf.nist.gov/13.14) and
[Tricomi integral](https://dlmf.nist.gov/13.4.E4), and
[modified Bessel](https://dlmf.nist.gov/10.25). These functions do not
select mu,K,ell or an E8 parent.

Therefore the complete first-order decaying space for K>0 has complex
dimension4:two odd,two even. The mixed scalar/degree2 and degree1/top
channels must NOT be omitted because the transverse response is positive.

## 3. The actual boundary plane and physical field map

At any cut, put F=phi>0,G=phi',c=G+(W+1/ell)F and
d=-G+(W-1/ell)F in the columns above. Rank4 follows already from the
nonzero F and L factors. With Cr=epsilon_r-iota_r, direct multiplication
gives B* Cr B=0:the half-dimensional plane is maximal null. Equivalently
the normal Green current between any two decaying Q solutions is
constant and vanishes at infinity. The explicit check binds the actual
fields, rather than concluding nullity from its dimension alone.

The prior norm-preserving physical map is NOT replaced:

    Sodd(lambda,rho)=rho+lambda vol,
    Seven(f,v)=-f+*v,
    Q Sodd=Seven R, Q Seven=Sodd R*.

Under Sodd the two odd columns become

    (lambda,rho_r,rho_X,rho_Y)=(0,c,iLF,0),
    (lambda,rho_r,rho_X,rho_Y)=(F,0,0,i d/L).

They are local candidate Weyl-operator Cauchy data, not two new particles.
Mixed gaugino/chiral components are allowed by the full FIRST-ORDER bulk
equation. Whether they meet the actual core/allowed real gauge/bosonic/
supersymmetric response is not established here. In particular the compact
charged lambda=0 interface law cannot simply be silently discarded or
silently applied as if gluing had not changed that domain.

## 4. Angular zero, basis limits and the neutral threshold

At K=0 the four systems decouple. For mu>0 their decaying supports are
scalar,X,XY,Y, with factors exp(-r/ell-int W), exp(-int W),
exp(+r/ell-int W), exp(-int W). For mu<0 they are rX,r,rY,top,
with exp(+int W), exp(+r/ell+int W), exp(+int W), exp(-r/ell+int W).
Both have dimension4/two odd/two even. Pure-degree distributions differ;
these are NOT physical chirality/generation counts.

K>0 formula columns contain1/L and can vanish/diverge as K tends to0.
The subspace, not a singular basis, is the object to compare. At fixed
nonzero mu the scalar log derivative is smooth in K2, and the normalized
column/projector limits yield exactly the corresponding four supports.
Indeed the Euler integrand is t^delta(1+t)^(-delta) exp(-x t).
For delta in a compact interval containing0 its derivatives in delta
are dominated near0 by integrable logarithmic powers, and at infinity
by exp(-x t) times powers. Differentiation in x has the same domination.
Hence at the fixed cut G=-beta-1/ell+O(K2). For mu>0, c=O(K2) and
d=2beta+O(K2); for mu<0, c=-2beta+O(K2) and d=O(K2). Substitution
in the four disjoint2-component projectors gives the stated limits,
without mistaking a singular column normalization for a vanished mode.
Numerical tests compare projectors at declared small K, not claim exact
zero-angle equality at finite K or count a vanishing column as a lost mode.

At the JOINT neutral corner mu=0,K=0, only scalar and top exp(-r/ell)
are L2. Tangential constant channels are zero-energy resonances, not L2;
radial/XY exp(+r/ell) grow. Thus the end has the retained zero threshold,
not a uniformly isolated four-channel gap. The limit in this corner
cannot be confused with fixed-nonzero-wall continuity.

## 5. What remains

This computes zero-energy end Cauchy data of the SAME local operator,
retiring its uncomputed zero-plane duty only. It does NOT compute the
frequency-dependent matrix response, full core match, index on the new
noncompact domain or normalized interactions. Full normal, vector/real
gauge, fermion and whole-superfield domains must be joined before a
global particle claim. Both charge signs and neutral continuum retained.
Actual field/core selection, parent/metric/phase/amplitude inputs, integral/
torsion holonomies,3 generations, realistic Higgs/extras/parameters/quantum/
gravity/register/observer/qualia remain duties. No selected SM/TOE or a
programme-wide no-go is derived from this local zero-space theorem.
