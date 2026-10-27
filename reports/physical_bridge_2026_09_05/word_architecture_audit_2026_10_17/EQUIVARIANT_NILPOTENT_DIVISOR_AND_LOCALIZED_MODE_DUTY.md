# Symmetry removes the two-zero nilpotent branch in the specified compact model

October 27, 2026. UNREVIEWED author hand derivation and targeted primary
reading. No scientific executable, CAS, import, producer or test run.
This is a CONDITIONAL reduction within an ordinary compact rank-two
Higgs model, not a foundational derivation of that model or a physical
three-generation result. It retains the full Q8 carrier; it is not a
statement about m004 alone or every allowed relational architecture.

## 1. Recover the prior, then state precisely what is being reduced

COMPACT_UNIFORMIZING_CORE_AND_GLOBAL_INPUTS sections 3–4 retained two
possible kernel degrees, d=1 and d=2. It supplied the zero-free split
uniformizing branch to construct a compact solution. The present
argument adds the already-existing FULL Q8 action to that degree test.
The group has only trivial or order-two stabilizers on the smooth
compact quaternion cover. Its four ramification points form one orbit
of length four; every other orbit has length eight.

The scope assumptions are: Y is that fixed genus-three cover; E is a
holomorphic rank-two bundle with trivial determinant; Phi:E->E tensor K_Y
is holomorphic, nonzero, nilpotent and stable as an ordinary Higgs pair;
the Q8 action on Y lifts to this pair, possibly projectively through
central gauge signs. It suffices that it preserve the rank-zero locus
and its vanishing multiplicities. A symmetry broken by the background
does not satisfy this hypothesis. No full-E8 selection is assumed.

The named choice to reduce is which nilpotent kernel degree/zero divisor
is admitted. It is not the choice of carrier, action, physical metric,
spinor dictionary or end law.

## 2. A short global proof without a split-bundle assumption

Let L=ker(Phi). Since Phi is a nonzero nilpotent map on a smooth curve,
L is a saturated line subbundle: E/L is isomorphic to the torsion-free
image sheaf, hence is a line bundle. Trivial determinant identifies
E/L with L^(-1). Nilpotence implies that Phi factors as

  E -> L^(-1) --f--> L tensor K_Y -> E tensor K_Y,
  0 != f in H0(Y,L^2 tensor K_Y).

The kernel is invariant, so stability gives deg L<0. Put d=-deg L.
Since deg K_Y=4, the effective zero divisor D=(f)_0 has

  deg D = 4-2d >=0, hence d=1 or d=2.

The divisor is intrinsic to the rank-zero locus of Phi; a lift preserving
the pair carries it to itself, including multiplicities. Every effective
Q8-invariant divisor is a sum of full orbits with nonnegative integral
multiplicities. Its nonzero degree is at least four. A degree-two D is
therefore impossible. It follows that

  d=2,  D=0,  L^2 tensor K_Y is isomorphic to O_Y.             (1)

Thus, WITH these symmetry/stability/nonzero assumptions, the zero-free
nilpotent kernel branch is forced. It need not be separately selected
from d=1,d=2. Its inverse S=L^(-1) is a square root of K_Y. The result
uses the complete compact orbit structure, not just a puncture chart.

This does NOT show that the primitive selects Q8 invariance, stability,
nonzero rank-two nilpotence, or the ordinary Hitchin parent. It does not
identify a complex E8 quadratic-null field with this rank-two field.
The earlier modular norm/character hypotheses remain unchanged.

## 3. What (1) does not remove: extensions and the physical parent

One still has an exact sequence

  0 -> L -> E -> L^(-1) -> 0.

Equation (1) does not split it. Before equivariance its extension data
lie in Ext1(L^(-1),L)=H1(L^2)=H1(K_Y^(-1)), of complex dimension six by
Serre duality and h0(K_Y^2)=3g-3=6. The earlier explicit uniformizing
solution used extension class zero. That is still an extra restriction
unless separately derived. Nor does (1) identify all square roots or
lifts on the complete charged physical field content.

If a chosen lift induces the canonical action on L^2=K_Y^(-1), then
invariant extension classes are constrained to H1(K_Y^(-1))^Q8.
Serre duality and the previously derived one-dimensional invariant
H0(K_Y^2)^Q8 bound this space to one complex dimension. This is a
necessary invariant-class condition, not a construction/classification
of all compatible lifts, real structures or physical vacua. With a
different induced character, recompute the representation; do not
silently reuse the one-dimensional count.

In particular, after tensoring with S a NONSPLIT extension gives
0->O->S tensor E->K->0, not a prescribed O direct-sum K. The canonical
bundle identity used in the split recovery control is conditional on
splitting. All of the interacting surface and Majorana-Weyl field maps
remain separate duties. No degree count supplies a chiral SM spectrum.

## 4. The coupled local equations specify the missing localization map

I personally read the introduction, equations 2.1–2.13 and complete
section 4 of Cecotti–Cordova–Heckman–Vafa, T-Branes and Monodromy,
1010.5780v1, https://arxiv.org/html/1010.5780 (accessed October 27).
This is targeted technical reading, not a claim to have read the whole
paper or Appendix C's complete proof. The previously read 1906.02212v2
is a different G2/PW paper. Their parents are not interchangeable.

The relevant source equations are 2.7–2.11, 4.2, 4.9–4.11 and 4.40–4.42.
On a contractible holomorphic surface patch the linear F-equations give

  a = dbar xi,  varphi = [Phi,xi]+h,  dbar h=0,
  h modulo [Phi,chi] for holomorphic chi.

This follows directly: dbar varphi+[a,Phi]=0 after cancellation of the
two commutators. It is the coupled connection/Higgs fluctuation, not an
arbitrary canonical form renamed as a spinor. D-flatness selects the
metric representative and physical norm; it is not discarded when
claiming normalized physical couplings.

Here is an explicit local test, derived by hand. Let O be the holomorphic
local ring of a smooth surface and N=E_+ in sl2(C). In the adjoint,
[N,H]=-2N and [N,E_-]=H. Hence

  coker(ad_N) = O [E_-],

which is free, with no O-torsion. In the fundamental doublet N maps
e_2 to e_1, so coker(N)=O[e_2], also free. These statements distinguish
bulk classes from localized torsion classes; they do not say that all
bulk classes vanish or that their global harmonic representatives lack
spatial concentration.

For a nilpotent field f N instead, with f a nonunit nonzero holomorphic
function, the exact quotients are

  coker(ad_(fN)) = O[E_-] plus (O/(f))[H] plus (O/(f))[N],
  coker(fN on doublet) = O[e_2] plus (O/(f))[e_1].

Thus a DERIVED zero divisor can supply localized matter support, while
a locally zero-free root core cannot supply this particular torsion
mechanism by merely declaring an old branch point to be a defect.
A nowhere-vanishing scalar coefficient is a unit and changes neither
quotient. The test generalizes on any fixed finite representation:
constant N has constant Jordan rank and free local kernel/cokernel.
Extra commuting background fields, fluxes, boundaries, varying orbit
or field content change the calculation and are retained possibilities.

The symmetry result (1) rules out the two-zero ordinary rank-two branch
ONLY when the full Q8 symmetry is preserved. If a derived physical
state breaks it, the d=1 divisor route remains live. This is a precise
conditional fork, not a prohibition on emergent symmetry breaking.

## 5. What the residue mechanism can and cannot discharge

The source residue formula 4.42 requires localized classes with
annihilators f_i, representatives satisfying f_i varphi_i=[Phi,eta_i],
and isolated intersection of their support curves. That is a faithful
localization map which can replace a guessed cubic; it is not supplied
by matching a fibre contour to a surface Yukawa by name. A single
puncture extended along the base is not itself an isolated intersection
of independent matter curves. Boundary terms and metric normalization
also keep their own duties.

Next: recover a SAME-parent derived background and charged sector with
actual bulk or torsion classes, reconstruct the complete multiplets and
evaluate its interaction. For a zero-free constant root, use the global
bulk complex and end response; for a derived varying-rank background,
use the displayed torsion test and, if its intersection hypotheses hold,
the residue formula. Neither path authorizes a freely placed defect.

## 6. Before-and-after dependency accounting

Before: fixed compact ordinary rank-two model + stability/nonzero
nilpotence + full Q8 symmetry + selected zero-free kernel branch +
selected split extension + physical interpretation.
After: the selected zero-free DEGREE/DIVISOR branch is eliminated by (1).
The symmetry/model/stability/nonzero assumptions, extension/lift data,
metric/physical-action identification and end conditions remain priced.
This is a conditional analytical reduction awaiting independent review;
no foundational input or measured SM parameter is marked derived.

The already-banked query 'nilpotent torsion localized Higgs' was run as
a locator, yielding broad older hits (including B1222 and B213), not an
absence certificate. This note makes no repository-wide novelty claim.
It reuses the prior compact degree proof and the established cover.
