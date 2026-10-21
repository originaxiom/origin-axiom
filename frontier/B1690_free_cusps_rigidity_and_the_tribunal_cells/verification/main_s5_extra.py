"""P-229, GENESIS §5: m004's cyclic levels in F-FC (sm:B1368) and the hexagonal-cusp counts of the F-AP cells (sm:B1501's
which-cusps statement): m004's cusp shape, m003's, and the covers of m004 of degree <= 10 with a hexagonal cusp."""
import json, pathlib, snappy
HERE = pathlib.Path(__file__).resolve().parent
def reduce_shape(t):
    for _ in range(200):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-12: t = -1 / t
        else: break
    return t
OMEGA = complex(-0.5, 3 ** 0.5 / 2)
def hexagonal(t): t = reduce_shape(t); return abs(abs(t) - 1) < 1e-9 and abs(abs(t.real) - 0.5) < 1e-9
out = {}
lv = []
for k in range(1, 13):
    M = snappy.Manifold("b++" + "LR" * k)
    H = M.homology(); lv.append(dict(k=k, cusps=M.num_cusps(), b1=H.betti_number(), H1=str(H)))
out["m004_levels"] = lv
out["m004_shape"] = str(complex(snappy.Manifold("m004").cusp_info(0)["shape"]))
out["m004_hexagonal"] = hexagonal(complex(snappy.Manifold("m004").cusp_info(0)["shape"]))
out["m003_hexagonal"] = hexagonal(complex(snappy.Manifold("m003").cusp_info(0)["shape"]))
M = snappy.Manifold("m004"); covers = []
for d in range(1, 11):
    for C in M.covers(d):
        C = snappy.Manifold(C)
        shapes = [complex(C.cusp_info(i)["shape"]) for i in range(C.num_cusps())]
        covers.append(dict(degree=d, cusps=len(shapes), hex=sum(hexagonal(s) for s in shapes)))
out["m004_covers_le10"] = dict(n=len(covers), with_hex_cusp=sum(1 for c in covers if c["hex"] > 0),
                               by_degree={d: sum(1 for c in covers if c["degree"] == d) for d in range(1, 11)},
                               hex_by_degree={d: sum(1 for c in covers if c["degree"] == d and c["hex"] > 0) for d in range(1, 11)})
print(json.dumps(out, indent=1))
json.dump(out, open(HERE / "main_s5_extra.json", "w"), indent=1)
