#!/usr/bin/env python3
"""B1529 instrument (b): the eigenvalue-one crossings on the ten word states' type-two rings near the hyperbolic point, and the
class index read there.  Written before the seal; before the seal it was run only to locate crossings on +LR (no index, h1 or
interior value read at any crossing; PREREGISTRATION section 6).

The ring (sm:B1527 X1): Ballas' slice at a = 1e-5 with b free, l's translation z_l pinned at length R0 (that of the hyperbolic
point); along it the frame angle alpha of z_l turns.  rho(l) has the eigenvalues e^{-psi/4} (on e1, e4: a Jordan block),
e^{(3 psi_a - psi_b)/4} (e2) and e^{(3 psi_b - psi_a)/4} (e3), psi_a = a X_l, psi_b = b Y_l, psi = psi_a + psi_b.  Crossings:
    E1  psi_a + psi_b = 0   the four (e1) and Lambda^2 (e1^e4, e2^e3)
    E2  3 psi_a - psi_b = 0  the four (e2)
    E3  3 psi_b - psi_a = 0  the four (e3)
    E4  psi_a - psi_b = 0    Lambda^2 (e1^e2, e2^e4 and e1^e3, e3^e4)
Locate:
  1. brackets: the sign changes of the four functions between adjacent converged frames of X1's banked grid (x1_<name>.json,
     5 degrees apart; both |b| < 50 a, as X1 counted);
  2. float64: bisection on X1's pinned float64 solve (post_run_x1.Pinned) to 0.001 degrees;
  3. 60 digits: Gauss-Newton (X1c's gn: SVD pseudo-inverse cut at 1e-14, step halving) on the crossing system: the b-free
     equations, |z_l|^2 = R0^2, and the crossing function = 0 (the angle free), from the float64 solution, to |F| < 1e-48.
     If it fails, X1c's pinned 60-digit solve at the float64 angle first, then the crossing system again.
Read at each crossing (60 digits):
  - rho(l)'s eigenvalues and the crossing function; per module the crossing concerns: e = dim W^l, and the special twists
    kappa* = the eigenvalues of W(t')^-1 on W^l (route T's T_A): t0 >= 1 exactly at nu(t') = kappa*;
  - route T on EVERY torsion character at each kappa*: h1, h1*, t0, s0, I (Lemma F), the interior value chi_K(kappa*), the
    hypothesis H^0(F; V) = H^0(F; V*) = 0;
  - route Fox (cusp_lib.class_index) and route W (wang_lib.index_wang) on a subset: the trivial character and the first two
    others in sorted order, with their negatives (Lemma P's pairs), at each kappa*.
  lambda* = kappa* for sign +, kappa* zeta^-(i+j) for sign - (t' = abt).
Writes crossings_<name>.json; prints one line per crossing.
Usage: python3 crossings.py SIGN WORD [--locate-only] [--max N]   or   python3 crossings.py --all  (four processes)"""
import json
import sys
import time
import warnings
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

import fibre_lib as T  # noqa: E402

FL = T.load_b1527("family_lib")
L = T.load_b1527("cusp_lib")
R = T.load_b1527("run")
WL = T.load_b1527("wang_lib")
X1 = T.load_b1527("post_run_x1")
XC = T.load_b1527("post_run_x1c")
B1527 = T.B1527

A = mp.mpf(X1.A)                     # the solver's slice scale: the float 1e-5, exactly as X1 and X1c use it
GRID_B_MAX = 50
FLOAT_STEPS = 13                     # 5 degrees -> 0.0006 degrees
FUNCS = {"E1": lambda pa, pb: pa + pb, "E2": lambda pa, pb: 3 * pa - pb, "E3": lambda pa, pb: 3 * pb - pa,
         "E4": lambda pa, pb: pa - pb}
MODULES_OF = {"E1": ("4", "L2"), "E2": ("4",), "E3": ("4",), "E4": ("L2",)}
SUBSET_OTHERS = 2


def brackets(name):
    x1 = json.loads((B1527 / ("x1_" + name + ".json")).read_text())
    grid = x1["grid"]
    a = x1["a"]
    out = []
    for k in range(len(grid)):
        g, h = grid[k], grid[(k + 1) % len(grid)]
        if not (g["converged"] and h["converged"]) or abs(g["b"]) > GRID_B_MAX * a or abs(h["b"]) > GRID_B_MAX * a:
            continue
        for kind, f in FUNCS.items():
            fg, fh = f(g["psi_a(l)"], g["psi_b(l)"]), f(h["psi_a(l)"], h["psi_b(l)"])
            if np.sign(fg) != np.sign(fh):
                hi = h["alpha0"] if h["alpha0"] > g["alpha0"] else h["alpha0"] + 360
                out.append({"kind": kind, "between": [g["alpha0"], hi]})
    return out


def residual_crossing(V, a, G, img, R0, kind):
    mats, (Xl, Yl, Xt, Yt) = FL.unpack(V)
    b = V[52]
    inv = {g: mp.inverse(mats[g]) for g in mats}
    out = []
    for g in "ab":
        Rm = mats["t"] * mats[g] - FL._word(mats, img[g], inv) * mats["t"]
        out += [Rm[i, j] for i in range(4) for j in range(4)]
    for w, (X, Y) in ((G.cusp[0], (Xl, Yl)), (G.cusp[1], (Xt, Yt))):
        Rm = FL._word(mats, w, inv) - XC.slice_ab(X, Y, a, b)
        out += [Rm[i, j] for i in range(4) for j in range(4)]
    out += [mp.det(mats["a"]) - 1, mp.det(mats["b"]) - 1]
    out += [(Xl ** 2 + Yl ** 2 - R0 ** 2) / R0, FUNCS[kind](a * Xl, b * Yl) / a]
    return mp.matrix(out)


def locate(P64, P60, br, G, img):
    """float64 bisection on the bracket, then the 60-digit crossing system"""
    f = FUNCS[br["kind"]]
    lo, hi = np.radians(br["between"][0]), np.radians(br["between"][1])
    rlo, rhi = P64.solve(lo), P64.solve(hi)
    if not (rlo["converged"] and rhi["converged"]):
        return {"float64": "an endpoint did not converge"}, None
    flo = f(rlo["psi_a(l)"], rlo["psi_b(l)"])
    best = rlo
    for _ in range(FLOAT_STEPS):
        mid = 0.5 * (lo + hi)
        rm = P64.solve(mid)
        if not rm["converged"]:
            break
        fm = f(rm["psi_a(l)"], rm["psi_b(l)"])
        best = rm
        if np.sign(fm) == np.sign(flo):
            lo, flo = mid, fm
        else:
            hi = mid
    rec = {"float64 alpha (deg)": float(np.degrees(0.5 * (lo + hi)) % 360), "float64 |F|": best["|F|"]}
    mp.mp.dps = XC.DPS
    fun = lambda v: residual_crossing(v, P60.a, G, img, P60.R0, br["kind"])  # noqa: E731
    V0 = mp.matrix([mp.mpf(float(x)) for x in best["u"]])
    V, fv, it, ok = XC.gn(fun, V0)
    rec.update({"route": "crossing system from float64", "60-digit |F|": mp.nstr(fv, 3), "iterations": it})
    if not ok:
        Vp, fp, itp, okp = P60.solve(rec["float64 alpha (deg)"], V0)
        if okp:
            V, fv, it, ok = XC.gn(fun, Vp)
            rec.update({"route": "pinned 60-digit, then the crossing system", "60-digit |F|": mp.nstr(fv, 3),
                        "iterations": it})
    rec["converged"] = bool(ok)
    return rec, (V if ok else None)


def special_twists(Wmod, sign):
    """the distinct eigenvalues of W(t')^-1 on W^l (within 1e-20): the twists kappa* at which t0 >= 1"""
    TA, TD, e, mg = T.cusp_ends(Wmod.word("abAB"), Wmod.word(T.tprime(sign)))
    ks = []
    for k in (list(mp.eig(TA)[0]) if e else []):
        if all(abs(k - x) > mp.mpf(10) ** -20 * max(1, abs(x)) for x in ks):
            ks.append(k)
    return TA, TD, e, mg, ks


def subset(chars, D):
    others = [u for u in chars if u != (0, 0)][:SUBSET_OTHERS]
    keep = [(Fraction(0), Fraction(0))] + others
    neg = [((-u[0]) % 1, (-u[1]) % 1) for u in keep]
    out = []
    for u in keep + neg:
        if u not in out and u in chars:
            out.append(u)
    return out


def read(sign, word, G, img, V, kind, chars, D):
    mats = FL.unpack(V)[0]
    mats = {g: mp.matrix(mats[g]) for g in "abt"}
    rho = L.Module(mats)
    out = {"relator residual": mp.nstr(L.relator_residual(G, rho), 3)}
    ev = FL.eig_sorted(rho.word("abAB"))
    out["rho(l) eigenvalues"] = [mp.nstr(x, 15) for x in ev]
    out["min |eigenvalue - 1|"] = mp.nstr(min(abs(x - 1) for x in ev), 3)
    SM = T.StateModules(sign, img, mats, D)
    mods = {"4": mats, "L2": {g: L.wedge2(mats[g]) for g in "abt"}}
    sub = subset(chars, D)
    for name in MODULES_OF[kind]:
        W = L.Module(mods[name])
        TA, TD, e, mg, ks = special_twists(W, sign)
        rec = {"e": e, "cusp margins": {k: (mp.nstr(v, 3) if v is not None else None) for k, v in mg.items()},
               "kappa*": [mp.nstr(k, 20) for k in ks], "twists": []}
        if len(ks) == 2:
            rec["|kappa1 kappa2 - 1|"] = mp.nstr(abs(ks[0] * ks[1] - 1), 3)
        for ks_k in ks:
            tw = {"kappa*": mp.nstr(ks_k, 20), "route T": {"rows": 0, "I != 0": 0, "I values": {}, "hypothesis fails": 0,
                                                            "smallest |chi_K(kappa*)| rel": None, "rows by (t0, s0)": {}},
                  "Fox and W": []}
            smallest = None
            for u in chars:
                i, j = int(u[0] * D), int(u[1] * D)
                rt = SM.row(name, i, j, ks_k)
                (TC, slot, cond), f0 = SM.TC(name, "V", i, j)
                iv = T.interior_value(TC.charpoly(), TD, ks_k)
                tr = tw["route T"]
                tr["rows"] += 1
                tr["I values"][str(rt["I"])] = tr["I values"].get(str(rt["I"]), 0) + 1
                if rt["I"] != 0:
                    tr["I != 0"] += 1
                if rt["H0(F; V), H0(F; V*)"] != [0, 0]:
                    tr["hypothesis fails"] += 1
                key = str((rt["t0"], rt["s0"]))
                tr["rows by (t0, s0)"][key] = tr["rows by (t0, s0)"].get(key, 0) + 1
                if smallest is None or iv["chi_K(kappa) rel"] < smallest:
                    smallest = iv["chi_K(kappa) rel"]
                if u in sub:
                    lam = ks_k if sign == "+" else ks_k * mp.expjpi(-2 * mp.mpf(i + j) / D)
                    nu = R.nu_of(u, lam)
                    tm = R.twisted(mats, nu, wedge=(name == "L2"))
                    fox = L.class_index(G, L.Module(tm))
                    w = WL.index_wang(img, G.cusp, tm)
                    tw["Fox and W"].append({
                        "u": [str(u[0]), str(u[1])], "lambda*": mp.nstr(lam, 15),
                        "Fox": {"I": fox["I"], "h1": fox["V"]["h1"], "h1*": fox["V*"]["h1"], "t0": fox["V"]["t0"],
                                "s0": fox["V*"]["t0"], "a0": fox["V"]["a0"], "b0": fox["V*"]["a0"], "checks": fox["checks"],
                                "margins": fox["margins"]},
                        "W": {k: w[k] for k in ("I", "h1(V)", "h1(V*)", "a0", "b0", "t0", "s0", "margins")},
                        "T": {k: rt[k] for k in ("I", "h1", "h1*", "t0", "s0")},
                        "chi_K(kappa*) rel": mp.nstr(iv["chi_K(kappa) rel"], 3)})
            tw["route T"]["smallest |chi_K(kappa*)| rel"] = mp.nstr(smallest, 3) if smallest is not None else None
            rec["twists"].append(tw)
        out[name] = rec
    return out


def run_one(sign, word, locate_only=False, max_n=None):
    t0 = time.time()
    name = R.name_of(sign, word)
    G, img = FL.word_group(sign, word)
    chars, D = FL.torsion_characters(img)
    P64 = X1.Pinned(sign, word)
    P60 = XC.Problem(sign, word)
    brs = brackets(name)
    if max_n is not None:
        brs = brs[:max_n]
    res = {"manifold": sign + word, "a": mp.nstr(A, 20), "D": D, "brackets": len(brs),
           "brackets by kind": {k: sum(1 for b in brs if b["kind"] == k) for k in FUNCS}, "crossings": []}
    for br in brs:
        t1 = time.time()
        loc, V = locate(P64, P60, br, G, img)
        entry = {"kind": br["kind"], "bracket (deg)": br["between"], "locate": loc}
        if V is not None:
            Xl, Yl = V[48], V[49]
            entry["alpha (deg)"] = float(mp.degrees(mp.atan2(Yl, Xl)) % 360)
            entry["b/a"] = mp.nstr(V[52] / A, 12)
            entry["crossing function / a"] = mp.nstr(FUNCS[br["kind"]](A * Xl, V[52] * Yl) / A, 3)
            if locate_only:
                mats = {g: mp.matrix(FL.unpack(V)[0][g]) for g in "abt"}
                ev = FL.eig_sorted(L.Module(mats).word("abAB"))
                entry["min |eigenvalue - 1|"] = mp.nstr(min(abs(x - 1) for x in ev), 3)
            else:
                entry["read"] = read(sign, word, G, img, V, br["kind"], chars, D)
        entry["seconds"] = round(time.time() - t1)
        res["crossings"].append(entry)
        print(f"{sign}{word} {br['kind']} {br['between']}: converged {loc.get('converged')}, "
              f"alpha {entry.get('alpha (deg)')}, {entry['seconds']} s", flush=True)
    res["seconds"] = round(time.time() - t0)
    if not locate_only:
        (HERE / ("crossings_" + name + ".json")).write_text(json.dumps(res, indent=1, default=str))
    return res


def main():
    args = sys.argv[1:]
    if args == ["--all"]:
        from multiprocessing import Pool
        with Pool(4) as pool:
            pool.starmap(run_one, R.MANIFOLDS)
        return
    locate_only = "--locate-only" in args
    max_n = int(args[args.index("--max") + 1]) if "--max" in args else None
    pos = [a for a in args if not a.startswith("--") and not a.isdigit()]
    out = run_one(pos[0], pos[1], locate_only, max_n)
    if locate_only:
        print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
