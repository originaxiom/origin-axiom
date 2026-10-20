"""B1678 -- the lifted register, verified on main (the audit lane's word-architecture audit; P-207's sign audit). Live: the
record's pointwise lift M_of is not a group section -- on seeded pairs of positive words the composite's lift equals the
product of the factors' lifts or its negative, and the negative occurs (the bite: a section would give none); B1630's
S~ = R L^-1 R has eigen-turns (3/8, 7/8, 7/8) under the multiplicative lift and its negative under M_of. Stored: the
composition law (Delta^4 lifts to eps J_c; the commutator J_c) and the joint image 192."""
import contextlib, importlib.util, io, pathlib, random
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1678_the_lifted_register_verified"


def _om():
    spec = importlib.util.spec_from_file_location("om", ROOT / "frontier" / "B1617_the_weave_at_tau_omega" / "verification" / "weave_at_omega.py")
    om = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(om)
    return om


def test_the_pointwise_lift_is_not_a_section():
    om = _om(); L, R = {"a": "a", "b": "ab"}, {"a": "ab", "b": "b"}
    def auto(w):
        a = {"a": "a", "b": "b"}
        for ch in w: a = om.compose(a, L if ch == "L" else R)
        return a
    rng = random.Random(1678); plus = minus = other = 0
    for _ in range(80):
        f = "".join(rng.choice("LR") for _ in range(rng.randint(1, 5))); g = "".join(rng.choice("LR") for _ in range(rng.randint(1, 5)))
        Mf, Mg, Mfg = om.M_of(auto(f)), om.M_of(auto(g)), om.M_of(auto(f + g))
        cands = [Mf @ Mg, Mg @ Mf]                                               # the action's order is a convention
        if any(np.allclose(Mfg, P, atol=1e-8) for P in cands): plus += 1
        elif any(np.allclose(Mfg, -P, atol=1e-8) for P in cands): minus += 1
        else: other += 1
    assert other == 0 and minus > 0 and plus > 0                                  # off by exactly -1 sometimes: not a section


def test_b1630_eigen_turns_under_the_multiplicative_lift():
    om = _om(); T_of = lambda a: om.cp.restrict(om.M_of(a), om.cp.TB)
    L, R, l = {"a": "a", "b": "ab"}, {"a": "ab", "b": "b"}, {"a": "a", "b": "Ab"}
    direct = T_of(om.compose(om.compose(R, l), R)); mult = T_of(R) @ np.linalg.inv(T_of(L)) @ T_of(R)
    turns = lambda M: sorted(round(float((np.angle(e) / (2 * np.pi)) % 1), 4) for e in np.linalg.eigvals(M))
    assert turns(mult) == [0.375, 0.875, 0.875] and turns(direct) == [0.375, 0.375, 0.875]
    assert np.allclose(direct, -mult, atol=1e-9)


def test_stored_composition_law_and_joint_image():
    mc = A / "verification" / "main_check"
    s1 = (mc / "s1_log.txt").read_text(); s2 = (mc / "s2_log.txt").read_text()
    assert "Delta^4 == I_c: True" in s1 and "-> equals J_c (g=-1)" in s1 and "J^2==id: True" in s1
    assert "four wordings : |V image|= 96  |W image|= 48  |joint V+W|= 192" in s2
