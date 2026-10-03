"""B1462 -- the seats harvested: P is the swap; the levels; the bar's null contract; GENESIS v1.7."""
import importlib.util, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1462_the_seats_harvested_p_is_the_swap_and_the_levels"); V = os.path.join(A, "verification")


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(A, rel)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_p_is_the_swap_live():
    r = subprocess.run([sys.executable, os.path.join(V, "p_is_the_swap.py")], capture_output=True, text=True, cwd=V)
    assert r.returncode == 0 and "VERDICT p-is-the-swap: PASS" in r.stdout, r.stdout[-400:] + r.stderr[-400:]
    d = json.load(open(os.path.join(V, "p_is_the_swap.json")))
    assert d["P_m_is_conj_nM_of_n"] and d["P_n_is_conj_nM_of_m"] and not d["control_P_m_equals_m"] and d["relator_in_PSL_lift"] == "-I"


def test_the_levels_record_and_the_instrument_on_m2():
    d = json.load(open(os.path.join(V, "levels_count_odd.json")))
    assert d["agrees_with_sm_B1522"] and [l["unfixed_off_circle"] for l in d["levels"]] == [0, 0, 0, 0, 20, 96]
    assert [l["invariant_factors"] for l in d["levels"]] == [[], [5], [4, 4], [3, 15], [11, 11], [8, 40]]
    g = d["golden_M5"]; assert g["unfixed"] == g["unfixed_single_sheet"] == g["single_sheet_total"] == 20 and sorted(g["per_sheet"].values()) == [10, 10]
    assert len(d["classes"]) == 8 and sum(1 for c in d["classes"] if c["dualising"]) == 4
    # live, small: the Fox complex at n = 2 and the identity control that caught the arc's one bug
    sys.argv = [sys.argv[0]]; lc = load("verification/levels_count_odd.py", "levels_count_odd")
    cov = lc.Cover(2); assert cov.invariants == [1, 5, 0] or sorted(cov.invariants) == [0, 1, 5]
    I = cov.induced({"a": "a", "b": "b"}, 1); Mid = cov.induced({"a": "BabbaBAA", "b": "aabABBAbab"}, 1)   # equal in the group
    z = cov.free[0]; ti = cov.torsion[0][0]
    assert I[ti][ti] % 5 == 1 and I[ti][z] % 5 == 0 and Mid[ti][ti] % 5 == 1 and Mid[ti][z] % 5 == 0 and Mid[z][z] == 1
    Mt = cov.induced({"a": "baB", "b": "b"}, 1); assert Mt[ti][ti] % 5 == 4 and Mt[z][z] == 1 and Mt[ti][z] % 5 == 0   # the deck: -1 on Z/5, z fixed


def test_the_bar_contract_checks_live_and_the_page():
    r = subprocess.run([sys.executable, os.path.join(V, "bar_contract_checks.py")], capture_output=True, text=True, cwd=V)
    assert r.returncode == 0 and "VERDICT bar-contract-checks: PASS" in r.stdout
    b = open(os.path.join(ROOT, "docs", "THE_BAR.md")).read()
    assert "Amended on main 2026-10-03 (B1462)" in b and "| **PASSED** |" in b and "Bonferroni" in b and "is the SM seat's proposal" in b and "this seat's proposal" not in b


def test_genesis_v1_7_and_the_corrections():
    am = load("adoption/amend.py", "amend_b1462"); t = am.build(); assert len(am.CHANGES) == 4
    cur = open(os.path.join(ROOT, "GENESIS.md")).read()
    if "**Version 1.7 ·" in cur: assert cur == t
    assert "followed by dualising it fixes the module (B1297; **[v1.7]** main's B1459" in cur and "- **v1.7 · 2026-10-03 · main B1462.**" in cur
    assert "followed by dualising reverses the order (B1297), and a vacuum" not in cur
    add = open(os.path.join(ROOT, "frontier", "B1455_the_selection_rule_and_the_deciding_test", "ADDENDUM_2026-10-03_P_is_the_swap.md")).read()
    assert "P is the swap's class" in add
    h = open(os.path.join(ROOT, "docs", "HARVEST_LEDGER.md")).read()
    assert "| sm | `<remote>/standard-model-derivation-0qt6ao` | `48f6af3b` |" in h and all(("| sm:B152%d |" % k) in h for k in range(1, 7))
