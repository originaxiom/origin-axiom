"""SHARED SOURCE MODULE for outside-bench certificates that read the
primary record — created 2026-08-29 in response to CODEX's evidence-
contract audit, which charged that "multiple outside scripts depend on
FLOATING GIT REFS, ABSENT MAIN ARTIFACTS or self-scan growing files".

THE CHARGE WAS CORRECT.  Six certificates read `origin/main` (a ref that
MOVES, so a re-run months later reads different data and the vendored
output stops matching) or `/tmp/av` (a scratch directory that exists only
on the machine that made it).  Neither is reproducible by a second seat,
which is the whole point of a certificate.

THE FIX, in one place:
  * PINNED_REF is a COMMIT SHA, not a branch.  A re-run reads exactly the
    bytes the vendored output was produced from, forever.
  * arc_verdicts() materializes the arc files FROM THAT SHA into a cache
    directory it creates itself — no pre-existing scratch dir required.
  * OA_REF may still be overridden by environment for a deliberate
    re-point; the DEFAULT is pinned.
"""
import json, os, subprocess, tempfile, glob

# main @ B1212, the state every vendored output in this lane was read from
PINNED_REF = "3c58527bc3851ae44fef4f48ecc1eac8aa9dd41b"

REPO = os.environ.get("OA_REPO", os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))
REF = os.environ.get("OA_REF", PINNED_REF)

def _git(*args, check=True):
    r = subprocess.run(["git", "-C", REPO, *args],
                       capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr[:200]}")
    return r.stdout

def primary_text(path):
    """Exact bytes of one file at the pinned commit."""
    return _git("show", f"{REF}:{path}")

def primary_json(path):
    return json.loads(primary_text(path))

def grep(pattern, *pathspec, flags=("-h", "-i", "-o", "-E")):
    """git grep at the pinned commit (never a moving branch)."""
    out = _git("grep", *flags, pattern, REF, "--", *pathspec, check=False)
    return [l for l in out.splitlines() if l.strip()]

_CACHE = None
def arc_verdicts():
    """Every frontier/*/arc_verdict.json AT THE PINNED COMMIT, materialized
    into a cache dir this function creates — no /tmp/av precondition."""
    global _CACHE
    if _CACHE is not None:
        return _CACHE
    d = os.path.join(tempfile.gettempdir(), f"oa_arcs_{REF[:12]}")
    if not os.path.isdir(d) or not glob.glob(os.path.join(d, "**", "arc_verdict.json"),
                                             recursive=True):
        os.makedirs(d, exist_ok=True)
        names = [n for n in _git("ls-tree", "-r", "--name-only", REF).splitlines()
                 if n.endswith("arc_verdict.json")]
        tar = subprocess.run(["git", "-C", REPO, "archive", REF, *names],
                             capture_output=True)
        subprocess.run(["tar", "-x", "-C", d], input=tar.stdout, check=True)
    out = {}
    for p in glob.glob(os.path.join(d, "**", "arc_verdict.json"), recursive=True):
        try:
            v = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        if isinstance(v.get("id"), str):
            out[v["id"]] = v
    _CACHE = out
    return out
