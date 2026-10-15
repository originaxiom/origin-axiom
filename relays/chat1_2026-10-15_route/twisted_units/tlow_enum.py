"""T-low's configurations, by pure algebra (no mass): Lyndon words in L, R up to length 12, height <= 3; lines w of
exact order N (N = 9, 11, 12) fixed up to sign (w gamma = +-w mod N, chat1's (a, b) row convention of the 13:40
addendum), with N^2 | Q_gamma(w), Q = C a^2 + (A - D) a b - B b^2: the charge-independent closing set (c = 0 mod N)."""
import math, json
def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()
def mat(w):
    A, B, C, D = 1, 0, 0, 1
    for ch in w:
        if ch == "L": A, B, C, D = A + B, B, C + D, D
        else: A, B, C, D = A, A + B, C, C + D
    return A, B, C, D
def height(w):
    best = None
    for i in range(len(w)):
        A, B, C, D = mat(w[i:] + w[:i]); m = min(abs(B), abs(C))
        if best is None or m < best[0]: best = (m, A + D)
    c, t = best
    return math.sqrt(t * t - 4) / (2 * c)
out = {}
for N in (9, 11, 12):
    rows = []
    for w in lyndon(12):
        if len(w) < 2 or "L" not in w or "R" not in w: continue
        h = height(w)
        if h > 3.0: continue
        A, B, C, D = mat(w)
        seen = set()
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
    out[N] = rows
    words = sorted(set(r[0] for r in rows), key=lambda x: (len(x), x))
    print(f"N = {N}: {len(rows)} (word, line) configurations on {len(words)} words; heights {min([r[1] for r in rows], default=None)}..{max([r[1] for r in rows], default=None)}; lengths {sorted(set(len(x) for x in words))}")
json.dump({str(k): v for k, v in out.items()}, open("tlow_configurations.json", "w"), indent=0)
