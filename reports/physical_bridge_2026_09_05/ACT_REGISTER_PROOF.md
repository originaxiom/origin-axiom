# Standard quotient criteria and explicit detector countermodels

Authored explanatory proof, October 2, 2026; classical/generic mathematics,
not an original theorem or independent scientific acceptance. Context:
B37 and B130 supply the detector questions; R57/R58/R79 supply the physical
transport duty. No interpretation of experience is a premise.

## AR1: an update and an output are separate descent obligations

Let q:X->Y be surjective, T:X->X a function and O:X->Z an output.
There exists Tbar:Y->Y with q*T=Tbar*q iff q(x)=q(x') implies
q(Tx)=q(Tx'). Necessity is substitution; sufficiency defines Tbar(qx)
as q(Tx), which is well-defined by the fibre condition. Similarly O
factors through q iff it is constant on fibres. Surjectivity gives
uniqueness. Check this separately for every declared update and output.

Both conditions together preserve observations along every finite word
of updates by induction. A lost historical difference is therefore not
automatically relevant. An output descending now does not suffice if an
update exposes a difference later. An update descending does not suffice
if a required output was already discarded. In a physical theory the
admissible updates, outputs, gauge equivalences and domains must be earned.

## AR2: sufficient future record, conditional on supplied dynamics

Define x~x' iff every finite word of declared updates, including the
empty word, gives the same declared outputs. This is an equivalence
relation, each output is constant on it, and every update preserves it
(prepend the update to the tested future word). Every other equivalence
preserving the updates/outputs refines it, by the AR1 induction.
It is thus the coarsest sufficient record for those specified duties.

On a finite X, refining the initial output partition by the tuple of
successor blocks stops after finitely many splits and yields that
equivalence. Independently, x and x' are distinguished exactly when
their ordered pair reaches an unequal-output pair under common updates.
Reachability visits at most |X|^2 pairs. This explains the two instruments.
It is not a derivation of the update, output, clock, norm or qualia.

## AR3: symbol presence is not semantic mechanism

B37's map is T(x,y,z)=(z,x,2*x*z-y), with
I=x^2+y^2+z^2-2*x*y*z-1. Its invariant and nonlinearity can be checked.
Set r=I on the graph of the record. Replace the last component by
2*x*z-y+(r-I). This is exactly the same map on that graph, but a free-
symbol test now reports r. The added term is zero on every allowed input.
This disproves using symbol presence alone as a representation-invariant
mechanism test; it does not establish self-modeling in either description.
B37's literal operational convention remains literally satisfied.

## AR4: global projection does not classify every component

Over characteristic zero, x(x-1)=0 and x*k=0 imply either x=0 with
arbitrary k, or x=1 and k=0. At (1,0), the Jacobian of these two equations
is the identity, and a neighbourhood excluding x=0 contains only that
point. The isolated component coexists with a line projecting to every k.
Any polynomial in k vanishing on the variety is zero; elimination onto
k is therefore the zero ideal. A lexicographic Groebner check is a control,
not the proof. For the point-only ideal (x-1,k), elimination contains k.

Thus B130's global empty-elimination result does not, by itself, exclude
isolated fixed-locus components. The actual metallic variety must receive
a componentwise argument before that stronger conclusion. No particular
isolated point or unsymmetrizable physical choice is asserted here.

## AR5 and AR6: retain positives while correcting identifications

sqrt(4^2+4)=2*sqrt(1^2+4): m=1 and m=4 have the same quadratic Perron
field Q(sqrt(5)). Distinct traces 1 and 4 still prohibit conjugacy of
their incidence matrices. Do not infer inequivalent matrices require
distinct fields.

K=Q(sqrt(-3)). Complex conjugation sends sqrt(-3) to its negative and
therefore does not fix K pointwise. It cannot belong to Gal(K^ab/K),
whose definition requires fixing K. This is the elementary distinction
already banked in B942 and explicitly carried by B723's correction.
It does not classify thermal states or identify a physical measurement.
