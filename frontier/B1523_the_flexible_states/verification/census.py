#!/usr/bin/env python3
"""B1523 -- the census, run after the seal: both routes on every manifold of the 758 word states to length 12 (536 manifolds).

For each manifold, route R (route_r.py: the real form, SnapPy's simplified presentation) and route C (route_c.py: the complex
form, the unsimplified presentation) each give: H^1 with coefficients in R, so(3,1) and v (dimensions and singular-value
margins); when dim H^1(v) = 1, the class's restriction to the cusp, the two slopes (the fibre boundary and the section), and for
every isometry its cusp map, its sign eps on the class, its action on H^1(P; v), and the residual, lattice and normaliser checks.
Nothing is interpreted here; read_out.py reads the predictions.

Before any census record is used, the three literature controls are re-read and must agree with controls.json (the banked
identity). The run appends each manifold to census_partial.jsonl as it finishes (a killed run resumes where it stopped) and
writes census.json at the end.
Usage: python3 census.py   (four workers; about an hour)"""
import json
import multiprocessing as mpc
import pathlib
import sys
import time
import warnings

warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import words  # noqa: E402

CONTROLS = ["b++LR", "b++LLRR", "b++LLR"]


def slim(r, c):
    """the fields the read-out uses, from the two routes' records"""
    def dims(x):
        return {k: {"dim": x["H1 " + k]["dim"], "fox margin": x["H1 " + k]["fox margin"],
                    "coboundary margin": x["H1 " + k]["coboundary margin"]} for k in ("triv", "so", "v")}
    out = {"R": {"relator error": r["relator error"], "H1": dims(r)}, "C": {"relator error": c["relator error"], "H1": dims(c)}}
    if r["H1 v"]["dim"] == 1:
        out["R"].update({"shape": [r["cusp"]["shape t_lambda / t_mu"]], "H1(P; v)": r["cusp"]["H1(P; v)"],
                         "class on the cusp (relative norm)": r["cusp"]["class in H1(P; v) (norm, relative)"],
                         "slope residual": r["cusp"]["slope residual"], "slope box": r["cusp"]["slope box"],
                         "translation defect": r["cusp"]["translation acts trivially (defect)"],
                         "isometries": [{k: i[k] for k in ("cusp map", "det", "inverts the fibre boundary", "eps", "residual",
                                                           "lattice check", "normaliser check", "on H1(P; v)")} for i in r["isometries"]]})
    if c["H1 v"]["dim"] == 1:
        out["C"].update({"shape": [c["cusp"]["shape t_lambda / t_mu"]], "H1(P; v)": c["cusp"]["H1(P; v)"],
                         "class on the cusp (relative norm)": c["cusp"]["class in H1(P; v) (norm, relative)"],
                         "slope test": c["slope test"], "translation defect": c["translation acts trivially (defect)"],
                         "isometries": [{k: i[k] for k in ("cusp map", "det", "inverts the fibre boundary", "eps", "residual",
                                                           "lattice check", "normaliser check", "on H1(P; v)")} for i in c["isometries"]]})
    return out


def one(rec):
    try:
        import route_c as RC
        import route_r as RR
        t0 = time.time()
        r = RR.record(rec["snappy"])
        t1 = time.time()
        c = RC.record(rec["snappy"])
        t2 = time.time()
        return {"snappy": rec["snappy"], "manifold": rec["sign"] + rec["word"], "length": rec["length"],
                "states": [s + w for s, w in rec["states"]], "kinds": rec["kinds"], "isometry order (words)": rec["isometry order"],
                "a longitude-inverting isometry (words)": rec["a longitude-inverting isometry"],
                **slim(r, c), "seconds": [round(t1 - t0, 1), round(t2 - t1, 1)]}
    except Exception as e:  # reported, never swallowed
        import traceback
        return {"snappy": rec["snappy"], "error": f"{type(e).__name__}: {e}", "trace": traceback.format_exc()[-2000:]}


def banked_identity(census_by_name):
    """the census's own records of the literature controls agree with controls.json's (dimensions, signs, slopes)"""
    ctrl = json.loads((HERE / "controls.json").read_text())
    ok = ctrl["all controls pass"]
    for name in CONTROLS:
        cr = ctrl["C5"]["records"][name]["R"]
        d = census_by_name[name]
        ok &= [cr["H1 " + k]["dim"] for k in ("triv", "so", "v")] == [d["R"]["H1"][k]["dim"] for k in ("triv", "so", "v")]
        ok &= [i["cusp map"] for i in cr["isometries"]] == [i["cusp map"] for i in d["R"]["isometries"]]
        ok &= all(abs(a["eps"] - b["eps"]) < 1e-30 for a, b in zip(cr["isometries"], d["R"]["isometries"]))
        ok &= all((cr["cusp"]["slope residual"][k] > 1e-20) == (d["R"]["slope residual"][k] > 1e-20) for k in cr["cusp"]["slope residual"])
    return bool(ok)


def main():
    import snappy  # noqa: F401  (imported in the main thread first)
    t0 = time.time()
    man = words.manifolds(12)
    recs = sorted(man.values(), key=lambda m: (m["length"], m["snappy"]))
    partial = HERE / "census_partial.jsonl"
    done = {}
    if partial.exists():
        for line in partial.read_text().splitlines():
            d = json.loads(line)
            if "error" not in d:
                done[d["snappy"]] = d
    # the controls go first, so the banked identity is read before anything else
    order = [r for r in recs if r["snappy"] in CONTROLS] + [r for r in recs if r["snappy"] not in CONTROLS]
    todo = [r for r in order if r["snappy"] not in done]
    print(f"census: {len(recs)} manifolds, {len(done)} already done, {len(todo)} to run", flush=True)
    with mpc.Pool(4) as pool, partial.open("a") as f:
        for k, d in enumerate(pool.imap(one, todo, chunksize=1), 1):
            f.write(json.dumps(d) + "\n")
            f.flush()
            if "error" in d:
                print("ERROR", d["snappy"], d["error"], flush=True)
                continue
            done[d["snappy"]] = d
            print(f"{k}/{len(todo)} {d['snappy']} v: R {d['R']['H1']['v']['dim']} C {d['C']['H1']['v']['dim']} "
                  f"({d['seconds'][0]} s, {d['seconds'][1]} s)", flush=True)
    missing = [r["snappy"] for r in recs if r["snappy"] not in done]
    ident = banked_identity(done) if all(n in done for n in CONTROLS) else False
    census = {"manifolds": [done[r["snappy"]] for r in recs if r["snappy"] in done], "missing": missing,
              "banked identity (controls re-read)": ident, "seconds": round(time.time() - t0)}
    (HERE / "census.json").write_text(json.dumps(census, separators=(",", ":")))
    print(f"census.json written: {len(census['manifolds'])} manifolds, missing {len(missing)}, banked identity {ident}, "
          f"{census['seconds']} s", flush=True)


if __name__ == "__main__":
    main()
