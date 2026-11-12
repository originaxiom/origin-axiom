#!/usr/bin/env python3
"""The eight tests that fail in the full suite on a fresh clone of the patch, run alone, one process, in a fresh clone of
main's head and in a fresh clone of the patch.  The clone is made as the review's tool makes it.
usage: the_eight_in_fresh_clones.py <repository> <commit> [<commit> ...]"""
import os, shutil, subprocess, sys, tempfile
EIGHT = """frontier/B1849_the_leads_confirmed_one_by_one/verification/test_b1849_the_leads_confirmed_one_by_one.py::test_the_cyclic_texture_check_reproduces
frontier/B1850_the_open_leads_and_the_backlog_confirmed/verification/test_b1850_the_open_leads_and_the_backlog_confirmed.py::test_the_generating_pair_check_reproduces
frontier/B1866_the_agy_lanes_join_relay_scrutinised/verification/test_b1866_the_agy_lanes_join_relay_scrutinised.py::test_the_scrutiny_reproduces
tests/test_b1425_determinism.py::test_the_papers_retraction_count_matches_the_index
tests/test_b1426_every_lane_is_watched.py::test_no_lane_with_unique_work_is_outside_the_gate
tests/test_b1449_silent_receipts.py::test_the_decisive_test_of_b469_reproduces_with_the_fix_live
tests/test_b805_forcing.py::test_gaps_are_reported_not_hidden
tests/test_b805_forcing.py::test_graph_builds_and_separates_authored_edges_from_attachment""".split()
root = sys.argv[1]
for head in sys.argv[2:]:
    tmp = tempfile.mkdtemp(prefix="oa-fresh-eight-")
    try:
        subprocess.run(["git", "clone", "--quiet", "--no-local", root, tmp], check=True, capture_output=True)
        subprocess.run(["git", "checkout", "--quiet", head], cwd=tmp, check=True, capture_output=True)
        subprocess.run(["git", "fetch", "--quiet", root, "+refs/remotes/origin/*:refs/remotes/origin/*"], cwd=tmp, capture_output=True)
        env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:randomly", "-p", "no:cacheprovider", "-rf", "--tb=line"] + EIGHT,
                           cwd=tmp, capture_output=True, text=True, env=env)
        print("== in a fresh clone of %s" % head)
        print("\n".join(l.replace(tmp, "<the clone>") for l in (r.stdout + r.stderr).splitlines() if l.strip()))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
