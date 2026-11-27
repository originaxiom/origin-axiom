#!/usr/bin/env python3
"""The sandboxed rerun (the framework's thin path, patch T5; rebuilt by T7b; draft 1 § 9; main's M54, M58, M62, M64 and
M65; register row P-885).

The intake reruns a card's decisive script at its sealed commit and requires its failing control to fail. It decides:
  REPRODUCED          the script ran, printed as many lines marked "DECISIVE:" as the card says, their normalised hash is
                      the card's, and the failing control failed: it exited exactly 1 with no traceback (T1b);
  RETURNED_AT_INTAKE  a check failed; the reasons are given;
  HEAVY               the card needs sage or GAP, declares itself heavy, ran past the time limit, or no sandbox can be
                      made on this machine: the same code reruns it on the author's machine, when the author chooses
                      (§ 9). Heavy is not a failure.

THE ORDER (M64, items 6 and 7). Every check that needs no run comes first, for every card, heavy or not: the script's path,
its content against the card's hash, symlinks, the imports of the decisive script, of the control's script and of every
module beside them that they import, and the two commands. Then the decisive run. A run whose lines or exit already fail
returns the card before the control runs, so a slow control cannot turn a failed rerun into HEAVY.

THE FILES (M64, items 1 and 2). The commit's files are written from their blobs (`git ls-tree -r -z`, `git cat-file`), not by
`git archive`, so a commit's `.gitattributes` (export-subst, ident, export-ignore) cannot change what runs; the decisive
script's hash is checked on the file as written. Symlinks are not written, and a decisive script, a control's script or an
imported module that is a symlink at the commit returns the card.

THE SANDBOX (M62, M64 item 5). Seat code runs as the unprivileged user `nobody`, which owns only the temporary directory
the commit is written to, inside a new network namespace: `unshare -n -- setpriv --reuid=nobody ...` as root, or the same
under `sudo -n` (hosted runners). The wrap is trusted only once a probe inside it sees no interface but the loopback AND
fails to write into a directory the runner owns. It cannot write the queue's folder or `scripts/queue/`, which judge the
round. Where no such wrap works, no seat code runs: the card is HEAVY, for the author's machine, where the author may run
it without a sandbox by choice (`allow_static`).

THE STATIC GUARD (M64 item 4) is a second wall, never the first. It refuses the network modules (with `_socket` and `_ssl`),
`ctypes`, `multiprocessing`, `logging.handlers`, `importlib`, `exec`, `eval` and `compile`, any use of `__import__`, and any
change to `sys.path`. It does not refuse `subprocess`: main's trial wrapper runs banked scripts that way (M65), and a
script run so is not read by the guard. For such a script the namespace and the unprivileged user are the wall.

THE DECISIVE LINES, NORMALISED: each line the script prints that opens "DECISIVE:", with its spaces collapsed and every
number with a point or an exponent written to 12 significant digits. Floating-point noise below that is the producer's to
round (main's M57). The full output's hash is recorded and not decided on.

THE ALLOWED PACKAGES and their pins are in ALLOWED_PACKAGES.json beside this file; the versions found are recorded.

A HEAVY RERUN on the author's machine runs sage, and for main's B2016 wrapper also a `python3` on the PATH that has
python-flint (M65): set the PATH so before such a rerun.

    python3 scripts/queue/rerun.py --record queue/cards/Q0001.json [--root REPO] [--limit SECONDS] [--allow-static-guard]
Prints the result as JSON. Exit 0 when REPRODUCED or HEAVY, 1 when returned."""
import ast
import hashlib
import importlib.metadata
import importlib.util
import json
import os
import pathlib
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TIME_LIMIT = 1800
TRACEBACK = "Traceback (most recent call last)"
NOBODY = 65534


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    return m


CF = _load("card_form_for_the_rerun", HERE / "card_form.py")
PINS = json.loads((HERE / "ALLOWED_PACKAGES.json").read_text(encoding="utf-8"))
PACKAGES = {name: pin["module"] for name, pin in PINS["packages"].items()}       # distribution -> module
HEAVY_MODULES = {"sage", "gappy", "sage_all"}
HEAVY_SUFFIXES = (".sage", ".g", ".gap")
NETWORK = {"socket", "_socket", "ssl", "_ssl", "http", "urllib", "ftplib", "smtplib", "poplib", "imaplib", "telnetlib",
           "xmlrpc", "socketserver", "asyncio", "selectors", "webbrowser", "nntplib"}
REFUSED = NETWORK | {"ctypes", "_ctypes", "multiprocessing", "_multiprocessing", "importlib"}
REFUSED_DOTTED = {"logging.handlers"}
REFUSED_CALLS = {"exec", "eval", "compile", "__import__", "import_module"}
STDLIB = set(sys.stdlib_module_names) - REFUSED
NUMBER = re.compile(r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?")
# inside the wrap: the only interface is the loopback, and a file cannot be written into a directory the runner owns.
# The probe exits 7 then, and 0 anywhere else
PROBE = ("import socket, sys\nnet = [n for _, n in socket.if_nameindex()] == ['lo']\n"
         "try:\n    open(sys.argv[1], 'w').write('x')\n    wrote = True\nexcept OSError:\n    wrote = False\n"
         "raise SystemExit(7 if net and not wrote else 0)\n")


def normalise(line):
    """one decisive line as the rerun compares it"""
    text = " ".join(line.split())

    def num(m):
        s = m.group(0)
        if "." in s or "e" in s or "E" in s:
            return "%.12g" % float(s)
        return s
    return NUMBER.sub(num, text)


def decisive(stdout):
    """(the number of decisive lines, the first 16 hex of their normalised hash)"""
    lines = [normalise(l) for l in stdout.splitlines() if l.lstrip().startswith("DECISIVE:")]
    blob = "".join(l + "\n" for l in lines).encode("utf-8")
    return len(lines), hashlib.sha256(blob).hexdigest()[:16]


def _guard_node(node, rel):
    """the static guard's reasons for one node of a script's syntax tree"""
    bad = []
    if isinstance(node, (ast.Name, ast.Attribute)):
        name = node.id if isinstance(node, ast.Name) else node.attr
        if name == "__import__":
            bad.append("%s uses __import__" % rel)
    if isinstance(node, ast.Constant) and node.value == "__import__":
        bad.append("%s names __import__" % rel)
    if isinstance(node, ast.Call):
        f = node.func
        name = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else "")
        if name in REFUSED_CALLS:
            bad.append("%s calls %s, which the guard cannot read" % (rel, name))
        if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Attribute) and f.value.attr == "path" \
                and isinstance(f.value.value, ast.Name) and f.value.value.id == "sys":
            bad.append("%s changes sys.path" % rel)
    if isinstance(node, (ast.Assign, ast.AugAssign)):
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        for t in targets:
            for sub in ast.walk(t):
                if isinstance(sub, ast.Attribute) and sub.attr == "path" and isinstance(sub.value, ast.Name) \
                        and sub.value.id == "sys":
                    bad.append("%s changes sys.path" % rel)
    return bad


def imports_of(path, root, seen=None, modes=None):
    """(the top-level modules the script imports, problems), read from the syntax tree and followed into every module beside
    it that it imports; `seen` collects the files read; `modes` ({path: git mode}) refuses a module that is a symlink"""
    seen = set() if seen is None else seen
    seen.add(path)
    rel = path.relative_to(root)
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), str(path))
    except (SyntaxError, UnicodeDecodeError) as exc:
        return set(), ["%s cannot be read as Python (%s)" % (rel, exc.__class__.__name__)]
    mods, dotted, bad = set(), set(), []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                mods.add(a.name.split(".")[0])
                dotted.add(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                bad.append("%s imports relatively" % rel)
            elif node.module:
                mods.add(node.module.split(".")[0])
                dotted.add(node.module)
                dotted |= {"%s.%s" % (node.module, a.name) for a in node.names}
        bad += _guard_node(node, rel)
    bad += ["%s imports %s" % (rel, d) for d in sorted(dotted & REFUSED_DOTTED)]
    out = set()
    for m in sorted(mods):
        sib = path.parent / (m + ".py")
        sib_rel = str(sib.relative_to(root))
        if modes and modes.get(sib_rel) == "120000":
            bad.append("%s imports %s, which is a symlink at the commit" % (rel, sib_rel))
        elif sib.is_file():
            if sib not in seen:
                more, more_bad = imports_of(sib, root, seen, modes)
                out |= more
                bad += more_bad
        else:
            out.add(m)
    return out, sorted(set(bad), key=bad.index)


def materialise(root, commit, dest):
    """write the commit's files into dest from their blobs; {path: mode} of every entry, symlinks not written"""
    r = subprocess.run(["git", "ls-tree", "-r", "-z", commit], cwd=root, capture_output=True)
    if r.returncode != 0:
        return None
    modes, blobs = {}, []
    for entry in r.stdout.split(b"\0"):
        if not entry:
            continue
        meta, path = entry.split(b"\t", 1)
        mode, kind, sha = meta.decode().split()
        p = path.decode("utf-8", "surrogateescape")
        modes[p] = mode
        if kind == "blob" and mode in ("100644", "100755"):
            blobs.append((p, sha, mode))
    proc = subprocess.Popen(["git", "cat-file", "--batch"], cwd=root, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        for p, sha, mode in blobs:
            proc.stdin.write((sha + "\n").encode())
            proc.stdin.flush()
            header = proc.stdout.readline().split()
            size = int(header[2])
            data = proc.stdout.read(size)
            proc.stdout.read(1)
            target = pathlib.Path(dest, p)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            if mode == "100755":
                target.chmod(0o755)
    finally:
        proc.stdin.close()
        proc.wait()
    return modes


def _command(cmd):
    """the argument list of a plain run of a script of the commit, or None: `python3 <a .py> [arguments]` (or, for a heavy
    script, `sage <a .sage>` or `gap <a .g>`), a relative path inside the commit, and no shell signs"""
    try:
        argv = shlex.split(cmd)
    except ValueError:
        return None
    if len(argv) < 2 or any(c in cmd for c in ";|&`$><"):
        return None
    run, path = argv[0], argv[1]
    if path.startswith(("/", "-")) or ".." in pathlib.PurePosixPath(path).parts:
        return None
    if run in ("python3", "python") and path.endswith(".py"):
        return [sys.executable, "-E", "-s"] + argv[1:]
    if run == "sage" and path.endswith(".sage") or run == "gap" and path.endswith((".g", ".gap")):
        return argv
    return None


STRATEGIES = [
    (lambda: os.geteuid() == 0,
     ["unshare", "-n", "--", "setpriv", "--reuid=%d" % NOBODY, "--regid=%d" % NOBODY, "--clear-groups", "--"],
     "unshare -n, as nobody"),
    (lambda: True,
     ["sudo", "-n", "unshare", "-n", "--", "setpriv", "--reuid=%d" % NOBODY, "--regid=%d" % NOBODY, "--clear-groups",
      "--"], "sudo unshare -n, as nobody"),
]


def _hand_over(path, prefix):
    """give the run's directory to nobody, who must own it alone"""
    if prefix[:1] == ["sudo"]:
        return subprocess.run(["sudo", "-n", "chown", "-R", "%d:%d" % (NOBODY, NOBODY), str(path)],
                              capture_output=True).returncode == 0
    try:
        for d, dirs, files in os.walk(path):
            os.chown(d, NOBODY, NOBODY)
            for f in files:
                os.chown(os.path.join(d, f), NOBODY, NOBODY)
        return True
    except OSError:
        return False


def _take_back(path, prefix):
    if prefix[:1] == ["sudo"]:
        subprocess.run(["sudo", "-n", "rm", "-rf", str(path)], capture_output=True)
    shutil.rmtree(path, ignore_errors=True)


def sandbox_prefix():
    """(the prefix that runs a command as nobody with the network cut, its name), tested both ways; ([], "no sandbox")
    when none works"""
    for usable, prefix, name in STRATEGIES:
        if not usable() or not all(shutil.which(c) for c in (prefix[0], "setpriv", "unshare")):
            continue
        marker = pathlib.Path(tempfile.mkdtemp(prefix="probe_"))
        try:
            marker.chmod(0o755)                       # readable by nobody, writable only by the runner
            r = subprocess.run(prefix + [sys.executable, "-I", "-c", PROBE, str(marker / "x")], capture_output=True,
                               timeout=30, cwd="/")
            if r.returncode == 7 and not (marker / "x").exists():
                return prefix, name
        except (OSError, subprocess.TimeoutExpired):
            pass
        finally:
            shutil.rmtree(marker, ignore_errors=True)
    return [], "no sandbox"


def _run(prefix, argv, cwd, limit):
    env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(cwd), "LANG": "C.UTF-8", "PYTHONHASHSEED": "0"}
    t0 = time.time()
    try:
        r = subprocess.run(prefix + argv, cwd=cwd, capture_output=True, text=True, timeout=limit, env=env)
        return r.returncode, r.stdout, r.stderr, time.time() - t0
    except subprocess.TimeoutExpired:
        return None, "", "", time.time() - t0


def versions():
    out = {"python": "%d.%d.%d" % sys.version_info[:3]}
    for dist in PACKAGES:
        try:
            out[dist] = importlib.metadata.version(dist)
        except importlib.metadata.PackageNotFoundError:
            out[dist] = None
    return out


def _checks(tmp, modes, script, want_hash, cmd, control):
    """every check that needs no run: (reasons, heavy reasons, the decisive argv, the control's argv)"""
    bad, heavy = [], []
    if pathlib.PurePosixPath(script).is_absolute() or ".." in pathlib.PurePosixPath(script).parts:
        return ["the decisive script's path %r leaves the commit" % script], heavy, None, None
    if modes.get(script) == "120000":
        return ["the decisive script %s is a symlink at the commit" % script], heavy, None, None
    path = tmp / script
    if not path.is_file():
        return ["the decisive script %s is not at the commit" % script], heavy, None, None
    got = hashlib.sha256(path.read_bytes()).hexdigest()[:16]
    if got != want_hash:
        bad.append("the decisive script as written is not the one the card hashes (%s, the card says %s)" % (got, want_hash))
    is_heavy_script = script.endswith(HEAVY_SUFFIXES)
    argv = _command(cmd)
    if argv is None or (argv[3] if argv[0] == sys.executable else argv[1]) != script:
        bad.append("the decisive command is not a plain run of the decisive script: %r" % cmd)
    cargv = _command(control)
    if cargv is None:
        bad.append("the failing control is not a plain run of a script of the commit: %r" % control)
    elif argv is not None and cargv == argv:
        bad.append("the failing control is the decisive command itself")
    scripts = [script] + ([cargv[3] if cargv[0] == sys.executable else cargv[1]] if cargv else [])
    mods = set()
    for s in dict.fromkeys(scripts):
        if modes.get(s) == "120000":
            bad.append("%s is a symlink at the commit" % s)
            continue
        if not (tmp / s).is_file():
            bad.append("the control's script %s is not at the commit" % s)
            continue
        if s.endswith(".py"):
            m, b = imports_of(tmp / s, tmp, None, modes)
            mods |= m
            bad += b
    allowed = STDLIB | set(PACKAGES.values()) | HEAVY_MODULES
    outside = sorted(mods - allowed)
    if outside:
        bad.append("the script imports what is not allowed: %s" % ", ".join(outside))
    if is_heavy_script:
        heavy.append("the decisive script is run by sage or GAP")
    if mods & HEAVY_MODULES:
        heavy.append("the decisive script imports %s" % ", ".join(sorted(mods & HEAVY_MODULES)))
    return bad, heavy, argv, cargv


def rerun(root, commit, card_text, limit=TIME_LIMIT, prefix=None, allow_static=False):
    """the result of rerunning one card at one commit: {status, reasons, ...}"""
    _title, f, _ = CF.read(card_text)
    res = {"status": None, "reasons": [], "commit": commit, "guard": None, "versions": versions(), "pins_differ": []}
    res["pins_differ"] = sorted(d for d, v in res["versions"].items()
                                if d in PINS["packages"] and v is not None and v != PINS["packages"][d]["pin"])
    m = CF.SCRIPT.match(f.get("decisive script", ""))
    d = CF.DECISIVE.fullmatch(f.get("decisive lines", ""))
    if not m or not d:
        res.update(status="RETURNED_AT_INTAKE", reasons=["the card's decisive script or decisive lines are not in form"])
        return res
    script, cmd, control = m.group(1), m.group(3).strip(), f.get("failing control", "")
    want = CF.HEX16.search(f["decisive script"]).group(1)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="rerun_"))
    if prefix is None:
        prefix, guard = sandbox_prefix()
    else:
        guard = " ".join(prefix) or "no sandbox"
    try:
        modes = materialise(root, commit, tmp)
        if modes is None:
            res.update(status="RETURNED_AT_INTAKE", reasons=["the sealed commit cannot be read"])
            return res
        bad, heavy, argv, cargv = _checks(tmp, modes, script, want, cmd, control)
        if bad:
            res.update(status="RETURNED_AT_INTAKE", reasons=bad)
            return res
        if CF.declared_heavy(f):
            heavy.append("the card declares its decisive script heavy")
        if heavy:
            res.update(status="HEAVY", reasons=heavy)
            return res
        if not prefix and not allow_static:
            res.update(status="HEAVY", reasons=["no sandbox can be made here (no unprivileged user in a network namespace):"
                                                " no seat code runs; for the author's machine"])
            return res
        res["guard"] = guard if prefix else "none: the author's machine, by the author's choice"
        if prefix and not _hand_over(tmp, prefix):
            res.update(status="HEAVY", reasons=["the run's directory could not be given to the unprivileged user"])
            return res
        rc, out, err, secs = _run(prefix, argv, tmp, limit)
        res["seconds"] = round(secs, 1)
        if rc is None:
            res.update(status="HEAVY", reasons=["the decisive script ran past %d seconds" % limit])
            return res
        res["output_sha256"] = hashlib.sha256(out.encode("utf-8")).hexdigest()[:16]
        n, h = decisive(out)
        res["decisive"] = {"lines": n, "sha256": h}
        if rc != 0:
            res["reasons"].append("the decisive script exited with %d: %s" % (rc, err.strip().splitlines()[-1:] or ""))
        if (n, h) != (int(d.group(1)), d.group(2)):
            res["reasons"].append("the decisive lines are %d with hash %s; the card says %s with %s"
                                  % (n, h, d.group(1), d.group(2)))
        if res["reasons"]:                            # M64 item 6: what the run found decides before the control runs
            res["status"] = "RETURNED_AT_INTAKE"
            return res
        crc, _, cerr, csecs = _run(prefix, cargv, tmp, max(1, limit - int(secs)))
        res["control_exit"] = crc
        if crc is None:
            res.update(status="HEAVY", reasons=["the failing control ran past the time limit"])
            return res
        if crc == 0:
            res["reasons"].append("the failing control exited 0: it did not fail")
        elif crc != 1 or TRACEBACK in cerr:
            res["reasons"].append("the failing control is invalid: it exited %d%s; a control fails by exiting 1 with no "
                                  "traceback" % (crc, " with a traceback" if TRACEBACK in cerr else ""))
        res["status"] = "RETURNED_AT_INTAKE" if res["reasons"] else "REPRODUCED"
        return res
    finally:
        _take_back(tmp, prefix)


def main(argv):
    rec = json.loads(pathlib.Path(argv[argv.index("--record") + 1]).read_text(encoding="utf-8"))
    root = pathlib.Path(argv[argv.index("--root") + 1]) if "--root" in argv else ROOT
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else TIME_LIMIT
    card = subprocess.run(["git", "show", "%s:%s" % (rec["commit"], rec["card_path"])], cwd=root, capture_output=True,
                          text=True)
    if card.returncode != 0:
        print(json.dumps({"status": "RETURNED_AT_INTAKE", "reasons": ["the card is not at its sealed commit"]}))
        return 1
    res = rerun(root, rec["commit"], card.stdout, limit, allow_static="--allow-static-guard" in argv)
    print(json.dumps(res, indent=1, sort_keys=True))
    return 0 if res["status"] in ("REPRODUCED", "HEAVY") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
