"""B1740 (P-345): the non-null Higgs under the Standard Model's reading, the census (no data).  B1656's frame at B1667's
canonical end (both horocycles, L read at Im tau from its Re tau = 1/4 column, as B1712-B1732), with the Higgs direction
F_-2 = eta^5 (th2^-2, th4^-2, i th3^-2) (B1730's zero-free family at a = -2, eps = i^((a + 2)/2) = 1; led at the cusp by
rho(T)'s non-null eigenline, so nearly real at the band, B1739) in place of DR, on B1713's 266 lines (orders 1-12 up to
sign), at B1726's 23 940 points (Re tau in {0.05, 0.2, 0.35, 0.55, 0.7, 0.85}, Im tau in {2.05, ..., 3.45}); no F_-2 row
of main's frame with these readings has been computed.  The Higgs's scalar eta^5 and its twist change no ratio, |V| or
J, so the direction is used.  The covariant readings only (B1724): every sector with S and with S~ = eps S* eps^T, and
the CKM (V = U_u^H U_d, ascending mass) for each (up, down) pair of them.  Checkpointed: each point is appended to
census.jsonl as it completes; a rerun skips the points already there.
    python3 -B census.py [--workers 8]
Importing computes nothing."""
import sys, io, json, math, contextlib, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OUT = HERE / "census.jsonl"
RE = (0.05, 0.2, 0.35, 0.55, 0.7, 0.85)
IM = tuple(round(2.05 + 0.1 * k, 2) for k in range(15))
RD = ("S", "St")
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
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


import functools


@functools.lru_cache(maxsize=1)
def lines():
    """B1713's 266 flat lines of exact order 1-12 up to sign, in its order (orders 1-7, then 8-12)"""
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


def higgs(t, which="Fm2"):
    """the Higgs's components at tau: F_-2's direction (th2^-2, th4^-2, i th3^-2), or DR (B1726's, for the control)"""
    import mpmath as mp
    M = _modules(); te = M["te"]
    if which == "DR":
        return [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    T = mp.mpc(t.real, t.imag)
    th2 = mp.fsum(mp.exp(1j * mp.pi * T * (n + mp.mpf(1) / 2) ** 2) for n in range(-30, 30))
    th3 = mp.fsum(mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31))
    th4 = mp.fsum((-1) ** n * mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31))
    v = [th2 ** -2, th4 ** -2, 1j * th3 ** -2]; m = max(abs(x) for x in v)
    return [complex(x / m) for x in v]


def compute(re_t, im_t, a, b, Ls=None, which="Fm2"):
    """every sector in S and S~ at both horocycles, and the CKM for each (up, down) pair (moduli and J)"""
    import mpmath as mp
    M = _modules(); B, te, col = M["B"], M["te"], M["col"]
    t = complex(re_t, im_t); w = float(a) * t + float(b)
    av = higgs(t, which)
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    reading = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}
    if Ls is None:
        Ls = {"L_max": float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col])), "L_2": float(np.interp(im_t, [q[0] for q in col], [q[2] for q in col]))}
    out, Y = {}, {}
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
                J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
                out["ckm|%s|%s|%s" % (h, ru, rd)] = [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2])), J]
    return out


def point(task):
    k, re_t, im_t = task
    a, b = lines()[k]
    r = compute(re_t, im_t, a, b); r.update(line=k, Re_tau=re_t, Im_tau=im_t); return r


def tasks():
    return [(k, r, y) for k in range(266) for r in RE for y in IM]


def control():
    """C1: (i) the instrument, with the Higgs switched to DR, against B1725's verified census at its best point (0.4 + 2.7i,
    line (2/5, 1/10)), every shared key -- the shared machinery; (ii) T-covariance with the Higgs F_-2, both readings, at
    0.35 + 2.75i on (2/5, 1/10) and (1/7, 3/7): (tau, (a, b)) against (tau + 1, (a, b - a)); (iii) B1730's norm law in the
    instrument's own theta functions: v_i v_j v_k = i (th2 th3 th4)^-2 for v = (th2^-2, th4^-2, i th3^-2)"""
    rec = None
    for l in (ROOT / "frontier" / "B1725_the_two_ingredients_on_main" / "received" / "two_ingredients_census.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(l)
        if r["Re_tau"] == 0.4 and r["Im_tau"] == 2.7 and lines()[r["line"]] == (Fr(2, 5), Fr(1, 10)): rec = r; break
    mine = compute(0.4, 2.7, Fr(2, 5), Fr(1, 10), which="DR")
    def dev(x, y): return max((abs(math.log(p / q)) for p, q in zip(x, y) if p > 1e-10 and q > 1e-10), default=0.0)
    d1 = max(dev(mine[k][:3] if k.startswith("ckm") else mine[k], rec[k][:3] if k.startswith("ckm") else rec[k]) for k in mine)
    dT = 0.0
    for a, b in ((Fr(2, 5), Fr(1, 10)), (Fr(1, 7), Fr(3, 7))):
        x, y = compute(0.35, 2.75, a, b), compute(1.35, 2.75, a, b - a)
        dT = max(dT, max(dev(x[k][:3] if k.startswith("ckm") else x[k], y[k][:3] if k.startswith("ckm") else y[k]) for k in x))
    import mpmath as mp
    T = mp.mpc(0.35, 2.75)
    th2 = mp.fsum(mp.exp(1j * mp.pi * T * (n + mp.mpf(1) / 2) ** 2) for n in range(-30, 30))
    th3 = mp.fsum(mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31))
    th4 = mp.fsum((-1) ** n * mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31))
    nv = th2 ** -2 * th4 ** -2 * 1j * th3 ** -2
    d3 = float(abs(nv / (1j * (th2 * th3 * th4) ** -2) - 1))
    return {"against_B1725": d1, "T_covariance": dT, "Fm2_norm_law": d3}


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    done = set()
    if OUT.exists():
        for l in OUT.read_text(encoding="utf-8").splitlines():
            if l.strip(): r = json.loads(l); done.add((r["line"], r["Re_tau"], r["Im_tau"]))
    todo = [t for t in tasks() if t not in done]
    print(len(tasks()), "points;", len(done), "done;", len(todo), "to do", flush=True)
    with Pool(nw) as P, open(OUT, "a", encoding="utf-8") as f:
        for r in P.imap_unordered(point, todo, chunksize=8):
            f.write(json.dumps(r) + "\n"); f.flush()
    c = control()
    json.dump(c, open(HERE / "control.json", "w"), indent=1)
    print("control: against B1725 %.2e, T-covariance %.2e, F_-2's norm law %.2e" % (c["against_B1725"], c["T_covariance"], c["Fm2_norm_law"]))


if __name__ == "__main__":
    main()
