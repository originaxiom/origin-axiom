#!/usr/bin/env python3
"""Why point-debt fails on agy-002's checkout of Part 2 and passes on main's bf76e5ab1 and head: the gate's day is HEAD's
commit day (scripts/checks/point_debt.py, commit_day.py), and the patches applied here by git am carry today's committer date.
The point-debt check is run on the Part 2 tree three ways: as it is; with OA_POINT_TODAY=2026-11-12; with OA_POINT_TODAY=2026-11-13."""
import os, pathlib, shutil, subprocess, sys, tempfile
REPO = pathlib.Path(__file__).resolve().parents[2]
ENV = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", PYTHONDONTWRITEBYTECODE="1")
R = "relays/advisor_2026-11-10_audit/r80b"
tmp = pathlib.Path(tempfile.mkdtemp(prefix="agy002_pdday_")); wt = tmp / "wt"; pd = tmp / "p"; pd.mkdir()
show = lambda s: subprocess.check_output(["git", "-C", str(REPO), "show", s])
try:
    for n in ("0001_message.txt", "0001_the_plans_page_gives_the_owners_answer_in_plain_words.py",
              "0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch", "0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch"):
        (pd / ("a_" + n)).write_bytes(show("112e73d67:%s/part_1/%s" % (R, n)))
    p2 = sorted(x.split("/")[-1] for x in subprocess.check_output(["git", "-C", str(REPO), "ls-tree", "--name-only", "bc71f9373", R + "/on_mains_bf76e5ab1/part_2/"], text=True).split())
    for n in p2:
        (pd / ("b_" + n)).write_bytes(show("bc71f9373:%s/on_mains_bf76e5ab1/part_2/%s" % (R, n)))
    subprocess.run(["git", "-C", str(REPO), "worktree", "add", "-q", "--detach", str(wt), "bf76e5ab1"], check=True, env=ENV)
    subprocess.run([sys.executable, "-B", str(pd / "a_0001_the_plans_page_gives_the_owners_answer_in_plain_words.py"), str(wt)], check=True, capture_output=True, env=ENV)
    subprocess.run(["git", "-C", str(wt), "commit", "-qF", str(pd / "a_0001_message.txt")], check=True, env=ENV)
    subprocess.run(["git", "-C", str(wt), "am", "-q", str(pd / "a_0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch"), str(pd / "a_0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch")] + [str(pd / ("b_" + n)) for n in p2], check=True, env=ENV)
    print("HEAD's committer day here:", subprocess.check_output(["git", "-C", str(wt), "log", "-1", "--format=%cs"], text=True).strip())
    print("bf76e5ab1's committer day:", subprocess.check_output(["git", "-C", str(wt), "log", "-1", "--format=%cs", "bf76e5ab1"], text=True).strip())
    for label, extra in (("as it is", {}), ("OA_POINT_TODAY=2026-11-12", {"OA_POINT_TODAY": "2026-11-12"}), ("OA_POINT_TODAY=2026-11-13", {"OA_POINT_TODAY": "2026-11-13"})):
        r = subprocess.run([sys.executable, "-B", "scripts/checks/point_debt.py"], cwd=str(wt), capture_output=True, text=True, env=dict(ENV, **extra))
        fails = [l.strip() for l in r.stdout.splitlines() if l.strip().startswith("FAIL")]
        print("point_debt.py on Part 2, %s: rc=%d; %d failing rows: %s" % (label, r.returncode, len(fails), "; ".join(f[:60] for f in fails)))
finally:
    subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(wt)], capture_output=True)
    shutil.rmtree(tmp, ignore_errors=True)
