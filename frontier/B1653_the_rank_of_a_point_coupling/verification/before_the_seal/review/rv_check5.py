"""Reviewer check 5 (the structural question): with twisted fields, is the full residue coupling's first generation lifted?
- the 2x2 residue matrix Res B_mn: rank one?
- the four-vector (R_1, R_i, R_j, R_k): R_1^2 + R.R = 0?
- the full mass matrix Y_pq = Res (C_p F~_x)^T eps S (C_q F~_y), generations C_p = (QJ, QI, QK) as in B1642's BLOCKS,
  Higgs S = s0 1 + a.(QI, QJ, QK): its singular values at 40 digits, against the triplet-only Y(a; R) of the draft's U5
- the left null vectors of the up and down sectors (both contain Q): aligned?"""
import sys
sys.path.insert(0, ".")
import numpy as np
from rv_core import *

def twist_of(w, t): return (mp.im(w) / mp.im(t), 2 * (mp.re(w) - mp.re(t) * mp.im(w) / mp.im(t)))

def res_bil(x, y, t, rad=mp.mpf("0.02"), N=96):
    acc = mp.matrix(2, 2)
    for m in range(N):
        z = rad * mp.exp(2 * J * mp.pi * m / N); B = bil(x, y, z, t)
        acc += B * z
    return acc / N

BLOCKS = [QJ, QI, QK]           # B1642: parities (1/2,0), (0,1/2), (1/2,1/2)
UNITS = [ONE, QI, QJ, QK]

def full_Y(RB, S):
    Y = mp.matrix(3, 3)
    for p, Cp in enumerate(BLOCKS):
        for q, Cq in enumerate(BLOCKS):
            M = Cp.T * QJ * S * Cq
            Y[p, q] = mp.fsum(M[m, n] * RB[m, n] for m in range(2) for n in range(2))
    return Y

def unit_res(RB):
    out = []
    for C in UNITS:
        M = QJ * C
        out.append(mp.fsum(M[m, n] * RB[m, n] for m in range(2) for n in range(2)))
    return out                    # (R_1, R_i, R_j, R_k)

def svals(Y):
    S = mp.svd_c(Y, compute_uv=False)
    S = sorted([abs(s) for s in S], reverse=True)
    return S

def null_left(Y):
    U, S, V = mp.svd_c(Y)
    k = min(range(3), key=lambda i: abs(S[i]))
    return mp.matrix([mp.conj(U[i, k]) for i in range(3)])     # u with u^T Y ~ 0  (left singular vector conj)

om = mp.exp(2 * J * mp.pi / 3); tg = mp.mpc("0.13", "1.07")
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
rng = np.random.default_rng(7)
Sdirs = []
def mc(c): c = complex(c); return mp.mpc(c.real, c.imag)
for _ in range(3):
    a = rng.normal(size=3) + 1j * rng.normal(size=3)
    Sdirs.append(("a only", mc(a[0]) * QI + mc(a[1]) * QJ + mc(a[2]) * QK, a))
s0 = complex(rng.normal() + 1j * rng.normal()); a = rng.normal(size=3) + 1j * rng.normal(size=3)
Sdirs.append(("s0 + a", mc(s0) * ONE + mc(a[0]) * QI + mc(a[1]) * QJ + mc(a[2]) * QK, a))

def triplet_Y(R3, a):
    av = mp.matrix([mp.mpc(c.real, c.imag) for c in a]); Rv = mp.matrix(R3)
    return av * Rv.T + Rv * av.T - (av.T * Rv)[0] * mp.eye(3)

cases = [("generic twists", tg, (mp.mpf("0.13"), mp.mpf("0.31")), (mp.mpf("-0.07"), mp.mpf("0.22")))]
for (name, wl) in [("half-period w=1/2, down", mp.mpf(1) / 2), ("Higgs line w=omega/9-1/9, down", om / 9 - mp.mpf(1) / 9)]:
    f1, f2 = SECT["down"]
    cases.append((name, om, twist_of(SIXY[f1] * wl, om), twist_of(SIXY[f2] * wl, om)))

for (name, t, x, y) in cases:
    RB = res_bil(x, y, t)
    det = RB[0, 0] * RB[1, 1] - RB[0, 1] * RB[1, 0]
    nrm = max(abs(RB[m, n]) for m in range(2) for n in range(2))
    R = unit_res(RB)
    RR = R[1] ** 2 + R[2] ** 2 + R[3] ** 2
    print(f"\n== {name} (tau {mp.nstr(t,4)}) ==")
    print(f"  Res B rank one: |det|/max^2 = {mp.nstr(abs(det)/nrm**2, 3)}")
    print(f"  |R.R|/|R|^2 = {mp.nstr(abs(RR)/sum(abs(R[k])**2 for k in (1,2,3)), 5)};  R_1/sqrt(-R.R) = {mp.nstr(R[0]/mp.sqrt(-RR), 8)}"
          f"  -> R_1^2 + R.R = {mp.nstr(abs(R[0]**2 + RR)/abs(RR), 3)} (relative)")
    for (lab, S, avec) in Sdirs:
        Y = full_Y(RB, S); sv = svals(Y)
        line = f"  Higgs {lab:6s}: FULL coupling s_min/s_max = {mp.nstr(sv[-1]/sv[0], 3)}"
        if lab == "a only":
            sv2 = svals(triplet_Y(R[1:], avec))
            line += f" | draft's triplet-only Y(a;R) s_min/s_max = {mp.nstr(sv2[-1]/sv2[0], 3)}"
        print(line)

print("\n== left null vectors at the Higgs line w = omega/9 - 1/9: up vs down (both contain Q) ==")
wl = om / 9 - mp.mpf(1) / 9
S = Sdirs[0][1]
nl = {}
for sec in ("up", "down"):
    f1, f2 = SECT[sec]
    RB = res_bil(twist_of(SIXY[f1] * wl, om), twist_of(SIXY[f2] * wl, om), om)
    Y = full_Y(RB, S); u = null_left(Y)
    nl[sec] = u
    print(f"  {sec}: |u^T Y|/|Y| = {mp.nstr(mp.norm(u.T * Y) / mp.mnorm(Y, 'F'), 3)}")
ov = abs(sum(mp.conj(nl['up'][i]) * nl['down'][i] for i in range(3))) / (mp.norm(nl['up']) * mp.norm(nl['down']))
print(f"  |<u_up, u_down>| = {mp.nstr(ov, 15)}  (1 = aligned: no Cabibbo angle at leading order)")
