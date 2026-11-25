"""B1982 correction, second part (main, 2026-11-25; data-free): B1980's duality family tau -> -K/tau (K != 1) rerun with the
end evaluated covariantly at every tau: L(tau) = L_2(tau_FD) + 1/2 log(Im tau_FD / Im tau), which is B1921's invariant
L-tilde read at the fundamental-domain point and returned to tau (for SL(2, Z) moves it is the record's law L + log|tau|).
Heights above 6 still read the table's value at 6 (the clamp on record). Plain matching as in B1980.
    python3 -B fricke_endlaw.py > fricke_endlaw_run.txt"""
import sys, pathlib, math, time
from multiprocessing import Pool
sys.path.insert(0, str(next((pathlib.Path(__file__).resolve().parents[2]).glob("B1980_*")) / "verification"))
import duality_cov as D
def L_law(y):
    t = D.fd("0", y); return D.FM.CR.canon(t)["L_2"] + 0.5 * math.log(t.imag / y)
if __name__ == "__main__":
    t0 = time.time(); res = {}
    print("check: L_law(0.4) - L_law(2.5) = %.12f, log 2.5 = %.12f" % (L_law(0.4) - L_law(2.5), math.log(2.5)), flush=True)
    with Pool(6) as pool:
        for K in D.KS:
            r = []
            for f in (1.5, 2.5):
                y = f * math.sqrt(K); yp = K / y
                src = dict(zip(D.P96, pool.map(D.outputs, [("0", y, a, b, L_law(y)) for (a, b) in D.P96], chunksize=8)))
                par = dict(zip(D.E30, pool.map(D.outputs, [("0", yp, a, b, L_law(yp)) for (a, b) in D.E30], chunksize=8)))
                big, med = D.match(src, par); r.append(big)
                print("K = %d, the end law: height %.4f against %.4f: largest d %.1e, median %.1e  [%.0f s]" % (K, y, yp, big, med, time.time() - t0), flush=True)
            res[K] = r
    print("SUMMARY F-law: K != 1 passing with the end law: %s" % [K for K in D.KS if all(x < 1e-8 for x in res[K])])
    print("SUMMARY least largest-d over K: %s" % sorted((round(min(res[K]), 4), K) for K in D.KS)[:3])
