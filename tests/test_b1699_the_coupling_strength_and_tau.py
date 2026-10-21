"""B1699 -- the coupling's strength and tau (P-247), sealed 8ac889d14, NEGATIVE as sealed. Live: the strength's invariance
at one point and the arc saddle's kind; the comparison re-run from the stored rows and the pinned data reproduces H1, H2,
H3 failing. Stored: S0 (no interior critical point, monotone on the symmetry lines); the seal's hashes."""
import hashlib, importlib.util, io, contextlib, json, math, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1699_the_coupling_strength_and_tau"


def _load(name, mod):
    spec = importlib.util.spec_from_file_location(mod, A / "verification" / name)
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def test_the_strength_live():
    s = _load("the_strength.py", "b1699_strength")
    t = complex(0.13, 1.37)
    a, b = s.top_DR(t), s.top_DR(-1 / t)
    assert abs(a / b - 1) < 1e-12
    th = json.loads((A / "verification" / "the_strength.json").read_text(encoding="utf-8"))["selected"]["theta_over_pi"] * math.pi
    assert s.dS_dtheta(th - 0.01) > 0 > s.dS_dtheta(th + 0.01)                     # a maximum along the arc ...
    z = s.on_arc(th)
    assert s.top_DR(z * 1.01) > s.top_DR(z)                                         # ... rising outward: a saddle


def test_s0_stored():
    d = json.loads((A / "verification" / "the_strength.json").read_text(encoding="utf-8"))
    assert d["invariance_max_rel_dev"] < 1e-12 and d["grid"]["DR"]["dS_dy_nonpositive_at"] == []
    assert all(v["monotone_increasing"] and not v["critical_y"] for v in d["symmetry_lines"].values())
    assert d["selected"]["kind"] == "saddle" and abs(d["selected"]["tau"][1] - 0.9613) < 1e-3


def test_the_cells_live():
    o = _load("compare.py", "b1699_compare").out
    assert not o["H1_within_factor_3"] and not o["H2_specific_p_below_0.01"] and not o["H3_chi2_below_16.75"]
    assert abs(o["best_by_worst_factor"]["worst_factor"] - 224.57) < 0.1
    assert min(o["smallest_model_ratio_over_all_rows"][k] for k in ("up m2/m3", "down m2/m3", "lep m2/m3")) > 0.3


def test_the_seal():
    for name in ("the_strength.py", "the_selected_tau.py", "compare.py", "b1656_funcs.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("317b4d67")
