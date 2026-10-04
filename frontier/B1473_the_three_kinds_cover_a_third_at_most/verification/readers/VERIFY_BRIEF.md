# Second-reader brief — adversarial check of the three-kind assignments

Each entry was assigned PAIRING, FLATNESS or NON-UNIQUENESS by a first reader, with a quote. Your job is to REFUTE the
assignment where the text does not support it. Definitions (same as the first reader's):
- PAIRING: the quantity is cancelled/neutralised by a symmetry partner (mirror, conjugate, dual, involution, orientation
  reversal, sign pairing, 2-torsion forcing zero).
- FLATNESS: there is nothing to read because the structure is flat/constant/degenerate (flat bundle, zero curvature,
  vanishing class, no gradient/potential/dynamics, invariant identically trivial).
- NON-UNIQUENESS: the quantity exists but too many candidates and nothing selects (family not point, moduli, continuum,
  non-canonical, no selection principle, fitted/numerology/short catalogue).
Rules: judge from claim_killed / kill_form / hatch ONLY. Default to DEMOTE when the text names a different mechanism
(a false premise, a number that does not match, a tool error, nowhere to land, a value compared to data and missed) or
names no mechanism. CONFIRM only when the text itself names the pairing / flatness / non-selection as the reason.
Output a JSON list to the path you are given, in order, one object per entry:
{"id":..., "verdict":"CONFIRM|DEMOTE|RECLASS", "kind": "<the kind you would assign; for DEMOTE write OTHER and a label
after a colon, e.g. OTHER:premise-false>", "why": "<at most 15 words>"}. Every entry exactly once; no prose outside the JSON.
