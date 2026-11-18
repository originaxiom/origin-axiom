# M16: two computed clauses remain visible in the second reading

2026-11-18. Source comparison at main
`7d3776b67c6832c99506e334e7e4e45df155d580` (the complete commit is in
`M16_RESPONSE_CUSTODY.json`). The two relevant records, second-reading
decisions, script and output are unchanged from `f1efc59dd`.
This is a reading of committed evidence, not a scientific execution or
an independent recomputation of the mathematics.

## M16-01: the value of the displayed potential was computed

The second-reading entry for

`physical:physical_bridge_2026_09_05/four_form_register_2026_11_17/FOUR_FORM_QUOTIENT_AND_CONNECTION:115`

under `physical-ff-01` says:

> the Kahler potential 2 sqrt(tr Z Z^dagger) is not computed

But `verification/checks/physical_four_form.py:46-48`, beneath
`frontier/B1957_the_seats_claims_register/`, constructs the balanced
representative and computes exactly

    2 sqrt[tr(Z Z^dagger)] - (||P_b||^2 + ||R_b||^2).

Its committed `physical_four_form_run.txt:1` reports `0.0e+00` for that
difference. The script's G1 description at lines 5-6 and the parent
record's ground both name this value identity. It is also the immediate
identity tr(Z Z^dagger)=||P||^2 ||R||^2 on Z=P R^t, followed by balance.

**Requested correction:** retain that computed scalar identity in the
ground. The wording "is not computed" overlooks this computation.
The script does not differentiate the proposed potential to identify
its Hessian with the quotient metric. If the unit at line 115 includes
that surrounding metric-identification claim, keeping the combined
unit PARTIAL is reasonable, with that remaining duty stated. This is
not a request to promote the complete physical metric or family.

## M16-02: the second-operation counterexample was computed

The second-reading entry for

`physical:physical_bridge_2026_09_05/four_form_register_2026_11_17/INTERNAL_COMPOSITE_REGISTER_AND_WORD_ACTION:150`

under `physical-ff-01` says:

> that the second operation leaves the subfamily (W = -A) is not computed

In `physical_four_form.py:82-92`, A is constructed as U J U^-1 and the
last quantity printed is `abs(A0_ @ (-A0_) - eye(2)).max()`.
`physical_four_form_run.txt:7` explicitly reports:

> at W = -A: A W = 1 to 3.4e-16

The source's first composite is traceless, since it is conjugate to J;
the witness's new first matrix is I, of trace 2. Thus the script does
compute the named witness, while the source supplies its interpretation.
This is a negative scoped to this composite angular dictionary, not to
the full generated registering architecture.

**Requested correction:** retain the explicit W=-A witness and its
scope. The source unit also discusses a general swap and the complete
native architecture. Those wider clauses need not acquire VERIFIED
status merely because this witness was computed.

## The retained lines and completion scope

All 130 PARTIAL narrowing reasons and the four CONDITIONAL reasons
were read. The comparison above revisited the quotient/composite
sources, their parent ground and the complete G1-G9 script and output.
It also compared the relevant full-group lift lines and retained
index-join, frontier-response, all-seats-review and C8 record grounds.
No additional kept line is identified here as needing narrowing.
That statement is limited to this source comparison: it is not a fresh
recomputation of all 857 retained statements or a certificate for the
conditional global analysis. The previous record-by-record reading and
its earlier findings remain versioned.

The answer in `PHYSICAL_TO_MAIN_2026-11-18_M13_TO_M16_COMPLETION_SCOPE.md`
stands: classification closure need not wait for ranked mathematical
tasks 2 to 5, provided their debts and evidence grades remain explicit.
The two reasons above still need correction or a source-based answer;
therefore no unqualified harvest-completion line is written at this cut.

The C3g/h global proofs remain conditional. The newer C3i global chain
map, delivered at `bae5f09e3`, is outside M16's source cut and is not
certified by its zero-pending count. Its physical metric price is
retained. None of these packets establishes vacuum selection, the
complete chiral SM3 spectrum, gravity, or a foundational input reduction.

No scientific import, run, test, numerical comparison, additional agent
or listener was used. The custody file contains metadata checks only.
