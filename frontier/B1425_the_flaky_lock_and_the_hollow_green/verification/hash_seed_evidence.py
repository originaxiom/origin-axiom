"""B1425 evidence -- the lock called flaky was hash-order-dependent (E83), measured on both versions.

Pulls the PRE-FIX script out of git (the committed version at HEAD) and runs it beside the fixed one
under a range of PYTHONHASHSEED values. A lock that is genuinely flaky fails at random; a lock with
this defect fails on a REPRODUCIBLE set of seeds, which is what separates E83 from load.
"""
import json
import os
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[3]
REL = "frontier/B1411_the_sm_seats_v10_arcs_harvested/verification/main_b1355_geometry.py"
OUT = pathlib.Path(__file__).resolve().parent / "hash_seed_evidence.json"
SEEDS = [str(s) for s in range(8)]


def run(path, seed):
    env = dict(os.environ, PYTHONHASHSEED=seed)
    r = subprocess.run([sys.executable, str(path)], capture_output=True, text=True, timeout=900, env=env)
    return {"seed": seed, "returncode": r.returncode, "verified": "VERIFIED" in r.stdout,
            "tail": (r.stdout + r.stderr).strip().split("\n")[-1][:200]}


def main():
    res = {"script": REL, "seeds": SEEDS}
    pre = subprocess.run(["git", "show", "HEAD:" + REL], cwd=ROOT, capture_output=True, text=True)
    assert pre.returncode == 0, "cannot read the pre-fix script from git"
    res["pre_fix_hands_a_set_to_the_solver"] = "list(X.free_symbols)" in pre.stdout
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "pre_fix_main_b1355_geometry.py"
        p.write_text(pre.stdout)
        res["pre_fix"] = [run(p, s) for s in SEEDS]
    res["post_fix"] = [run(ROOT / REL, s) for s in SEEDS]
    res["post_fix_sorts_the_unknowns"] = "sorted(X.free_symbols" in (ROOT / REL).read_text()

    res["pre_fix_pass_seeds"] = [r["seed"] for r in res["pre_fix"] if r["returncode"] == 0]
    res["pre_fix_fail_seeds"] = [r["seed"] for r in res["pre_fix"] if r["returncode"] != 0]
    res["post_fix_pass_seeds"] = [r["seed"] for r in res["post_fix"] if r["returncode"] == 0]
    # the finding: the pre-fix script is seed-DEPENDENT (both outcomes occur), the fixed one is not
    res["pre_fix_is_seed_dependent"] = bool(res["pre_fix_pass_seeds"]) and bool(res["pre_fix_fail_seeds"])
    res["post_fix_is_seed_independent"] = len(res["post_fix_pass_seeds"]) == len(SEEDS)
    res["verdict"] = ("E83 CONFIRMED and FIXED" if res["pre_fix_is_seed_dependent"] and res["post_fix_is_seed_independent"]
                      else "INCONCLUSIVE")
    OUT.write_text(json.dumps(res, indent=1) + "\n")
    print(json.dumps({k: v for k, v in res.items() if k not in ("pre_fix", "post_fix")}, indent=1))


if __name__ == "__main__":
    main()
