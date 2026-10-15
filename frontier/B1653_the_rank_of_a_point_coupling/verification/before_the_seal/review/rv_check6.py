"""Reviewer check 6: the exact form of the record's coupling (B1644's Y_unit, generalised to twisted pairs) in the units'
labels: Y_full = a R^T + R a^T - (a.R) 1 + c * R_1 [a]_x ; find c, check the untwisted limit, and det = 0 by R_1^2 = -R.R."""
import sys
sys.path.insert(0, ".")
import numpy as np
from rv_core import *
exec(open("rv_check5.py").read().split("om = mp.exp")[0])      # reuse res_bil, full_Y, unit_res, svals (reviewer's own)

def mc(c): c = complex(c); return mp.mpc(c.real, c.imag)
t = mp.mpc("0.13", "1.07")
perm = [1, 0, 2]          # BLOCKS (QJ, QI, QK) -> units' labels (i, j, k): generation p in BLOCKS has unit label perm[p]
for (x, y, lab) in [((0, 0), (0, 0), "untwisted"), ((mp.mpf("0.13"), mp.mpf("0.31")), (mp.mpf("-0.07"), mp.mpf("0.22")), "twisted")]:
    RB = res_bil(x, y, t); R = unit_res(RB); R1, Rv = R[0], mp.matrix(R[1:])
    a = [mc(v) for v in (0.3 + 0.2j, -0.7 + 0.1j, 0.4 - 0.5j)]
    S = a[0] * QI + a[1] * QJ + a[2] * QK
    Yb = full_Y(RB, S)
    Y = mp.matrix(3, 3)                       # to units' labels
    for p in range(3):
        for q in range(3):
            Y[perm[p], perm[q]] = Yb[p, q]
    av = mp.matrix(a)
    Ytr = av * Rv.T + Rv * av.T - (av.T * Rv)[0] * mp.eye(3)
    ax = mp.matrix([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    D = Y - Ytr
    nrm = mp.mnorm(Y, "F")
    if abs(R1) > 1e-30:
        c = D[0, 1] / (R1 * ax[0, 1])
        print(f"{lab}: |Y - Y_triplet|/|Y| = {mp.nstr(mp.mnorm(D,'F')/nrm,4)}; c = {mp.nstr(c,10)}; "
              f"residual of Y = Y_triplet + c R1 [a]x: {mp.nstr(mp.mnorm(D - c*R1*ax,'F')/nrm,3)}; R1^2/(-R.R) = {mp.nstr(R1**2/(-(Rv.T*Rv)[0]),10)}")
    else:
        print(f"{lab}: R1 = {mp.nstr(abs(R1),3)}; |Y - Y_triplet|/|Y| = {mp.nstr(mp.mnorm(D,'F')/nrm,3)} (B1645's identity in the untwisted case)")
    print(f"   det Y_full / |Y|^3 = {mp.nstr(abs(mp.det(Y))/nrm**3,3)};  det Y_triplet / |Y_triplet|^3 = {mp.nstr(abs(mp.det(Ytr))/mp.mnorm(Ytr,'F')**3,4)}")
