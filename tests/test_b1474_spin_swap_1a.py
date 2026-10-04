"""B1474 -- the spin swap, phase 1a: the table re-derived from the stored searches; the controls live."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route", "verification")


def test_table_from_stored_searches():
    r = subprocess.run([sys.executable, os.path.join(V, "close_k.py")], capture_output=True, text=True, cwd=V); assert r.returncode == 0, r.stderr[-400:]
    t = json.load(open(os.path.join(V, "table.json"))); s = t["summary"]
    assert set(s["genuine_swap"]) == {"m003", "m207", "s955", "s957", "s960", "t12838", "o10_150695"}
    assert set(s["fix"]) == {"m004", "m206", "s961", "t12839", "o10_150707", "o10_150696"}
    assert s["undetermined"] == [] and s["all_decided_agree"] and s["etas_all_in_cosets"]
    assert s["chiral_none"] == s["chiral_total"] == 41
    assert t["table"]["s957"]["K_order"] == 2 and t["table"]["s960"]["K_order"] == 4 and t["table"]["m003"]["K_order"] == 1


def test_controls_live():
    sys.path.insert(0, V); sys.path.insert(0, os.path.join(ROOT, "frontier", "B1471_the_cancellation_is_a_theorem_of_amphichirality", "verification"))
    import spin_swap as SS
    r3 = SS.classify("m003", Ls=(5,)); assert r3["verdict"] == "SWAP" and r3["etas"] == [{"a": -1, "b": 1}]
