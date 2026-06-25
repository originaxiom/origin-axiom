"""B205 -- the quantum (skein) trace map for the metallic family (V201). pyenv + sympy.

Generic-q skein algebra of the once-punctured torus; the quantum Dehn twists are verified
automorphisms; classical limit = the Kohmoto trace map. Machinery known (skein/DAHA/MGO);
nothing to CLAIMS.md.
"""
import os
import sys
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B205_metallic_quantum_trace_map"))
from quantum_trace_map import (  # noqa: E402
    q, X, Y, Z, gx, gy, gz, Omega, R_img, L_img, comm, is_zero,
    is_automorphism, classical, apply_hom, add, scal)


def test_central_element():
    assert all(is_zero(comm(Omega, g)) for g in (gx, gy, gz))


def test_central_classical_limit_is_fricke():
    x, y, z = sp.symbols('x y z')
    assert sp.expand(classical(Omega) - (x**2 + y**2 + z**2 - 2 * x * y * z)) == 0


def test_quantum_dehn_twists_are_automorphisms():
    assert is_automorphism(R_img)
    assert is_automorphism(L_img)


def test_automorphism_check_has_teeth():
    # re-audit (2026-06-25): the earlier is_automorphism relation-clause was VACUOUS (it applied the
    # map to an already-zero reduced relation). Lock that the corrected check REJECTS non-automorphisms
    # -- each of these fixes neither the relations nor (in general) Omega, so it must return False.
    assert not is_automorphism({X: scal(2, gx), Y: gy, Z: gz})        # X -> 2X (scaling)
    assert not is_automorphism({X: gx, Y: gz, Z: gy})                 # naive Y <-> Z swap
    assert not is_automorphism({X: add(gx, gy), Y: gy, Z: gz})        # X -> X + Y (junk)


def test_classical_limit_is_kohmoto_map():
    x, y, z = sp.symbols('x y z')
    assert sp.expand(classical(R_img[Z]) - (2 * x * z - y)) == 0
    assert sp.expand(classical(L_img[Z]) - (2 * y * z - x)) == 0
    assert classical(R_img[X]) == x and classical(R_img[Y]) == z


def test_q_chebyshev_leading_coeff():
    # R_q^m(Z) leading coeff (X^m Z) = (1+q^-2)^m
    img = {X: gx, Y: gy, Z: gz}
    for m in (1, 2, 3):
        img = {g: apply_hom(R_img, img[g]) for g in (X, Y, Z)}
        lead = img[Z][(X,) * m + (Z,)]
        assert sp.simplify(lead - (1 + q**-2)**m) == 0, m


if __name__ == "__main__":
    test_central_element()
    test_central_classical_limit_is_fricke()
    test_quantum_dehn_twists_are_automorphisms()
    test_classical_limit_is_kohmoto_map()
    test_q_chebyshev_leading_coeff()
    print("ALL CHECKS PASS")
