"""W60: the quark sector with a Wilson line. The matter's local system rho_Q, twisted by a flat line L_phi, on the
punctured fibre at tau = omega; its spectrum on a triangular lattice with the puncture's half flux in one plaquette; the
line's potential from heat-trace differences. The rule (W60_RULE.md) was committed before this script.

  P1  the abelian control (rank 1, no flux) against Kronecker's formula and the exact lattice sum
  P2  the symmetries on the lattice: period 1/2, phi -> -phi, the order-3 rotation
  P3  the matter's two-dimensional term at the special points (N = 192)
  P4  the matter's six-dimensional term at the special points (N = 192) and on the grid (N = 96)
  plus the read-outs: convergence, the geodesic estimate's shape, a stated content's net term

Run: python3 the_quark_sector_and_the_line.py  ->  the_quark_sector_and_the_line.json beside it.
"""
import os

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
from multiprocessing import Pool  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import scipy.sparse as sp  # noqa: E402
from scipy.sparse.linalg import eigsh  # noqa: E402
from scipy.special import exp1  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_one_loop_potential_on_the_fibre as OP  # noqa: E402  (W59: Kronecker's form, the parities, the charges)

OUT = HERE / "the_quark_sector_and_the_line.json"
AREA = math.sqrt(3) / 2
K = 300
QI = np.array([[1j, 0], [0, -1j]])
QJ = np.array([[0, 1], [-1, 0]], dtype=complex)
SPECIAL = {"0": (0.0, 0.0), "(1/4, 0)": (0.25, 0.0), "(0, 1/4)": (0.0, 0.25), "(1/4, 1/4)": (0.25, 0.25),
           "(1/6, 1/6)": (1 / 6, 1 / 6), "(1/3, 1/3)": (1 / 3, 1 / 3)}
EXTRA = {"(1/9, 1/9)": (1 / 9, 1 / 9), "(2/9, 2/9)": (2 / 9, 2 / 9), "(1/18, 1/18)": (1 / 18, 1 / 18)}


# ------------------------------------------------------------------------------------------------------- the lattice
def hamiltonian(N, phi, rank):
    """the six-point covariant Laplacian on the triangular grid z_ij = ((i + 1/3) + (j + 2/3) omega)/N; links crossing
    s = 0 carry G1, crossing t = 0 carry G2, crossing both G2 G1; the half flux sits in the puncture's triangle"""
    e1, e2 = np.exp(2j * np.pi * phi[0]), np.exp(2j * np.pi * phi[1])
    if rank == 2:
        G1, G2 = QI * e1, QJ * e2
    else:
        G1, G2 = np.array([[e1]]), np.array([[e2]])
    one = np.eye(rank, dtype=complex)
    c = 2.0 * N * N / 3.0
    i, j = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    i, j = i.ravel(), j.ravel()
    x = i * N + j
    rows, cols, vals = [], [], []
    for a in range(rank):
        rows.append(x * rank + a)
        cols.append(x * rank + a)
        vals.append(np.full(x.size, 6 * c, dtype=complex))
    for d0, d1 in ((1, 0), (0, 1), (1, 1)):
        cs, ct = (i + d0) == N, (j + d1) == N
        y = ((i + d0) % N) * N + (j + d1) % N
        for mask, U in ((~cs & ~ct, one), (cs & ~ct, G1), (~cs & ct, G2), (cs & ct, G2 @ G1)):
            if not mask.any():
                continue
            xs, ys = x[mask], y[mask]
            for a in range(rank):
                for b in range(rank):
                    if U[a, b] == 0:
                        continue
                    rows += [xs * rank + a, ys * rank + b]
                    cols += [ys * rank + b, xs * rank + a]
                    vals += [np.full(xs.size, -c * U[a, b]), np.full(xs.size, -c * np.conj(U[a, b]))]
    n = N * N * rank
    return sp.csc_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n))


def spectrum(args):
    N, phi, rank = args
    H = hamiltonian(N, phi, rank)
    v = eigsh(H, k=K, sigma=-1.0, which="LM", return_eigenvectors=False, tol=1e-12)
    return np.sort(np.real(v))


def i1(lam, t0):
    return exp1(lam * t0)


def i3(lam, t0):
    return np.exp(-lam * t0) * (1 / (2 * t0 ** 2) - lam / (2 * t0)) + lam ** 2 / 2 * exp1(lam * t0)


def deltas(lam, ref, t0):
    """Delta log det = -int dK dt/t and Delta V6 = -int dK t^-3 dt, against the reference spectrum"""
    return float(-np.sum(i1(lam, t0) - i1(ref, t0))), float(-np.sum(i3(lam, t0) - i3(ref, t0)))


# ---------------------------------------------------------------------------------------------- exact abelian values
def lattice_sum(phi, ref, coeff=None, M=80):
    m, n = np.meshgrid(np.arange(-M, M + 1), np.arange(-M, M + 1), indexing="ij")
    m, n = m.ravel(), n.ravel()
    keep = (m != 0) | (n != 0)
    m, n = m[keep], n[keep]
    w = 1.0 / np.abs(m + n * OP.OMEGA) ** 6
    c = np.ones_like(w) if coeff is None else coeff(m, n)
    th = lambda p: np.cos(2 * np.pi * (m * p[0] + n * p[1]))  # noqa: E731
    return float(-(AREA / (4 * np.pi)) * 128 * np.sum(c * w * (th(phi) - th(ref))))


def kronecker(phi, ref):
    """Delta log det by W59's closed form, with (a, b) = (phi2, -phi1)"""
    return OP.logdet_theta(OP.OMEGA, phi[1], -phi[0]) - OP.logdet_theta(OP.OMEGA, ref[1], -ref[0])


def joint_coeff(m, n):
    return sum(np.cos(2 * np.pi * (m * u + n * v)) for u, v in OP.PARITIES)


# ------------------------------------------------------------------------------------------------------------- cells
def P1(pool):
    ref = (0.5, 0.5)
    pts = [(0.25, 0.0), (0.5, 0.0), (1 / 3, 1 / 3), (0.1, 0.37), (0.4, 0.15)]
    out, ok = {"reference": list(ref)}, True
    errs = {}
    for N in (96, 192):
        specs = pool.map(spectrum, [(N, p, 1) for p in [ref] + pts])
        t0 = 30.0 / specs[0][-1]
        rows = []
        for p, lam in zip(pts, specs[1:]):
            dl, dv = deltas(lam, specs[0], t0)
            el, ev = kronecker(p, ref), lattice_sum(p, ref)
            rows.append({"phi": list(p), "Delta log det": dl, "Kronecker": el, "|diff|": abs(dl - el),
                         "Delta V6": dv, "exact": ev, "relative diff": abs(dv - ev) / abs(ev)})
        out[f"N = {N}"] = {"t0": t0, "rows": rows}
        errs[N] = (max(r["|diff|"] for r in rows), max(r["relative diff"] for r in rows))
    ok = errs[192][0] < 2e-3 and errs[192][1] < 0.03 and errs[96][0] > errs[192][0] and errs[96][1] > errs[192][1]
    out["the largest errors (log det, V6) by N"] = {str(k): list(v) for k, v in errs.items()}
    out["holds"] = bool(ok)
    return out


def rot(p):
    return (p[1], -p[0] - p[1])


def P2(pool):
    gens = [(0.07, 0.19), (0.31, 0.05), (0.13, 0.41), (0.22, 0.29), (0.38, 0.33), (0.46, 0.11)]
    jobs = [(96, (0.0, 0.0), 2)]
    for p in gens:
        jobs += [(96, p, 2), (96, (p[0] + 0.5, p[1]), 2), (96, (-p[0], -p[1]), 2), (96, rot(p), 2)]
    specs = pool.map(spectrum, jobs)
    ref, t0 = specs[0], 30.0 / specs[0][-1]
    rows, worst_spec, worst_pot = [], 0.0, 0.0
    for g, p in enumerate(gens):
        s, sh, sm, sr = specs[1 + 4 * g: 5 + 4 * g]
        d_sh = float(np.max(np.abs(sh - s) / s))
        d_sm = float(np.max(np.abs(sm - s) / s))
        a, b = deltas(s, ref, t0), deltas(sr, ref, t0)
        d_rot = max(abs(a[0] - b[0]), abs(a[1] - b[1]) / max(1.0, abs(a[1])))
        worst_spec = max(worst_spec, d_sh, d_sm)
        worst_pot = max(worst_pot, d_rot)
        rows.append({"phi": list(p), "period 1/2 (relative)": d_sh, "phi -> -phi (relative)": d_sm,
                     "the order-3 image: the potentials' difference": d_rot})
    return {"rows": rows, "holds": bool(worst_spec < 1e-9 and worst_pot < 1e-6)}


def matter(pool):
    """the special points and the extra points at N = 96 and 192; the 12 x 12 grid at N = 96"""
    res = {}
    for N in (96, 192):
        pts = dict(SPECIAL)
        if N == 192:
            pts.update(EXTRA)
        names = list(pts)
        specs = pool.map(spectrum, [(N, pts[k], 2) for k in names])
        ref = specs[names.index("0")]
        t0 = 30.0 / ref[-1]
        pnts = {k: dict(zip(("Delta log det", "Delta V6"), deltas(s, ref, t0))) for k, s in zip(names, specs)}
        res[N] = {"t0": t0, "lowest ten at phi = 0": ref[:10].tolist(), "points": pnts}
    grid = [(a / 24, b / 24) for a in range(12) for b in range(12)]
    specs = pool.map(spectrum, [(96, p, 2) for p in grid])
    ref = specs[0]
    t0 = 30.0 / ref[-1]
    res["grid"] = [{"phi": [round(p[0], 6), round(p[1], 6)], "Delta log det": d[0], "Delta V6": d[1]}
                   for p, d in ((p, deltas(s, ref, t0)) for p, s in zip(grid, specs))]
    return res


def P3_P4(res):
    pts = res[192]["points"]
    f2 = {k: -0.5 * v["Delta log det"] for k, v in pts.items() if k in SPECIAL}
    f6 = {k: -v["Delta V6"] for k, v in pts.items() if k in SPECIAL}
    sixth = ("(1/6, 1/6)", "(1/3, 1/3)")

    def lowest_at_zero_highest_at_sixth(f):
        others = [v for k, v in f.items() if k != "0"]
        top = max(f.values())
        return all(v > f["0"] for v in others) and all(abs(f[k] - top) < 1e-6 * max(1.0, abs(top)) for k in sixth)
    grid_ok = all(-g["Delta V6"] >= -1e-9 for g in res["grid"])
    p3 = {"the fermion's two-dimensional potential (-1/2 Delta log det) at N = 192": f2,
          "holds": bool(lowest_at_zero_highest_at_sixth(f2))}
    p4 = {"the fermion's six-dimensional potential (-Delta V6) at N = 192": f6,
          "no grid point (N = 96) lower than phi = 0": bool(grid_ok),
          "holds": bool(lowest_at_zero_highest_at_sixth(f6) and grid_ok)}
    return p3, p4


def readouts(res):
    lo96, lo192 = np.array(res[96]["lowest ten at phi = 0"]), np.array(res[192]["lowest ten at phi = 0"])
    shape = []
    for g in res["grid"]:
        p = g["phi"]
        est = -sum(np.cos(2 * np.pi * 2 * (k[0] * p[0] + k[1] * p[1])) - 1 for k in
                   ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1)))
        shape.append((est, g["Delta V6"]))
    est, val = np.array(shape).T
    corr = float(np.corrcoef(est, val)[0, 1]) if np.std(est) > 0 and np.std(val) > 0 else None
    pts = res[192]["points"]
    v6 = lambda key: pts[key]["Delta V6"]  # noqa: E731

    def mod_half(p):
        q = [x % 0.5 for x in p]
        best = None
        for cand in (q, [(-x) % 0.5 for x in q]):
            for r in range(3):
                for key, s in list(SPECIAL.items()) + list(EXTRA.items()):
                    if max(abs(((cand[t] - s[t]) + 0.25) % 0.5 - 0.25) for t in range(2)) < 1e-9:
                        best = key
                cand = list(rot(cand))
                cand = [x % 0.5 for x in cand]
        return best
    lines = {"0": (0.0, 0.0), "w0 = (1/3, 1/3)": (1 / 3, 1 / 3), "(1/9, 1/9)": (1 / 9, 1 / 9),
             "(2/9, 2/9)": (2 / 9, 2 / 9)}
    net = {}
    for name, w in lines.items():
        quark = 0.0
        missing = []
        for f, n_states in (("Q", 18), ("u^c", 9), ("d^c", 9)):
            q = OP.CHARGES[f]
            key = mod_half((q * w[0] % 1, q * w[1] % 1))
            if key is None:
                missing.append(f)
                continue
            quark += -2 * n_states * v6(key)
        higgs = 2 * lattice_sum((3 * w[0] % 1, 3 * w[1] % 1), (0.0, 0.0), coeff=joint_coeff)
        net[name] = {"quarks": quark, "Higgs": higgs, "net": quark + higgs, "unmatched": missing}
    return {"the lowest ten at phi = 0, N = 96 and 192": [lo96.tolist(), lo192.tolist()],
            "their relative change": (np.abs(lo192 - lo96) / lo192).tolist(),
            "the geodesic estimate against Delta V6 on the grid (correlation)": corr,
            "a stated content's net six-dimensional term (heat-trace units; quarks -2 per state, Higgs +2)": net}


def main():
    with Pool(4) as pool:
        p1 = P1(pool)
        p2 = P2(pool)
        res = matter(pool)
    p3, p4 = P3_P4(res)
    out = {"status": "W60: the quark sector with a Wilson line at tau = omega (the rule W60_RULE.md first; one run)",
           "P1": p1, "P2": p2, "P3": p3, "P4": p4,
           "the matter's values": {"N = 96": res[96], "N = 192": res[192], "the grid (N = 96)": res["grid"]},
           "read-outs": readouts(res)}
    out["cells"] = {k: out[k]["holds"] for k in ("P1", "P2", "P3", "P4")}
    out["every cell holds"] = all(out["cells"].values())
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1), "\nevery cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
