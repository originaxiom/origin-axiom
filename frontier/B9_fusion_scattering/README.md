# Probe B9 — Fusion–scattering correspondence

> **Speculative frontier work.** Everything here is a *logged observation*, not a
> claim (see `../../GOVERNANCE.md` §5). Nothing in this directory is promoted to
> `CLAIMS.md`.

## The question

The cubic term `κε²` in the B8 expansion is a `2 ↔ 1` vertex (two quanta in, one
out, or the reverse). The Fibonacci fusion rule is `τ × τ = 1 + τ`. Both involve
the same polynomial `τ² − τ − 1` (P2 for fusion; P16 for the vertex — see the
"six faces" observation). Is the cubic field-theory vertex *the same structure*
as the fusion rule, or merely analogous?

## What the probe computes (`probe.py`)

It lays the two side by side symbolically:

- the fusion rule `τ × τ = 1 + τ`, rearranged to `τ² − τ − 1 = 0` (P2 / exact);
- the cubic vertex coefficient from expanding `V(φ + ε)` (the `ε²` term, exact
  given B6).

and checks that both rest on `τ² − τ − 1`.

## The caveat (verbatim from SESSION3_SYNTHESIS.md)

> "analogous to" is not "derived from." The fusion category is exact algebra; the
> cubic vertex is a perturbative field theory artifact. They share a structure but
> the mapping is not rigorous.

So B9 records a **shared polynomial**, not a derived equivalence. The fusion rule
(P2) is exact category theory; the cubic vertex is an artifact of the inserted
field theory (B6) expanded around its minimum. That they share `τ² − τ − 1` is
the same "six faces" fact — one polynomial in several contexts — not a functor
between a TQFT and a scattering amplitude.

## Verdict

`STALLED` — shared polynomial, not a rigorous fusion ↔ scattering map. See
`FINDINGS.md`.
