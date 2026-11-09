# Physical output bundles and a direct neutral threshold control

2026-11-09. AUTHOR HAND ARGUMENT, UNREVIEWED. No CAS, scientific imports,
enumeration, collection or tests. Source baseline is 3234bbdd76245bcd484cbbf1bae24aab84d281da.
AGY roster d1f2125a8 is reviewed against the actual curved action and
weave_physical_mass_2026_10_08/PROOF.md. This note supplies corrections
and constructive witnesses, not an independently certified spectrum.

## 1. Read the output bundles from the physical map

Let E_m denote the smooth unitary gauge-weight bundle with geometric
spin power S^-m, where [H/2,X]=mX. Keep the original density conventions
and trace-dual target. The physical input is

    lambda in E_m,
    a in barK tensor E_m,
    (u,v) in S tensor F tensor E_m.

The weighted mass map has g=D0^dagger x in its first row, a scalar
gauge-parameter-type section. Its second row is 2it+sqrt(2) Dz lambda,
which is a (1,0)-form section. Its last two rows are the metric dual
of spin fields and use conjugate flavour transport. Consequently the
actual smooth target bundles are

    g in E_m,
    2it+sqrt(2) Dz lambda in K tensor E_m,
    (p2/Omega,-p1/Omega) in barS tensor barF tensor E_m.

Using the metric identifications barK equivalent to S^-2 and barS
equivalent to S^-1 gives the input/output power tables

| | scalar | form | flavour pair |
|---|---|---|---|
| input | S^-m | S^(-2-m) | S^(1-m) tensor F |
| output | S^-m | S^(2-m) | S^(-1-m) tensor barF |

These smooth metric identifications are not replacements of the
holomorphic structures used in a sheaf calculation. AGY's output
powers S^(1-m), S^(-1-m), S^-m have the wrong geometric weights.
Already at m=0 the scalar output g cannot acquire a spin factor.

One can also check the spin row directly under a holomorphic coordinate
change with t=dz/dw. A spin coefficient gains t^(1/2), Dbar adds bar(t),
and division by Omega adds |t|^-1. The result is bar(t)^(1/2), the
conjugate-spin target. The density weights remain Omega^2,1/2,Omega,Omega
in their respective coordinate frames. Their metric volume factors and
the target convention must travel with all operator comparisons.

If the compact spin choice is written as an explicit order-two flat
character eta AFTER factoring a reference spin bundle, its core factors
are eta^-m Ad_K on lambda,a and eta^(1-m) rho Ad_K on the spin pair.
The output has eta^-m Ad_K and eta^(-1-m) bar(rho) Ad_K. These are
already included when the corresponding powers of S carry that spin
choice. Do not count eta twice or omit its gauge-induced power.

## 2. The mixed V_(2,2) spin states give a full physical Weyl sequence

The old neutral note was explicitly exploratory. Its critical endpoint
can be tested directly in the ORIGINAL four-slot operator, without
identifying compact H1 with a physical kernel.

In the balanced flavour coordinates, q' is proportional to E_+ and r'
to E_-. Carry the epsilon pairing through this constant unitary change
of coordinates. In V_(2,2) choose normalized vectors

    v_u=|-2,+2>, v_v=|+2,-2>.

Both have total m=0. The actual raising/lowering actions give

    E_+^dagger v_u=0, E_- v_u=0,
    E_-^dagger v_v=0, E_+ v_v=0.

For lambda=a=0, u'=f(t)v_u, v'=0 on a cusp, these identities kill
EVERY Higgs term in the scalar and form output rows. The only remaining
mass-map output is the spin derivative of u'. The same holds with
u'=0,v'=f(t)v_v. The induced gauge spin connection vanishes at m=0.
The full cusp transition is +1 in this integer-root D5 block, so a
zero-angular coefficient is admitted on either coherent phase.

Use canonical physical spin coefficients, with radial norm a fixed
positive multiple of integral |f(t)|^2 dt, t=log y. Just as in the
existing A3 tail calculation, the remaining mass row has derivative
norm bounded by c_ell ||f'||. There is no residual commutator mass.
Choose smooth normalized chi supported in (0,1) and

    f_L(t)=L^(-1/2) chi((t-L^2)/L).

After the fixed circle/coefficient normalization the full physical input
has norm one, escapes every compact set, and satisfies

    ||M psi_L|| <= c_ell ||chi'||/L -> 0.

The fields lie in the compact-support core. In the self-adjoint doubled
operator [[0,M^dagger],[M,0]], use (psi_L,0). This is a singular sequence
at zero, proving the asserted V_(2,2) threshold at author/hand scope
DIRECTLY on the physical domain. No finite boundary projector, compact
Euler characteristic, auxiliary zero mode or gauge quotient was used.
It neither counts the global L2 kernel nor establishes a finite gap.

This control is conditional on the exact balanced asymptotics and
complete cusp. It survives changes confined to a compact core. Other
asymptotics, generated carriers or earned end dynamics need their own
analysis. The half-root block has antiperiodic full cusp transport and
does not admit this zero-angular sequence. Thus the argument preserves
the actual 120/128 distinction rather than universally excluding OA.

## 3. Construct the vector-block comparison instead of asserting it

On W=V_(2,0) direct sum V_(0,2) put Z=diag(+1,-1). The bare A
exchanges the two summands and obeys AZ=-ZA. D commutes with Z.
The unitary map

    T=exp(i pi Z/4)

is scalar on each triple module and therefore commutes with the actions
of E_+,E_-, their adjoints and H. Direct algebra gives

    T A T^-1=-i A Z,
    T (i A) T^-1=A Z, T D T^-1=D.

T^-1 instead sends iA to -AZ. These are explicit intertwiners from the
connected corrected vector transition to the two outer axis/vector
types. Keep their physical source and trace-dual target maps. This
supports the comparison of the UNLABELLED linearized vector blocks.
The unbroken gauge representations are 3+bar3 versus 1+5. It is not
an E8 gauge equivalence or a proof that the full cubic vertices coincide.

## 4. Label the outer half-root packages by X

On the combined 128 block, h1^2=Zeta=-1, so h1 has eigenvalues +/-i.
It cannot itself label eigenvalues alpha=+/-1 as in AGY's roster wording.
Those are eigenvalues of X=A h1 on the simultaneous highest space.

That space has dimension 8, two equivalent Spin5 four-plets coming
from (16,4) and (bar16,bar4). X interchanges them, commutes with the
surviving Spin5 and squares to K_pi=+1 there (m=3,Zeta=-1). Thus it
has a +1 four-plet and a -1 four-plet. Extend each highest vector by
the two lowering strings. The identity

    X (E_+^dagger)^n (E_-^dagger)^k v_top
      =alpha i^(n+k) (E_+^dagger)^k (E_-^dagger)^n v_top

and the diagonal D weights specify its whole 16-dimensional module.
This justifies the two 64-dimensional X-labelled packages while retaining
the interchange of the original half-root summands. Any claim about
global kernels still needs the weighted contraction, actual domains,
all target maps and full physical interactions. Dimensions alone do
not provide that transfer.

## 5. Retain both extremes of the paired vector fibre

For V_(2,0)+V_(0,2), both independent highest vectors survive in
Koszul degree zero and both lowest vectors survive in degree two.
The first degree has four mixed representatives, two at each of
the powers 3 and -1. The ranks are therefore

    rank(G0)=2, rank(V3)=2, rank(V_minus1)=2, rank(G2)=2.

The aggregate Koszul ranks are (2,4,2) on each 10-dimensional vector
fibre. This follows also by tensoring the one nontrivial raising string
with the zero string on each five-dimensional summand. The old up-sector
proof already retains these ranks and the two top characters. The new
roster's phrase 'rank-1 extremes' must be corrected before kernel counts.
