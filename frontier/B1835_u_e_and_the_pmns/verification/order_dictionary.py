"""THE ORDER IS THE UNIFICATION PATTERN (P-682; data-free). From B1728's law -- on a line of order N a charge shift by N
multiplies a sector's matrices by one phase, the left-right swap transposes them, and negating both charges leaves them
unchanged -- two sectors X = (qL, qR), Y = (qL', qR') have M_X ∝ M_Y when (qL', qR') ≡ ±(qL, qR) (mod N), and
M_X ∝ M_Y^T when (qL', qR') ≡ ±(qR, qL) (mod N). Predicted for every N, then confirmed on main's instrument (B1835's
card_instrument, B1726's compute path, the Higgs DR, both horocycles' L_max) at two lines of exact order N and two tau:
each predicted relation must hold, each unpredicted one must fail."""
import itertools, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier/B1835_u_e_and_the_pmns/verification"))
from card_instrument import yukawas
SECT = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6), "nu": (-3, 0)}
def eq(x, y, N): return all((a - b) % N == 0 for a, b in zip(x, y))
def rel(X, Y, N):
    a, b = SECT[X]; c, d = SECT[Y]
    out = set()
    if eq((c, d), (a, b), N) or eq((c, d), (-a, -b), N): out.add("=")
    if eq((c, d), (b, a), N) or eq((c, d), (-b, -a), N): out.add("T")
    return out
def prop(A, B):
    c = np.vdot(B.ravel(), A.ravel()) / np.vdot(B.ravel(), B.ravel()); return float(np.max(np.abs(A - c * B)) / np.max(np.abs(A)))
ORDERS = [2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 30]
print("PREDICTED (exact, from the charges mod N): '=' proportional, 'T' transposed")
pred = {}
for N in ORDERS:
    pred[N] = {(X, Y): rel(X, Y, N) for X, Y in itertools.combinations(SECT, 2)}
    pred[N].update({(X, X): rel(X, X, N) & {"T"} for X in SECT})
    print("N = %2d: " % N + "; ".join("%s~%s %s" % (X, Y, "".join(sorted(v))) for (X, Y), v in pred[N].items() if v))
print("\nCONFIRMED on main's instrument (reading S for every sector; max deviation where predicted, min where not):")
worst_hold = 0.0; least_fail = 9.0; nfail = 0
for N in ORDERS:
    lines = [(F(1, N), F(0)), (F(1, N), F(1, N))]
    for (re_t, im_t) in ((0.31, 2.9), (0.12, 3.2)):
        for (a, b) in lines:
            Y = yukawas(re_t, im_t, float(a), float(b), "L_max", tuple(SECT))
            for (X, Z), v in pred[N].items():
                A, B = Y[(X, "S")], Y[(Z, "S")]
                for kind, M2 in (("=", B), ("T", B.T)):
                    if X == Z and kind == "=": continue
                    d = prop(A, M2)
                    if kind in v: worst_hold = max(worst_hold, d)
                    else:
                        least_fail = min(least_fail, d)
                        if d < 1e-8: nfail += 1; print("  UNPREDICTED HOLD: N=%d line %s %s %s %s dev %.1e" % (N, (a, b), X, kind, Z, d))
print("predicted relations: max deviation %.1e ; unpredicted: min deviation %.2e ; unpredicted holds: %d" % (worst_hold, least_fail, nfail))
