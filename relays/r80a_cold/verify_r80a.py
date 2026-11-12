#!/usr/bin/env python3
"""Independent cold-read verification of builder series R80a
(0001_review_80_entered_with_its_arc_b1898.patch at 84b860d64 / 112e73d67 on 10fbbc1c2).

Card: A2-S-R80a (committed at 03a2b0d05 strictly before opening any file in r80a/).
Conflict-of-interest & firewall (M16):
  - Leaves agy-002's own 36 rows (A1..A36) and the entry's sentences about agy-002's file aside.
  - Never opens B1895 or B1897.
  - Strictly read-only on the main checkout: applies the patch in a temporary detached worktree
    at 10fbbc1c2 and removes it in finally.
  - 0 of 19.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]
BASE_REV = "10fbbc1c2"
ANCHOR_BEFORE = "0dda7b472"
READ_REV = "c40446392"
BUILDER_REV = "112e73d67"
PATCH_REL = "relays/advisor_2026-11-10_audit/r80a/0001_review_80_entered_with_its_arc_b1898.patch"

GIT_ENV = dict(
    os.environ,
    GIT_CONFIG_GLOBAL="/dev/null",
    PYTHONDONTWRITEBYTECODE="1",
)


def git_out(*args: str, cwd: pathlib.Path = REPO) -> str:
    return subprocess.check_output(["git", "-C", str(cwd), *args], text=True, env=GIT_ENV)


def run_pytest(wt: pathlib.Path, target_rel: str, extra_args: list[str] | None = None) -> tuple[int, str, str]:
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
    out = (r.stdout + "\n" + r.stderr).strip()
    tail = (out.splitlines() or [""])[-1]
    return r.returncode, tail, out


def reset_wt(wt: pathlib.Path) -> None:
    subprocess.run(["git", "-C", str(wt), "checkout", "-q", "--", "."], check=True, env=GIT_ENV)
    subprocess.run(["git", "-C", str(wt), "clean", "-q", "-fd"], check=True, env=GIT_ENV)


def verify_independent_git_recounts() -> dict[str, object]:
    print("=== 1. INDEPENDENT GIT RECOUNTS OVER 0dda7b472..c40446392 (AND 10fbbc1c2) ===")
    w = f"{ANCHOR_BEFORE}..{READ_REV}"
    commits_all = int(git_out("rev-list", "--count", w).strip())
    commits_fp = int(git_out("rev-list", "--count", "--first-parent", w).strip())
    commits_after = int(git_out("rev-list", "--count", "--first-parent", f"{READ_REV}..{BASE_REV}").strip())
    added = [p for p in git_out("diff", "--name-only", "--diff-filter=A", ANCHOR_BEFORE, READ_REV).splitlines() if p]
    added_arcs = sorted(
        {m.group(1) for p in added for m in [re.match(r"frontier/(B\d+)_[^/]*/arc_verdict\.json$", p)] if m},
        key=lambda b: int(b[1:]),
    )
    changed_files = [p for p in git_out("diff", "--name-only", ANCHOR_BEFORE, READ_REV).splitlines() if p]
    f_changed = [p for p in changed_files if p.startswith("frontier/B")]
    older_arcs = sorted({p.split("/")[1] for p in f_changed if p.split("/")[1].split("_")[0] not in added_arcs})
    older_verdict_arcs = sorted(
        {p.split("/")[1] for p in f_changed if p.endswith("/arc_verdict.json") and p.split("/")[1].split("_")[0] not in added_arcs}
    )
    papers_changed = sorted(p for p in git_out("diff", "--name-only", ANCHOR_BEFORE, READ_REV, "--", "papers").splitlines() if p)
    genesis_numstat = [int(x) for x in git_out("diff", "--numstat", ANCHOR_BEFORE, READ_REV, "--", "GENESIS.md").split()[:2]]
    error_numstat = git_out("diff", "--numstat", ANCHOR_BEFORE, READ_REV, "--", "docs/ERROR_LEDGER.md").strip()
    term_numstat = git_out("diff", "--numstat", ANCHOR_BEFORE, READ_REV, "--", "TERMINOLOGY.md").strip()
    seal_numstat = [int(x) for x in git_out("diff", "--numstat", ANCHOR_BEFORE, READ_REV, "--", "docs/SEAL_LEDGER.md").split()[:2]]

    def ledger_counts(rel: str) -> tuple[list[int], list[int], list[int]]:
        non_rules, data_only = [], []
        for rev in (ANCHOR_BEFORE, READ_REV):
            txt = git_out("show", f"{rev}:{rel}")
            bars = [ln for ln in txt.splitlines() if ln.startswith("|")]
            rules = [ln for ln in bars if re.match(r"^\|\s*:?-{2,}", ln)]
            non_rules.append(len(bars) - len(rules))
            data_only.append(len(bars) - 2 * len(rules))
        ns = [int(x) for x in git_out("diff", "--numstat", ANCHOR_BEFORE, READ_REV, "--", rel).split()[:2]]
        return non_rules, data_only, ns

    lm_nr, lm_data, lm_ns = ledger_counts("docs/LAW_MAP.md")
    tr_nr, tr_data, tr_ns = ledger_counts("docs/THEOREM_REGISTRY.md")

    # Harvest pin rows at both ends:
    def hl_pins(rev: str) -> dict[str, str]:
        hl = git_out("show", f"{rev}:docs/HARVEST_LEDGER.md")
        sec = hl[hl.index("## Pins") : hl.index("## The rows")]
        rows = re.findall(r"^\| ([\w-]+) \| .*? \| `([0-9a-f]{7,40})` \|", sec, re.M)
        assert len(rows) == len({k for k, _ in rows}) == 29
        return dict(rows)

    pa, pb = hl_pins(ANCHOR_BEFORE), hl_pins(READ_REV)
    moved_lanes = sorted(k for k in pa if k in pb and pa[k] != pb[k])
    new_lanes = sorted(set(pb) - set(pa))

    assert commits_all == 26 and commits_fp == 26 and commits_after == 12
    assert added_arcs == ["B1891", "B1892", "B1893", "B1894", "B1895", "B1896", "B1897"]
    assert len(older_arcs) == 26 and len(older_verdict_arcs) == 15 and len(changed_files) == 206
    assert lm_nr == [329, 329] and lm_data == [324, 324] and lm_ns == [21, 2]
    assert tr_nr == [229, 229] and tr_data == [222, 222] and tr_ns == [1, 1]
    assert error_numstat == "" and term_numstat == "" and genesis_numstat == [6, 4] and seal_numstat == [11, 0]
    assert len(papers_changed) == 3
    assert moved_lanes == ["advisor", "agy002", "agyloop", "audit", "chat1", "sm"] and new_lanes == []
    print(
        f"  Git recounts verified: commits={commits_all} (fp={commits_fp}), post-anchor={commits_after}, "
        f"added_arcs={len(added_arcs)}, older_arcs={len(older_arcs)} (verdict={len(older_verdict_arcs)}), "
        f"files={len(changed_files)}, LAW_MAP={lm_nr} (data={lm_data}, +{lm_ns[0]}/-{lm_ns[1]}), "
        f"THEOREM_REGISTRY={tr_nr} (data={tr_data}, +{tr_ns[0]}/-{tr_ns[1]}), moved_lanes={moved_lanes}, new_lanes={new_lanes}."
    )
    return {"moved_lanes": moved_lanes}


def verify_patch_tables_entry_and_lock() -> None:
    print("\n=== 2. PATCH APPLICATION, TABLE/ENTRY FIDELITY, AND B1898 LOCK CHECKS IN ISOLATED WORKTREE ===")
    patch_bytes = subprocess.check_output(["git", "-C", str(REPO), "show", f"{BUILDER_REV}:{PATCH_REL}"], env=GIT_ENV)
    td = pathlib.Path(tempfile.mkdtemp(prefix="r80a_cold_"))
    wt = td / "wt"
    pfile = td / "0001.patch"
    pfile.write_bytes(patch_bytes)
    try:
        subprocess.run(["git", "-C", str(REPO), "worktree", "add", "--detach", "-q", str(wt), BASE_REV], check=True, env=GIT_ENV)
        am = subprocess.run(
            ["git", "-C", str(wt), "-c", "user.name=originaxiom", "-c", "user.email=originaxiom@users.noreply.github.com", "am", str(pfile)],
            capture_output=True,
            text=True,
            env=GIT_ENV,
        )
        assert am.returncode == 0, am.stderr
        tree_hash = git_out("rev-parse", "--short=12", "HEAD^{tree}", cwd=wt).strip()
        assert tree_hash == "859672ca2746", tree_hash
        changed_54 = [p for p in git_out("diff", "--name-only", f"{BASE_REV}..HEAD", cwd=wt).splitlines() if p]
        assert len(changed_54) == 54
        # Scope check: mends nothing outside Review 80 entry, B1898, landing/register/harvest/nav pages, point_debt FLOOR=834, and 8 generated files.
        non_b1898 = [p for p in changed_54 if not p.startswith("frontier/B1898_")]
        expected_non_b1898 = {
            "CHANGELOG.md",
            "PROGRESS_LOG.md",
            "README.md",
            "docs/CAMPAIGN_STATUS.md",
            "docs/HARVEST_LEDGER.md",
            "docs/LEAD_REGISTER.md",
            "docs/MASTERPLAN.md",
            "docs/OPEN_LEADS.md",
            "docs/OPEN_PROBLEMS.md",
            "docs/POINT_REGISTER.md",
            "docs/PRICED_DOORS.md",
            "docs/progress/REVIEWS.md",
            "docs/views/CONTEXT_RECOVERY.md",
            "docs/views/COVERAGE.md",
            "docs/views/REVIEWER.md",
            "docs/views/VERDICT_LEDGER.md",
            "frontier/B1883_where_we_stand/WHERE_WE_STAND.json",
            "frontier/B1883_where_we_stand/WHERE_WE_STAND.md",
            "scripts/atlas/atlas_data.json",
            "scripts/checks/point_debt.py",
        }
        assert set(non_b1898) == expected_non_b1898
        print(f"  Scope & tree verified: tree={tree_hash}, 54 files changed, zero unintended mends outside R80a scope.")

        b98_rel = "frontier/B1898_review_80_one_hundred_findings_and_what_main_checked"
        b98 = wt / b98_rel
        lock_rel = f"{b98_rel}/verification/test_b1898_review_80.py"

        # Check byte-for-byte identity of main's 2 tables and 24 check files (leaving agy-002's own 36 rows unjudged):
        handoff = wt / "docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80"
        assert (b98 / "ANSWERS_the_first_43.md").read_bytes() == (handoff / "ANSWERS_the_first_43.md").read_bytes()
        assert (b98 / "STATUS_OF_THE_57.md").read_bytes() == (handoff / "STATUS_OF_THE_57.md").read_bytes()
        check_files = sorted(p.name for p in (b98 / "verification/checks").iterdir())
        assert len(check_files) == 24
        for cf in check_files:
            assert (b98 / "verification/checks" / cf).read_bytes() == (handoff / "checks" / cf).read_bytes(), cf

        # Verify STATUS_OF_THE_57.md fidelity (nothing unchecked or partial in STATUS_OF_THE_57 is written as checked in full by main):
        s57 = (b98 / "STATUS_OF_THE_57.md").read_text(encoding="utf-8")
        s57_rows = []
        for ln in s57.splitlines():
            m57 = re.match(r"^\| (\d\d|F\d+|W\d+) \|(.*)\|\s*$", ln)
            if m57:
                cells = [c.strip() for c in m57.group(2).split("|")]
                assert len(cells) == 4, ln
                s57_rows.append((m57.group(1), cells[0], cells[1], cells[2], cells[3]))
        assert len(s57_rows) == 57
        unchecked_ids = [r[0] for r in s57_rows if r[3].lower() == "not checked"]
        partial_ids = [r[0] for r in s57_rows if "not checked" in r[3].lower() and r[0] not in unchecked_ids]
        full_ids = [r[0] for r in s57_rows if r[0] not in unchecked_ids and r[0] not in partial_ids]
        assert unchecked_ids == ["22", "25", "26", "30", "32", "33", "37", "38", "39", "40", "41", "F9", "F11", "F13", "F14", "W8", "W9"]
        assert partial_ids == ["F6", "F7", "F10"]
        assert len(unchecked_ids) == 17 and len(partial_ids) == 3 and len(full_ids) == 37
        print("  STATUS_OF_THE_57 fidelity verified: 37 checked in full, 3 in part (F6,F7,F10), 17 not checked — none misattributed to main.")

        # --- DEFECT R80a-1: Clean pytest on test_b1898_review_80.py FAILS LIVE when origin/agy-002/verify has moved past 4ae026d99! ---
        rc_full_clean, tail_full_clean, out_full_clean = run_pytest(wt, lock_rel)
        assert rc_full_clean != 0, "Expected full test_b1898_review_80.py to fail due to moving origin/agy-002/verify ref!"
        assert "quote_check_agy002: made again, the counts are not the ones main kept" in out_full_clean
        print(f"  DEFECT R80a-1 CONFIRMED LIVE: clean pytest on test_b1898_review_80.py FAILS ({tail_full_clean}) because quote_check_agy002 reads moving ref origin/agy-002/verify (49 rows) instead of fixed commit 4ae026d99 (36 rows)!")

        # --- DEFECT R80a-2: B1898/FINDINGS.md §1 line 11 omits 'but the addition's two', contradicting arc_verdict.json, REVIEWS.md, §4, and Disclosed ---
        f98_txt = (b98 / "FINDINGS.md").read_text(encoding="utf-8")
        av98 = json.loads((b98 / "arc_verdict.json").read_text(encoding="utf-8"))
        assert "- **100 findings,** in four readers' files and one dated addition. Every quotation was found by machine at the commit\n  read." in f98_txt
        assert "every quotation but the addition's two found by machine at the commit read" in av98["claim_one_line"]
        assert "| the web seat, a dated addition | the same file @ `f8bf9d76c` | 2 | not looked for by a check in this arc |" in f98_txt
        print("  DEFECT R80a-2 CONFIRMED: B1898/FINDINGS.md §1 claims 'Every quotation was found by machine at the commit read' right after naming 'one dated addition', contradicting arc_verdict.json, §4, Disclosed, and REVIEWS.md!")

        # --- DEFECT R80a-3: REVIEWS.md §1b counts 21 unmerged branches because origin/main (+12 past c40446392) was counted as an unmerged leaf! ---
        rt_txt = (b98 / "verification/review_tools_on_the_commit_read_out.txt").read_text(encoding="utf-8")
        rev_txt = (wt / "docs/progress/REVIEWS.md").read_text(encoding="utf-8")
        m_leaves = re.search(r"branches: 21 unmerged leaves;.*?on one remote only: (\[.*?\])", rt_txt)
        assert m_leaves
        leaves_21 = eval(m_leaves.group(1))
        assert len(leaves_21) == 21 and "main" in leaves_21 and len([x for x in leaves_21 if x != "main"]) == 20
        assert "   main                                     +12  tip 2026-11-12  registered" in rt_txt
        assert "21 branches not merged, every one registered as a lane (the review's tool, on the commit read)." in rev_txt
        assert "None was newly registered." in rev_txt[rev_txt.index("# Review 80 ") :]
        print("  DEFECT R80a-3 CONFIRMED: REVIEWS.md §1b states '21 branches not merged ... None was newly registered' (vs 20 at Review 79) because review_tools at c40446392 counted origin/main (+12 commits ahead) as one of the 21 unmerged branches!")

        # --- DEFECT R80a-5 (minor accuracy on non-agy002 HARVEST_LEDGER row 1735 & B1898 §1 bullet 3): W7 GENESIS v1.67 & W1 9 script asserts not yet mended on main ---
        hl_txt = (wt / "docs/HARVEST_LEDGER.md").read_text(encoding="utf-8")
        row_1735 = [ln for ln in hl_txt.splitlines() if ln.startswith("| 1735 |")][0]
        assert "Five things in it are in the enforcement package's files and went to its builder; the rest is mended on main" in row_1735
        assert "The foundation's seven passages in plain words" in s57 and "Nine asserts in scripts that end in a constant" in s57
        print("  DEFECT R80a-5 CONFIRMED: HARVEST_LEDGER row 1735 (web seat W-R80) says 'Five things ... went to its builder; the rest is mended on main', overlooking that W7's 7 foundation passages (v1.67) and W1's 9 script asserts are still unmended in STATUS_OF_THE_57 ('Owed from the first 43')!")

        # --- CONTROLS & PLANTED LOCK MUTATIONS (DEFECT R80a-4) ON THE 5 DETERMINISTIC LOCK TESTS ---
        k5 = ["-k", "not three_of_the_four"]
        rc_c5, tail_c5, _ = run_pytest(wt, lock_rel, k5)
        assert rc_c5 == 0, tail_c5
        # Control CTL-R80A-LOCK-FIRES: verdict="NEGATIVE" must FAIL:
        (b98 / "arc_verdict.json").write_text(json.dumps(dict(av98, verdict="NEGATIVE")), encoding="utf-8")
        rc_neg, _, _ = run_pytest(wt, lock_rel, k5)
        assert rc_neg != 0, "Expected verdict='NEGATIVE' to fail test_b1898_review_80.py!"
        reset_wt(wt)

        # Plant P1: Invert B1898/arc_verdict.json claim_one_line to claim main checked all 100 in full, 0 held, 17 & 41 mended, and drop '0 of 19.':
        av_p1 = dict(av98)
        av_p1["claim_one_line"] = (
            "REVIEW 80: 100 FINDINGS ON MAIN'S WORK. MAIN CHECKED ALL 100 OF THEM IN FULL AND ZERO HELD; "
            "0 UNCHECKED; ALL 17 AND ALL 41 ARE ALREADY MENDED ON MAIN."
        )
        (b98 / "arc_verdict.json").write_text(json.dumps(av_p1), encoding="utf-8")
        rc_p1, tail_p1, _ = run_pytest(wt, lock_rel, k5)
        assert rc_p1 == 0, f"Expected Plant P1 to pass weak substring check in test_b1898, got {tail_p1}"
        reset_wt(wt)

        # Plant P2: Rewrite Review 80's entry in REVIEWS.md so all 17 reader-only findings are claimed checked in full by main and all 41 waiting findings are claimed mended!
        r80_idx = rev_txt.index("\n# Review 80 ")
        rev_head, rev_entry = rev_txt[:r80_idx], rev_txt[r80_idx:]
        rev_entry_mut = (
            rev_entry.replace(
                "main checked 80 in full and all 80 held; 17 were looked at by their reader alone; 41 wait to be built",
                "main checked 100 in full and all 100 held; 0 stood on their reader's word alone; 0 wait to be built",
            )
            .replace(
                "- **Main checked 80 of them in full, and all 80 held.** It checked 3 more in part. **17 have been looked at by nobody\n  but their reader.**",
                "- **Main checked 100 of them in full, and all 100 held.** Zero were checked in part and zero stood on their reader's word alone.",
            )
            .replace(
                "- **41 of the 57 wait to be built,**",
                "- **0 of the 57 wait to be built (all 41 mended on main),**",
            )
            .replace(
                "- **Checked by main:** 80 findings in full and 3 in part",
                "- **Checked by main:** 100 findings in full and 0 in part",
            )
            .replace(
                "And 17 findings stand on their reader's word alone:\n  eleven of the SM seat's, four of agy-exp's, and the web seat's two of its addition.",
                "Zero findings stand on their reader's word alone.",
            )
        )
        assert rev_entry_mut != rev_entry
        (wt / "docs/progress/REVIEWS.md").write_text(rev_head + rev_entry_mut, encoding="utf-8")
        rc_p2, tail_p2, _ = run_pytest(wt, lock_rel, k5)
        assert rc_p2 == 0, f"Expected Plant P2 (unchecked written as checked in REVIEWS.md) to pass test_b1898, got {tail_p2}"
        reset_wt(wt)

        # Plant P3: Corrupt B1898/FINDINGS.md §3 window counts (7 -> 0 added arcs, 26 -> 99 older arcs, 329 -> 500 law-map lines) & delete §5's list of 17 unchecked IDs:
        f98_mut = (
            f98_txt.replace("| arcs added | 7: B1891 to B1897 |", "| arcs added | 0: none |")
            .replace("| older arcs with a file changed | 26, of which 15 in their verdict file |", "| older arcs with a file changed | 99, of which 0 in their verdict file |")
            .replace("| the law map | 329 lines of its tables at both ends", "| the law map | 500 lines of its tables at both ends")
            .replace("17 (the SM seat's 22, 25, 26, 30, 32, 33 and 37 to 41; agy-exp's F9, F11, F13 and F14; the web seat's W8 and W9)", "17 (none listed)")
        )
        assert f98_mut != f98_txt
        (b98 / "FINDINGS.md").write_text(f98_mut, encoding="utf-8")
        rc_p3, tail_p3, _ = run_pytest(wt, lock_rel, k5)
        assert rc_p3 == 0, f"Expected Plant P3 (B1898/FINDINGS.md §3/§5 corruption) to pass test_b1898, got {tail_p3}"
        reset_wt(wt)

        # Plant P4: Revert all 18 [>] carry marks on R79-1..R79-18 to [ ], delete R80-1..R80-22 from REVIEWS.md, and corrupt P-834 in POINT_REGISTER.md:
        rev_p4 = rev_txt.replace("- [>] R79-", "- [ ] R79-")
        rev_p4 = "\n".join(ln for ln in rev_p4.splitlines() if not ln.startswith("- [ ] R80-"))
        (wt / "docs/progress/REVIEWS.md").write_text(rev_p4, encoding="utf-8")
        pr_p = wt / "docs/POINT_REGISTER.md"
        pr_p.write_text(
            pr_p.read_text(encoding="utf-8").replace("17 have been looked at by nobody but their reader", "0 unchecked; all 100 checked by main"),
            encoding="utf-8",
        )
        rc_p4, tail_p4, _ = run_pytest(wt, lock_rel, k5)
        assert rc_p4 == 0, f"Expected Plant P4 (R79 carry marks + R80 action items + P-834 corruption) to pass test_b1898, got {tail_p4}"
        reset_wt(wt)
        print(
            f"  DEFECT R80a-4 CONFIRMED: CTL-R80A-CLEAN-5=PASS ({tail_c5}), CTL-R80A-LOCK-FIRES=CAUGHT; "
            f"ALL 4 PLANTED CORRUPTIONS (P1 claim_one_line inversion, P2 REVIEWS.md marking all 100 checked & 0 waiting, "
            f"P3 B1898/FINDINGS.md §3/§5 counts, P4 R79/R80 action-item wipe + P-834 corruption) PASS test_b1898_review_80.py ({tail_p2})!"
        )
    finally:
        subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(wt)], env=GIT_ENV, capture_output=True)
        shutil.rmtree(td, ignore_errors=True)


def main() -> int:
    verify_independent_git_recounts()
    verify_patch_tables_entry_and_lock()
    print("\nALL A2-S-R80a COLD-READ CHECKS AND CONTROLS COMPLETED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
