# Coherent transport of the existing parity bundles

2026-10-11. Follow-up to the sealed `word_lifts/` packet. Object: the existing quaternion common-point local systems on F(a,b), their first cohomology, and B1606's local puncture solution representation. Generality: all inner base-point changes by proof, with exact tests on the four fixed positive elementary pairs. No physical parameter, gauge representation selection, spacetime action or full analytic boundary-value problem is computed.

## Question and conventions

Does the explicit simultaneous conjugacy of the positive word pairs transport the existing matter and puncture data without changing their grading or selecting new end data? These are two different six-dimensional spaces and must be tested separately.

Take rho(a)=i=diag(I,-I), rho(b)=j=[[0,1],[-1,0]], k=ij. For p=(1,0),(0,1),(1,1), set rho_p=chi_p rho. On cohomology use the pullback C(f,g)[z]=[g^-1 z composed with f], where rho(f(x))=g rho(x) g^-1. The chosen generator lifts are gL=(1+i)/sqrt(2), gR=(1-j)/sqrt(2). Composition of these cohomology maps is reversed. No helper may silently select the first of two lifts.

For h=J_q, U=rho(q), use the transported move f'=h f h^-1 and lift g'=U g U^-1. On cohomology the predicted transport is D_q=diag(chi_p(q) I2). On B1606's puncture space, where u_p=(j,i,k), it is E_q=diag(u_p^-1 U u_p). The two transports must not be identified.

## Sealed tests

1. Reconstruct cohomology in an exact chart z(a)=0. Verify its quotient projection on coboundaries and against a second chart z(b)=0; verify cocycle and inverse rules independently of a numerical rank tolerance.
2. Reconstruct the original lifts, verify their intertwining on a and b, the parity twists, and peripheral holonomy -I. Test both signs of each generator lift.
3. Compute C(J_q,rho(q))=D_q directly for q=1,b,A,Ab and additional signed-word controls. For each positive pair, compute C(f',g') directly and compare with D_q^-1 C(f,g) D_q, not only a matrix assigned by conjugation.
4. Reconstruct the central cohomology operator from Delta=L R^-1 L and its squared move product. It must have square -I and projectors of rank three at eigenvalues +i and -i. Transport those projectors, preserving their rank and each parity projector. This checks the existing algebraic triplet split, not the independent Hodge-theoretic identification of either triplet as physical left-handed matter.
5. Reconstruct B1606's local six-dimensional matrices directly from u_p, g and parity permutations. Verify their exact commutant dimension 2 without grading and 1 with grading. For all four pairs, verify the independent reconstruction equals E_q M E_q^-1, that E_q is unitary and block diagonal, and that the grading projectors are unchanged. Irreducibility with grading then leaves only the two extreme invariant subspaces, transported to themselves.
6. Control the central lift sign: rho(c)=-I for c=aBAb; C(J_c,-I)=I and C(J_c,+I)=-I. Thus a word automorphism alone does not determine its cohomology lift. Check that coherent transport preserves, rather than erases, this distinction.
7. Uniform Laurent pole order is preserved by an invertible constant transport. Use a nonzero leading coefficient at orders -2,-1,0,1,2 as finite controls; the general statement is proved without sampling. No preferred integer order is inferred.

The formulas and predictions were worked out before this seal, not blind. A failure is preserved and any revision is post-seal. PASS certifies only the specified finite identities plus the separately written analytic implications. It does not prove an unconstructed physical Dirac domain, the W45/W46 index theorem, or Λ.

## Seen first and load-bearing inputs

Pinned main `6c148ddd495d133213140995976ff08849793d5d`; pinned SM branch `6877cc87d31941a85f139e2f25e5e13694e22ce6`. The preceding all-retained-ref topic sweep on `Sturmian|Nielsen|inner automorphism|braid|word.*lift|positive.*lift` found 33 of 1408 main arcs (PROVED 28, NEGATIVE 4, OPEN 1), 18 retained lanes. A focused current-main full-FINDINGS search additionally used `base.point.*transport|inner automorphism|parity grading|puncture condition`, with quoted Git pathspecs so the older local checkout cannot restrict the search. No absence or novelty claim is made.

Read B1606 FINDINGS, its dependency addendum and its full `puncture_condition.py`; B1617's cohomology helper and B1632's index producer; the SM W10 `the_chiral_triplet.py` through the group-construction code, `the_spin_room.py` through its cohomology and Fox routines, W21's pairing and controls, and the full W46 rule. None of their numerical outputs is imported as a certificate. The elementary word helper from the preceding packet is the only imported project code, pinned in the hash manifest.

Literature search: naturality of group cohomology under inner automorphisms. Sharifi's *Group and Galois Cohomology*, chapter 1, definitions 1.2.1–1.2.5, read at https://www.math.ucla.edu/~sharifi/notes/groupcoh-ch01.html (2026-10-11). These supply background definitions; the degree-one formulas used here are derived explicitly. No unread theorem supports a verdict.

Seal PREREGISTRATION.md, PROOF.md and verify.py and the imported word helper before first execution. Run with Python 3.12, SymPy 1.14 and bytecode disabled, preserve the first transcript, and recheck hashes. No canonical GENESIS or shared registry changes before normal adoption.
