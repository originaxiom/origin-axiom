#!/usr/bin/env python3
"""Modules of any rank on a level of a signed word state, over a prime field, for main's index code (B1427).

Level        the level's group, its monodromy-fixed characters, the extension cocycle of a character and its boundary
             vector (value on the meridian, value on the longitude).
two_step     W = (sum of characters alpha_i) extended by (sum of characters beta_j), a class on each chosen edge.
n_formula    the interior-class count of a two-step module from boundary data alone: dim(D cap Im C).
build        a triangular module with given diagonal characters, one superdiagonal at a time; None if obstructed.
ext2, dsum   exterior square, direct sum.
"""
import sys, itertools, random, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1435_the_interaction_census" / "verification"))
import interaction_census as ic
from relcup import Bundle, Cocycle, solve
from myindex import Mod, index, cohom, rank_and_null
cc = ic.cc

class Level:
    def __init__(self, eps, word, k, pstart=3000):
        self.ng, self.rels, self.mu, self.lam, self.tau, A, self.tors = ic.ac.level(eps, word, k)
        self.N = max(1, ic.ac.torsion_exponent(A)); self.p = cc.primes_1mod(self.N, 1, pstart)[0]
        self.zeta = pow(cc.primroot(self.p), (self.p - 1) // self.N, self.p)
        self.chars = [c for c in cc.characters(self.rels, self.mu, 3, self.N)]
        self.Lr = [cc.letters(r) for r in self.rels]; self.Lmu = cc.letters(self.mu); self.Llam = cc.letters(self.lam)
        self.B = Bundle(ic.Phi_of(eps, word, k)); self.lamel = (self.B.lam, 0)
        self.coc = {}; self.bdry = {}
    def val(self, c): return [pow(self.zeta, e % self.N, self.p) for e in c]
    def cocycle(self, c):
        """a non-coboundary cocycle of the character c, and its boundary vector (value on mu, value on lam)"""
        if c not in self.coc:
            h1, ct = cc.cocycle(c, self.rels, 3, self.N, self.zeta, self.p); assert ct is not None
            co = Cocycle(ic.char_module(self.B, c, self.N, self.zeta, self.p), [ct[0]], [ct[1]], [ct[2]])
            self.coc[c] = ct; self.bdry[c] = (co.vt[0] % self.p, co(self.lamel)[0] % self.p)
        return self.coc[c], self.bdry[c]
    def add(self, x, y): return tuple((a + b) % self.N for a, b in zip(x, y))
    def neg(self, x): return tuple((-a) % self.N for a in x)

def two_step(L, alphas, betas, gamma):
    """gamma[(i, j)] in GF(p): the coefficient of the extension class on the edge (i, j) (0 = no edge)"""
    p = L.p; a, b = len(alphas), len(betas); d = a + b; gens = ["a", "b", "c"]; mats = {}
    for gi, g in enumerate(gens):
        M = [[0] * d for _ in range(d)]
        for i, al in enumerate(alphas): M[i][i] = L.val(al)[gi]
        for j, be in enumerate(betas): M[a + j][a + j] = L.val(be)[gi]
        for (i, j), gm in gamma.items():
            if gm:
                ct, _ = L.cocycle(L.add(alphas[i], L.neg(betas[j])))
                M[i][a + j] = gm * ct[gi] % p * L.val(betas[j])[gi] % p
        mats[g] = M
    V = Mod(gens, mats, p); assert V.ok(L.Lr), "not a representation"
    return V

def n_formula(L, alphas, betas, gamma):
    p = L.p; a, b = len(alphas), len(betas); rowsC = []
    for j in range(b):
        vec = [0] * (2 * a)
        for i in range(a):
            gm = gamma.get((i, j), 0)
            if gm:
                _, (cm, cl) = L.cocycle(L.add(alphas[i], L.neg(betas[j]))); vec[2 * i] = gm * cm % p; vec[2 * i + 1] = gm * cl % p
        rowsC.append(vec)
    rowsD = []
    for i in range(a):
        _, (um, ul) = L.cocycle(alphas[i]); vec = [0] * (2 * a); vec[2 * i] = um; vec[2 * i + 1] = ul; rowsD.append(vec)
    rk = lambda rows: rank_and_null(rows, 2 * a, p)[0] if rows else 0
    return rk(rowsD) + rk(rowsC) - rk(rowsD + rowsC)

def dual_data(L, alphas, betas, gamma):
    return [L.neg(b) for b in betas], [L.neg(a) for a in alphas], {(j, i): g for (i, j), g in gamma.items()}

def build(L, chars, coeff):
    p = L.p; n = len(chars); gens = ["a", "b", "c"]
    vals = [L.val(c) for c in chars]
    M = {g: [[(vals[i][gi] if i == j else 0) for j in range(n)] for i in range(n)] for gi, g in enumerate(gens)}
    def relator_entries(i, j):
        V = Mod(gens, M, p); out = []
        for r in L.Lr: out.append(V.word(r)[i][j])
        return out
    for m in range(1, n):
        for i in range(n - m):
            j = i + m
            base = relator_entries(i, j)                      # with the unknowns at zero
            cols = []
            for gi, g in enumerate(gens):
                M[g][i][j] = 1; e = relator_entries(i, j); M[g][i][j] = 0
                cols.append([(a - b) % p for a, b in zip(e, base)])
            rows = [[cols[0][r], cols[1][r], cols[2][r]] for r in range(len(L.Lr))]
            sol = solve(rows, [(-b) % p for b in base], p)
            if sol is None: return None
            l = L.add(chars[i], L.neg(chars[j])); gm = coeff.get((i, j), 0)
            if gm and any(l):
                ct, _ = L.cocycle(l)
                sol = [(sol[gi] + gm * ct[gi] * vals[j][gi]) % p for gi in range(3)]
            for gi, g in enumerate(gens): M[g][i][j] = sol[gi]
    V = Mod(gens, M, p)
    assert V.ok(L.Lr), "not a representation"
    return V

def ext2(V):
    p = V.p; d = V.d; pairs = [(i, j) for i in range(d) for j in range(i + 1, d)]; mats = {}
    for g in V.gens:
        A = V.M[g]
        mats[g] = [[(A[i][k] * A[j][l] - A[i][l] * A[j][k]) % p for (k, l) in pairs] for (i, j) in pairs]
    return Mod(V.gens, mats, p)

def dsum(V, W):
    d = V.d + W.d; mats = {}
    for g in V.gens:
        M = [[0] * d for _ in range(d)]
        for i in range(V.d):
            for j in range(V.d): M[i][j] = V.M[g][i][j]
        for i in range(W.d):
            for j in range(W.d): M[V.d + i][V.d + j] = W.M[g][i][j]
        mats[g] = M
    return Mod(V.gens, mats, V.p)
