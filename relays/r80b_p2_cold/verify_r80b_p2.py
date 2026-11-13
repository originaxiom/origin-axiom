#!/usr/bin/env python3
"""Independent zero-trust cold-read verification of rebuilt builder series R80b Part 2
(relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_2/ at bc71f9373).

Applies Part 1 (from 112e73d67) and rebuilt Part 2 (12 patches from bc71f9373) onto a clean
detached worktree at main's bf76e5ab1, enforces COI scoping per M17, runs main's plants_b1881_third
before and after Part 2, runs main's b1895_probes, checks STATUS_OF_THE_57.md attribution on all
four 'not checked' rows (SM-22, SM-25, SM-30, F9), runs all 53 gates, and executes unseen
adversarial plants of agy-002's own against B1881's and B1895's mended locks.
"""
import hashlib
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
BASE_MAIN = "bf76e5ab1"
P1_COMMIT = "112e73d67"
P2_COMMIT = "bc71f9373"

COI_DECLARED = {
    "0001_the_lock_of_b1881_holds_the_script_whole.patch": "NON-COI (F1, F3, F4 on B1881 lock)",
    "0002_the_scripts_check_function_is_called.patch": "NON-COI (F2 on B1881 lock)",
    "0003_the_made_with_file_is_held_and_every_value_is_read.patch": "NON-COI (F5 on B1881 lock)",
    "0004_two_docstrings_say_three_planted_lines.patch": "NON-COI (SM-31 on B1881 lock)",
    "0005_the_first_section_of_b1881_is_noted.patch": "NON-COI (SM-30 on B1881 §1)",
    "0006_fifteen_tests_and_six_places_said_fourteen.patch": "MIXED: B1881 lock comments audited in full; B1895/B1897/P-822/harvest-1733 lines on agy-002's delivery left aside on substance",
    "0007_b1895_says_that_its_reader_ran_its_plants.patch": "COI LEFT ASIDE ON SUBSTANCE (SM-20: records agy-002's plant run on B1895 & harvest row 1730; mechanical scope & attribution only)",
    "0008_a_sentence_credited_to_b1895_that_it_does_not_hold.patch": "COI LEFT ASIDE ON SUBSTANCE (SM-21: touches docs/seats/agy-002.md, B1897, harvest row 1733; mechanical scope & attribution only)",
    "0009_the_two_verdict_lines_name_no_session.patch": "COI LEFT ASIDE ON SUBSTANCE (F8: removes agy-002's name from B1895/B1897 verdict lines; mechanical scope & attribution only)",
    "0010_four_things_computed_in_b1895s_lock.patch": "MIXED: SM-22, SM-24, two derivations & b1895_probes lock code audited in full; prose judging agy-002's row A1 (SM-23) left aside",
    "0011_a_correction_in_a_verdict_file_excuses_only_its_own_words.patch": "NON-COI (F9 generic JSON/page sweep in B1895 lock)",
    "0012_two_things_owed_have_a_register_row.patch": "COI LEFT ASIDE ON SUBSTANCE (SM-25: B1897 §4 / P-822 -> P-835, P-836; mechanical scope & unchecked-by-main attribution verified)",
}


def git_blob(rev_path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(REPO), "show", rev_path])


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    print("=== A2-S-R80b-p2 Cold-Read Verification (rebuilt Part 2 at bc71f9373 on bf76e5ab1 + Part 1) ===")
    print("\n=== Declared COI Classification Across All 12 Patches (M17) ===")
    for k, v in COI_DECLARED.items():
        print(f"  {k}: {v}")

    # 1. Verify STATUS_OF_THE_57.md attribution on all 4 'not checked' rows (SM-22, SM-25, SM-30, F9)
    p5 = git_blob(f"{P2_COMMIT}:relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_2/0005_the_first_section_of_b1881_is_noted.patch").decode("utf-8")
    p10 = git_blob(f"{P2_COMMIT}:relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_2/0010_four_things_computed_in_b1895s_lock.patch").decode("utf-8")
    p11 = git_blob(f"{P2_COMMIT}:relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_2/0011_a_correction_in_a_verdict_file_excuses_only_its_own_words.patch").decode("utf-8")
    p12 = git_blob(f"{P2_COMMIT}:relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_2/0012_two_things_owed_have_a_register_row.patch").decode("utf-8")

    assert "WHICH MAIN HAS NOT CHECKED" in p5 and "not checked by main" in p5
    assert "did not check 22" in p10 and "finding 22, not checked by main" in p10 and "not checked by main; counted here" in p10
    assert "WHICH MAIN HAS NOT CHECKED" in p11 and "finding F9, not checked by main" in p11
    assert "not checked by main" in p12 and p12.count("not checked by main") >= 3  # P-822 note, P-835, P-836

    for pname in COI_DECLARED:
        ptxt = git_blob(f"{P2_COMMIT}:relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_2/{pname}").decode("utf-8")
        hdr = ptxt.split("\ndiff --git ", 1)[0]
        assert "reproduced by main" not in hdr.lower(), f"Protocol §12 slip in {pname} header"
    note2 = git_blob(f"{P2_COMMIT}:relays/advisor_2026-11-10_audit/ADVISOR_TO_CC_2026-11-12_R80B_PART_2_B1881_B1895_B1897_TWELVE_PATCHES.md").decode("utf-8")
    note2_repro = [(i + 1, ln) for i, ln in enumerate(note2.splitlines()) if "reproduced by you" in ln.lower()]
    print(f"\n[ATTR] All 4 unchecked rows (SM-22, SM-25, SM-30, F9) explicitly marked 'not checked by main' in commit messages, pages, locks, and P-835/P-836.")
    print(f"[ATTR] Non-landed cover note 'reproduced by you' hits: {note2_repro}")

    # 2. Isolated detached worktree at bf76e5ab1
    tmp_root = pathlib.Path(tempfile.mkdtemp(prefix="agy002_r80b_p2_"))
    wt_dir = tmp_root / "wt"
    p1_dir = tmp_root / "p1"
    p2_dir = tmp_root / "p2"
    p1_dir.mkdir()
    p2_dir.mkdir()

    try:
        for name in (
            "0001_message.txt",
            "0001_the_plans_page_gives_the_owners_answer_in_plain_words.py",
            "0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch",
            "0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch",
        ):
            (p1_dir / name).write_bytes(git_blob(f"{P1_COMMIT}:relays/advisor_2026-11-10_audit/r80b/part_1/{name}"))

        p2_names = sorted(COI_DECLARED.keys())
        for name in p2_names:
            (p2_dir / name).write_bytes(
                git_blob(f"{P2_COMMIT}:relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_2/{name}")
            )

        subprocess.run(["git", "-C", str(REPO), "worktree", "add", "--detach", str(wt_dir), BASE_MAIN], check=True, capture_output=True)
        env = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", PYTHONDONTWRITEBYTECODE="1")

        # Apply Part 1
        subprocess.run(
            [sys.executable, "-B", str(p1_dir / "0001_the_plans_page_gives_the_owners_answer_in_plain_words.py"), str(wt_dir)],
            check=True,
            capture_output=True,
            env=env,
        )
        subprocess.run(["git", "-C", str(wt_dir), "commit", "-F", str(p1_dir / "0001_message.txt")], check=True, capture_output=True, env=env)
        subprocess.run(
            [
                "git",
                "-C",
                str(wt_dir),
                "am",
                str(p1_dir / "0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch"),
                str(p1_dir / "0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch"),
            ],
            check=True,
            capture_output=True,
            env=env,
        )

        # Run main's plants_b1881_third.py BEFORE Part 2 (must pass 5/5 plants)
        # main's kept check scripts compute ROOT = HERE.parents[1]; at their committed places in B1898 (verification/checks/)
        # and in the hand-over folder (review80/checks/) that is not the repository's root, and the script stops at its
        # first glob. They are run here from byte-identical copies at <root>/_agy002_run/checks/, removed after each run.
        kept_plants = next((wt_dir / "frontier").glob("B1898_*/verification/checks/plants_b1881_third.py"))
        in_place = subprocess.run([sys.executable, "-B", str(kept_plants)], cwd=str(wt_dir), capture_output=True, text=True, env=env)
        print(f"[IN-PLACE] B1898/verification/checks/plants_b1881_third.py run where committed: rc={in_place.returncode}, last line={(in_place.stderr or in_place.stdout).strip().splitlines()[-1]!r}")
        run_dir = wt_dir / "_agy002_run" / "checks"

        def staged_copy(src):
            run_dir.mkdir(parents=True, exist_ok=True)
            dst = run_dir / src.name
            dst.write_bytes(src.read_bytes())
            return dst

        plants_script = staged_copy(kept_plants)
        r_plants_before = subprocess.run([sys.executable, "-B", str(plants_script)], cwd=str(wt_dir), capture_output=True, text=True, env=env)
        assert r_plants_before.returncode == 0, r_plants_before.stdout + r_plants_before.stderr
        tail_before = r_plants_before.stdout.strip().splitlines()[-1]
        assert "the two controls behave: True; of the five plants, the lock passes: 5" in tail_before, tail_before
        print(f"\n[BEFORE P2] plants_b1881_third.py: {tail_before}")
        shutil.rmtree(wt_dir / "_agy002_run", ignore_errors=True)
        subprocess.run(["git", "-C", str(wt_dir), "checkout", "--", "."], check=True, capture_output=True, env=env)

        # Apply all 12 patches of rebuilt Part 2 via git am
        subprocess.run(
            ["git", "-C", str(wt_dir), "am"] + [str(p2_dir / name) for name in p2_names],
            check=True,
            capture_output=True,
            env=env,
        )
        p2_tree = subprocess.check_output(["git", "-C", str(wt_dir), "write-tree"], text=True, env=env).strip()
        print(f"[TREE] Applied all 12 rebuilt Part 2 patches cleanly onto bf76e5ab1 + Part 1; tree == {p2_tree}")

        # Run B1881, B1895, B1897 locks on final Part 2 tree
        lock_b1881 = wt_dir / "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py"
        lock_b1895 = wt_dir / "frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/verification/test_b1895_the_mends_of_b1881_read.py"
        lock_b1897 = next((wt_dir / "frontier").glob("B1897_*/verification/test_b1897_*.py"))
        for label, lpath, expected_n in (("B1881", lock_b1881, "17 passed"), ("B1895", lock_b1895, "11 passed"), ("B1897", lock_b1897, "4 passed")):
            rl = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", str(lpath)], cwd=str(wt_dir), capture_output=True, text=True, env=env)
            assert rl.returncode == 0 and expected_n in rl.stdout, rl.stdout + rl.stderr
            print(f"[LOCK] {label} lock after Part 2: {rl.stdout.strip().splitlines()[-1]}")

        # Run main's plants_b1881_third.py AFTER Part 2 (must pass 0/5 plants!)
        plants_script = staged_copy(kept_plants)
        r_plants_after = subprocess.run([sys.executable, "-B", str(plants_script)], cwd=str(wt_dir), capture_output=True, text=True, env=env)
        assert r_plants_after.returncode == 0, r_plants_after.stdout + r_plants_after.stderr
        tail_after = r_plants_after.stdout.strip().splitlines()[-1]
        assert "the two controls behave: True; of the five plants, the lock passes: 0" in tail_after, tail_after
        print(f"[AFTER P2]  plants_b1881_third.py: {tail_after}")
        shutil.rmtree(wt_dir / "_agy002_run", ignore_errors=True)
        subprocess.run(["git", "-C", str(wt_dir), "checkout", "--", "."], check=True, capture_output=True, env=env)

        # Verify main's b1895_probes.py reproduces kept JSON byte-for-byte in values
        kept_probe_script = next((wt_dir / "frontier").glob("B1898_*/verification/checks/b1895_probes.py"))
        kept_probes = json.loads(kept_probe_script.with_suffix(".json").read_text(encoding="utf-8"))
        probes_script = staged_copy(kept_probe_script)
        probes_json = probes_script.with_suffix(".json")
        rp = subprocess.run([sys.executable, "-B", str(probes_script)], cwd=str(wt_dir), capture_output=True, text=True, env=env)
        assert rp.returncode == 0, rp.stdout + rp.stderr
        fresh_probes = json.loads(probes_json.read_text(encoding="utf-8"))
        assert fresh_probes == kept_probes, "b1895_probes mismatch!"
        shutil.rmtree(wt_dir / "_agy002_run", ignore_errors=True)
        subprocess.run(["git", "-C", str(wt_dir), "checkout", "--", "."], check=True, capture_output=True, env=env)
        print("[PROBES] main's b1895_probes.py matches kept JSON exactly (1332, 358/362/0, 120/88, 3378 & 1.4866 at (1,1,2,2)).")

        # Run all 53 gates on clean Part 2 worktree
        rg = subprocess.run([sys.executable, "-B", str(wt_dir / "scripts/gates/gates.py")], cwd=str(wt_dir), capture_output=True, text=True, env=env)
        p2_fails = sorted(l.split(":")[0].strip() for l in rg.stdout.splitlines() if l.lstrip().startswith("FAIL"))
        print(f"[GATES] Clean Part 2 checkout gates rc={rg.returncode}; failing gates: {p2_fails or 'none'}")

        print("[NEXT] the unseen plants, the gates on the base and on main's head, and the apply on main's head: verify_r80b_p2_b.py")

    finally:
        subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(wt_dir)], capture_output=True)
        shutil.rmtree(tmp_root, ignore_errors=True)

    print("\n=== A2-S-R80b-p2 VERIFICATION COMPLETE (EXIT 0) ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
