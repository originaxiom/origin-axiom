"""B1744 -- the Higgs's own twist (P-324), NEGATIVE for its question, the data-free parts PROVED.  Live: the evenness of
the residue quaternion in the twist (H_u = H_d), with a planted contrast (the odd theta_1 is not even); the null
quaternion; the four-dimensional determinant (sympy).  Stored: the twisted Higgs's data look below no bar."""
import contextlib, io, json, pathlib, re, sys
import numpy as np
import sympy as sp
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1744_the_higgs_own_twist"
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import b1656_funcs as B      # noqa: E402


def _q(z, t):
    R = B.residues(B.twist_of(z, t), (0.0, 0.0), t); return np.array([R["1"], R["i"], R["j"], R["k"]])


def test_even_in_the_twist_and_null_live():
    for t, w in ((complex(0.4375, 2.1), complex(0.4375, 2.1) * 0.4 + 0.1), (complex(0.2, 2.9), complex(0.3, 0.7))):
        a, b = _q(3 * w, t), _q(-3 * w, t)
        assert np.linalg.norm(a - b) < 1e-12 * np.linalg.norm(a)
        assert abs(a @ a) < 1e-12 * np.vdot(a, a).real
    t = complex(0.3, 1.2); th1 = lambda z: B.th_mp(1, z, t)                      # planted: theta_1 is odd, not even
    assert abs(complex(th1(0.17 + 0.05j)) + complex(th1(-0.17 - 0.05j))) < 1e-12 and abs(complex(th1(0.17 + 0.05j))) > 1e-3


def test_determinant_four_dimensional():
    u1, u2, u3, w, h1, h2, h3, h0 = sp.symbols("u1 u2 u3 w h1 h2 h3 h0")
    u = sp.Matrix([u1, u2, u3]); h = sp.Matrix([h1, h2, h3])
    cross = lambda v: sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]]); dot = lambda a, b: (a.T * b)[0]
    Y = u * h.T + h * u.T - dot(u, h) * sp.eye(3) + w * cross(h) + h0 * (w * sp.eye(3) + cross(u))
    assert sp.expand(Y.det() - (h0 ** 2 + dot(h, h)) * (w ** 2 + dot(u, u)) * (h0 * w + dot(u, h))) == 0


def test_stored():
    d = json.loads((A / "verification" / "the_twist.json").read_text(encoding="utf-8"))
    assert all(abs(r["invariant"] - r["|R1|^2/|R_ijk|^2"]) < 1e-3 and r["invariant"] > 0.05 for r in d["C"])
    run = (A / "verification" / "twisted_higgs_run.txt").read_text(encoding="utf-8")
    mins = [float(m) for m in re.findall(r"min chi2_nine\s+([0-9.]+)", run)]
    assert len(mins) == 6 and min(mins) > 400 and all("nine < 21.67: 0, six < 16.75: 0" in l for l in run.splitlines() if "min chi2_nine" in l)
