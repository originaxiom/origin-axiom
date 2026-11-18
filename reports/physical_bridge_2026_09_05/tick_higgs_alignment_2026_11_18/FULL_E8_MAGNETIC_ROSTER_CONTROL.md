# Keep all E8 directions in the compact magnetic action control

2026-11-18. P-C8 author hand calculation, not independently checked.
No scientific execution, import, CAS or tests. This supplements the
local action field map sealed at 0217bd0b3. The compact torus, degree
three, Cartan flux and action are its supplied premises. This is not
the spectrum of the separate complete-cusp background or of the whole
generated architecture.

## 1. Recover the existing root-SU2 decomposition, do not rediscover it

The root-SU2 branching into 133 singlets, 56 doublets and one triplet
is already in weave_cusp_condensate_2026_10_08/PROOF.md:142–148.
Its E7 centralizer is also in weave_global_condensate_2026_10_08/PROOF.md,
in the section on the actual unbroken compact algebra. Those are prior
finite algebraic positives, reused here with a different operator.
Their cusp threshold and gluing statements are not transferred to a torus.

In the selected A2 let alpha=e1-e2, beta=e2-e3. Its Cartan
C=H_alpha+H_beta is the coroot of alpha+beta=e1-e3. Thus its E8
adjoint weights are precisely the root-SU2 Cartan weights 0,±1,±2.
The following direct count avoids a numerical root loop.

## 2. Count every root and Cartan coefficient

Use the standard E8 root realization:

    ±e_i±e_j, i<j,                                  112 roots,
    (±e1±...±e8)/2, an even number of minus signs,   128 roots.

For charge q under C, q=r_1-r_3 on a root r. Among the first kind,
the roots C and -C alone have q=+2,-2. The q=+1 roots contain e1
with coefficient +1 and another coordinate other than e3 (12), or
e3 with coefficient -1 and another coordinate other than e1 (12).
There are 24; likewise 24 of q=-1. The remaining 62 have q=0.

Among the half-integer roots, q=+1 fixes signs s1=+,s3=-.
The remaining six signs must have odd minus parity, giving 32 choices.
There are likewise 32 of q=-1, and 64 of q=0. Add all eight Cartans,
which have charge zero. The full 248-dimensional coefficient roster is

| Charge q | Root coefficients | Cartan coefficients | Total |
|---|---:|---:|---:|
| -2 | 1 | 0 | 1 |
| -1 | 56 | 0 | 56 |
| 0 | 126 | 8 | 134 |
| +1 | 56 | 0 | 56 |
| +2 | 1 | 0 | 1 |

The dimensions sum to 248. With no additional nontrivial Wilson line,
the continuous flux centralizer has algebra e7+u1. Cartan Wilson
holonomies may reduce its global unbroken algebra; degree-zero root
profiles need their actual flat character before being counted massless.
Neither this pointwise centralizer nor its dimension is the SM group.

If kappa is specifically the adjoint trace Tr_248, this table also
gives kappa(C,C)=112+8=120. Its restriction kappa=iota tr_3 has
iota=60 because tr_3(C²)=2. This fixes a convention-dependent trace
factor; it does not determine the physical gauge coupling. The local
action proof keeps iota explicit and is compatible with this value.

## 3. Actual transverse negative modes, not just a coefficient capacity

In the compact action control the root line of charge q has degree
3q, with whatever commuting flat Cartan Wilson factors are retained.
For q<0 its negative degree implies no holomorphic sections. On an
elliptic curve Riemann–Roch therefore gives

    dim_C H^1(L_q)=-3q.

Hodge representatives are (0,1)-forms obeying D_z a=0, hence the
real connection tangent has zero linear curvature and zero real
gauge divergence. Each is an actual finite-norm transverse variation,
with the inherited Hermitian conjugate in the real connection. A
root and its conjugate are not counted as two independent complex
negative-mode species.

For normalized E_q with [C,E_q]=q E_q, trace invariance gives

    kappa(C,[E_q,E_q†])=q kappa(E_q,E_q†).

The quadratic curvature is [a,a†]/2. Dividing its cross term with
F0=B C by the same one-half connection kinetic norm yields the
physical mass squared

    m_q²=q B<0, B=6pi/A_T.

Thus the full root count exhibits the following mutually independent
complex negative connection directions in this particular background:

| Root charge | Number of roots | Modes per root | Complex negative directions | Mass squared |
|---|---:|---:|---:|---|
| -1 | 56 | 3 | 168 | -B |
| -2 | 1 | 6 | 6 | -2B |
| Total | | | 174 | |

Their real dimension is 348. The statement needs no choice of a
special point in the Wilson torus: tensoring these negative-degree
lines by flat unitary characters does not change their H^1 dimensions.
The unitary mode norms and transversality were derived from the actual
action. This is stronger than counting 174 available coefficients,
but it is still an author hand argument pending independent checking.

The six-mode Higgs band is the most negative band here, not an
isolated complete low-energy theory. The other 168 negative directions,
degree-zero Wilson/gauge modes, matter fields and their interactions
cannot be eliminated as a positive massive complement. No scalar
index is used to declare a chiral or vector-like SM spectrum.

## 4. How this changes the next calculation

The Cartan relaxation of the single-band proof remains an exact
admitted path and a countercontrol to its frozen quartic. It is not
a normal solution for the full 174-direction unstable sector. The
full stationary problem must retain those directions, or provide an
action-derived stabilizer and check its effects on the claimed matter
and gauge fields. Deleting them by a projector would add a physical
condition, not derive a vacuum.

This scoped instability is not a programme-wide exclusion. The
curved parallel cusp construction has different spin curvature,
background Higgs fields, gauge potential and domains. A larger
generated geometry or physical source/end law can change the operator;
its effects have to be derived on all these fields. The control shows
exactly why a local overlap realization alone does not complete that
physical bridge. Foundational inputs removed: zero. Full vacuum
selection, SM3 and gravity remain open.
