"""High-precision (mirrors b238.su3_data / pairing_law_scan.py odd_form) build
of the odd hearing form B_odd at kappa=5 (k=2) and kappa=10 (k=7), done with
mpmath at 80 digits so the printed 50-digit values are trustworthy.
"""
import itertools
import mpmath as mp

mp.mp.dps = 80


def su3_data(k):
    N = 3
    kap = k + 3
    weights = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    n = len(weights)

    def Lvec(w):
        return [mp.mpf(w[0] + w[1] + 2), mp.mpf(w[1] + 1), mp.mpf(0)]

    def ip(u, v):
        s = sum(u[i] * v[i] for i in range(3))
        su = sum(u)
        sv = sum(v)
        return s - su * sv / 3

    perms = list(itertools.permutations(range(3)))

    def sgn(p):
        inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
        return (-1) ** inv

    S = mp.matrix(n, n)
    for i, wl in enumerate(weights):
        Ll = Lvec(wl)
        for j, wm in enumerate(weights):
            Lm = Lvec(wm)
            tot = mp.mpc(0)
            for p in perms:
                Lp = [Ll[p[0]], Ll[p[1]], Ll[p[2]]]
                val = ip(Lp, Lm)
                tot += sgn(p) * mp.e ** (-2j * mp.pi * val / kap)
            S[i, j] = tot
    # normalize like the numpy code: S /= sqrt(sum_i |S[i,0]|^2)
    norm = mp.sqrt(sum(abs(S[i, 0]) ** 2 for i in range(n)))
    for i in range(n):
        for j in range(n):
            S[i, j] = S[i, j] / norm

    c = mp.mpf(k * 8) / (k + 3)
    Tdiag = []
    for (a, b) in weights:
        expo = ((mp.mpf(2) / 3) * (a * a + a * b + b * b) + 2 * (a + b)) / (2 * kap) - c / 24
        Tdiag.append(mp.e ** (2j * mp.pi * expo))
    T = mp.matrix(n, n)
    for i in range(n):
        T[i, i] = Tdiag[i]
    return weights, S, T, c


def odd_form(k):
    w, S, T, c = su3_data(k)
    n = len(w)
    Cm = mp.matrix(n, n)
    for i, wt in enumerate(w):
        Cm[w.index((wt[1], wt[0])), i] = 1

    Si = S ** -1
    Ti = T ** -1
    WRL = T * (Si * Ti * S)

    # commutation check
    comm = Cm * WRL - WRL * Cm
    maxc = max(abs(comm[i, j]) for i in range(n) for j in range(n))

    pairs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    m = len(pairs)
    U = mp.matrix(n, m)
    for j, (a, b) in enumerate(pairs):
        U[w.index((a, b)), j] = 1 / mp.sqrt(2)
        U[w.index((b, a)), j] = -1 / mp.sqrt(2)

    UT = U.T
    B = -(UT * WRL * U)
    return w, pairs, B, maxc


def fmt(z, d=50):
    re = mp.nstr(z.real, d, strip_zeros=False)
    im = mp.nstr(z.imag, d, strip_zeros=False)
    sign = '+' if z.imag >= 0 else '-'
    return f"{re} {sign} {mp.nstr(abs(z.imag), d, strip_zeros=False)}j"


if __name__ == "__main__":
    print("=" * 100)
    print("KAPPA = 5  (k=2)  ---  B_odd 2x2 exact (80dps internal, 50 printed)")
    print("=" * 100)
    w2, pairs2, B2, maxc2 = odd_form(2)
    print("weights:", w2)
    print("pairs (odd basis order):", pairs2)
    print(f"[Cm,WRL] max abs entry = {mp.nstr(maxc2, 10)}")
    for i in range(2):
        for j in range(2):
            print(f"B_odd[{i},{j}] = {fmt(B2[i,j])}")

    print()
    trace = B2[0, 0] + B2[1, 1]
    det = B2[0, 0] * B2[1, 1] - B2[0, 1] * B2[1, 0]
    print(f"trace = {fmt(trace)}")
    print(f"det   = {fmt(det)}")

    # unitarity check: B B^† =? I
    Bdag = mp.matrix(2, 2)
    for i in range(2):
        for j in range(2):
            Bdag[i, j] = mp.conj(B2[j, i])
    P = B2 * Bdag
    print("\nB_odd @ B_odd^dagger =")
    for i in range(2):
        for j in range(2):
            print(f"  [{i},{j}] = {fmt(P[i,j], 30)}")

    # symmetric?
    print(f"\nB_odd symmetric (B[0,1]==B[1,0])? diff = {fmt(B2[0,1]-B2[1,0],30)}")
    print(f"B_odd Hermitian? B[0,1] vs conj(B[1,0]) diff = {fmt(B2[0,1]-mp.conj(B2[1,0]),30)}")
    print(f"B_odd normal (BB^dag == B^dag B)? ", end="")
    Q = Bdag * B2
    diffs = [abs(P[i,j]-Q[i,j]) for i in range(2) for j in range(2)]
    print(mp.nstr(max(diffs), 10))

    # eigenvalues/eigenvectors exact via mpmath
    E, V = mp.eig(B2)
    print("\nEigenvalues:")
    for e in E:
        print(" ", fmt(e))
        ang = mp.arg(e)
        print("    arg/pi =", mp.nstr(ang/mp.pi, 30), "  |lambda| =", mp.nstr(abs(e), 30))

    print("\nEigenvector matrix V (columns = eigenvectors, un-normalized as returned):")
    for i in range(2):
        for j in range(2):
            print(f"  V[{i},{j}] = {fmt(V[i,j])}")

    # normalize eigenvectors to unit norm (standard convention)
    Vn = mp.matrix(2, 2)
    for j in range(2):
        col = [V[i, j] for i in range(2)]
        nrm = mp.sqrt(sum(abs(c) ** 2 for c in col))
        for i in range(2):
            Vn[i, j] = V[i, j] / nrm
    print("\nNormalized eigenvector matrix V (unit columns):")
    for i in range(2):
        for j in range(2):
            print(f"  V[{i},{j}] = {fmt(Vn[i,j])}")
    print("\n|V_11|^2 and |V_21|^2 (col 0), |V_12|^2,|V_22|^2 (col1):")
    for i in range(2):
        for j in range(2):
            val = abs(Vn[i, j]) ** 2
            print(f"  |V[{i},{j}]|^2 = {mp.nstr(val, 50)}")

    print("=" * 100)
    print("KAPPA = 10 (k=7) --- full odd hearing form dimension check + golden subblock")
    print("=" * 100)
    w7, pairs7, B7, maxc7 = odd_form(7)
    n7 = len(w7)
    m7 = len(pairs7)
    print(f"n (weights) = {n7}, dim_odd (pairs) = {m7}  <-- ACTUAL, per pairing_law_scan.py construction")
    print("pairs list:", pairs7)
    print(f"[Cm,WRL] max abs entry = {mp.nstr(maxc7, 10)}")

    trace7 = sum(B7[i, i] for i in range(m7))
    print(f"trace(B_odd, kappa=10) = {fmt(trace7)}")

    E7, V7 = mp.eig(B7)
    print(f"\nfull spectrum ({m7} eigenvalues), |lambda|^2:")
    for e in sorted(E7, key=lambda z: (mp.re(z), mp.im(z))):
        print(f"  lambda = {fmt(e,30)}   |lambda|^2 = {mp.nstr(abs(e)**2,40)}   arg/pi = {mp.nstr(mp.arg(e)/mp.pi,20)}")

    # the golden 2x2 sub-block: same pair-basis directions (1,0)-(0,1) and (2,0)-(0,2)
    # embedded in the kappa=10 weight space (the naive V2 test's basis)
    idx01 = pairs7.index((0, 1))
    idx02 = pairs7.index((0, 2))
    print(f"\nindices of pairs (0,1) and (0,2) within the kappa=10 odd-basis: {idx01}, {idx02}")
    sub = mp.matrix(2, 2)
    sub[0, 0] = B7[idx01, idx01]
    sub[0, 1] = B7[idx01, idx02]
    sub[1, 0] = B7[idx02, idx01]
    sub[1, 1] = B7[idx02, idx02]
    print("golden 2x2 sub-block (extracted from the full 16x16 B_odd at the (0,1),(0,2) pair rows/cols):")
    for i in range(2):
        for j in range(2):
            print(f"  sub[{i},{j}] = {fmt(sub[i,j])}")
    Es, Vs = mp.eig(sub)
    print("sub-block eigenvalues:")
    for e in Es:
        print("  ", fmt(e, 30), " |lambda|^2=", mp.nstr(abs(e)**2, 30))
