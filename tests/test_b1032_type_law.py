"""B1032 locks — the type law (the resolution bound verified as amended)."""
import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1032_type_law"


def _cells():
    spec = importlib.util.spec_from_file_location("b1032_typecheck", ARC / "b1032_typecheck.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_v1_v2_menus():
    m = _cells()
    assert all(m.v1_tones_are_bare_character_values().values())
    assert all(m.v2_mirror_is_the_tensor_menu().values())
    # independent: the census total must be |2I| = 120 classes-weighted
    assert sum(sz for _, sz, _ in m.CLASSES_2I) == 120
    assert sum(sz for _, sz, _ in m.CLASSES_2T) == 24


def test_v3_amendment_exact():
    m = _cells()
    assert all(m.v3_family_needs_the_amendment().values())
    # re-derive: sqrt5 = phi + 1/phi and the pair sums to 1
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(phi + 1/phi - sp.sqrt(5)) == 0
    assert sp.simplify((1 - 1/sp.sqrt(5))/2 + (1 + 1/sp.sqrt(5))/2 - 1) == 0


def test_findings_carry_the_law_and_the_honest_typing():
    flat = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8")
                    .replace("**", "").replace("−", "-").replace("∓", "-+").split())
    assert "FINITE LABEL" in flat and "RELATION" in flat
    assert "may NOT target a generic real by value" in flat
    # the amendment is load-bearing (verify-don't-trust produced it):
    assert "character ring" in flat.lower() or "character-ring" in flat.lower()
    # the honest correction of the relay's overreach:
    assert "TYPE-PERMITTED" in flat
    assert "correcting the relay" in flat
    # the fences:
    assert "c = 6" in flat and "outside" in flat
    # quarantine honored, stated:
    assert "unopened" in flat


def test_verdict_and_terminology():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1032" and v["verdict"] == "PROVED"
    assert "FINITE ALGEBRAIC MENU" in v["claim_one_line"]
    for dep in ("B1011", "B915", "B1027", "B659"):
        assert dep in v["depends_on"]
    t = " ".join((ROOT / "TERMINOLOGY.md").read_text(encoding="utf-8")
                 .replace("**", "").split())
    assert "names TWO banked objects" in t
    assert "value-set registry" in t.lower() or "The value-set registry" in t
