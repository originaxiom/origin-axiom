# F06 correction to the local algebraic spectrum only

Post-failure derivation, to be checked by a separately sealed execution.
Sections 1--4 of the initial PROOF remain unchanged. Section 5's quadratic
form and multiplicities are superseded as follows; the first failure is
retained in FIRST_RUN.md.

At the normalized center let S_i=(E_0i+E_i0)/2 and
u_i=t_i e0+sum_j b_ij e_j, using i,j=1,2,3. Then

    T* u = ((tr b)e0 + sum_i t_i e_i)/2,
    (Tu)_ij = ((b_ji-b_ij)e0 + t_j e_i-t_i e_j)/2, i<j.

The omitted piece was sum |t_i|^2/4 in ||T* u||^2. Each t_i also
appears twice in ||Tu||^2. Hence the correct full expression is

    <u,H1 u>=(|tr b|^2+3 sum|t_i|^2
                          +sum_(i<j)|b_ij-b_ji|^2)/4.

For the ordinary positive norm ||u||^2=sum|t|^2+sum|b_ij|^2, its orthogonal
subspaces are: symmetric trace-free b, dimension five and eigenvalue zero;
antisymmetric b, dimension three and eigenvalue 1/2; scalar b, dimension
one and eigenvalue 3/4; and arbitrary t, dimension three and eigenvalue 3/4.
The last two combine into multiplicity four at 3/4. This accounts for all
twelve dimensions and gives the corrected polynomial

    lambda^5 (lambda-1/2)^3 (lambda-3/4)^4.

The one-form u=e0 dx1 has norm one and <u,H1u>=3/4, whereas the discarded
formula assigns 1/2. This controls the specific missing term without using
an eigenvalue fit. General complex components will check the entire norm
identity, not only that example.

The analytic implications do not expand: this is a pointwise algebraic
kernel, the covariant derivative of Psi is nonzero, mixed terms remain,
and no global normalizable zero mode, generation count or chiral index
has been computed. The first incorrect formula remains visible, not green.
