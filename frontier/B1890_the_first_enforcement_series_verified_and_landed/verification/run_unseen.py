"""B1890: main's unseen cases for series 1 of WP-0.7 (U9.a-c, U15.a-c, U22.a-c), as they were run on main's head with the four patches applied.

Kept as it was run.  It expects, beside its own folder, a scratch checkout of main with the series applied, named wt_s1; it makes its
exports and its shallow clones beside itself and removes them.  Every gate is run through the runner, as a stranger would run it,
and its line is kept.  Stages: export, shallow, dates, clock."""
import datetime, json, os, pathlib, re, shutil, subprocess, sys
T = pathlib.Path(__file__).resolve().parent
W = T.parent / "wt_s1"
OUT = {}

def sh(args, cwd=None, env=None, check=False):
    return subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True)

def gates(tree, env_extra=None):
    """run the gate runner in `tree`; {gate: (PASS/FAIL/SKIP, detail)}"""
    env = dict(os.environ); env.pop("GIT_DIR", None)
    for k in list(env):
        if re.fullmatch(r"OA_[A-Z_]*TODAY", k):
            env.pop(k)
    env.update(env_extra or {})
    r = sh([sys.executable, str(pathlib.Path(tree) / "scripts" / "gates" / "gates.py")], cwd=str(tree), env=env)
    res = {}
    for l in r.stdout.splitlines():
        m = re.match(r"\s*(PASS|FAIL|SKIP)\s+([\w-]+):\s?(.*)$", l)
        if m:
            res[m.group(2)] = (m.group(1), m.group(3))
    return res, r.returncode

def differ(a, b):
    """gates whose line differs, with timings and counts of seconds taken out"""
    norm = lambda s: re.sub(r"\[\d+(\.\d+)?s\]|\b\d+(\.\d+)? ?s\b", "", s)
    return sorted(k for k in set(a) | set(b) if (a.get(k, ("", ""))[0], norm(a.get(k, ("", ""))[1])) != (b.get(k, ("", ""))[0], norm(b.get(k, ("", ""))[1])))

mod = {}
exec(compile((W / "scripts/gates/gates.py").read_text().split("def run_all")[0], "gates_table", "exec"), mod) if False else None
src = (W / "scripts/gates/gates.py").read_text()
TRACKED = set(re.findall(r'"([\w-]+)"', re.search(r"READS_TRACKED = frozenset\(\{(.*?)\}\)", src, re.S).group(1)))
HISTORY = set(re.findall(r'"([\w-]+)"', re.search(r"READS_HISTORY = frozenset\(\{(.*?)\}\)", src, re.S).group(1)))
head_day = datetime.date.fromisoformat(sh(["git", "-C", str(W), "log", "-1", "--format=%cs", "HEAD"]).stdout.strip())
print("series head", sh(["git", "-C", str(W), "log", "-1", "--format=%h", "HEAD"]).stdout.strip(), "its day", head_day, "| the table: tracked", len(TRACKED), "history", len(HISTORY), flush=True)

stage = sys.argv[1] if len(sys.argv) > 1 else "all"

if stage in ("all", "dates", "clock"):
    base, rc0 = gates(W)
    OUT["baseline"] = {"gates": len(base), "failing": sorted(k for k, v in base.items() if v[0] == "FAIL")}
    print("baseline: %d gates, failing: %s" % (len(base), OUT["baseline"]["failing"]), flush=True)
    seams = ["OA_LEAD_TODAY", "OA_POINT_TODAY", "OA_RELAY_TODAY", "OA_HARVEST_TODAY", "OA_TODAY"]
    for name, days in ((("U15.a/b +400 days", 400), ("U15.a/b -30 days", -30)) if stage != "clock" else ()):
        res, _ = gates(W, {s: (head_day + datetime.timedelta(days=days)).isoformat() for s in seams})
        d = differ(base, res)
        OUT[name] = {"gates whose line changed": d, "lines": {k: [base.get(k), res.get(k)] for k in d}}
        print(name, "-> changed:", d, flush=True)
    # U15.c: the system's date read by a stub: every python the runner starts sees today as the head's day + 400
    stub = T / "stub"; stub.mkdir(exist_ok=True)
    (stub / "sitecustomize.py").write_text('''
import datetime as _d, time as _t
_SHIFT = 400 * 86400
_real_time = _t.time
class _Date(_d.date):
    @classmethod
    def today(cls):
        return cls.fromtimestamp(_real_time() + _SHIFT)
class _DateTime(_d.datetime):
    @classmethod
    def now(cls, tz=None):
        return cls.fromtimestamp(_real_time() + _SHIFT, tz)
    @classmethod
    def today(cls):
        return cls.fromtimestamp(_real_time() + _SHIFT)
    @classmethod
    def utcnow(cls):
        return cls.utcfromtimestamp(_real_time() + _SHIFT)
_d.date, _d.datetime = _Date, _DateTime
_t.time = lambda: _real_time() + _SHIFT
_lt, _gt = _t.localtime, _t.gmtime
_t.localtime = lambda s=None: _lt(_real_time() + _SHIFT if s is None else s)
_t.gmtime = lambda s=None: _gt(_real_time() + _SHIFT if s is None else s)
_sf, _ct, _at = _t.strftime, _t.ctime, _t.asctime
_t.strftime = lambda f, tup=None: _sf(f, _lt(_real_time() + _SHIFT) if tup is None else tup)
_t.ctime = lambda s=None: _ct(_real_time() + _SHIFT if s is None else s)
_t.asctime = lambda tup=None: _at(_lt(_real_time() + _SHIFT) if tup is None else tup)
''')
    probe = sh([sys.executable, "-c", "import datetime,time;print(datetime.date.today(), datetime.datetime.now().date(), time.strftime('%Y-%m-%d'))"], env={**os.environ, "PYTHONPATH": str(stub)})
    print("the stub is live (a python started under it says today is):", probe.stdout.strip(), probe.stderr.strip()[-200:], flush=True)
    res, _ = gates(W, {"PYTHONPATH": str(stub)})
    d = differ(base, res)
    OUT["U15.c the system's date + 400 days"] = {"stub says": probe.stdout.strip(), "gates whose line changed": d, "lines": {k: [base.get(k), res.get(k)] for k in d}}
    print("U15.c -> changed:", d, flush=True)

if stage in ("all", "export"):
    # a minimal export: the gates and their checkers, and the two logs.  A gate of the table must be refused before it reads anything.
    E = T / "export"; shutil.rmtree(E, ignore_errors=True); E.mkdir()
    tar = subprocess.run(["git", "-C", str(W), "archive", "HEAD", "scripts", "PROGRESS_LOG.md", "CHANGELOG.md", "WORKING_RULES.md"], capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", str(E)], input=tar, check=True)
    def table(res):
        t = {k: res.get(k) for k in sorted(TRACKED | HISTORY)}
        return {"refused": sorted(k for k, v in t.items() if v and v[0] == "FAIL" and "refused" in v[1]),
                "failing otherwise": {k: v[1][:110] for k, v in t.items() if v and v[0] == "FAIL" and "refused" not in v[1]},
                "PASSING": {k: v[1][:110] for k, v in t.items() if v and v[0] != "FAIL"}, "absent": sorted(k for k, v in t.items() if not v)}
    res, _ = gates(E); OUT["export, plain (the seat's own case)"] = table(res); print("export plain:", {k: (len(v) if not isinstance(v, dict) else v) for k, v in OUT["export, plain (the seat's own case)"].items()}, flush=True)
    (E / ".git").mkdir()
    res, _ = gates(E); OUT["U9.a an empty .git directory"] = table(res); print("U9.a:", {k: (len(v) if not isinstance(v, dict) else v) for k, v in OUT["U9.a an empty .git directory"].items()}, flush=True)
    shutil.rmtree(E / ".git")
    extra = ["tracked-deps", "seal-immutable", "artifact-hashes", "arrival-phrases", "seal-order-unshown"]
    res, _ = gates(E); OUT["U9.c the five the seat's list of ten did not name"] = {k: list(res.get(k, ("ABSENT", ""))) for k in extra}; print("U9.c:", {k: v[0] + (" refused" if "refused" in v[1] else "") for k, v in OUT["U9.c the five the seat's list of ten did not name"].items()}, flush=True)
    sh(["git", "init", "-q"], cwd=str(E))
    res, _ = gates(E); OUT["U9.b git init and no commit"] = table(res); print("U9.b (init, nothing added):", {k: (len(v) if not isinstance(v, dict) else v) for k, v in OUT["U9.b git init and no commit"].items()}, flush=True)
    sh(["git", "add", "-A"], cwd=str(E))
    res, _ = gates(E); OUT["U9.b', the files added and still no commit"] = table(res); print("U9.b' (added, no commit):", {k: (len(v) if not isinstance(v, dict) else v) for k, v in OUT["U9.b', the files added and still no commit"].items()}, flush=True)
    shutil.rmtree(E, ignore_errors=True)

if stage in ("all", "shallow"):
    def cut(name, clone_args, after=None):
        S = T / name; shutil.rmtree(S, ignore_errors=True)
        r = sh(["git", "clone", "-q", "--no-checkout", *clone_args, "file://" + str(W), str(S)])
        assert r.returncode == 0, r.stderr
        sh(["git", "-C", str(S), "sparse-checkout", "set", "scripts"]); sh(["git", "-C", str(S), "checkout", "-q", "HEAD"])
        if after:
            after(S)
        shallow = sh(["git", "-C", str(S), "rev-parse", "--is-shallow-repository"]).stdout.strip()
        n = sh(["git", "-C", str(S), "rev-list", "--count", "HEAD"]).stdout.strip()
        res, _ = gates(S)
        hist = {k: res.get(k) for k in sorted(HISTORY)}; tr = {k: res.get(k) for k in sorted(TRACKED)}
        out = {"git says shallow": shallow, "commits it holds": n,
               "history gates refused as shallow": sorted(k for k, v in hist.items() if v and v[0] == "FAIL" and "shallow" in v[1]),
               "history gates NOT refused": {k: (v[0] + ": " + v[1][:100]) if v else "ABSENT" for k, v in hist.items() if not (v and v[0] == "FAIL" and "shallow" in v[1])},
               "tracked-file gates refused": sorted(k for k, v in tr.items() if v and "refused" in v[1])}
        shutil.rmtree(S, ignore_errors=True)
        return out
    OUT["U22.a depth 1"] = cut("d1", ["--depth", "1"]); print("U22.a:", OUT["U22.a depth 1"], flush=True)
    OUT["U22.b depth 50"] = cut("d50", ["--depth", "50"]); print("U22.b:", OUT["U22.b depth 50"], flush=True)
    def graft(S):
        # a full clone, its oldest hundred commits cut off by hand: the hundred-and-first commit from the root is written into .git/shallow
        revs = sh(["git", "-C", str(S), "rev-list", "--first-parent", "--reverse", "HEAD"]).stdout.split()
        (S / ".git" / "shallow").write_text(revs[100] + "\n")
    OUT["U22.c a full clone cut by a hand-written .git/shallow"] = cut("graft", ["--shared"], graft); print("U22.c:", OUT["U22.c a full clone cut by a hand-written .git/shallow"], flush=True)

(T / ("unseen_%s.json" % stage)).write_text(json.dumps(OUT, indent=1, ensure_ascii=False))
print("written", flush=True)
