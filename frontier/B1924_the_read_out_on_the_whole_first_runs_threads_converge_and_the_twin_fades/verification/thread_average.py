"""P-845's condition, first run: the frame's thread average at the mark for allowed words, with the invariant end.

A word w in L, R (matrices L = [[1,1],[0,1]], R = [[1,0],[1,1]]) is ALLOWED when it keeps the mark: W v = +-v mod 5, v = (1, 2)
(B1872, B1914; the frame's line (2/5, 4/5) is the same line). Its thread is the closed geodesic of gamma_w = W^T acting on
the modulus. Along one period the frame is evaluated at the mark (2/5, 4/5) with the end L = L~ - (1/2) log Im tau (the
invariant end, B1921); for accuracy each node is first carried into the fundamental domain by B1724's transport rules
(T^-n: (a, b) -> (a, b + n a); S: tau -> -1/tau, (a, b) -> (-b, a), L -> L + log|tau|), which leave the outputs unchanged
(covariance). A(w) = the arclength average over one period of the covariant readings' outputs (S and St; S* is not
periodic, B1922). Checks built in, named before the run: (1) window independence: two starts of the period agree;
(2) the mark kept: a word that does not keep it is refused. VALUES ARE WRITTEN TO THE JSON ONLY AND PRINTED NEVER; the
printout is structure only (window spreads, sample sizes). Main's code with B1724's frame."""
import sys, math, json, pathlib, random
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1724_the_readings_covariance" / "verification"))
import covariance as C

LM = np.array([[1, 1], [0, 1]]); RM = np.array([[1, 0], [1, 1]])
MARK = (0.4, 0.8)
LT = {"L_max": 1.3, "L_2": 0.9}                     # the invariant end L~, two conventions (B1724's two ends); held fixed


def word_matrix(w):
    M = np.eye(2, dtype=np.int64)
    for ch in w:
        M = M @ (LM if ch == "L" else RM)
    return M


def keeps_mark(w):
    M = word_matrix(w); v = np.array([1, 2])
    u = (M @ v) % 5
    return tuple(u) in ((1, 2), (4, 3))


def geodesic(w):
    a, b, c, d = (int(x) for x in word_matrix(w).T.ravel())     # gamma = W^T = [[a, b], [c, d]], z -> (a z + b)/(c z + d)
    tr = a + d; D = tr * tr - 4
    assert D > 0, "not hyperbolic"
    r1 = ((a - d) + math.sqrt(D)) / (2 * c); r2 = ((a - d) - math.sqrt(D)) / (2 * c)
    beta, betap = max(r1, r2), min(r1, r2)
    lam = (abs(tr) + math.sqrt(D)) / 2
    g = lambda z: (a * z + b) / (c * z + d)
    return beta, betap, 2 * math.log(lam), g


def reduce(t, a, b, Lend):
    for _ in range(200):
        n = round(t.real)
        if n:
            t = t - n; b = b + n * a
        if abs(t) < 1 - 1e-12:
            Lend = {h: Lend[h] + math.log(abs(t)) for h in Lend}
            t, a, b = -1 / t, -b, a
        else:
            return t, a % 1.0, b % 1.0, Lend
    raise RuntimeError("reduction did not end")


def outputs(t):
    Lend = {h: LT[h] - 0.5 * math.log(t.imag) for h in LT}
    tr, a, b, Lr = reduce(complex(t), MARK[0], MARK[1], Lend)
    out = C.frame(tr, a, b, Lr)
    return {k: v for k, v in out.items() if "conjS" not in k}


def thread_average(w, start=0.0, nodes=12):
    beta, betap, ell, g = geodesic(w)
    zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
    s0 = start * ell - ell / 2
    if abs(g(zt(s0)) - zt(s0 + ell)) > 1e-7 * (1 + abs(zt(s0))):
        ell = -ell
    # the trapezoid rule over one period: the integrand is periodic (checked pointwise to 1e-13), so the rule converges
    # spectrally; Gauss-Legendre (the first version) is not periodic-aware and left a window dependence of 0.1
    acc = None
    for j in range(nodes):
        o = outputs(zt(s0 + ell * j / nodes))
        if acc is None:
            acc = {k: np.zeros(len(v)) for k, v in o.items()}
        for k in acc:
            acc[k] += np.log(np.maximum(np.array(o[k]), 1e-300)) / nodes        # average of log ratios (scale-free)
    return {k: v.tolist() for k, v in acc.items()}, abs(ell)


def spread(A, B):
    return max(float(np.max(np.abs(np.array(A[k]) - np.array(B[k])))) for k in A)


if __name__ == "__main__":
    out = {"named": {}, "sample": {}}
    for name, w in (("the golden ground LR", "LR"), ("the run of 6 with one period", "LLLLLLRLR")):
        assert keeps_mark(w)
        A0, ell = thread_average(w, 0.0); A1, _ = thread_average(w, 0.37)
        out["named"][name] = {"word": w, "length": ell, "A": A0, "window spread": spread(A0, A1)}
        print("%s (%s): geodesic length %.3f; window independence: max |difference| of averaged log ratios %.1e" % (name, w, ell, spread(A0, A1)), flush=True)
    rng = random.Random(20261113)
    for n in (8, 10, 12):
        words = []
        while len(words) < 6:
            w = "".join(rng.choice("LR") for _ in range(n))
            if "L" in w and "R" in w and keeps_mark(w) and w not in words:
                words.append(w)
        rows = []
        for w in words:
            A, ell = thread_average(w, 0.0)
            rows.append({"word": w, "length": ell, "A": A})
        out["sample"][str(n)] = rows
        print("n = %d: %d allowed words sampled (lengths %.2f to %.2f); averages written, not printed" % (n, len(rows), min(r["length"] for r in rows), max(r["length"] for r in rows)), flush=True)
        (HERE / "thread_average.json").write_text(json.dumps(out, indent=1))
    (HERE / "thread_average.json").write_text(json.dumps(out, indent=1))
