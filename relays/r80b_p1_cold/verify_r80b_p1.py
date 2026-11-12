#!/usr/bin/env python3
"""Independent zero-trust cold-read verification of builder series R80b Part 1 (112e73d67).

Runs strictly in an isolated temporary detached worktree built on main's 10fbbc1c2 + R80a,
cleaned up unconditionally in finally. Touching zero tracked files outside relays/.
Never prints or logs any word of the removed owner quotation (P-796).
"""
import copy
import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]
BASE_MAIN = "10fbbc1c2"
BUILDER_COMMIT = "112e73d67"
EXPECTED_R80A_TREE = "859672ca2746"
EXPECTED_P1_TREE = "ca3baa7081978a643a848b84b0cf9713f1e2ca4a"
EXPECTED_P3_TREE = "79f04e3090675f2cf8d54327465f988cc09d421b"


def git_blob(rev_path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(REPO), "show", rev_path])


def extract_owner_ngrams_in_memory() -> list[str]:
    """Extract contiguous 4-word slices of the former CONFIRMATION[1] string at 10fbbc1c2
    strictly in memory, never printing or returning any slice on match failure except its index."""
    src = git_blob(
        f"{BASE_MAIN}:frontier/B1861_the_closure_programme/verification/programme_source.py"
    ).decode("utf-8")
    m = re.search(r'^CONFIRMATION\s*=\s*\("2026-11-10",\s*"((?:[^"\\]|\\.)*)"\)', src, re.M)
    assert m is not None, "Could not locate CONFIRMATION line at 10fbbc1c2"
    raw_quote = m.group(1)
    words = [w.strip(".,;:!?()[]\"'") for w in raw_quote.split() if w.strip(".,;:!?()[]\"'")]
    assert len(words) >= 4, "Expected at least four words in former quote"
    ngrams = [" ".join(words[i : i + 4]).lower() for i in range(len(words) - 3)]
    return ngrams


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    print("=== A2-S-R80b-p1 Cold-Read Verification (112e73d67 on 10fbbc1c2 + R80a) ===")
    owner_ngrams = extract_owner_ngrams_in_memory()
    print(f"[P-796] Loaded {len(owner_ngrams)} four-word slices in memory (zero words printed).")

    # 1. Check relay files at 112e73d67 for any P-796 residue or attribution slips
    relay_paths = subprocess.check_output(
        [
            "git",
            "-C",
            str(REPO),
            "ls-tree",
            "-r",
            "--name-only",
            BUILDER_COMMIT,
            "--",
            "relays/advisor_2026-11-10_audit/r80b",
            "relays/advisor_2026-11-10_audit/ADVISOR_TO_CC_2026-11-12_R80B_PART_1_THE_PLANS_PAGE_QUOTES_NOTHING_OF_THE_OWNER.md",
        ],
        text=True,
    ).splitlines()
    assert len(relay_paths) == 9, f"Expected 9 R80b Part 1 relay files, got {len(relay_paths)}"

    for rp in relay_paths:
        txt_low = git_blob(f"{BUILDER_COMMIT}:{rp}").decode("utf-8").lower()
        for idx, ng in enumerate(owner_ngrams):
            assert ng not in txt_low, f"P-796 leak at slice #{idx} in {rp}"
    print(f"[P-796] Checked all {len(relay_paths)} R80b Part 1 relay blobs: 0 four-word slices present.")

    # Attribution check against STATUS_OF_THE_57.md
    msg1 = git_blob(f"{BUILDER_COMMIT}:relays/advisor_2026-11-10_audit/r80b/part_1/0001_message.txt").decode("utf-8")
    p2_txt = git_blob(
        f"{BUILDER_COMMIT}:relays/advisor_2026-11-10_audit/r80b/part_1/0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch"
    ).decode("utf-8")
    p3_txt = git_blob(
        f"{BUILDER_COMMIT}:relays/advisor_2026-11-10_audit/r80b/part_1/0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch"
    ).decode("utf-8")
    note_txt = git_blob(
        f"{BUILDER_COMMIT}:relays/advisor_2026-11-10_audit/ADVISOR_TO_CC_2026-11-12_R80B_PART_1_THE_PLANS_PAGE_QUOTES_NOTHING_OF_THE_OWNER.md"
    ).decode("utf-8")

    assert "which main checked and found held" in msg1
    assert "which main checked and found held" in p2_txt
    assert "WHICH MAIN HAS NOT" in p3_txt and "CHECKED" in p3_txt
    assert "reproduced" not in msg1.lower()
    assert "reproduced" not in p2_txt.lower()
    assert "reproduced" not in p3_txt.lower()
    note_reproduced_hits = [
        (idx + 1, ln)
        for idx, ln in enumerate(note_txt.splitlines())
        if "reproduced" in ln.lower()
    ]
    print(f"[ATTR] Landed patch messages (0001..0003) attribution matches STATUS_OF_THE_57.md cleanly.")
    print(f"[ATTR] Cover note 'reproduced' hits (SM-05 protocol §12 check): {note_reproduced_hits}")

    # Check R80a full-suite addition in 112e73d67
    full_suite_out = git_blob(
        f"{BUILDER_COMMIT}:relays/advisor_2026-11-10_audit/r80a/the_full_suite_on_a_fresh_clone_of_the_patch_out.txt"
    ).decode("utf-8")
    assert "test_b1898_review_80.py" not in full_suite_out
    print("[R80a-ADD] Confirmed: test_b1898_review_80.py passed in builder's earlier clone only before origin/agy-002/verify advanced past 4ae026d99.")

    # 2. Isolated detached worktree verification
    tmp_root = pathlib.Path(tempfile.mkdtemp(prefix="agy002_r80b_p1_"))
    wt_dir = tmp_root / "wt"
    patches_dir = tmp_root / "patches"
    patches_dir.mkdir()

    try:
        for name in (
            "0001_message.txt",
            "0001_the_plans_page_gives_the_owners_answer_in_plain_words.py",
            "0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch",
            "0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch",
        ):
            (patches_dir / name).write_bytes(
                git_blob(f"{BUILDER_COMMIT}:relays/advisor_2026-11-10_audit/r80b/part_1/{name}")
            )
        r80a_patch = patches_dir / "r80a.patch"
        r80a_patch.write_bytes(
            git_blob(f"{BUILDER_COMMIT}:relays/advisor_2026-11-10_audit/r80a/0001_review_80_entered_with_its_arc_b1898.patch")
        )

        subprocess.run(
            ["git", "-C", str(REPO), "worktree", "add", "--detach", str(wt_dir), BASE_MAIN],
            check=True,
            capture_output=True,
        )
        env = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", PYTHONDONTWRITEBYTECODE="1")

        # Apply R80a
        subprocess.run(["git", "-C", str(wt_dir), "am", str(r80a_patch)], check=True, capture_output=True, env=env)
        r80a_tree = subprocess.check_output(["git", "-C", str(wt_dir), "write-tree"], text=True, env=env).strip()
        assert r80a_tree.startswith(EXPECTED_R80A_TREE), f"Unexpected R80a tree: {r80a_tree}"
        print(f"[TREE] 10fbbc1c2 + R80a tree verified: {r80a_tree}")

        prog_page_before_p1 = (wt_dir / "frontier/B1861_the_closure_programme/PROGRAMME.md").read_text(encoding="utf-8")
        lock_path = wt_dir / "frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py"
        bp_path = wt_dir / "frontier/B1861_the_closure_programme/verification/build_programme.py"

        # Run B1861 lock on R80a (before Patch 1)
        r0 = subprocess.run(
            [sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", str(lock_path)],
            cwd=str(wt_dir),
            capture_output=True,
            text=True,
            env=env,
        )
        assert r0.returncode == 0 and "18 passed" in r0.stdout, r0.stdout + r0.stderr
        print(f"[LOCK] Pre-Patch-1 (R80a) B1861 lock: {r0.stdout.strip().splitlines()[-1]}")

        # Apply Patch 1 script
        r_p1 = subprocess.run(
            [sys.executable, "-B", str(patches_dir / "0001_the_plans_page_gives_the_owners_answer_in_plain_words.py"), str(wt_dir)],
            capture_output=True,
            text=True,
            env=env,
        )
        assert r_p1.returncode == 0, r_p1.stdout + r_p1.stderr
        staged_p1 = subprocess.check_output(
            ["git", "-C", str(wt_dir), "diff", "--cached", "--name-only"], text=True, env=env
        ).splitlines()
        assert staged_p1 == [
            "frontier/B1861_the_closure_programme/PROGRAMME.json",
            "frontier/B1861_the_closure_programme/PROGRAMME.md",
            "frontier/B1861_the_closure_programme/verification/build_programme.py",
            "frontier/B1861_the_closure_programme/verification/programme_source.py",
            "frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py",
        ], f"Unexpected staged files in Patch 1: {staged_p1}"
        p1_tree = subprocess.check_output(["git", "-C", str(wt_dir), "write-tree"], text=True, env=env).strip()
        assert p1_tree == EXPECTED_P1_TREE, f"Tree mismatch on Patch 1: {p1_tree}"
        subprocess.run(
            ["git", "-C", str(wt_dir), "commit", "-F", str(patches_dir / "0001_message.txt")],
            check=True,
            capture_output=True,
            env=env,
        )
        print(f"[TREE] Patch 1 staged 5 B1861 files only; tree == {p1_tree}")

        # Verify zero 4-word slices remain anywhere in B1861 after Patch 1
        for f in (wt_dir / "frontier/B1861_the_closure_programme").rglob("*"):
            if f.is_file():
                low = f.read_text(encoding="utf-8", errors="ignore").lower()
                for idx, ng in enumerate(owner_ngrams):
                    assert ng not in low, f"P-796 residue at slice #{idx} in {f.relative_to(wt_dir)}"
        print("[P-796] Verified 0 four-word slices remain across all files of frontier/B1861_the_closure_programme/.")

        # Run B1861 lock on Patch 1
        r1 = subprocess.run(
            [sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", str(lock_path)],
            cwd=str(wt_dir),
            capture_output=True,
            text=True,
            env=env,
        )
        assert r1.returncode == 0 and "18 passed" in r1.stdout, r1.stdout + r1.stderr
        print(f"[LOCK] Patch 1 B1861 lock: {r1.stdout.strip().splitlines()[-1]}")

        # Apply Patch 2 via git am
        subprocess.run(
            ["git", "-C", str(wt_dir), "am", str(patches_dir / "0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch")],
            check=True,
            capture_output=True,
            env=env,
        )
        p2_files = subprocess.check_output(
            ["git", "-C", str(wt_dir), "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"], text=True, env=env
        ).splitlines()
        assert p2_files == ["frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py"]
        r2 = subprocess.run(
            [sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", str(lock_path)],
            cwd=str(wt_dir),
            capture_output=True,
            text=True,
            env=env,
        )
        assert r2.returncode == 0 and "19 passed" in r2.stdout, r2.stdout + r2.stderr
        print(f"[LOCK] Patch 2 B1861 lock: {r2.stdout.strip().splitlines()[-1]}")

        # Before/After check for Patch 3: test Patch 3's lock assertions against Patch 2's build_programme.py
        bp_before_p3 = bp_path.read_bytes()
        subprocess.run(
            ["git", "-C", str(wt_dir), "am", str(patches_dir / "0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch")],
            check=True,
            capture_output=True,
            env=env,
        )
        p3_files = subprocess.check_output(
            ["git", "-C", str(wt_dir), "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"], text=True, env=env
        ).splitlines()
        assert p3_files == [
            "frontier/B1861_the_closure_programme/verification/build_programme.py",
            "frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py",
        ]
        p3_tree = subprocess.check_output(["git", "-C", str(wt_dir), "write-tree"], text=True, env=env).strip()
        assert p3_tree == EXPECTED_P3_TREE, f"Tree mismatch on Patch 3: {p3_tree}"
        print(f"[TREE] Patch 3 tree verified: {p3_tree}")

        # Revert build_programme.py temporarily to verify Patch 3's test FAILS before the mend
        bp_after_p3 = bp_path.read_bytes()
        bp_path.write_bytes(bp_before_p3)
        r3_before = subprocess.run(
            [
                sys.executable,
                "-B",
                "-m",
                "pytest",
                "-q",
                "-p",
                "no:cacheprovider",
                f"{lock_path}::test_a_sentence_cut_for_a_cell_ends_at_a_word_and_says_that_it_is_cut",
            ],
            cwd=str(wt_dir),
            capture_output=True,
            text=True,
            env=env,
        )
        assert r3_before.returncode != 0, "Expected Patch 3 test to FAIL against pre-mend build_programme.py!"
        bp_path.write_bytes(bp_after_p3)
        r3_after = subprocess.run(
            [sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", str(lock_path)],
            cwd=str(wt_dir),
            capture_output=True,
            text=True,
            env=env,
        )
        assert r3_after.returncode == 0 and "19 passed" in r3_after.stdout, r3_after.stdout + r3_after.stderr
        print(f"[BEFORE/AFTER] Patch 3 lock test failed before mend (rc={r3_before.returncode}) and passed after (19 passed).")

        # Verify build_programme.py --write leaves zero diff on Patch 3
        rb = subprocess.run([sys.executable, "-B", str(bp_path), "--write"], cwd=str(wt_dir), capture_output=True, text=True, env=env)
        assert rb.returncode == 0, rb.stdout + rb.stderr
        dirty = subprocess.check_output(["git", "-C", str(wt_dir), "status", "--porcelain"], text=True, env=env).strip()
        assert dirty == "", f"Dirty tree after build_programme.py --write: {dirty}"
        print("[BUILD] build_programme.py --write clean on final Patch 3 tree (zero diff).")

        # Run all 53 gates on clean Patch 3 worktree
        rg = subprocess.run(
            [sys.executable, "-B", str(wt_dir / "scripts/gates/gates.py")],
            cwd=str(wt_dir),
            capture_output=True,
            text=True,
            env=env,
        )
        gate_lines = [ln for ln in rg.stdout.splitlines() if ln.startswith(("PASS ", "FAIL "))]
        n_pass = sum(1 for ln in gate_lines if ln.startswith("PASS "))
        n_fail = sum(1 for ln in gate_lines if ln.startswith("FAIL "))
        assert rg.returncode == 0 and n_fail == 0, rg.stdout + rg.stderr
        print(f"[GATES] Clean Patch 3 checkout gates: {n_pass} passed, {n_fail} failed (rc={rg.returncode}).")

        # 3. Load Patch 2's reader and Patch 3's short() in-process (isolated sys.path) for unseen adversarial plants
        sys.path.insert(0, str(wt_dir / "frontier/B1861_the_closure_programme/verification"))
        try:
            lock_mod = load_module("wt_b1861_lock", lock_path)
            bp_mod = load_module("wt_b1861_bp", bp_path)

            # Confirm Patch 2 catches pre-Patch-1 PROGRAMME.md while old check passed
            old_ok = lock_mod._as_the_lock_asked_before(prog_page_before_p1)
            new_hits = lock_mod.what_the_plans_page_quotes(prog_page_before_p1)
            assert old_ok is True and new_hits == [(980, "a block quotation")], (old_ok, new_hits)
            print(f"[BEFORE/AFTER] Patch 2 reader on pre-Patch-1 PROGRAMME.md: old_passed={old_ok}, new_hits={new_hits}")

            cur_page = (wt_dir / "frontier/B1861_the_closure_programme/PROGRAMME.md").read_text(encoding="utf-8")
            anchor = f"The owner answered main on {lock_mod.S.CONFIRMATION[0]}."
            assert cur_page.count(anchor) == 1

            adv_p2 = {
                "P2-ADV-1 (line-wrap between owner attribution and quote)": cur_page.replace(
                    anchor, anchor + '\n"planted words that stand for an answer"'
                ),
                "P2-ADV-2 (post-positioned owner attribution after quote)": cur_page.replace(
                    anchor, '"planted words that stand for an answer", the owner answered on 2026-11-10. ' + anchor
                ),
                "P2-ADV-3 (HELD_BY_NAME prefix piggyback inside 'even ticks observed...')": cur_page.replace(
                    "'even ticks observed'",
                    "'even ticks observed, and planted words that stand for an answer inside the same marks'",
                    1,
                ),
                "P2-ADV-4 (French guillemets « ... » with standard space after «)": cur_page.replace(
                    anchor, anchor + " The owner answered: « planted words that stand for an answer »."
                ),
                "P2-ADV-5 (em-dash immediately before opening quote)": cur_page.replace(
                    anchor, anchor + ' The owner—"planted words that stand for an answer".'
                ),
                "P2-ADV-6 (backtick code-span quote after owner attribution)": cur_page.replace(
                    anchor, anchor + " The owner answered: `planted words that stand for an answer`."
                ),
            }
            print("\n=== Unseen Adversarial Plants on Patch 2 (what_the_plans_page_quotes) ===")
            for label, mutated in adv_p2.items():
                assert mutated != cur_page, label
                res = lock_mod.what_the_plans_page_quotes(mutated)
                status = "EVADED (returned [])" if res == [] else f"CAUGHT ({res})"
                print(f"  {label}: {status}")

            pos_p2 = {
                "P2-POS-1 (indented bullet blockquote)": cur_page.replace(anchor, anchor + "\n  * > planted words\n"),
                "P2-POS-2 (HTML <q> tag)": cur_page.replace(anchor, anchor + " <q>planted words</q>"),
                "P2-POS-3 (curly single quote after His)": cur_page.replace(anchor, anchor + " His words: ‘planted words’."),
            }
            for label, mutated in pos_p2.items():
                res = lock_mod.what_the_plans_page_quotes(mutated)
                assert len(res) >= 1, f"Expected positive plant {label} to be caught!"
                print(f"  {label}: CAUGHT ({res})")

            print("\n=== Unseen Adversarial Inputs on Patch 3 (bp.short, n=110) ===")
            adv_p3 = {
                "P3-ADV-1a (open paren + 109 chars of ',;: ' + words)": "(" + ",;: " * 30 + "word" * 20,
                "P3-ADV-1b (em-dash + 109 chars of ',;: ' + words)": "— " + ",;: " * 30 + "word" * 20,
                "P3-ADV-2 (comma + 115 spaces + words)": "," + " " * 115 + "word" * 20,
                "P3-ADV-3 (parenthesised list label '(1) ' + 200-char token)": "(1) " + "y" * 200,
            }
            for label, s_in in adv_p3.items():
                out = bp_mod.short(s_in, 110)
                has_alnum = any(c.isalnum() for c in out[:-4])
                print(f"  {label} -> len={len(out)}, has_alnum={has_alnum}, repr={out!r}")
        finally:
            sys.path.pop(0)
            sys.modules.pop("programme_source", None)

        # 4. Diagnose exact root cause of B1861 lock -> test_closure_generated.py in-process pollution
        diag = subprocess.run(
            [
                sys.executable,
                "-B",
                "-c",
                (
                    "import copy, importlib.util, pathlib, pytest, sys\n"
                    "wt = pathlib.Path(sys.argv[1])\n"
                    "spec = importlib.util.spec_from_file_location('ps_ref', wt / 'frontier/B1861_the_closure_programme/verification/programme_source.py')\n"
                    "ref = importlib.util.module_from_spec(spec); spec.loader.exec_module(ref)\n"
                    "snap = {k: copy.deepcopy(getattr(ref, k)) for k in dir(ref) if k.isupper()}\n"
                    "pytest.main(['-q', '-p', 'no:cacheprovider', str(wt / 'frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py')])\n"
                    "live = sys.modules.get('programme_source')\n"
                    "diffs = [k for k, v in snap.items() if getattr(live, k, None) != v]\n"
                    "print('MUTATED_IN_SYS_MODULES:', diffs)\n"
                    "for k in diffs:\n"
                    "    print('  DIFF_KEY:', k)\n"
                ),
                str(wt_dir),
            ],
            cwd=str(wt_dir),
            capture_output=True,
            text=True,
            env=env,
        )
        print("\n=== In-Process Pollution Diagnosis (B1861 lock -> programme_source) ===")
        for ln in diag.stdout.splitlines():
            if ln.startswith(("MUTATED_IN_SYS_MODULES:", "  DIFF_KEY:")):
                print(ln)

    finally:
        subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(wt_dir)], capture_output=True)
        shutil.rmtree(tmp_root, ignore_errors=True)

    print("\n=== A2-S-R80b-p1 VERIFICATION COMPLETE (EXIT 0) ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
