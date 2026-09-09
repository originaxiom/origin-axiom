"""B1302 Q1: on m202 (exact holonomy in SL(2, Z[omega])), h^1(m202; Sym^k) for even k <= 22 and the induced 2x2 action of the inversion
(a,b) -> (a^-1, b^-1) and of the order-3 rotation (a,b) -> (a^-1 b, a^-1) on H^1, with eigenvalues.  sm:B1282 predicts h^1 = 2, inversion =
scalar (-1)^(k/2+1), order-3 = (omega, omega-bar) for k = 2 mod 6 and (1, 1) for k = 4 mod 6."""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1297_the_spectral_cover_index", "verification"))
import d2lib as L
from d2lib import K, ONE, ZERO, Z12, OMEGA
ex = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "m202_exact.json")))
z2 = Z12 * Z12
A = L.mat([[z2 * (-2), K(-1) - z2], [z2, z2]]); B = L.mat([[-z2, z2], [K(-1) + z2, ZERO]])
gens = ["a", "b"]; RELS = [L.word_from_snappy(ex["rel"])]; pres = L.Presentation(gens, RELS); rho = L.Rep({"a": A, "b": B})
assert L.meq(rho(RELS[0]), L.eye(2))
SIG = {"inversion": {"a": L.word_from_snappy("A"), "b": L.word_from_snappy("B")}, "order3": {"a": L.word_from_snappy("Ab"), "b": L.word_from_snappy("A")}}
def subst(word, im):
    out = []
    for g, e in word: out += im[g] if e == 1 else L.inv_word(im[g])
    return L.free_reduce(out)
def intertwiner(im):
    rows = []
    for g in gens:
        X = rho([(g, 1)]); Y = rho(im[g])
        for i in range(2):
            for j in range(2):
                row = [ZERO] * 4
                for k in range(2):
                    row[2 * i + k] = row[2 * i + k] + X[k][j]; row[2 * k + j] = row[2 * k + j] - Y[i][k]
                rows.append(row)
    rk, null = L.rref_rank_null(rows); assert len(null) == 1, ("intertwiner space", len(null))
    n = null[0]; N = [[n[0], n[1]], [n[2], n[3]]]
    for g in gens: assert L.meq(L.mmul(N, rho([(g, 1)])), L.mmul(rho(im[g]), N))
    return N, L.det2(N)
def charpoly2(M):  # x^2 - tr x + det
    return L.tr(M), L.det2(M)
res = {}
for name, im in SIG.items():
    r = rho(subst(RELS[0], im)); assert L.meq(r, L.eye(2)) or L.meq(r, L.mneg(L.eye(2))), name
    N, d = intertwiner(im); Ninv = L.general_inv(N); res[name] = {"det": str(d), "k": {}}
    print(f"sigma = {name}: N = {N}, det = {d}")
    for k in range(0, 23, 2):
        n = k + 1; mats = {g: L.sym_power(rho([(g, 1)]), k) for g in gens}; V = L.Rep(mats)
        d0, d1 = L.cochain_maps(pres, V); r0 = L.rank(d0); _, Z1 = L.rref_rank_null(d1)
        h1 = (2 * n - L.rank(d1)) - r0
        # a basis of H^1: Z1 vectors independent modulo B^1
        basis = []; cur = d0
        for v in Z1:
            if L.rank(L.hstack(cur, L.cols_from_vectors([v], 2 * n))) > L.rank(cur): basis.append(v); cur = L.hstack(cur, L.cols_from_vectors([v], 2 * n))
            if len(basis) == h1: break
        Nk = L.sym_power(N, k); Nkinv = L.general_inv(Nk) if k else [[ONE]]
        def act(z):
            za, zb = z[:n], z[n:]
            def fval(word):
                Dd = L.fox(V, word, gens)
                return [sum((Dd["a"][i][j] * za[j] for j in range(n)), ZERO) + sum((Dd["b"][i][j] * zb[j] for j in range(n)), ZERO) for i in range(n)]
            out = []
            for g in gens:
                w = fval(im[g]); out += [sum((Nkinv[i][j] * w[j] for j in range(n)), ZERO) for i in range(n)]
            return out
        # matrix of the action on H^1 in the chosen basis: z'_j = sum_i M[i][j] z_i + d0 v
        Mact = [[ZERO] * h1 for _ in range(h1)]
        for j, z in enumerate(basis):
            zp = act(z)
            Mx = L.hstack(L.hstack(L.cols_from_vectors(basis, 2 * n), d0), L.cols_from_vectors([[-x for x in zp]], 2 * n))
            _, nul = L.rref_rank_null(Mx); sols = [v for v in nul if not v[-1].is_zero()]; assert sols, "z' not in the span"
            s = sols[0]; last = s[-1]
            for i in range(h1): Mact[i][j] = s[i] / last
        # det normalisation: eigenvalues scale by det(N)^(k/2)
        scale = ONE
        for _ in range(k // 2): scale = scale * d
        Mn = L.mscale(Mact, scale)
        trM, detM = charpoly2(Mn) if h1 == 2 else (Mn[0][0], ONE)
        res[name]["k"][k] = dict(h1=h1, tr=str(trM), det=str(detM), scalar=str(Mn[0][0]) if h1 == 2 and L.meq(Mn, L.mscale(L.eye(2), Mn[0][0])) else None)
        print(f"  k={k:2d}: h1={h1}  action tr={trM} det={detM}  scalar? {res[name]['k'][k]['scalar']}")
# predictions
ok = True
for k in range(0, 23, 2):
    exp = K(1) if (k // 2 + 1) % 2 == 0 else K(-1)
    r = res["inversion"]["k"][k]; ok &= (r["h1"] == 2 and r["scalar"] == str(exp))
    r3 = res["order3"]["k"][k]
    if k % 6 == 2: ok &= (r3["tr"] == str(K(-1)) and r3["det"] == str(ONE))           # (omega, omega-bar): tr -1, det 1
    elif k % 6 == 4 and k > 0: ok &= (r3["scalar"] == str(ONE))                           # (1, 1)
print("Q1:", "PASS" if ok else "FAIL")
json.dump(res, open("b1302_signs.json", "w"), indent=1)
