"""B1127 lock -- V-2' the antilinear completion: compact color reachable in M(O,C) via a
second-level conjugation (sigma_mirror color I2 = (0,8)), specific 4/48, controls green;
the framing fenced (object's arithmetic mirror trivial on the color layer; observer's tau)."""
import json
from pathlib import Path
ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1127_antilinear_completion"


def test_math_compact_reachable_and_specific():
    r = json.loads((ARC / "b1127_results.json").read_text(encoding="utf-8"))
    blob = json.dumps(r)
    # sigma_c control: the detector sees compact color when present
    assert r["layer6_sigma_c_control"]["color_I2_compact"] is True
    assert r["layer6_sigma_c_control"]["color_I2_signature"] == [0, 8, 0]
    # sigma_mirror: color I2 compact (0,8)
    assert r["layer7_sigma_mirror_primary"]["color_I2_signature"] == [0, 8, 0]
    # specific, not generic: exactly 4 of 48 torsor elements
    assert r["n_torsor_compact_hits_reverified"] == 4
    # secondary construction is NON-compact (not 'any antilinear map compactifies')
    assert r["layer8b_secondary_compact_referenced_construction"]["color_I2_antilinear_signature"] == [5, 3, 0]


def test_framing_fence_object_mirror_is_trivial():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    # the load-bearing fence: object's own Galois mirror acts trivially; tau is generic/observer's
    assert "acts as the identity on the color layer" in f
    assert "OBSERVER'S archimedean closing" in f
    assert "over-reads its own" in f          # the agent's headline is corrected, not adopted
    assert "relayed to cc3" in f              # the open bridge routed for the 3rd opinion
    assert "M(𝕆,ℂ)" in f                       # the compact form is the object's own algebra
