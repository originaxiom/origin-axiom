"""B1466 -- the count is the order, and the count is a bit."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1466_the_two_orders_and_the_register_bit"); V = os.path.join(A, "verification")


def test_the_two_orders_and_the_cup_product_record():
    d = json.load(open(os.path.join(V, "two_orders.json")))
    by = {r["label"]: r for r in d}
    for lab in ("q0 = 17 + 12 sqrt2, mu = -1", "q0' = 17 - 12 sqrt2, mu = -1"):
        r = by[lab]
        assert r["I W (1 on top of A)"]["I"] == -1 and r["I W' (A on top of 1)"]["I"] == 1 and r["I_split"] == 0
        assert r["C2 W* ~ iota*W'"]["found"] and not r["C2 control W* ~ W' (no iota)"]["found"]
        assert float(r["C3 ob(c1)"]["ob_norm"]) == 0 and float(r["C3 ob(c2)"]["ob_norm"]) == 0
        assert float(r["C3 ob(c1 + c2)"]["ob_norm"]) > 1 and float(r["C3 ob(c1 + c2)"]["residual_mod_im_d1"]) < 1e-40     # the class is zero: unobstructed
        assert r["C3 ob(c1 + c2)"]["dim_H2"] == 5
    c = by["7 + 4 sqrt3, mu = i (control: counts 0)"]; assert c["I W (1 on top of A)"]["I"] == 0 and c["I W' (A on top of 1)"]["I"] == 0
    q2 = by["q = 2, mu = -1 (control: h1 = 0)"]; assert q2["h1_up(Ext(1,A))"] == 0 and q2["h1_down(Ext(A,1))"] == 0


def test_the_fused_module_is_irreducible_and_counts_zero():
    d = json.load(open(os.path.join(V, "c3b_mixed_module.json")))
    assert len(d) == 4
    for r in d:
        assert float(r["relator_residual"]) < 1e-40 and r["commutant_dim"] == 1 and r["commutant_dim_W_Wprime_S"] == [1, 1, 2]
        assert r["invariant_line_(sub 1)"] == 0 and r["dual_invariant_line_(quotient 1)"] == 0 and r["same_for_W_Wprime_S"] == [[0, 1], [1, 0], [1, 1]]
        assert r["I_mixed"]["I"] == 0 and r["I_mixed"]["h1"] == 0 and r["I_mixed"]["h1_dual"] == 0


def test_the_seal_and_the_script_are_what_was_pushed():
    import hashlib
    pre = open(os.path.join(A, "PREREGISTRATION.md"), "rb").read(); assert hashlib.sha256(pre).hexdigest().startswith("dbda2860")
    assert "P4" in pre.decode() and "60%" in pre.decode()
