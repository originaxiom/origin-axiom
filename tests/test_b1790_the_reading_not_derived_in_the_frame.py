"""B1790 -- the reading is not derived in B1656's frame.  Seven maps of (tau, w) on record preserve both readings at every
committed point (the half-periods do not); a search over all 266 lines finds no partner for the flipped assignment while the
unflipped control finds the source exactly."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1790_the_reading_not_derived_in_the_frame" / "verification" / "referee"
SYMMETRIES = ("mirror (1-conj tau, a, -a-b)", "pure conj (-conj tau, a, -b)", "charge conj w->-w (tau, -a, -b)",
              "mirror o C: w-> conj w (1-conj tau, -a, a+b)", "T (tau+1, a, b-a)", "w->w+1 (tau, a, b+1)", "w->w+tau (tau, a+1, b)")


def test_every_map_on_record_preserves_both_readings():
    pts = json.loads((V / "maps.json").read_text(encoding="utf-8"))
    assert len(pts) == 6
    for p in pts:
        for m in SYMMETRIES:
            assert p[m]["preserve_worst"] < 1e-10, (p["p"], m)
        for m in ("w->w+1/2", "w->w+tau/2", "w->w+(1+tau)/2"):
            assert p[m]["preserve_worst"] > 0.1, (p["p"], m)        # the half-periods are not symmetries (true ones sit at 1e-12)


def test_no_line_is_a_flip_partner():
    f = json.loads((V / "flip_search.json").read_text(encoding="utf-8"))
    assert len(f) == 4
    for src, r in f.items():
        assert min(x[0] for x in r["flip: 3 best (max-sector ln dev, line)"]) > 1.5, src
        assert r["control unflipped: 3 best"][0][0] < 1e-9, src
