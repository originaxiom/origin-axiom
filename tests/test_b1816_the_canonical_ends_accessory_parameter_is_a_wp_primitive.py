"""B1816 -- the canonical end's accessory parameter is a Weil-Petersson primitive: the committed checks (main's, the
referee's regenerated on main), the off-branch control, the volume closure, and the depth tail on B1667's stored grid."""
import json, math, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1816_the_canonical_ends_accessory_parameter_is_a_wp_primitive"
V = A / "verification"
B1667 = ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"
DELTA = 4 * math.log(2) / math.pi


def test_mains_check_on_the_true_root_and_the_control():
    d = json.loads((V / "verify_wp.json").read_text(encoding="utf-8"))
    pts = [k for k in d if k.startswith("(")]
    assert len(pts) == 4
    for k in pts:
        assert abs(d[k]["Im dC/dtaubar / FN route"] - 1) < 1e-7 and d[k]["|Re| / |dC/dtaubar|"] < 1e-7
    assert abs(d["(0.3+5j)"]["h_WP (FN route)"] / d["(0.3+5j)"]["cusp form (pi^2/2)/(y+delta)^3"] - 1) < 0.02   # WP's cusp form
    assert d["(0.3+5j)"]["hyperbolic (pi/4)/y^2"] / d["(0.3+5j)"]["h_WP (FN route)"] > 1.2                      # not area's
    ctl = d["control: root from c = 0 at 0.15+3j (not the uniformisation)"]
    assert abs(ctl["c"][0] + 4.1224) < 1e-3 and abs(ctl["Im dC/dtaubar / FN route"] - 1) < 1e-7          # the identity is branch-blind
    assert ctl["h (FN route of this root's holonomy)"] > 10 * ctl["true root's h_WP"]


def test_the_referees_checks_regenerated_on_main():
    M = V / "referee" / "main_rerun"
    for line in (M / "chk1_out.txt").read_text(encoding="utf-8").splitlines():
        r = json.loads(line)["0.0005"]; assert abs(r["Im/half|det|"] - 1) < 1e-9 and r["ReOverAbs"] < 1e-9 and r["det"] > 0
    gate = (M / "chk2_out.txt").read_text(encoding="utf-8").splitlines()
    true = [float(re.search(r"Im u min (\S+)", l).group(1)) for l in gate if l.startswith("true")]
    ctl = [float(re.search(r"Im u min (\S+)", l).group(1)) for l in gate if l.startswith("control")]
    assert len(true) == 5 and min(true) > 0.05 and ctl and ctl[0] < -0.1                                    # the gate discriminates
    low = float(re.search(r"lower region integral \(both halves\): (\S+)", (M / "chk4_out.txt").read_text(encoding="utf-8")).group(1))
    avg = float(re.search(r"<Re c>_x\(1\) = (\S+)", (M / "chk6_out.txt").read_text(encoding="utf-8")).group(1))
    assert abs(low - avg) < 1e-6                                                                              # Stokes: the volume closes
    rho = {l.split(" h ")[0]: float(l.split("rho=h*y^2 ")[1]) for l in (M / "chk7_out.txt").read_text(encoding="utf-8").splitlines()}
    assert abs(rho["(0.02+1j)"] - 0.961) < 2e-3 and max(rho.values()) < 0.97 and rho["(0.5+3j)"] < 0.8          # a 0.5% bulk variation


def test_the_depth_tail_on_b1667s_grid():
    pts = json.loads(B1667.read_text(encoding="utf-8"))["points"]
    P = {round(q["tau"][1], 2): 1 - 12 * q["c"][0] / math.pi ** 2 for q in pts if abs(q["tau"][0] - 0.25) < 1e-9}
    assert abs(P[3.0] - 0.2016) < 1e-3 and abs(P[2.0] - 0.3723) < 1e-3
    for Y in (3.0, 3.5):
        assert abs(P[Y] / (3 / (Y + DELTA) ** 2) - 1) < 0.02                                                 # WP's tail
        assert P[Y] < 0.75 * 3 / (math.pi * Y)                                                                # thinner than area's
    ys = sorted(y for y in P if y >= 1)
    assert all(P[a] > P[b] for a, b in zip(ys, ys[1:]))
