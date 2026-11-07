# Candidate complete zero-mode roster in the level-five transport

2026-11-07. **UNREVIEWED conditional hand derivation.** No scientific
implementation, import, collection, CAS, quadrature or test execution.
This follows the transport/end design sealed at `c0d19629f`; it is new
kernel scope, not a result of those six unimplemented controls.

Quantifier: the same supplied balanced E8 action, complete punctured
elliptic curve, extending spin eta, old nontrivial order-three Wilson,
and coherent Dic_5 transport `(J,R_(k pi/5)J)`, k=1,2,3,4. Keep all 248
coefficients, four physical Weyl slots and their domains. The physical
carrier/holonomy map is still supplied. The chosen pair's failure to
descend to a fixed LR mapping torus remains explicit.

## 1. Source reduction and what must actually be counted

The [transport-family proof](PIN2_TRANSPORT_FAMILY_AND_LEVEL_FIVE_FREDHOLM_CANDIDATE.md)
gives the candidate complete-complex Fredholm argument and a direct
compact-resolvent estimate on 128 at five. Reuse the old full two-triple
complex and source physical isometry `M=Uout T Uin`. Physical chiral
zeros are total cohomological degree one; the degree-three part gives
the physical gaugino. Right antiparticles are not additional independent
left fields, and bosonic gauge quotienting does not delete a gaugino.

The old branching and local bounded retraction are inputs already
exhibited. The new calculation is the **actual flat action on the
surviving cohomology**, including its nontrivial peripheral. An old
flat-line kernel count cannot be transferred by representation name.

## 2. A compact double cover turns the mixed cohomology into line problems

Write w1 for the Pin2 component character. Both marked generators a,b
are reflections, so `w1(a)=w1(b)=1`. Its connected double cover extends
to an unramified compact elliptic cover

    pi:C' -> C.

The two lifts p+,p- of the cusp differ by the nonzero order-two deck
translation t. Thus `T=O_C'(p+-p-)` is a nontrivial order-two line.
Let eta_c be the nontrivial order-two line on C associated with the
cover: its marked signs are (-1,-1), and `pi^*eta_c=O`.

A rank-two Pin2 cohomology representation of rotation weight w has
rotation eigencharacters `exp(+-i w alpha)` and reflection square
`(-1)^w`. Its bundle is induced from one unitary character on C' minus
the two punctures. On the cover the scalar spin is pi^*eta, with no
additional chosen spin line. Induced-bundle sections on C have exactly
the line sections on C', and their source L2 norms agree under integration
over the two sheets. Do not double their dimension again.

The character on the first lifted cycle a² is `(-1)^w`. Its two puncture
phases are inverse and may be written `exp(+-2pi i theta)` with the
principal weights `-1/2<theta<1/2`. Avoid the half-integer endpoints in
the following compact-extension argument; all needed n=5 weights do.

## 3. Determine the compact critical-spin line, including its discrete class

Use the holomorphic extension in which local coefficients have powers
`u^theta` at p+ and `u^-theta` at p-. Its degree is zero: the unitary
connection is flat off the punctures and its logarithmic residues sum
to zero, so integrating the curvature with the two boundary circles
gives first Chern number zero. This is an auxiliary holomorphic extension,
not a change to the physical norm.

Denote the resulting compact line by L_theta. The deck translation
exchanges the two character eigenlines, inducing the dual character.
The principal extensions commute with that duality since neither weight
is a half-integer endpoint. Hence

    deck^* L_theta = L_theta^-1.

Translation acts trivially on degree-zero line classes on an elliptic
curve. It follows that

    L_theta²=O.                                       (1)

This finite constraint prevents supplying a continuously fitted compact
line to get a favourable kernel. Within an interval of weights containing
no half-integer, the local extension frames and their holomorphic gluing
vary continuously. Equation (1) puts their classes in a discrete four-point
set, so the class is constant in that interval.

At beta=0 in the family `(J,R_beta J)`, the lifted character on a² is
`(-1)^w` and that on a^-1 b is 1. Thus:

- for even w, its compact line begins at O;
- for odd w, it begins at a nontrivial two-torsion line L_odd whose
  first lifted-cycle character is -1.

When the continuous puncture weight crosses a half-integer, keeping the
principal weights subtracts a local power at one puncture and adds it
at the other. The compact line is tensored by T or T^-1, which are the
same class. Each crossing toggles this one order-two factor. No arbitrary
phase or divisor is selected at that step.

For even w this gives `L_theta=T^r`, where r is the number of half-integer
crossings from zero. The parity of r is the parity of the nearest integer
to `w*k/5`; the sign of the peripheral convention changes r's sign, not
its parity. For odd w the classes are L_odd or L_odd tensor T.

The image of the four extending spin lines under pi^* consists of
`{O,T}`. Indeed it has size two, lies in the norm map's kernel by
`Nm(pi^*eta)=eta²`, and T is the nontrivial kernel member since its divisor
pushes to zero. L_odd is outside this image: every pulled-back spin has
first lifted-cycle character +1, whereas L_odd has -1 at beta=0.
Toggling by T cannot change membership in the image.

These extension, degree, continuity and norm-map steps are load-bearing
analytical review duties. They are not proved by an unrun finite-character
table. At a half-integer the two-sided dual extension changes and the
critical L2 endpoint must be handled separately.

## 4. Read the actual source norm at the two punctures

For the compact spin power S^a and a local pole of integer order m,
the actual physical radial norm with coefficient exponent theta is

    integral r^(a-1+2theta-2m) [log(1/r)]^(a-2) dr.

Therefore the maximal allowed pole is the largest integer m satisfying

    m<a/2+theta,
    or m=a/2+theta when a<1.                            (2)

This follows by the power integral and then its exact logarithmic
endpoint; no finite-radius tolerance replaces equality. At p- use -theta.
The compact line to count on C' is

    (pi^*eta)^a tensor L_theta
          tensor O(b_+(a,theta)p+ + b_-(a,theta)p-),   (3)

with b_+,b_- from (2). On the compact elliptic curve a positive degree d
has h0=d and h1=0, a negative degree -d has h0=0 and h1=d, and a degree-
zero unitary line has a section exactly when trivial. These are the source
elliptic line counts; (2) supplies their new physical divisors.

For `a=1` and `|theta|<1/2`, both pole bounds are zero. Thus its H0 is
one precisely if `(pi^*eta) tensor L_theta` is trivial. For odd w this
never occurs. For even w it depends on T^r and the actual pulled-back
spin. A nontrivial order-three Wilson line cannot cancel either order-two
factor: its pullback is still nontrivial because pi has degree two,
coprime to three. This covers **all eight** nontrivial source Wilson
characters, not a selected character.

## 5. The entire 128 kernel and its primitive-point dependence

The two spinor modules have `(j,l)=(3/2,3/2)`. Their extreme cohomology
lines on C are `S^-3` and `S^5`; their flat peripherals are trivial.
Their source divisor degrees are -2 and +2. They contribute two to the
physical degree-one kernel and no gauge/gaugino mode. The middle is
the induced representation of weight w=4 just calculated.

For k=1,2,3,4 the parities of the nearest integers to 4k/5 are respectively

    odd, even, even, odd.                              (4)

Consequently at the proposed physical odd spin eta=O the actual candidate
counts per gauge coefficient are

| k | triplet `3_(-1/3)` and conjugate, each | singlet `1_(+1)` and conjugate, each |
|---|---:|---:|
| 1 or 4 | 2 | 2 |
| 2 or 3 | 2 | 3 |

The triplet's old nontrivial order-three Wilson kills its middle H0;
the charged singlet has trivial old Wilson. The result uses the actual
line problem, not a chosen three-mode truncation. The corresponding 128
left-kernel dimensions are 16 and 18, retaining representation dimensions
and both conjugates. The adjoint-kernel dimensions agree by the dual
complex; no nonzero U3 index is introduced.

For eta=eta_c the table is unchanged. The other two extending spins swap
the two singlet rows. Thus the invariant description is whether the
pulled-back spin equals T^r, not a permanent label for a or b under
untransported markings. The two coherent electromagnetic sign choices
change the induced description by eta_c, whose pullback is trivial;
these counts are insensitive to that sign. Equality of this kernel count
does not prove equality of every physical observable or core spectrum.

As a known-answer control, the coherent quaternion case has w=4 and
beta=pi/2, raw weight 2 and even crossing parity. It gives one middle
singlet section exactly when eta(a)=eta(b), recovering the separate
quaternion kernel candidate. The full quaternion operator remains
non-Fredholm in other sectors. Its kernel table is a control, not a
substitute for (1)–(3) on the new transport.

## 6. Compute every remaining coefficient rather than stop at the spinors

For the unequal pair `(j,0)+(0,j)`, its two extreme lines are induced
rank-two bundles on C with powers `-j` and `2+j`, rotation weight j.
Its two middle packages have powers `1+j` and `1-j`, rotation weight
`1+j`. Reflection exchanges equal-power members across the two modules;
this is why they must be kept as pairs.

At five and primitive k, all weights 1,2,3,4 have nonzero noncritical
theta. Substituting (2) gives:

| j | degree at -j | degree at 1+j | degree at 1-j | degree at 2+j | physical H1 |
|---|---:|---:|---:|---:|---:|
| 1 | -2 | 1 | -1 | 2 | 2+1=3 |
| 2 | -3 | 2 | -2 | 3 | 3+2=5 |
| 3 | -4 | 3 | -3 | 4 | 4+3=7 |

All nonzero degrees have counts independent of flat characters and spin.
There is no gauge/gaugino kernel in these packages. Their adjoint counts
are the positive degree of the last column plus H1 of the low middle
line, giving the same totals. The spin line/old Wilson are retained in
(3) even when the degree makes the resulting dimension independent of
them. They are not declared physically irrelevant.

In the D5 adjoint the j=1 and j=3 pairs therefore give 3 and 7 neutral
chiral modes. Its remaining `(2,2)` module has extreme spin powers -4
and 6 on C, giving two; its middle weight-five peripheral is trivial
but its two core eigencharacters have values +-i on a. No order-two
extending spin can cancel them, so its middle H0 vanishes. This gives
12 D5 neutral chiral modes in total.

The `(10,6)` package is the j=2 pair, giving five chiral modes in **each**
actual colour-up coefficient `3_(+2/3)` and its conjugate. It is not a
count of five total across both conjugates.

Finally A3 has its entire `(0,0)` complex. Its middle weight-one bundle
has odd w and therefore no normalizable spin zero modes by section 4,
including the old Wilson factors. Its scalar/form lines retain the
source flat compact counts: nine Wilson/compensator-invariant directions
have one vector/gaugino and one chiral connection/form mode each. The
six other A3 directions have nontrivial old order-three character (with
the compensator's retained sign) and no such zeros. They are not discarded
as representations; their nonzero modes remain physical companions.

## 7. Candidate complete roster and its physical meaning

At eta=O or eta_c the complete massless chiral-multiplet roster is

| Actual U3 representation | k=1,4 | k=2,3 |
|---|---:|---:|
| colour adjoint `8_0` | 1 | 1 |
| neutral singlet `1_0` | 13 | 13 |
| `3_(+2/3)` and its conjugate, each | 5 | 5 |
| `3_(-1/3)` and its conjugate, each | 2 | 2 |
| `1_(+1)` and `1_(-1)`, each | 2 | 3 |

There are nine gauge vectors and nine physical gaugino modes. Counting
representation dimensions gives 67 or 69 chiral profiles, hence
76 or 78 independent-left mass-map zeros after including the gauginos.
For the two other spins the two charged-singlet columns interchange.
All conjugate representations are retained; zero net U3 index is a
check of this roster, not its derivation.

This is a better-posed candidate physical operator than the n=2 threshold
problem, but it is **not** the observed massive fermion spectrum or three
SM generations. In particular its colour-up and colour-down massless
multiplicities differ. A weak-current interpretation requires the actual
massive vector profiles and opposite-grading overlaps from the same
action. Quantum effects, other stationary states or a different derived
end cannot be excluded by this fixed-background classical count.

The primitive k choices give different charged-singlet counts even though
their Fredholm end verdict agrees. They cannot all be erased as a basis
convention from that coarse agreement. Nor can one add the spectra of
different backgrounds and call the sum one universe without deriving the
state or interaction law for that family. This preserves the full weave
while keeping the physical combination honest.

Before: a permitted line-normalizer background and no actual full kernel.
After, as a reviewable candidate: a complete same-action kernel roster,
the source of its discrete k/spin dependence and a scoped physical duty.
No hand-built Yukawa, added projector or favourable root deletion enters.
The physical transport/carrier dictionary, parent action, spin/flavour
assignment and state law remain hypotheses. No foundational input, SM
parameter, weak chirality, anomaly-complete SM3 phase or gravity is paid.

Independent review must especially check the induced-cover character,
extension duality/degree, the discrete-class continuation and wall twist,
all exact logarithmic endpoints, reflection-exchanged modules, old Wilson
pullbacks and the complete-domain Hodge/physical mass-map transfer.
Finite arithmetic alone cannot discharge those proof obligations.
