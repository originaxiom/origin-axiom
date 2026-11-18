"""B1957: the physical lane's reply to main's message M12 (its M12_RECORD_REVIEW.md and sender note at 01dc0774f): what it
says of main's records, held against those records at the commit it read, dbd7c24e3, and against main's own outputs
(data-free; nothing of the lane's is run).  Its mathematical statements are in physical_c8_magnetic.py (G9) and
physical_c8_dominant.py (A8).
 R1  the verdicts of the records it names, at dbd7c24e3.     R2  the figures it quotes from main's outputs.
 R3  the line of the cusp paragraph in physical-m9-03."""
import json, pathlib, re, subprocess
HERE = pathlib.Path(__file__).resolve().parent; ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
rec = lambda rid: json.loads(subprocess.run(["git", "show", "dbd7c24e3:frontier/B1957_the_seats_claims_register/verification/records/%s.json" % rid], capture_output=True, text=True, cwd=ROOT).stdout)
said = {"physical-m9-03": "PARTIAL", "physical-c8-02": "PARTIAL", "physical-c8-04": "PARTIAL", "physical-c8-07": "PARTIAL", "physical-c8-10": "CONDITIONAL"}
got = {r: rec(r)["verdict"] for r in said}; c8 = [rec("physical-c8-%02d" % i)["verdict"] for i in range(1, 12)]
print("R1: at dbd7c24e3: %s, as the lane says: %s; physical-m9-03 holds %d units (the lane: seven); the eleven records physical-c8-01 to -11 exist: %s; physical-ij-03, physical-c3e-02, physical-m10r-01 and -02 exist: %s"
      % (got, got == said, len(rec("physical-m9-03")["units"]), len(c8) == 11, all(rec(r)["id"] == r for r in ("physical-ij-03", "physical-c3e-02", "physical-m10r-01", "physical-m10r-02"))))
n1 = (HERE / "physical_m9_review_run.txt").read_text().split("\n")[0]; kc = (HERE / "physical_outputs_key_coverage_run.txt").read_text()
grp = dict((k, int(v)) for k, v in re.findall(r"([a-z_]+) (\d+)", kc.split("compared, by group:")[1].split("\n")[0]))
print("R2: main's control of the corrected bound prints 13/16 and 16/13: %s; main's boundary script compares %s keys, by group %s (the lane: 8 + 5 + 18 + 2 = 33); its endgame script %s (the lane: 45)"
      % ("13/16" in n1 and "16/13" in n1, re.search(r"physical_boundary_outputs: .*recomputation: (\d+)", kc).group(1), list(grp.values()), re.search(r"physical_endgame_outputs: .*recomputation: (\d+)", kc).group(1)))
print("R3: the units of physical-m9-03 at dbd7c24e3 include the cusp paragraph at line 97 (88 before main's dated insertion): %s" % any(u.endswith("CUSP_GAUGE_INVERSE_AND_LOCAL_STATIONARY_BRANCH:97") for u in rec("physical-m9-03")["units"]))
