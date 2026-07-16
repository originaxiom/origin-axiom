"""B643 step 3 — the global companion via block-scalar correction.

Step 2: the derived per-side pullback acts on rep0 but not all reps;
the SL(2) diagnostic Q = [[1, r],[0,1]] != +-I proves NO global SL(2)
companion. At 27 = Sym16+Sym8+Sym0 the commutant is 3-dimensional:
T = V.D with D = P diag(d) P^{-1} may still satisfy the side-2
equations. Condition: G diag(d) H = block-scalar, where
G = conj(P)^{-1} U27i V'^{-1} V P, H = P^{-1} U27 conj(P).
Solve the linear system in (d0, d1, d2); if an invertible solution
exists, verify T as a true 4-letter intertwiner and rerun F1-F3 with
the single pullback (tau* z)(y) = T^{-1} z(Phi y).
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
double_Y = mod["double_Y"]
apply_ = mod["apply"]
kconj, mconj, minv, lift_sl2 = (mod["kconj"], mod["mconj"], mod["minv"],
                                mod["lift_sl2"])
meye, mmul = mod["meye"], mod["mmul"]
nullspace = mod["nullspace"]
ns = mod["ns"]
from fractions import Fraction as Fr
A27, B27, A27i, B27i = mod["A27"], mod["B27"], mod["A27i"], mod["B27i"]
UW, UWi = mod["U27"], mod["U27i"]
e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
Solver = ns["Solver"]

ZB6 = K(Fr(1, 2), Fr(-1, 2))
U_phi = lift_sl2([[K1, ZB6], [K0, K1]])
U_phi_i = minv(U_phi)

# ---- the f-string block basis P (as in b639_stage3) ---------------------------
def rows_minus(M, lam):
    return [[M[i][j] - (lam if i == j else K0) for j in range(27)]
            for i in range(27)]


BLOCKV = {}
for T_ in (16, 8):
    e_rows = [[e_pr[i][j] for j in range(27)] for i in range(27)]
    st = nullspace(rows_minus(h_pr, K(T_)) + e_rows)
    hi = st[0]
    vecs = [hi]
    for _ in range(T_):
        vecs.append(apply_(f_pr, vecs[-1]))
    BLOCKV[T_] = vecs
fix = nullspace(rows_minus(A27, K1) + rows_minus(B27, K1))
BLOCKV[0] = [fix[0]]
order = [(16, i) for i in range(17)] + [(8, i) for i in range(9)] + [(0, 0)]
Pcols = [BLOCKV[T_][i] for (T_, i) in order]        # 27 basis vectors
Pmat = [[Pcols[c][r] for c in range(27)] for r in range(27)]
PcolsC = [[kconj(x) for x in v] for v in Pcols]
PmatC = [[PcolsC[c][r] for c in range(27)] for r in range(27)]
blk = [0] * 17 + [1] * 9 + [2] * 1

SP = Solver([v[:] for v in Pcols])
SPC = Solver([v[:] for v in PcolsC])


def coords_matrix(S, X):
    """columns of X expressed in the basis behind S: returns C with
    X = basis-matrix . C  (C[k][j] = coefficient of basis k in col j)."""
    C = [[K0] * 27 for _ in range(27)]
    for j in range(27):
        col = [X[r][j] for r in range(27)]
        co = S.coords(col)
        for k in range(27):
            C[k][j] = co[k]
    return C


V1 = mmul(UW, mconj(U_phi))
V2 = mmul(U_phi, UWi)
N = mmul(minv(V2), V1)
G = coords_matrix(SPC, mmul(mmul(UWi, N), Pmat))
H = coords_matrix(SP, mmul(UW, PmatC))

# ---- solve G diag(d) H = block-scalar -----------------------------------------
print("== the block-scalar system ==", flush=True)
rows = []
for i in range(27):
    for j in range(27):
        if blk[i] == blk[j] and i == j:
            continue
        # off-diagonal entries must vanish (including off-diag inside a
        # block: D' block-SCALAR, so all off-diagonal of the product = 0)
        coef = [K0, K0, K0]
        for k2 in range(27):
            coef[blk[k2]] = coef[blk[k2]] + G[i][k2] * H[k2][j]
        if not all(c.is_zero() for c in coef):
            rows.append(coef)
sol = nullspace(rows) if rows else [[K1, K0, K0], [K0, K1, K0], [K0, K0, K1]]
print(f"  off-diagonal system: {len(rows)} nontrivial rows; "
      f"solution space dim = {len(sol)}", flush=True)
good = None
for s_ in sol:
    if all(not x.is_zero() for x in s_):
        good = s_
        break
if good is None and len(sol) >= 2:
    for t in range(1, 8):
        s_ = [sol[0][m] + K(t) * sol[1][m] for m in range(3)]
        if all(not x.is_zero() for x in s_):
            good = s_
            break
print(f"  invertible solution d = "
      f"{[str(x) for x in good] if good else None}", flush=True)

if good is None:
    print("NO block-scalar companion: the side-exchanging flip does not "
          "act on the 27 local system — bank the strengthened "
          "obstruction (inner-freedom probes pending).", flush=True)
else:
    # consistency: diagonal blocks scalar
    d1, d2, d3 = good
    dvals = [d1, d2, d3]
    diagv = {}
    okblk = True
    for i in range(27):
        s_ = K0
        for k2 in range(27):
            s_ = s_ + G[i][k2] * dvals[blk[k2]] * H[k2][i]
        b_ = blk[i]
        if b_ in diagv:
            if not (diagv[b_] - s_).is_zero():
                okblk = False
        else:
            diagv[b_] = s_
    print(f"  diagonal block-scalar consistency: {okblk}; "
          f"d' = {[str(diagv[b_]) for b_ in (0, 1, 2)]}", flush=True)

    # build D in the weight frame: D = P diag(d) P^{-1}
    Dw = [[K0] * 27 for _ in range(27)]
    for j in range(27):
        ej = [K1 if r == j else K0 for r in range(27)]
        co = SP.coords(ej)
        for r in range(27):
            acc = K0
            for k2 in range(27):
                acc = acc + Pcols[k2][r] * dvals[blk[k2]] * co[k2]
            Dw[r][j] = acc
    T = mmul(V1, Dw)
    Ti = minv(T)

    Yn, reps, sides_of, side2 = double_Y(None, verbose=False)
    lets4 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i,
             'c': side2.lets['a'], 'd': side2.lets['b'],
             'C': side2.lets['A'], 'D': side2.lets['B']}
    S1L = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
    S2L = side2.lets

    def wordmat(wd, L):
        M = meye(27)
        for ch in wd:
            M = mmul(M, L[ch])
        return M

    print("\n== T is a true companion? (the four letters, exact) ==",
          flush=True)
    pairs = [("a", "a", S1L, S2L), ("b", "baB", S1L, S2L),
             ("c", "a", None, None), ("d", "baB", None, None)]
    allok = True
    # side 1 letters: rho(Phi y) = rho_2(phi y); side 2: rho_1(phi y)
    for (nm, img, _, _) in pairs[:2]:
        lhs = mmul(mmul(T, S1L[nm]), Ti)
        rhs = wordmat(img, S2L)
        ok = all((lhs[i][j] - rhs[i][j]).is_zero() for i in range(27)
                 for j in range(27))
        print(f"  T rho({nm}) T^-1 = rho2(phi {nm}): {ok}", flush=True)
        allok = allok and ok
    for (nm, img) in (("a", "a"), ("b", "baB")):
        lhs = mmul(mmul(T, S2L[nm]), Ti)
        rhs = wordmat(img, S1L)
        ok = all((lhs[i][j] - rhs[i][j]).is_zero() for i in range(27)
                 for j in range(27))
        print(f"  T rho2({nm}) T^-1 = rho1(phi {nm}): {ok}", flush=True)
        allok = allok and ok

    if not allok:
        print("companion verification FAILED — stop; adjudicate.",
              flush=True)
    else:
        def word_val(z, wd, L):
            val = [K0] * 27
            Pm = meye(27)
            for ch in wd:
                if ch == 'a':
                    add = apply_(Pm, z[0])
                elif ch == 'b':
                    add = apply_(Pm, z[1])
                elif ch == 'A':
                    add = [K0 - x for x in
                           apply_(mmul(Pm, L['A']), z[0])]
                else:
                    add = [K0 - x for x in
                           apply_(mmul(Pm, L['B']), z[1])]
                val = [val[t] + add[t] for t in range(27)]
                Pm = mmul(Pm, L[ch])
            return val

        def tau_star(z):
            za = (z[0:27], z[27:54])
            zc = (z[54:81], z[81:108])
            na = apply_(Ti, word_val(zc, "a", S2L))
            nb = apply_(Ti, word_val(zc, "baB", S2L))
            nc = apply_(Ti, word_val(za, "a", S1L))
            nd = apply_(Ti, word_val(za, "baB", S1L))
            return list(na) + list(nb) + list(nc) + list(nd)

        prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
                'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
        relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
                    "aC",
                    LONG + LONG.translate(str.maketrans("abAB", "cdCD"))]
        rows_all = []
        for w_ in relators:
            Lm = {g: [[K0] * 27 for _ in range(27)] for g in "abcd"}
            Pi = meye(27)
            for ch in w_:
                g = prim[ch]
                if ch.islower():
                    term = Pi
                else:
                    term = ns["mscale"](K(-1), mmul(Pi, lets4[ch]))
                Lm[g] = ns["madd"](Lm[g], term)
                Pi = mmul(Pi, lets4[ch])
            for i in range(27):
                rows_all.append([Lm[g][i][j] for g in "abcd"
                                 for j in range(27)])

        def is_cocycle(z):
            for row in rows_all:
                s_ = sum((row[t] * z[t] for t in range(108)
                          if not z[t].is_zero()), K0)
                if not s_.is_zero():
                    return False
            return True

        print("\n== F1 (corrected): tau* acts on all 5? ==", flush=True)
        oks = [is_cocycle(tau_star(r)) for r in reps]
        print(f"  cocycle: {oks}", flush=True)
        if all(oks):
            cob = []
            for j in range(27):
                v = [K1 if t == j else K0 for t in range(27)]
                entry = []
                for g in "abcd":
                    gv = apply_(lets4[g], v)
                    entry.extend([gv[i] - v[i] for i in range(27)])
                cob.append(entry)

            def in_span(vecs, w_):
                try:
                    Solver([v[:] for v in vecs]).coords(list(w_))
                    return True
                except ValueError:
                    return False

            icob = []
            for c in cob:
                if not icob or not in_span(icob, c):
                    icob.append(c)
            basis = [r[:] for r in icob] + [list(r) for r in reps]
            SB = Solver(basis)
            print("\n== F2: the tau*-matrix ==", flush=True)
            for i, r in enumerate(reps):
                co = SB.coords(list(tau_star(r)))
                row = co[len(icob):]
                print(f"  tau*[{i}] = " + " ".join(
                    ("0" if x.is_zero() else str(x)) for x in row),
                    flush=True)
            sq = all(in_span(icob, [a - b for a, b in
                                    zip(tau_star(tau_star(r)), r)])
                     for r in reps)
            print(f"  tau*^2 = id mod coboundaries: {sq}", flush=True)

            print("\n== F3: the law of Y under tau* ==", flush=True)

            def Yval(zA, zB, zC):
                (a1, a2), (b1, b2), (c1, c2) = map(sides_of,
                                                   (zA, zB, zC))
                om1 = side1.make_omega(a1, b1, c1)
                om2 = side2.make_omega(a2, b2, c2)
                P1 = freduce("a" + LONG)
                MU2, LAM2 = "a", inv(LONG)
                P2 = freduce("a" + inv(LONG))
                Sa = lambda g, h, gh: side1.S_eval(om1, g, h, gh)
                Sb = lambda g, h, gh: side2.S_eval(om2, g, h, gh)
                return (Sa("a", LONG, P1) - Sa(LONG, "a", P1)) \
                     - (Sb(MU2, LAM2, P2) - Sb(LAM2, MU2, P2))

            for (i, j, k2) in [(0, 2, 3), (1, 2, 3), (0, 1, 2),
                               (2, 3, 4)]:
                y = Yval(reps[i], reps[j], reps[k2])
                yt = Yval(tau_star(reps[i]), tau_star(reps[j]),
                          tau_star(reps[k2]))
                ratio = "n/a"
                if not y.is_zero():
                    try:
                        ratio = str(yt / y)
                    except Exception:
                        ratio = "div-fail"
                print(f"  triple {(i, j, k2)}: Y = {y}; Y(tau*) = {yt}; "
                      f"ratio = {ratio}", flush=True)

print("\nB643 step 3 DONE", flush=True)
