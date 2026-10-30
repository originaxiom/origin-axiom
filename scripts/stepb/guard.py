"""STEP B's generator, the push-before-read guard (the fourth review's integrity items; data-free).

Before any driver reads the refined census, the census's manifest must be committed, and the commit that last changed it
must be an ancestor of origin/main (pushed); its recorded sha256_of_the_manifest must equal the value the driver is given,
and the working file must equal the committed one.  The check uses git only; it reads no census file."""
from __future__ import annotations

import hashlib, json, pathlib, subprocess


def _git(root, *args) -> str:
    """git's output; any git failure is a refusal (no commit, no repository, no origin/main)"""
    try:
        return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True).stdout.strip()
    except subprocess.CalledProcessError as e:
        raise SystemExit("refused: git %s failed (%s)" % (" ".join(args[:2]), (e.stderr or "").strip()[:120]))


def require_pushed_manifest(manifest_path, expected_sha256: str) -> dict:
    p = pathlib.Path(manifest_path).resolve()
    root = pathlib.Path(_git(p.parent, "rev-parse", "--show-toplevel"))
    rel = str(p.relative_to(root))
    commit = _git(root, "log", "-n", "1", "--format=%H", "--", rel)
    if not commit:
        raise SystemExit("refused: the manifest %s is not committed" % rel)
    try:
        committed = subprocess.run(["git", "-C", str(root), "show", "%s:%s" % (commit, rel)], check=True, capture_output=True).stdout
    except subprocess.CalledProcessError:
        raise SystemExit("refused: the manifest cannot be read at its commit %s" % commit[:12])
    if committed != p.read_bytes():
        raise SystemExit("refused: the working manifest differs from its last commit %s" % commit[:12])
    try:
        subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor", commit, "origin/main"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        raise SystemExit("refused: the manifest's commit %s is not on origin/main (push it first)" % commit[:12])
    man = json.loads(committed)
    per = man["per_file"]
    h = hashlib.sha256("".join("%s  %s\n" % (v, n) for n, v in sorted(per.items())).encode()).hexdigest()
    if h != man["sha256_of_the_manifest"] or h != expected_sha256:
        raise SystemExit("refused: the manifest's hash %s is not the one given" % h)
    return {"manifest_commit": commit, "sha256_of_the_manifest": h, "files": len(per), "per_file": per}
