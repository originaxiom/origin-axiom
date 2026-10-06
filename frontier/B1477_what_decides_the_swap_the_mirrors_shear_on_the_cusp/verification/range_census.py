#!/usr/bin/env python3
"""B1477 cell C1: the sealed range -- every manifold of the installed orientable cusped census (SnapPy 3.3.2: 212,641
manifolds, at most ten tetrahedra), one cusp or several.  Prefilter: the Chern-Simons class must be 0 or 1/4 (mod 1/2) -- amphichirality forces it (B1224), so nothing
amphichiral is lost; a manifold whose CS SnapPy cannot compute is kept.  Then SnapPy's complete list of self-isometries:
for every orientation-reversing f and every cusp c with f(c) = c, the cusp map F in GL(2,Z) (det -1, an involution) is
RECTANGULAR if F = 1 (mod 2) and RHOMBIC otherwise.  Recorded per manifold: for each reversing f, the number of invariant
cusps and the number of rhombic ones.  THE LAW UNDER TEST (P1): CS = 1/4 (mod 1/2)  <=>  the number of rhombic invariant
cusps is odd -- for every reversing f."""
import sys, json, pathlib, multiprocessing, warnings; warnings.filterwarnings("ignore")
import snappy
HERE = pathlib.Path(__file__).resolve().parent


def one(name):
    try:
        M = snappy.Manifold(name)
        try:
            cs = float(M.chern_simons()); x = cs % 0.5
            cls = "zero" if min(x, 0.5 - x) < 1e-7 else ("quarter" if abs(x - 0.25) < 1e-7 else "other")
        except Exception as e:
            cs, cls = None, "unavailable"
        if cls == "other": return dict(name=name, cs_class=cls)
        isos = M.is_isometric_to(M, return_isometries=True)
        rev = []
        for iso in isos:
            maps = iso.cusp_maps(); imgs = list(iso.cusp_images())
            dets = {int(m[0, 0]) * int(m[1, 1]) - int(m[0, 1]) * int(m[1, 0]) for m in maps}
            if dets != {-1}: continue
            inv = [i for i, j in enumerate(imgs) if i == j]
            rh = [i for i in inv if [int(maps[i][0, 0]) % 2, int(maps[i][0, 1]) % 2, int(maps[i][1, 0]) % 2, int(maps[i][1, 1]) % 2] != [1, 0, 0, 1]]
            rev.append(dict(invariant=len(inv), rhombic=len(rh), maps=[[int(m[0, 0]), int(m[0, 1]), int(m[1, 0]), int(m[1, 1])] for m in maps], images=imgs))
        if not rev: return dict(name=name, cs_class=cls, amphichiral=False)
        par = sorted({r["rhombic"] % 2 for r in rev})
        return dict(name=name, cusps=M.num_cusps(), cs=cs, cs_class=cls, amphichiral=True, n_isometries=len(isos), n_reversing=len(rev),
                    rhombic_parity=(par[0] if len(par) == 1 else "MIXED"), per_isometry=[(r["invariant"], r["rhombic"]) for r in rev],
                    maps=[r["maps"] for r in rev][:4], h1=str(M.homology()), volume=float(M.volume()))
    except Exception as e:
        return dict(name=name, error=repr(e)[:200])


if __name__ == "__main__":
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    extra = sys.argv[2:]                                  # names outside the census range (the family's members beyond nine tetrahedra)
    outp = HERE / "range_census.jsonl"
    done = set()
    if outp.exists(): done = {json.loads(l)["name"] for l in open(outp) if l.strip()}
    names = [M.name() for M in snappy.OrientableCuspedCensus] + list(extra)
    todo = [n for n in names if n not in done]
    print("range:", len(names), "todo:", len(todo), flush=True)
    n_amph = 0
    with multiprocessing.Pool(workers) as pool, open(outp, "a") as fh:
        for k, r in enumerate(pool.imap(one, todo, chunksize=50)):
            fh.write(json.dumps(r) + "\n")
            if r.get("amphichiral"):
                n_amph += 1; fh.flush()
                law = (r["cs_class"] == "quarter") == (r["rhombic_parity"] == 1) if r["rhombic_parity"] != "MIXED" and r["cs_class"] in ("zero", "quarter") else None
                print("%-12s cusps %d CS %-8s rhombic parity %s per-isometry %s  LAW %s" % (r["name"], r["cusps"], r["cs_class"], r["rhombic_parity"], sorted(set(map(tuple, r["per_isometry"]))), law), flush=True)
            if k % 5000 == 0: print("...", k, "of", len(todo), "amphichiral so far", n_amph, flush=True)
    print("DONE", flush=True)
