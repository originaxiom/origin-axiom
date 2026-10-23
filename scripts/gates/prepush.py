"""R68-8 (Review 68): the pre-push gates run on the commit being pushed, not on the working tree.

git's pre-push hook receives on stdin one line per ref: <local ref> <local sha> <remote ref> <remote sha>.  For every
ref that is not a deletion, this checks out <local sha> in a temporary detached worktree, runs that commit's own
scripts/gates/gates.py there, and removes the worktree.  It exits non-zero if any run fails.

Why: gates.py reads the tree it sits in.  On 2026-10-23 a clean outputs commit (B1726's) failed atlas-fresh,
views-generated and point-debt because the next landing's uncommitted arcs and register rows were in the working tree;
it was gated and pushed by hand from a clean worktree at its own head, where every gate passed.  A gate that reads the
tree can block a correct push or pass a wrong one.
    python3 scripts/gates/prepush.py < <pre-push stdin>      # the hook passes its stdin through"""
import os, subprocess, sys, tempfile

ZERO = "0" * 40


def shas_to_gate(lines):
    """the local shas of the refs being pushed (deletions skipped), in order, without repeats"""
    out = []
    for line in lines:
        parts = line.split()
        if len(parts) != 4: continue
        sha = parts[1]
        if sha == ZERO or sha in out: continue
        out.append(sha)
    return out


def gate_commit(root, sha, runner=None):
    """run the gates of commit `sha` in a temporary detached worktree; return (exit status, the worktree's HEAD)"""
    runner = runner or (lambda cmd, cwd: subprocess.run(cmd, cwd=cwd).returncode)
    tmp = tempfile.mkdtemp(prefix="oa-prepush-")
    wt = os.path.join(tmp, "wt")
    subprocess.run(["git", "-C", root, "worktree", "add", "-q", "--detach", wt, sha], check=True)
    try:
        head = subprocess.run(["git", "-C", wt, "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        status = runner([sys.executable, os.path.join(wt, "scripts", "gates", "gates.py")], wt)
        return status, head
    finally:
        subprocess.run(["git", "-C", root, "worktree", "remove", "--force", wt], check=False)
        try: os.rmdir(tmp)
        except OSError: pass


def main(stdin=None, root=None, runner=None):
    root = root or subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
    shas = shas_to_gate((stdin or sys.stdin).read().splitlines())
    worst = 0
    for sha in shas:
        print("[pre-push] gating %s in a clean worktree..." % sha[:9], flush=True)
        status, _ = gate_commit(root, sha, runner)
        if status: print("[pre-push] gates FAILED on %s" % sha[:9], flush=True)
        worst = worst or status
    return worst


if __name__ == "__main__":
    sys.exit(main())
