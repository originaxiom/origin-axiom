#!/usr/bin/env python3
"""Exact C-2 retrieval: character and base field of the B_0 block.

The input is the already certified stable-branch character ledger

    B = 3 Reg(C12) + chi_0 + chi_11.

This certificate distinguishes four copies of the trivial character over a
splitting field from a rational cyclotomic module on which the generator acts
by multiplication by a primitive twelfth root.  Those representations have
different exact character decompositions and characteristic polynomials.
"""

from __future__ import annotations

from pathlib import Path


N = 12
UNITS = tuple(a for a in range(N) if a in (1, 5, 7, 11))


def character(*labels: int) -> tuple[int, ...]:
    values = [0] * N
    for label in labels:
        values[label % N] += 1
    return tuple(values)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    r017 = root / "certificates/r017_yukawa_primary/verify_yukawa_cup_product_308_scope.py"
    source = r017.read_text(encoding="utf-8")
    assert "B = add([3 * multiplicity for multiplicity in reg], character(0, 11))" in source
    assert "C12 acts as the identity on B_0" in source

    regular = (1,) * N
    base = tuple(3 * value for value in regular)
    actual = add(base, character(0, 11))
    assert actual == (4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4)

    # B_0 means the chi_0-isotypic space over a splitting field K containing
    # zeta_12.  Its generator exponent is therefore exactly zero.
    b0_dimension_over_k = actual[0]
    b0_generator_exponents = (0,) * b0_dimension_over_k
    assert b0_dimension_over_k == 4
    assert b0_generator_exponents == (0, 0, 0, 0)

    # A rank-one Q(zeta_12) module viewed over Q, with the C12 generator acting
    # by multiplication by any primitive root zeta_12^a, splits over K into
    # the full Galois orbit {chi_1,chi_5,chi_7,chi_11}.  It is never 4 chi_0.
    primitive_orbits = {
        a: tuple(sorted((a * unit) % N for unit in UNITS)) for a in UNITS
    }
    assert all(orbit == UNITS for orbit in primitive_orbits.values())
    scalar_rank_one = character(*UNITS)
    four_trivial = character(0, 0, 0, 0)
    assert scalar_rank_one != four_trivial
    assert scalar_rank_one == (0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1)
    assert four_trivial == (4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # Equivalent Q-linear characteristic-polynomial control:
    # identity on a four-dimensional Q-space gives (t-1)^4, whereas primitive
    # cyclotomic multiplication gives Phi_12(t)=t^4-t^2+1.
    identity_charpoly = (1, -4, 6, -4, 1)      # ascending coefficients
    cyclotomic_charpoly = (1, 0, -1, 0, 1)    # Phi_12, ascending
    assert identity_charpoly != cyclotomic_charpoly

    # Over K=Q(zeta_12), a splitting field, the chi_0 block is K^4.
    # Restricting that particular K-realization to Q would have Q-dimension
    # 16 and does not turn identity into cyclotomic action.  The isolated
    # trivial block also admits a separate Q^4 form; R017 does not select a
    # unique arithmetic descent field.  Either realization base-changes to
    # the same four-dimensional identity block over C.
    degree_k_over_q = 4
    b0_dimension_over_q_after_restriction = degree_k_over_q * b0_dimension_over_k
    assert b0_dimension_over_q_after_restriction == 16
    b0_identity_q_form_dimension = 4
    assert b0_identity_q_form_dimension == b0_dimension_over_k

    # A rational representation must have Galois-invariant split
    # multiplicities.  The full 38-dimensional ledger is not invariant
    # (m_11=4 but m_1=m_5=m_7=3), so the whole displayed split representation
    # does not descend to Q with those multiplicities.  This does not prevent
    # the isolated trivial block from admitting its evident Q^4 form.
    assert tuple(actual[a] for a in UNITS) == (3, 3, 3, 4)

    print("INPUT B = 3 Reg_C12 + chi_0 + chi_11")
    print("RESULT B_0 generator exponents =", b0_generator_exponents)
    print("RESULT marked C12 generator acts on B_0 by I_4 = zeta_12^0 I_4")
    print("RESULT after base change to K=Q(zeta_12): B_0 = K^4 and P(B_0) = P^3_K")
    print("RESULT after an archimedean embedding: P^3_C (complex dimension 3)")
    print("CONTROL primitive scalar rank-one orbit =", UNITS, "!= four copies of chi_0")
    print("CONTROL Q-linear charpolys: (t-1)^4 != Phi_12(t)=t^4-t^2+1")
    print("CONTROL Res_K/Q(K^4) has Q-dimension", b0_dimension_over_q_after_restriction,
          "; the isolated identity block also admits Q^4")
    print("ANSWER primitive root on B_0: none; K-rank: 4, not 1")
    print("R031A B_0 character/base-field retrieval: PASS")


if __name__ == "__main__":
    main()
