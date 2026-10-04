#!/usr/bin/env python3
"""B1536 control K3 (banked data only): the cover's own classes.  sm:B1535's Part M read the silver squares' abelian covers at
their own classes (pure classes in one character component, and generic mixed classes over every component), in two routes.
Here both of this arc's routes read the same covers:
  - every pure class whose base class is canonical ('the class', 'c_int'): route N through Lemma O with
    c_hat(g)_x = z(g) f(x), f(x) = e^(2 pi i x_chi0) (P(g) f = chi0(g) f, so c_hat is a cocycle when z is one of nu^5 chi0 rho),
    route R with c = z on the Schreier words (Shapiro: c(h) = c_hat(h)_0 = z(h));
  - the full stratum's generic class (every class of the cover), two random draws in each route, against Part M's two generic
    mixed classes.  Part M's coefficients are small (1 to 97), so one of its two draws can land on a special class: the generic
    reading is the one with the largest connecting ranks (lower semicontinuity of rank), and both routes' draws must equal the
    banked reading of largest ranks in count, k and every connecting rank; banked pairs whose two draws differ are listed.
Each must read Part M's banked count and k (route RS, first prime).

    python3 control_k3.py [--record]   ->  k3.json"""
import json
import random
import sys
import time
import warnings
from collections import defaultdict
from fractions import Fraction as Fr
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import numpy as np  # noqa: E402
import cover_lib as CL  # noqa: E402
import gf  # noqa: E402
import route_n as N  # noqa: E402
import route_r as R  # noqa: E402
import control_k2 as K2  # noqa: E402

PART_M = ROOT / "frontier" / "B1535_the_cap" / "verification" / "part_m.jsonl"
NAMES = {"-LLRR": "m135", "+LLRR": "m136"}


def lab(t):
    return f"({t[0]}, {t[1]}; {t[2]})"


def cover_pts(H, sign):
    """control_k2's cover with its point tuples (one coordinate per character of sorted(H))"""
    chis = [K2.parse_char(h) for h in sorted(H)]
    val = {"a": tuple(c[0] for c in chis), "b": tuple(c[1] for c in chis),
           "t": tuple((c[2] if sign == "+" else c[2] - c[0] - c[1]) % 1 for c in chis)}
    zero = tuple(Fr(0) for _ in chis)
    pts, idx, todo = [zero], {zero: 0}, [zero]
    while todo:
        x = todo.pop()
        for g in "abt":
            for s in (1, -1):
                y = tuple((xi + s * gi) % 1 for xi, gi in zip(x, val[g]))
                if y not in idx:
                    idx[y] = len(pts)
                    pts.append(y)
                    todo.append(y)
    perms = {g: [idx[tuple((xi + gi) % 1 for xi, gi in zip(x, val[g]))] for x in pts] for g in "abt"}
    return perms, pts, sorted(H)


def main():
    t0 = time.time()
    if PART_M.exists():
        text = PART_M.read_text()
    else:                               # a fresh checkout keeps sm:B1535's rows compressed (part_m.jsonl.gz)
        import gzip
        text = gzip.open(str(PART_M) + ".gz", "rt").read()
    rows = [json.loads(line) for line in text.splitlines()]
    groups = defaultdict(list)
    for r in rows:
        groups[(r["state"], tuple(r["nu"]), tuple(tuple(b) for b in r["B"]))].append(r)
    pN = gf.primes_1_mod(120, N.P_BOUND, 1)[0]
    pR = gf.primes_1_mod(120, 1 << 31, 1)[0]
    FN, FR = gf.GF(pN, 120), gf.GF(pR, 120)
    bases = {}
    out = {"pure": [], "generic": [], "primes": {"route N": pN, "route R": pR}}
    for (state, nu, B), grp in sorted(groups.items()):
        name = NAMES[state]
        if name not in bases:
            st = CL.state(name)
            bases[name] = (st, N.Base(st, FN), N.Base(st, FR))
        st, BN, BR = bases[name]
        H = [lab(b) for b in B]
        perms, pts, Hs = cover_pts(H, st["sign"])
        pa = N.perm_arrays(BN.G, perms)
        cov = R.PCover(BR.G, perms)
        d = len(pts)
        u, kap = (Fr(nu[0]), Fr(nu[1])), Fr(nu[2])
        chiN, chiR = BN.character(u, kap), BR.character(u, kap)
        for r in grp:
            cls, comps = r["class"], r["components"]
            if cls.startswith("pure-") and cls.split(":", 1)[1] in ("the class", "c_int"):
                x0 = tuple(comps[0])
                c0 = BN.character((Fr(x0[0]), Fr(x0[1])), Fr(x0[2]))
                c0R = BR.character((Fr(x0[0]), Fr(x0[1])), Fr(x0[2]))
                # route N: the base class of nu^5 chi0 rho, spread by f(x) = e(x_chi0)
                mods = {g: BN.rho[g] * (pow(int(chiN[g]), 5, pN) * c0[g] % pN) % pN for g in BN.gens}
                mod = N.Module(BN.gens, {g: N.BM(np.array([0]), mods[g].reshape(1, 4, 4).copy(), pN) for g in BN.gens}, pN)
                clsN = N.base_classes(BN, mod)
                key = "c1" if cls.endswith("the class") else "int"
                z = clsN[key]
                i0 = Hs.index(lab(x0))
                f = [FN.root(pt[i0]) for pt in pts]
                cl = {g: [(z[gi * 4:(gi + 1) * 4] * f[x]) % pN for x in range(d)] for gi, g in enumerate(BN.gens)}
                rN = N.reading(BN, pa, chiN, cl)
                # route R: z (its own) on the Schreier words
                modsR = {g: BR.rho[g] * (pow(int(chiR[g]), 5, pR) * c0R[g] % pR) % pR for g in BR.gens}
                zR = K2.route_r_classes(BR.G, modsR, pR)[key]
                cv = R.cocycle_on_words(BR.G, modsR, zR, cov.sword, pR)
                rR = R.reading(cov, BR.rho, chiR, cv, pR)
                bank = r["RS p1"]
                rec = {"state": name, "nu": list(nu), "|B|": len(B), "class": cls,
                       "banked": [bank["I(W)"], bank["I(L2W)"], bank["k"]],
                       "route N": [rN["I(W)"], rN["I(L2W)"], rN["k"]], "route R": [rR["I(W)"], rR["I(L2W)"], rR["k"]],
                       "identities": [rN["all"], rR["all"]]}
                rec["ok"] = rec["banked"] == rec["route N"] == rec["route R"] and rN["all"] and rR["all"]
                out["pure"].append(rec)
        gens_ = [r for r in grp if r["class"].startswith("mixed-generic")]
        if gens_:
            cus = CL.cusps(BN.G, perms)
            trivial = [(kap * c["j0"]).denominator == 1 for c in cus]
            T = [i for i, t in enumerate(trivial) if t]
            sN = [x for x in N.strata_readings(BN, pa, chiN, [dict(c, trivial=t) for c, t in zip(cus, trivial)],
                                               random.Random(7), only=[T]) if x[0] == T]
            sR = [x for x in R.strata_readings(cov, BR.rho, chiR, pR, trivial, random.Random(8), only=[T]) if x[0] == T]
            def key(x):
                return [x["I(W)"], x["I(L2W)"], x["k"], x["rk d1"]["L2*"], x["rk d1"]["E*"], x["rk d1"]["E"], x["rk d1"]["L2"]]
            gN = [key(x) for x in sN[0][1]] if sN else []
            gR = [key(x) for x in sR[0][1]] if sR else []
            bank = [key(g["RS p1"]) for g in gens_]
            top = max(bank, key=lambda b: (b[3], b[4], b[5], b[2]))
            rec = {"state": name, "nu": list(nu), "|B|": len(B), "banked generic": bank, "banked, largest ranks": top,
                   "route N": gN, "route R": gR, "banked draws differ": len({json.dumps(b) for b in bank}) > 1}
            rec["ok"] = bool(gN) and bool(gR) and all(x == top for x in gN + gR)
            out["generic"].append(rec)
        print(name, nu, len(B), "pure ok", all(x["ok"] for x in out["pure"]), "generic ok",
              all(x["ok"] for x in out["generic"]), f"{time.time() - t0:.0f}s", flush=True)
    out["pure readings"] = len(out["pure"])
    out["generic readings"] = len(out["generic"])
    out["banked pairs whose two generic draws differ"] = [[x["state"], x["nu"], x["|B|"], x["banked generic"]]
                                                          for x in out["generic"] if x["banked draws differ"]]
    out["holds"] = all(x["ok"] for x in out["pure"]) and all(x["ok"] for x in out["generic"])
    out["seconds"] = round(time.time() - t0)
    print(json.dumps({k: v for k, v in out.items() if k not in ("pure", "generic")}))
    if "--record" in sys.argv:
        (HERE / "k3.json").write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    main()
