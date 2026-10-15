# EXPLORATION: least-volume closing threads among words L^a R^b and L^a R^b L^c R^d (exponents <= 30 and <= 12),
# for N = 5, 7, 9, 11 and both signs; closing = an order-N line with N^2 | Q_gamma(w).
import math, warnings, snappy, itertools
warnings.filterwarnings("ignore")
def mat(w):
    A, B, C, D = 1, 0, 0, 1
    for ch in w:
        if ch == "L": A, B, C, D = A + B, B, C + D, D
        else: A, B, C, D = A, A + B, C, C + D
    return A, B, C, D
def closing(w, N, eps):
    A, B, C, D = mat(w); out = 0
    for a in range(N):
        for b in range(N):
            if (a, b) == (0, 0) or math.gcd(math.gcd(a, b), N) != 1: continue
            if ((a*D + b*B) - eps*a) % N or ((a*C + b*A) - eps*b) % N: continue
            Q = C*a*a + (A - D)*a*b - B*b*b
            if (Q // N) % N == 0: out += 1
    return out
words = ["L"*a + "R"*b for a in range(1, 31) for b in range(a, 31)]
words += ["L"*a + "R"*b + "L"*c + "R"*d for a, b, c, d in itertools.product(range(1, 13), repeat=4)
          if (a, b) <= (c, d)]
best = {}
for w in words:
    for N in (5, 7, 9, 11):
        for eps in (1, -1):
            n = closing(w, N, eps)
            if not n: continue
            key = (N, eps)
            M = snappy.Manifold(f"b+{'+' if eps > 0 else '-'}{w}")
            v = float(M.volume())
            best.setdefault(key, []).append((v, w, n, str(M.homology())))
for key in sorted(best):
    lst = sorted(set(best[key]))[:3]
    print(f"N={key[0]} eps={key[1]:+d}:", "; ".join(f"{w} Vol {v:.5f} lines {n} H1 {h}" for v, w, n, h in lst), flush=True)
