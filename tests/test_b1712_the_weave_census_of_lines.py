"""B1712 -- the weave census of lines (P-260), sealed a35ab5642, NEGATIVE as sealed. Live: the comparison re-run from the
stored rows and the pinned data reproduces H1 holding and H2, H3 failing; the order-12 lepton zero read from the stored
rows. Stored: the seal's hashes."""
import hashlib, importlib.util, io, contextlib, json, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1712_the_weave_census_of_lines"


def test_the_cells_live():
    spec = importlib.util.spec_from_file_location("b1712_compare", A / "verification" / "compare.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    o = m.out
    assert o["H1_within_factor_3"] and not o["H2_specific_p_below_0.01"] and not o["H3_chi2_below_16.75"]
    assert abs(o["best_by_worst_factor"]["worst_factor"] - 2.3685) < 0.001 and abs(o["calibration"]["fraction_fit_as_well"] - 0.2245) < 1e-9
    assert o["best_by_worst_factor"]["line"] == ["N=8", "3/8", "0"] and o["rows"] == 51408


def test_the_order12_lepton_zero():
    G = json.loads((A / "verification" / "the_line_census_masses.json").read_text(encoding="utf-8"))
    lep = {}                                   # per line: the largest lepton m1/m3 over the grid
    for r in G["rows"]:
        for k, v in r.items():
            if k.startswith("lep|"):
                lep[r["line"]] = max(lep.get(r["line"], 0.0), v[1])
    for k, m1 in lep.items():
        if G["lines"][k][0] == "N=12":
            assert m1 < 1e-13
        else:
            assert m1 > 1e-12


def test_the_seal():
    for name in ("the_line_census_masses.py", "compare.py", "b1656_funcs.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("c4856e37")
