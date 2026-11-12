#!/usr/bin/env python3
"""Independent verification of main's answers and mends (ANSWERS_the_first_43.md at 10fbbc1c2)
for agy-002's 36 Review 80 findings (A1 through A36).

Card: A2-R80c (committed at 7c8aa5f1d strictly before opening ANSWERS_the_first_43.md).
Strictly read-only on the main checkout: all pytest lock mutations run inside an isolated
temporary git worktree at 10fbbc1c2 (and c40446392 for CTL-R80C-BASE-C404), removed in finally.
Conflict-of-interest & firewall: B1895 and B1897 are never opened; W1..W7 are left aside; 0 of 19.
"""
from __future__ import annotations

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
REV_BEFORE = "c40446392"
REV_MENDED = "10fbbc1c2"

GIT_ENV = dict(
    os.environ,
    GIT_CONFIG_GLOBAL="/dev/null",
    PYTHONDONTWRITEBYTECODE="1",
)


def git_show(rev: str, rel: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "show", f"{rev}:{rel}"], text=True, env=GIT_ENV
    )


def run_pytest(wt: pathlib.Path, target_rel: str, extra_args: list[str] | None = None) -> tuple[int, str]:
    cmd = [
        sys.executable,
        "-B",
        "-m",
        "pytest",
        "-q",
        "-p",
        "no:cacheprovider",
        *(extra_args or []),
        str(wt / target_rel),
    ]
    r = subprocess.run(cmd, cwd=str(wt), capture_output=True, text=True, env=GIT_ENV)
    tail = ((r.stdout + "\n" + r.stderr).strip().splitlines() or [""])[-1]
    return r.returncode, tail


def reset_wt(wt: pathlib.Path) -> None:
    subprocess.run(["git", "-C", str(wt), "checkout", "-q", "--", "."], check=True, env=GIT_ENV)
    subprocess.run(["git", "-C", str(wt), "clean", "-q", "-fd"], check=True, env=GIT_ENV)


def verify_prose_and_ledger_mends() -> None:
    print("=== 1. PROSE, COUNT, AND LEDGER MENDS AT 10fbbc1c2 (A1..A4, A7..A8, A10..A14, A16..A23) ===")

    # A1: B1892 section 5 governing-pages cell corrected 2 -> 3 (sum 53 + 43 + 3 = 99),
    # BUT B1892 section 1 line 10 (added in the same commit 5fa8ac1d5) says "the first reader has 52 findings"!
    b92_md = git_show(REV_MENDED, "frontier/B1892_review_79_read_by_those_who_did_not_build_it/FINDINGS.md")
    assert "| the governing pages | 3 [CORRECTED 2026-11-12" in b92_md
    assert "with it the two columns sum to 53 and 43, and with B1889's three to 99" in b92_md
    # Re-sum section 5 first-reader column directly from the table at 10fbbc1c2:
    sec5 = b92_md.split("## 5.")[1].split("## 6.")[0]
    col1_nums = []
    col2_nums = []
    for ln in sec5.splitlines():
        if ln.startswith("| ") and not ln.startswith("| what |") and not ln.startswith("|---"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            m1 = re.match(r"^(\d+)\b", cells[1])
            m2 = re.match(r"^(\d+)\b", cells[2])
            assert m1 and m2, ln
            col1_nums.append(int(m1.group(1)))
            col2_nums.append(int(m2.group(1)))
    assert sum(col1_nums) == 53 and sum(col2_nums) == 43
    assert "In the arcs two readers read, the first reader has 52 findings, the second 43" in b92_md
    print(
        f"  A1: B1892 §5 sum fixed to {sum(col1_nums)}+{sum(col2_nums)}+3=99, "
        "RESIDUAL FOUND: B1892 §1 line 10 (added in 5fa8ac1d5) states stale 'the first reader has 52 findings'!"
    )

    # A2: B1892 "every arc of the window" -> P-830 note in B1892 FINDINGS, arc_verdict, REVIEWS.md, RETRACTIONS.md;
    # check residual in POINT_REGISTER P-805 ("every arc of the window read in full").
    b92_av = json.loads(git_show(REV_MENDED, "frontier/B1892_review_79_read_by_those_who_did_not_build_it/arc_verdict.json"))
    rev_md = git_show(REV_MENDED, "docs/progress/REVIEWS.md")
    pr_md = git_show(REV_MENDED, "docs/POINT_REGISTER.md")
    assert "ten were on no card, and six more changed in other files only" in b92_md
    assert "ten were on no reader's card (register row P-830)" in b92_av["claim_one_line"]
    assert "Ten were\n  on no card" in rev_md
    p805_row = [ln for ln in pr_md.splitlines() if ln.startswith("| P-805 ")][0]
    assert "every arc of the window read in full" in p805_row and "P-830" not in p805_row
    print("  A2: B1892 FINDINGS/arc_verdict + REVIEWS.md + P-830 mended (minor residual: P-805 still says 'every arc of the window read in full' without P-830 note).")

    # A3: B1892 18 -> 20 generated-only commits, none touching a session's page alone.
    assert "Of this window's 49, twenty touched nothing but generated pages [CORRECTED 2026-11-12" in b92_md
    print("  A3: B1892 20 generated-only / 0 session-page-only commits mended with old words kept: CLOSED.")

    # A4: "25 of 44" -> "25 of 43" across B1892 FINDINGS, arc_verdict, POINT_REGISTER #88, and VERDICT_LEDGER.md.
    vl_md = git_show(REV_MENDED, "docs/views/VERDICT_LEDGER.md")
    assert "25 of 43 caught [CORRECTED 2026-11-12" in b92_md
    assert "25 of 43 errors planted against them [CORRECTED 2026-11-12" in b92_av["claim_one_line"]
    assert "88. P-811 — the locks on five of the audit's corrections caught 25 of 43 errors" in pr_md
    assert "25 of 43 errors planted against them" in vl_md
    print("  A4: 25 of 43 carried to all 4 surfaces (B1892 FINDINGS, arc_verdict, POINT_REGISTER #88, VERDICT_LEDGER): CLOSED.")

    # A7 & A8: B1896 46 phrases + 8 readings = 54 rows; and 3 -> 9 / 92 (24 held, 68 unheld).
    b96_md = git_show(REV_MENDED, "frontier/B1896_the_third_enforcement_series_verified_and_landed/FINDINGS.md")
    assert "The sweep read 29 of the registry's 46 phrases [CORRECTED 2026-11-12" in b96_md
    assert "The reader counts nine by its own shape. Main's scan by the syntax tree finds 92 tests" in b96_md
    assert not re.search(r"\b68\b", "\n".join(ln for ln in pr_md.splitlines() if ln.startswith("| P-8")))
    print("  A7: CLOSED. A8: B1896 prose mended; NOTE: 'the 68 registered as a debt' is in STATUS_OF_THE_57.md ('Owed from the first 43'), not yet a P-row in POINT_REGISTER.md.")

    # A9 (register part): P-806 updated to 24 of 32.
    p806_row = [ln for ln in pr_md.splitlines() if ln.startswith("| P-806 ")][0]
    assert "With the third series the gates catch 24 of 32 (B1896)" in p806_row
    print("  A9 (P-806 part): P-806 updated to 24 of 32: CLOSED (lock part checked in Section 2).")

    # A12 (PROGRAMME.md part): B1878 FINDINGS & arc_verdict fixed, check PROGRAMME.md row G9.
    b78_md = git_show(REV_MENDED, "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/FINDINGS.md")
    b78_av = json.loads(git_show(REV_MENDED, "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/arc_verdict.json"))
    prog_md = git_show(REV_MENDED, "frontier/B1861_the_closure_programme/PROGRAMME.md")
    assert "Five, not\n> four." in b78_md
    assert "replaced the same day by B1880, five of them" in b78_av["claim_one_line"]
    g9_row = [ln for ln in prog_md.splitlines() if ln.startswith("| G9 ")][0]
    assert "B1878: the attribution gate reads every commit message on the first-parent line after da25c4f49, the last that carried a vendor's name or a co-author trailer; 695 commits pass" in g9_row
    assert "B1880" not in g9_row
    print("  A12 (prose part): B1878 FINDINGS & arc_verdict mended; RESIDUAL: PROGRAMME.md row G9 col 7 still states unmended 'B1878: ... on the first-parent line ... 695 commits pass' without B1880.")

    # A13: B1880 docstrings mended; check whether test_b1880 locks either docstring mend.
    m_py = git_show(REV_MENDED, "frontier/B1880_the_third_and_fourth_re_audits_answered/verification/measure_all_hash_lists.py")
    r_py = git_show(REV_MENDED, "frontier/B1880_the_third_and_fourth_re_audits_answered/verification/read_class_a.py")
    tb80 = git_show(REV_MENDED, "frontier/B1880_the_third_and_fourth_re_audits_answered/verification/test_b1880_the_third_and_fourth_re_audits_answered.py")
    assert "measure_all_hash_lists_run.txt in this folder" in m_py and "[CORRECTED 2026-11-12" in m_py
    assert "nine files are read, the seven of class A and\nthe two of class B" in r_py
    assert "measure_all_hash_lists" not in tb80 and "nine files are read" not in tb80
    print("  A13: Both B1880 script docstrings corrected; RESIDUAL: test_b1880 still leaves both docstrings unlocked.")

    # A14 (prose/JSON part): Check B1885/arc_verdict.json internal contradiction between scope.hypotheses ("two checks") and claim_one_line ("three checks")!
    b85_av = json.loads(git_show(REV_MENDED, "frontier/B1885_the_golden_state_on_the_whole_verified/arc_verdict.json"))
    assert "18 digits for the grid and the two checks made on it" in b85_av["scope"]["hypotheses"]
    assert "18 for the grid and the three checks made on it, A4, A5 and H5" in b85_av["claim_one_line"]
    plants_j = json.loads(git_show(REV_MENDED, "docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/checks/plants_agy002.json"))
    b85_note_plant = [x for x in plants_j if x["arc"] == "B1885" and "18 digits" in x["plant"]][0]
    assert b85_note_plant["the lock"] == "passes"
    print(
        "  A14 (JSON & check-artifact part): DEFECT FOUND: B1885/arc_verdict.json scope.hypotheses STILL says 'the two checks made on it' "
        "contradicting claim_one_line ('the three checks made on it'), AND plants_agy002.json records 'the lock': 'passes' due to a stale regex no-op in plants_agy002.py!"
    )

    # A16, A17, A18: docs/RETRACTIONS.md mends + P-823 check.
    ret_md = git_show(REV_MENDED, "docs/RETRACTIONS.md")
    assert "elliptic points at which the character forces a zero, at the one level 17, and not of levels" in ret_md
    assert "this cell also named B1894, which changed only the note on the grid's 18 digits" in ret_md
    assert "Review 78 carried the word to three more places, and it stands in five files" in ret_md
    assert "Five reviews landed in this\nwindow, 75 to 79, and not two" in ret_md
    assert "| B997 |" in ret_md and "B1859" in ret_md
    p823_row = [ln for ln in pr_md.splitlines() if ln.startswith("| P-823 ")][0]
    assert "75" not in p823_row and "76" not in p823_row and "77" not in p823_row
    print("  A16 & A17: CLOSED. A18: RETRACTIONS.md note + B997/B1859 row added; RESIDUAL: RETRACTIONS.md cites P-823 for Reviews 75-77 and window arc-by-arc reading, but P-823 in POINT_REGISTER.md was not updated to mention Reviews 75-77 or standalone non-review corrections.")

    # A19..A23: REVIEWS.md and RETRACTED_PHRASES.md mends.
    rp_md = git_show(REV_MENDED, "docs/RETRACTED_PHRASES.md")
    assert "six, of five sessions. By the ledger's\npin rows at both ends of the window three lanes moved" in rev_md
    assert "neither gained a row. The law map has 329 rows and the theorem registry 229" in rev_md
    assert "two rows of the ledger's table were edited in place, and twelve instances were added as a list" in rev_md
    assert "three pages under the papers' folder changed in the window besides the manifest" in rev_md
    assert '"Two rows of the tables above take back a reading" counts too few. Eight rows\ndo.' in rp_md
    print("  A19, A20, A21, A22, A23: ALL FIVE CLOSED cleanly with old words kept.")


def verify_lock_mends_and_surviving_plants() -> None:
    print("\n=== 2. SCRATCH-WORKTREE PYTEST VERIFICATION OF LOCK MENDS AND SURVIVING PLANTS (A5, A6, A9, A10, A12, A14, A15) ===")
    tmp_parent = pathlib.Path(tempfile.mkdtemp(prefix="r80c_wt_"))
    wt_mended = tmp_parent / "wt_10fbbc1c2"
    wt_before = tmp_parent / "wt_c40446392"
    try:
        subprocess.run(
            ["git", "-C", str(REPO), "worktree", "add", "--detach", "-q", str(wt_mended), REV_MENDED],
            check=True,
            env=GIT_ENV,
        )
        subprocess.run(
            ["git", "-C", str(REPO), "worktree", "add", "--detach", "-q", str(wt_before), REV_BEFORE],
            check=True,
            env=GIT_ENV,
        )

        # CTL-R80C-BASE-C404: Verify on c40446392 that mutating B1878 arc_verdict.json to invalid JSON PASSED before the mend,
        # and FAILS on 10fbbc1c2 after the mend!
        b78_lock = "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/verification/test_b1878_the_goal_as_ruled.py"
        (wt_before / "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/arc_verdict.json").write_text("{bad json\n", encoding="utf-8")
        rc_b78_before, _ = run_pytest(wt_before, b78_lock)
        assert rc_b78_before == 0, "Expected pre-mend B1878 lock at c40446392 to pass broken arc_verdict.json"
        reset_wt(wt_before)

        # --- A5 (B1892): Clean check + surviving plants ---
        b92_dir = "frontier/B1892_review_79_read_by_those_who_did_not_build_it"
        b92_lock = f"{b92_dir}/verification/test_b1892_review_79.py"
        rc, tail = run_pytest(wt_mended, b92_lock)
        assert rc == 0, tail
        # Plant 1 on B1892: mutate verdict PROVED -> NEGATIVE, corrupt claim_one_line, wipe ANSWERS.md cols 2..4, empty answers.json sublists:
        av92_p = wt_mended / b92_dir / "arc_verdict.json"
        av92 = json.loads(av92_p.read_text(encoding="utf-8"))
        av92["verdict"] = "NEGATIVE"
        av92["claim_one_line"] = "CORRUPTED VERDICT LINE 0 of 19."
        av92_p.write_text(json.dumps(av92), encoding="utf-8")
        aj_p = wt_mended / b92_dir / "verification/answers.json"
        aj = json.loads(aj_p.read_text(encoding="utf-8"))
        aj["held in all but one detail"] = []
        aj["sent on to the builder of the enforcement package"] = []
        aj["not mended"] = []
        aj_p.write_text(json.dumps(aj), encoding="utf-8")
        ans_p = wt_mended / b92_dir / "ANSWERS.md"
        ans_p.write_text(
            re.sub(
                r"^\| ((?:W|SM-|A|X)\d+) \|.*$",
                r"| \1 | WIPED | WIPED | WIPED |",
                ans_p.read_text(encoding="utf-8"),
                flags=re.M,
            ),
            encoding="utf-8",
        )
        rc_a5_surv, tail_a5 = run_pytest(wt_mended, b92_lock)
        assert rc_a5_surv == 0, f"Expected surviving A5 plant to still pass test_b1892, got {tail_a5}"
        # Also test quote_check.placed() basename fallback bug:
        spec = importlib.util.spec_from_file_location("qc_mended", wt_mended / b92_dir / "verification/quote_check.py")
        qc_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(qc_mod)
        placed_typo = qc_mod.placed(
            "99 findings, and all 99 held.",
            "B1881",
            "frontier/B1881_NONEXISTENT_TYPO/FINDINGS.md",
            (REV_MENDED,),
        )
        assert placed_typo == "named", placed_typo
        reset_wt(wt_mended)
        print(
            f"  A5 (B1892): STILL OPEN IN PART -> clean=PASS; verdict='NEGATIVE'+wiped ANSWERS.md+emptied answers.json sublists STILL PASSES ({tail_a5}); "
            f"and quote_check.placed() on nonexistent 'frontier/B1881_NONEXISTENT_TYPO/FINDINGS.md' matches B1892/FINDINGS.md and returns {placed_typo!r}!"
        )

        # --- A6 (B1893): Clean check + mended plants fail + surviving R06 plant still passes ---
        b93_dir = "frontier/B1893_the_second_enforcement_series_verified_and_landed"
        b93_lock = f"{b93_dir}/verification/test_b1893_the_second_enforcement_series_verified_and_landed.py"
        rc, tail = run_pytest(wt_mended, b93_lock)
        assert rc == 0, tail
        # Mended plant: verdict -> NEGATIVE now FAILS:
        av93_p = wt_mended / b93_dir / "arc_verdict.json"
        av93_orig = json.loads(av93_p.read_text(encoding="utf-8"))
        av93 = dict(av93_orig, verdict="NEGATIVE")
        av93_p.write_text(json.dumps(av93), encoding="utf-8")
        rc_neg, _ = run_pytest(wt_mended, b93_lock)
        assert rc_neg != 0
        reset_wt(wt_mended)
        # Surviving R06 plant: keep prefix of claim_one_line, invert count inside claim_one_line ("ZERO OF MAIN'S UNSEEN CASES ARE CAUGHT"),
        # and delete U11, U12.a, U12.c, U13..U19 from B1893/FINDINGS.md:
        av93_mut = dict(av93_orig)
        av93_mut["claim_one_line"] = av93_orig["claim_one_line"].replace(
            "ALL THIRTEEN OF MAIN'S UNSEEN CASES ARE CAUGHT",
            "ZERO OF MAIN'S UNSEEN CASES ARE CAUGHT",
        )
        assert av93_mut["claim_one_line"] != av93_orig["claim_one_line"]
        av93_p.write_text(json.dumps(av93_mut), encoding="utf-8")
        f93_p = wt_mended / b93_dir / "FINDINGS.md"
        f93_orig = f93_p.read_text(encoding="utf-8")
        f93_mut = "\n".join(
            ln
            for ln in f93_orig.splitlines()
            if not re.match(r"^\|\s*U1[13-9]\.", ln)
            and not ln.startswith("| U12.a ")
            and not ln.startswith("| U12.c ")
        )
        assert f93_mut != f93_orig
        f93_p.write_text(f93_mut, encoding="utf-8")
        rc_a6_surv, tail_a6 = run_pytest(wt_mended, b93_lock)
        assert rc_a6_surv == 0, f"Expected surviving A6 plant to pass test_b1893, got {tail_a6}"
        reset_wt(wt_mended)
        print(
            f"  A6 (B1893): STILL OPEN IN PART -> verdict='NEGATIVE' now FAILS; "
            f"but deleting 10 case rows (U11, U12.a, U12.c, U13..U19) from FINDINGS.md + 'ZERO OF MAIN\\'S UNSEEN CASES ARE CAUGHT' in claim_one_line STILL PASSES ({tail_a6})!"
        )

        # --- A9 (B1896): Clean check + mended plants fail + surviving claim_one_line & AR3/AR4 gate-name plant ---
        b96_dir = "frontier/B1896_the_third_enforcement_series_verified_and_landed"
        b96_lock = f"{b96_dir}/verification/test_b1896_the_third_enforcement_series_verified_and_landed.py"
        fast_k = ["-k", "not what_main_changed_at_the_landing_stands"]
        rc, tail = run_pytest(wt_mended, b96_lock, fast_k)
        assert rc == 0, tail
        # Mended plant: deleting run_unseen_s3.py now FAILS:
        (wt_mended / b96_dir / "verification/run_unseen_s3.py").unlink()
        rc_del, _ = run_pytest(wt_mended, b96_lock, fast_k)
        assert rc_del != 0
        reset_wt(wt_mended)
        # Surviving R09 plant: corrupt counts inside claim_one_line after the pinned prefix, AND swap AR3/AR4 gate names in FINDINGS.md!
        av96_p = wt_mended / b96_dir / "arc_verdict.json"
        av96_orig = json.loads(av96_p.read_text(encoding="utf-8"))
        av96_mut = dict(av96_orig)
        av96_mut["claim_one_line"] = re.sub(
            r"17 OF MAIN'S 22 UNSEEN CASES ARE CAUGHT[^.;]*",
            "0 OF MAIN'S 22 UNSEEN CASES ARE CAUGHT, TWENTY-TWO PASS",
            av96_orig["claim_one_line"],
        )
        assert av96_mut["claim_one_line"] != av96_orig["claim_one_line"]
        av96_p.write_text(json.dumps(av96_mut), encoding="utf-8")
        f96_p = wt_mended / b96_dir / "FINDINGS.md"
        f96_orig = f96_p.read_text(encoding="utf-8")
        f96_mut = re.sub(r"^(\|\s*AR[34]\s*\|[^|]+\|)\s*[^|]+\|", r"\1 attribution |", f96_orig, flags=re.M)
        assert f96_mut != f96_orig
        f96_p.write_text(f96_mut, encoding="utf-8")
        rc_a9_surv, tail_a9 = run_pytest(wt_mended, b96_lock)  # FULL lock run without -k!
        assert rc_a9_surv == 0, f"Expected surviving A9 plant to pass full test_b1896, got {tail_a9}"
        reset_wt(wt_mended)
        print(
            f"  A9 (B1896): STILL OPEN IN PART -> runner deletion & 'Five are not caught' now FAIL; "
            f"but '0 OF MAIN\\'S 22 UNSEEN CASES ARE CAUGHT' in claim_one_line + false AR3/AR4 gate names in FINDINGS.md STILL PASSES full test_b1896 ({tail_a9})!"
        )

        # --- A10 (B1862 third & fourth parts): SKELETON.md unmarked E5 copy passes BOTH test_b1862 AND test_b892_walls_on_the_line,
        #     and B862/arc_verdict.json 'FORCES Z6' -> 'FORCES Z3' still passes test_b1862! ---
        sk_p = wt_mended / "papers/structure_paper/SKELETON.md"
        sk_p.write_text(
            sk_p.read_text(encoding="utf-8")
            + "\n\n## Unmarked Appendix\n\nThe 120-point + golden-section real-line scan excludes any wall.\n",
            encoding="utf-8",
        )
        b862_av_p = wt_mended / "frontier/B862_global_form/arc_verdict.json"
        b862_av_p.write_text(b862_av_p.read_text(encoding="utf-8").replace("FORCES Z6", "FORCES Z3"), encoding="utf-8")
        rc_b892, tail_b892 = run_pytest(wt_mended, "tests/test_b892_walls_on_the_line.py")
        rc_b1862, tail_b1862 = run_pytest(
            wt_mended, "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py"
        )
        assert rc_b892 == 0 and rc_b1862 == 0, (tail_b892, tail_b1862)
        reset_wt(wt_mended)
        print(
            f"  A10 (B1862 parts 3 & 4): STILL OPEN -> unmarked E5 old-form paragraph in SKELETON.md passes BOTH test_b892_walls_on_the_line ({tail_b892}) "
            f"AND test_b1862 ({tail_b1862}), and 'FORCES Z6'->'FORCES Z3' in B862/arc_verdict.json still passes test_b1862 (dropped from ANSWERS & STATUS_OF_THE_57)!"
        )

        # --- A12 (B1878 lock): Clean + both plants fail on 10fbbc1c2 ---
        rc, tail = run_pytest(wt_mended, b78_lock)
        assert rc == 0, tail
        (wt_mended / "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/arc_verdict.json").write_text("{bad json\n", encoding="utf-8")
        rc_b78_after, _ = run_pytest(wt_mended, b78_lock)
        assert rc_b78_after != 0
        reset_wt(wt_mended)
        (wt_mended / "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/FINDINGS.md").write_text(
            "\n".join(
                ln
                for ln in (wt_mended / "frontier/B1878_the_goal_as_ruled_in_the_governing_documents/FINDINGS.md").read_text(encoding="utf-8").splitlines()
                if "CORRECTED 2026-11-12" not in ln
            ),
            encoding="utf-8",
        )
        rc_b78_note, _ = run_pytest(wt_mended, b78_lock)
        assert rc_b78_note != 0
        reset_wt(wt_mended)
        print("  A12 (B1878 lock + CTL-R80C-BASE-C404): broken JSON passed on c40446392 and FAILS on 10fbbc1c2; note removal FAILS on 10fbbc1c2: LOCK CLOSED.")

        # --- A14 (B1885 lock): Clean + real removal of 18-digit note FAILS test_b1885, while mutating scope.hypotheses PASSES ---
        b85_dir = "frontier/B1885_the_golden_state_on_the_whole_verified"
        b85_lock = f"{b85_dir}/verification/test_b1885_the_golden_state_on_the_whole_verified.py"
        rc, tail = run_pytest(wt_mended, b85_lock)
        assert rc == 0, tail
        av85_p = wt_mended / b85_dir / "arc_verdict.json"
        av85_orig = json.loads(av85_p.read_text(encoding="utf-8"))
        av85_real_strip = dict(av85_orig)
        av85_real_strip["claim_one_line"] = av85_orig["claim_one_line"].replace(
            "18 for the grid and the three checks made on it, A4, A5 and H5", "30 for all checks"
        )
        av85_p.write_text(json.dumps(av85_real_strip), encoding="utf-8")
        rc_b85_strip, _ = run_pytest(wt_mended, b85_lock, ["-k", "test_the_verdict_and_the_note_on_the_grids_precision_are_held"])
        assert rc_b85_strip != 0
        reset_wt(wt_mended)
        print("  A14 (B1885 lock): real strip of 18-digit note FAILS test_b1885 (confirming plants_agy002.py's 'passes' was a stale-regex no-op; scope.hypotheses still stale at 'two checks').")

        # --- A15 (B1890 lock): Clean + all 3 plants fail ---
        b90_dir = "frontier/B1890_the_first_enforcement_series_verified_and_landed"
        b90_lock = f"{b90_dir}/verification/test_b1890_the_first_enforcement_series_verified_and_landed.py"
        rc, tail = run_pytest(wt_mended, b90_lock)
        assert rc == 0, tail
        (wt_mended / b90_dir / "arc_verdict.json").write_text("{bad\n", encoding="utf-8")
        rc1, _ = run_pytest(wt_mended, b90_lock)
        assert rc1 != 0
        reset_wt(wt_mended)
        g_p = wt_mended / "scripts/gates/gates.py"
        g_orig = g_p.read_text(encoding="utf-8")
        g_p.write_text(
            re.sub(r"READS_HISTORY = frozenset\(\{.*?\}\)", 'READS_HISTORY = frozenset({"retraction-sweep", "test-vacuity"})', g_orig, count=1, flags=re.S),
            encoding="utf-8",
        )
        rc2, _ = run_pytest(wt_mended, b90_lock)
        assert rc2 != 0
        g_p.write_text(
            g_orig.replace('            if state == "empty":\n                return False, REFUSED_EMPTY', '            if state == "never":\n                return False, REFUSED_EMPTY'),
            encoding="utf-8",
        )
        rc3, _ = run_pytest(wt_mended, b90_lock)
        assert rc3 != 0
        reset_wt(wt_mended)
        print("  A15 (B1890 lock): all 3 lock plants (invalid arc_verdict.json, shrunk READS_HISTORY, disabled empty refusal) now FAIL test_b1890: LOCK CLOSED.")
    finally:
        for wt in (wt_mended, wt_before):
            subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(wt)], env=GIT_ENV, capture_output=True)
        shutil.rmtree(tmp_parent, ignore_errors=True)


def verify_builder_handoff_coverage() -> None:
    print("\n=== 3. HANDOFF COVERAGE CHECK FOR A24..A36 (ROWS 41..53 IN builder_rows_probe*.py/.json) ===")
    probe1_py = git_show(REV_MENDED, "docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/checks/builder_rows_probe.py")
    probe2_j = json.loads(git_show(REV_MENDED, "docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/checks/builder_rows_probe2.json"))
    probed_46_53: dict[int, list[str]] = {}
    for entry in probe2_j:
        probed_46_53.setdefault(entry["row"], []).append(entry["case"])
    assert "NUL" not in probe1_py and "symlink" not in probe1_py  # A28 (row 45) sub-case (c) unprobed
    assert len(probed_46_53[46]) == 1  # A29 (row 46): only (a) probed; (b) and (c) unprobed
    assert all("(b)" not in c for c in probed_46_53[47])  # A30 (row 47): (b) STANDS_AS_FOUND count ceiling unprobed
    assert len(probed_46_53[48]) == 2  # A31 (row 48): (b) RAISED_BY_NAME unbounded further increase unprobed
    assert len(probed_46_53[49]) == 2  # A32 (row 49): (b,c) discontinuous intervals & raise deletion unprobed
    assert len(probed_46_53[51]) == 1  # A34 (row 51): 3-commit git history both directions not run
    assert len(probed_46_53[52]) == 1  # A35 (row 52): (b) gate_chain_locks [AXIOM] downgrade & lowercase [theorem] crash unprobed
    assert len(probed_46_53[53]) == 2  # A36 (row 53): (c) mutable staging index git rm --cached unprobed
    print(
        "  A24..A36: all 13 rows open with the builder by design; 8 of the 13 rows (A28, A29, A30, A31, A32, A34, A35, A36) "
        "have sub-cases in REVIEW_80_AGY-002.md absent from main's builder_rows_probe scripts — itemized so builder patches must close full rows, not just main's single-case probes."
    )


def main() -> int:
    verify_prose_and_ledger_mends()
    verify_lock_mends_and_surviving_plants()
    verify_builder_handoff_coverage()
    print("\nALL A2-R80c (M15 ANSWERS_the_first_43.md) CHECKS AND CONTROLS COMPLETED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
