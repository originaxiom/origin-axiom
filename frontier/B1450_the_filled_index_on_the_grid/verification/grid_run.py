#!/usr/bin/env python3
"""The population run: the formula on B1419's grid, |p| <= 8, 1 <= q <= 8, gcd 1 (87 slopes), to q^10."""
import sys, json, math, pathlib, multiprocessing
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from filled_index import filled
X = 20
def one(sl):
    ser, info = filled(sl[0], sl[1], X)
    return dict(slope=list(sl), dual=info["dual"], terms=info.get("terms"),
                series=None if ser is None else {str(k): v for k, v in sorted(ser.items())})
if __name__ == "__main__":
    grid = [(p, q) for p in range(-8, 9) for q in range(1, 9) if math.gcd(p, q) == 1]
    assert len(grid) == 87
    with multiprocessing.Pool(4) as pool: rows = pool.map(one, grid, chunksize=1)
    json.dump(dict(x_degree=X, rows=rows), open(HERE / "grid_index.json", "w"), indent=0)
    print("wrote", len(rows), "slopes;", sum(r["series"] is None for r in rows), "undefined")
