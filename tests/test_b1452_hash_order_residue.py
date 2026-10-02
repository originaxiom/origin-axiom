"""B1452 lock -- the hash-order residue, run.

Live: two of the sixteen scripts under two hash seeds print the same thing; B904's script, run in a copy of its
directory, prints one dictionary in an order that may differ and is equal as a dictionary; and the comparison can
fail (a seed-dependent line is detected).  Recorded: the sixteen scripts' classification over four seeds.
"""
import ast
import json
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1452_the_hash_order_residue_run"


def run(script, seed, cwd):
    env = dict(os.environ, PYTHONHASHSEED=str(seed), PYTHONDONTWRITEBYTECODE="1", MPLBACKEND="Agg")
    r = subprocess.run([sys.executable, str(script)], cwd=str(cwd), capture_output=True, text=True, timeout=900, env=env)
    assert r.returncode == 0, r.stderr[-400:]
    return r.stdout


def test_two_scripts_print_the_same_thing_on_two_seeds_live():
    for rel in ("frontier/B155_golden_phase_bridge/golden_phase_bridge.py", "frontier/B469_breath_campaign/br3_orbit_fields.py"):
        p = ROOT / rel
        assert run(p, 0, p.parent) == run(p, 1, p.parent), rel


def test_the_comparison_can_fail_live(tmp_path):
    probe = tmp_path / "probe.py"
    probe.write_text("print(list({'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta'}))\n")
    outs = {run(probe, s, tmp_path) for s in range(6)}
    assert len(outs) > 1, "a set of strings printed unsorted depends on the seed, and the comparison sees it"


def test_b904_differs_only_in_the_order_of_one_dictionary_live(tmp_path):
    d = tmp_path / "B904"; shutil.copytree(ROOT / "frontier" / "B904_barton_sudbery", d)
    got = []
    for seed in (0, 1):
        out = run(d / "stage2c_final.py", seed, d)
        line = next(l for l in out.splitlines() if l.startswith("fitted: "))
        got.append((ast.literal_eval(line[len("fitted: "):]), [l for l in out.splitlines() if not l.startswith("fitted: ")], json.load(open(d / "stage2c_results.json"))))
    assert got[0][0] == got[1][0] and got[0][1] == got[1][1] and got[0][2] == got[1][2]


def test_the_sixteen_recorded():
    d = json.load(open(ARC / "verification" / "seed_runs.json"))
    assert d["scripts"] == 16 and d["sites"] == 24 and d["numbers_changed"] == 0 and d["sites_settled_by_execution"] == 22
    assert d["counts"] == {"COSMETIC": 1, "DOES NOT RUN HERE; SETTLED BY READING": 1, "IDENTICAL": 14}
    sweep = json.load(open(ROOT / d["source"]))
    listed = {}
    for s in sweep["unsorted_sites"]:
        if not s["file"].startswith("tests/"): listed.setdefault(s["file"], []).append(s["line"])
    assert {r["script"]: r["sites"] for r in d["runs"]} == listed, "the sixteen are the sweep's"
    for r in d["runs"]:
        assert r["seeds"] == 4 and (ROOT / r["script"]).is_file()
        assert r["distinct_outputs_after_removing_timings"] == (2 if r["classification"] == "COSMETIC" else 1), r["script"]
    assert "L238" in open(ROOT / "docs" / "OPEN_LEADS.md").read()
