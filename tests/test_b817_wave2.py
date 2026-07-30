"""B817 — locks wave 2's gate, its scope limit, and writer safety.

The scope-limit lock is the important one: it is the flaw this run FOUND IN ITSELF, and a lock
is what stops it from quietly becoming untrue-but-unnoticed later.
"""
import importlib.util
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B817_verdict_wave2"

_SPEC = importlib.util.spec_from_file_location(
    "fleiss_kappa", ROOT / "scripts" / "checks" / "fleiss_kappa.py")
fk = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(fk)


def _ratings():
    return json.loads((ARC / "calibration_ratings.json").read_text(encoding="utf-8"))


def test_the_calibration_block_is_complete_12x15():
    """Fleiss' kappa needs every item rated by every rater; a gap would void the statistic."""
    r = _ratings()
    assert len(r) == 15
    assert {len(v) for v in r.values()} == {12}


def test_kappa_clears_the_sealed_gate():
    table, cats, _ = fk.table_from_ratings(_ratings())
    k, _, _, _, _ = fk.fleiss_kappa(table)
    assert k >= 0.75, f"sealed gate is 0.75; got {k}"
    assert abs(k - 0.9312) < 0.001, f"recorded kappa is 0.9312; got {k}"


def test_the_gate_was_measured_on_only_TWO_categories():
    """The flaw this run caught in itself, locked so it cannot be forgotten.

    kappa was computed on a PROVED/NEGATIVE block and then used to license work that also used
    OPEN and RETRACTED. If a future edit adds categories to this block, this lock fails and the
    scope note in FINDINGS must be revisited -- which is exactly what should happen.
    """
    used = {v for m in _ratings().values() for v in m.values()}
    assert used == {"PROVED", "NEGATIVE"}, (
        f"the calibration block exercised {used}; FINDINGS section 3 documents it as exactly "
        f"two categories and scopes the result on that basis")


def test_the_scope_limit_is_stated_in_findings():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "only two of the four verdict categories" in f
    assert "13.1 %" in f and "3.7 %" in f


def test_the_marginal_flag_is_applied_per_the_pre_committed_rule():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "PASS (marginal)" in f
    assert "0.7485" in f, "the CI lower bound that triggers the flag must be shown"


def test_the_conservatism_offset_is_measured_not_asserted():
    """10 of 12 readers gave the identical 5:10 mix -- the fact that resolves wave 1's confound."""
    per = fk.per_rater_distribution(_ratings())
    mixes = Counter((c["NEGATIVE"], c["PROVED"]) for c in per.values())
    assert mixes[(5, 10)] == 10, f"expected 10 readers at 5:10, got {dict(mixes)}"
    assert len(per) == 12


def test_writer_safety_no_verdict_without_findings():
    """Every authored verdict must sit beside an actual FINDINGS.md -- no verdicts on empty arcs."""
    bad = [p.parent.name for p in (ROOT / "frontier").glob("*/arc_verdict.json")
           if not (p.parent / "FINDINGS.md").is_file()]
    assert not bad, f"verdicts written for arcs with no FINDINGS.md: {bad[:10]}"


def test_every_written_verdict_uses_the_sealed_vocabulary():
    vocab = {"PROVED", "NEGATIVE", "OPEN", "RETRACTED", "PARTIAL"}
    bad = []
    for p in (ROOT / "frontier").glob("*/arc_verdict.json"):
        v = json.loads(p.read_text(encoding="utf-8")).get("verdict")
        if v not in vocab:
            bad.append((p.parent.name, v))
    assert not bad, f"out-of-vocabulary verdicts: {bad[:10]}"
