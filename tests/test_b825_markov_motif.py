"""B825 — locks the motif that closed the last known lexicon gap, and its stated limits."""
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location("atlas", ROOT / "scripts" / "atlas" / "atlas.py")
atlas = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(atlas)


def _probes():
    return json.loads((ROOT / "scripts" / "atlas" / "atlas_data.json").read_text(
        encoding="utf-8"))["probes"]


def test_the_motif_exists_and_hits_its_target():
    assert "markov_cubic" in atlas.LEXICON
    assert "markov_cubic" in (_probes().get("B537", {}).get("motifs") or []), (
        "B537 was the single genuine gap; the motif exists to cover it")


def test_it_stays_inside_its_sealed_vacuity_ceiling():
    p = _probes()
    n = sum(1 for v in p.values() if "markov_cubic" in (v.get("motifs") or []))
    assert n / len(p) <= 0.15, f"matched {n}/{len(p)} -- the sealed ceiling was 15%"


def test_it_does_NOT_carry_the_ambient_term():
    """'character variety' measured 13.8% alone -- the programme's subject, not a topic."""
    pats = " ".join(atlas.LEXICON["markov_cubic"]["patterns"])
    assert "character variety" not in pats.lower(), (
        "the ambient term was what killed B824; it must not come back")


def test_it_is_not_redundant_with_an_existing_motif():
    p = _probes()
    mine = {k for k, v in p.items() if "markov_cubic" in (v.get("motifs") or [])}
    others = {}
    for k, v in p.items():
        for m in (v.get("motifs") or []):
            if m != "markov_cubic":
                others.setdefault(m, set()).add(k)
    worst = max(len(mine & s) / len(mine) for s in others.values())
    assert worst < 0.90, f"{worst:.1%} contained in one existing motif -- that is a relabel"


def test_zero_gaps_is_not_claimed_as_completeness():
    reg = (ROOT / "docs" / "atlas" / "BLIND_ARCS.md").read_text(encoding="utf-8")
    assert "NOT" in reg and "lexicon is complete" in reg, (
        "an empty GAP column must not read as a finished instrument")
    assert "false-positive mode" in reg, "the mentions-not-subjects limitation must be stated"
