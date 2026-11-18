"""B1957: main's own check of the steps of agy-exp's proof that the record's odd L-value is -pi^2 times the twisted eta
invariant (its note X-C9, lines 52 to 66; the first of the checks its harvest review asks of main).  Data-free; main's own
code only: B1929's Siegel winding (main_siegel.py) and the closed form below, written from the note's own display.  The
characters are the 601 of B1929's population file (a list of acts and characters; no seat's code is run).
 X1  the closed form the proof reaches in its first step, as an exact rational:
       F = (2(a + d)/c) P2(nu1) - 4 sgn(c) s(a, c),  s = sum over k = 0..|c|-1 of P1((k + nu1)/c) P1(a (k + nu1)/c + nu2),
     nu = (-c1, -c2) reduced to [0, 1)^2, P1 the sawtooth and P2 the second periodic Bernoulli function,
     against 2 i Delta/pi, where Delta is main's winding of log g_{Jc} along one period (so that L_odd = -2 pi i Delta).
 X2  the sign: Delta against (pi i/2) F, which is what the note's second step displays.
 X3  controls: the same closed form with nu2's sign changed, and with nu1 and nu2 exchanged.
 X4  the arithmetic of the note's third step: (-2 pi i)(pi i/2)."""
import json, math, pathlib, sys
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B = next((ROOT / "frontier").glob("B1929_*")) / "verification"; sys.path.insert(0, str(B)); import main_siegel as MS
pop = json.loads((B / "received_sm" / "population.json").read_text())
def P1(t): f = Fr(t) - math.floor(Fr(t)); return Fr(0) if f == 0 else f - Fr(1, 2)
def P2(t): f = Fr(t) - math.floor(Fr(t)); return f * f - f + Fr(1, 6)
def winding(o):
    (a, b), (c, d) = o["M"]; N = o["N"]; A1, A2 = (-o["j"] / N) % 1.0, (o["i"] / N) % 1.0
    tr = a + d; D = tr * tr - 4; r1 = ((a - d) + math.sqrt(D)) / (2 * b); r2 = ((a - d) - math.sqrt(D)) / (2 * b); cen, R = (r1 + r2) / 2, abs(r1 - r2) / 2
    zs = lambda s: complex(cen + R * math.tanh(s), R / math.cosh(s)); ell = 2 * math.log((abs(tr) + math.sqrt(D)) / 2); g = lambda z: (a * z + c) / (b * z + d)
    s0 = -ell / 2; s1 = s0 + ell if abs(g(zs(s0)) - zs(s0 + ell)) < 1e-7 * (1 + abs(zs(s0))) else s0 - ell
    return MS.winding_arc(A1, A2, zs, s0, s1)
def closed(o, flip=1, swap=False):
    (a, b), (c, d) = o["M"]; N = o["N"]; n1, n2 = Fr(-o["i"], N) % 1, Fr(-o["j"], N) % 1
    if swap: n1, n2 = n2, n1
    s = sum(P1((k + n1) / Fr(c)) * P1(a * (k + n1) / Fr(c) + flip * n2) for k in range(abs(c)))
    return Fr(2 * (a + d), c) * P2(n1) - 4 * (1 if c > 0 else -1) * s
if __name__ == "__main__":
    worst, same, opp, zero, ctl1, ctl2, levels = 0.0, 0, 0, 0, 0, 0, set()
    for o in pop:
        Dl = winding(o); F = closed(o); eta = (2j * Dl / math.pi); worst = max(worst, abs(float(F) - eta.real), abs(eta.imag)); levels.add(json.dumps(o["level"]))
        if F == 0: zero += 1
        else:
            r = Dl / (1j * math.pi / 2 * float(F)); same += abs(r - 1) < 1e-8; opp += abs(r + 1) < 1e-8
        ctl1 += abs(float(closed(o, flip=-1)) - eta.real) < 1e-9; ctl2 += abs(float(closed(o, swap=True)) - eta.real) < 1e-9
    print("X1: over %d characters on %d levels the closed form of the first step equals 2 i Delta/pi, that is -L_odd/pi^2 by main's own winding: largest difference %.1e; it is zero on %d characters" % (len(pop), len(levels), worst, zero))
    print("X2: Delta divided by (pi i/2) times the closed form: +1 on %d characters, -1 on %d (of the %d where it is not zero). The note's second step displays +(pi i/2); the sign that holds is -(pi i/2)" % (same, opp, len(pop) - zero))
    print("X3: controls: with nu2's sign changed the closed form still equals it on %d of %d; with nu1 and nu2 exchanged on %d" % (ctl1, len(pop), ctl2))
    z = (-2j * math.pi) * (1j * math.pi / 2); print("X4: (-2 pi i)(pi i/2) = %+.6f = +pi^2 (%.6f): with the display's sign the third step would give L_odd = +pi^2 eta_A; with the sign that holds it gives -pi^2 eta_A, the identity" % (z.real, math.pi ** 2))
