# The one-sided current has a second charged-vector species at the same pole

2026-11-08. **NEW AUTHOR HAND DERIVATION, UNREVIEWED AND UNRUN.**
No science imports, test collection, matrix/CAS/numerical evaluation or
scientific execution. Target source6fc2aa20654806b9ab0f0f3d831fcb8bed299fc9.
This is a conditional successor to the actual-current and preliminary
cross-check reports. It preserves their positive single-mode vertex and
adds a previously unresolved physical obligation. It is not a no-go
theorem for the generated architecture or for every stationary E8 model.
All mass, coupling and pole statements here are CLASSICAL/TREE LEVEL.
No claim of protection against quantum self-energies is made.

## 1. Fixed hypotheses and the question the single-mode proof left open

Retain the balanced complete-cusp E8 parent, coherent h4 lift, eta=O,
optional old Wilson chi=0, physical kinetic metrics and complete graph
domain. Both spinor modules (16,4) and (bar16,bar4) are retained. The
candidate supplied action, metric and spin/flavour identification remain
inputs. No new quotient, field identification or boundary condition is made.

The previous construction exhibits a Q=+1, principal grade mu=-2 vector
w_L with mass squared m0^2=7/(2ell^2), and a rank-one left quark current.
Its right current on the exhibited zero-mode spaces vanishes. It expressly
left other right-current vectors and possible degeneracies open. The
question here is whether the same construction in the other charge block
already supplies one. It does, under the stated analytical hypotheses.

The argument below establishes existence of current witnesses directly.
It does not need the earlier claim that the entire up kernel has exactly
three coefficients: constructing a nonzero product killed by the actual
M is enough. Completeness of the three-family candidate roster remains
an independent duty, not a prerequisite for preserving these witnesses.

## 2. Apply the global vector construction to BOTH charges

Let sigma=+1 or -1 label the electromagnetic charge, not a particle's
four-dimensional helicity. In either (16,4) singlet or its conjugate,
the two principal Spin5 modules are V_(3/2) tensor V_(3/2). On their
grade-minus-two vector plane the basis is

    |-3/2,-1/2>, |-1/2,-3/2>.

For either charge the actual source D0 gives

    Pv|_(sigma,-2)=Dbar^{*v}Dbar+7/(2ell^2).              (1)

The coherent highest character alpha_sigma obeys alpha_sigma^2=1.
Do not set alpha_+=alpha_- without a frame/duality proof; their equality
is unnecessary here. Five lowering operations yield

    A_sigma=i alpha_sigma sigma_x,
    D_sigma=diag(i,-i), B_sigma=D_sigma A_sigma.

These are unitary, square to -I and have commutator -I for BOTH charges.
The physical vector coefficient is S^2 V_sigma. The actual cusp norm
permits a simple pole in its half-power extension and forbids a double
pole. Thus the allowed compact sheaf is E(V_sigma)(p), not a degree-zero
rank-two flat bundle. The same determinant, maximum-principle and genus-one
RR/duality proof gives

    h0(E(V_sigma)(p))=1.                                (2)

Choose a normalized nonzero holomorphic profile z_sigma. It is smooth
on the core and decays in the physical end frame. The same complete
cutoff/form argument as the earlier witness puts it in the actual Pv
operator domain. Therefore

    Q z_sigma=sigma z_sigma,
    (H/2) z_sigma=-2 z_sigma,
    Pv z_sigma=m0^2 z_sigma.                             (3)

This is TWO existence constructions, one for each charge. The positive
charge construction alone does not exhaust the real vector field.

## 3. Count real charged species without counting antiparticles twice

Let J be compact conjugation of the gauge-profile bundle. It is antiunitary,
preserves the actual domain and commutes with Pv at moment zero. It flips
both Q and principal H weight. This uses the source real-gauge identity,
also checked explicitly by the curvature/rough-Laplacian rearrangement
in PRELIMINARY_CURRENT_CROSSCHECKS_2026_11_08.md.

The four profiles are:

| Profile | Q | mu | Charged vector component |
|---|---:|---:|---|
| z_+ | +1 | -2 | W_L^+ |
| J z_+ | -1 | +2 | W_L^- |
| z_- | -1 | -2 | W_R^- |
| J z_- | +1 | +2 | W_R^+ |

Set w_L=z_+ and w_R=J z_-. Both have Q=+1 and mass squared m0^2, but
different principal grades. They are orthogonal in the positive source
gauge norm. In particular z_- is NOT J z_+: it has the wrong grade.
The real vector field contains

    W_L w_L + conjugate(W_L) J w_L
     + W_R w_R + conjugate(W_R) J w_R.                    (4)

There are at least two independent complex charged-vector species at
this pole, each with its own antiparticle, rather than one species
counted twice. Other degenerate states have not been excluded.

Neither compact reality nor a Weyl-fermion reality condition identifies
the independent left quark/conjugate-quark coefficients. The source
mass proof already makes this distinction. A broken gauge generator's
massive transverse vector also remains physical after its Goldstone
and gauge-fixing bookkeeping; it is not removed by a scalar gauge quotient.
An unbroken unitary transformation preserving the Higgs pair also
preserves their moment sum H and cannot identify opposite H grades.
No extra gauged parity or conjugation quotient is supplied here.

## 4. Both species have nonzero currents on exhibited quark modes

At eta=O, chi=0, each down coefficient and its conjugate has one
holomorphic spin representative on

    u': |-3/2,+3/2>, v': |+3/2,-3/2>.

The combined middle characters are alpha sigma_x and I; exactly one
flat eigenline is trivial. A nonzero section on that line has both spin
components. Direct substitution into all rows of the source M verifies
the zero equation. The cusp norm and graph cutoff are the original ones.
This existence step does not infer chirality from an index.

Let d be the down spin profile and d_c its independent LEFT conjugate-
charge counterpart. The actual Spin10 map 16 tensor16 ->10 and the
barred counterpart are both nonzero. Their restriction is
Gamma5 tensor J5 plus J5 tensor Gamma5, with the A3 exterior factor.
The extremal coefficients used in the previous proof are nonzero in
both modules; the ten appears once, and no new coefficient is inserted.

Consequently [z_+,d] and [z_-,d_c] are nonzero holomorphic up and
up-conjugate spin profiles, respectively. They have the same extremal
raising/lowering annihilations as the previous product witness. Thus
M kills them directly and their actual physical norms are finite.
Normalize these products as u and u_c, with d,d_c,z_+,z_- normalized.
The source vertex gives nonzero coefficients

    g_L=g6 ||[z_+,d]||_spin,
    g_c=g6 ||[z_-,d_c]||_spin.                           (5)

Both norms are strictly positive. The norm comparison in the next section
earns equality of their magnitudes in this particular pure-h4 background;
it does not evaluate their common value.

The z_- vertex is a Q=-1 vertex between independent LEFT d_c and u_c.
Its Hermitian conjugate is the w_R=J z_- vertex, from u_c to d_c.
In the usual right-quark notation this is a nonzero RIGHT charged
current with |g_R|=|g_c|. The principal-weight selection table gives,
on these exhibited quark spin subspaces,

    w_L: nonzero left, zero right,
    w_R: zero left, nonzero right.                       (6)

The original left-current witness survives. The larger physical theory
also contains the second species; retaining only the first vertex is
not a completed chiral-sector analysis.

## 4a. The relative coupling is fixed by actual norm intertwiners

This extra step was not established by the single-mode proof. It requires
transporting the profiles, fibre bracket and measuring metrics together,
rather than identifying equal-dimensional spaces.

First compare the vector bundles for the two holomorphic witnesses.
The two alpha_sigma are each real signs. Their D matrices agree, and
their A matrices agree up to a sign. If the signs agree take T=I; if
they differ take T=diag(1,-1). In either case T is constant unitary,

    T A_+=A_- T, T D_+=D_- T.

It therefore also intertwines B, their flat connections, half-power
extensions and physical S^2 metrics. The one-dimensional holomorphic
spaces are isometric: after a constant phase,

    z_-=T z_+,          |z_-(x)|^2=|z_+(x)|^2.            (7)

This is a coefficient-bundle comparison, not a gauge identification
of opposite-charge physical fields. Their charges and currents remain.
No base orientation reversal or unprovided surface isometry is invoked.

Next compare d and d_c. Each lies in a unitary TRIVIAL flat eigenline
of its combined middle transport, tensor the SAME spin S. A normalized
flat eigenvector of a phase times sigma_x has two components of equal
absolute value. Each compact holomorphic line section is the same
nonzero section of S, up to phase and overall normalization. Therefore
the physically normalized d and d_c have the same pointwise norm,
with each of their two spin components carrying half that norm.
The shared Omega slot metric is essential here.

Finally compare the actual brackets. In orthonormal weight frames their
two nonzero component maps have a common absolute coefficient C:
the compact gauge exchange of the two Spin5 factors preserves the E8
trace and relates these coefficients. For the barred module, compact
conjugation of the E8 bracket followed, at the FIBRE level, by the two
unitary principal-SU2 rotations that reverse m and n relates its extreme
coefficients to the unbarred ones. The rotations send highest to lowest
normalized weights; bracket covariance and the trace preserve C's
magnitude. This fibre argument is not asserted to be a global symmetry
of the background or a global anti-linear intertwiner of Dbar.

For a vector with components a,b, the product components are, up to
unit phases, C b d_u and C a d_v. Hence in physical orthonormal frames
the pointwise product norm is

    |[z,d]|^2=(C^2/2)|z|^2 |d|^2.

The same formula, with the same C, holds in the barred sector. Equation
(7), the pointwise down-norm equality and the original common positive
kinetic measure give

    ||[z_+,d]||_spin=||[z_-,d_c]||_spin,
    |g_R|=|g_L|>0.                                      (8)

No numerical wavefunction integral or measured datum is used. The
relative magnitude is a conditional tree-level consequence; its common
value and the input g6/metric remain. The actual coefficient intertwiners
and fibre bracket norm relation are explicit new review duties. The
statement is not extended to arbitrary additional flat twists, new
stationary fields or quantum self-energies without redoing those maps.

## 5. Positive pole residues prevent hiding the second species by a basis

In the two normalized charged-vector coordinates the transverse
quadratic operator has (p^2-m0^2) times the identity, up to the overall
Lorentz/sign convention. The two species couple to the displayed
left/right quark currents with column vectors (g_L,0) and (0,g_R).
The contribution to the pole-residue matrix on these two current
channels is therefore

    R0=diag(|g_L|^2,|g_R|^2)=|g_L|^2 I2.                 (9)

This is a rank-two positive matrix. A unitary change of basis among
degenerate vectors leaves the corresponding coupling Gram invariant.
Choosing a different pair of vector names cannot remove its positive
right-current residue. Additional positive-norm degenerate vector modes
add positive-semidefinite residue contributions; they cannot cancel
the diagonal right-current contribution by a basis relabeling.
This is the direct finite Gaussian/resolvent consequence of the source
kinetic metric, not an independent assumption about a selected vacuum.

The old complete-mode-elimination proof also gives the correct scope:
attempting to integrate out W_R at p^2=m0^2 makes the actual complement
inverse singular. Its response has a pole. A local constant response
or a freely chosen boundary projection cannot erase it while preserving
the same action, positive norm and graph domain. Well below this mass,
both vectors can instead be eliminated, producing both left and right
current interactions. Their sizes still need actual norm integrals.

## 6. What can change this conclusion, and what cannot

Within the retained balanced constant-curvature construction the vector
existence lemma holds for either coherent central sign, any extending
spin (eta^2=O in S^2), and any extra unitary flat line tensor factor in
the charge-one coefficient. The extension maximum principle and RR
apply to those twists too. Changing the elliptic modulus changes the
profiles, but the two holomorphic mass eigenvalues remain7/(2ell^2).
Changing ell rescales both. These changes alone cannot split this pair.
The quark-current assertion (5) specifically retains the exhibited
eta=O, chi=0 quark spin modes; a different twist must recheck the modes
and their currents rather than inherit (5) blindly.

Deriving a different nonlinear stationary background, a physical source/
end law from the registering architecture, a justified new representation
map, or quantum vacuum dynamics could change the operator or its modes.
Those are named open duties, not results of this note. A finite complete
roster and actual normalized overlaps are needed before an empirical
comparison. At this pure-h4 tree-level point the relative magnitude is
one, not an adjustable suppression. An observed scale assignment,
complete low-state interpretation and quantum response are not supplied;
no universal exclusion of approximations to the SM is inferred.

The concrete revision to our working picture is this: the pure-h4
candidate has a constructive left-current witness, but its own conjugate
sector also supplies a degenerate right-current species. The next model
test must account for that full pole; matching the remaining form-current
eigenvalue alone would not discharge the weak-chirality duty.

This conclusion does not depend on an asserted zero index, a sampled
search or the unreviewed completeness of the up count. Its load-bearing
dependencies are the actual source vector operator/compact real
structure, the two spinor transition planes, cusp extension and domain,
and both nonzero product brackets. They require independent scrutiny.
No scientific pass, formal claim promotion or programme-wide kill is made.
