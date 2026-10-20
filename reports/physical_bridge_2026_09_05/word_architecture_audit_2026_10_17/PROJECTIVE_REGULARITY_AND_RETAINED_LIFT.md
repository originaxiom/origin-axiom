# Projective regularity and the retained unitary lift

October 20, 2026. Authored conditional analytical argument, awaiting
independent review. No scientific code was imported, collected or run.
This successor is outside the frozen root/trace verification proposal.

For the specified rank-six punctured elliptic coefficient, requiring
the EXISTING projective connection to extend holomorphically through
the puncture selects the two extreme extension lattices. Their ordinary
sheaf indices are -3 and +3. This supplies a concrete candidate end
condition to derive, not a derivation of that condition or of physical
generations. It differs from requiring a smooth traceless completion.

## The fixed coefficient and the extension being tested

Retain the [actual puncture problem](ACTUAL_PUNCTURE_CONNECTING_MAP_AND_TRACE.md)
and [determinant calculation](SMOOTH_COMPLETION_DETERMINANT_AND_END_PRICE.md).
Here W=C3 tensor rho on X=E-p, E is elliptic, and rho has quaternion
holonomy. For Lambda in C6, d=dim Lambda, the compact extension has

    local frame z^(-1/2)e on Lambda, z^(1/2)e on Lambda_perp,
    R_Lambda=(1/2)I6-P_Lambda,
    det E_Lambda=O_E((d-3)p),  chi(E_Lambda)=d-3.

The ordinary odd spin line is the earlier degree-zero one. The index
is not transplanted to the complete-cusp ordinary-spin operator.
The local logarithmic connection above is the ORIGINAL flat connection
written in this extension, not a newly chosen connection on its bundle.

This is an audit of all seven ranks in this specified local extension
problem. It neither exhausts generated carriers nor excludes other ends,
twists, sources, interacting backgrounds or full charged complements.

## Projective regularity selects only the extremes

Pass from GL6 to PGL6 at the level of the connection. Its residue is
the class of R_Lambda modulo scalar matrices, represented by

    R_Lambda^0=R_Lambda-(tr R_Lambda/6)I6
              =(d/6)I6-P_Lambda.                         (1)

In a holomorphic frame extending over p, a logarithmic connection is
regular precisely when its residue vanishes. A holomorphic invertible
frame change conjugates the residue; its derivative has no pole. Thus
the induced projective connection is regular in P(E_Lambda) precisely
when (1) is zero. The projector has eigenvalues zero and one, so

    R_Lambda^0=0 iff d=0 or d=6.                          (2)

For those two ranks the local connection matrix is scalar, so its
projective connection actually has no pole. On the punctured curve
it was already flat. This proves sufficiency as well as necessity for
this given connection and these extensions.

For every intermediate rank, projective peripheral HOLONOMY is still
identity: exp(-2 pi i R_Lambda)=-I6. Identity holonomy therefore does
not imply regularity in the chosen projective extension. For example,
at d=3 the residue has three eigenvalues +1/2 and three -1/2. Its
trace vanishes but its projective residue does not. Removing its pole
by a singular meromorphic frame change changes the extension; it is
not a regular gauge transformation of the same completion.

Equivalently the scalar projective monodromy does extend to a flat
projective bundle over E, but identifying that extension with a specified
P(E_Lambda), with the connection retained, is an additional requirement.
Neither a bare smooth cap nor peripheral holonomy imposes it.

## The projective data do not fix the unitary lift

The two extreme bundles satisfy E6=E0 tensor O_E(p). Consequently
P(E6) and P(E0) are naturally isomorphic, and their induced projective
connections agree: tensoring by this line changes only a scalar
connection term. They nevertheless have different determinants and
opposite ordinary sheaf indices. Projective data alone cannot pick
between them.

More generally a scalar logarithmic residue lambda I6 with peripheral
monodromy -I6 has lambda=1/2-q for integer q. Its local extension is
E0 tensor O_E(qp). The determinant section calculation gives

    degree=-6 lambda=-3+6q.                              (3)

Thus this family of scalar lifts retains degree 3 modulo 6, not a
preferred integer or sign. The two extremes are q=0,1. Restricting to
the original one-step modification leaves exactly those choices;
allowing further scalar modifications retains every q. Selecting a
minimum magnitude, a sign or a flux sector needs a stated reason.

This is also why (2) does not contradict the earlier traceless smooth
completion constraint d=3. That constraint changes the connection in
the cap while retaining its SU6 determinant. Equation (2) instead
retains the original projective connection through the puncture and
allows a scalar logarithmic singularity in its vector lift. They are
different completion conditions. No rank simultaneously satisfies both
conditions within these E_Lambda without changing the hypotheses.

## Three copies are not forced by the commutator alone

The primitive unitary relation AB=-BA does force an irreducible block
to have dimension two, but not a total rank of six. Here is a direct
argument, independent of a numerical rank calculation. In an irreducible
finite-dimensional unitary representation, A^2 and B^2 commute with
both A and B and hence are nonzero scalars. If Av=alpha v, the space
spanned by v and Bv is invariant under A and B; the two vectors have
distinct eigenvalues alpha and -alpha. Irreducibility makes this the
whole representation. Complete reducibility then gives arbitrary sums
of such doublets. The specified rank six supplies three blocks, not a
new derivation of that rank from the commutator.

For the retained quaternion representation the copies are already
identified in the source. Their family interaction and registering
action contain further information that must not be replaced by this
dimension statement. Likewise the source's faithful SL6-to-E8 embedding
acts nontrivially on its defining charged sector at -I6. Projectivizing
this six-dimensional sector does not make that action trivial throughout
E8 or justify deleting its charged fields or compensating lift factors.

## Literature check and remaining derivation

Nitin Nitsure's [The Narasimhan Seshadri Theorem revisited](https://arxiv.org/html/2509.24617v1)
was inspected in its relevant sections 2.1, 3.1-3.5, 4.6-4.7 and 8,
including the proof of Lemma 8.1. The scalar-residue construction in
3.5 requires specifying the residue, not merely its exponential.
Section 3.4 exhibits the failure of extension uniqueness with integer
eigenvalue differences. The unitary irreducibility criterion in 8.1
agrees with the doublet argument above. These are external mathematical
comparators, not physical selection principles.

The rendered v1 text of Lemma 4.7 omits a trace in its rank-general
statement and ends its proof with a sign inconsistent with the preceding
scalar-residue conventions. No sign is inferred from that ending here:
the determinant-section proof in the earlier note fixes (3), consistently
with this paper's sections 1, 6 and 7.10. A source citation is not a
substitute for checking its convention and formula.

The targeted repository search located the existing parabolic degree,
extension, companion and faithful-embedding proofs. No novelty or
repository-wide absence claim follows. The useful question is now
precise: does the SAME admitted action require regularity of this
projective connection, or permit its change by an end response? If it
requires regularity, what retains and selects the vector/spin lift and
accounts for its determinant and all companion fields? An arbitrary
preference for the +3 result would reintroduce the choice being audited.

This note pays no complete physical-input row. The finite-distance
Fredholm application, physical parent, stationary joining law, full
charged spectrum and independent review retain their previous duties.
The frozen eighteen tests do not verify this new argument; a separately
sealed successor would be needed before new scientific execution.
