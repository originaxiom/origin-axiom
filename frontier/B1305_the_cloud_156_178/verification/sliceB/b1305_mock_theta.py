"""B1305 slice B, Q3 -- the two mock-theta growth rates with an own estimator (DESIGN_B sealed fa793cf2).
F_0(q) = sum_n q^{n^2}/(q^{n+1};q)_n (Ramanujan, order 7; GM eq. 175 = Zhat_0(-Sigma(2,3,7)) up to -q^{-1/2}) and
chi_0(q) = sum_n q^n/(q^{n+1};q)_n (order 5; Gukov-Jagadale's Sigma(2,3,5) series). Exact integers for the first coefficients
(controls against the printed series), float64 to N = 20000 for the growth fit log a_n = A sqrt(n) + B log n + C on the upper half,
c_eff = 3A^2/(2 pi^2); the estimator is calibrated on 1/(q;q)_inf (must give 1) and on Rogers-Ramanujan G(q) (must give 2/5)."""
import json, math, sys
import numpy as np
fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok: fails.append(label)
def mul_1_minus(a, j):            # a *= (1 - q^j)
    if j < len(a): a[j:] -= a[:-j].copy()
def div_1_minus(a, j):            # a /= (1 - q^j)   via cumulative sums along residue classes
    n = len(a)
    if j >= n: return
    pad = (-n) % j
    b = np.concatenate([a, np.zeros(pad)]).reshape(-1, j)
    np.cumsum(b, axis=0, out=b); a[:] = b.reshape(-1)[:n]
def series(kind, N, dtype=float):
    """T_n = q^{e(n)}/(q^{n+1};q)_n  with  T_n = T_{n-1} * q^{e(n)-e(n-1)} * (1-q^n) / ((1-q^{2n-1})(1-q^{2n}))"""
    tot = np.zeros(N, dtype=dtype); T = np.zeros(N, dtype=dtype); T[0] = 1   # T_0 = 1
    tot += T; n = 0
    while True:
        n += 1
        shift = (2 * n - 1) if kind == "F0" else 1
        if shift >= N: break
        T2 = np.zeros(N, dtype=dtype); T2[shift:] = T[:-shift]; T = T2
        mul_1_minus(T, n); div_1_minus(T, 2 * n - 1); div_1_minus(T, 2 * n)
        if not T.any(): break
        tot += T
        if kind == "chi0" and n >= N: break
    return tot
def exact_series(kind, N):
    """the same recurrence in exact Python integers (lists): no floating-point cancellation across the chained steps"""
    tot = [0] * N; T = [0] * N; T[0] = 1
    for i in range(N): tot[i] += T[i]
    n = 0
    while True:
        n += 1
        shift = (2 * n - 1) if kind == "F0" else 1
        if shift >= N or (kind == "chi0" and n >= N): break
        T = [0] * shift + T[:N - shift]
        j = n
        if j < N:
            for i in range(N - 1, j - 1, -1): T[i] -= T[i - j]          # * (1 - q^n)
        for j in (2 * n - 1, 2 * n):                                     # / (1 - q^j)
            if j < N:
                for i in range(j, N): T[i] += T[i - j]
        if not any(T): break
        for i in range(N): tot[i] += T[i]
    return tot
def exact_first(kind, N=60): return exact_series(kind, N)
def partitions(N):
    a = np.zeros(N); a[0] = 1
    for j in range(1, N): div_1_minus(a, j)
    return a
def rogers_ramanujan_G(N):      # sum q^{n^2}/(q;q)_n
    tot = np.zeros(N); T = np.zeros(N); T[0] = 1; tot += T; n = 0
    while True:
        n += 1; s = 2 * n - 1
        if s >= N: break
        T2 = np.zeros(N); T2[s:] = T[:-s]; T = T2; div_1_minus(T, n); tot += T
    return tot
def fit(a, lo_frac=0.5):
    n = np.arange(len(a)); m = (n >= lo_frac * len(a)) & (a > 0)
    X = np.stack([np.sqrt(n[m]), np.log(n[m]), np.ones(m.sum())], 1); y = np.log(a[m])
    A, B, C = np.linalg.lstsq(X, y, rcond=None)[0]
    return 3 * A * A / (2 * math.pi ** 2), B
N = 20000
print("=== exact controls (first coefficients) ===")
f0 = exact_first("F0"); c0 = exact_first("chi0")
print("  F_0 :", f0[:14]); print("  chi_0:", c0[:12])
check("F_0's first 14 coefficients are GM eq. (175)'s 1,1,0,1,1,1,0,2,1,2,1,2,1,3", f0[:14] == [1, 1, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2, 1, 3])
check("chi_0's first 12 coefficients are 1,1,1,2,1,3,2,3,3,5,3,6 (the cloud's control, GJ eq. 33)", c0[:12] == [1, 1, 1, 2, 1, 3, 2, 3, 3, 5, 3, 6])
print("=== calibration of the estimator ===")
cp, Bp = fit(partitions(N)); cg, Bg = fit(rogers_ramanujan_G(N))
print(f"  1/(q;q)_inf: c_eff = {cp:.5f} (B = {Bp:.3f})   Rogers-Ramanujan G: c_eff = {cg:.5f} (B = {Bg:.3f})")
check("calibration: 1/(q;q)_inf -> 1 +- 0.001 and G(q) -> 2/5 +- 0.001", abs(cp - 1) < 1e-3 and abs(cg - 0.4) < 1e-3)
print("=== the two mock theta functions ===")
F = np.array([float(x) for x in exact_series("F0", N)]); NX = 6000; X = np.array([float(x) for x in exact_series("chi0", NX)])   # chi_0 exact to the cloud's N = 6000
cF, BF = fit(F); cX, BX = fit(X)
print(f"  F_0 (order 7):  c_eff = {cF:.6f}   1/7 = {1/7:.6f}   B = {BF:.3f}")
print(f"  chi_0 (order 5): c_eff = {cX:.6f}   1/5 = {1/5:.6f}   B = {BX:.3f}")
check("c_eff(F_0) = 1/7 +- 0.0005 and c_eff(chi_0) = 1/5 +- 0.0005, B = -1/2 +- 0.01", abs(cF - 1 / 7) < 5e-4 and abs(cX - 0.2) < 5e-4 and abs(BF + 0.5) < 0.01 and abs(BX + 0.5) < 0.01)
json.dump(dict(F0_first=f0[:14], chi0_first=c0[:12], calib=dict(partitions=cp, RR=cg), F0=dict(c_eff=cF, B=BF, N=N), chi0=dict(c_eff=cX, B=BX, N=NX), fails=fails), open("b1305_mock_theta.json", "w"), indent=1)
print("Q3:", "PASS" if not fails else f"FAIL ({len(fails)})"); sys.exit(0 if not fails else 1)
