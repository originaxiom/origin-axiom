"""B1235 -- the two-seat harvest. Locks pin FACTS (E53 rule 3), never strings.

The family count is RECOMPUTED (proper chirality test) on the named witnesses; the full 112 recount
is the arc's cell 1 and its JSON is checked for internal consistency against B1224 here.
"""
import json
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1235_two_seat_harvest"
VER = ARC / "verification"


def _cs_mod_half(cs):
    return (cs + 0.25) % 0.5 - 0.25


def test_the_named_witnesses_by_the_proper_test():
    snappy = pytest.importorskip("snappy")
    got = {}
    for name in ("o10_150700", "t12840", "s955", "m202", "s118", "m004"):
        M = snappy.Manifold(name)
        got[name] = (M.symmetry_group().is_amphicheiral(), round(_cs_mod_half(float(M.chern_simons())), 4))
    assert got["o10_150700"] == (False, -0.0833)        # chiral, CS = -1/12  (the B8147 '83/83' killer)
    assert got["m202"][0] is False and got["s118"][0] is False
    assert got["t12840"] == (True, 0.0)
    assert got["s955"][0] is True and abs(abs(got["s955"][1]) - 0.25) < 1e-3
    assert got["m004"] == (True, 0.0)                    # the headline survives


def test_the_112_recount_is_38_and_b1224_consistent():
    rows = json.loads((VER / "chirality_112.json").read_text(encoding="utf-8"))
    assert len(rows) == 112
    amph = [r for r in rows if r["amphicheiral"] is True]
    chir = [r for r in rows if r["amphicheiral"] is False]
    assert len(amph) == 38 and len(chir) == 74
    for r in amph:                                       # amphichiral => CS in {0, 1/4} mod 1/2 (B1224)
        v = _cs_mod_half(r["cs"])
        assert min(abs(v), abs(abs(v) - 0.25)) < 1e-6, r
    silent = [r for r in chir if min(abs(_cs_mod_half(r["cs"])), abs(abs(_cs_mod_half(r["cs"])) - 0.25)) < 1e-6]
    assert len(silent) == 38                             # CS-silent chirality: what a CS-only check misses


def test_the_free_deck_selects_cs_zero_as_data():
    d = json.loads((VER / "a6_cover_cs.json").read_text(encoding="utf-8"))
    s = d["summary"]
    assert s["covers_cs0"] == s["slice"] == 40 and s["covers_cs_quarter"] == 0
    c = d["control"]
    assert c["family112_at_quarter"] + c["census200_at_quarter"] >= 10   # the 1/4 class is COMMON among amphichiral manifolds
    # so 40/40 at zero is not what amphichirality alone would give: (1-0.36)^40 ~ 2e-8


def test_b1233_minimum_is_a_box_minimum():
    r = subprocess.run([sys.executable, str(VER / "markoff_box_minimum.py")], capture_output=True, text=True, cwd=str(VER))
    assert r.returncode == 0, r.stdout + r.stderr
    assert "NOT global on R^3" in r.stdout and "equality only at the origin" in r.stdout


def test_b994_chains_are_not_subgroup_chains_but_the_endpoint_survives():
    su = {n: n * n - 1 for n in (3, 4, 5)}
    assert su[4] > su[3] and su[5] > su[3]               # a simple algebra maps injectively or trivially
    r = subprocess.run([sys.executable, str(VER / "b994_parent_menus.py")], capture_output=True, text=True, cwd=str(VER))
    assert r.returncode == 0, r.stdout + r.stderr
    block = r.stdout.split("parent SU(3)^3")[1].split("cascade")[0]
    assert "su(4)" not in block and "su(5)" not in block   # no Pati-Salam / SU(5) rung on SU(3)^3's menu
    assert r.stdout.count("endpoint: su(2) + su(3) + 3 u(1)") == 3


def test_ten_a2a1_subdiagrams():
    r = subprocess.run([sys.executable, str(VER / "a2a1_subdiagrams.py")], capture_output=True, text=True)
    assert r.returncode == 0 and "10" in r.stdout


def test_e51_manifest_and_the_gitignore_trap():
    m = json.loads((VER / "e51_manifest.json").read_text(encoding="utf-8"))
    assert len(m["files"]) == 9 and m["head"] == "53da05f6"
    assert sum(f["bytes"] for f in m["files"]) == 88060
    try:
        subprocess.check_output(["git", "cat-file", "-t", m["head"]], cwd=str(ROOT), stderr=subprocess.DEVNULL)
    except Exception:
        pytest.skip("audit/b775-braver-questions not fetched on this bench")
    for f in m["files"]:
        size = int(subprocess.check_output(["git", "cat-file", "-s", f"{m['head']}:{f['path']}"], cwd=str(ROOT)))
        assert size == f["bytes"]
    # A03: the trap is real -- B1148's named witnesses are ignored repo-wide
    r = subprocess.run(["git", "check-ignore", "-q", "frontier/B1148_carrier_harvest/verification/reproduce.log"], cwd=str(ROOT))
    assert r.returncode == 0


def test_b1181_is_retracted_and_its_lock_now_pins_the_fact():
    d = json.loads((ROOT / "frontier" / "B1181_amphichirality_closure" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "RETRACTED" and d["superseded_by"] == "B1235"
    t = (ROOT / "tests" / "test_b1181_amphichirality_closure.py").read_text(encoding="utf-8")
    assert "38" in t and "is_amphicheiral" in t


def test_the_two_spin_rows_are_registered_unearned_and_the_baseline_was_raised_by_hand():
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8")
    for row in ("I-10", "I-11"):
        line = next(l for l in led.splitlines() if l.startswith(f"| {row} |"))
        assert "UNEARNED" in line
    base = json.loads((ROOT / "docs" / "IDENTIFICATION_BASELINE.json").read_text(encoding="utf-8"))
    assert base["unearned"] == 5 and any(r.get("to") == 5 for r in base["_baseline_raises"])


def test_the_absence_rule_and_its_instrument():
    w = (ROOT / "WORKING_RULES.md").read_text(encoding="utf-8")
    assert "THE ABSENCE RULE" in w and "swipe the repo first" in w   # the owner's words, verbatim
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "checks" / "absence_sweep.py"), "--selftest"],
                       capture_output=True, text=True, cwd=str(ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CONTROLS PASS" in r.stdout
