# Reader brief — L244 (a): the three-kind census of the kill graph

You are classifying NEGATIVE results (kills) of a mathematics research record by the *shape of the reason* the kill
gives. You judge from the text of each entry ONLY (fields `claim_killed`, `kill_form`, `hatch`, `scope`). You do not
evaluate whether the kill is correct. You do not open any other file.

Each entry gets exactly ONE kind:

- **PAIRING** — the sought quantity exists but is cancelled or neutralised by a symmetry partner: a mirror image,
  complex conjugate, dual, involution, orientation reversal, a ↔ ā pairing, sign pairing, even/odd cancellation, a
  2-torsion that forces zero, "the two contributions cancel", "θ-symmetric", "amphichiral".
- **FLATNESS** — there is no quantity to read because the structure is flat, constant or degenerate: a flat bundle,
  zero curvature, a vanishing characteristic class, no gradient, no potential, no dynamics that selects, an
  invariant identically zero/trivial for structural reasons, "every value equal", "the index is zero on this locus",
  "the period is trivial".
- **NON-UNIQUENESS** — the quantity exists but too many candidates exist and nothing selects among them: a family
  not a point, a moduli space, a continuum, "non-canonical", "no selection principle", "any value can be produced",
  "the choice is the observer's", "fitted / numerology / short catalogue" (a match that does not single out).
- **OTHER** — anything else; give a short label from this list where it fits, else your own two-word label:
  `premise-false` (the claim assumed something untrue), `arithmetic-mismatch` (the field/discriminant/number does not
  match), `value-miss` (a predicted number compared against data and missed), `no-landing-site` (the construction has
  nowhere to land), `instrument` (a tool or computation error, or not computed), `scope` (true elsewhere, false here),
  `unstated` (the text gives no reason).

Output: write a JSON list to the path you are given, one object per entry, in the batch's order:
`{"id": ..., "kind": "PAIRING|FLATNESS|NON-UNIQUENESS|OTHER", "label": "<short>", "quote": "<at most 20 words copied
verbatim from claim_killed or kill_form that justify the kind>", "confidence": "high|medium|low"}`.
Every entry in the batch must appear exactly once. Do not summarise, do not skip, do not add prose outside the JSON.
Mixed cases: pick the kind that the kill's *mechanism* names, and set confidence "low".
