"""B1744 (P-324; data-free): the Higgs at its own hypercharge twist in B1656's frame.
(A) evenness: the frame's residue quaternion at the Higgs's twist, T0(z) = residues(twist_of(z), (0, 0), tau), equals T0(-z)
    (B1728's residues(-x, -y) = residues(x, y)), so the up sector's Higgs (6Y = +3) and the down quarks' and leptons' (6Y = -3)
    coincide; and its triplet part is the theta-square triplet (-th2(z)^2, -th4(z)^2, i th3(z)^2) up to a scalar.
(B) on the alpha = 2/5 lines (5w = 2 tau + k/2): 3w = -2w + k/2 mod the lattice, so the Higgs's twist is the down twist 2w
    (shifted by a half-period when k is odd), checked on the residues.
(C) the triplet's directions at the band against DR: delta, epsilon in rho(T)'s eigenframe and the invariant |h.h|/|h|^2,
    which equals |R_1|^2/|R|^2 because the quaternion is null (B1658's T0; the SM seat's W91): R_1^2 + R.R = 0.
(D) symbolic (sympy): B1736's closed form has det Y = (h0^2 + h.h)(w^2 + u.u)(h0 w + u.h) (h0 = 0: the web seat's
    (h.h)(u.h)(u.u + w^2), B1659's J1 in that form) and Y h = Y^T h = (h.h) u at h0 = 0 (the web seat's Lemma A).
    python3 -B the_twist.py      # writes the_twist.json"""
import sys, json, math, pathlib, contextlib, io
import numpy as np
import mpmath as mp
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import b1656_funcs as B      # noqa: E402
E1 = np.array([1, 0, 0], dtype=complex); N0 = np.array([0, 1, 1j]) / math.sqrt(2); N1 = np.array([0, 1, -1j]) / math.sqrt(2)


def quat(R): return np.array([R["1"], R["i"], R["j"], R["k"]])


def T0(z, t): return quat(B.residues(B.twist_of(z, t), (0.0, 0.0), t))


def theta_sq(z, t):
    T = mp.mpc(t.real, t.imag); Z = mp.mpc(z.real, z.imag)
    s2 = mp.fsum(mp.exp(1j * mp.pi * T * (n + mp.mpf(1) / 2) ** 2 + 2j * mp.pi * (n + mp.mpf(1) / 2) * Z) for n in range(-30, 30))
    s3 = mp.fsum(mp.exp(1j * mp.pi * T * n * n + 2j * mp.pi * n * Z) for n in range(-30, 31))
    s4 = mp.fsum((-1) ** n * mp.exp(1j * mp.pi * T * n * n + 2j * mp.pi * n * Z) for n in range(-30, 31))
    return np.array([-complex(s2) ** 2, -complex(s4) ** 2, 1j * complex(s3) ** 2])


def collinear(a, b): return float(np.linalg.norm(np.cross(a, b)) / np.linalg.norm(a) / np.linalg.norm(b))


def decompose(h):
    c1, c0, c0b = np.vdot(E1, h), np.vdot(N0, h), np.vdot(N1, h); lead, other = (c0, c0b) if abs(c0) >= abs(c0b) else (c0b, c0)
    return abs(c1 / lead), abs(other / lead), float(abs(h @ h) / np.vdot(h, h).real)


def part_A():
    rng = np.random.default_rng(1744); worst_even, worst_theta = 0.0, 0.0
    for _ in range(12):
        t = complex(rng.uniform(0, 1), rng.uniform(1.5, 3.5)); w = complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) * t.imag / 2
        a, b = T0(3 * w, t), T0(-3 * w, t)
        worst_even = max(worst_even, float(np.linalg.norm(a - b) / np.linalg.norm(a)))
        worst_theta = max(worst_theta, collinear(a[1:], theta_sq(3 * w, t)))
    return {"max |T0(3w) - T0(-3w)| / |T0|": worst_even, "max triplet vs theta squares (sine of angle)": worst_theta}


def part_B():
    out = []
    for k in range(10):
        for t in (complex(0.3, 2.2), complex(0.6, 3.0)):
            w = 0.4 * t + k / 10
            a, b = T0(3 * w, t), T0(2 * w + (k / 2 if k % 2 else 0), t)
            out.append(float(1 - abs(np.vdot(a, b)) / (np.linalg.norm(a) * np.linalg.norm(b))))
    return {"max 1 - |<T0(3w), T0(2w + k/2)>| / (|.||.|) over the ten lines (the same direction)": max(out)}


def part_C():
    from importlib import util
    spec = util.spec_from_file_location("te", ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification" / "the_exponents.py")
    sys.path.insert(0, str(ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"))
    te = util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
    rows = []
    for im_t in (2.1, 2.6, 3.0):
        for k in (1, 3, 6):
            t = complex(0.4375, im_t); w = 0.4 * t + k / 10; q = T0(3 * w, t); h = q[1:]
            d, e, inv = decompose(h)
            DR = np.array([complex(te.ev(c, mp.mpc(t.real, t.imag))) for c in te.B[1]])
            dD, eD, invD = decompose(DR)
            rows.append({"tau": [t.real, t.imag], "line": "(2/5, %d/10)" % k, "|delta|": round(d, 4), "|eps|": round(e, 4), "invariant": round(inv, 4),
                         "|R1|^2/|R_ijk|^2": round(float(abs(q[0]) ** 2 / np.vdot(h, h).real), 4), "null quaternion |R1^2 + R.R|/|R|^2": float(abs(q @ q) / np.vdot(q, q).real),
                         "DR |delta|, invariant": [round(dD, 4), round(invD, 4)]})
    return rows


def part_D():
    u1, u2, u3, w, h1, h2, h3, h0 = sp.symbols("u1 u2 u3 w h1 h2 h3 h0")
    u = sp.Matrix([u1, u2, u3]); h = sp.Matrix([h1, h2, h3])
    cross = lambda v: sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    dot = lambda a, b: (a.T * b)[0]
    Y = u * h.T + h * u.T - dot(u, h) * sp.eye(3) + w * cross(h); Yh0 = Y + h0 * (w * sp.eye(3) + cross(u))
    return {"det Y - (h.h)(u.h)(u.u + w^2)": str(sp.expand(Y.det() - dot(h, h) * dot(u, h) * (dot(u, u) + w ** 2))),
            "det Y(h0) - (h0^2 + h.h)(w^2 + u.u)(h0 w + u.h)": str(sp.expand(Yh0.det() - (h0 ** 2 + dot(h, h)) * (w ** 2 + dot(u, u)) * (h0 * w + dot(u, h)))),
            "Y h - (h.h) u": str(sp.simplify(Y * h - dot(h, h) * u).T), "Y^T h - (h.h) u": str(sp.simplify(Y.T * h - dot(h, h) * u).T)}


if __name__ == "__main__":
    res = {"A": part_A(), "B": part_B(), "C": part_C(), "D": part_D()}
    for k, v in res.items():
        if isinstance(v, list):
            for x in v: print(k, x)
        else: print(k, v)
    (HERE / "the_twist.json").write_text(json.dumps(res, indent=1) + "\n")
