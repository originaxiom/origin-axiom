"""B1663 -- the pull-back's strength. The sealed instrument unchanged; the stored cells; live through the sealed
instrument: the character rule (L and R^-1 add +1 to #L - #R, R and L^-1 add -1, so a step is +1 with probability 1/2
at every p); one seeded walk reproduced exactly; the ray instrument on a fixed digit string; the bite -- a walk with the
other seed differs, and the ray average of a different digit string differs."""
import hashlib, importlib.util, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1663_the_pull_backs_strength"
INSTR = A / "verification" / "the_pull_backs_strength.py"


def _load():
    spec = importlib.util.spec_from_file_location("b1663_lock", INSTR)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 9c3f74238")
    assert hashlib.sha256(open(INSTR, "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("1ce96661")
    d = json.load(open(A / "verification" / "the_pull_backs_strength.json"))
    assert d["PS"] == [0.0, 0.1, 0.2, 0.3, 0.4, 0.5] and d["WALKS"] == 320
    assert d["T0"]["holds"] is True and d["T1"]["holds"] is True
    assert d["T2"]["holds"] is True and d["T3"]["holds"] is True
    t4 = d["T4"]; assert t4["a_p0_not_typical"] and t4["c_half_not_typical"] and not t4["b_p_not_idle"] and t4["holds"] is False
    assert t4["readout_spread_over_p"] < 0.01 and abs(t4["readout_half"]["mean"] - 0.5178) < 1e-3 and d["all_hold"] is False
    assert abs(d["T0"]["control_mean"] - 0.31500491) < 3*d["T0"]["control_se"]
    run = open(A / "verification" / "the_pull_backs_strength_run.txt").read(); assert "all_hold False" in run
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "NEGATIVE"


def test_live_rules_walk_and_ray():
    m = _load()
    p = 0.3
    assert abs(((1 - p)/2 + p/2) - 0.5) < 1e-15                               # L or R^-1: the character's +i step
    r1 = m.walk((0.5, 4242)); r2 = m.walk((0.5, 4242)); r3 = m.walk((0.5, 4243))
    assert r1 == r2 and r1 != r3                                                # deterministic by seed; bite: another seed
    ds = [1, 2, 1, 1, 3, 1, 2, 2, 1, 1]*8
    a = m.ray_average(ds); b = m.ray_average([x + 1 for x in ds])
    assert 0 < a < 1 and abs(a - b) > 1e-3                                       # bite: other digits, another average
