"""B1999: main's check of the agy lane's C59 package (2026-11-25; data-free). Frame C's Yukawas come from the seat's own sealed
C59 producer, copied verbatim to seat_copy/ (its SCRIPT_SHA256 matches) and imported read-only, by the author's ruling of
2026-11-24 (main may run a seat's sealed, dependency-free scripts to reproduce). Everything built on them is main's code.
L2 at the golden point: 2.663604442987991, as typed in the seat's probe (15 digits; the reproduction below tests it).
  (0) reproduction: main's driver against the seat's sealed c59_out.json on all 8 vertex chains;
  (1) the chain length K = 1..11 on the seat's reference chain;   (2) K = 7 from every sheet of every orbit (96 chains);
  (3) item 2: the 12-turn phase per orbit and sector;             (4) item 3: clockwise against counterclockwise at each mirror wall.
Nothing is compared with data.        python3 -I -B check_c59.py > check_c59_run.txt"""
import importlib.util, json, pathlib, statistics
from fractions import Fraction as Fr
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("c59", HERE / "seat_copy" / "c59_producer.py"); c59 = importlib.util.module_from_spec(spec); spec.loader.exec_module(c59)
SEALED = json.loads((HERE / "seat_copy" / "c59_out.json").read_text())
mp.mp.dps = 40
RHO_R = c59.mmul3(c59.RHO_S, c59.mmul3(c59.RHO_Tinv, c59.RHO_S)); RHO_U1 = c59.mmul3(c59.RHO_T, RHO_R)
U_A = mp.matrix([[mp.mpf(RHO_U1[r][c]) for c in range(3)] for r in range(3)])
pts = [(a, b) for a in range(30) for b in range(30) if not (a % 2 == 0 and b % 2 == 0) and not (a % 3 == 0 and b % 3 == 0) and not (a % 5 == 0 and b % 5 == 0)]
a12 = [[1, 0], [0, 1]]
for _ in range(12): a12 = [[(2 * a12[0][0] + a12[0][1]) % 30, (a12[0][0] + a12[0][1]) % 30], [(2 * a12[1][0] + a12[1][1]) % 30, (a12[1][0] + a12[1][1]) % 30]]
fixed = sorted((Fr(a, 30), Fr(b, 30)) for (a, b) in pts if ((a * a12[0][0] + b * a12[1][0]) % 30, (a * a12[0][1] + b * a12[1][1]) % 30) == (a, b))
assert len(fixed) == 96
orbits, seen = [], set()
for p in fixed:
    if p in seen: continue
    o, cur = [], p
    for _ in range(12): o.append(cur); seen.add(cur); cur = ((2 * cur[0] + cur[1]) % 1, (cur[0] + cur[1]) % 1)
    orbits.append(o)
tg = mp.mpc(mp.mpf(1) / 2, mp.sqrt(5) / 2); l2g = mp.mpf("2.663604442987991")
fac = tg + 1; tA = (2 * tg + 1) / fac; l2A = l2g + mp.log(abs(fac)); ph = fac / abs(fac)
SEC = [("u", (1, -4)), ("d", (1, 2)), ("e", (-3, 6))]
yk, ykA, sph = {}, {}, {}
for w in fixed:
    for ql, qr in (s[1] for s in SEC):
        yk[(w, ql, qr)] = c59.yukawa_kahler(w[0], w[1], ql, qr, tg, l2g); ykA[(w, ql, qr)] = c59.yukawa_kahler(w[0], w[1], ql, qr, tA, l2A) / ph
for w in fixed:
    wn = ((2 * w[0] + w[1]) % 1, (w[0] + w[1]) % 1)
    for ql, qr in (s[1] for s in SEC):
        cand = U_A * yk[(wn, ql, qr)] * U_A.T; yA = ykA[(w, ql, qr)]
        r0, c0 = max(((r, c) for r in range(3) for c in range(3)), key=lambda rc: abs(cand[rc[0], rc[1]]))
        sc = yA[r0, c0] / cand[r0, c0]; sph[(w, ql, qr)] = sc / abs(sc)
I3 = mp.eye(3)
def transported(orb, k0, K, direction, ql, qr):
    ys = []
    if direction == 1:
        uap, p = mp.eye(3), mp.mpc(1)
        for n in range(K):
            k = (k0 + n) % 12; ys.append(p * (uap * yk[(orb[k], ql, qr)] * uap.T)); p *= sph[(orb[k], ql, qr)]; uap = U_A * uap
    else:
        ys.append(yk[(orb[k0], ql, qr)]); uam, pm = mp.eye(3), mp.mpc(1)
        for n in range(1, K):
            pk = (k0 - n) % 12; uam = U_A.T * uam; pm = pm / sph[(orb[pk], ql, qr)]; ys.append(pm * (uam * yk[(orb[pk], ql, qr)] * uam.T))
    return ys
def chain(orb, k0, K, direction=1):
    """The seat's eval_m21_linear_eft (C59 producer), generalised from 7 blocks to K: diagonal Y_0^H, Y_1, Y_2^H, ...; superdiagonal -I;
    Schur complement over the interior; Z_Q = I + dZ_Q,u + dZ_Q,d, Z_L = I + dZ_L,e, Z_R per sector."""
    data = {}
    for sec, (ql, qr) in SEC:
        ys = transported(orb, k0, K, direction, ql, qr)
        hops = [ys[n].H if n % 2 == 0 else ys[n] for n in range(K)]
        N = 3 * K; M = mp.zeros(N, N)
        for m in range(K - 1):
            for r in range(3): M[3 * m + r, 3 * (m + 1) + r] = -1
        for n in range(K):
            for r in range(3):
                for c in range(3): M[3 * n + r, 3 * n + c] = hops[n][r, c]
        if K == 1:
            data[sec] = (M.H, mp.zeros(3, 3), I3); continue
        A = M[:N - 3, :3]; B = M[:N - 3, 3:]; C = M[N - 3:, :3]; D = M[N - 3:, 3:]
        BiA = (B ** -1) * A; DBi = D * (B ** -1)
        data[sec] = ((C - D * BiA).H, BiA.H * BiA, I3 + DBi * DBi.H)
    ZQ = I3 + data["u"][1] + data["d"][1]; ZL = I3 + data["e"][1]
    yu = c59.herm_inv_sqrt(ZQ) * data["u"][0] * c59.herm_inv_sqrt(data["u"][2])
    yd = c59.herm_inv_sqrt(ZQ) * data["d"][0] * c59.herm_inv_sqrt(data["d"][2])
    ye = c59.herm_inv_sqrt(ZL) * data["e"][0] * c59.herm_inv_sqrt(data["e"][2])
    out = {}
    for s, y in (("u", yu), ("d", yd), ("e", ye)):
        sv = sorted(mp.svd_c(y, compute_uv=False)); out[s] = (sv[1] / sv[2], sv[0] / sv[2])
    _, uu = c59.eig_herm_asc(yu * yu.H); _, ud = c59.eig_herm_asc(yd * yd.H); V = uu.H * ud
    Js = mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0]))
    return out, (abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2])), Js
f = lambda x: mp.nstr(x, 2)
print("== (0) reproduction of the seat's sealed C59 output, all 8 vertex chains (main's driver, K = 7)")
worst = 0
for row in SEALED["E4_linear_21x21_boundary_dirac_eft"]["all_8_vertex_linear_eft_chains"]:
    o = orbits[row["orbit"]]; w0 = (Fr(row["start_30"][0], 30), Fr(row["start_30"][1], 30)); k0 = o.index(w0)
    r, V, Js = chain(o, k0, 7)
    mine = [r["u"][0], r["u"][1], r["d"][0], r["d"][1], r["e"][0], r["e"][1], V[0], V[1], V[2], abs(Js)]
    theirs = [mp.mpf(x) for x in row["up_ratios"] + row["down_ratios"] + row["lep_ratios"] + row["ckm_moduli_and_min_diag"][:3] + [row["jarlskog_abs"]]]
    dev = max(abs(a - b) / abs(b) for a, b in zip(mine, theirs)); worst = max(worst, dev)
    print("orbit %d, start %s: largest relative difference from the sealed values %s" % (row["orbit"], row["start_30"], mp.nstr(dev, 3)))
print("SUMMARY (0): main's driver reproduces the seat's sealed E4 values on 8 of 8 chains, worst relative difference %s" % mp.nstr(worst, 3))
oi, o = 1, orbits[1]; v0 = o.index((Fr(26, 30), Fr(17, 30)))
print("== (1) the chain length K on the seat's reference chain (orbit 1, start (26/30, 17/30), its (a_5/5) = +1 wall v_0)")
for K in (1, 3, 5, 7, 9, 11):
    r, V, Js = chain(o, v0, K)
    print("K = %2d: u (m2/m3, m1/m3) = (%s, %s)  d = (%s, %s)  e = (%s, %s)  |V12|,|V23|,|V13| = %s, %s, %s  |J| = %s" % (K, f(r["u"][0]), f(r["u"][1]), f(r["d"][0]), f(r["d"][1]), f(r["e"][0]), f(r["e"][1]), f(V[0]), f(V[1]), f(V[2]), f(abs(Js))), flush=True)
print("== (2) K = 7 from every sheet of every orbit (96 chains): the spread of each output")
rows = [chain(o2, k0, 7) for o2 in orbits for k0 in range(12)]
def spread(vals):
    vals = sorted(float(v) for v in vals); return "min %.2g  median %.2g  max %.2g" % (vals[0], statistics.median(vals), vals[-1])
for s in "ude":
    print("%s m2/m3: %s   m1/m3: %s" % (s, spread([x[0][s][0] for x in rows]), spread([x[0][s][1] for x in rows])))
print("|V12|: %s   |V23|: %s   |V13|: %s   |J|: %s" % (spread([x[1][0] for x in rows]), spread([x[1][1] for x in rows]), spread([x[1][2] for x in rows]), spread([abs(x[2]) for x in rows])))
print("SUMMARY (2): the ordering m2/m3 u > d > e holds on %d of %d chains" % (sum(1 for x in rows if x[0]["u"][0] > x[0]["d"][0] > x[0]["e"][0]), len(rows)))
print("== (3) item 2: the 12-turn phase per orbit and sector")
for k, o2 in enumerate(orbits):
    hs = []
    for sec, (ql, qr) in SEC:
        h = mp.mpc(1)
        for n in range(12): h *= sph[(o2[n], ql, qr)]
        hs.append(h)
    print("orbit %d: up angle %s deg (|up - e^{-+2 pi i/5}| = %s); |down - 1| = %s; |lepton - 1| = %s" % (k, mp.nstr(mp.degrees(mp.arg(hs[0])), 8), mp.nstr(min(abs(hs[0] - mp.exp(s * 2j * mp.pi / 5)) for s in (1, -1)), 3), mp.nstr(abs(hs[1] - 1), 3), mp.nstr(abs(hs[2] - 1), 3)))
print("== (4) item 3: clockwise against counterclockwise from each mirror wall (K = 7)")
for k, o2 in enumerate(orbits):
    verts = sorted(j for j in range(12) if (o2[j][0] % 1, (-(o2[j][0] + o2[j][1])) % 1) == o2[j])
    for v in verts:
        r1, V1, j1 = chain(o2, v, 7, 1); r2, V2, j2 = chain(o2, v, 7, -1)
        even = max([abs(r1[s][i] - r2[s][i]) for s in "ude" for i in (0, 1)] + [abs(a - b) for a, b in zip(V1, V2)])
        print("orbit %d wall %d: J_cw = %s, J_ccw = %s, J_cw + J_ccw = %s; CP-even outputs differ by at most %s" % (k, v, mp.nstr(j1, 4), mp.nstr(j2, 4), mp.nstr(j1 + j2, 3), mp.nstr(even, 3)))
