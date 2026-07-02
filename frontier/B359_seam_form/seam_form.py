"""THE SEAM FORM -- exact readout of the Par-inserted pair invariants for pairs (1,3) and (2,3),
in BOTH lifts (theta + canonical), extending B358's engine. Pure Fraction arithmetic.

Question (pre-registered, Chat-2's proposal + L57): are the sqrt(-15) coefficients PAIR-SPECIFIC
(a seam-valued pairing form on the metallic family) or shared/absent? Null: (1,3) and (2,3)
tables are seam-free or duplicate (1,2)'s values.

Seed 3 (bronze): A_3 word 'RRRLLL'; order mod 15 = 6 (A_3 = I mod 3 -- the divisibility law).
"""
from fractions import Fraction as Fr
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B358_seam_certification"))
from cyclo_engine import (DEG, add, sub, scal, mul, ZERO, ONE, zeta, e15,
                        SQRT5, SQRTm3, SQRTm15, conj_elt, mmul,
                        Tmat, Tinv, Smat, Sinv, G15_INV, SQRT15)

N = 15


def is_identity(M):
    for i in range(N):
        for j in range(N):
            if M[i][j] != (ONE if i == j else ZERO):
                return False
    return True


def theta_gens():
    D = [[ZERO for _ in range(N)] for _ in range(N)]
    Di = [[ZERO for _ in range(N)] for _ in range(N)]
    for j in range(N):
        t = (j * (j - 1)) // 2
        D[j][j] = e15(t)
        Di[j][j] = e15(-t)
    INV_SQRT15 = scal(Fr(1, 15), SQRT15)
    F = [[mul(e15(i * j), INV_SQRT15) for j in range(N)] for i in range(N)]
    Fi = [[mul(e15(-i * j), INV_SQRT15) for j in range(N)] for i in range(N)]
    WR = mmul(mmul(F, Di), Fi)
    return WR, D


def canonical_ops():
    T, Ti, S, Si = Tmat(), Tinv(), Smat(), Sinv()

    def A(m):
        Tm = T
        Tim = Ti
        for _ in range(m - 1):
            Tm = mmul(Tm, T)
            Tim = mmul(Tim, Ti)
        return mmul(mmul(Tm, S), mmul(Tim, Si))
    return A(1), A(2), A(3)


def theta_ops():
    WR, WL = theta_gens()
    W1 = mmul(WR, WL)
    W2 = mmul(mmul(WR, WR), mmul(WL, WL))
    WR3 = mmul(mmul(WR, WR), WR)
    WL3 = mmul(mmul(WL, WL), WL)
    W3 = mmul(WR3, WL3)
    return W1, W2, W3


def powers(W, n):
    out = [None] * n
    out[0] = [[ONE if i == j else ZERO for j in range(N)] for i in range(N)]
    for k in range(1, n):
        out[k] = mmul(out[k - 1], W)
    assert is_identity(mmul(out[n - 1], W)), f"order != {n}"
    return out


def par_trace(M):
    t = ZERO
    for x in range(N):
        t = add(t, M[(-x) % N][x])
    return t


def C_table(Wa_pows, Wb_pows):
    na, nb = len(Wa_pows), len(Wb_pows)
    return [[par_trace(mmul(Wa_pows[j], Wb_pows[l]) if (j, l) != (0, 0) else Wa_pows[0])
             for l in range(nb)] for j in range(na)]


GAL_H = [1, 19, 31, 49]


def sigma(a, c):
    out = [Fr(0)] * DEG
    for k in range(DEG):
        if a[k]:
            out = add(out, scal(a[k], zeta((c * k) % 60)))
    return out


def solve_H(t):
    cols = [ONE, SQRT5, SQRTm3, SQRTm15]
    Ab = [[cols[c][row] for c in range(4)] + [t[row]] for row in range(DEG)]
    r = 0
    piv = []
    for c in range(4):
        p = next((i for i in range(r, DEG) if Ab[i][c] != 0), None)
        if p is None:
            continue
        Ab[r], Ab[p] = Ab[p], Ab[r]
        pv = Ab[r][c]
        Ab[r] = [v / pv for v in Ab[r]]
        for i in range(DEG):
            if i != r and Ab[i][c] != 0:
                f = Ab[i][c]
                Ab[i] = [Ab[i][j] - f * Ab[r][j] for j in range(5)]
        piv.append(c)
        r += 1
    sol = [Fr(0)] * 4
    for i, c in enumerate(piv):
        sol[c] = Ab[i][4]
    for i in range(r, DEG):
        if Ab[i][4] != 0:
            return None
    return tuple(sol)


def readout(C, na_ord, nb_ord, zeta_a, zeta_b):
    """all doubles (1/(na*nb)) sum zeta_a^{-ja} zeta_b^{-lb} C[j][l], H-averaged, solved."""
    na, nb = len(C), len(C[0])
    out = {}
    for a in range(na_ord):
        for b in range(nb_ord):
            t = ZERO
            for j in range(na):
                zja = zeta((-zeta_a * j * a) % 60)
                for l in range(nb):
                    t = add(t, mul(mul(zja, zeta((-zeta_b * l * b) % 60)), C[j][l]))
            t = scal(Fr(1, na_ord * nb_ord), t)
            if t == ZERO:
                continue
            avg = ZERO
            for c in GAL_H:
                avg = add(avg, sigma(t, c))
            sol = solve_H(scal(Fr(1, 4), avg))
            assert sol is not None, (a, b)
            out[(a, b)] = sol
    return out


def summarize(name, table):
    seam = {k: v for k, v in table.items() if v[3] != 0}
    svals = sorted({v[3] for v in seam.values()})
    print(f"{name}: nonzero {len(table)} | seam-bearing {len(seam)} | distinct s-values {len(svals)}")
    for k in sorted(seam)[:8]:
        print(f"   {k}: p={seam[k][0]} q={seam[k][1]} r={seam[k][2]} s=[{seam[k][3]}]")
    return svals


def main():
    print("=== THETA LIFT ===", flush=True)
    W1, W2, W3 = theta_ops()
    P1 = powers(W1, 20)
    print("W1 powers ok", flush=True)
    P2 = powers(W2, 12)
    print("W2 powers ok", flush=True)
    P3 = powers(W3, 6)
    print("W3 powers ok (order 6 gate = the divisibility law)", flush=True)
    C13 = C_table(P1, P3)
    C23 = C_table(P2, P3)
    t13 = readout(C13, 20, 6, 3, 10)     # zeta20 = z^3 ; zeta6 = z^10
    t23 = readout(C23, 12, 6, 5, 10)     # zeta12 = z^5
    s13 = summarize("theta (1,3)", t13)
    s23 = summarize("theta (2,3)", t23)
    json.dump(dict(t13={str(k): [str(x) for x in v] for k, v in t13.items()},
                   t23={str(k): [str(x) for x in v] for k, v in t23.items()}),
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "seam_form_theta.json"), "w"))

    print("=== CANONICAL LIFT (control: expect s == 0 everywhere) ===", flush=True)
    V1, V2, V3 = canonical_ops()
    Q1 = powers(V1, 20)
    Q2 = powers(V2, 12)
    Q3 = powers(V3, 6)
    print("canonical powers ok", flush=True)
    D13 = C_table(Q1, Q3)
    D23 = C_table(Q2, Q3)
    u13 = readout(D13, 20, 6, 3, 10)
    u23 = readout(D23, 12, 6, 5, 10)
    bad = sum(1 for v in list(u13.values()) + list(u23.values()) if v[3] != 0)
    print(f"canonical (1,3)+(2,3): nonzero {len(u13)}+{len(u23)} | seam-bearing {bad} (expect 0)")

    # pair-specificity verdict vs the banked (1,2) s-set
    s12 = [Fr(1, 48), Fr(-1, 48), Fr(1, 160), Fr(-1, 160), Fr(1, 480), Fr(-1, 480),
           Fr(1, 240), Fr(-1, 240), Fr(1, 120), Fr(-1, 120), Fr(1, 80), Fr(-1, 80)]
    print("\nPAIR-SPECIFICITY:")
    print("  s-values (1,3):", [str(x) for x in s13])
    print("  s-values (2,3):", [str(x) for x in s23])
    print("  overlap with (1,2) set:", [str(x) for x in s13 if x in s12], "|",
          [str(x) for x in s23 if x in s12])


if __name__ == "__main__":
    main()


def load_banked():
    """The committed exact readout (regenerable by main())."""
    here = os.path.dirname(os.path.abspath(__file__))
    data = json.load(open(os.path.join(here, "seam_form_theta.json")))
    t13 = {eval(k): tuple(Fr(x) for x in v) for k, v in data["t13"].items()}
    t23 = {eval(k): tuple(Fr(x) for x in v) for k, v in data["t23"].items()}
    return t13, t23


def regenerate_matches_banked():
    """OA_SLOW tier: rerun the full exact pipeline and compare with the committed JSON."""
    W1, W2, W3 = theta_ops()
    P1, P2, P3 = powers(W1, 20), powers(W2, 12), powers(W3, 6)
    t13 = readout(C_table(P1, P3), 20, 6, 3, 10)
    t23 = readout(C_table(P2, P3), 12, 6, 5, 10)
    b13, b23 = load_banked()
    return t13 == b13 and t23 == b23
