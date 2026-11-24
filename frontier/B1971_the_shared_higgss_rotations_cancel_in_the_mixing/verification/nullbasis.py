"""B1971 (main, 2026-11-24; data-free): the all-S frame's vectors in the unitary null basis
n = (1, 0, i)/sqrt2, nb = (1, 0, -i)/sqrt2, e = (0, 1, 0) (closed-form order).  Coordinates are Hermitian projections.
Rates (eps units) of every coordinate of h, u_up, u_down, of w, and of the left singular vectors in this basis, plus V."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import invariants as IV
from fractions import Fraction as Fr
mp = IV.mp
import cusp_mixing as CM   # on the path from invariants (B1945)

def basis():
    s = 1 / mp.sqrt(2)
    return [mp.matrix([s, 0, 1j * s]), mp.matrix([s, 0, -1j * s]), mp.matrix([0, 1, 0])]
def coords(v):
    P = basis(); return [sum(mp.conj(P[k][i]) * v[i] for i in range(3)) for k in range(3)]

def snap(y, a, b):
    out = {}
    for sec in ("up", "down"):
        V = IV.vars_of(y, a, b, sec)
        out[sec] = dict(h=coords(V["h"]), u=coords(V["u"]), w=V["w"], U=CM.U_of(V["Y"]), Y=V["Y"],
                        nh=abs(IV.dot(V["h"], V["h"])) / sum(abs(x) ** 2 for x in V["h"]),
                        nu=abs(IV.dot(V["u"], V["u"]) + V["w"] ** 2) / (sum(abs(x) ** 2 for x in V["u"]) + abs(V["w"]) ** 2),
                        ov=abs(IV.dot(V["u"], V["h"])) / mp.sqrt(sum(abs(x) ** 2 for x in V["u"]) * sum(abs(x) ** 2 for x in V["h"])))
        P = basis(); U = out[sec]["U"]
        out[sec]["Ub"] = [[sum(mp.conj(P[k][i]) * U[i, c] for i in range(3)) for c in range(3)] for k in range(3)]
    out["V"] = out["up"]["U"].H * out["down"]["U"]
    return out

if __name__ == "__main__":
    y1, y2 = 20.0, 30.0
    R = lambda p, q: IV.rate(p, q, y1, y2)
    f = lambda x: "  -  " if x is None else "%6.2f" % x
    for name, (a, b) in {"mark": (Fr(2, 5), Fr(4, 5)), "twin": (Fr(1, 5), Fr(2, 5))}.items():
        A, B = snap(y1, a, b), snap(y2, a, b)
        print("==", name)
        for sec in ("up", "down"):
            sh = R(sum(abs(x) ** 2 for x in A[sec]["h"]) ** 0.5, sum(abs(x) ** 2 for x in B[sec]["h"]) ** 0.5)
            su = R(sum(abs(x) ** 2 for x in A[sec]["u"]) ** 0.5, sum(abs(x) ** 2 for x in B[sec]["u"]) ** 0.5)
            print("  %-4s h (n, nb, e) rel: %s | u rel: %s | w rel: %s | nullity h %s, u(+w) %s, overlap u.h %s" % (
                sec, " ".join(f(None if R(A[sec]["h"][k], B[sec]["h"][k]) is None else R(A[sec]["h"][k], B[sec]["h"][k]) - sh) for k in range(3)),
                " ".join(f(None if R(A[sec]["u"][k], B[sec]["u"][k]) is None else R(A[sec]["u"][k], B[sec]["u"][k]) - su) for k in range(3)),
                f(None if R(A[sec]["w"], B[sec]["w"]) is None else R(A[sec]["w"], B[sec]["w"]) - su),
                f(R(A[sec]["nh"], B[sec]["nh"])), f(R(A[sec]["nu"], B[sec]["nu"])), f(R(A[sec]["ov"], B[sec]["ov"]))))
            for k, lab in enumerate(("n ", "nb", "e ")):
                print("       left vectors (light, middle, heavy) on %s: %s" % (lab, " ".join(f(R(A[sec]["Ub"][k][c], B[sec]["Ub"][k][c])) for c in range(3))))
        print("  |V| rates:", [[f(R(A["V"][i, j], B["V"][i, j])) for j in range(3)] for i in range(3)])
