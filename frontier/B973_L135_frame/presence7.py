#!/usr/bin/env python3
"""B973 / L135 -- the remaining B958 presence-side structural legs, on the
rebuilt frame, at the two primes rebuild.py validated at.

B958 (arc_verdict.json) lists SEVEN claims that a rebuilt frame would let this
bench test:
  (1) [M12,M12] escapes by exactly 4 INTO THE TORUS
  (2) [floor, M12] = 12 with ZERO escape
  (3) M12 is not a module over the FMT so(10) (escape 50)
  (4) centre 0
  (5) twelve multiplicity-one colour-blind weight lines
  (6) closure under exactly W_frame, three free orbits
  (7) the orbit <-> generation bijection
(4) is settled exactly over Q in rebuild.py (centre of derived(floor) = 0).
(5)(6)(7) are settled in weightlines.py. This file does (1)(2)(3).

REPRESENTATION: adjoint sector; every bracket below is inside e6. No 27 VEV.
TIER: mod p, two primes; mod-p rank <= char-0 rank. Evidence, not a certificate.
"""
import sys, json, time
sys.path.insert(0, "/Users/dri/origin-axiom/frontier/B961_frame_instrument")
import sympy as sp
import frame

T0 = time.time()
def log(m): print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)
DIM = frame.DIM; BB = frame.BB
INV = frame._G["INV"]; NS = [8, 14, 16, 22]; CH = {n: INV[n] for n in NS}
R = {}
AD = {n: frame.ad(CH[n]) for n in NS}
core = AD[8].nullspace(); Bc = sp.Matrix.hstack(*core); cdim = Bc.shape[1]
P = (Bc.T * Bc).inv() * Bc.T; C14 = P * AD[14] * Bc
fl = C14.nullspace(); Bf = Bc * sp.Matrix.hstack(*fl); fdim = Bf.shape[1]
piv = list(sp.Matrix(sp.Matrix.hstack(*fl).T).rref()[1])
comp = [i for i in range(cdim) if i not in piv][: cdim - fdim]
Tm = sp.Matrix.hstack(sp.Matrix.hstack(*fl), sp.eye(cdim)[:, comp]); Ti = Tm.inv()
C22 = P * AD[22] * Bc
Q14 = (Ti * C14 * Tm)[fdim:, fdim:]; Q22 = (Ti * C22 * Tm)[fdim:, fdim:]
s = sp.symbols('s'); qd = Q14.shape[0]
nu = sp.expand(sp.interpolate(
    list(zip(range(qd + 1), [(Q14 + sp.Rational(x) * Q22).det() for x in range(qd + 1)])), s))
kap = [sp.Poly(sp.primitive(f_)[1], s) for f_, m_ in sp.factor_list(sp.Poly(nu, s))[1]
       if m_ == 6 and sp.degree(f_, s) == 3][0]
kco = [int(kap.as_expr().coeff(s, i)) for i in range(4)]
assert kco == [-6859, -56402640, 3033676800, 2771822592000]
K = [[0] * DIM for _ in range(DIM)]
SPr = [[(q, kk, BB[i][q][kk]) for q in range(DIM) for kk in range(DIM) if BB[i][q][kk]]
       for i in range(DIM)]
for i in range(DIM):
    for j in range(i, DIM):
        t = 0
        for (q, kk, c) in SPr[i]:
            d = BB[j][kk][q]
            if d: t += c * d
        K[i][j] = int(t); K[j][i] = int(t)
log("build ready")
PRIMES = [41131, 41201]


def run(p):
    r = {}
    def rd(x):
        x = sp.Rational(x); return x.p % p * pow(x.q % p, p - 2, p) % p
    def mp(M): return [[rd(M[i, j]) for j in range(M.shape[1])] for i in range(M.shape[0])]
    def rref(rows):
        rows = [x[:] for x in rows]; n = len(rows[0]) if rows else 0; wh = {}; rk = 0
        for c in range(n):
            pv = next((i for i in range(rk, len(rows)) if rows[i][c]), None)
            if pv is None: continue
            rows[rk], rows[pv] = rows[pv], rows[rk]
            iv = pow(rows[rk][c], p - 2, p); rows[rk] = [v * iv % p for v in rows[rk]]
            for i in range(len(rows)):
                if i != rk and rows[i][c]:
                    f = rows[i][c]
                    rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[rk])]
            wh[c] = rk; rk += 1
        return rows, wh, rk
    def rank(vs): return 0 if not vs else rref([list(x) for x in zip(*vs)])[2]
    def basis(vs): return [x[:] for x in rref(vs)[0] if any(x)]
    def null(rows, n=DIM):
        rr, wh, _ = rref(rows); out = []
        for fc in [c for c in range(n) if c not in wh]:
            v = [0] * n; v[fc] = 1
            for c, rw in wh.items(): v[c] = (-rr[rw][fc]) % p
            out.append(v)
        return out
    def inter(A, B):
        return 0 if not A or not B else len(basis(A)) + len(basis(B)) - rank(A + B)
    BBp = [[[(kk, int(cv) % p) for kk, cv in enumerate(BB[a][b]) if cv] for b in range(DIM)]
           for a in range(DIM)]
    def brk(u, v):
        w = [0] * DIM
        for pp in range(DIM):
            if not u[pp]: continue
            for qq in range(DIM):
                if not v[qq]: continue
                cc = u[pp] * v[qq] % p
                for kk, cv in BBp[pp][qq]: w[kk] = (w[kk] + cc * cv) % p
        return w

    ADp = {n: mp(AD[n]) for n in NS}
    Kp = [[K[i][j] % p for j in range(DIM)] for i in range(DIM)]
    corep = [[rd(Bc[i, j]) for i in range(DIM)] for j in range(cdim)]
    floorp = [[rd(Bf[i, j]) for i in range(DIM)] for j in range(fdim)]
    torus = [[rd(sp.Rational(CH[n][i])) for i in range(DIM)] for n in NS]
    kr = sorted(x for x in range(p) if sum(c * pow(x, i, p) for i, c in enumerate(kco)) % p == 0)
    W = [null([[(ADp[14][i][j] + r0 * ADp[22][i][j]) % p for j in range(DIM)]
               for i in range(DIM)]) for r0 in kr]
    M12 = null([[sum(v[i] * Kp[i][j] for i in range(DIM) if v[i]) % p for j in range(DIM)]
                for v in W[0] + W[1] + W[2]])
    assert len(M12) == 12
    r["M12_dim"] = 12

    # (1) [M12,M12]: dimension, how much escapes M12, and WHERE it goes.
    B11 = basis([brk(M12[a], M12[b]) for a in range(12) for b in range(a + 1, 12)])
    r["dim_bracket_M12"] = len(B11)
    r["bracket_cap_M12"] = inter(B11, M12)
    r["bracket_escape"] = len(B11) - r["bracket_cap_M12"]
    r["bracket_cap_core"] = inter(B11, corep)
    r["bracket_cap_floor"] = inter(B11, floorp)
    r["bracket_cap_torus"] = inter(B11, torus)
    # the escape is INTO THE TORUS iff [M12,M12] subset M12 + torus
    r["escape_lands_in_torus"] = (rank(M12 + torus + B11) == rank(M12 + torus))
    r["torus_dim"] = rank(torus)

    # (2) [floor, M12]: rank and escape
    Bfm = basis([brk(f, v) for f in floorp for v in M12])
    r["dim_bracket_floor_M12"] = len(Bfm)
    r["floor_M12_escape"] = len(Bfm) - inter(Bfm, M12)

    # (3) the FMT so(10) wall z(x_i), x = g8 + rho*g16 at a mu-root: escape of [z, M12]
    mu_solo = [2197, -4769856, -2075673600, 500716339200]
    mur = sorted(x for x in range(p)
                 if sum(c * pow(x, t, p) for t, c in enumerate(mu_solo)) % p == 0)
    r["mu_roots"] = mur
    zx = null([[(ADp[8][i][j] + mur[0] * ADp[16][i][j]) % p for j in range(DIM)]
               for i in range(DIM)])
    r["dim_z_noncompact_wall"] = len(zx)
    Bzm = basis([brk(g, v) for g in zx for v in M12])
    r["dim_bracket_so10_M12"] = len(Bzm)
    r["so10_M12_escape"] = len(Bzm) - inter(Bzm, M12)
    # CONTROL: the same escape routine returns 0 for the floor (claim 2) and >0 here
    r["control_escape_routine_can_be_zero"] = (r["floor_M12_escape"] == 0)
    r["control_escape_routine_can_be_nonzero"] = (r["so10_M12_escape"] > 0)
    return r


for p in PRIMES:
    log(f"--- p = {p} ---")
    q = run(p); R[f"p{p}"] = q
    log(f"  (1) [M12,M12] dim {q['dim_bracket_M12']}, inside M12 {q['bracket_cap_M12']}, "
        f"ESCAPE {q['bracket_escape']}; escape lands in torus (dim {q['torus_dim']}): "
        f"{q['escape_lands_in_torus']}; cap core {q['bracket_cap_core']}, "
        f"cap floor {q['bracket_cap_floor']}, cap torus {q['bracket_cap_torus']}")
    log(f"  (2) [floor,M12] rank {q['dim_bracket_floor_M12']}, escape {q['floor_M12_escape']}")
    log(f"  (3) z(noncompact wall) dim {q['dim_z_noncompact_wall']}; [z,M12] rank "
        f"{q['dim_bracket_so10_M12']}, escape {q['so10_M12_escape']}")

V = []
def v(n, got, want):
    V.append({"check": n, "got": got, "want": want, "pass": bool(got == want)})
    log(f"  [{'PASS' if got == want else 'FAIL'}] {n}: {got} (expect {want})")
for p in PRIMES:
    q = R[f"p{p}"]
    v(f"(1) [M12,M12] escape == 4 (p={p})", q["bracket_escape"], 4)
    v(f"(1) escape lands in the torus (p={p})", q["escape_lands_in_torus"], True)
    v(f"(2) [floor,M12] rank == 12 (p={p})", q["dim_bracket_floor_M12"], 12)
    v(f"(2) [floor,M12] escape == 0 (p={p})", q["floor_M12_escape"], 0)
    v(f"(3) z(noncompact wall) dim == 46 (p={p})", q["dim_z_noncompact_wall"], 46)
    v(f"(3) [so(10),M12] escape == 50 (p={p})", q["so10_M12_escape"], 50)
    v(f"CONTROL escape routine returns 0 somewhere (p={p})",
      q["control_escape_routine_can_be_zero"], True)
    v(f"CONTROL escape routine returns >0 somewhere (p={p})",
      q["control_escape_routine_can_be_nonzero"], True)
R["VERDICT"] = V
R["ALL_PASS"] = all(x["pass"] for x in V)
R["FAILURES"] = [x for x in V if not x["pass"]]
log(f"presence legs (1)(2)(3): {sum(1 for x in V if x['pass'])}/{len(V)}; "
    f"ALL PASS = {R['ALL_PASS']}")
json.dump(R, open("/Users/dri/origin-axiom/frontier/B973_L135_frame/presence7_results.json", "w"),
          indent=1, sort_keys=True, default=str)
log("DONE")
