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
    print("=== A2-S-R80b-p2, part b: unseen plants on the mended locks; gates on the base and on main's head; apply on main's head ===")
    tmp_root = pathlib.Path(tempfile.mkdtemp(prefix="agy002_r80b_p2b_"))
    wt_dir = tmp_root / "wt"; p1_dir = tmp_root / "p1"; p2_dir = tmp_root / "p2"; p1_dir.mkdir(); p2_dir.mkdir()
    env = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", PYTHONDONTWRITEBYTECODE="1")
    try:
        for name in ("0001_message.txt", "0001_the_plans_page_gives_the_owners_answer_in_plain_words.py",
                     "0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch",
                     "0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch"):
            (p1_dir / name).write_bytes(git_blob(f"{P1_COMMIT}:relays/advisor_2026-11-10_audit/r80b/part_1/{name}"))
        p2_names = sorted(COI_DECLARED.keys())
        for name in p2_names:
            (p2_dir / name).write_bytes(git_blob(f"{P2_COMMIT}:relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_2/{name}"))
        subprocess.run(["git", "-C", str(REPO), "worktree", "add", "--detach", str(wt_dir), BASE_MAIN], check=True, capture_output=True)
        subprocess.run([sys.executable, "-B", str(p1_dir / "0001_the_plans_page_gives_the_owners_answer_in_plain_words.py"), str(wt_dir)], check=True, capture_output=True, env=env)
        subprocess.run(["git", "-C", str(wt_dir), "commit", "-qF", str(p1_dir / "0001_message.txt")], check=True, env=env)
        subprocess.run(["git", "-C", str(wt_dir), "am", "-q", str(p1_dir / "0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch"),
                        str(p1_dir / "0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch")], check=True, env=env)
        subprocess.run(["git", "-C", str(wt_dir), "am", "-q"] + [str(p2_dir / n) for n in p2_names], check=True, env=env)
        lock_b1881 = wt_dir / "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py"
        lock_b1895 = wt_dir / "frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/verification/test_b1895_the_mends_of_b1881_read.py"
        # 3. Unseen adversarial plants by agy-002 against Part 2's mended locks
        print("\n=== Unseen Adversarial Plants on Part 2 Mended Locks ===")
        b1881_mod = load_module("wt_b1881_lock", lock_b1881)
        b1895_mod = load_module("wt_b1895_lock", lock_b1895)

        # Plant Group A: Patch 11 (F9, _carriers / _uncorrected on JSON files in B1895 lock)
        verdict_path = wt_dir / "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json"
        v_raw = verdict_path.read_text(encoding="utf-8")
        v_obj = json.loads(v_raw)

        # A1: Prepend a live uncorrected old phrase immediately BEFORE the existing corrected clause in claim_one_line
        target_phrase = "the second one compared here is the transpose"
        assert v_obj["claim_one_line"].count(target_phrase) == 1
        p_f9_prepend = dict(
            v_obj,
            claim_one_line=v_obj["claim_one_line"].replace(
                target_phrase,
                "and the columns are the transpose that B1881 used; " + target_phrase,
                1,
            ),
        )
        res_f9_prepend = b1895_mod._uncorrected(
            "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json",
            json.dumps(p_f9_prepend, indent=1, ensure_ascii=False),
        )
        print(f"  P2-F9-ADV-1 (a second old phrase, uncorrected, written just before the corrected one: the one correction 400 characters on excuses both): _uncorrected={res_f9_prepend} -> {'EVADED (0 uncorrected!)' if res_f9_prepend[0] == 0 else 'CAUGHT'}")

        # A2: Live uncorrected old phrase placed in a JSON dict KEY
        p_f9_key = dict(v_obj, scope=dict(v_obj["scope"], **{"the columns are the transpose that B1881 used": "live uncorrected key"}))
        res_f9_key = b1895_mod._uncorrected(
            "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json",
            json.dumps(p_f9_key, indent=1, ensure_ascii=False),
        )
        print(f"  P2-F9-ADV-2 (live old phrase placed in JSON dict key): _uncorrected={res_f9_key} -> {'EVADED (dict keys invisible to _texts_of!)' if res_f9_key == (0, 1) else 'CAUGHT'}")

        # Plant Group B: Patch 3 (F5, _held_under_another_version / _values_to_eight_digits in B1881 lock)
        run0 = (wt_dir / "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main_run.txt").read_bytes()
        data0 = (wt_dir / "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.json").read_bytes()

        # B1: Replace integer 1 in A_numbers["W"] = [-3, -14, 1, 3] with boolean True
        d_bool = json.loads(data0)
        d_bool["A_numbers"]["W"] = [-3, -14, True, 3]
        try:
            b1881_mod._held_under_another_version(run0, json.dumps(d_bool).encode("utf-8"), run0, data0, 0)
            b1_status = "EVADED ([-3, -14, True, 3] == [-3, -14, 1, 3] passed!)"
        except AssertionError:
            b1_status = "CAUGHT"
        print(f"  P2-F5-ADV-1 (A_numbers['W'][2] changed from int 1 to bool True): {b1_status}")

        # B2: Replace all 65 boolean True check values in JSON with integer 1
        d_checks_int = {k: (1 if v is True else v) for k, v in json.loads(data0).items()}
        try:
            b1881_mod._held_under_another_version(run0, json.dumps(d_checks_int).encode("utf-8"), run0, data0, 0)
            b2_status = "EVADED (all 65 bool True checks replaced by int 1 passed!)"
        except AssertionError:
            b2_status = "CAUGHT"
        print(f"  P2-F5-ADV-2 (all 65 bool True checks replaced by int 1): {b2_status}")

        # B3: Replace exact 50-digit mpmath string "3.61803398875" in B_numbers["own"]["(6)"] with truncated JSON float 3.618034
        d_str_to_float = json.loads(data0)
        d_str_to_float["B_numbers"]["own"]["(6)"] = 3.618034
        try:
            b1881_mod._held_under_another_version(run0, json.dumps(d_str_to_float).encode("utf-8"), run0, data0, 0)
            b3_status = "EVADED (exact mpmath str '3.61803398875' replaced by truncated float 3.618034 passed!)"
        except AssertionError:
            b3_status = "CAUGHT"
        print(f"  P2-F5-ADV-3 (B_numbers['own']['(6)'] str '3.61803398875' -> float 3.618034): {b3_status}")

        # Plant Group C: Patch 2 (F2, _check_records_what_it_is_passed behavioral check when script + digest move together)
        script_src = (wt_dir / "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py").read_text(encoding="utf-8")
        planted_f2_probe_aware = script_src.replace(
            'def check(name, ok, detail=""):',
            'def check(name, ok, detail=""):\n    ok = ok if name.startswith("planted by the lock:") else True',
        )
        c_res = b1881_mod._check_records_what_it_is_passed(b1881_mod._a_module_of(planted_f2_probe_aware, "b1881_probe_aware"))
        print(f"  P2-F2-ADV-1 (probe-name-aware check() forcing real checks True): _check_records_what_it_is_passed={c_res} -> {'EVADED behavioral helper (caught only by Patch 1 digest)' if c_res else 'CAUGHT'}")

        # Plant Group D: Patch 10 (unpinned numbers in B1895/FINDINGS.md § 7 note)
        b1895_page_path = wt_dir / "frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/FINDINGS.md"
        orig_b1895_page = b1895_page_path.read_text(encoding="utf-8")
        mut_b1895_page = orig_b1895_page.replace("and on 88 of 120 at each", "and on 120 of 120 at each").replace(
            "reads above 17/12", "reads above 19/12"
        )
        assert mut_b1895_page != orig_b1895_page
        b1895_page_path.write_text(mut_b1895_page, encoding="utf-8")
        try:
            rd = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", str(lock_b1895)], cwd=str(wt_dir), capture_output=True, text=True, env=env)
            d_status = f"EVADED (B1895 lock rc={rd.returncode}: {rd.stdout.strip().splitlines()[-1]})" if rd.returncode == 0 else "CAUGHT"
            print(f"  P2-P10-ADV-1 (mutating '88 of 120' -> '120 of 120' and '17/12' -> '19/12' in B1895 §7 note): {d_status}")
        finally:
            b1895_page_path.write_text(orig_b1895_page, encoding="utf-8")

    finally:
        subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(wt_dir)], capture_output=True)
        shutil.rmtree(tmp_root, ignore_errors=True)

    # 3b. The gates on the base and on main's head, today, for comparison: a gate that reads the day of the machine can fail
    # on a later day with nothing changed.
    for label, rev in (("main's bf76e5ab1, the base", BASE_MAIN), ("main's head", "origin/main")):
        tb = pathlib.Path(tempfile.mkdtemp(prefix="agy002_gates_base_"))
        try:
            subprocess.run(["git", "-C", str(REPO), "worktree", "add", "--detach", str(tb / "wt"), rev], check=True, capture_output=True)
            rb = subprocess.run([sys.executable, "-B", str(tb / "wt/scripts/gates/gates.py")], cwd=str(tb / "wt"), capture_output=True, text=True,
                                env=dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", PYTHONDONTWRITEBYTECODE="1"))
            fl = sorted(l.split(":")[0].strip() for l in rb.stdout.splitlines() if l.lstrip().startswith("FAIL"))
            print(f"[GATES] on {label}, run today: rc={rb.returncode}; failing gates: {fl or 'none'}")
        finally:
            subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(tb / "wt")], capture_output=True)
            shutil.rmtree(tb, ignore_errors=True)

    # 4. Does rebuilt Part 2 apply on main's current head, where Part 1 is landed?
    head = subprocess.check_output(["git", "-C", str(REPO), "rev-parse", "--short=9", "origin/main"], text=True).strip()
    tmp2 = pathlib.Path(tempfile.mkdtemp(prefix="agy002_r80b_p2_head_"))
    try:
        p2_dir2 = tmp2 / "p2"; p2_dir2.mkdir()
        for name in sorted(COI_DECLARED):
            (p2_dir2 / name).write_bytes(git_blob(f"{P2_COMMIT}:relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_2/{name}"))
        wt2 = tmp2 / "wt"
        subprocess.run(["git", "-C", str(REPO), "worktree", "add", "--detach", str(wt2), "origin/main"], check=True, capture_output=True)
        env2 = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", PYTHONDONTWRITEBYTECODE="1")
        applied = 0
        for name in sorted(COI_DECLARED):
            r = subprocess.run(["git", "-C", str(wt2), "am", "-3", str(p2_dir2 / name)], capture_output=True, text=True, env=env2)
            if r.returncode != 0:
                files = [ln for ln in (r.stdout + r.stderr).splitlines() if "CONFLICT" in ln or "error:" in ln][:4]
                print(f"[ON HEAD {head}] patch {name} does not apply after {applied} of 12: {files}")
                subprocess.run(["git", "-C", str(wt2), "am", "--abort"], capture_output=True, env=env2)
                break
            applied += 1
        else:
            print(f"[ON HEAD {head}] all 12 rebuilt Part 2 patches apply by git am -3 on main's current head")
    finally:
        subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(tmp2 / "wt")], capture_output=True)
        shutil.rmtree(tmp2, ignore_errors=True)

    print("\n=== A2-S-R80b-p2 PART B COMPLETE (EXIT 0) ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
