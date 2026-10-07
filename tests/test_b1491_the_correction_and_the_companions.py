"""B1491 -- the correction to B1487's T3 is on the record; GENESIS at v1.17; the two companion facts stored."""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1491_the_correction_and_the_companions"


def test_the_correction_is_on_the_record_and_genesis_is_at_v1_17():
    root = HERE.parents[1]
    assert (root / "frontier" / "B1487_the_ends" / "ADDENDUM_2026-10-07_T3_is_one_sided_the_SM_seats_correction.md").exists()
    assert "two-sided form |I(W₁)| ≤ m_A + b0 first written here was withdrawn" in (root / "docs" / "THEOREM_REGISTRY.md").read_text()
    g = (root / "GENESIS.md").read_text(); assert "- **v1.17 · 2026-10-07 · main B1491.**" in g and "fixed-point companions" in g and "L8a15" in g
    r = subprocess.run([sys.executable, str(HERE / "adoption" / "amend.py"), "--check"], capture_output=True, text=True); assert r.returncode == 0, r.stdout + r.stderr


def test_the_two_companion_facts():
    d = json.load(open(HERE / "verification" / "companions_check.json"))
    assert d["ok"] and d["o10_150729_is_L10n113"] and d["L10n113_cusps"] == 5
    c = d["LLLR_companion"]; assert c["cusps"] == 3 and c["H1"] == "Z + Z + Z" and abs(c["volume_ratio"] - 3) < 1e-9 and c["symmetry_order"] == 12 and not c["amphicheiral"]
    assert any("L8a15" in x for x in c["identify"])
    for name, ends in (("b++LR", 1), ("b+-LR", 5), ("b++LLRR", 4), ("b+-LLRR", 8), ("b++LLLR", 3)):
        assert d["states"][name]["ends"] == ends
