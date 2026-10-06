#!/usr/bin/env python3
"""B1477, second seal: THE ORBIT FORM of the shear law.  A reversing isometry f permutes the cusps; on an orbit O of odd
length l the power f^l is again orientation-reversing and preserves each cusp of O, acting on its H_1 by the product of
f's cusp maps around the cycle (an involution of determinant -1).  n(f) = the number of odd orbits on which that product
is RHOMBIC (not 1 mod 2).  THE LAW: CS = n(f)/4 (mod 1/2) for every reversing f.  Orbits of even length contribute
nothing (B1239's swap corollary); an orbit of length one is the sealed form's 'invariant cusp'.

The composition order is validated, not assumed: the product must square to the identity as an integer matrix."""
import sys, json, pathlib, multiprocessing, warnings; warnings.filterwarnings("ignore")
import snappy
HERE = pathlib.Path(__file__).resolve().parent


def mul(A, B): return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]], [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
I2 = [[1, 0], [0, 1]]


def orbit_count(iso):
    maps = [[[int(m[0, 0]), int(m[0, 1])], [int(m[1, 0]), int(m[1, 1])]] for m in iso.cusp_maps()]; perm = list(iso.cusp_images())
    seen, out = set(), []
    for c in range(len(perm)):
        if c in seen: continue
        cyc = [c]; seen.add(c); x = perm[c]
        while x != c: cyc.append(x); seen.add(x); x = perm[x]
        if len(cyc) % 2 == 0: out.append((len(cyc), None, None)); continue
        Fcol, Frow = I2, I2
        for k in cyc: Fcol = mul(maps[k], Fcol); Frow = mul(Frow, maps[k])       # column convention / row convention
        ok_col, ok_row = mul(Fcol, Fcol) == I2, mul(Frow, Frow) == I2
        F = Fcol if ok_col else (Frow if ok_row else None)
        if F is None: out.append((len(cyc), "INVALID", None)); continue
        rh = [F[0][0] % 2, F[0][1] % 2, F[1][0] % 2, F[1][1] % 2] != [1, 0, 0, 1]
        both = None
        if ok_col and ok_row: both = ([Frow[0][0] % 2, Frow[0][1] % 2, Frow[1][0] % 2, Frow[1][1] % 2] != [1, 0, 0, 1]) == rh
        out.append((len(cyc), rh, both))
    return out


def one(name):
    try:
        M = snappy.Manifold(name)
        try:
            cs = float(M.chern_simons()); x = cs % 0.5
            cls = "zero" if min(x, 0.5 - x) < 1e-7 else ("quarter" if abs(x - 0.25) < 1e-7 else "other")
        except Exception:
            cs, cls = None, "unavailable"
        if cls == "other": return dict(name=name, cs_class=cls)
        isos = M.is_isometric_to(M, return_isometries=True); rows = []
        for iso in isos:
            dets = {int(m[0, 0]) * int(m[1, 1]) - int(m[0, 1]) * int(m[1, 0]) for m in iso.cusp_maps()}
            if dets != {-1}: continue
            oc = orbit_count(iso)
            rows.append(dict(orbits=sorted(l for l, _, _ in oc), n=sum(1 for l, rh, _ in oc if rh is True), invalid=sum(1 for l, rh, _ in oc if rh == "INVALID"),
                             conventions_disagree=sum(1 for l, rh, b in oc if b is False), sealed_form=sum(1 for l, rh, _ in oc if l == 1 and rh is True)))
        if not rows: return dict(name=name, cs_class=cls, amphichiral=False)
        par = sorted({r["n"] % 2 for r in rows}); spar = sorted({r["sealed_form"] % 2 for r in rows})
        return dict(name=name, cusps=M.num_cusps(), cs=cs, cs_class=cls, amphichiral=True, n_reversing=len(rows),
                    orbit_parity=(par[0] if len(par) == 1 else "MIXED"), sealed_parity=(spar[0] if len(spar) == 1 else "MIXED"),
                    odd_orbits_longer_than_one=any(l > 1 and l % 2 for r in rows for l in r["orbits"]),
                    invalid=sum(r["invalid"] for r in rows), conventions_disagree=sum(r["conventions_disagree"] for r in rows),
                    patterns=sorted({(tuple(r["orbits"]), r["n"]) for r in rows}))
    except Exception as e:
        return dict(name=name, error=repr(e)[:200])


if __name__ == "__main__":
    which, workers = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 4
    if which == "census":
        names = [json.loads(l)["name"] for l in open(HERE / "range_census.jsonl") if l.strip() and json.loads(l).get("amphichiral")]
    elif which == "links":
        names = [M.name() for k in range(2, 12) for M in snappy.HTLinkExteriors(cusps=k)]
    else:
        names = sys.argv[3:]
    outp = HERE / ("orbit_form_%s.jsonl" % which); done = set()
    if outp.exists(): done = {json.loads(l)["name"] for l in open(outp) if l.strip()}
    todo = [n for n in names if n not in done]; print("range:", len(names), "todo:", len(todo), flush=True)
    with multiprocessing.Pool(workers) as pool, open(outp, "a") as fh:
        for k, r in enumerate(pool.imap(one, todo, chunksize=20)):
            fh.write(json.dumps(r) + "\n")
            if r.get("amphichiral"):
                fh.flush()
                law = ((r["cs_class"] == "quarter") == (r["orbit_parity"] == 1)) if r["orbit_parity"] != "MIXED" and r["cs_class"] in ("zero", "quarter") else None
                print("%-14s cusps %d CS %-8s orbit parity %-5s (sealed form %-5s) odd orbits>1: %-5s patterns %s  LAW %s" % (r["name"], r["cusps"], r["cs_class"], r["orbit_parity"], r["sealed_parity"], r["odd_orbits_longer_than_one"], r["patterns"][:4], law), flush=True)
            if k % 10000 == 0: print("...", k, "of", len(todo), flush=True)
    print("DONE", flush=True)
