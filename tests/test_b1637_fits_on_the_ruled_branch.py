"""B1637 -- fits on the ruled branch.  Sealed instrument unchanged; the stored cells graded as on the page: F3 (each sector
alone fits, spread of best Im tau > 1), F4 (u and d at weight 3 fail on all 13), F5 (fits exist, every one with P >= 15;
the smallest 21), F2's recorded failure as worded (the masses-only chi2 below 100) kept visible; the bite -- the stored
P formula reproduces 2 + sum(2 d(k) - 1) for every assignment."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch"


def _d():
    return json.load(open(A / "verification" / "fits_on_the_ruled_branch.json"))


def test_sealed_unchanged():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 3ef9c3f8f")
    assert hashlib.sha256(open(A / "verification" / "fits_on_the_ruled_branch.py", "rb").read()).hexdigest() == first.split()[4]
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def test_cells_as_graded():
    d = _d()
    f3 = d["F3_each_sector_alone"]
    assert all(r["chi2_min"] < 3 for r in f3)
    ys = [r["tau"][1] for r in f3]; assert max(ys) - min(ys) > 1
    best = {}
    for r in d["F4_scan_a0.10"]:
        if r["ckm"]:
            k = tuple(r["ks"]); best[k] = min(best.get(k, 1e99), r["chi2_min"])
    assert all(v > 13 for k, v in best.items() if k[0] == 3 and k[1] == 3)
    fits = [k for k, v in best.items() if v <= 13]
    assert fits and d["F5"]["smallest_P_that_fits"] == 21
    m010 = [r["chi2_min"] for r in d["F2"] if r["a"] == 0.1 and not r["ckm"]]
    assert min(m010) < 100                          # F2 failed as worded: kept visible
    assert all(r["chi2_min"] > 300 for r in d["F2"] if r["ckm"])   # but excluded on all 13 at every allowance


def test_bite_parameter_count():
    dims = {int(k): v for k, v in _d()["dims"].items()}
    for r in _d()["F4_scan_a0.10"]:
        assert r["P"] == 2 + sum(2 * dims[k] - 1 for k in r["ks"])
