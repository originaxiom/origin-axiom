"""B1477 -- what decides the swap: the stored results re-read (the shear law on the census and on the link range, the
spin cells, existence at zero, the rotation-pi criterion), Theorem A's lattice step live, and the two controls live."""
import json, os, itertools, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1477_what_decides_the_swap_the_mirrors_shear_on_the_cusp", "verification")
J = lambda f: json.load(open(os.path.join(V, f)))
SEVEN = {"v3103", "t10425", "o10_085947", "o10_134228", "o10_146654", "o10_148196", "o10_149515"}


def lawful(r, key):
    return r[key] != "MIXED" and r["cs_class"] in ("zero", "quarter") and (r["cs_class"] == "quarter") == (r[key] == 1)


def test_the_sealed_form_fails_on_one_manifold_and_the_one_cusped_law_on_none():
    d = J("range_census_amphichiral.json"); am = d["amphichiral"]
    assert d["summary"]["range"] == 212641 and d["summary"]["errors"] == 0 and len(am) == 283
    one = [r for r in am if r["cusps"] == 1]; assert len(one) == 181 and all(lawful(r, "rhombic_parity") for r in one)
    assert sum(1 for r in one if r["cs_class"] == "quarter") == 75
    bad = [r["name"] for r in am if not lawful(r, "rhombic_parity")]; assert bad == ["o10_150729"]
    # the check can fail: a rectangular member relabelled quarter breaks it
    fake = dict(one[0]); fake["cs_class"] = "quarter" if fake["rhombic_parity"] == 0 else "zero"; assert not lawful(fake, "rhombic_parity")


def test_the_orbit_form_holds_on_the_census_and_on_the_fresh_range():
    c = J("orbit_form_census.json"); assert c["summary"]["exceptions"] == [] and len(c["rows"]) == 283 and all(lawful(r, "orbit_parity") for r in c["rows"])
    assert c["summary"]["sealed_form_mixed"] == ["o10_150729"] and set(c["summary"]["odd_orbit_longer_than_one"]) == {"t12067", "o10_150729"}
    l = J("orbit_form_links_amphichiral.json"); s = l["summary"]
    assert s["range"] == 120574 and s["amphichiral"] == 922 and s["exceptions"] == [] and s["conventions_disagree"] == 0 and s["quarter"] == 126
    assert all(lawful(r, "orbit_parity") and not r["invalid"] for r in l["amphichiral"])
    assert len(s["odd_orbit_longer_than_one"]) == 25 and len(s["sealed_form_mixed"]) == 9          # the range tests what the first seal got wrong


def test_theorem_a_covers_every_quarter_member_and_the_equivalence_dies_at_zero():
    rows = J("range_spin.json"); assert len(rows) == 181
    q = [r for r in rows if r["cs_class"] == "quarter"]; z = [r for r in rows if r["cs_class"] == "zero"]
    assert len(q) == 75 and all(r["rhombic"] and r["all_L_minus"] and r["theoremA_certifies"] == r["n_spin"] for r in q)
    assert sum(r["n_spin"] for r in q) == 292 and not any(r["rhombic"] for r in z)
    assert all(r["k_parity_exact"] == r["k_parity_geometric"] == (1 if r["rhombic"] else 0) for r in rows)
    rk1 = [r for r in rows if isinstance(r.get("torsion_real"), int)]; assert len(rk1) == 174
    assert sum(r["torsion_real"] for r in rk1 if r["cs_class"] == "quarter") == 0
    assert {r["name"] for r in rk1 if r["cs_class"] == "zero" and r["torsion_real"] == 0} == SEVEN
    assert all(r.get("spectrum_symmetric") == 0 for r in rows if r["name"] in SEVEN)


def test_existence_at_zero_by_witness_and_by_certificate():
    cu = J("zero_witness_cusped.json"); cl = J("zero_witness_closed.json")
    assert collections.Counter(v["verdict"] for v in cu.values()) == {"EXISTS": 7, "UNDECIDED": 2}
    assert len(cu["m136"]["invariant"]) == 4 and cu["m136"]["n_spin"] == 8 and not cu["m136"]["geometric_lift_fixed"]
    assert collections.Counter(v["verdict"] for v in cl.values()) == {"EXISTS": 13, "NONE-CERTIFIED": 15, "UNDECIDED": 9}
    assert all(v["spectrum_symmetric"] == 0 and not v["invariant"] for v in cl.values() if v["verdict"] == "NONE-CERTIFIED")
    assert all(v["spectrum_symmetric"] >= 1 for v in cl.values() if v["n_spin"] == 1)             # a single spin structure is fixed by everything


def test_rotation_pi_criterion_never_meets_a_survivor():
    p = [r for r in J("pi_geodesics.json").values() if "error" not in r]; odd = [r for r in p if r["odd_lengths"]]
    assert len(odd) == 39 and all(r["status"] == "NONE" for r in odd) and sum(1 for r in p if r["status"] == "EXISTS") == 20


def test_theorem_a_lattice_step_live():
    """every involution of determinant -1 in GL(2,Z) with small entries is 1 mod 2 or fixes exactly one nonzero class mod 2;
    a sign character is invariant under the second kind iff it is +1 on that class"""
    kinds = collections.Counter()
    for a, b, c, d in itertools.product(range(-3, 4), repeat=4):
        if a * d - b * c != -1 or (a * a + b * c, a * b + b * d, c * a + d * c, c * b + d * d) != (1, 0, 0, 1): continue
        F = lambda v: ((a * v[0] + b * v[1]) % 2, (c * v[0] + d * v[1]) % 2); nz = [(1, 0), (0, 1), (1, 1)]
        fixed = [v for v in nz if F(v) == v]
        if len(fixed) == 3: kinds["rectangular"] += 1; continue
        assert len(fixed) == 1; kinds["rhombic"] += 1; w = fixed[0]
        for sx, sy in itertools.product((1, -1), repeat=2):
            sig = lambda v: (sx if v[0] else 1) * (sy if v[1] else 1)
            assert all(sig(F(v)) == sig(v) for v in nz) == (sig(w) == 1)
    assert kinds["rectangular"] > 0 and kinds["rhombic"] > 0


def test_the_two_controls_live():
    import snappy
    for nm, want in (("m004", 0), ("m003", 1)):
        M = snappy.Manifold(nm); par = set()
        for iso in M.is_isometric_to(M, return_isometries=True):
            m = iso.cusp_maps()[0]
            if int(m[0, 0]) * int(m[1, 1]) - int(m[0, 1]) * int(m[1, 0]) == -1:
                par.add(int([int(m[0, 0]) % 2, int(m[0, 1]) % 2, int(m[1, 0]) % 2, int(m[1, 1]) % 2] != [1, 0, 0, 1]))
        assert par == {want}, nm
        x = float(M.chern_simons()) % 0.5; assert (abs(x - 0.25) < 1e-7) == bool(want)
