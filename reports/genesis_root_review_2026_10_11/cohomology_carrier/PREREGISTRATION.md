# Carrier information required by the existing cocycles

2026-10-11. Author: originaxiom. Branch-local dependency audit.

## Scope and question

Which part of faithful F2 is needed by the record's existing degree-one coefficient cohomology? Fix F=F(a,b), derived series F^(0)=F and F^(n+1)=[F^(n),F^(n)], and G_d=F/F^(d). Compare the sign-character modules and the quaternion doublet modules already used by the weave. This is a grammar-level, all-word statement, not a selected-thread calculation. It assumes these coefficient choices, not their physical necessity.

The target is two-sided: the Q8 representation should survive G_2, but its doublet H1 should vanish there; G_3 should retain the full F2 doublet H1 and its lifted automorphism action. Thus a specified downstream construction can reject one weaker carrier without requiring the whole free group. No claim identifies G_2 with the earlier affine path image; that identification is unnecessary.

Conventions: [u,v]=uv u^-1 v^-1, uppercase letters mean inverses, cocycles satisfy z(gh)=z(g)+rho(g)z(h), coboundaries are (rho(g)-I)v. Use rho(a)=diag(i,-i), rho(b)=[[0,1],[-1,0]], and all four parity twists, with the three nonzero parities forming the record's six-dimensional sum. The comparison is ordinary group H1 in the specified module, not adjoint deformation theory, a Hodge realization, a Fredholm index or physical chirality.

## Prior and two outcomes

The prior is that both the vanishing and retention statements hold. PASS requires the elementary all-word proofs in PROOF.md and every exact safeguard. A finite pass cannot prove all derived-series relations. Any failure is retained unchanged and stops the proposed conclusion pending diagnosis. No external theorem is load-bearing: cocycle descent is proved with an explicit affine homomorphism; the quotient properties follow directly from the definition of the derived series.

## Fixed checks before first execution

1. Quaternion matrices have squares -I, anticommute, and have commutator -I for all four twists. Cocycles have a two-dimensional coboundary space and two-dimensional quotient on F2. Each nontrivial sign character has one-dimensional H1 on F2.
2. Let c=[a,b], r=[c,a c a^-1], t=[r,a r a^-1]. Both r and t are freely nontrivial, verified by two free-reduction procedures. They lie in F'' and F''' respectively by their written commutator construction. In the normalized chart z(a)=0, require z(r)=4 z(b) for every quaternion twist. Hence the relation r=1 kills the complete doublet H1, not just selected vectors. Require z(t)=0 for every generator assignment.
3. Check the direct cocycle evaluator against a separate block-affine matrix product on 17 reduced words through length two and on r,t, for all four quaternion twists. On 161 reduced words through length four, test the cocycle law against each generator and inverses.
4. Generate a fixed family r_uv=[[u,v], a[u,v]a^-1] for u,v drawn from (a,b,ab,aB), omitting freely trivial words. Their next commutators with a- and b-conjugates supply F''' fixtures. Every such F''' fixture must have identity quaternion image and zero full cocycle derivative. Sign-character cocycles must already kill the F'' fixtures; quaternion cocycles must detect at least one of them.
5. Reconstruct the existing L,R cohomology matrices with the earlier sealed helpers. Verify the lifted intertwining, cocycle-chart consistency, noncommutation, and the central splitting into two rank-three eigenspaces. The proof, not a different normal-form implementation, establishes that these same matrices act on H1(G_3,V). Multiplication by F''' fixture t must leave quaternion cocycle data unchanged in every position of the fixed short-word controls; replacing it by r must fail for a nonzero normalized doublet cocycle.

The restricted sum of three sign-character H1 spaces and the sum of three quaternion doublet H1 spaces are different modules. No dimension match is used to identify them. Retaining the algebraic six and its central split does not transport a surface metric, cup pairing, holomorphic interpretation, end condition or spacetime action.

Hash and commit all scientific sources and their imported dependencies before execution. Preserve the first run and its exit status. Independent analytic review and full repository publication certification remain pending; canonical GENESIS and banked arcs remain unchanged.
