"""B1975's lock: the plant list committed here is the one sealed before reading (its sha256), it holds seven plants in
seven arcs, and the window's two mend computations are present with the results the entry states."""
import pathlib, hashlib, json
HERE = pathlib.Path(__file__).resolve().parent
FR = HERE.parents[1]


def test_plants_sealed():
    b = (HERE / "plants.json").read_bytes()
    assert hashlib.sha256(b).hexdigest() == "b448cab25ac73ae6f70d910bd503a1d9c0011e719a9f99674e84ce4b2d5dd232"
    p = json.loads(b); assert len(p) == 7 and len({x["arc"] for x in p}) == 7 and "B1964" not in {x["arc"] for x in p}


def test_mends_present():
    m10 = next(FR.glob("B1971_*")) / "verification" / "missing_order10_run.txt"
    t = m10.read_text(); assert t.count("NOT aligned") == 4 and t.count("| aligned") == 4
    d4 = (next(FR.glob("B1970_*")) / "verification" / "d4_coupling_run.txt").read_text()
    assert "reading S :" in d4 and "reading St:" in d4
    s = float(d4.split("reading S :")[1].split("to")[1].split()[0]); st = float(d4.split("reading St:")[1].split("from")[1].split()[0])
    assert s < 1e-20 and st > 0.5
