#!/usr/bin/env python3
"""B1477, POST-SEAL and UNSEALED (an exploratory check, archived on 2026-10-07 so that it is not lost; it grades nothing).
The residue of FINDINGS section 4: manifolds certified to have NO mirror-invariant spin structure on which Theorem B's
criterion found no odd count of rotation-pi geodesics at the sealed cutoff 3.0.  Question: is that the cutoff's doing?
Read the same criterion at a longer cutoff.  The residue is recomputed here from pi_geodesics.json (status NONE, no odd
length, zero class -- at 1/4 a rhombic cusp already explains the member by Theorem A), not typed in.  A member that shows an odd count at the longer cutoff is explained by Theorem B; one that does
not is still unexplained.  Usage: residue_cutoff.py [cutoff]   (default 3.8)."""
import sys, json, math, pathlib, collections, multiprocessing, warnings; warnings.filterwarnings("ignore")
import snappy
HERE = pathlib.Path(__file__).resolve().parent
CUTOFF = float(sys.argv[1]) if len(sys.argv) > 1 else 3.8


def one(name):
    try:
        spec = snappy.Manifold(name).length_spectrum(CUTOFF, grouped=False); c = collections.Counter()
        for g in spec:
            L = complex(g["length"])
            if abs(abs(L.imag) - math.pi) < 1e-6: c[round(L.real, 6)] += 1
        return dict(name=name, cutoff=CUTOFF, geodesics=len(spec), rotation_pi=sum(c.values()),
                    odd_lengths=sorted(l for l, n in c.items() if n % 2))
    except Exception as e:
        return dict(name=name, cutoff=CUTOFF, error=repr(e)[:160])


if __name__ == "__main__":
    base = json.load(open(HERE / "pi_geodesics.json"))
    residue = sorted(nm for nm, r in base.items() if "error" not in r and r["status"] == "NONE" and not r["odd_lengths"] and r["cs_class"] == "zero")
    print("residue at the sealed cutoff 3.0 (zero class, certified none, no odd rotation-pi count):", len(residue)); print(" ", residue)
    with multiprocessing.Pool(4) as pool: res = pool.map(one, residue, chunksize=1)
    out = {r["name"]: dict(r, kind=base[r["name"]]["kind"], cs_class=base[r["name"]]["cs_class"]) for r in res}
    tag = ("%.1f" % CUTOFF).replace(".", "p")
    json.dump(out, open(HERE / ("residue_cutoff_%s.json" % tag), "w"), indent=1)
    for nm, r in out.items():
        print("  %-16s %-7s CS %-6s" % (nm, r["kind"], r["cs_class"]),
              ("ERROR " + r["error"]) if "error" in r else "geodesics %5d  rotation-pi %3d  odd at lengths %s" % (r["geodesics"], r["rotation_pi"], r["odd_lengths"]))
    ok = [r for r in out.values() if "error" not in r]
    print("explained by Theorem B at cutoff %.1f: %d of %d  |  still unexplained: %s  |  errors: %d"
          % (CUTOFF, sum(bool(r["odd_lengths"]) for r in ok), len(out), sorted(r["name"] for r in ok if not r["odd_lengths"]), len(out) - len(ok)))
