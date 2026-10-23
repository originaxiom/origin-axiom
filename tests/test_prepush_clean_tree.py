"""R68-8: the pre-push runner gates the commit being pushed in a clean worktree, not the working tree. The failing path:
a failing gate run makes the push fail; the worktree sits at the pushed commit and is removed afterwards; deletions are
skipped. The gates themselves are replaced by a recording runner, so this test does not run them."""
import io, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "gates"))
import prepush as P


def _head():
    return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()


def _worktrees():
    return subprocess.run(["git", "-C", str(ROOT), "worktree", "list", "--porcelain"], capture_output=True, text=True, check=True).stdout


def test_deletions_and_repeats_skipped():
    h = _head()
    lines = ["refs/heads/main %s refs/heads/main %s" % (h, "1" * 40), "(delete) %s refs/heads/x %s" % (P.ZERO, h),
             "refs/heads/y %s refs/heads/y %s" % (h, P.ZERO), "garbage"]
    assert P.shas_to_gate(lines) == [h]


def test_the_commit_is_gated_in_a_clean_worktree_and_removed():
    h = _head(); seen = []
    def runner(cmd, cwd):
        seen.append((cmd, cwd, subprocess.run(["git", "-C", cwd, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip(),
                     subprocess.run(["git", "-C", cwd, "status", "--porcelain", "--untracked-files=no"], capture_output=True, text=True).stdout))
        return 0
    status, head = P.gate_commit(str(ROOT), h, runner)
    assert status == 0 and head == h and len(seen) == 1
    cmd, cwd, wt_head, wt_status = seen[0]
    assert wt_head == h and wt_status == ""                                   # the pushed commit, with no local edits
    assert cmd[-1].startswith(cwd) and cmd[-1].endswith("scripts/gates/gates.py")   # that commit's own gates
    assert cwd not in _worktrees() and not pathlib.Path(cwd).exists()         # removed afterwards


def test_a_failing_gate_fails_the_push():
    h = _head()
    st = P.main(stdin=io.StringIO("refs/heads/main %s refs/heads/main %s\n" % (h, "1" * 40)), root=str(ROOT), runner=lambda cmd, cwd: 1)
    assert st == 1
    assert P.main(stdin=io.StringIO("refs/heads/main %s refs/heads/main %s\n" % (h, "1" * 40)), root=str(ROOT), runner=lambda cmd, cwd: 0) == 0
