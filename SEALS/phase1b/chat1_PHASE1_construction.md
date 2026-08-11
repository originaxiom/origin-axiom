# CHAT1 — PHASE 1 — CONSTRUCTION LANE
# TARGET: is the absence of a typed object->physics functor a THEOREM, or CONTINGENT?
# Seat: chat1 (web). Lane: construction. Date: 2026-08-10.
# Taken as banked, not re-derived: B1012, B813, B782, B936, the weight ledger.

## VERDICT

CONTINGENT. Not a theorem. The obstruction that is currently proved is proved
only over R and C, and it demonstrably FAILS over an integral structure. What is
missing is one named, unrun computation, stated in section 4.

Declared prior, before writing section 3: I expected to end at OBSTRUCTED, on my
own resolution bound. I did not. The bound turns out to be compatible with the
construction rather than to block it (section 5).

## 1. WHAT IS ACTUALLY PROVED ABSENT

B962 Q4: F4 is transitive on Jordan frames, so choosing a VEV is a choice with no
canonical answer. This is the strongest form of the obstruction in the corpus and
cc3 correctly used it to supersede my "missing potential" framing: a potential
cannot break a tie inside a transitive orbit.

But transitivity is a statement about the REAL (or complex) form. F4 compact/split
acts transitively on the frames of J3(O) over R. That is the whole content.

Q4 itself names the exception: "an arithmetic/integral structure ... that is the
one live opening, and it is unworked."

## 2. THE OPENING IS NOT HYPOTHETICAL - IT IS CONSTRUCTED IN THE LITERATURE

Elkies-Gross constructed an integral structure (J, E) on the exceptional Jordan
algebra of Hermitian 3x3 matrices over the Cayley octonions. Over that integral
structure the automorphism group is ARITHMETIC, hence DISCRETE, hence its orbits
on integral frames are FINITE in number - transitivity is impossible.

The literature reports the orbit count for the relevant integral structures as
TWO: one orbit containing the identity matrix, the other containing the circulant
with entries {2, eta, eta*}. The first yields E8^3; the second yields the Leech
lattice. (Elkies-Gross; the two-orbit statement is secondary-source and is flagged
UNVERIFIED here - see section 6.)

So: over R the frame choice is a continuum with no canonical member. Over Z it is
a choice among FINITELY MANY, i.e. a DISCRETE LABEL.

## 3. THE CONSTRUCTION

A typed functor needs a canonical selection. Over R there is none, by transitivity.
Over Z the selection problem is finite. Therefore:

  F : (object, integral structure) -> physics

is constructible as soon as the object's own arithmetic maps to the finite orbit
set. The frame ceases to be a continuous modulus and becomes a discrete datum -
which is EXACTLY the type of the programme's banked closing set (3 F2 bits, 8
states, B717/audit). The functor's domain is not "object alone"; it is object
together with an integral structure, and the programme already has one: the trace
field Q(sqrt-3), its ring of integers, the conductor-4 order O_4, the class group.

This is why the absence is contingent rather than theorematic. The theorem on
record forbids canonical selection over R. It says nothing over Z, and over Z the
mechanism that makes it impossible (transitivity) is absent.

## 4. WHAT IS MISSING, NAMED EXACTLY

ONE computation, and it is not a research programme:

  Does the object's own arithmetic select an orbit in the finite F4(Z)-orbit set
  of integral frames of J3(O_Z)?

Concretely, three candidate selectors, all already banked as object data:
  (a) the conductor-4 class group Cl(O_4) = Z/2 (h(-48)=2), with Frob_7 as
      generator (banked, Cell 4);
  (b) the image 2T = SL(2,F3) of the holonomy, which sits inside F4 and whose
      F4(Z)-conjugacy class is a finite datum;
  (c) the 3 F2 bits of the closing set, if they are the orbit labels rather than
      a separate structure.

If any of (a)-(c) lands on the orbit set, the functor is built and the absence was
contingent. If all three provably fail to map, the absence upgrades toward
theorem - but only after (a)-(c) are run, not before.

## 5. WHY MY OWN RESOLUTION BOUND DOES NOT BLOCK THIS

This session I proved: any FORCED value equals Re chi_V(M)/dim V, hence is a
character value, hence coarse - it resolves the object only to its group data.
I expected that to obstruct the functor.

It does not. An orbit selection is a DISCRETE LABEL - precisely a coarse datum.
The bound says a forced quantity cannot carry fine arithmetic; it does not say a
forced quantity cannot carry a finite label. So the bound is CONSISTENT with, and
in fact PREDICTS the type of, the selection in section 4: if the object selects an
orbit, it must do so with coarse data, and (a)-(c) are all coarse.

That is a nontrivial consistency check between the two halves of my own week's
work, and it moved my verdict from OBSTRUCTED to CONTINGENT.

## 6. WHAT WOULD REFUTE ME - stated so the adversarial phase has purchase

R1. If F4(Z) (or the relevant arithmetic automorphism group) is in fact TRANSITIVE
    on integral frames, section 2 collapses and the obstruction extends to Z. The
    two-orbit count is secondary-source in my hands and I have NOT verified it
    against Elkies-Gross directly. This is my weakest link and I name it as such.
R2. If "typed functor" in the target means something stronger than canonical
    selection - e.g. requires preservation of a monoidal or dynamical structure -
    then section 3 builds the wrong arrow and my verdict does not address the
    target. I have read "typed" as kind-correct in the R5 sense.
R3. If the object's integral structure is provably NOT of Cayley-integer type -
    i.e. J3(O_Z) is the wrong integral model for whatever the object supplies -
    then (a)-(c) cannot map by construction, and the missing piece is larger than
    one computation.
R4. If B962 Q4's transitivity argument already covers integral forms and I have
    read it as real-only when it is not.

## 7. ONE COINCIDENCE, FLAGGED AND NOT LEANED ON

The object's conductor-4 class number is 2. The reported integral-Jordan orbit
count is 2. Both Z/2. This is a match of CARDINALITY ONLY. Two-element sets are
the commonest finite sets in mathematics and I attach no weight to it; I record it
because a later seat will notice it and should find it already priced at zero.

## 8. SUMMARY

Absence of the functor: CONTINGENT.
Missing: a map from the object's arithmetic to a finite orbit set.
Status of that map: unrun, cheap, and with three named candidate inputs.
Weakest link: the two-orbit count, secondary-source, unverified by me.
