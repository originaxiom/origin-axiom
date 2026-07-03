"""B386 L1 -- the tensor identity gate: C[j,l] == C3[j,l] * C5[j,l] on all 240 cells.

Local theta models at q in {3,5} with multiplier u (registered conventions: (1,1) then (2,2)):
  D_q = diag zeta_q^{u j(j-1)/2},  F_q = [zeta_q^{u i j}],  WR = F D^{-1} F^{-1} / q,
  W_m = WR^m D^m,  Par_q = [i == -j mod q].
Global C from the banked step0 machinery."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

def zq(q, k):
    """zeta_q^k as an engine element (q in {3,5}; zeta60 engine)."""
    return E.zeta((60 // q) * (k % q))

def local_model(q, u, m):
    N = q
    def diagm(f): return [[f(j) if i == j else E.ZERO for j in range(N)] for i in range(N)]
    D  = diagm(lambda j: zq(q, u * (j * (j - 1) // 2)))
    Di = diagm(lambda j: zq(q, -u * (j * (j - 1) // 2)))
    F  = [[zq(q, u * i * j) for j in range(N)] for i in range(N)]
    Fi = [[E.scal(Fr(1, q), zq(q, -u * i * j)) for j in range(N)] for i in range(N)]
    WR = E.mmul(E.mmul(F, Di), Fi)
    W = [[E.ONE if i == j else E.ZERO for j in range(N)] for i in range(N)]
    for _ in range(m): W = E.mmul(W, WR)
    Dm = diagm(lambda j: zq(q, m * u * (j * (j - 1) // 2)))
    return E.mmul(W, Dm)

def local_partrace_table(q, u, m1, m2, o1, o2):
    W1 = local_model(q, u, m1); W2 = local_model(q, u, m2)
    # power caches up to the GLOBAL orders (indices mod local order implicitly via powers)
    def powers(W, n):
        P = [[E.ONE if i == j else E.ZERO for j in range(q)] for i in range(q)]
        out = [P]
        for _ in range(n - 1):
            P = E.mmul(out[-1], W)
            out.append(P)
        return out
    p1, p2 = powers(W1, o1), powers(W2, o2)
    T = {}
    for j in range(o1):
        for l in range(o2):
            t = E.ZERO
            M = E.mmul(p1[j], p2[l])
            for x in range(q):
                t = E.add(t, M[(-x) % q][x])
            T[(j, l)] = t
    return T

W1 = build_theta_W(1); W2 = build_theta_W(2)
o1, p1 = matrix_order(W1); o2, p2 = matrix_order(W2)
C = {(j, l): par_trace(p1[j], p2[l]) for j in range(o1) for l in range(o2)}

for (u3, u5) in ((1, 1), (2, 2)):
    T3 = local_partrace_table(3, u3, 1, 2, o1, o2)
    T5 = local_partrace_table(5, u5, 1, 2, o1, o2)
    bad = 0
    for j in range(o1):
        for l in range(o2):
            if C[(j, l)] != E.mul(T3[(j, l)], T5[(j, l)]):
                bad += 1
    print(f"convention (u3,u5)=({u3},{u5}): mismatches {bad}/240")
    if bad == 0:
        json.dump(dict(convention=[u3, u5], mismatches=0),
                  open(os.path.join(HERE, "tensor_gate.json"), "w"), indent=1)
        print("L1 PASS"); break
else:
    json.dump(dict(convention=None), open(os.path.join(HERE, "tensor_gate.json"), "w"), indent=1)
    print("L1 KILL (banked)")
print("DONE")
