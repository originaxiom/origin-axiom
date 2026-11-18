"""agy-002's card A2-X1 (its branch agy-002/verify at 55f72ee3f; its script verify_a2_x1.py read as text, not run), the
statements of it that main had not computed, on main's own construction of frame D1 (the flux-(3, 3, 6) three-point
function of physical_c8_tick_higgs.py's K6, 80 digits; the mark (2/5, 4/5), Re tau = 0.13, the unshifted lift).

X1  the coherent vector h* = (1/sqrt 2, e^(i pi/12)/2, 0, 0, 0, e^(i pi/12)/2): its mixing classes at height 8 over the
    24 points of order 5 and the four lifts, with main's classifier (sm_c18_to_c21.py, C4), and how many of the 24 have
    s3 > 1e-12 s1 in each sector (the seat: lifts (0,0), (0,1): 0, 0, 0, 24 with 10 up and 15 down above the cutoff;
    lifts (1,0), (1,1): 0, 4, 0, 20).
X2  P-873's question 3, the seat's answer: |V(h*)| at the mark tends, as Im tau grows, to the matrix with rows
    (1/sqrt 2, 0, 1/sqrt 2), (1/sqrt 2, 0, 1/sqrt 2), (0, 1, 0); main computes |V| at heights 8, 14 and 24 and its
    distance to that matrix under the best ordering of rows and columns, and says which ordering.
X3  the seat's law under tau + 5 for this frame: every entry (i, j, m) of the three-point function, at xi = Delta (a tau + b)/2,
    is multiplied by exp(5 pi i c^2/6 + pi i c Delta (5a) + 3 pi i Delta^2 (5a)^2/10), c = i - j + 3m; and the fifth-root
    part of that factor is trivial in the up sector at all 24 points and not at the 20 points with 5a not divisible by 5
    in the down and lepton sectors.
X4  the invariants on the ground plane: real polynomials invariant under the common phase, the transport and the tick, by
    degree, to degree 24 (the seat: 1, 2, 2, 3, 3, 4, 6 at 2 to 14, and 15 at 24, against 7 for N and Delta^2 alone);
    numerically on main's modes, and exactly by counting N^a Delta^b w^k with k a multiple of 6 and the tick's sign.
X5  the smaller items: the Hermitian forms on E that the tick keeps and that it reverses (the seat: one dimension each);
    the two lifts of the tick, T6 S6 K and P T6 S6 K, differ by an operator of norm exactly 2 on the parity's odd plane
    (P commutes with T6 and S6 and is real, so the difference there is (1 - P) = 2); where v- is top-aligned at
    height 8 (the seat: the four points with a = 0); and h*'s ratio exponents at the mark from heights 6 -> 8 and
    8 -> 10, the columns of the seat's table that main's K6 (8 -> 11, 11 -> 14) does not have.
X6  the seat's M_lepton(h) = e^(i phi) M_down(h)^T at the mark, for h* and for v+ (heights 8 and 14).
X7  its status page's statements about main's record: B1957's four agy-002 lanes at main's 4921ee923 (files 11, 12, 18,
    13; statements 500, 207, 271, 189; none pending), and its twenty deliveries before 2026-11-15 each named in a
    harvest-ledger row between 1705 and 1828 (main's ledger at 4921ee923).
"""
import sys, itertools, functools, json, re, subprocess
import numpy as np, mpmath as mp
print = functools.partial(print, flush=True)

mp.mp.dps = 80; DELTA = {"up": 5, "down": -1, "lepton": -9}
def Ymp(tau, xi):
    y = mp.im(tau); pre = (3 * y) ** mp.mpf("0.25"); res = {}
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                kk = (i + j + 1 + 3 * m) % 6; a = mp.mpf((i - j + 3 * m) % 6) / 6; n0 = mp.nint(a + mp.im(xi) / y); s = mp.mpf(0)
                for n_ in range(-25, 26):
                    n = n_ + a - n0; s += mp.exp(6j * mp.pi * xi * mp.im(xi) / y + 6j * mp.pi * n ** 2 * tau + 12j * mp.pi * n * xi)
                res[(i, j, kk)] = pre * mp.exp(2j * mp.pi * kk / 6) * s
    return res
def Msec(tau, a, b, sec, h):
    xi = mp.mpf(DELTA[sec]) * (mp.mpf(a) * tau + mp.mpf(b)) / 2; Y = Ymp(tau, xi)
    return mp.matrix([[sum(Y.get((i, j, kk), 0) * h[kk] for kk in range(6)) for j in range(3)] for i in range(3)])
def left(M):
    U, S, Vh = mp.svd_c(M); order = sorted(range(3), key=lambda i: -abs(S[i])); return [mp.matrix([U[r, i] for r in range(3)]) for i in order], [abs(S[i]) for i in order]
e12 = mp.exp(1j * mp.pi / 12); hstar = [1 / mp.sqrt(2), e12 / 2, mp.mpc(0), mp.mpc(0), mp.mpc(0), e12 / 2]
def Vmod(tau, a, b, h):
    Uu, Su = left(Msec(tau, a, b, "up", h)); Ud, Sd = left(Msec(tau, a, b, "down", h))
    return [[abs(sum(mp.conj(Uu[r][t]) * Ud[c][t] for t in range(3))) for c in range(3)] for r in range(3)], Su, Sd

# ---- X1
print("X1: h*'s mixing classes at height 8 (24 points of order 5, four lifts; main's classifier of sm_c18_to_c21.py, C4):")
for lift in itertools.product((0, 1), repeat=2):
    cnt = {"aligned": 0, "top-aligned": 0, "permutation": 0, "other": 0}; fu = fd = 0; tops = []
    for i5 in range(5):
        for j5 in range(5):
            if (i5, j5) == (0, 0): continue
            a, b = mp.mpf(i5) / 5 + lift[1], mp.mpf(j5) / 5 + lift[0]; tau = mp.mpc("0.13", 8)
            Vm, Su, Sd = Vmod(tau, a, b, hstar); Vm = [[float(x) for x in row] for row in Vm]
            fu += Su[2] > mp.mpf("1e-12") * Su[0]; fd += Sd[2] > mp.mpf("1e-12") * Sd[0]
            if Vm[0][0] > 0.99 and all(Vm[d][d] > 0.9 for d in range(3)): cnt["aligned"] += 1
            elif Vm[0][0] > 0.99: cnt["top-aligned"] += 1; tops.append((i5, j5))
            elif all(max(row) > 0.99 for row in Vm): cnt["permutation"] += 1
            else: cnt["other"] += 1
    print("  lift %s: %s; s3 > 1e-12 s1 at %d of 24 points (up), %d (down); top-aligned at (5a, 5b) = %s" % (lift, cnt, fu, fd, tops))

# ---- X2
r2 = 1 / np.sqrt(2); claim = np.array([[r2, 0, r2], [r2, 0, r2], [0, 1, 0]])
print("X2: |V(h*)| at the mark (2/5, 4/5), rows the up sector's left singular vectors and columns the down sector's, each by decreasing singular value:")
for y in (8, 14, 24):
    Vm, Su, Sd = Vmod(mp.mpc("0.13", y), mp.mpf(2) / 5, mp.mpf(4) / 5, hstar); A = np.array([[float(x) for x in row] for row in Vm])
    best = min((float(np.abs(A[list(p)][:, list(q)] - claim).max()), p, q) for p in itertools.permutations(range(3)) for q in itertools.permutations(range(3)))
    print("  height %2d: |V| = %s; s3/s1 up %.2e, down %.2e; distance to the seat's limit %.2e with rows in the order %s and columns %s"
          % (y, np.round(A, 6).tolist(), float(Su[2] / Su[0]), float(Sd[2] / Sd[0]), best[0], best[1], best[2]))

# ---- X3
print("X3: under tau + 5 at the 24 points (unshifted lift; heights 1.3 and 2.1):")
z5 = lambda x: x
for sec in ("up", "down", "lepton"):
    worst = mp.mpf(0); obstructed = 0; D = DELTA[sec]
    for i5 in range(5):
        for j5 in range(5):
            if (i5, j5) == (0, 0): continue
            a, b = mp.mpf(i5) / 5, mp.mpf(j5) / 5; ob = False
            for tau in (mp.mpc("0.13", "1.3"), mp.mpc("-0.21", "2.1")):
                xi0 = D * (a * tau + b) / 2; xi1 = D * (a * (tau + 5) + b) / 2; Y0, Y1 = Ymp(tau, xi0), Ymp(tau + 5, xi1)
                for i in range(3):
                    for j in range(3):
                        for m in (0, 1):
                            kk = (i + j + 1 + 3 * m) % 6; c = i - j + 3 * m; r = Y1[(i, j, kk)] / Y0[(i, j, kk)]
                            law = mp.exp(5j * mp.pi * c ** 2 / 6 + 1j * mp.pi * c * D * (5 * a) + 3j * mp.pi * D ** 2 * (5 * a) ** 2 / 10)
                            worst = max(worst, abs(r / law - 1)); ob |= abs(r ** 12 - 1) > mp.mpf("1e-40")
            obstructed += ob
    print("  %-6s: |ratio / law - 1| at most %s over 18 entries x 24 points x 2 moduli; points where a fifth root remains (ratio^12 != 1): %d of 24" % (sec, mp.nstr(worst, 3), obstructed))

# ---- X4
k6 = np.arange(6); T6 = np.diag(np.exp(1j * np.pi * k6 ** 2 / 6)); F6 = np.exp(-2j * np.pi * np.outer(k6, k6) / 6) / np.sqrt(6); S6 = np.exp(-1j * np.pi / 4) * F6
inv = np.linalg.inv; U = T6 @ inv(S6) @ inv(T6) @ S6; ev, V = np.linalg.eig(U); ph = np.angle(ev) / np.pi
vp = V[:, int(np.argmin(abs(ph - 1 / 6)))]; vm = V[:, int(np.argmin(abs(ph + 1 / 6)))]; vp, vm = vp / np.linalg.norm(vp), vm / np.linalg.norm(vm)
A = T6 @ S6; B = [vp, vm]
UE = np.array([[np.vdot(B[r], U @ B[c]) for c in range(2)] for r in range(2)]); Sg = np.array([[np.vdot(B[r], A @ B[c].conj()) for c in range(2)] for r in range(2)])
rng = np.random.default_rng(11)
def invariants(n):
    mons = [(a, n - a, cc, n - cc) for a in range(n + 1) for cc in range(n + 1)]; half = [m for m in mons if (m[0], m[1]) >= (m[2], m[3])]
    def feats(z):
        out = []
        for a, b, cc, d in half:
            mm = z[0] ** a * z[1] ** b * np.conj(z[0]) ** cc * np.conj(z[1]) ** d; out.append(mm.real)
            if (a, b) != (cc, d): out.append(mm.imag)
        return np.array(out)
    rows = []
    for _ in range(4 * len(mons)):
        z = rng.normal(size=2) + 1j * rng.normal(size=2); z /= np.linalg.norm(z)
        rows.append(feats(UE @ z) - feats(z)); rows.append(feats(Sg @ z.conj()) - feats(z))
    sv = np.linalg.svd(np.array(rows), compute_uv=False); return int(len(feats(np.ones(2))) - np.sum(sv > 1e-9 * sv[0]))
# exactly: on E, with N, Delta and w = z+ conj(z-), a basis of the polynomials of degree 2n is N^a Delta^b w^k and N^a Delta^b conj(w)^k, a + b + k = n;
# the transport multiplies w by e^(i pi/3), so k is a multiple of 6; the tick sends Delta to -Delta and w to e^(i pi/6) w, so (-1)^b e^(i pi k/6) = 1
wU = UE[0, 0] * np.conj(UE[1, 1]); wS = Sg[0, 1] * np.conj(Sg[1, 0])            # how w = z+ conj(z-) moves under U and under the tick
def exact(n):
    tot = 0
    for kk in range(0, n + 1, 6):
        for b in range(0, n - kk + 1):
            if (-1) ** b * (-1) ** (kk // 6) == 1: tot += 1 if kk == 0 else 2
    return tot
dims = {2 * n: invariants(n) for n in (1, 2, 3, 4, 5, 6, 7, 12)}; ex = {2 * n: exact(n) for n in (1, 2, 3, 4, 5, 6, 7, 12)}; plain = {2 * n: n // 2 + 1 for n in (1, 2, 3, 4, 5, 6, 7, 12)}
print("X4: under the transport w moves by e^(i pi %.4f), under the tick by e^(i pi %.4f) (Delta to -Delta); invariant real polynomials on E by degree, numerically: %s; exactly: %s; in N and Delta^2 alone: %s"
      % (np.angle(wU) / np.pi, np.angle(wS) / np.pi, dims, ex, plain))

# ---- X5
P = np.zeros((6, 6)); P[(-k6) % 6, k6] = 1
herm = [np.array([[1, 0], [0, 0]], complex), np.array([[0, 0], [0, 1]], complex), np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex)]
conjH = lambda H: Sg @ H.conj() @ inv(Sg)
vec = lambda H: np.concatenate([H.real.flatten(), H.imag.flatten()])
dim_even = 4 - np.linalg.matrix_rank(np.array([vec(conjH(H) - H) for H in herm]).T, tol=1e-9)
dim_odd = 4 - np.linalg.matrix_rank(np.array([vec(conjH(H) + H) for H in herm]).T, tol=1e-9)
oddv = [V[:, i] for i in range(6) if abs(np.vdot(V[:, i], P @ V[:, i]) + 1) < 1e-9]; Q, _ = np.linalg.qr(np.array(oddv).T)
D = (A - P @ A)                                   # the two lifts differ by (1 - P) T6 S6, applied after conjugation
on_odd = np.linalg.svd(Q.conj().T @ D @ Q.conj(), compute_uv=False)
print("X5: Hermitian forms on E kept by the tick: dimension %d; reversed by it: dimension %d; |[P, T6]| = %.1e, |[P, S6]| = %.1e; on the parity's odd plane (dimension %d) the two lifts of the tick differ by an operator with singular values %s"
      % (dim_even, dim_odd, np.abs(P @ T6 - T6 @ P).max(), np.abs(P @ S6 - S6 @ P).max(), len(oddv), np.round(on_odd, 12).tolist()))
vmm = [mp.mpc(complex(x)) for x in vm]; tops = []
for i5 in range(5):
    for j5 in range(5):
        if (i5, j5) == (0, 0): continue
        Vm, Su, Sd = Vmod(mp.mpc("0.13", 8), mp.mpf(i5) / 5, mp.mpf(j5) / 5, vmm)
        if float(Vm[0][0]) > 0.99 and not all(float(Vm[d][d]) > 0.9 for d in range(3)): tops.append((i5, j5))
print("X5: v- is top-aligned at height 8 (unshifted lift) at (5a, 5b) = %s" % tops)
for sec in ("up", "down"):
    L = {y: sorted((abs(x) for x in mp.svd_c(Msec(mp.mpc("0.13", y), mp.mpf(2) / 5, mp.mpf(4) / 5, sec, hstar), compute_uv=False)), reverse=True) for y in (6, 8, 10)}
    E = lambda y0, y1, i: float(-(mp.log(L[y1][i] / L[y1][0]) - mp.log(L[y0][i] / L[y0][0])) / (mp.pi * (y1 - y0)))
    print("X5: h* %-4s at the mark: E2 %+.4f (6 -> 8), %+.4f (8 -> 10); E3 %+.4f, %+.4f" % (sec, E(6, 8, 1), E(8, 10, 1), E(6, 8, 2), E(8, 10, 2)))

# ---- X6
for name, h in (("h*", hstar), ("v+", [mp.mpc(complex(x)) for x in vp])):
    for y in (8, 14):
        tau = mp.mpc("0.13", y); Md = Msec(tau, mp.mpf(2) / 5, mp.mpf(4) / 5, "down", h); Ml = Msec(tau, mp.mpf(2) / 5, mp.mpf(4) / 5, "lepton", h); MdT = Md.T
        c = sum(mp.conj(MdT[i, j]) * Ml[i, j] for i in range(3) for j in range(3)) / sum(abs(MdT[i, j]) ** 2 for i in range(3) for j in range(3))
        res = max(abs(Ml[i, j] - c * MdT[i, j]) for i in range(3) for j in range(3)) / max(abs(Ml[i, j]) for i in range(3) for j in range(3))
        print("X6: %s, height %d: |M_lepton - c M_down^T| / |M_lepton| = %s with |c| = %s" % (name, y, mp.nstr(res, 3), mp.nstr(abs(c), 12)))

# ---- X7
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
summ = json.loads(git("show", "4921ee923:frontier/B1957_the_seats_claims_register/verification/SUMMARY.json"))["lanes"]
print("X7: B1957 at main's 4921ee923, agy-002's lanes (files, statements, pending): %s" % {k: (v["files"], v["statements"], v["PENDING"]) for k, v in summ.items() if k.startswith("agy-002")})
rows = {}
for l in git("show", "4921ee923:docs/HARVEST_LEDGER.md").split("\n"):
    m = re.match(r"\| (\d+) \| ([^|]+) \|", l)
    if m and 1705 <= int(m.group(1)) <= 1828: rows[int(m.group(1))] = l
status = git("show", "55f72ee3f:relays/STATUS_AGY-002.md").split("\n")
items = [(int(m.group(1)), m.group(2)) for l in status for m in [re.match(r"(\d+)\. \*\*`(A2-[A-Za-z0-9-]+)`", l)] if m and int(m.group(1)) <= 20]
where = {}
for n, card in items:
    key = card if not card.startswith("A2-S-R80") else ("R80a" if card.endswith("R80a") else "R80b parts 1 to 5")
    where[card] = [r for r, l in sorted(rows.items()) if key in l]
print("X7: its twenty deliveries before 2026-11-15 and the ledger rows (1705 to 1828) that name them: %s; without a row: %s" % (where, [c for c, r in where.items() if not r]))
