#!/usr/bin/env python3
"""B463 (Relation R4) — the centralizer of the principal sl2 in e6, EXACT.

C = {x in e6 : [x,e]=[x,h]=[x,f]=0} from B351's exact algebra (Fractions).
CONTROL GATE (must pass first): the same computation for the LONG-ROOT A1 must
reproduce the banked C_{e6}(su2_long) = sl6 (dim 35, B247).

Run: python3 centralizer.py    (prints ALL CHECKS PASS)
"""
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "B351_exact_e6_chevalley"))
import exact_e6 as E6


def ad_matrix_of(vec):
    return E6._ad_matrix(vec)


def joint_kernel(vecs):
    """dim of the joint kernel of ad(v) for v in vecs, exact over Q (Fraction Gauss)."""
    rows = []
    for v in vecs:
        M = ad_matrix_of(v)
        rows.extend(M)          # stack: x in kernel of all  <=>  (stacked M) x = 0
    # exact Gaussian elimination
    m = [row[:] for row in rows]
    ncols = E6.DIM
    rank = 0
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(m)):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        r += 1
        rank += 1
        if r == len(m):
            break
    return ncols - rank


def run():
    ok = True
    # CONTROL GATE: the long-root A1. Long root = the highest root theta of E6.
    # e_theta / f_theta / h_theta: highest root = index of the highest root in POS.
    # find theta = the positive root of maximal height
    heights = [sum(r) for r in E6.POS]  # coefficient sum in the simple-root basis? POS entries
    # POS entries are root vectors in the simple-root coordinate convention used by B351
    hmax = max(heights)
    itheta = heights.index(hmax)
    theta = E6.POS[itheta]
    ntheta = tuple(-x for x in theta)
    e_t = {6 + E6.RIDX[theta]: 1}
    f_t = {6 + E6.RIDX[ntheta]: 1}
    # h_theta = [e_theta, f_theta]
    h_t = E6.brk(e_t, f_t)
    dimC_long = joint_kernel([e_t, h_t, f_t])
    print(f"CONTROL (long-root A1): dim C = {dimC_long}   (banked B247: 35 = sl6)")
    ok &= (dimC_long == 35)

    # THE CELL: the principal sl2
    e, h, f = E6.principal_sl2()
    dimC = joint_kernel([e, h, f])
    print(f"PRINCIPAL sl2: dim C_e6(principal) = {dimC}   (prediction: 0)")
    ok &= (dimC == 0)
    # the ker(ad e) weight check from the plan (chains have ad-h weights 2m, all > 0)
    kern = E6._nullspace(E6._ad_matrix(e))
    ws = []
    for v in kern:
        p = next(iter(v))
        w = int(E6.brk(h, v).get(p, 0) / v[p])
        ws.append(w)
    print(f"ker(ad e) ad-h weights: {sorted(ws)}  (all > 0 => weight-0 intersection empty)")
    ok &= all(w > 0 for w in ws)

    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    print("\nScoped consequence: the algebra centralizer of the PRINCIPAL lift is 0 =>")
    print("the group centralizer is FINITE (Kostant: = Z(E6), Z/3 simply-connected /")
    print("trivial adjoint - LIT-GATE citation, not computed). No continuous 4d gauge")
    print("group from the principal lift. The long-root lift's SU(6) (banked) shows the")
    print("kill is embedding-specific - stated, not overclaimed.")
    return bool(ok)


if __name__ == '__main__':
    run()
