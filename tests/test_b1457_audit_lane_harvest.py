"""B1457 -- the audit lane's records from R32 to R80 harvested."""
import json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1457_the_audit_lanes_source_records_harvested")


def test_the_algebra_live():
    r = subprocess.run([sys.executable, "-W", "ignore", os.path.join(A, "verification", "own_checks.py")], capture_output=True, text=True)
    assert r.returncode == 0 and "VERDICT audit-own-checks: PASS" in r.stdout, r.stdout[-500:]
    d = json.load(open(os.path.join(A, "verification", "own_checks.json")))
    assert d["K1 table"] == {"T = diag(1,1,1,1,-4)": [0, 0, 0], "U = diag(3,-1,-1,-1,0)": [12, 8, 4], "-U": [-12, -8, -4], "E00 - E44": [3, 2, 1]}
    assert d["K2"]["q_ab"] == d["K2"]["q_ba"] and d["K2"]["commutator"] == "abAB"
    assert d["K4"]["two_ended"]["m202"][0] == 2 and d["K4"]["one_ended"]["m010"][0] == 1


def test_the_table_and_the_ledger():
    T = json.load(open(os.path.join(A, "verification", "harvest_table.json")))
    assert T["pin"] == "7b088f50" and len(T["rows"]) == 116 and len(T["relays"]) == 9
    disp = {}
    for r in T["rows"]: disp[r["disp"]] = disp.get(r["disp"], 0) + 1
    assert disp == {"REGISTERED": 105, "PARTLY VERIFIED": 7, "AGREES WITH MAIN": 2, "VERIFIED": 2}
    led = open(os.path.join(ROOT, "docs", "HARVEST_LEDGER.md")).read()
    for r in T["rows"]:
        assert "`reports/physical_bridge_2026_09_05/%s.md` @ 7b088f50" % r["name"] in led, r["name"]
    assert re.search(r"\| audit \| `origin/audit/physical-bridge-2026-09-05` \| `[0-9a-f]{8}` \|", led)      # the pin moves at every harvest; B1457's was 7b088f50
    assert len(os.listdir(os.path.join(A, "verification", "readers"))) == 6


def test_no_grade_is_raised_without_a_computation():
    T = json.load(open(os.path.join(A, "verification", "harvest_table.json")))
    for r in T["rows"]:
        if r["disp"] in ("VERIFIED", "PARTLY VERIFIED", "AGREES WITH MAIN"):
            assert r["note"] == "as its report" and r["name"].endswith("_PROOF") or re.search(r"B14\d\d|own_checks", r["note"]), "a raised grade names the computation: " + r["name"]
    v = json.load(open(os.path.join(A, "arc_verdict.json")))
    assert v["verdict"] == "PROVED" and v["scope"]["reach"] == "single" and "NO REPORT DERIVES THE SOURCE" in v["claim_one_line"]
