"""B1483 -- the end of the frame space: the stored runs re-read against the five sealed predictions, the lemma's
dictionary and its two consequences checked live on lattices, and the j-function's reduction shown able to fail."""
import json, os, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1483_the_end_of_the_frame_space", "verification")
sys.path.insert(0, V)


def test_the_end_curves_of_the_68_states():
    import end_curve as E
    d = json.load(open(os.path.join(V, "end_curve.json"))); st = d["states"]; assert d["summary"]["states"] == 68 and d["summary"]["errors"] == {}
    plus = [r for n, r in st.items() if n.startswith("b++")]; minus = [r for n, r in st.items() if n.startswith("b+-")]
    assert len(plus) == len(minus) == 34
    assert all(row["sigma"][0] == -1 for r in plus + minus for row in r["rows"])
    assert all(row["j_real"] for r in plus for row in r["rows"])                                        # R1, + states
    for r in minus:                                                                                     # R1, - states
        c = E.classes(r); assert set(c) == {(-1, 1), (-1, -1)} and E.conj_pair(c[(-1, 1)]["j"], c[(-1, -1)]["j"]), r["name"]
    real = sorted(r["name"] for r in minus if E.classes(r)[(-1, 1)]["j_real"])
    assert real == ["b+-LLRR", "b+-LR"] and abs(E.classes(st["b+-LR"])[(-1, 1)]["j"][0] - 54000) < 1e-3    # R2: 32 of 34 not real
    assert not E.conj_pair([1.0, 2.0], [1.0, 2.0]) and E.conj_pair([1.0, 2.0], [1.0, -2.0])              # the pairing test can fail


def test_the_dictionary_and_its_two_consequences_live():
    """rectangular (Re z integral): all four curves have real j; rhombic with sigma(L) = -1: tau and -conj(tau) mod 1"""
    import end_curve as E
    from mpmath import mpc, mp
    mp.dps = 25
    z = mpc(-2, 0.71)                                           # a rectangular shape that is not special
    for tau in (z, z / 2, (z + 1) / 2, 2 * z): assert abs(E.j_of(tau).imag) < 1e-9 * max(1, abs(E.j_of(tau)))
    z = mpc(-2.5, 0.71)                                         # a rhombic shape that is not special
    a, b = E.j_of(z / 2), E.j_of((z + 1) / 2)
    assert abs(a - b.conjugate()) < 1e-9 * abs(a) and abs(a.imag) > 1e-3 * abs(a)
    assert abs(E.j_of(mpc(0, 3 ** 0.5)) - 54000) < 1e-6 and abs(E.j_of(mpc(0, 1)) - 1728) < 1e-9          # two classical values


def test_the_two_covers():
    n = json.load(open(os.path.join(V, "cover_m003_45_5.json")))[0]
    assert (n["tetrahedra"], n["cusps"], n["mirrors"], n["spin_structures"], n["invalid"]) == (90, 5, 180, 128, 0) and abs(n["cs_mod_half"] - 0.25) < 1e-9
    assert n["mirror_patterns"] == [[[1, 4], [[1, "rhombic"]]]] and n["excluded_for_every_mirror"] == 8
    by = collections.Counter(sum(1 for v in s["signs"].values() if v == -1) for s in n["spin"]); assert dict(by) == {1: 40, 3: 80, 5: 8}
    assert collections.Counter(s["mirrors_excluded"] for s in n["spin"]) == {36: 40, 108: 80, 180: 8}
    w = json.load(open(os.path.join(V, "witness_o10_150729.json")))
    assert w["verdict"] == "NONE-CERTIFIED" and w["n_spin"] == 32 and w["n_tau"] == 40 and w["invariant"] == [] and w["spectrum_symmetric"] == 0 and w["partner_failures"] == 0
    assert all(r[0] is False for r in w["spectrum_rows"])


def test_the_two_exceptions_are_the_hexagonal_and_the_square_cusp():
    """post-seal addendum: (E, sigma_+) = (E, sigma_-) iff the cusp lattice has an automorphism of order > 2"""
    import json, pathlib
    here = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1483_the_end_of_the_frame_space" / "verification"
    d = json.load(open(here / "exceptions_explained.json")); s = d["summary"]
    assert s["states"] == 68 and s["minus"] == 34 and s["plus"] == 34 and s["every_cusp_modulus_real"]
    assert s["cusp_lattice_hexagonal_or_square"] == {"b+-LR": "hexagonal", "b+-LLRR": "square"}
    assert s["minus_states_with_real_end_curves"] == ["b+-LLRR", "b+-LR"] and s["the_two_sets_agree"]
    assert s["plus_states_with_real_end_curves"] == 34
    # the failing path: a - state that is neither hexagonal nor square must not have real end curves
    assert not any(r["sign"] == "-" and r["lattice"] is None and r["end_curves_real"] for r in d["rows"].values())
