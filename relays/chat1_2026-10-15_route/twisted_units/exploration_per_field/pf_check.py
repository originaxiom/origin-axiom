"""chat1: the per-field reading in factored form against the SM seat's W92 (series form), at excluded orders only;
and the closure law with the Higgs conjugated (c (qL^2 + qR^2 - qH^2) = 0 mod N) on a thread where c is a unit."""
import sys, importlib.util, pickle, time
import mpmath as mp, flint
from flint import arb, acb
sys.path.insert(0, sys.argv[1]); import units_cells as UC
spec = importlib.util.spec_from_file_location("w92", sys.argv[2]); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)
P = pickle.load(open(sys.argv[3], "rb"))
t0 = time.time()
flint.ctx.prec = 800
mine = UC.PerFieldFactoredSource(P)
theirs = W.PerFieldSource(P, UC)
flint.ctx.prec = 300; mp.mp.dps = 60
worst = 0.0; n = 0
for N, line, q in ((5, (0, 1), 2), (5, (1, 2), -4), (7, (1, 3), 6), (3, (1, 1), 1)):
    for weight in ("3/2", "-1/2", "7/2"):
        S_theirs = theirs.units("x", weight, q, line, N)
        S_mine = mine.units("x", weight, q, line, N)
        for t in (mp.mpc("0.17", "1.02"), mp.mpc("-0.4", "1.6")):
            tA = acb(arb(mp.nstr(t.real, 50)), arb(mp.nstr(t.imag, 50)))
            exps = set().union(*[set(s) for s in S_theirs + S_mine])
            pw = {e: (2 * acb.pi() * acb(0, 1) * tA * arb(e.numerator) / e.denominator).exp() for e in exps}
            D = mine.dress(tA, q, line, N)
            for Xs, Xm in zip(S_theirs, S_mine):
                a = UC.ev(Xs, pw); b = UC.ev(Xm, pw)
                b = [b[c] * D[c] for c in range(3)]
                sc = max(float(abs(x).mid()) for x in a)
                worst = max(worst, max(float(abs(a[c] - b[c]).mid()) for c in range(3)) / sc); n += 1
print(f"factored dressing against W92's dressed series: {n} unit evaluations, worst relative {worst:.1e}")
# closure with the Higgs conjugated, on L R^3 at N = 3 (line (0, 1): c = -1 is a unit): sums qL^2 + qR^2 - qH^2
for name, src in (("per-field", mine), ("minimal", UC.UntwistedSource(P))):
    r = UC.configuration(src, 3, (0, 1), 3, UC.SM, 128)
    print(name, "closure on L R^3, N = 3:", {s: f"{v:.1e}" for s, v in r["closure"].items()})
print("SM sums qL^2+qR^2-qH^2:", {s: (UC.SM[l]**2 + UC.SM[r]**2 - UC.SM["H"]**2) for s, (l, r, h) in UC.SECTORS.items()},
      " qL^2+qR^2:", {s: (UC.SM[l]**2 + UC.SM[r]**2) for s, (l, r, h) in UC.SECTORS.items()})
print("seconds", round(time.time() - t0, 1))
