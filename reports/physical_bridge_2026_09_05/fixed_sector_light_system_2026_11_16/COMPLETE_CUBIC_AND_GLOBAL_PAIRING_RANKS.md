# The actual cubic on the complete fixed-sector light space

2026-11-16. P-C3e author hand derivation pending independent review.
No scientific producer, CAS, collection or tests ran. The complete
kernel and actual source cubic are the preceding proofs' inputs.
Use an odd or aligned coherent state with the two charged spin lines.

## 1. Carry the field slots and all weights into the cubic

The eleven chiral zero-mode coefficients are

    A, B1,B2, N_+,N_-,
    P_1,P_2,S of charge +1,
    R_1,R_2,T of charge -1.

A is the neutral Q form. B1,B2 are D5 cross-module forms, with gauge
weight w=4. N_delta are neutral spin fields of weight w=-3 and flat
character (delta,delta). P_i,R_i are the actual charged highest-weight
forms with w=3. S,T are the opposite-charge spin modes of weight zero.
The only parent cubic is

    W3=(i/G) integral kappa(a,[u,v]).                    (1)

It contains one form slot. Q charge conservation, the two-triple
weight pairing and that slot rule leave three possible channel types,

    A S T,
    N_delta T times a linear functional of P_1,P_2,
    N_delta S times a linear functional of R_1,R_2.      (2)

For example B has w=4, while pairs of available spin weights sum to
0,-3 or -6. None pairs with B. Two pure-form inputs cannot fill (1).
A with neutral N modes also fails the weight pairing and Q bracket.
This accounts for every light mode before declaring any cubic zero.

## 2. Select the permitted N character through the literal gauge action

In charge +/-1 write the existing normalized spin polarizations as
delta_+=eta(a)alpha_+ and delta_-=eta(a)alpha_-, with
alpha_+=-alpha_-. Thus delta_-=-delta_+.

Let L_+^(3),L_-^(3) be the lowest elements of the j=3 adjoints in the
two so5 factors. Their spinor action lowers one principal j=3/2
factor by three. That extreme matrix element is nonzero. The spinor
four is faithful for so5 and its adjoint j=3 summand has a unique
weight-three matrix element in End(V_(3/2)). The other factor is
unchanged. This proves a literal nonzero gauge coefficient.

For a charge +1 highest form Z_+, put

    C=kappa(Z_+,[L_+^(3),Y_-]).

Here Y_- is the charge -1 spin vector with weights (j,-j). The
reflection interchanges the two lowest adjoints with phase -i and
interchanges the mixed spin extremes with phase -i alpha_-.
Invariance of kappa, alpha_+alpha_-=-1, and the order of the bracket
give the same coefficient C for
kappa(Z_+,[L_-^(3),X_-]). The two polarized terms in (1) therefore
sum to a nonzero constant times

    C(delta_--delta_N).                                 (3)

Only N_(delta_+) couples P to T. Interchanging charges gives the
other channel, N_(delta_-) coupling R to S. The remaining character
gives a pointwise cancelling coefficient. Both coherent correction
signs exchange the labels consistently.

## 3. Verify the global section map and its actual rank

N_delta is a section of the actual compact line S^4 L_delta with
one allowed puncture pole. Each such space has dimension one.
The charge -1 spin zero line has a nowhere-zero compact section psi_T
of S L_eta, where L_eta has core character eta. This follows from
alpha_- delta_-=eta and the physical spin line already retained.

The Hodge-dual holomorphic space of the charge +1 forms is

    H0(S^5 L_top,+^-1(2p)), dim=2.

For the selected delta=delta_+=eta alpha_+,

    L_delta L_eta=L_top,+^-1.

Consequently the actual multiplication is

    M_T: H0(S^4 L_(delta_+)(p))
                    -> H0(S^5 L_top,+^-1(2p)),
          n -> n psi_T.                                (4)

Its product has at most one allowed pole, so belongs to the target
with its inherited two-pole allowance. It is nonzero and injective,
and hence has rank one. No equality of line dimensions was used
to invent the map. For the other charge the same reasoning gives
a rank-one M_S from N_(delta_-) into the R Hodge-dual space.

The actual a representative of h in that target has the factor
Omega^-3/2 bar(h); the N spin representative has Omega^-3/2 n.
Inserting them in (1) gives the Hodge pairing with density Omega^-3.
Choosing h=n psi_T makes it a positive norm times the nonzero gauge
coefficient (3). The integral is finite in the exact source domain.
The explicit pole bounds give bounded decaying physical profiles
and their nonlinear products. Thus the rank-one statement describes
the physical integral and its complete-domain representatives.

## 4. Normalize without assigning a new flavour tensor

Use the positive source Gram to choose in each charged form two-space
one unit vector paired with (4) and its orthogonal annihilator.
Denote the coefficients by P_c,P_s and R_c,R_s. This is a choice of
complete mode coordinates with the original metric transported.
Let N_c=N_(delta_+), N_d=N_(delta_-). The full light cubic becomes

    W3_light=y A S T+lambda_+ N_c P_c T
                                      +lambda_- N_d R_c S.           (5)

y is the existing normalized same-action coefficient. Each lambda is
the corresponding literal integral divided by the square roots of
its three source kinetic coefficients. They are nonzero and fixed
by the supplied parent, actual sections and metric. Their numerical
values and any relation between their magnitudes require that very
integral calculation. No independently adjustable lambda is inserted.

The modes B1,B2,P_s,R_s remain in the complete light space. Their
displayed zero coefficients in (5) are tree-level projected cubic
facts. Heavy response and higher order retain their own equations.

The actual normalized unbroken gauge current is diagonal on the
three +1 and three -1 coefficients. Its projected quadratic moment is

    D_Q^(2)=e_Q(|S|^2+|P_c|^2+|P_s|^2
                              -|T|^2-|R_c|^2-|R_s|^2).               (6)

The neutral modes have zero Q charge. Equations (5)-(6) give explicit
bounded projections of the nonlinear F/moment source. Every controlled
second-order correction is annihilated by the corresponding normalizable
dual zero modes, exactly as in P-C3c. Additional residual projections
can also be present and need the full response.

## 5. An enlarged tangent changes the previous obstruction test

With only A,S,T active, (5)-(6) recover the earlier protected quartic.
With S=T=N_c=N_d=0 and charged forms present, every derivative of
(5) vanishes at quadratic order. Equation (6) then allows nonzero
forms with equal positive and negative total norm. In the misaligned
state S,T are absent and the complete projected cubic is zero, while
the same form moment test still applies.

The next proof tests whether the remaining raw quadratic residual in
these form directions can actually be cancelled by an admitted field
response. A vanishing projection alone does not supply that response.
The larger allowed light space and its coupled tensors must accompany
the interpretation of any positive or excluded tangent.

Independent review must check the complete character calculation,
literal two-term coefficient (3), nonzero extreme spinor action,
global product lines and exact pole allowance, physical Hodge pairing,
canonical normalization and every retained mode/current in (5)-(6).
No full stationary join, three-family SM interpretation or foundational
input reduction is claimed by these conditional light couplings.
