#!/usr/bin/env python3
"""B1483 cell C1: the elliptic curve at the end of the frame space.

For a cusped hyperbolic M with a spin structure s (an SL(2,C) lift rho_s, Gamma_s its image) the frame space is
X_s = Gamma_s \\ SL(2,C).  At a cusp the peripheral group P_s sits in B = +-N (N the unipotent upper-triangular group,
N = C), and  P_s \\ SL(2,C) -> B \\ SL(2,C) = (C^2 - 0)/+-1  is a principal bundle with fibre  B / P_s = C / ker(sigma_s),
where sigma_s = tr rho_s / 2 : P -> {+-1} is the peripheral sign character and P = Lambda is the cusp's lattice.
So the end of X_s is fibred by the elliptic curve  E_s = C / ker(sigma_s)  (E = C / Lambda itself when sigma_s is trivial).

With L the rational longitude, Mu a dual class and z = Mu / L the cusp shape:
    sigma = (sigma(L), sigma(Mu)) = (+,+): tau = z      (-,+): tau = z/2      (-,-): tau = (z+1)/2      (+,-): tau = 2z.
A mirror conjugates the lattice; j(E_s) real  <=>  E_s is isomorphic to its conjugate curve."""
import sys, json, pathlib, multiprocessing, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent; FR = next(p for p in HERE.parents if p.name == "frontier")
sys.path.insert(0, str(FR / "B1477_what_decides_the_swap_the_mirrors_shear_on_the_cusp" / "verification"))


def reduce_tau(t):
    """to the standard fundamental domain (|Re| <= 1/2, |tau| >= 1), tau in the upper half-plane"""
    from mpmath import mpc, floor, mpf
    t = mpc(t)
    if t.imag < 0: t = -t
    for _ in range(10000):
        t = mpc(t.real - floor(t.real + mpf(1) / 2), t.imag)
        if abs(t) < 1 - mpf(10) ** -30: t = -1 / t
        else: break
    return t


def j_of(tau):
    from mpmath import kleinj
    return 1728 * kleinj(reduce_tau(tau))


def one(name):
    import cusp_shear as CSH
    from mpmath import mp, mpc
    mp.dps = 30
    out = dict(name=name)
    try:
        sh = CSH.shear(name); z = mpc(sh["shape"][0], sh["shape"][1]); out["shape"] = sh["shape"]; out["two_re"] = sh["two_re"]
        g = CSH.longitude_signs(name); out["h1"] = g["h1"]; rows = []
        for r in g["rows"]:
            sL = 1 if r["tr_L"] > 0 else -1; sM = 1 if r["tr_Mu"] > 0 else -1
            tau = {(1, 1): z, (-1, 1): z / 2, (-1, -1): (z + 1) / 2, (1, -1): 2 * z}[(sL, sM)]
            j = j_of(tau); t = reduce_tau(tau)
            rows.append(dict(chi=r["chi"], sigma=[sL, sM], tau=[float(t.real), float(t.imag)], j=[float(j.real), float(j.imag)],
                             j_real=bool(abs(j.imag) < 1e-9 * max(1.0, abs(j)))))
        out["rows"] = rows
    except Exception as e:
        out["error"] = repr(e)[:160]
    return out


def classes(r):
    """the distinct end curves of a state, by sigma: {sigma: (j, real?, number of spin structures)}"""
    d = {}
    for row in r["rows"]:
        k = tuple(row["sigma"]); d.setdefault(k, dict(j=row["j"], j_real=row["j_real"], n=0)); d[k]["n"] += 1
    return d


def conj_pair(a, b, tol=1e-7):
    s = max(1.0, abs(complex(*a)))
    return abs(a[0] - b[0]) < tol * s and abs(a[1] + b[1]) < tol * s


if __name__ == "__main__":
    S = json.load(open(FR / "B1479_the_bit_is_the_sign_of_the_word_state" / "verification" / "sign_law.json"))["rows"]
    names = [r["name"] for r in S if r["amphichiral"]] if len(sys.argv) < 2 or sys.argv[1] == "all" else sys.argv[1:]
    with multiprocessing.Pool(5) as pool: res = pool.map(one, names, chunksize=2)
    summ = dict(states=len(res), errors={r["name"]: r["error"] for r in res if "error" in r})
    for sg, key in (("b++", "plus"), ("b+-", "minus")):
        rs = [r for r in res if r["name"].startswith(sg) and "rows" in r]; cl = {r["name"]: classes(r) for r in rs}
        d = dict(states=len(rs), spin_structures=sum(len(r["rows"]) for r in rs),
                 sigma_patterns=sorted({str(sorted(c)) for c in cl.values()}),
                 all_L_minus=sum(1 for r in rs if all(row["sigma"][0] == -1 for row in r["rows"])),
                 states_all_j_real=sum(1 for c in cl.values() if all(v["j_real"] for v in c.values())),
                 states_no_j_real=sum(1 for c in cl.values() if not any(v["j_real"] for v in c.values())))
        pr = [n for n, c in cl.items() if set(c) == {(-1, 1), (-1, -1)} and conj_pair(c[(-1, 1)]["j"], c[(-1, -1)]["j"])]
        d["two_classes_with_conjugate_j"] = len(pr)
        d["conjugate_and_not_real"] = sorted(n for n in pr if not cl[n][(-1, 1)]["j_real"]); d["conjugate_and_real"] = sorted(n for n in pr if cl[n][(-1, 1)]["j_real"])
        summ[key] = d
    json.dump(dict(summary=summ, states={r["name"]: r for r in res}), open(HERE / "end_curve.json", "w"), indent=0); print(json.dumps(summ)[:2200])
