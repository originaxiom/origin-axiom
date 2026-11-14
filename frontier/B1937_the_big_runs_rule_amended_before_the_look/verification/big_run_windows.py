"""THE BIG RUN's window companion (main, 2026-11-14, before the look; the rule's amendment A2, audit finding V1).
B1720's random-target windows are a declared choice whose price is not known. This script reports the two governing
calibrations (chi2_7 and the worst factor over the seven, best of the four options) with every window's ends moved half
a decade out, and half a decade in, beside B1720's own. REPORTED, NOT GOVERNING: the outcome is big_run_look_v2.py's.
It reads the same pinned files and writes big_run_windows_output.json.
    python3 -B big_run_windows.py"""
import hashlib, json, pathlib, random, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import big_run_look_v2 as L
WINDOWS = {   # (r2, r1) per mass sector, then (a, b, c) for the moduli: log10 ranges
    "B1720": {"r2": (-3, -1), "r1": (-6, -2.5), "a": (-1.5, -0.2), "b": (-2.5, -0.7), "c": (-3.5, -1.5)},
    "half a decade out": {"r2": (-3.5, -0.5), "r1": (-6.5, -2.0), "a": (-2.0, 0.3), "b": (-3.0, -0.2), "c": (-4.0, -1.0)},
    "half a decade in": {"r2": (-2.5, -1.5), "r1": (-5.5, -3.0), "a": (-1.0, -0.7), "b": (-2.0, -1.2), "c": (-3.0, -2.0)},
}


def random_nine(rng, W):
    r = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(*W["r2"]); r1 = 10 ** rng.uniform(*W["r1"])
            if r1 < r2:
                break
        r += [r2, r1]
    while True:
        a, b, c = 10 ** rng.uniform(*W["a"]), 10 ** rng.uniform(*W["b"]), 10 ** rng.uniform(*W["c"])
        if c < b < a:
            break
    return r + [a, b, c]


def windows(values_path, data_path, ckm_path, out_path):
    V = json.loads(pathlib.Path(values_path).read_text(encoding="utf-8"))
    assert V["positions"] == L.POSITIONS and sorted(V["options"]) == sorted(L.OPTIONS)
    tl, sig = L.targets(data_path, ckm_path)
    M = np.log(np.array([L.nine_from_option(V["options"][o]["values"]) for o in L.OPTIONS]))
    S = L.stats(M, tl, sig); keys = ("chi2_seven", "worst_factor_seven")
    best = {k: float(np.min(S[k])) for k in keys}
    out = {"reported_not_governing": True, "best": best, "by_window": {}}
    for name, W in WINDOWS.items():
        rng = random.Random(L.SEED); hits = {k: 0 for k in keys}
        for _ in range(L.N_CAL):
            R = L.stats(M, np.log(np.array(random_nine(rng, W))), sig)
            for k in keys:
                hits[k] += float(np.min(R[k])) <= best[k] + 1e-12
        out["by_window"][name] = {"windows_log10": W, "fraction_as_good": {k: hits[k] / L.N_CAL for k in keys}}
    pathlib.Path(out_path).write_text(json.dumps(out, indent=1))
    return out


def main():
    assert hashlib.sha256(L.VALUES.read_bytes()).hexdigest() == L.VALUES_SHA, "the values are not the committed ones"
    assert hashlib.sha256(L.DATA.read_bytes()).hexdigest() == L.SHA and hashlib.sha256(L.CKMDATA.read_bytes()).hexdigest() == L.CKMSHA
    windows(L.VALUES, L.DATA, L.CKMDATA, HERE / "big_run_windows_output.json")
    print("written; sha256", hashlib.sha256((HERE / "big_run_windows_output.json").read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
