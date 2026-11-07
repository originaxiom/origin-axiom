# The coupled half-root kernel and its sensitivity to the core lift

2026-11-07. **UNREVIEWED conditional hand derivation.** No scientific
module, CAS, producer, collection or tests were run. This extends the
coupled quaternion construction, not the accepted scope of an earlier
finite check or independent review. It needs particular scrutiny of the
equivariant contraction and complete-domain passage below.

Quantifier: the entire 128 half-root block of the stated balanced E8
stationary bundle on the complete once-punctured elliptic curve, with
the old nontrivial order-three Wilson character retained. Compare the
bare full Spin10 lift with the two specified electromagnetic corrections
that extend to the continuous Pin2 compensator. Keep the physical spin
and all four Weyl slots. Conclusions travel with the complete marked
bundle, rather than being assertions about every generated carrier.

## 1. The named dependency and source reuse

The [discrete-sector estimate](CONFINED_HALF_ROOT_SECTOR_AND_SURVIVING_CONTINUUM.md)
gives a finite-kernel problem despite the centralizer continuum. The
[index proof](QUATERNION_SECTOR_INDEX_AND_WEAK_CURRENT_DUTY.md) gives zero
net index under U3. Neither counts the actual kernels.

The [old full two-triple kernel](ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md)
already constructs the bounded Koszul retraction of the physical complex.
Its old flat/spin characters cannot be copied into the new bundle. Here
reuse its local contraction and compute the **new action on its surviving
lines**. The full mass-map isometry is the existing source's
`M=Uout T Uin`, with the actual weighted domains and trace-dual target.

The half-root source consists of `(16,4)+(bar16,bar4)`. Under the two
principal Spin5 triples each 16 is `V_(3/2) tensor V_(3/2)`. Thus no
spinor-product coefficient is discarded. The complementary four branches
under the actual U3 as `1_(+1)+3_(-1/3)`; the other four is its conjugate.

The old Wilson acts on the former singlet by 1 and on its triplet by a
nontrivial character chi of order three. On the conjugate coefficients
it acts by their inverse characters. This is a supplied old Wilson datum,
not a selection made by the following calculation.

## 2. Reduce the local complex, retaining the new transitions

At the balanced state the unitary flavour change

    (q',r')=((q+r)/sqrt(2),(q-r)/sqrt(2))

gives multiples of `(E_+,E_-)`. In this flavour frame

    rho(Fi)=i sigma_x,   rho(Fk)=diag(i,-i).

This is a change of field coordinates, not an additional physical
SU2 symmetry: its determinant is -1. Transport the epsilon pairing and
the degree-two slot with it. No unchanged-superpotential assertion or
removal of a physical phase is inferred from that coordinate change.

The gauge compensators are A and D, with B=DA. Both bare and corrected
versions obey

    Ad_A E_+=-i E_-,     Ad_A E_-=-i E_+,
    Ad_D E_+=-i E_+,     Ad_D E_-=+i E_-.

The electromagnetic correction commutes with both triples and changes
neither conjugation equation. The old Wilson also commutes with them.

For the `(j,j)` module with `j=3/2`, take normalized highest vector
`v_top=|j,j>`. The surviving fibre Koszul cohomology has representatives

    degree 0: v_top,
    degree 1: e_+ tensor |-j,j>, e_- tensor |j,-j>,
    degree 2: e_+ wedge e_- tensor |-j,-j>.

The source line powers, after the compact spin factors are included, are

    S^-3,       S and S,       S^5.                    (1)

They agree with the old four-line formula at `j=k=3/2`. The middle
flat transport, rather than these powers alone, is the missing datum.

Let alpha be A's eigenvalue on `v_top` in a fixed complementary gauge
coefficient. It is a unit complex number. D has eigenvalue one there,
so B also has eigenvalue alpha. Lowering three times in one factor and
using `Ad_A E_+†=i E_-†` gives

    A|-j,j>=-i alpha |j,-j>,
    A|j,-j>=-i alpha |-j,j>.

Multiplication by the actual `i sigma_x` flavour action cancels the
factor -i on the middle representatives. D's gauge eigenvalues there
are -i and +i, canceled by its flavour eigenvalues +i and -i. Hence the
induced flat cohomology actions are

| Degree | A action | D action | B action |
|---|---|---|---|
| 0 | alpha | 1 | alpha |
| 1 | alpha sigma_x | I2 | alpha sigma_x |
| 2 | -alpha | 1 | -alpha |

The last minus is `i^6=-1` from the two lowering strings; the determinant
of the flavour action is one. This is a calculation on the actual
spinor cohomology, not its dimension alone.

All these flat peripheral actions are identity. On the actual line powers
in (1), the extending cusp spin sign is -1 and all powers are odd. Thus
the reduced lines remain antiperiodic, consistent with the all-slot
128-sector estimate. One must not replace their end by the old periodic
scalar/form end or a freely chosen compact boundary projector.

## 3. Why the retraction can be glued

The highest, two mixed-extreme and lowest subspaces above are invariant
under the **combined** gauge/flavour transitions. The middle subspaces
need not be separately fixed; their sum is invariant. A projection onto
the whole surviving subspace and its inclusion therefore intertwine A,
D and the old Wilson, with all degree factors included.

Start with the old bounded local chain homotopy

    delta h+h delta=I-i p.

Average h over the finite combined flat transition image. The bare lift
has finite order, as does its Wilson product; the corrected Q8 image is
also finite. The differential and ip intertwine this group, so the
averaged homotopy retains the same identity and is equivariant. This is
an auxiliary chain comparison, not an averaging of physical states or a
change of the mass operator.

Every non-extreme inverse in the source contraction is between identical
spin-weighted holomorphic lines after its S factor is retained. It is
bounded in the actual metrics. Finite averaging preserves boundedness,
holomorphicity and compact-support cores. Totalizing with Dolbeault gives
the same chain homotopy with the usual degree signs. It passes to the
complete differential graph domains by the source core approximation.

The reduced line complexes have the antiperiodic complete ends just
checked. Their finite-dimensional L2 cohomology can therefore be used in
the source mass-map Hodge identification. This step depends on the full
domain-preserving contraction, not just finite fibre cohomology; it is a
load-bearing review duty. Compact resolvent alone would not supply it.

## 4. Read the actual line counts

Write L_+ and L_- for the two degree-one flat lines, before the spin S.
If the Wilson in the coefficient is chi_R, their characters on a,b are

    L_+: (alpha chi_R(a), alpha chi_R(b)),
    L_-: (-alpha chi_R(a), -alpha chi_R(b)).            (2)

The degree-zero character is the first one, and the degree-two character
is the second one. Both have unitary compact extensions since their
peripheral transport is identity. Write `S=eta` on the compact elliptic
curve, eta a flat order-two spin line, and delta(L)=1 for a holomorphically
trivial degree-zero unitary line, zero otherwise.

The complete cusp norm supplies the old strict pole bounds. Explicitly,
in a compact puncture coordinate w, a pole of integer order n in S^a
has radial norm proportional to

    integral r^(a-1-2n) (log(1/r))^(a-2) dr.

It is integrable when `n<a/2`, or at equality when `a<1`. Consequently
the permitted divisor degrees at a=-3,1,5 are respectively -2,0,2.
On the compact elliptic curve, a negative-degree line has no section,
a degree-two line has two, and a degree-zero unitary line has a section
exactly when trivial. The equality endpoint is not rounded away.

The old physical Hodge map now yields

    dim ker M_R = 2 + delta(eta L_+) + delta(eta L_-),   (3)
    no 128-sector gauge/gaugino zero modes.             (4)

The term 2 is H1 of the negative-degree degree-zero-Koszul line, by
its actual trace-dual Hodge partner of divisor degree two. H0 of that
negative line and H1 of the degree-two final line vanish; this accounts
for the degree-zero and degree-three parts of the complete complex.
The two middle Dolbeault H0 terms are precisely the two deltas in (3).
Both conjugate gauge sectors remain independent left fields. Their
adjoint-kernel counts agree, recovering the earlier zero index without
inferring that either kernel is empty.

## 5. Bare and coherent corrected lifts differ in the core

For the bare lift `A^4=Zeta`, so on either spinor alpha obeys

    alpha^4=-1.

Neither line in (2), even after tensoring any order-two spin and the
old order-three Wilson, can be trivial: an order-eight character cannot
be canceled by characters of orders two and three. Independent Zeta
signs on a,b do not change that conclusion. Equation (3) gives two
zero modes per complementary gauge coefficient in the bare construction,
for every extending spin and all four bare central lift choices.

For the two specified coherent electromagnetic corrections, use

    A_tilde^2=K_pi,
    K_pi=exp[-i pi(H_+-H_-)/2].

On `v_top`, `H_+-H_-=0`; thus `alpha^2=1`. In the specified continuous
Pin2 map B_tilde=D A_tilde, so its highest-vector character is the same
alpha on both core generators. The two allowed corrections differ by
Zeta, exchanging alpha and -alpha and hence the unordered pair of lines.

If the physical spin is the registering quadratic form's proposed odd
class `eta=O`, the consequences are:

| Complementary U3 coefficient | Wilson | Bare lift | Specified coherent corrected lift |
|---|---|---:|---:|
| `3_(-1/3)` | nontrivial order-three chi | 2 | 2 |
| `1_(+1)` | trivial | 2 | 3 |
| conjugate triplet | chi^-1 | 2 | 2 |
| conjugate singlet | trivial | 2 | 3 |

The triplet's order-three character prevents either middle line from
becoming trivial. In the singlet exactly one of `(alpha,alpha)` and
`(-alpha,-alpha)` is trivial. Counting representation dimensions, this
is a candidate 128-sector kernel dimension 16 bare, 18 corrected, at
that spin. It is not a count of generations.

For a general extending spin the corrected singlet count is three when
`eta(a)=eta(b)` and two otherwise, in this marking. Arbitrary additional
independent central signs change that condition. They are not silently
eliminated: the stated two corrections are the continuous-Pin2 prescription,
not a theorem that every allowed free-group lift obeys it. Pulling back
the entire marked construction preserves the corresponding invariant
line-triviality statement, rather than retaining a,b signs by fiat.

## 6. Physical and foundational account

This candidate derivation removes an unspecified **kernel multiplicity
inside a supplied model**. It predicts a difference between core lifts
whose cusp transition, connected gauge group and index agree. The core
phase is therefore not disposable merely because those coarser diagnostics
do not see it. Agreement of an index does not establish full physical
equivalence.

Three singlet pairs are not three chiral SM generations. The triplet
multiplicity is different; the integer-root sector and its continuum are
still present; the actual weak-current vertices and masses are uncomputed
here. These charged zero modes themselves require a physical account in
any candidate intended to describe the observed massive charged spectrum.
This is a local statement about this classical background, not an exclusion
of other backgrounds, quantum effects, end laws or generated carriers.

The parent/action, physical flavour holonomy, complete metric/end, E8
embedding, Wilson, spin identification and compensation prescription
remain hypotheses. The registering-quadratic-form-to-odd-spin map is a
conditional geometric map, not yet an earned physical identification.
Coherent compensation likewise remains a named physical requirement.
No foundational input or SM parameter is certified paid.

Review next: derive the finite cohomology action from the full source
Spin10 matrices, check the averaged contraction in every degree and the
complete domains, verify the exact pole endpoint and all conjugate Wilson
characters, then calculate the same-action weak-current overlaps. No
favourable kernel submatrix or three-mode truncation can replace those
checks. A separate prospective source design precedes any implementation.
