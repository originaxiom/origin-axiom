"""For arcs whose verdict is PROVED and whose atlas tag is 'dead', print the first line of query.arc_card and of
query.revive, and the meeting-point lines' brackets, at the scratch checkout given as argv[1]."""
import glob, json, os, sys, importlib.util
root = sys.argv[1]
sys.path.insert(0, os.path.join(root, "scripts", "atlas"))
spec = importlib.util.spec_from_file_location("q", os.path.join(root, "scripts/atlas/query.py")); q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
g = q.load()
shown = 0
for pid in sorted(g["probes"], key=lambda s: int(s[1:])):
    p = g["probes"][pid]
    hits = sorted(glob.glob(os.path.join(root, "frontier", pid + "_*", "arc_verdict.json")))
    v = json.load(open(hits[0], encoding="utf-8")).get("verdict")
    if v == "PROVED" and p["status"] == "dead":
        print("arc_card :", q.arc_card(pid, g)["text"].splitlines()[0][:100])
        print("revive   :", q.revive(pid, g)["text"].splitlines()[0][:100])
        shown += 1
        if shown == 3: break
mp = q.meeting_points(g)["text"].splitlines()
print("meet     :", mp[1][:100] if len(mp) > 1 else "")
cc = q.context_card(g)["text"].splitlines()
print("card     :", cc[1][:140])
r = q.resolutions_for(g["obstacles"][0], g)["text"].splitlines()[0]
print("obstacle :", r)
