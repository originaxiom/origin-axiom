# Reader brief — the flat-sector check (chat1's handoff, 2026-10-04)

A research record proved many negatives of the form "the object cannot fix X". A reader claims these rest on theorems
about FLAT structures (flat bundles, representations of the fundamental group, the character variety, holonomy, cusp
shapes, torsion, Chern-Simons VALUES) while physical values need CURVATURE or DYNAMICS. Your job: for each kill, from its
text ONLY (claim_killed, kill_form, hatch), answer three questions:
1. `premise`: is the kill's mathematical premise in the FLAT sector (character variety / representation / flat bundle /
   holonomy / moduli of flat structures / cusp data / torsion / CS value / arithmetic of a trace field), in a CURVED or
   DYNAMICAL sector (a metric, Yang-Mills, instantons, a potential, RG running, a bulk action), MIXED, or UNCLEAR?
2. `target`: what the kill denies -- a CONTINUOUS physical value (mass, coupling, angle, ratio, cosmological constant,
   scale), a DISCRETE physical datum (a count, rank, generation number, a bit, a group, a sign), a NON-PHYSICAL object
   (a mathematical identity, an existence of a structure), or UNCLEAR?
3. `overreach`: does the text state its negative as holding BEYOND the flat sector -- words like "the object cannot
   fix", "no value can", "impossible", "every", "no mechanism" without naming the flat hypothesis? YES / NO, with a
   quote of at most 15 words copied verbatim.
Output a JSON list to the path you are given, in order: {"id":..., "premise":..., "target":..., "overreach":"YES|NO",
"quote":"..."}. Every entry exactly once; no prose outside the JSON.
