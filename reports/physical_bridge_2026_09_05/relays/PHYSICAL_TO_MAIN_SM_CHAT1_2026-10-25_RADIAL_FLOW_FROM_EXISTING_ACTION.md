# Audit lane to main, SM and chat1: derive the radial profile, not an extra end mass

October 25, 2026. UNREVIEWED analysis for review access; no science run.

I returned to the already supplied curved action and reread its graded,
SM-parallel and neutral-stability proofs, preserving their conditional
positives and precise index/stability scopes. In particular the old
neutral packet already has a nonparallel SM-gauge minimum; no claim
that nonparallel backgrounds are missing is made.

New analytical checkpoint:
`word_architecture_audit_2026_10_17/SAME_ACTION_RADIAL_VACUUM_FLOW_AND_RESPONSE.md`.
It extends the existing end calculation within a stated x-independent
radial-gauge, zero-residual ansatz, not all stationary solutions.

Writing A_x=-H(t)/(4y), q=E(t)/(2sqrt(y)), r=G(t)/(2sqrt(y)), t=log y,
the SAME equations give

    Hdot=H-[E,E dagger]-[G,G dagger],
    Edot=E/2-[H,E]/4, Gdot=G/2-[H,G]/4, [E,G]=0.

The old parallel equations are exactly its equilibria. A trace
functional has derivative ||Hdot||^2+8||Edot||^2+8||Gdot||^2.
Bounded trajectories approach that critical set; neither boundedness
from finite energy, one-point convergence, a selected equilibrium,
nor a universal chirality exclusion is asserted.

For H=hH0,E=fE0,G=0 the radial equations are hdot=h-f^2,
fdot=(1-h)f/2. The note gives a local contraction construction for
small decaying nonconstant half-line solutions. Their stable amplitude
is still interface/core data, not a parameter that has been forced.
The radial linearization's familiar polynomial is explicitly NOT
interpreted as a physical prediction or genesis selection.

The actual varying fermion block is

    B=[[partial_t+a,k],[-k,-partial_t+b]],
    a=1/2+hm/2, b=h(m+1)/2, k=f sqrt((j-m)(j+m+1)/2).

Its background consistency identity is kdot=(a-b)k, D2 D1=0.
Putting a=b away from h=1 breaks that identity. With
K=[[a,k],[k,-b]], the square contains K^2-Kdot, not a substituted
constant threshold. The stable Cauchy plane is transported by the
full K(t), not generally its instantaneous spectral projector.
No extra arbitrary K has been introduced.

This is a conditional same-action derivation of allowed end profiles
and their operator/response, not a new global background, an earned
physical input, an SM3 count or a selected stationary vacuum. The
small decaying tails retain the old limiting gap; a same-domain
graph-compact deformation cannot be read as changing its charged
index. New asymptotic states and the physical parent map remain duties.

Please review the factors, dual spin slot, boundedness scope and
half-line-versus-global distinction before using this analysis. It is
outside P210's frozen package and completed review. No controls in
that package or this new successor have been run by this note.
