"""B141 -- split S031. Items 1-3 sympy-exact (unconditional, rigorous); Item 4 a small seeded numeric sample."""
from frontier.B141_s031_split.probe import (
    finiteness_vs_density,
    phi2_tower_irreducible,
    phi_fixed_search_sl3,
    phi_fixed_tower_reducible,
    q8_group_order,
    q8_relations,
    q8_sym2_character,
)


def test_phi_fixed_rep_is_q8():
    """The phi-fixed (0,0,0) rep satisfies the quaternion relations and generates a group of order 8 (Item 1)."""
    r = q8_relations()
    assert r["A2_eq_-I"] and r["B2_eq_-I"] and r["AB_eq_-BA"]
    assert r["detA"] == 1 and r["detB"] == 1
    assert q8_group_order() == 8


def test_phi_fixed_tower_reducible_for_n_ge_3():
    """Sym^{n-1} of the Q8 rep is reducible for all n>=3, irreducible only at n=2 (Item 1, RIGOROUS)."""
    t = phi_fixed_tower_reducible()
    assert t["irreducible_only_at_n2"] is True
    assert t["reducible_for_all_n_ge_3"] is True
    assert t["rows"][3]["alg_dim"] == 3 and t["rows"][4]["alg_dim"] == 4


def test_q8_sym2_character():
    """chi_{Sym^2 V} = (3,3,-1,-1,-1) = chi_a + chi_b + chi_c (Q8 character cross-check)."""
    assert q8_sym2_character()["is_3_3_-1_-1_-1"] is True


def test_phi2_geometric_tower_irreducible_in_q3():
    """Sym^{n-1} of the fig-8 holonomy is irreducible (alg_dim n^2) all n, traces in Q(sqrt-3) (Item 2, RIGOROUS)."""
    t = phi2_tower_irreducible()
    assert t["irreducible_all_n"] is True
    assert t["all_traces_in_Q3"] is True


def test_finiteness_vs_density():
    """Q8 image finite (order 8); fig-8 image infinite (Item 3)."""
    f = finiteness_vs_density()
    assert f["q8_image_order"] == 8
    assert f["fig8_A_order_infinite"] is True


def test_phi_fixed_sl3_sample_all_reducible():
    """A small seeded sample of SL(3) phi-fixed intertwiner solutions are all reducible (Item 4, conjecture sample)."""
    s = phi_fixed_search_sl3(starts=15, seed=20260609)
    assert s["converged"] > 0
    assert s["irreducible_found"] == 0
