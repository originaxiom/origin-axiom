"""B650 locks — the type system's battery is reproducible."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
B650 = os.path.join(HERE, "..", "frontier", "B650_typed_functor")


def test_checker_reproduces_battery():
    out = subprocess.run([sys.executable,
                          os.path.join(B650, "types_checker.py")],
                         capture_output=True, text=True).stdout
    assert "B584 antiphase-listener coefficient: ('T_coup(listener)', ('W(RL)', 'core', 'dimless'))" in out
    assert "B613 closure predicate: ('T_spec'" in out
    assert "B632/B637 chord cubic Y: ('T_coup(partner-object)'" in out
    assert "ILL-TYPED" not in out  # post-revision: everything types


def test_frozen_hash_recorded():
    hh = open(os.path.join(B650, "ARTIFACT_HASHES.txt")).read()
    assert "306d6cde" in hh and "FROZEN before the held-out check" in hh
    fnd = open(os.path.join(B650, "FINDINGS.md")).read()
    assert "one disclosed revision cycle used" in fnd.lower()
    assert "K1 does not fire" in fnd


def test_wave2_equivariance_wall():
    import sympy as sp
    phi = (1 + sp.sqrt(5)) / 2
    As = sp.Matrix([[2, 1], [1, 1]])
    At = sp.Matrix([[0, -1], [1, -1 / phi]])
    assert sp.simplify(At.trace() + 1 / phi) == 0
    assert sp.simplify(At.det() - 1) == 0
    assert sp.simplify(At ** 10 - sp.eye(2)) == sp.zeros(2, 2)
    t = sp.symbols("t0:4")
    T = sp.Matrix([[t[0], t[1]], [t[2], t[3]]])
    eqs = sp.expand(T * As - At * T)
    sol = sp.solve([eqs[i, j] for i in range(2) for j in range(2)], t,
                   dict=True)
    assert sol == [] or all(all(v == 0 for v in s.values()) for s in sol)
