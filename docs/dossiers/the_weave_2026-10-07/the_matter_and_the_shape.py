"""W62: what holds tau at the selected state. The matter's six-dimensional tau-dependence (rho_Q with the puncture's
half flux), computed on one triangular lattice for every torus shape of a stated family, against the exact periodic part
(an abelian "comb") and E(tau, 3); and, in closed form, the Higgs's copies at the half-period line W60 selected. The
rule (W62_RULE.md) was committed before this script.

  M0  the construction: plaquettes, Kramers pairs, W60's N = 96 spectrum, the abelian spectrum in closed form,
      lambda_K t0
  M1  the comb on the lattice against (31/1024)[E(tau, 3) - E(omega, 3)]
  M2  the diffraction is there;  M3 its sign and size;  M4 not a multiple of E(tau, 3)
  M5  the matter's own critical points;  M6  convergence (n against 4n)
  A1  the Higgs's copies at w = (1/2, 1/2);  A2  the selected state is not stationary in tau;  A3  the cusps
  plus the read-outs: the contents, the shape of D, the content window, the reference's orientation, extrapolations

Run: python3 the_matter_and_the_shape.py  ->  the_matter_and_the_shape.json beside it.
"""
import os

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
from multiprocessing import Pool  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
import scipy.sparse as sp  # noqa: E402
from scipy.sparse.linalg import eigsh  # noqa: E402
from scipy.special import exp1, gamma, kv, zeta  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_one_loop_potential_on_the_fibre as OP  # noqa: E402  (W59: omega, E(tau, 3), the parities)

OUT = HERE / "the_matter_and_the_shape.json"
W60 = json.loads((HERE / "the_quark_sector_and_the_line.json").read_text(encoding="utf-8"))
OMEGA = OP.OMEGA
N_FAMILY = 8400
K = 400
EPS = 1e-7
Z6 = float(zeta(6))
QI = np.array([[1j, 0], [0, -1j]])
QJ = np.array([[0, 1], [-1, 0]], dtype=complex)
DELTAS = ((1, 0), (0, 1), (1, 1))


# ------------------------------------------------------------------------------------------------- shapes and family
def reduce(t):
    """reduce mod SL(2, Z) to the fundamental domain, then the mirror to x >= 0"""
    for _ in range(500):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-12:
            t = -1 / t
        else:
            break
    return complex(abs(t.real), t.imag)


def family(n):
    """every Hermite sublattice (a, c, d) of index n; the first per reduced shape; the axis, arc and hexagonal shapes"""
    first, hexes = {}, []
    for a in range(1, n + 1):
        if n % a:
            continue
        d = n // a
        for c in range(a):
            t = reduce((c + d * OMEGA) / a)
            key = (round(t.real, 9), round(t.imag, 9))
            if abs(t.real - 0.5) < 1e-9 and abs(t.imag - math.sqrt(3) / 2) < 1e-9:
                hexes.append((a, c, d))
            first.setdefault(key, (a, c, d, t))
    axis = sorted((v for v in first.values() if abs(v[3].real) < 1e-9 and 1 + 1e-9 < v[3].imag <= 2.1),
                  key=lambda v: v[3].imag)
    arc = sorted((v for v in first.values() if abs(abs(v[3]) - 1) < 1e-9 and 1e-9 < v[3].real < 0.5 - 1e-9),
                 key=lambda v: -v[3].real)
    return hexes, axis, arc


# ------------------------------------------------------------------------------------------------------- the lattice
def links(a, c, d, G1, G2):
    """for each forward step delta: the target site and the link matrix; sites at Z^2 + (1/3, 2/3) mod the sublattice
    with rows (a, 0), (c, d); a link crossing the cut through v2 carries G1, through v1 carries G2, both: their product
    in the order crossed; the cuts are shifted by EPS"""
    r = G1.shape[0]
    i, j = np.meshgrid(np.arange(a), np.arange(d), indexing="ij")
    i, j = i.ravel(), j.ravel()
    p1, p2 = i + 1 / 3, j + 2 / 3
    beta = p2 / d + EPS
    alpha = (p1 - (beta - EPS) * c) / a + EPS
    al, be = alpha - np.floor(alpha), beta - np.floor(beta)
    out = []
    for d1, d2 in DELTAS:
        db = d2 / d
        da = (d1 - db * c) / a
        ka, kb = np.floor(al + da).astype(int), np.floor(be + db).astype(int)
        with np.errstate(divide="ignore", invalid="ignore"):
            la = np.where(ka != 0, (np.where(ka > 0, 1.0, 0.0) - al) / da, np.inf)
            lb = np.where(kb != 0, (np.where(kb > 0, 1.0, 0.0) - be) / db, np.inf)
        U = np.broadcast_to(np.eye(r, dtype=complex), (i.size, r, r)).copy()
        Ga = {1: G1, -1: G1.conj().T}
        Gb = {1: G2, -1: G2.conj().T}
        for s in range(i.size):
            if ka[s] == 0 and kb[s] == 0:
                continue
            if kb[s] == 0:
                U[s] = Ga[ka[s]]
            elif ka[s] == 0:
                U[s] = Gb[kb[s]]
            elif la[s] < lb[s]:
                U[s] = Ga[ka[s]] @ Gb[kb[s]]
            else:
                U[s] = Gb[kb[s]] @ Ga[ka[s]]
        jj = j + d2
        y = jj // d
        jn = jj - y * d
        im = (i + d1 - y * c) % a
        out.append((im * d + jn, U))
    return out


def hamiltonian(a, c, d, G1, G2):
    r = G1.shape[0]
    n = a * d
    cc = 2.0 / 3.0
    x = np.arange(n)
    rows, cols, vals = [], [], []
    for q in range(r):
        rows.append(x * r + q)
        cols.append(x * r + q)
        vals.append(np.full(n, 6 * cc, dtype=complex))
    for y, U in links(a, c, d, G1, G2):
        for p in range(r):
            for q in range(r):
                u = U[:, p, q]
                nz = u != 0
                if not nz.any():
                    continue
                rows += [x[nz] * r + p, y[nz] * r + q]
                cols += [y[nz] * r + q, x[nz] * r + p]
                vals += [-cc * u[nz], -cc * np.conj(u[nz])]
    return sp.csc_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n * r, n * r))


def plaquettes(a, c, d):
    """the holonomy of every triangle; returns (the number at -1, the number at +1, the largest deviation)"""
    (y1, U1), (y2, U2), (y3, U3) = links(a, c, d, QI, QJ)
    up = np.einsum("sij,sjk,slk->sil", U1, U2[y1], U3.conj())
    down = np.einsum("sij,sjk,slk->sil", U2, U1[y2], U3.conj())
    hol = np.concatenate([up, down])
    tr = np.real(np.einsum("sii->s", hol)) / 2
    minus = tr < 0
    dev = max(float(np.max(np.abs(hol[minus] + np.eye(2)))) if minus.any() else 0.0,
              float(np.max(np.abs(hol[~minus] - np.eye(2)))))
    return int(minus.sum()), int((~minus).sum()), dev


def comb_spectrum(a, c, d, phi):
    """the closed-form spectrum of the abelian twist phi along (v1, v2)"""
    m1, m2 = np.meshgrid(np.arange(a), np.arange(d), indexing="ij")
    k1 = (m1.ravel() + phi[0]) / a
    k2 = (m2.ravel() + phi[1] - c * k1) / d
    return (4.0 / 3.0) * (3 - np.cos(2 * np.pi * k1) - np.cos(2 * np.pi * k2) - np.cos(2 * np.pi * (k1 + k2)))


COMB = [((u / 2, v / 2), -0.5) for u in range(2) for v in range(2)] + \
       [((u / 4, v / 4), 0.25) for u in range(4) for v in range(4)]


def spectrum(job):
    a, c, d, rank, phi, k = job
    area = a * d * math.sqrt(3) / 2
    if rank == 2:
        G1, G2 = QI, QJ
    else:
        G1, G2 = np.array([[np.exp(2j * np.pi * phi[0])]]), np.array([[np.exp(2j * np.pi * phi[1])]])
    H = hamiltonian(a, c, d, G1, G2)
    v = eigsh(H, k=k, sigma=-4 * np.pi / area, which="LM", return_eigenvectors=False, tol=1e-12)
    return np.sort(np.real(v))


def i3(lam, t0):
    lam = np.asarray(lam, dtype=float)
    out = np.full(lam.shape, 1 / (2 * t0 ** 2))
    pos = lam > 1e-14
    lp = lam[pos]
    out[pos] = np.exp(-lp * t0) * (1 / (2 * t0 ** 2) - lp / (2 * t0)) + lp ** 2 / 2 * exp1(lp * t0)
    return out


# ------------------------------------------------------------------------------------------------------ closed forms
def E_cs(t, s, N=40):
    """E(tau, s) = Sum' y^s / |m + n tau|^(2s), by the Chowla-Selberg expansion"""
    x, y = t.real, t.imag
    head = (2 * zeta(2 * s) * y ** s
            + 2 * math.sqrt(math.pi) * gamma(s - 0.5) * zeta(2 * s - 1) / gamma(s) * y ** (1 - s))
    tail = 0.0
    for k in range(1, N + 1):
        sig = sum(dd ** (1 - 2 * s) for dd in range(1, k + 1) if k % dd == 0)
        tail += k ** (s - 0.5) * sig * kv(s - 0.5, 2 * math.pi * k * y) * math.cos(2 * math.pi * k * x)
    return float(head + 8 * math.pi ** s * math.sqrt(y) / gamma(s) * tail)


def S(t, char, M=400):
    """S_c(tau) = Sum' c(m, n) y^3 / |m + n tau|^6 for a character c (a phase pair) or 'comb'"""
    m, n = np.meshgrid(np.arange(-M, M + 1), np.arange(-M, M + 1), indexing="ij")
    m, n = m.ravel(), n.ravel()
    keep = (m != 0) | (n != 0)
    m, n = m[keep], n[keep]
    w = t.imag ** 3 / np.abs(m + n * t) ** 6
    if char == "comb":
        ev = (m % 2 == 0) & (n % 2 == 0)
        f4 = (m % 4 == 0) & (n % 4 == 0)
        cc = np.where(f4, 2.0, np.where(ev, -2.0, 0.0))
    else:
        cc = np.cos(2 * np.pi * (m * char[0] + n * char[1]))
    return float(np.sum(cc * w))


def copies(line):
    return [((p[0] + line[0]) % 1.0, (p[1] + line[1]) % 1.0) for p in OP.PARITIES]


def A1():
    rows, ok = [], True
    for t in (OMEGA, 1j, complex(0.3, 1.1), complex(0.1, 1.7), complex(-0.4, 0.95)):
        tot = sum(S(t, ch, M=600) for ch in copies((0.5, 0.5)))
        s_hh = S(t, (0.5, 0.5), M=600)
        e3 = E_cs(t, 3)
        ident = abs(tot - (e3 / 16 - s_hh)) / e3
        s_inv = abs(S(-1 / t, (0.5, 0.5), M=600) - s_hh) / e3
        t_two = abs(S(t + 2, (0.5, 0.5), M=600) - s_hh) / e3
        t_one = abs(S(t + 1, (0.5, 0.5), M=600) - s_hh)
        rows.append({"tau": [t.real, t.imag], "|copies - (E/16 - S_(1/2,1/2))| / E": ident,
                     "S: tau -> -1/tau (relative to E)": s_inv, "S: tau -> tau + 2 (relative to E)": t_two,
                     "S: tau -> tau + 1 (absolute change)": t_one})
        ok &= ident < 1e-10 and s_inv < 1e-10 and t_two < 1e-10 and t_one > 1e-3
    return {"rows": rows, "holds": bool(ok)}


def VH(t, line=(0.5, 0.5)):
    """the Higgs's copies' boson term per unit weight, -Sum S"""
    return -sum(S(t, ch) for ch in copies(line))


def A2(arc_pts):
    h = 1e-5
    w0 = OMEGA
    gx = (VH(w0 + h) - VH(w0 - h)) / (2 * h)
    gy = (VH(w0 + 1j * h) - VH(w0 - 1j * h)) / (2 * h)
    v0 = VH(w0)
    path = [w0] + [complex(x, math.sqrt(1 - x * x)) for x in arc_pts] + [1j]
    vals = [VH(t) for t in path]
    mono = all(vals[k + 1] < vals[k] for k in range(len(vals) - 1))
    ok = math.hypot(gx, gy) > 0.01 * abs(v0) and mono and vals[-1] < vals[0]
    return {"V_H at omega": v0, "its gradient (d/dx, d/dy) at omega": [gx, gy],
            "V_H along the arc from omega (x = 1/2 by the mirror) to i": [[t.real, t.imag, v] for t, v in
                                                                         zip(path, vals)],
            "decreasing from omega to i": bool(mono), "holds": bool(ok)}


def A3():
    t = 8j
    y3 = 512.0
    kap = {"trivial": 2 * Z6, "(1/2, 0)": -31 / 16 * Z6, "(0, 1/2)": 2 * Z6, "(1/2, 1/2)": -31 / 16 * Z6,
           "comb": -31 / 512 * Z6}
    chars = {"trivial": (0.0, 0.0), "(1/2, 0)": (0.5, 0.0), "(0, 1/2)": (0.0, 0.5), "(1/2, 1/2)": (0.5, 0.5),
             "comb": "comb"}
    rows, ok = {}, True
    for k, ch in chars.items():
        val = S(t, ch) / y3
        err = abs(val - kap[k]) / (2 * Z6)
        rows[k] = {"S / y^3 at 8i": val, "kappa": kap[k], "|diff| / 2 zeta(6)": err}
        ok &= err < 1e-4
    return {"rows": rows, "holds": bool(ok)}, kap


def e_controls():
    mp.mp.dps = 30
    L3 = lambda s: (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3)) / 3 ** s  # noqa: E731
    beta = lambda s: (mp.zeta(s, mp.mpf(1) / 4) - mp.zeta(s, mp.mpf(3) / 4)) / 4 ** s  # noqa: E731
    exact = {"E(i, 3)": float(4 * mp.zeta(3) * beta(3)), "E(omega, 3)": float((mp.sqrt(3) / 2) ** 3 * 6 * mp.zeta(3)
                                                                             * L3(3)),
             "E(i, 2)": float(4 * mp.zeta(2) * beta(2)), "E(omega, 2)": float(0.75 * 6 * mp.zeta(2) * L3(2))}
    got = {"E(i, 3)": E_cs(1j, 3), "E(omega, 3)": E_cs(OMEGA, 3), "E(i, 2)": E_cs(1j, 2), "E(omega, 2)": E_cs(OMEGA, 2)}
    w59 = abs(OP.E3(complex(0.2, 1.3)) / E_cs(complex(0.2, 1.3), 3) - 1)
    worst = max(abs(got[k] / exact[k] - 1) for k in exact)
    return {"closed forms": exact, "Chowla-Selberg": got, "largest relative difference": worst,
            "against W59's E3 at 0.2 + 1.3i": w59}, worst < 1e-12 and w59 < 1e-12


# ------------------------------------------------------------------------------------------------------------- main
def main():
    hexes, axis, arc = family(N_FAMILY)
    ref = hexes[0]
    members = [("reference (omega)", ref[0], ref[1], ref[2], complex(0.5, math.sqrt(3) / 2))]
    members += [(f"axis y = {v[3].imag:.4f}", v[0], v[1], v[2], v[3]) for v in axis]
    members += [(f"arc x = {v[3].real:.4f}", v[0], v[1], v[2], v[3]) for v in arc]
    other = [h for h in hexes if h != ref]
    extra = ("other hexagonal", *other[0], complex(0.5, math.sqrt(3) / 2)) if other else None
    tori = members + ([extra] if extra else [])

    sizes = {"n": 1, "4n": 2}
    jobs, keys = [], []
    for sz, f in sizes.items():
        for name, a, c, d, _ in tori:
            jobs.append((f * a, f * c, f * d, 2, (0.0, 0.0), K))
            keys.append(("rho", sz, name))
    jobs.append((96, 0, 96, 2, (0.0, 0.0), 10))
    keys.append(("w60", "", ""))
    for name, a, c, d, _ in [members[0], members[1], members[len(axis) + 1]]:
        jobs.append((a, c, d, 1, (0.25, 0.5), 50))
        keys.append(("abelian", "n", name))
    with Pool(4) as pool:
        specs = dict(zip(keys, pool.map(spectrum, jobs, chunksize=1)))

    out = {"status": "W62: the matter's six-dimensional tau-dependence and the closed forms at the selected line "
                     "(the rule W62_RULE.md first; one run)",
           "the family": {"n": N_FAMILY, "members": [[nm, a, c, d, [t.real, t.imag]] for nm, a, c, d, t in tori],
                          "hexagonal sublattices": [list(h) for h in hexes]}}

    # M0
    plaq, ok_plaq = {}, True
    for sz, f in sizes.items():
        for name, a, c, d, _ in tori:
            neg, pos, dev = plaquettes(f * a, f * c, f * d)
            plaq[f"{sz} {name}"] = [neg, pos, dev]
            ok_plaq &= neg == 1 and pos == 2 * f * f * a * d - 1 and dev < 1e-12
    kram = max(float(np.max(np.abs(v[1::2] - v[0::2]) / v[0::2])) for k, v in specs.items() if k[0] == "rho")
    w60_ten = np.array(W60["read-outs"]["the lowest ten at phi = 0, N = 96 and 192"][0]) / 96 ** 2
    w60_diff = float(np.max(np.abs(specs[("w60", "", "")] / w60_ten - 1)))
    ab = {}
    for name, a, c, d, _ in [members[0], members[1], members[len(axis) + 1]]:
        exact = np.sort(comb_spectrum(a, c, d, (0.25, 0.5)))[:50]
        ab[name] = float(np.max(np.abs(specs[("abelian", "n", name)] / exact - 1)))
    t0 = {}
    for sz, f in sizes.items():
        area = f * f * N_FAMILY * math.sqrt(3) / 2
        t0[sz] = area / (25 * max(t.imag for _, _, _, _, t in members))
    lk = {f"{k[1]} {k[2]}": float(v[-1] * t0[k[1]]) for k, v in specs.items() if k[0] == "rho"}
    m0 = {"(a) plaquettes [at -1, at +1, largest deviation]": plaq, "(b) Kramers: largest relative pair split": kram,
          "(c) W60's N = 96 lowest ten: largest relative difference": w60_diff,
          "(d) the abelian check (phases (1/4, 1/2)): largest relative difference": ab,
          "(e) lambda_K t0 per torus": lk, "t0": t0}
    m0["holds"] = bool(ok_plaq and kram < 1e-9 and w60_diff < 1e-9 and max(ab.values()) < 1e-10
                       and min(lk.values()) >= 30)

    # the six-dimensional values, relative to the reference, in W59's units at fixed area
    e3 = {nm: E_cs(t, 3) for nm, _, _, _, t in tori}
    e2 = {nm: E_cs(t, 2) for nm, _, _, _, t in tori}
    vals = {}
    for sz, f in sizes.items():
        area = f * f * N_FAMILY * math.sqrt(3) / 2
        conv = math.pi * area ** 2 / 32
        rr, rc = {}, {}
        for name, a, c, d, _ in tori:
            rr[name] = -float(np.sum(i3(specs[("rho", sz, name)], t0[sz])))
            rc[name] = -sum(w * float(np.sum(i3(comb_spectrum(f * a, f * c, f * d, phi), t0[sz]))) for phi, w in COMB)
        r0 = "reference (omega)"
        vals[sz] = {name: {"dV_rho": conv * (rr[name] - rr[r0]), "dV_comb": conv * (rc[name] - rc[r0])}
                    for name, *_ in tori}
        for name in vals[sz]:
            v = vals[sz][name]
            v["dD"] = v["dV_rho"] - v["dV_comb"]
            v["dV_per exact"] = 31 / 1024 * (e3[name] - e3[r0])
            v["dE3"], v["dE2"] = e3[name] - e3[r0], e2[name] - e2[r0]
    names = [nm for nm, *_ in members[1:]]
    out["the values (W59 units, against the reference)"] = vals

    # M1
    err = {sz: max(abs(vals[sz][nm]["dV_comb"] - vals[sz][nm]["dV_per exact"]) for nm in names) for sz in sizes}
    scale = max(abs(vals["n"][nm]["dV_per exact"]) for nm in names)
    m1 = {"largest |dV_comb - dV_per| by size": err, "max |dV_per|": scale,
          "holds": bool(err["n"] <= 0.005 * scale and err["4n"] < err["n"])}

    # M2, M3
    big = vals["4n"]
    maxd = max(abs(big[nm]["dD"]) for nm in names)
    m2 = {"max |dD| at 4n": maxd, "10 x the M1 error at 4n": 10 * err["4n"], "holds": bool(maxd > 10 * err["4n"])}
    sel = [nm for nm in names if abs(big[nm]["dV_per exact"]) > 0.1 * scale]
    m3_rows = {nm: [big[nm]["dD"], big[nm]["dV_per exact"]] for nm in sel}
    m3 = {"[dD, dV_per] at 4n": m3_rows,
          "holds": bool(all(np.sign(d) == -np.sign(p) and abs(d) < abs(p) for d, p in m3_rows.values()))}

    # M4
    dv = np.array([big[nm]["dV_rho"] for nm in names])
    de = np.array([big[nm]["dE3"] for nm in names])
    beta3 = float(dv @ de / (de @ de))
    res = dv - beta3 * de
    unc = np.array([max(abs(big[nm]["dV_rho"] - vals["n"][nm]["dV_rho"]), err["4n"]) for nm in names])
    k = int(np.argmax(np.abs(res)))
    m4 = {"beta (dV_rho = beta dE3)": beta3, "31/1024": 31 / 1024,
          "residuals": dict(zip(names, res.tolist())), "uncertainties": dict(zip(names, unc.tolist())),
          "the largest residual / its uncertainty": float(abs(res[k]) / unc[k]), "at": names[k],
          "holds": bool(abs(res[k]) > 3 * unc[k])}

    # M5
    ax_names = [nm for nm in names if nm.startswith("axis")]
    arc_names = [nm for nm in names if nm.startswith("arc")]
    ax_v = [big[nm]["dV_rho"] for nm in ax_names]
    arc_v = [big[nm]["dV_rho"] for nm in arc_names]
    m5 = {"axis by y": dict(zip(ax_names, ax_v)), "arc from omega toward i": dict(zip(arc_names, arc_v)),
          "holds": bool(all(v > 0 for v in ax_v + arc_v) and all(np.diff(ax_v) > 0) and all(np.diff(arc_v) > 0))}

    # M6
    sel6 = [nm for nm in names if abs(big[nm]["dD"]) > 0.2 * maxd]
    m6_rows = {nm: [vals["n"][nm]["dD"], big[nm]["dD"]] for nm in sel6}
    m6 = {"[dD(n), dD(4n)]": m6_rows,
          "holds": bool(all(abs(b - a) < 0.25 * abs(b) for a, b in m6_rows.values()))}

    # A
    ec, ec_ok = e_controls()
    a1 = A1()
    a2 = A2([big_t.real for nm, _, _, _, big_t in members if nm.startswith("arc")])
    a3, kap = A3()

    out.update({"M0": m0, "M1": m1, "M2": m2, "M3": m3, "M4": m4, "M5": m5, "M6": m6, "A1": a1, "A2": a2, "A3": a3,
                "the E(tau, s) controls": ec})
    out["cells"] = {k: out[k]["holds"] for k in ("M0", "M1", "M2", "M3", "M4", "M5", "M6", "A1", "A2", "A3")}
    out["every cell holds"] = all(out["cells"].values())
    out["the E controls hold"] = bool(ec_ok)
    out["read-outs"] = readouts(vals, names, ax_names, members, kap, ref, extra)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1), "\nevery cell holds:", out["every cell holds"])


def readouts(vals, names, ax_names, members, kap, ref, extra):
    big, small = vals["4n"], vals["n"]
    ro = {}
    # the contents
    contents = {"(a) W60's: the matter (45 states) and the Higgs's three copies": (45, True, 0.0),
                "(b) (a) with the 12 gauge bosons": (45, True, 24.0),
                "(c) (b) with the graviton": (45, True, 28.5),
                "(d) the matter alone": (45, False, 0.0)}
    lines = {"(1/2, 1/2)": (0.5, 0.5), "(1/2, 0)": (0.5, 0.0), "(0, 1/2)": (0.0, 0.5)}
    taus = {nm: t for nm, _, _, _, t in members}
    rows = {}
    for cname, (states, higgs, wt) in contents.items():
        crow = {}
        best = None
        for lname, line in lines.items():
            ks = -2 * states * kap["comb"] + wt * kap["trivial"]
            if higgs:
                ks += sum(2 * (kap["trivial"] if ch[0] == 0 else kap["(1/2, 0)"]) for ch in copies(line))
            tot = {}
            for nm, t in taus.items():
                v = -2 * states * (big[nm]["dV_rho"] if nm in big else 0.0) - wt * E_cs(t, 3)
                if higgs:
                    v += 2 * VH(t, line)
                tot[nm] = v
                if best is None or v < best[2]:
                    best = (lname, nm, v)
            crow[lname] = {"Sum W kappa at the cusp i infinity (units of zeta(6))": ks / Z6,
                           "stable at that cusp": bool(ks < 0), "totals at the members": tot}
        crow["the lowest among the members and lines"] = list(best)
        rows[cname] = crow
    ro["the contents"] = rows
    # the shape of D
    dd = np.array([big[nm]["dD"] for nm in names])
    E3d = np.array([big[nm]["dE3"] for nm in names])
    E2d = np.array([big[nm]["dE2"] for nm in names])
    fits = {}
    for fname, X in (("E3", E3d[:, None]), ("E2", E2d[:, None]), ("E3 and E2", np.stack([E3d, E2d], axis=1))):
        coef, *_ = np.linalg.lstsq(X, dd, rcond=None)
        r = dd - X @ coef
        fits[fname] = {"coefficients": coef.tolist(), "rms residual / rms dD": float(np.sqrt(np.mean(r ** 2))
                                                                                     / np.sqrt(np.mean(dd ** 2)))}
    par = -3 / (128 * float(zeta(4))) * E2d
    fits["the paraxial estimate -(3/(128 zeta(4))) dE2"] = {
        "least-squares amplitude": float(dd @ par / (par @ par)), "correlation": float(np.corrcoef(dd, par)[0, 1])}
    ro["the shape of D (4n)"] = fits
    # the content window
    win = []
    for sz, V in (("n", small), ("4n", big)):
        r = []
        for k in range(len(ax_names) - 1):
            a, b = ax_names[k], ax_names[k + 1]
            r.append((V[b]["dV_rho"] - V[a]["dV_rho"]) / (V[b]["dE3"] - V[a]["dE3"]))
        win.append((sz, r))
    ro["the content window"] = {
        "intervals": [[ax_names[k], ax_names[k + 1]] for k in range(len(ax_names) - 1)],
        "the ratio dV_rho / dE3 per interval": dict(win),
        "the range at 4n (a stationary point on the axis needs -c_E/c_rho inside it)": [min(win[1][1]),
                                                                                        max(win[1][1])]}
    # the reference's orientation
    if extra:
        ro["the other hexagonal sublattice against the reference"] = {
            sz: {"dV_rho": vals[sz]["other hexagonal"]["dV_rho"], "dD": vals[sz]["other hexagonal"]["dD"]}
            for sz in vals}
    # extrapolations
    ro["dD extrapolated"] = {nm: {"O(h)": 2 * big[nm]["dD"] - small[nm]["dD"],
                                  "O(h^2)": (4 * big[nm]["dD"] - small[nm]["dD"]) / 3} for nm in names}
    return ro


if __name__ == "__main__":
    main()
