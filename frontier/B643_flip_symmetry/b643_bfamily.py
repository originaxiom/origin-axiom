"""B643 step 4 — (i) the singular-d diagnostic for the a-family flip;
(ii) the phi(a)=b involution family through the same companion pipeline.

phi_b: a -> b, b -> abA (B605 family 3, U_phib = [[0,1],[z6,1]], det
-z6, normalized into SL(2) by z3^{-1}).  phi_b does not fix the
peripheral letters, so first find w with phi_b(mu) = w mu^{s} w^{-1}
and phi_b(LONG) = w LONG^{t} w^{-1} (exact SL(2) search); then
psi = Ad(w^{-1}) . phi_b fixes the peripheral system and
Phi_b = swap . psi is an automorphism of the double.  Companion:
U_psi = rho(w)^{-1} U_phib; V1 = UW conj(U_psi), V2 = U_psi UWi;
solve the block-scalar system as in step 3.
"""
import os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "B637_corrected_cell3")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG = mod["LONG"]
apply_ = mod["apply"]
kconj, mconj, minv, lift_sl2 = (mod["kconj"], mod["mconj"], mod["minv"],
                                mod["lift_sl2"])
meye, mmul = mod["meye"], mod["mmul"]
nullspace = mod["nullspace"]
ns = mod["ns"]
A27, B27, A27i, B27i = mod["A27"], mod["B27"], mod["A27i"], mod["B27i"]
UW, UWi = mod["U27"], mod["U27i"]
e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
Solver = ns["Solver"]
lets2 = mod["lets2"]

Z6 = K(Fr(1, 2), Fr(1, 2))            # zeta6 = (1 + r)/2
ZB6 = K(Fr(1, 2), Fr(-1, 2))
Z3 = K(Fr(-1, 2), Fr(1, 2))           # zeta3
Z3B = K(Fr(-1, 2), Fr(-1, 2))         # zeta3^{-1} = conj

# ---- SL(2) helpers -------------------------------------------------------------
def mm2(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)]
            for i in range(2)]


def mi2(M):
    return [[M[1][1], K0 - M[0][1]], [K0 - M[1][0], M[0][0]]]


def mc2(M):
    return [[kconj(x) for x in row] for row in M]


def wmat2(w):
    M = [[K1, K0], [K0, K1]]
    for ch in w:
        M = mm2(M, lets2[ch])
    return M


def sc2(c, M):
    return [[c * M[i][j] for j in range(2)] for i in range(2)]


def eq2(A, B):
    return all((A[i][j] - B[i][j]).is_zero() for i in range(2)
               for j in range(2))


def eq2pm(A, B):
    return eq2(A, B) or eq2(A, sc2(K(-1), B))


# ---- part (i): the singular d of the a-family ---------------------------------
def rows_minus(M, lam):
    return [[M[i][j] - (lam if i == j else K0) for j in range(27)]
            for i in range(27)]


BLOCKV = {}
for T_ in (16, 8):
    e_rows = [[e_pr[i][j] for j in range(27)] for i in range(27)]
    st = nullspace(rows_minus(h_pr, K(T_)) + e_rows)
    vecs = [st[0]]
    for _ in range(T_):
        vecs.append(apply_(f_pr, vecs[-1]))
    BLOCKV[T_] = vecs
fix = nullspace(rows_minus(A27, K1) + rows_minus(B27, K1))
BLOCKV[0] = [fix[0]]
order = [(16, i) for i in range(17)] + [(8, i) for i in range(9)] + [(0, 0)]
Pcols = [BLOCKV[T_][i] for (T_, i) in order]
Pmat = [[Pcols[c][r] for c in range(27)] for r in range(27)]
PcolsC = [[kconj(x) for x in v] for v in Pcols]
PmatC = [[PcolsC[c][r] for c in range(27)] for r in range(27)]
blk = [0] * 17 + [1] * 9 + [2] * 1
SP = Solver([v[:] for v in Pcols])
SPC = Solver([v[:] for v in PcolsC])


def coords_matrix(S, X):
    C = [[K0] * 27 for _ in range(27)]
    for j in range(27):
        col = [X[r][j] for r in range(27)]
        co = S.coords(col)
        for k in range(27):
            C[k][j] = co[k]
    return C


def blockscalar_solve(U_comp27, tag):
    """V1 = UW conj(U), V2 = U UWi; report the d-solution space."""
    V1 = mmul(UW, mconj(U_comp27))
    V2 = mmul(U_comp27, UWi)
    N = mmul(minv(V2), V1)
    G = coords_matrix(SPC, mmul(mmul(UWi, N), Pmat))
    H = coords_matrix(SP, mmul(UW, PmatC))
    rows = []
    for i in range(27):
        for j in range(27):
            if i == j:
                continue
            coef = [K0, K0, K0]
            for k2 in range(27):
                coef[blk[k2]] = coef[blk[k2]] + G[i][k2] * H[k2][j]
            if not all(c.is_zero() for c in coef):
                rows.append(coef)
    sol = nullspace(rows) if rows else [[K1, K0, K0], [K0, K1, K0],
                                        [K0, K0, K1]]
    print(f"  [{tag}] off-diag rows {len(rows)}; solution dim {len(sol)}",
          flush=True)
    for s_ in sol:
        print(f"    d = ({', '.join(str(x) for x in s_)})   "
              f"[blocks Sym16, Sym8, Sym0]", flush=True)
    inv_ok = any(all(not x.is_zero() for x in s_) for s_ in sol)
    print(f"    invertible member: {inv_ok}", flush=True)
    return inv_ok


print("== (i) a-family singular-d diagnostic ==", flush=True)
U_phi_a = lift_sl2([[K1, ZB6], [K0, K1]])
blockscalar_solve(U_phi_a, "phi(a)=a, w = e")

# ---- part (ii): the b-family ----------------------------------------------------
print("\n== (ii) phi(a)=b: the peripheral conjugator search ==", flush=True)


def phi_b(wd):
    m = {'a': "b", 'b': "abA", 'A': "B", 'B': inv("abA")}
    return freduce("".join(m[ch] for ch in wd))


PB_MU = wmat2(phi_b("a"))
PB_L = wmat2(phi_b(LONG))
MU = wmat2("a")
Lm = wmat2(LONG)
targets_mu = {1: MU, -1: mi2(MU)}
targets_l = {1: Lm, -1: mi2(Lm)}

found = None
frontier = [""]
seen = {""}
for depth in range(10):
    if found:
        break
    new = []
    for wd in frontier:
        for ch in "abAB":
            if wd and wd[-1] == {'a': 'A', 'A': 'a', 'b': 'B',
                                 'B': 'b'}[ch]:
                continue
            w2 = wd + ch
            if w2 in seen:
                continue
            seen.add(w2)
            new.append(w2)
            W = wmat2(w2)
            Wi = mi2(W)
            for s_ in (1, -1):
                if not eq2pm(PB_MU, mm2(mm2(W, targets_mu[s_]), Wi)):
                    continue
                for t_ in (1, -1):
                    if eq2pm(PB_L, mm2(mm2(W, targets_l[t_]), Wi)):
                        found = (w2, s_, t_)
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    frontier = new
print(f"  conjugator: {found}", flush=True)

if found is None:
    print("  no peripheral conjugator to depth 9 — the b-family flip "
          "does not normalize the peripheral system in range; bank as "
          "bounded-search negative.", flush=True)
else:
    w_word, s_sign, t_sign = found
    # normalized U_phib in SL(2): U/z3  (det [[0,1],[z6,1]] = -z6 = z3^2)
    U_phib2 = [[K0 * Z3B, K1 * Z3B], [Z6 * Z3B, K1 * Z3B]]
    dcheck = U_phib2[0][0] * U_phib2[1][1] - U_phib2[0][1] * U_phib2[1][0]
    print(f"  det(normalized U_phib) = {dcheck}", flush=True)
    U_phib27 = lift_sl2(U_phib2)
    W27 = meye(27)
    for ch in w_word:
        W27 = mmul(W27, {'a': A27, 'b': B27, 'A': A27i,
                         'B': B27i}[ch])
    U_psi27 = mmul(minv(W27), U_phib27)
    print("\n== (ii) b-family block-scalar system ==", flush=True)
    inv_ok = blockscalar_solve(U_psi27, f"phi(a)=b, w = {w_word!r}")
    if inv_ok:
        print("  INVERTIBLE companion exists — proceed to gates "
              "(next stage).", flush=True)
    else:
        print("  NO invertible companion for the b-family either: the "
              "chord breaks BOTH flip classes; only the deck swap "
              "sigma* survives.", flush=True)

print("\nB643 step 4 DONE", flush=True)
