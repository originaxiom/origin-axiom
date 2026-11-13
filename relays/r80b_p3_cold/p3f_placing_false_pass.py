#!/usr/bin/env python3
"""P3-F again, with a plant that can show the false pass the builder disclosed for Part 3 patch 17 (B1894's strict placing).
The first plant used a sentence of the foundation, which stands in no FINDINGS.md; this one uses a sentence that stands in
another arc's FINDINGS.md, and a finding that names a path not at the commit ending in FINDINGS.md."""
import importlib.util, os, pathlib, shutil, subprocess, sys, tempfile
REPO = pathlib.Path(__file__).resolve().parents[2]
ENV = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", PYTHONDONTWRITEBYTECODE="1")
P17 = "relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_3/0017_b1894s_quotation_checker_places_strictly.patch"
tmp = pathlib.Path(tempfile.mkdtemp(prefix="agy002_p3f_")); wt = tmp / "wt"
try:
    subprocess.run(["git", "-C", str(REPO), "worktree", "add", "-q", "--detach", str(wt), "bf76e5ab1"], check=True, env=ENV)
    (tmp / "p.patch").write_bytes(subprocess.check_output(["git", "-C", str(REPO), "show", "bc71f9373:" + P17]))
    subprocess.run(["git", "-C", str(wt), "apply", "--include=frontier/B1894_review_79_the_second_round/verification/quote_check.py", str(tmp / "p.patch")], check=True, env=ENV)
    spec = importlib.util.spec_from_file_location("qc", wt / "frontier/B1894_review_79_the_second_round/verification/quote_check.py")
    qc = importlib.util.module_from_spec(spec); spec.loader.exec_module(qc)
    other_page = wt / "frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md"
    sentence = "- **Nothing is selected.** No point named here is compared with anything."
    assert sentence in other_page.read_text(encoding="utf-8")
    q = "Nothing is selected.** No point named here is compared with anything."
    print("a sentence of B1881's FINDINGS.md, for a finding on B1894 that names frontier/B9999_no_such_arc/FINDINGS.md:")
    print("  placed() ->", repr(qc.placed(q, "B1894", "frontier/B9999_no_such_arc/FINDINGS.md")))
    print("  the same, the finding naming B1894's own FINDINGS.md (at the commit) ->", repr(qc.placed(q, "B1894", "frontier/B1894_review_79_the_second_round/FINDINGS.md")))
finally:
    subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(wt)], capture_output=True)
    shutil.rmtree(tmp, ignore_errors=True)
