"""B1271 — the chain taken all the way: the rank reduction by the 27's singlets, the vanishing of the
E8-forced Yukawa on the triplet and the cubic's SO(10) content fast; the family tensor on the icosian E8
(same-class sums never roots, cross-class sums landing in the third index' conjugate class) in one block fast
and the whole table in the slow lane."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1271_the_chain_all_the_way" / "verification"
for arc in ("B1267_spectrum_law_rebuilt", "B1269_transport_computed", "B1270_e6_from_the_two_faces"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))
sys.path.insert(0, str(VER))


@pytest.fixture(scope="module")
def AW():
    import all_the_way as AW
    return AW


def test_the_27s_two_singlets_take_the_rank_from_6_to_4(AW, capsys):
    """Exactly two SM singlets in the 27 (nu^c in the 16, the SO(10) singlet), and their charges under the
    two extra U(1)s of the rank-6 Levi are independent: VEVs for both leave exactly su(3)+su(2)+u(1)_Y."""
    assert AW.part_b()
    out = capsys.readouterr().out
    assert "weights [12, 13]" in out
    assert "rank = 2" in out
    assert "{12: '16', 13: '1'}" in out


def test_the_e8_forced_yukawa_on_the_triplet_vanishes_identically(AW, capsys):
    """W = d_abc eps^{ijk} 27^a_i 27^b_j 27^c_k == 0 for generic symmetric d on the 45-triple support;
    the symmetric-family-tensor control is nonzero."""
    assert AW.part_c()
    out = capsys.readouterr().out
    assert "expands to 0" in out
    assert "135 monomials, nonzero" in out


def test_the_e6_cubic_has_so10_content_40_plus_5(AW, capsys):
    assert AW.part_d()
    out = capsys.readouterr().out
    assert "summing to zero: 45" in out


def test_the_family_tensor_on_the_triplet_is_eps_one_block(AW):
    """The fast lane of (a): one same-class block and one cross-class block of the 3 x 3 table on the icosian
    E8.  The three classes of the g-orbit have Eisenstein pairings summing to zero; same-class root sums of
    (27,3)_0 are never roots; the (27,3)_0 + (27,3)_1 root sums, 270 = 6 x 45 of them, all land in the
    class -e_2 of the third index."""
    TF = AW.TF
    units = TF.unit_icosians()
    roots = TF.e8_roots(units)
    one = (TF.Q5(1), TF.Q5(0), TF.Q5(0), TF.Q5(0))
    w = next(u for u in units if TF.orders_of(u, one, TF.key) == 3)
    rk = {TF.key(r) for r in roots}
    cls = {TF.key(r): (TF.bil(r, one), TF.bil(r, w)) for r in roots}
    import collections
    counts = collections.Counter(cls.values())
    triplet = [c for c, n in counts.items() if n == 27]
    assert len(triplet) == 6
    byclass = collections.defaultdict(list)
    for r in roots:
        byclass[cls[TF.key(r)]].append(r)
    c0 = triplet[0]
    r0 = byclass[c0][0]
    r1 = TF.qmul(w, r0)
    c1 = cls[TF.key(r1)]
    c2 = cls[TF.key(TF.qmul(w, r1))]
    assert len({c0, c1, c2}) == 3 and all(c in triplet for c in (c1, c2))
    assert all(c0[t] + c1[t] + c2[t] == 0 for t in range(2))          # the weights of a 3 sum to zero
    same = sum(1 for r in byclass[c0] for s in byclass[c0]
               if TF.key(tuple(a + b for a, b in zip(r, s))) in rk)
    assert same == 0
    landing = collections.Counter()
    for r in byclass[c0]:
        for s in byclass[c1]:
            t = tuple(a + b for a, b in zip(r, s))
            if TF.key(t) in rk:
                landing[cls[TF.key(t)]] += 1
    assert sum(landing.values()) == 270
    assert list(landing) == [tuple(-x for x in c2)]                     # e_0 + e_1 = -e_2: the eps structure


@pytest.mark.slow
def test_the_whole_family_tensor_table_is_eps_ijk(AW):
    assert AW.part_a()
