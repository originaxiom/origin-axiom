"""Brute-force count of SL(2,Z)-classes of trace t via cycles of reduced indefinite forms (all forms, primitive or not),
and test where R^nL^n and K(E_N) land. Form of K=[[a,b],[c,d]]: (c, d-a, -b), disc t^2-4. Equivalence = proper (SL2Z)."""
import math, json, sys
def is_reduced(f, D):
    a, b, c = f; r = math.isqrt(D)
    return 0 < b <= r and r - b < 2 * abs(a) <= r + b if True else False
def rho(f, D):  # Gauss reduction step (right neighbour)
    a, b, c = f; r = math.sqrt(D); A = c
    # choose b' ≡ -b mod 2|c| with sqrt(D)-2|c| < b' < sqrt(D) when |c| < sqrt(D) else -|c| < b' <= |c|
    m = 2 * abs(c)
    if abs(c) < r:
        lo = r - m
        bp = -b % m
        while bp <= lo: bp += m
        while bp > r: bp -= m
        while bp <= lo: bp += m
    else:
        bp = -b % m
        if bp > abs(c): bp -= m
    return (c, bp, (bp * bp - D) // (4 * c))
def reduce(f, D):
    seen = 0
    while not is_red(f, D):
        f = rho(f, D); seen += 1
        if seen > 10000: raise RuntimeError
    return f
def is_red(f, D):
    a, b, c = f; r = math.sqrt(D)
    return 0 < b < r and r - b < 2 * abs(a) < r + b
def cycle(f, D):
    f = reduce(f, D); cyc = [f]; g = rho(f, D)
    while g != f:
        cyc.append(g); g = rho(g, D)
        if len(cyc) > 10000: raise RuntimeError
    return frozenset(cyc)
def form_of(K):
    (a, b), (c, d) = K
    return (c, d - a, -b)
def classes(t):
    D = t * t - 4; r = math.isqrt(D); cycs = set()
    for b in range(1, r + 1):
        if (b * b - D) % 4: continue
        ac = (b * b - D) // 4
        for a in range(-2 * r, 2 * r + 1):
            if a == 0 or ac % a: continue
            f = (a, b, ac // a)
            if is_red(f, D): cycs.add(cycle(f, D))
    return cycs
def matmul(X, Y): return [[sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def mpow(X, n):
    P = [[1, 0], [0, 1]]
    for _ in range(n): P = matmul(P, X)
    return P
L = [[1, 0], [1, 1]]; R = [[1, 1], [0, 1]]
def KE(N): return [[-2, 2 * N - 9], [-1, N - 5]]  # closed form, checked against ref_check.json
def KEH(N): return [[4, 27 - 4 * N], [1, 7 - N]]   # DHIZ-II (5.4)
out = {}
for t in [3, 4, 5, 6, 7, 11, 18]:
    cs = classes(t); D = t * t - 4
    lab = {i: sorted(c)[0] for i, c in enumerate(cs)}
    def which(K):
        cy = cycle(form_of(K), D)
        return [i for i, c in enumerate(cs) if c == cy]
    row = {"D": D, "n_classes": len(cs), "reps": {i: lab[i] for i in lab},
           "content of reps": {i: math.gcd(math.gcd(*lab[i][:2]), lab[i][2]) for i in lab},
           "K(E_{t+7})": which(KE(t + 7))}
    if 11 - t >= 0: row["K(E^H_{11-t})"] = which(KEH(11 - t))
    n = round(math.sqrt(t - 2))
    if n * n == t - 2: row["R^nL^n (n=%d)" % n] = which(matmul(mpow(R, n), mpow(L, n)))
    if t == 3: row["LR"] = which(matmul(L, R)); row["(LR)^-1"] = which([[2, -1], [-1, 1]]); row["RL"] = which(matmul(R, L))
    out[t] = row
print(json.dumps(out, indent=1, default=str))
json.dump(out, open(__import__("pathlib").Path(__file__).with_name("cycles.json"), "w"), indent=1, default=str)
