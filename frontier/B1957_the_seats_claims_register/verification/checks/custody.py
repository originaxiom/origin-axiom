"""B1957: custody and static checks of a seat's sealed trail, without running any of its code.
For a results note: every commit it names exists on the seat's branch; the commits named for the card, the script and the
output are in that order of ancestry; and a named script, read as text and parsed, has the float and complex literals and
the imports the note says it has."""
import ast, json, pathlib, re, subprocess, sys
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True)


def on_branch(c, ref):
    return git("merge-base", "--is-ancestor", c, ref).returncode == 0


def before(a, b):
    return git("merge-base", "--is-ancestor", a, b).returncode == 0 and git("rev-parse", a).stdout != git("rev-parse", b).stdout


def static(ref, path):
    src = git("show", "%s:%s" % (ref, path)).stdout
    if not src: return None
    t = ast.parse(src); fl = cx = 0; imps = set()
    for n in ast.walk(t):
        if isinstance(n, ast.Constant) and isinstance(n.value, float): fl += 1
        if isinstance(n, ast.Constant) and isinstance(n.value, complex): cx += 1
        if isinstance(n, ast.Import): imps |= {a.name.split(".")[0] for a in n.names}
        if isinstance(n, ast.ImportFrom) and n.module: imps.add(n.module.split(".")[0])
    return {"lines": src.count("\n") + 1, "float_literals": fl, "complex_literals": cx, "imports": sorted(imps)}


def trail(ref, note_path):
    text = git("show", "%s:%s" % (ref, note_path)).stdout
    commits = re.findall(r"`([0-9a-f]{9})`", text); paths = sorted(set(re.findall(r"`(relays/[\w./-]+\.py)`", text)))
    seq = []
    for c in commits:
        if c not in seq: seq.append(c)
    exist = {c: on_branch(c, ref) for c in seq}
    order = [(a, b, before(a, b)) for a, b in zip(seq, seq[1:]) if exist[a] and exist[b]]
    return {"note": note_path, "commits": seq, "all_on_branch": all(exist.values()), "missing": [c for c, e in exist.items() if not e],
            "consecutive_in_order": sum(1 for *_, o in order if o), "consecutive_pairs": len(order), "out_of_order": [(a, b) for a, b, o in order if not o],
            "scripts": {p: static(ref, p) for p in paths}}


if __name__ == "__main__":
    ref = sys.argv[1]; out = []
    for note in sys.argv[2:]:
        r = trail(ref, note); out.append(r)
        print("%s: %d commits named, all on the branch: %s%s; in the order named: %d of %d consecutive pairs%s" % (
            note.split("/")[-1], len(r["commits"]), r["all_on_branch"], "" if r["all_on_branch"] else " (missing %s)" % r["missing"], r["consecutive_in_order"], r["consecutive_pairs"],
            "" if not r["out_of_order"] else " (not in order: %s)" % r["out_of_order"]))
        for p, s in r["scripts"].items():
            print("     %s: %s" % (p.split("/")[-1], "not found at the head" if s is None else "%d lines, %d float and %d complex literals, imports %s" % (s["lines"], s["float_literals"], s["complex_literals"], s["imports"])))
    json.dump(out, open(pathlib.Path(__file__).with_name("custody_%s.json" % re.sub(r"\W+", "_", ref.split("/", 1)[1])), "w"), indent=1)
