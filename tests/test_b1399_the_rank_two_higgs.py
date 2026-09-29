"""B1399 lock -- THE RANK-TWO HIGGS, run as sealed.

With 27 matter the frame's rule admits one anomaly-free family, g generations at t = g(1, 0, -1, 0, 1, -2) on six direction classes.
On the sealed census (the degree-2 and degree-3 covers of B1186's 99 arithmetic members with cuspidal dimension >= 2, 109 up to
isometry) 102 members resolved and none realises any g: P1 NONE, P2 NONE.  The reason is parity: a leading shell whose vectors span a
sublattice of index m gives a cusp term in multiples of m, and on the resolved set every leading shell has one direction (a band, 0)
or three directions spanning index 2.  The census's hexagonal cusps (index 1, odd terms possible) sit on four members, all unresolved."""
import importlib.util
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1399_the_rank_two_higgs"
VER = ARC / "verification"
NONZERO = "EvvLvvwvLAvQMMQQwQQQQggp"                                  # the degree-3 cover of o10_150708
HEXAGONAL = "EvvLLLwvLwAQPvwPQQQQQgjk"                                # the four-cusped cover of o10_150725
SMALL = "yLvLwAvLwMMPPAMQQaeeghpj"                                    # a one-cusped member of dimension 2 (parent t12833)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _checks():
    return _load("b1399_post_run_checks", VER / "post_run_checks.py")


def _census():
    return json.load(open(VER / "census.json"))


def _member(d, prefix):
    (m,) = [m for m in d["members"] if m["label"].startswith(prefix)]
    return m


def test_the_census_as_recorded():
    d = _census()
    ms = d["members"]
    res = [m for m in ms if m["status"] == "resolved"]
    un = [m for m in ms if m["status"] != "resolved"]
    assert (len(ms), len(res), len(un)) == (109, 102, 7)
    assert sum(m["dim"] == 3 for m in res) == 18
    assert all(len(m["circles"]) == 203 for m in res if m["dim"] == 3)          # every sealed plane read
    # P1 and P2: no g on any resolved member, on any plane
    assert all(m["achievable_g"] == [] and m["g3"] is False and m["positive"] == {} for m in res)
    assert all(c["g"] == [] for m in res for c in m["circles"])
    # P3: max |C| is 0 on 101 members and 2 on one; the summary agrees with the members
    assert sorted(m["maxC"] for m in res) == [0] * 101 + [2]
    s = d["summary"]
    assert s["maxC_resolved"] == {"0": 101, "2": 1} and s["achievable_g_any"] == [] and s["P1_g3_members"] == []
    assert sorted(u["label"] for u in s["unresolved_members"]) == sorted(m["label"] for m in un)
    # the ladder moved on after a seed disagreement (the E2 fix): the four such members tried all three rungs
    disagree = [m for m in un if m["reason"] == "no rung passes acceptance with both seeds" and m["cusps"] == 4]
    assert len(disagree) == 4
    assert all(len(m["rungs"]) == 3 and all(r["accepted"].startswith("seeds disagree") for r in m["rungs"]) for m in disagree)


def test_parity_on_the_resolved_set():
    """every resolved leading shell has one direction or three at the third shell of a sqrt(-3) cusp, so C is even everywhere"""
    d = _census()
    res = [m for m in d["members"] if m["status"] == "resolved"]
    lead = [(v["index"], v["vectors"]) for m in res for v in m["leading"].values()]
    assert len(lead) == 207 and sorted(set(lead)) == [(0, 1), (1, 1), (2, 3)] and lead.count((2, 3)) == 3
    assert all(x % 2 == 0 for m in res if "V_circle" in m for x in m["V_circle"]["vals"])
    nz = _member(d, NONZERO)
    assert nz["parent"] == "o10_150708" and nz["maxC"] == 2
    assert sorted(set(nz["V_circle"]["vals"])) == [-2, 0, 2]
    assert len(nz["V_circle"]["bps"]) == 12 and all(abs(j) == 2 for _, j in nz["V_circle"]["bps"])


def test_the_parity_lemma_and_the_lattices():
    P = _checks()
    lemma = P.parity_lemma()                                    # asserts inside: every value a multiple of the index, one non-zero
    assert set(lemma["sqrt(-3) third shell, index 2"]) == {"-2", "0", "2"}
    assert set(lemma["hexagonal first shell, index 1"]) == {"-1", "0", "1"}
    assert set(lemma["hexagonal sqrt(3) shell, index 3"]) == {"-3", "0", "3"}
    d = _census()
    # the non-zero member: cusp 1 has shape sqrt(-3), its third shell has three directions spanning index 2 and leads
    nz = _member(d, NONZERO)
    cu = P.cusps_of(nz["label"])
    assert cu[1]["form"] == "0 + 1*sqrt(-3)" and cu[1]["shell_directions"][:3] == [1, 1, 3] and cu[1]["shell_span_index"][2] == 2
    assert nz["leading"]["1"]["index"] == 2 and nz["leading"]["1"]["vectors"] == 3
    assert cu[0]["cls"] == "other" and cu[0]["shell_directions"][nz["leading"]["0"]["index"]] == 1
    # a hexagonal member: two hexagonal cusps, first shell three directions spanning the whole lattice; the member is unresolved
    hx = _member(d, HEXAGONAL)
    cu = P.cusps_of(hx["label"])
    hexes = [x for x in cu if x["cls"] == "hexagonal"]
    assert len(hexes) == 2 and all(x["shell_directions"][0] == 3 and x["shell_span_index"][0] == 1 for x in hexes)
    assert hx["status"] == "unresolved"
    # the recorded census-wide check
    rec = json.load(open(VER / "post_run_checks.json"))["summary"]
    assert rec["cusps_by_status_and_class"] == {"resolved/other": 207, "unresolved/hexagonal": 8, "unresolved/other": 14}
    assert rec["leading_shell_directions_match_the_lattice"] is True and rec["every_shape_in_Q_sqrt_minus_3"] is True


def test_linear_programs_and_the_pattern():
    """the banked identity's parts (3) and (4): a synthetic count realising g = 3 is found, one jump removed is infeasible"""
    P = _checks()
    R = P.R
    rays = []
    for (pa, pb), t in zip(R.CLASSES, R.PATTERN):
        th = math.atan2(pb, pa) % R.TWO_PI
        rays += [(th, 3 * t), ((th + math.pi) % R.TWO_PI, -3 * t)]
    rays.sort()
    mids = [((rays[i][0] + ((rays[(i + 1) % 12][0] - rays[i][0]) % R.TWO_PI) / 2) % R.TWO_PI) for i in range(12)]

    def synthetic(values_by_ray):
        bps = sorted((m, 0) for m in mids)
        vals = []
        for st, ln in R.arcs_of(bps):
            ray = min(rays, key=lambda r: R.adist(r[0], (st + ln / 2) % R.TWO_PI))
            vals.append(values_by_ray[ray[0]])
        bps = [(t, vals[i] - vals[i - 1]) for i, (t, _) in enumerate(bps)]
        return dict(cusps={}, bps=bps, arcs=R.arcs_of(bps), vals=vals)
    good = synthetic({th: val for th, val in rays})
    assign = next(R.assignments(good, 3), None)
    assert assign is not None
    L, margin = R.max_margin(assign)
    imgs = [math.atan2(*(L @ R.np.array(p, dtype=float))[::-1]) % R.TWO_PI for p in R.CLASSES]
    assert margin > 0 and all(R.value_on(good["bps"], good["vals"], th) == 3 * t for th, t in zip(imgs, R.PATTERN))
    bad_vals = {th: val for th, val in rays}
    bad_vals[0.0], bad_vals[math.pi] = 3, -3                    # (1, 0) given (3, -2)'s value: a required jump removed
    assert next(R.assignments(synthetic(bad_vals), 3), None) is None
    FV = _load("b1398_frame_verdict", ROOT / "frontier" / "B1398_the_frame_verdict_on_three" / "verification" / "frame_verdict.py")
    got = FV.main()["V5 the anomaly-free family at g = 3: N per class"]
    assert got == {str(cls): 3 * t for cls, t in zip(R.CLASSES, R.PATTERN)}


def test_members_rerun_to_their_records():
    """the seeded build is deterministic (the E1 fix), and the non-zero member and a small one reproduce their census records"""
    P = _checks()
    R = P.R
    d = _census()
    for prefix in (SMALL, NONZERO):
        rec = _member(d, prefix)
        G1 = R.manifold(rec["label"]).fundamental_group(simplify_presentation=False)
        G2 = R.manifold(rec["label"]).fundamental_group(simplify_presentation=False)
        assert G1.relators(as_int_list=True) == G2.relators(as_int_list=True)
        again = json.loads(json.dumps(R.run_member(R.manifold(rec["label"]), expect_dim=rec["dim"], label=rec["label"]), default=float))
        for k in ("status", "dim", "maxC", "achievable_g", "g3", "leading", "circles", "V_circle", "positive"):
            assert again.get(k) == rec.get(k), (prefix, k)
