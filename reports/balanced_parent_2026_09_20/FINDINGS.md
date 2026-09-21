# F08: the balanced parent links the local tensor kernel to a global Codazzi problem

2026-09-20. Local branch `audit/fork-2026-09-20`. This checkpoint constructs
another complete classical background in the adopted parent and identifies
its possible matter profiles. It does not construct a chiral Standard Model
or derive the parent, spacetime, gravity or measured constants.

## The constructive result

Replace the earlier coefficient `Sym3(h)` by

    rho(g)=g tensor conjugate(g).

This is a different global rank-four representation, not an unchanged-
holonomy replacement inside a ball. In the SAME supplied hyperbolic metric
and SU4-in-E8 parent, it gives a smooth noncommuting solution of all complex
flatness and real moment equations. The bundle descends by explicitly unitary
transitions, and its positive Higgs norm is `6 Vol(M)` in the defining-four
trace. It is finite on every complete finite-volume quotient in scope.

Its compact unbroken gauge algebra is exactly **so(10)**: the actual
common-kernel calculations in the parent 4, 6 and traceless 15 leave no
extra generators. No fourth-root Wilson twist is needed for this reduction.
The representation factors through PSL2, so its definition does not depend
on the sign lift of geometric holonomy. Neither fact selects this bundle
physically or derives four-dimensional fermion spin data.

This uses the full noncommuting classical equations of the adopted gauge
sector, not the later commuting electrostatic truncation.
[Braun et al., equations 2.9--2.19 and 2.34--2.42](https://arxiv.org/html/1812.06072v2).
The E8 embedding and branching are reused from R38/R39; they are not
rediscovered or promoted to a derived theory of everything.

## The connection that the previous local picture concealed

In an explicit positive-orthonormal coefficient basis, the three Higgs
matrices are `N_i+N_i^T`, with `N_i=E_(0,i+1)`. Thus the degree-one
algebraic operator is **exactly four times F06's corrected center operator**,
not just another occurrence of its kernel dimension. Its spectrum is

    0 (5), 2 (3), 3 (4).

Unlike F06's local core, this homogeneous background has covariantly
parallel Higgs field, including both the unitary connection and the
Levi-Civita connection. Its full Laplacian is `Delta_A+H`, with both
terms nonnegative. This gives an actual global kernel dictionary:

    ordinary-L2 harmonic coefficient one-forms
    = complex L2 symmetric trace-free Codazzi tensors.

Here a Codazzi tensor satisfies `nabla_i b_kj=nabla_k b_ij`. Its divergence
vanishes by contraction. This is a differential equation and a global
normalizability condition; the five-dimensional pointwise kernel is NOT
five generations and NOT a four-dimensional graviton. The full proof
uses F02's complete-space domain and cutoff control.

There is a useful literature connection: the same Codazzi space appears
in a DIFFERENT hyperbolic gauge problem and in conformal deformation
theory. [Bera, Proposition 4.3 and section 4.2](https://arxiv.org/html/2408.01522v2).
Those results concern closed bases. Neither their action nor their compact
cohomology conclusions are substituted for this cusped physical operator.
The direct identification above is checked in this fork; no claim of
literature novelty is made.

This also guards a scope error: the symmetric-power vanishing used in R27
and F05 does not automatically apply to a coefficient involving conjugate
holonomy. [Menal-Ferrer--Porti's specified coefficients](https://arxiv.org/html/1001.2242v2)
are holomorphic symmetric powers. Conversely, the disappearance of their
strict algebraic bound here does NOT prove a zero eigenvalue or absence
of every other possible global gap.

## Two limits that were tested, not assumed away

**Cusp normalizability.** The entire zero-Fourier Codazzi sector has three
constant coefficients and grows as z or z^3 in the orthonormal frame.
The full squared-norm density per unit coordinate cusp area is

    (3/2)|c|^2 z^3 + (|d|^2/2+2|e|^2)/z.

Every nonzero such mode is non-L2. The producer derives the independent
Codazzi equations and verifies their general solution and norm. Higher
Fourier modes and their matching through the compact core are not excluded
or counted. We have NOT computed the global Codazzi dimension on m004,
m202, s959 or their covers. A constant tensor in the pointwise kernel is
explicitly checked to fail the differential equation.

**Mirror pairing.** In this frame C is real and preserves the unitary
bilinear map `J=diag(-1,1,1,1)`. J intertwines the untwisted coefficient
and dual physical operators, in the same form degree and on their complete
domains. The kinetic metric stays positive: J is not used as an indefinite
Hilbert norm.

An order-four scalar twist breaks this LINEAR global pairing, but does
not produce spectral chirality. The ANTIUNITARY map `v -> J conjugate(v)`
still intertwines the two sectors: conjugation inverts the unitary
character. Exact m004 matrices verify both the failed linear map and the
working antiunitary one. Thus the free spinor spectra remain paired,
whether their zero multiplicity is zero or nonzero. No Fredholm/index
claim is needed to establish this pairing. Arbitrary new representations,
nonmatched domains, additional fields and interacting phases are outside
this result.

## How this changes the research direction

| Construction | What it now provides | Matter conclusion in its stated domain |
|---|---|---|
| F05, twisted holomorphic Sym3 | Complete parent background, so(10), explicit strict gap | No ordinary-L2 charged zero modes. |
| F06, local isotropic core | Regular local full-parent solution and a pointwise tensor kernel | No global spectrum; fixed-holonomy regular gluing cannot create zeros by F07. |
| F08, balanced holonomy | Complete hyperbolic parent background, so(10), exact Codazzi dictionary | Global zero count not computed; full dual-sector pairing survives the scalar unitary twists. |

The useful positive is a concrete globally defined spectral problem that
genuinely changes F07's holonomy premise while reusing F06's verified
algebra. The limiting result is equally specific: merely replacing the
principal representation by this balanced one cannot yield an unpaired
free spectrum. Breaking a linear self-duality is still insufficient when
an antiunitary map remains.

The next chirality candidate should therefore identify what breaks BOTH
the actual linear and antiunitary intertwiners, and then solve the same
parent and end equations. A Codazzi calculation can establish matter
multiplicities or deformation data, but must not be sold as a chirality
mechanism by itself. Existing nonsplit/source and interacting mechanisms
remain different tasks, with their known domain, action and anomaly duties.

No physical parameter prediction, complete vacuum, global G2 geometry,
quantum anomaly completion or four-dimensional gravity follows. The full
TOE goal remains active and unachieved.

**Follow-through F09:** the [actual parent one-form vertex](../balanced_vertex_2026_09_20/FINDINGS.md)
now has an explicit cofactor map on these tensor profiles, with nonzero
and vanishing controls. The exterior-square coefficient has a strict
complete-L2 gap. The antiunitary pairing also relates the full normalized
wedge coupling tensors, so a selected-mediator asymmetry is not yet a
derived mirror hierarchy. This extends the interaction dictionary without
counting global modes or proving an interacting phase. The scientific
files and original F08 proof remain unchanged.

**Follow-through F10:** the [real-projective deformation calculation](../projective_escape_2026_09_21/FINDINGS.md)
identifies the geometric point of Ballas' known family with this balanced
coefficient by an actual simultaneous intertwiner. Away from that point,
the longitude forbids both invertible flat linear and antilinear dual
bundle maps, including on finite-cover pullbacks. Its changed cusp has
an explicit full-equation tail solution but necessarily infinite Higgs
norm in the fixed hyperbolic metric. Whole-core ordinary H1 dimensions
still agree; physical L2 multiplicities and a global vacuum are not
computed. This qualifies the candidate change, not F08's proved pairing
in its unchanged background. Frozen F08 science remains untouched.

## Verification and custody

- Four scientific files and both reused producers hashed before execution;
  science committed at `89be4ccf`.
- **19 new exact checks passed on the first run**, including the full
  equations, local-to-global tensor identity, real/bilinear representation
  maps, gauge commutants, failed-twist comparator and entire cusp zero sector.
- **123 unchanged F01-v2 through F07-v2 checks passed**, one optional GUI
  warning. Earlier retained failed versions are not erased or called green.
- All six new/reused scientific hashes are unchanged; F01--F07 directories
  were unchanged against `054bebb3` before living-report additions.

[Proof](PROOF.md), [design](DESIGN.md), [execution and reading receipt](RECHECKS.md).
Finite exact controls are not independent acceptance of the global analytic
arguments. No full-suite/gate certificate, new all-head retrieval, shared B
number, other-seat edit, push or external publication is claimed.
