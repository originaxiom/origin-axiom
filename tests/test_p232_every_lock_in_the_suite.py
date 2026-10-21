"""P-232 -- every lock runs in the full suite. Review 66's full suite collected tests/ only, so the arcs' own locks in
frontier/B*/verification/ never ran in it, and a lock the review's own edits broke (B1626's) went unseen until a landing
set named it. Locked here: pyproject's testpaths names the arcs' locks; the runner names no path, so the testpaths apply;
the glob catches every file in a verification folder that defines a test and nothing that does not (the bite: the
probe scripts named *_test.py there); no lock shares a basename with a test in tests/; the changed-file selector knows
the locks, and a ledger edit selects B1626's lock (the case that was missed)."""
import glob, importlib.util, re, tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GLOB = "frontier/B*/verification/test_b*.py"
DEFINES_TEST = re.compile(r"^(def|    def) test_", re.M)


def _defines_test(p):
    return bool(DEFINES_TEST.search(Path(ROOT, p).read_text(encoding="utf-8", errors="ignore")))


def uncovered(paths, covered):
    """the verification-folder files that define a test but that the lock glob does not collect"""
    return sorted(p for p in paths if p not in covered and _defines_test(p))


def test_testpaths_and_the_runner():
    cfg = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["tool"]["pytest"]["ini_options"]
    assert cfg["testpaths"] == ["tests", GLOB]
    sh = (ROOT / "scripts" / "run_suite.sh").read_text(encoding="utf-8")
    assert "exec python3 -m pytest -q" in sh and "pytest tests/" not in sh


def test_the_glob_catches_every_lock_and_no_script():
    covered = {Path(p).as_posix() for p in glob.glob(str(ROOT / GLOB))}
    covered = {str(Path(p).relative_to(ROOT).as_posix()) for p in covered}
    in_verification = {str(Path(p).relative_to(ROOT).as_posix()) for p in glob.glob(str(ROOT / "frontier/B*/verification/*.py"))}
    assert len(covered) >= 14 and all(_defines_test(p) for p in covered)
    assert uncovered(in_verification, covered) == []
    # the bite: the two probe scripts in verification folders define no test and are not collected
    for script in ("frontier/B1189_close_loop_batch1/verification/arithmeticity_test.py",
                   "frontier/B1345_the_jorgensen_number/verification/b1345_amphichirality_test.py"):
        assert script in in_verification and script not in covered and not _defines_test(script)
    # and a lock named outside the pattern would be reported
    lock = "frontier/B1626_the_relay_closure_pass/verification/test_b1626_the_relay_closure_pass.py"
    assert uncovered({lock}, covered - {lock}) == [lock]


def test_no_basename_collision():
    locks = {Path(p).name for p in glob.glob(str(ROOT / GLOB))}
    assert not locks & {Path(p).name for p in glob.glob(str(ROOT / "tests" / "*.py"))}


def test_the_selector_knows_the_locks():
    spec = importlib.util.spec_from_file_location("affected_tests_p232", ROOT / "scripts" / "affected_tests.py")
    A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
    lock = "frontier/B1626_the_relay_closure_pass/verification/test_b1626_the_relay_closure_pass.py"
    assert lock in A.LOCKS and A.ALL[0].startswith("tests/")
    sel, full = A.select({"docs/RELAY_LEDGER.md"})
    assert lock in sel and not full
    sel, full = A.select({"frontier/B1626_the_relay_closure_pass/FINDINGS.md"})
    assert lock in sel and not full
