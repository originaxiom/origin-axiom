"""B1298 (a): the twelve signs, exactly. For k = 0, 2, ..., 22 the strong inversion S (a->a^-1, b->b^-1) and the period-2 P
(a->a^-1, b->a^3 b) act on the one-dimensional H^1(m004; Sym^k rho_geo); the intertwiner N_sigma with N rho(g) N^-1 = rho(sigma g)
is solved as an exact nullspace over Q(zeta_12), the induced map f -> Sym^k(N)^-1 f o sigma is applied to a cocycle spanning H^1,
and the eigenvalue is read off by exhibiting z' - eps z in B^1.  Prediction (DESIGN P1): eps_S(k) = (-1)^(k/2+1), eps_P(k) = +1."""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1297_the_spectral_cover_index", "verification"))
import d2lib as L
from d2lib import K, OMEGA, ONE, ZERO

REL = L.word_from_snappy("aaabABBAb"); gens = ["a", "b"]; pres = L.Presentation(gens, [REL])
A = L.mat([[1 - OMEGA, 1], [-1, 0]]); B = L.mat([[0, -1], [1, OMEGA * (-2)]]); rho = L.Rep({"a": A, "b": B})
assert L.meq(rho(REL), L.eye(2))
SIG = {"S": {"a": [("a", -1)], "b": [("b", -1)]}, "P": {"a": [("a", -1)], "b": [("a", 1)] * 3 + [("b", 1)]}}
def subst(word, im):
    out = []
    for g, e in word: out += im[g] if e == 1 else L.inv_word(im[g])
    return L.free_reduce(out)
for name, im in SIG.items():
    r = rho(subst(REL, im)); assert L.meq(r, L.eye(2)) or L.meq(r, L.mneg(L.eye(2))), name
def intertwiner(im):
    """solve N rho(g) = rho(sigma g) N for g in {a,b}: 8 linear equations in the 4 entries of N"""
    rows = []
    for g in gens:
        X = rho([(g, 1)]); Y = rho(im[g])
        # (N X - Y N)_{ij} = sum_k N_{ik} X_{kj} - sum_k Y_{ik} N_{kj} = 0 ; unknown vector n = (N00, N01, N10, N11)
        for i in range(2):
            for j in range(2):
                row = [ZERO] * 4
                for k in range(2):
                    row[2 * i + k] = row[2 * i + k] + X[k][j]          # N_{ik} X_{kj}
                    row[2 * k + j] = row[2 * k + j] - Y[i][k]          # - Y_{ik} N_{kj}
                rows.append(row)
    rk, null = L.rref_rank_null(rows); assert len(null) == 1, ("intertwiner space dim", len(null))
    n = null[0]; N = [[n[0], n[1]], [n[2], n[3]]]
    for g in gens: assert L.meq(L.mmul(N, rho([(g, 1)])), L.mmul(rho(im[g]), N))
    return N, L.det2(N)
res = {}
for name, im in SIG.items():
    N, d = intertwiner(im); res[name] = {"N": [[str(x) for x in r] for r in N], "det": str(d), "eps": {}}
    print(f"sigma = {name}: intertwiner N = {N}, det N = {d}")
    Ninv = L.general_inv(N)
    for k in range(0, 23, 2):
        mats = {g: L.sym_power(rho([(g, 1)]), k) for g in gens}; V = L.Rep(mats); n = k + 1
        d0, d1 = L.cochain_maps(pres, V)
        _, Z1 = L.rref_rank_null(d1)
        # a cocycle spanning H^1: the first Z1 vector not in im d0
        r0 = L.rank(d0); z = next(v for v in Z1 if L.rank(L.hstack(d0, L.cols_from_vectors([v], 2 * n))) > r0)
        za, zb = z[:n], z[n:]
        Nk = L.sym_power(N, k); Nkinv = L.general_inv(Nk) if k else [[ONE]]
        def fval(word):  # f(word) = sum_x rho(dword/dx) f(x)
            D = L.fox(V, word, gens)
            va = [sum((D["a"][i][j] * za[j] for j in range(n)), ZERO) for i in range(n)]
            vb = [sum((D["b"][i][j] * zb[j] for j in range(n)), ZERO) for i in range(n)]
            return [va[i] + vb[i] for i in range(n)]
        zp = []
        for g in gens:
            w = fval(im[g]); zp += [sum((Nkinv[i][j] * w[j] for j in range(n)), ZERO) for i in range(n)]
        # solve zp = eps z + d0 v : nullspace of [z | d0 | -zp] has one vector (eps, v, 1) up to scale
        M = L.hstack(L.hstack(L.cols_from_vectors([z], 2 * n), d0), L.cols_from_vectors([[-x for x in zp]], 2 * n))
        _, nul = L.rref_rank_null(M)
        sols = [v for v in nul if not v[-1].is_zero()]; assert sols, "z' is not eps z + coboundary"
        ratios = {str(v[0] / v[-1]) for v in sols}; assert len(ratios) == 1, ("eps not unique", ratios)   # ker d0 adds (0, v, 0) only
        eps_raw = sols[0][0] / sols[0][-1]
        # normalise the intertwiner to det 1: N = lambda N0 with lambda^2 = 1/d  =>  eps = eps_raw * d^(k/2)
        eps = eps_raw
        for _ in range(k // 2): eps = eps * d
        res[name]["eps"][k] = str(eps)
        print(f"  k={k:2d}: h1={2*n - L.rank(d1) - r0}  eps_raw={eps_raw}  det^(k/2)-normalised eps = {eps}")
pred_S = {k: (1 if (k // 2 + 1) % 2 == 0 else -1) for k in range(0, 23, 2)}
okS = all(res["S"]["eps"][k] == str(K(pred_S[k])) for k in range(0, 23, 2))
okP = all(res["P"]["eps"][k] == str(K(1)) for k in range(0, 23, 2))
print("\nP1: eps_S(k) = (-1)^(k/2+1) for all even k <= 22:", okS, "   eps_P(k) = +1 for all:", okP)
six = {2: "V2 (f4)", 8: "V8 (26)", 10: "V10 (f4)", 14: "V14 (f4)", 16: "V16 (26)", 22: "V22 (f4)"}
print("the six deformation classes:", {six[k]: res["S"]["eps"][k] for k in six}, " theta_D = (+,-,+,+,-,+)")
json.dump(res, open("b1298_signs.json", "w"), indent=1)
print("B1298 SIGNS:", "PASS" if okS and okP else "FAIL")
