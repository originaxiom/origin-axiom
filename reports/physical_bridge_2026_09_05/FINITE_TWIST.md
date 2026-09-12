# R27: geometric zeros explained; an exact complex positive preserved

September 12, 2026. Path-local audit, no reserved B allocation.
Original seal dbb55201; observed-data follow-on seal 59e92302. Both
were pushed before their respective executions. Scientific files and
the original failed assertions remain unchanged.

## Result

Two different mathematical facts now survive independent checking.

1. For a nontrivial symmetric power of **complete geometric SL2(C)
   holonomy**, tensored with a finite-image coefficient system,
   restriction of ordinary H1 to the full boundary is injective.
   Thus B1297's interior-image dimension is zero for V and V*, not
   merely equal. This follows by a finite-cover application of the
   published Menal-Ferrer--Porti theorem; it does not require mirror
   symmetry, cusp-triviality, a Galois involution or a moving character.
2. The specified B1335 positive is real, and **it lifts exactly to
   Q(sqrt(-3)) with I=+1 and dual I=-1**. It is not merely a
   characteristic-13 artifact. However, the coefficient representation
   is **not completely reducible**. The received irreducibility filter
   misses a common invariant line with different generator eigenvalues.
   The two dimension equalities do not establish the original
   reductive-domain hypothesis. Its actual semisimplification has I=0.

Neither statement is the physical chirality theorem for the singular
source operator. R18/R19's conditional three/zero kernel and R26's
specified perturbation stability are unchanged. A stationary common
source/end action, anomaly completion and a physical low-energy limit
are still the declared next tasks. No complete TOE is established.

## 1. The smooth geometric theorem: what has actually been verified

Let Q be a compact core of a connected orientable complete finite-volume
nonelementary hyperbolic three-manifold M, with full boundary T. Let h
be a genuine lift of its complete geometric holonomy. For m>=1 and
finite-image F, set V=Sym^m(h) tensor F and

    n_Q(V) = dim im[H^1(Q,T;V) -> H^1(Q;V)]
           = dim ker[H^1(Q;V) -> H^1(T;V)].

The conclusion is n_Q(V)=n_Q(V*)=0, hence I_Q(V)=0. The compact core
is not a punctured source manifold with an additional mass potential.

The input is [Menal-Ferrer--Porti, Theorem 0.1](https://ir.library.osaka-u.ac.jp/repo/ouka/all/23151/ojm49_03_741.pdf),
with its explicit nontrivial-representation qualification. The full
arXiv paper was personally read, and the published theorem/proof were
compared. This is standard mathematics already used in B264/B445;
the claim here is its checked application, not rediscovery or a claim
that no other branch has used it. [Source/retrieval receipt](FINITE_TWIST_PRIOR.md).

Pass to the finite cover defined by ker F. The pulled-back representation
is a direct sum of nontrivial symmetric powers of that cover's own
complete geometric holonomy. Restriction is injective there. Summing
over sheets gives the local-coefficient identity tr p*=degree(p) id,
commuting with boundary restriction. Since the degree is invertible
over C, pullback is injective; the result descends. Apply the same
argument to V* using the global SL2 invariant pairing. Every lifted
cusp is included. [Complete argument](FINITE_TWIST_PROOF.md).

The executable mechanism checks recover the sl2 relations, the correct
monomial Hermitian metric, and strict positivity of the Bochner term
on one- and two-forms for powers 1 through 6 by exact principal minors.
The trivial power gives zero, as it must. Actual cellular circle-cover
pullback and trace commute with the differentials at degrees 1,2,3,4,6;
the coefficient-characteristic control rejects division by a vanishing
cover degree. These checks do not prove the infinite family by sampling:
that quantifier rests on the displayed proof and qualified primary theorem.

Finite direct sums retain zero I. Trivial geometric blocks tensored
with finite-image coefficients also have zero I by unitary conjugation,
but their individual n_Q need not vanish. The proof does not cover
arbitrary non-geometric E6/SL3 representations or every nonunitary
infinite-order character. In particular it does not validate B1334's
whole complex character-torus statement.

## 2. The positive: explicit matrices and exact characteristic-zero lift

SnapPy 3.3.2 exposed the target presentation and peripheral marking:

    pi1(m010) = <a,b | aabaBaaBab>,
    mu=AbAA, longitude=babA,
    triangulation isosig=dLQbccchhsj_Bbab.

Upper-case letters denote inverses. SnapPy supplies this combinatorial
input, not numerical ranks, the complex lift, a hyperbolicity certificate
or a physical index identification. The first producer independently
enumerated the specified target: the second of the first four honest
SL2(F13) representations, reached within 2,300 candidate pairs. That
is a selection receipt, not a census or a number of vacua.

The lift is particularly small. For u^2-u+1=0, take

    A = [[0,1],[-1,1]],
    B = [[0,u^2],[u,-2]],
    chi(a)=u, chi(b)=-1,
    V = Sym^3(rho) tensor chi.

Reduction u->4 modulo 13 gives exactly the received target matrices
and character (4,12). Choosing these small coefficients was informed
by the first output and registered before the lift computation; it is
not a unique reconstruction or a blind prediction. Both generators
have determinant one and the relator evaluates to +I. The character
obeys the relation and is trivial on both peripheral words.

The following dimensions hold **both over F13 and over Q(u)**:

| Coefficients | a0 | a1 | t0 | t1 | r1 | n=a1-r1 |
|---|---:|---:|---:|---:|---:|---:|
| V | 0 | 1 | 1 | 2 | 0 | 1 |
| V* | 0 | 2 | 1 | 2 | 2 | 0 |
| V semisimplified | 1 | 4 | 4 | 8 | 4 | 0 |
| Dual of the semisimplification | 1 | 4 | 4 | 8 | 4 | 0 |

Thus the original has I=+1, its dual -1, and the semisimplification zero.
All pair/torus/Euler identities and both dimension equalities hold.
The field extension Q(u)->C preserves these exact ranks, so this is a
complex example, without an SVD or tolerance inference.

The first producer derives cocycles with Fox blocks and independent
affine block-matrix multiplication. Modular ranks are cross-checked
against SymPy's finite-field implementation. The separate Sage producer
recomputes over F13 and the exact number field, using Fox blocks and a
right-to-left crossed-homomorphism recurrence. Each checks relators,
coboundaries, cusp commutation and the actual boundary cochain map
before reading n. Restriction ranks agree from a kernel basis and from
the stacked-rank formula, with its containment hypothesis checked.
Sources: [first producer](finite_twist.py),
[exact-ring follow-on](finite_twist_reductivity.py).

## 3. The domain error, not a reason to erase the positive

The vector (1,u) is a common eigenvector of A and B, with eigenvalues
u and -1. With P=[[1,0],[u,1]], the exact conjugates are

    P^-1 A P = [[u,1],[0,1-u]],
    P^-1 B P = [[-1,u^2],[0,-1]].

This is a reducible, nonsplit base representation, not complete
geometric holonomy. Its generated matrix algebra has dimension 3.
The symmetric-cube change of basis exhibits a full invariant flag
for V; its generated algebra has dimension 9, not 16. The ranks of
(V(b)-I)^j, j=1..4, are (3,2,1,0): one nontrivial length-four
unipotent Jordan block. Every one-dimensional composition factor
has b acting as 1. The full module cannot be their direct sum.

A separate linear-system certificate asks for a commuting projection
onto the first invariant line. Such a projection would give an invariant
complement. For the base module the equation/augmented ranks are 2/3;
for V they are 3/4. Neither system is consistent, over either field.
The same instrument recovers a complemented line in a diagonal
semisimple module and the full dimension-four algebra for an irreducible
two-dimensional control. Reducibility is not being equated with
nonsemisimplicity without this discriminating test.

The [received prime-scan filter](https://github.com/originaxiom/origin-axiom/blob/c83b6b802ee0e610a50ee07426ed610c2c6bd674/frontier/B1335_the_vanishing_is_not_formal_exhibited/verification/primescan.py)
tests whether every generator has a common vector with the **same**
eigenvalue lambda. An invariant line can have a different eigenvalue
for each generator; here those are 4 and 12 over F13. The filter
accepts this target although its common line is explicit. The later
tests a0=a0* and t0=t0* do not recover the omitted reductivity check.
This invalidates that claimed domain certificate, not every raw census
number or every representation it sampled. No corrected census is
claimed in this round.

B1297's original D sentence requires a reductive representation; the
dimension equalities are consequences, not an equivalent definition.
In characteristic zero this lift fails complete reducibility, so it
does not exhibit a nonzero index inside that original domain. If a
later D is intentionally weakened to just the equalities and the
peripheral condition, the example belongs to that weaker class even
over C. The change of definition must be explicit.

## 4. Two further positives that survive stricter verification

**Non-self-duality is genuine.** The first producer has a generator
trace obstruction: tr V(a)=9, tr V*(a)=3 over F13. The exact-ring
calculation finds a one-dimensional Hom(V,V*) spanned by a rank-three
matrix. Its determinant is zero, so no nonzero element is an isomorphism.
This corrects the author's too-strong initial expectation Hom=0 without
discarding non-self-duality. Literal inequality with an inverse transpose
is not a test for isomorphism; a separate SL2 control demonstrates that.

**One-sided isotropy is insufficient.** Using the actual invariant
Sym^3 boundary pairing and both transport factors, the finite-field
restriction image for V is zero and hence isotropic. The dual image
has Gram matrix [[0,3],[3,0]], rank two. The form descends modulo
boundary coboundaries. This independently reproduces the particular
two-sided-isotropy correction, not its reported multi-manifold census
or a universal vanishing proof.

There is also a direct corollary of the displayed invariant flag:
V and its semisimplification have **the same trace on every group
word**, although their n and I differ. For upper-triangular invertible
matrices, taking the diagonal commutes with multiplication and inversion;
the trace is the sum of these diagonal characters. This proves the
all-word statement, not a finite word sample. Thus this index cannot
be recovered from word-trace characters alone on a class that includes
such nonsemisimple representations. This is a precise example of
extension data being lost by passage to the semisimplification, not a
new physical particle spectrum or an object-selection principle.

## 5. The B1334 rank step and the geometric theorem remain separate

For J(t)=[t-1,0] and F=[1,0], with t in C*, rank F is always one.
But rank(F restricted to ker J) is zero at t=2 and one at t=1.
Polynomial entries alone therefore do not justify the asserted lower
semicontinuity of a map after choosing a parameter-dependent kernel.
This is an exact algebraic control of the inference, **not** a
three-manifold counterexample satisfying all of B1334's hypotheses.
The global self-duality and reductivity obligations in the original
argument also remain distinct from boundary self-duality.

The finite-cover theorem bypasses those steps for genuine geometric
symmetric powers with finite twists. It does not prove the stronger
claim for all complex points of a character torus. Conversely the new
nonsemisimple complex positive is not a counterexample to that geometric
theorem. Its base holonomy preserves a line and is not the complete
nonelementary geometric holonomy required by the primary theorem.

## 6. Physical lesson and retained next work

Repeated zero calculations in the declared smooth geometric finite-twist
class now have a structural explanation. Continuing that same class
while only changing the cover, its handedness or a finite character
does not evade this theorem. This is not a theorem about arbitrary
representations, singular sources, partial-filling boundary levels,
or a sourced Dirac operator with a real mass and a different domain.

The exact complex positive identifies extension data as mathematically
capable of changing the relative-image index. It does not prove those
data satisfy an admissible harmonic metric, the field equations,
finite action, physical boundary laws or the four-dimensional fermion
dictionary. Those are discriminating questions, not grounds to discard
the example or to promote it directly into physics.

For the retained R18--R26 source path the next milestone remains one
source/end action producing the background, allowed gauge transformations,
stationary solution, full mode spectrum and anomaly response together.
Any proposed nonabelian/extension-data transfer must explicitly map its
operator and ends into that calculation. The ordinary trace character
alone is insufficient. Source activation/selection, the neutral 4D
limit, gravity and empirical prediction duties are not discharged.

## 7. Verification, failures and custody

The original run deliberately remains a failed run: its arithmetic
positive and geometric controls passed, but the author's expected
irreducibility and zero-dimensional Hom were false. The correct
disposition is the nonsplit flag and singular rank-three intertwiner
proved by the separately sealed follow-on. Neither old assertion was
silently rewritten, deleted or marked xfail.

- Original native: exit 1, 14.222525 seconds,
  [complete first output](FINITE_TWIST_NATIVE_FIRST.txt).
- Original focused group including R26: 33 passed, 2 failed, one
  optional-GUI warning in 74.68 seconds,
  [first test receipt](FINITE_TWIST_FOCUSED_FIRST.txt).
- Follow-on native: exit 0, 4.623542 seconds, Sage 10.7,
  [complete exact output](FINITE_TWIST_REDUCTIVITY_FIRST.txt).
- Follow-on tests: all 10 pass in 3.15 seconds,
  [first test receipt](FINITE_TWIST_REDUCTIVITY_TESTS_FIRST.txt).
- Broad: the prior 47 files plus both new files, 384 passed, 16 failed,
  8 errors, one warning in 364.80 seconds; exit 1. The FAILED/ERROR
  set contains all 22 R26 IDs plus exactly the two disclosed author
  assertions. None of the old IDs disappeared.
  [Complete regression](FINITE_TWIST_REGRESSION.txt).

The raw native follow-on SHA-256 is
9213103c2a903bbb3d9f1c141aaaa7a9567d4c2ec52202ca7916483287364993;
the raw broad SHA-256 is
31a58be5f3b8ec4c5c1c21fb22ca3f2531d548e1aa2e82df0b8266ab5cb6191e.
Raw originals and exit receipts remain in the supplied local data area;
public transcripts redact environment prefixes only. Raw trailing
whitespace is retained. No scientific file changed during any run.

This is an authored proof/application and exact computational audit,
not an independent banking review, a full-green repository certificate,
a new physical prediction, or a complete TOE. The frozen designs and
proof have their final disposition in this report; their original
pre-execution wording is retained as historical custody.

The [reporting checks](FINITE_TWIST_FINAL_CHECKS.txt) give 27 passing
gates and exactly the three prior failing gate details, unchanged.
All 61 seals and the 364-entry pre-receipt manifest match; all 203
checked local links resolve. No gate exemption or baseline change was
made. The reporting receipt is added afterward and separately hashed.
