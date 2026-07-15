"""B637 part 2b — the alternating cubic 3-form on the h1 >= 3 doubles
(prereg 99815a48).

DERIVATION (the gate): for the amalgam pi = G1 *_P G2 with cd(G_i) = 2,
H3(pi;C) ~ coker(H2(G1)+H2(G2) -> H2(P)) and the MV boundary of [D] is
the torus class; hence for the C-contracted triple-cup 3-cocycles
omega_i (trivial coefficients),
    Y(a,b,c) = S_1(z_T) - S_2(z_T'),   S_i = omega_i . H2^(i),
with z_T = [mu|lam] - [lam|mu] (side-1 section words), z_T' its image
under the peripheral identification (side-2 words), and H the
equivariant bar-vs-Fox comparison homotopy built recursively via the
bar contraction s on free generators:
    H2([g|h]) = s([g|h] - Phi2 Psi2([g|h]) - H1(d2[g|h])),
    H1([g])   = s([g] - Phi1 Psi1([g])),   H0 = 0.
Psi2([g|h]) = sum_j e_j u_j . f_r from a van Kampen certificate of the
section defect sig(g)sig(h)sig(gh)^-1 (beam search, replay-verified);
Phi2(f_r) = the corrected inverse-letter bar 2-chain (B632/audit).

VALIDATION: delta S = omega on test 3-cells (both trivial-defect and
certificate-bearing); full antisymmetry of Y; coboundary invariance in
every slot; section independence.
"""
import heapq
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = os.path.join(HERE, "..", "B575_bridge_obstruction", "l51_obstruction.py")
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time()
print("executing B575 stages 0-3...", flush=True)
exec(compile(src[:cut], B575, "exec"), ns)
print(f"prefix done in {time.time()-t0:.1f}s", flush=True)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
W27 = ns["W27"]
REL = ns["REL"]
nullspace, rref = ns["nullspace"], ns["rref"]
meye, mmul = ns["meye"], ns["mmul"]
LONG = "abABaaBAbA"
RELI = REL[::-1].swapcase()


def kconj(x): return K(x.a, -x.b)
def mconj(M): return [[kconj(x) for x in row] for row in M]
def freduce(w):
    out = []
    for ch in w:
        if out and out[-1] == ch.swapcase():
            out.pop()
        else:
            out.append(ch)
    return "".join(out)
def inv(w): return w[::-1].swapcase()


def minv(M):
    n = len(M)
    aug = [[M[i][j] for j in range(n)] + [K1 if i == j else K0
                                          for j in range(n)] for i in range(n)]
    R, piv = rref(aug)
    assert len(piv) == n
    out = [[K0] * n for _ in range(n)]
    for r_i, pc in enumerate(piv):
        for j in range(n):
            out[pc][j] = R[r_i][n + j]
    return out


def apply(M, v):
    return [sum((M[i][j] * v[j] for j in range(27) if not v[j].is_zero()), K0)
            for i in range(27)]


# ---------------- the cubic ----------------------------------------------------
support, SUPIDX = [], {}
for p in range(27):
    for q in range(p, 27):
        for r_ in range(q, 27):
            if all(W27[p][k] + W27[q][k] + W27[r_][k] == 0 for k in range(6)):
                SUPIDX[(p, q, r_)] = len(support)
                support.append((p, q, r_))
eqs = {}
for gi, X in enumerate(list(ns["E6_e"]) + list(ns["E6_f"])):
    xent = [(s, t) for s in range(27) for t in range(27)
            if not X[s][t].is_zero()]
    for (a, b, c) in support:
        k = SUPIDX[(a, b, c)]
        for (u, v, w) in ((a, b, c), (b, a, c), (c, a, b)):
            for s, t in xent:
                if s == u:
                    key = (gi,) + tuple(sorted((t, v, w)))
                    row = eqs.setdefault(key, {})
                    row[k] = row.get(k, K0) + X[u][t]
rows = [[row.get(k, K0) for k in range(len(support))] for row in eqs.values()]
solC = nullspace(rows)
assert len(solC) == 1
CFULL = {}
for (p, q, r_), k in SUPIDX.items():
    if not solC[0][k].is_zero():
        for perm in {(p, q, r_), (p, r_, q), (q, p, r_), (q, r_, p),
                     (r_, p, q), (r_, q, p)}:
            CFULL[perm] = solC[0][k]
print(f"cubic rebuilt: {len(CFULL)} ordered entries", flush=True)


def Cval(u, v, w):
    return sum((c * u[p] * v[q] * w[r_] for (p, q, r_), c in CFULL.items()
                if not (u[p].is_zero() or v[q].is_zero() or w[r_].is_zero())),
               K0)


# ---------------- certificates -------------------------------------------------
CERT_CACHE = {}


def certify(word):
    w0 = freduce(word)
    if w0 == "":
        return []
    if w0 in CERT_CACHE:
        return CERT_CACHE[w0]
    seen = {w0: (None, None, None)}
    beam = [(len(w0), w0)]
    ok = False
    for depth in range(1, 18):
        cand = {}
        for _, w in beam:
            for ins, sgn in ((REL, +1), (RELI, -1)):
                for i in range(len(w) + 1):
                    nw = freduce(w[:i] + ins + w[i:])
                    if nw not in seen and nw not in cand:
                        cand[nw] = (w, i, sgn)
        seen.update(cand)
        if "" in cand:
            ok = True
            break
        beam = heapq.nsmallest(600, ((len(nw), nw) for nw in cand))
        assert beam, f"certificate dead end: {w0}"
    assert ok, f"no certificate within depth: {w0}"
    chain = []
    node = ""
    while seen[node][0] is not None:
        parent, i, sgn = seen[node]
        chain.append((parent, i, sgn))
        node = parent
    chain.reverse()
    cert = []
    w = w0
    for (parent, i, sgn) in chain:
        assert parent == w
        cert.append((w[:i], -sgn))
        w = freduce(w[:i] + (REL if sgn > 0 else RELI) + w[i:])
    assert w == ""
    prod = ""
    for (u, e) in cert:
        prod += u + (REL if e > 0 else RELI) + inv(u)
    assert freduce(prod) == w0, "certificate replay failed"
    CERT_CACHE[w0] = cert
    return cert


# the corrected relator bar 2-chain: list of (coeff_word, slot1, slot2, sign)
def rel_chain():
    cells = []
    pre = ""
    for ch in REL:
        cells.append(("", pre, ch, +1))          # 1 * [p_{i-1} | x_i]
        if ch in 'AB':
            # correction: - p_{i-1} [l^-1 | l] (prefix BEFORE the letter;
            # the p_i transcription was THE class-level-gate bug, found by
            # the literal chain machine's formal boundary check)
            cells.append((pre, ch, ch.lower(), -1))
        pre = freduce(pre + ch)
    return cells


RELCHAIN = rel_chain()


class Side:
    """One side of the amalgam: letter matrices + the T.H evaluator."""

    def __init__(self, lets):
        self.lets = lets
        self._mc = {}

    def mat(self, w):
        w = freduce(w)
        if w not in self._mc:
            M = meye(27)
            for ch in w:
                M = mmul(M, self.lets[ch])
            self._mc[w] = M
        return self._mc[w]

    def zval(self, z, w):
        val = [K0] * 27
        P = meye(27)
        for ch in freduce(w):
            if ch == 'a':
                add = apply(P, z[0])
            elif ch == 'b':
                add = apply(P, z[1])
            elif ch == 'A':
                add = [K0 - x for x in apply(mmul(P, self.lets['A']), z[0])]
            else:
                add = [K0 - x for x in apply(mmul(P, self.lets['B']), z[1])]
            val = [val[t] + add[t] for t in range(27)]
            P = mmul(P, self.lets[ch])
        return val

    def make_omega(self, za, zb, zc):
        cache = {}
        def om(x, y, z):
            x, y, z = freduce(x), freduce(y), freduce(z)
            if not x or not y or not z:
                return K0                     # identity slot: cocycle val 0
            key = (x, y, z)
            if key not in cache:
                vx = self.zval(za, x)
                vy = apply(self.mat(x), self.zval(zb, y))
                vz = apply(self.mat(x + y), self.zval(zc, z))
                cache[key] = Cval(vx, vy, vz)
            return cache[key]
        return om

    @staticmethod
    def fox_positions(w):
        """free Fox terms of the word w: list of (prefix_word, letter, sign)."""
        out = []
        for i, ch in enumerate(w):
            pre = w[:i]
            if ch.islower():
                out.append((pre, ch, +1))
            else:
                out.append((freduce(pre + ch), ch.lower(), -1))
        return out

    def S_eval(self, om, g, h, gh):
        """S([g|h]) = om(H2([g|h])) with section words g, h, gh.
        Full formula; identity-slot terms vanish inside om."""
        total = K0
        # s([g|h]) -> [1|g|h] : om("",g,h) = 0 automatically; keep for form
        total = total + om("", g, h)
        # - s(Phi2 Psi2): certificate of the defect
        for (u, e) in certify(g + h + inv(gh)):
            for (cw, s1, s2, sgn) in RELCHAIN:
                coeff = e * sgn
                cell1 = freduce(u + cw)          # combined coefficient word
                val = om(cell1, s1, s2)
                if coeff > 0:
                    total = total - val
                else:
                    total = total + val
        # - s(H1(d2[g|h])) = - s( g H1[h] - H1[gh] + H1[g] )
        # H1([w]) = [1|w] - sum_(fox pos) sign * [pre|letter]
        def s_of_H1(coeffword, w, outer_sign):
            nonlocal total
            # s(coeff * [1|w]) = [coeff|1|w] -> om(coeff,"",w) = 0
            t1 = om(coeffword, "", w)
            total = total - K(outer_sign) * t1 if False else total
            # (identity-slot: zero; skipped consistently)
            for (pre, ch, sgn) in self.fox_positions(w):
                val = om(coeffword, pre, ch)
                # contribution: - outer_sign * ( - sgn * val )
                contrib_pos = (outer_sign * (-sgn)) < 0
                if contrib_pos:
                    total = total + val
                else:
                    total = total - val
        # term g*H1([h]) with outer sign +1 (then overall minus applied inside)
        s_of_H1(g, h, +1)
        s_of_H1("", gh, -1)
        s_of_H1("", g, +1)
        return total


# ---------------- delta S = omega validation ----------------------------------
def validate_side(side, za, zb, zc, label):
    om = side.make_omega(za, zb, zc)
    S = lambda g, h, gh: side.S_eval(om, g, h, gh)
    tests = [("a", "b", "ab", "aa"), ("b", "A", "bA", "ba"),
             ("ab", "AB", "abAB", "a")]
    allok = True
    for (g, h, k, _pad) in tests:
        gh, hk, ghk = (freduce(g + h), freduce(h + k), freduce(g + h + k))
        lhs = (S(h, k, hk) - S(gh, k, ghk) + S(g, hk, ghk) - S(g, h, gh))
        rhs = om(g, h, k)
        ok = (lhs - rhs).is_zero()
        allok = allok and ok
        print(f"    deltaS=omega on [{g}|{h}|{k}]: {ok}", flush=True)
    # a certificate-bearing test: sections with nontrivial defect
    g, h = LONG, "a"
    gh = freduce("a" + LONG)                 # sig(lam mu) := a LONG (defect!)
    k = "b"
    ghk = freduce(gh + k)
    hk = freduce(h + k)
    lhs = (S(h, k, hk) - S(gh, k, ghk) + S(g, hk, ghk) - S(g, h, gh))
    rhs = om(g, h, k)
    ok = (lhs - rhs).is_zero()
    allok = allok and ok
    print(f"    deltaS=omega on [lam|mu|b] (certificate path): {ok}",
          flush=True)
    assert allok, f"VALIDATION FAILED on side {label}"


# ---------------- assemble the weld double ------------------------------------
def lift_sl2(g):
    e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
    mexp_nil, mscale = ns["mexp_nil"], ns["mscale"]
    p, q, r_, s = g[0][0], g[0][1], g[1][0], g[1][1]
    det = p * s - q * r_
    if p.is_zero():
        w27 = mmul(mmul(mexp_nil(e_pr), mexp_nil(mscale(K(-1), f_pr))),
                   mexp_nil(e_pr))
        return mmul(w27, lift_sl2([[K0 - r_, K0 - s], [p, q]]))
    lower = mexp_nil(mscale(r_ * p.inv(), f_pr))
    upper = mexp_nil(mscale(q * p.inv(), e_pr))
    t2 = (p * p) * det.inv()
    D = meye(27)
    for i in range(27):
        wgt = int(ns["h_pr"][i][i].a)
        e = wgt // 2
        val = K1
        base = t2 if e >= 0 else t2.inv()
        for _ in range(abs(e)):
            val = val * base
        D[i][i] = val
    return mmul(mmul(lower, D), upper)


from fractions import Fraction as Fr
Ag = [[K1, K1], [K0, K1]]
Bg = [[K1, K0], [ns["OMEGA"], K1]]
lam2 = None
lets2 = {'a': Ag, 'b': Bg,
         'A': [[K1, K(-1)], [K0, K1]],
         'B': [[K1, K0], [K0 - ns["OMEGA"], K1]]}
def wmat2(w):
    M = [[K1, K0], [K0, K1]]
    def mm(A, B):
        return [[sum((A[i][t] * B[t][j] for t in range(2)), K0)
                 for j in range(2)] for i in range(2)]
    for ch in w:
        M = mm(M, lets2[ch])
    return M
lam2 = wmat2(LONG)
lam2i = [[lam2[1][1], K0 - lam2[0][1]], [K0 - lam2[1][0], lam2[0][0]]]
lam2c = [[kconj(x) for x in row] for row in wmat2(LONG)]
Agc = [[kconj(x) for x in row] for row in Ag]
rows_u = []
for (X, Y_) in ((Agc, Ag), (lam2c, lam2i)):
    for i in range(2):
        for j in range(2):
            row = [K0] * 4
            for kk in range(2):
                row[i * 2 + kk] = row[i * 2 + kk] + X[kk][j]
                row[kk * 2 + j] = row[kk * 2 + j] - Y_[i][kk]
            rows_u.append(row)
solu = nullspace(rows_u)
u = None
for s_ in solu:
    cand = [[s_[0], s_[1]], [s_[2], s_[3]]]
    det = cand[0][0] * cand[1][1] - cand[0][1] * cand[1][0]
    if not det.is_zero():
        u = cand
        break
U27 = lift_sl2(u)
U27i = minv(U27)
lets1 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
side2lets = {ch: mmul(mmul(U27, mconj(lets1[ch])), U27i) for ch in "abAB"}
print("weld side-2 letters built", flush=True)

side1 = Side(lets1)


def double_Y(bend_m, verbose=True):
    """the 10 components of Y on the h1=5 double D_bent(M; m)."""
    if bend_m is None:
        s2 = dict(side2lets)
        tag = "none"
    else:
        c = ns["mexp_nil"](ns["BLOCKS"][bend_m][0])
        ci = minv(c)
        s2 = {ch: mmul(mmul(c, side2lets[ch]), ci) for ch in "abAB"}
        tag = f"m={bend_m}"
    side2 = Side(s2)
    # amalgam cocycles: 5 classes from the part-1 kernel
    lets4 = {'a': lets1['a'], 'b': lets1['b'], 'A': lets1['A'],
             'B': lets1['B'], 'c': s2['a'], 'd': s2['b'],
             'C': s2['A'], 'D': s2['B']}
    prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
            'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
    relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
                "aC", LONG + inv(LONG.translate(str.maketrans("abAB", "cdCD")))]
    # NOTE relation 4: lam(a,b) * lam'(c,d)^{-1}... the weld identification is
    # lam' = lam^{-1}; relator = LONG(a,b) + LONG(c,d): keep part-1 convention
    relators[3] = LONG + LONG.translate(str.maketrans("abAB", "cdCD"))
    rows_all = []
    for w in relators:
        L = {g: [[K0] * 27 for _ in range(27)] for g in "abcd"}
        Pi = meye(27)
        for ch in w:
            g = prim[ch]
            if ch.islower():
                term = Pi
                sgn = 1
            else:
                term = mmul(Pi, lets4[ch])
                sgn = -1
            if sgn < 0:
                term = ns["mscale"](K(-1), term)
            L[g] = ns["madd"](L[g], term)
            Pi = mmul(Pi, lets4[ch])
        assert ns["mzero_p"](ns["msub"](Pi, meye(27)))
        for i in range(27):
            rows_all.append([L[g][i][j] for g in "abcd" for j in range(27)])
    Zc = nullspace(rows_all)
    # coboundary space
    cob = []
    for j in range(27):
        v = [K1 if t == j else K0 for t in range(27)]
        entry = []
        for g in "abcd":
            gv = apply(lets4[g], v)
            entry.extend([gv[i] - v[i] for i in range(27)])
        cob.append(entry)
    # pick 5 kernel vectors independent mod coboundaries
    Solver = ns["Solver"]
    reps = []
    basis = [r[:] for r in cob]
    for z in Zc:
        try:
            Solver(basis).coords(z)
        except ValueError:
            reps.append(z)
            basis.append(z)
            if len(reps) == 5:
                break
    assert len(reps) == 5, f"only {len(reps)} independent classes"
    # split each amalgam cocycle into side data
    def sides_of(z):
        za1 = (z[0:27], z[27:54])            # side 1: letters a,b
        za2 = (z[54:81], z[81:108])          # side 2: letters c,d
        return za1, za2
    # peripheral sections: side 1: mu = a, lam = LONG, sig(mulam) = a+LONG
    # side 2 (weld): mu2 = a(c-letters) -> word "a"; lam2 = LONG^{-1} in c,d
    # as side-2 group words over its own letters {a,b}: mu2 = "a",
    # lam2w = inv(LONG); sig(mu2 lam2) := "a" + inv(LONG)
    out = {}
    import itertools as it
    for (i, j, k) in it.combinations(range(5), 3):
        zi, zj, zk = reps[i], reps[j], reps[k]
        (zi1, zi2), (zj1, zj2), (zk1, zk2) = map(sides_of, (zi, zj, zk))
        om1 = side1.make_omega(zi1, zj1, zk1)
        om2 = side2.make_omega(zi2, zj2, zk2)
        S1 = lambda g, h, gh: side1.S_eval(om1, g, h, gh)
        S2 = lambda g, h, gh: side2.S_eval(om2, g, h, gh)
        MU1, LAM1, PROD1 = "a", LONG, freduce("a" + LONG)
        MU2, LAM2 = "a", inv(LONG)
        PROD2 = freduce("a" + inv(LONG))
        y = (S1(MU1, LAM1, PROD1) - S1(LAM1, MU1, PROD1)) \
            - (S2(MU2, LAM2, PROD2) - S2(LAM2, MU2, PROD2))
        out[(i, j, k)] = y
        if verbose:
            print(f"    Y[{i}{j}{k}] ({tag}) = "
                  f"{'0' if y.is_zero() else str(y)}", flush=True)
    return out, reps, sides_of, side2


if __name__ == "__main__":
    # validation on side 1 with a genuine cocycle triple from the unbent double
    print("\n(validation)", flush=True)
    outN, repsN, sides_ofN, side2N = None, None, None, None
    # build unbent double classes first (cheap reuse)
    outN, repsN, sides_ofN, side2N = (None, None, None, None)
    # -- validate using the m=None double's first three classes
    Yn, reps, sides_of, s2obj = double_Y(None, verbose=False)
    z1s, _ = sides_of(reps[0])
    z2s, _ = sides_of(reps[1])
    z3s, _ = sides_of(reps[2])
    validate_side(side1, z1s, z2s, z3s, "1 (weld none)")
    print("\n(the 3-form, unbent weld double)", flush=True)
    for key in sorted(Yn):
        y = Yn[key]
        print(f"  Y[{key}] = {'0' if y.is_zero() else str(y)}", flush=True)
    nz = sum(1 for y in Yn.values() if not y.is_zero())
    print(f"\nnonzero components (none): {nz}/10", flush=True)
    print("B637 part 2b stage-1 DONE", flush=True)
