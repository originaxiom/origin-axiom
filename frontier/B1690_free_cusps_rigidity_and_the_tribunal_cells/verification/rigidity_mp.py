"""sm:B1523's P2 on main, at 60 digits (the float64 route in main_b1523.py miscounted ranks: its relative tolerance and its
precision, found on b++LLLLLR before any reading of the census; that route's output is void).  v = {J S : S symmetric,
tr(J S) = 0} with J = diag(1, 1, 1, -1), nine exact coordinates; the holonomy SnapPy's polished one at 200 bits;
ranks by mpmath's SVD with the gap reported (the smallest kept and the largest dropped singular value, relative)."""
import sys, json, pathlib
import mpmath as mp
import snappy
mp.mp.dps = 60
HERE = pathlib.Path(__file__).resolve().parent
J = mp.diag([1, 1, 1, -1])
OFF = [(i, j) for i in range(4) for j in range(i + 1, 4)]

def basis():
    B = []
    for i, j in OFF:
        S = mp.zeros(4, 4); S[i, j] = 1; S[j, i] = 1; B.append(J * S)
    for d in ([1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, 1]):
        B.append(J * mp.diag(d))
    return B
VB = basis()
def coords(X):
    S = J * X
    a = S[0, 0]; b = S[1, 1] + a; c = S[3, 3]
    return [S[i, j] for i, j in OFF] + [a, b, c]
for k, b in enumerate(VB):                                   # the coordinate map inverts the basis exactly
    v = coords(b); assert all(abs(v[i] - (1 if i == k else 0)) < mp.mpf(10) ** -50 for i in range(9))

SIG = [mp.matrix([[0, 1], [1, 0]]), mp.matrix([[0, -1j], [1j, 0]]), mp.matrix([[1, 0], [0, -1]]), mp.eye(2)]
def so31(A):
    Ah = A.H; R = mp.zeros(4, 4)
    for j, Bj in enumerate(SIG):
        Y = A * Bj * Ah
        for i, Ci in enumerate(SIG):
            R[i, j] = mp.re((Ci * Y)[0, 0] + (Ci * Y)[1, 1]) / 2
    return R
def ad(R):
    Ri = J * R.T * J
    M = mp.zeros(9, 9)
    for k, b in enumerate(VB):
        c = coords(R * b * Ri)
        for i in range(9): M[i, k] = c[i]
    return M
def fox(word, gens, mats, inv):
    g = len(gens); D = mp.zeros(9, 9 * g); P = mp.eye(9)
    for ch in word:
        k = gens.index(ch.lower())
        if ch.islower():
            for a in range(9):
                for b in range(9): D[a, 9 * k + b] += P[a, b]
            P = P * mats[k]
        else:
            P = P * inv[k]
            for a in range(9):
                for b in range(9): D[a, 9 * k + b] -= P[a, b]
    return D, P
def vstack(Ms):
    rows = sum(M.rows for M in Ms); out = mp.zeros(rows, Ms[0].cols); r = 0
    for M in Ms:
        for i in range(M.rows):
            for j in range(M.cols): out[r + i, j] = M[i, j]
        r += M.rows
    return out
def hstack(A, B):
    out = mp.zeros(A.rows, A.cols + B.cols)
    for i in range(A.rows):
        for j in range(A.cols): out[i, j] = A[i, j]
        for j in range(B.cols): out[i, A.cols + j] = B[i, j]
    return out
def rank(A, cut=mp.mpf(10) ** -35):
    s = sorted(mp.svd_r(A, compute_uv=False), reverse=True)
    top = s[0] if s else 1
    r = sum(1 for x in s if x > cut * top)
    kept = float(s[r - 1] / top) if r else None; dropped = float(s[r] / top) if r < len(s) else None
    return r, kept, dropped
def num(z): return mp.mpc(mp.mpf(str(z.real())), mp.mpf(str(z.imag())))
def rigidity(name):
    M = snappy.Manifold(name); G = M.fundamental_group(); gens = G.generators(); g = len(gens)
    H = M.polished_holonomy(bits_prec=200, lift_to_SL2=False)
    mats = []
    for x in gens:
        A = H.SL2C(x); mats.append(ad(so31(mp.matrix([[num(A[0, 0]), num(A[0, 1])], [num(A[1, 0]), num(A[1, 1])]]))))
    inv = [m ** -1 for m in mats]
    rels = G.relators()
    Jac = vstack([fox(r, gens, mats, inv)[0] for r in rels]) if rels else mp.zeros(1, 9 * g)
    rJ = rank(Jac); dimZ = 9 * g - rJ[0]
    rB = rank(vstack([m - mp.eye(9) for m in mats])); h1 = dimZ - rB[0]
    m, l = G.peripheral_curves()[0]
    Fm, Pm = fox(m, gens, mats, inv); Fl, Pl = fox(l, gens, mats, inv)
    Sys = vstack([hstack(Jac, mp.zeros(Jac.rows, 9)), hstack(Fm, -(Pm - mp.eye(9))), hstack(Fl, -(Pl - mp.eye(9)))])
    rS = rank(Sys); dimS = 9 * g + 9 - rS[0]
    rP = rank(vstack([Pm - mp.eye(9), Pl - mp.eye(9)])); vP = 9 - rP[0]
    ker = dimS - 9 - vP
    gaps = [x for t in (rJ, rB, rS, rP) for x in t[1:]]
    return dict(name=name, gens=g, h1_v=h1, dim_vP=vP, kernel=ker, rigid=(ker == 0),
                min_kept=min(x for x in gaps[0::2] if x is not None),
                max_dropped=max((x for x in gaps[1::2] if x is not None), default=0.0))
if __name__ == "__main__":
    if sys.argv[1] == "controls":
        for nm in ("m004", "m003", "b++LLRR", "b++RRL", "b++LLLLLR", "b++LLRLRRLLRRLR"):
            print(rigidity(nm), flush=True)
    else:
        lo, hi = int(sys.argv[2]), int(sys.argv[3])
        d = json.load(open(HERE / "main_b1523_mirror.json"))["manifolds"][lo:hi]
        out = []
        for r in d:
            rec = rigidity("b+" + r["states"][0]); rec["state"] = r["states"][0]; out.append(rec)
            print(rec["state"], rec["h1_v"], rec["kernel"], "%.1e %.1e" % (rec["min_kept"], rec["max_dropped"]), flush=True)
        json.dump(out, open(HERE / f"rigidity_mp_{lo}_{hi}.json", "w"), indent=0)
