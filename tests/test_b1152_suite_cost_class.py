"""B1152 lock -- the cost failure class harvest (cc3 B8139) + the fast lane. Locks (a) main staying
clean of the four drift classes cost let through in cc3's band, (b) the changed-file selector's SAFETY
property (an unbounded change falls back to FULL -- never a false green), (c) the slow marker registered.
Method/tooling; Gate 5 n/a."""
import glob
import json
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1152_suite_cost_class"


def _d():
    return json.loads((ARC / "b1152_results.json").read_text(encoding="utf-8"))


def _load_selector():
    spec = importlib.util.spec_from_file_location("affected_tests", ROOT / "scripts" / "affected_tests.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)                       # NB: module chdir's to repo root at import (intended)
    return m


def test_arc_verdict_proved():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1152" and d["verdict"] == "PROVED"


def test_main_band_clean_of_the_drift_classes():
    # the ongoing guard: main stays clean of what "cost" let through in cc3's band
    SEALED = {"PROVED", "NEGATIVE", "OPEN", "RETRACTED"}
    bad_inst = bad_verd = miss_find = 0
    for p in glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json")):
        d = json.loads(Path(p).read_text(encoding="utf-8"))
        arc = Path(p).parent
        if not isinstance(d.get("instrument"), bool):
            bad_inst += 1
        if d.get("verdict") not in SEALED:
            bad_verd += 1
        if not ((arc / "FINDINGS.md").is_file() or (arc / "VERDICT.md").is_file()):
            miss_find += 1
    assert bad_inst == 0, f"{bad_inst} arcs with non-bool instrument"
    assert bad_verd == 0, f"{bad_verd} arcs with off-vocabulary verdict"
    assert miss_find == 0, f"{miss_find} arcs with neither FINDINGS.md nor VERDICT.md"


def test_selector_is_conservative_never_a_false_green():
    A = _load_selector()
    # an unbounded change (scripts code) MUST fall back to FULL, not a subset
    _, full = A.select({"scripts/gates/gates.py"})
    assert full, "a scripts/ code change must fall back to FULL"
    # conftest affects every test -> FULL
    _, full = A.select({"tests/conftest.py"})
    assert full
    # a lone test file -> exactly itself, no FULL
    lone = Path(A.ALL[0]).as_posix()
    sel, full = A.select({lone})
    assert sel == [lone] and not full
    # a frontier arc -> its own test + the corpus/gate aggregates (a bounded SUPERSET), no FULL
    sel, full = A.select({"frontier/B1151_gue_larget_superposition/FINDINGS.md"})
    assert not full
    assert "tests/test_repo_gates.py" in sel and any("b1151" in f for f in sel)
    assert "tests/test_b833_negative_routing.py" in sel   # negative-routing runs on any arc change


def test_selector_relay_only_runs_nothing_not_full():
    # B8140 (cc3's audit): a relay-only diff must select NO tests (relays are test-inert), NOT fall
    # back to the full suite -- writing a relay is the commonest operation, and the tool defeated
    # itself on it by conflating "nothing matched (inert)" with "cannot bound". Fix verified 3 ways:
    A = _load_selector()
    sel, full = A.select({"CC_TO_CLOUD_2026-08-25_AUDIT.md"})
    assert not full and not sel                          # relay alone -> nothing affected
    sel, full = A.select({"CC_TO_CLOUD_x.md", "frontier/B1151_gue_larget_superposition/FINDINGS.md"})
    assert not full and any("b1151" in f for f in sel)   # relay + arc -> the arc's tests (not full)
    sel, full = A.select({"CC_TO_CLOUD_x.md", "scripts/gates/gates.py"})
    assert full                                          # relay + script -> full (unmappable dominates)


def test_run_suite_uses_set_u_safe_array_expansion():
    # regression (B1152, caught by the suite it introduced): macOS ships bash 3.2, where under
    # `set -u` the empty-array expansion "${MARK[@]}" is an UNBOUND-VARIABLE error -- the --fast/
    # --serial flag machinery must use the ${MARK[@]+"${MARK[@]}"} guard so the runner still runs.
    import subprocess
    sh_path = ROOT / "scripts" / "run_suite.sh"
    assert subprocess.run(["bash", "-n", str(sh_path)]).returncode == 0     # syntax
    sh = sh_path.read_text(encoding="utf-8")
    assert sh.count('${MARK[@]+"${MARK[@]}"}') == 1                         # the set -u-safe guard is used
    # every "${MARK[@]}" must sit INSIDE that guard (the safe form contains the substring once),
    # so equal counts <=> no bare unguarded "${MARK[@]}" survives
    assert sh.count('"${MARK[@]}"') == sh.count('${MARK[@]+"${MARK[@]}"}')


def test_slow_marker_registered_and_finding_recorded():
    conf = (ROOT / "tests" / "conftest.py").read_text(encoding="utf-8")
    assert "addinivalue_line" in conf and '"slow' in conf     # the marker is registered
    r = _d()
    assert "cost" in r["the_finding_harvested"].lower() and "1f455266" in r["harvest_source"]
    assert "CLEAN" in r["main_band_audit"]["negative_routing"]
    assert "FULL" in r["remedy"]["changed_file_selector"]      # the safety property is documented
