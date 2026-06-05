"""B76 (Path F2/F3, V58) -- locking test for the cusp-torsion x quantum-group closure.

Locks: (1) the literal identity 2cos(pi/k)=[2]_q at q=e^{i pi/k} (cusp value = SU(2)_{k-2} value),
k=3..8; (2) the cusp k-set {3..m+2}, k=m(mod2) and its level map level=k-2 (m=1..6); (3) the golden
anchor 2cos(pi/5)=phi at SU(2)_3 (k=5). The categorification barrier (V28) is cited, not re-derived;
the honest split (literal numbers vs no MTC family) lives in FINDINGS, not asserted as a positive."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b76_cqg", _ROOT / "frontier" / "B76_cusp_quantum_group" / "probe.py")
cqg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cqg)


def test_quantum_two_equals_cusp_value():
    """2cos(pi/k) = [2]_q at q=e^{i pi/k} for k=3..8 -- the cusp value IS the SU(2)_{k-2} [2]-value."""
    chk = cqg.check_identity(8)
    assert all(chk.values()), chk


def test_cusp_kset_and_level_map():
    """cusp k-set {3..m+2} with k=m(mod2); SU(2) level = k-2; torsion order = 2k (m=1..6)."""
    assert cqg.cusp_kset(1) == [3]
    assert cqg.cusp_kset(3) == [3, 5]
    assert cqg.cusp_kset(6) == [4, 6, 8]
    for m, ks, levels, ord2k in cqg.level_table(6):
        assert levels == [k - 2 for k in ks]
        assert ord2k == [2 * k for k in ks]
        assert all((k % 2) == (m % 2) for k in ks)


def test_golden_anchor_at_k5_su2_3():
    """The golden/Fibonacci point: 2cos(pi/5)=phi sits at k=5 -> SU(2)_3 (level 3), appearing for odd m>=3."""
    assert sp.simplify(2 * sp.cos(sp.pi / 5) - (1 + sp.sqrt(5)) / 2) == 0
    assert 5 in cqg.cusp_kset(3) and (5 - 2) == 3  # k=5 in m=3 set, level 3
