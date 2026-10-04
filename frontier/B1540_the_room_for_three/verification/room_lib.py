"""B1540 -- the library: sm:B1536's modules by path (unique names), the population of room covers, the abelianisation of a
cover on route R's Schreier generators, the restriction of a state's character to a cover in own coordinates, the abelian and
cyclic covers along own characters (Lemma A), and the direct reading of a cover at its trivial character (route N, route R and
integer homology).  Self-contained: it loads only sm:B1536's banked modules (cover_lib, route_r, route_n, gf, population),
never another arc's unsealed files.

Conventions (sm:B1536): a cover N of M is a transitive permutation action of Gamma = pi_1 M on X with base point 0; route_r's
PCover gives its Schreier generators s_j (non-tree edges) with base words w_j.  H_1(N) = Z^n / (relator rows); with U A V = D
(PARI's Smith form, A padded square), s_j has coordinates row j of V reduced mod D.  An own character of order dividing m is
c = (c_i) over the coordinates with d_i != 1 (c_i in Z/m on a free coordinate, d_i c_i = 0 mod m on a torsion one), with value
zeta_m^(sum_i c_i V[j][i]) on s_j.  A state's character psi = (u_a, u_b, kappa) (turns; sm:B1536's Base.character) has
psi(a) = u_a, psi(b) = u_b, psi(t) = kappa on m004 (sign +) and kappa - u_a - u_b on m003 (sign -, t' = abt)."""
import importlib.util
import json
import sys
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

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


R = _load("b1540_b1536_route_r", B1536V / "route_r.py")      # allocates PARI's stack: load first
CL = _load("b1540_b1536_cover_lib", B1536V / "cover_lib.py")
GF = _load("b1540_b1536_gf", B1536V / "gf.py")
N = _load("b1540_b1536_route_n", B1536V / "route_n.py")
POP = _load("b1540_b1536_population", B1536V / "population.py")
from cypari import pari  # noqa: E402


def members():
    """sm:B1536's covers of degree <= 12 where both supplies live at the trivial character (n(1) >= 1 and n(rho) >= 1) or the
    four has two (n(rho) >= 2): [(state, cover, degree, n(1), n(rho), cusps)], m004 first, then by degree and name (30)"""
    rooms = json.loads((B1536V / "post_run_rooms.json").read_text())
    out = []
    for st in ("m004", "m003"):
        for x in rooms[st]["trivial character supplies"]:
            if (x["n(1)"] >= 1 and x["n(rho)"] >= 1) or x["n(rho)"] >= 2:
                out.append((st, x["cover"], x["degree"], x["n(1)"], x["n(rho)"], x["cusps"]))
    return sorted(out, key=lambda r: (r[0] != "m004", r[2], r[1]))


_STATES = {}


def cover(st, cid):
    """(state, perms, PCover) of one of sm:B1536's covers"""
    if st not in _STATES:
        S = CL.state(st)
        _STATES[st] = (S, dict(POP.covers(S)))
    S, covs = _STATES[st]
    perms = covs[cid]
    return S, perms, R.PCover(S["G"], perms)


class Ab:
    """the abelianisation of pi_1 N on cov's Schreier generators (U A V = D asserted; every relator checked to die)"""

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
        assert len(rows) == n, "more relators than generators"
        A = pari.matrix(n, n, [x for r in rows for x in r])
        U, V, D = pari.matsnf(A, 1)
        self.n = n
        self.d = [abs(int(D[i, i])) for i in range(n)]
        self.V = [[int(V[i, j]) for j in range(n)] for i in range(n)]
        UA = [[sum(int(U[i, k]) * rows[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        UAV = [[sum(UA[i][k] * self.V[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        assert all(UAV[i][j] == int(D[i, j]) for i in range(n) for j in range(n)), "U A V != D"
        for r in rows:
            img = [sum(r[j] * self.V[j][i] for j in range(n)) for i in range(n)]
            assert all((img[i] % self.d[i] == 0) if self.d[i] else img[i] == 0 for i in range(n)), "a relator survives"
        Vi = pari.matrix(n, n, [x for r in self.V for x in r]) ** -1
        self.Vi = [[int(Vi[i, j]) for j in range(n)] for i in range(n)]
        self.coords = [i for i in range(n) if self.d[i] != 1]
        self.free = [i for i in self.coords if self.d[i] == 0]
        self.torsion = [self.d[i] for i in self.coords if self.d[i] > 1]

    def exponents(self, c, m):
        """the own character c's values on the Schreier generators, as exponents of zeta_m"""
        return [sum(ci * self.V[j][i] for ci, i in zip(c, self.coords)) % m for j in range(self.n)]

    def coordinates(self, exps, m):
        """the inverse: the own character with these values on the Schreier generators, or None if they are not one"""
        full = [sum(self.Vi[i][j] * exps[j] for j in range(self.n)) % m for i in range(self.n)]
        for i in range(self.n):
            if self.d[i] == 1 and full[i] % m:
                return None
            if self.d[i] > 1 and (self.d[i] * full[i]) % m:
                return None
        c = tuple(full[i] for i in self.coords)
        return c if self.exponents(c, m) == list(exps) else None


def restrict(S, cov, ab, psi, m):
    """the restriction of the state's character psi = (u_a, u_b, kappa) (Fractions, turns) to the cover, in own coordinates mod m
    (asserted to be a character of H_1(N))"""
    ua, ub, k = psi
    vals = {"a": ua, "b": ub, "t": (k if S["sign"] == "+" else k - ua - ub)}
    exps = []
    for w in cov.sword:
        tot = Fr(0)
        for ch in w:
            tot += vals[ch.lower()] if ch.islower() else -vals[ch.lower()]
        tot = (tot * m) % m
        assert tot.denominator == 1, "the modulus does not carry the character"
        exps.append(int(tot))
    c = ab.coordinates(exps, m)
    assert c is not None, "a restricted character is not a character of H_1(N)"
    return c


def order_of(c, m):
    g = m
    for x in c:
        g = gcd(g, x)
    return m // g


def cyclic_cover(cov, ab, c, m):
    """Lemma A's cover N_c: Gamma acting on X x Z/k (k = the order of c) by (x, i)^g = (x^g, i + e(x, g)), e the exponent of c on
    the edge's Schreier generator (0 on tree edges), reduced to Z/k; connected because c is onto mu_k.  Returns (perms, k)."""
    k = order_of(c, m)
    E = ab.exponents(c, m)
    step = {sg: (E[j] * k // m) % k for j, sg in enumerate(cov.sgens)}
    assert all((E[j] * k) % m == 0 for j in range(len(E)))
    perms = {}
    for g in cov.gens:
        img = [0] * (cov.d * k)
        for x in range(cov.d):
            s = step.get((x, g), 0)
            for i in range(k):
                img[x * k + i] = cov.P[g][x] * k + (i + s) % k
        perms[g] = img
    return perms, k


def read_cover(S, perms):
    """a cover read directly at its trivial character: route N (Shapiro on the state with the cover's permutation module, at the
    largest prime below route_n's bound with p = 1 mod N_root), route R (the cover's own presentation, at the largest prime below
    2^31 with p = 1 mod N_root), and H_1 of the presentation (PARI's Smith form)"""
    G = S["G"]
    cus = CL.cusps(G, perms)
    _, _, Nroot, _ = POP.characters(S, perms)
    pN = GF.primes_1_mod(Nroot, N.P_BOUND, 1)[0]
    BN = N.Base(S, GF.GF(pN, Nroot))
    sN = N.supplies(BN, N.perm_arrays(G, perms), BN.character((Fr(0), Fr(0)), Fr(0)))
    pR = GF.primes_1_mod(Nroot, 1 << 31, 1)[0]
    BR = N.Base(S, GF.GF(pR, Nroot))
    cov = R.PCover(G, perms)
    sR = R.supplies(cov, BR.rho, BR.character((Fr(0), Fr(0)), Fr(0)), pR)
    ab = Ab(cov)
    return {"degree": len(perms[G.gens[0]]), "cusps": len(cus), "connected": bool(CL.check_cover(G, perms)),
            "route N (prime, n(1), n(rho), capW, capL2)": [pN, sN["n(L)"], sN["n((VL)*)"], sN["capW"], sN["capL2"]],
            "route R (prime, n(1), n(rho), capW, capL2)": [pR, sR["n(L)"], sR["n((VL)*)"], sR["capW"], sR["capL2"]],
            "H_1 (free rank, torsion); b1 - cusps": [len(ab.free), sorted(ab.torsion), len(ab.free) - len(cus)]}


def canonical(S, perms):
    """sm:B1536's canonical form of the cover as a Gamma-set (equal iff the covers are conjugate)"""
    return CL.canonical(perms, S["G"].gens)
