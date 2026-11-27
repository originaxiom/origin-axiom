"""B2019's lock: Review 89's published plant list is the one sealed before the readers started, and the arc's tally
matches it."""
import hashlib, json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
SEAL = "5c5427cd44717178e642c3c97dbacc6081fba468328214490e5e5a813ed33d47"


def test_the_plant_list_is_the_sealed_one():
    assert hashlib.sha256((HERE / "plants.json").read_bytes()).hexdigest() == SEAL
    assert SEAL in (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")


def test_eight_plants_in_eight_files_six_caught():
    plants = json.loads((HERE / "plants.json").read_text(encoding="utf-8"))
    assert [p["key"] for p in plants] == ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2"]
    assert len({p["file"].split("/", 1)[1] for p in plants}) == 8
    text = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    rows = [l for l in text.splitlines() if re.match(r"\| [ABC][123] \|", l)]
    assert len(rows) == 8
    missed = [l.split("|")[1].strip() for l in rows if "**missed**" in l]
    assert missed == ["A3", "B2"] and "Six of eight caught" in text


def test_every_plant_differs_from_its_original():
    for p in json.loads((HERE / "plants.json").read_text(encoding="utf-8")):
        assert p["old"] != p["new"] and p["old"] and p["new"]
