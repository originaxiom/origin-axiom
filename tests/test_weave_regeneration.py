"""Regeneration: the weave dossier's fast scripts rerun in a scratch copy reproduce their stored outputs.

Step 4 of the assurance plan (2026-10-08). The mutation run showed that the result tests, which read stored JSON, catch
bugs in the shared conventions but not bugs introduced later into an arc's own script. Rerunning and diffing caught all
ten injected bugs. So this test reruns each fast script in a copy of the dossier and compares its output with the stored
file. For W41, whose script takes minutes, a probe recomputes three of its stored numbers.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
FAST = ["the_mixing_patterns_verified", "the_couplings_verified", "the_couplings_exact", "the_weave_at_omega_verified",
        "the_breaking_verified", "the_trimaximal_families", "the_index_on_the_weaves_surface",
        "the_end_conditions_on_the_weaves_surface", "the_unit_at_the_weaves_cusp", "the_outside_source_at_the_cusp",
        "the_generations_are_a_multiplicity", "the_parity_grading_at_a_fixed_tau"]


def close(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(close(a[k], b[k]) for k in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(close(x, y) for x, y in zip(a, b))
    if isinstance(a, float) and isinstance(b, float):
        return abs(a - b) <= 1e-9 * max(1.0, abs(a))
    return a == b


@pytest.fixture(scope="module")
def copy(tmp_path_factory):
    """a mirror of the repository: symlinks everywhere except a real copy of the weave dossier (the scripts find the
    repository root by its frontier/ directory, and some read files there)"""
    repo = tmp_path_factory.mktemp("repo")
    for top in ROOT.iterdir():
        if top.name != "docs" and not top.name.startswith("."):
            (repo / top.name).symlink_to(top)
    for sub in (ROOT / "docs").iterdir():
        if sub.name != "dossiers":
            (repo / "docs").mkdir(exist_ok=True)
            (repo / "docs" / sub.name).symlink_to(sub)
    (repo / "docs" / "dossiers").mkdir(parents=True, exist_ok=True)
    for d in (ROOT / "docs" / "dossiers").iterdir():
        if d.name != HERE.name:
            (repo / "docs" / "dossiers" / d.name).symlink_to(d)
    dst = repo / "docs" / "dossiers" / HERE.name
    shutil.copytree(HERE, dst, ignore=shutil.ignore_patterns("__pycache__"))
    return dst


@pytest.mark.parametrize("script", FAST)
def test_fast_scripts_reproduce_their_outputs(copy, script):
    stored = json.loads((HERE / (script + ".json")).read_text(encoding="utf-8"))
    r = subprocess.run([sys.executable, str(copy / (script + ".py"))], cwd=copy, capture_output=True, text=True,
                       timeout=600)
    assert r.returncode == 0, r.stderr[-2000:]
    fresh = json.loads((copy / (script + ".json")).read_text(encoding="utf-8"))
    assert close(stored, fresh), script


def test_w41_probe(copy):
    probe = r'''
import json, sys
sys.path.insert(0, ".")
import numpy as np, mpmath as mp
import the_zero_modes_weight as ZW
mp.mp.dps = 20
d = json.load(open("the_zero_modes_weight.json"))
W, r, e = ZW.laws(ZW.MATS["T"], ZW.TAU0)
ok_T = bool(np.allclose(W, np.diag([1, 1j]), atol=1e-9) and abs(e[0] - np.exp(1j * np.pi / 4)) < 1e-9 and r < 1e-10)
W, r, e = ZW.laws(ZW.MATS["U"], ZW.TAU1)
ok_U = bool(r < 1e-10 and abs(e[0] + 1j) < 1e-9)
g0 = ZW.g_of(ZW.TAU0, npts=48)
gS = ZW.g_of(ZW.act(ZW.MATS["S"], ZW.TAU0), npts=48)
ok_g = bool(abs(g0 / d["K1: g = N / (Im tau)^(3/4) under the moves"]["tau0"]["g(tau)"] - 1) < 1e-6 and abs(gS / g0 - 1) < 1e-6)
print(json.dumps([ok_T, ok_U, ok_g]))
'''
    r = subprocess.run([sys.executable, "-c", probe], cwd=copy, capture_output=True, text=True, timeout=900)
    assert r.returncode == 0, r.stderr[-2000:]
    assert json.loads(r.stdout.strip().splitlines()[-1]) == [True, True, True]
