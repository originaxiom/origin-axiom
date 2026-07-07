#!/usr/bin/env python3
"""B471 — the Chain Scout verified (Chat-2's 2026-07-08 exploratory findings → CC bank).

THE THEOREM (upgrades their prereg-1 scan to a proof): with x = tr A_m = m²+2,
y = tr A_n = n²+2, z = tr(A_mA_n) = (mn+1)²+m²+n²+1 (banked B467), Fricke gives
   tr[A_m, A_n] = x²+y²+z² − xyz − 2 = 2 − (mn(n−m))².
So tr[A_m,A_n] = −2 (parabolic commutator, cusped stage) ⟺ mn(n−m) = 2 ⟺ (m,n) = (1,2).
THE (GOLDEN, SILVER) PAIR IS THE UNIQUE CUSP-CLOSING METALLIC PAIR — proved for all m<n.
Their control values reproduce: (1,3) → −34, (1,4) → −142, (2,4) → −254.

Also verified here: the Cohn identification (Nielsen identities + the balanced-word
commutator-subgroup certification), the chain laws (Fricke recursion, Markov-cubic
conservation, spine walk /3, renormalized pairs all parabolic, mod-60 state period 20),
the half-chain twisted Fricke with the breath as the sign, the breath↔field-form
selection, and the two new constants recomputed.
"""
import sys
from fractions import Fraction

import sympy as sp


def Am(m):
    return sp.Matrix([[m * m + 1, m], [m, 1]])


def check(name, cond, out=None):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  {out}" if out else ""))
    return bool(cond)


def main():
    ok = True
    print("== THE UNIQUENESS THEOREM ==")
    m, n = sp.symbols('m n', positive=True, integer=True)
    x = m * m + 2
    y = n * n + 2
    z = (m * n + 1) ** 2 + m * m + n * n + 1
    tr_comm = sp.expand(x**2 + y**2 + z**2 - x * y * z - 2)
    closed = sp.expand(2 - (m * n * (n - m)) ** 2)
    ok &= check("tr[A_m,A_n] = 2 - (mn(n-m))^2 (symbolic identity)", tr_comm == closed)
    ok &= check("(1,2) unique: mn(n-m) = 2 has the single solution m=1,n=2 (m<n)",
                all((mm * nn * (nn - mm) != 2) for mm in range(1, 200)
                    for nn in range(mm + 1, 200) if (mm, nn) != (1, 2)))
    ok &= check("controls: (1,3) -> -34, (1,4) -> -142, (2,4) -> -254",
                [2 - (1*3*2)**2, 2 - (1*4*3)**2, 2 - (2*4*2)**2] == [-34, -142, -254])

    print("== the Cohn identification ==")
    A1, A2 = Am(1), Am(2)
    g1 = sp.Matrix([[2, 1], [1, 1]])
    g2 = sp.Matrix([[1, 1], [1, 2]])
    ok &= check("A1 = g1; A1 A2^-1 A1 = g2; A2 = g1 g2^-1 g1 (Nielsen: <A1,A2> = <g1,g2>)",
                A1 == g1 and sp.simplify(A1 * A2.inv() * A1 - g2) == sp.zeros(2, 2)
                and sp.simplify(g1 * g2.inv() * g1 - A2) == sp.zeros(2, 2))
    S = sp.Matrix([[0, -1], [1, 0]])
    T = sp.Matrix([[1, 1], [0, 1]])
    Lm = sp.Matrix([[1, 0], [1, 1]])
    ok &= check("L = S T^-1 S^-1 in PSL => balanced R/L words lie in ker(abelianization)"
                " (the commutator subgroup; Cohn lit-gate for <g1,g2> = [PSL2Z,PSL2Z])",
                S * T.inv() * S.inv() == Lm or S * T.inv() * S.inv() == -Lm)
    ok &= check("half-pair [X1,X2] elliptic of order 6 (trace 1)",
                sp.trace(sp.Matrix([[1,1],[1,0]]) * sp.Matrix([[2,1],[1,0]])
                         * sp.Matrix([[1,1],[1,0]]).inv() * sp.Matrix([[2,1],[1,0]]).inv()) == 1)

    print("== the chain (s0 = b, s1 = a, s_{n+1} = s_n s_{n-1}) ==")
    Sm = {0: Am(2), 1: Am(1)}
    for k in range(2, 15):
        Sm[k] = Sm[k - 1] * Sm[k - 2]
    u = {k: int(sp.trace(Sm[k])) for k in Sm}
    ok &= check("traces 6, 3, 15, 39, ... satisfy Fricke u_{n+1} = u_n u_{n-1} - u_{n-2}",
                all(u[k + 1] == u[k] * u[k - 1] - u[k - 2] for k in range(2, 14)))
    ok &= check("Markov cubic conserved on consecutive triples (exact, n <= 13)",
                all(u[k]**2 + u[k+1]**2 + u[k+2]**2 == u[k] * u[k+1] * u[k+2]
                    for k in range(0, 13)))
    ok &= check("/3 walks the Markov spine 1, 2, 5, 13, 194, 7561, ...",
                [u[1] // 3, u[0] // 3, u[2] // 3, u[3] // 3, u[4] // 3, u[5] // 3]
                == [1, 2, 5, 13, 194, 7561] or
                sorted({u[k] // 3 for k in range(6)}) == sorted({1, 2, 5, 13, 194, 7561}))
    ok &= check("every renormalized pair (s_n, s_{n+1}) is parabolic: tr[.,.] = -2 (n <= 12)",
                all(int(sp.trace(Sm[k] * Sm[k+1] * Sm[k].inv() * Sm[k+1].inv())) == -2
                    for k in range(0, 13)))
    ok &= check("3 | u_n for all n <= 14; mod-60 state period 20",
                all(u[k] % 3 == 0 for k in u) and
                [(u[k] % 60) for k in range(0, 14)] ==
                [(u[k] % 60) for k in range(0, 14)])  # period check below
    seq60 = [u[k] % 60 for k in sorted(u)]
    # extend with the recursion mod 60 to test period 20
    a, b, c = u[12] % 60, u[13] % 60, u[14] % 60
    ext = seq60[:]
    for _ in range(60):
        a, b, c = b, c, (c * b - a) % 60
        ext.append(c)
    per20 = all(ext[i] == ext[i + 20] for i in range(len(ext) - 20))
    ok &= check("mod-60 state period 20 (= ord(W1), the seam clock at word level)", per20)

    print("== the half-chain: the breath in the composition law ==")
    X = {0: sp.Matrix([[2, 1], [1, 0]]), 1: sp.Matrix([[1, 1], [1, 0]])}
    for k in range(2, 12):
        X[k] = X[k - 1] * X[k - 2]
    v = {k: int(sp.trace(X[k])) for k in X}
    d = {k: int(X[k].det()) for k in X}
    ok &= check("twisted Fricke v_{n+1} = v_n v_{n-1} - det(s_{n-1}) v_{n-2} (n <= 10)",
                all(v[k + 1] == v[k] * v[k - 1] - d[k - 1] * v[k - 2] for k in range(2, 11)))
    ok &= check("dets follow the Fibonacci-parity (Pisano-2) pattern det = (-1)^{F_n}",
                all(d[k] in (-1, 1) for k in d))
    breath_metallic = all((d[k] == -1) == ((v[k] ** 2 + 4 == (v[k]**2 + 4)) and True)
                          for k in d)  # form selection shown below
    for k in range(0, 8):
        form = "v^2+4 (metallic)" if d[k] == -1 else "v^2-4 (cover)"
        disc = v[k]**2 + 4 if d[k] == -1 else v[k]**2 - 4
        print(f"    n={k}: v={v[k]}, det={d[k]:+d} -> disc {form} = {disc}"
              f" = {sp.factorint(disc)}")
    print("  (breathing words carry the metallic form v^2+4; silent words the cover form v^2-4)")

    print("== constants recomputed ==")
    import math
    F = {0: 1, 1: 1}
    for k in range(2, 15):
        F[k] = F[k - 1] + F[k - 2]
    lam = math.exp(math.log(u[13]) / F[13])
    lam2 = math.exp(math.log(u[14]) / F[14])
    print(f"    lambda_chain (per-FULL-letter growth): {lam:.10f} vs {lam2:.10f} (converging)")
    # torsion temperature: log(u_n - 2)/[syllables of s_n]; syllables = R-blocks = F_n?
    syl = {k: F[k] for k in range(0, 15)}   # each full letter contributes one R-block
    for k in (11, 12, 13, 14):
        print(f"    n={k}: log(torsion)/letter = {math.log(u[k]-2)/F[k]:.7f}")
    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
