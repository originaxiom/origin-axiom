#!/usr/bin/env python3
"""B1530 -- Part A: B1515's frame at the kappa = 1 members of one state, by route E (exact) and route N (60 digits).

    python3 run_a.py                 the sealed run: m135 = -LLRR, its eight characters at kappa = 1 -> run_a.json, run_a_log.txt
    python3 run_a.py --dry-run       the banked dry run (before the seal): M6 = +(LR)^6 at u = (1/8, 1/2) and (0, 0), lam = 1,
                                     sm:B1515's members -> dry_run_a.json (not a reading of m135)

At each character nu (kappa = nu(t') = 1): V = nu (x) rho, L = nu^-4, V_eta = nu^5 (x) rho, V (x) L = nu^-3 (x) rho.  A member is a
class c != 0 in H^1(V_eta); W1 = [[V, c L], [0, L]], and W2 is read through W2* = [[V*, c' L^-1], [0, L^-1]], c' in H^1(V_eta*),
with I(W2) = -I(W2*) and I(Lambda^2 W2) = -I(Lambda^2 W2*).  Classes read:
  - h^1(V_eta) = 1: the class;
  - h^1(V_eta) >= 2 (one interior class c_int): c_int, a boundary-type class c_b, c_b + c_int, c_b - c_int, c_b + 2 c_int,
    and c'_int, c'_b, c'_b + c'_int in W2*.
Route N reads at the same classes: route E's exact cocycles carried to route N's frame by the conjugator X (X rho_E X^-1 =
rho_N on a, b, t; X^-T for the duals), and also at route N's own numerical interior class.  The routes are compared class by
class.
The mechanism, route E only (PREREGISTRATION section 3):
  - Lemma A/C: x cup c = 0 (the fibre test), and the Jordan type of S0 on C at 1;
  - Lemma B: mu (the lift of c_int, restricted to P) against Lambda_A;
  - Lemma 8 / D: bit = [e ^ c|_P in Lambda_A] at boundary-type classes."""
import json
import sys
import time
import warnings
from fractions import Fraction as Fr
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402

import exact_lib as E  # noqa: E402
import exact_states as S  # noqa: E402
import route_n as N  # noqa: E402

LOG = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    LOG.append(s)


def pair(r):
    return [r["I(W)"], r["I(L2W)"]]


# ============================================================================================ route E at one character
def route_e(G, img, sign, rho, u):
    ch = S.nu(sign, u, 0)
    V = rho.twist(ch)
    Lc = S.power_char(ch, -4)
    trivial_L = all(v == E.ONE for v in Lc.values())
    L = None if trivial_L else E.line(G.gens, Lc)
    Veta = rho.twist(S.power_char(ch, 5))
    VL = rho.twist(S.power_char(ch, -3))
    CV, CE, CQ = E.Cohomology(G, V), E.Cohomology(G, Veta), E.Cohomology(G, VL)
    row = {"u": [str(x) for x in u], "case": "(a)" if trivial_L else "(b)",
           "h1": {"V": CV.h1, "V_eta": CE.h1, "V (x) L": CQ.h1}, "n": {"V": CV.n, "V_eta": CE.n, "V (x) L": CQ.n},
           "simple": CV.h1 == CE.h1 == CQ.h1 == 1, "W1": {}, "W2": {}}
    ints = CE.interior()
    classes = {}
    if CE.h1 == 1:
        classes["the class"] = CE.reps[0]
    else:
        assert len(ints) == 1, "more than one interior class: not covered by this run's class list"
        c_int = CE.combine(ints[0])
        c_b = next(z for z in CE.reps if E.rank_vectors(CE.Bvecs + [c_int, z], CE.d * CE.ng) == CE.dimB + 2)

        def lin(x, y):
            return [E.K.of(x) * p + E.K.of(y) * q for p, q in zip(c_b, c_int)]
        classes = {"c_int": c_int, "c_b": c_b, "c_b + c_int": lin(1, 1), "c_b - c_int": lin(1, -1), "c_b + 2 c_int": lin(1, 2)}
    for name, c in classes.items():
        W1 = E.extension(V, c, L)
        assert W1.check(G.rels)
        a, b = E.class_index(G, W1), E.class_index(G, W1.wedge2())
        row["W1"][name] = {"I(W)": a["I"], "I(L2W)": b["I"], "W1": a, "L2W1": b,
                           "c|P is a coboundary": CE.coboundary_on_P(c) is not None}
    # W2* at the dual classes
    Vd = V.dual()
    Linv = None if trivial_L else E.line(G.gens, S.power_char(ch, 4))
    CEd = E.Cohomology(G, Veta.dual())
    if CEd.h1 == 1:
        dclasses = {"the class": CEd.reps[0]}
    else:
        dints = CEd.interior()
        cd_int = CEd.combine(dints[0])
        cd_b = next(z for z in CEd.reps if E.rank_vectors(CEd.Bvecs + [cd_int, z], CEd.d * CEd.ng) == CEd.dimB + 2)
        dclasses = {"c'_int": cd_int, "c'_b": cd_b, "c'_b + c'_int": [p + q for p, q in zip(cd_b, cd_int)]}
    for name, c in dclasses.items():
        W2s = E.extension(Vd, c, Linv)
        assert W2s.check(G.rels)
        a, b = E.class_index(G, W2s), E.class_index(G, W2s.wedge2())
        row["W2"][name] = {"I(W)": -a["I"], "I(L2W)": -b["I"]}
    # the mechanism
    FL = S.family()
    phi_p, tp = S.phi_prime(sign, img), S.tprime(sign)
    mech = {}
    Q, coords = E.fibre_C(V, phi_p, tp)
    mech["Jordan type of S0 on C at 1"] = E.jordan_partition(Q, 1)
    mech["chi_C (highest first)"] = [str(x) for x in E.charpoly(Q)]
    if trivial_L:
        for name, c in classes.items():
            if name in ("c_int", "c_b", "the class"):
                mech[f"x cup {name} = 0"] = E.cup_with_fibration_class_vanishes(V, c, phi_p, tp)[0]
    if "c_int" in classes:
        in_lamA, dimLamA, is_cob, lifts = E.mu_test(G, V, classes["c_int"], L, None if trivial_L else
                                                    CQ.combine(CQ.interior()[0]))
        mech["mu (the lift of c_int) in Lambda_A"] = in_lamA
        mech["dim Lambda_A"] = dimLamA
        mech["mu a P-coboundary"] = is_cob
        mech["c_int lifts"] = lifts
    # bit at a boundary-type class: e ^ c|_P against Lambda_A
    bname = "c_b" if "c_b" in classes else "the class"
    c = classes[bname]
    if CE.coboundary_on_P(c) is None:
        CL2 = E.Cohomology(G, V.wedge2())
        e = E.nullspace(sum((E.madd(P, E.eye(4), -1) for P in CV.Pm), []), 4)
        assert len(e) == 1
        cP = CE.restrict(c)
        ewc = E.wedge_vec(e[0], cP[:4]) + E.wedge_vec(e[0], cP[4:])
        LamA = [CL2.restrict(z) for z in CL2.Z]
        mech[f"bit at {bname}: e ^ c|_P in Lambda_A"] = E.in_span(ewc, CL2.BP + LamA, 2 * CL2.d)
    row["mechanism (route E)"] = mech
    return row, classes, dclasses


# ============================================================================================ route N at one character
def conjugator(rhoE, matsN):
    """X with X rho_E(g) X^-1 = rho_N(g) for g = a, b, t (the four, no character): the frames of the two routes"""
    rows = []
    for g in "abt":
        A = mp.matrix([[x.num(mp) for x in r] for r in rhoE.M[g]])
        B = matsN[g]
        # X A - B X = 0, vec(X) row-major: (X A)_{ij} = sum_k X_ik A_kj; (B X)_{ij} = sum_k B_ik X_kj
        for i in range(4):
            for j in range(4):
                row = [mp.mpc(0)] * 16
                for k in range(4):
                    row[i * 4 + k] += A[k, j]
                    row[k * 4 + j] -= B[i, k]
                rows.append(row)
    M = mp.matrix(rows)
    U, Sv, Vh = mp.svd_c(M, full_matrices=True)
    s = sorted([abs(Sv[k]) for k in range(16)], reverse=True)
    assert s[-1] < mp.mpf(10) ** -40 * s[0] and s[-2] > mp.mpf(10) ** -20 * s[0], ("conjugator", s[-2:])
    x = [mp.conj(Vh[15, k]) for k in range(16)]
    X = mp.matrix(4, 4)
    for i in range(4):
        for j in range(4):
            X[i, j] = x[i * 4 + j]
    return X, {"smallest singular value (rel)": mp.nstr(s[-1] / s[0], 3), "next (rel)": mp.nstr(s[-2] / s[0], 3)}


def transport(c, X, gens):
    """a cocycle's generator values (exact, route E's frame) carried to route N's frame by X, as one column"""
    d = X.rows
    out = mp.matrix(d * len(gens), 1)
    for gi in range(len(gens)):
        v = mp.matrix([[c[gi * d + i].num(mp)] for i in range(d)])
        w = X * v
        for i in range(d):
            out[gi * d + i, 0] = w[i, 0]
    return out


def route_n(G, sign, mats, u, X, classes, dclasses):
    ch = N.char_values(sign, u, 0)
    V = N.module(mats, ch)
    lval = N.char_power(ch, -4)
    trivial_L = all(abs(v - 1) < mp.mpf(10) ** -40 for v in lval.values())
    Veta = N.module(mats, N.char_power(ch, 5))
    C = N.Classes(G, Veta)
    ints = C.interior()
    row = {"u": [str(x) for x in u], "h1(V_eta)": C.h1, "interior": ints.cols, "W1": {}, "W2": {}}
    # route E's classes carried over, and route N's own interior class
    zs = {name: transport(c, X, G.gens) for name, c in classes.items()}
    if ints.cols:
        zs["route N's own interior class"] = ints[:, 0]
    for name, z in zs.items():
        W1 = N.extension(V, z, G.gens, None if trivial_L else lval)
        r = N.reading(G, W1)
        row["W1"][name] = {"I(W)": r["I(W)"], "I(L2W)": r["I(L2W)"], "checks": r["checks"], "margins": r["margins"],
                           "relator residual": r["relator residual"]}
    # W2* = [[V*, c' L^-1], [0, L^-1]]: the dual frames are related by X^-T
    L = N.lib()
    Vd = L.Module({g: mp.inverse(V.M[g]).T for g in "abt"})
    Xd = mp.inverse(X).T
    linv = N.char_power(ch, 4)
    for name, c in dclasses.items():
        W2s = N.extension(Vd, transport(c, Xd, G.gens), G.gens, None if trivial_L else linv)
        r = N.reading(G, W2s)
        row["W2"][name] = {"I(W)": -r["I(W)"], "I(L2W)": -r["I(L2W)"], "checks": r["checks"]}
    row["margins (classes)"] = C.mg.as_dict()
    return row


def run(sign, word, level, chars_subset, out_name, holonomy):
    t0 = time.time()
    G, img, chars, D = S.group(sign, word * level if level > 1 else word)
    if holonomy == "m135":
        rho = S.four_module(S.m135_sl2())
    else:
        rho = S.four_module(S.power_t(S.eisenstein_sl2(sign, word), level))
    assert rho.check(G.rels)
    mats = N.four_mats(sign, word, level=level)
    X, xinfo = conjugator(rho, mats)
    todo = chars_subset if chars_subset is not None else chars
    out = {"state": sign + word * level if level > 1 else sign + word, "D": D, "characters": len(todo),
           "the frames' conjugator": xinfo, "rows": []}
    say(f"Part A on {out['state']}: {len(todo)} characters at kappa = 1, routes E and N")
    for u in todo:
        t1 = time.time()
        re_, classes, dclasses = route_e(G, img, sign, rho, u)
        rn_ = route_n(G, sign, mats, u, X, classes, dclasses)
        # the routes compared class by class (route E's classes carried to route N's frame)
        cmp_ = {("W1", k): pair(re_["W1"][k]) == pair(rn_["W1"][k]) for k in classes}
        cmp_.update({("W2", k): pair(re_["W2"][k]) == pair(rn_["W2"][k]) for k in dclasses})
        cmp_[("classes", "interior dimension of H^1(V_eta)")] = rn_["interior"] == re_["n"]["V_eta"]
        if "c_int" in classes:
            cmp_[("W1", "route N's own interior class")] = (pair(rn_["W1"]["route N's own interior class"])
                                                            == pair(re_["W1"]["c_int"]))
        cmp_ = {f"{a}: {b}": v for (a, b), v in cmp_.items()}
        row = {"u": re_["u"], "route E": re_, "route N": rn_, "routes agree": all(cmp_.values()), "comparison": cmp_,
               "seconds": round(time.time() - t1)}
        out["rows"].append(row)
        w1 = {k: pair(v) for k, v in re_["W1"].items()}
        w2 = {k: pair(v) for k, v in re_["W2"].items()}
        say(f"  u = {tuple(re_['u'])}: case {re_['case']}, h1 {re_['h1']}, simple {re_['simple']}; W1 {w1}; W2 {w2}; "
            f"route N W1 {({k: pair(v) for k, v in rn_['W1'].items()})}; routes agree {row['routes agree']}; "
            f"mechanism {re_['mechanism (route E)']} ({row['seconds']} s)")
    out["routes agree everywhere"] = all(r["routes agree"] for r in out["rows"])
    out["seconds"] = round(time.time() - t0)
    (HERE / out_name).write_text(json.dumps(out, indent=1, default=str))
    say(f"routes agree everywhere: {out['routes agree everywhere']} ({out['seconds']} s)")
    return out


def main():
    if "--dry-run" in sys.argv:
        run("+", "LR", 6, [(Fr(1, 8), Fr(1, 2)), (Fr(0), Fr(0))], "dry_run_a.json", "m004")
        (HERE / "dry_run_a_log.txt").write_text("\n".join(LOG) + "\n")
        return
    run("-", "LLRR", 1, None, "run_a.json", "m135")
    (HERE / "run_a_log.txt").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
