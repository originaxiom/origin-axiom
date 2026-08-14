"""B922: banking-seat spot checks on the received lambda_2."""
import mpmath as mp

R_STR = "4.9000853730625213014795758"


def arithmetic_identity():
    mp.mp.dps = 40
    r = mp.mpf(R_STR)
    return 1 + r**2


def spot_pslq():
    mp.mp.dps = 26
    r = mp.mpf(R_STR); lam = 1 + r**2
    consts = {
        "BTZ": mp.log((5 + mp.sqrt(21))/2),
        "Vol": mp.mpf("2.029883212819307250042405108549"),
        "pi2": mp.pi**2, "zeta3": mp.zeta(3),
        "logphi": mp.log((1 + mp.sqrt(5))/2), "sqrt21": mp.sqrt(21),
    }
    hits = []
    for name_t, t in (("r", r), ("lambda", lam)):
        for name_c, c in consts.items():
            rel = mp.pslq([t, c, mp.mpf(1)], maxcoeff=10**4, maxsteps=10**4)
            if rel:
                hits.append((name_t, name_c, rel))
    return hits


if __name__ == "__main__":
    print("lambda =", mp.nstr(arithmetic_identity(), 27))
    print("spot hits:", spot_pslq())
