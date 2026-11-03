"""S297: LAW_MAP rows that state what a later correction narrowed, sharpened in place (B1216's rule: targeted, each verified
by main at its source; the original words kept, a dated bracket added; an outright error replaced with the old reading kept).
Rows 334 (B1739, applied first, by hand), and here: 50, 150, 154, 164, 172, 234, 256 (old era) and 293, 298, 305, 322, 329,
330, 335, 344 (the fibre era). Each replacement asserted to occur exactly once."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
P = ROOT / "docs/LAW_MAP.md"
t = P.read_text(encoding="utf-8")
S = "carried here 2026-11-03, S297"
EXACT = ("the end is the small-cut norm 2πL + c_s at L_max's height (B1726's compute()), not the canonical end's exact norm, "
         "which lies 35–38% below it there; with the exact norms the six fail near these rows (RETRACTIONS, 2026-10-28; the "
         "web seat's THE EXACT END reproduced on main, S238; P-421)")
R = [
 # 50 -- member scope; E-3b finished
 ("The object contains 3 not 5, so it generates a minimal being-doublet but NOT the composite-totient hearing-richness",
  "The object contains 3 not 5, so it generates a minimal being-doublet but NOT the composite-totient hearing-richness "
  "[scoped: m004's complete hyperbolic structure, a member's fact (PRACTICES' member-scope rule); at cone angle π its "
  "spherical end has trace field ℚ(√5) (B981); " + S + "]"),
 ("E-3b (interfere/decouple + chirality) running**", "E-3b (interfere/decouple + chirality) running [finished: B695, E-3b "
  "verified (the row above); " + S + "]**"),
 # 150 -- member scope
 ("the θ-symmetric (amphichiral) object is robustly VECTOR-LIKE",
  "the θ-symmetric (amphichiral) object is robustly VECTOR-LIKE [scoped: m004's, a member's wall, not the family's -- B713 "
  "is on the member-scope gate's frozen baseline with its scope addendum owed (PRACTICES; B1476's census; P-589); " + S + "]"),
 # 154 -- the signature is the holonomy's
 ("Time/4d/Lorentzian-signature enter through the COUPLING, like chirality (B713)",
  "Time/4d/Lorentzian-signature enter through the COUPLING, like chirality (B713) [sharpened 2026-10-29 in B716 (the web "
  "seat's THE CONE AND THE SIGN, reproduced on main): the Lorentzian signature is the holonomy's, not the observer's -- "
  "PSL(2, ℂ) ≅ SO⁺(3, 1), H³ the mass hyperboloid, generic to every hyperbolic 3-manifold; time, 4d and the "
  "identification with spacetime stay the observer's; " + S + "]"),
 # 164 -- the amplitudes' field
 ("need a real QUARTIC ℚ(√φ)", "need a real QUARTIC ℚ(√φ) [corrected in B726 (B729, B730): ℚ(√φ) is the F-symbol field; "
  "the amplitudes live in ℚ(√(2+φ)) = ℚ(ζ₂₀)⁺, x⁴ − 5x² + 5, as the row below states; " + S + "]"),
 # 172 -- an error: the 3-manifold's continuous spectrum
 ("open→continuous Laplacian spectrum [1/4,∞)", "open→continuous Laplacian spectrum [1,∞) [corrected 2026-11-03, S297: "
  "read '[1/4,∞)', the hyperbolic surface's value; a cusped hyperbolic 3-manifold's continuous spectrum starts at "
  "(n − 1)²/4 = 1 (B739: m004's is [1,∞), one channel)]"),
 # 234 -- status lag
 ("**Unworked: L138**", "**Unworked: L138** [fired 2026-08-08, verified by B969 (OPEN_LEADS, L138); " + S + "]"),
 # 256 -- status lag
 ("returns it to an axis (not on the record)", "returns it to an axis (not on the record) [closed in that form 2026-10-04: a "
  "smooth quartic cannot return a generic independent source exactly to an axis (B1466's R83 addendum); " + S + "]"),
 # 293 -- the lift formula is the large-L limit
 ("the lift is D(τ)/(2πL), with D", "the lift is D(τ)/(2πL) [its large-L limit: at the canonical radius, L of order one "
  "(B1667), the exact lift differs by 17–25% (B1691's correction, RETRACTIONS); " + S + "], with D"),
 # 298 -- the quarter is by trace
 ("so coherent averages live on a quarter of the threads;", "so coherent averages live on a quarter of the threads [by "
  "trace, 0.248–0.252; by word length the share alternates with the cut's parity, 0.32 and 0.17 (B1815 § 5, "
  "RETRACTIONS; THE_WEAVE scoped 2026-10-29); " + S + "];"),
 # 305 -- characterises, not derives
 ("so GM1's two records follows from", "so GM1's two records is characterised by [read 'follows from' until S297: the "
  "input characterises two records, GM1 in an invariant form, not a weaker premise (B1677's sharpening of 2026-10-21, "
  "B1682, GENESIS v1.50; the row below)]"),
 # 322 -- the exact end; the widest menu
 ("the seats' third opinion owed (P-304) |", "the seats' third opinion owed (P-304) [scoped 2026-11-03, S297, from the arc's "
  "dated note: " + EXACT + "; 'the canonical end' above reads the small-cut formula; under W138's widest menu the six are "
  "3.365%, not specific (P-304 DONE); UNSETTLED under GENESIS v1.61 (B1829)] |"),
 # 329
 ("the seats' third opinion owed (P-339, P-340) |", "the seats' third opinion owed (P-339, P-340) [scoped 2026-11-03, S297: "
  "B1734's census runs through B1726's compute(), so " + EXACT + "; under W138's widest menu 2.22%, not specific (the "
  "arc's own note); UNSETTLED under GENESIS v1.61 (B1829)] |"),
 # 330
 ("third opinion owed (P-342); τ's placement P-343 |", "third opinion owed (P-342); τ's placement P-343 [scoped 2026-11-03, "
  "S297: B1726's grid through its compute(), so " + EXACT + "; post hoc, FITTED, never a candidate (B1829)] |"),
 # 335
 ("the nine fail (B1739); third opinion owed (P-348) |", "the nine fail (B1739); third opinion owed (P-348) [scoped "
  "2026-11-03, S297, from the arc's dated note: 'census frame, L_max' means " + EXACT + "] |"),
 # 344 -- hypothesis (b) fails on three slopes
 ("16 line-sectors with a vanishing theta constant excluded) |", "16 line-sectors with a vanishing theta constant excluded) "
  "[narrowed 2026-11-03 (S287, B1826; B1788's dated note): hypothesis (b) fails identically on the slopes 1/12, 1/4 and "
  "5/12 at finite τ in all three sectors, so those slopes are excluded too; the agy lane's replacement of hypothesis (a) "
  "is unverified on main (P-559); " + S + "] |"),
]
for old, new in R:
    assert t.count(old) == 1, (t.count(old), old[:70])
    assert "|" not in new.replace(" |", "").replace("| ", "") or old.endswith("|"), old[:40]
    t = t.replace(old, new)
P.write_text(t, encoding="utf-8")
print("LAW_MAP: %d replacements" % len(R))

# B1734 and B1735 run through B1726's compute(): the exact-end note was never carried to them
NOTE = ("\n## Dated note (2026-11-03, S297; the triage's recheck)\n\nThis arc's rows come through B1726's compute(), so its "
        "L_max is the small-cut norm 2πL + c_s at L = L_max(Im τ), not the maximal horoball's exact norm, which lies 35–38% "
        "below it there; with the exact norms the six fail near the four families' rows (RETRACTIONS, the row of 2026-10-28; "
        "the web seat's THE EXACT END, reproduced on main at S238; P-421). That correction named B1726, B1741, B1749, B1753 "
        "and B1786 and missed this arc. Nothing else in this arc changes.\n")
for arc in ("B1734", "B1735"):
    f = next((ROOT / "frontier").glob(arc + "_*")) / "FINDINGS.md"
    s = f.read_text(encoding="utf-8")
    assert "the triage's recheck" not in s
    f.write_text(s.rstrip("\n") + "\n" + NOTE, encoding="utf-8")
rt = (ROOT / "docs/RETRACTIONS.md").read_text(encoding="utf-8")
old = "dated notes on B1726, B1741, B1749, B1753, B1786 |"
assert rt.count(old) == 1
rt = rt.replace(old, "dated notes on B1726, B1741, B1749, B1753, B1786 (and B1734, B1735, which run through B1726's "
                "compute(): carried 2026-11-03, S297) |")
(ROOT / "docs/RETRACTIONS.md").write_text(rt, encoding="utf-8")
print("B1734, B1735 dated notes; RETRACTIONS row extended")
