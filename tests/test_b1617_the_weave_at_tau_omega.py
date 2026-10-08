"""B1617 -- THE WEAVE AT TAU = OMEGA: the sealed instrument unchanged; the residual group and T as recorded; GENESIS carries
the owner's ruling."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1617_the_weave_at_tau_omega"


def test_sealed_and_recorded():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at da3027e03: ")
    assert hashlib.sha256(open(ARC / "verification" / "weave_at_omega.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "weave_at_omega.json"))
    assert d["Z0"]["U_fixes_omega"]["action_by_matrix"] and d["Z1"]["order"] == 48 and d["Z1"]["preserves_T"]
    assert d["Z2"]["T_commutant_under_residual"] == 1
    assert d["Z3"]["Dirac T-bar(x)T"]["fixed_dim"] == 1 and d["Z3"]["Majorana Sym2 T"]["fixed_dim"] == 0
    assert d["Z4"]["U_order_on_T"] == 12 and len(set(d["Z4"]["U_eigen_turns_on_T"])) == 3


def test_genesis_carries_the_modulus_ruling():
    g = open(ROOT / "GENESIS.md", encoding="utf-8").read()
    assert int(g.split("**Version 1.")[1].split()[0]) >= 34 and "A TAGGED WORKING POSTULATE (the owner's ruling of 2026-10-08, made with main)" in g
