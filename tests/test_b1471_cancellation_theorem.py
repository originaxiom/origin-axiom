"""B1471 -- the cancellation is a theorem of amphichirality: the stored census re-scored, the m004 control re-run live,
and the lane's anti-homomorphism named (the control that cannot fail: a homomorphism check on main's sym)."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1471_the_cancellation_is_a_theorem_of_amphichirality", "verification")
LANE_FIVE = ["m206", "m207", "s957", "s960", "s961"]


def test_analysis_rescored_from_the_stored_census():
    r = subprocess.run([sys.executable, os.path.join(V, "analyze.py")], capture_output=True, text=True, cwd=V)
    assert r.returncode == 0, r.stderr[-400:]
    a = json.load(open(os.path.join(V, "analysis.json")))
    assert a["members"] == 112 and a["usable"] == 54 and len(a["excluded"]) == 58
    assert len(a["P1"]["holds"]) == 54 and a["P1"]["fails"] == []
    assert len(a["P2"]["holds"]) == 13 and a["P2"]["fails"] == []
    assert len(a["chiral_members"]["complex"]) == 40 and a["chiral_members"]["real"] == ["o10_150709"]
    assert a["column_disagreements"] == []
    for nm in LANE_FIVE:
        f = a["lane_five"][nm]
        assert f["amphi_iso"] and f["duality"] and f["real_even"] and f["phase_even"] == ["real", "real"], (nm, f)


def test_odd_n_characters_are_exact_and_split_five_two():
    d = json.load(open(os.path.join(V, "odd_characters.json")))
    assert len(d) == 7
    through = {nm: any(m["factors_through_phi"] for m in v["matches"]["1"]) for nm, v in d.items()}
    assert sum(through.values()) == 5 and not through["s955"] and not through["s957"]
    for nm, v in d.items():
        for n in ("1", "3"):
            assert all(m["unit"] == [0, 1] for m in v["matches"][n]), (nm, n)


def test_m004_control_live_against_b425():
    sys.path.insert(0, V)
    import realness as R
    from mpmath import mpf
    pk, err = R.setup("m004"); assert err is None
    t = mpf(2); banked = {1: (t * t - 4 * t + 1) / t ** 2, 2: (t - 1) * (t * t - 5 * t + 1) / t ** 3, 3: (t * t - 4 * t + 1) ** 2 / t ** 4}
    for n, want in banked.items():
        v = R.Wada(pk, n).value(t); assert v is not None
        assert min(abs(v - want), abs(v + want)) < mpf(10) ** -40, (n, v, want)
    # main's sym is a homomorphism (the lane's was an anti-homomorphism: the check that its m004 control could not make)
    from mpmath import norm
    A, B = pk["rho"]["a"], pk["rho"]["b"]
    assert norm(R.sym(A * B, 3) - R.sym(A, 3) * R.sym(B, 3)) < mpf(10) ** -40
    assert norm(R.sym(A * B, 3) - R.sym(B, 3) * R.sym(A, 3)) > 1
