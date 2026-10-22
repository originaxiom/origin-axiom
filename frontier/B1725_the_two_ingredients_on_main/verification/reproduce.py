"""B1725 (P-293), part A: the web seat's TWO_INGREDIENTS census reproduced on main.  A random sample of its points (seed
1724) is recomputed here with main's frame functions (B1656's, B1691's S, B1667's end read from its Re tau = 1/4 column,
as B1712, B1720 and B1723 read it) in this arc's own loop: every sector in every reading (S, S~ = eps S* eps^T, S*), both
horocycles, and the CKM (V = U_u^H U_d, ascending mass) for every (up, down) reading pair.  Each stored value is compared:
the ratios by |log| (values below 1e-10 not compared, both must be below), the moduli by |log|, J by absolute difference.
    python3 -B reproduce.py [--workers 8] [--n 48]      # writes reproduce.json beside itself
Importing computes nothing."""
import sys, io, json, math, random, hashlib, contextlib, importlib.util, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
CENSUS = HERE.parent / "received" / "two_ingredients_census.jsonl"
CENSUS_SHA = "f379a4b8cfe2966d9d067abff323f6f654560d589c1d55f55320d816d59c5c4b"
RD = ("S", "St", "conjS")
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
_M = {}


def _modules():
    """B1656's functions (B1723's verbatim copy), B1691's S, B1667's column; loaded on first use"""
    if not _M:
        sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); _argv = sys.argv; sys.argv = ["x"]
        import b1656_funcs as B
        sys.argv = _argv
        P1691 = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
        sys.path.insert(0, str(P1691))
        spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
        col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads((ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text(encoding="utf-8"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
        _M.update(B=B, te=te, col=col)
    return _M


def lines():
    """B1713's 266 flat lines of exact order 1-12 up to sign, in its order (orders 1-7, then 8-12)"""
    from fractions import Fraction as Fr
    def block(lo, hi):
        seen, out = set(), []
        for N in range(lo, hi + 1):
            for j in range(N):
                for k in range(N):
                    if math.gcd(math.gcd(j, k), N) != 1: continue
                    a, b = Fr(j, N), Fr(k, N); key = min((a, b), ((-a) % 1, (-b) % 1))
                    if key in seen: continue
                    seen.add(key); out.append(key)
        return out
    return block(1, 7) + block(8, 12)


def compute(re_t, im_t, a, b):
    import mpmath as mp
    M = _modules(); B, te, col = M["B"], M["te"], M["col"]
    t = complex(re_t, im_t); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    reading = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    out, Y = {}, {}
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for h, k in (("L_max", 1), ("L_2", 2)):
            L = float(np.interp(t.imag, [q[0] for q in col], [q[k] for q in col]))
            u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
            Mw = B.weighted_M(u)
            for rn in RD:
                Ym = B.coupling(reading[rn], Mw); Y[(sec, h, rn)] = Ym
                sv = np.linalg.svd(Ym, compute_uv=False); out["%s|%s|%s" % (sec, h, rn)] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    for h in ("L_max", "L_2"):
        for ru in RD:
            for rd in RD:
                Uu = np.linalg.svd(Y[("up", h, ru)])[0][:, ::-1]; Ud = np.linalg.svd(Y[("down", h, rd)])[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
                J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
                out["ckm|%s|%s|%s" % (h, ru, rd)] = [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2])), J]
    return out


def compare(stored, mine):
    """max |log| over ratios and moduli (both below 1e-10: equal; one below: a mismatch), max |dJ|"""
    dl, dj, keys = 0.0, 0.0, 0
    for k, v in mine.items():
        s = stored[k]; keys += 1
        vals = list(zip(s[:3], v[:3])) if k.startswith("ckm") else list(zip(s, v))
        for p, q in vals:
            if p < 1e-10 and q < 1e-10: continue
            dl = max(dl, abs(math.log(max(p, 1e-300) / max(q, 1e-300))))
        if k.startswith("ckm"): dj = max(dj, abs(s[3] - v[3]))
    return dl, dj, keys


def one(row_and_line):
    row, (a, b) = row_and_line
    mine = compute(row["Re_tau"], row["Im_tau"], a, b)
    dl, dj, keys = compare(row, mine)
    return {"line": row["line"], "Re_tau": row["Re_tau"], "Im_tau": row["Im_tau"], "max_abs_log": dl, "max_abs_dJ": dj, "keys": keys}


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 48
    assert hashlib.sha256(CENSUS.read_bytes()).hexdigest() == CENSUS_SHA
    rows = [json.loads(l) for l in CENSUS.read_text(encoding="utf-8").splitlines() if l.strip()]
    L = lines(); assert len(L) == 266 and len(rows) == 8512
    sample = random.Random(1724).sample(range(len(rows)), n)
    with Pool(nw) as P:
        res = P.map(one, [(rows[i], L[rows[i]["line"]]) for i in sample])
    out = {"census_sha256": CENSUS_SHA, "sample_seed": 1724, "n": n, "points": res,
           "max_abs_log": max(r["max_abs_log"] for r in res), "max_abs_dJ": max(r["max_abs_dJ"] for r in res),
           "keys_per_point": res[0]["keys"]}
    out["reproduced_to_1e-9"] = out["max_abs_log"] < 1e-9 and out["max_abs_dJ"] < 1e-12
    json.dump(out, open(HERE / "reproduce.json", "w"), indent=1)
    print("%d points, %d keys each: max |log| %.2e, max |dJ| %.2e; reproduced %s" % (n, out["keys_per_point"], out["max_abs_log"], out["max_abs_dJ"], out["reproduced_to_1e-9"]))


if __name__ == "__main__":
    main()
