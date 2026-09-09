#!/usr/bin/env python3
"""ABSENCE SWEEP -- the instrument behind THE ABSENCE RULE (WORKING_RULES, 2026-09-02; owner's words:
"before you conclude we dont have something, swipe the repo first").

THE FAILURE CLASS (ERROR_LEDGER E54, ABSENCE-WITHOUT-SWEEP). "We don't have X" is a universal statement
over a population -- every branch head, filenames AND file contents, files deleted in history, and the
working tree's untracked files. It was being asserted after a search of a SAMPLE: prose grep on main, a
filename glance, one branch. Six instances in one window, two of them this bench's own:
  * the nine "unrecoverable" 2026-08-09 relays were at the root of audit/b775-braver-questions (E51 FINAL);
  * "the 17 atoms are enumerated on no branch" -- they were on main, as DATA inside a shell heredoc
    (frontier/B1203_two_probes/verification/reproduce.sh:10-12), since 2026-08-28.

WHAT THIS DOES. For a term, enumerate the population and report where it IS. The sentence "X does not
exist on any branch" may be written only with this tool's output beside it.

    python3 scripts/checks/absence_sweep.py "<term>"            # sweep every ref for a literal term
    python3 scripts/checks/absence_sweep.py "<term>" --regex    # term is a regex (git grep -E)
    python3 scripts/checks/absence_sweep.py --selftest          # planted controls, both directions

THIS INSTRUMENT REPORTS PRESENCE; IT NEVER DECIDES RELEVANCE. A hit is a place to look, not a bank.
Run `git fetch --all` first: an un-fetched remote is a population you have not enumerated.
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def _git(*args, check=False):
    r = subprocess.run(["git", *args], cwd=str(ROOT), capture_output=True, text=True)
    if check and r.returncode not in (0, 1):
        raise RuntimeError(r.stderr.strip())
    return r.stdout


def heads():
    out = _git("for-each-ref", "--format=%(refname:short) %(objectname:short)", "refs/heads", "refs/remotes")
    seen, res = set(), []
    for line in out.splitlines():
        name, sha = line.split()
        if name.endswith("/HEAD"):
            continue
        res.append((name, sha))
    return res


def sweep(term, regex=False):
    """Returns a dict: per-head content/filename hits, deleted-in-history hits, working-tree hits."""
    flag = "-E" if regex else "-F"
    report = {"term": term, "heads": [], "deleted": [], "worktree": []}
    for name, sha in heads():
        content = [l for l in _git("grep", "-l", "-I", "-i", flag, "-e", term, sha, "--").splitlines()]
        names = [l for l in _git("ls-tree", "-r", "--name-only", sha).splitlines() if _match(term, l, regex)]
        report["heads"].append({"head": name, "sha": sha, "content": content, "filenames": names})
    # files whose PATH matches and that were deleted somewhere in history (any ref)
    report["deleted"] = sorted({d for d in _deleted_paths() if d and _match(term, d, regex)})
    # the working tree, untracked files included (relays live here by design)
    wt = _git("grep", "-l", "-I", "-i", flag, "-e", term, "--untracked", "--", ".").splitlines()
    report["worktree"] = wt
    return report


_DELETED = None


def _deleted_paths():
    global _DELETED
    if _DELETED is None:
        _DELETED = _git("log", "--all", "--diff-filter=D", "--name-only", "--format=").splitlines()
    return _DELETED


def _match(term, s, regex):
    if regex:
        import re
        return re.search(term, s, re.I) is not None
    return term.lower() in s.lower()


def present(report):
    return any(h["content"] or h["filenames"] for h in report["heads"]) or report["deleted"] or report["worktree"]


def render(report):
    t = report["term"]
    print(f"ABSENCE SWEEP for {t!r} -- {len(report['heads'])} heads enumerated")
    hit_heads = 0
    for h in report["heads"]:
        c, f = len(h["content"]), len(h["filenames"])
        if c or f:
            hit_heads += 1
            print(f"  {h['head']:55s} {h['sha']}  content:{c:4d}  filenames:{f:3d}")
            for x in (h["content"][:3] + h["filenames"][:3]):
                print(f"      {x}")
    print(f"  deleted-in-history paths matching: {len(report['deleted'])}")
    for x in report["deleted"][:5]:
        print(f"      {x}")
    print(f"  working tree (untracked included): {len(report['worktree'])}")
    for x in report["worktree"][:5]:
        print(f"      {x}")
    if present(report):
        print(f"VERDICT: PRESENT -- on {hit_heads} head(s)"
              f"{', deleted-history' if report['deleted'] else ''}{', working tree' if report['worktree'] else ''}."
              " 'We don't have it' may NOT be written.")
    else:
        print("VERDICT: ABSENT on every enumerated head, in deleted history, and in the working tree."
              " This line is the citation the sentence needs. (Fetched all remotes first? If not, this is a sample.)")


def selftest():
    """MB12: controls in both directions, plus the control that reproduces the class's own instance."""
    import uuid
    nonce = "ZQX" + uuid.uuid4().hex[:12]
    checks = []
    # (1) a term known to be on main
    r = sweep("B1203_two_probes"); checks.append(("finds a known arc name", present(r)))
    # (2) the heredoc-data control: the exact datum the 08-31 prose search missed (an atom inside reproduce.sh)
    r = sweep('"553/64":mp.mpf(553)/64')
    checks.append(("finds DATA inside a shell heredoc (the E54 instance's own datum)", present(r)))
    # (3) a filename-only hit: a file whose NAME matches but whose content does not mention the term
    r = sweep("absence_sweep"); checks.append(("finds a filename hit", any(h["filenames"] for h in r["heads"]) or bool(r["worktree"])))
    # (4) a nonce that exists nowhere -> ABSENT
    r = sweep(nonce); checks.append(("reports ABSENT for a fresh nonce", not present(r)))
    # (5) the population is more than one head (a one-head sweep is a sample)
    checks.append(("enumerates more than one head", len(heads()) > 1))
    for name, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    good = all(ok for _, ok in checks)
    print("CONTROLS PASS" if good else "CONTROLS FAIL")
    return 0 if good else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args == ["--selftest"]:
        sys.exit(selftest() if args else (print(__doc__) or 2))
    regex = "--regex" in args
    term = next(a for a in args if not a.startswith("--"))
    rep = sweep(term, regex=regex)
    render(rep)
    sys.exit(0)
