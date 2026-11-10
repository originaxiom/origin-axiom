# Full cut variation, supported blocks and binding repairs

2026-11-10. Exact AGY head `95cec984eb523bea7e04c287ed4bed6d19ed2d38`.
Decision `PARTIAL_HAND_RESULT_SUPPORTED_WITH_BINDING_REPAIRS`.
Personally checked source formulas and hand algebra. No scientific module,
CAS, test collection or new numerical control was run for this packet.
This seat authored several action, transmission and response dependencies.
This collaborative source review leaves formal nonauthoring review,
main acceptance, execution admission and banking outstanding.

The original author packet and its first errors remain at the reviewed
commit. The receipt records exact hashes. Every full SHA-256 dependency
named in the proof matches its Git source. Matching a hash establishes
source identity. Mathematical support below comes from the stated checks.

## Supported results to preserve

The bosonic boundary potential at line20 follows by integrating the
declared action's connection and spin derivative terms. In particular,
`delta F_mu,a=-D_a delta V_mu+...`,
`delta F_xy=D_x delta A_y-D_y delta A_x` and
`delta R_q=Dbar delta q+[delta A_y,q]-i[delta A_x,q]` give the printed
outward momenta at lines22–23. The corresponding bosonic radial Gauss
equation at line27 has the source commutators and signs. Fermionic
backreaction on that equation remains a later duty.

The displayed coordinate mass map at line34 reproduces the source map,
including every Omega coefficient. Its displayed `M*` is the weighted
formal adjoint on compact-support sections in the corresponding local
input/output frames. The coordinate Hermitian Green pairing at line39
is correct. With `n_-=n_x-i n_y` and `n_+=n_x+i n_y`, its matrix is

```text
C_n = [[0,-n_-/sqrt(2),0,0],
       [n_-/sqrt(2),0,0,0],
       [0,0,0,n_+],
       [0,0,-n_+,0]].
Gamma_coord = [[0,-C_n*],[C_n,0]].
```

The four row densities cancel the derivative coefficients as claimed.
For example, `Omega^2 M_01=-D_z/sqrt(2)` and
`(1/2)M_10=D_z/sqrt(2)`. Compact-adjoint commutator terms cancel in
the Hermitian Green identity. The opposite outward normals therefore
cancel the two raw Green forms on the common diagonal trace graph.

At a regular finite cut, positive smooth metrics and ellipticity give
the usual local trace setting. The diagonal graph has half the trace
dimension and equals its Green annihilator. With the inherited complete
operator and remote domain fixed, it recovers transparent transmission.
The bosonic momenta sum to zero under the common variation. Preserve
the distinction between this cancellation and the remote cutoff estimate.
This establishes an interface law within the supplied parent. Solving
the nonlinear response requires additional existence and domain work.

The two previously requested notes in `FORM_SPIN_VECTOR_OPERATOR_JOINT.md`
are incorporated. Its graph-closure statement now uses each operator's
own graph norm. The converted derivative adjoint retains the differentiated
Omega factor. Earlier conditional lepton ranks, parity scope and unresolved
form-vector spectral target retain their previous grades.

## R1. Correct the physical trace normalization

Lines41–45 confuse the kinetic density against `dx dy` with the physical
fibre metric against `dvol=Omega^2 dx dy`. For the eight-slot density `h`,

```text
G = Omega^-2 h,
||Xi||^2 = integral dx dy Xi* h Xi
         = integral dvol Xi* G Xi.
hatXi = G^(1/2) Xi = Omega^-1 h^(1/2) Xi.
```

Thus the physical orthonormal input coefficients are
`(lambda, a/(sqrt(2)Omega), u/sqrt(Omega), v/sqrt(Omega))`, with the
corresponding output coefficients. Since `ds_phys=Omega ds_0`, the
actual boundary matrix conversion is

```text
Gamma_phys = Omega h^(-1/2) Gamma_coord h^(-1/2),
C_phys = Omega h_out^(-1/2) C_n h_in^(-1/2).
```

This gives the unit-entry matrix printed on the right of line44. For
instance, its `(0,1)` entry is
`Omega (1/Omega)(-n_-/sqrt(2))sqrt(2)=-n_-`.
Consequently `Gamma_phys*=-Gamma_phys` and
`(i Gamma_phys)^2=I_8` for a coordinate unit normal.

The packet instead puts `Omega^-1` in this conversion and uses
`h^(1/2)Xi` as the physical coefficients. Its formula gives
`C_phys=Omega^-2 C_unit`, whose doubled square is `Omega^-4 I_8`.
That contradicts its asserted unit matrix for general Omega. Correct
the density, coefficient frame and measure together. The repaired
formula uses the existing metric and introduces no choice of metric.
The coordinate Green identity and diagonal sewing survive this repair.

## R2. Separate the Weyl transpose and Hermitian test bundles

Line33 defines `Phi` in the output Hilbert bundle. Lines37–38 then apply
`M` to that same `Phi` in a bilinear transpose formula. In the physical
source, `M_q` maps charge-q left profiles into the conjugate Hilbert
bundle of the opposite-charge left profiles. A Hermitian output test
field and an independent opposite-charge left input have different types.

Use an independently named `chi` in `H_in,-q` for the Weyl bilinear,
with the invariant complex trace pairing, and keep `Phi` in `H_out,q`
for the Hermitian Green identity. In corresponding trace-dual frames,
the source transpose statement is

```text
B_q(p) = B_-q(-p)^T,
B_q = h_out,q M_q,
```

where `B_q` denotes the density-valued bilinear map. Its differential
version pairs `chi` with `M_q Psi` and `Psi` with `M_-q chi`, including
the boundary term and momentum reversal. The component expression in
line38 can be retained after giving these two independent inputs and
the actual trace identification. The Hermitian line39 already has the
right input/output roles. This repair earns no identification of the
independent opposite-charge left fields.

## R3. Repair the superpotential cut sign

Line24's oriented expression is correct. The packet itself states
`dz|oriented=-sigma_R dx` at this cut. Therefore

```text
delta W_boundary = -i/2 integral_oriented (q delta r-r delta q) dz
                 = +i sigma_R/2 integral_0^1 (q delta r-r delta q) dx.
```

Its second equality currently has the opposite sign. The opposite-side
cancellation survives, while each one-sided primitive needs the fix.

## R4. Restore the actual neutral kernels and threshold carriers

Lines69 and73 contradict the packet's own pinned neutral and joined
kernel sources. The source decomposition is

| Block | Normalizable left slots | Critical spin contribution |
|---|---|---|
| `W_1` | `1 a`, `0 lambda`, `0 spin` | Surviving exponents `{-1,2,0,3}` avoid1 |
| `W_3` | `3 a + 2 spin`, `0 lambda` | Surviving exponents `{-3,4,-2,5}` avoid1 |
| `V_(2,2),perp` | `2 a`, `0 lambda`, `0 spin` | Noncritical complement |
| `S tensor V_1^(2,2)` | `0 left`, `0 adjoint` | Decoupled rank-two `a=1` threshold |
| `A_3=(1,15)` spin/flavour fields | `0 spin` |15 coefficient directions with free cusp spin channels |

The neutral `D_5` count `(1,5,2)` totals six form-slot and two spin-slot
left profiles. It contains no gaugino profile. The separate centralizer
has nine scalar/gaugino and nine form modes on `h_4`, with the ten/ten
outer-phase counterpart retained from the earlier source.

The exact neutral critical input is the balanced-flavour pair

```text
(u',v') = (f_1 |-2,+2>, f_2 |+2,-2>) in V_(2,2).
```

Both incoming and outgoing Higgs maps vanish on this pair. Its global
orthogonal splitting and escaping logarithmic-cusp sequence establish
zero essential spectrum for the doubled or squared realization.
The `A_3` spin/flavour block supplies the other threshold channels.
The earlier sources already contain these positives.

Peripheral `Ad(Zeta)=+1` only supplies integer gauge-coefficient cusp
frequencies. Higgs couplings, the spin/flavour factors and the global
domain still matter. It does not make the whole `W_1+W_3` spin block a
zero-mass free operator. Withdraw the claimed twelve-dimensional
threshold carrier there. Preserve the zero-energy elimination obstruction
on the actual critical carriers.

For a selfadjoint nonnegative squared realization `L`,
`(L+s)^-1` is bounded for `s>0`. For the doubled realization use an
off-real resolvent parameter. At a finite cut specify the one-sided
realization or use its Cauchy response relation. The compactly supported
escaping sequence proves the end obstruction across compatible regular
cut realizations. Retain the threshold limit as an actual response duty.

## Reuse and scope notes

The response table should name the flat flavour bundle `F` in the
spin-field types. Its local formulas may use parallel frames, with
their global transitions and epsilon pairing transported.

The finite-frequency core response already has an analytic expression
in the next cited source. Its concrete core Neumann data remain
unevaluated. Remove the suggestion that the whole formula is missing.
Carry the source quartic's overall negative Schur-exchange coefficient
`-1/(2g6^2)` together with both terms in its bracket. The table's plus
between the transverse and Gauss terms is an internal relative sign.
Harmonic coordinates, compatibility pairings and restricted inverses
remain present.

The mass-source line locator255–308 is stale for the matching Git blob.
Cite its named operator/transpose sections or refresh that locator.

## Disposition and next return

Release `AGY-03a-r1` for one bounded hand/source repair. Carry R1–R4
through the proof, reuse table, input table, RESUME and relay. Bundle
the reuse notes. The common trace law and source reuse are genuine
partial progress. Full matter/fermion response, nonlinear coupled
stationarity, backreaction and the registering-to-action map remain
open. Canonical independent inputs reduced by this packet remain zero.

The earlier22-test external reproduction tested an older finite package.
It supplies no executed control for these new operator/trace assertions.
Keep the received formal statuses unchanged and stop after the repair
checkpoint for review.
