#!/usr/bin/env python3
"""W137 — the joint frame's Yukawas: which weight the record allows, the minimal mass relation, the free numbers
against the quark data, and theta-bar with J (the rule: W137_RULE.md, committed and pushed before this script).

  Y0  reading II: the full symmetrisation of det(psi_a, psi_b, psi_c) is 0 (sympy, exact)
  Y1  reading I: rho'_k(-I) = 1, so k_Phi is even; the weights 3 k_Phi - h and C(w) from W136's closed forms (checked
      against W136's table); the 27s' weight (3 + m)/2 at W134's admissible data
  Y2  the minimal relation: lambda(h) symmetric, so M_e = M_d^T and D = 1, at five random points of the weight-6 space
  Y3  the instrument: M_w(Sym^3 rho') for w = 2, 6 by projection of the degree-w polynomials in v = 2 eta^3 R through
      the 48-element image (exact, Gaussian integers, modulo v.v = 0); the laws under S and T; CP: v(-conj tau) =
      X conj v(tau) with X = diag(1, 1, -1), and the CP-fixed bases
  Y4  theta-bar and J on the CP line tau = iy and at five random tau off it (60 digits)
  Y5  the rank of the Jacobian of the quark invariants, w = 6 and w = 2, with and without CP
  Y6  the read-out

    python3 -B the_joint_yukawas.py      # writes the_joint_yukawas.json beside itself
"""
import contextlib
import functools
import io
import itertools
import json
import random
import sys
from pathlib import Path

import flint
import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_coupling_forms as CF  # noqa: E402  (W136: twisted, to_gauss, closure, thetas, eta, vvec; BR = W134)

BR = CF.BR
OUT = HERE / "the_joint_yukawas.json"
I = CF.I
SYM = list(itertools.combinations_with_replacement(range(3), 3))
D_DATA = (10.58, 0.11)  # P-094's double ratio (W58's A2)
mp.mp.dps = 60


# ------------------------------------------------------------------ dimensions (W136's closed forms)
def dim_level_one(k):
    if k < 0 or k % 2:
        return 0
    return k // 12 if k % 12 == 2 else k // 12 + 1


def dims(w):
    if w < 0 or w % 2:
        return {"1'": 0, "rho'": 0, "rho' (x) sgn": 0}
    return {"1'": dim_level_one(w - 6) if w >= 6 else 0, "rho'": (w + 2) // 4 if w >= 2 else 0,
            "rho' (x) sgn": w // 4}


def C(w):
    d = dims(w)
    return d["1'"] + 2 * d["rho'"] + d["rho' (x) sgn"]


# ------------------------------------------------------------------ Y0
def Y0():
    a, b, c = (sp.Matrix(sp.symbols(f"{n}0:3")) for n in "abc")
    vecs = {"a": a, "b": b, "c": c}
    tot = sum(sp.Matrix.hstack(*(vecs[x] for x in p)).det() for p in itertools.permutations("abc"))
    ok = sp.expand(tot) == 0
    return {"checks": {"the full symmetrisation of det(psi_a, psi_b, psi_c) is 0": bool(ok)}}, bool(ok)


# ------------------------------------------------------------------ Y1
def Y1():
    c = {}
    minus_one = {}
    for k in (5, 13, 21):
        S, _ = CF.twisted(k)
        S2 = S * S
        minus_one[str(k)] = all(sp.simplify(sp.expand_complex(S2[i, j] - (1 if i == j else 0))) == 0
                                for i in range(3) for j in range(3))
    c["rho'_k(-I) = 1 for k = 5, 13, 21, so k_Phi is even"] = all(minus_one.values())
    w136 = json.loads((HERE / "the_coupling_forms.json").read_text(encoding="utf-8"))
    tab = w136["L1"]["the table, even w to 24 (route a)"]
    c["the closed forms equal W136's table, w <= 24"] = all(
        dims(w) == {s: tab[str(w)][s] for s in ("1'", "rho'", "rho' (x) sgn")} for w in range(0, 25, 2))
    kphis = list(range(-12, 15, 2))
    global_w = {str(k): {"w": 3 * k, "C": C(3 * k)} for k in kphis}
    sugra_w = {str(k): {"w": 3 * k - 1, "C": C(3 * k - 1)} for k in kphis}
    c["h = 0: the least positive weight is 6 (k_Phi = 2) with C = 6; k_Phi = 0 gives none"] = (
        min(3 * k for k in kphis if C(3 * k) > 0) == 6 and C(6) == 6 and C(0) == 0)
    c["h = 1: every weight is odd and carries no coupling"] = all(v["C"] == 0 and v["w"] % 2 for v in sugra_w.values())
    adm = {r: [m for m in range(-24, 25) if BR.admissible(r, m)] for r in BR.ALLOWED}
    c["k_Phi = (3 + m)/2 is an even integer at every admissible (r, m)"] = all(
        (3 + m) % 2 == 0 and ((3 + m) // 2) % 2 == 0 for r in adm for m in adm[r])
    least = {"m = 1 (r = 4 mod 8)": 1, "m = -3 (r = 0 mod 8)": -3}
    least_out = {k: {"k_Phi": (3 + m) // 2, "w": 3 * (3 + m) // 2, "C": C(3 * (3 + m) // 2)} for k, m in least.items()}
    threes = {}
    for r, m, cond in BR.PREDICTED_THREES:
        kp = (3 + m) // 2
        threes[f"({r}, {m}, {cond})"] = {"k_Phi": kp, "w": 3 * kp, "C": C(3 * kp)}
    c["least data: m = 1 gives w = 6 with C = 6, m = -3 gives none"] = (
        least_out["m = 1 (r = 4 mod 8)"]["C"] == 6 and least_out["m = -3 (r = 0 mod 8)"]["C"] == 0)
    by_m = {}
    for key, v in threes.items():
        m = int(key.split(",")[1])
        by_m.setdefault(m, set()).add((v["w"], v["C"]))
    c["three-generation data: m = -23, -19 none (five data); m = 17 w = 30, C = 26; m = 21 w = 36, C = 30"] = (
        by_m.get(-23) == {(-30, 0)} and by_m.get(-19) == {(-24, 0)} and by_m.get(17) == {(30, 26)}
        and by_m.get(21) == {(36, 30)}
        and sum(1 for v in threes.values() if v["C"] == 0) == 5)
    out = {"checks": c, "global supersymmetry (h = 0): k_Phi -> (w, C)": global_w,
           "supergravity, one modulus (h = 1): k_Phi -> (w, C)": sugra_w,
           "the 27s' weight at W134's least data": least_out, "the 27s' weight at W134's twelve data": threes}
    return out, all(c.values())


# ------------------------------------------------------------------ Y3: the coupling spaces, exact
@functools.lru_cache(maxsize=None)
def reduce_mono(beta):
    """v^beta modulo v.v = 0, in the normal form with v3's exponent at most 1: {monomial: integer}"""
    a, b, c = beta
    if c <= 1:
        return {beta: 1}
    out = {}
    for sub in ((a + 2, b, c - 2), (a, b + 2, c - 2)):
        for mono, k in reduce_mono(sub).items():
            out[mono] = out.get(mono, 0) - k
    return {m: k for m, k in out.items() if k}


def mono_apply(alpha, M):
    """f = v^alpha; f(M v) = coef * v^beta for a monomial matrix M"""
    coef, beta = complex(1), [0, 0, 0]
    for i in range(3):
        j = next(j for j in range(3) if M[i][j] != 0)
        coef *= M[i][j] ** alpha[i]
        beta[j] += alpha[i]
    return coef, tuple(beta)


def sym_unit(t):
    u = np.zeros((3, 3, 3), dtype=np.int64)
    for p in set(itertools.permutations(t)):
        u[p] = 1
    return u


def gauss(z):
    a, b = int(round(z.real)), int(round(z.imag))
    assert z == complex(a, b), z
    return complex(a, b)


def project(alpha, t, pairs):
    """sum over the image of rho'(g)^-1 (x3) u * (f | g): an element of M_w(Sym^3 rho'), as {(slot, monomial): coef}"""
    u = sym_unit(t)
    acc = {}
    for M, O in pairs:
        coef, beta = mono_apply(alpha, M)
        On = np.array([[int(round(x.real)) for x in r] for r in O], dtype=np.int64)
        tu = np.einsum("ia,jb,kc,ijk->abc", On, On, On, u)
        for s in SYM:
            if tu[s]:
                acc[(s, beta)] = acc.get((s, beta), 0) + coef * int(tu[s])
    out = {}
    for (s, beta), cc in acc.items():
        if cc == 0:
            continue
        for mono, k in reduce_mono(beta).items():
            out[(s, mono)] = out.get((s, mono), 0) + cc * k
    return {key: gauss(v) for key, v in out.items() if v != 0}


def crank(vectors, keys):
    if not vectors:
        return 0
    rows = []
    for v in vectors:
        re = [int(v.get(k, 0).real) for k in keys]
        im = [int(v.get(k, 0).imag) for k in keys]
        rows.append(re + im)
        rows.append([-x for x in im] + re)
    return int(flint.fmpz_mat(rows).rank()) // 2


def normal_monos(w):
    return [m for m in ((a, b, w - a - b) for a in range(w + 1) for b in range(w + 1 - a)) if m[2] <= 1]


def space(w, pairs):
    keys = [(s, m) for s in SYM for m in normal_monos(w)]
    basis = []
    for a in range(w + 1):
        for b in range(w + 1 - a):
            for t in SYM:
                cand = project((a, b, w - a - b), t, pairs)
                if cand and crank(basis + [cand], keys) > len(basis):
                    basis.append(cand)
    return basis, keys


def cp_map(lam):
    """C(lambda) = X^(x3) conj(lambda) at v -> X v, X = diag(1, 1, -1)"""
    out = {}
    for (s, mono), cc in lam.items():
        sign = (-1) ** sum(1 for i in s if i == 2) * (-1) ** mono[2]
        out[(s, mono)] = sign * cc.conjugate()
    return out


def lin(a, x, b=None, y=0):
    out = {}
    for d, f in ((x, a), (b, y)):
        if d is None:
            continue
        for k, v in d.items():
            out[k] = out.get(k, 0) + f * v
    return {k: gauss(v) for k, v in out.items() if v != 0}


def cp_basis(basis, keys):
    sel = []
    for b in basis:
        Cb = cp_map(b)
        for cand in (lin(1, b, Cb, 1), lin(1j, b, Cb, -1j)):
            if cand and crank(sel + [cand], keys) > len(sel):
                sel.append(cand)
    return sel


def evaluate(lam, v):
    T = [[[mp.mpc(0)] * 3 for _ in range(3)] for _ in range(3)]
    vals = {}
    for (s, mono), cc in lam.items():
        vals[s] = vals.get(s, mp.mpc(0)) + mp.mpc(cc) * v[0] ** mono[0] * v[1] ** mono[1] * v[2] ** mono[2]
    for s, x in vals.items():
        for p in set(itertools.permutations(s)):
            T[p[0]][p[1]][p[2]] = x
    return T


def transform(O, T):
    return [[[sum(mp.mpc(O[a][i] * O[b][j] * O[c][k]) * T[i][j][k] for i in range(3) for j in range(3)
                  for k in range(3) if O[a][i] != 0 and O[b][j] != 0 and O[c][k] != 0)
              for c in range(3)] for b in range(3)] for a in range(3)]


def tdiff(A, B):
    num = max(abs(A[i][j][k] - B[i][j][k]) for i in range(3) for j in range(3) for k in range(3))
    den = max(abs(B[i][j][k]) for i in range(3) for j in range(3) for k in range(3))
    return float(num / den)


def the_group():
    PS3, PT3 = CF.twisted(3)
    PS21, PT21 = CF.twisted(21)
    MS, MT, OS, OT = (CF.to_gauss(x) for x in (PS3, PT3, PS21, PT21))
    pairs = CF.closure([(MS, OS), (MT, OT)], lambda x, y: (CF.mul(x[0], y[0]), CF.mul(x[1], y[1])),
                       (CF.eye(3), CF.eye(3)))
    return pairs, OS, OT


def Y3(pairs, OS, OT):
    rng = random.Random(1371)
    taus = [mp.mpc(mp.mpf(str(round(rng.uniform(-0.45, 0.45), 6))), mp.mpf(str(round(rng.uniform(0.8, 1.6), 6))))
            for _ in range(3)]
    spaces, cps, c, worst = {}, {}, {}, {}
    for w in (2, 6):
        basis, keys = space(w, pairs)
        spaces[w] = basis
        cps[w] = cp_basis(basis, keys)
        law = 0.0
        for lam in basis:
            for tau in taus:
                T0 = evaluate(lam, CF.vvec(tau))
                law = max(law, tdiff(evaluate(lam, CF.vvec(-1 / tau)), [[[tau ** w * x for x in r] for r in m]
                                                                            for m in transform(OS, T0)]))
                law = max(law, tdiff(evaluate(lam, CF.vvec(tau + 1)), transform(OT, T0)))
        worst[f"w = {w}: the law under S and T"] = law
        cpfix = all(cp_map(b) == b for b in cps[w]) and len(cps[w]) == len(basis)
        c[f"dim M_{w}(Sym^3 rho') = C({w})"] = len(basis) == C(w)
        c[f"w = {w}: the CP-fixed forms span the space"] = bool(cpfix and crank(cps[w], keys) == len(basis))
    cpv = 0.0
    for tau in taus:
        v0, v1 = CF.vvec(tau), CF.vvec(-mp.conj(tau))
        cpv = max(cpv, CF.relerr(v1, [mp.conj(v0[0]), mp.conj(v0[1]), -mp.conj(v0[2])]))
    worst["v(-conj tau) = X conj v(tau)"] = cpv
    c["each basis form transforms by Sym^3 rho' under S and T, to 1e-40"] = all(
        x < 1e-40 for k, x in worst.items() if "law" in k)
    c["v(-conj tau) = X conj v(tau), to 1e-40"] = cpv < 1e-40
    out = {"checks": c, "worst deviations": worst, "dimensions": {str(w): len(spaces[w]) for w in spaces},
           "terms per CP-fixed basis form": {str(w): [len(b) for b in cps[w]] for w in cps}}
    return out, all(c.values()), cps


# ------------------------------------------------------------------ the mass matrices and invariants
def lam_at(basis, g, tau):
    v = CF.vvec(tau)
    T = [[[mp.mpc(0)] * 3 for _ in range(3)] for _ in range(3)]
    for gn, b in zip(g, basis):
        E = evaluate(b, v)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    T[i][j][k] += gn * E[i][j][k]
    return T


def mass(T, h):
    return mp.matrix([[sum(h[i] * T[i][j][k] for i in range(3)) for k in range(3)] for j in range(3)])


def herm(M):
    return M * M.H


def jarlskog(Mu, Md):
    Hu, Hd = herm(Mu), herm(Md)
    Cm = Hu * Hd - Hd * Hu
    eu, _ = mp.eighe(Hu)
    ed, _ = mp.eighe(Hd)
    du = (eu[1] - eu[0]) * (eu[2] - eu[0]) * (eu[2] - eu[1])
    dd = (ed[1] - ed[0]) * (ed[2] - ed[0]) * (ed[2] - ed[1])
    return float(abs(mp.det(Cm)) / (2 * abs(du * dd)))


def theta_dist(Mu, Md):
    th = mp.arg(mp.det(Mu)) + mp.arg(mp.det(Md))
    r = th % mp.pi
    return float(min(r, mp.pi - r))


def svals(M):
    S = mp.svd_c(M, compute_uv=False)
    return sorted(float(S[i]) for i in range(S.rows))


def Y2(cps):
    rng = random.Random(1372)
    sym, Dv = 0.0, 0.0
    for _ in range(5):
        g = [mp.mpc(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in cps[6]]
        tau = mp.mpc(rng.uniform(-0.45, 0.45), rng.uniform(0.9, 1.6))
        hd = [mp.mpc(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(3)]
        Md = mass(lam_at(cps[6], g, tau), hd)
        sym = max(sym, float(mp.mnorm(Md - Md.T, 1) / mp.mnorm(Md, 1)))
        d, e = svals(Md), svals(Md.T)
        Dv = max(Dv, abs((e[1] / e[0]) / (d[1] / d[0]) - 1))
    c = {"lambda(h) is symmetric, so M_e = M_d^T = M_d, to 1e-40": sym < 1e-40,
         "D = 1 at every point, to 1e-12": Dv < 1e-12}
    sig = (D_DATA[0] - 1) / D_DATA[1]
    return {"checks": c, "worst asymmetry": sym, "worst |D - 1|": Dv, "P-094's D": list(D_DATA),
            "the distance of D = 1 from P-094's D, in sigma": sig}, all(c.values())


def Y4(cps):
    rng = random.Random(1373)
    g = [mp.mpf(rng.uniform(-1, 1)) for _ in cps[6]]
    hu = [mp.mpf(rng.uniform(-1, 1)), mp.mpf(rng.uniform(-1, 1)), I * mp.mpf(rng.uniform(-1, 1))]
    hd = [mp.mpf(rng.uniform(-1, 1)), mp.mpf(rng.uniform(-1, 1)), I * mp.mpf(rng.uniform(-1, 1))]
    on, off = {}, {}
    for y in ("0.9", "1.3", "2.1"):
        T = lam_at(cps[6], g, mp.mpc(0, mp.mpf(y)))
        Mu, Md = mass(T, hu), mass(T, hd)
        on[y] = {"J": jarlskog(Mu, Md), "theta-bar from {0, pi}": theta_dist(Mu, Md)}
    for n in range(5):
        tau = mp.mpc(mp.mpf(str(round(rng.uniform(0.05, 0.45), 6))), mp.mpf(str(round(rng.uniform(0.9, 1.6), 6))))
        T = lam_at(cps[6], g, tau)
        Mu, Md = mass(T, hu), mass(T, hd)
        off[str(tau)] = {"J": jarlskog(Mu, Md), "theta-bar from {0, pi}": theta_dist(Mu, Md)}
    c = {"on tau = iy: J = 0 and theta-bar in {0, pi}, to 1e-30": all(
        v["J"] < 1e-30 and v["theta-bar from {0, pi}"] < 1e-30 for v in on.values()),
         "off the line: J != 0 and theta-bar not in {0, pi}, above 1e-6": all(
             v["J"] > 1e-6 and v["theta-bar from {0, pi}"] > 1e-6 for v in off.values())}
    return {"checks": c, "on the CP line": on, "off it": off}, all(c.values())


def invariants(Mu, Md):
    Hu, Hd = herm(Mu), herm(Md)
    tr = lambda A: mp.re(sum(A[i, i] for i in range(3)))  # noqa: E731
    Cm = Hu * Hd - Hd * Hu
    return [tr(Hu), tr(Hu * Hu), tr(Hu * Hu * Hu), tr(Hd), tr(Hd * Hd), tr(Hd * Hd * Hd), tr(Hu * Hd),
            tr(Hu * Hu * Hd), tr(Hu * Hd * Hd), tr(Hu * Hu * Hd * Hd), mp.re(mp.det(Cm) / I)]


def model(case, basis, p):
    n = len(basis)
    if "no CP" not in case:
        g = [p[i] for i in range(n)]
        tau = mp.mpc(p[n], p[n + 1])
        hu = [p[n + 2], p[n + 3], I * p[n + 4]]
        hd = [p[n + 5], p[n + 6], I * p[n + 7]]
    else:
        g = [mp.mpc(p[2 * i], p[2 * i + 1]) for i in range(n)]
        o = 2 * n
        tau = mp.mpc(p[o], p[o + 1])
        hu = [mp.mpc(p[o + 2 + 2 * i], p[o + 3 + 2 * i]) for i in range(3)]
        hd = [mp.mpc(p[o + 8 + 2 * i], p[o + 9 + 2 * i]) for i in range(3)]
    T = lam_at(basis, g, tau)
    return invariants(mass(T, hu), mass(T, hd))


def nparams(case, n):
    return n + 8 if "no CP" not in case else 2 * n + 14


def jac_rank(case, basis, p, step=mp.mpf("1e-25")):
    cols = []
    for i in range(len(p)):
        pp, pm = list(p), list(p)
        pp[i] += step
        pm[i] -= step
        fp, fm = model(case, basis, pp), model(case, basis, pm)
        cols.append([(a - b) / (2 * step) for a, b in zip(fp, fm)])
    J = mp.matrix([[cols[j][i] for j in range(len(p))] for i in range(len(cols[0]))])
    for i in range(J.rows):
        nrm = mp.sqrt(sum(J[i, j] ** 2 for j in range(J.cols)))
        if nrm > 0:
            for j in range(J.cols):
                J[i, j] /= nrm
    S = mp.svd_r(J, compute_uv=False)
    s = sorted((abs(S[i]) for i in range(S.rows)), reverse=True)
    return sum(1 for x in s if x / s[0] > mp.mpf("1e-20")), [float(x) for x in s]


def Y5(cps):
    rng = random.Random(1374)
    pred = {"w = 6, CP": 10, "w = 6, no CP": 10, "w = 2, CP": 9, "w = 2, no CP": 10}
    out, ok = {}, True
    for case, want in pred.items():
        w = 6 if case.startswith("w = 6") else 2
        basis = cps[w]
        ranks, svs = [], []
        for _ in range(5):
            npar = nparams(case, len(basis))
            p = [mp.mpf(rng.uniform(-1, 1)) for _ in range(npar)]
            n = len(basis) if "no CP" not in case else 2 * len(basis)
            p[n] = mp.mpf(rng.uniform(0.05, 0.45))
            p[n + 1] = mp.mpf(rng.uniform(0.9, 1.6))
            r, s = jac_rank(case, basis, p)
            ranks.append(r)
            svs.append(s)
        out[case] = {"parameters": nparams(case, len(basis)), "ranks": ranks, "predicted": want,
                     "singular values at the first point": svs[0]}
        ok &= all(r == want for r in ranks)
    c = {"the ranks are 10, 10, 9 and 10 at every point": bool(ok)}
    return {"checks": c, **out}, bool(ok)


def Y6(y1, y5):
    return {"the weight reading I allows, least": "w = 6 (k_Phi = 2, global supersymmetry), C(6) = 6 complex constants",
            "parameters against the ten quark observables": {k: v["parameters"] for k, v in y5.items()
                                                             if isinstance(v, dict) and "parameters" in v},
            "the three lepton masses": "tied to the down masses by M_e = M_d (Y2)",
            "what the thirteen would need (a READING in the record, not here)": [
                "a principle fixing the constants and the vev directions",
                "a Clebsch beyond 16.16.10 that breaks M_e = M_d"]}


def main():
    y0, ok0 = Y0()
    y1, ok1 = Y1()
    pairs, OS, OT = the_group()
    y3, ok3, cps = Y3(pairs, OS, OT)
    y2, ok2 = Y2(cps)
    y4, ok4 = Y4(cps)
    y5, ok5 = Y5(cps)
    cells = {"Y0": ok0, "Y1": ok1, "Y2": ok2, "Y3": ok3, "Y4": ok4, "Y5": ok5}
    out = {"arc": "W137", "rule": "W137_RULE.md", "status": "one run", "Y0": y0, "Y1": y1, "Y2": y2, "Y3": y3,
           "Y4": y4, "Y5": y5, "Y6 (read-out)": Y6(y1, y5), "cells": {k: bool(v) for k, v in cells.items()},
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
