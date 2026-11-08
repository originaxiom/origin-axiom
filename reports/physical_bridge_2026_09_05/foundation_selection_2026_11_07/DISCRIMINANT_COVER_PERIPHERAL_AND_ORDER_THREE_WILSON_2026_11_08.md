# The actual discriminant cover, its triplet and its unchanged order-three twist

2026-11-08. **Author hand derivation and targeted source audit, UNREVIEWED.**
No scientific imports, collection, CAS, numerical calculation or code
execution. Scope: the existing affine quaternion register and AGY's
Wall 2 / three-sheet comparison at exact head
56e4eac8a6b1831919dfebfd628362adcacbc05d. This is not a verdict on every
other claim at that head or a no-go for the full generated architecture.

## 1. Reuse the actual register instead of a cover chosen by its name

The [affine D4 proof](AFFINE_DOUBLET_KERNEL_D4_AND_PARITY_2026_11_08.md)
already supplies F=F(a,b), rho(a)=A, rho(b)=B in Q8, N=ker rho and

    P_(uv)=P_u+rho(u)P_v, P_a=0, P_b=I,
    P(N)=L=D4={z in Z^4: sum z_i even}.

On N this is an additive homomorphism. The old normal generators obey

    P_(a^4)=0,
    P_(a^2 b^-2)=-(I+B),
    P_(b^-1 a b a)=B+C, C=AB.

The [whole first-order register proof](JOINT_FIRST_ORDER_REGISTER_AND_OLD_QUATERNION_COVER_2026_11_08.md)
already identifies N as a free group of rank nine. Its degree-eight
quaternion surface cover has compact genus three and four punctures.
Those are credited prior results, not newly inferred matter counts.

AGY's Wall 2 function constructs a useful lattice extension and four
characters. Its description calls the latter N/2N, N/(2L_D4), and later
a three-sheeted D4 cover. These are different objects. Specify the
subgroup and actual spatial holonomy before transporting a physical
operator.

## 2. A correct four-character quotient exists, but is not L/2L

For the Euclidean D4 lattice,

    L*=Z^4 union (Z+1/2)^4,
    2L*=2Z^4 union (2Z+1)^4,                         (1)

and 2L* is contained in L. To verify the first formula, pairing with
every e_i-e_j makes all dual coordinates equal modulo Z, and pairing
with e_i+e_j makes twice that common fractional part integral. Conversely
integer coordinates or all half-integer coordinates pair integrally
with every even-sum integer vector. Scaling gives the second formula.

Reduction modulo two sends L to the eight even-parity vectors in F2^4.
The subgroup 2L* identifies the zero vector and (1,1,1,1). Hence

    A_disc=L/(2L*) is (Z/2)^2, of order four.          (2)

Its dual character labels are (1/2 L)/L*, represented by the zero
vector and the three half-pair vectors used by AGY. By contrast L/2L
has order sixteen because L has rank four. If N/2N means mod-two
ABELIANIZATION of the actual free N, it has order 2^9; doubling is
not itself a definition of a subgroup quotient for a nonabelian N.

Define the actual subgroup

    K=P|_N^-1(2L*).                                  (3)

Surjectivity P(N)=L gives [N:K]=4 and [F:K]=32. Q8 left multiplication
is a signed coordinate permutation preserving both L and L*, so K is
normal in F. No splitting of the resulting order-32 quotient is assumed.
Thus there is an actual regular four-sheet cover of the quaternion
cover, not a three-sheet cover obtained merely by omitting a character.
This quotient retains a specified part of the register; it is not the
whole first-order register or an argument that physical registration
must factor through it.

## 3. The spatial cusp is invisible to these discriminant characters

Let c=[a,b]=a b a^-1 b^-1 be the original puncture loop. The supplied
quaternion algebra and cocycle law give

    rho(c)=-I,
    P_c=I+A,
    P_(c^2)=P_c+rho(c)P_c=0.                         (4)

For example P_(b^-1)=B, rho(a b a^-1)=-B, so the final inverse-b
contribution to P_c is (-B)B=I; the earlier b contribution is A.
This proves (4) with the existing based/inverse convention.

The quaternion cover's puncture loops are conjugates of c^2. Since
rho(c^2)=I and P_(c^2)=0, the conjugation law also gives

    P_(h c^2 h^-1)=0.

Consequently ALL FOUR A_disc characters are trivial on EVERY spatial
cusp loop of that cover. Any common extending-spin or other pulled-back
peripheral sign multiplies every character in the same way. It does not
single out the trivial character for deletion while preserving the other
three by this discriminant twist alone.

The three Q8 PRESENTATION relators r2,r3,r2 r3 used in AGY's sign table
are not these spatial cusp loops. They are core words in N with nonzero
P values. Requiring nontrivial character on at least one of those words
does select the three nontrivial characters algebraically. Calling that
criterion an antiperiodic cusp condition requires an additional actual
boundary/defect/field map; it is not supplied by the sign table itself.

Because the cusp monodromy in (2) is trivial, (3) extends unbranched over
the four compactified punctures of the quaternion cover. Its compact
genus is 1+4(3-1)=9 and it has sixteen punctures. Equivalently
2-2*9-16=-32, matching the degree-32 cover of the original once-punctured
torus. This conditional cover is a valid possible carrier. Its changed
geometry and full operator/domain must be transported, not replaced by
the old surface with three identical copies.

## 4. Preserve the triplet positive with the correct full action

The regular representation of A_disc has four character lines. Its
canonical invariant subspace is the trivial line; the orthogonal
augmentation subspace W has the other three character lines. Splitting
1 plus W is a mathematical construction. Selecting W as the physical
field content is a further duty, not a consequence of the splitting.

On W, the two pure triality permutations in AGY's source are transpositions
of three coordinates. They generate S3. Under this PURE permutation
action, (1,1,1) spans an invariant line and the sum-zero plane is invariant:

    W|_S3 = 1 plus 2.                                (5)

Its commutant is a I+b J, not only scalar matrices. It cannot be an
irreducible three-dimensional S3 representation with Burnside span rank
nine. AGY's source docstring itself gives the character norm two,
consistent with (5), while the relay's 'irreducible S3 triplet' wording
must be corrected. A three-dimensional reducible family is not thereby
physically impossible; irreducibility and generation number are distinct.

There IS a positive repair. Retain the ACTUAL deck translations as well
as triality permutations. In AGY's ordered nontrivial-character basis,
the two generator translations act by

    D2=diag(-1,+1,-1), D3=diag(+1,-1,-1).             (6)

They distinguish all three character lines. A complex subspace invariant
under both unitary deck matrices splits into a subset of those lines;
invariance under the transitive S3 permutations then forces it to be
zero or all of W. Thus W is irreducible for the COMBINED
A_disc semidirect S3 action, the order-24 signed permutation group.
The same argument forces every constant Hermitian form invariant under
that full action to be one positive scalar times I.

This uses the deck action and is not the same theorem as irreducibility
under S3 alone. It is consistent with the old deck-plus-move norm
arguments. It does not identify this module with the paper's native
triplet without exhibiting its full lifted action, phases and central
character. Nor does it identify a constant coefficient metric with an
integrated profile metric at an arbitrary physical vacuum.

For an actual covariant operator family D_x, moves can take x to gx:
D_(gx) U_g=U_g D_x, including domains and norms. Only the stabilizer of
the COMPLETE state acts on one fixed D_x. Full family covariance alone
therefore does not force all three spectra/kinetic weights to coincide at
that state. This is the earlier fixed-state/family distinction applied
to this specific cover, not a new assumption of an invariant vacuum.

## 5. An order-three Wilson character survives the actual cover

Here is a general exact control. Let chi:G->C_m be a surjective finite
cyclic character and H a finite-index subgroup. The preimage of chi(H)
contains H, so [C_m:chi(H)] divides [G:H]. It also divides m. If
gcd([G:H],m)=1, both divisibilities force chi(H)=C_m. Thus a nontrivial
order-m character cannot be killed by pullback to a coprime-degree cover.

For the old nontrivial order-three Wilson on F and K in (3), the degree
is 32, coprime to three. Its pullback to K is still nontrivial. The
intermediate quaternion degree eight and discriminant degree four cannot
remove it either. A two-torsion character cannot cancel a genuinely
order-three character, since equality would force its order to divide
both two and three.

The current AGY three-sheet comparison instead changes

    chi3 * alpha * sigma_x
       to I3 tensor (alpha * sigma_x),               (7)

without the old chi3 factor. This is visible in the actual producer,
not inferred from the output label. Under the same finite comparator
alpha=1, retaining chi3 would give eigenvalues +chi3 and -chi3 in each
block, neither equal to one for nontrivial order three. Its middle-line
fixed columns would remain absent, whereas deleting chi3 gives one
per supplied copy. That difference is a change of coefficient system,
not pullback of the old Wilson bundle along (3).

The full geometric cover has new genus, norms and domains. It may have
additional cohomology for other reasons; the character argument does
not exclude those modes or every possible SM3 construction. It DOES
show why the displayed replacement and its three fixed columns do not
derive the desired family spectrum from the old bundle.

An unchanged genuine direct-sum operator I3 tensor D, with corresponding
domains, has kernel C3 tensor ker D. It triples EVERY retained kernel
component, including the old extreme lines, rather than establish one
family mode per character or eliminate unwanted partners. Comparing a
full old roster with only a new middle-line count is not like-for-like.

## 6. What next could actually earn the family map

The correct construction provides a concrete four-sheet cover, its
rank-three augmentation module and a faithful combined deck/triality
action. These are useful conditional positives. The unearned physical
duties are now more exact:

1. Explain why the registering dynamics selects the augmentation sector
   or removes its singlet, using an actual field/gauge/source equation.
2. Pull back the complete physical fields, old Wilson, metric, spin,
   action and domains to K, or explicitly define and price a different
   carrier/representation. Do not delete an order-three character by
   choosing an order-two character basis.
3. Exhibit the lifted register action on that operator and its stationary
   backgrounds; compare it with the native triplet including all phases.
4. Compute the full spectrum and weak current on that SAME construction,
   retaining extreme lines, conjugates, charged sectors and continua.

The gauge-sector response and quartic work supports the boundary/action
part of this task; it does not yet supply these family identifications.
No new foundational input, physical generation count or empirical
parameter is certified as derived by this note. Independent proof/code
review and any separately sealed controls remain owed.
