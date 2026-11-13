#!/usr/bin/env python3
"""SM-C8 calibration, outside the record's population: SM-C8's instrument (conditioned counts by Fox calculus) and the
duality identities of relays/SM_LITERATURE_NOTE_1.md (sections 4-5), on link complements that are not covers of a word
state (L5a1 and m125, volume 3.6639; L6a4, volume 7.3277; the word states' covers have volumes in multiples of their own).

Modules: V = [[alpha, z beta], [0, beta]] with alpha, beta characters of finite order through H1 and z a twisted cocycle
for l = alpha / beta that is not a coboundary (non-split).  V* = rho^(-T).  For each module and each cusp T_i:
  C1   dim A_V + dim A_V* = h1(dM; V)                                   (half lives, half dies, twisted)
  C2   [h1(V*) - h0(V*)] - [h1(V) - h0(V)] = dim A_V* - h0(dM; V*)
  C3a  n(V | 0) - n(V* | all) = -h0(dM; V) + h0(V) - h0(V*)
  C3b  n(V | 0 elsewhere, S_i) - n(V* | all elsewhere, S*_i) = dim S_i - h0(dM; V) + h0(V) - h0(V*)
       S_i the image of H1(T_i; sub) in H1(T_i; V); S*_i that of H1(T_i; beta^-1) in H1(T_i; V*)
  and SM-C8's quantities, reported: D_ord = n(V | 0 else, S_i) - n(V* | 0 else, S*_i), and the leak.
Plants that must fail somewhere: P1 V in place of V* in C3b; P2 a random line in place of S*_i in C3b;
P3 2 dim A_V = h1(dM; V) in place of C1.
    python3 cal_duality.py [out.json]"""
import sys, json, cmath, math, itertools, pathlib, warnings
import numpy as np
warnings.filterwarnings("ignore")
import snappy
HERE = pathlib.Path(__file__).resolve().parent
rng = np.random.default_rng(20261113)
TOL = 1e-7


def rank(M):
    if M.size == 0: return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > TOL * max(1.0, s[0])))


def null(M):
    if M.shape[0] == 0: return np.eye(M.shape[1], dtype=complex)
    u, s, vh = np.linalg.svd(M)
    r = int(np.sum(s > TOL * max(1.0, s[0]))) if s.size else 0
    return vh[r:].conj().T


def orth(M):
    if M.size == 0 or M.shape[1] == 0: return np.zeros((M.shape[0], 0), dtype=complex)
    u, s, vh = np.linalg.svd(M, full_matrices=False)
    r = int(np.sum(s > TOL * max(1.0, s[0])))
    return u[:, :r]


class Group:
    def __init__(self, name):
        M = snappy.Manifold(name)
        G = M.fundamental_group()
        self.gens = G.generators(); self.rels = G.relators(); self.periph = G.peripheral_curves()
        self.n = len(self.gens); self.k = len(self.periph)
        E = np.array([[r.count(g) - r.count(g.upper()) for g in self.gens] for r in self.rels], dtype=float)
        self.hom = null(E).real            # real basis of homomorphisms to R (H1 free part)
        self.E = E
        import sympy
        ns = sympy.Matrix(E.astype(int)).nullspace()
        self.int_basis = []
        for v in ns:
            den = sympy.ilcm(*[sympy.fraction(x)[1] for x in v])
            self.int_basis.append(np.array([int(x * den) for x in v], dtype=float))

    def idx(self, ch):
        return self.gens.index(ch.lower()), ch.isupper()


def char_vals(G, theta):
    """character g_j -> exp(2 pi i theta_j); theta must satisfy E theta = 0 mod 1 (checked)"""
    assert np.allclose((G.E @ theta) % 1.0, 0) or np.allclose((G.E @ theta) % 1.0, 1)
    return np.exp(2j * math.pi * theta)


def word_mat(rho, G, w):
    M = np.eye(rho[0].shape[0], dtype=complex)
    for ch in w:
        j, inv = G.idx(ch)
        M = M @ (np.linalg.inv(rho[j]) if inv else rho[j])
    return M


def fox(rho, G, w):
    d = rho[0].shape[0]
    D = [np.zeros((d, d), dtype=complex) for _ in range(G.n)]
    pre = np.eye(d, dtype=complex)
    for ch in w:
        j, inv = G.idx(ch)
        if not inv:
            D[j] += pre; pre = pre @ rho[j]
        else:
            pre = pre @ np.linalg.inv(rho[j]); D[j] -= pre
    return np.hstack(D)


class Module:
    def __init__(self, G, rho):
        self.G, self.rho = G, rho; d = self.d = rho[0].shape[0]
        self.rel_ok = all(np.allclose(word_mat(rho, G, r), np.eye(d), atol=1e-8) for r in G.rels)
        J = np.vstack([fox(rho, G, r) for r in G.rels])
        self.Z = null(J)                                                    # Z1(M; V), coordinates on generators
        Bm = np.vstack([rho[j] - np.eye(d) for j in range(G.n)])
        self.h0 = d - rank(Bm); self.dimB = rank(Bm)
        self.h1 = self.Z.shape[1] - self.dimB
        self.cusps = []
        for (mu, la) in G.periph:
            Rm, Rl = word_mat(rho, G, mu), word_mat(rho, G, la)
            Zt = null(np.hstack([-(Rl - np.eye(d)), Rm - np.eye(d)]))         # (z_mu, z_la) with (Rm-1)z_la = (Rl-1)z_mu
            Bt = np.vstack([Rm - np.eye(d), Rl - np.eye(d)])
            h0t = d - rank(Bt)
            self.cusps.append({"Rm": Rm, "Rl": Rl, "Z": Zt, "B": orth(Bt), "h0": h0t,
                               "h1": Zt.shape[1] - rank(Bt), "F": np.vstack([fox(rho, G, mu), fox(rho, G, la)])})
        self.R = np.vstack([c["F"] for c in self.cusps])                     # restriction, generator coords -> boundary
        self.Bnd = self.blockdiag([c["B"] for c in self.cusps])

    def blockdiag(self, blocks):
        rows = 2 * self.d * len(self.cusps)
        out = np.zeros((rows, sum(b.shape[1] for b in blocks)), dtype=complex); c0 = 0
        for i, b in enumerate(blocks):
            out[2 * self.d * i: 2 * self.d * (i + 1), c0: c0 + b.shape[1]] = b; c0 += b.shape[1]
        return out

    def line_cocycles(self, i, vec):
        """cocycles of T_i valued in the line spanned by vec (assumed rho-invariant on T_i), plus coboundaries"""
        c = self.cusps[i]; d = self.d
        P = np.zeros((2 * d, 2), dtype=complex); P[:d, 0] = vec; P[d:, 1] = vec
        cond = np.hstack([-(c["Rl"] - np.eye(d)), c["Rm"] - np.eye(d)]) @ P
        K = null(cond)
        return orth(np.hstack([P @ K, c["B"]]))

    def dim_A(self):
        RZ = self.R @ self.Z
        return rank(np.hstack([RZ, self.Bnd])) - rank(self.Bnd)

    def h0_bd(self): return sum(c["h0"] for c in self.cusps)
    def h1_bd(self): return sum(c["h1"] for c in self.cusps)

    def n_cond(self, blocks):
        """dim {x in H1(M; V): restriction lies in the boundary condition given per cusp (column space incl. B1_T)}"""
        Bt = orth(self.blockdiag(blocks))
        P = np.eye(Bt.shape[0], dtype=complex) - Bt @ Bt.conj().T
        return self.Z.shape[1] - rank(P @ self.R @ self.Z) - self.dimB

    def quot_dim(self, i, blk):
        return rank(blk) - rank(self.cusps[i]["B"])


def build(G, a_theta, b_theta):
    al, be = char_vals(G, a_theta), char_vals(G, b_theta)
    l = al / be
    J = np.vstack([np.hstack([np.array([[x]]) for x in fox([np.array([[v]]) for v in l], G, r)[0]]) for r in G.rels])
    Zl = null(J)
    Bl = orth((l - 1).reshape(-1, 1))
    if Zl.shape[1] - rank(Bl) < 1: return None
    # a cocycle not a coboundary: project a random element of Z1 off B1
    z = Zl @ (rng.normal(size=Zl.shape[1]) + 1j * rng.normal(size=Zl.shape[1]))
    if Bl.shape[1]: z = z - Bl @ (Bl.conj().T @ z)
    if np.linalg.norm(z) < 1e-6: return None
    z = z / np.linalg.norm(z)
    rho = [np.array([[al[j], z[j] * be[j]], [0, be[j]]], dtype=complex) for j in range(G.n)]
    rhos = [np.linalg.inv(m).T for m in rho]
    return Module(G, rho), Module(G, rhos)


def main():
    out_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "cal_duality.json"
    rows = []; summ = {}
    for name, Nq in (("L5a1", (2, 3, 4, 5, 6)), ("m125", (2, 3, 4, 5, 6)), ("L6a4", (2, 3, 4))):
        G = Group(name)
        # characters through the free part: integer combinations of an integral basis of Hom(H1, Z)
        basis = np.array(G.int_basis)       # exact integral basis of Hom(H1, Z) (sympy), not the SVD's rotated one
        cnt = 0
        for N in Nq:
            for ca in itertools.product(range(N), repeat=len(basis)):
                for cb in itertools.product(range(N), repeat=len(basis)):
                    if ca == cb: continue
                    ta = (np.array(ca) @ basis) / N; tb = (np.array(cb) @ basis) / N
                    mm = build(G, ta, tb)
                    if mm is None: continue
                    V, Vs = mm
                    if not (V.rel_ok and Vs.rel_ok): rows.append({"manifold": name, "error": "relators"}); continue
                    hb = V.h0_bd(); hbs = Vs.h0_bd()
                    dA, dAs = V.dim_A(), Vs.dim_A()
                    r = {"manifold": name, "N": N, "a": list(ca), "b": list(cb), "h0": [V.h0, Vs.h0], "h1": [V.h1, Vs.h1],
                         "h0_bd": [hb, hbs], "h1_bd": [V.h1_bd(), Vs.h1_bd()], "dimA": [dA, dAs],
                         "cusp_h1": [c["h1"] for c in V.cusps], "cusp_h0": [c["h0"] for c in V.cusps]}
                    r["C1"] = dA + dAs == V.h1_bd() == Vs.h1_bd()
                    r["C2"] = (Vs.h1 - Vs.h0) - (V.h1 - V.h0) == dAs - hbs
                    zero = [c["B"] for c in V.cusps]; zero_s = [c["B"] for c in Vs.cusps]
                    allv = [c["Z"] for c in V.cusps]; all_s = [c["Z"] for c in Vs.cusps]
                    base = - hb + V.h0 - Vs.h0
                    r["C3a"] = V.n_cond(zero) - Vs.n_cond(all_s) == base
                    r["P3_fails"] = not (2 * dA == V.h1_bd())
                    r["cusps"] = []
                    for i in range(G.k):
                        if V.cusps[i]["h1"] == 0:
                            r["cusps"].append({"i": i, "vacuous": True}); continue
                        S = V.line_cocycles(i, np.array([1, 0], dtype=complex))
                        Ss = Vs.line_cocycles(i, np.array([0, 1], dtype=complex))
                        dS = V.quot_dim(i, S)
                        bl = [zero[j] if j != i else S for j in range(G.k)]
                        bls_all = [all_s[j] if j != i else Ss for j in range(G.k)]
                        bls_zero = [zero_s[j] if j != i else Ss for j in range(G.k)]
                        nV = V.n_cond(bl); nVs_all = Vs.n_cond(bls_all); nVs_zero = Vs.n_cond(bls_zero)
                        c3b = nV - nVs_all == dS - hb + V.h0 - Vs.h0
                        # P1: V in place of V*
                        bl_all_V = [allv[j] if j != i else S for j in range(G.k)]
                        p1 = not (nV - V.n_cond(bl_all_V) == dS - hb + V.h0 - Vs.h0)
                        # P2: a random line of H1(T_i; V*) in place of S*_i
                        c = Vs.cusps[i]
                        rnd = orth(np.hstack([c["Z"] @ (rng.normal(size=(c["Z"].shape[1], 1)) + 0j), c["B"]]))
                        p2 = not (nV - Vs.n_cond([all_s[j] if j != i else rnd for j in range(G.k)]) == dS - hb + V.h0 - Vs.h0)
                        r["cusps"].append({"i": i, "vacuous": False, "split_on_T": bool(np.allclose(V.cusps[i]["Rm"][0, 1], 0)
                                           and np.allclose(V.cusps[i]["Rl"][0, 1], 0)), "dimS": dS,
                                           "dimS*": Vs.quot_dim(i, Ss), "n(V|0,S)": nV, "n(V*|all,S*)": nVs_all,
                                           "n(V*|0,S*)": nVs_zero, "D_ord": nV - nVs_zero, "leak": nVs_all - nVs_zero,
                                           "C3b": bool(c3b), "P1_fails": bool(p1), "P2_fails": bool(p2)})
                    rows.append(r); cnt += 1
        summ[name] = cnt
        print(name, cnt, "modules", flush=True)
    good = [r for r in rows if "error" not in r]
    cusp = [(r, c) for r in good for c in r["cusps"] if not c["vacuous"]]
    s = {"modules": summ, "relator_errors": sum("error" in r for r in rows),
         "C1": [sum(r["C1"] for r in good), len(good)], "C2": [sum(r["C2"] for r in good), len(good)],
         "C3a": [sum(r["C3a"] for r in good), len(good)],
         "C3b": [sum(c["C3b"] for _, c in cusp), len(cusp)],
         "dimS_plus_dimS*_eq_h1T": [sum(c["dimS"] + c["dimS*"] == r["cusp_h1"][c["i"]] for r, c in cusp), len(cusp)],
         "vacuous_joins": sum(c["vacuous"] for r in good for c in r["cusps"]),
         "plants": {"P1 V for V*: fails on": [sum(c["P1_fails"] for _, c in cusp), len(cusp)],
                    "P2 random line for S*: fails on": [sum(c["P2_fails"] for _, c in cusp), len(cusp)],
                    "P3 2dimA = h1(dM): fails on": [sum(r["P3_fails"] for r in good), len(good)]},
         "index_h1(V*)-h1(V)_values": sorted(set(r["h1"][1] - r["h1"][0] for r in good)),
         "D_ord_values": sorted(set(c["D_ord"] for _, c in cusp)), "leak_values": sorted(set(c["leak"] for _, c in cusp))}
    json.dump({"summary": s, "rows": rows}, open(out_path, "w"), indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o))
    print(json.dumps(s, indent=1))


if __name__ == "__main__":
    main()
