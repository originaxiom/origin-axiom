"""B472 — locks: the kappa_q table, the (2,3) closure, the CRT mechanism."""
import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))


def test_kq_verify_all_checks_pass():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "..", "frontier", "B472_quantum_commutator", "kq_verify.py")],
        capture_output=True, text=True, timeout=600)
    assert "ALL CHECKS PASS" in r.stdout


def test_par_faces_are_zeta60_8_and_4():
    sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B465_monodromy_intake"))
    from exact_engine import build, matmul, find_root_of_unity
    for p in (61, 421):
        z, i4, W1, W2, Par = build(p, c=1)
        z60 = find_root_of_unity(p, 60)
        f1 = sum(matmul(Par, matmul(W1, W2, p), p)[i][i] for i in range(15)) % p
        f2 = sum(matmul(Par, matmul(W2, W1, p), p)[i][i] for i in range(15)) % p
        assert f1 == pow(z60, 8, p) and f2 == pow(z60, 4, p)
