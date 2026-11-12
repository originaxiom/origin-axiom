#!/usr/bin/env python3
"""Card A2-R79c (Commit 2, pre-prose): Run agy-002's pre-registered planted errors
against B1881's lock as landed on main at 3c5ab6bef (arc B1895).

All planted error categories (Group A: exact pre-existing 5c7f1879d / Row R17 plants P01..P03;
Group B: blind pre-inspection adversarial plants P04..P12) and controls (CTL-CLEAN,
CTL-KNOWN-FAIL) were committed and pushed in Commit 1 (41d0b7faa) prior to opening any file
of B1881 or B1895 at 3c5ab6bef.

0 of 19: data-free lock and provenance mutation testing only.
"""
import json
import pathlib
import re
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]
TARGET = "3c5ab6bef"

FILES = (
    "docs/HARVEST_LEDGER.md",
    "frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md",
    "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json",
    "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py",
    "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.json",
    "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main_run.txt",
    "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py",
)

CHILD_RUNNER = r"""
import importlib.util, json, pathlib, sys, traceback

test_path = pathlib.Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("test_b1881_lock", test_path)
mod = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(mod)
except Exception as exc:
    print(json.dumps({"import_error": f"{type(exc).__name__}: {exc}", "passed": [], "failed": [["<import>", f"{type(exc).__name__}: {exc}"]]}))
    sys.exit(0)

passed, failed = [], []
for name in [k for k in dir(mod) if k.startswith("test_") and callable(getattr(mod, k))]:
    try:
        getattr(mod, name)()
        passed.append(name)
    except Exception as exc:
        msg = str(exc).splitlines()[0] if str(exc) else type(exc).__name__
        failed.append([name, f"{type(exc).__name__}: {msg}"])

print(json.dumps({"import_error": None, "passed": passed, "failed": failed}))
"""


def git_show(rel_path: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "show", f"{TARGET}:{rel_path}"],
        text=True,
    )


def load_clean_snapshot() -> dict[str, str]:
    return {p: git_show(p) for p in FILES}


def replace_exact(text: str, old: str, new: str, label: str) -> str:
    assert old in text, f"[{label}] target substring not found: {old!r}"
    out = text.replace(old, new, 1)
    assert out != text, f"[{label}] mutation was a no-op"
    return out


def run_case(clean: dict[str, str], case_id: str, group: str, desc: str, mutator) -> dict:
    with tempfile.TemporaryDirectory(prefix=f"b1881_{case_id}_") as tmp:
        root = pathlib.Path(tmp)
        mutated = dict(clean)
        if mutator is not None:
            mutator(mutated)
            assert any(mutated[k] != clean[k] for k in FILES), f"[{case_id}] no file changed!"
        for rel, content in mutated.items():
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(content, encoding="utf-8")
        test_file = root / "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py"
        proc = subprocess.run(
            [sys.executable, "-B", "-c", CHILD_RUNNER, str(test_file)],
            capture_output=True,
            text=True,
            timeout=120,
        )
        assert proc.returncode == 0, f"[{case_id}] runner crashed: {proc.stderr}"
        res = json.loads(proc.stdout.strip().splitlines()[-1])
        caught = len(res["failed"]) > 0 or res["import_error"] is not None
        return {
            "id": case_id,
            "group": group,
            "desc": desc,
            "caught": caught,
            "passed_count": len(res["passed"]),
            "failed_count": len(res["failed"]),
            "failed_tests": res["failed"],
        }


def build_cases():
    F_PATH = "frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md"
    AV_PATH = "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json"
    PY_PATH = "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.py"
    JS_PATH = "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main.json"
    RUN_PATH = "frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main_run.txt"
    T_PATH = "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py"

    cases = []

    # Controls
    cases.append(("CTL-CLEAN", "Control", "Unmodified 3c5ab6bef baseline (all 10 lock tests must pass)", None))
    cases.append((
        "CTL-KNOWN-FAIL",
        "Control",
        "Corrupt cusp widths [1, 5] -> [2, 4] in test_the_two_quotients_recomputed (must fail)",
        lambda m: m.__setitem__(
            T_PATH,
            replace_exact(m[T_PATH], "census(lines, line_of) == ([1, 5], 2, 0, 0)", "census(lines, line_of) == ([2, 4], 2, 0, 0)", "CTL-KNOWN-FAIL"),
        ),
    ))

    # Group A — Exact pre-existing plants from 5c7f1879d (CTL-R79B-LOCK-B1881) and 944c2987b (Row R17)
    def p01a(m):
        s = re.sub(r"\[CORRECTED\s+2026-11-12 \(Review 79\):.*?\]", "", m[F_PATH], flags=re.S)
        s = replace_exact(s, "- **Three checks did not check what they said**", "- **Note**", "P01a")
        m[F_PATH] = s

    def p01b(m):
        s = re.sub(r"\[CORRECTED.*?\]", "", m[F_PATH], flags=re.S)
        s = re.sub(r"\n> \*\*CORRECTED 2026-11-12, a second time,\*\*.*?(?=\n- On all 47,988)", "", s, flags=re.S)
        s = replace_exact(s, "- **Three checks did not check what they said**", "- **Note**", "P01b")
        m[F_PATH] = s

    cases.append(("P01a", "Group A", "Strip Review 79 [CORRECTED ...] brackets and 'Three checks did not check what they said' from FINDINGS.md", p01a))
    cases.append(("P01b", "Group A", "Strip ALL [CORRECTED ...] brackets and second-round correction blockquote from FINDINGS.md", p01b))
    cases.append((
        "P02a",
        "Group A",
        "Revert SM-13/X7 mirror_ok check condition in whole_and_value_on_main.py back to literal True (JSON untouched)",
        lambda m: m.__setitem__(
            PY_PATH,
            replace_exact(
                m[PY_PATH],
                "mirror_ok and len(box) >= 200 and sum(1 for x in box if x[2] != 0) >= 200",
                "True",
                "P02a",
            ),
        ),
    ))
    cases.append((
        "P02b",
        "Group A",
        "Revert SM-13/X7 single_ok check condition in whole_and_value_on_main.py back to literal True (JSON untouched)",
        lambda m: m.__setitem__(
            PY_PATH,
            replace_exact(
                m[PY_PATH],
                'check("the own values of the allowed single runs increase without bound: 5m/2 + sqrt5/2 for the run of 5m + 1", single_ok,',
                'check("the own values of the allowed single runs increase without bound: 5m/2 + sqrt5/2 for the run of 5m + 1", True,',
                "P02b",
            ),
        ),
    ))
    cases.append((
        "P03",
        "Group A",
        "Drop SM-14 0.9..1 percentage-offset bound from E11 check in whole_and_value_on_main.py (JSON untouched)",
        lambda m: m.__setitem__(
            PY_PATH,
            replace_exact(
                m[PY_PATH],
                ' and mp.mpf("0.9") < (one6 - own["(6)"]) / own["(6)"] * 100 < 1',
                "",
                "P03",
            ),
        ),
    ))

    # Group B — Blind pre-inspection adversarial plants (committed in 41d0b7faa before reading 3c5ab6bef's lock)
    cases.append((
        "P04a",
        "Group B",
        "Remove B1895 coordinate-swap correction blockquote on 'transpose' from FINDINGS.md (keeping Review 79 brackets)",
        lambda m: m.__setitem__(
            F_PATH,
            re.sub(r"\n> \*\*CORRECTED 2026-11-12, a second time,\*\*.*?(?=\n- On all 47,988)", "", m[F_PATH], flags=re.S),
        ),
    ))
    cases.append((
        "P04b",
        "Group B",
        "Remove B1895 'CORRECTED AGAIN' coordinate-swap clause from B1881/arc_verdict.json (reverting to B1894's 'is the transpose')",
        lambda m: m.__setitem__(
            AV_PATH,
            replace_exact(
                m[AV_PATH],
                ". CORRECTED AGAIN the same day, found by a second reading of that note: it is not the transpose; it is the seat's with every matrix conjugated by the swap of the two coordinates, read on the column that is the swap of the one the mark annihilates, and the two tests are one test on every matrix of determinant 1 mod 5, so the agreement that follows is an instance of an identity]",
                "]",
                "P04b",
            ),
        ),
    ))
    cases.append((
        "P04c",
        "Group B",
        "Append fresh unbracketed separate paragraph in FINDINGS.md asserting [[2, 1], [1, 1]] is the matrix transpose of [[1, 1], [1, 2]] (P-817 shape)",
        lambda m: m.__setitem__(
            F_PATH,
            replace_exact(
                m[F_PATH],
                "- On all 47,988 run sequences of length 2, 4 and 6 with runs to 6, the two agree, with no exception.",
                "In short, the column convention [[2, 1], [1, 1]] is the matrix transpose of the seat's ground [[1, 1], [1, 2]].\n\n- On all 47,988 run sequences of length 2, 4 and 6 with runs to 6, the two agree, with no exception.",
                "P04c",
            ),
        ),
    ))
    cases.append((
        "P05a_b1872",
        "Group B",
        "Revert keeps_line_main docstring in whole_and_value_on_main.py to attribute column convention to B1872",
        lambda m: m.__setitem__(
            PY_PATH,
            replace_exact(
                m[PY_PATH],
                '    """this arc\'s second convention: L = [[1,1],[0,1]], R = [[1,0],[1,1]], columns, v = (1,2).\n    [CORRECTED 2026-11-12: this read "B1872\'s convention".  B1872 writes the seat\'s, rows.  These letters are the seat\'s\n    conjugated by the swap of the two coordinates; see the note at E12 in the header.]"""',
                '    """B1872\'s convention: L = [[1,1],[0,1]], R = [[1,0],[1,1]], columns, v = (1,2)"""',
                "P05a_b1872",
            ),
        ),
    ))
    cases.append((
        "P05a_transpose",
        "Group B",
        "Mutate keeps_line_main docstring in whole_and_value_on_main.py to call the column convention 'the transpose of the seat's'",
        lambda m: m.__setitem__(
            PY_PATH,
            replace_exact(
                m[PY_PATH],
                "These letters are the seat's\n    conjugated by the swap of the two coordinates;",
                "These letters are the transpose of the seat's convention;",
                "P05a_transpose",
            ),
        ),
    ))
    cases.append((
        "P05b",
        "Group B",
        "Remove E12 header docstring correction in whole_and_value_on_main.py",
        lambda m: m.__setitem__(
            PY_PATH,
            re.sub(r"\n     \[CORRECTED 2026-11-12, twice\..*?with a mark for which it fails\.\]", "", m[PY_PATH], flags=re.S),
        ),
    ))
    cases.append((
        "P06a",
        "Group B",
        "Revert 'is recomputed' back to unbracketed 'is reproduced' in section 1 of FINDINGS.md",
        lambda m: m.__setitem__(
            F_PATH,
            replace_exact(
                m[F_PATH],
                '- **Every exact fact of both relays is recomputed by main\'s own code:** 65 checks, none failing. [CORRECTED\n  2026-11-12, found by a second reading of Review 79\'s mends: this read "is reproduced". The record keeps that word\n  for the same code run again on a clean checkout (`docs/seats/README.md` § 12). None of the seat\'s code was run.]',
                "- **Every exact fact of both relays is reproduced by main's own code:** 65 checks, none failing.",
                "P06a",
            ),
        ),
    ))
    cases.append((
        "P06b",
        "Group B",
        "Revert 'every printed number recomputed [CORRECTED ...]' back to 'every printed number reproduced' in B1881/arc_verdict.json",
        lambda m: m.__setitem__(
            AV_PATH,
            replace_exact(
                m[AV_PATH],
                "every printed number recomputed [CORRECTED 2026-11-12: this read 'reproduced', a word the record keeps for the same code run again; none of the seat's code was run]",
                "every printed number reproduced",
                "P06b",
            ),
        ),
    ))
    cases.append((
        "P06c",
        "Group B",
        "Revert 'recomputed' back to 'reproduced' in whole_and_value_on_main.py header docstring",
        lambda m: m.__setitem__(
            PY_PATH,
            replace_exact(
                m[PY_PATH],
                "code is run or imported; its printed numbers are typed below only as the things to be recomputed.\n[CORRECTED 2026-11-12, found by a second reading of Review 79's mends: this header said 'reproduced' here and at E10.  The record\nkeeps that word for the same code run again; none of the seat's code was run, so every number here is recomputed.]",
                "code is run or imported; its printed numbers are typed below only as the things to be reproduced.",
                "P06c",
            ),
        ),
    ))
    cases.append((
        "P07",
        "Group B",
        "Remove only SM-12's [CORRECTED ...] bracket in ## Disclosed of FINDINGS.md while keeping all other brackets intact",
        lambda m: m.__setitem__(
            F_PATH,
            replace_exact(
                m[F_PATH],
                " [CORRECTED 2026-11-12\n  (Review 79): the section cited is about a re-audit that sat unread for eight hours, not about these relays. The ten\n  hours are main's reckoning and no file is cited for them.]",
                "",
                "P07",
            ),
        ),
    ))
    cases.append((
        "P08",
        "Group B",
        "Type literal integer counts 16275, 2815, 5575 in whole_and_value_on_main.py instead of computing them (M9: 'computes the three counts and types none')",
        lambda m: m.__setitem__(
            PY_PATH,
            replace_exact(
                m[PY_PATH],
                '    seqs = [seq for n in (2, 4, 6) for seq in itertools.product(range(1, 6), repeat=n)]\n    by_all = len({min(seq[i:] + seq[:i] for i in range(len(seq))) for seq in seqs})\n    by_even = len({min(seq[i:] + seq[:i] for i in range(0, len(seq), 2)) for seq in seqs})\n    RES["B_counts"] = {"sequences_as_written": len(lows), "up_to_every_rotation": by_all, "up_to_rotations_that_keep_the_letters": by_even}',
                '    seqs = lows\n    by_all = 2815\n    by_even = 5575\n    RES["B_counts"] = {"sequences_as_written": 16275, "up_to_every_rotation": 2815, "up_to_rotations_that_keep_the_letters": 5575}',
                "P08",
            ),
        ),
    ))

    def p09a(m):
        js = json.loads(m[JS_PATH])
        old_key = [k for k in js if k.startswith("the least apex over every run sequence")][0]
        val = js.pop(old_key)
        js["the least apex over every cyclic run sequence of even length to 6 with runs to 5 is the ground's own, sqrt5/2 (16275 sequences)"] = val
        m[JS_PATH] = json.dumps(js, indent=1) + "\n"

    cases.append(("P09a", "Group B", "Revert least-apex check label in whole_and_value_on_main.json back to 'every cyclic run sequence ... (16275 sequences)'", p09a))
    cases.append((
        "P09b",
        "Group B",
        "Desynchronize whole_and_value_on_main_run.txt alone (alter sequence counts and set notation in _run.txt while leaving .py and .json intact)",
        lambda m: m.__setitem__(
            RUN_PATH,
            replace_exact(
                replace_exact(
                    m[RUN_PATH],
                    "(16275 sequences as written; 2815 up to rotation; 5575 up to the rotations that keep which letter a run is)",
                    "(16275 sequences)",
                    "P09b_counts",
                ),
                "{'the twin exchange': ['-11 + 2*I', '-11 - 2*I'], 'W': ['5*sqrt(5)'], 'W with the twin exchange': ['-5*sqrt(5)']}",
                "{'the twin exchange': {'-11 - 2*I', '-11 + 2*I'}, 'W': {'5*sqrt(5)'}, 'W with the twin exchange': {'-5*sqrt(5)'}}",
                "P09b_set",
            ),
        ),
    ))
    cases.append((
        "P09c",
        "Group B",
        "Remove SM-17's [CORRECTED ...] bracket on 16,275 vs 2,815/5,575 from FINDINGS.md while keeping other brackets intact",
        lambda m: m.__setitem__(
            F_PATH,
            re.sub(
                r" \[CORRECTED\n  2026-11-12 \(Review 79\): this read \"cyclic run sequences\"\..*?which letter a run is\]",
                "",
                m[F_PATH],
                flags=re.S,
            ),
        ),
    ))
    cases.append((
        "P10",
        "Group B",
        "Non-literal tautology 'or len(box) > 0' appended to SM-13 mirror_ok and single_ok checks in whole_and_value_on_main.py (JSON untouched)",
        lambda m: m.__setitem__(
            PY_PATH,
            replace_exact(
                replace_exact(
                    m[PY_PATH],
                    "mirror_ok and len(box) >= 200 and sum(1 for x in box if x[2] != 0) >= 200",
                    "(mirror_ok and len(box) >= 200 and sum(1 for x in box if x[2] != 0) >= 200) or len(box) > 0",
                    "P10_mirror",
                ),
                'check("the own values of the allowed single runs increase without bound: 5m/2 + sqrt5/2 for the run of 5m + 1", single_ok,',
                'check("the own values of the allowed single runs increase without bound: 5m/2 + sqrt5/2 for the run of 5m + 1", single_ok or len(box) > 0,',
                "P10_single",
            ),
        ),
    ))
    cases.append((
        "P11a",
        "Group B",
        "Revert M9's first self-caught mend in whole_and_value_on_main.py: E12 check from 'and' back to 'disagree == 0 or rev == 0 or rot == 0'",
        lambda m: m.__setitem__(
            PY_PATH,
            replace_exact(
                m[PY_PATH],
                "RES[name] = (disagree == 0 and rev == 0 and agree == 6 ** 2 + 6 ** 4 + 6 ** 6)",
                "RES[name] = (disagree == 0 or rev == 0 or rot == 0)",
                "P11a",
            ),
        ),
    ))
    cases.append((
        "P11b",
        "Group B",
        "Revert M9's second self-caught mend in whole_and_value_on_main.py: drop sorted(v) back to unsorted set dict 'over' on E5",
        lambda m: m.__setitem__(
            PY_PATH,
            replace_exact(
                m[PY_PATH],
                "{k: sorted(v) for k, v in over.items()}",
                "over",
                "P11b",
            ),
        ),
    ))
    cases.append((
        "P12",
        "Group B",
        "Revert B1881/arc_verdict.json convention attribution back to unbracketed 'the seat's convention and B1872's name one allowed set'",
        lambda m: m.__setitem__(
            AV_PATH,
            re.sub(
                r" \[CORRECTED 2026-11-12 \(Review 79's second round\): B1872's convention is the seat's.*?instance of an identity\]",
                "",
                m[AV_PATH],
                flags=re.S,
            ),
        ),
    ))

    return cases


def main():
    clean = load_clean_snapshot()
    print(f"=== CARD A2-R79c: B1881 PLANTED-ERROR SUITE AGAINST main@{TARGET} ===")
    cases = build_cases()
    results = []
    for cid, grp, desc, mut in cases:
        r = run_case(clean, cid, grp, desc, mut)
        results.append(r)
        if grp == "Control":
            status = "CONTROL_OK" if ((cid == "CTL-CLEAN" and not r["caught"]) or (cid == "CTL-KNOWN-FAIL" and r["caught"])) else "CONTROL_BROKEN"
        else:
            status = "CAUGHT (lock failed)" if r["caught"] else "PASSED (lock missed!)"
        failed_names = ", ".join(x[0] for x in r["failed_tests"]) if r["failed_tests"] else "none"
        print(f"[{cid:14s}] ({grp:7s}) -> {status:22s} | passed={r['passed_count']:2d}, failed={r['failed_count']:2d} [{failed_names}]")
        print(f"    desc: {desc}")

    assert not results[0]["caught"] and results[0]["passed_count"] == 10, "CTL-CLEAN must pass all 10 tests!"
    assert results[1]["caught"], "CTL-KNOWN-FAIL must fail!"

    grp_a = [r for r in results if r["group"] == "Group A"]
    grp_b = [r for r in results if r["group"] == "Group B"]
    print("\n=== SUMMARY ===")
    print(f"Controls: 2/2 behaved as required (CTL-CLEAN 10/10 passed; CTL-KNOWN-FAIL caught)")
    print(f"Group A (exact pre-existing 5c7f1879d / Row R17 plants): {sum(r['caught'] for r in grp_a)}/{len(grp_a)} caught, {sum(not r['caught'] for r in grp_a)} passed")
    print(f"Group B (blind pre-inspection adversarial plants from 41d0b7faa): {sum(r['caught'] for r in grp_b)}/{len(grp_b)} caught, {sum(not r['caught'] for r in grp_b)} passed")
    missed = [r for r in grp_a + grp_b if not r["caught"]]
    print("Plants that PASSED the lock at 3c5ab6bef:", [r["id"] for r in missed])
    print("0 of 19.")


if __name__ == "__main__":
    main()
