"""B1629 -- the sealed instrument unchanged and its run kept; the repaired run: LR the unique lowest thread (sqrt5/2, then sqrt2 --
B482's Markov values), L^k R climbing, the cusp-time fraction (k+1)/2^k at every length; GENESIS v1.38."""
import hashlib, json, math, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1629_does_the_principle_reach_the_weaves_cusp"


def test_sealed_and_repaired():
    first = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 0ec9e2673: ")
    assert hashlib.sha256(open(ARC / "verification" / "cusp_reach.py", "rb").read()).hexdigest() == first.split()[4]
    s = json.load(open(ARC / "verification" / "sealed_run" / "cusp_reach.json"))
    assert s["C1"]["longest_run_L"] == 3 and s["C4"]["trace_L"] == 2                        # the sealed run as it was
    p = json.load(open(ARC / "verification" / "post_seal_cusp.json"))
    assert p["P2"]["LR_is_lowest"] and p["P2"]["argmin"] == ["LR"] and abs(p["P2"]["min_top"] - math.sqrt(5) / 2) < 1e-6
    assert abs(p["P2"]["second_lowest"] - math.sqrt(2)) < 1e-6
    tops = p["P2"]["L^k R"]; assert all(tops[str(k + 1)] > tops[str(k)] for k in range(1, 12))
    for n, row in p["P4_fraction_of_letters_in_runs_ge_k"].items():
        if int(n) >= 16:
            assert all(abs(row[str(k)] - (k + 1) / 2 ** k) < 2e-3 for k in range(2, 9))
    g = ROOT.joinpath("GENESIS.md").read_text(encoding="utf-8")
    assert int(g.split("**Version 1.")[1].split()[0]) >= 38 and "nothing the principle forces visits the weave's cusp" in g
    assert subprocess.run([sys.executable, str(ARC / "adoption" / "amend.py"), "--check"]).returncode == 0
