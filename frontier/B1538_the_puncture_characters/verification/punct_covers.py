#!/usr/bin/env python3
"""B1538 -- the fibre-direction covers of a word state, their fibre groups, and the characters of their own.  Library; nothing
sealed is computed on import.

THE STATE.  sm:B1527's presentation (family_lib.word_group): Gamma = F x| <t>, F = <a, b>, t g t^-1 = phi(g), the cusp
<l, t'>, l = abAB, t' = t (+) or abt (-).  M = family_lib.homology_matrix(phi) (column j holds the exponent sums of
phi(gen_j)), so [phi(g)] = M [g] in H_1(F) = Z^2, with e_a = (1, 0) and e_b = (0, 1).

THE COVERS (design notes, section 1).  Take a sublattice Lam of Z^2 with M Lam = Lam, D = Z^2 / Lam, K = ker(F -> D), and a
class wbar in D (w = u_wbar, a word of F with image wbar).  Then H = <K, tau>, with tau = t w.
  - K is normal in Gamma, H n F = K, and H has index |D|.
  - Two such subgroups with the same Lam are conjugate iff wbar - wbar' lies in (M - 1) D.
  - Gamma acts on the right cosets H\Gamma = D (H u <-> ubar for u in F) by
        x^a = x + e_a,   x^b = x + e_b,   x^t = M^-1 x - wbar      (mod Lam),
    since H u t = H t phi^-1(u) = H tau w^-1 phi^-1(u).

THE FIBRE GROUP.
  - K is free on the |D| + 1 Schreier generators y_(x,g) = u_x g u_(x+e_g)^-1 that are not freely trivial. Here u is the BFS
    transversal of D's Cayley graph on e_a, e_b, with the generators tried in the order a, b, A, B.
  - The monodromy f(k) = tau k tau^-1 = phi(w k w^-1) is an automorphism of K.
  - The fibre's punctures are the conjugates l_x = u_x l u_x^-1, one per x in D.
  - f sends l_x to a conjugate of l_pi(x), with pi(x) = M(x + wbar) (+), and M(x + wbar) - e_a - e_b (-), since
    phi(abAB) = abAB (+) and (ab)^-1 abAB (ab) (-).

CHARACTERS of H are chi = (zeta, s), with zeta a character of K such that zeta o f = zeta, and s = chi(tau).
  - Both are stored as exponents of z_L = e^{2 pi i / L}: zeta(y_i) = z_L^ez[i] and s = z_L^es.
  - chi is a PUNCTURE character when zeta(l_x) != 1 for some x.
  - On Gamma's Reidemeister-Schreier generators of H (the coset graph of D on a, b, t, with the same transversal u):
      - chi(s_(x,g)) = zeta(y_(x,g)) for g = a, b;
      - chi(s_(x,t)) = zeta(k_x) s, with k_x = u_x phi(u_(x^t)^-1 w^-1) in K (s_(x,t) = u_x t u_(x^t)^-1 = k_x tau).
  - chi of any word of H is read along its path from the coset 0 (chi_exp).

The invariant characters are Hom(coker(f_* - 1), Q/Z), read from the Smith form of f_* - 1 (PARI's matsnf, checked)."""
import importlib.util
import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1527V = ROOT / "frontier" / "B1527_the_cusp_decides" / "verification"
B1536V = ROOT / "frontier" / "B1536_the_finite_covers" / "verification"


def _load(path, alias):
    """a module by path under a name of its own (the E12 hazard: never a bare import of another arc's module)"""
    if alias in sys.modules:
        return sys.modules[alias]
    spec = importlib.util.spec_from_file_location(alias, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


def family():
    """sm:B1527's family_lib (word_group, homology_matrix); it puts its own directory on sys.path for its cusp_lib"""
    return _load(B1527V / "family_lib.py", "b1527_family_lib")


def cover_lib():
    """sm:B1536's cover_lib (check_cover, cusps, canonical, periph_word), read only"""
    return _load(B1536V / "cover_lib.py", "b1536_cover_lib")


def pari():
    from cypari import pari as P
    return P


# ============================================================================================ words
def inv_word(w):
    return "".join(c.swapcase() for c in reversed(w))


def free_reduce(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def substitute(w, img):
    """the image of w under the endomorphism with images img[g] for the lower-case generators g"""
    return free_reduce("".join(img[c] if c.islower() else inv_word(img[c.lower()]) for c in w))


_STEP_INV = {"L": {"a": "aB", "b": "b"}, "R": {"a": "a", "b": "bA"}}
_IOTA = {"a": "A", "b": "B"}


class State:
    """a word state: G (sm:B1527's presentation), phi and phi^-1 as images, M = phi on H_1(F)"""

    def __init__(self, sw):
        sign, word = sw[0], sw[1:]
        assert sign in "+-" and word and set(word) <= set("LR"), sw
        FL = family()
        G, img = FL.word_group(sign, word)
        self.name, self.sign, self.word, self.G, self.img = sw, sign, word, G, dict(img)
        H = FL.homology_matrix(img)
        self.M = ((H[0][0], H[0][1]), (H[1][0], H[1][1]))
        assert self.M[0][0] * self.M[1][1] - self.M[0][1] * self.M[1][0] == 1, (sw, self.M)
        assert abs(self.M[0][0] + self.M[1][1]) > 2, ("not Anosov", sw)
        # phi = iota^[-] o sigma_w1 o ... o sigma_wn, so phi^-1(g) = sigma_wn^-1( ... sigma_w1^-1( iota^[-](g) ))
        inv = {g: (_IOTA[g] if sign == "-" else g) for g in "ab"}
        for letter in word:
            inv = {g: substitute(inv[g], _STEP_INV[letter]) for g in "ab"}
        self.img_inv = inv
        for g in "ab":
            assert substitute(substitute(g, self.img_inv), self.img) == g, (sw, g)
            assert substitute(substitute(g, self.img), self.img_inv) == g, (sw, g)
        self.tprime = "t" if sign == "+" else "abt"

    def phi(self, w):
        return substitute(w, self.img)


def minv(M):
    (a, b), (c, d) = M
    return ((d, -b), (-c, a))


def mvec(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])


# ============================================================================================ the lattices
def _divisors(n):
    return [k for k in range(1, n + 1) if n % k == 0]


def in_lattice(lat, v):
    p, q, r = lat
    if v[1] % r:
        return False
    return (v[0] - (v[1] // r) * q) % p == 0


def lattices(M, nmax, nmin=1):
    """every sublattice Lam of Z^2 with M Lam = Lam and nmin <= index <= nmax, by its column Hermite basis (p, 0), (q, r):
    p r = index, 0 <= q < p (unique for each sublattice)"""
    out = []
    for n in range(nmin, nmax + 1):
        for p in _divisors(n):
            r = n // p
            for q in range(p):
                lat = (p, q, r)
                if in_lattice(lat, mvec(M, (p, 0))) and in_lattice(lat, mvec(M, (q, r))):
                    out.append(lat)
    return out


# ============================================================================================ the cover
class Cover:
    """H = <K, t w> for the lattice lat = (p, q, r) and the class wbar (a label of D)"""

    def __init__(self, st, lat, wbar_label=0):
        self.st, self.lat = st, lat
        p, q, r = lat
        self.d = d = p * r
        self.vecs = [(i, j) for j in range(r) for i in range(p)]           # label x = i + p j
        assert all(self.label(v) == x for x, v in enumerate(self.vecs))
        self.wbar = self.vecs[wbar_label]
        Mi = minv(st.M)
        self.perms = {
            "a": [self.label((v[0] + 1, v[1])) for v in self.vecs],
            "b": [self.label((v[0], v[1] + 1)) for v in self.vecs],
            "t": [self.label(tuple(z - y for z, y in zip(mvec(Mi, v), self.wbar))) for v in self.vecs],
        }
        self.pinv = {g: self._inverse(pm) for g, pm in self.perms.items()}
        CL = cover_lib()
        assert CL.check_cover(st.G, self.perms), ("not a transitive action of Gamma", st.name, lat, wbar_label)
        # ---------------------------------------------------------------- the transversal of D on e_a, e_b (BFS)
        u = {0: ""}
        order = [0]
        k = 0
        while k < len(order):
            x = order[k]
            k += 1
            for g in "abAB":
                y = self.perms[g][x] if g.islower() else self.pinv[g.lower()][x]
                if y not in u:
                    u[y] = u[x] + g
                    order.append(y)
        assert len(u) == d
        self.u = [u[x] for x in range(d)]
        self.w = self.u[wbar_label]
        # ---------------------------------------------------------------- K's free basis
        self.gens, self.gword, self.gidx = [], [], {}
        for x in range(d):
            for g in "ab":
                word = free_reduce(self.u[x] + g + inv_word(self.u[self.perms[g][x]]))
                if word:
                    self.gidx[(x, g)] = len(self.gens)
                    self.gens.append((x, g))
                    self.gword.append(word)
        self.n = len(self.gens)
        assert self.n == d + 1, (self.n, d)
        # ---------------------------------------------------------------- the monodromy f(y) = phi(w y w^-1)
        self.fimg = [self.rewrite(st.phi(self.w + y + inv_word(self.w))) for y in self.gword]
        self.fstar = [[0] * self.n for _ in range(self.n)]       # column i: exponent sums of f(y_i)
        for i, img in enumerate(self.fimg):
            for j, e in img:
                self.fstar[j][i] += e
        P = pari()
        det = int(P.matdet(P.matrix(self.n, self.n, [v for row in self.fstar for v in row])))
        assert abs(det) == 1, ("f_* is not unimodular", det)
        # ---------------------------------------------------------------- punctures and their permutation
        self.ell = [self.abelian(self.rewrite(self.u[x] + "abAB" + inv_word(self.u[x]))) for x in range(d)]
        assert all(sum(v[j] for v in self.ell) == 0 for j in range(self.n)), "the punctures do not sum to zero"
        shift = (0, 0) if st.sign == "+" else (1, 1)
        self.pi = [self.label(tuple(z - s_ for z, s_ in zip(mvec(st.M, (v[0] + self.wbar[0], v[1] + self.wbar[1])), shift)))
                   for v in self.vecs]
        for x in range(d):                                       # [f(l_x)] = [l_pi(x)]
            fl = [sum(self.fstar[j][i] * self.ell[x][i] for i in range(self.n)) for j in range(self.n)]
            assert fl == self.ell[self.pi[x]], ("the monodromy does not permute the punctures as pi", x)
        # ---------------------------------------------------------------- k_x for chi(s_(x,t))
        self.kx = []
        for x in range(d):
            y = self.perms["t"][x]
            self.kx.append(self.abelian(self.rewrite(self.u[x] + st.phi(inv_word(self.u[y]) + inv_word(self.w)))))
        # ---------------------------------------------------------------- the cusps (sm:B1536's cover_lib)
        self.cusps = CL.cusps(st.G, self.perms)
        self.orbits = self._pi_orbits()
        assert sorted(sorted(c["orbit"]) for c in self.cusps) == sorted(sorted(o) for o in self.orbits), \
            "the cusps are not the orbits of pi"
        self.periph = []
        for c in self.cusps:
            (i1, j1), (i2, j2) = c["lattice"]
            ux = self.u[c["x"]]
            self.periph.append([ux + CL.periph_word(st.G, i1, j1) + inv_word(ux),
                                ux + CL.periph_word(st.G, i2, j2) + inv_word(ux)])
        # ---------------------------------------------------------------- the invariant characters
        self._character_group()

    # ------------------------------------------------------------------------------------------------ D
    def label(self, v):
        return lat_label(self.lat, v)

    @staticmethod
    def _inverse(pm):
        out = [0] * len(pm)
        for x, y in enumerate(pm):
            out[y] = x
        return out

    def _pi_orbits(self):
        seen, out = set(), []
        for x in range(self.d):
            if x in seen:
                continue
            orb, y = [], x
            while y not in seen:
                seen.add(y)
                orb.append(y)
                y = self.pi[y]
            out.append(orb)
        return out

    # ------------------------------------------------------------------------------------------------ K
    def rewrite(self, word):
        """a word of F lying in K, as [(generator index, +-1)] in K's free basis"""
        cur, out = 0, []
        for c in word:
            g = c.lower()
            if c.islower():
                if (cur, g) in self.gidx:
                    out.append((self.gidx[(cur, g)], 1))
                cur = self.perms[g][cur]
            else:
                prev = self.pinv[g][cur]
                if (prev, g) in self.gidx:
                    out.append((self.gidx[(prev, g)], -1))
                cur = prev
        assert cur == 0, ("the word is not in K", word)
        red = []
        for t in out:
            if red and red[-1][0] == t[0] and red[-1][1] == -t[1]:
                red.pop()
            else:
                red.append(t)
        return red

    def abelian(self, kword):
        v = [0] * self.n
        for i, e in kword:
            v[i] += e
        return v

    # ------------------------------------------------------------------------------------------------ characters
    def _character_group(self):
        """coker(f_* - 1) = Z^r + sum Z/d_i, and U with: u (row) is invariant iff c = u U^-1 has c_i d_i in Z"""
        P = pari()
        n = self.n
        C = P.matrix(n, n, [self.fstar[i][j] - (1 if i == j else 0) for i in range(n) for j in range(n)])
        U, V, Dg = P.matsnf(C, 1)
        assert U * C * V == Dg
        assert abs(int(P.matdet(U))) == 1 and abs(int(P.matdet(V))) == 1
        self.snf = [int(Dg[i, i]) for i in range(n)]
        assert all(Dg[i, j] == 0 for i in range(n) for j in range(n) if i != j)
        # u C in Z^n  <=>  (u U^-1) Dg V^-1 in Z^n  <=>  c Dg in Z^n with c = u U^-1, so u = c U
        self.U = [[int(U[i, j]) for j in range(n)] for i in range(n)]
        Ui = U ** -1
        self.Uinv = [[int(Ui[i, j]) for j in range(n)] for i in range(n)]
        assert all(sum(self.U[i][k] * self.Uinv[k][j] for k in range(n)) == (1 if i == j else 0)
                   for i in range(n) for j in range(n))
        self.free_rank = sum(1 for x in self.snf if x == 0)
        self.torsion = sorted(abs(x) for x in self.snf if abs(x) > 1)

    def characters(self, m):
        """every invariant character zeta of K with zeta^m = 1, as exponent vectors ez mod m"""
        n = self.n
        ranges = []
        for di in self.snf:
            if di == 0:
                ranges.append(list(range(m)))
            else:
                g = gcd(abs(di), m)
                ranges.append([k * (m // g) for k in range(g)])
        out = []

        def rec(i, acc):
            if i == n:
                ez = [sum(acc[k] * self.U[k][j] for k in range(n)) % m for j in range(n)]
                out.append(tuple(ez))
                return
            for c in ranges[i]:
                rec(i + 1, acc + [c])
        rec(0, [])
        assert len(set(out)) == len(out)
        for ez in out:                                           # zeta o f = zeta
            assert all(sum(ez[j] * self.fstar[j][i] for j in range(n)) % m == ez[i] % m for i in range(n))
        return out

    def galois_reps(self, m):
        """[(ez reduced to its exact order m', m', orbit size)]: one representative (the least) of each Galois orbit of the
        invariant characters zeta != 1 with zeta^m = 1; the Galois group acts through (Z/m')^*, freely on the characters of
        exact order m'"""
        units = [a for a in range(1, m) if gcd(a, m) == 1]
        seen, out = set(), []
        for ez in self.characters(m):
            if ez in seen or not any(ez):
                continue
            orbit = {tuple(a * e % m for e in ez) for a in units}
            seen |= orbit
            rep = min(orbit)
            g = m
            for e in rep:
                g = gcd(g, e)
            out.append((tuple(e // g for e in rep), m // g, len(orbit)))
        return out

    def puncture_trivial(self):
        """the invariant characters trivial on every puncture, as (ez, m): the characters of Z^n / <im(f_* - 1), [l_x]>, a finite
        group (of order |det(M - 1)|, the closed torus's Lam / (M - 1) Lam)"""
        P = pari()
        n = self.n
        cols = [[self.fstar[i][j] - (1 if i == j else 0) for i in range(n)] for j in range(n)] + [list(v) for v in self.ell]
        A = P.matrix(n, len(cols), [cols[j][i] for i in range(n) for j in range(len(cols))])
        B = P.mathnf(A)
        assert int(P.matsize(B)[1]) == n, "the lattice is not of full rank"
        U, V, Dg = P.matsnf(B, 1)
        assert U * B * V == Dg
        d = [int(Dg[i, i]) for i in range(n)]
        Ui = [[int(U[i, j]) for j in range(n)] for i in range(n)]
        m = 1
        for x in d:
            m = m * abs(x) // gcd(m, abs(x))
        out = []

        def rec(i, acc):
            if i == n:
                out.append(tuple(sum(acc[k] * Ui[k][j] for k in range(n)) % m for j in range(n)))
                return
            for c in range(abs(d[i])):
                rec(i + 1, acc + [c * (m // abs(d[i]))])
        rec(0, [])
        for ez in out:
            assert not self.is_puncture(ez, m)
            assert all(sum(ez[j] * self.fstar[j][i] for j in range(n)) % m == ez[i] % m for i in range(n))
        return out, m

    def fourth_roots(self, ez, m):
        """every invariant character zeta' with zeta'^4 = zeta (zeta = ez mod m), as (ez', m'): in the Smith coordinates
        c = u U^-1 (u = ez / m), c'_i = (c_i + t) / 4 (t = 0..3) on a free coordinate, and c'_i = a / |d_i| with 4 a = |d_i| c_i
        mod |d_i| on a torsion one"""
        from fractions import Fraction as Fr
        n = self.n
        u = [Fr(e % m, m) for e in ez]
        c = [sum(u[k] * self.Uinv[k][j] for k in range(n)) % 1 for j in range(n)]
        choices = []
        for i, di in enumerate(self.snf):
            if di == 0:
                choices.append([(c[i] + t) / 4 for t in range(4)])
            else:
                D_ = abs(di)
                assert (c[i] * D_).denominator == 1
                choices.append([Fr(a, D_) for a in range(D_) if (4 * a - c[i] * D_) % D_ == 0])
        out = []

        def rec(i, acc):
            if i == n:
                up = [sum(acc[k] * self.U[k][j] for k in range(n)) % 1 for j in range(n)]
                mm = 1
                for x in up:
                    mm = mm * x.denominator // gcd(mm, x.denominator)
                ezp = tuple(int(x * mm) % mm for x in up)
                assert all((4 * x - y) % 1 == 0 for x, y in zip(up, u))
                assert all(sum(ezp[j] * self.fstar[j][k] for j in range(n)) % mm == ezp[k] % mm for k in range(n))
                out.append((ezp, mm))
                return
            for x in choices[i]:
                rec(i + 1, acc + [x])
        rec(0, [])
        return out

    def count_characters(self, m):
        tot = 1
        for di in self.snf:
            tot *= m if di == 0 else gcd(abs(di), m)
        return tot

    def puncture_values(self, ez, m):
        """zeta(l_x) as exponents mod m"""
        return [sum(e * v for e, v in zip(ez, self.ell[x])) % m for x in range(self.d)]

    def is_puncture(self, ez, m):
        return any(self.puncture_values(ez, m))

    # ------------------------------------------------------------------------------------------------ chi on Gamma's words
    def rs_values(self, ez, es, L):
        """chi(s_(x,g)) as exponents mod L, for x in D and g = a, b, t"""
        out = {}
        for x in range(self.d):
            for g in "ab":
                out[(x, g)] = ez[self.gidx[(x, g)]] % L if (x, g) in self.gidx else 0
            out[(x, "t")] = (sum(e * v for e, v in zip(ez, self.kx[x])) + es) % L
        return out

    def chi_exp(self, word, vals, L, start=0, closed=True):
        """chi of the element read along word's path from the coset start (an element of H when closed)"""
        cur, tot = start, 0
        for c in word:
            g = c.lower()
            if c.islower():
                tot += vals[(cur, g)]
                cur = self.perms[g][cur]
            else:
                prev = self.pinv[g][cur]
                tot -= vals[(prev, g)]
                cur = prev
        if closed:
            assert cur == start, ("the word does not lie in H", word)
        return tot % L

    def trivial_cusps(self, ez, es, L):
        """the cusps (indices) where chi is trivial on both peripheral generators"""
        vals = self.rs_values(ez, es, L)
        return [k for k, (h1, h2) in enumerate(self.periph)
                if self.chi_exp(h1, vals, L) == 0 and self.chi_exp(h2, vals, L) == 0]

    def summary(self):
        return {"lattice": list(self.lat), "D": self.d, "wbar": list(self.wbar), "cusps": len(self.cusps),
                "orbit sizes": sorted(len(o) for o in self.orbits), "free rank": self.free_rank, "torsion": self.torsion}


def lat_label(lat, v):
    """the label i + p j of v mod Lam, 0 <= i < p, 0 <= j < r"""
    p, q, r = lat
    k = v[1] // r
    i, j = v[0] - k * q, v[1] - k * r
    return (i % p) + p * j


def classes(st, lat):
    """the classes wbar in D / (M - 1) D, each by its least label"""
    p, q, r = lat
    vecs = [(i, j) for j in range(r) for i in range(p)]
    M = st.M
    img = {lat_label(lat, tuple(a - b for a, b in zip(mvec(M, v), v))) for v in vecs}      # (M - 1) D, a subgroup
    seen, reps = set(), []
    for x, v in enumerate(vecs):
        if x in seen:
            continue
        reps.append(x)
        for y in img:
            seen.add(lat_label(lat, (v[0] + vecs[y][0], v[1] + vecs[y][1])))
    return reps


def covers(st, nmax, nmin=2):
    """every fibre-direction cover with nmin <= |D| <= nmax, up to conjugacy: [(lat, wbar label)]"""
    return [(lat, w) for lat in lattices(st.M, nmax, nmin) for w in classes(st, lat)]
