"""B1411 lock: main's own re-derivations of the SM seat's B1351 (level 3) and B1355 (geometry) re-run live; the 21-lock
receipt and the B1352 run are present and carry their numbers."""
import os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1411_the_sm_seats_v10_arcs_harvested", "verification")

def test_b1355_geometry_is_exact():
    # DIAGNOSIS CORRECTED 2026-09-18 (B1425). On 2026-09-17 this was called a timeout under load and the
    # timeout was raised from 600 to 1800 s. That was WRONG. The script was hash-order dependent -- it
    # solved for the commutant's unknowns in the order a SET happened to iterate -- so it passed on about
    # one PYTHONHASHSEED in five, independently of load. Measured over eight seeds: PASS on 4 and 7 only, and the failing set is reproducible. Both an
    # outside referee's "it passes for me" and this bench's "it passes in isolation" were luck. The script
    # is now deterministic and asserts the mathematics rather than one normalisation of sympy's answer;
    # the generous timeout is kept because it costs nothing.
    r = subprocess.run([sys.executable, os.path.join(V, "main_b1355_geometry.py")], capture_output=True, text=True, timeout=1800)
    assert r.returncode == 0 and "VERIFIED" in r.stdout and "|2T| = 24" in r.stdout, r.stdout[-800:] + r.stderr[-800:]

def test_b1352_run_carries_both_points():
    t = open(os.path.join(V, "main_b1352_locus_check_run.txt"), encoding="utf-8").read()
    assert t.count("h^1(27) = 3") == 2 and t.count("N = h^1(27) - h^1(27bar) = 0") == 2 and t.count("dim 3") == 2
    assert all(float(x) < 1e-50 for x in re.findall(r"relator residual \(a->1, b->2\): ([0-9.e+-]+)", t))

def test_sm_locks_receipt_is_green():
    t = open(os.path.join(V, "sm_locks_rerun_1703c0d8.txt"), encoding="utf-8").read()
    assert "21 passed" in t and "failed" not in t and t.rstrip().endswith("EXIT 0")

def test_b1351_level_three_live():
    """the level-3 half of main_b1351_closings.py, live (seconds): 15 characters, no mismatch"""
    src = open(os.path.join(V, "main_b1351_closings.py"), encoding="utf-8").read().replace("for n in (3,4,5): run(n)", "run(3)")
    r = subprocess.run([sys.executable, "-c", src], capture_output=True, text=True, timeout=900)
    assert r.returncode == 0 and "n=3:" in r.stdout and "h^1(psi) != h^1(psi-bar): 0" in r.stdout, r.stdout[-600:] + r.stderr[-600:]
