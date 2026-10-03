#!/usr/bin/env python3
"""B1523 post-run check X1 (written after the seal and after the census ran): route F on a stratified set of manifolds, compared with
the census. Route F rebuilds each bundle from its word (no SnapPy holonomy) and finds its hyperbolic fibre representation by Newton on
the trace map; SnapPy's cusp shape only picks which fixed point is the hyperbolic one. Where the search does not find it within its
starts, the manifold is reported as not reached (a coverage gap, never a reading).

The set: every manifold of length <= 8 (68), the 42 swaprev-only and the 2 swap-only manifolds (whose dualising status turns on the
fibre boundary's rigidity), the 14 golden ones, and the 23 whose section is not a rigid slope.
Usage: python3 route_f_batch.py   (writes route_f_batch.jsonl as it goes, and route_f_batch.json at the end)"""
import json
import multiprocessing as mpc
import pathlib
import sys
import time
import warnings

warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def chosen():
    rows = json.loads((HERE / "read_out.json").read_text())["rows"]
    ctrl = json.loads((HERE / "controls.json").read_text())
    golden = {g["state"] for g in ctrl["C1"]["golden (monodromy field Q(sqrt5))"]}
    pick = []
    for r in rows:
        k = r["kinds"]
        kind = ("swaprev only" if k["swaprev"] and not k["rev"] and not k["swap"] else
                "swap only" if k["swap"] and not k["rev"] and not k["swaprev"] else None)
        if r["length"] <= 8 or kind or r["manifold"] in golden or r.get("section rigid") is False:
            pick.append(r["manifold"])
    return pick


def one(state):
    import snappy
    import route_f as F
    sign, word = state[0], state[1:]
    t0 = time.time()
    try:
        sh = complex(snappy.Manifold(("b++" if sign == "+" else "b+-") + word).cusp_info("shape")[0])
        rec = F.record_fast(sign, word, sh, starts=600)
    except Exception as e:  # reported, never swallowed
        rec = {"state": state, "error": f"{type(e).__name__}: {e}"}
    rec["seconds"] = round(time.time() - t0, 1)
    return rec


def main():
    import snappy  # noqa: F401
    states = chosen()
    out_path = HERE / "route_f_batch.jsonl"
    done = {}
    if out_path.exists():
        for line in out_path.read_text().splitlines():
            d = json.loads(line)
            done[d["state"]] = d
    todo = [s for s in states if s not in done]
    print(f"route F batch: {len(states)} manifolds, {len(done)} done, {len(todo)} to run", flush=True)
    with mpc.Pool(4) as pool, out_path.open("a") as f:
        for d in pool.imap_unordered(one, todo):
            f.write(json.dumps(d, default=str) + "\n")
            f.flush()
            done[d["state"]] = d
            print(d["state"], d.get("hyperbolic found"), [d.get("H1 " + k, {}).get("dim") for k in ("triv", "so", "v")],
                  d.get("fibre boundary residual"), d["seconds"], flush=True)
    # the comparison with the census
    rows = {r["manifold"]: r for r in json.loads((HERE / "read_out.json").read_text())["rows"]}
    reached = [d for d in done.values() if d.get("hyperbolic found")]
    agree = [d for d in reached if [d["H1 " + k]["dim"] for k in ("triv", "so", "v")] == rows[d["state"]]["dims R"]
             and (d["fibre boundary residual"] is not None and d["fibre boundary residual"] > 1e-20) == rows[d["state"]]["fibre boundary rigid"]]
    summary = {"chosen": len(states), "reached": len(reached), "not reached": sorted(s for s in states if not done.get(s, {}).get("hyperbolic found")),
               "agree with the census (dimensions and the fibre boundary)": len(agree),
               "disagree": sorted(d["state"] for d in reached if d not in agree),
               "smallest fibre-boundary residual among those reached": min((d["fibre boundary residual"] for d in reached
                                                                            if d["fibre boundary residual"] is not None), default=None),
               "records": sorted(done.values(), key=lambda d: d["state"])}
    (HERE / "route_f_batch.json").write_text(json.dumps(summary, indent=1, default=str))
    print(json.dumps({k: v for k, v in summary.items() if k != "records"}, default=str))


if __name__ == "__main__":
    main()
