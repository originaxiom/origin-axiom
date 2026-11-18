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
    ticked = re.findall(r"`([0-9a-f]{9})`", text); paths = sorted(set(re.findall(r"`(relays/[\w./-]+\.py)`", text)))
    # MENDED 2026-11-18 (the web seat's finding, its status page section 7.2 item 8): ids were looked for in backticks only, so
    # a note that writes them bare was recorded with 0 commits, as if nothing had been checked.  Now a bare hex word of 7 to
    # 40 characters counts when it names a commit object; a bare word of exactly 9 that names none is listed apart
    # (it may be a commit that does not exist, or a hash of something else: to be read by a person).
    seq = []; bare_unresolved = []
    for m in re.finditer(r"(?<![0-9a-zA-Z_./-])([0-9a-f]{7,40})(?![0-9a-zA-Z_])", text):
        c = m.group(1)
        if c in ticked:
            if c not in seq: seq.append(c)
            continue
        if not re.search(r"[0-9]", c) or not re.search(r"[a-f]", c): continue                       # bare: a plain number or a plain word is not taken
        is_commit = git("rev-parse", "--verify", "--quiet", c + "^{commit}").returncode == 0
        if is_commit and c not in seq: seq.append(c)
        elif len(c) == 9 and not is_commit and c not in bare_unresolved: bare_unresolved.append(c)
    mains = [c for c in seq if not on_branch(c, ref) and on_branch(c, "origin/main")]                # main's own commits, named by the seat: not expected on its branch
    seq = [c for c in seq if c not in mains]
    exist = {c: on_branch(c, ref) for c in seq}
    order = [(a, b, before(a, b)) for a, b in zip(seq, seq[1:]) if exist[a] and exist[b]]
    return {"note": note_path, "commits": seq, "all_on_branch": all(exist.values()), "missing": [c for c, e in exist.items() if not e], "bare_nine_hex_not_commits": bare_unresolved, "mains_commits_named": mains,
            "consecutive_in_order": sum(1 for *_, o in order if o), "consecutive_pairs": len(order), "out_of_order": [(a, b) for a, b, o in order if not o],
            "scripts": {p: static(ref, p) for p in paths}}


if __name__ == "__main__":
    ref = sys.argv[1]; out = []
    for note in sys.argv[2:]:
        r = trail(ref, note); out.append(r)
        print("%s: %d commits named, all on the branch: %s%s; in the order named: %d of %d consecutive pairs%s" % (
            note.split("/")[-1], len(r["commits"]), r["all_on_branch"], "" if r["all_on_branch"] else " (on neither the seat's branch nor main: %s)" % r["missing"], r["consecutive_in_order"], r["consecutive_pairs"],
            "" if not r["out_of_order"] else " (not in order: %s)" % r["out_of_order"]) + ("" if not r["bare_nine_hex_not_commits"] else "; bare nine-character hex words that name no commit: %s" % r["bare_nine_hex_not_commits"]) + ("" if not r["mains_commits_named"] else "; main's own commits named: %s" % r["mains_commits_named"]))
        for p, s in r["scripts"].items():
            print("     %s: %s" % (p.split("/")[-1], "not found at the head" if s is None else "%d lines, %d float and %d complex literals, imports %s" % (s["lines"], s["float_literals"], s["complex_literals"], s["imports"])))
    json.dump(out, open(pathlib.Path(__file__).with_name("custody_%s.json" % re.sub(r"\W+", "_", ref.split("/", 1)[1])), "w"), indent=1)
