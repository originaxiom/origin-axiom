#!/usr/bin/env python3
"""WP-1.5, main's second instrument for a cover: the kernel of a map to a finite group, by Reidemeister-Schreier.

WHY.  Main's cover instrument (B1602's forced_every.site_of) reads a cover through SnapPy's triangulation of the cover and
SnapPy's own presentation of its group.  That presentation does not say how the cover's group sits in the base's, so it
gives no deck action on the cover's characters: no orbits, no parities.  This module builds the cover's group from the
BASE's presentation alone.

WHAT.  M is a one-cusped manifold with SnapPy's presentation G = <x | r>, its holonomy and its peripheral pair (mu, lam).
q: G -> Q is onto a finite group.  K = ker q.
  transversal      rep[h], a word of G with q(rep[h]) = h, closed under prefixes (breadth first from the identity)
  generators       y(h, x) = rep[h] x rep[h q(x)]^-1 for every h in Q and generator x, those that are not the empty word
  rewriting        a word l_1 .. l_k of K, read from the coset of the identity: a letter x at coset h gives y(h, x), a
                   letter x^-1 at coset h gives y(h q(x)^-1, x)^-1                      (Reidemeister's tau)
  relators         tau(rep[h] r rep[h]^-1) for every h and every relator r             (the theorem of Reidemeister-Schreier)
  cusps            one for each coset h q(P) of the image of the peripheral group P; its peripheral pair is
                   rep[h] (basis of P meet K) rep[h]^-1
  holonomy         rho(y(h, x)) = rho(rep[h]) rho(x) rho(rep[h q(x)])^-1, from M's own matrices
  deck action      conjugation by rep[h], rewritten: an integer matrix on the exponents of a character
  characters       of order dividing d: the exponent vectors e mod d with (relator matrix) e = 0 mod d, by Smith's form
THE READING is main's sealed one (B1492's multicusp.Site.counts): h^1 from the Fox matrices, r^1 the rank of the
restriction to all cusps at once, n = h^1 - r^1.  `counts_mp` assembles the sealed code's matrices from Fox data computed
once (40 digits, ranks by the sealed routine MC.rank).  `as_room()` hands the same presentation to B1493's Room, letters
for generators, so that the sealed code itself can be run on it.  (A double-precision reading was tried and removed: the
singular values it kept and those it dropped met at 1e-7, so it could not decide a rank.)

HOW IT COULD FAIL: the number of generators must be |Q|(g - 1) + 1; every relator must hold in the holonomy to 1e-30;
the peripheral pairs must commute; the deck matrices must carry characters to characters; and on a sample the fast
assembly must give the sealed code's own answer (tested in the scripts that use this module)."""
import sys, pathlib, string, math
import sympy
from sympy.matrices.normalforms import smith_normal_decomp
from mpmath import mp, mpc, mpf, matrix, eye, zeros, exp, pi

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1492_the_three_ended_companion_read" / "verification"))
sys.path.insert(0, str(ROOT / "frontier" / "B1493_the_room_on_the_companions" / "verification"))
import multicusp as MC          # noqa: E402   (sets mp.dps = 40)
import room as RM               # noqa: E402

mp.dps = 60                     # SnapPy's high-precision holonomy carries 63 digits; B1492's module sets 40 on import.  At 40
                                # the peripheral pairs of the longer threads' covers commute only to 1e-29 (first run, 2026-11-12).
                                # The sealed rank routine and its tolerance (1e-24, relative) are used unchanged at 60 digits.

LETTERS = string.ascii_lowercase


def reduce_word(w):
    out = []
    for ch in w:
        if out and out[-1] == ch.swapcase(): out.pop()
        else: out.append(ch)
    return "".join(out)


def inv_word(w): return w[::-1].swapcase()


def sl2_inverse(m): return matrix([[m[1, 1], -m[0, 1]], [-m[1, 0], m[0, 0]]])


def four_of(Mx):
    """B1492's four: H -> g H g^* on Hermitian matrices, in the basis E11, E22, the two off-diagonal ones (copied from
    multicusp.Site.four, with nu = 1)"""
    Ms = matrix([[Mx[j, i].conjugate() for j in range(2)] for i in range(2)])
    basis = [matrix([[1, 0], [0, 0]]), matrix([[0, 0], [0, 1]]), matrix([[0, 1], [1, 0]]), matrix([[0, 1j], [-1j, 0]])]
    cols = []
    for H in basis:
        Hp = Mx * H * Ms; cols.append([Hp[0, 0], Hp[1, 1], (Hp[0, 1] + Hp[1, 0]) / 2, (Hp[0, 1] - Hp[1, 0]) / (2j)])
    return matrix([[cols[j][i] for j in range(4)] for i in range(4)])


class Kernel:
    def __init__(self, M, q, mul, inv, E, label="", shorten=False, longest=6, budget=40):
        """shorten: remove generators by Tietze moves.  A relator of at most `longest` letters in which a generator stands
        once gives that generator as a word in the others; it is substituted everywhere and the relator dropped, while the
        substitution adds at most `budget` letters in all.  The group, its cusps and the holonomy are the same; the
        matrices are smaller.  (The covers of the threads whose groups have three generators have 25 generators before.)"""
        H = M.high_precision(); G = H.fundamental_group()
        self.label = label or M.name(); self.Gobj = G
        self.g = list(G.generators()); self.r = list(G.relators())
        pc = G.peripheral_curves(); assert len(pc) == 1, "one cusp expected"
        self.mu, self.lam = pc[0]
        self.q, self.mul, self.inv, self.E = dict(q), mul, inv, E
        assert all(self.qw(rel) == E for rel in self.r), "q is not a homomorphism"
        assert self.mul(self.qw(self.mu), self.qw(self.lam)) == self.mul(self.qw(self.lam), self.qw(self.mu))
        # ---- the transversal
        self.rep = {E: ""}; frontier = [E]
        while frontier:
            nxt = []
            for h in frontier:
                for x in self.g:
                    for ch, hh in ((x, mul(h, self.q[x])), (x.upper(), mul(h, inv(self.q[x])))):
                        if hh not in self.rep:
                            self.rep[hh] = self.rep[h] + ch; nxt.append(hh)
            frontier = nxt
        self.Q = list(self.rep)
        # ---- the generators
        self.idx, self.gen_words = {}, []
        for h in self.Q:
            for x in self.g:
                w = reduce_word(self.rep[h] + x + inv_word(self.rep[mul(h, self.q[x])]))
                if w:
                    self.idx[(h, x)] = len(self.gen_words); self.gen_words.append(w)
        self.n = self.n_raw = len(self.gen_words)
        assert self.n == len(self.Q) * (len(self.g) - 1) + 1, (self.n, len(self.Q), len(self.g))
        assert self.n <= 26, "more than 26 generators: the letters run out"
        self._subst, self._new = {}, None                             # no generator removed yet: tau gives raw words
        # ---- the relators
        rels = []
        for h in self.Q:
            for rel in self.r:
                t = self.tau(self.rep[h] + rel + inv_word(self.rep[h]))
                if t and t not in rels: rels.append(t)
        self.rels = rels
        # ---- the cusps: P meet K, then one cusp for each coset of q(P)
        qm, ql = self.qw(self.mu), self.qw(self.lam)
        def power(a, k):
            out = E
            for _ in range(k): out = mul(out, a)
            return out
        d = next(k for k in range(1, len(self.Q) + 1) if power(ql, k) == E)
        i1, j1 = next((i, j) for i in range(1, len(self.Q) + 1) for j in range(d) if mul(power(qm, i), power(ql, j)) == E)
        self.periph_basis = ((i1, j1), (0, d))                       # P meet K = Z (i1, j1) + Z (0, d) in the basis mu, lam
        imgP = {mul(power(qm, i), power(ql, j)) for i in range(i1) for j in range(d)}
        assert len(imgP) == i1 * d
        seen, self.cusp_reps = set(), []
        for h in self.Q:
            if h in seen: continue
            self.cusp_reps.append(h); seen |= {mul(h, p) for p in imgP}
        assert len(self.cusp_reps) * len(imgP) == len(self.Q)
        w1 = self.mu * i1 + self.lam * j1; w2 = self.lam * d
        self.cusps = [(self.tau(self.rep[h] + w1 + inv_word(self.rep[h])), self.tau(self.rep[h] + w2 + inv_word(self.rep[h]))) for h in self.cusp_reps]
        if shorten: self._shorten(longest, budget)
        # ---- the holonomy on the generators of G and of K
        def m2(x):
            S = G.SL2C(x)
            return matrix([[mpc(MC.num(S[i, j].real()), MC.num(S[i, j].imag())) for j in range(2)] for i in range(2)])
        self.rho_G = {x: m2(x) for x in self.g}
        self.rho = [self.word_G(w) for w in self.gen_words]
        self.F = [four_of(m) for m in self.rho]
        self.Finv = [four_of(sl2_inverse(m)) for m in self.rho]
        # ---- the guards
        I4 = eye(4)
        self.relator_residual = max([max(abs(x) for x in (self.word_K(t) - I4)) for t in self.rels] or [mpf(0)])
        assert self.relator_residual < mpf(10) ** -30, ("a relator does not hold in the holonomy", self.relator_residual)
        self.peripheral_residual = mpf(0)
        for (a, b) in self.cusps:
            A, B = self.word_K(a), self.word_K(b)
            self.peripheral_residual = max(self.peripheral_residual, max(abs(x) for x in (A * B - B * A)))
        assert self.peripheral_residual < mpf(10) ** -30, ("a peripheral pair does not commute", self.peripheral_residual)
        self._prepare()

    # ------------------------------------------------------------------------------------------------ words
    def qw(self, w):
        p = self.E
        for ch in w: p = self.mul(p, self.q[ch] if ch.islower() else self.inv(self.q[ch.lower()]))
        return p

    def tau(self, w):
        """a word of G that lies in K, as a tuple of (generator of K, +-1), freely reduced"""
        h, out = self.E, []
        for ch in w:
            x = ch.lower()
            if ch.islower():
                k = self.idx.get((h, x)); h = self.mul(h, self.q[x]); s = 1
            else:
                h = self.mul(h, self.inv(self.q[x])); k = self.idx.get((h, x)); s = -1
            if k is None: continue
            if out and out[-1] == (k, -s): out.pop()
            else: out.append((k, s))
        assert h == self.E, "the word is not in the kernel"
        return self._final(tuple(out))

    @staticmethod
    def _fred(t):
        out = []
        for k, s in t:
            if out and out[-1] == (k, -s): out.pop()
            else: out.append((k, s))
        return tuple(out)

    @staticmethod
    def _inv_t(t): return tuple((k, -s) for k, s in reversed(t))

    def _final(self, t):
        """a raw word, with the removed generators written out and the others renumbered"""
        if not self._subst and self._new is None: return t
        out = []
        for k, s in t:
            w = self._subst.get(k)
            if w is None: out.append((k, s))
            else: out.extend(w if s > 0 else self._inv_t(w))
        out = self._fred(out)
        return tuple((self._new[k], s) for k, s in out) if self._new is not None else out

    def _shorten(self, longest, budget):
        import collections
        rels, cusps, subst, spent = list(self.rels), list(self.cusps), {}, 0
        while True:
            occ = collections.Counter(k for r in rels for k, _ in r); occ.update(k for a, b in cusps for k, _ in a + b)
            best = None
            for ri, r in enumerate(rels):
                if len(r) > longest: continue
                cnt = collections.Counter(k for k, _ in r)
                for k, c in cnt.items():
                    if c == 1:
                        cost = (len(r) - 2) * (occ[k] - 1)
                        if best is None or cost < best[0]: best = (cost, ri, k)
            if best is None or spent + best[0] > budget: break
            cost, ri, k = best; r = rels[ri]; spent += cost
            i = next(j for j, (kk, _) in enumerate(r) if kk == k); sgn = r[i][1]
            w = self._fred(self._inv_t(r[:i]) + self._inv_t(r[i + 1:]))    # A k^s B = 1  gives  k^s = A^-1 B^-1
            wk = w if sgn == 1 else self._inv_t(w)
            def sub(t):
                out = []
                for kk, ss in t:
                    if kk == k: out.extend(wk if ss > 0 else self._inv_t(wk))
                    else: out.append((kk, ss))
                return self._fred(out)
            new_rels = []
            for j, r2 in enumerate(rels):
                if j == ri: continue
                x = sub(r2)
                if x and x not in new_rels: new_rels.append(x)
            rels = new_rels; cusps = [(sub(a), sub(b)) for a, b in cusps]
            subst = {kk: sub(v) for kk, v in subst.items()}; subst[k] = wk
        kept = [k for k in range(self.n_raw) if k not in subst]
        self._subst = subst; self._new = {k: i for i, k in enumerate(kept)}
        ren = lambda t: tuple((self._new[k], s_) for k, s_ in t)
        self.rels = [ren(r) for r in rels]; self.cusps = [(ren(a), ren(b)) for a, b in cusps]
        self.gen_words = [self.gen_words[k] for k in kept]; self.n = len(kept)
        self.removed = len(subst); self.letters_added = spent

    def word_G(self, w):
        R = eye(2)
        for ch in w: R = R * (self.rho_G[ch] if ch.islower() else sl2_inverse(self.rho_G[ch.lower()]))
        return R

    def word_K(self, t):
        R = eye(4)
        for k, s in t: R = R * (self.F[k] if s > 0 else self.Finv[k])
        return R

    def exps(self, t):
        v = [0] * self.n
        for k, s in t: v[k] += s
        return v

    # ------------------------------------------------------------------------------------------- characters
    def relator_matrix(self): return [self.exps(t) for t in self.rels]

    def characters(self, d):
        """every exponent vector e mod d with (relator matrix) e = 0 mod d, as tuples"""
        A = sympy.Matrix(self.relator_matrix())
        S, U, V = smith_normal_decomp(A, sympy.ZZ)                       # S = U A V
        k = min(S.shape); choices = []
        for i in range(self.n):
            s = int(S[i, i]) if i < k else 0
            step = d // math.gcd(d, s) if s else 1
            choices.append(range(0, d, step))
        Vm = [[int(V[i, j]) % d for j in range(self.n)] for i in range(self.n)]
        out = set()
        import itertools
        for f in itertools.product(*choices):
            e = tuple(sum(Vm[i][j] * f[j] for j in range(self.n)) % d for i in range(self.n))
            out.add(e)
        A_int = self.relator_matrix()
        assert all(all(sum(a * b for a, b in zip(row, e)) % d == 0 for row in A_int) for e in out)
        return sorted(out)

    def deck_matrix(self, h):
        """row i: the exponents of rep[h] y_i rep[h]^-1.  A character with exponents e goes to (matrix) e."""
        return [self.exps(self.tau(self.rep[h] + self.gen_words[i] + inv_word(self.rep[h]))) for i in range(self.n)]

    def act(self, Cm, e, d): return tuple(sum(a * b for a, b in zip(row, e)) % d for row in Cm)

    def value(self, e, d, t):
        """the exponent mod d of the character on a word of K"""
        return sum(e[k] * s for k, s in t) % d

    # ---------------------------------------------------------------------------- the Fox data, once for all
    def _fox(self, t):
        """the occurrences of each generator in a word of K: (generator, sign, exponents of the prefix, its matrix)"""
        val, ex, out = eye(4), [0] * self.n, []
        for k, s in t:
            if s > 0:
                out.append((k, 1, tuple(ex), val.copy())); val = val * self.F[k]; ex[k] += 1
            else:
                val = val * self.Finv[k]; ex[k] -= 1; out.append((k, -1, tuple(ex), val.copy()))
        return out, tuple(ex), val

    def _prepare(self):
        self.fox_rels = [self._fox(t)[0] for t in self.rels]
        self.fox_cusps = []
        for (a, b) in self.cusps:
            fa, ea, Wa = self._fox(a); fb, eb, Wb = self._fox(b)
            self.fox_cusps.append((fa, ea, Wa, fb, eb, Wb))

    # --------------------------------------------------------------------------------- the reading, 40 digits
    def counts_mp(self, e, d):
        z = [exp(2j * pi * k / d) for k in range(d)]
        nu = lambda ex: z[sum(a * b for a, b in zip(ex, e)) % d]
        n, ng = 4, self.n; I4 = eye(4)
        d0 = MC.stack([z[e[k] % d] * self.F[k] - I4 for k in range(ng)])
        d1 = zeros(n * len(self.rels), n * ng)
        for ri, occ in enumerate(self.fox_rels):
            for (k, s, ex, P) in occ:
                c = nu(ex) * s
                for i in range(4):
                    for j in range(4): d1[n * ri + i, n * k + j] += c * P[i, j]
        Rs, Bs, t0 = [], [], []
        for (fa, ea, Wa, fb, eb, Wb) in self.fox_cusps:
            R = zeros(2 * n, n * ng)
            for off, occ in ((0, fa), (n, fb)):
                for (k, s, ex, P) in occ:
                    c = nu(ex) * s
                    for i in range(4):
                        for j in range(4): R[off + i, n * k + j] += c * P[i, j]
            B = MC.stack([nu(ea) * Wa - I4, nu(eb) * Wb - I4]); Rs.append(R); Bs.append(B); t0.append(n - MC.rank(B))
        r0, rd1 = MC.rank(d0), MC.rank(d1); a0 = n - r0; a1 = ng * n - rd1 - r0
        rows_R = sum(R.rows for R in Rs); cols_B = sum(B.cols for B in Bs)
        block = zeros(d1.rows + rows_R, d1.cols + cols_B); block[:d1.rows, :d1.cols] = d1
        r, c = d1.rows, d1.cols
        for R, B in zip(Rs, Bs):
            block[r:r + R.rows, :R.cols] = R; block[r:r + R.rows, c:c + B.cols] = B; r += R.rows; c += B.cols
        rBT = sum(MC.rank(B) for B in Bs); r1 = MC.rank(block) - rd1 - rBT
        return dict(a0=a0, a1=a1, t0=t0, t0_sum=sum(t0), r1=r1, n=a1 - r1)

    # ----------------------------------------------------------------- the same presentation for the sealed code
    def letters(self, t): return "".join(LETTERS[k] if s > 0 else LETTERS[k].upper() for k, s in t)

    def as_room(self):
        S = RM.Room.__new__(RM.Room); S.name = self.label; S.M = None
        S.gens = [LETTERS[k] for k in range(self.n)]; S.rels = [self.letters(t) for t in self.rels]
        S.cusps = [(self.letters(a), self.letters(b)) for (a, b) in self.cusps]
        S.rho = {LETTERS[k]: self.rho[k] for k in range(self.n)}; S.m = len(S.cusps)
        return S

    def nu_of(self, e, d):
        z = [exp(2j * pi * k / d) for k in range(d)]
        return {LETTERS[k]: z[e[k] % d] for k in range(self.n)}
