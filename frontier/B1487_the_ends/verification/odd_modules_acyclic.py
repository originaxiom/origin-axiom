#!/usr/bin/env python3
"""B1487 THE ENDS -- cells E2 and E3 (first run unsealed on m135 and m136 on 2026-10-07; disclosed in the seal).
On a word state the fibre's boundary is a commutator whose SL(2,C) image has trace -2 on every lift; so every odd
symmetric power of every lift has no invariants on the cusp, the cusp is acyclic, and (Menal-Ferrer--Porti) the module
is acyclic on the manifold: no classes, no count.  The even modules (the four) have h^1 = number of cusps.  Read here on
SnapPy's own presentation of the named states for all 2^b1 lifts, with the numerical twin of main's instrument
(B1485/fused.py: counts).  Usage: odd_modules_acyclic.py m135 m136 ...   -> odd_modules_acyclic.json"""
import sys, os, json, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "frontier").is_dir())
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / "frontier" / "B1486_the_two_orders_at_the_silver_members" / "verification"))
import fused as F
import snappy
from math import comb
from mpmath import mp, mpf, mpc, matrix, zeros, nstr
mp.dps = 40; F.mp.mp.dps = 40; F.TOL = mpf(10) ** -25


def num(x): return mpf(str(x).replace(" ", ""))


def sym(M, n):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]; S = zeros(n + 1, n + 1)
    for j in range(n + 1):
        coeffs = [mpc(0)] * (n + 1)
        for p in range(n - j + 1):
            for q in range(j + 1):
                coeffs[(n - j - p) + (j - q)] += comb(n - j, p) * comb(j, q) * a ** (n - j - p) * c ** p * b ** (j - q) * d ** q
        for xdeg in range(n + 1): S[n - xdeg, j] = coeffs[xdeg]
    return S


def four(M):
    Ms = matrix([[M[j, i].conjugate() for j in range(2)] for i in range(2)])
    basis = [matrix([[1, 0], [0, 0]]), matrix([[0, 0], [0, 1]]), matrix([[0, 1], [1, 0]]), matrix([[0, 1j], [-1j, 0]])]
    cols = []
    for H in basis:
        Hp = M * H * Ms; cols.append([Hp[0, 0], Hp[1, 1], (Hp[0, 1] + Hp[1, 0]) / 2, (Hp[0, 1] - Hp[1, 0]) / (2j)])
    return matrix([[cols[j][i] for j in range(4)] for i in range(4)])


def one(name):
    M = snappy.ManifoldHP(name); G = M.fundamental_group(); gens = G.generators(); rels = G.relators(); mu, lam = G.peripheral_curves()[0]
    rho = {g: matrix([[mpc(num(G.SL2C(g)[i, j].real()), num(G.SL2C(g)[i, j].imag())) for j in range(2)] for i in range(2)]) for g in gens}
    tl = F.word(lam, rho); tm = F.word(mu, rho)
    rec = dict(name=name, gens=gens, rels=rels, cusp=[mu, lam], tr_mu=nstr(tm[0, 0] + tm[1, 1], 10), tr_lam=nstr(tl[0, 0] + tl[1, 1], 10), lifts=[])
    for eps in itertools.product((1, -1), repeat=len(gens)):
        lift = {g: e * rho[g] for g, e in zip(gens, eps)}
        if max(abs(F.word(r, lift)[i, j] - (1 if i == j else 0)) for r in rels for i in range(2) for j in range(2)) > 1e-20: continue   # not a lift
        row = dict(signs=list(eps))
        for n in (1, 3):
            c = F.counts(gens, rels, (mu, lam), {g: sym(lift[g], n) for g in gens}); row["Sym%d" % n] = c
        row["four"] = F.counts(gens, rels, (mu, lam), {g: four(lift[g]) for g in gens})
        rec["lifts"].append(row); print(name, eps, {k: (v["a1"], v["n"]) for k, v in row.items() if k != "signs"}, flush=True)
    rec["odd_modules_acyclic_on_every_lift"] = all(r["Sym1"]["a1"] == 0 and r["Sym3"]["a1"] == 0 for r in rec["lifts"])
    return rec


if __name__ == "__main__":
    out = [one(n) for n in sys.argv[1:]]
    json.dump(out, open(HERE / "odd_modules_acyclic.json", "w"), indent=1, default=str)
    print({r["name"]: r["odd_modules_acyclic_on_every_lift"] for r in out})
