"""Review 84: the readers' quotations checked by machine, each AT THE PATH ITS FINDING CITES (Review 83's check searched
the whole window's text, which a reader of this review pointed out).  The reading copy was main's head 1fc1e224e with
the seven plants of plants.json applied; it is rebuilt here from that commit and that file, so the check can be rerun
while the commit exists.  For each finding: is the quotation in the cited file (whitespace-normalised), is it at the
cited line (within two lines), and is the finding at a planted line.  Usage: python3 quote_check.py"""
import json, pathlib, re, subprocess, hashlib
HERE = pathlib.Path(__file__).resolve().parent; ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
READ = "1fc1e224e"; raw = (HERE / "plants.json").read_text(); PLANTS = json.loads(raw)
assert hashlib.sha256(raw.encode()).hexdigest() == (HERE / "plants_sha256.txt").read_text().strip()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
def reading_copy(path):
    r = subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (READ, path)], capture_output=True)
    if r.returncode != 0: return None
    t = r.stdout.decode("utf-8", "replace")
    for p in PLANTS:
        if p["file"] == path: assert t.count(p["old"]) == 1; t = t.replace(p["old"], p["new"])
    return t
if __name__ == "__main__":
    caught = {}
    for name in ("A", "B", "C"):
        t = (HERE / ("READING_%s.md" % name)).read_text(); blocks = re.findall(r"(?ms)^### (F-R84-%s\d+)\n(.*?)(?=^### F-R84-|^## )" % name, t)
        n = infile = atline = 0; missing = []
        for fid, body in blocks:
            mf = re.search(r"\*\*File:\*\* (\S+?)(?:,| \(|$)", body); ml = re.search(r"line (\d+)", body); mq = re.search(r"\*\*Verbatim quotation:\*\* `(.+?)`", body)
            if not (mf and mq): missing.append((fid, "not parsed")); continue
            n += 1; path = mf.group(1).strip(); txt = reading_copy(path); q = norm(mq.group(1))
            if txt is None: missing.append((fid, "no such file: " + path)); continue
            ok = q in norm(txt); infile += ok
            if not ok: missing.append((fid, q[:70]))
            if ok and ml:
                ln = int(ml.group(1)); lines = txt.split("\n"); win = norm(" ".join(lines[max(0, ln - 3):ln + 2])); atline += (q in win) or (norm(lines[ln - 1]) in q if 0 < ln <= len(lines) and len(norm(lines[ln - 1])) > 20 else False)
            for p in PLANTS:
                if p["file"] == path and ok:
                    lines = txt.split("\n"); pl = next(i for i, l in enumerate(lines) if p["new"].split("\n")[0] in l) + 1
                    if ml and int(ml.group(1)) == pl: caught.setdefault(p["id"], []).append(fid)
        print("reader %s: %d findings; %d quotations parsed; %d found in the cited file; %d at the cited line; not found: %s" % (name, len(blocks), n, infile, atline, missing if missing else "none"))
    print("plants caught (plant: the finding at its line): %s; missed: %s" % ({k: v for k, v in sorted(caught.items())}, [p["id"] for p in PLANTS if p["id"] not in caught] or "none"))
