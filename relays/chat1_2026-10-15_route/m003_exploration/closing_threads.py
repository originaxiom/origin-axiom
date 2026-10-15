# which threads (Lyndon words up to length 16, both signs) carry an order-N line w (N in 5,7,9,11) on which all three
# Standard Model sectors close, i.e. N^2 | Q_gamma(w) (law: phase exp(-2 pi i c (qL^2+qR^2)/N), c = eps Q_gamma(w)/N);
# their height (the geodesic's top, in the fundamental domain's reduction) and length.
import math
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
    # the geodesic's maximal height in the fundamental domain: sqrt(t^2-4) / (2 min over rotations of min(|B|,|C|))
    # (corrected after the referee: the first version used min |C| only, which gives impossible heights below sqrt(3)/2)
    best = None
    for i in range(len(w)):
        A, B, C, D = mat(w[i:] + w[:i])
        m = min(abs(B), abs(C))
        if best is None or m < best[0]: best = (m, A + D)
    c, t = best
    return math.sqrt(t*t - 4) / (2*c)
SECT = {"up": (1, -4), "down": (1, 2), "lepton": (-3, 6)}
found = {}
for w in lyndon(16):
    if len(w) < 2: continue
    A, B, C, D = mat(w)
    for N in (5, 7, 9, 11, 13):
        for eps in (1, -1):
            for a in range(N):
                for b in range(N):
                    if (a, b) == (0, 0) or math.gcd(math.gcd(a, b), N) != 1: continue
                    if ((a*D + b*B) - eps*a) % N or ((a*C + b*A) - eps*b) % N: continue
                    Q = C*a*a + (A - D)*a*b - B*b*b
                    c = eps * Q // N
                    closes = {s: (c*(qL*qL + qR*qR)) % N == 0 for s, (qL, qR) in SECT.items()}
                    if all(closes.values()):
                        key = (N, eps)
                        h = height(w)
                        if key not in found or (len(w), h) < (len(found[key][0]), found[key][1]):
                            found[key] = (w, h, (a, b), A + D)
for (N, eps), (w, h, line, t) in sorted(found.items()):
    print(f"N={N} eps={eps:+d}: shortest thread closing all three sectors: {('+' if eps > 0 else '-')}{w} (length {len(w)}, trace {t}, height {h:.2f}), line {line}/{N}")
# also: the lowest-height such thread per N, among all lengths <= 16
low = {}
for w in lyndon(16):
    if len(w) < 2: continue
    A, B, C, D = mat(w)
    for N in (5, 7, 9):
        for eps in (1, -1):
            ok = False
            for a in range(N):
                for b in range(N):
                    if (a, b) == (0, 0) or math.gcd(math.gcd(a, b), N) != 1: continue
                    if ((a*D + b*B) - eps*a) % N or ((a*C + b*A) - eps*b) % N: continue
                    Q = C*a*a + (A - D)*a*b - B*b*b
                    if (Q // N) % N == 0: ok = True
            if ok:
                h = height(w)
                if (N, eps) not in low or h < low[(N, eps)][1]: low[(N, eps)] = (w, h)
print("lowest-height closing thread (length <= 16):", {k: (v[0], round(v[1], 2)) for k, v in low.items()})
