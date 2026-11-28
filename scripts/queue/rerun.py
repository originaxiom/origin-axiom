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

THE SANDBOX (M62, M64 item 5, M68, M70). Seat code runs as the unprivileged user `nobody`, with no groups, which owns only
the temporary directory the commit is written to. It runs inside new network, mount, IPC and PID namespaces (`unshare -n
-m -i -p -f --kill-child --mount-proc`, as root, or the same under `sudo -n` on hosted runners):
  - its directory is bound at `/mnt`;
  - every directory the runner finds world-writable on the machine (`/tmp`, `/var/tmp`, `/dev/shm`, `/run/lock`, and any
    other) is covered by a fresh tmpfs, so no run can leave a file for another, and none survives the run (M68 point 2,
    M70 point 2);
  - System V IPC and POSIX message queues are the run's own (M70 point 2);
  - its processes die with it: in the PID namespace a run's last process is its first, and before and after every run
    every process of nobody is killed, and the next run waits until none is left. A run that leaves one that cannot be
    killed is HEAVY (M70 point 3). So the runner's machine runs nothing else as nobody, and its sandboxed runs take a
    lock, one at a time, so that two rounds, or tests in parallel, do not end each other's runs.
The wrap is trusted only once a probe inside it, run as a card is run, reports:
  - no interface up but the loopback (SIOCGIFFLAGS: a kernel with tunnel modules shows `tunl0`, `gre0`, `sit0` and others,
    all down; M68 point 1);
  - user and group nobody, and no groups (M70 point 1);
  - a write into a directory the runner owns, outside every tmpfs, refused for want of permission, and for no other reason
    (M70 point 1);
  - no directory it can write, searched over the whole filesystem, but its own folder and the tmpfs it was given; and a
    file written into each of those that is not there afterwards (M70 point 2).
It cannot write the queue's folder or `scripts/queue/`. Where no such wrap works, no seat code runs: the card is HEAVY, for
the author's machine, where the author may run it without a sandbox by choice (`allow_static`).

THE STATIC GUARD (M64 item 4, M68 point 3, M69) is a second wall, never the first, and it sees only what is written
plainly. It refuses the network modules (with `_socket` and `_ssl`), `ctypes`, `multiprocessing`, `logging.handlers`,
`importlib`, a call of `exec`, `eval`, `compile` or `__import__` by its bare name or as an attribute of `builtins` or of a
name the script binds to it (`import builtins as b`, `b = builtins`), the import of any of them from `builtins` (M70 point
5), any use of the name `__import__` or the string "__import__", and any change to `sys.path`; `re.compile` passes (M69). It
does not see `getattr(__builtins__, '__imp' + 'ort__')`, `vars(builtins)[...]`, an unpickler that imports a module, or
`os.system`; nor a script run by `subprocess`, which main's trial wrapper uses (M65). For all of these the namespaces and
the unprivileged user are the wall.

THE DECISIVE LINES, NORMALISED: each line the script prints that opens "DECISIVE:", with its spaces collapsed and every
number with a point or an exponent written to 12 significant digits. Floating-point noise below that is the producer's to
round (main's M57). The full output's hash is recorded and not decided on.

THE ALLOWED PACKAGES and their pins are in ALLOWED_PACKAGES.json beside this file; the versions found are recorded.

A HEAVY RERUN on the author's machine runs sage, and for main's B2016 wrapper also a `python3` on the PATH that has
python-flint (M65): set the PATH so before such a rerun.

    python3 scripts/queue/rerun.py --record queue/cards/Q0001.json [--root REPO] [--limit SECONDS] [--allow-static-guard]
    python3 scripts/queue/rerun.py --heavy-result Q0006 --queue-dir DIR [--root REPO] [--author-allows]
On the author's machine only (main's M83): reruns a heavy card at its sealed commit with no wrap and the caller's PATH,
and writes queue/heavy/<card id>.json for main to land; a card of another seat only with --author-allows, the author's
word for that card.
Prints the result as JSON. Exit 0 when REPRODUCED or HEAVY, 1 when returned."""
import ast
import contextlib
import fcntl
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
REFUSED_CALLS = {"exec", "eval", "compile", "__import__"}         # by bare name, or as an attribute of builtins (M69)
BUILTINS_NAMES = {"builtins", "__builtins__"}
STDLIB = set(sys.stdlib_module_names) - REFUSED
NUMBER = re.compile(r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?")
# THE PROBE, run inside the wrap as the run would be (M68 point 1, M70 points 1 and 2). It prints, as JSON: the interfaces up
# but the loopback; what a write into a directory the runner owns, outside every tmpfs, met ("denied" only for a permission
# error); its user, group and groups; whether it wrote a file named by the token into each directory the wrap covered; and
# every directory it can write that is neither the run's folder nor one the wrap covered, found by walking the filesystem
PROBE = (
    "import fcntl, json, os, socket, struct, sys\n"
    "up = []\nfor _, n in socket.if_nameindex():\n    s = socket.socket()\n    try:\n"
    "        flags = struct.unpack('16sH', fcntl.ioctl(s.fileno(), 0x8913, struct.pack('16sH', n.encode(), 0)))[1]\n"
    "    finally:\n        s.close()\n    if flags & 1 and n != 'lo':\n        up.append(n)\n"
    "try:\n    open(sys.argv[1], 'w').write('x')\n    write = 'wrote'\n"
    "except PermissionError:\n    write = 'denied'\nexcept OSError as e:\n    write = 'not denied: ' + type(e).__name__\n"
    "covered = [c for c in os.environ.get('SANDBOX_COVERED', '').split('\\n') if c]\nput = []\n"
    "for c in covered:\n    try:\n        open(os.path.join(c, sys.argv[2]), 'w').write('x')\n        put.append(c)\n"
    "    except OSError:\n        pass\n"
    "inside = lambda d, c: d == c or d.startswith(c.rstrip('/') + '/')\nwritable = []\n"
    "for d, dirs, _ in os.walk('/'):\n"
    "    if d in ('/proc', '/sys') or inside(d, '/mnt') or any(inside(d, c) for c in covered):\n"
    "        dirs[:] = []\n        continue\n"
    "    if os.access(d, os.W_OK):\n        writable.append(d)\n        dirs[:] = []\n"
    "print(json.dumps({'up': up, 'write': write, 'ids': [os.getuid(), os.geteuid(), os.getgid(), os.getegid()],\n"
    "                  'groups': os.getgroups(), 'put': put, 'writable': writable[:20]}))\n")
# THE WRAP, run as root inside new network, mount, IPC and PID namespaces (M70 points 2 and 3): the run's folder bound at
# /mnt, a fresh tmpfs over each directory the runner found world-writable (argv[2], as JSON), then the user nobody
WRAP = (
    "import json, os, subprocess, sys\n"
    "run, cover, argv = sys.argv[1], json.loads(sys.argv[2]), sys.argv[3:]\n"
    "subprocess.run(['mount', '--bind', run, '/mnt'], check=True)\n"
    "done = []\nfor d in cover:\n"
    "    if os.path.isdir(d) and not os.path.islink(d):\n"
    "        subprocess.run(['mount', '-t', 'tmpfs', '-o', 'mode=1777,size=512m', 'tmpfs', d], check=True)\n"
    "        done.append(d)\n"
    "os.environ['SANDBOX_COVERED'] = '\\n'.join(done)\n"
    "os.setgroups([])\nos.setgid(%d)\nos.setuid(%d)\nos.chdir('/mnt')\nos.execvp(argv[0], argv)\n" % (65534, 65534))
SKIP_WALK = ("/proc", "/sys", "/mnt", "/dev/pts")
RUN = "{RUN}"


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


def builtins_aliases(tree):
    """the names a script binds to the builtins module (M70 point 5): `import builtins as b`, `b = builtins`"""
    names = set(BUILTINS_NAMES)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names |= {a.asname or a.name for a in node.names if a.name == "builtins"}
    for _ in range(3):                                # an alias of an alias
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Name) and node.value.id in names:
                names |= {t.id for t in node.targets if isinstance(t, ast.Name)}
    return names


def _guard_node(node, rel, aliases=BUILTINS_NAMES):
    """the static guard's reasons for one node of a script's syntax tree"""
    bad = []
    if isinstance(node, ast.ImportFrom) and node.module == "builtins":
        for a in node.names:
            if a.name in REFUSED_CALLS or a.name == "*":
                bad.append("%s imports %s from builtins, which the guard cannot read" % (rel, a.name))
    if isinstance(node, (ast.Name, ast.Attribute)):
        name = node.id if isinstance(node, ast.Name) else node.attr
        if name == "__import__":
            bad.append("%s uses __import__" % rel)
    if isinstance(node, ast.Constant) and node.value == "__import__":
        bad.append("%s names __import__" % rel)
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Name) and f.id in REFUSED_CALLS:
            bad.append("%s calls %s, which the guard cannot read" % (rel, f.id))
        elif isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name):
            if f.value.id in aliases and f.attr in REFUSED_CALLS:
                bad.append("%s calls %s.%s, which the guard cannot read" % (rel, f.value.id, f.attr))
            elif f.value.id == "importlib" and f.attr == "import_module":
                bad.append("%s calls importlib.import_module, which the guard cannot read" % rel)
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
    aliases = builtins_aliases(tree)
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
        bad += _guard_node(node, rel, aliases)
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
        # `-s`, not `-E` (Review 89, main's M74 point 1): the environment is built clean already, and `-E` would ignore the
        # PYTHONHASHSEED it sets, so a script printing a set of strings would give other decisive lines on each rerun
        return [sys.executable, "-s"] + argv[1:]
    if run == "sage" and path.endswith(".sage") or run == "gap" and path.endswith((".g", ".gap")):
        return argv
    return None


NAMESPACES = ["unshare", "-n", "-m", "-i", "-p", "-f", "--kill-child", "--mount-proc", "--"]


def strategies():
    """(usable, the prefix before the wrap's cover list, its name): read when called, so a test can bend the wrap"""
    wrap = [sys.executable, "-I", "-c", WRAP, RUN]
    return [(lambda: os.geteuid() == 0, NAMESPACES + wrap, "unshare -n -m -i -p, as nobody"),
            (lambda: True, ["sudo", "-n"] + NAMESPACES + wrap, "sudo unshare -n -m -i -p, as nobody")]


STRATEGIES = None                                      # a test may set a list of its own; None reads strategies()
# ADDED 2026-11-28 (main, at the author's word, after the runner's first round on the workflow, M78 point 2): why each
# strategy was refused at the last probe, so that "no sandbox" says why; the round prints it, and a HEAVY rerun carries it
WHY_NOT = []


def world_writable(top="/"):
    """every directory the filesystem holds that anyone may write, outermost only (covering it covers what is below)"""
    found = []
    for d, dirs, _ in os.walk(top):
        if d in SKIP_WALK:
            dirs[:] = []
            continue
        try:
            mode = os.lstat(d).st_mode
        except OSError:
            continue
        if mode & 0o002:
            found.append(d)
            dirs[:] = []
    return found


def wrapped(prefix, run_dir, argv, cover=None):
    """the command that runs argv in run_dir under the prefix: the run's directory stands for RUN in it, and the list of
    directories to cover, when given, for the one the prefix was probed with"""
    out = [str(run_dir) if a == RUN else a for a in prefix]
    if cover is not None and RUN in prefix and prefix.index(RUN) + 1 < len(prefix):
        out[prefix.index(RUN) + 1] = json.dumps(cover)
    return out + list(argv)


def _as_root(prefix):
    return ["sudo", "-n"] if prefix[:1] == ["sudo"] else []


def reap(prefix):
    """M70 point 3: kill every process of nobody, and True only when none is left. Run before and after every run and
    after the probe. In the PID namespace a run's processes die with it; on the sudo path a timeout's kill reaches only
    sudo, and this is what ends the run there. It kills every process of the user nobody on the machine, so the runner's
    machine must run nothing else as nobody"""
    if not prefix:
        return True
    for _ in range(50):
        subprocess.run(_as_root(prefix) + ["pkill", "-KILL", "-U", str(NOBODY)], capture_output=True)
        live = subprocess.run(_as_root(prefix) + ["pgrep", "-U", str(NOBODY), "-r", "R,S,D,T,t,I"], capture_output=True)
        if live.returncode == 2:                      # a pgrep without -r: a zombie, already dead, is counted too
            live = subprocess.run(_as_root(prefix) + ["pgrep", "-U", str(NOBODY)], capture_output=True)
        if live.returncode == 1:
            return True
        time.sleep(0.1)
    return False


@contextlib.contextmanager
def one_at_a_time():
    """the machine's sandbox lock, held from the kill before a run to the kill after it, and around the probe: the kill
    ends every process of nobody, so two runs at once on one machine (two rounds, or tests in parallel) would end each
    other's"""
    with open(os.path.join(tempfile.gettempdir(), "queue-sandbox.lock"), "a") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


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


def _marker_base(cover):
    """a directory the runner owns that no tmpfs of the wrap covers (M70 point 1): the probe's write into it must be denied
    because the user is nobody, not because the path is hidden"""
    inside = lambda d, c: d == c or d.startswith(c.rstrip("/") + "/")
    for base in (os.path.expanduser("~"), str(HERE), str(ROOT)):
        real = os.path.realpath(base)
        if os.path.isdir(real) and os.access(real, os.W_OK) and not inside(real, "/mnt") and \
                not any(inside(real, os.path.realpath(c)) for c in cover):
            return real
    return None


def probe_holds(out, token, cover):
    """the probe's report read: (True, "") when the wrap holds, else (False, why)"""
    try:
        r = json.loads(out.strip().splitlines()[-1])
    except (ValueError, IndexError):
        return False, "the probe printed no report"
    if r["up"]:
        return False, "interfaces up beside the loopback: %s" % ", ".join(r["up"])
    if r["write"] != "denied":
        return False, "a write into a directory the runner owns was %s" % r["write"]
    if r["ids"] != [NOBODY] * 4 or r["groups"]:
        return False, "the run is not nobody alone: ids %s, groups %s" % (r["ids"], r["groups"])
    if r["writable"]:
        return False, "the run can write outside its folder and its own tmpfs: %s" % ", ".join(r["writable"])
    if sorted(r["put"]) != sorted(cover) or any(os.path.exists(os.path.join(c, token)) for c in cover):
        return False, "a covered directory is shared with the runner"
    return True, ""


def sandbox_prefix():
    """(the prefix that runs a command as nobody with the network cut, in its own mount, IPC and PID namespaces, with a
    fresh tmpfs over every world-writable directory; its name), tested by the probe; ([], "no sandbox") when none works.
    The whole probe holds the machine's sandbox lock"""
    with one_at_a_time():
        return _sandbox_prefix_held()


def _sandbox_prefix_held():
    # CHANGED 2026-11-28 (main, at landing, at the author's word): the whole filesystem was walked before any wrap was
    # known to be usable, so a machine where none can be made (the author's, for heavy cards) walked its whole disk on
    # every call for nothing. The walk is now made once, and only for a wrap that passes the checks below.
    # The line as it stood, first in this function: cover = world_writable()
    cover = None
    del WHY_NOT[:]
    for usable, prefix, name in (STRATEGIES if STRATEGIES is not None else strategies()):
        if not usable():
            WHY_NOT.append("%s: not usable here" % name)
            continue
        missing = [c for c in (prefix[0], "unshare", "mount", "pkill", "pgrep") if not shutil.which(c)]
        if missing:
            WHY_NOT.append("%s: missing %s" % (name, ", ".join(missing)))
            continue
        if cover is None:
            cover = world_writable()
        # ADDED 2026-11-28 (the builder, at M78 point 2 and main's guess there): the wrap covers each world-writable
        # directory with an empty tmpfs, so an interpreter under one (actions/setup-python's, under /opt/hostedtoolcache,
        # where the image leaves it writable by all) is gone inside the wrap. Said before anything is run
        exe = os.path.realpath(sys.executable)
        hidden = [c for c in cover if exe.startswith(os.path.realpath(c).rstrip("/") + "/")]
        if hidden:
            WHY_NOT.append("%s: the interpreter %s is under %s, which anyone may write and the wrap covers with an empty "
                           "tmpfs; run the intake with an interpreter outside every world-writable directory" % (
                               name, exe, hidden[0]))
            continue
        if prefix[-1:] == [RUN]:                     # the wrap's second argument: what it covers
            prefix = prefix + [json.dumps(cover)]
        base = _marker_base(cover)
        if base is None:
            WHY_NOT.append("%s: no directory the runner owns outside every covered one (home, the queue code, the root)" % name)
            continue
        marker = pathlib.Path(tempfile.mkdtemp(prefix=".probe_", dir=base))
        run_dir = pathlib.Path(tempfile.mkdtemp(prefix="probe_run_"))
        token = "probe_%s" % os.urandom(6).hex()
        try:
            marker.chmod(0o755)                       # readable by nobody, writable only by the runner
            if not _hand_over(run_dir, prefix):
                WHY_NOT.append("%s: the run's directory could not be given to nobody" % name)
                continue
            if not reap(prefix):
                WHY_NOT.append("%s: a process of nobody could not be ended before the probe" % name)
                continue
            try:
                r = subprocess.run(wrapped(prefix, run_dir, [sys.executable, "-I", "-c", PROBE, str(marker / "x"), token]),
                                   capture_output=True, text=True, timeout=120, cwd="/")
            finally:
                reaped = reap(prefix)
            held, why = probe_holds(r.stdout, token, cover) if r.returncode == 0 else (False, "")
            if r.returncode == 0 and held and not (marker / "x").exists() and reaped:
                return prefix, name
            WHY_NOT.append("%s: %s" % (name, "; ".join(x for x in (
                "the probe exited %d" % r.returncode if r.returncode else "",
                why, "the probe's file was written" if (marker / "x").exists() else "",
                "a process of nobody outlived the probe" if not reaped else "",
                "its stderr ends: " + " | ".join(r.stderr.strip().splitlines()[-4:])[-600:] if r.stderr.strip() else "",
                "%d directories covered: %s" % (len(cover), ", ".join(cover)[:400])) if x)))
        except (OSError, subprocess.TimeoutExpired) as exc:
            WHY_NOT.append("%s: %s: %s" % (name, type(exc).__name__, str(exc)[:200]))
        finally:
            shutil.rmtree(marker, ignore_errors=True)
            _take_back(run_dir, prefix)
    return [], "no sandbox"


def _run(prefix, argv, cwd, limit, path=None):
    """(exit, out, err, seconds); exit None past the time limit, or when a process of nobody outlives the run (M70).
    `path`, given only for a heavy rerun on the author's machine, is the caller's PATH, where sage and GAP are found"""
    inside = bool(prefix)
    with one_at_a_time() if inside else contextlib.nullcontext():
        return _run_held(prefix, argv, cwd, limit, inside, path)


def _run_held(prefix, argv, cwd, limit, inside, path=None):
    if inside and not reap(prefix):
        return None, "", "a process of the unprivileged user is left from before", 0.0
    env = {"PATH": path or "/usr/local/bin:/usr/bin:/bin", "HOME": "/mnt" if inside else str(cwd), "LANG": "C.UTF-8",
           "PYTHONHASHSEED": "0"}
    t0 = time.time()
    try:
        # the world-writable directories are found again for each run, so one made since the probe is covered too
        r = subprocess.run(wrapped(prefix, cwd, argv, world_writable()) if inside else argv, cwd="/" if inside else cwd,
                           capture_output=True, text=True, timeout=limit, env=env)
        out = (r.returncode, r.stdout, r.stderr, time.time() - t0)
    except subprocess.TimeoutExpired:
        out = (None, "", "", time.time() - t0)
    if inside and not reap(prefix):
        return None, "", "a process of the unprivileged user outlived the run", time.time() - t0
    return out


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
    if argv is None or (argv[2] if argv[0] == sys.executable else argv[1]) != script:
        bad.append("the decisive command is not a plain run of the decisive script: %r" % cmd)
    cargv = _command(control)
    if cargv is None:
        bad.append("the failing control is not a plain run of a script of the commit: %r" % control)
    elif argv is not None and cargv == argv:
        bad.append("the failing control is the decisive command itself")
    scripts = [script] + ([cargv[2] if cargv[0] == sys.executable else cargv[1]] if cargv else [])
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


def rerun(root, commit, card_text, limit=TIME_LIMIT, prefix=None, allow_static=False, heavy=False):
    """the result of rerunning one card at one commit: {status, reasons, ...}. `heavy` (main's M83) is the author's
    machine running a heavy card, by the author's choice: no wrap, the caller's PATH, and sage or GAP allowed to run"""
    heavy_mode = heavy
    if heavy:
        prefix, allow_static = [], True
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
        heavy_run = bool(prefix == [] and allow_static and heavy_mode)
        bad, heavy, argv, cargv = _checks(tmp, modes, script, want, cmd, control)
        if bad:
            res.update(status="RETURNED_AT_INTAKE", reasons=bad)
            return res
        if CF.declared_heavy(f):
            heavy.append("the card declares its decisive script heavy")
        if heavy and not heavy_run:
            res.update(status="HEAVY", reasons=heavy)
            return res
        if not prefix and not allow_static:
            # CHANGED 2026-11-28 (M78 point 2): the reason is the probe's, not a fixed "no unprivileged user in a network
            # namespace", which named a cause nothing had checked
            res.update(status="HEAVY", reasons=["no sandbox can be made here (%s): no seat code runs; for the author's "
                                                "machine" % ("; ".join(WHY_NOT) or "no strategy was tried")])
            return res
        res["guard"] = guard if prefix else "none: the author's machine, by the author's choice"
        if prefix and not _hand_over(tmp, prefix):
            res.update(status="HEAVY", reasons=["the run's directory could not be given to the unprivileged user"])
            return res
        path = os.environ.get("PATH") if heavy_run else None
        rc, out, err, secs = _run(prefix, argv, tmp, limit, path)
        res["seconds"] = round(secs, 1)
        if rc is None:
            res.update(status="HEAVY", reasons=[err or "the decisive script ran past %d seconds" % limit])
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
        crc, _, cerr, csecs = _run(prefix, cargv, tmp, max(1, limit - int(secs)), path)
        res["control_exit"] = crc
        if crc is None:
            res.update(status="HEAVY", reasons=[cerr or "the failing control ran past the time limit"])
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


HEAVY_DIR = "queue/heavy"                       # main's M83: the author's heavy results, landed on main


def tool_versions():
    """the heavy tools' versions on this machine: sage's and GAP's first line, or None"""
    out = {}
    for name, cmd, stdin in (("sage", ["sage", "--version"], None),
                             ("gap", ["gap", "-q"], 'Print(GAPInfo.Version, "\\n");\nQUIT;\n')):
        try:
            r = subprocess.run(cmd, input=stdin, capture_output=True, text=True, timeout=120)
            out[name] = (r.stdout.strip().splitlines() or [None])[0] if r.returncode == 0 else None
        except (OSError, subprocess.TimeoutExpired):
            out[name] = None
    return out


def heavy_result(root, rec, limit=TIME_LIMIT, author_allows=False, at=None):
    """main's M83: (the result file's content, or None, and why not). The author's machine reruns a heavy card at its
    sealed commit, with no wrap, by the author's choice; a card of another seat only with the author's word"""
    if rec.get("seat_code") != CF.QS.MAIN_CODE and not author_allows:
        return None, ("%s is %s's card, not main's: it is rerun here only at the author's word (--author-allows)"
                      % (rec.get("id"), rec.get("seat_code")))
    card = subprocess.run(["git", "show", "%s:%s" % (rec["commit"], rec["card_path"])], cwd=root, capture_output=True,
                          text=True)
    if card.returncode != 0:
        return None, "the card is not at its sealed commit"
    _t, f, _ = CF.read(card.stdout)
    m = CF.SCRIPT.match(f.get("decisive script", ""))
    res = rerun(root, rec["commit"], card.stdout, limit, heavy=True)
    return {"card": rec["id"], "branch": rec["branch"], "path": rec["card_path"], "commit": rec["commit"],
            "script": {"path": m.group(1) if m else None,
                       "sha256": CF.HEX16.search(f["decisive script"]).group(1) if m else None},
            "decisive": res.get("decisive"), "control_exit": res.get("control_exit"), "guard": res.get("guard"),
            "versions": dict(res.get("versions") or {}, **tool_versions()),
            "at": at or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "status": res["status"], "reasons": res["reasons"]}, None


def main(argv):
    if "--heavy-result" in argv:                 # main's M83: on the author's machine
        cid = argv[argv.index("--heavy-result") + 1]
        qdir = pathlib.Path(argv[argv.index("--queue-dir") + 1]) if "--queue-dir" in argv else None
        root = pathlib.Path(argv[argv.index("--root") + 1]) if "--root" in argv else ROOT
        f = qdir / "cards" / ("%s.json" % cid) if qdir else None
        if f is None or not f.is_file():
            print("no record of %s under --queue-dir DIR/cards" % cid)
            return 1
        rec = json.loads(f.read_text(encoding="utf-8"))
        out, why = heavy_result(root, rec, author_allows="--author-allows" in argv)
        if out is None:
            print("refused: %s" % why)
            return 1
        dest = pathlib.Path(root, HEAVY_DIR, "%s.json" % cid)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        print("%s: %s; written to %s, for main to land" % (cid, out["status"], dest))
        return 0 if out["status"] == "REPRODUCED" else 1
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
