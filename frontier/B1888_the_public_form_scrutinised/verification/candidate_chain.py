"""B1888 -- what the record's candidate really uses: its chain of code, read from the code.

The advisor seat's opinion on the repository's public form rests on one measurement: by the arcs' own `depends_on` lists the
candidate (B1841) has 736 arcs upstream.  That list mixes what an arc uses with what it cites.  The seat asked main, at the
owner's word, what the true chain is (its weak points 1, 2 and 5).  This script measures it from the code.

HOW.  Static, and an upper bound.  Starting from the candidate's own scripts, each Python file is parsed.  From its string
constants (docstrings left out) are taken the arc folders it names and the file names it names; from its import statements,
the local modules.  A name is resolved in the file's own folder first, then in the arc folders that file names.  Every
Python file so reached is parsed in turn.  A file that is only cited in a comment or a docstring is not reached; a file
that is named and never opened IS reached, so the chain here can be longer than the true one and not shorter.
[CORRECTED 2026-11-12 (Review 79): "and not shorter" is wrong.  A file whose name is built at run time is not reached, so
the chain here can also be shorter than the true one.  What holds: an upper bound on the files the code names.]

WHAT COULD FAIL.  The chain not closing (a named file that does not exist); the candidate not reaching the measured values
at all, which would mean this instrument does not see how they enter; or a chain as long as the list of dependencies, which
would mean the opinion's central step, a rebuild in a few thousand lines, has nothing under it.

No file of data is opened: names and sizes only.  The file of measured values is identified by its name and never read.
"""
import ast
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FRONTIER = ROOT / "frontier"
ARC = re.compile(r"B\d{3,4}_[A-Za-z0-9_]+")
FILE = re.compile(r"[\w.\-]+\.(?:py|json|npz|npy|txt|csv|gz|jsonl|sha256)")
MEASURED = "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"
CANDIDATE = "B1841_the_principled_ends_card"
OUT = []


def P(*a):
    s = " ".join(str(x) for x in a); OUT.append(s); print(s, flush=True)


def tracked():
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files", "frontier", "scripts", "src", "outside_bench"], capture_output=True, text=True).stdout.split("\n")
    return {x for x in out if x}


TRACKED = tracked()
BY_DIR = {}
for rel in TRACKED:
    BY_DIR.setdefault(rel.rsplit("/", 1)[0], []).append(rel.rsplit("/", 1)[1])
ARC_DIRS = sorted({r.split("/")[1] for r in TRACKED if r.startswith("frontier/") and r.count("/") >= 2})
FILES_OF_ARC = {}
for rel in TRACKED:
    if rel.startswith("frontier/"):
        FILES_OF_ARC.setdefault(rel.split("/")[1], []).append(rel)


def arc_of(rel):
    return rel.split("/")[1] if rel.startswith("frontier/") else rel.split("/")[0]


def names_in(rel):
    """(arc folders named, file names named, local modules imported) by one Python file; docstrings are left out"""
    src = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return set(), set(), set()
    doc = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.body:
            b = n.body[0]
            if isinstance(b, ast.Expr) and isinstance(b.value, ast.Constant) and isinstance(b.value.value, str):
                doc.add(id(b.value))
    strings = [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in doc]
    arcs, files = set(), set()
    for s in strings:
        for a in ARC.findall(s):
            hit = [d for d in ARC_DIRS if d == a or d.startswith(a)]
            arcs.update(hit[:1] if len(hit) == 1 else [d for d in hit if d == a])
        for m in re.finditer(r"B\d{3,4}_\*", s):
            arcs.update(d for d in ARC_DIRS if d.startswith(m.group(0)[:-1]))
        for f in FILE.findall(s):
            files.add(f.rsplit("/", 1)[-1])
        if "/" in s and (ROOT / s).is_file() and s in TRACKED:
            files.add(s)
    mods = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            mods.update(a.name.split(".")[0] for a in n.names)
        elif isinstance(n, ast.ImportFrom) and n.module and n.level == 0:
            mods.add(n.module.split(".")[0])
    return arcs, files, mods


def resolve(rel, arcs, files, mods):
    """the tracked files that one Python file reaches"""
    here = rel.rsplit("/", 1)[0]
    scope = [here] + sorted({r.rsplit("/", 1)[0] for a in arcs | {arc_of(rel)} for r in FILES_OF_ARC.get(a, [])})
    reached = set()
    # A name is taken wherever it is found in that scope, the file's own folder included.  Main's first version stopped at
    # the file's own folder; the candidate's census.py loads B1839's census.py, a file of the same name, and the chain ended
    # at the candidate's two scripts without reaching the measured values, which is the failure this script's header names.
    for f in files:
        if "/" in f:
            reached.add(f); continue
        for d in scope:
            if f in BY_DIR.get(d, ()):
                reached.add(d + "/" + f)
    for m in mods:
        for d in scope:
            if m + ".py" in BY_DIR.get(d, ()):
                reached.add(d + "/" + m + ".py")
    reached.discard(rel)
    return reached


def chain(start):
    seen, order, via = set(start), list(start), {}
    k = 0
    while k < len(order):
        rel = order[k]; k += 1
        if not rel.endswith(".py"):
            continue
        for r in sorted(resolve(rel, *names_in(rel))):
            if r not in seen:
                seen.add(r); order.append(r); via[r] = rel
    return order, via


def path_to(target, via):
    out = [target]
    while out[-1] in via:
        out.append(via[out[-1]])
    return out[::-1]


def upstream_by_depends_on(aid="B1841"):
    V = {}
    for d in ARC_DIRS:
        p = FRONTIER / d / "arc_verdict.json"
        if p.is_file():
            try:
                x = json.loads(p.read_text(encoding="utf-8")); V[x.get("id")] = x
            except Exception:
                pass
    up, stack = set(), [aid]
    while stack:
        for y in (V.get(stack.pop(), {}).get("depends_on") or []):
            if y not in up:
                up.add(y); stack.append(y)
    return up, V


if __name__ == "__main__":
    start = sorted(r for r in FILES_OF_ARC[CANDIDATE] if r.endswith(".py") and "/referee/" not in r)
    P("THE CANDIDATE'S OWN SCRIPTS:", ", ".join(s.rsplit("/", 1)[1] for s in start))
    order, via = chain(start)
    py = [r for r in order if r.endswith(".py")]
    data = [r for r in order if not r.endswith(".py")]
    arcs = sorted({arc_of(r) for r in order if r.startswith("frontier/")})
    lines = sum(len((ROOT / r).read_text(encoding="utf-8", errors="replace").splitlines()) for r in py)
    size = sum((ROOT / r).stat().st_size for r in data if (ROOT / r).is_file())
    P("THE CHAIN OF CODE (an upper bound): %d Python files, %d lines; %d other files named, %.1f MB; in %d arc folders" % (len(py), lines, len(data), size / 1e6, len(arcs)))
    for a in arcs:
        fs = [r for r in order if r.startswith("frontier/" + a + "/")]
        P("   %-62s %2d python, %2d other" % (a, sum(1 for r in fs if r.endswith(".py")), sum(1 for r in fs if not r.endswith(".py"))))
    outside = sorted(r for r in order if not r.startswith("frontier/"))
    P("   outside the arcs: %s" % (", ".join(outside) or "none"))
    up, V = upstream_by_depends_on()
    chain_ids = {a.split("_")[0] for a in arcs}
    P("BY THE ARCS' OWN LISTS: %d arcs upstream of the candidate (%d direct).  IN THE CHAIN OF CODE: %d arcs, the candidate included; %d of them are not on the lists' upstream" % (
        len(up), len(V["B1841"].get("depends_on") or []), len(arcs), len(chain_ids - up - {"B1841"})))
    P("   the candidate's ten direct dependencies that the code reaches: %s; that it does not: %s" % (
        sorted(set(V["B1841"]["depends_on"]) & chain_ids), sorted(set(V["B1841"]["depends_on"]) - chain_ids)))
    reaches = MEASURED in order
    P("THE MEASURED VALUES (%s): reached by the chain: %s" % (MEASURED.rsplit("/", 1)[1], reaches))
    route = path_to(MEASURED, via) if reaches else []
    short = lambda r: (r.split("/")[1].split("_")[0] + "/" + r.rsplit("/", 1)[1]) if r.startswith("frontier/") else r
    if reaches:
        P("   by this route: " + "  ->  ".join(short(r) for r in route))
    # the two halves apart: the census computes what the frame gives; the look sets it beside the measured values
    halves = {}
    for s0 in start:
        o, v = chain([s0])
        halves[s0.rsplit("/", 1)[1]] = dict(python=sum(1 for r in o if r.endswith(".py")), arcs=len({arc_of(r) for r in o}), reaches_measured=MEASURED in o,
                                            lines=sum(len((ROOT / r).read_text(encoding="utf-8", errors="replace").splitlines()) for r in o if r.endswith(".py")))
        P("   from %-10s alone: %2d Python files, %4d lines, %2d arcs; reaches the measured values: %s" % (s0.rsplit("/", 1)[1], halves[s0.rsplit("/", 1)[1]]["python"],
          halves[s0.rsplit("/", 1)[1]]["lines"], halves[s0.rsplit("/", 1)[1]]["arcs"], MEASURED in o))
    # helpers that enter by copy and not by reference: a file of the chain whose name carries another arc's number
    copies = sorted(short(r) for r in py if (m := re.match(r"b(\d{3,4})_", r.rsplit("/", 1)[1])) and ("B" + m.group(1)) != arc_of(r).split("_")[0])
    P("   helpers of other arcs present as copies in the chain: %s" % (", ".join(copies) or "none"))
    namers = sorted(r for r in py if MEASURED.rsplit("/", 1)[1] in (ROOT / r).read_text(encoding="utf-8", errors="replace"))
    allnamers = subprocess.run(["git", "-C", str(ROOT), "grep", "-l", "-F", MEASURED.rsplit("/", 1)[1], "--", "*.py"], capture_output=True, text=True).stdout.split()
    P("   Python files of the chain that name that file: %d (%s); in the whole tree: %d" % (len(namers), ", ".join(n.split("/")[1].split("_")[0] + "/" + n.rsplit("/", 1)[1] for n in namers), len(allnamers)))
    res = dict(start=start, python=py, other=data, arcs=arcs, lines=lines, other_bytes=size, upstream_by_lists=len(up), arcs_in_chain=len(arcs),
               direct_reached=sorted(set(V["B1841"]["depends_on"]) & chain_ids), direct_not_reached=sorted(set(V["B1841"]["depends_on"]) - chain_ids),
               measured_reached=reaches, route=route, namers_in_chain=namers, namers_in_tree=len(allnamers), halves=halves, copies=copies)
    (HERE / "candidate_chain.json").write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
    (HERE / "candidate_chain_run.txt").write_text("\n".join(OUT) + "\n", encoding="utf-8")
