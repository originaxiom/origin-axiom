"""B117 -- locking test: the tower is the Sym two-sequence; the "promotion" is a Sym^1 absence.
The dimension identity (n+1)(n+2)/2-(n^2-1) = -(n-4)(n+1)/2 (roots {-1,4}) DERIVES the shape of B103's
two-sequence mu_d; Sym^0..4 product = the B80 proved n=4 tower; mu_n=1 for all n>=2 (Sym^n always present)
=> char(M^n) is always a tower factor = degree=rank at the char-poly level (status: dim-forced only at n=3).
NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b117", _ROOT / "frontier" / "B117_interleaving" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_dimension_identity():
    di = B.dimension_identity()
    assert di["roots"] == [-1, 4]                    # zero iff n=4
    assert di["unique_perfect_fit"] is True
    assert di["surplus_per_n"][3] == 2 and di["surplus_per_n"][4] == 0  # n=3 omits one module; n=4 perfect


def test_sym_selection_equals_two_sequence():
    ss = B.sym_selection_equals_two_sequence(8)
    assert ss["all_total_dims_match"] is True        # every n: sum (d+1)*mu_d = n^2-1
    assert ss["sym_n_always_present"] is True        # mu_n = 1 for all n
    assert ss["per_n"][5]["doubled"] == [2]          # n=5 doubles Sym^2
    assert ss["per_n"][6]["doubled"] == [2, 3]       # n=6 doubles Sym^2, Sym^3 (the [2<=d<=n-3] overlap)


def test_n3_uniqueness_sym1_absent():
    u = B.n3_uniqueness()
    assert u["unique"] is True
    assert u["solutions"] == [[0, 2, 3]]             # the unique subset summing to 8
    assert u["sym1_absent"] is True                  # the "promotion" is a Sym^1 absence


def test_sym_product_equals_b80_tower():
    sp4 = B.sym_product_equals_b80_tower()
    assert sp4["sym_degree"] == 15 and sp4["dim_sl4"] == 15
    assert sp4["roots_match_b80_tower"] is True      # Sym^0..4 product = the B80 proved n=4 tower


def test_sym_n_presence_status():
    sn = B.sym_n_presence_status()
    assert sn["char_Mn_always_a_factor"] is True
    # honor the DO-NOT: Sym^n presence is dim-FORCED only at n=3; rep-theory at n=2,4
    assert "unique subset" in sn["per_n"][3]["basis"]
    assert "NOT dim-necessity" in sn["per_n"][4]["basis"]


def test_n6_path4_crosscheck():
    c = B.n6_path4_crosscheck()
    assert c["k3_total_prediction"] == 3             # a_3+b_3 = 2+1 = 3 (= max(n-d,1))
    assert c["b66_measured_k3"] == 2                 # B66 gauge under-count (B58 Phase A) -- consistency, not decisive
