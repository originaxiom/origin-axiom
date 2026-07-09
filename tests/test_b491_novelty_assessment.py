"""Locks for B491 (adversarial novelty assessment of R1/R2/R3).

Documentation-integrity lock, not a recompute: the node records a prior-art hunt
(deep-research run), which cannot be re-executed in a test. Asserts the load-bearing
verdicts: R1 and R2 = PARTIALLY-KNOWN / APPEARS-NOVEL / NEEDS-SPECIALIST, R3 = KNOWN /
CLASSICAL (Fox's formula), the net two-novel-cores statement, and the firewall. The
round-2 field CORRECTION carried by R1 is cheap exact algebra and IS recomputed
(sympy): d=3 minpoly z^2-z+2 has disc -7; the d=5 minpoly z^4-3z^3+7z^2-4z+4 is
irreducible of degree 4 (so NOT the quadratic Q(sqrt41)) with 41 a discriminant factor;
and Cantat's quartic mechanism check (factors over Q(sqrt17)).
"""
import pathlib

import sympy as sp

_FIND = (pathlib.Path(__file__).resolve().parents[1]
         / "frontier" / "B491_novelty_assessment" / "FINDINGS.md").read_text(encoding="utf-8")


def test_r1_verdict_appears_novel():
    assert ("## R1 — the held-breath torsion law (= P3 Theorem F7, B479): "
            "PARTIALLY-KNOWN / APPEARS-NOVEL / NEEDS-SPECIALIST") in _FIND


def test_r2_verdict_appears_novel():
    assert ("## R2 — the seam broken-lattice selection rule (= P1, B459): "
            "PARTIALLY-KNOWN / APPEARS-NOVEL / NEEDS-SPECIALIST") in _FIND
    # the decisive gap: known Galois equivariance is a signed permutation, cannot vanish
    assert "signed permutation" in _FIND
    assert "can never send a nonzero value to" in _FIND


def test_r3_verdict_known_classical():
    assert "## R3 — the cover-tower torsion |L(2n)−2| (= B489): KNOWN / CLASSICAL" in _FIND
    assert "Fox's formula" in _FIND


def test_net_and_firewall():
    assert "two genuinely novel-looking mathematical cores" in _FIND
    assert "nothing to CLAIMS.md" in _FIND
    assert "not because they are the SM (they are not, B490)" in _FIND


def test_r1_corrected_fields_exact():
    # the round-2 correction, recomputed exactly
    assert "d=3 gives ℚ(√−7) (minpoly z²−z+2)" in _FIND
    assert "z⁴−3z³+7z²−4z+4, disc 5²·41" in _FIND and "NOT ℚ(√41)" in _FIND
    z = sp.symbols('z')
    assert sp.discriminant(z**2 - z + 2, z) == -7                   # Q(sqrt-7)
    q5 = sp.Poly(z**4 - 3 * z**3 + 7 * z**2 - 4 * z + 4, z)
    assert q5.is_irreducible                                        # degree-4 field, not Q(sqrt41)
    disc = sp.discriminant(q5.as_expr(), z)
    assert disc == 16400 and sp.factorint(disc) == {2: 4, 5: 2, 41: 1}   # odd part 5^2 * 41


def test_cantat_mechanism_quartic_exact():
    # closest prior art: Cantat's fixed-point quartic x^4-3x^3+x^2+4x-2 splits over Q(sqrt17)
    assert "x⁴−3x³+x²+4x−2=0" in _FIND and "ℚ(√17)" in _FIND
    z = sp.symbols('z')
    qc = z**4 - 3 * z**3 + z**2 + 4 * z - 2
    assert sp.Poly(qc, z).is_irreducible                            # not already rational
    factors = sp.factor_list(qc, extension=sp.sqrt(17))[1]
    assert sorted(sp.Poly(f, z).degree() for f, _ in factors) == [2, 2]
