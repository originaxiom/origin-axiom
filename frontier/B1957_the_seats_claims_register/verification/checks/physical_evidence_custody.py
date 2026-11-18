"""B1957: the physical lane's package 'all seats, main preparation' (2026-11-16): its seventeen findings F01 to F17 on
other seats' sources rest on quotations it pinned in two files (commit, path, line, quotation, sha256 of the whole
file).  This holds every one of them against the repository's own objects: the file at that commit has that sha256,
and its line of that number contains the quotation.  The seats' scripts are read as bytes and text; none is run.
Needs the seats' branches fetched (git fetch origin); a commit that is not present is reported, not skipped.
Also: the heads its coverage table names are commits of the branches it names them for; the change between the two
heads of F08 is four files; the function F11 names is in the other seat's script and not in the lane's own.
Run from anywhere inside the repository:  python3 physical_evidence_custody.py"""
import functools, hashlib, json, subprocess, collections
print = functools.partial(print, flush=True)
LANE = "8d5c91032"; DIR = "reports/physical_bridge_2026_09_05/all_seats_main_preparation_2026_11_16/"
FILES = ["QUOTED_SOURCE_EVIDENCE.json", "LATE_CLOSURE_QUOTED_EVIDENCE.json"]


def blob(commit, path):
    r = subprocess.run(["git", "show", "%s:%s" % (commit, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


if __name__ == "__main__":
    tot = collections.Counter(); per = collections.defaultdict(collections.Counter); bad = []
    for name in FILES:
        raw = blob(LANE, DIR + name); assert raw is not None, name
        items = json.loads(raw)["items"]
        for it in items:
            f = it.get("finding", "?"); b = blob(it["commit"], it["path"])
            if b is None: tot["missing"] += 1; bad.append((f, it["commit"][:9], it["path"], "the file is not present at that commit")); continue
            sha_ok = hashlib.sha256(b).hexdigest() == it["sha256"]; lines = b.decode("utf-8", "replace").split("\n")
            ln = it.get("line"); q = it.get("quote", "")
            if isinstance(ln, int) and 1 <= ln <= len(lines): at = q.strip() in lines[ln - 1] or lines[ln - 1].strip() in q
            else: at = False
            anywhere = q.strip() in b.decode("utf-8", "replace")
            tot["items"] += 1; tot["sha256 right"] += sha_ok; tot["quotation at its line"] += at; tot["quotation in the file"] += anywhere
            per[f]["items"] += 1; per[f]["held"] += (sha_ok and at)
            if not (sha_ok and at): bad.append((f, it["commit"][:9], it["path"].split("/")[-1], ln, "sha256 %s, at its line %s, in the file %s" % (sha_ok, at, anywhere)))
        print("%s: %d items" % (name, len(items)))
    print("all: %s" % dict(tot))
    print("by finding (held / items): %s" % {k: "%d/%d" % (v["held"], v["items"]) for k, v in sorted(per.items())})
    print("not held as pinned: %s" % (bad if bad else "none"))
    table = blob(LANE, DIR + "BRANCH_COVERAGE.md").decode(); rows = [l.split("|") for l in table.split("\n") if l.startswith("| `origin/")]
    okh = 0; badh = []
    for r in rows:
        br = r[1].strip().strip("`"); hd = r[2].strip().strip("`")
        ok = subprocess.run(["git", "merge-base", "--is-ancestor", hd, br], capture_output=True).returncode == 0
        okh += ok
        if not ok: badh.append((br, hd))
    print("the coverage table: %d branches; the head named is a commit of that branch for %d; not so: %s" % (len(rows), okh, badh if badh else "none"))
    st = subprocess.run(["git", "diff", "--name-only", "989dd8ed3", "e6129316e"], capture_output=True, text=True).stdout.split()
    g4 = blob("844db35d0", "relays/agy002_closure_g4/verify_closure_g4.py").decode(); own = blob(LANE, "reports/physical_bridge_2026_09_05/registered_domain_index_join_2026_11_16/verification/checks.py").decode()
    print("F08: files changed between the two heads: %d; F11: 'y3_from_sm' occurs %d times in the other seat's first gate-4 script and %d times in the lane's own checker" % (len(st), g4.count("y3_from_sm"), own.count("y3_from_sm")))
