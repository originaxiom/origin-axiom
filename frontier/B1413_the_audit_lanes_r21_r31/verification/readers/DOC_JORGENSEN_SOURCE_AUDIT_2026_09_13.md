HEADLINE
# Jorgensen source audit: retain the stronger geometric selector

WHAT IT IS
An owner-requested literature/reception audit of the primary sources (Callahan, Adams) behind a banked result (B1345), explicitly "not a new physical-spectrum calculation, a new B arc or independent main banking."

VERDICTS AND CLAIMS
- "Callahan's Theorem 2.3 characterizes the figure-eight complement by J-tilde=1 among orientable hyperbolic three-manifolds." — cited as literature fact.
- "B1345's corollary wording is actually present in the primary paper; it is not merely an inaccurate paraphrase." (verifies main's B1345 against source)
- "Adams' cusp characterization then identifies the manifold, without assuming the ambient group has two generators."
- "The published generalized-infimum statement is cited, not re-proved... this audit does not supply a separate attainment theorem."
- Witness check: "A=[[1,1],[0,1]], B=[[1,0],[u,1]], u=exp(i*pi/3). Direct symbolic multiplication gives tr[A,B]=2+u^2... j(A,B)=1." — "No new numerical reproduction is claimed in this checkpoint."
- "The fibre kappa=-2 belongs to a different marked pair/group problem; substituting it into the meridian calculation is not licensed."
- Table distinguishing axiom-ledger objects: A1 = "integer record state space Z^2" (not two generators of a fundamental group); A2 = GL(2,Z) updates (not arbitrary Möbius transformations); A3 = det +1 for integer updates (not orientation preservation without a lattice map); A5 = torsion-free first homology (not absence of finite-order group elements).
- "This inference is not valid as written" — re: memo 226 equating a two-generator group with A1 and inferring the theorem assumes A1.
- "This does NOT establish the earlier memo's count of five discharged axioms. Neither count is accepted by vocabulary matching."
- "A torsion-free fundamental group can have torsion in its abelianization. The repo's A5 is explicitly about the latter. This is not an objection to Callahan's theorem; it is a correction to a cross-structure reading."
- "This is a genuine geometric uniqueness criterion. It narrows selection much more sharply than a small census or a matching dimension does."
- "If the unit obstruction was first evaluated after selecting m004, the implication back to m004 is a characterization, not an independent derivation from weaker starting premises."
- "Complex conjugating both matrices preserves j; this trace-modulus functional by itself cannot distinguish a geometry from its mirror."
- "R19's conditional sourced kernel and R29's finite-width construction are not refuted by this theorem."
- "B1345/B1401 are present on that paper-review pin; B1345's path is not present at origin-main b94ed03a." (custody claim)
- "The existing bank query returned no local frontier hit for its ASCII term, while the twelve-head synonym sweep returned PRESENT... neither output licenses a universal absence statement."
- "26 PASS / 4 FAIL, the same failed identities as R29, with only the old relay's age incremented. All 403 then-latest artifact hashes and 63 design seals match; 131 relative links resolve."

CORRECTIONS TO MAIN OR TO ITSELF
- Corrects an external memo (memo 226), not main: "The received memo 226 equates a two-generator group with A1, then says the theorem assumes A1. That inference is not valid as written" — with the A1/A2/A3/A5 table as the correction. This is explicitly framed as "The later axiom correction also needs correcting" (a correction of a correction, on the outside/paper-review branch, not main).
- No statement that main's own docs/frontier record is wrong; in fact confirms B1345's corollary quoting is accurate ("it is not merely an inaccurate paraphrase") and that "R19's conditional sourced kernel and R29's finite-width construction are not refuted by this theorem."

ROADMAP ITEMS
N/A (audit/literature-read doc; forward items given as two parallel duties rather than a task list):
1. "Audit the non-circular entrance: starting class, discreteness, extremality, and the map from selected geometry to record dynamics."
2. "Continue the existing physical path: derive the finite-width/end fermion action and domain, then its spectrum, anomaly and currents."

CONFLICTS WITH MAIN
- Claim: "B1345's path is not present at origin-main b94ed03a." Checked: `git -C <repo> ls-tree -r --name-only b94ed03a | grep -i B1345` returns nothing (confirmed absent at that commit); `git -C <repo> merge-base --is-ancestor b94ed03a HEAD` succeeds, confirming main has since advanced past that pin. Current main HEAD (6684db67) DOES contain `frontier/B1345_the_jorgensen_number/` (landed at commit 83cb185a, "B1345 the Jorgensen number: the theorem is real, the record already had the number"). No contradiction — the doc's claim is accurate as of its stated pin, and its exact wording ("not present at origin-main b94ed03a") already anticipates main advancing past that point.
- No other claim in this document asserts main's docs/frontier record is factually wrong; its corrections target an outside-branch memo, not main.
NONE

WHAT MAIN WOULD HAVE TO VERIFY
Whether B1345's actual wording in `frontier/B1345_the_jorgensen_number/FINDINGS.md` matches Callahan's Corollary 2.4 as claimed, and whether B1345/B1401's own axiom-identification language (A1/A2/A3/A5) already avoids the type conflation this audit flags in memo 226 — i.e., confirm main's own record never made the same A1=two-generator identification the audit corrects in the outside memo.
