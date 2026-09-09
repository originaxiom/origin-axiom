"""R39 disposition (the physics-seat evaluation branch's 'recovered Z1 ladder'): the deleted
frontier/B775_phase2_wave1/cells/_verify_Z1/ directory (removed by c8f3167c as a scratch copy) held a
compute.py BYTE-IDENTICAL to the live cell frontier/B775_phase2_wave1/cells/P2W4-Z1/compute.py, whose
results.json carries the ladder to k=28 with certificates. Nothing was ever lost. This script compares
(a) this bench's rerun of that script to k=22 (z1_rerun_output.txt, 'Z1 rc=0'), (b) main's banked ladder,
(c) the deleted copy's partial.json (z1_deleted_cell_partial.json, recovered from c8f3167c^ for the record).
Run from the repo root."""
import json, re, pathlib, subprocess
H = pathlib.Path(__file__).resolve().parent
main = json.load(open("frontier/B775_phase2_wave1/cells/P2W4-Z1/results.json"))
banked = {r["k"]: (str(r["Z"]).replace(" ", ""), r["cert"]) for r in main["ladder"]}
rerun = {}
for line in open(H / "z1_rerun_output.txt"):
    m = re.match(r"\s*(\d+)\s+(\d+)\s+(\d+)\s+(.+?)\s+OK\s+\[", line)
    if m:
        rerun[int(m.group(1))] = m.group(4).strip().replace(" ", "")
orig = json.load(open(H / "z1_deleted_cell_partial.json"))
rows = orig if isinstance(orig, list) else orig.get("ladder", [])
orig_l = {r["k"]: str(r["Z"]).replace(" ", "") for r in rows}
# the deleted copy was byte-identical to the live cell (git is the witness; skipped if git is unavailable)
try:
    old = subprocess.run(["git", "show", "c8f3167c^:frontier/B775_phase2_wave1/cells/_verify_Z1/compute.py"],
                         capture_output=True, text=True, check=True).stdout
    same = old == open("frontier/B775_phase2_wave1/cells/P2W4-Z1/compute.py", encoding="utf-8").read()
    print("deleted _verify_Z1/compute.py == live P2W4-Z1/compute.py (byte-identical):", same)
except Exception as e:  # noqa: BLE001
    print("git witness unavailable:", type(e).__name__)
print("main banked kmax:", main["kmax"], "| rerun levels:", len(rerun), "| deleted-copy partial levels:", len(orig_l))
mism = [(k, rerun[k], banked[k][0]) for k in rerun if banked[k][0] != rerun[k]]
print("rerun == main banked at levels:", len(rerun) - len(mism), "/", len(rerun), " mismatches:", mism)
print("rerun == deleted partial at levels:", sum(1 for k in rerun if orig_l.get(k) == rerun[k]), "/", len(rerun))
print("main certificates all True for k<=22:", all(banked[k][1] for k in rerun))
print("Z18 =", rerun[18], "| Z21 =", rerun[21], "| Z22 =", rerun[22])
print("irrational levels (5|kappa forced):", [(k, k + 12) for k in rerun if "sqrt" in rerun[k]],
      "| rational levels with 5|kappa (the converse fails):", [k for k in rerun if (k + 12) % 5 == 0 and "sqrt" not in rerun[k]])
