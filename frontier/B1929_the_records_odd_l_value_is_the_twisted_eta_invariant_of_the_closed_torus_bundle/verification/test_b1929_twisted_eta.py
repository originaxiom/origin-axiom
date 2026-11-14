"""The lock of B1929: recomputes the Siegel winding on a few characters and the identity end to end; planted cases fail."""
import json, math, pathlib, sys
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "received_sm"))
import main_siegel as MS
import run_c9 as C

POP = json.loads((HERE / "received_sm" / "population.json").read_text())
ROWS = {(json.dumps(r["level"]), r["i"], r["j"]): r for r in json.loads((HERE / "received_sm" / "sm_c7_results.json").read_text())["rows"]}


def winding(o, use_jc=True):
    (a, b), (c, d) = o["M"]; N = o["N"]; c1, c2 = o["i"] / N, o["j"] / N
    A1, A2 = ((-c2) % 1.0, c1 % 1.0) if use_jc else (c1 % 1.0, c2 % 1.0)
    tr = a + d; D = tr * tr - 4
    r1 = ((a - d) + math.sqrt(D)) / (2 * b); r2 = ((a - d) - math.sqrt(D)) / (2 * b)
    cen, R = (r1 + r2) / 2, abs(r1 - r2) / 2
    zs = lambda s: complex(cen + R * math.tanh(s), R / math.cosh(s))
    ell = 2 * math.log((abs(tr) + math.sqrt(D)) / 2)
    g = lambda z: (a * z + c) / (b * z + d)
    s0 = -ell / 2
    s1 = s0 + ell if abs(g(zs(s0)) - zs(s0 + ell)) < 1e-7 * (1 + abs(zs(s0))) else s0 - ell
    return MS.winding_arc(A1, A2, zs, s0, s1)


def test_siegel_winding_is_the_odd_value():
    picked = [o for o in POP if o["N"] in (5, 13)][:6]
    for o in picked:
        Dl = winding(o)
        L = complex(*ROWS[(json.dumps(o["level"]), o["i"], o["j"])]["step2"]["c_odd"]["Lodd1"])
        assert abs(Dl.real) < 1e-10
        if abs(Dl) > 1e-9:
            assert abs(L / (math.pi * 1j * Dl) + 2) < 1e-8


def test_planted_characteristic():
    # planted: the characteristic c itself in place of Jc must not give the identity on every character
    bad = 0
    for o in [o for o in POP if o["N"] in (5, 13)][:6]:
        Dl = winding(o, use_jc=False)
        L = complex(*ROWS[(json.dumps(o["level"]), o["i"], o["j"])]["step2"]["c_odd"]["Lodd1"])
        if abs(Dl) < 1e-9 or abs(L / (math.pi * 1j * Dl) + 2) > 1e-6:
            bad += 1
    assert bad > 0


def test_end_to_end_on_stored_windings():
    D = {(json.dumps(r["level"]), r["i"], r["j"]): r["Delta"] for r in json.loads((HERE / "main_siegel.json").read_text())}
    worst = 0.0
    for o in POP:
        N = o["N"]; nu = (Fr((-o["i"]) % N, N), Fr((-o["j"]) % N, N))
        etaA = C.rho_467(o["M"], nu) + C.eta_untw(o["M"])
        L = -2 * math.pi * 1j * complex(*D[(json.dumps(o["level"]), o["i"], o["j"])])
        worst = max(worst, abs(float(etaA) + (L / math.pi ** 2).real))
    assert worst < 1e-10
    # planted: dropping the untwisted eta breaks it on the levels where eta != 0
    worst2 = max(abs(float(C.rho_467(o["M"], (Fr((-o["i"]) % o["N"], o["N"]), Fr((-o["j"]) % o["N"], o["N"])))) + (-2 * math.pi * 1j * complex(*D[(json.dumps(o["level"]), o["i"], o["j"])]) / math.pi ** 2).real) for o in POP)
    assert worst2 > 1e-3
