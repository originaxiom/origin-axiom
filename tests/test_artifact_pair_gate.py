"""A cell's two committed artifacts must not contradict each other.

Locks `scripts/checks/artifact_pair_gate.py`. Three things are asserted:

  1. the gate is GREEN at HEAD;
  2. its own bite control passes (the detector can fire and can stay quiet);
  3. a HISTORICAL REGRESSION: the three real contradictions found on 2026-09-12 -- the
     verdict pairs are transcribed below from the artifacts as they stood at the commit
     before their repair -- still make the detector fire. Without (3) this lock would go
     vacuous the moment the corpus is clean, which is exactly when it stops being watched.
"""
import importlib.util
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
GATE = ROOT / "scripts" / "checks" / "artifact_pair_gate.py"


def _load():
    spec = importlib.util.spec_from_file_location("artifact_pair_gate", GATE)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _run(*a):
    return subprocess.run([sys.executable, str(GATE), *a],
                          capture_output=True, text=True, cwd=str(ROOT))


def test_gate_is_green_at_head():
    r = _run()
    assert r.returncode == 0, r.stdout + r.stderr
    assert "artifact-pair-gate: ok" in r.stdout


def test_bite_control_passes():
    r = _run("--selftest")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "selftest: PASS" in r.stdout


# (text verdict, json verdicts) exactly as the three cells stood before their 2026-09-12
# regeneration.  Provenance: memo 212 / memo 216, outside-bench branch.
HISTORICAL = [
    ("P2W5-L72", "RESOLVED-A", ["UNRESOLVED"]),       # the JSON was stale (h1 = 0 everywhere)
    ("W2-270", "UNRESOLVED", ["RESOLVED-B"]),         # the TEXT was stale -- the other direction
    ("W4-017r", "RESOLVED-A", ["PENDING_PART_B"]),    # the JSON was a mid-run snapshot
]


def test_historical_contradictions_still_fire():
    g = _load()
    for name, txt, js in HISTORICAL:
        assert g.is_mismatch(txt, js), f"{name}: the gate no longer detects a real contradiction"


def test_agreement_and_one_sided_pairs_do_not_fire():
    g = _load()
    assert not g.is_mismatch("RESOLVED-A", ["RESOLVED-A"])
    assert not g.is_mismatch("HARDENS", ["HARDENS", "other"])   # nested/extra verdicts are fine
    assert not g.is_mismatch("RESOLVED-A", [])                  # one-sided: a gap, not a lie
    assert not g.is_mismatch(None, ["RESOLVED-A"])


def test_the_three_printed_verdict_shapes_parse():
    g = _load()
    assert g.text_verdict("=== VERDICT ===\nVERDICT: RESOLVED-A\n") == "RESOLVED-A"
    assert g.text_verdict("[   860.0s]   FINAL VERDICT: RESOLVED-B\n") == "RESOLVED-B"
    assert g.text_verdict("VERDICT: UNRESOLVED (=> EXTERNAL).\n") == "UNRESOLVED"
    assert g.text_verdict("nothing here\n") is None
