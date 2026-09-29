"""B1502 section 5 -- THE CUBIC INFLOW: Witten's SU(N)^3 inflow at the apex of B1501's two torus models, checked with own code.

Witten (hep-th/0108165, section 3, (3.5)-(3.8)): on an A_{N-1} locus B the normal space is twisted by Lambda' = U(1), the centraliser
of Gamma = Z_N in the SU(2) containing it; the invariants x = a^N, y = b^N are sections of L, L^-1 for a line bundle L over B, and the
interaction  int_B K/2pi ^ omega_5(A)  (K the curvature of L) forces, at a point P where the normal singularity is worse, charged
chiral fields with SU(N)^3 anomaly n_P = c_1(L restricted to a small surface wrapping P in Q).  At a cusp point that surface is the
torus link F, so the cubic half of the anomaly criterion asks for deg(L|_F).

On F the normal bundle nu, with the complex structure in which d gamma acts as the scalar zeta = e^{2 pi i k/N}, is E_zeta, the
zeta-eigenbundle of d gamma on nu (x) C, a U(2) = (SU(2) x U(1)_Gamma)/Z_2 bundle with det E_zeta = L^{2/N}; so deg L = (N/2) c_1(E_zeta).

(1) c_1(E_zeta) over F for every torus class of the census of order >= 3 (22 on S3 x S3, 2 on F12): E_zeta(q) is carried into the
    ambient space of the link's embedding (so the frame is global), and c_1 is the lattice Chern number of Fukui-Hatsugai-Suzuki on a
    grid of the torus that sweeps F (the acting torus: T^3 / U(1)_diag on S3 x S3, simply; the maximal torus of SU(3) on F12, which
    covers F |Z(SU(3))| = 3 times).  Two grids.
(2) The reason (theorem): the torus acting on F commutes with gamma, so L is a homogeneous line bundle over a torus; every character of
    a closed subgroup of a torus extends to the torus, so L is trivial.  Checked: the acting torus commutes with gamma and preserves F.
(3) Positive control: the same lattice routine gives the Qi-Wu-Zhang lower band's Chern numbers (+-1 for 0 < |m| < 2, 0 for |m| > 2).
"""
import importlib.util
import json
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location(
    "b1501_census", ROOT / "frontier" / "B1501_the_torus_link_census" / "verification" / "torus_link_census.py")
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)

GRIDS = (16, 28)


# ------------------------------------------------------------------------------------------------------------ the lattice routine
def lattice_chern(frames):
    """Fukui-Hatsugai-Suzuki: frames[i][j] an orthonormal (D x r) frame of the subbundle at grid point (i, j) of a periodic grid"""
    n1, n2 = len(frames), len(frames[0])

    def link(A, B):
        d = np.linalg.det(A.conj().T @ B)
        return d / abs(d)
    total = 0.0
    worst_overlap = 1.0
    for i in range(n1):
        for j in range(n2):
            a, b = frames[i][j], frames[(i + 1) % n1][j]
            c, d = frames[(i + 1) % n1][(j + 1) % n2], frames[i][(j + 1) % n2]
            u1, u2, u3, u4 = link(a, b), link(b, c), link(d, c), link(a, d)
            worst_overlap = min(worst_overlap, *(abs(np.linalg.det(X.conj().T @ Y)) for X, Y in ((a, b), (b, c), (d, c), (a, d))))
            total += np.angle(u1 * u2 / u3 / u4)
    return total / (2 * np.pi), worst_overlap


def qwz_frames(m, n):
    """the Qi-Wu-Zhang model's lower band on an n x n grid of the Brillouin torus"""
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]])
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    out = []
    for i in range(n):
        row = []
        for j in range(n):
            kx, ky = 2 * np.pi * i / n, 2 * np.pi * j / n
            H = np.sin(kx) * sx + np.sin(ky) * sy + (m + np.cos(kx) + np.cos(ky)) * sz
            w, v = np.linalg.eigh(H)
            row.append(v[:, :1])
        out.append(row)
    return out


# ------------------------------------------------------------------------------------------------------------- the eigenbundle
def eigenframe(link, gam, g, zeta):
    """E_zeta at the fixed point gK: the zeta-eigenspace of d gamma on m (x) C, pushed into the embedding's ambient space (x) C,
    orthonormalised; also the +1-eigenspace dimension (the tangent space of F) and the eigenvalue residual"""
    D = link.differential(gam, g)
    w, V = np.linalg.eig(D)
    sel = [i for i in range(6) if abs(w[i] - zeta) < 1e-6]
    ones = sum(1 for i in range(6) if abs(w[i] - 1) < 1e-6)
    cols = []
    for i in sel:
        c = V[:, i]
        Yr = T.from_coords(c.real, link.m_basis)
        Yi = T.from_coords(c.imag, link.m_basis)
        cols.append(link.dembed(g, Yr) + 1j * link.dembed(g, Yi))
    A = np.array(cols).T
    Q, _ = np.linalg.qr(A)
    return Q, len(sel), ones


def normal_eigenvalue(link, gam, g):
    """the eigenvalue zeta of d gamma on the normal space with 0 < arg zeta <= pi (constant along F)"""
    w = np.linalg.eigvals(link.differential(gam, g))
    nz = [x for x in w if abs(x - 1) > 1e-6]
    return sorted(nz, key=lambda x: (0 if x.imag > 1e-9 else 1, float(np.angle(x))))[0], nz


def s3xs3_setup(x):
    link = T.S3xS3()
    gam = ("left", link.torus((x, x, x)))
    g0 = np.eye(6, dtype=complex)

    def point(a, b):
        s = T.blockdiag3(np.diag([np.exp(1j * a), np.exp(-1j * a)]), np.diag([np.exp(1j * b), np.exp(-1j * b)]), np.eye(2))
        return s @ g0
    return link, gam, point, 1                      # T^3 / U(1)_diag acts simply on F: the (a, b) grid sweeps F once


def f12_setup(outer):
    link = T.F12()
    t = link.torus((Fraction(0), Fraction(1, 3)))  # diag(1, w, w^2)
    n = link.outer[outer]
    gam = ("right", t, n)
    # a fixed point g0 with g0^-1 t g0 = n^-1 (n^-1 has the eigenvalues 1, w, w^2 of t): t g0 n = g0
    w, V = np.linalg.eig(np.linalg.inv(n))
    order = [int(np.argmin(np.abs(w - d))) for d in np.diag(t)]
    V = V[:, order]
    V = V / np.linalg.norm(V, axis=0)
    g0 = np.linalg.inv(V)                           # g0 n^-1 g0^-1 = t
    g0 = g0 / np.linalg.det(g0) ** (1 / 3)

    def point(a, b):
        s = np.diag([np.exp(1j * a), np.exp(1j * b), np.exp(-1j * (a + b))])
        return s @ g0
    return link, gam, point, 3                      # the maximal torus covers F |Z(SU(3))| = 3 times


def chern_over_f(link, gam, point, n):
    g0 = point(0.0, 0.0)
    zeta, nz = normal_eigenvalue(link, gam, g0)
    frames, worst_fix, dims, ones = [], 0.0, set(), set()
    for i in range(n):
        row = []
        for j in range(n):
            g = point(2 * np.pi * i / n, 2 * np.pi * j / n)
            worst_fix = max(worst_fix, float(np.linalg.norm(link.residual(gam, g))))
            Q, r, o = eigenframe(link, gam, g, zeta)
            dims.add(r)
            ones.add(o)
            row.append(Q)
        frames.append(row)
    c1, overlap = lattice_chern(frames)
    return {"zeta": [round(zeta.real, 12), round(zeta.imag, 12)], "normal eigenvalues": sorted(round(float(np.angle(x)), 9) for x in nz),
            "grid": n, "worst fixed-point residual on the grid": worst_fix, "dim E_zeta": sorted(dims), "dim T F (+1-eigenspace)": sorted(ones),
            "lattice c_1 over the sweep": float(round(c1, 9)) + 0.0, "smallest link overlap": float(round(overlap, 6))}


def commutes_check(link, gam, point, rng):
    """the acting torus commutes with gamma: gamma(s . g) = s . gamma(g) for random s in the torus and random g in the link"""
    worst = 0.0
    for _ in range(5):
        g = link.random_elements(rng, 1)[0]
        a, b = rng.uniform(0, 2 * np.pi, 2)
        s = point(a, b) @ np.linalg.inv(point(0.0, 0.0))
        lhs = link.embed(link.act(gam, s @ g))
        rhs = link.embed(s @ link.act(gam, g))
        worst = max(worst, float(np.linalg.norm(lhs - rhs)))
    return worst


def main():
    t0 = time.time()
    lines = []

    def log(s):
        print(s)
        lines.append(s)
    rng = np.random.default_rng(1502)
    log("B1502 section 5 THE CUBIC INFLOW -- own-code verification")
    ctrl = {m: float(round(lattice_chern(qwz_frames(m, 24))[0], 9)) + 0.0 for m in (-3.0, -1.0, 1.0, 3.0)}
    log(f"(3) positive control, Qi-Wu-Zhang lower band on a 24 x 24 grid: Chern numbers {ctrl}")
    cases = []
    census = json.load(open(ROOT / "frontier" / "B1501_the_torus_link_census" / "verification" / "census.json"))
    for r in census["records"]:
        tor = [c for c in r["components"] if c.get("topology", {}).get("type") == "torus"]
        if not tor or r["order"] < 3:
            continue
        if r["link"] == "S3xS3":
            link, gam, point, cover = s3xs3_setup(Fraction(r["q"][0]))
        else:
            link, gam, point, cover = f12_setup(r["outer"])
        res = [chern_over_f(link, gam, point, n) for n in GRIDS]
        comm = commutes_check(link, gam, point, rng)
        c1s = [x["lattice c_1 over the sweep"] for x in res]
        zeta = complex(*res[0]["zeta"])
        N = next(k for k in range(1, 100) if abs(zeta ** k - 1) < 1e-9)      # the order of zeta: the transverse Z_N
        case = {"class": r["label"], "order": r["order"], "transverse Z_N": N, "sweep covers F": cover, "runs": res,
                "acting torus commutes with gamma (worst)": comm,
                "c_1(E_zeta) = 0": all(abs(c) < 1e-6 for c in c1s),
                "deg L = (N/2) c_1(E_zeta) / cover": 0 if all(abs(c) < 1e-6 for c in c1s) else None}
        cases.append(case)
        log(f"(1) {r['label']:<24} order {r['order']:>2}, transverse Z_{N}: c_1(E_zeta) over the sweep {c1s} (grids {list(GRIDS)}), "
            f"dim E_zeta {res[0]['dim E_zeta']}, dim TF {res[0]['dim T F (+1-eigenspace)']}, fixed-point residual <= "
            f"{max(x['worst fixed-point residual on the grid'] for x in res):.1e}, smallest overlap {min(x['smallest link overlap'] for x in res)}; "
            f"(2) the acting torus commutes with gamma to {comm:.1e}")
    ok = (all(c["c_1(E_zeta) = 0"] for c in cases) and ctrl[-3.0] == 0 and ctrl[3.0] == 0 and abs(ctrl[1.0]) == 1
          and abs(ctrl[-1.0]) == 1 and all(c["acting torus commutes with gamma (worst)"] < 1e-12 for c in cases)
          and all(c["runs"][0]["dim E_zeta"] == [2] and c["runs"][0]["dim T F (+1-eigenspace)"] == [2] for c in cases)
          and len(cases) == 24)
    log(f"    => n_P = deg(L|_F) = 0 on all {len(cases)} torus classes of order >= 3: Witten's cubic SU(N)^3 inflow forces nothing at "
        f"the apex either")
    log("ALL CHECKS PASS" if ok else "CHECK FAILED")
    log(f"{time.time() - t0:.1f} s")
    out = {"positive control (QWZ Chern numbers)": {str(k): v for k, v in ctrl.items()}, "classes": cases,
           "n_P = 0 on every torus class": ok, "all checks pass": ok}
    json.dump(T.jsonable(out) if hasattr(T, "jsonable") else out, open(HERE / "cubic_inflow.json", "w"), indent=1)
    (HERE / "cubic_inflow_run.txt").write_text("\n".join(lines) + "\n")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
