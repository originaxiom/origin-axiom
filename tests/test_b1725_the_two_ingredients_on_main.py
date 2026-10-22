"""B1725 -- the two ingredients on main (P-293), PROVED (a verification arc). Live: the received census's sha256 and
size; two of its points recomputed with main's frame in the arc's loop; the sealed configuration's best six and nine
re-derived from the census. Stored: the 48-point reproduction and the recalibration's menus."""
import hashlib, json, math, pathlib, importlib.util
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1725_the_two_ingredients_on_main"


def _load(name):
    spec = importlib.util.spec_from_file_location("b1725_" + name, A / "verification" / (name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_received_census():
    b = (A / "received" / "two_ingredients_census.jsonl").read_bytes()
    assert hashlib.sha256(b).hexdigest() == "f379a4b8cfe2966d9d067abff323f6f654560d589c1d55f55320d816d59c5c4b"
    assert sum(1 for l in b.decode("utf-8").splitlines() if l.strip()) == 8512


def test_two_points_live():
    m = _load("reproduce")
    rows = [json.loads(l) for l in m.CENSUS.read_text(encoding="utf-8").splitlines() if l.strip()]
    L = m.lines()
    for i in (0, 4321):
        r = rows[i]; dl, dj, keys = m.compare(r, m.compute(r["Re_tau"], r["Im_tau"], *L[r["line"]]))
        assert keys == 36 and dl < 1e-9 and dj < 1e-12


def test_the_sealed_numbers_live():
    m = _load("recalibrate")
    data = m.menus(m.arrays()["T6"]); data9 = m.menus(m.arrays()["T9"])
    assert abs(math.exp(data["sealed"]) - 1.513) < 0.001 and abs(math.exp(data9["sealed"]) - 2.087) < 0.001
    assert abs(math.exp(data["seat_menu"]) - 1.270) < 0.001 and abs(math.exp(data["cov_read"]) - 1.270) < 0.001


def test_the_stored_results():
    r = json.loads((A / "verification" / "reproduce.json").read_text(encoding="utf-8"))
    assert r["n"] == 48 and r["reproduced_to_1e-9"] and r["keys_per_point"] == 36
    s = json.loads((A / "verification" / "recalibrate.json").read_text(encoding="utf-8"))["summary"]
    assert abs(s["six|sealed"]["seed_1720"] - 0.00725) < 1e-9 and abs(s["nine|sealed"]["seed_1720"] - 0.00475) < 1e-9
    assert s["six|seat_menu"]["seeds_at_or_below_1pct"] == 20 and s["six|c_free"]["seeds_at_or_below_1pct"] == 20
    assert 0.009 < s["six|cov_read"]["mean_100_119"] < 0.011 and s["six|cov_read"]["seeds_at_or_below_1pct"] == 14
    assert s["nine|c_free"]["seeds_at_or_below_1pct"] == 0 and s["nine|cov_read"]["seeds_at_or_below_1pct"] == 0
