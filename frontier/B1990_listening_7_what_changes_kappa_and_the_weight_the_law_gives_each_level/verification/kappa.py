"""B1990 (main, 2026-11-25; data-free): K1 the grammar's moves conserve kappa; K2 B497's non-invertible strata change it by
kappa' - 2 = (kappa - 2) M; K3 kappa = tr[a, b]; K4 the number of readings on each leaf X_kappa(F_p), p <= 47. Exact.
    python3 -B kappa.py > kappa_run.txt"""
import sympy as sp
X, Y, Z = sp.symbols("X Y Z")
kap = lambda v: sp.expand(v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2] - 2)
K = kap((X, Y, Z))
moves = {"L": (X, Z, X * Z - Y), "R": (Z, Y, Y * Z - X), "L^-1": (X, X * Y - Z, Y), "R^-1": (X * Y - Z, Y, X), "P (swap)": (Y, X, Z),
         "sign (-x,-y,z)": (-X, -Y, Z), "sign (-x,y,-z)": (-X, Y, -Z), "sign (x,-y,-z)": (X, -Y, -Z)}
inv_ok = all(sp.expand(sp.Matrix(moves[a]).subs({X: moves[b][0], Y: moves[b][1], Z: moves[b][2]}, simultaneous=True) - sp.Matrix([X, Y, Z])) == sp.zeros(3, 1) for a, b in (("L", "L^-1"), ("R", "R^-1")))
print("K1: the grammar's moves and the open ones conserve kappa: %s (inverses checked as inverses: %s)" % ({m: sp.expand(kap(v) - K) == 0 for m, v in moves.items()}, inv_ok))
strata = {"2 squaring a->a^2, b->b^2": (X ** 2 - 2, Y ** 2 - 2, X * Y * Z - X ** 2 - Y ** 2 + 2),
          "2' period doubling a->ab, b->aa": (Z, X ** 2 - 2, (X ** 2 - 1) * Z - X * Y),
          "3 Thue-Morse a->ab, b->ba": (Z, Z, X * Y * Z - X ** 2 - Y ** 2 + 2)}
for n, v in strata.items():
    M = sp.factor(sp.cancel((kap(v) - 2) / (K - 2)))
    print("K2: stratum %s: (kappa' - 2)/(kappa - 2) = %s" % (n, M))
a11, a12, a21, b11, b12, b21 = sp.symbols("a11 a12 a21 b11 b12 b21")
A = sp.Matrix([[a11, a12], [a21, (1 + a12 * a21) / a11]]); B = sp.Matrix([[b11, b12], [b21, (1 + b12 * b21) / b11]])
x, y, z = A.trace(), B.trace(), (A * B).trace()
print("K3: tr(a b a^-1 b^-1) = x^2 + y^2 + z^2 - xyz - 2 on SL(2): %s" % (sp.simplify((A * B * A.inv() * B.inv()).trace() - (x ** 2 + y ** 2 + z ** 2 - x * y * z - 2)) == 0))
def leg(a, p): return 0 if a % p == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
for p in [q for q in range(3, 48) if all(q % d for d in range(2, int(q ** 0.5) + 1))]:
    cnt = [0] * p
    for u in range(p):
        for v in range(p):
            for w in range(p): cnt[(u * u + v * v + w * w - u * v * w - 2) % p] += 1
    cusp, nothing = cnt[(-2) % p], cnt[2 % p]
    others = sorted(set(cnt[k] - p * p for k in range(p) if k not in ((-2) % p, 2 % p)))
    print("K4: p = %2d: cusp (kappa=-2) %4d = p^2 %+d [p^2 + 3(-1/p)p + 1 = %d]; nothing (kappa=2) %4d = p^2 %+d; the other leaves: p^2 + %s; most populated kappa %s, least %s" % (
        p, cusp, cusp - p * p, p * p + 3 * leg(-1, p) * p + 1, nothing, nothing - p * p, others,
        sorted(k if k <= p // 2 else k - p for k in range(p) if cnt[k] == max(cnt)), sorted(k if k <= p // 2 else k - p for k in range(p) if cnt[k] == min(cnt))))
