"""B1662's re-grades (the owner's ruling of 2026-10-16 on P-179): a dated addendum on each of the six arcs the sweep found
(§9.3 of speculations/S_THE_PUSH_BACK.md), and a bracket on the three re-graded arcs' claim lines. Correcting old
bankings: targeted, the computations kept."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4] if (pathlib.Path(__file__).resolve().parents[4] / "frontier").is_dir() else next(
    d for d in pathlib.Path(__file__).resolve().parents if (d / "frontier").is_dir())
HEAD = "\n\n## Addendum (2026-10-16, B1662): the pull-back acts on the records (GENESIS v1.48)\n\n"
ADD = {
 "B1482": ("- **Re-graded, wording only.** The owner ruled (P-179, by the math) that the inverse moves are legal (GM5b adopted). "
           "So §2's \"positivity is what excludes\" the − states, and \"the handed states are precisely what a chosen restriction "
           "removes\", hold of the forward semigroup only. Under GM5b, −I = (L·R⁻¹·L)² is generated and the − states are "
           "reachable.\n- **What stands.** S1–S4 are elementary facts and unchanged: no word in L, R and P gives a − state, "
           "and −I brings no inverse letters with it. §3's reading (cancelling as the negation −I) and B1662's (cancelling as "
           "the inverse move) agree on the outcome: the sign is generated.\n",
           "[Re-graded 2026-10-16 by B1662 (GENESIS v1.48): GM5b adopted, so 'positivity excludes the - states' holds of the forward semigroup only; S1-S4 stand.]"),
 "B1479": ("- **Re-graded, wording only.** §2's \"the part of the state space the genesis does not yet generate\" is "
           "superseded. Under GM5b (adopted, P-179) the − states are generated, so the place where a hand can be registered "
           "on a fermion is generated, not added.\n- **What stands.** P1–P3 and the census laws stand, as facts about reachable "
           "states.\n",
           "[Re-graded 2026-10-16 by B1662 (GENESIS v1.48): under GM5b the - states are generated; 'not yet generate' superseded; P1-P3 stand.]"),
 "B1083": ("- **Re-graded: the arrow re-homed.** This arc places the arrow in the register's positivity, \"present … as "
           "non-invertibility\". Under GM5b (adopted, P-179) every move is invertible, so that home is gone.\n"
           "- **The arrow survives as escape.** At equal strength the walk on SL(2, ℤ) moves away from its start at a positive "
           "rate with no preference (0.099 per step; Furstenberg; B1662's W3). \"The arrow was never a choice\" holds, now as "
           "a theorem about the motion rather than a restriction on states. Which end the motion reaches is the side "
           "(GENESIS v1.48, FK6).\n- **What stands.** The torsor's C and P bits, det M = −1 and M² = RL stand. "
           "'bb' having no preimage holds of the forward monoid.\n",
           "[Re-graded 2026-10-16 by B1662 (GENESIS v1.48): GM5b adopted, so non-invertibility is no longer the arrow's home; the arrow survives as escape (positive rate at equal strength, Furstenberg); the C and P bits stand.]"),
 "B1640": ("- **A scope sentence.** v1.42 scoped GM5d to the semigroup of updates, because ⟨L, R⟩ contains −I. Under GM5b "
           "(adopted, P-179) the updates are the group. The scoping is consistent with the ruling, which it anticipated.\n", None),
 "B1454": ("- **A scope sentence.** The root's uniqueness is stated with and without positivity (G1), so it holds under GM5b "
           "(adopted, P-179). GM5d's status line is re-read in GENESIS v1.48.\n", None),
 "B1422": ("- **A scope sentence.** The a = b = −1 branch noted here (\"over ℤ alone ab = 1 also admits a = b = −1\") is a "
           "reachable state under GM5b (adopted, P-179). The 144 → 1 collapse is stated for the positive sector and stands "
           "there.\n", None),
}
for arc, (text, bracket) in ADD.items():
    d = next((ROOT / "frontier").glob(arc + "_*"))
    f = d / "FINDINGS.md"; s = f.read_text(encoding="utf-8")
    if "## Addendum (2026-10-16, B1662)" not in s:
        f.write_text(s.rstrip("\n") + HEAD + text, encoding="utf-8")
    if bracket:
        v = d / "arc_verdict.json"; raw = v.read_text(encoding="utf-8"); j = json.loads(raw)
        if "B1662" not in j["claim_one_line"]:
            j["claim_one_line"] = j["claim_one_line"].rstrip() + " " + bracket
            orig = json.loads(raw)
            fmt = next((i, a) for i in (1, 2, 4) for a in (False, True) if json.dumps(orig, indent=i, ensure_ascii=a).rstrip("\n") == raw.rstrip("\n"))
            v.write_text(json.dumps(j, indent=fmt[0], ensure_ascii=fmt[1]) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")
    print(arc, "ok")
