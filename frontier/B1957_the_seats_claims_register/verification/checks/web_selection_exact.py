"""B1957: the web seat's report on the selection principle (2026-10-14): its exact, data-free parts, on main.
The frame outputs of the report (the thread frame's ratios, the height law) are NOT recomputed here.
 E1  the threads: primitive cyclic words in L, R with both letters (Lyndon words), lengths 2 to 12, 16 and 18:
     745, 8,798 and 31,040.
 E2  the residual act (its section 4b): W modulo 2 in SL(2, F_2) = S_3 acts on the three half-periods.  A word of odd
     length is a transposition (L and R are transpositions, so the sign is (-1)^length); a word of even length is the
     identity or a 3-cycle, and it is a 3-cycle exactly when its trace is odd.  Checked on all 31,040.
     To length 8, up to the exchange of the letters: the three classes number 16, 13 and 8 (B1602's census).
 E3  the reversal: M(reverse w) = F M(w)^-1 F with F = diag(-1, 1), on every word to length 12 (8,190 words).
 E4  the orbit-space theorem (its section 2a), numerically: on the sphere |a| = 1 in C^3, V = g |a.a|^2 + Re(b a.a)
     has its minimum at |a.a| = |b|/(2g) for |b| < 2g (10^5 random points and a direct minimisation), and at the ends
     0 or 1 when b = 0.
 E5  two curvatures it quotes at omega: log(y |eta|^4) has -1/3 and E(tau, 3) has +8.28 (half the Hessian's
     eigenvalue), so their ratio is 24.85."""
import itertools, functools, random, math
import mpmath as mp
print = functools.partial(print, flush=True)
Lm = ((1, 1), (0, 1)); Rm = ((1, 0), (1, 1)); F = ((-1, 0), (0, 1)); ONE = ((1, 0), (0, 1))
mul = lambda X, Y: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
inv = lambda X: ((X[1][1], -X[0][1]), (-X[1][0], X[0][0]))                     # determinant 1
M = lambda u: functools.reduce(mul, [Lm if c == "L" else Rm for c in u], ONE)


def lyndon(n):
    """binary Lyndon words of length n (Duval), as strings over L < R, both letters present for n >= 2"""
    w = [0]; out = []
    while w:
        if len(w) == n: out.append("".join("LR"[c] for c in w))
        w = (w * (n // len(w) + 1))[:n]
        while w and w[-1] == 1: w.pop()
        if w: w[-1] = 1
    return [x for x in out if "L" in x and "R" in x]


def cls(w):
    A = M(w); m2 = tuple(tuple(v % 2 for v in r) for r in A)
    if m2 == ONE: return "identity"
    return "3-cycle" if (A[0][0] + A[1][1]) % 2 == 1 else "transposition"


if __name__ == "__main__":
    words = {n: lyndon(n) for n in range(2, 19)}
    tot = lambda a, b: sum(len(words[n]) for n in range(a, b + 1))
    print("E1: threads of length 2 to 12: %d; to 16: %d; to 18: %d" % (tot(2, 12), tot(2, 16), tot(2, 18)))
    ok_odd = ok_trace = True; counts = {"identity": 0, "3-cycle": 0, "transposition": 0}
    for n in range(2, 19):
        for w in words[n]:
            c = cls(w); counts[c] += 1; A = M(w)
            ok_odd &= (c == "transposition") == (n % 2 == 1); ok_trace &= (c == "3-cycle") == ((A[0][0] + A[1][1]) % 2 == 1)
    print("E2: on all %d: a transposition exactly at odd length: %s; a 3-cycle exactly at odd trace: %s; the classes: %s" % (tot(2, 18), ok_odd, ok_trace, counts))
    sw = str.maketrans("LR", "RL"); canon = lambda w: min(min(w[i:] + w[:i] for i in range(len(w))), min((w.translate(sw))[i:] + (w.translate(sw))[:i] for i in range(len(w))))
    up = {}
    for n in range(2, 9):
        for w in words[n]: up[canon(w)] = cls(w)
    c8 = {k: sum(1 for v in up.values() if v == k) for k in ("3-cycle", "transposition", "identity")}
    print("E2: to length 8, up to the exchange of the letters: %d threads; 3-cycle (odd trace) %d, transposition (odd length) %d, identity %d" % (len(up), c8["3-cycle"], c8["transposition"], c8["identity"]))
    n_rev = 0; ok = True
    for n in range(1, 13):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t); n_rev += 1; ok &= M(w[::-1]) == mul(mul(F, inv(M(w))), F)
    print("E3: M(reverse w) = F M(w)^-1 F on %d words of length 1 to 12: %s" % (n_rev, ok))
    random.seed(5); g = 1.0; res = []
    for b in (0.0, 0.3, 1.1, 1.9):
        best = None
        for _ in range(100000):
            v = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(3)]; nrm = math.sqrt(sum(abs(z) ** 2 for z in v)); v = [z / nrm for z in v]
            s = sum(z * z for z in v); val = g * abs(s) ** 2 + (b * s).real
            if best is None or val < best[0]: best = (val, abs(s))
        res.append((b, round(best[1], 3), b / (2 * g), round(best[0], 4), -b * b / (4 * g)))
    print("E4: (b, |a.a| at the least value found, |b|/2g, the least value, -b^2/4g): %s" % res)
    import pathlib as _pl, sys as _sys; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))          # the sibling below is found in isolated mode too (the web seat's section 9, 2026-11-18)
    import web_weave_action_on_tau as W
    h1 = W.grad_hess(W.f_eta, W.OM)[1]; h3 = W.grad_hess(lambda x, y: W.E_fourier(mp.mpc(x, y), mp.mpf(3)), W.OM)[1]
    print("E5: at omega: half the Hessian of log(y |eta|^4): %.4f, %.4f; of E(tau, 3): %.4f, %.4f; the ratio: %.2f" % (h1[0] / 2, h1[1] / 2, h3[0] / 2, h3[1] / 2, -h3[0] / h1[0]))
