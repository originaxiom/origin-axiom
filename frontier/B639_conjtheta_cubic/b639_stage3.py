"""B639 stage 3 (L92) — the CORRECT theta-realization: the form-adjoint.
B_theta = the block-diagonal SL(2)-invariant symmetric pairing on
27 = Sym16 + Sym8 + Sym0; the contragredient = B_theta-adjoint (the
weight-basis transpose was the stage-2 bug: Sym-functor and transpose
do not commute in a non-self-dual basis). Side 2 = W . B-adjoint-conj
. W^-1 with W = lift(Weyl); gates: peripherals, C-invariance question,
h0/h1, and (if h1 >= 3) the cubic.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "B637_corrected_cell3")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG, REL = mod["LONG"], mod["REL"]
side1, Side = mod["side1"], mod["Side"]
apply_ = mod["apply"]
kconj, mconj, minv, lift_sl2 = (mod["kconj"], mod["mconj"], mod["minv"],
                                mod["lift_sl2"])
meye, mmul = mod["meye"], mod["mmul"]
nullspace = mod["nullspace"]
ns = mod["ns"]
Cval = mod["Cval"]
A27, B27, A27i, B27i = mod["A27"], mod["B27"], mod["A27i"], mod["B27i"]
e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
lets1 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}

# ---- B_theta: block-diagonal invariant symmetric pairing ---------------------
def rows_minus(M, lam):
    return [[M[i][j] - (lam if i == j else K0) for j in range(27)]
            for i in range(27)]
BLOCKV = {}
for T in (16, 8):
    e_rows = [[e_pr[i][j] for j in range(27)] for i in range(27)]
    st = nullspace(rows_minus(h_pr, K(T)) + e_rows)
    hi = st[0]
    vecs = [hi]
    for _ in range(T):
        vecs.append(apply_(f_pr, vecs[-1]))
    BLOCKV[T] = vecs
fix = nullspace(rows_minus(A27, K1) + rows_minus(B27, K1))
BLOCKV[0] = [fix[0]]
# the invariant pairing on Sym^{2s} in the f-string basis:
# <f^i v, f^j v> = 0 unless i+j = 2s; with <f^i v, f^{2s-i} v> =
# (-1)^i * i! * (2s-i)! * binom-normalization; solve invariance directly:
# B(e u, v) + B(u, e v) = 0 determines the antidiagonal recursively.
import sympy  # noqa (only for factorial safety if needed)
Bth = [[K0]*27 for _ in range(27)]
order = [(16, i) for i in range(17)] + [(8, i) for i in range(9)] + [(0, 0)]
P = [[None]*27 for _ in range(27)]
for col, (T, i) in enumerate(order):
    for row in range(27):
        P[row][col] = BLOCKV[T][i][row]
# build the block pairing in block coordinates then push to weight basis:
# recursion: b_{i+1} = -b_i * (coefficient from e f^{i+1} v = c_i f^i v):
# e f^{k} v_top = k(2s - k + 1) f^{k-1} v_top  (standard sl2)
Bblk = [[K0]*27 for _ in range(27)]
off = 0
for (T, dim) in ((16, 17), (8, 9), (0, 1)):
    s2 = T
    b = [K0]*dim
    b0 = K1
    b[0] = b0
    # B(f^i v, f^{2s-i} v): invariance under e:
    # B(e f^i v, f^{j} v) + B(f^i v, e f^j v) = 0 with i+j = 2s+1... derive:
    # i(2s-i+1) B(f^{i-1}, f^{j}) + j(2s-j+1) B(f^i, f^{j-1}) = 0 at i+j-1=2s
    for i in range(1, dim):
        j = (dim - 1) - i + 1          # so that (i-1) + j = 2s
        ci = K(i * (s2 - i + 1))
        cj = K(j * (s2 - j + 1))
        b[i] = K0 - (cj * b[i-1]) * ci.inv() if not ci.is_zero() else K0
    for i in range(dim):
        Bblk[off + i][off + (dim - 1 - i)] = b[i]
    off += dim
Pm = P
Pmi = minv([row[:] for row in Pm])
# B_theta in the weight basis: B_w = (P^-1)^T Bblk P^-1
PmiT = [[Pmi[j][i] for j in range(27)] for i in range(27)]
Bth = mmul(mmul(PmiT, Bblk), Pmi)
Bthi = minv([row[:] for row in Bth])
# gate: invariance rho^T B rho = B for the letters
def transpose(M):
    return [[M[j][i] for j in range(27)] for i in range(27)]
inv_ok = all(ns["mzero_p"](ns["msub"](mmul(mmul(transpose(lets1[ch]), Bth),
                                           lets1[ch]), Bth))
             for ch in "ab")
print(f"B_theta invariance (rho^T B rho = B): {inv_ok}", flush=True)

def form_adjoint_conj(M):
    # B . conj(M) . B^-1  = the theta-twisted mirror letter
    return mmul(mmul(Bth, mconj(M)), Bthi)

W27 = lift_sl2([[K0, K(-1)], [K1, K0]])
W27i = minv(W27)
for tag, wrap in (("plain", lambda X: X),
                  ("W-conj", lambda X: mmul(mmul(W27, X), W27i))):
    s2l = {ch: wrap(form_adjoint_conj(lets1[ch])) for ch in "abAB"}
    lam1 = meye(27)
    lam2 = meye(27)
    for ch in LONG:
        lam1 = mmul(lam1, lets1[ch])
        lam2 = mmul(lam2, s2l[ch])
    g_mu_p = ns["mzero_p"](ns["msub"](s2l['a'], A27))
    g_lam_inv = ns["mzero_p"](ns["msub"](mmul(lam1, lam2), meye(27)))
    g_lam_pl = ns["mzero_p"](ns["msub"](lam2, lam1))
    print(f"  [{tag}] mu-match {g_mu_p}; lambda-inverted {g_lam_inv}; "
          f"lambda-plus {g_lam_pl}", flush=True)
    if g_mu_p and (g_lam_inv or g_lam_pl):
        print(f"  GLUING FOUND ({tag}); proceeding to h0/h1...", flush=True)
        prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
                'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
        r4 = LONG + (LONG.translate(str.maketrans("abAB", "cdCD"))
                     if g_lam_inv else
                     inv(LONG.translate(str.maketrans("abAB", "cdCD"))))
        relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
                    "aC", r4]
        lets4 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i,
                 'c': s2l['a'], 'd': s2l['b'], 'C': s2l['A'],
                 'D': s2l['B']}
        rows_all = []
        for w_ in relators:
            L = {g: [[K0]*27 for _ in range(27)] for g in "abcd"}
            Pi = meye(27)
            for ch in w_:
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
                rows_all.append([L[g][i][j] for g in "abcd"
                                 for j in range(27)])
        Zc = nullspace(rows_all)
        cob = []
        for j in range(27):
            v = [K1 if t == j else K0 for t in range(27)]
            entry = []
            for g in "abcd":
                gv = apply_(lets4[g], v)
                entry.extend([gv[i] - v[i] for i in range(27)])
            cob.append(entry)
        Solver = ns["Solver"]
        reps, basis = [], [r[:] for r in cob]
        for z in Zc:
            try:
                Solver(basis).coords(z)
            except ValueError:
                reps.append(z)
                basis.append(z)
        print(f"  h1(D_theta; 27) = {len(reps)}", flush=True)
        # C-invariance of the side-2 letters (the theta-side cubic question)
        u1 = [K(i % 5 - 2) for i in range(27)]
        v1 = [K((2*i) % 7 - 3) for i in range(27)]
        w1 = [K((3*i) % 4 - 1) for i in range(27)]
        ci = (Cval(apply_(s2l['a'], u1), apply_(s2l['a'], v1),
                   apply_(s2l['a'], w1)) - Cval(u1, v1, w1)).is_zero()
        print(f"  C-invariance of theta-side letters: {ci}", flush=True)
        break
print("B639 stage 3 DONE", flush=True)
