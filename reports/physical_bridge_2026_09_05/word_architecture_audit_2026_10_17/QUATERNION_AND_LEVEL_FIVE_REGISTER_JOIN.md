# Two registering representations: a common source, not an identification

2026-11-07. **UNREVIEWED conditional hand derivation and joining audit.**
No scientific imports, collection, numerical or CAS execution. This note
addresses the highest-level physical input still supplied by the present
candidate: what connects the proposed quantum registering sector to the
spin/flavour/gauge fields and their interactions?

The quantifier is the already defined quaternion based-register extension
and the declared level-five Weil representation. It is not a theorem about
every possible registering representation, quantization or genesis axiom.
No physical state, observer, qualia mechanism or SM parameter is derived.

## 1. Recover the two actual representations

The [faithful registering tower](FAITHFUL_LIFTED_REGISTER_TOWER.md) already
retains

    E={(phi,g): rho(phi(h))=g rho(h) g^-1 for every h in F2},
    rho(F2)=Q8,  g in SU2,
    projection E -> 2O,
    homology map E -> SL(2,Z), e -> M_phi.              (1)

Its geometric/spin successor retains the required metaplectic information
when fields and the curve move. The physical flavour proposal uses the
two-dimensional quaternion representation of g. It is not a faithful
representation of the whole based source E; the other registering data
must remain alongside it.

Main's B1856 at `217e37c4f` supplies a different finite representation: the
level-five Weil space C5, split into even dimension three and odd dimension
two. Its independently constructed `verification/weil5_check.py` was read
as source, not run. The report correctly prices the interpretation of
that space as physical, and its quantum-superposition premise. The present
note uses the source's actual diagonal T and parity basis to check the
potential join; it does not certify its 120-element numerical enumeration.

## 2. The odd level-five space cannot be the fixed quaternion flavour action

There is a direct all-frame discriminator. A unitary normalizing Q8
permutes its six noncentral elements `+-Fi,+-Fj,+-Fk`. On the real
three-space of imaginary quaternions its adjoint is a signed permutation
of the three axes, preserving the product orientation. The projective
normalizer is therefore the rotational octahedral group, of order 24.
Its SU2 preimage is 2O of order 48, as already derived in (1).

In particular its projective action has no element of order five.
The conclusion is invariant under conjugating the quaternion subgroup
or changing its orthonormal basis.

By contrast use B1856's actual diagonal operator

    W5(T)|x>=zeta^(3x²)|x>, zeta=exp(2pi i/5).

On the odd parity basis

    v1=(|1>-|4>)/sqrt(2),
    v2=(|2>-|3>)/sqrt(2),

its matrix is exactly

    W5^-(T)=diag(zeta³,zeta²).                         (2)

The eigenvalue ratio is zeta, so its projective order is five. Overall
phases and scalar metaplectic sign choices do not change that ratio.
No unitary intertwiner can therefore identify this entire action with
the g action in (1) on a fixed marked quaternion register.

An explicit check in the displayed Pauli frame gives

    W5^-(T) Fj W5^-(T)^-1
       =cos(2pi/5) Fj+sin(2pi/5) Fk.                  (3)

Both coefficients are nonzero, so the result is not one of Q8's six
noncentral elements. The order argument proves that merely changing
the Pauli frame cannot cure it. Testing only unitarity, dimension two,
the shared central sign, or a quaternion subgroup inside a larger finite
group would miss this mismatch of the **whole generator action**.

This is a scoped failure of a particular identification. It does not
refute either register, the full architecture, or the possibility of an
interaction between them. Nor does it exclude order-five **images** of
elements of the larger source E in another representation. The source
element can have infinite order while its two finite images have different
orders. The error would be demanding that those images be identical.

## 3. A natural common-source join exists without that identification

Keep both arrows from (1). Reduction of M_phi modulo five followed by
the declared Weil representation gives a second action of the same E:

    E -> SL(2,Z) -> SL(2,F5) -> PU(W5).                 (4)

It coexists with the physical flavour action `e -> g` in (1). A common
word thus acts on the product record by its two **different** matrices.
Their equality is neither required nor generally possible. The based
kernel lost in (4) remains visible in the existing faithful tower, so
adding this finite record does not justify discarding that tower.

At the level of Hilbert representations, a supplied physical action U
and this supplied projective Weil action V give

    e -> [U(e) tensor V(M_phi)]                        (5)

as a projective product action. Indeed
`V(M_e)V(M_f)=c(M_e,M_f)V(M_e M_f)` implies that the two sides of the group
law in (5) differ by the same scalar c, which disappears in PU. If exact
phases are observables, retain the pullback central extension with this
cocycle. Do not assign a convenient phase separately on each generator.

For the actual physical fields, U transports the whole structured curve,
bundle and domain over the marking family. Equation (5) is understood
fibrewise with those pullbacks; it does not fix a different geometry and
claim that every word preserves its spectrum pointwise. This is the same
family-versus-single-state distinction already established by the full
E8 transport proof.

Equation (4) is a mathematical construction from the declared source maps.
It introduces no arbitrary intertwiner identifying the two dimension-two
spaces. It also does not explain why W5 is a physical measuring sector.
Making (5) an extra physical field tensor factor would add degrees of
freedom and require the action/kinetic map. Making it an instrument would
require the instrument coupling and state/measurement rule. Neither is
paid by the common-source construction alone.

### The common source does not by itself force an internal correlation

There is a sharper conditional consequence for just the two proposed
rank-two internal spaces, with no geometry, based reference or other
fields added. Their projective images are S4 for the quaternion flavour
and A5 for the odd level-five Weil representation. The former is the
already computed octahedral action. For the latter, the centre -I of
SL(2,F5) acts as a scalar on odd parity, so the projective action factors
through PSL(2,F5)=A5. It is nontrivial by (2); simplicity of A5 makes the
image faithful. This uses the standard finite Weil representation as
a hypothesis, beyond just the single diagonal comparator.

The image H of E in S4 times A5 projects onto both factors. It is actually
their full direct product. To see this without assuming independent word
generators, put `N={a in A5 : (1,a) in H}`. N is normal in A5. If N=1,
the first projection would identify H with S4, which cannot surject onto
the group A5 of order 60. Thus N=A5; together with surjectivity to S4
this gives `H=S4 times A5`. Simplicity can also be checked from A5's
conjugacy-class sizes 1,12,12,15,20: a nontrivial proper union containing
the identity cannot have order dividing 60.

Consequently full E-invariance of a **density operator on these two
internal rank-two spaces alone**, in the ordinary quantum interpretation,
requires invariance under independent conjugation in both factors.
The quaternion two-space is irreducible, so its operator commutant is
scalar. The odd Weil two-space is also irreducible: the two distinct T
eigenlines are mixed by S. Hence their combined operator commutant is
scalar, and a positive trace-one invariant density must be

    density = I4/4 = (I2/2) tensor (I2/2).             (6)

There is also a proof of (6) which makes the retained based record explicit.
The natural inner lifts `J_a,J_b` project to Fi,Fj on flavour and to the
identity on homology/Weil. A density commuting with `Fi tensor I` and
`Fj tensor I` is `I2 tensor sigma` by their scalar commutant. Remaining
word invariance makes sigma commute with the irreducible odd Weil action,
so sigma is scalar; trace normalization gives (6). Discarding the based
inner lifts would discard the first step of this argument.

Likewise a fully invariant Hamiltonian **acting only on those four
internal coefficients** is scalar. This is a finite conditional
classification, not a derivation that the physical universe uses (6).
Full invariance of a state, standard quantum states, and the two-space
truncation are all explicit premises. The prior faithful-tower proof
already discusses conditional invariant/Haar measures; this argument
does not introduce a probability law on the full histories.

In the actual physical parent an inner move also acts on gauge data and
the reference; its action is not flavour alone. Thus (6) must not be
transferred to the full E8 fermion/state space by forgetting those factors.

This prevents another false shortcut: attaching the two finite records
does not automatically supply an entangling dynamics or a preferred
relative orientation. It also identifies the constructive next place to
work: retain the relational geometry, based register, reference and
interacting fields. Their nontrivial common-source action can enter an
invariant interaction that is absent from the internal truncation.
A non-invariant state or spontaneous selection is another possibility,
but its selection law must be derived rather than hidden in (6).

## 4. A moving quaternion family is a second compatible construction

There is another explicit positive if a full SU2 element g is meant to
rotate the physical flavour frame. With joint gluing

    rho(h) Ad_(K(h)) Phi=Phi,

set

    rho_g(h)=g rho(h) g^-1,  Phi_g=g Phi,  K_g=K.

Then `rho_g(h) Ad_(K(h)) Phi_g=Phi_g` for every h, exactly. All source
unitary kinetic forms and the epsilon pairing travel with this move.
The resulting quaternion subgroup is a conjugate of the old one, and
composition is coherent for every g.

If the registering/reference fields also move, this can be a change of
frame of the complete relational data. It is not a new physical occupation
probability, nor a rule selecting a point of the fixed-reference vacuum
family. If a reference is held fixed instead, the earlier quartic readout
distinguishes states and the full coupled data must be reexamined. Do not
switch between those two readings mid-proof.

This family construction and (4) are distinct ways to retain the allowed
actions. Neither licenses replacing the original fixed rho by the full
level-five representation without specifying which construction is used.

## 5. What remains to derive, and why it matters for the goal

The useful reduction is to stop treating an arbitrary equality of the two
rank-two spaces as a prerequisite. The full source already supplies a
common mathematical action. Its internal invariant-state classification
is (6) under the named extra premises. The physical obligation is an **interaction
and observable map**, not an equality of two finite matrix lists.

To count a foundational reduction, derive from the stated principle:

1. which registering sectors are physical and which are representations
   used by an instrument;
2. the action that couples them to the full spin/gauge/fermion roster;
3. the normalized state, dynamics or distribution entering a readout;
4. why any fixed-level charge-invisibility or minimization condition is the
   relevant physical condition for that coupled action.

The current field action supplies a global flavour symmetry but does not,
by that symmetry alone, supply these four answers. Their appearance under
new names would not reduce the input count. Conversely, the order-five
mismatch above must not be banked as a whole-programme impossibility: (4)
and the moving-family construction show precisely how both mathematical
structures can coexist.

No empirical target or hierarchy is evaluated here. The remaining
physical-spectrum and boundary-law work continues in the same-action
candidate, with its source assumptions visible. This hand note requires
independent review; its future finite controls require a prior design.
