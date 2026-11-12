#!/usr/bin/env python3
"""Card A2-R79d (Commit 2, pre-prose): Re-run agy-002's exact 23 planted errors
from A2-R79c (bfb11498c) against B1881's lock as landed on main at c40446392 (arc B1897).

Imports build_cases() directly from relays/r79c/run_b1881_planted_errors.py so that
every single one of the 23 planted mutations (Group A: 5; Group B: 18) and both controls
(CTL-CLEAN, CTL-KNOWN-FAIL) are byte-for-byte identical in mutation logic to bfb11498c.

0 of 19: data-free lock and provenance mutation testing only.
"""
import concurrent.futures
import json
import pathlib
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "relays" / "r79c"))
import run_b1881_planted_errors as r79c  # noqa: E402

TARGET = "c40446392"

CHILD_RUNNER = r"""
import importlib.util, inspect, json, pathlib, sys, tempfile

test_path = pathlib.Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("test_b1881_lock", test_path)
mod = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(mod)
except Exception as exc:
    print(json.dumps({"import_error": f"{type(exc).__name__}: {exc}", "passed": [], "failed": [["<import>", f"{type(exc).__name__}: {exc}"]]}))
    sys.exit(0)

passed, failed = [], []
for name in sorted(k for k in dir(mod) if k.startswith("test_") and callable(getattr(mod, k))):
    fn = getattr(mod, name)
    params = list(inspect.signature(fn).parameters)
    try:
        if params == ["tmp_path"]:
            with tempfile.TemporaryDirectory(prefix=f"pytest_{name}_") as td:
                fn(pathlib.Path(td))
        elif not params:
            fn()
        else:
            raise RuntimeError(f"Unsupported fixture parameters: {params}")
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


def list_tracked_files() -> tuple[str, ...]:
    arc_files = subprocess.check_output(
        ["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", TARGET, "--", "frontier/B1881_the_whole_and_the_value_verified"],
        text=True,
    ).splitlines()
    return ("docs/HARVEST_LEDGER.md", *sorted(f.strip() for f in arc_files if f.strip()))


def run_one_case(files: tuple[str, ...], clean: dict[str, str], item: tuple) -> dict:
    case_id, group, desc, mutator = item
    with tempfile.TemporaryDirectory(prefix=f"b1881_r79d_{case_id}_") as tmp:
        root = pathlib.Path(tmp)
        mutated = dict(clean)
        if mutator is not None:
            mutator(mutated)
            assert any(mutated[k] != clean[k] for k in files), f"[{case_id}] no file changed!"
        for rel, content in mutated.items():
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(content, encoding="utf-8")
        test_file = root / "frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py"
        proc = subprocess.run(
            [sys.executable, "-B", "-c", CHILD_RUNNER, str(test_file)],
            capture_output=True,
            text=True,
            timeout=240,
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


def main():
    import mpmath
    import sympy

    files = list_tracked_files()
    clean = {p: git_show(p) for p in files}
    recorded_versions = json.loads(clean["frontier/B1881_the_whole_and_the_value_verified/verification/whole_and_value_on_main_made_with.json"])
    local_versions = {
        "python": "%d.%d" % sys.version_info[:2],
        "mpmath": mpmath.__version__,
        "sympy": sympy.__version__,
    }
    same_versions = recorded_versions == local_versions

    print(f"=== CARD A2-R79d: RE-RUN OF EXACT 23 A2-R79c PLANTS AGAINST main@{TARGET} ===")
    print("Tracked files materialized per isolated workspace:", list(files))
    print("Recorded made_with versions:", json.dumps(recorded_versions, sort_keys=True))
    print("Local environment versions: ", json.dumps(local_versions, sort_keys=True))
    print("Comparison branch exercised:", "EXACT_BYTES (versions match)" if same_versions else "EIGHT_DIGITS_AND_CHECKS (versions differ)")

    cases = r79c.build_cases()
    assert len([c for c in cases if c[1] in ("Group A", "Group B")]) == 23

    # Execute in parallel across isolated temp dirs, preserving exact case order in output
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futs = [pool.submit(run_one_case, files, clean, item) for item in cases]
        results = [f.result() for f in futs]

    for r in results:
        cid, grp, desc = r["id"], r["group"], r["desc"]
        if grp == "Control":
            status = "CONTROL_OK" if ((cid == "CTL-CLEAN" and not r["caught"]) or (cid == "CTL-KNOWN-FAIL" and r["caught"])) else "CONTROL_BROKEN"
        else:
            status = "CAUGHT (lock failed)" if r["caught"] else "PASSED (lock missed!)"
        failed_names = ", ".join(x[0] for x in r["failed_tests"]) if r["failed_tests"] else "none"
        print(f"[{cid:14s}] ({grp:7s}) -> {status:22s} | passed={r['passed_count']:2d}, failed={r['failed_count']:2d} [{failed_names}]")
        print(f"    desc: {desc}")

    assert not results[0]["caught"] and results[0]["passed_count"] == 15, f"CTL-CLEAN failed or wrong count: {results[0]}"
    assert results[1]["caught"], "CTL-KNOWN-FAIL must fail!"

    grp_a = [r for r in results if r["group"] == "Group A"]
    grp_b = [r for r in results if r["group"] == "Group B"]
    all_plants = grp_a + grp_b
    previously_passing_ids = ("P04c", "P05a_transpose", "P08", "P09b", "P10", "P11b")
    prev_six = [r for r in all_plants if r["id"] in previously_passing_ids]

    print("\n=== SUMMARY ===")
    print(f"Controls: 2/2 behaved as required (CTL-CLEAN {results[0]['passed_count']}/15 passed; CTL-KNOWN-FAIL caught)")
    print(f"Group A (exact pre-existing 5c7f1879d / Row R17 plants): {sum(r['caught'] for r in grp_a)}/{len(grp_a)} caught, {sum(not r['caught'] for r in grp_a)} passed")
    print(f"Group B (blind pre-inspection adversarial plants from 41d0b7faa): {sum(r['caught'] for r in grp_b)}/{len(grp_b)} caught, {sum(not r['caught'] for r in grp_b)} passed")
    print(f"Previously passing 6 plants (P04c, P05a_transpose, P08, P09b, P10, P11b): {sum(r['caught'] for r in prev_six)}/{len(prev_six)} caught")
    print(f"Total across all 23 plants: {sum(r['caught'] for r in all_plants)}/{len(all_plants)} caught, {sum(not r['caught'] for r in all_plants)} passed")
    missed = [r["id"] for r in all_plants if not r["caught"]]
    print("Plants that PASSED the lock at c40446392:", missed)
    print("0 of 19.")


if __name__ == "__main__":
    main()
