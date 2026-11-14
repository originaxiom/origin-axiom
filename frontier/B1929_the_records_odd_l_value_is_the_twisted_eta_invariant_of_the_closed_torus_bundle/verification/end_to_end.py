"""The identity end to end on main (written before the run): eta_A(T^2_M) = rho_A + eta(T^2_M) from the SM seat's
transcription of Bohn's (4.67) (received_sm/run_c9.py, run unchanged; agy-exp transcribed Bohn independently in X-C9),
against -L_odd(1, chi_c)/pi^2 with L_odd = -2 pi i Delta from main's own Siegel winding (main_siegel.json).
Expectation: equal on all 601 characters to rounding."""
import json, math, pathlib, sys
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "received_sm"))
import run_c9 as C


def compare():
    pop = json.loads((HERE / "received_sm" / "population.json").read_text())
    D = {(json.dumps(r["level"]), r["i"], r["j"]): r["Delta"] for r in json.loads((HERE / "main_siegel.json").read_text())}
    worst = 0.0
    for o in pop:
        N = o["N"]; nu = (Fr((-o["i"]) % N, N), Fr((-o["j"]) % N, N))
        etaA = C.rho_467(o["M"], nu) + C.eta_untw(o["M"])
        L = -2 * math.pi * 1j * complex(*D[(json.dumps(o["level"]), o["i"], o["j"])])
        worst = max(worst, abs(float(etaA) + (L / math.pi ** 2).real))
    return len(pop), worst


if __name__ == "__main__":
    n, w = compare()
    print("eta_A (Bohn, the seat's transcription) against -L_odd/pi^2 (main's Siegel winding): %d characters, largest |difference| %.1e" % (n, w))
