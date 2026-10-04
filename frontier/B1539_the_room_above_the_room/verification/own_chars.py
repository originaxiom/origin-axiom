"""B1539 -- the library: the covers' own characters.

The abelianisation of pi_1 N on route R's Schreier generators, the characters of H_1(N) of order dividing m, their Galois orbits
(Lemma C), the frame's supplies at an own character in two routes, and the abelian covers N_A (Lemma A').

A cover N of M (sm:B1536's cover_lib: a transitive permutation action of Gamma on X with base point 0) is read by route_r.PCover:
Schreier generators s_j (the non-tree edges (x, g)), their base words w_j, and the relators rewritten at every coset.
H_1(N) = Z^n / (relator rows).  With U R V = D (PARI matsnf, R padded to a square matrix), the generator s_j has coordinates
row j of V, reduced mod D's diagonal: free coordinates (d_i = 0) and torsion coordinates (d_i > 1).
A character of order dividing m is c = (c_i): c_i in Z/m on a free coordinate, and c_i in (m/g_i) Z/m with g_i = gcd(m, d_i)
on a torsion one (so that d_i c_i = 0 mod m).  Its value on s_j is zeta_m^(sum_i c_i V[j][i]).
  - route R' (frame_own): sm:B1536's route_r on the cover, by path, unchanged;
  - route P' (frame_own_p): sm:B1538's punct_present on the cover's own presentation, by path, unchanged;
  - the two routes read at two different primes (route_primes), so that their agreement also certifies the reductions.
Drafted as the golden covers dossier's gc_own_chars.py (controls there: K1 36, K2 14, K3 52 readings, all hold)."""
import importlib.util
import itertools
import sys
from math import gcd
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
B1536V = ROOT / "frontier" / "B1536_the_finite_covers" / "verification"


def _load(alias, path):
    if alias not in sys.modules:
        if str(B1536V) not in sys.path:
            sys.path.append(str(B1536V))
        spec = importlib.util.spec_from_file_location(alias, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


R = _load("b1539_b1536_route_r", B1536V / "route_r.py")      # allocates PARI's stack: load first
CL = _load("b1539_b1536_cover_lib", B1536V / "cover_lib.py")
GF = _load("b1539_b1536_gf", B1536V / "gf.py")
RN = _load("b1539_b1536_route_n", B1536V / "route_n.py")
from cypari import pari  # noqa: E402


class Ab:
    """the abelianisation of pi_1 N on cov's Schreier generators"""

    def __init__(self, cov):
        n = len(cov.sgens)
        rows = []
        for w in cov.rels:
            v = [0] * n
            for j, e in w:
                v[j] += e
            rows.append(v)
        while len(rows) < n:
            rows.append([0] * n)
        assert len(rows) == n, "more relators than generators: pad the other way"
        A = pari.matrix(n, n, [x for r in rows for x in r])
        U, V, D = pari.matsnf(A, 1)
        self.n = n
        self.d = [abs(int(D[i, i])) for i in range(n)]
        self.V = [[int(V[i, j]) for j in range(n)] for i in range(n)]
        # check: U A V = D, and every relator maps to 0 in Z^n / D
        UA = [[sum(int(U[i, k]) * rows[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        UAV = [[sum(UA[i][k] * self.V[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        assert all(UAV[i][j] == (int(D[i, j])) for i in range(n) for j in range(n)), "U A V != D"
        for r in rows:
            img = [sum(r[j] * self.V[j][i] for j in range(n)) for i in range(n)]
            assert all((img[i] % self.d[i] == 0) if self.d[i] else img[i] == 0 for i in range(n)), "a relator survives"
        self.coords = [i for i in range(n) if self.d[i] != 1]
        self.free = [i for i in self.coords if self.d[i] == 0]
        self.torsion = [(i, self.d[i]) for i in self.coords if self.d[i] > 1]

    def characters(self, m):
        """every character of order dividing m, as a tuple c over self.coords (exponents of zeta_m)"""
        ranges = []
        for i in self.coords:
            if self.d[i] == 0:
                ranges.append(range(m))
            else:
                g = gcd(m, self.d[i])
                ranges.append(range(0, m, m // g))
        return list(itertools.product(*ranges))

    def coordinates(self, exps, m):
        """the inverse: the character with these values on the Schreier generators, as c over self.coords, or None if the
        values are not a character of H_1(N) (non-zero on a trivial Smith coordinate, or not killed by a torsion order)"""
        Vi = pari.matrix(self.n, self.n, [x for r in self.V for x in r]) ** -1
        full = [sum(int(Vi[i, j]) * exps[j] for j in range(self.n)) % m for i in range(self.n)]
        # exps_j = sum_i full_i V[j][i]  <=>  exps = V full (column convention): check the convention explicitly
        for i in range(self.n):
            if self.d[i] == 1 and full[i] % m:
                return None
            if self.d[i] > 1 and (self.d[i] * full[i]) % m:
                return None
        c = tuple(full[i] for i in self.coords)
        return c if self.exponents(c, m) == list(exps) else None

    def exponents(self, c, m):
        """the character c's values on the Schreier generators, as exponents of zeta_m"""
        return [sum(ci * self.V[j][i] for ci, i in zip(c, self.coords)) % m for j in range(self.n)]


def frame_own(cov, rho_np, exps, m, p):
    """sm:B1515's frame at the own character nu = zeta_m^exps (route_r's modules, as punct_four's supplies_r)"""
    r = pari.znprimroot(p) ** ((p - 1) // m)
    r = int(pari.lift(r))
    nu = [pow(r, e, p) for e in exps]
    rw = [R.base_word(rho_np, w, p) for w in cov.sword]
    Veta = R.CMod([mm * pow(v, 5, p) % p for mm, v in zip(rw, nu)], p)
    Lm = R.CMod([np.array([[pow(v, -4, p)]], dtype=np.int64) for v in nu], p)
    Q = R.CMod([mm * pow(v, -3, p) % p for mm, v in zip(rw, nu)], p)
    Line = R.CMod([np.array([[v]], dtype=np.int64) for v in nu], p)
    Four = R.CMod([mm * v % p for mm, v in zip(rw, nu)], p)
    Ce, Cl, Cq = R.Coh(cov, Veta), R.Coh(cov, Lm), R.Coh(cov, Q.dual())
    Cline, Cfour = R.Coh(cov, Line), R.Coh(cov, Four)
    return {"h1(V_eta)": Ce.h1, "n(V_eta)": Ce.n, "b0": Cl.a0, "n(L)": Cl.n, "n((VL)*)": Cq.n,
            "capW": Cl.a0 + Cl.n, "capL2": Cq.n, "n(nu)": Cline.n, "h1(nu)": Cline.h1, "n(rho nu)": Cfour.n,
            "h1(rho nu)": Cfour.h1}


def cyclic_cover(cov, ab, c, m):
    """the cyclic cover N_e of N for the character e = c (order k dividing m), as a transitive action of Gamma on X x Z/k:
    (x, i)^g = (x^g, i + e(x, g)), with e(x, g) the exponent (in units of zeta_k) of e on the Schreier generator of the edge
    (x, g), 0 on tree edges.  Returns (perms, k)."""
    exps = ab.exponents(c, m)
    k = m // gcd(m, gcd(*exps)) if any(exps) else 1
    step = {}
    for j, (x, g) in enumerate(cov.sgens):
        step[(x, g)] = (exps[j] * k // m) % k
    d = cov.d
    perms = {}
    for g in cov.gens:
        img = [0] * (d * k)
        for x in range(d):
            y = cov.P[g][x]
            s = step.get((x, g), 0)
            for i in range(k):
                img[x * k + i] = y * k + (i + s) % k
        perms[g] = img
    return perms, k


def order_of(c, m):
    """the order of the character c (exponents of zeta_m)"""
    g = m
    for x in c:
        g = gcd(g, x)
    return m // g


def units(m):
    return [a for a in range(1, m + 1) if gcd(a, m) == 1]


def galois_orbit(c, m):
    """Lemma C's orbit of c: {a c : a a unit mod m}, sorted"""
    return sorted({tuple((a * x) % m for x in c) for a in units(m)})


def orbit_reps(ab, m):
    """every character of order dividing m, once, grouped into Galois orbits: [(rep, orbit size, order)], the representative
    being the orbit's least member (characters() runs in lexicographic order, so the first member met is the least)"""
    seen, out, U = set(), [], units(m)
    for c in ab.characters(m):
        if c in seen:
            continue
        orb = {tuple((a * x) % m for x in c) for a in U}
        seen |= orb
        k = order_of(c, m)
        assert len(orb) == sum(1 for a in range(1, k + 1) if gcd(a, k) == 1), "an orbit's size is not phi(order)"
        assert min(orb) == c
        out.append((c, len(orb), k))
    assert len(seen) == len(ab.characters(m))
    return out


def subgroup(gens, m):
    """the subgroup of characters generated by gens (tuples mod m), as a set"""
    if not gens:
        return set()
    zero = tuple(0 for _ in gens[0])
    S, frontier = {zero}, [zero]
    while frontier:
        nxt = []
        for v in frontier:
            for g in gens:
                w = tuple((a + b) % m for a, b in zip(v, g))
                if w not in S:
                    S.add(w)
                    nxt.append(w)
        frontier = nxt
    return S


def abelian_cover(cov, ab, gens, m):
    """Lemma A''s cover N_A: the characters of N_A's deck group are the subgroup generated by gens.  Gamma acts on X x A, A the
    image of pi_1 N in (Z/m)^r under (chi_1, ..., chi_r): (x, v)^g = (x^g, v + e(x, g)), e(x, g) the exponent vector of the
    chis on the Schreier generator of the edge (x, g), 0 on tree edges (cyclic_cover's convention, which control K2 checks
    against the banked covers).  Returns (perms, |A|), with |A| checked against the order of the subgroup of characters."""
    E = [ab.exponents(c, m) for c in gens]
    zero = tuple(0 for _ in gens)
    step = {sg: tuple(E[i][j] for i in range(len(gens))) for j, sg in enumerate(cov.sgens)}
    idx, pts = {(0, zero): 0}, [(0, zero)]
    for (x, v) in pts:
        for g in cov.gens:
            s = step.get((x, g), zero)
            key = (cov.P[g][x], tuple((a + b) % m for a, b in zip(v, s)))
            if key not in idx:
                idx[key] = len(pts)
                pts.append(key)
    perms = {}
    for g in cov.gens:
        img = [0] * len(pts)
        for (x, v), i in idx.items():
            s = step.get((x, g), zero)
            img[i] = idx[(cov.P[g][x], tuple((a + b) % m for a, b in zip(v, s)))]
        perms[g] = img
    nA = len(pts) // cov.d
    assert len(pts) == cov.d * nA and nA == len(subgroup(list(gens), m)), "N_A's degree is not deg N times |A|"
    assert sorted(set(perms[cov.gens[0]])) == list(range(len(pts)))
    return perms, nA


def root_order(m):
    """the roots of unity the readings need: zeta_24 (the exact holonomy's field, sm:B1536's gf.GF) and zeta_m"""
    return GF.lcm(24, m)


def route_primes(m):
    """route R' reads at the largest prime p < 2^31 with p = 1 mod root_order(m), route P' at the next one"""
    a, b = GF.primes_1_mod(root_order(m), 1 << 31, 2)
    return {"R": a, "P": b}


# ============================================================================================ route P' (sm:B1538's punct_present)
B1538V = ROOT / "frontier" / "B1538_the_puncture_characters" / "verification"


def punct_present():
    if str(B1538V) not in sys.path:
        sys.path.append(str(B1538V))
    return _load("b1539_b1538_punct_present", B1538V / "punct_present.py")


class Shim:
    """the attributes punct_present.Presentation reads, for a general cover of M (sm:B1536's covers): d, perms, pinv, st.G and
    periph, the cusps' peripheral pairs as closed words at the coset 0 (u_x w u_x^-1, u_x a path 0 -> x)"""

    def __init__(self, G, perms):
        class _St:
            pass
        self.st = _St()
        self.st.G = G
        self.d = len(perms[G.gens[0]])
        self.perms = {g: list(perms[g]) for g in G.gens}
        self.pinv = {g: [0] * self.d for g in G.gens}
        for g in G.gens:
            for x, y in enumerate(self.perms[g]):
                self.pinv[g][y] = x
        path = {0: ""}
        order = [0]
        for x in order:
            for g in G.gens:
                for y, ch in ((self.perms[g][x], g), (self.pinv[g][x], g.upper())):
                    if y not in path:
                        path[y] = path[x] + ch
                        order.append(y)
        self.periph = []
        for cu in CL.cusps(G, perms):
            ux = path[cu["x"]]
            ws = [ux + CL.periph_word(G, i, j) + CL.inv_word(ux) for (i, j) in cu["lattice"]]
            self.periph.append(tuple(ws))


def frame_own_p(G, perms, cov, rho_np, exps, m, p, Pr=None):
    """route P': the same quantities as frame_own, on punct_present's own presentation (python-flint); the character's values
    on its generators come from rewriting each generator's word into route R's Schreier generators (the shared input)"""
    RP = punct_present()
    if Pr is None:
        Pr = RP.Presentation(Shim(G, perms))
    r = int(pari.lift(pari.znprimroot(p) ** ((p - 1) // m)))
    vals = []
    for (_, _, w) in Pr.gens:
        rw, end = cov.rewrite(0, w)
        assert end == 0
        vals.append(sum(e * exps[j] for j, e in rw) % m)
    nu = [pow(r, v, p) for v in vals]
    rw4 = [R.base_word(rho_np, w, p).tolist() for (_, _, w) in Pr.gens]

    def mod(mats):
        return RP.ModP(mats, p)
    sc = lambda M_, c: [[x * c % p for x in row] for row in M_]  # noqa: E731
    Veta = mod([sc(M_, pow(v, 5, p)) for M_, v in zip(rw4, nu)])
    Lm = mod([[[pow(v, -4, p)]] for v in nu])
    Q = mod([sc(M_, pow(v, -3, p)) for M_, v in zip(rw4, nu)])
    Line = mod([[[v]] for v in nu])
    Four = mod([sc(M_, v) for M_, v in zip(rw4, nu)])
    Ce, Cl, Cq = RP.read_module(Pr, Veta), RP.read_module(Pr, Lm), RP.read_module(Pr, Q.dual())
    Cline, Cfour = RP.read_module(Pr, Line), RP.read_module(Pr, Four)
    return {"h1(V_eta)": Ce["h1"], "n(V_eta)": Ce["n"], "b0": Cl["h0"], "n(L)": Cl["n"], "n((VL)*)": Cq["n"],
            "capW": Cl["h0"] + Cl["n"], "capL2": Cq["n"], "n(nu)": Cline["n"], "h1(nu)": Cline["h1"],
            "n(rho nu)": Cfour["n"], "h1(rho nu)": Cfour["h1"]}
