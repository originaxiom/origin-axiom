# Report-guided second pass: reuse the results, correct the joins

2026-09-20. Branch `audit/fork-2026-09-20`. This is a second reading and
targeted recheck of the [whole-picture report](../whole_picture_audit_2026_09_20/AUDIT.md),
not twenty new discoveries, a new B arc, or a completed physical theory.

## Verdict

**The second pass was useful. Its most important correction is to our own
next-step wording: derive the physical admissibility condition before using
finite harmonic-map energy as an unavoidable physical requirement.** The
repository already contains the distinction needed to prevent that mistake.

It also supplies a reusable all-orders smoothness result, an existing coupled
source construction, sharper flavor/vacuum constraints, and specific examples
of corrected mathematics surviving beside obsolete prose. These strengthen
the original recommendation to test compatible mechanisms in one theory;
they change the order and precision of that work. They do not establish that
the framework is physically inevitable or that chirality has been completed.

## 1. Coverage and what these numbers mean

Fresh remote-head/tag retrieval succeeded; no branches were merged. The
completed [discovery receipt](discovery.json.gz) records **4,664 reachable
commits, 16,630 distinct tip blobs, and 31,209 searched non-NUL file versions**
(3,658,998,481 bytes; 16,478 at enumerated ref tips). It excludes 198
NUL-containing objects. The raised 32 MB limit excluded no object by size.

The first sweep searched 30,818 versions with an extension whitelist and a
5 MB ceiling. The new sweep removes that whitelist: shell heredocs,
extensionless files, tabular text and notebooks can now be searched. Changed
refs also contribute to the population difference; **391 extra versions is
not a count of missed scientific results**. Different search terms likewise
make hit-count comparisons unsuitable as discovery counts.

A concrete positive retrieval control succeeds: B1203's shell heredoc contains
`553/64` at line 11, blob `a090a7433bb7c6fae84a5f460d694fa27c1d12ca`.
The first extension filter excluded this file. It was read, not executed.
This recovers an already-known retrieval failure example, not new physics.

The 24 dictionaries target all 22 recommendations, F01's analytic hypotheses,
and that heredoc control. Literal matching is navigation, not semantic
absence proof. One historical pathname is kept per object; PDF/image contents
are not decoded, archives are not unpacked, and untracked/ignored/unreachable
work is not covered. A non-NUL byte stream is not necessarily readable text.
No claim of personally reading 31,209 files or verifying all history is made.

Important pins:

- Main: `987c0c8fdb07f7f79beccd6c82c1154e3e75fa47`.
- SM seat: `235325396b2db79c78df303531af6878931b00f2`.
- Other audit branch: `cc0484ea07d34e9ffdb680814842afe1270ef2a0`.
- This fork's input: `be669308089aa47e632e330bda58129a3184b8c5`.

The receipt also includes archived tags and retained tracking refs. They are
not all live seats. In particular, the other audit branch's reconciliation
is now committed at cc0484ea; its R39 drafts remain unexecuted there and were
not imported or executed here.

## 2. Substantive findings, in impact order

### A. Three different energy/norm questions were too easy to conflate

F01 proves a statement conditional on a smooth, source-free harmonic flat
bundle on a complete finite-volume base with **integral |Psi|^2 finite**.
Under those hypotheses the bundle splits. The exact nonsplit witness fails
that admissibility test. Nothing in this second pass refutes the proof or
its cohomological positive.

But [R28's proof](../physical_bridge_2026_09_05/SOURCE_ACTION_PROOF.md)
already distinguishes:

| Quantity | Question it answers |
|---|---|
| integral norm(Psi)^2 | F01's harmonic-metric/map energy condition |
| integral of curvature and moment-map residual squares | Static bulk potential in the adopted twisted gauge action |
| integral norm(partial_t phi)^2, with the action's coefficients | Whether a parameter variation is a normalizable 4D field |

These are not interchangeable. In R28's commuting source complement,
phi = u dF has zero static bulk potential while specified residue/end-data
variations have divergent kinetic norm. The exact tube calculation retains
the curvature and boundary terms that a rough-gradient shortcut would lose.
The source's action and kinetic terms were checked directly in
[Braun et al., (2.11)--(2.24), B.12](https://arxiv.org/html/1812.06072v2).
The R28 producer and tests were read; the unchanged R28/R29 suites pass
**44 tests** in this turn.

**Correction to the roadmap:** a source is not yet proved the only physically
allowed continuation of F01. First derive the norm, allowed asymptotics and
boundary variation law from the selected action. A fixed-asymptotic background
with infinite harmonic-map energy but an acceptable physical residual action
and normalizable fluctuations is a question to investigate, not a solution
we have constructed. R28's commuting example is not a global noncommuting
m010 counterexample. Nor does zero bulk potential establish acceptable
boundary flux, gravity/backreaction, a quantum measure or a 4D spectrum.

If the physical construction really requires F01's finite-energy class,
its source/boundary balance remains compulsory. If it does not, examine the
actual class rather than declaring it excluded by a theorem about another.

### B. The source does not have to be invented from scratch

[R29](../physical_bridge_2026_09_05/DEFECT_GAUGE.md) already varies an actual
charge-four tube field together with the gauge and Higgs fields. Its compact,
finite-width, added H theory has a stationary zero-residual construction.
Its source density is not held fixed during the field variation. This is
more than a prescribed Poisson right-hand side.

Reuse its construction and its limitations: tube locations, widths, weights,
amplitudes and coefficients are supplied; the full parent couplings are not
derived. Its thin-limit gauge-capacity result and the different fermion
domains remain. [R38](../physical_bridge_2026_09_05/PARENT_VERTEX.md) already
proposes testing actual parent one-forms in the full equations. Repeating
that proposal as a newly discovered source mechanism would be duplication.

There is also a terminology guard for F01. The obstruction to a source
`J = j Id` means **scalar on the particular coefficient bundle**. It is not
an obstruction to every abelian or Cartan-valued gauge current. Such a current
can act differently on different summands. Evaluate its actual representation
and pairing with the trace-free projector; do not decide this from its name.
R29 has not thereby been shown to balance F01's nonsplit extension.

### C. All-orders principal E6 smoothness is reusable prior work

The other audit branch's [smoothness reconciliation][smoothness] resolves a
conflict between older B274/R6 statements and L53's finite-order residual.
I read that note and checked the relevant primary theorem statements and
hypotheses rather than accepting its title.

For the principal geometric representation into **complex adjoint E6**,
the six adjoint summands give tangent dimension 6t for t torus cusps and
boundary restriction is injective. The source explicitly supplies the
centerless-group hypothesis and principal decomposition.
[Ishibashi--Mizuno, section 5.4--5.5](https://arxiv.org/html/2603.00816v2).

The dimension lower bound needs strong irreducibility and boundary
regularity, **not Zariski density in all of E6**. This is Theorem 5, not the
paper's narrower Theorem 1.
[Falbel--Guilloux, pp. 8--10](https://arxiv.org/pdf/1510.00567).
The tangent identification also needs goodness. A principal triple's
centralizer is the center: its regular semisimple element forces a
centralizer into a torus, and its simple-root components force every
simple-root character to be one. For adjoint E6 that centralizer is trivial.
[Sikora, Proposition 8 and Theorem 53(2)](https://arxiv.org/html/0902.2589v3).

Thus the source-based application in the existing note supports a smooth
6t-dimensional germ. **Do not restart an order-by-order obstruction hunt at
that already-covered point.** This is reuse, not our new theorem. It neither
classifies all components nor supplies six physical particles per cusp.
The geometric coefficient metric's non-L2 qualification is explicit in
[Menal-Ferrer--Porti, Theorem 0.3 and its underlying vanishing argument](https://arxiv.org/pdf/1001.2242v2).
The principal point also is not automatically an SM-preserving background.

Reading boundary: selected primary definitions/theorems and their nearby
arguments, not a fresh complete reading of all four papers or an independent
specialist review. Web PDF screenshot attempts failed; mathematical text was
available, including the unversioned Falbel--Guilloux PDF labelled v1.

### D. Flavor and vacuum consistency deserve earlier, specific checks

The first report named the hollow texture and neutrino duties, but its
summary underused the SM seat's stronger B1361/B1362/B1365 results.

For a complex symmetric hollow 3-by-3 matrix, the largest singular value
equals the sum of the other two. If M = M0 + E with M0 in that class, the
singular-value perturbation bound gives

    ||E||_op >= (m3 - m2 - m1)/3.

This is the existing B1362 analytic bound, not a new fit. Its numerical
search for near saturation is only an upper-bound search, not a proof of
global minimization. I read B1361/B1362 and the B1362 producer, but did not
rerun its random optimization. The physical reading needs the actual kinetic
normalization and the stated tree-level symmetry/Higgs placement; arbitrary
kinetic mixing cannot be assumed either absent or a free cure.

B1365 additionally identifies the same-sign singlet charges of its specific
three-27 design. With its displayed zero-FI D-term, SM-preserving singlet
VEVs cannot give a nonzero D-flat breaking direction. This constrains its
proposed neutrino and exotic-mass mechanisms. The findings and charge/D-term
code were inspected. Its full cohomology census, empirical mass limits and
broad claims about every possible FI/UV completion were **not** independently
verified here and are not adopted as universal exclusions.

**Roadmap change:** test the actual candidate's singlet charges, allowed
neutrino operators, Higgs/triplet masses and normalized flavor relations at
the first low-energy model checkpoint. Do not spend months obtaining a
chiral count before noticing that the same supplied action forbids the
needed vacuum. These are existing tests to reuse, not reasons to abandon
every E6 or nonsplit construction.

Pinned bodies: [B1361][texture], [B1362][hierarchy], [B1365][bulk].

### E. Some apparent chirality closures carry their own later scope repair

B1351's headline and section 2(ii) say that an acyclic whole torus forces
zero whatever its Morse partition. Its later addendum explicitly restricts
that implication to whole-torus/annular conventions: relative disc data are
a counterexample to the unrestricted wording. Read the addendum with the
headline. Its closed-manifold result is a different statement.

The [boundary-table audit](../physical_bridge_2026_09_05/BOUNDARY_TABLE_AUDIT_2026_09_16.md)
also already distinguishes the undrilled core Q from the source exterior C:
chi(Q)=0, chi(C)=-k, chi(E)=-2k, so chi(C,E)=k, not 2k. It retains the
conditional singular three/zero result and the resolved light pairs on
their different domains. I reread that argument; its old 32-test receipt
was not a new run in this turn.

**No universal closure is revived or revoked here.** The actionable guard is
to attach the pair, bundle, operator and end domain to every claim. Later
arguments that cite cusp-fixedness must carry the applicable convention;
the exact peripheral charge arithmetic in B1372 is not by itself a theorem
for every sourced boundary realization. [B1351][index3], [B1372][doublets].

### F. Correct tests can coexist with misleading live prose

Main's B1248 both rejects `det X0 = squarefree(2-kappa)` and, later in the
same file, calls that formula unaffected. Its test-module introductory
docstring still repeats the old formula. But the actual implementation and
counterexample test use the corrected integral formula

    det X0 = (2-kappa)/g^2,  g = gcd(entries of AM-MA).

The existing counterexample has 2-kappa=-121 and g=1: the primitive integral
realizer has determinant -121, whereas the squarefree shortcut returns -1.
Both selected unchanged correction tests pass (**2 tests**). The scoped
square-class statement over a field is not being retracted.

This is a confirmed documentation inconsistency, not a new mathematical
correction. The old first-pass synthesis remains useful, but a prose-only
sweep can still reverse a result that its executable checks protect.
[B1248][norm]. No other seat's report or scientific code was edited here.

B1421 independently documents this propagation problem on a much larger
population, including secondary results missed by headline summaries. Its
524-orphan figure is its historical inventory, not a fresh count certified
by this second pass. The findings and stored inventory were read. [B1421][completeness].

### G. Recover the scalar identity before asking for the spin-2 extension

Reading B8101 in full makes the gap precise: its tests check a proposed
function's required three-dimensional functional equation and critical-line
properties. Its own scope calls those necessary conditions. They do not
identify the actual operator on the m004 cover. For example, multiplying a
candidate by exp(c(s-1)), real c, preserves the functional equation and
unit modulus on Re(s)=1; these properties alone cannot fix the function.
This elementary observation is a scope check, not a computed alternative
scattering determinant.

**Follow-through correction, same date:** the paragraph above assesses B8101's
tests correctly, but the original version of this section failed to credit
its explicit antecedent, **B739**. B739 already contains a function-level
one-cusp pullback argument, not just those necessary conditions. Its full
findings and proof block were read, and its three unchanged locks pass. The
scalar identity must not be put back on the missing-work list merely because
a later check is weaker. [Detailed recovery and reading limits](SCATTERING_RECOVERY.md).

The remaining task in entry 20 is to identify the **spin-2/ghost/twisted**
operators and their scattering data, and assemble all terms in a common
regularization. B739 explicitly excludes forms and vector-valued bundles.
Neither it nor the three rerun locks complete that physical calculation.
B8133's evaluation-point question and B8142's acyclicity correction also
remain separate. No new scattering determinant was computed here.

## 3. Disposition of all 22 recommendations

This is a report-guided triage map, **not 22 freshly certified results**.
“Retain” means no supplied closure was established by these readings; it is
not a proof that no closure exists anywhere. Previous reading/reproduction
grades remain in the original report.

| # | Recommendation | Second-pass disposition |
|---|---|---|
| 1 | Nonsplit physical admissibility | **Reorder:** derive physical norm/end class first; keep F01's conditional theorem. |
| 2 | Parent/source origin | **Reuse:** R29 source construction and R38 proposal exist; test the actual representation-valued current and whole action. |
| 3 | Physical operator domain | **Advance, scoped:** F02 gives the unique ordinary-L2 closure for smooth complete backgrounds; singular-source domains and the actual spectrum still require their own analysis. |
| 4 | Interacting mirror gap | Retain common-model/R38 form-degree and full-coupling requirements; no new phase calculation. |
| 5 | Full anomaly including ends | Retain; a classical source solution does not discharge the quantum gate. |
| 6 | Usable 4D limit | Retain; separate allowed backgrounds, normalizable fluctuations and neutral spectral weight. |
| 7 | Arithmetic parent maps | Retain existing Chat1 correspondence/descent proposal; no new family action on physical states established. |
| 8 | Dynamical state selection | Retain; zero residual potential in R28/R29 does not select source number or asymptotic data. |
| 9 | Noncircular gauge selector | Retain B1430's conditional-embedding fence; no successor solving it was verified. |
| 10 | Chirality plus Higgs/exotics | **Strengthen early gate:** include B1365's charged-singlet/vacuum constraints alongside the doublet-triplet pincer. |
| 11 | Observable input quotient | Retain; background parameters need not be dynamical moduli, but can still be physical input data. |
| 12 | Falsifiable flavor | **Sharpen:** reuse B1362's perturbation bound and check normalization, not just tensor support. |
| 13 | Global ADE/G2 completion | **Remove duplicate subtask:** principal E6 smoothness is available; global geometry and physical metric remain different duties. |
| 14 | 4D gravitational dynamics | Retain; none of these recovered statements supplies the missing Lorentzian kinetic/coupling test. |
| 15 | Certified full 3D boundary index | Retain finite-box versus global-tail distinction; no new tail proof executed or verified. |
| 16 | Partial filling to quantum boundary observable | Retain the named certified witness; no need to reproduce withdrawn grid counts. |
| 17 | Physical quantum state space | Retain existing state-integral positives and the separate inner-product/gluing/time duties. |
| 18 | Thresholds with zero modes | Retain non-acyclic torsion machinery; do not revive the acyclic shortcut. |
| 19 | Physical tower scale | Retain need for a coarse-graining/observable map, not a relabeling of degree. |
| 20 | Cusped one-loop determinant | **Reuse B739:** scalar function-level transfer exists; derive the spin-2/ghost/twisted extension, not the scalar identity again. |
| 21 | Index mechanism classification | Reuse the other branch's exact higher-index recovery; avoid a duplicate unfinished census. |
| 22 | Laboratory discriminator | Retain the isospectral/localization distinction and readout duty; no experiment performed. |

## 4. Revised immediate work order

1. **Admissibility from one action.** Declare the bundle/parent, physical
   kinetic metric, allowed fixed end data and boundary variation law.
   Decide whether F01's L2 background condition really follows. This is a
   discriminator between two explicitly stated routes, not permission to
   choose a domain merely because it gives the wanted index.
2. **Reuse before extending.** Keep the principal smoothness theorem,
   nonsplit index witnesses, R29 coupled source and R38 action dictionary as
   separately scoped inputs. Solve the remaining compatibility problem, not
   those already-paid subproblems again.
3. **One-model checkpoint.** Compute its physical operator/domain and whole
   charged/neutral spectrum; check anomaly, singlet vacuum, flavor/neutrino
   operators and exotic masses together. Keep the finishable boundary-index
   certificate and laboratory readout as distinct deliverables, not evidence
   that the 4D theory has already passed.

## 5. Verification and custody

- **44 passed in 33.79 s:** unchanged R28 and R29 test files.
- **2 passed in 0.96 s:** unchanged B1248 correction tests.
- Commands, exit codes and reading boundaries: [RECHECKS.md](RECHECKS.md).
- Retrieval wrapper: [resweep.py](resweep.py); it reuses the expanded first
  scanner. The original discovery receipt was not overwritten.
- The whole-picture report and F01's living findings receive a dated scope
  clarification. Their frozen designs, proofs, scientific producers, seals
  and original failure records remain unchanged.

No new PDE solution, parent background, census, quantum gap or prediction was
produced. No full-suite/gate rerun or independent banking pass is claimed.
This is a local research checkpoint; the full physical goal remains open.

### Follow-through from this sweep

[F02](../complete_domain_2026_09_20/FINDINGS.md) records and checks the standard
complete-space fermion-domain argument under the adopted Hilbert metric.
Sixteen exact controls pass; unique self-adjoint closure is kept separate
from Fredholmness and chirality. R15's already-existing homogeneous through-
flux construction supplies the zero-static-potential/non-L2-background
control. No new nonsplit background is claimed. The B739 scalar-scattering
recovery above is an additional correction to this report itself.

[F03](../nonsplit_cusp_growth_2026_09_20/FINDINGS.md) and then
[F04](../full_flag_growth_2026_09_20/FINDINGS.md) pursue the infinite-energy
background question without silently reinstating finite energy. F03 tests
the rank-two construction; F04 uses the actual full rank-four invariant
flag, including metrics not induced from rank two. Both exclude controlled
angular-growth classes, while retaining rapidly angle-varying and coupled
source possibilities. F04's 20 exact controls and 42 unchanged antecedent
checks pass. This is a scoped background constraint, not a physical chiral
realization or a revision of the exact algebraic index.

[F05](../parent_twist_gap_2026_09_20/FINDINGS.md) receives R39's now-sealed
geometric background at available local Git pin `8d2cced2` and reruns its
16 tests unchanged. It constructs a global order-four central twist in
the same classical parent, retaining the local BPS equations and reducing
so(11) to so(10). Crucially, removal of the displayed global self-duality
does not restore charged matter: the actual coefficient Laplacian has an
explicit positive lower bound, so neither spinor sector has an ordinary-L2
zero mode in this background. Twenty-four new and 62 unchanged antecedent
checks pass. This quantitatively joins the existing geometric vanishing
mechanism to a physical operator; it is not a new universal no-go or a
result about the distinct nonsplit m010 bundle. The next discriminator is
a full-parent source or nongeometric background that changes the operator
enough to close its gap. Fresh fetches failed, so the received local pin
is not claimed to be the current head of every other seat.

[F06](../isotropic_parent_core_2026_09_20/FINDINGS.md) then solves R39's
isotropic-current differential equations in an explicit local conformal
metric, using parent one-form fields rather than importing the scalar
source action. This positive does not complete the hyperbolic problem:
its curvature is positive, its maximal extension is singular and no global
matching or chiral spectrum is established. The separately priced auxiliary
Einstein--harmonic-map identity is not derived four-dimensional gravity.
An incorrect initial pointwise-spectrum expectation is preserved along
with its post-failure correction; 19 corrected checks and 86 unchanged
antecedent checks pass. The new physical question is whether a justified
global geometry and full fields can contain such a core, not whether its
pointwise tensor kernel can be renamed particles.

[F07](../core_gluing_invariance_2026_09_20/FINDINGS.md) then joins F06's
matching proposal to F05's global complex and the already-banked R18/R30
bounded-homotopy mechanism. It changes the priority again: regular compact
ball replacements preserving exterior flat holonomy and equivalent positive
L2 norms cannot create exact matter zeros, irrespective of their fixed
size. The quantitative bound Delta_new >= (9/4)m/M does not transfer the
old pointwise Higgs bound; it uses the global contraction and the actual new
adjoint. Classical matching remains a geometry question, but not an exact
matter mechanism within those hypotheses. Changed end/domain/holonomy or
field data and light-mode degenerations retain their own tests. The first
symbolic comparison failure is preserved; 18 corrected controls and 105
unchanged antecedent checks pass. This is an authored analytic application,
not an independently certified global model or a fresh all-head sweep.

[smoothness]: https://github.com/originaxiom/origin-axiom/blob/cc0484ea07d34e9ffdb680814842afe1270ef2a0/reports/physical_bridge_2026_09_05/SMOOTHNESS_RECONCILIATION_2026_09_20.md
[texture]: https://github.com/originaxiom/origin-axiom/blob/235325396b2db79c78df303531af6878931b00f2/frontier/B1361_the_decks_texture/FINDINGS.md
[hierarchy]: https://github.com/originaxiom/origin-axiom/blob/235325396b2db79c78df303531af6878931b00f2/frontier/B1362_the_hierarchy_is_u1_breaking/FINDINGS.md
[bulk]: https://github.com/originaxiom/origin-axiom/blob/235325396b2db79c78df303531af6878931b00f2/frontier/B1365_the_bulk_of_the_line/FINDINGS.md
[index3]: https://github.com/originaxiom/origin-axiom/blob/235325396b2db79c78df303531af6878931b00f2/frontier/B1351_the_index_on_a_three_manifold/FINDINGS.md
[doublets]: https://github.com/originaxiom/origin-axiom/blob/235325396b2db79c78df303531af6878931b00f2/frontier/B1372_the_doublet_halves/FINDINGS.md
[norm]: https://github.com/originaxiom/origin-axiom/blob/987c0c8fdb07f7f79beccd6c82c1154e3e75fa47/frontier/B1248_norm_classification/FINDINGS.md
[completeness]: https://github.com/originaxiom/origin-axiom/blob/987c0c8fdb07f7f79beccd6c82c1154e3e75fa47/frontier/B1421_the_completeness_sweep/FINDINGS.md
