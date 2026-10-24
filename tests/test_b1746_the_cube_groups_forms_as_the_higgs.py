"""B1746 -- the cube group's forms as the Higgs (P-357), NEGATIVE for its question, the identities PROVED.  Live: the
weight-6 rho' x sgn form is DR's direction at one tau; the weight-2 rho' form is Y2 and is equivariant up to the parity
(with the planted contrast that it is not equivariant without it).  Stored: the counts against W136 and the pencils."""
import importlib.util, contextlib, io, json, pathlib, re, sys
import numpy as np
import mpmath as mp
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1746_the_cube_groups_forms_as_the_higgs"


def _cf():
    spec = importlib.util.spec_from_file_location("b1746_cf", A / "verification" / "cube_forms.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m


def test_weight_six_twisted_is_DR_live():
    cf = _cf(); ms, null = cf.equivariant(6, 0); t = complex(0.37, 2.4); v = cf.vt(t)
    w6 = np.linalg.svd(np.array([cf.ev(ms, c, v) for c in null]))[2][0]
    sys.path.insert(0, str(ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"))
    spec = importlib.util.spec_from_file_location("te", ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification" / "the_exponents.py")
    te = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
    DR = np.array([complex(te.ev(c, mp.mpc(t.real, t.imag))) for c in te.B[1]])
    assert 1 - abs(np.vdot(w6, DR)) / np.linalg.norm(w6) / np.linalg.norm(DR) < 1e-12


def test_y2_parity_live():
    cf = _cf(); rng = np.random.default_rng(1746); v = rng.normal(size=3) + 1j * rng.normal(size=3)
    Y2 = lambda u: np.array([u[1] * u[2], u[2] * u[0], u[0] * u[1]])
    assert max(np.abs(Y2(g @ v) - cf.PAR(g) * (g @ Y2(v))).max() for g in cf.G) < 1e-12
    assert max(np.abs(Y2(g @ v) - (g @ Y2(v))).max() for g in cf.G) > 1e-3          # planted: without the parity it fails


def test_stored():
    d = json.loads((A / "verification" / "cube_forms.json").read_text(encoding="utf-8"))
    dims = {(r["type"], r["weight"]): r["dimension on the null cone"] for r in d.values() if isinstance(r, dict) and "weight" in r}
    assert [dims[("rho'", w)] for w in (2, 4, 6, 8)] == [1, 1, 2, 2] and [dims[("rho' x sgn", w)] for w in (2, 4, 6, 8)] == [0, 1, 1, 2]
    assert all(v["1 - |cos(weight-6 rho' x sgn, DR)|"] < 1e-12 for v in d["identities"].values())
    run = (A / "verification" / "cube_pencils_run.txt").read_text(encoding="utf-8")
    mins = [float(m) for m in re.findall(r"min chi2_nine\s+([0-9.]+)", run)]
    assert len(mins) == 6 and min(mins) > 21.67 and all(l.rstrip().endswith("rows below 21.67: 0") for l in run.splitlines() if "min chi2_nine" in l)
