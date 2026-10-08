#!/usr/bin/env python3
"""B1616 -- THE NEUTRINO MASSES ON THE WEAVE: the Majorana analysis B1615 left owed.  A Majorana mass term for the matter
triplet T is a symmetric matrix: it pairs T with T through Sym^2 T and a Higgs-type field H in an irreducible of Sym^2 T
(B1615: (Sym^2 T)^G = 0, so H is never a singlet).  With H's vacuum along the fixed directions of one of the weave's own
residual subgroups -- RRL (TM1's neutrino-side symmetry, B1612), RL, L, R -- the mass matrix M(v) = sum_k v_k C_k is
complex symmetric; its masses are its singular values (Takagi).  Exact up to floating point:
 N1  Sym^2 T and Lambda^2 T decomposed into irreducibles of G (dimensions; which pieces of T (x) T they are).
 N2  for each irreducible r of Sym^2 T and each residual subgroup: the dimension of r's fixed space; the mass ratios
     m1/m3, m2/m3 over it (rigid when one-dimensional; scanned densely over the projective space when two-dimensional).
 N3  every exact linear relation among the three masses the families obey (m1 + m2 = m3, m1 = m2, m1 = 0, ...), tested on
     the scan to 1e-9.
 N4  for each family obeying a sum rule of the form m_a + m_b = m_c: with the measured splittings (sealed inputs below),
     the absolute masses and their sum in normal and inverted ordering, solved exactly.
Inputs for N4 (named before the run; NuFIT 6.0, arXiv:2410.05380v2, IC24 with SK-atm best fits, read for B1612):
dm21^2 = 7.49e-5 eV^2; dm31^2 = +2.513e-3 eV^2 (NO); dm32^2 = -2.484e-3 eV^2 (IO).  No cosmological datum is read by this
instrument.  Writes neutrino_masses_on_the_weave.json."""
import json, pathlib, sys, os, importlib.util, itertools, collections
import numpy as np
from scipy.optimize import brentq
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("cw", FRONTIER / "B1615_the_couplings_the_weave_allows" / "verification" / "couplings_on_the_weave.py")
cw = importlib.util.module_from_spec(spec); spec.loader.exec_module(cw)
T = cw.T; element = cw.element; cp = cw.cp
IDX = [(i, j) for i in range(3) for j in range(i, 3)]


def sym_basis():
    B = np.zeros((9, 6), dtype=complex)
    for c, (i, j) in enumerate(IDX):
        v = np.zeros(9, dtype=complex); v[3 * i + j] += 1; v[3 * j + i] += 1; B[:, c] = v / np.linalg.norm(v)
    return B


def alt_basis():
    idx = [(i, j) for i in range(3) for j in range(i + 1, 3)]; B = np.zeros((9, 3), dtype=complex)
    for c, (i, j) in enumerate(idx):
        v = np.zeros(9, dtype=complex); v[3 * i + j] += 1; v[3 * j + i] -= 1; B[:, c] = v / np.linalg.norm(v)
    return B


def masses(Msym):
    s = np.sort(np.linalg.svd(Msym, compute_uv=False)); return s


def relations(a):
    """exact linear relations among sorted masses (m1 <= m2 <= m3), normalised by m3"""
    r1, r2 = a[:, 0], a[:, 1]; tests = {"m1 + m2 = m3": r1 + r2 - 1, "m1 = m2": r1 - r2, "m2 = m3": r2 - 1, "m1 = 0": r1,
                                        "m2 - m1 = m3": r2 - r1 - 1, "2 m2 = m1 + m3": 2 * r2 - r1 - 1}
    return {k: bool(np.max(np.abs(v)) < 1e-9) for k, v in tests.items()}


def solve_sum_rule(rule, dm21, dm3x, order):
    """absolute masses obeying the rule with the splittings; order NO: m1 < m2 < m3, IO: m3 < m1 < m2"""
    def ms(x):
        if order == "NO": m1 = x; m2 = np.sqrt(x ** 2 + dm21); m3 = np.sqrt(x ** 2 + dm3x); return m1, m2, m3
        m3 = x; m2 = np.sqrt(x ** 2 + dm3x); m1 = np.sqrt(x ** 2 + dm3x - dm21); return m1, m2, m3      # IO: m3 lightest, dm3x = |dm32^2|
    def f(x):
        a = sorted(ms(x)); return {"m1 + m2 = m3": a[0] + a[1] - a[2], "2 m2 = m1 + m3": 2 * a[1] - a[0] - a[2]}[rule]
    xs = np.logspace(-6, 0, 4000); vals = [f(x) for x in xs]; roots = []
    for k in range(len(xs) - 1):
        if np.sign(vals[k]) != np.sign(vals[k + 1]):
            r = brentq(f, xs[k], xs[k + 1]); roots.append([float(v) for v in ms(r)])
    return roots


def main():
    out = {}
    Bs, Ba = sym_basis(), alt_basis()
    sym_mats = [Bs.conj().T @ np.kron(A, A) @ Bs for A in T]
    pieces, comm = cp.decompose(sym_mats, 6)
    out["N1"] = {"Sym2_pieces_dims": sorted(P.shape[1] for P in pieces), "Sym2_commutant": comm,
                 "Alt2_dim": 3, "Alt2_irreducible": round(float(sum(abs(np.trace(Ba.conj().T @ np.kron(A, A) @ Ba)) ** 2 for A in T) / len(T)), 6)}
    N2 = {}; families = []
    for n, P in enumerate(pieces):
        Q, _ = np.linalg.qr(P); d = Q.shape[1]
        Cs = [(Bs @ Q[:, k]).reshape(3, 3) for k in range(d)]       # symmetric 3x3 Clebsch-Gordan matrices
        rows = {}
        for g in ("RRL", "RL", "L", "R"):
            M = Q.conj().T @ Bs.conj().T @ np.kron(element(g), element(g)) @ Bs @ Q
            ev, V = np.linalg.eig(M); fixed = V[:, [i for i, e in enumerate(ev) if abs(e - 1) < 1e-7]]
            if fixed.shape[1] == 0: rows[g] = {"fixed_dim": 0}; continue
            Qf, _ = np.linalg.qr(fixed); pts = []
            if Qf.shape[1] == 1:
                vs = [Qf[:, 0]]
            else:
                vs = [Qf @ np.array([np.cos(t), np.exp(1j * p) * np.sin(t)] + [0] * (Qf.shape[1] - 2)) for t in np.linspace(0, np.pi / 2, 181) for p in np.linspace(0, 2 * np.pi, 181, endpoint=False)]
            for v in vs:
                s = masses(sum(v[k] * Cs[k] for k in range(d)))
                if s[2] > 1e-12: pts.append((s[0] / s[2], s[1] / s[2]))
            a = np.array(pts)
            rel = relations(a) if len(a) else {}
            rows[g] = {"fixed_dim": int(Qf.shape[1]), "m1_m3_range": [float(a[:, 0].min()), float(a[:, 0].max())],
                       "m2_m3_range": [float(a[:, 1].min()), float(a[:, 1].max())], "relations": rel}
            for k, ok in rel.items():
                if ok and k in ("m1 + m2 = m3", "2 m2 = m1 + m3"): families.append((f"piece {n} (dim {d})", g, k))
        N2[f"piece {n} (dim {d})"] = rows
    out["N2"] = N2
    dm21, dm31, dm32 = 7.49e-5, 2.513e-3, -2.484e-3
    N4 = []
    for piece, g, rule in sorted(set(families)):
        no = solve_sum_rule(rule, dm21, dm31, "NO"); io = solve_sum_rule(rule, dm21, -dm32, "IO")
        N4.append({"piece": piece, "residual": g, "rule": rule,
                   "NO": [{"masses_eV": [round(m, 6) for m in r], "sum_eV": round(sum(r), 6)} for r in no],
                   "IO": [{"masses_eV": [round(m, 6) for m in r], "sum_eV": round(sum(r), 6)} for r in io]})
    out["N3"] = {"families_with_a_sum_rule": [list(f) for f in sorted(set(families))]}
    out["N4"] = N4
    json.dump(out, open(HERE / "neutrino_masses_on_the_weave.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
