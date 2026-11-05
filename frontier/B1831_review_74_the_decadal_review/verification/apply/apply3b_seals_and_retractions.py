"""Review 74 (S299), apply 3b: P-535's seal-order cases adjudicated (main verified each diff at source: B496 one title line;
B1486 five lines added to fused.py; B742 +9 and +4/-2 to FINDINGS; B749 +4 and +36 to FINDINGS and +4 to P019; B1490's five
lines outside C1-C4 and the reading rule, whose span is identical before and after), append-only notes and '# sealed at'
lines (B1654's precedent); RETRACTIONS +4 for this review's corrections; the paper's count (an erratum, S258's precedent)."""
import pathlib, glob
ROOT = pathlib.Path(__file__).resolve().parents[3]; D = "2026-11-04"; R = "Review 74, P-535"
def arcdir(a): return pathlib.Path(glob.glob(str(ROOT / "frontier" / (a + "_*")))[0])
def append(a, text, f="FINDINGS.md"):
    p = arcdir(a) / f; t = p.read_text(encoding="utf-8"); p.write_text(t.rstrip("\n") + "\n\n" + text.strip("\n") + "\n", encoding="utf-8")
def appline(a, line):
    p = arcdir(a) / "ARTIFACT_HASHES.txt"; t = p.read_text(encoding="utf-8"); assert line not in t; p.write_text(t.rstrip("\n") + "\n" + line + "\n", encoding="utf-8")
append("B496", "> *Dated note %s (%s):* PREREGISTRATION.md changed after this record in one line only, its title's id B493 → B496, at "
 "`88f293a41` (the renumber begun at `fbdbcaa36`); no statement, question or criterion changed, and the text as banked is at "
 "`baa49e6bd`. The preregistration and this record were committed together (the early practice), so git does not show which "
 "was written first.*" % (D, R))
append("B1486", "> *Dated note %s (%s):* the guard of § 3's second and third bullets is in `verification/fused.py`, changed at "
 "`82f0ccb27` (`relator_residual` and one assertion in `index`; five lines added, none removed; sealed sha256 2831b9f2… at "
 "`385c6891e`). It refuses to count a non-representation and changes no count on a representation; the sealed run is kept "
 "in `sealed_run/`. Separately: B3's sealed 'converges at ε = 0.1 and 0.02' held for 7 of the 8 sealed seeds (m136's first "
 "member at ε = 0.1 did not), which the grade cell's 'at every step that converged' covers but does not count.*" % (D, R))
append("B742", "> *Dated note %s (%s):* this FINDINGS.md was hashed at banking (`4860553a8`, sha256 a905b9fe…) and changed twice "
 "the same day, adding text only: the kill-graph diff section at `318133e46` and the B745 resolution of the revivals' status "
 "line (struck through, kept) at `eeef58ae4`. No verdict, target or criterion changed.*" % (D, R))
appline("B742", "# sealed at 4860553a8: a905b9fe000c812bab1eb7d5145ab8c9117d0ff907baa6eab18118b73657eabc  frontier/B742_negatives_hunt_p1/FINDINGS.md (changed after banking at 318133e46 and eeef58ae4, text added only; FINDINGS.md's dated note of 2026-11-04)")
append("B749", "> *Dated note %s (%s):* two files this arc hashes changed after its seal, adding text only: this FINDINGS.md (results "
 "seal `08e16340f`, sha256 d6de605b…) by the two dated F9 addenda above (`b9157703c`, `1c062b17a`), and the pinned "
 "`philosophy/P019_the_genesis_axiom_chain.md` (sealed sha256 9fab1ea1…) by a four-line pointer to GENESIS.md at "
 "`f655034b9`. The forks F1–F8, their verdicts and `RESULTS.json` are as sealed.*" % (D, R))
appline("B749", "# sealed at 08e16340f: d6de605bbd89ef28dcba82633a33e5bc0d065a0ccc0151d06580ebacca96b70d  frontier/B749_genesis_forks/FINDINGS.md (two dated addenda appended at b9157703c, 1c062b17a)")
appline("B749", "# sealed at 08e16340f: 9fab1ea1db5d784c61a5cc5802aeb7e8d8005dc498b80ca59b76c3b3e2f1b32d  philosophy/P019_the_genesis_axiom_chain.md (a four-line pointer header added at f655034b9, nothing removed)")
append("B1490", "> *Dated note %s (%s):* the in-place amendment of PREREGISTRATION.md (`4e617453e`, sealed 93b5777e → 7fe522c0) is three "
 "bracketed notes and two unbracketed rewordings of the group's name in § 2, not two notes. It touches § 2 and the last "
 "sentence of the reading rules only — C1–C4, their priors and 'VERIFIED iff C1 and C2 hold' are as sealed (main's diff of "
 "the span, empty) — and the generated seal ledger shows it only as a second commit; the sealed hash 93b5777e is recorded "
 "here and in the claim line. The verdict does rest on the disclosed post-seal fix of `common_cover_main.py`, with the "
 "sealed run kept.*" % (D, R))
append("B1409", "> *Dated note %s (%s):* the seal (`31cfd0325`) hashes the preregistration only; the instrument "
 "`verification/b1409_budget.py` was written after it against the sealed definitions and committed with its first outputs "
 "at `efa5fd465`, so git does not show its form before the run.*" % (D, R))
append("B1455", "> *Dated note %s (%s):* the seal (`12ed66bd8`) is the preregistration's text alone; the instruments under "
 "`verification/` were written after it and committed with their first outputs and this record at `7d65bf05a`, so git "
 "does not show their form before the run.*" % (D, R))
# RETRACTIONS +4
rows = [
 "| B1809's \"Isotropic directions … m₂ ≡ 0 only at L = ∞\" | B1809 | CORRECTED (scope) — false on the order-4 lines (every sector) and the order-12 lines (leptons), where m₂/m₃ ≤ 4 × 10⁻¹⁴; stands elsewhere | the web seat's THE RELATIONS THE FRAME FORCES (fe2f972cd), checked by main with B1821's evaluator (Review 74) |",
 "| B1823's \"every computed n = 3 and n = 4 vacuum lies on a line\" | B1823 | CORRECTED (false) — four converged, isolated vacua at λv = 1.0 in menu Z lie off every mirror line (summary.txt); the NEGATIVE stands (rank 3 on a line already exceeds τ's 2) | Review 74's seeded read, verified by main |",
 "| B1821's \"confirmed on every direction and line\" | B1821 | CORRECTED (scope) — confirmed on 154 of the census's 266 lines (all twelve orders); two earlier rows recorded 22 of 26 groups, undisclosed | Review 74's seeded read, verified by main |",
 "| \"the LL pair at twist ∓6 differs by order 10\" (main, S298: harvest rows 1512, 1538; B1826's note) | B1826 | CORRECTED (main's own) — it differs by 14–30 on three of four lines checked and is the charged norms with the channels permuted on (1/3, 1/6); the S298 check had no committed instrument | Review 74's P-086 check; B1826 verification/review74/ll_pair_norms.py |",
]
p = ROOT / "docs/RETRACTIONS.md"; t = p.read_text(encoding="utf-8")
anchor = [l for l in t.split("\n") if l.startswith("| \"the vanishing is exact at finite τ on these slopes\"")][0]
assert t.count(anchor) == 1; t = t.replace(anchor, anchor + "\n" + "\n".join(rows)); p.write_text(t, encoding="utf-8")
n = len([l for l in t.split("\n") if l.startswith("| ") and not l.startswith("|---") and "what was asserted" not in l])
W = {67: "sixty-seven", 68: "sixty-eight", 69: "sixty-nine", 70: "seventy", 71: "seventy-one", 72: "seventy-two", 73: "seventy-three",
     74: "seventy-four", 75: "seventy-five", 76: "seventy-six", 77: "seventy-seven", 78: "seventy-eight", 79: "seventy-nine", 80: "eighty"}
q = ROOT / "papers/P3_THE_PAPER/main.tex"; s = q.read_text(encoding="utf-8")
old = "retractions index holds sixty-four corrected or withdrawn statements"; assert s.count(old) == 1
q.write_text(s.replace(old, "retractions index holds %s corrected or withdrawn statements" % W[n]), encoding="utf-8")
tt = ROOT / "tests/test_b1425_determinism.py"; s = tt.read_text(encoding="utf-8")
old = '64: "sixty-four", 65: "sixty-five"}'; assert s.count(old) == 1
s = s.replace(old, '64: "sixty-four", 65: "sixty-five", 66: "sixty-six", ' + ", ".join('%d: "%s"' % kv for kv in sorted(W.items())) + "}")
tt.write_text(s, encoding="utf-8")
print("apply3b done; RETRACTIONS rows:", n)
