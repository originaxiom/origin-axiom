"""Attack 5: B1691's q-series (truncated at x^240, x = q^(1/8)) against this referee's direct sums near tau = i, for
R, dR, d2R and a weight-43/2 section's f2 = E6^3 d2R term (the largest weight the draft uses).  Also the largest
|coefficient| x |x|^k in the top 40 powers (the region products with x^-1 leading terms corrupt)."""
import sys, pathlib, json
from fractions import Fraction as F
import mpmath as mp
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"))
from qseries import S, theta2, theta3, E2, E4, E6, serre
from refkit import basis
mp.mp.dps = 50
th2, th3, th4 = theta2(), theta3(1), theta3(-1)
den = (th2 * th3 * th4).inv()
R = [-(th2 * th2) * den, -(th4 * th4) * den, (th3 * th3) * S.c(0, 1) * den]
e2 = E2(); dR = [serre(c, F(-1, 2), e2) for c in R]; d2R = [serre(c, F(3, 2), e2) for c in dR]
e6 = E6(); f2 = e6 * e6 * e6
def ev(s, tau):
    x = mp.exp(2j * mp.pi * tau / 8)
    return mp.fsum(mp.mpc(mp.mpf(p.numerator) / p.denominator, mp.mpf(q.numerator) / q.denominator) * x ** k for k, (p, q) in s.d.items())
def top(s, tau):
    x = abs(mp.exp(2j * mp.pi * tau / 8))
    return max([abs(mp.mpf(p.numerator) / p.denominator) * x ** k for k, (p, q) in s.d.items() if k > 200] + [mp.mpf(0)])
out = {}
for tau in (mp.mpc(0, 1) + mp.mpf("1e-3") * mp.exp(0.3j), mp.mpc(0, 1)):
    Rr, dRr, d2Rr, eta6, *_ = basis(tau)
    rel = lambda A, B: max(abs(ev(a, tau) - b) / abs(b) for a, b in zip(A, B))
    t = f2 * d2R[0]
    out[mp.nstr(tau, 6)] = {"R": mp.nstr(rel(R, Rr), 3), "dR": mp.nstr(rel(dR, dRr), 3), "d2R": mp.nstr(rel(d2R, d2Rr), 3),
                           "max top-40 term of E6^3 d2R_1": mp.nstr(top(t, tau), 3)}
print(json.dumps(out, indent=1)); pathlib.Path(__file__).resolve().parent.joinpath("ref_truncation.json").write_text(json.dumps(out, indent=1))
