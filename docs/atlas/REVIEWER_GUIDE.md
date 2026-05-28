# Reviewer Guide

Status: navigation guide. It does not replace the governed ledgers.

## Fastest Audit Route

Read in this order:

1. `GOVERNANCE.md`
2. `CLAIMS.md`
3. `docs/UNIQUENESS_THEOREM.md`
4. `docs/SESSION3_SYNTHESIS.md`
5. `docs/atlas/RESEARCH_TREE.md`
6. `docs/atlas/FAILURE_ATLAS.md`
7. `REPRODUCIBILITY.md`

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

## If You Are A Mathematician

Start with:

1. `docs/UNIQUENESS_THEOREM.md`
2. `tests/test_uniqueness_theorem.py`
3. `CLAIMS.md`

The main thing to inspect is the conditional theorem:

```text
minimal-record axioms -> A = LR, up to order -> P1-P16
```

The most useful external check is whether the hypotheses are stated minimally,
whether the torsion and mapping-torus facts are fully justified, and whether
the downstream connections are presented as known mathematics or genuinely new
packaging.

## If You Are A Physicist

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

The most valuable review is not encouragement or dismissal. It is a precise
statement of which inserted object is unavoidable and whether any bridge can be
made falsifiable.

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
