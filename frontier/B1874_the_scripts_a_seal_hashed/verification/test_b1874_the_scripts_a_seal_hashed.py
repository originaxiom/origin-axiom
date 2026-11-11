"""B1874 -- the measurement is what the script prints today, the page lists exactly the gate's frozen keys, and the gate is
registered with a control.  The planted violations themselves are in tests/test_artifact_hashes.py."""
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_b1874_lock", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def test_the_measurement_reproduces():
    out = subprocess.run([sys.executable, "-B", str(HERE / "measure_hash_lists.py")], capture_output=True, text=True, check=True, timeout=900).stdout
    sealed = (HERE / "measure_hash_lists_run.txt").read_text(encoding="utf-8")
    m = re.search(r"lists of hashed files: (\d+); entries: (\d+); verify: (\d+); do not: (\d+) \((\d+) distinct\)", out)
    assert m and int(m.group(3)) + int(m.group(4)) == int(m.group(2))
    # the sealed run is the dated count; a later repair may only lower the number that do not verify
    s = re.search(r"verify: (\d+); do not: (\d+) \((\d+) distinct\)", sealed)
    assert (int(s.group(1)), int(s.group(2)), int(s.group(3))) == (1430, 67, 63)
    assert int(m.group(5)) <= 63


def test_the_page_lists_the_frozen_keys_and_no_others():
    g = _gates()
    page = (ROOT / "docs" / "ARTIFACT_HASHES_BROKEN.md").read_text(encoding="utf-8")
    keys = set(re.findall(r"^\| `([0-9a-f]{12})` \|", page, re.M))
    assert keys == set(g.ARTIFACT_HASHES_BROKEN) and len(keys) == 63
    # every entry of class A carries main's reading of 2026-11-11: what changed, whether it is disclosed, whether it bears on the result
    a = page[page.index("## A. "):page.index("## B. ")]
    rows = [l for l in a.splitlines() if re.match(r"^\| `[0-9a-f]{12}` \|", l)]
    assert len(rows) == 11 and all(len(l.strip("|").split(" | ")) == 7 for l in rows)
    assert sum(1 for l in rows if l.rstrip(" |").split(" | ")[-1].startswith("YES")) == 2
    state = g.artifact_hash_state()
    broken = {k for (k, _, _, st) in state if st != "VERIFIES"}
    assert broken <= set(g.ARTIFACT_HASHES_BROKEN)                       # nothing new is broken; the ceiling may only shrink
    assert len(g.ARTIFACT_HASHES_IMMUTABLE_FROM) == 40 and set(g.ARTIFACT_HASHES_IMMUTABLE_FROM) != {"0"}


def test_the_gate_is_registered_with_a_control_and_a_practice():
    g = _gates()
    assert "artifact-hashes" in g.GATES
    controls = json.loads((ROOT / "tests" / "GATE_CONTROLS.json").read_text(encoding="utf-8"))
    assert controls["artifact-hashes"].startswith("tests/test_artifact_hashes.py::")
    assert "`artifact-hashes`" in (ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8")
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("The repo sweep:", "no verdict on an arc", "The frozen keys are in the gate's own source", "| a rule committed after its record | open |"):
        assert s in f, s
