HEADLINE
# R26 final all-head intake, September 12, 2026

WHAT IT IS
An intake note (read-only, post-run) reviewing all-head/tag fetch results and new commits on the paper-review and outside-bench branches, with no branch merged and no new census executed.

VERDICTS AND CLAIMS
- "No branch merged, upstream source edited, new census executed or received result independently certified" (scope statement).
- B1335: "reports an m010 Sym^3 character sector with nonzero index over finite fields ... and zero for the examined geometric characteristic-zero sectors" — graded "a positive candidate counterexample to vanishing from the four identities alone, not a physical chiral spectrum."
- "Numerical singular-value separation is evidence about the reported ranks, not an interval or exact characteristic-zero certificate" (downgrade).
- B1332 isotropy correction: "Isotropy of one restriction image gives an inequality, not half-dimension equality" (correction of scope).
- Broadened addendum: "106 sectors on six additional manifolds, 84 nonvacuous sectors and 128 scalar conditions" — but "Its claim that isotropy is the only possible route is not a completeness theorem established by these samples."
- Code custody: B1335's finite-field script "prints one selected sector after enumerating to four representations; it is not itself the full census."
- "Its displayed `V == dual(V)` compares literal matrices, not module isomorphism, so that display alone cannot exclude self-duality" (flagged defect).
- "The characteristic-zero script imports `recog12` after inserting `/tmp/sweep` ... not beside B1335's new script. A rerun must pin and resolve it explicitly" (reproducibility gap).
- "The paper-impact note still calls B1334 a proof on the identity component. The checked tree diff contains NO B1334 change" (CORRECTION — flags an unrepaired claim on the paper-review branch).
- Memo 205 (outside-bench): "six named cubic readouts giving the same field, a negative different-field control, inequivalent 27/78 modules" — received, "not reproduced" here.
- "six equal field outputs and the received trialitarian interpretation do not alone prove that every construction on the charge space must return that field" (scope duty, not refutation).
- Disposition: "R26's proof/source/test population is unchanged and its completed scientific receipts stand at their declared scope."

CORRECTIONS TO MAIN OR TO ITSELF
Not a correction to main, but a flagged unrepaired issue on the *paper-review* branch (not main): "The paper-impact note still calls B1334 a proof on the identity component. The checked tree diff contains NO B1334 change. The earlier intake's parameter-dependent kernel/rank obligation is therefore not repaired by this update, nor by adding numerical zero sectors." This references the document's own earlier intake, implying continuity/self-consistency rather than retraction.

ROADMAP ITEMS
N/A (intake/disposition note, not a status/roadmap doc). Disposition line: "Next is still one stationary source/end action and quantum completion; received other-seat results are not independent certification of that work."

CONFLICTS WITH MAIN
This document's B1334/B1332/B1335 claims concern the paper-review branch at commit c83b6b80, not main. `git -C <repo> grep -l -F "B1334" -- docs frontier` shows main HAS its own `frontier/B1334_the_deformation_proof/FINDINGS.md` and `docs/THE_CHAIN_STATUS.md` etc. (main's frontier now includes B1332/B1334/B1335/B1345 at HEAD 6684db67, later than the commits this intake examines). No contradiction found between this doc's characterization and main's current B1334 FINDINGS.md (which does describe S^0 as "its identity component"); the intake's complaint is about the *paper-impact note* mischaracterizing B1334 as already proved, not about B1334's FINDINGS itself. NONE.

WHAT MAIN WOULD HAVE TO VERIFY
Whether main's current `frontier/B1334_the_deformation_proof/` and `frontier/B1332_.../ADDENDUM_*` files (now merged past this intake's examined commits) have since closed the "parameter-dependent kernel/rank" and "isotropy is the only possible route" obligations this intake flags as still open, and whether B1335's finite-field script's `V == dual(V)` comparison and `/tmp/sweep` import have been fixed.
