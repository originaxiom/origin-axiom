"""B121 -- locking test: the monodromy sl(2) grading of the adjoint is an EXTERNAL det=-1 GL(2,Z)-rep, not the
principal one. The tower (monodromy rep) has ODD SL(2) highest weights for all n>=3 (Kostant principal is even-only)
-> INEQUIVALENT, agreeing only at n=2; the obstruction IS det(M_m)=-1 (det Sym^d(M_m)=(-1)^{d(d+1)/2}, a sign in
every block; the principal det=+1 partner gives all +1). NOT a dimension coincidence. NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b121", _ROOT / "frontier" / "B121_monodromy_grading" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_tower_vs_kostant_weights():
    assert B.tower_highest_weights(2) == B.kostant_highest_weights(2) == [2]      # agree at n=2
    assert B.tower_highest_weights(3) == [0, 2, 3]                                # odd weight 3 present
    assert B.kostant_highest_weights(3) == [2, 4]                                 # Kostant is even-only


def test_monodromy_inequivalent_for_n_ge_3():
    mv = B.monodromy_vs_principal(8)
    assert mv["agree_only_at_n2"] is True            # the two SL(2)-reps agree iff n=2
    assert mv["odd_weights_for_all_n_ge_3"] is True   # the tower has odd highest weights for all n>=3
    assert mv["dims_all_match"] is True               # both have dim n^2-1 (not a coincidence -- they still differ)


def test_obstruction_is_det_minus_one():
    dm = B.odd_weight_is_det_minus_one(6)
    assert dm["det_minus_one_leaves_sign"] is True    # det Sym^d(M_m) = (-1)^{d(d+1)/2}, a sign in every block


def test_relation_not_dimension_coincidence():
    rs = B.relation_summary()
    assert rs["not_a_dimension_coincidence"] is True   # same dim but inequivalent (the kill condition is NOT met)
    assert rs["obstruction_is_det_minus_one"] is True
