"""B1476 -- the spin swap, phase 1c: the stored results re-read (the 1/4 law in the family; the 1/24 lattice; the census
outside; the Pin signs), and the dilogarithm atom live."""
import json, os, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1476_the_spin_swap_phase_1c_the_quarter_law_the_pin_bit_and_what_a5_chose", "verification")
SWAP = {"m003", "m207", "s955", "s957", "s960", "t12838", "o10_150695"}; FIX = {"m004", "m206", "s961", "t12839", "o10_150696", "o10_150707"}


def test_quarter_law_in_the_family_and_the_lattice():
    P = json.load(open(os.path.join(V, "phase_1c.json")))
    assert P["C2_holds"]
    for nm in SWAP: assert P["C2"][nm]["cls"] == "quarter", nm
    for nm in FIX: assert P["C2"][nm]["cls"] == "zero", nm
    s = P["C2b"]["summary"]; assert s["family_on_lattice"] == s["family_total"] == 112 and s["outside_on_lattice"] == 0
    assert P["C2b"]["atom"]["Re_ok"] and P["C2b"]["atom"]["Im_ok"]
    assert P["C3"]["m003"] == [] and P["C3"]["m004"] == ["m000"]
    assert len(P["C1"]["m206"]["mirror_invariant_any_tau"]) == 2 and len(P["C1"]["o10_150707"]["mirror_invariant_any_tau"]) == 4


def test_the_certificate_needs_no_enumeration():
    """R92's answer: an invariant spin structure would have real odd torsion; no 1/4 member has a spin structure that
    does, every rank-one zero member read has at least two -- and the test can fail (m136's geometric lift is not real
    while four of its eight are; a real number passes, a generic complex one does not)."""
    fam = json.load(open(os.path.join(V, "r92_certificate_family.json"))); out = json.load(open(os.path.join(V, "r92_certificate.json")))
    assert set(fam) == SWAP | FIX
    for nm in SWAP: assert fam[nm]["torsion_real"] == 0 and fam[nm]["n_spin"] >= 2, nm
    for nm in FIX: assert fam[nm]["torsion_real"] >= 2 and fam[nm]["s0_real"], nm
    rk1 = {k: v for k, v in out.items() if "error" not in v}; assert len(rk1) == 12 and len(out) == 15
    q = [v for v in rk1.values() if v["cs"] == "quarter"]; z = [v for v in rk1.values() if v["cs"] == "zero"]
    assert len(q) == 6 and all(v["torsion_real"] == 0 for v in q)
    assert len(z) == 6 and all(v["torsion_real"] >= 2 for v in z)
    assert out["m136"]["torsion_real"] == 4 and out["m136"]["n_spin"] == 8 and out["m136"]["s0_real"] is False
    src = open(os.path.join(V, "r92_certificate_family.py")).read().split("out = {}")[0]; ns = {"__file__": os.path.join(V, "r92_certificate_family.py")}
    exec(compile(src, "r92fam", "exec"), ns)
    assert ns["is_real"]("(8.25 - 8.4e-51j)") and ns["is_real"]("(1e-40 + 3.5j)") and not ns["is_real"]("(1.25 + 1.73205080756888j)")


def test_the_law_outside_the_family_is_one_way():
    cu = json.load(open(os.path.join(V, "census_swap_cusped.json"))); cl = json.load(open(os.path.join(V, "census_swap_closed.json")))
    q = [v for v in cu.values() if v["cs_class"] == "quarter"]; assert len(q) == 6 and all(v["verdict"] == "GENUINE SWAP" for v in q)
    z = collections.Counter(v["verdict"].split(" (")[0] for v in cu.values() if v["cs_class"] == "zero"); assert z["FIX"] == 4 and z["GENUINE SWAP"] == 3
    c = collections.Counter(v["verdict"].split(" (")[0] for v in cl.values()); assert c["GENUINE SWAP"] == 14 and c["FIX"] == 11 and len(cl) == 37


def test_pin_signs_on_m004():
    d = json.load(open(os.path.join(V, "pin_sign_fixed.json")))
    rows = [r for r in d["m004"] if r.get("w")]; assert len(rows) >= 3
    for r in rows:
        assert r["eps_geometric"] == 1 and r["tau2_is_conj_by_w"] and set(r["pin"].values()) == {"Pin+", "Pin-"}


def test_atom_live():
    from mpmath import mp, polylog, pi, log, exp, mpc, re, im, mpf
    mp.dps = 30; z = exp(mpc(0, 1) * pi / 3); R = polylog(2, z) + log(z) * log(1 - z) / 2
    assert abs(re(R) - pi ** 2 / 12) < mpf(10) ** -25 and abs(im(R) - mpf("1.0149416064096536250212025542")) < mpf(10) ** -20
