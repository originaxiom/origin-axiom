"""B1814, A BLIND RERUN OF THE CENSUS (the rule: BLIND_RERUN_RULE.md, sealed c0259df7d).  This seat's own sampling code
for B1814's census steps 1-3, with fresh seeds; B1740's frame module (step 4) loaded unchanged from a checkout of main
with its sha256 asserted.  Writes census.jsonl and control.json in --out, with the keys B1814's compare.py reads.
Data-free.  The web seat, 2026-10-29.  0 of 19.

    python3 rerun_census.py --main <checkout of main> --out <dir> --workers 2
"""
import argparse, bisect, hashlib, importlib.util, json, math, pathlib, sys, warnings
from fractions import Fraction as Fr
from math import gcd
import numpy as np

B1740 = ("frontier/B1740_the_non_null_higgs_under_the_standard_models_reading/verification/census.py",
         "f5c874f7149752e33f5579d65a36a1213e1eaed5771f91c8d5bee34fcb40f5f1")
B1733 = ("frontier/B1733_the_threads_own_lines/verification/the_threads_own_lines.py",
         "c15c15a2be3e38f706c47fb104a0f10b73b7035810fd3c24f43da62a035e47a3")
B1726_ROW = ("frontier/B1726_the_two_ingredients_replicated/verification/census.jsonl",
             "d67432f0dc252e911514f211eb29844fd0bfcc5a270c00188312607435b0478d")
B1813_TRACE = ("frontier/B1813_the_weaves_own_measure_depends_on_how_its_threads_are_counted/verification/referee/check3_trace.json",
               "4ba94f8155a94c6355dc4f9f3afde533e39a1d2333ff1615c1ab8b8a979f074f")
NDRAW, NMOVE, TMAX, NLINE, YCAP = 4000, 16, 400, 12, 60.0
SEEDS = {"A0": 29101, "A1": 29102}
L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))
MAIN = None
_MOD = {}


def load(key):
    if key not in _MOD:
        rel, sha = {"b1740": B1740, "b1733": B1733}[key]
        p = MAIN / rel
        assert hashlib.sha256(p.read_bytes()).hexdigest() == sha, key
        name = {"b1740": "b1740_census_rerun", "b1733": "b1733_lines_rerun"}[key]
        sp = importlib.util.spec_from_file_location(name, p); m = importlib.util.module_from_spec(sp)
        sys.modules[name] = m; sp.loader.exec_module(m); _MOD[key] = m
    return _MOD[key]


def mm(X, Y):
    return ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]),
            (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))


def matrix(w):
    M = ((1, 0), (0, 1))
    for ch in w: M = mm(M, L if ch == "L" else R)
    return M


def lyndon_fkm(n):
    """all Lyndon words over {0 < 1} of length 1..n (Fredricksen-Kessler-Maiorana)"""
    w = [-1]
    while w:
        w[-1] += 1
        yield w[:]
        m = len(w)
        while len(w) < n: w.append(w[-m])
        while w and w[-1] == 1: w.pop()


def is_lyndon(w):
    """Duval: w is Lyndon iff its Lyndon factorisation is w itself"""
    n, i = len(w), 0
    j, k = 1, 0
    while j < n and w[k] <= w[j]:
        k = 0 if w[k] < w[j] else k + 1
        j += 1
    return k == 0 and j == n and n > 0


def classes_moves(n):
    out = []
    for t in lyndon_fkm(n):
        if 0 in t and 1 in t: out.append("".join("L" if c == 0 else "R" for c in t))
    return out


def classes_trace(T):
    """depth-first over positive words from L^k R (trace k + 2), pruned at trace T; keep the Lyndon words"""
    out = {}
    stack = []
    for k in range(1, T - 1):
        w = "L" * k + "R"; M = matrix(w)
        if M[0][0] + M[1][1] <= T: stack.append((w, M))
    while stack:
        w, M = stack.pop()
        t = M[0][0] + M[1][1]
        if is_lyndon(w): out[w] = t
        for ch, G in (("L", L), ("R", R)):
            M2 = mm(M, G)
            if M2[0][0] + M2[1][1] <= T: stack.append((w + ch, M2))
    return out


def axis(M):
    (a, b), (c, d) = M
    t = a + d; s = math.sqrt(t * t - 4.0)
    x1, x2 = ((a - d) + s) / (2 * c), ((a - d) - s) / (2 * c)
    return (x1 + x2) / 2, abs(x1 - x2) / 2, 2 * math.acosh(t / 2)


def reduce_z(z):
    """this seat's reduction: returns z' in the standard domain and gamma in SL(2, Z) with gamma z = z'"""
    g = ((1, 0), (0, 1))
    while True:
        n = round(z.real)
        if n: z -= n; g = mm(((1, -n), (0, 1)), g)
        if z.real < -0.5: z += 1; g = mm(((1, 1), (0, 1)), g)
        if z.real >= 0.5: z -= 1; g = mm(((1, -1), (0, 1)), g)
        if abs(z) < 1 - 1e-13:
            z = -1 / z; g = mm(((0, -1), (1, 0)), g)
        else:
            return z, g


def own_lines(M):
    (a, b), (c, d) = M; seen, out = set(), []
    for N in range(1, NLINE + 1):
        for p in range(N):
            for q in range(N):
                if gcd(gcd(p, q), N) != 1: continue
                u, v = (p * a + q * c) % N, (p * b + q * d) % N
                if (u, v) == (p, q) or (u, v) == ((-p) % N, (-q) % N):
                    key = min((Fr(p, N), Fr(q, N)), (Fr((-p) % N, N), Fr((-q) % N, N)))
                    if key not in seen: seen.add(key); out.append(key)
    return out


def transport(line, g):
    (p, q), (r, s) = g; al, b = line
    a2, b2 = (al * s - b * r) % 1, (-al * q + b * p) % 1
    return min((a2, b2), ((-a2) % 1, (-b2) % 1))


def mob(g, z): (p, q), (r, s) = g; return (p * z + q) / (r * z + s)


def arm_classes(arm):
    if arm == "A0":
        ws = classes_moves(NMOVE); tr = {w: sum(matrix(w)[i][i] for i in range(2)) for w in ws}
    else:
        tr = classes_trace(TMAX); ws = sorted(tr, key=lambda w: (tr[w], w))
    out = []
    for w in ws:
        M = matrix(w); m, r, ell = axis(M)
        out.append({"word": w, "M": M, "trace": tr[w], "m": m, "r": r, "ell": ell})
    return out


def draws():
    rows = []
    for arm, seed in SEEDS.items():
        cl = arm_classes(arm); cum = np.cumsum([c["ell"] for c in cl]); rng = np.random.default_rng(seed); cache = {}
        for i in range(NDRAW):
            k = int(np.searchsorted(cum, rng.random() * cum[-1], side="right")); c = cl[k]
            u = (rng.random() - 0.5) * c["ell"]
            z = complex(c["m"] + c["r"] * math.tanh(u), c["r"] / math.cosh(u))
            zr, g = reduce_z(z)
            if k not in cache: cache[k] = own_lines(c["M"])
            ln = cache[k][int(rng.integers(len(cache[k])))]
            al, bb = transport(ln, g)
            rows.append({"arm": arm, "i": i, "word": c["word"], "trace": c["trace"], "ell": c["ell"], "u": u,
                         "gamma": [list(g[0]), list(g[1])], "line_thread": [str(ln[0]), str(ln[1])],
                         "order": math.lcm(ln[0].denominator, ln[1].denominator), "n_lines": len(cache[k]),
                         "Re_tau": zr.real, "Im_tau": zr.imag, "alpha": str(al), "b": str(bb)})
    return rows


def point(t):
    if t["Im_tau"] > YCAP: return dict(t)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        r = load("b1740").compute(t["Re_tau"], t["Im_tau"], Fr(t["alpha"]), Fr(t["b"]), which="DR")
    r.update(t); r["warnings"] = sorted({str(x.message)[:80] for x in w}); return r


def at_cap(task):
    re_t, k = task; K = load("b1740"); a, b = K.lines()[k]
    with warnings.catch_warnings():
        warnings.simplefilter("error"); r = K.compute(re_t, YCAP, a, b, which="DR")
    return max(max(v) for key, v in r.items() if not key.startswith("ckm"))


def controls(pool):
    K = load("b1740"); out = {}
    ref = json.loads((MAIN / B1813_TRACE[0]).read_text())
    assert hashlib.sha256((MAIN / B1813_TRACE[0]).read_bytes()).hexdigest() == B1813_TRACE[1]
    out["C1a_trace_counts"] = {str(T): [len(classes_trace(T)), ref[str(T)]["classes"]] for T in (12, 18, 24, 30, 400)}
    out["C1a_move_count_14"] = [len(classes_moves(14)), 2536]
    out["R1_move_count_16"] = [len(classes_moves(16)), 8798]
    rng = np.random.default_rng(29103); worst = 0.0; same = True; nchk = 0
    OL = load("b1733")
    for arm in SEEDS:
        cl = arm_classes(arm)
        for _ in range(200):
            c = cl[int(rng.integers(len(cl)))]; u = (rng.random() - 0.5) * c["ell"]
            z = complex(c["m"] + c["r"] * math.tanh(u), c["r"] / math.cosh(u)); zr, g = reduce_z(z)
            worst = max(worst, abs(mob(g, z) - zr) / max(1.0, abs(zr)))
        for _ in range(300):
            c = cl[int(rng.integers(len(cl)))]; mine = set(own_lines(c["M"])); theirs = set()
            for N in range(1, NLINE + 1):
                for a, b in OL.fixed([list(c["M"][0]), list(c["M"][1])], N):
                    al, bb = Fr(a, N), Fr(b, N); theirs.add(min((al, bb), ((-al) % 1, (-bb) % 1)))
            same &= (mine == theirs); nchk += 1
    out["C1b_reduction_max_rel_err"] = worst
    out["R3_lines_equal_B1733"] = [bool(same), nchk]

    def dev(x, y):
        if any(v != v for v in list(x) + list(y)): return math.inf
        return max((abs(math.log(p / q)) for p, q in zip(x, y) if p > 1e-10 and q > 1e-10), default=0.0)
    S, T = ((0, -1), (1, 0)), ((1, 1), (0, 1))
    Ls = {"L_max": 0.69, "L_2": 2.7}; z = complex(0.21, 1.37); cov = 0.0; im_min = z.imag
    for g in (R, mm(T, S)):
        gz = mob(g, z); im_min = min(im_min, gz.imag); sh = math.log(abs(g[1][0] * z + g[1][1]))
        for ln in ((Fr(1, 5), Fr(2, 5)), (Fr(1, 3), Fr(1, 4))):
            x = K.compute(z.real, z.imag, *ln, Ls=Ls, which="DR"); a2, b2 = transport(ln, g)
            y = K.compute(gz.real, gz.imag, a2, b2, Ls={h: Ls[h] + sh for h in Ls}, which="DR")
            cov = max(cov, max(dev(x[k][:3] if k.startswith("ckm") else x[k], y[k][:3] if k.startswith("ckm") else y[k]) for k in x))
    out["C1c_covariance_R_TS_max_log"] = cov; out["C1c_least_Im_tau"] = im_min
    assert hashlib.sha256((MAIN / B1726_ROW[0]).read_bytes()).hexdigest() == B1726_ROW[1]
    rec = next(json.loads(l) for l in (MAIN / B1726_ROW[0]).read_text().splitlines()
               if l.strip() and json.loads(l)["line"] == 149 and json.loads(l)["Re_tau"] == 0.35 and json.loads(l)["Im_tau"] == 3.05)
    mine = K.compute(0.35, 3.05, *K.lines()[149], which="DR")
    out["C1d_against_B1726_row"] = max(dev(mine[k], rec[k]) for k in mine if k in rec)
    out["C1e_max_ratio_at_YCAP"] = max(pool.map(at_cap, [(x, k) for x in (0.05, 0.3) for k in range(266)], chunksize=4))
    return out


def main():
    global MAIN
    ap = argparse.ArgumentParser(); ap.add_argument("--main", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=1); ap.add_argument("--dry", action="store_true")
    A = ap.parse_args(); MAIN = pathlib.Path(A.main).resolve(); OUT = pathlib.Path(A.out).resolve()
    if A.dry:                                            # shapes and times only, no frame call
        import time; t0 = time.time(); n0 = len(classes_moves(14)); print("dry: classes built %.1fs" % (time.time() - t0)); return
    from multiprocessing import Pool
    T = draws()
    import os
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    with Pool(A.workers, initializer=_init, initargs=(str(MAIN),)) as P, open(OUT / "census.jsonl", "w") as f:
        for r in P.imap(point, T, chunksize=8):
            f.write(json.dumps(r) + "\n")
        c = controls(P)
    (OUT / "control.json").write_text(json.dumps(c, indent=1) + "\n")
    print("draws:", len(T), "| control:", json.dumps(c), flush=True)


def _init(m):
    global MAIN
    MAIN = pathlib.Path(m)


if __name__ == "__main__":
    main()
