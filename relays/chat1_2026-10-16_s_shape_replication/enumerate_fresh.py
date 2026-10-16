"""The replication's fresh configurations, by pure algebra (no mass): tlow_enum.py's closing rule (lines of exact
order N fixed up to sign, N^2 | Q_gamma(w)) on Lyndon words of length 13 and 14 at height <= 3 (T-low used length
<= 12, so no configuration is shared), grouped into classes by classes.py; each class is represented by its least
member in (word, line) order.
Usage: python3 -B enumerate_fresh.py > enumerate_fresh_run.txt   (writes fresh_configurations.json beside itself)"""
import json, math, os
from classes import mat, orbit
HERE = os.path.dirname(os.path.abspath(__file__))


def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()


def height(w):
    best = None
    for i in range(len(w)):
        A, B, C, D = mat(w[i:] + w[:i]); m = min(abs(B), abs(C))
        if best is None or m < best[0]: best = (m, A + D)
    c, t = best
    return math.sqrt(t * t - 4) / (2 * c)


def configs(N, lmin=13, lmax=14, hmax=3.0):
    rows = []
    for w in lyndon(lmax):
        if len(w) < lmin or "L" not in w or "R" not in w: continue
        h = height(w)
        if h > hmax: continue
        A, B, C, D = mat(w); seen = set()
        for a in range(N):
            for b in range(N):
                if math.gcd(math.gcd(a, b), N) != 1: continue
                key = min((a, b), ((-a) % N, (-b) % N))
                if key in seen: continue
                for eps in (1, -1):
                    if ((a * D + b * B) - eps * a) % N == 0 and ((a * C + b * A) - eps * b) % N == 0:
                        Q = C * a * a + (A - D) * a * b - B * b * b
                        if Q % (N * N) == 0:
                            seen.add(key); rows.append((w, round(h, 4), key, eps))
                        break
    return rows


if __name__ == "__main__":
    out = {}
    for N in (9, 11, 12):
        rows = configs(N)
        closing = {(w, key) for w, h, key, eps in rows}
        cls = {}
        for w, h, key, eps in rows:
            cls.setdefault(orbit(w, key, N), []).append((w, h, key, eps))
        bad = sum((w2, l2) not in closing for orb in cls for (w2, l2) in orb)
        reps = []
        for orb, mem in cls.items():
            mem = sorted(mem, key=lambda r: (r[0], r[2]))
            reps.append({"representative": [mem[0][0], mem[0][1], list(mem[0][2])], "members": [[m[0], list(m[2])] for m in mem]})
        reps.sort(key=lambda r: (r["representative"][0], r["representative"][2]))
        sizes = [len(r["members"]) for r in reps]
        print(f"N = {N}: {len(rows)} configurations in {len(reps)} classes (sizes: {sizes.count(4)} x 4, {sizes.count(2)} x 2, "
              f"{sizes.count(1)} x 1); images outside the closing set: {bad}; heights "
              f"{min(r[1] for r in rows)}..{max(r[1] for r in rows)}; lengths {sorted({len(r[0]) for r in rows})}")
        out[str(N)] = reps
    json.dump(out, open(os.path.join(HERE, "fresh_configurations.json"), "w"), indent=0)
