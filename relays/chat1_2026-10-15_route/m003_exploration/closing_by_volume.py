# EXPLORATION: rank the threads on which an order-N hypercharge line closes all three sectors (N^2 | Q_gamma(w)) by the
# hyperbolic volume of the punctured-torus bundle (SnapPy, 'b+<eps>word'), the record's action weight e^{-c Vol/6 pi}.
import math, warnings, snappy
warnings.filterwarnings("ignore")
exec(open("closing_threads.py").read().split("SECT =")[0])   # lyndon, mat, height
MAXLEN = 14
rows = []
for w in lyndon(MAXLEN):
    if len(w) < 2: continue
    A, B, C, D = mat(w)
    for N in (5, 7, 9, 11):
        for eps in (1, -1):
            closing = []
            for a in range(N):
                for b in range(N):
                    if (a, b) == (0, 0) or math.gcd(math.gcd(a, b), N) != 1: continue
                    if ((a*D + b*B) - eps*a) % N or ((a*C + b*A) - eps*b) % N: continue
                    Q = C*a*a + (A - D)*a*b - B*b*b
                    if (Q // N) % N == 0: closing.append((a, b))
            if closing:
                M = snappy.Manifold(f"b+{'+' if eps > 0 else '-'}{w}")
                rows.append((N, eps, float(M.volume()), w, height(w), len(closing), str(M.homology())))
for N in (5, 7, 9, 11):
    for eps in (1, -1):
        sel = sorted(r for r in rows if r[0] == N and r[1] == eps)[:4]
        print(f"N={N} eps={eps:+d}: least volume closing threads (length <= {MAXLEN}):")
        for r in sel:
            print(f"    {'+' if eps > 0 else '-'}{r[3]:16s} Vol {r[2]:.6f}  height {r[4]:.2f}  closing lines {r[5]}  H1 {r[6]}")
