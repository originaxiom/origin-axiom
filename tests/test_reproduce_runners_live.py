"""THE BELT RUNS (B1240). Twenty-seven tests on main lock `REPRODUCES` as a STRING found in a committed record,
with no subprocess anywhere in the file (`scripts/checks/reproduce_belt.py --string-locks`); five of the runners
they pin could not run on a fresh clone at all (their certificates lived on a seat branch; B1240 vendored the
closure). This file RUNS the runners. Every belt arc's `reproduce*.sh` executes in a temporary copy of its
verification directory -- the tree is never written (B1149's `our_trace_three.out` is tracked) -- except the
three that read sibling arcs by relative path, which run in place and are checked to write nothing.

Default lane: the 21 fast runners in full (~1 s each) and the five heavy harvest runners on their fastest
certificate via the `CERTS` override (~15 s total).  OA_SLOW=1: the five heavy runners in full (~4 min).
B1175 is RECORD-only by its own honesty note (it re-runs nothing and says so) and is excluded.
"""
import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
FRONTIER = ROOT / "frontier"

# arc directory -> runner. The 21 self-contained fast runners (each cd's to its own directory).
FAST = {
    "B1156_seam_a_gate2": "reproduce.sh",
    "B1157_dynamics_null": "reproduce.sh",
    "B1158_cloud_wave2_harvest": "reproduce.sh",
    "B1159_mssm_debt_ledger": "reproduce.sh",
    "B1160_hypercharge_forced": "reproduce.sh",
    "B1161_frontier_sweep": "reproduce.sh",
    "B1162_mssm_debt_closure": "reproduce.sh",
    "B1163_w0_attempt": "reproduce.sh",
    "B1164_cc_masterplan": "reproduce.sh",
    "B1165_gravity_terminal": "reproduce.sh",
    "B1166_charter_attack": "reproduce.sh",
    "B1167_seat_harvest": "reproduce.sh",
    "B1168_c5_investigation": "reproduce.sh",
    "B1169_qualia_parity_synthesis": "reproduce.sh",
    "B1174_z2_identification": "reproduce.sh",
    "B1180_family_retraction": "reproduce.sh",
    "B1182_c4prime_resolved": "reproduce.sh",
    "B1184_quine_synthesis": "reproduce.sh",
}
# read sibling arcs / docs by relative path: run in place, must write nothing
IN_PLACE = {
    "B1171_seam_harvest": "reproduce.sh",
    "B1172_lose_nothing_register": "reproduce.sh",
    "B1173_digest_partial_close": "reproduce.sh",
}
# the five outside-bench harvests: (runner, fastest certificate for the default lane)
HEAVY = {
    "B1147_clane_harvest": ("reproduce_all.sh", "cusp_beat"),
    "B1148_carrier_harvest": ("reproduce_new.sh", "kappa_beat"),
    "B1149_meridian_longitude_harvest": ("reproduce.sh", "trace_three"),
    "B1150_yukawa_clock_and_family": ("reproduce.sh", "family_yukawa"),
    "B1153_peripheral_and_superposition": ("reproduce.sh", "c4b_superposition"),
}
# verdict-shaped failure markers: the runners print "rc=N  DIFF" / "(no committed output)" on a verdict line;
# prose containing DIFFERENT (B1166) must not trip this, so DIFF is matched as a whole word at line end
BAD_MARKERS = (re.compile(r"\bDIFF\s*$", re.M), re.compile(r"\(no committed output\)"),
               re.compile(r"^Traceback \(most recent call last\)", re.M))


def _run(arc, runner, tmp_path, certs=None, timeout=900):
    src = FRONTIER / arc / "verification"
    assert (src / runner).is_file(), f"{arc}: runner {runner} missing"
    env = dict(os.environ)
    if certs:
        env["CERTS"] = certs
    if arc in IN_PLACE:
        cwd = src
    else:
        cwd = tmp_path / arc / "verification"
        shutil.copytree(src, cwd)
    res = subprocess.run(["bash", str(cwd / runner)], cwd=cwd, capture_output=True, text=True,
                         timeout=timeout, env=env)
    return res


def _problems(arc, res):
    """what a non-reproducing run looks like, as a list the caller asserts empty (the assert stays in the
    test body so the vacuity checker can see it)."""
    out = res.stdout + res.stderr
    bad = []
    if res.returncode != 0:
        bad.append(f"{arc}: rc={res.returncode}")
    if "REPRODUCES" not in res.stdout:
        bad.append(f"{arc}: no REPRODUCES in stdout")
    for m in BAD_MARKERS:
        if m.search(res.stdout):
            bad.append(f"{arc}: marker {m.pattern!r} in stdout")
    return [b + "\n" + out[-1500:] for b in bad]


@pytest.mark.parametrize("arc", sorted(FAST))
def test_fast_runner_reproduces_live(arc, tmp_path):
    problems = _problems(arc, _run(arc, FAST[arc], tmp_path))
    assert problems == [], problems


def _snapshot(paths):
    return {p: (p.stat().st_size, p.stat().st_mtime_ns) for p in paths if p.is_file()}


@pytest.mark.parametrize("arc", sorted(IN_PLACE))
def test_in_place_runner_reproduces_and_writes_nothing(arc, tmp_path):
    files = list((FRONTIER / arc).rglob("*"))
    before = _snapshot(files)
    res = _run(arc, IN_PLACE[arc], tmp_path)
    problems = _problems(arc, res)
    assert problems == [], problems
    assert _snapshot(list((FRONTIER / arc).rglob("*"))) == before, f"{arc}: runner wrote into the tree"


@pytest.mark.parametrize("arc", sorted(HEAVY))
def test_heavy_runner_fastest_certificate_live(arc, tmp_path):
    runner, cert = HEAVY[arc]
    res = _run(arc, runner, tmp_path, certs=cert)
    problems = _problems(arc, res)
    assert problems == [], problems
    assert f"===== {cert} =====" in res.stdout, f"{arc}: CERTS override not honoured\n{res.stdout[-800:]}"


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 for the five heavy runners in full (~4 min)")
@pytest.mark.parametrize("arc", sorted(HEAVY))
def test_heavy_runner_full_live(arc, tmp_path):
    runner, _ = HEAVY[arc]
    res = _run(arc, runner, tmp_path)
    problems = _problems(arc, res)
    assert problems == [], problems
    banners = re.findall(r"^===== (\S+) =====", res.stdout, re.M)
    n_cert = len([b for b in banners if "DONE" not in b])     # the closing DONE banner is not a certificate
    n_ok = res.stdout.count("REPRODUCES")
    assert n_ok >= n_cert > 0, f"{arc}: {n_ok} REPRODUCES for {n_cert} certificates\n{res.stdout[-1200:]}"


def test_belt_census_is_complete():
    """every string-lock arc is in exactly one of the three run sets or is the documented record-only arc"""
    belt = set(FAST) | set(IN_PLACE) | set(HEAVY)
    assert len(belt) == 26
    assert not (set(FAST) & set(IN_PLACE)) and not (set(FAST) & set(HEAVY)) and not (set(IN_PLACE) & set(HEAVY))
    for arc in belt:
        assert (FRONTIER / arc / "verification").is_dir(), arc
    rec = (FRONTIER / "B1175_charter_close_harvest" / "verification" / "reproduce.sh").read_text(encoding="utf-8")
    assert "RE-RUNS NOTHING" in rec and "RECORD" in rec     # the one excluded arc says so itself
