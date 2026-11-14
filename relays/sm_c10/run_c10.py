#!/usr/bin/env python3
"""SM-C10: the one-tick object, twisted duality on the tick's family (card relays/cards/SM_C10_the-one-tick-object.md,
committed and pushed before this run).  Own presentation of M_n, the mapping torus of phi^n, phi: x -> yx, y -> x
(abelianisation J = [[1,1],[1,0]], det -1, J^2 = LR); n = 1..6; SnapPy only for the cross-check of names.
Checks K1-K5, plants P1-P3, the census of the twisted and untwisted gaps.  Data-free.
    python3 run_c10.py [out.json]"""
import sys, json, math, itertools, pathlib, warnings
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
rng = np.random.default_rng(20261114)
TOL = 1e-7
NMAX, ORDERS = 6, (2, 3, 4, 5, 6)
SNAPPY = {1: "b-+R", 2: "b++LR", 3: "b-+RLR", 4: "b++LRLR", 5: "b-+RLRLR", 6: "b++LRLRLR"}


# ----------------------------------------------------------------------------------------------- free group words
def red(w):
    out = []
    for g in w:
        if out and out[-1] == -g: out.pop()
        else: out.append(g)
    return out


def winv(w): return [-g for g in reversed(w)]


PHI = {1: [2, 1], 2: [1]}                       # x -> yx, y -> x


def apply(m, w):
    out = []
    for g in w:
        out += m[g] if g > 0 else winv(m[-g])
    return red(out)


def phi_power(n):
    m = {1: [1], 2: [2]}
    for _ in range(n): m = {g: apply(PHI, m[g]) for g in (1, 2)}
    return m


class Group:
    """M_n: generators x=1, y=2, t=3"""
    def __init__(self, n):
        self.n = n; m = phi_power(n)
        self.rels = [red([3, 1, -3] + winv(m[1])), red([3, 2, -3] + winv(m[2]))]
        lam = [1, 2, -1, -2]
        img = apply(m, lam)
        self.s = 1 if n % 2 == 0 else -1
        assert img == (lam if self.s == 1 else winv(lam)), "phi^n([x,y]) = [x,y]^((-1)^n)"
        self.mu, self.lam = [3], lam
        self.prel = [1, 2, -1] + ([-2] if self.s == 1 else [2])        # m l m^-1 l^(-s) in peripheral letters m=1, l=2
        self.E = np.array([[sum((g == k) - (g == -k) for g in r) for k in (1, 2, 3)] for r in self.rels])


def mat_of(rho, w):
    M = np.eye(rho[1].shape[0], dtype=complex)
    for g in w: M = M @ (rho[g] if g > 0 else np.linalg.inv(rho[-g]))
    return M


def fox(rho, w, ngen):
    d = rho[1].shape[0]
    D = {k: np.zeros((d, d), dtype=complex) for k in range(1, ngen + 1)}
    pre = np.eye(d, dtype=complex)
    for g in w:
        if g > 0: D[g] += pre; pre = pre @ rho[g]
        else: pre = pre @ np.linalg.inv(rho[-g]); D[-g] -= pre
    return np.hstack([D[k] for k in range(1, ngen + 1)])


def rank(M):
    if M.size == 0: return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > TOL * max(1.0, s[0])))


def null(M):
    u, s, vh = np.linalg.svd(M)
    r = int(np.sum(s > TOL * max(1.0, s[0]))) if s.size else 0
    return vh[r:].conj().T


def orth(M):
    if M.size == 0 or M.shape[1] == 0: return np.zeros((M.shape[0], 0), dtype=complex)
    u, s, vh = np.linalg.svd(M, full_matrices=False)
    return u[:, :int(np.sum(s > TOL * max(1.0, s[0])))]


def coh(G, rho):
    """h0, h1, peripheral h0, h1, dim A for the module rho on M_n"""
    d = rho[1].shape[0]
    assert all(np.allclose(mat_of(rho, r), np.eye(d), atol=1e-8) for r in G.rels), "not a representation"
    Z = null(np.vstack([fox(rho, r, 3) for r in G.rels]))
    Bm = np.vstack([rho[k] - np.eye(d) for k in (1, 2, 3)])
    h0 = d - rank(Bm); dimB = rank(Bm); h1 = Z.shape[1] - dimB
    pr = {1: mat_of(rho, G.mu), 2: mat_of(rho, G.lam)}
    assert np.allclose(mat_of(pr, G.prel), np.eye(d), atol=1e-8), "peripheral relator"
    Zt = null(fox(pr, G.prel, 2))
    Bt = np.vstack([pr[1] - np.eye(d), pr[2] - np.eye(d)])
    h0b = d - rank(Bt); h1b = Zt.shape[1] - rank(Bt)
    R = np.vstack([fox(rho, G.mu, 3), fox(rho, G.lam, 3)])
    Bo = orth(Bt)
    dimA = rank(np.hstack([R @ Z, Bo])) - rank(Bo)
    return {"h0": h0, "h1": h1, "h0b": h0b, "h1b": h1b, "A": dimA}


def characters(G):
    """all characters of H1(M_n) of order dividing some N in ORDERS, as theta in (Q/Z)^3"""
    out = set()
    for N in ORDERS:
        for th in itertools.product(range(N), repeat=3):
            if all(sum(int(G.E[i, k]) * th[k] for k in range(3)) % N == 0 for i in range(len(G.rels))):
                out.add(tuple(Fr(a, N) for a in th))
    return sorted(out)


def cval(th): return {k + 1: complex(np.exp(2j * math.pi * float(th[k]))) for k in range(3)}


def module(G, a, b):
    al, be = cval(a), cval(b)
    l = {k: al[k] / be[k] for k in (1, 2, 3)}
    lr = {k: np.array([[l[k]]]) for k in (1, 2, 3)}
    Zl = null(np.vstack([fox(lr, r, 3) for r in G.rels]))
    Bl = orth(np.array([[l[k] - 1] for k in (1, 2, 3)]))
    if Zl.shape[1] - rank(Bl) < 1: return None
    z = Zl @ (rng.normal(size=Zl.shape[1]) + 1j * rng.normal(size=Zl.shape[1]))
    if Bl.shape[1]: z = z - Bl @ (Bl.conj().T @ z)
    if np.linalg.norm(z) < 1e-6: return None
    z = z / np.linalg.norm(z)
    return {k: np.array([[al[k], z[k - 1] * be[k]], [0, be[k]]], dtype=complex) for k in (1, 2, 3)}


def dual(rho): return {k: np.linalg.inv(m).T for k, m in rho.items()}
def twist(rho, w): return {k: m * w[k] for k, m in rho.items()}


def k12(cV, cP):
    """K1 and K2 for V with the partner P (P = V* (x) w in the theorem)"""
    k1 = cV["A"] + cP["A"] == cV["h1b"] and cV["h1b"] == cP["h1b"]
    k2 = (cP["h1"] - cP["h0"]) - (cV["h1"] - cV["h0"]) == cP["A"] - cP["h0b"]
    return k1, k2


def snappy_check():
    import snappy
    v0 = float(snappy.Manifold("m000").volume()); out = {}
    for n, nm in SNAPPY.items():
        M = snappy.Manifold(nm)
        G = Group(n)
        # abelianisation of this seat's presentation: Smith form of the relator matrix
        import sympy
        from sympy.matrices.normalforms import smith_normal_form
        S = smith_normal_form(sympy.Matrix(G.E.tolist()), domain=sympy.ZZ)
        diag = [abs(int(S[i, i])) for i in range(min(S.shape))]
        free = 3 - sum(1 for d in diag if d != 0)
        tors = sorted(d for d in diag if d > 1)
        H = M.homology()
        out[n] = {"name": nm, "identify": [str(x) for x in M.identify()][:1], "orientable": M.is_orientable(),
                  "volume_ratio": round(float(M.volume()) / v0, 6), "H1_snappy": str(H),
                  "H1_own": {"free": free, "torsion": tors},
                  "orientation_cover": ([str(x) for x in M.orientation_cover().identify()][:1] if not M.is_orientable() else None)}
    return out


def main():
    out_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "c10_results.json"
    res = {"snappy": snappy_check(), "levels": {}}
    sn = res["snappy"]
    res["K3"] = {"non_orientable_exactly_odd": all(sn[n]["orientable"] == (n % 2 == 0) for n in sn),
                 "volume_n_times_m000": all(abs(sn[n]["volume_ratio"] - n) < 1e-4 for n in sn),
                 "cover_of_odd_is_2n": {n: (sn[n]["orientation_cover"], sn[2 * n]["identify"] if 2 * n in sn else None)
                                        for n in sn if n % 2 == 1}}
    print(json.dumps(res["snappy"], indent=1), flush=True)
    for n in range(1, NMAX + 1):
        G = Group(n); chars = characters(G)
        w = {1: 1.0, 2: 1.0, 3: (-1.0 if n % 2 else 1.0)}
        # P2's wrong twists: order-2 characters trivial on t (the torsion's), for odd n
        chi2 = [c for c in chars if c[2] == 0 and any(c) and all(2 * x % 1 == 0 for x in c)] if n % 2 else []
        G2 = Group(2 * n) if (n % 2 and 2 * n <= 12) else None
        rows = []
        for a, b in itertools.permutations(chars, 2):
            V = module(G, a, b)
            if V is None: continue
            Vs = dual(V); Vsw = twist(Vs, w); Vw = twist(V, w)
            cV, cVs, cVsw, cVw = coh(G, V), coh(G, Vs), coh(G, Vsw), coh(G, Vw)
            k1, k2 = k12(cV, cVsw); p1 = k12(cV, cVs)
            r = {"a": [str(x) for x in a], "b": [str(x) for x in b], "record_like": a[2] == 0 and b[2] == 0,
                 "h1": [cV["h1"], cVs["h1"], cVsw["h1"], cVw["h1"]], "h0": [cV["h0"], cVs["h0"], cVsw["h0"]],
                 "h0b": cV["h0b"], "h1b": cV["h1b"], "A": [cV["A"], cVs["A"], cVsw["A"]],
                 "K1": k1, "K2": k2, "P1_fails": not (p1[0] and p1[1]),
                 "g_w": cVsw["h1"] - cV["h1"], "g_0": cVs["h1"] - cV["h1"]}
            if chi2:
                fails = False
                for c in chi2:
                    cw = cval(c); w2 = {k: w[k] * (1 if abs(cw[k] - 1) < 1e-9 else -1) for k in (1, 2, 3)}
                    q = k12(cV, coh(G, twist(Vs, w2)))
                    fails |= not (q[0] and q[1])
                r["P2_fails"] = fails
            if G2 is not None:
                V2 = {1: V[1], 2: V[2], 3: V[3] @ V[3]}
                h2 = coh(G2, V2)["h1"]
                r["K4"] = cV["h1"] + cVw["h1"] == h2
                r["P3_fails"] = 2 * cV["h1"] != h2
            rows.append(r)
        L = {"n": n, "characters": len(chars), "modules": len(rows),
             "record_like_modules": sum(r["record_like"] for r in rows),
             "K1": [sum(r["K1"] for r in rows), len(rows)], "K2": [sum(r["K2"] for r in rows), len(rows)],
             "P1_fails_on": [sum(r["P1_fails"] for r in rows), len(rows)],
             "P2_fails_on": [sum(r.get("P2_fails", False) for r in rows), len(rows)] if chi2 else "no wrong twist exists",
             "K4": [sum(r["K4"] for r in rows), len(rows)] if G2 is not None else "n even, or M_2n beyond 12",
             "P3_fails_on": [sum(r["P3_fails"] for r in rows), len(rows)] if G2 is not None else None,
             "g_w_ne_g_0": [sum(r["g_w"] != r["g_0"] for r in rows), len(rows)],
             "census_g_w": dict(Counter(str(r["g_w"]) for r in rows)), "census_g_0": dict(Counter(str(r["g_0"]) for r in rows)),
             "record_like_g_w_ne_g_0": [sum(r["g_w"] != r["g_0"] for r in rows if r["record_like"]),
                                        sum(r["record_like"] for r in rows)]}
        res["levels"][n] = {"summary": L, "rows": rows}
        print(json.dumps(L), flush=True)
    S = {n: res["levels"][n]["summary"] for n in res["levels"]}
    odd = [S[n] for n in S if n % 2]; even = [S[n] for n in S if n % 2 == 0]
    res["summary"] = {
        "K1_all": all(s["K1"][0] == s["K1"][1] for s in S.values()), "K2_all": all(s["K2"][0] == s["K2"][1] for s in S.values()),
        "K3": res["K3"]["non_orientable_exactly_odd"] and res["K3"]["volume_n_times_m000"],
        "K4_all_odd": all(isinstance(s["K4"], list) and s["K4"][0] == s["K4"][1] for s in odd if isinstance(s["K4"], list)),
        "K5_reading": {"even_n_g_w_eq_g_0_everywhere": all(s["g_w_ne_g_0"][0] == 0 for s in even),
                       "odd_n_g_w_ne_g_0_somewhere": any(s["g_w_ne_g_0"][0] > 0 for s in odd),
                       "P1_fails_on_some_odd_module": any(s["P1_fails_on"][0] > 0 for s in odd),
                       "P1_never_fails_on_even": all(s["P1_fails_on"][0] == 0 for s in even)},
        "P2_fires": any(isinstance(s["P2_fails_on"], list) and s["P2_fails_on"][0] > 0 for s in odd),
        "P3_fires": any(s["P3_fails_on"] and s["P3_fails_on"][0] > 0 for s in odd)}
    s = res["summary"]
    theorem_ok = s["K1_all"] and s["K2_all"] and s["K4_all_odd"]
    k5 = all(s["K5_reading"].values())
    s["outcome"] = "B" if not theorem_ok else ("A" if k5 else "C")
    json.dump(res, open(out_path, "w"), indent=1, default=str)
    print(json.dumps(res["summary"], indent=1, default=str))


if __name__ == "__main__":
    main()
