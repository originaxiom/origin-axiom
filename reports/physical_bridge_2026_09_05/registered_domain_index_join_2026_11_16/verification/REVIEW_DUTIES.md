# P-C3 source-complete proof and code review

2026-11-16. Bounded verification preparation under the P-C3 card. Scientific
checks, collection and mathematical imports remain unreleased. The new
source has been inspected statically by its author. Independent review is
addressed to the SM verification lane and main through the versioned relay.

## Exact packet

DESIGN.md and EXPECTED.json first appeared at 12755db8a, before checker
implementation. ENGINEERING_DESIGN.md first appeared at 657d7cd62, before
fixture implementation. Later design additions provide the existing
prospective gate's required metadata and clarify the engineering scope.
This is a prospective verification design for already hand-derived claims.

SPECIFICATION.json pins every local source, test, proof input and runtime
requirement in the declared inventory. SOURCE_RESOLUTION.json maps all 24
entries in the two prior receipts to available local review files. Two
main-only inputs are materialized from exact committed blobs. The first
packaging failure is retained in PREPARATION_FIRST_FAILURE.md.

## Proof duties

- Re-derive the quaternion contraction's full and traceless span. Check
  its entrywise bilinear convention and scalar-line hypotheses. Examine
  the exact equivalent stabilizer system L^T Y=Y B with B=R^-1.
- Check the full section operator, argument/deck cancellation and declared
  spin factor. These controls verify the specified free coefficient
  construction. The actual curved physical transitions remain a separate
  calculation.
- Re-derive the source cubic and all three kinetic factors from the parent.
  Check the one-half connection metric, the vector component normalization,
  the root charge and trace pairing and the spin/Wilson frame identity.
- Check the physical mass-map derivative with its target density and the
  absence of a spurious identical-field factor. Keep the vector-like
  exceptional modes and their conjugates in the interpretation.
- Re-derive the full-complement second-order map, including V2, and the
  hypothesis of a closed-range inverse on the actual domain. The finite
  heavy-block control supplies no such inverse for the curved operator.
- Check the rank-two slot rule and its pure-slot/no-gaugino hypotheses.
  The physical five-coefficient span is uncomputed.

## Code and admission duties

- Independently compare source equations with checks.py, rather than
  accepting the author's expected values. Check each planted discrepancy
  and ensure the positive identity is computed on a distinguishing input.
- Check source closure, runtime dependencies, imported gate code, the
  isolated gate bootstrap and both pre/post-run custody conditions.
- Check all twelve method identities and the rejection fixtures. The
  engineering fixtures exercise early failure of the real runner. They
  provide no positive admitted scientific-run fixture.
- Review the standard-library packaging of two missing source blobs and
  the stated scope of STATIC_INSPECTION.json. Its AST population is a
  static inventory, with mathematical tests still uncollected and unrun.
- Bind any acceptance to the exact sealed commit and specification using
  the existing prospective review/admission mechanism. No synthetic
  admission or retrospective scientific run is supplied here.

The admitted scientific command is the one in SPECIFICATION.json. It must
run in a complete, clean, isolated Git checkout containing the real review
and acceptance evidence. Preserve first.jsonl and first.log on any failure.
The inherited staged material in the working checkout stays protected.

## Scientific scope after a future finite pass

The conditional normalized vertex/current relation and the constant-lift
classification would gain bounded algebraic evidence. Their foundations,
physical mode/domain hypotheses, actual family interpretation, vacuum
selection, quantum completion and gravity still carry their existing
obligations. This package counts no independent input as removed.
