"""main's unseen cases for series 2 of WP-0.7 (U10.a-c, U19.a-b, U11.a-b, U12.a-c, U13.a-c), run on main's head with series 1 and 2 applied.
Each case is planted in the scratch checkout, COMMITTED there, and every gate is run through the runner.  Local: not in the repository."""
import base64, glob, json, os, pathlib, re, subprocess, sys
T = pathlib.Path(__file__).resolve().parent
W = T.parent / "wt_s1"
HEAD = subprocess.run(["git", "-C", str(W), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip() if len(sys.argv) < 2 else sys.argv[1]

def git(*a):
    return subprocess.run(["git", "-C", str(W), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)

def gates():
    env = {k: v for k, v in os.environ.items() if not re.fullmatch(r"OA_[A-Z_]*TODAY", k) and k != "GIT_DIR"}
    r = subprocess.run([sys.executable, str(W / "scripts/gates/gates.py")], cwd=str(W), env=env, capture_output=True, text=True)
    res = {}
    for l in r.stdout.splitlines():
        m = re.match(r"\s*(PASS|FAIL|SKIP)\s+([\w-]+):\s?(.*)$", l)
        if m:
            res[m.group(2)] = (m.group(1), m.group(3))
    return res

def reset():
    git("reset", "-q", "--hard", HEAD); git("clean", "-fdq")

def P(rel):
    return W / rel

def three_rows():
    f = P("docs/IDENTIFICATION_LEDGER.md"); t = f.read_text(encoding="utf-8").rstrip("\n")
    f.write_text(t + "".join("\n| I-9%d | **a planted identification, number %d** | planted | planted | UNEARNED | planted |" % (k, k) for k in (1, 2, 3)) + "\n", encoding="utf-8")

def tokens():
    src = P("scripts/gates/gates.py").read_text(encoding="utf-8")
    m = re.search(r"_VENDOR_TOKS = tuple\(base64\.b64decode\(b\)\.decode\(\) for b in\s*\((.*?)\)\)", src, flags=re.S)
    return [base64.b64decode(b).decode() for b in re.findall(r'b?"([A-Za-z0-9+/=]+)"', m.group(1))]

def u10a():
    P("docs/IDENTIFICATION_BASELINE.json").write_text('{"unearned": 20, "rows": [', encoding="utf-8"); three_rows()
def u10b():
    f = P("docs/IDENTIFICATION_BASELINE.json"); d = json.loads(f.read_text(encoding="utf-8")); d["unearned"] += 3; d["total_rows"] += 3
    f.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"); three_rows()
def u10c():
    f = P("docs/IDENTIFICATION_BASELINE.json"); d = json.loads(f.read_text(encoding="utf-8")); d["unearned_rows"] = d.pop("unearned")
    f.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"); three_rows()
def u19a():
    tok = tokens()[0]
    f = P("docs/ATTRIBUTION_BASELINE.json"); d = json.loads(f.read_text(encoding="utf-8")); d["frozen"]["docs/A_PLANTED_PAGE.md"] = 4
    f.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    P("docs/A_PLANTED_PAGE.md").write_text("# a planted page\n\n" + " ".join("made with %s." % tok for _ in range(4)) + "\n", encoding="utf-8")
def u19b():
    tok = tokens()[0]
    f = P("docs/ATTRIBUTION_BASELINE.json"); d = json.loads(f.read_text(encoding="utf-8"))
    big = [k for k, v in d["frozen"].items() if v >= 4 and P(k).is_file()]
    low, high = big[0], next(k for k in d["frozen"] if k.endswith(".md") and k != big[0] and P(k).is_file())
    d["frozen"][low] -= 2; d["frozen"][high] += 2
    f.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    g = P(high); g.write_text(g.read_text(encoding="utf-8").rstrip("\n") + "\n\nmade with %s and %s.\n" % (tok, tok), encoding="utf-8")
    return "lowered %s, raised %s" % (low, high)
def u11a():
    f = P("docs/RETRACTED_PHRASES.md"); L = f.read_text(encoding="utf-8").split("\n")
    first = next(k for k, l in enumerate(L) if l.startswith("| "))
    f.write_text("\n".join(L[:first + 2]) + "\n", encoding="utf-8")                       # the table's two header lines and nothing below
def u11b():
    f = P("docs/RETRACTED_PHRASES.md"); L = f.read_text(encoding="utf-8").split("\n")
    rows = [k for k, l in enumerate(L) if re.match(r"^\| \d+ \|", l)]
    last = rows[-10:]
    phrase = re.search(r"`([^`]+)`", L[last[0]]).group(1)
    f.write_text("\n".join(l for k, l in enumerate(L) if k not in last), encoding="utf-8")
    r = P("README.md"); r.write_text(r.read_text(encoding="utf-8").rstrip("\n") + "\n\nA planted line: " + phrase + ".\n", encoding="utf-8")
    return "pasted: " + phrase[:50]
def u12a():
    n = 0
    for f in glob.glob(str(W / "frontier" / "*" / "verification" / "test_*.py")):
        os.remove(f); n += 1
    return "%d locks deleted" % n
def u12b():
    n = 0
    for f in glob.glob(str(W / "tests" / "test_b*.py")):
        p = pathlib.Path(f); p.write_text(p.read_text(encoding="utf-8").rstrip("\n") + "\n\nimport pytest as _planted\npytestmark = _planted.mark.skip\n", encoding="utf-8"); n += 1
    return "%d files made to skip (the mark appended at the end, where the case said the second line: the same effect without breaking a docstring)" % n
def u12c():
    fs = sorted(glob.glob(str(W / "tests" / "test_b*.py")))[:20]
    for f in fs:
        git("mv", f, f.replace("/tests/test_b", "/tests/tst_b"))
    return "%d files renamed" % len(fs)
def u13a():
    f = P("docs/LAW_MAP.md"); L = f.read_text(encoding="utf-8").split("\n")
    rows = [k for k, l in enumerate(L) if l.startswith("| **")]
    drop = set(rows[1::2])
    f.write_text("\n".join(l for k, l in enumerate(L) if k not in drop), encoding="utf-8")
    return "%d of %d rows deleted" % (len(drop), len(rows))
def u13b():
    f = P("docs/THEOREM_LEDGER.md"); t = f.read_text(encoding="utf-8")
    f.write_text(t[:t.index("**C2 [")], encoding="utf-8")
def u13c():
    f = P("docs/IDENTIFICATION_LEDGER.md"); L = f.read_text(encoding="utf-8").split("\n")
    f.write_text("\n".join(l for l in L if not re.match(r"^\|\s*I-\d+\s*\|", l)), encoding="utf-8")

CASES = [("U10.a", u10a, ["identification-register"]), ("U10.b", u10b, ["identification-register"]), ("U10.c", u10c, ["identification-register"]),
         ("U19.a", u19a, ["attribution"]), ("U19.b", u19b, ["attribution"]), ("U11.a", u11a, ["retraction-sweep"]), ("U11.b", u11b, ["retraction-sweep"]),
         ("U12.a", u12a, None), ("U12.b", u12b, None), ("U12.c", u12c, None), ("U13.a", u13a, None), ("U13.b", u13b, ["chain-locks"]), ("U13.c", u13c, ["identification-register"])]
reset()
base = gates(); base_fail = sorted(k for k, v in base.items() if v[0] == "FAIL")
print("series head", HEAD[:9], "| gates", len(base), "| failing before any plant:", base_fail, flush=True)
OUT = {"head": HEAD, "failing before any plant": base_fail}
for name, plant, must in CASES:
    reset()
    note = plant() or ""
    git("add", "-A"); c = git("commit", "-q", "-m", "planted case " + name)
    # ADDED 2026-11-12 (Review 80; owed by main's word in its third folder for the builder, section 6, item 4).  A PLANT THAT
    # CHANGES NOTHING STOPS THE RUN.  A case is committed in the scratch checkout.  Where the case had changed nothing there was
    # nothing to commit: the gates were then run on the tree as it stood, and the case was written down with "committed": false
    # and "not caught".  No case of the kept output is so; the run now ends there, with a sentence.
    if c.returncode != 0:
        reset()
        raise SystemExit("STOPPED at %s: the planted case changed nothing in the checkout, and no commit was made. Gates that pass on it show nothing: mend the case" % name)
    res = gates()
    new = sorted(k for k, v in res.items() if v[0] == "FAIL" and k not in base_fail)
    caught = bool(new) if must is None else all(m in new for m in must)
    OUT[name] = {"note": note, "committed": c.returncode == 0, "named gate": must, "gates newly failing": {k: res[k][1][:260] for k in new}, "CAUGHT": caught}
    print("%-6s committed=%s caught=%s  newly failing: %s  %s" % (name, c.returncode == 0, caught, new, note[:90]), flush=True)
    (T / "unseen_s2.json").write_text(json.dumps(OUT, indent=1, ensure_ascii=False))
reset()
print("written", flush=True)
