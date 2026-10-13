#!/usr/bin/env python3
"""B1639 -- THE GOLDEN IDENTITY FROM RAMANUJAN'S QUINTIC MODULAR EQUATION.  B1638: H(tau) = sum_p g_p(tau) g_p(N tau) = 8 to 49
digits (g_p = (theta_p/eta)^2, N = [[-1, -2], [2, -1]]), which makes the weave's lowest coupling golden on every discriminant-5
geodesic.  The proof route: with lambda = theta_2^4/theta_3^4,
  g_3^12 = 2^8 / (lambda (1 - lambda))^2,  g_2 = g_3 * s(lambda),  g_4 = g_3 * c(lambda)   (s^2 = lambda, c^2 = 1 - lambda),
so H = g_3 g_3' (1 + s s' + c c') with ' at N tau, and
  H^12 = 2^16 (1 + s s' + c c')^12 / (alpha beta (1-alpha)(1-beta))^2,  alpha = lambda(tau), beta = lambda(N tau).
Ramanujan (Berndt, Ramanujan's Notebooks III, ch. 19, Entry 13(xii)): if beta has degree 5 over alpha,
  (alpha beta)^(1/2) + ((1-alpha)(1-beta))^(1/2) + 2 (16 alpha beta (1-alpha)(1-beta))^(1/6) = 1,
which with the branches s s', c c' (signs fixed below) gives (1 + s s' + c c')^6 = 2^10 alpha beta (1-alpha)(1-beta), hence
H^12 = 8^12; H is continuous on the connected upper half-plane with values in 8 x (12th roots of unity), so constant, and one
evaluation fixes 8.  This instrument checks the three computable steps:
 R1  that beta = lambda(N tau) has degree 5 over alpha = lambda(tau): a factorisation N = G1 D G2 with D in {diag(1, 5),
     diag(5, 1)} and G1, G2 in SL(2, Z) acting on lambda compatibly (both in Gamma(2), or the same anharmonic map on alpha and
     beta so that the symmetric relation is kept) -- searched over small integer matrices.
 R2  at 20 random tau (50 digits): g_3^12 (alpha (1-alpha))^2 = 2^8; g_2/g_3 and g_4/g_3 square to alpha and 1 - alpha.
 R3  at the same points: (1 + s s' + c c')^6 - 2^10 alpha beta (1-alpha)(1-beta) = 0, with s s' = g_2 g_2'/(g_3 g_3') and
     c c' = g_4 g_4'/(g_3 g_3'); and Ramanujan's relation itself with the principal branches and each sign pattern of the two
     square roots, reporting which pattern vanishes.
Writes golden_from_ramanujan.json."""
import json, pathlib, random, itertools
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 50


def thetas(t):
    e = lambda x: mp.exp(1j * mp.pi * t * x)
    K = 80
    th2 = mp.fsum(e((n + mp.mpf(1) / 2) ** 2) for n in range(-K, K))
    th3 = mp.fsum(e(n * n) for n in range(-K, K + 1))
    th4 = mp.fsum((-1) ** abs(n) * e(n * n) for n in range(-K, K + 1))
    eta = mp.exp(1j * mp.pi * t / 12) * mp.fprod(1 - mp.exp(2j * mp.pi * t * n) for n in range(1, 600))
    return th2, th3, th4, eta


def gs(t):
    th2, th3, th4, eta = thetas(t)
    return (th2 / eta) ** 2, (th3 / eta) ** 2, (th4 / eta) ** 2, th2 ** 4 / th3 ** 4


def mob(M, t):
    return (M[0][0] * t + M[0][1]) / (M[1][0] * t + M[1][1])


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def inv(A):
    return [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]


def mod2(A):
    return tuple(x % 2 for row in A for x in row)


def r1():
    N = [[-1, -2], [2, -1]]
    found = []
    rng = range(-6, 7)
    for a, b, c in itertools.product(rng, rng, rng):
        for D in ([[1, 0], [0, 5]], [[5, 0], [0, 1]]):
            # G2 = [[a, b], [c, d]] with det 1; G1 = N G2^-1 D^-1 must be integral with det 1
            if a == 0: continue
            if (1 + b * c) % a: continue
            d = (1 + b * c) // a
            G2 = [[a, b], [c, d]]
            M = mul(N, inv(G2))                                  # = G1 D
            Dinv5 = [[D[1][1], 0], [0, D[0][0]]]                  # 5 D^-1
            G1x5 = mul(M, Dinv5)
            if any(x % 5 for row in G1x5 for x in row): continue
            G1 = [[x // 5 for x in row] for row in G1x5]
            if G1[0][0] * G1[1][1] - G1[0][1] * G1[1][0] != 1: continue
            found.append({"G1": G1, "D": D, "G2": G2, "G1_mod2": mod2(G1), "G2_mod2": mod2(G2),
                          "both_in_Gamma2": mod2(G1) == (1, 0, 0, 1) and mod2(G2) == (1, 0, 0, 1),
                          "same_class_mod2": mod2(G1) == mod2(inv(G2))})
    good = [f for f in found if f["both_in_Gamma2"]]
    return {"factorisations_found": len(found), "both_in_Gamma2": good[:3], "count_both_in_Gamma2": len(good),
            "any_same_anharmonic_class": any(f["same_class_mod2"] for f in found)}


def main():
    out = {"R1": r1()}
    N = [[-1, -2], [2, -1]]
    rnd = random.Random(1639)
    pts = [mp.mpc(rnd.uniform(-0.5, 0.5), rnd.uniform(0.5, 2.5)) for _ in range(20)]
    r2, r3, pat = [], [], {}
    for t in pts:
        g2, g3, g4, al = gs(t)
        h2, h3, h4, be = gs(mob(N, t))
        r2.append(max(abs(g3 ** 12 * (al * (1 - al)) ** 2 - 256), abs((g2 / g3) ** 2 - al), abs((g4 / g3) ** 2 - (1 - al))))
        ss = g2 * h2 / (g3 * h3); cc = g4 * h4 / (g3 * h3)
        X = al * be * (1 - al) * (1 - be)
        r3.append(abs((1 + ss + cc) ** 6 - 2 ** 10 * X) / abs(2 ** 10 * X))
        for e1, e2 in itertools.product((1, -1), repeat=2):
            for k in range(6):                                   # the six branches of the sixth root
                root6 = mp.root(16 * X, 6) * mp.exp(2j * mp.pi * k / 6)
                v = e1 * mp.sqrt(al * be) + e2 * mp.sqrt((1 - al) * (1 - be)) + 2 * root6 - 1
                pat.setdefault((e1, e2, k), []).append(abs(v))
    out["R2_max_residual"] = float(max(r2))
    out["R3_max_relative_residual"] = float(max(r3))
    zero = {str(k): float(max(v)) for k, v in pat.items() if max(v) < mp.mpf(10) ** -30}
    out["R3_ramanujan_branch_patterns_vanishing_at_all_points"] = zero
    out["R3_patterns_vanishing_at_some_point"] = sorted({str(k) for k, v in pat.items() if min(v) < mp.mpf(10) ** -30})
    json.dump(out, open(HERE / "golden_from_ramanujan.json", "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
