# AGY successor audit: repairs, foundation claims and debt closures

2026-11-07. Target: `1010fce5e66c56b7d7513deca92ffc2428bdf58a`.
Independent author of this audit: physical-bridge lane. Status: source and
hand-proof review, shared as an UNREVIEWED audit checkpoint. This is not
execution approval, a scientific test receipt, or main's acceptance.

## Verdict

There is useful correction work here. The corrected determinant and twist
witnesses, separate phase switches, and more honest evidence/population labels
should be retained. The strongest new foundation and blanket debt-closure
claims are not established by the delivered package. Several proposed closures
are already-known corrections or settle only one item of a larger debt.
No newly verified Standard Model parameter or foundational physical-input
reduction is established by these three commits.

This does not exclude the OA programme, its actual quaternion normalizer,
its whole architecture, or a future physical construction. It identifies
specific equations, assumptions and verification duties. In particular, the
mod-4 finding below does NOT refute the genuine `2O` subgroup of `SU(2)` that
normalizes the quaternion point; that is a different group construction.

## Frozen scope and method

Fetch completed successfully. The only changed remote branch, relative to the
immediately preceding inventory, was `origin/agy/audit-2026-11-02`:

- `8256798188b5bf5f2b5e2faec7bbeb4794799a1c`: F1–F6 response.
- `8ad51ef7407a90bc69e627674e2ee08f378d2205`: P000 bridge.
- `1010fce5e66c56b7d7513deca92ffc2428bdf58a`: five proposed debt closures.

Main stayed at `217e37c4f37bd80998f3c3e10cad358023f58114`, chat1 at
`195e8f1bdd7207970645c4fbd5847d238efb4d9c`, SM at
`47228ae85cb813ea1bcad3daba8b9446f64ff8d4`, and explore at
`af81fb6ef45f3544a5113a118599c16f185225a2`.

Read the three relays, both new modules, their tests, and the load-bearing
changes in `toe_closure.py` and its tests. Recovered main's actual register,
GENESIS premises, B997's dated correction, B1221's addendum, and B1832's
existing residue and half-lift results. Used Git reads, source hashes and
stdlib AST inspection only. No scientific module was imported; no test was
collected or run. AGY's reported test passes and numerical errors are its
claims, not reproduced execution evidence from this audit.

The receipt pins the nine changed files and the recovered upstream evidence.
Line numbers below refer to the frozen AGY target, not this checkout's older
versions. The previous audit at `ebee6ac2a` is preserved.

## 1. F1–F6 response: real improvements with remaining limits

| Finding | What the new source repairs | Remaining limitation |
|---|---|---|
| F1 | T141 distinguishes `det(A-I)=-1` from `det(A+I)=5`; its displayed SNF witnesses multiply correctly by hand. | It now equates the cusped bundle `M_-A = m003` with the closed branched cover `Sigma_2(4_1)`. These are different carriers. |
| F2 | T145 solves the four nonzero vectors `(x,2x)/5`, rejects `(1,0)/5` in the original marking, and gives `B=[[1,0],[-2,1]]`, `BAB^-1=[[4,1],[-5,-1]]`. It evaluates the natural witnesses separately. | A matrix conjugator does not complete transport of the modulus, fields, spin and physical operator. The horizontal evaluation remains a separate conditional control. |
| F3 | T155 now has four cells with independent real-modulus and Weil-phase switches. | Its numerical cell outcomes have not been rerun here. The old single-switch name survives only as an explicitly labelled joint removal. |
| F4 | T155 explicitly calls its matrix a supplied schematic texture, rather than the B1656 physical residue operator. | It remains a texture control. The conjugate-pair symmetry is valid within its assumptions and is not a no-go for general physical sewing. |
| F5 | T154/T156 distinguish imported geometric decimals and internal alternate-precision checks from fresh geometry and external review. | The new classifier consumes manually supplied booleans; it does not inspect the producer or evidence chain. It improves labels, not automatic provenance enforcement. |
| F6 | T147 separates the one-dimensional clock from the three-dimensional surface; T149 labels Pi2 a rationale and its shares a restricted-family calculation. | These labels do not derive the readout law, the population, the measure or a physical selection mechanism. |

### F1 carrier correction still owed

For a punctured-torus bundle, abelianization gives
`H1(M_A)=Z direct-sum coker(A-I)`. For
`A=[[2,1],[1,1]]`, the ordinary and negative-monodromy torsion orders are 1
and 5. These calculations survive.

But a double branched cover of the **closed** space `S3` along a knot is
closed; the once-punctured-torus mapping torus has a torus end. The figure-eight
branched cover has finite first homology of order 5, whereas `M_-A` has the
additional free `Z`. Their shared 5-torsion does not make them the same
3-manifold. Remove the slash/equality in T141's docstring and claim labels
(approximately lines 25123–25140 and 25290 onward). Any use of linking or CS
data from one on the other needs the actual filling/transport map.

### F5 discriminator limitation

At approximately lines 29382–29405, `_classify_numeric_source(True,False)` is
declared recomputation and `_classify_numeric_source(False,True)` imported.
Re-reading those labels passes even if the actual producer changes. Bind a
real artifact, its producing equation/code and its execution receipt before
calling this an enforcing provenance gate. Do not discard the useful corrected
evidence ledger while repairing this gap.

## 2. The mod-4 E7 identification repeats a recorded error

Theorem A's relay identifies the order-48 mod-4 group with `2O -> E7`.
`pure_logic_debt_closures.py:109–150` classifies the exceptional shadows from
the dictionary of **orders** `{24,48,120}` and tests mod-4 order 48.
An order test does not establish the corresponding isomorphism.

There is a short exact discriminator. In `SL(2,Z/4)`, both

`U=[[1,2],[0,1]]` and `V=[[1,0],[2,1]]`

are distinct nonidentity involutions: their squares are `I` modulo 4.
In `SU(2)`, any involution has eigenvalues both `-1` and is exactly `-I`;
the identity is the only other solution of `g^2=I`. Consequently
`SL(2,Z/4)` cannot be `2O` or any finite subgroup of `SU(2)`.

This was already recorded on main in
`frontier/B997_golden_conductor_uniqueness/ADDENDUM_2026-08-31_N4_is_an_order_coincidence.md`.
That note also recovers B1019's involution discriminator. This is a recovered
correction, not a newly discovered absence in the programme.

Retain the genuine mod-3 `2T`, mod-5 `2I`, and separate quaternion-normalizer
constructions. Reword the new criterion, if wanted, as **own-conductor 2I
plus specified modular shadow conditions**. It does not automatically supply
three binary McKay groups by reducing the same integer matrices mod 3,4,5.
Also, `4=1 mod 3`, so the m=4 generators themselves generate `SL(2,F3)`
mod 3 as well. Requiring just those two separate shadows does not distinguish
m=1 from m=4; the additional mod-4 condition is doing selection work.

## 3. Bounded metallic census versus a universal proof; a hand repair

The delivered routine enumerates `m=1..6` (`:114–150`), treating the last
case by component orders. The relay's all-`m` CRT proof is not written there.
The following independent hand argument supports the **exceptional
own-conductor** conclusion without relying on that finite range.

Put `N=m^2+4`, `G_m=<L^m,R^m> mod N`, with elementary upper/lower unipotents
`L,R`. Here 'exceptional' means one of `2T,2O,2I`; no claim about a
fundamental selection law is added.

1. **m odd.** `gcd(m,N)=1`. Powers of `L^m,R^m` recover `L,R` modulo N
   by Bezout, hence `G_m=SL(2,Z/N)`. Elementary row reduction over each prime
   power, combined by CRT, proves that these shears generate the whole group.
   If `m>=3`, `N>=13`, and the exact order
   `N^3 product_(p|N)(1-p^-2) >= 6N^3/pi^2 > 120`
   excludes all three exceptional groups. `m=1` gives `SL(2,F5)=2I`.
2. **m divisible by 4.** Write `m=4r`, `N=4d`, `d=4r^2+1` odd.
   Both generators are identity mod 4 and `m` is a unit mod d. CRT identifies
   their image with `SL(2,Z/d)`. At `r=1`, `d=5`, giving `G_4=2I`.
   At `r>=2`, `d>=17`, the same order bound excludes the exceptional groups.
3. **m=2 mod 4.** Write `m=2s`, s odd. N is divisible by 8.
   `(L^m)^(N/4)=I+(N/2)E12` and
   `(R^m)^(N/4)=I+(N/2)E21` modulo N. These are distinct nonidentity
   involutions, so `G_m` embeds in no `SU(2)` and is not a McKay group.

Thus the exceptional own-conductor hits are exactly `m=1,4`, with both
groups `2I`. This argument is hand-reviewed here, not independently reviewed
or executed as a new OA package. It repairs an evidence gap; it does not
repair the false mod-4 isomorphism.

The numerical subgroup-order product at m=6 requires care in general: CRT
alone does not make a subgroup generated diagonally the product of its
projections. In this case generator powers separate the coprime component
orders, so the product can be justified. Do not generalize that shortcut
without the separating-power or subdirect-product argument.

The rank-six simply-laced WZW comparison also survives in its **specified
category**: `A6,D6,E6` all have c=6 at level 1, with 7,4,3 primaries. Adding
the three-primary condition selects E6 in that category. Its physical use,
level and category still need premises. Header T-order numbers disagree with
the relay; the code asserts E6's value only. Do not promote every displayed
comparison entry to a separately checked theorem.

## 4. The foundation bridge needs its actual hypotheses

### Noncommutativity does not establish faithful F2 realization

The naturality correction survives: abelianization is natural, and it kills
the commutator. If a nontrivial commutator is required, `Z^2` is inadmissible.
Within the stated faithful-F2 surface category and a hyperbolic homology
action, the punctured-torus argument is useful and conditional.

But 'Z2 is excluded' does not establish 'every quotient is excluded'. For
example, the characteristic quotient `F2/gamma3(F2)` is the integral
Heisenberg group. In coordinates its multiplication is

`(x,y,z)(x',y',z')=(x+x',y+y',z+z'+xy')`.

Its generators have nontrivial central commutator `(0,0,1)`. The elementary
Nielsen automorphisms descend, and their hyperbolic action on abelianization
is still aperiodic. Sending the two generators to quaternion units gives
a nonabelian `SL(2,C)` representation with commutator `-I` and trace `-2`.
It is a proper quotient: triple commutators vanish. This is a countermodel
to inferring **faithfulness from the retained remainder and homology
aperiodicity alone**, not a proof that it meets every stronger OA premise.
If preservation of all free words is required, write that premise explicitly.

The rank-free proposal also needs a complete quantifier statement. A bare
requirement for a nontrivial invariant conjugacy class has an n=1 loophole:
`Aut^+(F1)` is trivial. A nonabelian requirement, applied to both alternatives
of the proposed word/character predicate, closes that loophole. The source
does not implement such a general predicate; it checks finite rank/length
populations and the already-known conditional formulas.

### Odd-prime conjugation is not an unconditional exclusion

For an irreducible Heisenberg sector with central scalar `zeta_p`, an
orientation-reversing move sends that scalar to `zeta_p^-1`. These are equal
only for p=2 among primes. The scalar argument is general; the code samples
p=2,3,5. Preserve the positive **single complex-linear fixed-sector** result.

The extra requirement that one irreducible sector be fixed, instead of
paired or transported, is essential. `rho_zeta direct-sum rho_zeta^-1` has
a character preserved when its two summands are exchanged. Alternatively,
for a clock/shift pair, Fourier transform composed with complex conjugation
implements the swap antiunitarily (choose the Fourier convention accordingly).
Neither option is excluded by the computed unequal traces of one summand.
The physical/register interpretation of these alternatives must be derived
or priced before calling p=2 forced by the foundational principle.

There is a concrete witness mismatch at p=2 as well: the code uses unscaled
clock/shift matrices `X2,Z2` with square `I` and determinant `-1`. They generate
the dihedral Pauli group, not the specified quaternion subgroup of `SU(2)`.
Multiplying by suitable `i` phases gives quaternion generators; this retains
the commutator sign but changes the full representation and move laws. The
p=2 comparison must test the actual Q8 witness, not only its shared central
trace. The separate explicit quaternion matrices earlier in the routine are
useful but are not consumed by this p-loop.

### Verification flags overstate the independent coverage

At `p000_pure_logic_bridge.py:728–735`, mutation cases 4,5,7,8 are literal
`True`. Case 3 rechecks that abelianization kills the commutator rather than
passing an erroneous carrier through an enforcing rejection routine. The
wrapper reports '8/8' and tests read that report. Other tests contain some
real controls, but that does not turn these four constants into executed
mutations or establish the advertised independent count.

At `:603–615`, the F3 transvection list is indexed by 80 nonzero vectors,
but `T_u=T_-u`, so it contains 40 distinct matrices. Checking those generators
can still establish invariance under the group they generate, including
their inverses, with an explicit generator argument. It is not an enumeration
of 80 distinct transvections. The F2 Arf decomposition `[6,10]` is unaffected.

## 5. The five debt closures: preserve the results, retain the unpaid duties

**Hypercharge kernel (P604).** The central-element proof gives an exact
cyclic kernel of order `6k` for the **supplied SM representation with charges
rescaled by k**. From the charged singlet `u^(6k)=1`; the down and lepton
equations force `z3=u^(2k)` and `z2=u^(3k)`, and all other equations follow.
Each of the 6k roots gives one element. This corrects B1221's bad table.
Main's P604 already names this correction; carrying it into the actual dated
addendum and citations remains distinct from recomputing it. It does not
derive the representation, kinetic normalization or a measured coupling.

**Quadratic trace field (P606).** A transitive Galois orbit has size 1 or 2;
that places no bound of 2 on module multiplicities. The direct-sum
counterexample is valid and already identified in main's P606. The new
specific code witness is reducible: its diagonal two-dimensional V has
`End(V^3)=M3(K) direct-sum M3(K)` over the stated splitting field, dimension
18, not the single dimension-9 commutant suggested at `:316–317`. Use a
one-dimensional V, or an actually absolutely irreducible V, for that extra
commutant claim. The headline correction survives either repair.

**Twist coincidences (P355).** The exact arithmetic enumeration distinguishes
full-lattice, half-period and other twist pairs. It does not calculate the
complete normalized physical spectra or prove that the complement has no
special Higgs coincidences. In particular the relay's 'd=e iff v_i=0' on
the half-lifts is too strong. Main already has the stronger reusable source
identity (B1832 T-HALF-LIFT): on order-10 points,

`Y_e(S)=lambda D Y_d(Sigma_10 S)^T D`,

where `Sigma_10` flips the QI coefficient and `|lambda|=1`. For the nonzero
pure direction `S=QI`, `Sigma_10 S=-S`; bilinearity in S gives
`Y_e(QI)=-lambda D Y_d(QI)^T D`, hence equal singular values even though
`v_i != 0`. A generic-Higgs sufficient condition is not an unconditional
iff statement for every Higgs. This countercontrol uses the existing
frame identity and does not claim an observationally viable Higgs vacuum.

B1832 also retains its scalar-Higgs qualifications and earlier retractions.
Reuse them before extending the result to every S. P355 still asks for a
precision off-identity construction and a definite amount of breaking;
an arithmetic list alone does not discharge those items.

**Theta duplication and zero laws (P262/P268/P292/P337).** The theta-product
route is useful and main's B1832 already derives the residue/sum-twist
structure. But the delivered new routine compares residues on 20 random
inputs, not the advertised full-u identity. It then uses Laurent-coefficient
moduli as a `D_proxy`; it does not compute the complete regularized norms.
The relay's 30-digit full-u error has no corresponding implemented mpmath
full-u control or preserved output in the changed files. Supply its source,
precision/truncation analysis and receipt; do not treat a missing control as
an identity refutation. At a zero residue the normalized expression `P/R`
also needs a limiting or unnormalized identity, not division by zero.

**P318/P618 as rows.** Their actual main entries contain additional dated
corrections and sweep obligations beyond McKay and WZW. No modifications to
those main documents are in the three commits. Accept precise sub-results
after review; do not mark the entire multi-item rows DONE from this bundle.

## 6. Required next actions and implications for our lane

1. Preserve the F1–F6 improvements, fix the new branched-cover conflation,
   and keep the complete physical transport duty visible.
2. Recover B997's mod-4 addendum in every cascade claim; distinguish modular
   shadows from the genuine SU2 normalizer and its lifted action.
3. State the bridge as a conditional theorem with explicit target/category,
   faithfulness and fixed-sector assumptions. Test paired and antiunitary
   alternatives before promoting exclusions to the whole architecture.
4. Replace literal mutation results with controls that actually exercise
   rejecting behavior. Count distinct matrices, tests and independent sources.
5. Reuse B1832's matrix identities and full physical norms for the spectral
   extension; supply an actual full-u check for the new advertised identity.
6. Carry only verified individual corrections to main, preserving historical
   wording and the remaining portions of each debt. Keep the scoreboard at
   zero newly confirmed physical parameters from this package.

For our own programme, these findings favour continuing the registered,
transported whole-family construction rather than choosing a convenient
component or confusing a trace invariant with the full physical operator.
Our new conditional Pin2/Dic5 spectrum and end analyses remain separate
author candidates, not validations supplied by AGY's results. The explicit
cover-line realization, physical weak-current overlaps and the derivation
of the transport/end law remain load-bearing work. No conclusion here
licenses combining incompatible carriers or counts.
