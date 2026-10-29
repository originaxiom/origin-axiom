"""B1814 (P-437, stage 3 of the owner's whole-existence computation): the census (no data).  Draws from the weave's own
measure under each of B1813's two clocks, each draw carried through B1656's frame by B1740's sealed census module.

One draw:
  1. a thread (a primitive positive class with both letters), chosen with probability proportional to its geodesic
     length l = 2 arccosh(t / 2) -- B1813's arclength mass;
       A0, the move clock:      every class of word length 2-16 (B1813's move table; converged by n = 12);
       A1, the geometric clock: every class of trace 3-400 (B1813's trace table, the referee's enumeration; 0.315 of
                                the height tail above 3 against hyperbolic area's 0.318);
  2. a uniform arclength point z on its closed geodesic (the axis of its matrix A, GENESIS's L = [[1,1],[0,1]],
     R = [[1,0],[1,1]]), reduced to the standard fundamental domain by gamma (z' = gamma z, tracked exactly);
  3. one of the thread's own flat lines (B1733's rule: (a, b) A = +-(a, b) mod N), uniformly among those of exact order
     1-12 up to sign, carried to z' by the frame's covariance (a, b) -> (a, b) gamma^-1 (B1724; B1733 section 1);
  4. B1740's compute(z', line, which="DR") unchanged: every sector in S and S~ at both horocycles (B1667's radii as
     B1740 reads them: interpolated in Im tau from the Re tau = 1/4 column, held at its end values outside [1, 4]), and
     the CKM for each (up, down) reading pair.
  5. a draw above Im tau = YCAP = 60 is not computed (B1740's module overflows near Im tau = 120, and at Im tau = 60
     every ratio of every line is below 1e-12 -- control C1e): the comparison sets its ratios to its floor.
4 000 draws per arm.  Seeds 18140 (A0) and 18141 (A1).  Checkpointed: each draw is appended to census.jsonl as it
completes; a rerun skips the draws done.  The controls are written to control.json.
    OPENBLAS_NUM_THREADS=1 nice -n 10 python3 -B census.py --workers 8
Importing computes nothing."""
import sys, json, math, bisect, hashlib, importlib.util, itertools, random, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OUT = HERE / "census.jsonl"
SRC = {
    "b1740": (ROOT / "frontier" / "B1740_the_non_null_higgs_under_the_standard_models_reading" / "verification" / "census.py",
              "f5c874f7149752e33f5579d65a36a1213e1eaed5771f91c8d5bee34fcb40f5f1"),
    "b1733": (ROOT / "frontier" / "B1733_the_threads_own_lines" / "verification" / "the_threads_own_lines.py",
              "c15c15a2be3e38f706c47fb104a0f10b73b7035810fd3c24f43da62a035e47a3"),
}
B1726_CENSUS = (ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification" / "census.jsonl",
                "d67432f0dc252e911514f211eb29844fd0bfcc5a270c00188312607435b0478d")
B1813_TRACE = (ROOT / "frontier" / "B1813_the_weaves_own_measure_depends_on_how_its_threads_are_counted" / "verification" / "referee" / "check3_trace.json",
               "4ba94f8155a94c6355dc4f9f3afde533e39a1d2333ff1615c1ab8b8a979f074f")
NDRAW, NMOVE, TMAX, NLINE, YCAP = 4000, 16, 400, 12, 60.0
ARMS = {"A0": 18140, "A1": 18141}
LG, RG = ((1, 1), (0, 1)), ((1, 0), (1, 1))
_M = {}


def _load(key):
    if key not in _M:
        path, sha = SRC[key]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == sha, key
        name = {"b1740": "b1740_census", "b1733": "b1733_lines"}[key]
        sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp)
        sys.modules[name] = m; sp.loader.exec_module(m); _M[key] = m
    return _M[key]


def mul(X, Y): return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def word_mat(w):
    M = ((1, 0), (0, 1))
    for ch in w: M = mul(M, LG if ch == "L" else RG)
    return M


def canon(w): return min(w[i:] + w[:i] for i in range(len(w)))


def primitive(w): k = len(w); return not any(w == w[:p] * (k // p) for p in range(1, k) if k % p == 0)


def classes_by_moves(n):
    """every primitive positive class with both letters, word length 2..n (B1720's necklaces)"""
    out = set()
    for k in range(2, n + 1):
        for t in itertools.product("LR", repeat=k):
            w = "".join(t)
            if "L" in w and "R" in w and primitive(w): out.add(canon(w))
    return sorted(out, key=lambda s: (len(s), s))


def word_of(a, b, c, d):
    w = []
    while (a, b, c, d) != (1, 0, 0, 1):
        if a >= c and b >= d: w.append("L"); a, b = a - c, b - d
        else: w.append("R"); c, d = c - a, d - b
        assert min(a, b, c, d) >= 0
    return "".join(w)


def classes_by_trace(T):
    """every primitive positive class with both letters, trace 3..T (the B1813 referee's enumeration, check 3)"""
    out = {}
    for t in range(3, T + 1):
        for a in range(1, t):
            d = t - a; n = a * d - 1
            if n < 1: continue
            for b in range(1, n + 1):
                if n % b: continue
                w = word_of(a, b, n // b, d); cw = canon(w)
                if primitive(cw): out[cw] = t
    return sorted(out, key=lambda s: (out[s], s))


def own_lines(M):
    """the thread's flat lines of exact order 1..NLINE up to sign, as (alpha, b) in [0, 1)^2 (B1740's key)"""
    OL = _load("b1733"); seen = set(); out = []
    for N in range(1, NLINE + 1):
        for a, b in OL.fixed([list(M[0]), list(M[1])], N):
            al, bb = Fr(a, N), Fr(b, N); key = min((al, bb), ((-al) % 1, (-bb) % 1))
            if key not in seen: seen.add(key); out.append(key)
    return out


def axis(M):
    a, b, c, d = (float(x) for x in (M[0][0], M[0][1], M[1][0], M[1][1])); t = a + d
    disc = (d - a) ** 2 + 4 * b * c; r1 = ((a - d) + math.sqrt(disc)) / (2 * c); r2 = ((a - d) - math.sqrt(disc)) / (2 * c)
    return (r1 + r2) / 2, abs(r1 - r2) / 2, 2 * math.acosh(abs(t) / 2)


def reduce_track(z):
    """z' = gamma z in the standard fundamental domain, with gamma in SL(2, Z) (B1813's reduction, tracked)"""
    g = ((1, 0), (0, 1))
    for _ in range(100000):
        k = math.floor(z.real + 0.5)
        z = complex(z.real - k, z.imag); g = mul(((1, -k), (0, 1)), g)
        if abs(z) < 1 - 1e-12: z = -1 / z; g = mul(((0, -1), (1, 0)), g)
        else: return z, g
    raise RuntimeError("reduction did not terminate")


def transport(line, g):
    """(alpha, b) -> (alpha, b) gamma^-1 mod 1, canonical up to sign"""
    (p, q), (r, s) = g; al, b = line                      # gamma^-1 = [[s, -q], [-r, p]]
    a2, b2 = (al * s - b * r) % 1, (-al * q + b * p) % 1
    return min((a2, b2), ((-a2) % 1, (-b2) % 1))


def mobius(g, z): (p, q), (r, s) = g; return (p * z + q) / (r * z + s)


def arm_classes(arm):
    ws = classes_by_moves(NMOVE) if arm == "A0" else classes_by_trace(TMAX)
    out = []
    for w in ws:
        M = word_mat(w); m, r, ell = axis(M)
        out.append({"word": w, "M": M, "trace": M[0][0] + M[1][1], "m": m, "r": r, "ell": ell})
    return out


def tasks():
    out = []
    for arm, seed in ARMS.items():
        cl = arm_classes(arm); cum = list(itertools.accumulate(c["ell"] for c in cl)); rng = random.Random(seed)
        lines_cache = {}
        for i in range(NDRAW):
            k = bisect.bisect_right(cum, rng.random() * cum[-1]); c = cl[k]
            u = rng.random() * c["ell"]; z = complex(c["m"] + c["r"] * math.tanh(u), c["r"] / math.cosh(u))
            zr, g = reduce_track(z)
            if k not in lines_cache: lines_cache[k] = own_lines(c["M"])
            ln = lines_cache[k][rng.randrange(len(lines_cache[k]))]
            al, bb = transport(ln, g)
            out.append({"arm": arm, "i": i, "word": c["word"], "trace": c["trace"], "ell": c["ell"], "u": u,
                        "gamma": [list(g[0]), list(g[1])], "line_thread": [str(ln[0]), str(ln[1])],
                        "order": math.lcm(ln[0].denominator, ln[1].denominator), "n_lines": len(lines_cache[k]),
                        "Re_tau": zr.real, "Im_tau": zr.imag, "alpha": str(al), "b": str(bb)})
    return out


def point(t):
    """the frame at the draw; every numpy warning raised in the call is recorded on the row"""
    import warnings
    if t["Im_tau"] > YCAP: return dict(t)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        r = _load("b1740").compute(t["Re_tau"], t["Im_tau"], Fr(t["alpha"]), Fr(t["b"]), which="DR")
    r.update(t); r["warnings"] = sorted({str(x.message)[:80] for x in w}); return r


def at_cap(task):
    """C1e: the largest ratio of any sector, reading and horocycle at Im tau = YCAP on one of B1713's 266 lines (B1740's
    lines()), with every numpy warning an error"""
    import warnings
    re_t, k = task; K = _load("b1740"); a, b = K.lines()[k]
    with warnings.catch_warnings():
        warnings.simplefilter("error"); r = K.compute(re_t, YCAP, a, b, which="DR")
    return max(max(v) for key, v in r.items() if not key.startswith("ckm"))


def control(pool):
    """C1 (a) the class counts: trace <= 12, 18, 24, 30, 400 against B1813 (29, 60, 96, 151) and its referee's check 3;
    the move classes of length <= 14 against B1813's 2 536.  (b) the reduction: |gamma z - z'| over 200 draws per arm.
    (c) the covariance the transport uses, at fixed radii: compute(z, line) against compute(gamma z, line gamma^-1), with
    gamma = R and gamma = TS (Im tau changes; the images stay above Im tau = 0.31, B1724's bound), with B1667's radius
    law L -> L + log|c tau + d| (B1724), at two lines, every key, max |log| (a NaN fails it).  (d) B1740's compute with DR reproduces
    B1726's stored row at (0.35 + 3.05i, its line 149).  (e) at Im tau = YCAP, Re tau in {0.05, 0.3}, every one of the
    266 lines: the largest ratio, below 1e-12, with no numpy warning."""
    K = _load("b1740"); out = {}
    assert hashlib.sha256(B1813_TRACE[0].read_bytes()).hexdigest() == B1813_TRACE[1]
    ref = json.loads(B1813_TRACE[0].read_text(encoding="utf-8"))
    out["C1a_trace_counts"] = {str(T): [len(classes_by_trace(T)), ref[str(T)]["classes"]] for T in (12, 18, 24, 30, 400)}
    out["C1a_move_count_14"] = [len(classes_by_moves(14)), 2536]
    rng = random.Random(1814); worst = 0.0
    for arm in ARMS:
        cl = arm_classes(arm)
        for _ in range(200):
            c = cl[rng.randrange(len(cl))]; u = rng.random() * c["ell"]
            z = complex(c["m"] + c["r"] * math.tanh(u), c["r"] / math.cosh(u)); zr, g = reduce_track(z)
            worst = max(worst, abs(mobius(g, z) - zr) / max(1.0, abs(zr)))
    out["C1b_reduction_max_rel_err"] = worst
    def dev(x, y):
        if any(v != v for v in list(x) + list(y)): return math.inf
        return max((abs(math.log(p / q)) for p, q in zip(x, y) if p > 1e-10 and q > 1e-10), default=0.0)
    S, T, Rm = ((0, -1), (1, 0)), ((1, 1), (0, 1)), ((1, 0), (1, 1))
    Ls = {"L_max": 0.69, "L_2": 2.7}; z = complex(0.21, 1.37); cov = 0.0; im_min = z.imag
    for g in (Rm, mul(T, S)):
        gz = mobius(g, z); im_min = min(im_min, gz.imag); sh = math.log(abs(g[1][0] * z + g[1][1]))
        for ln in ((Fr(1, 5), Fr(2, 5)), (Fr(1, 3), Fr(1, 4))):
            x = K.compute(z.real, z.imag, *ln, Ls=Ls, which="DR"); a2, b2 = transport(ln, g)
            y = K.compute(gz.real, gz.imag, a2, b2, Ls={h: Ls[h] + sh for h in Ls}, which="DR")
            cov = max(cov, max(dev(x[k][:3] if k.startswith("ckm") else x[k], y[k][:3] if k.startswith("ckm") else y[k]) for k in x))
    out["C1c_covariance_R_TS_max_log"] = cov; out["C1c_least_Im_tau"] = im_min
    assert hashlib.sha256(B1726_CENSUS[0].read_bytes()).hexdigest() == B1726_CENSUS[1]
    rec = None
    for l in B1726_CENSUS[0].read_text(encoding="utf-8").splitlines():
        r = json.loads(l)
        if r["line"] == 149 and r["Re_tau"] == 0.35 and r["Im_tau"] == 3.05: rec = r; break
    mine = K.compute(0.35, 3.05, *K.lines()[149], which="DR")
    assert not any(v != v for k in mine for v in mine[k])
    out["C1d_against_B1726_row"] = max(dev(mine[k], rec[k]) for k in mine if k in rec)
    out["C1e_max_ratio_at_YCAP"] = max(pool.map(at_cap, [(x, k) for x in (0.05, 0.3) for k in range(266)], chunksize=4))
    return out


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    done = set()
    if OUT.exists():
        good = []
        for l in OUT.read_text(encoding="utf-8").splitlines():
            try: r = json.loads(l)
            except ValueError: continue                      # a line cut by an interrupted run: dropped, the draw redone
            done.add((r["arm"], r["i"])); good.append(l)
        OUT.write_text("".join(x + "\n" for x in good), encoding="utf-8")
    T = tasks(); todo = [t for t in T if (t["arm"], t["i"]) not in done]
    print(len(T), "draws;", len(done), "done;", len(todo), "to do", flush=True)
    with Pool(nw) as P, open(OUT, "a", encoding="utf-8") as f:
        for r in P.imap_unordered(point, todo, chunksize=4):
            f.write(json.dumps(r) + "\n"); f.flush()
        c = control(P)
    (HERE / "control.json").write_text(json.dumps(c, indent=1) + "\n", encoding="utf-8")
    print("control:", json.dumps(c), flush=True)


if __name__ == "__main__":
    main()
