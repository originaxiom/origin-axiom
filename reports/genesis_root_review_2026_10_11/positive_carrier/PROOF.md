# Positive word fidelity does not force a free group

2026-10-11. Author: originaxiom. Elementary proof for review.

A proper quotient of F(a,b) can retain every positive word, their order, a nontrivial commutator and all substitution endomorphisms. Therefore none of those requirements, jointly, forces injectivity on all signed words. This distinguishes two meanings of faithful description without rejecting the use of F2 or its conditional surface realization.

## The affine path quotient

Let R=Z[X^±1,Y^±1]. Pairs (m,u), with m=X^rY^s and u a column in R², multiply by

    (m,u)(n,v) = (mn, u + m v).

Associativity follows by expanding both triple products to (mnp,u+mv+mnw). The identity is (1,0) and the inverse is (m^-1,-m^-1u). Set

    A = (X,(1,0)), B = (Y,(0,1)).

Evaluation gives a homomorphism E:F(a,b)→G=<A,B>. The monomial is the signed letter-count vector. The two Laurent polynomials record the oriented horizontal and vertical edges traversed by the lattice path starting at (0,0). A backward step subtracts the corresponding forward-oriented edge at its lower endpoint. This is a second direct way to compute E.

## Every positive word can be recovered

A positive word of length n traces a monotone lattice path. At step t, numbered from zero, its departure monomial has total degree t. Exactly one term occurs at that total degree in the two components together, with coefficient +1. Its component specifies a or b. Sorting these terms by total degree reconstructs every letter, including its position. The empty word has zero flow.

Thus E restricted to the entire free positive monoid is injective, at every length. In particular it retains all factors of any Sturmian word. No theorem about Sturmian complexity is needed for this implication. E(ab) and E(ba) have the same monomial XY but different flows (1,X) and (Y,1).

## Some signed words are identified

Projection (m,u)→m has an abelian image and an abelian kernel: translations (1,u) add. Every commutator is a translation, so all commutators commute. In particular

    E([a,b]) = (1,(1-Y,X-1)) ≠ (1,0),
    E([[a,b],[a,b²]]) = (1,0).

The latter word is not the identity in F2. Write C=abAB and D=abbABB. In CDC^-1D^-1 the only cancellations reduce the result to

    abABabbABaBAbbaBBA,

which has length eighteen and no adjacent inverse pair. This explicit freely reduced kernel element makes G a proper quotient, despite positive injectivity and the survival of the first commutator. In particular noncommutativity alone does not force faithful F2.

## All substitutions descend

For any endomorphism f of F2, let E(f(a))=(m_a,v_a) and E(f(b))=(m_b,v_b). Define the ring endomorphism S_f by X→m_a and Y→m_b, and let J_f be the matrix with columns v_a,v_b. The formula

    Phi_f(m,u) = (S_f(m), J_f S_f(u))

is a homomorphism of the ambient affine group: substituting into u+mv yields J_f S_f(u)+S_f(m)J_f S_f(v). On A and B it agrees with evaluating f(a) and f(b). Therefore E(f(w))=Phi_f(E(w)) for every signed word w. Equal encodings remain equal after any substitution, so ker E is fully invariant. The restriction of Phi_f to G is well-defined independently of the chosen spelling of an element.

For an automorphism f, the construction for f^-1 is its inverse on G: both composites are the identity on A,B and hence on G. Thus the counterexample retains all automorphisms, not just one chosen golden map. It is natural under renaming and change of free basis. It does not need a selector choosing a representative of an equivalence class.

For sigma(a)=ab, sigma(b)=a and tau=sigma^-1 with tau(a)=b, tau(b)=Ba, the formulas are

    S_sigma: X→XY, Y→X;    J_sigma = [[1,1],[X,0]],
    S_tau: X→Y, Y→X/Y;    J_tau = [[0,Y^-1],[1,-Y^-1]].

The polynomial matrices are semilinear data: their composition includes substitution of the matrix entries, not ordinary matrix multiplication alone. Direct substitution gives sigma(tau(a))=a, sigma(tau(b))=b and the reverse identities. Therefore the induced golden substitution and its inverse are exact automorphisms of G.

## What would force F2 instead

The universal group completion is a stronger requirement than some injective embedding of the positive monoid into a group. If a group H with distinguished generators h_a,h_b permits a unique homomorphism to every group K for every prescribed pair in K, then H is isomorphic to F2. Indeed, the assignments give maps H→F2 and F2→H that fix the respective generators under composition, hence are inverse. This is a self-contained universal-property proof, not a derivation of why physical descriptions must meet that requirement.

There are therefore three separate statements:

1. Retain all positive descriptions and their substitution laws. The explicit G meets this.
2. Retain all freely reduced signed descriptions, or require the unrestricted universal group completion. This specifies F2 and excludes G.
3. Realize that group and its automorphisms by the chosen geometric and physical structures. This is a further requirement.

B1380 §2 starts with statement 2 and a surface category; its conditional punctured-torus argument is untouched. Its §3 cannot infer statement 2 from statement 1. GENESIS GM4 already keeps the stronger premise explicit after R57. The refinement here is that the alternative need not forget positive order, and FK5's test of a nontrivial commutator distinguishes F2 from its abelianization but not from this quotient.

## Consequence for the root audit

The constructive question is which signed distinctions an independently justified observable or reversible-context principle must retain. Neither this quotient nor F2 is declared the physical answer here. A justified universal completion could remove this ambiguity; merely preferring the downstream geometry that works cannot count as deriving it from positive-word fidelity. Conversely this counterexample to one implication is not a theorem that the stronger premise cannot be justified.

The affine construction is Magnus-style classical mathematics. No identification with the complete free metabelian quotient, embedding theorem or external classification is needed or claimed. The all-word statements above are analytic arguments; finite checks in verify.py are safeguards, not replacements for them.
