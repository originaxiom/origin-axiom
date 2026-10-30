"""compare the referee's independent forms with the draft's model at three points"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(1, str(HERE / "rerun"))
import mpmath as mp
import ref_model as rm
import model as dm
mp.mp.dps = 30
for tau in (mp.mpc("0.17", "1.23"), mp.mpc("-0.43", "0.95"), mp.mpc("0.5", "2.6")):
    fv = dm.mp_form_values(tau)
    th, dth, ddth, E4, E6, ae = fv
    t2, t3, t4 = rm.thetas(tau); E2, E4r, E6r = rm.eisenstein(tau); et = rm.eta(tau)
    print("tau", tau)
    print("  E4 dev", mp.nstr(abs(E4r - E4) / abs(E4), 3), " E6 dev", mp.nstr(abs(E6r - E6) / abs(E6), 3),
          " |eta| dev", mp.nstr(abs(abs(et) - ae) / ae, 3), " eta^3 vs th2th3th4/2", mp.nstr(abs(et ** 3 - t2 * t3 * t4 / 2) / abs(et ** 3), 3))
    for kind, a in (("F", 2), ("F", 6), ("F", -2), ("F", 18), ("DR", None), ("A0", None)):
        T = dm.Triplet(kind, a)
        vec, fac = dm.mp_triplet(T, fv)
        dr = [fac * c for c in vec]                 # draft: |eta|^(3-a) x theta vector (F) ; vector / |2 eta^3| (DR)
        if kind == "F":
            mine = rm.Fvec(a, tau, et)
            # the draft uses |eta|, so compare moduli of every component and the projective class
            dev = max(abs(abs(x) - abs(y)) / abs(y) for x, y in zip(mine, dr))
        elif kind == "DR":
            mine = rm.DRvec(tau)
            # the draft's DR = (DV - E2 V/12) / |2 eta^3|: equal to the holomorphic DR up to the phase of 2 eta^3
            ph = (t2 * t3 * t4) / abs(t2 * t3 * t4)
            dev = max(abs(x * ph - y) / abs(y) for x, y in zip(mine, dr))
        else:
            continue
        print("  %s %s component-modulus dev %s" % (kind, a, mp.nstr(dev, 3)))
