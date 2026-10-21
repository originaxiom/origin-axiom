"""P-222, part 2: the SM seat's W62 (what holds tau at the selected state) checked by main's own code, written from
W62_RULE.md and the seat's recorded read-out, not from its script.

    python3 main_w62.py family                  # the shapes (exact Gram reduction), into family_w62.json
    python3 main_w62.py spectra [--workers 8]   # the matter's lowest K = 400 eigenvalues per member at n and 4n (cached)
    python3 main_w62.py read                    # the cells into main_w62.json

The closed-form cells (A1-A3, the contents' cusp coefficients) need no spectrum. Units: W59's, E(tau, s) = sum'
y^s/|m + n tau|^{2s}; a lattice six-dimensional term V = - int_{t0}^inf t^{-3} K(t) dt on a torus of area A = n sqrt(3)/2
(unit spacing) is converted by pi A^2 / 32."""
import json, os, sys, math
from fractions import Fraction as Fr
import numpy as np
from scipy.special import exp1, gamma, kv

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
CACHE = os.path.join(HERE, "spectra_w62")
OMEGA = complex(-0.5, math.sqrt(3) / 2)
N_INDEX = 8400
K = 200      # the rule's 400 is more than the cutoff needs: lambda_K t0 stays near 55 (the rule asks >= 30); checked per member
ZETA6 = math.pi ** 6 / 945
PAR = [(0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]


# ---------------- exact lattice arithmetic in the basis (1, omega) ----------------
def gram(u, v):                       # 2 Re(u conj v) for u = u0 + u1 omega (an integer)
    return 2 * u[0] * v[0] + 2 * u[1] * v[1] - (u[0] * v[1] + u[1] * v[0])


def reduce_basis(v1, v2):
    """Gauss (Lagrange) reduction with exact integers: |u1| <= |u2|, |2 Re(u2 conj u1)| <= |u1|^2, Re(u2 conj u1) >= 0
    after the mirror; returns (u1, u2, (A, B, C)) with A = 2|u1|^2, B = 2 Re(u2 conj u1), C = 2|u2|^2 (doubled)"""
    u1, u2 = list(v1), list(v2)
    while True:
        a, b = gram(u1, u1), gram(u1, u2)
        q = round(Fr(b, a))
        u2 = [u2[0] - q * u1[0], u2[1] - q * u1[1]]
        if gram(u2, u2) < gram(u1, u1): u1, u2 = u2, u1; continue
        break
    A, B, C = gram(u1, u1), gram(u1, u2), gram(u2, u2)
    return u1, u2, (A, B, C)


def shape_of(ABC, n):
    A, B, C = ABC                     # tau = u2/u1: x = B/A (the doubled gram cancels), y = area/|u1|^2
    area = n * math.sqrt(3) / 2
    return complex(abs(B) / A, 2 * area / A)


def family(n=N_INDEX):
    """every index-n sublattice (Hermite normal form (a, 0), (b, d), a d = n, 0 <= b < a, in order of a then b) whose
    reduced shape lies on the imaginary axis with 1 < y <= 2.1 or on the unit arc with 0 < x < 1/2; the first in that
    order for each shape; and the hexagonal reference (and the next sublattice with the hexagonal shape)"""
    out, hexa = {}, []
    for a in range(1, n + 1):
        if n % a: continue
        d = n // a
        for b in range(a):
            u1, u2, (A, B, C) = reduce_basis((a, 0), (b, d))
            area2 = 3 * n * n                          # (2 * area)^2 * (4/3)... exact test below uses y^2 = 3 n^2 / A^2
            on_axis = (B == 0 and C > A and 3 * n * n <= (2.1 ** 2) * A * A)
            on_arc = (A == C and 0 < 2 * abs(B) < A)
            is_hex = (A == C and 2 * abs(B) == A)
            key = (A, abs(B), C)
            if is_hex:
                if len(hexa) < 2:
                    hexa.append({"hnf": [a, b, d], "u1": u1, "u2": u2, "ABC": list(key)})
                continue
            if (on_axis or on_arc) and key not in out:
                out[key] = {"hnf": [a, b, d], "u1": u1, "u2": u2, "ABC": list(key), "kind": "axis" if on_axis else "arc"}
    mem = list(out.values())
    for m in mem: m["tau"] = [shape_of(m["ABC"], n).real, shape_of(m["ABC"], n).imag]
    mem.sort(key=lambda m: (m["kind"], m["tau"][1] if m["kind"] == "axis" else -m["tau"][0]))
    for h in hexa: h["tau"] = [shape_of(h["ABC"], n).real, shape_of(h["ABC"], n).imag]
    return {"n": n, "members": mem, "hexagonal": hexa}


# ---------------- closed forms ----------------
def E_direct(tau, s, M=200):
    m, n = np.meshgrid(np.arange(-M, M + 1), np.arange(-M, M + 1), indexing="ij"); m = m.ravel(); n = n.ravel()
    nz = (m != 0) | (n != 0)
    return float(np.sum(tau.imag ** s / np.abs(m[nz] + n[nz] * tau) ** (2 * s)))


def E_cs(tau, s, Kmax=60):
    """Chowla-Selberg: E(tau, s) = 2 zeta(2s) y^s + 2 sqrt(pi) Gamma(s - 1/2) zeta(2s - 1) y^{1-s} / Gamma(s)
    + (8 pi^s sqrt(y) / Gamma(s)) sum_{k >= 1} k^{s - 1/2} sigma_{1-2s}(k) K_{s-1/2}(2 pi k y) cos(2 pi k x)"""
    from mpmath import zeta
    x, y = tau.real, tau.imag
    tot = 2 * float(zeta(2 * s)) * y ** s + 2 * math.sqrt(math.pi) * gamma(s - 0.5) * float(zeta(2 * s - 1)) * y ** (1 - s) / gamma(s)
    for k in range(1, Kmax):
        sig = sum(dd ** (1 - 2 * s) for dd in range(1, k + 1) if k % dd == 0)
        tot += 8 * math.pi ** s * math.sqrt(y) / gamma(s) * k ** (s - 0.5) * sig * kv(s - 0.5, 2 * math.pi * k * y) * math.cos(2 * math.pi * k * x)
    return float(tot)


def S_c(tau, p, M=60):
    """S_c(tau) = sum' cos 2 pi (m p1 + n p2) y^3 / |m + n tau|^6 (the rule: |m|, |n| <= 60)"""
    m, n = np.meshgrid(np.arange(-M, M + 1), np.arange(-M, M + 1), indexing="ij"); m = m.ravel(); n = n.ravel()
    nz = (m != 0) | (n != 0); m, n = m[nz], n[nz]
    return float(np.sum(np.cos(2 * np.pi * (m * p[0] + n * p[1])) * tau.imag ** 3 / np.abs(m + n * tau) ** 6))


def copies(w):                         # the Higgs's three parity copies at the line w: p + 3w
    return [((p[0] + 3 * w[0]) % 1.0, (p[1] + 3 * w[1]) % 1.0) for p in PAR]


def V_H(tau, w=(0.5, 0.5)):           # the copies' boson term
    return -sum(S_c(tau, c) for c in copies(w))


def closed_form_cells():
    out = {}
    pts = [complex(0.13, 1.21), complex(-0.31, 0.98), complex(0.4, 1.7), OMEGA, 1j]
    a1 = []
    for t in pts:
        lhs = sum(S_c(t, c) for c in copies((0.5, 0.5)))
        rhs = E_cs(t, 3) / 16 - S_c(t, (0.5, 0.5))
        sinv = abs(S_c(-1 / t, (0.5, 0.5)) - S_c(t, (0.5, 0.5)))
        t2 = abs(S_c(t + 2, (0.5, 0.5)) - S_c(t, (0.5, 0.5)))
        t1 = abs(S_c(t + 1, (0.5, 0.5)) - S_c(t, (0.5, 0.5)))
        mirror = abs(S_c(t + 1, (0.5, 0.5)) - S_c(complex(-(t + 1).real, (t + 1).imag), (0.5, 0.5)))
        a1.append({"tau": [t.real, t.imag], "identity_err_over_E": abs(lhs - rhs) / E_cs(t, 3), "S_inv": sinv, "T2": t2, "T1": t1,
                   "T1_equals_mirror_err": mirror})
    out["A1"] = a1
    h = 1e-5
    f = lambda t: V_H(t)
    g = ((f(OMEGA + h) - f(OMEGA - h)) / (2 * h), (f(OMEGA + 1j * h) - f(OMEGA - 1j * h)) / (2 * h))
    arc = [complex(math.cos(th), math.sin(th)) for th in np.linspace(math.pi / 3, math.pi / 2, 31)]  # omega's mirror image to i
    arc = [complex(-z.real, z.imag) if False else z for z in arc]
    va = [f(complex(-z.real, z.imag)) for z in arc]        # from omega = (-1/2, sqrt3/2) to i along |tau| = 1
    out["A2"] = {"V_H_omega": f(OMEGA), "grad_omega": list(g), "grad_over_V": math.hypot(*g) / abs(f(OMEGA)),
                 "V_H_i": f(1j), "monotone_decreasing_omega_to_i": bool(all(va[k + 1] < va[k] for k in range(len(va) - 1)))}
    y = 8.0; t = complex(0, y)
    kap = {"trivial": 2 * ZETA6, "(1/2,0)": -31 / 16 * ZETA6, "(0,1/2)": 2 * ZETA6, "(1/2,1/2)": -31 / 16 * ZETA6}
    a3 = {}
    for name, p in (("trivial", (0, 0)), ("(1/2,0)", (0.5, 0)), ("(0,1/2)", (0, 0.5)), ("(1/2,1/2)", (0.5, 0.5))):
        a3[name] = abs(S_c(t, p) / y ** 3 - kap[name]) / (2 * ZETA6)
    comb = sum(-0.5 * S_c(t, (a / 2, b / 2)) for a in range(2) for b in range(2)) + sum(0.25 * S_c(t, (a / 4, b / 4)) for a in range(4) for b in range(4))
    a3["comb"] = abs(comb / y ** 3 - (-31 / 512) * ZETA6) / (2 * ZETA6)
    out["A3_rel_errors"] = a3
    # the contents' cusp coefficients, exact (units of zeta(6)): kappa_c = sum_{m != 0} c(m, 0)/m^6
    kq = {(0, 0): Fr(2), (Fr(1, 2), 0): Fr(-31, 16), (0, Fr(1, 2)): Fr(2), (Fr(1, 2), Fr(1, 2)): Fr(-31, 16)}
    k_rho = Fr(-31, 512)
    def kap_of(p): return kq[(p[0] % 1, p[1] % 1)]
    res = {}
    for line in ((Fr(1, 2), Fr(1, 2)), (Fr(1, 2), 0), (0, Fr(1, 2))):
        cps = [((p[0] + 3 * line[0]) % 1, (p[1] + 3 * line[1]) % 1) for p in ((Fr(1, 2), 0), (0, Fr(1, 2)), (Fr(1, 2), Fr(1, 2)))]
        higgs = sum(2 * kap_of(c) for c in cps)
        matter = -2 * 45 * k_rho
        gauge = 2 * 12 * Fr(2); grav = Fr(9, 2) * Fr(2)
        res[str(line)] = {"(a) matter + Higgs": float(matter + higgs), "(b) + gauge": float(matter + higgs + gauge),
                          "(c) + graviton": float(matter + higgs + gauge + grav), "(d) matter alone": float(matter)}
    out["contents_cusp_coefficients_zeta6"] = res
    return out


# ---------------- the lattice members ----------------
def key(tag, n, rank):
    return os.path.join(CACHE, "%s_n%d_r%d.npy" % (tag, n, rank))


def member_list():
    fam = json.load(open(os.path.join(HERE, "family_w62.json")))
    L = [("ref", fam["hexagonal"][0])] + ([("hex2", fam["hexagonal"][1])] if len(fam["hexagonal"]) > 1 else [])
    L += [("%s%02d" % (m["kind"], i), m) for i, m in enumerate(fam["members"])]
    return L


def solve(task):
    from lattice import Torus, lowest
    tag, m, scale = task
    n = N_INDEX * scale * scale
    path = key(tag, n, 2)
    if os.path.exists(path): return path
    u1 = [scale * x for x in m["u1"]]; u2 = [scale * x for x in m["u2"]]
    T = Torus(u1, u2)
    H = T.operator((0.0, 0.0), rank=2)
    pl = T.plaquettes(2)
    neg = sum(np.allclose(hh, -np.eye(2), atol=1e-12) for _, hh in pl); pos = sum(np.allclose(hh, np.eye(2), atol=1e-12) for _, hh in pl)
    w = lowest(H, K, sigma=-0.5)
    np.save(path + ".tmp.npy", w); os.replace(path + ".tmp.npy", path)
    json.dump({"neg": int(neg), "pos": int(pos), "triangles": len(pl)}, open(path + ".plaq.json", "w"))
    return path


def abelian_spectrum_hnf(hnf, scale, phi):
    """all n eigenvalues of the rank-1 operator on Z^2 / Lambda, Lambda = <(a, 0), (b, d)> scaled, with twists phi
    along those two basis vectors: k1 = (r + phi1)/a, k2 = (s + phi2 - k1 b)/d"""
    a, b, d = [scale * x for x in hnf]
    r = np.arange(a)[:, None]; s = np.arange(d)[None, :]
    k1 = (r + phi[0]) / a; k2 = (s + phi[1] - k1 * b) / d
    k1 = np.broadcast_to(k1, k2.shape)
    lam = (4 / 3) * (3 - np.cos(2 * np.pi * k1) - np.cos(2 * np.pi * k2) - np.cos(2 * np.pi * (k1 + k2)))
    return lam.ravel()


def V6(lam, t0):
    lam = np.asarray(lam, float); x = lam * t0
    I = np.where(lam > 1e-12, np.exp(-x) / (2 * t0 ** 2) - lam * np.exp(-x) / (2 * t0) + lam ** 2 * exp1(np.maximum(x, 1e-300)) / 2, 1 / (2 * t0 ** 2))
    return float(-np.sum(I))


def tail_ok(lam, t0):
    return float(lam[-1] * t0)



def lattice_cells(write=True):
    from lattice import Torus, lowest, lattice_spectrum_abelian_general
    fam = json.load(open(os.path.join(HERE, "family_w62.json")))
    mem = member_list()
    out = {"members": []}
    lmin = min(math.sqrt(m["ABC"][0] / 2) for _, m in mem)        # the shortest torus vector at n (unit spacing)
    E3w = E_cs(OMEGA, 3)
    for scale in (1, 2):
        n = N_INDEX * scale * scale; A = n * math.sqrt(3) / 2; conv = math.pi * A * A / 32
        t0 = (scale * lmin) ** 2 / 25
        rows = {}
        for tag, m in mem:
            lam = np.load(key(tag, n, 2)); pq = json.load(open(key(tag, n, 2) + ".plaq.json"))
            Vr = V6(lam, t0)
            sp = [(-0.5, abelian_spectrum_hnf(m["hnf"], scale, (a / 2, b / 2))) for a in range(2) for b in range(2)] \
               + [(0.25, abelian_spectrum_hnf(m["hnf"], scale, (a / 4, b / 4))) for a in range(4) for b in range(4)]
            comb = sum(c * V6(x, t0) for c, x in sp)
            # the truncation control: the comb's rank-2 periodic part is a sum of abelian spectra; cut each at the same
            # lambda_K as the matter's spectrum and compare (an upper estimate of what truncation does to V_rho)
            cut = lambda x: np.sort(x)[:np.searchsorted(np.sort(x), lam[-1], side="right")]
            combK = sum(c * V6(cut(x), t0) for c, x in sp)
            tau = complex(*m["tau"])
            rows[tag] = {"tau": m["tau"], "V_rho": Vr * conv, "V_comb": comb * conv, "E3": E_cs(tau, 3), "E2": E_cs(tau, 2),
                         "plaquettes_neg": pq["neg"], "plaquettes_pos": pq["pos"], "triangles": pq["triangles"],
                         "kramers_rel": float(np.max(np.abs(lam[0::2] - lam[1::2]) / lam[1::2])), "lamK_t0": float(lam[-1] * t0),
                         "V_comb_truncated": combK * conv}
        ref = rows["ref"]
        for tag, r in rows.items():
            r["dV_rho"] = r["V_rho"] - ref["V_rho"]; r["dV_comb"] = r["V_comb"] - ref["V_comb"]
            r["dV_per"] = (31 / 1024) * (r["E3"] - E3w); r["dD"] = r["dV_rho"] - r["dV_comb"]
            r["dE3"] = r["E3"] - E3w; r["dE2"] = r["E2"] - ref["E2"]
            r["trunc_err_d"] = (r["V_comb_truncated"] - ref["V_comb_truncated"]) - r["dV_comb"]
        out["n%d" % n] = rows
    n1, n4 = "n%d" % N_INDEX, "n%d" % (4 * N_INDEX)
    tags = [t for t, _ in mem if t not in ("ref", "hex2")]
    R1, R4 = out[n1], out[n4]
    maxper = max(abs(R4[t]["dV_per"]) for t in tags)
    m1err = {s: max(abs(out[s][t]["dV_comb"] - out[s][t]["dV_per"]) for t in tags) for s in (n1, n4)}
    cells = {}
    cells["M0"] = {"one_negative_triangle_everywhere": all(out[s][t]["plaquettes_neg"] == 1 and out[s][t]["plaquettes_pos"] == out[s][t]["triangles"] - 1 for s in (n1, n4) for t in out[s]),
                   "kramers_max_rel": max(out[s][t]["kramers_rel"] for s in (n1, n4) for t in out[s]),
                   "lamK_t0_min": min(out[s][t]["lamK_t0"] for s in (n1, n4) for t in out[s]),
                   "hex2_minus_ref_V_rho": {s: abs(out[s]["hex2"]["V_rho"] - out[s]["ref"]["V_rho"]) for s in (n1, n4)} if "hex2" in R1 else None}
    cells["M1"] = {"max_err": m1err, "max_dV_per": maxper, "holds": bool(m1err[n1] <= 0.005 * max(abs(R1[t]["dV_per"]) for t in tags) and m1err[n4] < m1err[n1])}
    maxD = max(abs(R4[t]["dD"]) for t in tags)
    cells["truncation_control"] = {s_: max(abs(out[s_][t]["trunc_err_d"]) for t in tags) for s_ in (n1, n4)}
    cells["M2"] = {"max_abs_dD_4n": maxD, "ratio_to_M1_err": maxD / m1err[n4], "holds": bool(maxD > 10 * m1err[n4])}
    big = [t for t in tags if abs(R4[t]["dV_per"]) > 0.1 * maxper]
    cells["M3"] = {"ratios_dD_over_dVper": {t: R4[t]["dD"] / R4[t]["dV_per"] for t in tags if abs(R4[t]["dV_per"]) > 1e-12},
                   "holds": bool(all(np.sign(R4[t]["dD"]) == -np.sign(R4[t]["dV_per"]) and abs(R4[t]["dD"]) < abs(R4[t]["dV_per"]) for t in big))}
    x = np.array([R4[t]["dE3"] for t in tags]); yv = np.array([R4[t]["dV_rho"] for t in tags])
    beta = float(x @ yv / (x @ x)); res = yv - beta * x
    unc = np.array([max(abs(R4[t]["dV_rho"] - R1[t]["dV_rho"]), m1err[n4]) for t in tags])
    k = int(np.argmax(np.abs(res)))
    cells["M4"] = {"beta": beta, "largest_residual": float(res[k]), "at": tags[k], "its_uncertainty": float(unc[k]),
                   "ratio": float(abs(res[k]) / unc[k]), "holds": bool(abs(res[k]) > 3 * unc[k])}
    axis = sorted([t for t in tags if t.startswith("axis")], key=lambda t: R4[t]["tau"][1])
    arc = sorted([t for t in tags if t.startswith("arc")], key=lambda t: -R4[t]["tau"][0])     # from omega toward i
    va = [R4[t]["dV_rho"] for t in axis]; vr = [0.0] + [R4[t]["dV_rho"] for t in arc]
    cells["M5"] = {"axis": [(R4[t]["tau"][1], R4[t]["dV_rho"]) for t in axis], "arc": [(R4[t]["tau"][0], R4[t]["dV_rho"]) for t in arc],
                   "holds": bool(all(va[i + 1] > va[i] for i in range(len(va) - 1)) and all(vr[i + 1] > vr[i] for i in range(len(vr) - 1)))}
    bigD = [t for t in tags if abs(R4[t]["dD"]) > 0.2 * maxD]
    cells["M6"] = {"worst_rel_change": max(abs(R4[t]["dD"] - R1[t]["dD"]) / abs(R4[t]["dD"]) for t in bigD),
                   "holds": bool(all(abs(R4[t]["dD"] - R1[t]["dD"]) < 0.25 * abs(R4[t]["dD"]) for t in bigD))}
    # the read-outs: D's shape
    for s in (n1, n4):
        D = np.array([out[s][t]["dD"] for t in tags]); e2 = np.array([out[s][t]["dE2"] for t in tags]); e3 = np.array([out[s][t]["dE3"] for t in tags])
        c2 = float(e2 @ D / (e2 @ e2)); X = np.column_stack([e2, e3]); c23 = np.linalg.lstsq(X, D, rcond=None)[0]
        rms = lambda r: float(np.sqrt(np.mean(r ** 2)) / np.sqrt(np.mean(D ** 2)))
        cells["D_shape_" + s] = {"c_E2": c2, "c_E2_over_31_1024": c2 / (31 / 1024), "rms_rel_E2_alone": rms(D - c2 * e2),
                                 "c_E2_E3": c23.tolist(), "rms_rel_both": rms(D - X @ c23)}
    out["cells"] = cells
    if write: json.dump(out, open(os.path.join(HERE, "main_w62.json"), "w"), indent=1)
    return cells


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "family":
        f = family(); json.dump(f, open(os.path.join(HERE, "family_w62.json"), "w"), indent=1)
        print(len(f["members"]), "members:", [(m["kind"], round(m["tau"][0], 4), round(m["tau"][1], 4)) for m in f["members"]])
        print("hexagonal:", f["hexagonal"])
    elif cmd == "closed":
        o = closed_form_cells(); json.dump(o, open(os.path.join(HERE, "main_w62_closed.json"), "w"), indent=1); print(json.dumps(o, indent=1))
    elif cmd == "read":
        print(json.dumps(lattice_cells(), indent=1))
    elif cmd == "spectra":
        os.makedirs(CACHE, exist_ok=True)
        nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
        scales = (1,) if "--scale1" in sys.argv else (2, 1)
        T = [(tag, m, sc) for sc in scales for tag, m in member_list()]
        if "--reverse" in sys.argv: T = T[::-1]           # a second pool from the other end; a task the first pool holds can still be taken again (FINDINGS, Disclosed)
        from multiprocessing import Pool
        with Pool(nw) as P:
            for p in P.imap_unordered(solve, T): print(os.path.basename(p), flush=True)
