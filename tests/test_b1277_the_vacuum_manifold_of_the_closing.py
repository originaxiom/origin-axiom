"""B1277 — the vacuum manifold of the object's closing and its Wilson lines: the SM's commutant su(2)_beta + u(1)^2,
the sixteen characters of H_1(Y_3) = Z_4^2 (h^1 = 1 exactly for the three sign characters), the Standard-Model
point W = z_L o chi_j at the cost of one generation's doublets, the no-three-generation theorem, the object's abelian
local systems (zero modes only at t = phi^(+-2)); the full tree-level manifold slow-marked."""
import sys
from pathlib import Path
from fractions import Fraction as F
import pytest

ROOT = Path(__file__).resolve().parents[1]
for arc in ("B1267_spectrum_law_rebuilt", "B1269_transport_computed", "B1273_the_three_fold_closing",
            "B1275_the_cubic_made_explicit", "B1276_the_relations_the_chain_forces",
            "B1277_the_vacuum_manifold_of_the_closing"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))


@pytest.fixture(scope="module")
def V():
    import vacuum_manifold as V
    return V


@pytest.fixture(scope="module")
def data(V):
    wts, rep = V.C.load()
    lab, hy, wts2 = V.R.sm_labels()
    assert wts2 == wts
    sub, Y, rts, Mf, ip, a1, a2 = V.descent_data()
    neutral = V.neutral_components(wts, hy, ip, a1, a2)
    names = {i: {'S': 'N', 'nu^c': 'nu^c', 'H_u': 'h_u0', 'H_d': 'h_d0', 'L': 'nu'}[lab[i]] for i in neutral}
    return dict(wts=wts, lab=lab, hy=hy, ip=ip, a1=a1, a2=a2, rts=rts, neutral=neutral, names=names)


def test_the_five_neutral_components(data):
    assert sorted(data['names'].values()) == ['N', 'h_d0', 'h_u0', 'nu', 'nu^c']
    t3y = {data['names'][i]: v for i, v in data['neutral'].items()}
    assert t3y['N'] == (0, 0) and t3y['nu^c'] == (0, 0)
    assert t3y['h_u0'] == (F(-1, 2), F(1, 2)) and t3y['h_d0'] == (F(1, 2), F(-1, 2)) and t3y['nu'] == (F(1, 2), F(-1, 2))


def test_the_wilson_lines_and_the_theorem(V, data, capsys):
    inv = {v: k for k, v in data['names'].items()}
    d = V.part_d(data['wts'], data['lab'], data['hy'], data['ip'], data['a1'], data['a2'], data['rts'], {'neutral_idx': inv})
    out = capsys.readouterr().out
    assert d['even'] == 32 and d['joint_ok'] and d['crank'] == 4          # z_L: A1A5; joint stabilizer with <N>,<nu^c> = the SM
    assert d['orth'] == 2 and d['connects'] and d['joint_b'] == 20        # su(2)_beta; every SU(5) root connects two weights of the 10
    assert d['lost'] == {1: 12, 2: 0, 3: 0} and d['adj'] == 40            # W = z_L o chi_1 costs generation 1's doublets
    assert d['lost_b'] == {1: 12, 2: 0, 3: 0}                              # W = (-1_beta) o chi_1 keeps SU(5)
    assert "characters of order 2: 3; (h^1, h^0) values: {(1, 0): 3}" in out
    assert "characters of order 4: 12; (h^1, h^0) values: {(0, 0): 12}" in out
    assert "equals (-1)^(6Y) on every component: True" in out
    assert "the roots are exactly the SM's (colour A2 + weak A1): True" in out
    assert "all of them exp(2 pi i k beta^v/4) in SU(2)_beta's torus: True" in out


def test_the_objects_abelian_local_systems_zero_modes_only_at_the_golden_values(V, capsys):
    assert V.part_e()
    out = capsys.readouterr().out
    assert "(t - phi^2)(t - phi^-2) = t**2 - 3*t + 1" in out and "|t| = 1 for none of them: True" in out


@pytest.mark.slow
def test_the_full_tree_level_manifold(V, capsys):
    assert V.main()
    out = capsys.readouterr().out
    assert "maximal F-flat paired branches: 9" in out
    assert "branches containing BOTH a rank-reducing VEV (N or nu^c) and an electroweak VEV (h_u0, h_d0, nu): 9 of 9" in out
    assert "a maximal branch with e6-part su(3)+su(2)+u(1): False" in out
    assert "<N> -> so(10)+u(1), rank 7; <N>,<nu^c> -> su(5), rank 6; all five -> su(4), rank 4" in out
    assert "NOT conjugate-paired: 0" in out
