#!/usr/bin/env python3
"""B1462 -- main's own route to the SM seat's B1522 on the levels M_1..M_6 of m004: which twists of a vacuum
nu (x) rho_q are fixed by a count-odd map, for lambda generic off the unit circle.

Nothing here is the seat's code.  Steps, each checked against something that could fail:
 1. the symmetries of pi_1(m004) in Ballas' presentation <m, n | R>: maps m -> u, n -> v over reduced words of length
    <= 4 that send R to the identity in the SL(2, C) holonomy (filter) AND in Ballas' SL(4, Q) representation at q = 2
    (exact), and whose square is inner (an involution up to conjugacy; the search also keeps the order-4 classes if any);
    classified by orientation (the SL(2) character conjugated or kept), the meridian sign eps (exponent sum of u) and the
    longitude (tr rho_2(beta(l)) against tr rho_2(l) = 3q + q^-3 and tr rho_2(l^-1) = 3/q + q^3): a map DUALISES when the
    longitude is inverted (B1455);
 2. transport to SnapPy's <a, b | aaabABBAb> through m = ab, n = aabA, a = MnmN, b = nMNmm (verified in the holonomy);
 3. H_1(M_n) = ker d1 / im d2 of the Fox complex over Z[Z/n] (Shapiro; no Reidemeister-Schreier), Smith form with
    transforms (B1297's d2lib); the induced map of each symmetry, semilinear by t -> t^eps; the deck lifts are
    conjugation by b (phi(b) = 1), i.e. multiplication by t;
 4. a torsion character nu_F of T_n together with lambda generic off the circle is FIXED by a count-odd map iff some
    dualising beta with eps = -1 (a lift of a strong inversion -- for eps = +1 the free part forces |lambda| = 1, and
    so does conjugation of the twist) satisfies nu_F(beta_* x) = nu_F(x)^-1 on T_n and nu_F(tau_beta) = 1 where
    beta_*(z) = -z + tau_beta.  Counted for every nu_F.
Controls: n = 1 (T_1 trivial: zero unfixed, as B1455); the invariant factors of T_n against coker(Phi^n - 1) with
Phi = [[2,1],[1,1]]; d1 d2 = 0; every induced map preserves ker d1 and im d2.
"""
import sys, os, json, itertools, cmath, pathlib
from fractions import Fraction as F
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1297_the_spectral_cover_index" / "verification"))
import d2lib as DL
import snappy

SWAP = str.maketrans("mnMN", "MNmn")
def inv(w): return w[::-1].translate(SWAP)
def reduce(w):
    out = []
    for c in w:
        if out and out[-1] == c.translate(SWAP): out.pop()
        else: out.append(c)
    return "".join(out)
def subst(w, img):   # img: {'m': word, 'n': word}
    out = ""
    for c in w: out += img[c.lower()] if c.islower() else inv(img[c.lower()])
    return reduce(out)
R = "mnMNmNMnmN"; LONG = "nMNmmNMn"

# ---------------------------------------------------------------- representations
def mul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def ident(k, one=F(1)): return [[one if i == j else one * 0 for j in range(k)] for i in range(k)]
def tr(A): return sum(A[i][i] for i in range(len(A)))
def inverse4(A):
    n = len(A); M = [[F(x) for x in r] + [F(int(i == j)) for j in range(n)] for i, r in enumerate(A)]
    for c in range(n):
        p = next(i for i in range(c, n) if M[i][c] != 0); M[c], M[p] = M[p], M[c]
        pv = M[c][c]; M[c] = [x / pv for x in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0: M[i] = [x - M[i][c] * y for x, y in zip(M[i], M[c])]
    return [r[n:] for r in M]
def ballas(q):
    t = F(q) / 2
    m = [[F(1), F(0), F(1), t - 1], [F(0), F(1), F(1), t], [F(0), F(0), F(1), t + F(1, 2)], [F(0), F(0), F(0), F(1)]]
    n = [[F(1), F(0), F(0), F(0)], [2 + 1 / t, F(1), F(0), F(0)], [F(2), F(1), F(1), F(0)], [F(1), F(1), F(0), F(1)]]
    return {"m": m, "n": n, "M": inverse4(m), "N": inverse4(n)}
def wordmat(w, g, k):
    first = next(iter(g.values()))[0][0]
    A = ident(k, F(1)) if isinstance(first, F) else [[complex(i == j) for j in range(k)] for i in range(k)]
    for c in w: A = mul(A, g[c])
    return A
def holonomy():
    """SnapPy's m004 holonomy, lifted to a genuine SL(2) rep by a -> -a, transported to m = ab, n = aabA"""
    M = snappy.Manifold("m004"); G = M.fundamental_group()
    assert G.generators() == ["a", "b"] and G.relators() == ["aaabABBAb"]
    cx = lambda X: [[complex(X[0][0]), complex(X[0][1])], [complex(X[1][0]), complex(X[1][1])]]
    a = cx(G.SL2C("a")); b = cx(G.SL2C("b")); a = [[-x for x in r] for r in a]
    inv2 = lambda A: [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]
    ab = {"a": a, "b": b, "A": inv2(a), "B": inv2(b)}
    m = wordmat("ab", ab, 2); n = wordmat("aabA", ab, 2)
    return {"m": m, "n": n, "M": inv2(m), "N": inv2(n)}, ab
def close(A, B, tol=1e-9): return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A))) < tol
def pm_identity(A):
    k = len(A); I = [[complex(i == j) for j in range(k)] for i in range(k)]
    return close(A, I) or close(A, [[-x for x in r] for r in I])

# ---------------------------------------------------------------- step 1: the symmetries
def symmetries(maxlen=4):
    g2, _ = holonomy(); g4 = ballas(2)
    words = [""]
    for L in range(1, maxlen + 1):
        words += ["".join(p) for p in itertools.product("mnMN", repeat=L) if reduce("".join(p)) == "".join(p)]
    words = [w for w in words if w]
    expo = lambda w: sum(1 if c.islower() else -1 for c in w)
    zero_sum = [w for w in ["mN", "mnMN", "mmNN", "mNmN", "mnmNMN"]]
    probe = next(w for w in zero_sum if abs(tr(wordmat(w, g2, 2)).imag) > 1e-6)
    t_probe = tr(wordmat(probe, g2, 2))
    tl, tli = tr(wordmat(LONG, g4, 4)), tr(wordmat(inv(LONG), g4, 4)); assert tl != tli
    found = []
    for u in words:
        if abs(expo(u)) != 1: continue
        for v in words:
            if expo(v) != expo(u): continue
            img = {"m": u, "n": v}
            if not pm_identity(wordmat(subst(R, img), g2, 2)): continue
            if wordmat(subst(R, img), g4, 4) != ident(4): continue          # exact, in SL(4, Q)
            tp = tr(wordmat(subst(probe, img), g2, 2))
            orient = "preserving" if abs(tp - t_probe) < 1e-6 else ("reversing" if abs(tp - t_probe.conjugate()) < 1e-6 else "?")
            tL = tr(wordmat(subst(LONG, img), g4, 4))
            longitude = "kept" if tL == tl else ("inverted" if tL == tli else "?")
            found.append(dict(m=u, n=v, eps=expo(u), orientation=orient, longitude=longitude, dualising=(longitude == "inverted")))
    # drop the degenerate endomorphisms (onto a cyclic subgroup: the relator holds, the character does not)
    found = [f for f in found if f["orientation"] != "?" and f["longitude"] != "?"]
    return found

# ---------------------------------------------------------------- step 2: transport to <a, b>
AB = {"m": "ab", "n": "aabA"}          # Ballas' generators in SnapPy's
MN = {"a": "MnmN", "b": "nMNmm"}       # SnapPy's generators in Ballas'
SWAP_AB = str.maketrans("abAB", "ABab")
def inv_ab(w): return w[::-1].translate(SWAP_AB)
def reduce_ab(w):
    out = []
    for c in w:
        if out and out[-1] == c.translate(SWAP_AB): out.pop()
        else: out.append(c)
    return "".join(out)
def to_ab(w_mn):
    out = ""
    for c in w_mn: out += AB[c.lower()] if c.islower() else inv_ab(AB[c.lower()])
    return reduce_ab(out)
def transport(beta_mn):
    """beta on a, b: a = MnmN -> beta(MnmN) in m, n -> in a, b"""
    return {g: to_ab(subst(MN[g], beta_mn)) for g in "ab"}

# ---------------------------------------------------------------- step 3: Fox over Z[Z/n]
PHI = {"a": 0, "b": 1}      # the abelianisation of <a, b | aaabABBAb>: the relator's exponent sums are a: 1, b: 0, so a -> 0, b -> 1 (B1297)
def perm(n, k):
    P = [[0] * n for _ in range(n)]
    for j in range(n): P[(j + k) % n][j] = 1
    return P
def imul(X, Y): return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]
def iadd(X, Y): return [[a + b for a, b in zip(r, s)] for r, s in zip(X, Y)]
def isub(X, Y): return [[a - b for a, b in zip(r, s)] for r, s in zip(X, Y)]
def fox(word_ab, n, phi=None):
    """Fox derivatives of a word in a, b in the regular representation of Z/n (phi: a -> 0, b -> 1), as n x n integer blocks"""
    phi = phi or PHI
    D = {g: [[0] * n for _ in range(n)] for g in "ab"}; Pm = perm(n, 0)
    for c in word_ab:
        g, e = c.lower(), (1 if c.islower() else -1)
        if e == 1: D[g] = iadd(D[g], Pm); Pm = imul(Pm, perm(n, phi[g]))
        else: Pm = imul(Pm, perm(n, -phi[g])); D[g] = isub(D[g], Pm)
    return D
def block(rows_of_blocks, n):
    out = []
    for br in rows_of_blocks:
        for i in range(n): out.append([x for blk in br for x in blk[i]])
    return out

class Cover:
    def __init__(self, n):
        self.n = n
        self.d1 = block([[isub(perm(n, PHI[g]), perm(n, 0)) for g in "ab"]], n)        # n x 2n   (g - 1)
        D = fox("aaabABBAb", n); self.d2 = block([[D["a"]], [D["b"]]], n)              # 2n x n
        assert all(x == 0 for r in imul(self.d1, self.d2) for x in r), "d1 d2 != 0"
        # ker d1 by Smith: U d1 V = Dg ; kernel basis = last columns of V
        Dg, U, V = DL.smith([r[:] for r in self.d1], 2 * n)
        rk = sum(1 for i in range(min(len(Dg), len(Dg[0]))) if Dg[i][i] != 0)
        self.K = [[V[i][j] for i in range(2 * n)] for j in range(rk, 2 * n)]          # kernel vectors (rows), length 2n
        self.rk = rk; self.kdim = 2 * n - rk
        # express im d2 in the kernel basis: solve K^T c = d2 column (integer, since im d2 <= ker d1)
        self.Kinv = self._left_inverse()                                              # (kdim x 2n) with Kinv K^T = I
        cols = [[self.d2[i][j] for i in range(2 * n)] for j in range(n)]
        self.B = [[sum(self.Kinv[a][i] * c[i] for i in range(2 * n)) for a in range(self.kdim)] for c in cols]  # n x kdim
        for c, b in zip(cols, self.B): assert c == [sum(b[a] * self.K[a][i] for a in range(self.kdim)) for i in range(2 * n)]
        self.B = [[_int(x) for x in r] for r in self.B]
        # H1 = Z^kdim / rowspan(B): Smith of B (n x kdim): U B V = Dg2 ; coordinates y = V^-1 x ; H1 = (+) Z/Dg2[i][i] (+) Z^free
        Dg2, U2, V2 = DL.smith([r[:] for r in self.B], self.kdim)
        # rows of B are relation vectors r in x-coordinates; U2 B V2 = D2 means the relation lattice is V2^{-T}(rowspan D2),
        # so in the coordinates y = V2^T x the relations read y_i = 0 mod d_i
        self.V2T = [list(c) for c in zip(*V2)]; self.V2Tinv = DL_inv(self.V2T)
        diag = [Dg2[i][i] if i < len(Dg2) and i < len(Dg2[0]) else 0 for i in range(self.kdim)]
        self.invariants = [abs(d) for d in diag]                                     # 1 = killed, k > 1 torsion, 0 free
        self.torsion = [(i, abs(d)) for i, d in enumerate(diag) if abs(d) > 1]
        self.free = [i for i, d in enumerate(diag) if d == 0]
        assert len(self.free) == 1, self.invariants
    def _left_inverse(self):
        # K rows are a Z-basis of a saturated sublattice; a rational left inverse suffices for integer solutions
        from fractions import Fraction as Fr
        K = self.K; k = len(K); m = len(K[0])
        G = [[sum(K[a][i] * K[b][i] for i in range(m)) for b in range(k)] for a in range(k)]
        Gi = inverse4([[Fr(x) for x in r] for r in G])
        return [[sum(Gi[a][b] * K[b][i] for b in range(k)) for i in range(m)] for a in range(k)]
    def induced(self, beta_ab, eps):
        """the matrix of beta_* on H1 coordinates y (Smith coordinates of the kernel): y -> M y"""
        n = self.n
        D = {g: fox(beta_ab[g], n) for g in "ab"}                      # D[g][h] = d beta(g) / d h
        T = [[0] * (2 * n) for _ in range(2 * n)]
        for gi, g in enumerate("ab"):
            for k in range(n):
                col = gi * n + k                                           # source t^k e_g
                tw = perm(n, eps * k)
                for hi, h in enumerate("ab"):
                    v = imul(tw, D[g][h]); vec = [v[i][0] for i in range(n)]  # image of e_g (k = 0) twisted by t^{eps k}
                    for i in range(n): T[hi * n + i][col] = vec[i]
        # action on kernel coordinates: K^T x -> T K^T x ; must stay in ker d1 and preserve im d2
        imgK = [[sum(T[i][j] * self.K[a][j] for j in range(2 * n)) for i in range(2 * n)] for a in range(self.kdim)]
        for v in imgK: assert all(sum(self.d1[i][j] * v[j] for j in range(2 * n)) == 0 for i in range(n)), "not into ker d1"
        A = [[sum(self.Kinv[b][i] * imgK[a][i] for i in range(2 * n)) for b in range(self.kdim)] for a in range(self.kdim)]  # row a = coords of beta_*(K_a)
        for a in range(self.kdim): assert imgK[a] == [sum(A[a][b] * self.K[b][i] for b in range(self.kdim)) for i in range(2 * n)]
        A = [[_int(x) for x in r] for r in A]
        # in Smith coordinates y = V2^T x ; beta_*: x -> A^T x ; so y -> V2^T A^T V2^{-T} y
        At = [[A[b][a] for b in range(self.kdim)] for a in range(self.kdim)]
        M = imul(imul(self.V2T, At), self.V2Tinv)
        return M
def _int(x):
    from fractions import Fraction as Fr
    assert isinstance(x, int) or (isinstance(x, Fr) and x.denominator == 1), x
    return int(x)
def DL_inv(V):
    from fractions import Fraction as Fr
    k = len(V); Vi = inverse4([[Fr(x) for x in r] for r in V])
    assert all(x.denominator == 1 for r in Vi for x in r); return [[int(x) for x in r] for r in Vi]

# ---------------------------------------------------------------- step 4: the characters
def unfixed_count(cov, maps):
    """maps: list of (M, eps) induced matrices; a torsion character is a tuple of residues c_i mod d_i (nu(y_i) = e^{2 pi i c_i / d_i});
    fixed iff some map with eps = -1 has nu(M y) = nu(y)^-1 on the torsion generators and nu(tau) = 1 where M z = -z + tau"""
    tors = cov.torsion; z = cov.free[0]
    chars = list(itertools.product(*[range(d) for _, d in tors]))
    def val(c, vec):   # nu on a coordinate vector, as a rational mod 1
        s = F(0)
        for (i, d), ci in zip(tors, c): s += F(ci * vec[i], d)
        return s % 1
    fixed = set(); dualising_lifts = 0
    for M, eps in maps:
        if eps != -1: continue
        dualising_lifts += 1
        Mz = [M[r][z] for r in range(cov.kdim)]
        assert Mz[z] == -1, ("a strong inversion must send z to -z + torsion", Mz[z])
        assert all(M[r][z] == 0 for r in cov.free if r != z)
        for c in chars:
            if c in fixed: continue
            if val(c, Mz) != 0: continue
            ok = True
            for (i, d), ci in zip(tors, c):
                col = [M[r][i] for r in range(cov.kdim)]
                if (val(c, col) + F(ci, d)) % 1 != 0: ok = False; break
            if ok: fixed.add(c)
    return len(chars), len(chars) - len(fixed), dualising_lifts

def main():
    out = dict(symmetries=[], levels=[])
    found = symmetries()
    for f in found:
        f = dict(f); f["ab"] = transport({"m": f["m"], "n": f["n"]}); out["symmetries"].append(f)
    # the eight classes: (orientation, eps, longitude) and the action on T_2 = Z/5 (P acts as -1 on the fibre, the identity as +1, the order-four symmetries as +-2)
    c2 = Cover(2); assert [d for _, d in c2.torsion] == [5]
    ti = c2.torsion[0][0]
    for f in out["symmetries"]:
        M = c2.induced(f["ab"], f["eps"]); f["sign_on_T2"] = M[ti][ti] % 5
        assert f["sign_on_T2"] in (1, 2, 3, 4), f          # 1 = identity-like, 4 = P-like (-1); 2 and 3 = the order-four classes, whose square is P
    classes = {}
    for f in out["symmetries"]:
        key = (f["orientation"], f["eps"], f["longitude"], f["sign_on_T2"])
        if key not in classes or len(f["m"]) + len(f["n"]) < len(classes[key]["m"]) + len(classes[key]["n"]): classes[key] = f
    assert len(classes) == 8, sorted(classes)
    for key, f in sorted(classes.items()):
        print("%-10s eps %+d longitude %-8s dualising %-5s T2 %s  m->%-5s n->%-6s  a->%-12s b->%s" % (f["orientation"], f["eps"], f["longitude"], f["dualising"], {1: "+1", 4: "-1", 2: "x2", 3: "x3"}[f["sign_on_T2"]], f["m"], f["n"], f["ab"]["a"], f["ab"]["b"]))
    out["classes"] = [dict(v, key=list(map(str, k))) for k, v in sorted(classes.items())]
    print("%d symmetry words kept, 8 classes" % len(out["symmetries"]))
    # the transport is consistent: the holonomy of beta(a), beta(b) in a, b equals that of beta(MnmN), beta(nMNmm) in m, n
    g2, ab = holonomy()
    for f in out["symmetries"]:
        for g in "ab":
            X = wordmat(f["ab"][g], ab, 2); Y = wordmat(subst(MN[g], {"m": f["m"], "n": f["n"]}), g2, 2)
            assert close(X, Y) or close(X, [[-x for x in r] for r in Y]), "transport"
    Phi = [[2, 1], [1, 1]]
    for n in range(1, 7):
        cov = Cover(n)
        # control: the torsion of coker(Phi^n - 1)
        Pn = [[1, 0], [0, 1]]
        for _ in range(n): Pn = imul(Pn, Phi)
        Dg, _, _ = DL.smith([[Pn[0][0] - 1, Pn[0][1]], [Pn[1][0], Pn[1][1] - 1]], 2)
        want = sorted(abs(Dg[i][i]) for i in range(2) if abs(Dg[i][i]) > 1); have = sorted(d for _, d in cov.torsion)
        assert want == have, (n, want, have)
        maps = []
        for f in out["symmetries"]:
            if not f["dualising"]: continue
            M0 = cov.induced(f["ab"], f["eps"])
            maps.append((M0, f["eps"]))
            # compose with the deck transformation k times (conjugation by b, phi(b) = 1: a -> b a B, b -> b)
            Mt = cov.induced({"a": "baB", "b": "b"}, 1)
            Mk = M0
            for k in range(1, n):
                Mk = imul(Mt, Mk); maps.append((Mk, f["eps"]))
        total, unfixed, lifts = unfixed_count(cov, maps)
        lev = dict(n=n, invariant_factors=have, torsion_characters=total, unfixed_off_circle=unfixed, dualising_strong_inversion_lifts=lifts)
        out["levels"].append(lev)
        print("M_%d: T_n invariants %s, %d twists, %d unfixed off the circle (%d strong-inversion lifts tried)" % (n, have, total, unfixed, lifts), flush=True)
    # the golden reading on M_5 (sm:B1522 Lemmas C and G, the M_5 case): the unfixed twists are exactly the single-sheet
    # characters -- the eigenvectors of the deck action on the dual of T_5 = F_11^2 -- ten on each sheet
    cov = Cover(5); tors = cov.torsion; z = cov.free[0]; p = 11; assert [d for _, d in tors] == [p, p]
    Mt = cov.induced({"a": "baB", "b": "b"}, 1); ti = [i for i, _ in tors]
    Phi5 = [[Mt[r][c] % p for c in ti] for r in ti]
    trc = (Phi5[0][0] + Phi5[1][1]) % p; det = (Phi5[0][0] * Phi5[1][1] - Phi5[0][1] * Phi5[1][0]) % p
    eig = [x for x in range(p) if (x * x - trc * x + det) % p == 0]; assert len(eig) == 2, eig
    maps = []
    for f in out["symmetries"]:
        if not f["dualising"] or f["eps"] != -1: continue
        Mk = cov.induced(f["ab"], -1); maps.append((Mk, -1))
        for k in range(1, 5): Mk = imul(Mt, Mk); maps.append((Mk, -1))
    chars = list(itertools.product(range(p), range(p)))
    def val(c, vec): return sum(F(ci * vec[i], p) for (i, _), ci in zip(tors, c)) % 1
    fixed = set()
    for M, _ in maps:
        Mz = [M[r][z] for r in range(cov.kdim)]
        for c in chars:
            if val(c, Mz) != 0: continue
            if all((val(c, [M[r][i] for r in range(cov.kdim)]) + F(ci, p)) % 1 == 0 for (i, _), ci in zip(tors, c)): fixed.add(c)
    unfixed = [c for c in chars if c not in fixed]
    def sheet(c):
        if c == (0, 0): return None
        v = [(c[0] * Phi5[0][j] + c[1] * Phi5[1][j]) % p for j in range(2)]
        for lam in eig:
            if all((v[j] - lam * c[j]) % p == 0 for j in range(2)): return lam
        return None
    golden = dict(deck_on_T5_mod_11=Phi5, eigenvalues_mod_11=eig, unfixed=len(unfixed),
                  unfixed_single_sheet=sum(1 for c in unfixed if sheet(c) is not None), single_sheet_total=sum(1 for c in chars if sheet(c) is not None),
                  per_sheet={str(lam): sum(1 for c in unfixed if sheet(c) == lam) for lam in eig})
    out["golden_M5"] = golden
    print("M_5 golden reading: %d unfixed, %d of them single-sheet, %d single-sheet twists in all, per sheet %s" % (golden["unfixed"], golden["unfixed_single_sheet"], golden["single_sheet_total"], golden["per_sheet"]))
    want = {1: 0, 2: 0, 3: 0, 4: 0, 5: 20, 6: 96}
    ok = all(l["unfixed_off_circle"] == want[l["n"]] for l in out["levels"]) and golden["unfixed"] == golden["unfixed_single_sheet"] == golden["single_sheet_total"] == 20 and set(golden["per_sheet"].values()) == {10}
    out["agrees_with_sm_B1522"] = bool(ok)
    json.dump(out, open(HERE / "levels_count_odd.json", "w"), indent=1, default=str)
    print("VERDICT levels-count-odd: %s" % ("PASS" if ok else "FAIL")); return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
