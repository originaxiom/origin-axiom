# Auditor Guide

Status: navigation guide. It does not replace the governed ledgers.

## Fastest Audit Route

Read in this order:

1. `GOVERNANCE.md`
2. `CLAIMS.md`
3. `papers/REVIEWABILITY_INDEX.md`
4. `papers/FALSIFIABILITY_MATRIX.md`
5. `papers/VALIDATION_WORKFLOW.md`
6. `docs/UNIQUENESS_THEOREM.md`
7. `docs/SESSION3_SYNTHESIS.md`
8. `frontier/README.md`
9. `frontier/B25_fibonacci_spectrum_anchor/FINDINGS.md`
10. `frontier/B26_lambda1_derivation_attempt/FINDINGS.md`
11. `frontier/B32_selector_axiom_audit/FINDINGS.md`
12. `frontier/B47_s1_verdict_ledger/FINDINGS.md`
13. `docs/TRACE_SELECTOR_THEOREM.md`
14. `frontier/B37_operational_feedback_quarantine/FINDINGS.md`
15. `docs/atlas/RESEARCH_TREE.md`
16. `docs/atlas/FAILURE_ATLAS.md`
17. `REPRODUCIBILITY.md`

Then run:

```bash
python -m pytest -q
```

## If You Know No Physics

Start with:

1. `docs/atlas/RESEARCH_TREE.md`
2. `docs/atlas/GLOSSARY.md`
3. `docs/atlas/FAILURE_ATLAS.md`

The key distinction is simple: exact mathematical consequences are not the same
thing as physical claims. The project is strict about that boundary.

## If You Are Checking The Mathematics

Start with:

1. `docs/UNIQUENESS_THEOREM.md`
2. `tests/test_uniqueness_theorem.py`
3. `CLAIMS.md`

The main thing to inspect is the conditional theorem:

```text
minimal-record axioms -> A = LR, up to order -> P1-P16
```

The next conditional theorem to inspect is:

```text
T1 -> S1 -> I=1/4 -> lambda/h=1
```

The useful check is whether the hypotheses are stated minimally, whether the
torsion and mapping-torus facts are fully justified, whether T1 is a
standard/natural tangent-filter inheritance principle or an inserted axiom, and
whether the downstream connections are presented as known mathematics or
project-specific packaging.

For a compact handoff, start with `papers/REVIEWABILITY_INDEX.md`, then use
`papers/FALSIFIABILITY_MATRIX.md` to identify the missing object and the
kill/rescope condition. Record actionable findings in
`papers/VALIDATION_LEDGER.md`; do not change claim status until a finding is
triaged and linked to a commit or PR.

## If You Are Checking Physics-Like Language

Start with:

1. `CLAIMS.md`
2. `docs/SESSION3_SYNTHESIS.md`
3. `frontier/`
4. `paths/`

The current physics posture is conservative:

- Derived potential: exact as mathematics about `A`.
- Field-theory lift: frontier, because kinetic term and carrier are additional
  choices.
- Particle, gauge, cosmology, and observable bridges: open unless a specific
  probe states otherwise.
- Fibonacci spectrum at dimensionless `lambda/h=1`: finite-approximant anchor,
  not a prediction. `docs/TRACE_SELECTOR_THEOREM.md` shows that T1 implies S1
  and selects `I=1/4`, but T1 itself remains motivated rather than derived.

The most valuable check is a precise statement of which inserted object is
unavoidable and whether any bridge can be made falsifiable.

## If You Are Reproducing The Work

Use this order:

1. Run the full test suite.
2. Run the specific probe or test named by the page you are reading.
3. Compare the output to the stated verdict.
4. Check whether the result was promoted, held as frontier, or archived as dead.

The intended workflow is:

```text
public sentence
  -> atlas node
  -> governed ledger or probe
  -> code path
  -> local command
  -> reproduced output
  -> verdict
```

## What To Trust First

Trust in this order:

1. Tests and exact algebra.
2. Governed claim ledger.
3. Probe findings with bounded verdicts.
4. Atlas summaries.
5. Exploratory notes.

If a summary sounds stronger than the file it points to, trust the underlying
file and fix the summary.
