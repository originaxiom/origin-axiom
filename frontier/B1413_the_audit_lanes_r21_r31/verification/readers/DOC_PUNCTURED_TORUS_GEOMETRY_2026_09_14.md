HEADLINE
# Punctured-torus geometry and the physical bridge

WHAT IT IS
A literature-read / correction document that surveys Minsky's and Thurston's papers plus Jorgensen's 1977 construction and applies elementary consequences to check (not extend) the repo's chirality/fermion-source programme.

VERDICTS AND CLAIMS
- "The geometric literature supplies a useful reconstruction framework, but it does not yet supply the missing fermion/source action."
- Minsky's Theorem A "determines a marked discrete faithful punctured-torus surface representation... from its ordered end invariants"; source group free rank two, parabolic commutator (LITERATURE FACT).
- "Its section 9.5 figure-eight is a curve used in a general argument, not a uniqueness theorem for the figure-eight knot" (CORRECTIVE READING).
- Bibliography correction: Jorgensen's *On pairs of once-punctured tori* "was printed in 2003, following a circa-1975 manuscript; 2001 is the workshop year" (CORRECTION).
- 1977 Annals paper "correctly identified as volume 106, pages 61-72."
- G_n = <X,Y | [X,Y]^n = 1> construction is orbifold-to-manifold, "not an assertion that these finite-n examples are the cusped m004."
- Abelianized return-map gives t^2-3t+1, "an abelianized return-map calculation; it does not identify the full groups" (LIMITATION).
- "One must also resist substituting n=infinity into a trace and calling the result a verified cusp" (METHOD WARNING).
- "Section 11's suggestion that essentially one solution is discrete is a tentative remark, not a proved uniqueness theorem."
- Thurston Theorem 7.2: geometric limits require "convergence, faithfulness, the absence of an extra covering, and the claimed homeomorphism," none from traces alone.
- Reconstruction table: integral fibre record, fibre subgroup/cover, mapping-torus quotient — "not an automatic discharge of the programme's axioms."
- "the R19 witness uses the two-cusped m202, not the bare m004 fibre cover... Directly substituting the punctured-torus model for m202 is therefore unjustified."
- Repo-history blob search table: Minsky/Marden/Bromberg/veering/ending lamination = 0 each; Maskit = 1; Bers = 20; quasi-Fuchsian pattern = 324; end-invariant = 8; Thurston-norm = 2; fibered-face = 5 (SEARCH RESULT, not proof of absence).
- "the single Maskit hit is a Gilman-Maskit search lead... not evidence that Minsky's classification was already used."
- "Thus 'the geometry is absent' overstates what the search found" (SELF-CORRECTING OVERCLAIM WARNING).
- B1404 "now explicitly introduces Minsky. Its distinction between the fibre group and finite quotient... are useful" — but "The earlier name-search receipt must not be used to claim this material remains absent."
- Three cautions on B1404: (1) trace triple is necessary not sufficient for Minsky's hypotheses; (2) "ordered fixed-point orbit is not equivalent to the conjugacy class or dilatation," with A vs A^2 as explicit counterexample; (3) nonparabolic commutator of one pair doesn't exclude other markings.
- "The current verdict is useful geometric clarification and new transfer checks, not a completed chirality mechanism or TOE."
- Two physics checks: (1) lifting a finite-norm field to an infinite cyclic cover gives infinite L2 norm — "does not make the original finite-volume field unphysical"; (2) cutting a quotient along a fibre creates two faces requiring matched spin/gauge gluing U, "not follow[ing] from the quotient" automatically.

CORRECTIONS TO MAIN OR TO ITSELF
- Bibliography date correction on Jorgensen 2003 chapter vs. 2001 workshop year (see above), an external-literature correction, not to main's record per se.
- "The earlier name-search receipt must not be used to claim this material remains absent" — the document walks back its own earlier (zero-Minsky) search framing in light of B1404.
- "Thus 'the geometry is absent' overstates what the search found" — self-correction against overclaiming from the zero-count search.
- "This is not a refutation of additional axioms or of the separately established Jorgensen extremum for a complete cusp" — clarifies it is NOT contradicting a prior record.
- "None of those conclusions is obtained merely by inspecting limiting traces" — a methodological caution against a mistake the document implies could be made, not an identified error already in main.

ROADMAP ITEMS
N/A (this is the literature-read/assessment doc itself; its own "Strategy and completion tests" section lists five forward items, quoted for completeness though not framed as a status-doc roadmap):
1. "Finish the typed reconstruction."
2. "Resolve the core at the fermionic level."
3. "Track core gluing and the outer end separately."
4. "Calculate the full spectrum and currents together."
5. "Only then claim a physical milestone."

CONFLICTS WITH MAIN
- Checked `git -C <repo> grep -l -F "two-cusped m202"` and `"three/zero charged kernel"` against docs/frontier: no exact-phrase file for "two-cusped m202"; "three/zero charged kernel" phrase not found verbatim either (only a HARVEST_LEDGER.md hit for a partial/different phrase). This does not contradict the document — it references R19/HOLONOMY_SPECTRUM.md which is presumably in the audit lane, not main, so absence in main is expected, not a conflict.
- Checked B1404 exists in main: `frontier/B1404_the_family_has_a_name/FINDINGS.md` and `b1404_the_family.py` are present and other files reference Minsky, consistent with the document's claim that "B1404 now explicitly introduces Minsky." NONE (no contradiction).
- Checked "fibred" spelling: main's grep for "fibred" hits VERDICT_LEDGER.md and several frontier B1299/B1321/B1324 files — consistent with the doc's own caveat that its regex "does not cover the British spelling `fibred`," so no conflict, just confirms the caveat was warranted.
- Overall: NONE — no place found where this document's claims about main's record are contradicted by main's actual content.

WHAT MAIN WOULD HAVE TO VERIFY
Independently confirm: (1) the Jorgensen 1977/2003 bibliographic dates; (2) that R19's witness is indeed m202 not m004 (cross-check HOLONOMY_SPECTRUM.md in the audit lane); (3) the abelianized-return-map arithmetic (t^2-3t+1, B A0 B^-1) by hand; (4) that B1404 does not overclaim Minsky-hypothesis verification beyond a trace check.
