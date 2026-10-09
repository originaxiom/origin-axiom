"""B1630 -- the sealed instrument unchanged and its run kept; the tick's axis through i not omega; S fixes the clock's line;
generic couplings at i give a pair and a single, never three distinct, the single on the clock's line."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1630_the_ticks_point"


def test_sealed_and_repaired():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 87d769c7a: ")
    assert hashlib.sha256(open(ARC / "verification" / "weave_at_i.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "weave_at_i.json"))
    assert d["Z0"]["i_on_axis_exact"] and not d["Z0"]["omega_on_axis_exact"]
    assert d["Z1"]["S_fixes_i"] and d["Z2"]["lines_fixed_by_S"] == [[-1, -1]] and d["Z4"]["S_order_on_T"] == 8
    g = json.load(open(ARC / "verification" / "post_seal_generic.json"))
    for t in ("Tbar_x_T", "T_x_T", "Sym2_T"):
        assert not g[t]["any_three_distinct"]
        for c in g[t]["cells"]:
            assert set(c["kinds"]) == {"pair + single"}
    for t in ("T_x_T", "Sym2_T"):
        assert all(set(c["single_lines"]) == {"(-1, -1)"} for c in g[t]["cells"])
