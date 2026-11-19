#!/usr/bin/env python3
"""B1638 -- P-031 (2026-11-19): is the golden identity special to discriminant 5?  B1638's I3 tested five other closed
geodesics (discriminants 12, 12, 21, 32, 96), two of whose N_M have content 2 and 4.  Here every primitive hyperbolic
class of the ruled branch (a positive word in L and R up to rotation, so a conjugacy class of SL(2, Z)) with discriminant
tr^2 - 4 <= 100 is tested:
  - N_M = [[d - a, -2b], [2c, d - a]] (det = the discriminant) and its content gcd(d - a, 2b, 2c);
  - H_M^(k)(tau) = sum_p (theta_p/eta)^k(tau) (theta_p/eta)^k(N_M tau) at weights k = 1, 2 (B1638's) and 4, at six points
    tau with Im tau in [0.5, 2.5] and Im(N_M tau) >= 0.08, at 30 digits;
  - its spread over the points (relative to its size): a constant has spread below 1e-20.
B1638's own functions (theta series, eta product, N_M) are used as written there, at 30 digits.  Data-free.
    python3 -B discriminants_to_100.py > discriminants_to_100_run.txt"""
import json, pathlib, random, math
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 30


def gk(t, k):
    e = lambda x: mp.exp(1j * mp.pi * t * x)
    K = 60
    th2 = mp.fsum(e((n + mp.mpf(1) / 2) ** 2) for n in range(-K, K))
    th3 = mp.fsum(e(n * n) for n in range(-K, K + 1))
    th4 = mp.fsum((-1) ** abs(n) * e(n * n) for n in range(-K, K + 1))
    eta = mp.exp(1j * mp.pi * t / 12) * mp.fprod(1 - mp.exp(2j * mp.pi * t * n) for n in range(1, 500))
    return [(th / eta) ** k for th in (th2, th3, th4)]


def mob(M, t): return (M[0][0] * t + M[0][1]) / (M[1][0] * t + M[1][1])
def N_of(M): a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]; return [[d - a, -2 * b], [2 * c, d - a]]
def mul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
L = [[1, 1], [0, 1]]; R = [[1, 0], [1, 1]]


def classes(maxtr=10, maxlen=14):
    seen, out = set(), []
    for n in range(2, maxlen + 1):
        for bits in range(2 ** n):
            w = "".join("L" if (bits >> i) & 1 else "R" for i in range(n))
            if "L" not in w or "R" not in w: continue
            rots = [w[i:] + w[:i] for i in range(n)]; c = min(rots)
            if c in seen: continue
            M = [[1, 0], [0, 1]]
            for ch in c: M = mul(M, L if ch == "L" else R)
            tr = M[0][0] + M[1][1]
            if tr > maxtr: continue
            # primitive: the word is not a proper power
            if any(n % p == 0 and c == c[:n // p] * p for p in range(2, n + 1)): continue
            seen.add(c); out.append((c, M, tr))
    return out


def main():
    rnd = random.Random(31)
    rows = []
    for w, M, tr in sorted(classes(), key=lambda x: (x[2], x[0])):
        N = N_of(M); content = math.gcd(math.gcd(abs(N[0][0]), abs(N[0][1])), abs(N[1][0]))
        pts = []
        while len(pts) < 6:
            t = mp.mpc(rnd.uniform(-0.5, 0.5), rnd.uniform(0.5, 2.5))
            if mp.im(mob(N, t)) >= 0.08: pts.append(t)
        r = {"word": w, "trace": tr, "disc": tr * tr - 4, "N": N, "content": content}
        for k in (1, 2, 4):
            vals = [mp.fsum(a * b for a, b in zip(gk(t, k), gk(mob(N, t), k))) for t in pts]
            size = max(abs(v) for v in vals)
            r["spread_k%d" % k] = float(max(abs(v - vals[0]) for v in vals) / size)
            r["value_k%d" % k] = complex(vals[0])
        rows.append(r)
        print("%-12s tr %2d disc %3d content %d  spread k=1 %.1e  k=2 %.1e  k=4 %.1e  H2(first) %s" % (
            w, tr, tr * tr - 4, content, r["spread_k1"], r["spread_k2"], r["spread_k4"], mp.nstr(mp.mpc(r["value_k2"]), 8)), flush=True)
    const = [(r["word"], r["disc"], k) for r in rows for k in (1, 2, 4) if r["spread_k%d" % k] < 1e-20]
    print("classes: %d (discriminants %s)" % (len(rows), sorted({r["disc"] for r in rows})))
    print("constant (spread < 1e-20): %s" % const)
    print("discriminants with a constant: %s" % sorted({d for _, d, _ in const}))
    json.dump(rows, open(HERE / "discriminants_to_100.json", "w"), indent=1, default=str)


if __name__ == "__main__":
    main()
