# B1463 — THE TWO EARLY CORRECTIONS RE-DERIVED: B37'S DETECTOR COULD NOT DETECT, AND B130'S CONCLUSION HOLDS BY A BETTER ARGUMENT THAN ITS OWN

**Verdict: PROVED** (scope: B37's and B20's predicate on the metallic trace map; B130's fixed loci at m = 2, 3, 4 in
Fricke coordinates; reach *class* for the vacuity of the predicate, *single* (three values of m) for the components).
cc (main), 2026-10-03. Pays lead L243 (a); the audit lane's AR3 and AR4, carried into GENESIS by the SM seat's
sm:B1521 and read on main since v1.3, are now re-derived on main with main's own code and main's own files.

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "never reads|self-model predicate|forced choice|kappa.{0,10}free|elimination
  ideal|isolated (fixed )?point|primary decomposition"`: *VERDICT topic-sweep: 12 of 1335 arcs on main match (NEGATIVE 5,
  PROVED 7)*. Read: B20 and B37 (`probe.py` of each — the predicates as written), B130 (`probe.py::kappa_elimination`;
  FINDINGS §"The result", §"The tombstone" — the latter already names the component-wise kill condition and reports
  "none exists" from `sp.solve`), the audit lane's ACT_REGISTER AR3–AR4 as quoted in sm:B1521 (its script read, not
  run), GENESIS v1.7 §9's two [v1.6] rows. **Literature:** Krull's principal ideal theorem and primary decomposition
  are textbook; nothing searched.

## 1. AR3 — B37's "never reads" (`verification/two_corrections.py::ar3`)

B37's self-model predicate is, in its own file, `any(component.has(i_symbol) for component in trace_map)` with
`i_symbol = sp.symbols("I")`, a symbol that occurs in no map written in x, y, z. **It is False on every such map** —
it could not fail on its domain (MB12; the E82 class, from 2026-05). The audit lane's rewriting
T′(x, y, z, r) = (z, x, 2xz − y + (r − I), r) equals T on the record graph r = I and preserves the graph, yet the
predicate fires on it; the opposite control, a map that reads r off the graph, changes an orbit when r ≠ I. So B37's
conclusion "the trace map never reads κ" is not supported by B37's test. Whether the trace map reads κ in the
reads-and-branches sense is FK12's question, open; GENESIS §9's row "in B37's literal sense only" is right.

## 2. AR4 — B130's "κ is free" (`::ar4`; `b130_components.sage`)

B130 inferred "κ unconstrained on the fixed locus, no discrete value to select" from the k-elimination ideal of the
fixed locus being zero. The inference is invalid in general: V(x(x − 1), xk) is a line with k free and the isolated
regular point (1, 0), and eliminating x leaves the zero ideal in k (the point alone eliminates to (k)). **B130's
conclusion is nevertheless true on its domain, by a valid argument:** at m = 2 the fixed ideal has the lex basis
{2x − yz, y(y²z² − 2z² − 8)} — two generators in three variables, so by Krull no component is 0-dimensional; at m = 2,
3, 4 the Hilbert dimension is 1 and **the primary decomposition (Sage/Singular, recorded in
`b130_components_sage.out`; Sage is not the test environment) has every component of dimension one** — two, two and
four curve components, none a point. The "isolated points" of B130's tombstone (κ = −6, −158/21 at m = 2) and the
points main's own solver produced here (κ = 2/3, 13/2 at m = 4; one of them looked isolated under Newton for an
hour) are singular points of curve components. So: the record's "no forced choice in the trace-ring invariants" stands
for m = 2, 3, 4 with its proof replaced; for m ≥ 5 it rests on B130's numerics and is scoped accordingly.

## 3. What changes

Addenda on B37 and B130; an ERROR_LEDGER instance for B37's detector; L243 (a) paid; GENESIS v1.8 (log line only: the
two rows of §9 verified on main). Nothing in the derivation moved. The lesson is the MB12 one again, twenty weeks
back: a criterion that cannot fail certifies nothing, and a sound conclusion reached by an invalid step must be
re-proved, not re-cited.

## 4. Errors in this arc

My numerical isolation test misread a singular point of a curve as an isolated point for one hour; the exact
decomposition corrected it before anything was written. Recorded so the next reader does not trust that test alone.
