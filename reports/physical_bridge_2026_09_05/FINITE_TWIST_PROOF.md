# R27 pre-execution proof: finite twists of geometric local systems

This is an application of published mathematics plus an explicit
transfer argument, not a new general vanishing theorem. The executable
controls and their results are separate. Date: 2026-09-12.

## 1. Exact statement and the index actually at issue

Let M be connected, orientable, complete, nonelementary and hyperbolic
of finite volume, and Q a compact core with its full torus boundary T.
Let h:pi1(M)->SL2(C) be a lift of the **complete geometric holonomy**.
For m>=1 and a finite-image representation F:pi1(M)->GL(r,C), put

    V = Sym^m(h) tensor F.
    n_Q(V) = dim im[H1(Q,T;V) -> H1(Q;V)]
           = dim ker[H1(Q;V) -> H1(T;V)].
    I_Q(V) = n_Q(V) - n_Q(V*).

Here H1 means cohomology in degree one, as in B1297; it is not homology.
The conclusion is **n_Q(V)=n_Q(V*)=0, hence I_Q(V)=0**. No symmetry of M,
cusp-triviality of F, connected character family, numerical rank,
Galois automorphism, isotropy of an identified image, or D reduction
I=t0-r1 is needed. In particular, finite-order scalar characters are
covered even at isolated, non-real points of the character group.

## 2. Published input, with its nontriviality qualification

Menal-Ferrer--Porti, [Theorem 0.1](https://ir.library.osaka-u.ac.jp/repo/ouka/all/23151/ojm49_03_741.pdf),
Osaka J. Math. 49 (2012), 741--769, gives injectivity of restriction
in degree one for every nontrivial complex symmetric power of a
geometric SL2 holonomy lift on a complete topologically finite
nonelementary hyperbolic three-manifold. The theorem also treats degree
two. Its proof uses the positive algebraic term in a Bochner identity,
then the relative/ordinary long exact sequence.

The arXiv v2 was personally read in full, including the positivity
proof in Lemma 2.14 and the compact-support argument. The published
Theorem 0.1 and its proof were compared directly. The printed Theorem
2.1/Corollary 2.2 omit the nontriviality qualification in their brief
statements; Theorem 0.1 and Lemma 2.14 explicitly require dimension at
least two. This argument uses the latter qualified statements.

## 3. Remove the finite twist, without altering the geometric coefficient

The kernel of F has finite index d in pi1(M), so it defines a connected
degree-d cover p:N->M. Equip N with the pulled-back complete hyperbolic
metric. Finite covers remain complete, finite-volume, topologically
finite and nonelementary. The subgroup restriction h|pi1(N) is a
genuine SL2 lift of N's complete geometric holonomy. This is the
load-bearing identification; it would fail for an arbitrary SL2(C)
representation unrelated to the complete geometry.

Let Q_N=p^(-1)(Q), T_N=p^(-1)(T). Restricting F to the subgroup kills
its monodromy, so p*V is r copies of Sym^m(h|pi1(N)). The primary
theorem applies to each copy, and restriction

    H1(Q_N;p*V) -> H1(T_N;p*V)

is injective. No cusp is discarded; T_N includes every lifted component.

## 4. The trace, explicitly with local coefficients

For an evenly covered open set U in Q, all fibres of p*V above a point
x are canonically the same fibre V_x. Sum a local coefficient-valued
form over the d inverse sheets using this identification. The sums
agree on overlaps since a transition only permutes sheets and applies
the same coefficient transition. They define tr on forms/cochains.
It commutes with the flat differential and with restriction to the
boundary, and on every form from Q it satisfies

    tr(p*alpha) = d alpha.

Consequently tr p*=d id on cohomology and p* is injective over C.
This statement does not require unitary coefficients: it is a finite
cover identity for a pulled-back local system. The inverse integer
1/d is essential; the same inference is unavailable when the
coefficient characteristic divides d.

If [alpha] is in the kernel of boundary restriction on Q, naturality
puts p*[alpha] in that kernel on Q_N. Injectivity there makes it zero.
Applying tr gives d[alpha]=0, hence [alpha]=0. This proves n_Q(V)=0.

The standard SL2 invariant pairing gives Sym^m(h)* isomorphic to
Sym^m(h). The finite-image dual F* is again finite-image, so the same
argument, separately, proves n_Q(V*)=0. This step uses global geometric
self-duality, not just a pairing on the cusp. No identification of V
with V* is asserted: the finite twist can make them nonisomorphic.

## 5. Direct sums, trivial blocks and the correct algebraic distinction

The conclusion holds term by term for finite direct sums of nontrivial
geometric symmetric powers tensored with finite-image factors.
If a trivial geometric block occurs, its finite-image coefficient U
has an invariant positive Hermitian form obtained by averaging over
its finite image. Thus U* is linearly isomorphic to its conjugate
local system. Complex conjugation gives anti-linear isomorphisms of
the relative, ordinary and boundary cochain complexes and intertwines
their maps. It follows that n_Q(U)=n_Q(U*) and I_Q(U)=0.

It does **not** follow that n_Q(U)=0. Thus all such finite sums have
zero I, but only the nontrivial geometric blocks have the stronger
zero-interior-cohomology conclusion. This argument also establishes
zero I for any finite-dimensional unitary local system; that elementary
conjugation fact is already recorded in B1297 and is not new here.

In the executable Bochner control, the monomial metric is
G_jj=1/binomial(m,j), E*=F, and Y=(-H,i(E-F),-(E+F)) is Hermitian.
For p=1, positivity of H=T*T+TT* follows for every m>=1 by its kernel
argument: T alpha=0 imposes Y_i alpha_j=Y_j alpha_i. In the component
formula for H, the commutator contribution then cancels by the sl2
relations. If H alpha=0, summing the remaining Hermitian squares forces
Y_i alpha_j=0 for every i,j. A nontrivial irreducible sl2 module has
no invariant vector, so alpha=0. Degree two is related by the Hodge
star. The finite-dimensional positive minimum is uniform over the
homogeneous bundle; the complete-manifold theorem supplies the
analytic consequence. For m=0, every Y_i vanishes and there is no
positive lower bound. The code checks explicit matrices for m<=6,
not the full analytic theorem or a physical mass gap.

## 6. What this verifies in the repo, and what it does not

It supplies a route to verify the zero I for the geometric Sym^m
finite-character sectors in B1297 and the later cover probes,
including the noncyclic and isolated order-three sectors not protected
by those particular Galois/isometry arguments. The finite-dimensional
index equals the specified relative-image difference by definition;
there is no step declaring it the normalizable spectrum of any chosen
four-dimensional physical theory. A finite-field non-geometric positive
is compatible with the theorem, not an embarrassing outlier to discard.

For an application to an induced bundle, the induction/Shapiro map
must also intertwine **all** boundary restrictions. It is not earned
by matching dimensions or by this transfer argument alone. For the
direct local-system sectors just stated, no induction is needed.

The theorem does not cover arbitrary non-geometric SL3/E6 flat
connections, nonunitary infinite-image extra twists, incomplete or
singular hyperbolic structures, or a different boundary condition.
The more general B1334 character-torus claim is not proved by this
finite-cover argument. There is no claim that a one-cusped character
variety is finite, or that a negative peripheral SL2 trace defeats an
odd symmetric power after every possible scalar twist.

Most importantly, R18/R19 use a unitary scalar line on a **punctured
source manifold**, a real singular mass term dH, prescribed source
strengths and the maximal weighted Hilbert complex. Their comparison
is with a different finite pair, and R26 retains exactly that domain.
The mass is neither removed by a finite coefficient cover nor a
uniformly regular compact perturbation of the smooth geometric system.
Therefore this proof neither contradicts their conditional three/zero
kernel nor establishes their physical vacuum, anomaly completion or
source selection. Those tasks remain the declared PB-BOUNDARY duties.
