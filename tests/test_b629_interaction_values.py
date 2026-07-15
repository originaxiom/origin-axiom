"""B629 lock — the interaction-layer value bank.

Recomputes the sealed closed forms independently (sympy exact where
cheap, mpmath at 60 digits where sympy is slow) and locks the sealed
file's hash against the ledger.
"""
import hashlib
import math
import os

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B629 = os.path.join(HERE, "..", "frontier", "B629_interaction_values")
mp.mp.dps = 60


def test_sealed_hash_in_ledger():
    sealed = os.path.join(B629, "SEALED_INTERACTION_VALUES.md")
    h = hashlib.sha256(open(sealed, "rb").read()).hexdigest()
    ledger = open(os.path.join(
        HERE, "..", "frontier", "B598_l85_campaign",
        "ARTIFACT_HASHES.txt")).read()
    assert h in ledger, "sealed interaction values hash missing from ledger"


def _B_mp():
    A = [2 / mp.sqrt(7) * mp.sin(2 * mp.pi * k / 7) for k in (1, 2, 3)]
    z = mp.exp(1j * mp.pi / 7)
    idx = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    pw = [[10, 6, 4], [2, 5, 3], [12, 1, 6]]
    return mp.matrix([[A[idx[i][j] - 1] * z ** pw[i][j] for j in range(3)]
                      for i in range(3)]), A


def test_e62_hearing_matrix_gates():
    B, A = _B_mp()
    tol = mp.mpf(10) ** -55
    # unitarity
    BBd = B * B.transpose_conj()
    assert max(abs(BBd[i, j] - (1 if i == j else 0))
               for i in range(3) for j in range(3)) < tol
    # trace = -1
    assert abs(B[0, 0] + B[1, 1] + B[2, 2] + 1) < tol
    # B^4 = I (order 4)
    B4 = B ** 4
    assert max(abs(B4[i, j] - (1 if i == j else 0))
               for i in range(3) for j in range(3)) < tol
    # |B|^2 row0 = (A1^2, A2^2, A3^2); circulant; row sums 1
    row0 = [abs(B[0, j]) ** 2 for j in range(3)]
    for j in range(3):
        assert abs(row0[j] - A[j] ** 2) < tol
    assert abs(sum(row0) - 1) < tol
    # sealed 50-digit leading value
    assert str(row0[0])[:20] == "0.349291695416089829"


def test_e62_diagonal_is_banked_sine_kernel():
    B, _ = _B_mp()
    z = mp.exp(1j * mp.pi / 7)
    banked = [-(2 / mp.sqrt(7)) * mp.sin(2 * mp.pi / 7) * z ** 3,
              -(2 / mp.sqrt(7)) * mp.sin(6 * mp.pi / 7) * z ** -2,
              -(2 / mp.sqrt(7)) * mp.sin(4 * mp.pi / 7) * z ** -1]
    for j in range(3):
        assert abs(B[j, j] - banked[j]) < mp.mpf(10) ** -55


def test_golden_frame_closed_forms():
    phi = (1 + sp.sqrt(5)) / 2
    s5 = sp.sin(2 * sp.pi / 5) / sp.sqrt(5)
    s1 = sp.sin(sp.pi / 5) / sp.sqrt(5)
    Bo = sp.Matrix([[1 / (2 * phi) + sp.I * s5, -phi / 2 - sp.I * s1],
                    [phi / 2 - sp.I * s1, 1 / (2 * phi) - sp.I * s5]])
    assert sp.simplify(sp.expand(Bo * Bo.H) - sp.eye(2)) == sp.zeros(2, 2)
    assert sp.simplify(sp.trace(Bo) - 1 / phi) == 0
    assert sp.simplify(Bo.det() - 1) == 0
    # charpoly = x^2 - tr x + det with tr, det proven above; eigenvalues are
    # e^{+-2 pi i/5} iff tr = 2 cos(2 pi/5), i.e. 1/phi = 2 cos(2 pi/5)
    assert sp.simplify(1 / phi - 2 * sp.cos(2 * sp.pi / 5)) == 0
    # the frame angle and the structural identity
    assert sp.simplify(sp.cos(sp.atan(1 / phi)) ** 2 - (5 + sp.sqrt(5)) / 10) == 0
    h3sq = sp.Rational(1, 2) - sp.sqrt(5) / 10
    assert sp.simplify((5 - sp.sqrt(5)) / 10 - h3sq) == 0


def test_composite_spot_values():
    h3sq = sp.Rational(1, 2) - sp.sqrt(5) / 10
    assert sp.simplify(sp.Rational(1, 2) * h3sq
                       - (sp.Rational(1, 4) - sp.sqrt(5) / 20)) == 0
    assert sp.Rational(1, 5) * sp.Rational(2, 29) == sp.Rational(2, 145)
    assert (sp.Rational(1, 2) / sp.Rational(2, 29)) == sp.Rational(29, 4)
    assert (sp.Rational(1, 2) / sp.Rational(8, 25)) == sp.Rational(25, 16)


def test_object_scale_running_1loop_closed_form():
    a_mz = (0.0169434946, 0.0338011066, 0.118)
    b = (41 / 10, -19 / 6, -7)
    MZ = 91.1876
    sealed = {3.8597e14: (40.04798168, 44.23778484, 40.86531806),
              3.520e16: (37.1030628, 46.51231568, 45.89322834),
              1e16: (37.92425298, 45.8780631, 44.49119633)}
    for lam, refs in sealed.items():
        t = math.log(lam / MZ)
        for i in range(3):
            inv = 1 / a_mz[i] - b[i] * t / (2 * math.pi)
            assert abs(inv - refs[i]) < 5e-6, (lam, i, inv, refs[i])
