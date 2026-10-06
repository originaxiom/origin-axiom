#!/usr/bin/env python3
"""B1479 cell C1/C2: the sign of a word state and its cusp.  For every primitive cyclic word w in L, R (up to the swap),
length 2..12, and both signs (SnapPy's b++w and b+-w): volume, Chern-Simons class, amphichirality and the mirror's type
on the cusp (B1477's census reading), and the cusp shape z = Mu/L relative to the rational longitude (B1477's shear()).
P2 (the half-shift): Im z(-w) = Im z(+w) and Re z(-w) - Re z(+w) in 1/2 + Z, for EVERY word.
P1 (the sign law): on amphichiral words, + is rectangular with CS = 0 and - is rhombic with CS = 1/4.
P3: on every amphichiral - state the longitude's trace is -2 on every lift (so Theorem A forbids every survivor)."""
import sys, json, itertools, pathlib, multiprocessing, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(next(p for p in HERE.parents if p.name == "frontier") / "B1477_what_decides_the_swap_the_mirrors_shear_on_the_cusp" / "verification"))


def canon(w):
    sw = w.translate(str.maketrans("LR", "RL")); return min([w[i:] + w[:i] for i in range(len(w))] + [sw[i:] + sw[:i] for i in range(len(sw))])


def words(nmax=12):
    prim = lambda w: not any(w == w[:d] * (len(w) // d) for d in range(1, len(w)) if len(w) % d == 0)
    return sorted({canon("".join(t)) for n in range(2, nmax + 1) for t in itertools.product("LR", repeat=n) if "L" in t and "R" in t and prim("".join(t))}, key=lambda x: (len(x), x))


def one(arg):
    w, sg = arg; name = sg + w
    import snappy, cusp_shear as CSH, range_census as RC
    out = dict(word=w, sign="+" if sg == "b++" else "-", name=name)
    try:
        M = snappy.Manifold(name)
        if M.solution_type() != "all tetrahedra positively oriented" and M.volume() < 0.5: out["hyperbolic"] = False; return out
        out["hyperbolic"] = True; out["volume"] = float(M.volume())
        r = RC.one(name); out["cs_class"] = r.get("cs_class"); out["amphichiral"] = bool(r.get("amphichiral")); out["rhombic_parity"] = r.get("rhombic_parity")
        s = CSH.shear(name); out["shape"] = s.get("shape"); out["two_re"] = s.get("two_re")
        if out["amphichiral"] and sg == "b+-":
            g = CSH.longitude_signs(name); out["n_spin"] = g.get("n_spin"); out["all_L_minus"] = g.get("all_L_minus")
    except Exception as e:
        out["error"] = repr(e)[:160]
    return out


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 12; workers = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    todo = [(w, sg) for w in words(nmax) for sg in ("b++", "b+-")]
    print("words:", len(todo) // 2, "states:", len(todo), flush=True)
    with multiprocessing.Pool(workers) as pool: rows = pool.map(one, todo, chunksize=4)
    by = {}
    for r in rows: by.setdefault(r["word"], {})[r["sign"]] = r
    pairs = [(w, d["+"], d["-"]) for w, d in by.items() if d.get("+", {}).get("shape") and d.get("-", {}).get("shape")]
    frac = lambda x: abs((x % 1.0) - 0.5)
    p2 = [(w, a["shape"], b["shape"]) for w, a, b in pairs if not (abs(a["shape"][1] - b["shape"][1]) < 1e-7 and frac(b["shape"][0] - a["shape"][0]) < 1e-7)]
    am = [(w, a, b) for w, a, b in pairs if a["amphichiral"] or b["amphichiral"]]
    p1 = [w for w, a, b in am if not (a["amphichiral"] and b["amphichiral"] and a["cs_class"] == "zero" and a["rhombic_parity"] == 0 and b["cs_class"] == "quarter" and b["rhombic_parity"] == 1)]
    p3 = [w for w, a, b in am if b.get("all_L_minus") is not True]
    summ = dict(nmax=nmax, words=len(by), states=len(rows), hyperbolic=sum(1 for r in rows if r.get("hyperbolic")), errors=[r["name"] for r in rows if "error" in r], pairs=len(pairs),
                P2_exceptions=p2, amphichiral_words=len(am), amphichiral_by_length=sorted({len(w): sum(1 for x, _, _ in am if len(x) == len(w)) for w, _, _ in am}.items()),
                P1_exceptions=p1, P3_exceptions=p3, volume_mismatch=[w for w, a, b in pairs if abs(a["volume"] - b["volume"]) > 1e-8])
    json.dump(dict(summary=summ, rows=rows), open(HERE / "sign_law.json", "w"), indent=0)
    print(json.dumps(summ)[:1500], flush=True)
