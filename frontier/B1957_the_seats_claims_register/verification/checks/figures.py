"""B1957: two mechanical checks of a seat's results note against its own sealed files, without running any of its code.
figures:   every number a line of the note quotes beside a named output file is searched among that file's numeric leaves
           (to the precision the note prints); what is not found is listed.  It checks that the note reports its sealed
           output; it does not check that the output is right.
manifests: every SCRIPT_SHA256.txt and OUTPUT_SHA256.txt under a folder is compared with the SHA-256 of the file it names,
           as stored at the branch's head."""
import hashlib, json, pathlib, re, subprocess, sys
git = lambda *a: subprocess.run(["git", *a], capture_output=True)
NUM = re.compile(r"(?<![\w./^-])[-+]?\d+\.\d+(?:e[-+]?\d+)?(?![\w/])|(?<![\w./^-])[-+]?\d+e[-+]?\d+(?![\w/])")


def leaves(x, out):
    if isinstance(x, dict):
        for v in x.values(): leaves(v, out)
    elif isinstance(x, list):
        for v in x: leaves(v, out)
    elif isinstance(x, bool): pass
    elif isinstance(x, (int, float)): out.append(float(x))
    elif isinstance(x, str):
        for t in NUM.findall(x):
            try: out.append(float(t))
            except ValueError: pass
    return out


def matches(tok, vals):
    t = float(tok); m = re.match(r"[-+]?(\d+)\.?(\d*)(?:e([-+]?\d+))?", tok.lstrip("+-")); digs = len(m.group(2)); ex = int(m.group(3) or 0)
    tol = 10.0 ** (ex - digs) * 1.0000001                      # one unit of the last printed digit: rounding or truncation
    return any(abs(v - t) <= tol or abs(abs(v) - abs(t)) <= tol for v in vals)


def figures(ref, note):
    text = git("show", "%s:%s" % (ref, note)).stdout.decode(); rep = []
    files = sorted(set(re.findall(r"`(relays/[\w./-]+\.json)`", text))); data = {}
    for f in files:
        raw = git("show", "%s:%s" % (ref, f)).stdout
        if raw: data[f] = leaves(json.loads(raw), [])
    allv = [v for vs in data.values() for v in vs]
    for i, line in enumerate(text.splitlines(), 1):
        toks = NUM.findall(re.sub(r"`relays/[^`]*`", "", line))
        if not toks: continue
        named = [f for f in files if f in line and f in data]; pool = [v for f in named for v in data[f]] or allv
        miss = [t for t in toks if not matches(t, pool)]
        rep.append({"line": i, "quoted": len(toks), "found": len(toks) - len(miss), "not_found": miss, "against": "the file the line names" if named else "all the note's output files"})
    return {"note": note, "outputs_read": sorted(data), "outputs_missing": [f for f in files if f not in data], "lines": rep}


def manifests(ref, folder):
    out = []; ls = git("ls-tree", "-r", "--name-only", ref, folder).stdout.decode().split()
    for p in ls:
        if not p.endswith("_SHA256.txt"): continue
        for row in git("show", "%s:%s" % (ref, p)).stdout.decode().splitlines():
            m = re.match(r"([0-9a-f]{64})\s+\*?(\S+)", row.strip())
            if not m: continue
            cand = [q for q in ls if q.endswith("/" + m.group(2).split("/")[-1]) and q.rsplit("/", 1)[0] == p.rsplit("/", 1)[0]]
            got = hashlib.sha256(git("show", "%s:%s" % (ref, cand[0])).stdout).hexdigest() if cand else None
            out.append({"manifest": p, "file": m.group(2), "match": got == m.group(1), "found": bool(cand)})
    return out


if __name__ == "__main__":
    ref = sys.argv[1]; res = {"ref": ref, "notes": [], "manifests": []}
    for a in sys.argv[2:]:
        if a.endswith(".md"):
            r = figures(ref, a); res["notes"].append(r); q = sum(l["quoted"] for l in r["lines"]); f = sum(l["found"] for l in r["lines"])
            print("%s: %d output files read%s; %d numbers quoted on %d lines, %d found in the sealed outputs" % (a.split("/")[-1], len(r["outputs_read"]), "" if not r["outputs_missing"] else " (%d not at the head)" % len(r["outputs_missing"]), q, len(r["lines"]), f))
            for l in r["lines"]:
                if l["not_found"]: print("     line %d: not found: %s" % (l["line"], ", ".join(l["not_found"])))
        else:
            m = manifests(ref, a); res["manifests"] += m
            print("%s: %d manifest entries, %d match the file's SHA-256, %d name a file not beside them" % (a, len(m), sum(x["match"] for x in m), sum(not x["found"] for x in m)))
    json.dump(res, open(pathlib.Path(__file__).with_name("figures_%s.json" % re.sub(r"\W+", "_", ref.split("/", 1)[1])), "w"), indent=1)
