"""B637 part 1 — the dimension table by the amalgam-Fox route (prereg
99815a48..., sealed before this ran; the third method-disjoint pipeline).

The double D = M cup_T Mbar with the B582/B598 weld (mu fixed, lambda
inverted), side 2 = the conjugate representation, glued by an exact
peripheral intertwiner solved at the SL(2) level and lifted through the
principal embedding; bends c_m = exp(v_m) (banked dial slots, peripheral
by step7). Presentation: <a,b,c,d | r(a,b), r(c,d), a c^-1,
lambda(a,b) lambda(c,d)>. Fox calculus, exact over Q(omega).

Controls first (the standing rule): trivial coefficients must give
b1(D) = 1 (the audit's 'ordinary H1 = Z'). Registered predictions:
h1(D;27) = 2 at m = 4, 8; 5 at none/1/5/7/11.
"""
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
OMEGA = ns["OMEGA"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
e_pr, f_pr = ns["e_pr"], ns["f_pr"]
BLOCKS = ns["BLOCKS"]
REL = ns["REL"]
nullspace = ns["nullspace"]
meye, mmul, madd, mscale, msub, mzero_p = (ns[k] for k in
    ("meye", "mmul", "madd", "mscale", "msub", "mzero_p"))
mexp_nil = ns["mexp_nil"]

LONG = "abABaaBAbA"                        # the certified longitude (B598)


def kconj(x):
    return K(x.a, -x.b)                    # sqrt(-3) -> -sqrt(-3)


def mconj(M):
    return [[kconj(x) for x in row] for row in M]


def minv(M):
    """exact inverse via rref of [M | I]."""
    n = len(M)
    aug = [[M[i][j] for j in range(n)] + [K1 if i == j else K0
                                          for j in range(n)] for i in range(n)]
    R, piv = ns["rref"](aug)
    assert len(piv) == n, "singular matrix"
    out = [[K0] * n for _ in range(n)]
    for r_i, pc in enumerate(piv):
        assert pc == r_i
        for j in range(n):
            out[pc][j] = R[r_i][n + j]
    return out


def word_mat(word, lets):
    M = meye(len(lets['a']))
    for ch in word:
        M = mmul(M, lets[ch])
    return M


# ---------------- the SL(2) level: the weld intertwiner ----------------------
Ag = [[K1, K1], [K0, K1]]
Bg = [[K1, K0], [OMEGA, K1]]
Agi = [[K1, K(-1)], [K0, K1]]
Bgi = [[K1, K0], [K0 - OMEGA, K1]]
lets2 = {'a': Ag, 'b': Bg, 'A': Agi, 'B': Bgi}
rel2 = word_mat(REL, lets2)
assert mzero_p(msub(rel2, meye(2))), "SL2 relator fails"
lam2 = word_mat(LONG, lets2)
lam2i = minv(lam2)

Ag_c, Bg_c = mconj(Ag), mconj(Bg)
lets2c = {'a': Ag_c, 'b': Bg_c, 'A': mconj(Agi), 'B': mconj(Bgi)}
lam2c = word_mat(LONG, lets2c)

# solve u: u*conj(mu)*u^-1 = mu  and  u*conj(lam)*u^-1 = lam^-1
# linear system: u*conj(mu) - mu*u = 0 ; u*conj(lam) - lam^-1*u = 0
rows = []
for (X, Y) in ((Ag_c, Ag), (lam2c, lam2i)):
    # u X - Y u = 0, u as 4-vector (row-major 2x2)
    for i in range(2):
        for j in range(2):
            row = [K0] * 4
            for k in range(2):
                row[i * 2 + k] = row[i * 2 + k] + X[k][j]
                row[k * 2 + j] = row[k * 2 + j] - Y[i][k]
            rows.append(row)
sols = nullspace(rows)
print(f"\nweld intertwiner space (SL2): dim = {len(sols)}", flush=True)
u = None
for s in sols:
    cand = [[s[0], s[1]], [s[2], s[3]]]
    det = cand[0][0] * cand[1][1] - cand[0][1] * cand[1][0]
    if not det.is_zero():
        u = cand
        udet = det
        break
assert u is not None, "GATE FAIL: no invertible weld intertwiner"
print(f"  invertible u found; det = {udet}", flush=True)

# ---------------- lift u to GL(27) through the principal embedding -----------
# u = [[p,q],[r,s]]: Bruhat: if p != 0: u = [[1,0],[r/p,1]] [[p,0],[0,det/p]]
# [[1,q/p],[0,1]]; diagonal diag(t,1/t)*scalar: lift via exp(x h_pr)? h_pr
# exponential is not nilpotent — use the torus action: diag(t, t^-1) acts on
# the weight-w vector of Sym^k by t^w; our 27-basis (weight basis of h_pr)
# diagonalizes it: lift = diag(t^{w_i}) with w_i = h_pr eigenvalue. Scalars
# cancel in conjugation, so lift u/sqrt(det) projectively: use t^2 = p^2/det
# trick — implement via known eigenvalues (h_pr is diagonal in this basis?).
def lift_sl2(g):
    p, q, r, s = g[0][0], g[0][1], g[1][0], g[1][1]
    det = p * s - q * r
    assert not p.is_zero(), "Bruhat corner case not implemented"
    lower = mexp_nil(mscale(r * p.inv(), f_pr))
    upper = mexp_nil(mscale(q * p.inv(), e_pr))
    # diagonal part diag(p, det/p) = scalar sqrt(det) * diag(t, 1/t),
    # t^2 = p^2/det. Conjugation kills the scalar; need diag action with
    # t^2 known: on an h_pr-eigenvector of weight w, diag(t,1/t) acts by t^w;
    # w is EVEN on the 27 (weights of Sym^16+Sym^8+Sym^0 are even) => t^w =
    # (t^2)^(w/2) well-defined from t^2. Build via h_pr eigen-decomposition.
    t2 = (p * p) * det.inv()
    # h_pr diagonal? verify: off-diagonal entries zero
    h = ns["h_pr"]
    diag_ok = all(h[i][j].is_zero() for i in range(27) for j in range(27)
                  if i != j)
    assert diag_ok, "h_pr not diagonal in this basis"
    D = meye(27)
    for i in range(27):
        w = h[i][i]
        assert w.b == 0 and w.a.denominator == 1
        wi = int(w.a)
        assert wi % 2 == 0, f"odd weight {wi} on the 27?!"
        e = wi // 2
        val = K1
        base = t2 if e >= 0 else t2.inv()
        for _ in range(abs(e)):
            val = val * base
        D[i][i] = val
    return mmul(mmul(lower, D), upper)


U27 = lift_sl2(u)
U27i = minv(U27)

# gate: the lifted weld equations in GL(27)
A27c, B27c = mconj(A27), mconj(B27)
lets27c = {'a': A27c, 'b': B27c, 'A': mconj(A27i), 'B': mconj(B27i)}
side2 = {ch: mmul(mmul(U27, lets27c[ch]), U27i) for ch in "abAB"}
lam27 = word_mat(LONG, {'a': A27, 'b': B27, 'A': A27i, 'B': B27i})
lam27_2 = word_mat(LONG, side2)
g1 = mzero_p(msub(side2['a'], A27))
g2 = mzero_p(msub(mmul(lam27, lam27_2), meye(27)))
print(f"  27-level peripheral gates: mu-match {g1}, lambda-inversion {g2}",
      flush=True)
assert g1 and g2, "GATE FAIL: lifted weld equations do not hold"

# ---------------- the 4-generator Fox pipeline --------------------------------
def fox_h1(lets4, dim):
    """lets4: dict a,b,c,d (+ inverses A,B,C,D) -> dim x dim matrices.
    relators: REL(a,b), REL(c,d), a C, LONG(a,b)+LONG(c,d)."""
    prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
            'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
    relators = [REL,
                REL.translate(str.maketrans("abAB", "cdCD")),
                "aC",
                LONG + LONG.translate(str.maketrans("abAB", "cdCD"))]
    gens = "abcd"
    Z = [[K0] * dim for _ in range(dim)]
    rows_all = []
    for w in relators:
        L = {g: [[K0] * dim for _ in range(dim)] for g in gens}
        Pi = meye(dim)
        for ch in w:
            g = prim[ch]
            if ch.islower():
                term = Pi
                sgn = 1
            else:
                term = mmul(Pi, lets4[ch])
                sgn = -1
            if sgn < 0:
                term = mscale(K(-1), term)
            L[g] = madd(L[g], term)
            Pi = mmul(Pi, lets4[ch])
        assert mzero_p(msub(Pi, meye(dim))), f"relator {w[:12]}... not identity"
        for i in range(dim):
            rows_all.append([L[g][i][j] for g in gens for j in range(dim)])
    Zc = nullspace(rows_all)                     # cocycles in dim*4
    # coboundaries: v -> ((g-1)v)_g
    fixrows = []
    for g in gens:
        M = lets4[g]
        for i in range(dim):
            fixrows.append([M[i][j] - (K1 if i == j else K0)
                            for j in range(dim)])
    h0 = len(nullspace(fixrows))
    h1 = len(Zc) - (dim - h0)
    return h0, h1


# control: trivial coefficients
triv = {ch: meye(1) for ch in "abcdABCD"}
h0t, h1t = fox_h1(triv, 1)
print(f"\ncontrol (trivial coefficients): h0 = {h0t}, h1 = {h1t} "
      f"(target b1(D) = 1)", flush=True)
assert (h0t, h1t) == (1, 1), "CONTROL FAIL"

# the 27 table
lets27 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
BENDS = {"none": None, "m=1": 1, "m=4": 4, "m=5": 5, "m=7": 7,
         "m=8": 8, "m=11": 11}
PRED = {"none": 5, "m=1": 5, "m=4": 2, "m=5": 5, "m=7": 5, "m=8": 2,
        "m=11": 5}
print("\nthe dimension table (amalgam-Fox route):", flush=True)
results = {}
for name, m in BENDS.items():
    if m is None:
        s2 = side2
    else:
        c = mexp_nil(BLOCKS[m][0])
        ci = minv(c)
        s2 = {ch: mmul(mmul(c, side2[ch]), ci) for ch in "abAB"}
        # step7's banked peripherality: the bend must preserve the gates
        gg1 = mzero_p(msub(s2['a'], A27))
        gg2 = mzero_p(msub(mmul(lam27, word_mat(LONG, s2)), meye(27)))
        assert gg1 and gg2, f"bend {name} breaks the peripheral gates"
    lets4 = {'a': lets27['a'], 'b': lets27['b'],
             'A': lets27['A'], 'B': lets27['B'],
             'c': s2['a'], 'd': s2['b'], 'C': s2['A'], 'D': s2['B']}
    h0, h1 = fox_h1(lets4, 27)
    tag = "MATCHES PREDICTION" if h1 == PRED[name] else "*** DISCREPANCY ***"
    results[name] = (h0, h1)
    print(f"  {name:>5}: h0 = {h0}, h1(D;27) = {h1}   [{tag}]", flush=True)

ok = all(results[n][1] == PRED[n] for n in BENDS)
print(f"\nALL PREDICTIONS {'CONFIRMED' if ok else 'NOT CONFIRMED'} "
      f"by the method-disjoint pipeline", flush=True)
print("B637 part 1 DONE", flush=True)
