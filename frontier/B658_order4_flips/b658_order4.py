"""B658 — the two order-4 orientation-reversing families through B643's
companion pipeline (prereg 0c4a1115, sealed first).

Families (B605's exact census):
  phi_A: a -> A, b -> bAB, U_A = [[-1, zbar6], [0, 1]]
  phi_B: a -> B, b -> aBA, U_B = [[0, 1], [-z6, 1]]
Control: the a-family (known singular d = (0, 0, 1)).
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

Z6 = K(Fr(1, 2), Fr(1, 2))
ZB6 = K(Fr(1, 2), Fr(-1, 2))


def mm2(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)]
            for i in range(2)]


def mi2(M):
    d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    di = d.inv()
    return [[M[1][1] * di, (K0 - M[0][1]) * di],
            [(K0 - M[1][0]) * di, M[0][0] * di]]


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


# ---- the block basis + solvers (B643 step 3/4 verbatim) -----------------
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


def conjugator_search(phi):
    P_MU = wmat2(phi("a"))
    P_L = wmat2(phi(LONG))
    MU = wmat2("a")
    Lm = wmat2(LONG)
    tmu = {1: MU, -1: mi2(MU)}
    tl = {1: Lm, -1: mi2(Lm)}
    frontier = [""]
    seen = {""}
    for depth in range(10):
        for wd in frontier:
            W = wmat2(wd)
            Wi = mi2(W)
            for s_ in (1, -1):
                if not eq2pm(P_MU, mm2(mm2(W, tmu[s_]), Wi)):
                    continue
                for t_ in (1, -1):
                    if eq2pm(P_L, mm2(mm2(W, tl[t_]), Wi)):
                        return (wd, s_, t_)
        new = []
        for wd in frontier:
            for ch in "abAB":
                if wd and wd[-1] == {'a': 'A', 'A': 'a', 'b': 'B',
                                     'B': 'b'}[ch]:
                    continue
                w2 = wd + ch
                if w2 not in seen:
                    seen.add(w2)
                    new.append(w2)
        frontier = new
    return None


def run_family(name, mapping, U2):
    print(f"\n== family {name} ==", flush=True)

    def phi(wd):
        m = dict(mapping)
        m['A'] = inv(m['a'])
        m['B'] = inv(m['b'])
        return freduce("".join(m[ch] for ch in wd))

    found = conjugator_search(phi)
    print(f"  peripheral conjugator (w, s, t): {found}", flush=True)
    if found is None:
        print("  bounded-search negative to depth 9 (banked as such).",
              flush=True)
        return None
    w_word, s_sign, t_sign = found
    d2 = U2[0][0] * U2[1][1] - U2[0][1] * U2[1][0]
    print(f"  det(U2) = {d2}  (weight-even lift: PGL-valid)", flush=True)
    U27 = lift_sl2(U2)
    W27 = meye(27)
    for ch in w_word:
        W27 = mmul(W27, {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}[ch])
    U_psi27 = mmul(minv(W27), U27)
    return blockscalar_solve(U_psi27, f"{name}, w = {w_word!r}, "
                                      f"(s,t) = ({s_sign},{t_sign})")


print("== control: the a-family (expect singular d = (0,0,1)) ==",
      flush=True)
U_phi_a = lift_sl2([[K1, ZB6], [K0, K1]])
ok_ctrl = blockscalar_solve(U_phi_a, "control phi(a)=a, w = e")
print(f"  control singular as banked: {not ok_ctrl}", flush=True)

resA = run_family("phi(a)=A (order 4)",
                  {'a': "A", 'b': "bAB"},
                  [[K0 - K1, ZB6], [K0, K1]])
resB = run_family("phi(a)=B (order 4)",
                  {'a': "B", 'b': "aBA"},
                  [[K0, K1], [K0 - Z6, K1]])

print("\n== VERDICT ==", flush=True)
for nm, r in (("phi(a)=A", resA), ("phi(a)=B", resB)):
    print(f"  {nm}: " + ("ACTS (companion exists; gates stage required)"
                         if r else
                         ("BROKEN" if r is not None else
                          "bounded-search negative")), flush=True)
if resA is False and resB is False:
    print("  WALL-8 UPGRADE: all FOUR orientation-reversing families of "
          "D4 break on the double's 27 local system; the surviving "
          "symmetry is the deck swap sigma* exactly.", flush=True)

print("\nB658 DONE", flush=True)
