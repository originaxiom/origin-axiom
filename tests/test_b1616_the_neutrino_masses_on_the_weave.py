"""B1616 -- THE NEUTRINO MASSES ON THE WEAVE: the sealed instrument unchanged; no RRL vacuum; rigid spectra; GENESIS carries
the owner's rulings as relayed."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1616_the_neutrino_masses_on_the_weave"


def test_sealed_and_recorded():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 08b7f328f: ")
    assert hashlib.sha256(open(ARC / "verification" / "neutrino_masses_on_the_weave.py", "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(ARC / "verification" / "neutrino_masses_on_the_weave.json"))
    assert d["N1"]["Sym2_pieces_dims"] == [1, 2, 3]
    assert all(rows["RRL"]["fixed_dim"] == 0 for rows in d["N2"].values())
    for rows in d["N2"].values():
        for g, r in rows.items():
            if r["fixed_dim"]:
                assert abs(r["m1_m3_range"][0] - r["m1_m3_range"][1]) < 1e-9 and (r["relations"]["m1 = m2"] or r["relations"]["m2 = m3"])


def test_genesis_carries_the_rulings():
    g = open(ROOT / "GENESIS.md", encoding="utf-8").read()
    assert int(g.split("**Version 1.")[1].split()[0]) >= 33 and "THE OWNER'S RULINGS OF 2026-10-08" in g and "even ticks observed" in g
