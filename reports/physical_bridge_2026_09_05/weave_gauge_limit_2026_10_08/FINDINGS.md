# Classical gauge convergence misses the quantum end response

For the supplied curved E8 parent and its fixed complete cusp domain,
the previously tested covariant inverse current is discontinuous in
the classical scalar graph norm. Compact gauge parameters approach
the normalizable constant gauge mode in that norm, but their ultraviolet
current response is zero while the constant mode can retain a nonzero
end response at nonzero flux.

This is a conditional analytic result supported by two exact computational
routes. It identifies an obligation for the local quantum completion;
it does not construct that completion or exclude every possible one.
The parameter-free Standard Model and full TOE remain unachieved.

## What was checked

The calculation starts from the actual four-Weyl mass map and its
physical kinetic metric, not a substituted Dirac model. Normalizing
that metric and reordering the target gives two Dz and two Dbar
principal slots. Every Q/R potential is off-diagonal between those
blocks. Its contribution to the traced local heat coefficient vanishes.

An arbitrary-matrix first-jet calculation and a separately authored
direct differential-operator calculation agree. The latter reconstructs
the second-order operator by acting on polynomials and verifies its
action on a further test vector. Omitting the kinetic normalization,
losing a physical slot, inserting a diagonal potential, or overlapping
the two cutoff shells is detected by the corresponding control.

The zero-potential virtual bundle is E_internal tensor (2S-1-S^2).
Both its rank and degree-two Chern character vanish. Combining this
curvature identity with the actual potential calculation yields a
vanishing leading compactly smeared internal supertrace, including
finite neutral condensates. This extends the local density check,
not a trace-class assertion on the entire noncompact cusp.

The analytic heat expansion is a framework input from
[Vassilevich equations 2.1–2.4, 4.26–4.27 and 7.30](https://arxiv.org/html/hep-th/0306138).
The expansion is used on each fixed compact support, with no uniform
large-support limit assumed. The finite symbolic tests do not certify
that analytic theorem or the earlier global cusp estimates.

## Why two valid limits give different answers

Let eta_R be a smooth compact cutoff of the gauge parameter, and let
chi_T be the separate cutoff used to define the operator trace.
For T beyond the support of eta_R, the propagator end insertion in
the finite-cutoff Ward identity vanishes exactly on the trace diagonal.
The remaining local heat contribution tends to zero as the ultraviolet
cutoff is removed. This holds for every fixed finite R.

For the internally constant parameter, the previous Ward calculation
instead retains an integral of the external heat insertion against
the derivative of the internal cusp supertrace. On the earlier gapped,
slowly varying external color probes it is nonzero for sufficiently
large finite external metric scale whenever flux is nonzero. There
is no claimed numerical threshold for that scale.

Thus, for this current B,

    lim_R B(eta_R alpha) = 0, but B(alpha) != 0

on those probes. The full charged roster is unchanged: the color
coefficient is -1 at n=1, -3 for n>=2, reverses for negative flux,
and vanishes at n=0. No exotic or conjugate was discarded.

Nevertheless the squared graph distance between eta_R and 1 decays
as exp(-R). The executable C1 cubic-transition control gives the exact
coefficient 2160-5868/e, including the cusp tail; the analytic argument
uses smooth transitions with uniform derivative bounds. End evaluation
is itself discontinuous in this classical norm.

The issue is therefore not a failed classical normalizability check.
Classical admission of the gauge mode is established; quantum continuity
in that topology is not available for this current.

## Consequence for the physics route

Compact-support gauge invariance cannot be promoted to invariance
under this normalizable constant transformation merely by citing its
classical cutoff approximation. A proposed local fermion Gaussian
must specify and test the end or reference state and its gauge action,
or establish an appropriate continuity and cancellation result.

The state pairing in
[Witten and Yonekura section 2.1](https://arxiv.org/html/1909.08775)
illustrates the need to retain the end factor. It is not an operator
map or an admitted regulator for this cusp. A compensating anomaly
coefficient alone would not supply that missing physical construction.

The previous polar-paired phase is defined for internally parallel
external fields. It does not yet define the compactly supported
internal gauge directions used here. The two prescriptions cannot
be identified without an extension and comparison.

This information-loss example concerns a specified function-space
completion. It is not an observer or qualia theorem. The foundational
act/register/lift question remains a separate derivation duty.

## Verification and scope

Scientific checks were executed on October8; publication follows on
October9, after midnight in the working timezone.

Seal ac781525ad886af8ce32e356e60f76acee913df7 was committed,
pushed and server-confirmed before any scientific import, execution
or test collection. First attempts passed without execution repairs:

- 18 native predicates and 8 separately authored reference predicates.
- 12 focused tests, including wrong-input controls and scope guards.
- 314 tests across nineteen related packets.
- Seven science files and 23 pinned-and-working dependencies unchanged.

The regression ran on a clean, unchanged seal commit. Literal outputs,
exit codes, timings and hashes are retained. These are same-author
checks, not outside analytic acceptance. The full repository suite
was not run. Governance still has 26 passes and four inherited failure
categories; this is a branch research checkpoint, not completed main
banking.

The latest fetched main was 377c17f21 and the SM branch remained
d62458221. Main's new outside-review report and amendment producer
were read, not independently replayed. They change no pinned operator
input. This lane retains the full parameter-free SM/TOE objective.

Nonzero-flux saddles, zero-flux nonnegative gauge minima, source/silver
positives and the broader generated architecture are preserved. Stable
physical families, a generated parent and measure, complete interactions,
normalized parameters, observer/qualia and gravity remain distinct duties.
