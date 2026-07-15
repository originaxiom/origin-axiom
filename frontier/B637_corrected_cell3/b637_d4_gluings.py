"""B637 part 2a — the four B605 D4-intertwiner gluings D_g(M) (prereg
99815a48...): exact GL(27) peripheral gates; INCOMPATIBLE is an honest
verdict; h0/h1 per compatible family.

Per B605 (banked, certified over K): the four orientation-reversing
families phi with U * conj(rho(x)) * U^-1 = (+-) rho(phi(x)). At the
27-level the signs die (all principal weights on the 27 are even, so
-I in SL(2) lifts to the identity). The double D_phi = M cup_{phi|T} Mbar:
side 2 = g * conj(rho) * g^-1 with g = lift(conj(U))^-1; peripheral
relations i1(x) = i2(phi(x)) for x in {mu = a, lambda = LONG}.
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
from fractions import Fraction as Fr
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
REL = ns["REL"]
nullspace, rref = ns["nullspace"], ns["rref"]
meye, mmul, madd, mscale, msub, mzero_p = (ns[k] for k in
    ("meye", "mmul", "madd", "mscale", "msub", "mzero_p"))
mexp_nil = ns["mexp_nil"]
LONG = "abABaaBAbA"


def kconj(x): return K(x.a, -x.b)
def mconj(M): return [[kconj(x) for x in row] for row in M]


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


def lift_sl2(g):
    """lift g in SL(2,K) (or GL with square-free scalar ambiguity killed by
    even weights) to GL(27) via the principal embedding."""
    p, q, r, s = g[0][0], g[0][1], g[1][0], g[1][1]
    det = p * s - q * r
    if p.is_zero():
        # g = w * (w^-1 g), w = exp(e) exp(-f) exp(e)
        w27 = mmul(mmul(mexp_nil(e_pr), mexp_nil(mscale(K(-1), f_pr))),
                   mexp_nil(e_pr))
        ginv_w = [[K0 - r, K0 - s], [p, q]]        # w^-1 g, w^-1 = [[0,-1],[1,0]]
        return mmul(w27, lift_sl2(ginv_w))
    lower = mexp_nil(mscale(r * p.inv(), f_pr))
    upper = mexp_nil(mscale(q * p.inv(), e_pr))
    t2 = (p * p) * det.inv()
    D = meye(27)
    for i in range(27):
        w = h_pr[i][i]
        wi = int(w.a)
        e = wi // 2
        val = K1
        base = t2 if e >= 0 else t2.inv()
        for _ in range(abs(e)):
            val = val * base
        D[i][i] = val
    return mmul(mmul(lower, D), upper)


def word_mat(word, lets):
    M = meye(27)
    for ch in word:
        M = mmul(M, lets[ch])
    return M


def inv_word(w):
    return w[::-1].swapcase()


def phi_word(w, wa, wb):
    out = []
    m = {'a': wa, 'b': wb, 'A': inv_word(wa), 'B': inv_word(wb)}
    for ch in w:
        out.append(m[ch])
    return "".join(out)


lets1 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
lam1 = word_mat(LONG, lets1)

ZB6 = K(Fr(1, 2), Fr(-1, 2))                     # zeta6-bar = (1 - sqrt(-3))/2
Z6 = K(Fr(1, 2), Fr(1, 2))
FAMILIES = {
    "phi(a)=a": ("a", "baB", [[K1, ZB6], [K0, K1]]),
    "phi(a)=A": ("A", "bAB", [[K(-1), ZB6], [K0, K1]]),
    "phi(a)=b": ("b", "abA", [[K0, K1], [Z6, K1]]),
    "phi(a)=B": ("B", "aBA", [[K0, K1], [K0 - Z6, K1]]),
}


def fox_h1(lets4, dim, relators):
    prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
            'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
    gens = "abcd"
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
        assert mzero_p(msub(Pi, meye(dim))), f"relator not identity: {w[:16]}"
        for i in range(dim):
            rows_all.append([L[g][i][j] for g in gens for j in range(dim)])
    Zc = nullspace(rows_all)
    fixrows = []
    for g in gens:
        M = lets4[g]
        for i in range(dim):
            fixrows.append([M[i][j] - (K1 if i == j else K0)
                            for j in range(dim)])
    h0 = len(nullspace(fixrows))
    return h0, len(Zc) - (dim - h0)


print("\nthe four D4 gluings:", flush=True)
for name, (wa, wb, U) in FAMILIES.items():
    Ubar = mconj(U)
    g27 = minv(lift_sl2(Ubar))
    g27i = minv(g27)
    s2 = {ch: mmul(mmul(g27, mconj(lets1[ch])), g27i) for ch in "abAB"}
    # gates: rho(mu) = s(phi(mu)), rho(lambda) = s(phi(lambda))
    pm = phi_word("a", wa, wb)
    pl = phi_word(LONG, wa, wb)
    gate_mu = mzero_p(msub(word_mat(pm, s2), A27))
    gate_lam = mzero_p(msub(word_mat(pl, s2), lam1))
    print(f"  {name} (phi(b)={wb}): mu-gate {gate_mu}, lambda-gate {gate_lam}",
          flush=True)
    if not (gate_mu and gate_lam):
        print(f"    VERDICT: INCOMPATIBLE (the banked 27 local system does "
              f"not glue through this family)", flush=True)
        continue
    lets4 = {'a': lets1['a'], 'b': lets1['b'], 'A': lets1['A'],
             'B': lets1['B'],
             'c': s2['a'], 'd': s2['b'], 'C': s2['A'], 'D': s2['B']}
    c_pm = pm.translate(str.maketrans("abAB", "cdCD"))
    c_pl = pl.translate(str.maketrans("abAB", "cdCD"))
    relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
                "a" + inv_word(c_pm), LONG + inv_word(c_pl)]
    # trivial control
    triv = {ch: meye(1) for ch in "abcdABCD"}
    h0t, h1t = fox_h1(triv, 1, relators)
    h0, h1 = fox_h1(lets4, 27, relators)
    print(f"    trivial control: h0 = {h0t}, b1(D_phi) = {h1t}", flush=True)
    print(f"    VERDICT: COMPATIBLE — h0(D;27) = {h0}, h1(D;27) = {h1}"
          f"{'   [h1 >= 3: 3-form candidate]' if h1 >= 3 else ''}",
          flush=True)

print("\nB637 part 2a DONE", flush=True)
