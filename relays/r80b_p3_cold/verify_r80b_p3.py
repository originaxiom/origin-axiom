#!/usr/bin/env python3
"""Independent cold-read verification of rebuilt builder series R80b Part 3
(relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_3/ at bc71f9373), eighteen patches.

Applies Part 1 (112e73d67) + rebuilt Part 2 + rebuilt Part 3 onto main's bf76e5ab1 in a temporary detached worktree,
checks scope and attribution against STATUS_OF_THE_57.md, runs the changed tests and all gates, and puts unseen plants of
agy-002's own to each mended test.  COI (said in the card): patch 9's change to main's table of answers to agy-002's own
rows, the agy-002 page in patch 12, and the lines of B1894 that judge agy-002's Review 79 work are left aside on substance.
"""
import importlib.util
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]
BASE = "bf76e5ab1"
P1 = "112e73d67"
SENT = "bc71f9373"
D = "relays/advisor_2026-11-10_audit/r80b"
UNCHECKED_BY_MAIN = {   # patch number -> STATUS_OF_THE_57.md row given as "not checked"
    1: "W8", 2: "W9", 4: "SM-33", 5: "SM-26", 6: "SM-41", 11: "SM-32", 13: "F11", 14: "F14", 15: "F13", 16: "F6(b)",
}
ENV = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", PYTHONDONTWRITEBYTECODE="1")


def blob(spec):
    return subprocess.check_output(["git", "-C", str(REPO), "show", spec])


def names(rev, path):
    return [p.split("/")[-1] for p in subprocess.check_output(["git", "-C", str(REPO), "ls-tree", "--name-only", rev, path + "/"], text=True).split()]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def pytest(wt, *paths):
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *map(str, paths)], cwd=str(wt), capture_output=True, text=True, env=ENV)
    return r.returncode, (r.stdout.strip().splitlines() or [""])[-1]


def main():
    print("=== A2-S-R80b-p3 cold read: rebuilt Part 3 (bc71f9373) on bf76e5ab1 + Part 1 + rebuilt Part 2 ===")
    p3 = sorted(n for n in names(SENT, D + "/on_mains_bf76e5ab1/part_3") if n.endswith(".patch"))
    p2 = sorted(n for n in names(SENT, D + "/on_mains_bf76e5ab1/part_2") if n.endswith(".patch"))
    assert len(p3) == 18 and len(p2) == 12

    # 1. attribution: every row STATUS_OF_THE_57.md gives as not checked is said to be not checked, in the patch's subject
    for i, n in enumerate(p3, 1):
        subj = blob("%s:%s/on_mains_bf76e5ab1/part_3/%s" % (SENT, D, n)).decode("utf-8").split("\n\n", 1)[0]
        flat = " ".join(subj.split())
        if i in UNCHECKED_BY_MAIN:
            assert "NOT CHECKED" in flat or "not checked by main" in flat, (i, n)
        assert "reproduced by main" not in flat.lower(), n
    subj17 = " ".join(blob("%s:%s/on_mains_bf76e5ab1/part_3/%s" % (SENT, D, p3[16])).decode("utf-8").split("\n\n", 1)[0].split())
    assert "checked for its shape on B1892's checker and not on this one" in subj17
    print("[ATTR] the ten patches whose rows are 'not checked' by main say so in their subjects; patch 17 says F7 was checked for its shape only")

    tmp = pathlib.Path(tempfile.mkdtemp(prefix="agy002_r80b_p3_"))
    wt = tmp / "wt"
    try:
        pd = tmp / "p"; pd.mkdir()
        for n in ("0001_message.txt", "0001_the_plans_page_gives_the_owners_answer_in_plain_words.py",
                  "0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch",
                  "0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch"):
            (pd / ("p1_" + n)).write_bytes(blob("%s:%s/part_1/%s" % (P1, D, n)))
        for n in p2:
            (pd / ("p2_" + n)).write_bytes(blob("%s:%s/on_mains_bf76e5ab1/part_2/%s" % (SENT, D, n)))
        for n in p3:
            (pd / ("p3_" + n)).write_bytes(blob("%s:%s/on_mains_bf76e5ab1/part_3/%s" % (SENT, D, n)))
        subprocess.run(["git", "-C", str(REPO), "worktree", "add", "--detach", str(wt), BASE], check=True, capture_output=True)
        subprocess.run([sys.executable, "-B", str(pd / "p1_0001_the_plans_page_gives_the_owners_answer_in_plain_words.py"), str(wt)], check=True, capture_output=True, env=ENV)
        subprocess.run(["git", "-C", str(wt), "commit", "-qF", str(pd / "p1_0001_message.txt")], check=True, env=ENV)
        subprocess.run(["git", "-C", str(wt), "am", "-q", str(pd / "p1_0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch"),
                        str(pd / "p1_0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch")], check=True, env=ENV)
        subprocess.run(["git", "-C", str(wt), "am", "-q"] + [str(pd / ("p2_" + n)) for n in p2], check=True, env=ENV)
        before = subprocess.check_output(["git", "-C", str(wt), "rev-parse", "HEAD"], text=True).strip()
        subprocess.run(["git", "-C", str(wt), "am", "-q"] + [str(pd / ("p3_" + n)) for n in p3], check=True, env=ENV)
        tree = subprocess.check_output(["git", "-C", str(wt), "write-tree"], text=True).strip()
        changed = subprocess.check_output(["git", "-C", str(wt), "diff", "--name-only", before, "HEAD"], text=True).split()
        print("[TREE] all 18 apply by git am after Part 2; tree %s; %d files changed by Part 3" % (tree, len(changed)))
        outside = [f for f in changed if not f.startswith(("frontier/B732_", "frontier/B942_", "frontier/B1884_", "frontier/B1882_", "frontier/B874_",
                   "tests/", "docs/seats/", "docs/views/", "docs/handoffs/", "frontier/B1898_", "frontier/B1893_", "docs/POINT_REGISTER.md",
                   "CHANGELOG.md", "PROGRESS_LOG.md", "README.md", "docs/HARVEST_LEDGER.md", "docs/LAW_MAP.md", "frontier/B1894_",
                   "frontier/B862_", "frontier/B1222_", "frontier/B1891_", "frontier/B1883_", "scripts/atlas/", "frontier/B1641_"))]
        print("[SCOPE] files outside the arcs and pages the eighteen rows name: %s" % (outside or "none"))
        print("[SCOPE] Part 3 files: " + ", ".join(changed))

        tests = sorted({f for f in changed if f.endswith(".py") and pathlib.Path(f).name.startswith("test_")})
        rc, last = pytest(wt, *[wt / t for t in tests])
        print("[TESTS] the %d test files Part 3 changes, on its last patch: rc=%d, %s" % (len(tests), rc, last))

        rg = subprocess.run([sys.executable, "-B", str(wt / "scripts/gates/gates.py")], cwd=str(wt), capture_output=True, text=True, env=ENV)
        fails = [l for l in rg.stdout.splitlines() if l.lstrip().startswith("FAIL")]
        print("[GATES] on the last patch of Part 3: rc=%d; failing lines: %s" % (rg.returncode, fails or "none"))
        print("        " + " | ".join(l.strip() for l in rg.stdout.splitlines() if "review-due" in l))

        # 2. unseen plants of agy-002's own against the mended tests
        print("\n=== Unseen plants against Part 3's mended tests ===")

        # P3-A, patch 3 (SM-35): the verdict line of B1884 says main's own convention again, with a typographic apostrophe
        vpath = wt / "frontier/B1884_what_level_a_ground_names_verified/arc_verdict.json"
        orig = vpath.read_text(encoding="utf-8")
        v = json.loads(orig)
        v["claim_one_line"] = v["claim_one_line"].replace(" 0 of 19.", " The same counts hold in main\u2019s own convention. 0 of 19.")
        vpath.write_text(json.dumps(v, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        rc, last = pytest(wt, wt / "frontier/B1884_what_level_a_ground_names_verified/verification/test_b1884_what_level_a_ground_names_verified.py")
        vpath.write_text(orig, encoding="utf-8")
        print("  P3-A (B1884 line given 'main\u2019s own convention' again, typographic apostrophe): lock rc=%d %s -> %s" % (rc, last, "PASSES (not seen)" if rc == 0 else "caught"))

        # P3-B, patch 6 (SM-41): a false statement added to B874's bracket outside the two sentences the test holds word for word
        vpath = wt / "frontier/B874_measurement_ladder/arc_verdict.json"
        orig = vpath.read_text(encoding="utf-8")
        v = json.loads(orig)
        relay = "and over the reals {12, 16, 18}, with 30 and 46 degenerately."
        assert v["claim_one_line"].count(relay) == 1
        v["claim_one_line"] = v["claim_one_line"].replace(relay, relay + " So on the real line the nullity reaches 26.")
        vpath.write_text(json.dumps(v, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        rc, last = pytest(wt, wt / "tests/test_b874_ladder.py")
        vpath.write_text(orig, encoding="utf-8")
        print("  P3-B (B874 bracket given a false third sentence after the relay's words): test rc=%d %s -> %s" % (rc, last, "PASSES (not seen)" if rc == 0 else "caught"))

        # P3-C, patch 14 (F14): the old level stated in a verdict file's 'disclosed' field
        t734 = load("agy002_t734", wt / "tests/test_b734_m004_congruence.py")
        raw = json.dumps({"id": "B0", "claim_one_line": "Another matter. 0 of 19.", "disclosed": "m004 is a congruence subgroup of level 8"})
        seen = t734._states_the_old_level(t734._of_a_verdict_file(raw))
        print("  P3-C (B734 sweep: old level in a verdict file's 'disclosed' field): %s" % ("caught" if seen else "PASSES (only claim_one_line, scope and note are read)"))

        # P3-D, patch 15 (F13): a list written with a typographic bullet; the correction in one item, the zero in another
        t1028 = load("agy002_t1028", wt / "tests/test_b1028_freedom_ledger.py")
        note = "[CORRECTED 2026-11-11 (the audit's finding E7): " + t1028.MARK + ".]"
        dash = "The counterexamples:\n- one thing, noted. " + note + "\n- a second thing\n- **designer freedom 0.000 bits** is a count over the chain"
        dot = dash.replace("\n- ", "\n\u2022 ")
        print("  P3-D (B1028 sweep): with '- ' bullets reported=%d (control); with '\u2022 ' bullets reported=%d -> %s" % (
            len(t1028._bare_statements(dash)), len(t1028._bare_statements(dot)), "PASSES (not seen)" if not t1028._bare_statements(dot) else "caught"))

        # P3-E, patch 12 (SM-27): the old sign written on a page outside the four the test names
        rpath = wt / "docs/THE_CLAIM.md"
        orig = rpath.read_text(encoding="utf-8")
        rpath.write_text(orig + "\nOn the cusp, a unit on one line gives index one.\n", encoding="utf-8")
        rc, last = pytest(wt, wt / "frontier/B1894_review_79_the_second_round/verification/test_b1894_review_79_the_second_round.py")
        rpath.write_text(orig, encoding="utf-8")
        print("  P3-E (old sign of the index added to docs/THE_CLAIM.md, a page outside the four named): B1894 lock rc=%d %s -> %s" % (rc, last, "PASSES (not seen)" if rc == 0 else "caught"))

        # P3-F, patch 17 (F7): the disclosed false pass of the strict placing: a path not at the commit, ending in a common name
        qc = load("agy002_qc1894", wt / "frontier/B1894_review_79_the_second_round/verification/quote_check.py")
        other = "No item is added and no status cell changes."
        where = qc.placed(other, "B1894", "frontier/B9999_no_such_arc/FINDINGS.md")
        print("  P3-F (B1894 placed(): a sentence of a wide page, finding naming a path not at the commit that ends in 'FINDINGS.md'): placed=%r -> %s" % (
            where, "false 'named' (the builder's disclosed fault, confirmed)" if where == "named" else "not named"))

        # P3-G, patch 3 (SM-34): control: the count of levels with two points changed on the page is caught
        fpath = wt / "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md"
        orig = fpath.read_text(encoding="utf-8")
        assert "173 have none and 25 have two" in orig
        fpath.write_text(orig.replace("173 have none and 25 have two", "172 have none and 26 have two"), encoding="utf-8")
        rc, last = pytest(wt, wt / "frontier/B1884_what_level_a_ground_names_verified/verification/test_b1884_what_level_a_ground_names_verified.py")
        fpath.write_text(orig, encoding="utf-8")
        print("  P3-G (control: B1884's count changed on the page): lock rc=%d -> %s" % (rc, "caught" if rc else "PASSES"))

        # P3-H, patch 7 (B448): control: the degree list is computed, so a false list fails
        t448 = (wt / "tests/test_b448.py").read_text(encoding="utf-8")
        assert t448.count("== [1, 5]") == 1
        (wt / "tests/test_b448.py").write_text(t448.replace("== [1, 5]", "== [1, 2, 5]"), encoding="utf-8")
        rc, last = pytest(wt, wt / "tests/test_b448.py")
        (wt / "tests/test_b448.py").write_text(t448, encoding="utf-8")
        print("  P3-H (control: B448's asserted degrees changed to [1, 2, 5]): rc=%d -> %s" % (rc, "caught" if rc else "PASSES"))
    finally:
        subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(wt)], capture_output=True)
        shutil.rmtree(tmp, ignore_errors=True)
    print("\n=== A2-S-R80b-p3 VERIFICATION COMPLETE (EXIT 0) ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
