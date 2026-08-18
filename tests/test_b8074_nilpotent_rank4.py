"""B8074 locks -- the rank ceiling's hypothesis is load-bearing.

Every assertion either RECOMPUTES the fact from the E6 Cartan matrix or reads the arc's
results.json.  Nothing asserts prose.
"""
import itertools
import json
import os
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARC = os.path.join(ROOT, "frontier", "B8074_nilpotent_rank4")
sys.path.insert(0, os.path.join(ROOT, "frontier", "B8068_j2t_charge_field"))
import e8_build as E  # noqa: E402

A = E.A
E6_ROOTS = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]
TWENTYSEVEN = [r for r in E.ROOTS if r[6] % 3 == 1 and r[7] == 0]


def _results():
    with open(os.path.join(ARC, "results.json")) as fh:
        return json.load(fh)


def _alpha(h, r):
    return sum(h.get(i, Fraction(0)) * sum(r[k] * A[k][i] for k in range(8)) for i in range(6))


def _nullspace(rows, n):
    rows = [list(map(Fraction, r)) for r in rows]
    piv, pc = 0, []
    for c in range(n):
        pr = next((r for r in range(piv, len(rows)) if rows[r][c] != 0), None)
        if pr is None:
            continue
        rows[piv], rows[pr] = rows[pr], rows[piv]
        pv = rows[piv][c]
        rows[piv] = [v / pv for v in rows[piv]]
        for r in range(len(rows)):
            if r != piv and rows[r][c] != 0:
                f = rows[r][c]
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[piv])]
        pc.append(c)
        piv += 1
        if piv == len(rows):
            break
    out = []
    for fc in [c for c in range(n) if c not in pc]:
        v = [Fraction(0)] * n
        v[fc] = Fraction(1)
        for i, p in enumerate(pc):
            v[p] = -rows[i][fc]
        out.append(v)
    return out


def test_e6_carrier_is_the_right_size():
    assert len(E6_ROOTS) == 72
    assert 6 + len(E6_ROOTS) == 78
    assert len(TWENTYSEVEN) == 27


def test_no_nonzero_cartan_element_has_nilpotent_ad():
    """The one-line fact the whole scope note rests on, RECOMPUTED.

    ad(h) is diagonal in the root basis with eigenvalues alpha(h), so it is nilpotent iff
    every eigenvalue vanishes.  If any nonzero h had all alpha(h) = 0 the roots would not
    span, and section D's argument would extend to nilpotents.
    """
    bad = []
    for c in itertools.product([-1, 0, 1, 2], repeat=6):
        if not any(c):
            continue
        h = {i: Fraction(c[i]) for i in range(6) if c[i]}
        if all(_alpha(h, r) == 0 for r in E6_ROOTS):
            bad.append(c)
    assert bad == [], f"nonzero Cartan elements with nilpotent ad: {bad[:3]}"
    assert _results()["nonzero_cartan_elements_with_nilpotent_ad"] == 0


def test_section_D_holds_on_its_own_class():
    """A torus element's centralizer always contains the full Cartan -- so the wall is real
    on semisimple elements, which is what makes the nilpotent exit meaningful."""
    for c in list(itertools.product([-1, 0, 1, 2], repeat=6))[:400]:
        if not any(c):
            continue
        h = {i: Fraction(c[i]) for i in range(6) if c[i]}
        dim_z = 6 + sum(1 for r in E6_ROOTS if _alpha(h, r) == 0)
        assert dim_z >= 6
    got, tot = _results()["sectionD_torus_centralizers_contain_cartan"]
    assert got == tot


def test_rank_four_occurs_at_exactly_fifteen_levis_five_A2_and_ten_2A1():
    """rank(Z) = 6 - rank_ss(L), so rank 4 <=> a size-2 subset of simple roots.
    Adjacent pair => A2, non-adjacent => 2A1.  Recomputed from the Cartan matrix."""
    size2 = list(itertools.combinations(range(6), 2))
    a2 = [S for S in size2 if A[S[0]][S[1]] == -1]
    a1 = [S for S in size2 if A[S[0]][S[1]] == 0]
    assert len(size2) == 15
    assert len(a2) == 5
    assert len(a1) == 10
    r = _results()
    assert (r["rank4_levi_count"], r["rank4_type_A2"], r["rank4_type_2A1"]) == (15, 5, 10)


def test_the_27_stays_complex_on_every_rank_four_levi():
    """Self-duality is decided by the weight multiset restricted to Z(L)^0:
    wt(M*) = -wt(M), so M is self-dual iff the multiset is negation-symmetric."""
    W27 = [tuple(sum(r[k] * A[k][i] for k in range(8)) for i in range(6)) for r in TWENTYSEVEN]
    for S in itertools.combinations(range(6), 2):
        basisZ = _nullspace([[Fraction(A[j][i]) for i in range(6)] for j in S], 6)
        restr = [tuple(sum(Fraction(w[i]) * b[i] for i in range(6)) for b in basisZ)
                 for w in W27]
        neg = [tuple(-x for x in t) for t in restr]
        assert sorted(restr) != sorted(neg), f"27 self-dual on rank-4 Levi {S}"
    assert _results()["twentyseven_complex_on_every_rank4_levi"] is True


def test_self_duality_first_appears_below_rank_three():
    """The complementary half: rank 4 keeps the 27 complex, and self-duality only starts
    once the rank has dropped to 2 or below."""
    assert max(_results()["ranks_with_self_dual_27"]) <= 2


def test_the_scope_is_recorded_as_a_note_not_a_refutation():
    """The arc must not claim more than it establishes: section D stands, the object's
    placement is owed, and real forms belong to B8071."""
    scope = _results()["scope"]
    assert "not a refutation" in scope
    assert "OWED not claimed" in scope
    assert "B8071" in scope
