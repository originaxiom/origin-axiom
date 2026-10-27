# Which compact Higgs configuration is actually selected?

October 27, 2026. UNREVIEWED author hand derivation. No scientific
code, symbolic engine, test collection, optimizer or numerical solver
was run. This continues the input account of the compact ordinary
Higgs branch; it does not identify that branch with the physical parent.

## 1. Reuse and exact scope

Reuse the fixed genus-three quaternion cover pi:Y->E_tau, the preceding
COMPACT_UNIFORMIZING_CORE_AND_GLOBAL_INPUTS and combined spin/gauge
descent. The genus, ramification, quotient, form kernels and original
field-degree warning are already in the form-parent/theta-root proofs.
The read-only already-banked query `quaternion quadratic differential
Hitchin` returned B101 and B1233; their FINDINGS were read. B101 already
records the classical differential parameterization, for a different
punctured SL3 character problem. No discovery of that general mechanism
or repository-wide absence is claimed here.

The question here is narrower: for the fixed HOLomorphic gauge bundle
E=S^(-1) plus S, S^2=K_Y, classify its stable ordinary rank-two Higgs
pairs, then impose the actual Q8 geometric action. Do not assume the
nilpotent locus is the whole family. Do not vary the complex curve or
silently retain the old flat coefficient's physical spectrum.

I personally read Hitchin's section 11 through the complete proof of
Theorem 11.2 (printed pp.118-121), in addition to the earlier compact
existence/uniqueness proof:
https://pagine.dm.unipi.it/~a019210/Hitchin_Self-duality%20Equation%20on%20a%20Riemann%20surface.pdf
The classical Higgs section is reused; the specified-cover invariant
calculation and the conditional modular joint below are authored checks.

## 2. The full stable family on this fixed bundle

Write a trace-free ordinary holomorphic Higgs field in the displayed
splitting as

    Phi=[[a,b],[d,-a]],
    a in H0(K_Y), b in H0(O_Y)=C, d in H0(K_Y^2).

Bundle degrees require these spaces; they are not three scalar
coefficients on one common trivial line. If b=0, the positive-degree
line S is invariant, so the pair is unstable. If b is nonzero, a
constant complex diagonal automorphism normalizes it to 1. A lower
triangular automorphism g=[[1,0],[a,1]] then gives

    g Phi g^(-1)=[[0,1],[q,0]], q=d+a^2.          (1)

The lower entry of g is a global section of Hom(S^(-1),S)=K_Y,
so this is a genuine global holomorphic gauge change. The invariant
q=-det(Phi) is a quadratic differential, not a freely removable
amplitude of the old nilpotent orbit.

Conversely, every field (1) is stable. A holomorphic line N of degree
at least zero cannot have a nonzero projection to S^(-1): the degree
of Hom(N,S^(-1)) is negative. Hence its generic fibres would lie in
S. The upper entry 1 sends every nonzero such fibre outside S, so N
cannot be Phi-invariant. Thus all invariant lines have negative degree.
The compact theorem gives a harmonic solution for each q, unique up
to gauge within that holomorphic orbit. Distinct q's are separated by
the determinant. By Riemann-Roch dim H0(K_Y^2)=3g-3=6.

This is a classification only for this fixed split E and its stable
pairs. It does not classify all bundles, nilpotent degree-minus-one
branches, defects, higher-rank backgrounds or the whole architecture.

## 3. Actual deck invariance reduces six complex coefficients to one

An invariant holomorphic quadratic differential on Y descends away
from the branch point to a quadratic differential on the elliptic
quotient. At a branch point use z=w^2. Invariance under w->-w gives

    q_Y=f(w)dw^2, f(-w)=f(w),
    q_E=f(sqrt(z))/(4z) dz^2.

Thus the descended differential has at most a SIMPLE pole at the
single branch value p on E. Conversely any such differential pulls
back holomorphically. Therefore

    H0(Y,K_Y^2)^Q8 = pi^* H0(E,K_E^2(p)).         (2)

Since K_E is trivial and deg(p)=1, elliptic Riemann-Roch gives dimension
one. Constants already fill H0(O_E(p)); a meromorphic function on E
cannot have just one simple pole. With the registered coordinate z,
the complete invariant family in (1) is consequently

    q_c=c pi^*(dz^2), c in C.                    (3)

Near each of the four branch points it is 4c w^2 dw^2. These alternatives
keep regularity and the nilpotent leading value at each branch point;
they do NOT keep the exact nilpotent profile on an open disk. If exact
nilpotence is imposed on an open disk, the identity theorem forces
q=0 everywhere. That stronger restriction must stay explicit.

On the combined bundle V+=O plus K, (1) is the natural map with upper
entry 1 and lower entry q_c. Thus the finite deck group and combined
form descent alone do not select c=0. This is an explicit remaining
family, not an asserted absence or a programme-wide obstruction.

## 4. A conditional modular law can select c=0 without a fit

The registered root-family maps cover z'=z/(C tau+D) under a modular
matrix gamma=[[A,B],[C,D]]. Suppose q is transported as an UNTWiSTED
gauge-invariant quadratic differential; conjugating Phi by a gauge
change leaves its determinant unchanged. Equation (3) then requires

    c(gamma tau)=(C tau+D)^2 c(tau).              (4)

If, IN ADDITION, c is holomorphic on the upper half-plane, holomorphic
at the cusp, and equivariant under the FULL SL2Z action with trivial
character, it belongs to M2(SL2Z), which is zero. Hence q=0. This is a
conditional selection of the nilpotent orbit from (3), not a choice
of its coefficient by fitting a measured value.

The classical vanishing has two checks. The scalar ring used already
in main's B1691 Mbasis is generated in weights 4 and 6, with no weight-2
monomial. Independently, c(tau)d tau would descend to a meromorphic
one-form on compact X(1), a sphere. Holomorphy and the weight law make
it regular at elliptic points; at the single cusp it has at most a
simple pole. The residue theorem removes that sole residue, leaving
a holomorphic one-form on a sphere, hence zero. This proof does not
mistake an ordinary weight-2 form for the existing vector-valued forms.

The standard dimension statement/valence argument was personally
checked in Modular Forms III, section 2, Proposition 2.1 and
Corollary 2.1.1 (Columbia lecture notes, October 2024):
https://www.math.columbia.edu/~avizeff/Fermat/modular-forms-III.pdf
No claim of whole-note reading or a new modular-form theorem is made.

The assumptions in this paragraph are LOAD-BEARING. Fixed-fibre
holomorphy of Phi does not imply holomorphy in tau. A harmonic metric
normally depends on tau and its conjugate. A nonholomorphic weight-2
coefficient, meromorphic cusp data, a proper subgroup, a multiplier/R
twist or a family with only a selected modulus can evade this scalar
M2 condition. A phase on Phi can induce a character on its determinant.
The actual physical parent already has R data; setting it trivial in
(4) without its map would repeat the identification error. Modular
covariance itself does not force an individual broken-state vacuum
to be invariant; it can instead relate members of a state family.

There is a direct rejecting control for the cusp hypothesis: the
derivative j'(tau) of the modular invariant j satisfies (4), by
differentiating j(gamma tau)=j(tau). It is nonzero and has a pole at
the cusp. Thus a finite allowed cusp principal part changes the
answer; it cannot be discarded before reading the actual end law.

Accordingly this corollary is a useful target for deriving a selection
law from the real parent, not a license to impose convenient regularity
and declare that the foundational principle has paid for it.

## 5. The variational duty remains, including normal response

For a fixed scalar q in this stable section, the ordinary Hitchin
residuals vanish. A potential consisting solely of their positive
squares therefore does not distinguish the solutions in (3). It is
incorrect to infer selection of q=0 from uniqueness of the harmonic
metric within a fixed orbit.

A proposed additional positive Higgs-norm term must be checked in the
FULL equations. At a nonzero zero-residual background the derivative
of the residual-square potential vanishes, whereas the norm term has
nonzero variation along Phi->(1+t)Phi with A fixed. Merely minimizing
that term on the old zero-residual locus does not prove the old fields
remain stationary. A backreacted solution or a controlled effective
projection would be needed, with every complementary equation retained.
No new such term is added by this note.

## 6. Before/after and next same-parent map

| Dependency | Conditional deduction | Remaining duty |
|---|---|---|
| Holomorphic Higgs profile on fixed split E | Stable orbits parameterized by q in H0(K^2) | Why this bundle/ordinary field is physically admitted |
| Six complex q coefficients under fixed-fibre Q8 action | One complex c remains | State dynamics or stronger generated admissibility |
| c in a full, untwisted, holomorphic, cusp-regular modular section | Necessarily zero | Derive all those conditions for the actual physical determinant |
| Harmonic metric after an orbit is fixed | Unique up to gauge | Physical metric, couplings, full operator and charged lift |

This narrows the next question: identify the physical determinant's
base regularity, modular/R character and cusp domain from the SAME
field/action construction. If they meet section 4, the orbit choice
is conditionally removed without a fitted Higgs formula. If they do
not, keep the precise allowed c family or its actual state distribution.
Neither outcome supplies agy's inverse-Gram law by analogy, nor a
physical three-generation spectrum or gravity. All new deductions
remain unreviewed; no foundational input is marked paid.
