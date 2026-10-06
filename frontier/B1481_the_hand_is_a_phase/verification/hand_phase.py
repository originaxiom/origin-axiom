#!/usr/bin/env python3
"""B1481 cell: the phase of the odd twisted Alexander function, spin structure by spin structure.
R_1^{(s)}(t) (B1471's Wada function at Sym^1 of the lift rho_s) is defined up to a real unit +-t^k, so
    theta_s(t) = arg R_1^{(s)}(t)  in  R / pi Z
is an invariant of (M, s).  A mirror f gives theta_{f.s} = -theta_s; a mirror-invariant s has theta_s in {0, pi/2}.
Computed on every amphichiral word to length 12 (B1479's table), both signs, every spin structure, at t = 2, 3, 0.6 and
at t = 1 where the function is defined there."""
import sys, json, cmath, math, pathlib, multiprocessing, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent; FR = next(p for p in HERE.parents if p.name == "frontier")
sys.path.insert(0, str(FR / "B1477_what_decides_the_swap_the_mirrors_shear_on_the_cusp" / "verification"))
TS = ("1", "2", "3", "0.6")


def one(name):
    import cusp_shear as CSH
    from mpmath import mpf
    R, SQ = CSH.R, CSH.SQ
    out = dict(name=name)
    try:
        pk, err = CSH.setup_rank1(name)
        if err: out["error"] = err; return out
        gens = pk["gens"]; out["h1"] = pk["h1"]; rows = []
        for chi in SQ.characters(pk):
            pk2 = dict(pk); pk2["rho"] = {g: chi[g] * pk["rho"][g] for g in gens}; W = R.Wada(pk2, 1); th = {}; mod = {}
            for t in TS:
                z = W.value(mpf(t))
                if z is None or abs(z) < 1e-25: th[t] = None; continue
                z = complex(z); th[t] = cmath.phase(z) % math.pi; mod[t] = abs(z)
            rows.append(dict(chi=[chi[g] for g in gens], theta=th, modulus=mod))
        out["rows"] = rows
    except Exception as e:
        out["error"] = repr(e)[:160]
    return out


def near(x, y, tol=1e-8): return x is not None and min(abs(x - y), abs(x - y - math.pi), abs(x - y + math.pi)) < tol
def special(x): return near(x, 0.0) or near(x, math.pi / 2)


def read(r, t):
    """(n_spin, n_special, paired) at the point t: paired = the multiset of phases is closed under theta -> -theta with no fixed element"""
    ths = [row["theta"][t] for row in r["rows"]]
    if any(x is None for x in ths): return (len(ths), None, None)
    nsp = sum(1 for x in ths if special(x)); left = list(ths); ok = True
    while left:
        x = left.pop()
        if special(x): ok = False; break
        j = next((k for k, y in enumerate(left) if near(y, (-x) % math.pi)), None)
        if j is None: ok = False; break
        left.pop(j)
    return (len(ths), nsp, ok)


if __name__ == "__main__":
    S = json.load(open(FR / "B1479_the_bit_is_the_sign_of_the_word_state" / "verification" / "sign_law.json"))["rows"]
    names = [r["name"] for r in S if r["amphichiral"]] if len(sys.argv) < 2 or sys.argv[1] == "all" else sys.argv[1:]
    with multiprocessing.Pool(5) as pool: res = pool.map(one, names, chunksize=2)
    out = {r["name"]: r for r in res}
    summ = dict(states=len(res), errors={r["name"]: r["error"] for r in res if "error" in r})
    for sg, key in (("b+-", "minus"), ("b++", "plus")):
        rs = [r for r in res if r["name"].startswith(sg) and "rows" in r]
        summ[key] = dict(states=len(rs), spin_structures=sum(len(r["rows"]) for r in rs))
        for t in ("2", "3", "0.6"):
            rd = [read(r, t) for r in rs]
            summ[key]["t=" + t] = dict(special_total=sum(x[1] or 0 for x in rd), states_with_special=sum(1 for x in rd if x[1]), states_paired=sum(1 for x in rd if x[2]), undefined=sum(1 for x in rd if x[1] is None))
        q = []
        for r in rs:
            for row in r["rows"]:
                x = row["theta"]["1"]
                q.append(None if x is None else min(abs(x * d / math.pi - round(x * d / math.pi)) for d in (24,)) < 1e-7)
        summ[key]["t=1"] = dict(defined=sum(1 for x in q if x is not None), on_the_24_lattice=sum(1 for x in q if x), undefined=sum(1 for x in q if x is None))
    json.dump(dict(summary=summ, states=out), open(HERE / "hand_phase.json", "w"), indent=0); print(json.dumps(summ)[:1800])
