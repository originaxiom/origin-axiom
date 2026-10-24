# Realizing the symmetric state: retain the actual matter data

October 24, 2026. Authored analytical scope audit, UNREVIEWED.
No producer, new scientific check or test collection was run. This is
outside the frozen P210 specification and changes none of its sources.

Scope: the earlier declared state action on (tau,S,M), the paper's
point-residue and diagonal channel-weight prescriptions, and the
particular retained SU6/E8 gauge embedding. Not all possible matter,
end laws, physical completions, or the entire generated architecture.

## 1. The sources already distinguish the coefficient from its parent

Personally read the complete retained-embedding, surface-parent,
surface-global-spin and field-map proofs; the common-register,
coupling-transport and normal/principal-parts proofs; the paper's
relevant fibre, point-rank, norm and joint-law sections; B1659's full
joint-law producer and B1656's source head through weighted_M/coupling.
None was executed. The next-obligation lists were read, not just headlines.

The existing retained embedding faithfully maps the quaternion doublet
to SU6 and the regular gauge factor to E8. The ordinary surface Weyl
control has an actual local block map for (6,3,2) and its dual, with
all companions retained. The supersymmetric canonical Spin-c block is
a different twist, with its own R connection. These are positives,
not proofs that the paper's matrices are that parent's fields or that
the curve and surface theories have the same exterior.

The paper explicitly states the fibre-frame scope and the owed parent
map. Its universal joint-law identity over M2(C) x M2(C) is broader
than its point-residue realization. That distinction matters at the
state used in the P210 fixed-state calculation.

## 2. What Q8-fixed means for the full matrix state

Use epsilon=[[0,1],[-1,0]], i=diag(i,-i), j=epsilon and k=i j.
The earlier state action is

    S'=alpha(e) g S g^-1, M'=beta(e) g M g^T.

For its declared character choices alpha and beta are trivial on the
natural inner lifts J_a,J_b. These act on the matrices with g=i,j.
No geometric normal/spin factors are silently added to this state chart.
Set N=M epsilon. Since g^T epsilon=epsilon g^-1,

    N'=beta(e) g N g^-1.                         (1)

Thus, at this chart's fully Q8-fixed state, both S and N commute with
i and j. A matrix commuting with diagonal i is diagonal; commuting
also with j makes its two diagonal entries equal. Necessarily

    S=s I2, N=n I2, M=n epsilon^-1.              (2)

Conversely these matrices are fixed by those two natural inner lifts.
This proves only their matrix-state stabilizer, not invariance under
all other registered moves or of an unconstructed physical vacuum.
For n nonzero, det M=n^2 and rank M=2. Therefore a nonzero rank-one
point residue cannot realize (2). S=I alone is NOT a fully symmetric
state if the matter matrix is still nontrivial under those lifts.

This preserves the existing formal test S=I,M=epsilon^-1 and its
actual contraction Y=-2I3. Those are valid inputs of the universal
polynomial law, not automatically attainable point-residue data.

## 3. The diagonal channel weights do not fill that particular gap

The point construction has M_raw=p q^T and four unit pairings

    R_s=ell_s(M_raw),
    ell_s(M)=sum_mn (epsilon C_s)_mn M_mn,
    (C_1,C_i,C_j,C_k)=(I2,i,j,k).

These four functionals are a basis of the matrix dual. B1656's
weighted_M reconstructs the unique M_weighted with

    ell_s(M_weighted)=u_s=w_s R_s.               (3)

The source canonical prescription has w_s=sqrt(2pi L+c_s) on each
nonzero channel. The following argument requires only finite nonzero
w_s there, not equal weights or any numerical norm value. A channel
with R_s=0 contributes zero without dividing by it.

The point residues obey the source's null-quaternion identity

    R_1^2+R_i^2+R_j^2+R_k^2=0.                 (4)

This can also be seen directly from sum_s ell_s(M)^2=4 det M
and rank M_raw=1. No approximation or fitting argument is needed.

At the candidate (2), direct entrywise contraction gives

    ell_1(n epsilon^-1)=-2n,
    ell_i=ell_j=ell_k=0.                        (5)

Equations (3),(5) and nonzero weights require R_i=R_j=R_k=0.
Then (4) requires R_1=0, so (3),(5) give n=0. Consequently this
finite, nondegenerate diagonal weighting cannot produce a NONZERO
matrix-state (2) from the paper's null point-residue data either.

It certainly can produce full-rank matrices away from that state;
the established normalization-induced determinant defect remains
valid. Full rank is not the same condition as full Q8 invariance.
This argument neither refutes B1656/B1659 nor their later numerical
fits. It tests this one proposed matrix-state against their stated
realization rather than treating every formal M2 input as attained.

Non-diagonal profile mixing, sums of independent residues, two-point
data, different coefficient lines, or another end prescription change
the hypotheses. Vanishing weights on nonzero channels would be a
degenerate prescription, not an admissible positive-norm counterexample.
Singular limiting sequences require their own norm/domain analysis.
None of those alternatives is excluded by (3)--(5).

There is a quantitative control, not just an unattained equality. The
four matrices dual to ell_s are Hilbert-Schmidt orthogonal with squared
norm 1/2. Write C=span(epsilon^-1). Then

    ||M_weighted||_HS^2=(1/2) sum_s |u_s|^2,
    dist_HS(M_weighted,C)^2=(1/2) sum_(s=i,j,k) |u_s|^2.

If u_1 is nonzero, let eta be the least |w_s|/|w_1| among nonzero
imaginary residue channels. Equation (4) implies
sum_(s=i,j,k)|R_s|^2 >= |R_1|^2. Therefore

    dist_HS(M_weighted,C)/||M_weighted||_HS
          >= eta/sqrt(1+eta^2).                 (5a)

If u_1=0 the distance ratio is one. In particular, for fixed tau,
fixed flat line and finite channel constants, the canonical weights
sqrt(2pi L+c_s) have eta->1 as L->infinity: the lower bound tends
to 1/sqrt(2), not zero. Increasing that cutoff alone does not approach
the nonzero fully invariant matrix direction in relative norm.
This is a channel-matrix metric statement, not a bound on a physical
fermion mass, an infinite-dimensional domain or every cusp limit.

The bound's hypothesis and sharpness have an algebraic control:
R=(1,i,0,0), w=(1,delta,1,1), delta>0, give u=(1,i delta,0,0)
and distance ratio delta/sqrt(1+delta^2), saturating (5a). Letting
delta->0 approaches C only as the weighting loses uniform
nondegeneracy. This is not the fixed-tau canonical L->infinity limit
above; the two limiting prescriptions must not be confused.

The actual ramification point, spin line and root-normal derivative
also belong to the full geometric state. Their registered transport
was derived in REGISTERED_PRINCIPAL_PARTS_AND_GREEN_TRANSPORT.md.
If they change the state action, redo the stabilizer with those maps;
do not apply (2) or the old rank restriction to an altered action.
Fibre holonomy, natural based lifts and epsilon=(id,-1) are distinct
operations, not interchangeable central-sign names.

## 4. A matter-dependent trace plane survives S=I

There is a positive counterpart, using data already present rather
than inventing a replacement physical mass. On nonzero rank-one M,

    P_M=M M^dagger/tr(M M^dagger)                (6)

is a rank-one orthogonal projector onto image M. For unitary g and
any nonzero scalar beta, congruence transport gives

    P_(beta g M g^T)=g P_M g^dagger.

Hence Lambda_+=C3 tensor image M is a covariant rank-three coefficient
plane under the earlier common action, including its family-axis
permutation. It is defined when S=I and depends on the matter that
the S-only candidate ignored. The full state then does not satisfy
the Q8-fixed hypothesis of (2); no even-rank theorem is contradicted.

For the actual common-profile residue M=p q^T, image M=span p.
When p is the already retained puncture trace n_y, this is precisely
the earlier solution-trace plane U=C3 tensor span(n_y). That existing
finite-distance case has kernels (3,3) and conditional index zero,
not (3,0). It is a recovery, NOT a new physical boundary selector or
proof that matter dynamically chooses Lambda. The complete-cusp
operator is not changed into that finite-distance one by (6).

For more general M, the earlier H2 construction can be applied to N:
H2(N)=N N^dagger-tr(N N^dagger)I2/2. Its positive projector exists
where H2(N) is nonzero, independently of H2(S). It need not cover
all states and is not the full physical Hessian. A covariance witness
must not be promoted to a stationary action or an actual radial mass.

## 5. What the faithful gauge embedding does and does not identify

The retained embedding naturally supplies the traceless map

    S0=S-(tr S/2)I2 -> I3 tensor S0 in sl6,

conjugated by the existing fixed parity-frame isometry when needed.
It preserves the sl2 bracket. The underlying GROUP embedding retains
-I2 as -I6 on the defining six; conjugation on S0 remains centre-even.
But the scalar part of S maps to a multiple of I6 in the associative
matrix action, not an sl6 Lie-algebra element. A physical adjoint
assignment for that scalar requires an additional named component
in the full centralizer or another field interpretation; setting it
to zero would lose data. Existence of such components is not a
canonical choice of one, and the full E8 field content is retained.

There is also the already-earned weak-centre test. In this particular
embedding, the gauge puncture p=-I6 equals the old weak SU2 centre
as an E8 element. End(C2) under CONJUGATION is p-even, while a weak
doublet is p-odd. A bare gauge-equivariant linear map from this End
module into an odd weak-doublet block is therefore zero: its central
intertwining equation is X=-X. The paper already calls its embedded
traceless Higgs a flavon/SM singlet; this is not a new exclusion of
its fibre coupling or of every possible Higgs embedding.

An additional gauge-odd factor or a different embedding can change
the module. A geometric/R scalar factor changes total transport,
but does not by itself change a field's charge under the fixed WEAK
GAUGE centre. Any proposed repair needs the whole field/bundle map,
not cancellation of signs belonging to different groups by notation.

## 6. Consequence for the next derivation

P210's formal Q8-fixed boundary classification remains a conditional
result. Before assigning its index to the paper's actual matter or to
the physical parent, specify which state space is realized. On raw
point data, and on the stated finite nonzero diagonal weights, the
nonzero fixed matrix used as a control is outside that realization.
On raw point data the matter-dependent trace plane remains available
at S=I. Neither observation supplies physical chirality.

The next joint duty is a map from the retained sections/profile/norm
data to the SAME parent's full fields, kinetic metric, interaction,
asymptotic response and domain. The previous graded-cusp response
provides an example of a response derived AFTER a parent/background
is given; it is not identified with the paper's model by this note.

No independent physical input is counted as removed. The operator
dictionary and realization constraints are now more explicit, so we
can test a genuine join without importing a desired index or excluding
a state sector by a stabilizer it does not possess.

Verification remains owed: separate exact controls for (1)--(6),
zero/nonnull and weighted rank-one/full-rank comparisons, correct
conjugation versus congruence, the no-deleted-channel condition and
the actual normal/spin maps, as well as the dual-basis norm, sharp
distance control and nonuniform-weight limit in (5a). No existing mathematical test was run
or retroactively extended to certify this new argument. Source searches
were targeted, not a complete historical absence proof; the broad
already-banked terms returned many old hits, not a novelty certificate.
