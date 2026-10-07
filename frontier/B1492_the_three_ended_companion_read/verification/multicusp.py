#!/usr/bin/env python3
"""B1492 (draft): the class index of the harmonic frame on a manifold with SEVERAL cusps, numerically, with the cusp
decomposition the rules of 2026-10-07 require.

For a representation E of pi_1(N) (SnapPy's presentation; cusps i = 1..m with peripheral words mu_i, lam_i):
  a0 = h^0(N; E), a1 = h^1(N; E) from the Fox matrices; for each cusp t0_i = h^0(T_i; E); r1 = rank of the restriction
  H^1(N; E) -> (+) H^1(T_i; E) (the block [[d1, 0], [R, BT]] with every cusp stacked); n = a1 - r1 (the interior classes);
  I(E) = n(E) - n(E*).  A class z is 'dead' on cusp i when its restriction to T_i is a coboundary there; k = the number
  of cusps where it is not; m_A = cusps where the character is trivial; m_B = cusps where only nu^4 is; b0 = [nu^4 = 1].
The four = nu (x) (H -> g H g^* / |det g|) from SnapPy's SL2C holonomy at 40 digits (the four does not depend on the lift).
Extensions W1 = [[V, z], [0, 1]] at a cocycle z; Lambda^2 by the exterior square.  Ranks by SVD with a tolerance.
Controls: at one cusp the numbers must equal B1485's exact ones on m135 and m136 (every census row and member reading)."""
import sys, json, itertools, pathlib
import snappy
from mpmath import mp, mpf, mpc, matrix, eye, zeros, inverse, svd_c
mp.dps = 40
TOL = mpf(10) ** -24


def num(x): return mpf(str(x).replace(" ", ""))


def rank(M):
    if M.rows == 0 or M.cols == 0: return 0
    s = svd_c(M, compute_uv=False); top = max(1, abs(s[0])); return sum(1 for i in range(len(s)) if abs(s[i]) > TOL * top)


def nullspace(M):
    """an orthonormal basis of {v : M v = 0} (columns), by SVD"""
    U, s, Vh = svd_c(M, full_matrices=True); r = sum(1 for i in range(len(s)) if abs(s[i]) > TOL * max(1, abs(s[0]) if len(s) else 1))
    return [Vh[i, :].H for i in range(r, M.cols)]


def word(w, G):
    n = next(iter(G.values())).rows; R = eye(n)
    for ch in w: R = R * (G[ch] if ch.islower() else inverse(G[ch.lower()]))
    return R


def fox(w, G, gens):
    n = next(iter(G.values())).rows; val = eye(n); dd = {g: zeros(n) for g in gens}
    for ch in w:
        g = ch.lower()
        if ch.islower(): dd[g] += val; val = val * G[g]
        else: val = val * inverse(G[g]); dd[g] -= val
    return dd


def stack(bs):
    M = zeros(sum(b.rows for b in bs), bs[0].cols); r = 0
    for b in bs: M[r:r + b.rows, :] = b; r += b.rows
    return M


def hcat(bs):
    M = zeros(bs[0].rows, sum(b.cols for b in bs)); c = 0
    for b in bs: M[:, c:c + b.cols] = b; c += b.cols
    return M


def dual(E): return {g: inverse(M).T for g, M in E.items()}


class Site:
    def __init__(self, name):
        self.name = name; self.M = snappy.ManifoldHP(name); G = self.M.fundamental_group()
        self.gens = G.generators(); self.rels = G.relators(); self.cusps = G.peripheral_curves()
        self.rho = {g: matrix([[mpc(num(G.SL2C(g)[i, j].real()), num(G.SL2C(g)[i, j].imag())) for j in range(2)] for i in range(2)]) for g in self.gens}
        self.m = len(self.cusps)

    def four(self, nu):
        def f4(Mx):
            Ms = matrix([[Mx[j, i].conjugate() for j in range(2)] for i in range(2)])
            basis = [matrix([[1, 0], [0, 0]]), matrix([[0, 0], [0, 1]]), matrix([[0, 1], [1, 0]]), matrix([[0, 1j], [-1j, 0]])]
            cols = []
            for H in basis:
                Hp = Mx * H * Ms; cols.append([Hp[0, 0], Hp[1, 1], (Hp[0, 1] + Hp[1, 0]) / 2, (Hp[0, 1] - Hp[1, 0]) / (2j)])
            return matrix([[cols[j][i] for j in range(4)] for i in range(4)])
        return {g: nu[g] * f4(self.rho[g]) for g in self.gens}

    def pieces(self, E):
        n = next(iter(E.values())).rows; Id = eye(n); G = dict(E)
        d0 = stack([E[g] - Id for g in self.gens]); d1 = stack([hcat([fox(r, G, self.gens)[g] for g in self.gens]) for r in self.rels])
        R = []; BT = []; t0 = []
        for (mu, lam) in self.cusps:
            fm, fl = fox(mu, G, self.gens), fox(lam, G, self.gens)
            R.append(stack([hcat([fm[g] for g in self.gens]), hcat([fl[g] for g in self.gens])]))
            B = stack([word(mu, G) - Id, word(lam, G) - Id]); BT.append(B); t0.append(n - rank(B))
        return dict(n=n, d0=d0, d1=d1, R=R, BT=BT, t0=t0)

    def counts(self, E):
        p = self.pieces(E); n = p["n"]; ng = len(self.gens)
        r0, rd1 = rank(p["d0"]), rank(p["d1"]); a0 = n - r0; a1 = ng * n - rd1 - r0
        # the restriction to all cusps at once: block [[d1, 0..0], [R_1, BT_1, 0..], [R_2, 0, BT_2, ..], ...]
        rows_R = sum(R.rows for R in p["R"]); cols_B = sum(B.cols for B in p["BT"])
        block = zeros(p["d1"].rows + rows_R, p["d1"].cols + cols_B); block[:p["d1"].rows, :p["d1"].cols] = p["d1"]
        r, c = p["d1"].rows, p["d1"].cols
        for R, B in zip(p["R"], p["BT"]):
            block[r:r + R.rows, :R.cols] = R; block[r:r + R.rows, c:c + B.cols] = B; r += R.rows; c += B.cols
        rBT = sum(rank(B) for B in p["BT"]); r1 = rank(block) - rd1 - rBT
        return dict(a0=a0, a1=a1, t0=p["t0"], t0_sum=sum(p["t0"]), r1=r1, n=a1 - r1)

    def classes(self, E):
        """the interior classes (restricting to a coboundary on EVERY cusp at once: the z-part of the nullspace of the block
        [[d1, 0], [R, BT]]) modulo B^1, and a complement of them in Z^1 modulo B^1 ('other'); each with its per-cusp pattern"""
        p = self.pieces(E); n = p["n"]; ng = len(self.gens)
        rows_R = sum(R.rows for R in p["R"]); cols_B = sum(B.cols for B in p["BT"])
        block = zeros(p["d1"].rows + rows_R, p["d1"].cols + cols_B); block[:p["d1"].rows, :p["d1"].cols] = p["d1"]
        r, c = p["d1"].rows, p["d1"].cols
        for R, B in zip(p["R"], p["BT"]):
            block[r:r + R.rows, :R.cols] = R; block[r:r + R.rows, c:c + B.cols] = B; r += R.rows; c += B.cols
        Bcols = [p["d0"][:, j] for j in range(n)]
        def indep(vs): return rank(hcat(vs)) if vs else 0
        r0 = indep(Bcols)
        def dead_on(z, i):
            R, Bt = p["R"][i], p["BT"][i]; return rank(hcat([Bt, R * z])) == rank(Bt)
        interior = []
        for v in nullspace(block):
            z = v[:ng * n, :]
            if indep(Bcols + [q for q, _ in interior] + [z]) > r0 + len(interior): interior.append((z, [dead_on(z, i) for i in range(self.m)]))
        other = []
        for z in nullspace(p["d1"]):
            if indep(Bcols + [q for q, _ in interior] + [q for q, _ in other] + [z]) > r0 + len(interior) + len(other): other.append((z, [dead_on(z, i) for i in range(self.m)]))
        return interior, other

    def extension(self, V, z):
        n = next(iter(V.values())).rows; out = {}
        for k, g in enumerate(self.gens):
            W = zeros(n + 1); W[:n, :n] = V[g]
            for i in range(n): W[i, n] = z[k * n + i]
            W[n, n] = 1; out[g] = W
        return out

    def index(self, E):
        A = self.counts(E); B = self.counts(dual(E)); return dict(I=A["n"] - B["n"], E=A, Edual=B)


def ext2(M):
    n = M.rows; pairs = list(itertools.combinations(range(n), 2)); E = zeros(len(pairs))
    for a, (i, j) in enumerate(pairs):
        for b, (k, l) in enumerate(pairs): E[a, b] = M[i, k] * M[j, l] - M[i, l] * M[j, k]
    return E


def survey(name):
    S = Site(name); out = dict(name=name, gens=S.gens, rels=S.rels, cusps=S.m, rows=[])
    for vals in itertools.product((1, -1), repeat=len(S.gens)):
        nu = dict(zip(S.gens, vals))
        # a character: every relator must have even exponent sum per generator in its sign pattern
        if any(sum((1 if ch.islower() else -1) for ch in r if ch.lower() == g) % 2 and nu[g] == -1 for r in S.rels for g in S.gens): continue
        V = S.four(nu); cV = S.counts(V); interior, other = S.classes(V)
        def val(w): v = 1
        cusp_triv = []
        for (mu, lam) in S.cusps:
            vm = 1
            for ch in mu: vm *= nu[ch.lower()]
            vl = 1
            for ch in lam: vl *= nu[ch.lower()]
            cusp_triv.append(vm == 1 and vl == 1)
        row = dict(nu=nu, cusp_trivial=[bool(x) for x in cusp_triv], m_A=sum(cusp_triv), b0=1, V=cV, interior=len(interior), other=len(other), readings=[])
        for label, group in (("interior", interior), ("other", other)):
            for idx, (z, dead) in enumerate(group):
                W = S.extension(V, z); L2 = {g: ext2(W[g]) for g in S.gens}
                a, b = S.index(W), S.index(L2); k = sum(1 for d in dead if not d)
                row["readings"].append(dict(cls=f"{label} {idx}", dead_on_cusps=dead, k=k, I_W1=a["I"], I_L2W1=b["I"], W1=a["E"], W1dual=a["Edual"],
                                            floor=k - row["m_A"] - row["b0"], ceiling=2 * row["m_A"] + 0 - row["b0"]))
        out["rows"].append(row); print(json.dumps({k: v for k, v in row.items() if k != "readings"}), [(r["cls"], r["k"], r["I_W1"], r["I_L2W1"]) for r in row["readings"]], flush=True)
    return out


if __name__ == "__main__":
    for name in sys.argv[1:]:
        json.dump(survey(name), open(pathlib.Path(__file__).resolve().parent / f"survey_{name.replace('~', '_')}.json", "w"), indent=1, default=str)
