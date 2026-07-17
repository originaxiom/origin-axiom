"""B666 CELL A' (cellA2) — shared apparatus: the uncomputed cups on the
golden double D.

Loads the banked b637 apparatus (exec pattern, with the stage-3 certify
peeling patch, VERBATIM cellH), rebuilds the banked 5-class basis
(double_Y construction, bend None), and provides the coefficient-module
toolkit for the three new cups:

  * Lambda^2(27) = 351  : values = antisymmetric 27x27 matrices,
                          action  g.A = M_g A M_g^T          (351 coords)
  * Sym^2(27) = 27bar + 351' : values = symmetric 27x27 matrices,
                          action  g.S = M_g S M_g^T          (378 coords)
    (the 27bar summand U is cut out by the split Casimir; 351' component
     = P_W-projection along U onto W = ker(pi), pi = the polarized cubic)
  * 78 (adjoint)        : values = e6 coordinate vectors (E6_BASIS),
                          action  g.X = Ad(M_g) X            (78 coords)

Class-membership convention (banked, cellH): a 2-cocycle c with
coefficients M is a coboundary in H^2(pi;M) iff its evaluation E(c) on
the corrected relator bar 2-chains lies in the image of the Fox map
C^1(gens;M) -> C^2(rels;M).  Zero floats anywhere; exact K = Q(sqrt-3).
"""
import os
import time
import json
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B637DIR = os.path.normpath(os.path.join(HERE, "..", "..",
                                        "B637_corrected_cell3"))
T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


class NS:
    pass


# ---------------------------------------------------------------- K serialization
def kser(x):
    return [str(x.a), str(x.b)]


def vser(v):
    return [kser(x) for x in v]


def mser(M):
    return [vser(r) for r in M]


def make_kde(K):
    def kde(t):
        return K(Fr(t[0]), Fr(t[1]))
    return kde


# ---------------------------------------------------------------- loader
def load(run_g0=True, need_bar=True):
    """exec the banked apparatus; rebuild the banked 5-class basis;
    optional decisive G0 banked-Y control; 27bar basis for the 78-cup."""
    n = NS()
    log("LOAD: exec b637_threeform.py (banked apparatus)...")
    mod = {"__name__": "b637_module",
           "__file__": os.path.join(B637DIR, "b637_threeform.py")}
    exec(compile(open(os.path.join(B637DIR, "b637_threeform.py")).read(),
                 "b637_threeform.py", "exec"), mod)
    log("b637 module loaded")

    n.K, n.K0, n.K1 = mod["K"], mod["K0"], mod["K1"]
    n.kde = make_kde(n.K)
    n.freduce, n.inv = mod["freduce"], mod["inv"]
    n.LONG, n.REL = mod["LONG"], mod["REL"]
    n.apply = mod["apply"]
    n.nullspace, n.rref = mod["nullspace"], mod["rref"]
    n.meye, n.mmul, n.minv = mod["meye"], mod["mmul"], mod["minv"]
    b575 = mod["ns"]
    n.b575 = b575
    n.madd, n.msub, n.mscale, n.mzero_p = (b575["madd"], b575["msub"],
                                           b575["mscale"], b575["mzero_p"])
    n.Solver = b575["Solver"]
    n.flat = b575["flat"]
    n.E6_BASIS, n.E6_SOLVER = b575["E6_BASIS"], b575["E6_SOLVER"]
    n.CFULL = mod["CFULL"]
    n.lets1 = mod["lets1"]
    n.side2lets = mod["side2lets"]
    n.side1 = mod["side1"]
    n.Side = mod["Side"]
    n.mod = mod
    K, K0, K1 = n.K, n.K0, n.K1

    def applyg(M, v):
        """dimension-generic matrix-vector product (b637 apply is 27-only)."""
        nv = len(v)
        out = []
        for row in M:
            s = K0
            for j in range(nv):
                x = v[j]
                if not x.is_zero():
                    y = row[j]
                    if not y.is_zero():
                        s = s + y * x
            out.append(s)
        return out

    n.applyg = applyg
    freduce, inv = n.freduce, n.inv
    apply_ = n.apply

    # stage-3 certify peeling patch (verbatim b637_stage3 / cellH)
    _base_certify = mod["certify"]

    def certify_peeled(word):
        w = freduce(word)
        if w == "":
            return []
        if len(w) >= 2 and w[0] == w[-1].swapcase():
            inner = certify_peeled(w[1:-1])
            return [(freduce(w[0] + u), e) for (u, e) in inner]
        return _base_certify(w)

    mod["certify"] = certify_peeled
    assert mod["certify"] is certify_peeled

    # ------------------------------------------------ banked 5-class basis
    log("LOAD: rebuild the banked 5-class basis (double_Y, bend None)...")
    s2 = dict(n.side2lets)
    lets4 = {'a': n.lets1['a'], 'b': n.lets1['b'], 'A': n.lets1['A'],
             'B': n.lets1['B'], 'c': s2['a'], 'd': s2['b'],
             'C': s2['A'], 'D': s2['B']}
    n.lets4 = lets4
    prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
            'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
    n.prim = prim
    RELATORS = [n.REL, n.REL.translate(str.maketrans("abAB", "cdCD")),
                "aC", n.LONG + n.LONG.translate(str.maketrans("abAB", "cdCD"))]
    n.RELATORS = RELATORS
    rows_all = []
    for w in RELATORS:
        L = {g: [[K0] * 27 for _ in range(27)] for g in "abcd"}
        Pi = n.meye(27)
        for ch in w:
            g = prim[ch]
            if ch.islower():
                term = Pi
                sgn = 1
            else:
                term = n.mmul(Pi, lets4[ch])
                sgn = -1
            if sgn < 0:
                term = n.mscale(K(-1), term)
            L[g] = n.madd(L[g], term)
            Pi = n.mmul(Pi, lets4[ch])
        assert n.mzero_p(n.msub(Pi, n.meye(27))), "relator != identity"
        for i in range(27):
            rows_all.append([L[g][i][j] for g in "abcd" for j in range(27)])
    Zc = n.nullspace(rows_all)
    log(f"  Z^1(D;27) dim = {len(Zc)} (banked: 31)")
    assert len(Zc) == 31
    cob = []
    for j in range(27):
        v = [K1 if t == j else K0 for t in range(27)]
        entry = []
        for g in "abcd":
            gv = apply_(lets4[g], v)
            entry.extend([gv[i] - v[i] for i in range(27)])
        cob.append(entry)
    n.cob = cob
    reps = []
    basis = [r[:] for r in cob]
    for z in Zc:
        try:
            n.Solver(basis).coords(z)
        except ValueError:
            reps.append(z)
            basis.append(z)
            if len(reps) == 5:
                break
    assert len(reps) == 5, f"only {len(reps)} independent classes"
    n.reps = reps
    log("  5 class representatives rebuilt (greedy, banked order)")

    def sides_of(z):
        return (z[0:27], z[27:54]), (z[54:81], z[81:108])

    # ------------------------------------------------ G0 banked-Y control
    if run_g0:
        log("CONTROL G0 (decisive): recompute two banked Y components...")
        side2 = n.Side(dict(n.side2lets))
        MU1, LAM1, PROD1 = "a", n.LONG, freduce("a" + n.LONG)
        MU2, LAM2 = "a", inv(n.LONG)
        PROD2 = freduce("a" + inv(n.LONG))
        BANKED = {(0, 3, 4): K(0, Fr(2, 3)),
                  (1, 3, 4): K(Fr(1, 24), Fr(1, 72))}
        for (i, j, k), want in BANKED.items():
            (zi1, zi2), (zj1, zj2), (zk1, zk2) = map(
                sides_of, (reps[i], reps[j], reps[k]))
            om1 = n.side1.make_omega(zi1, zj1, zk1)
            om2 = side2.make_omega(zi2, zj2, zk2)
            y = ((n.side1.S_eval(om1, MU1, LAM1, PROD1)
                  - n.side1.S_eval(om1, LAM1, MU1, PROD1))
                 - (side2.S_eval(om2, MU2, LAM2, PROD2)
                    - side2.S_eval(om2, LAM2, MU2, PROD2)))
            ok = (y - want).is_zero()
            log(f"  Y[{(i,j,k)}] = {y}  banked = {want}  MATCH: {ok}")
            assert ok, "BASIS MATCH CONTROL G0 FAILED"
        log("  G0 PASS: the rebuilt basis IS the banked basis")

    # ------------------------------------------------ actions + caches
    def transpose(M):
        return [list(r) for r in zip(*M)]

    n.transpose = transpose
    DACT = {ch: transpose(lets4[ch.swapcase()]) for ch in lets4}
    n.DACT = DACT
    for x in "abcd":
        assert n.mzero_p(n.msub(n.mmul(lets4[x], lets4[x.upper()]),
                                n.meye(27)))
        assert n.mzero_p(n.msub(n.mmul(DACT[x], DACT[x.upper()]),
                                n.meye(27)))

    MATC, DMATC = {"": n.meye(27)}, {"": n.meye(27)}

    def mat(w):
        w = freduce(w)
        if w not in MATC:
            MATC[w] = n.mmul(mat(w[:-1]), lets4[w[-1]])
        return MATC[w]

    def dmat(w):
        w = freduce(w)
        if w not in DMATC:
            DMATC[w] = n.mmul(dmat(w[:-1]), DACT[w[-1]])
        return DMATC[w]

    n.mat, n.dmat = mat, dmat
    for w in RELATORS:
        assert n.mzero_p(n.msub(dmat(w), n.meye(27))), "rhobar relator gate"

    # ------------------------------------------------ relator 2-chains
    def relchain(word):
        cells = []
        pre = ""
        for ch in word:
            cells.append(("", pre, ch, +1))
            if ch.isupper():
                cells.append((pre, ch, ch.lower(), -1))
            pre = freduce(pre + ch)
        return cells

    n.RELCELLS = [relchain(w) for w in RELATORS]

    # Fox position lists: POSLIST[r][g] = [(word, sign)] with
    # lowercase occurrence at prefix pre -> (pre, +1);
    # uppercase ch at prefix pre -> (freduce(pre+ch), -1).
    POSLIST = []
    for w in RELATORS:
        P = {g: [] for g in "abcd"}
        pre = ""
        for ch in w:
            g = prim[ch]
            if ch.islower():
                P[g].append((pre, +1))
            else:
                P[g].append((freduce(pre + ch), -1))
            pre = freduce(pre + ch)
        POSLIST.append(P)
    n.POSLIST = POSLIST

    # ------------------------------------------------ cocycle evaluators
    def z4_of(z):
        return {g: z[gi * 27:(gi + 1) * 27] for gi, g in enumerate("abcd")}

    n.z4_of = z4_of
    n.UREP = [z4_of(z) for z in reps]

    def make_cocycle_eval(z4, matget):
        cache = {"": [K0] * 27}

        def ev(w):
            w = freduce(w)
            if w in cache:
                return cache[w]
            w1, letr = w[:-1], w[-1]
            base = ev(w1)
            if letr.islower():
                add = apply_(matget(w1), z4[letr])
                val = [base[t] + add[t] for t in range(27)]
            else:
                add = apply_(matget(w), z4[letr.lower()])
                val = [base[t] - add[t] for t in range(27)]
            cache[w] = val
            return val
        return ev

    n.make_cocycle_eval = make_cocycle_eval
    n.UEV = [make_cocycle_eval(n.UREP[i], mat) for i in range(5)]

    # 27bar classes (for the 78-cup slots), greedy per cellH
    if need_bar:
        LBAR = []
        for w in RELATORS:
            L = {g: [[K0] * 27 for _ in range(27)] for g in "abcd"}
            pre = ""
            for ch in w:
                g = prim[ch]
                if ch.islower():
                    L[g] = n.madd(L[g], dmat(pre))
                else:
                    L[g] = n.msub(L[g], dmat(freduce(pre + ch)))
                pre = freduce(pre + ch)
            LBAR.append(L)
        n.LBAR = LBAR
        rows_bar = []
        for L in LBAR:
            for i in range(27):
                rows_bar.append([L[g][i][j] for g in "abcd"
                                 for j in range(27)])
        Zbar = n.nullspace(rows_bar)
        cob_bar = []
        for j in range(27):
            v = [K1 if t == j else K0 for t in range(27)]
            entry = []
            for g in "abcd":
                gv = apply_(DACT[g], v)
                entry.extend([gv[i] - v[i] for i in range(27)])
            cob_bar.append(entry)
        reps_bar = []
        basis_b = [r[:] for r in cob_bar]
        for z in Zbar:
            try:
                n.Solver(basis_b).coords(z)
            except ValueError:
                reps_bar.append(z)
                basis_b.append(z)
                if len(reps_bar) == 5:
                    break
        assert len(reps_bar) == 5
        n.reps_bar = reps_bar
        log(f"  Z^1(D;27bar) dim = {len(Zbar)}; 5 27bar classes (greedy)")
        n.ZBEV = [make_cocycle_eval(z4_of(z), dmat) for z in reps_bar]

    # ------------------------------------------------ trivial-coefficient phi
    PHITRIV = []
    for w in RELATORS:
        row = {g: 0 for g in "abcd"}
        for ch in w:
            row[prim[ch]] += 1 if ch.islower() else -1
        PHITRIV.append([K(row[g]) for g in "abcd"])
    n.PHITRIV = PHITRIV
    nsol = n.nullspace([[PHITRIV[r][gi] for r in range(4)]
                        for gi in range(4)])
    assert len(nsol) == 1, f"coker H^2(Y;C) dim = {len(nsol)} != 1"
    nvec = nsol[0]
    for t in range(4):
        if not nvec[t].is_zero():
            nvec = [x * nvec[t].inv() for x in nvec]
            break
    n.nvec = nvec
    log(f"  phi (left-null of PHITRIV, normalized) = "
        f"{[str(x) for x in nvec]}")

    def phi(e4):
        s = K0
        for t in range(4):
            if not nvec[t].is_zero():
                s = s + nvec[t] * e4[t]
        return s

    n.phi = phi

    # deterministic exact "random" vectors (cellH rvec)
    def rvec(seed):
        st = seed
        out = []
        for t in range(27):
            st = (st * 1103515245 + 12345) % (1 << 31)
            out.append(K(Fr((st % 7) - 3), Fr(((st >> 8) % 5) - 2)))
        return out

    n.rvec = rvec

    # ------------------------------------------------ pair index arrays
    n.LT = [(p, q) for p in range(27) for q in range(p + 1, 27)]     # 351
    n.LE = [(p, q) for p in range(27) for q in range(p, 27)]         # 378
    n.LTIDX = {pq: m for m, pq in enumerate(n.LT)}
    n.LEIDX = {pq: m for m, pq in enumerate(n.LE)}

    # coords <-> matrix
    def coofLam(M):
        return [M[p][q] for (p, q) in n.LT]

    def matofLam(co):
        M = [[K0] * 27 for _ in range(27)]
        for m, (p, q) in enumerate(n.LT):
            M[p][q] = co[m]
            M[q][p] = K0 - co[m]
        return M

    def coofSym(M):
        return [M[p][q] for (p, q) in n.LE]

    def matofSym(co):
        M = [[K0] * 27 for _ in range(27)]
        for m, (p, q) in enumerate(n.LE):
            M[p][q] = co[m]
            M[q][p] = co[m]
        return M

    n.coofLam, n.matofLam = coofLam, matofLam
    n.coofSym, n.matofSym = coofSym, matofSym

    def wedgeco(x, y):
        return [x[p] * y[q] - x[q] * y[p] for (p, q) in n.LT]

    def symco(x, y):
        out = []
        for (p, q) in n.LE:
            if p == q:
                out.append(x[p] * y[p] + x[p] * y[p])
            else:
                out.append(x[p] * y[q] + x[q] * y[p])
        return out

    n.wedgeco, n.symco = wedgeco, symco

    def conjT(M, S):
        """M S M^T for 27x27."""
        return n.mmul(n.mmul(M, S), transpose(M))

    n.conjT = conjT

    # pi: Sym^2 V -> 27bar via the polarized cubic:
    # pi(S)_r = sum_{p,q ordered} C_pqr S[p][q]  ( = 2 cross on pure x.y )
    PIR = [[] for _ in range(27)]
    for (p, q, r_), cval in n.CFULL.items():
        PIR[r_].append((p, q, cval))
    n.PIR = PIR

    def piSym(S):
        out = []
        for r_ in range(27):
            s = K0
            for (p, q, cv) in PIR[r_]:
                spq = S[p][q]
                if not spq.is_zero():
                    s = s + cv * spq
            out.append(s)
        return out

    n.piSym = piSym

    # exact Fox column builder for the matrix modules
    def fox_column(kind, g, m):
        """Exact Fox-map column for generator g and basis index m of the
        module ('lam' -> 351 coords, 'sym' -> 378 coords); returns the
        stacked 4-relator-block column."""
        if kind == "lam":
            (p, q) = n.LT[m]
            npair, coords_of = 351, None
        else:
            (p, q) = n.LE[m]
            npair = 378
        col = []
        for r in range(4):
            acc = [K0] * npair
            for (w, sgn) in POSLIST[r][g]:
                Mw = mat(w)
                cp = [Mw[a][p] for a in range(27)]
                cq = [Mw[a][q] for a in range(27)]
                if kind == "lam":
                    term = wedgeco(cp, cq)
                else:
                    if p == q:
                        term = [cp[a] * cp[b] for (a, b) in n.LE]
                    else:
                        term = symco(cp, cq)
                if sgn > 0:
                    acc = [acc[t] + term[t] for t in range(npair)]
                else:
                    acc = [acc[t] - term[t] for t in range(npair)]
            col.extend(acc)
        return col

    n.fox_column = fox_column
    log("LOAD complete")
    return n
