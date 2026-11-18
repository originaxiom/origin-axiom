"""The physical lane's answer to M13 to M16 (its branch at ddae296f0): what it says that main can compute.
 Q1  the X-FRONTIER-3 producer and its output: the same git blob at af08bc3d2 and at agy-exp's head harvested (d7bb27195).
 Q2  C3i's scope commit 3cbb86bd2 adds the card; M15 at f1efc59dd records C3h's global persistence as conditional; M16 is on
     main at f1efc59dd."""
import subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout.strip()
for f in ("relays/x_frontier_3_verify/verify_x_frontier_3.py", "relays/x_frontier_3_verify/verify_x_frontier_3_out.json"):
    a, b = git("rev-parse", "af08bc3d2:" + f), git("rev-parse", "d7bb27195:" + f)
    print("Q1: %s: blob at af08bc3d2 %s, at d7bb27195 %s, the same: %s" % (f.split("/")[-1], a[:12], b[:12], a == b))
added = git("diff", "--name-status", "3cbb86bd2~1", "3cbb86bd2")
page = git("show", "f1efc59dd:docs/seats/physical.md"); m15 = page[page.index("### M15"):]; m15 = m15[:m15.index("\n### ", 5)]
print("Q2: 3cbb86bd2 adds the card C3i: %s; M15 records C3h's persistence argument as conditional: %s; M16 on main at f1efc59dd: %s"
      % ("A\trelays/cards/PHYSICAL_C3I_GLOBAL_CYCLIC_CROSS_FORM_JOIN_2026-11-18.md" in added, "conditional" in m15.split("\n")[0].lower(), "### M16" in page))
