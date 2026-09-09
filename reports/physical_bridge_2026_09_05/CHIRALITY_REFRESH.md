# Chirality after the all-seat refresh — 2026-09-09

## Verdict

There IS a conditional chiral construction on this branch: in the
prescribed sourced m202 model, R18 gives normalizable degree-one
counts four/one, R19 gives three/zero away from its exact exceptional
holonomy locus, and R20 supplies a compatible nontrivial C3 orbit.
R23 maps its actual operator to a mass-inflow operator and computes
normalized local anomaly transport. These results must not be lost.

There is NOT yet a source-selected, globally anomaly-consistent physical
three-generation theory. The work did not fail to obtain a nonzero
chiral kernel; it has reached the harder join between that kernel,
its physical source/domain law and its quantum boundary completion.
The full TOE remains unachieved. This review does not change that goal
or abandon the sourced path.

This is a documentary cross-seat audit, not a new B arc or a new
numerical proof. It records source checks and scope corrections.
The latest new computations are R23's separately sealed calculations.

## 1. What was fetched and actually read

All nine remote branch heads and tags were fetched without merging.
[The snapshot](CHIRALITY_REFRESH_HEADS.json) pins each head. Main advanced
to b94ed03a; SM to 1703c0d8; outside is 26864394; physics remains
659487bb. The numbered audit seat is unchanged at f7a49536.
The other older heads were fetched too, not silently discarded.

Read for this review:

- Main's new C47--C54 theorem-ledger entries, B1322's complete findings,
  B1324's complete findings, and the new verification-package report.
  The package reports its own seal pass; that is not an independent
  physics proof or a rerun of all its locks here.
- SM B1351, B1354 and B1355 complete findings; B1355's complete producer,
  test and committed output; the current cross-seat relay rows.
  Earlier inputs remain pinned in R23's prior sweep.
- Outside memos 188 and 189 complete, including 188's correction;
  memo 189's producer and main's actual freshness-selector source.
  Memos 185--187 were routed by their introductions, the relevant
  closing addendum and commit file lists; their knot computations were
  NOT independently rerun or used to decide physical chirality.
- The existing R18/R19 analytic comparison, character complex and
  anomaly arguments were re-read, not inferred from test counts.
- The primary Acharya--Witten and Witten sections cited below.

Pinned received sources: [SM B1355](https://github.com/originaxiom/origin-axiom/blob/1703c0d80b6ad4281de61feb882667515500e8e7/frontier/B1355_the_e7_point_made_explicit/FINDINGS.md),
[SM B1354](https://github.com/originaxiom/origin-axiom/blob/1703c0d80b6ad4281de61feb882667515500e8e7/frontier/B1354_the_maximal_persistence/FINDINGS.md),
[SM B1351](https://github.com/originaxiom/origin-axiom/blob/1703c0d80b6ad4281de61feb882667515500e8e7/frontier/B1351_the_index_on_a_three_manifold/FINDINGS.md),
[main B1324](https://github.com/originaxiom/origin-axiom/blob/b94ed03aecba8aae3afc62504e22ec664c26e94f/frontier/B1324_arc_b_and_the_dictionary/FINDINGS.md).

The held main-to-SM range relay was read again. B1300--B1319 and
B1350--B1399 are reserved to that seat; this audit takes NO B number.
Freshness is a timestamped snapshot, not a promise that another seat
cannot push again while it is being reviewed.

## 2. The constructions are not interchangeable

| Construction | What survives | What does not follow |
|---|---|---|
| Named partial filling | Interval-certified hyperbolic geometry, two complete cusps, CS outside the mirror-compatible classes | Chiral matter, a quantized quantum sector or a selected filling |
| Smooth closed Wilson-line closings | Real representation/cohomology results, including the banked SM-shaped sectors | A net chiral spectrum in those paired closed sectors |
| Unsourced smooth cusp with annular sign partition | Zero relative Euler contribution in that stated partition | Zero for every singular source, every partition or every operator |
| R18--R20 sourced m202, specified strong maximal domain | Four/one, or three/zero at the allowed nonexceptional characters | Physical selection of three sources, amplitudes, parent and boundary data |
| R21 enlarged subgroup EFT | Consistent added-field anomaly completion with explicit mass terms | Those added fields being the modes of the unchanged source operator |
| R23 same-operator local inflow | Actual mass map, unit signed response, full eigenbundle normalization | A global singular determinant, end sector or cancellation of the gauge-zero-mode anomaly |
| Received B1355 curved cone | A concrete candidate in a different local geometric class | An identified E7 unfolding, one 27 per apex, three selected apexes or a compact completion |

The sourced construction's fermions are Spin(10) spinors from an E6
adjoint. B1355 discusses E6-charged 27s and an E7 enhancement. Matching
the name E6 in the two stories does not make their gauge sectors equal.

## 3. Why the sourced model still needs completion

In R19's charge normalization, the net-three spinors have

    Tr(u) = 48,  Tr(u^3) = 48,  Spin(10)^2-u = 6.

These are anomalies of the extra U1, NOT a failure of SM hypercharge.
Removing the extra vectorlike pair does not change them. The commuting
constant U1 gauge mode is normalizable in this finite-volume model,
so it cannot be treated as a nondynamical local-cone symmetry by habit.

R22 tests the obvious completion join: the same scalar source makes
negative-charge spectator vectors emerge with the opposite chirality
from the one R21's cancellation needs. In the common-sign strong-source
class the chiral asymmetry follows the sign of the charge, so adding
such charged pairs reinforces the abelian anomaly traces. Opposite
source responses and more general coupled fields were not excluded.

R23 then derives the local response rather than appending a counterterm
by name. It cancels local defect anomalies for supported gauge variations,
but Stokes retains the complete outer boundary. For an internally
constant gauge parameter the bulk variation is zero and the net anomaly
remains at that boundary. The higher eigenbundle terms fix a separate
normalization issue, not this boundary balance.

This is a concrete, scoped obstruction to a shortcut. It is NOT a
universal no-go against chirality, inflow, a massive U1, defects or
nonabelian source dynamics. It also does not erase the computed kernel.
See [R19](HOLONOMY_SPECTRUM.md), [R22](GEOMETRIC_COMPLETION.md) and
[R23](MASS_INFLOW.md).

## 4. Corrections the new intake requires

### 4.1 The source does not require curved gauge transport

The SM relay at 1703c0d8 correctly registers R15--R22 but explains
their distinction by saying that a source curves the connection.
That is not this construction: F_A=0 and [A,phi]=0 on the smooth source
complement; phi=u dF is singular. The changed source/domain data, not
nonzero gauge curvature, distinguish its cohomology problem.
R19 section 5 states this explicitly; R22 checks that actually curving
A would invalidate the unchanged cochain differential.

### 4.2 Whole-torus acyclicity does not decide every relative partition

B1351 section 2(ii) concludes from H*(T2;L)=0 that the index vanishes
whatever the Morse partition. R23's exact solid-torus/disc restriction
cone disproves that algebraic implication. For k contractible boundary
discs and nontrivial longitude character, whole-space and whole-torus
cohomology vanish but relative H1 has dimension k.
Essential-annulus controls give zero.

This does NOT construct a physically selected disc partition of the
actual smooth cusp or contradict the scoped closed-space result. It
prevents an over-wide algebraic exclusion from killing a different
boundary problem.

### 4.3 Finite deformation evidence retains its actual quantifiers

B1322's four banked complex points are valuable high-precision
independent checks, not an exhaustive proof over a germ by themselves.
B1354 is stronger in a different direction: exact reductions through
order eight, at two primes, exhibit tuned persistence and vanishing
tested self-duality defects. Its OWN caveats say that lower coefficients
were specialized, all branches were not classified, no all-orders
self-duality theorem was proved, and the complex tuned realization
was abandoned. Those caveats govern the stronger headline.

Retain these positive and negative calculations at their proved scope.
Neither their bounded evidence nor this review establishes the opposite
claim that a missing chiral branch exists.

### 4.4 B1355's curved candidate survives; its exclusions and physics need narrowing

Acharya--Witten section 2.3 explicitly gives the general Kronheimer
quotient construction, including G=E6 with enhanced E7. Therefore
B1355's finite centralizer on H/2T obstructs that restricted substitution,
not the entire hyperkahler-U1 family. Its A-type-only conclusion is
too broad. Section 3 describes a different twistor construction and
distinguishes metric control from spectrum control. Their one-multiplet
calculation needs the corresponding nondegenerate unfolding; no map
identifying CP3/2T with that E7 unfolding is supplied in B1355.
The cone's additional A1 locus and unresolved higher-isotropy rays
must remain in its spectrum problem.
[Acharya--Witten, sections 2.3 and 3](https://arxiv.org/pdf/hep-th/0109152).

Witten's mixed-anomaly argument explicitly applies to all ADE groups,
so that part of B1355 is supported directly, not merely an analogy
from SU(N). Nonzero pairing requires an anomaly-carrying sector; it
does not identify its representation or multiplicity. Equation (3.14)
gives a global sum rule for forms extending over the excised compact
space. A local link class is not automatically such a global class.
Footnote 4 explicitly leaves the integral lattice and global gauge form
unanalyzed. The U(N) example does not by itself derive an E6 quotient.
[Witten, (3.11)--(3.14), footnote 4](https://arxiv.org/pdf/hep-th/0108165).

Consequently (E6 x U1)/Z3 is a candidate compatible with appropriately
charged 27s, not a global form computed from this cone's charge lattice.
It is also not literally our E6/Z3 parent: it has an additional Lie
algebra direction. Relating the constructions requires the actual
C-field and integral lattice, not renaming one group as the other.

B1355's compact sum-rule constraint is useful: three equally charged
apexes and an invariant single harmonic form cannot give a nonzero
total inflow on a compact closing without further contributions.
Nontrivial action on a larger global two-form space is a live design
option, not an already constructed three-apex compact G2 manifold.

### 4.5 Other seats add openings, not a new universal zero

Main B1324 reports 66 chiral covers in its fixed 87-cover enumeration,
including 54 multi-cusped ones whose index it leaves open. Its
orientation-aware computation is new positive received evidence; it
was NOT interval-recertified here. Geometric chirality can coexist
with CS=0: vanishing CS is not a test proving amphichirality. This
keeps the cover route and our certified partial-filling witness in
their distinct roles. No numerical cover census is a matter spectrum.

Outside memo 189 correctly identifies a narrow literal filename
selector; main still uses it. Its quoted coverage totals are from
the tree the producer actually reads, not automatically today's main.
Likewise the memo's old progress-log cutoff is not the cutoff on this
branch or fetched main. There is an additional safety issue in main's
selector runner: the timeout handler continues before restoration;
snapshot restoration is not in a finally block. Thus its advertised
non-mutation is not guaranteed on that path. Do not run that mutating
sweep on the working evidence tree as a casual verification step.
This review records the source-level issue; it does not change main's
checker or claim its hidden instruments are stale.

## 5. Strategy that preserves the progress

First stay on the sourced path and compute its actual GLOBAL mass-map
and end response. R23's local normalization is now available; R15--R19
supply the geometry, domain and kernel to test it against. Do not simply
postulate three isolated zeros. Track source tubes, cusp faces and
rounded seams together, with the covariant angular form.

Then construct a physical end/relative sector or a massive-U1 mechanism
in the SAME theory, including allowed gauge transformations, integral
coefficients and the rechecked charged spectrum. R22 shows why an
arbitrary anomaly-cancelling field list does not discharge this task.

For the curved route, keep B1355 as a candidate and restore the general
E7-to-E6 unfolding route it over-excluded. The next comparison is an
actual local singularity/unfolding and spectrum map, including its A1
sector; only then ask for three globally compatible apexes and the
extending C-field lattice. This is a complementary lead, not a reason
to discard the existing sourced calculation.

Source selection, Spin(10)-to-SM breaking, a controlled neutral-sector
4D limit, common gravity and discriminating observables remain separate
duties. A full TOE has not been obtained.

## 6. Preserved work and verification grade

R23 is pushed at 9ff4de85, with both pre-execution seals and complete
first-run receipts. Its 24 new tests pass; the expanded focused selection
is 93 passed. The 43-file regression is 309 passed, 13 failed, 8 errors,
with the SAME 21 old failed/error IDs as R22. All 288 then-indexed latest
artifact digests match. Reporting gates remain 27 PASS / 3 FAIL on old
attribution, vacuity and marker debts. This is not full-repository green
or independent analytic proof review.

No upstream proof, old negative, B number or sealed scientific source
is edited by this intake review. Public source references are pinned;
the present review and its own checkpoint are added, not substituted
for old evidence.
