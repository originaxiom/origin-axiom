"""B1724 (P-297): the covariance of B1660's three readings of the Higgs, S, S~ = eps S* eps^T and S*, in B1656's frame.
The controls of B1720 and B1723 tested S only.
(A) T on S's components: S = a_i i + a_j j + a_k k (B1691's triplet, B1644's quaternion units).  The 2 x 2 action of T on
    (a_j, a_k) is solved from two tau and checked on a third; the phase of a_i is read directly.
(B) T, T^2, T^3: the frame at (tau, (alpha, b)) against (tau + n, (alpha, b - n alpha)), every sector in every reading and
    the CKM for every (up, down) reading pair; the end read at Im tau (unchanged by T).
(C) S: (tau, (alpha, b)) against (-1/tau, (-b, alpha)) with the end passed explicitly, L' = L + log|tau| (B1667's law),
    both horocycles, the same comparisons.
(D) S T^2 S, the second generator of Gamma(2) with T^2: composed from (C) and (B) step by step, at base points whose whole
    chain stays at Im tau >= 0.3 (the frame's series are not reliable near Im tau = 0.1, where a first attempt from
    TAUS reached 0.09 and every reading failed, S included).
(E) T S, the order-3 coset of SL(2, Z)/Gamma(2) = S_3, composed the same way at the base points of (D).
(F) R: tau -> tau/(tau + 1) (the record's move, [[1, 0], [1, 1]] = T S T as a matrix), directly with its own law
    (alpha, b) -> (alpha - b, b) and L' = L + log|tau + 1|, at base points whose image stays at Im tau >= 0.6.
Together these place each reading's covariance group exactly: the subgroups of S_3 that contain R's image are {e, R} and
S_3 itself.
Ratios below 1e-10 are not compared (B1716's exact zeros).  The lines are of orders 3, 5, 7, 8, 10, 11 (no order 4 or 12).
    python3 -B covariance.py [--workers 8]      # writes covariance.json beside itself
Importing computes nothing."""
import sys, io, json, math, cmath, contextlib, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
RD = ("S", "St", "conjS")
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
TAUS = (complex(0.4, 2.7), complex(0.13, 1.9), complex(-0.31, 1.3), complex(0.27, 3.4))
TAUS_D = (complex(0.5, 0.6), complex(0.45, 0.7), complex(0.55, 0.5), complex(0.4, 0.8))
TAUS_R = (complex(-0.6, 0.7), complex(-0.55, 0.9), complex(-0.7, 0.6), complex(-0.45, 1.1))
LINES = ((Fr(1, 3), Fr(2, 3)), (Fr(2, 5), Fr(1, 5)), (Fr(1, 7), Fr(3, 7)), (Fr(3, 8), Fr(0)), (Fr(2, 5), Fr(1, 10)), (Fr(1, 11), Fr(10, 11)))
_M = {}


def _modules():
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


def components(t):
    import mpmath as mp
    te = _modules()["te"]
    return np.array([complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]])


def L_col(y):
    col = _modules()["col"]
    return {"L_max": float(np.interp(y, [q[0] for q in col], [q[1] for q in col])), "L_2": float(np.interp(y, [q[0] for q in col], [q[2] for q in col]))}


def frame(t, a, b, Ls):
    """every sector in every reading and the CKM for every (up, down) pair, at (tau, line (a, b)) with the end Ls"""
    B = _modules()["B"]
    c3 = components(t); S = c3[0] * B.QI + c3[1] * B.QJ + c3[2] * B.QK
    reading = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    w = float(a) * t + float(b); out, Y = {}, {}
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for h in ("L_max", "L_2"):
            L = Ls[h]
            u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
            Mw = B.weighted_M(u)
            for rn in RD:
                Ym = B.coupling(reading[rn], Mw); Y[(sec, h, rn)] = Ym
                sv = np.linalg.svd(Ym, compute_uv=False); out["%s|%s|%s" % (sec, h, rn)] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    for h in ("L_max", "L_2"):
        for ru in RD:
            for rd in RD:
                Uu = np.linalg.svd(Y[("up", h, ru)])[0][:, ::-1]; Ud = np.linalg.svd(Y[("down", h, rd)])[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
                out["ckm|%s|%s|%s" % (h, ru, rd)] = [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2]))]
    return out


def dev(x, y):
    return max((abs(math.log(p / q)) for p, q in zip(x, y) if p > 1e-10 and q > 1e-10), default=0.0)


def compare(base, other):
    """max |log| per reading (sectors) and per CKM reading pair"""
    out = {}
    for k in base:
        parts = k.split("|")
        key = parts[2] if parts[0] != "ckm" else "ckm %s|%s" % (parts[2], parts[3])
        out[key] = max(out.get(key, 0.0), dev(base[k], other[k]))
    return out


def part_a():
    ts = TAUS[:3]; C = [components(t) for t in ts]; Cp = [components(t + 1) for t in ts]
    A = np.array([C[0][1:], C[1][1:]]).T; Bm = np.array([Cp[0][1:], Cp[1][1:]]).T
    M = Bm @ np.linalg.inv(A)
    check = float(np.max(np.abs(M @ C[2][1:] - Cp[2][1:])) / np.max(np.abs(C[2])))
    ph_i = [(cmath.phase(Cp[n][0] / C[n][0]) / (2 * math.pi)) % 1 for n in range(3)]
    rot = M / cmath.exp(1j * math.pi / 4)
    return {"phase_i_over_2pi": ph_i, "M_over_e_ipi4": [[[z.real, z.imag] for z in row] for row in rot], "third_tau_check": check,
            "M_is_e_ipi4_times_R_minus90": float(np.max(np.abs(rot - np.array([[0, 1], [-1, 0]])))),
            "eigenphases_over_2pi": sorted((cmath.phase(e) / (2 * math.pi)) % 1 for e in np.linalg.eigvals(M))}


def task(job):
    kind, ti, li = job
    t = (TAUS_D if kind in ("D", "E") else TAUS_R if kind == "F" else TAUS)[ti]; a, b = LINES[li]; Ls = L_col(t.imag); base = frame(t, a, b, Ls)
    S_ = lambda tt, aa, bb, LL: (-1 / tt, -bb, aa, {h: LL[h] + math.log(abs(tt)) for h in LL})
    if kind == "E":
        s = S_(t, a, b, Ls); m1 = s[0].imag; s = (s[0] + 1, s[1], s[2] - s[1], s[3])
        return {"kind": "E", "tau": ti, "line": li, "min_im": min(t.imag, m1, s[0].imag), "dev": compare(base, frame(*s))}
    if kind == "F":
        tr = t / (t + 1)
        return {"kind": "F", "tau": ti, "line": li, "min_im": min(t.imag, tr.imag),
                "dev": compare(base, frame(tr, a - b, b, {h: Ls[h] + math.log(abs(t + 1)) for h in Ls}))}
    if kind == "D":
        S_ = lambda tt, aa, bb, LL: (-1 / tt, -bb, aa, {h: LL[h] + math.log(abs(tt)) for h in LL})
        s = S_(t, a, b, Ls); m1 = s[0].imag; s = (s[0] + 2, s[1], s[2] - 2 * s[1], s[3]); s = S_(*s)
        return {"kind": "D", "tau": ti, "line": li, "min_im": min(t.imag, m1, s[0].imag), "dev": compare(base, frame(*s))}
    if kind == "T":
        return {"kind": "T", "tau": ti, "line": li, "n": {str(n): compare(base, frame(t + n, a, b - n * a, Ls)) for n in (1, 2, 3)}}
    tS = -1 / t; LS = {h: Ls[h] + math.log(abs(t)) for h in Ls}
    return {"kind": "S", "tau": ti, "line": li, "dev": compare(base, frame(tS, -b, a, LS))}


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    A = part_a()
    jobs = [(k, ti, li) for k in ("T", "S", "D", "E", "F") for ti in range(len(TAUS)) for li in range(len(LINES))]
    with Pool(nw) as P:
        res = P.map(task, jobs)
    summ = {}
    for r in res:
        items = [("T^%s" % n, d) for n, d in r["n"].items()] if r["kind"] == "T" else [({"S": "S", "D": "ST^2S", "E": "TS", "F": "R"}[r["kind"]], r["dev"])]
        for g, d in items:
            for key, v in d.items():
                summ.setdefault(g, {}); summ[g][key] = max(summ[g].get(key, 0.0), v)
    json.dump({"part_a": A, "taus": [[t.real, t.imag] for t in TAUS], "lines": [[str(a), str(b)] for a, b in LINES], "rows": res, "summary": summ},
              open(HERE / "covariance.json", "w"), indent=1)
    print("A: i-phase/2pi", ["%.6f" % x for x in A["phase_i_over_2pi"]], "| (j, k) block vs e^{i pi/4} R_-90: %.1e | third tau %.1e | eigenphases" % (A["M_is_e_ipi4_times_R_minus90"], A["third_tau_check"]), ["%.4f" % x for x in A["eigenphases_over_2pi"]])
    for k in ("D", "E", "F"):
        print("%s: min Im on the chains %.2f" % (k, min(r["min_im"] for r in res if r["kind"] == k)))
    for g in ("T^1", "T^2", "T^3", "S", "ST^2S", "TS", "R"):
        print("%-4s" % g, "  ".join("%s %.1e" % (k, v) for k, v in sorted(summ[g].items())))


if __name__ == "__main__":
    main()
