#!/usr/bin/env python3
"""sm:B1551 -- the spin cover: library. Nothing is computed on import.

THE OBJECT. The root's tetrahedral cover N (sm:B1550: the kernel of pi_1 m004 -> A4, the 2Z^2 fibre cover of the third
level M_3 = +LRLRLR) carries the A4-invariant sign character eps = [1, 1, 1, 0, 1 | 1], the spin sign: the central
character of SL(2, F_3) under the holonomy's lift mod sqrt(-3) (sm:B1550's dossier, congruence.py). Its kernel is the
SPIN COVER S = ker(eps), the kernel of pi_1 m004 -> SL(2, F_3), the binary tetrahedral group: a cover of M_3 of degree 8
with deck group Q8, of m004 of degree 24. The line on N has room 4 at eps (sm:B1550's dossier), so S has room
n(1) = n_N(1) + n_N(eps) = 4 (Shapiro), SnapPy's unique degree-8 cover of s961 with four cusps and H1 = Z^8.

THE COVER as data, for sm:B1549's library: cosets (x, s), x a coset of N in M_3 (sm:B1538's labels), s in {0, 1} the
sheet; g moves (x, s) to (x.g, s + eps(s_(x, g))), with s_(x, g) N's Reidemeister-Schreier generator. The attributes d,
perms, pinv, st, u, periph, rs_values, chi_exp are those sm:B1538's Cover has, so route P (punct_present.Presentation) runs
on S unchanged. A character of S is an edge labelling (a value on every edge (y, g) of the coset graph), any gauge.

ROUTE P~ : S's own Reidemeister-Schreier presentation (route P of sm:B1549 on this cover).
ROUTE S~ : Shapiro on N's own presentation (route P's presentation of N): Ind_S^N nu (x) rho, two blocks, the class read
           back on S as the coset-0 block, then Ind W1 and Ind Lambda^2 W1 on N; S's cusps read through N's (Mackey).

The construction is general (DoubleCover: any fibre-direction cover N and any sign character of it). The controls use it on
a cover whose counts are banked: the tetrahedral cover N itself, rebuilt as the double cover of a fibre-direction double
cover N_p of the third level cut out by its lattice parity (lattice_parity_character)."""
import itertools
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent


def _root():
    """the repository: the first parent holding frontier/ (or ORIGIN_AXIOM_ROOT when run outside it)"""
    for p in HERE.parents:
        if (p / "frontier").is_dir():
            return p
    import os
    return Path(os.environ["ORIGIN_AXIOM_ROOT"])


ROOT = _root()
B1550V = ROOT / "frontier" / "B1550_the_three_parities" / "verification"
if str(B1550V) not in sys.path:
    sys.path.insert(0, str(B1550V))
import tetra_lib as L  # noqa: E402  (sm:B1550's library, banked; it loads sm:B1549's three_lib)

T, PC = L.T, L.PC
CL = PC.cover_lib()
EPS = (1, 1, 1, 0, 1, 1)
SW = "+LR"


class DoubleCover:
    """the double cover of a fibre-direction cover N of a word state (sm:B1538's Cover) cut out by a sign character
    chi = (ez, es) of N: cosets (x, s), sheets s in {0, 1}, g: (x, s) -> (x.g, s + chi(s_(x, g)))"""

    def __init__(self, N, state_word, eps):
        self.N, self.st, self.level3 = N, N.st, state_word
        self.eps = eps
        ev = N.rs_values(eps[:-1], eps[-1], 2)
        dN = N.d
        self.dN, self.d = dN, 2 * dN
        self.perms = {g: [None] * self.d for g in "abt"}
        for x in range(dN):
            for s in range(2):
                for g in "abt":
                    self.perms[g][self.lab(x, s)] = self.lab(N.perms[g][x], (s + ev[(x, g)]) % 2)
        self.pinv = {g: PC.Cover._inverse(pm) for g, pm in self.perms.items()}
        assert CL.check_cover(self.st.G, self.perms), "not a transitive action"
        u = {0: ""}
        order, k = [0], 0
        while k < len(order):
            x = order[k]
            k += 1
            for g in "abtABT":
                y = self.perms[g][x] if g.islower() else self.pinv[g.lower()][x]
                if y not in u:
                    u[y] = u[x] + g
                    order.append(y)
        assert len(u) == self.d
        self.u = [u[x] for x in range(self.d)]
        self.cusps = CL.cusps(self.st.G, self.perms)
        self.periph = []
        for c in self.cusps:
            (i1, j1), (i2, j2) = c["lattice"]
            ux = self.u[c["x"]]
            self.periph.append([ux + CL.periph_word(self.st.G, i1, j1) + PC.inv_word(ux),
                                ux + CL.periph_word(self.st.G, i2, j2) + PC.inv_word(ux)])
        self.edges = [(y, g) for y in range(self.d) for g in "abt"]

    def lab(self, x, s):
        return x + self.dN * s

    # ---------------------------------------------------------------------------------------------- characters
    def rs_values(self, ez, es, L_):
        return {e: ez[i] % L_ for i, e in enumerate(self.edges)}

    def chi_exp(self, word, vals, L_, start=0, closed=True):
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
            assert cur == start, ("the word does not lie in S", word)
        return tot % L_

    def trivial_cusps(self, ez, es, L_):
        vals = self.rs_values(ez, es, L_)
        return [k for k, (h1, h2) in enumerate(self.periph)
                if self.chi_exp(h1, vals, L_) == 0 and self.chi_exp(h2, vals, L_) == 0]

    def pullback(self, nu, L_):
        """N's character nu = (ez, es) mod L_, pulled back to S, as an edge labelling"""
        vN = self.N.rs_values(nu[0], nu[1], L_)
        return tuple(vN[(y % self.dN, g)] % L_ for (y, g) in self.edges)

    def relator_rows(self):
        """for every coset and relator of M_3, the signed edge counts along its path (a cocycle must kill each)"""
        idx = {e: i for i, e in enumerate(self.edges)}
        rows = []
        for y in range(self.d):
            for r in self.st.G.rels:
                v = [0] * len(self.edges)
                cur = y
                for c in r:
                    g = c.lower()
                    if c.islower():
                        v[idx[(cur, g)]] += 1
                        cur = self.perms[g][cur]
                    else:
                        prev = self.pinv[g][cur]
                        v[idx[(prev, g)]] -= 1
                        cur = prev
                assert cur == y
                rows.append(v)
        return rows

    def characters(self, L_):
        """every character of S of order dividing L_, one edge labelling each (tree edges of the BFS transversal 0)"""
        tree = set()
        for y in range(1, self.d):
            w = self.u[y]
            cur = 0
            for c in w:
                g = c.lower()
                if c.islower():
                    tree_e = (cur, g)
                    cur = self.perms[g][cur]
                else:
                    prev_ = self.pinv[g][cur]
                    tree_e = (prev_, g)
                    cur = prev_
            tree.add(tree_e)
        free = [i for i, e in enumerate(self.edges) if e not in tree]
        rows = [[r[i] for i in free] for r in self.relator_rows()]
        P = PC.pari()
        n = len(free)
        R = P.matrix(len(rows), n, [v for r in rows for v in r])
        U, V, D = P.matsnf(R, 1)          # U R V = D
        nrow = len(rows)
        diag = [int(D[i, i]) if i < min(nrow, n) else 0 for i in range(n)]
        # D is nrow x n with the diagonal in its last columns when nrow < n: read it column by column
        cols = []
        for j in range(n):
            dj = 0
            for i in range(nrow):
                if int(D[i, j]) != 0:
                    dj = int(D[i, j])
            cols.append(dj)
        from math import gcd
        ranges = []
        for dj in cols:
            if dj == 0:
                ranges.append(range(L_))
            else:
                g_ = gcd(abs(dj), L_)
                ranges.append([k * (L_ // g_) for k in range(g_)])
        Vm = [[int(V[i, j]) for j in range(n)] for i in range(n)]
        out = set()
        for z in itertools.product(*ranges):
            y = [sum(Vm[i][j] * z[j] for j in range(n)) % L_ for i in range(n)]
            full = [0] * len(self.edges)
            for i, fi in enumerate(free):
                full[fi] = y[i]
            out.add(tuple(full))
        return sorted(out)


def SpinCover(sw=SW, eps=EPS):
    """the root's spin cover: the double cover of its tetrahedral cover N cut out by the spin sign eps"""
    wl, N = L.tetra_cover(sw)
    return DoubleCover(N, L.level3(sw), eps)


def lattice_parity_character(Np, lat_fine=(2, 0, 2)):
    """for a fibre-direction cover Np whose lattice contains the finer lattice (default 2Z^2), the sign character of Np
    whose kernel is the finer cover with wbar 0: y -> the class of y's abelian image in Lam_p / Lam_fine, tau -> 0"""
    p, q, r = lat_fine
    out = []
    for w in Np.gword:
        v = [w.count("a") - w.count("A"), w.count("b") - w.count("B")]
        assert PC.in_lattice(Np.lat, tuple(v)), ("not in the coarse lattice", w)
        out.append(0 if PC.in_lattice(lat_fine, tuple(v)) else 1)
    return tuple(out) + (0,)


# ================================================================================================ route S~ (Shapiro on N)
_PRN = {}


def presentation_N(SC):
    """route P's presentation of N (sm:B1538's punct_present), and its Pres for the cohomology"""
    key = id(SC)
    if key not in _PRN:
        _PRN[key] = T.presentation_P(SC.N)
    return _PRN[key]


def m3_word(PrN, nword):
    """an N-word [(generator, +-1)] as a word in M_3's letters"""
    return "".join(PrN.gens[j][2] if s == 1 else PC.inv_word(PrN.gens[j][2]) for j, s in nword)


def sheet_walk(SC, word, start=0):
    cur = start
    for c in word:
        g = c.lower()
        cur = SC.perms[g][cur] if c.islower() else SC.pinv[g][cur]
    return cur


def sheets(SC, PrN):
    """the transversal of S in N: u_0 = 1 and u_1 = a loop of N at its coset 0 with eps = 1; and the right action of
    N's generators on the two sheets"""
    w1 = SC.u[SC.lab(0, 1)]
    u = [[], PrN.rewrite(w1, 0)]
    act = []
    for (_, _, w) in PrN.gens:
        row = []
        for s in range(2):
            end = sheet_walk(SC, m3_word(PrN, u[s]) + w, 0)
            assert end in (SC.lab(0, 0), SC.lab(0, 1)), "not a loop of N"
            row.append(0 if end == SC.lab(0, 0) else 1)
        act.append(row)
    return u, act


def inv_nword(nw):
    return [(j, -s) for j, s in reversed(nw)]


def read_SN(SC, chi, m, rngs=None):
    """route S~: the structure of Ind_S^N chi (x) rho on N's presentation and, for each rng, a generic interior class's
    count on S (the class read back as the coset-0 block)"""
    PrN, P = presentation_N(SC)
    F = T.holonomy(SC.level3)
    vals = SC.rs_values(chi, 0, m)
    u, act = sheets(SC, PrN)

    def chi_of(nw):
        return SC.chi_exp(m3_word(PrN, nw), vals, m)

    def four_of(nw):
        return T.to_list(T.word_four(F, m3_word(PrN, nw)))

    def ind_of(fn, size):
        mats = []
        for j in range(P.ngen):
            X = [[mp.mpc(0)] * (2 * size) for _ in range(2 * size)]
            for x in range(2):
                y = act[j][x]
                B = fn(u[x] + [(j, 1)] + inv_nword(u[y]))
                for i in range(size):
                    for k in range(size):
                        X[size * x + i][size * y + k] = B[i][k]
            mats.append(X)
        return mats

    def nu_rho(nw):
        z = T.root(chi_of(nw), m)
        Fw = four_of(nw)
        return [[z * Fw[i][k] for k in range(4)] for i in range(4)]
    A = ind_of(nu_rho, 4)
    modA = T.Mod(A)
    s = T.cohom(modA, P, want_interior=bool(rngs))
    out = {"structure": {k: s[k] for k in ("h0", "h1", "r1", "n", "gaps")}}
    if rngs:
        out["interior dimension"] = len(s["interior"])
        out["draws"] = []
    for rng in (rngs or []):
        if not s["interior"]:
            break
        z = T.generic(s["interior"], rng)
        e = 8

        def zword(nw):
            tot = [mp.mpc(0)] * e
            Pre = T.eye(e)
            for j, s_ in nw:
                if s_ == 1:
                    zj = z[j * e:(j + 1) * e]
                    tot = [t + v for t, v in zip(tot, T.matvec(Pre, zj))]
                    Pre = T.matmul(Pre, modA.M[j])
                else:
                    Pre = T.matmul(Pre, modA.Mi[j])
                    zj = z[j * e:(j + 1) * e]
                    tot = [t - v for t, v in zip(tot, T.matvec(Pre, zj))]
            return tot

        def W1_of(nw):
            nr = nu_rho(nw)
            ch = zword(nw)[:4]
            return [list(nr[i]) + [ch[i]] for i in range(4)] + [[mp.mpc(0)] * 4 + [mp.mpc(1)]]
        W1 = ind_of(W1_of, 5)
        L2 = ind_of(lambda nw: T.wedge2(W1_of(nw)), 10)
        m1, m2 = T.Mod(W1), T.Mod(L2)
        reads = {"W1": T.cohom(m1, P), "W1*": T.cohom(m1.dual(), P), "L2": T.cohom(m2, P),
                 "L2*": T.cohom(m2.dual(), P)}
        out["draws"].append({"count": [reads["W1"]["n"] - reads["W1*"]["n"], reads["L2"]["n"] - reads["L2*"]["n"]],
                             "reads": T._summ(reads)})
    return out


# ================================================================================================ the deck group 2T
def presentation_S(SC):
    """route P~'s presentation of S (sm:B1538's punct_present on this cover)"""
    return T.presentation_P(SC)


def key(SC, Pr, chi, m):
    """a character's values on route P~'s generators: a gauge-free key"""
    return tuple(Pr.values(chi, 0, m))


def golden_word(w):
    """conjugation by the root's stable letter t on a word of M_3 = +LRLRLR: phi on a and b, t_3 = t^3 fixed"""
    st1 = PC.State(SW)
    out = []
    for c in w:
        if c.lower() in "ab":
            img = st1.phi(c.lower())
            out.append(img if c.islower() else PC.inv_word(img))
        else:
            out.append(c)
    return "".join(out)


def action_matrices(SC, Pr):
    """the deck group of S over m004 (2T) on route P~'s generator values: chi o Ad(h) for h = u_y (y = 1..7, S's Q8 over
    M_3) and the golden map; each a matrix M with chi'(w_j) = sum_k M[j][k] chi(w_k)"""
    ng = len(Pr.gens)

    def row_of(word):
        v = [0] * ng
        for j, s in Pr.rewrite(PC.free_reduce(word), 0):
            v[j] += s
        return v
    mats = [[row_of(SC.u[y] + w + PC.inv_word(SC.u[y])) for (_, _, w) in Pr.gens] for y in range(1, SC.d)]
    mats.append([row_of(golden_word(w)) for (_, _, w) in Pr.gens])
    return mats
