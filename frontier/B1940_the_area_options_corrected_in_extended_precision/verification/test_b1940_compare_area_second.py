"""The area comparison's decision, fixed before any seat's output: a copy of main's values agrees; a value 3 % off with
small errors does not; the tolerance is the rule's."""
import importlib.util, pathlib
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cas", HERE / "compare_area_second.py"); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)


def test_the_decision_can_pass_and_can_fail():
    for o, (v, e) in C.main_area_options().items():
        assert C.compare(v, e, v, e)["agrees"] is True, o
        off = list(v); off[6] *= 1.03
        assert C.compare(v, e, off, e)["agrees"] is False, o           # 3 % is beyond 3 sqrt(...) at these errors
    assert C.DELTA == 5.4e-3
