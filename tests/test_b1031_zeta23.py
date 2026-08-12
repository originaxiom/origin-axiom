"""B1031 locks — the two-thirds theorem meets the voice (scrutiny + corollary)."""
import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1031_two_thirds_meets_the_voice"


def _cells():
    spec = importlib.util.spec_from_file_location("b1031_verify", ARC / "b1031_verify.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_v1_ideal_count_identity():
    m = _cells()
    r = m.v1_ideal_count_identity(N=1500)   # smaller N in-suite; the arc ran 3000
    assert all(r.values()), r
    # independent spot facts: r(1)=1, r(3)=1 (ramified), r(7)=2 (split), r(2)=0 (inert)
    import math
    for n, expect in ((1, 1), (3, 1), (7, 2), (2, 0), (4, 1), (13, 2)):
        cnt = sum(1 for x in range(-8, 9) for y in range(-8, 9)
                  if x * x + x * y + y * y == n)
        assert cnt // 6 == expect == sum(m.chi3(d) for d in sp.divisors(n))


def test_v2_v3():
    m = _cells()
    assert all(m.v2_union_arithmetic().values())
    assert all(m.v3_multiplicity_fence().values())


def test_findings_carry_provenance_fence_and_limits():
    flat = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8")
                    .replace("**", "").replace("−", "-").split())
    # provenance is load-bearing for an external-literature arc:
    assert "Fetched 2026-08-11" in flat and "3635e748" in flat
    assert "zeta-23-lean" in flat
    # the load-bearing word (the adversarial pass's flag): NUMERATOR must survive
    # every future compression -- "the VOICE's zeros" would be FALSE (denominator poles):
    assert "numerator zeros" in flat.lower()
    # the corollary with its exact hedges:
    assert "WITH multiplicity" in flat and "unconditionally" in flat
    assert "do NOT transfer" in flat
    # the imported walls (nobody retries naively):
    assert "degree-one method" in flat
    assert "RH itself is out of reach of the mechanism" in flat
    # the crux stays: the zeta is the field's
    assert "the field's, not the object's" in flat
    # the numerics lesson recorded:
    assert "Hurwitz" in flat


def test_verdict_json_and_k027():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1031" and v["verdict"] == "PROVED"
    assert "WITH MULTIPLICITY" in v["claim_one_line"]
    assert "B737" in v["depends_on"]
    k = " ".join((ROOT / "knowledge" / "K027_the_convergent_protocol.md")
                 .read_text(encoding="utf-8").replace("**", "").split())
    assert "convergence" in k and "vacuity controls" in k
    assert "B1031" in k
