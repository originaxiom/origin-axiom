"""B1515 -- post-run checks (after both sealed routes; not predictions).  python3 post_run_checks.py --record -> post_run_checks_run.txt

The census found, by both routes, 24 members on M6 (order-8 characters, four deck orbits, lam = 1) with h^1(V) = h^1(V_eta) =
h^1(V (x) L) = 2 and (I(W1), I(Lambda^2 W1)) = (+1, -1) at every class read with c|_P != 0, and (0, -1) at the interior class
(route L's first basis class).  These checks are run before anything is banked:

  (a) exactness: each of the four orbit representatives read EXACTLY over Q(zeta_8) = Q(sqrt 2, i) at q = 1, with route T's library
      (tower_lib.index asserts the annihilator and B1297 identities): h^1 of V, V_eta, V (x) L; W1 and Lambda^2 W1 at a boundary-type
      class (the fixed combination) and at the interior class c_int (c_int|_P = 0, solved for explicitly); W2 and Lambda^2 W2.  For
      contrast, one simple order-8 member (1, 0) exactly.
  (b) where M6's interior classes are: n(chi (x) rho_1) for all 320 characters at lam = 1, from both routes' records, compared.
  (c) the Lambda^2 count at a 'both' member (mod p): r1(Lambda^2 W1) = 4 split as Lambda_A's image (2) + the lift of the boundary
      class of V (x) L (1) + the lift of its interior class (1); s0 = 3; so I = 3 - 4 = -1.  And Lambda_A meets pi_A in 0 there too.
  (d) a third method for the interior classes (Wang): h^1(M_6; nu (x) rho_1) = dim ker(S^(6)_nu - 1) on H^1(F; nu_F (x) rho_1), from
      B1511's twisted fibre monodromy at q = 1, for every character of M_6 at one prime; it must equal both routes' h^1(V)."""
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import route_t as RT  # noqa: E402

T = RT.T
RECORD = HERE / "post_run_checks_run.txt"
K8 = sp.QQ.algebraic_field(sp.sqrt(2), sp.I)
BOTH_REPS = [(5, 20), (5, 25), (5, 35), (10, 15)]          # mod 40: the four deck orbits of the 24 (census_t_run.txt)


class ExactK8:
    """route T's modules on M6 over Q(zeta_8) at q = 1"""

    def __init__(self):
        self.lev = RT.Level(6)
        m1 = {k: v.subs(T.Q, 1) for k, v in T.symbolic_mats().items()}
        self.rho = {g: self.dm(T.word_matrix(m1, self.lev.cov["words"][g])) for g in self.lev.cov["gens"]}

    @staticmethod
    def dm(M):
        return DomainMatrix([[K8.from_sympy(sp.nsimplify(M[i, j])) for j in range(M.shape[1])] for i in range(M.shape[0])], M.shape, K8)

    @staticmethod
    def unit(e):
        ang = 2 * sp.pi * sp.Rational(e % 120, 120)
        val = sp.nsimplify(sp.cos(ang)) + sp.I * sp.nsimplify(sp.sin(ang))
        return K8.from_sympy(val)

    def twisted(self, ex, power):
        return T.DMRep(self.lev.cov["gens"], {g: self.rho[g] * self.unit(power * ex[g]) for g in self.lev.cov["gens"]})

    def line(self, ex, power):
        return T.DMRep(self.lev.cov["gens"], {g: DomainMatrix([[self.unit(power * ex[g])]], (1, 1), K8) for g in self.lev.cov["gens"]})


def brief(d):
    return {"I": d["I"], "(a0,a1,t0,r1)": [d["a0"], d["a1"], d["t0"], d["r1"]], "(b0,b1,s0,q1)": [d["b0"], d["b1"], d["s0"], d["q1"]]}


def interior_class(lev, rep, cls):
    """the class of H^1(rep) (as a combination of cls) whose restriction to P is a peripheral coboundary; None if there is none"""
    BP = RT.peripheral_coboundaries(rep, lev)
    res = [RT.restrict(rep, c, lev.mu).vstack(RT.restrict(rep, c, lev.lam)) for c in cls]
    M = res[0].hstack(*res[1:], BP)
    null = T.dm_nullspace(M)
    for v in null:
        coeffs = [v[i, 0].element for i in range(len(cls))]
        if any(x != K8.zero for x in coeffs):
            c = cls[0] * coeffs[0]
            for k in range(1, len(cls)):
                c = c + cls[k] * coeffs[k]
            return c
    return None


def check_a(log):
    E = ExactK8()
    lev = E.lev
    rels, mu, lam = lev.rels, lev.mu, lev.lam
    out = []
    for ab, kind in [(a, "both") for a in BOTH_REPS] + [((5, 0), "simple order-8 (contrast)")]:
        t0 = time.time()
        ex = lev.exponents(ab, 0)
        V, Veta, VL, L, Linv = E.twisted(ex, 1), E.twisted(ex, 5), E.twisted(ex, -3), E.line(ex, -4), E.line(ex, 4)
        assert V.check(rels) and Veta.check(rels) and VL.check(rels)
        cls, h1E = T.h1_classes(Veta, rels)
        row = {"char": [str(Fr(ab[0], 40)), str(Fr(ab[1], 40))], "kind": kind,
               "h1(V), h1(V_eta), h1(V(x)L)": [T.h1_classes(V, rels)[1], h1E, T.h1_classes(VL, rels)[1]]}
        trials = [("boundary-type (fixed combination)", RT.class_trials(cls)[-1][1])]
        cint = interior_class(lev, Veta, cls) if h1E >= 2 else None
        if cint is not None:
            trials.append(("interior class c_int", cint))
        row["W1"] = {}
        for name, c in trials:
            W = RT.ext_with_line(V, c, L, lev.cov["gens"])
            assert W.check(rels)
            row["W1"][name] = {"W1": brief(T.index(W, rels, mu, lam)), "L2W1": brief(T.index(T.wedge2_rep(W), rels, mu, lam))}
        clsd, _ = T.h1_classes(Veta.dual(), rels)
        W2s = RT.ext_with_line(V.dual(), RT.class_trials(clsd)[-1][1], Linv, lev.cov["gens"])
        row["W2 (fixed combination)"] = {"I(W2)": -T.index(W2s, rels, mu, lam)["I"], "I(L2W2)": -T.index(T.wedge2_rep(W2s), rels, mu, lam)["I"]}
        row["seconds"] = round(time.time() - t0, 1)
        log(f"(a) {row['char']} {kind}: {json.dumps({k: (v['W1']['I'], v['L2W1']['I']) for k, v in row['W1'].items()})} W2 {row['W2 (fixed combination)']}")
        out.append(row)
    ok = all(r["h1(V), h1(V_eta), h1(V(x)L)"] == [2, 2, 2]
             and r["W1"]["boundary-type (fixed combination)"]["W1"]["I"] == 1 and r["W1"]["boundary-type (fixed combination)"]["L2W1"]["I"] == -1
             and r["W1"]["interior class c_int"]["W1"]["I"] == 0 and r["W1"]["interior class c_int"]["L2W1"]["I"] == -1
             and r["W2 (fixed combination)"] == {"I(W2)": -1, "I(L2W2)": 1} for r in out if r["kind"] == "both") and \
        all(r["h1(V), h1(V_eta), h1(V(x)L)"] == [1, 1, 1] and r["W1"]["boundary-type (fixed combination)"]["W1"]["I"] == 1
            and r["W1"]["boundary-type (fixed combination)"]["L2W1"]["I"] == 0 for r in out if r["kind"] != "both")
    return out, ok


def check_b():
    rT = json.loads((HERE / "census_t_run.txt").read_text())
    rL = json.loads((HERE / "census_l_run.txt").read_text())
    nT, nL = {}, {}
    for x in rT["A"]:
        if x["level"] == 6 and x["lam"] == "1":
            v = x["row"]["pieces"]["V"]
            nT.setdefault(tuple(x["char"]), set()).add(v["E(a0,a1,t0,r1)"][1] - v["E(a0,a1,t0,r1)"][3])
    for x in rL["A"]:
        if x["level"] == 6 and x["lam"] == "1":
            nL.setdefault(tuple(x["char"]), set()).add(x["row"]["pieces"]["V"]["E(a0,h1,t0,n)"][3])
    agree = nT == nL and all(len(v) == 1 for v in nT.values())
    from collections import Counter
    dist = Counter(min(v) for v in nT.values())

    def order(ch):
        a, b = Fr(ch[0]), Fr(ch[1])
        from math import lcm
        return lcm(a.denominator, b.denominator)
    by = Counter((order(k), min(v)) for k, v in nT.items() if min(v) > 0)
    return {"routes agree on n(chi (x) rho_1) at every character of M6": agree,
            "distribution of n over the 320 characters": dict(dist),
            "(order, n) of the characters with interior classes": {f"{k}": v for k, v in sorted(by.items())}}, agree


def check_c(log):
    lev = RT.Level(6)
    p = 16624081
    A = RT.Arith("gf", lev.K, p=p)
    rho = T.rs_rho(lev.cov, A.field)
    ab = BOTH_REPS[0]
    ex = lev.exponents(ab, 0)
    V, Veta, VL, L = lev.twisted(A, rho, ex, 1), lev.twisted(A, rho, ex, 5), lev.twisted(A, rho, ex, -3), lev.line(A, ex, -4)
    rels, gens = lev.rels, lev.cov["gens"]
    cls, _ = T.h1_classes(Veta, rels)
    c = RT.class_trials(cls)[-1][1]
    W = RT.ext_with_line(V, c, L, gens)
    L2W = T.wedge2_rep(W)
    L2V = T.wedge2_rep(V)
    # restriction images in H^1(T; Lambda^2 W1): from Lambda^2 V's classes (as a submodule: pad), and from all of H^1(Lambda^2 W1)
    BW = RT.peripheral_coboundaries(L2W, lev)
    allcls, a1 = T.h1_classes(L2W, rels)
    cols_all = [RT.restrict(L2W, z, lev.mu).vstack(RT.restrict(L2W, z, lev.lam)) for z in allcls]
    r1 = T.dm_rank(BW.hstack(*cols_all)) - T.dm_rank(BW)
    # the Lambda^2 V part: its classes embed (coordinates e_i ^ e_j with i < j < 4 come first in tower_lib's pairs ordering of 5)
    pairs5 = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    sub_idx = [k for k, (i, j) in enumerate(pairs5) if j < 4]
    acls, ha = T.h1_classes(L2V, rels)
    dom = A.dom

    def embed(z):
        d4, d5, k = 6, 10, len(gens)
        rows = []
        for g in range(k):
            blk = [dom.zero] * d5
            for t, kk in enumerate(sub_idx):
                blk[kk] = z[g * d4 + t, 0].element
            rows += [[x] for x in blk]
        return DomainMatrix(rows, (k * d5, 1), dom)
    cols_A = [RT.restrict(L2W, embed(z), lev.mu).vstack(RT.restrict(L2W, embed(z), lev.lam)) for z in acls]
    rA = T.dm_rank(BW.hstack(*cols_A)) - T.dm_rank(BW)
    d = A.ix(L2W, rels, lev.mu, lev.lam)
    out = {"character": [str(Fr(ab[0], 40)), str(Fr(ab[1], 40))], "p": p, "h1(Lambda^2 V)": ha, "h1(V (x) L)": T.h1_classes(VL, rels)[1],
           "a1(Lambda^2 W1)": a1, "r1(Lambda^2 W1)": r1, "rank of Lambda^2 V's image in H^1(T; Lambda^2 W1)": rA,
           "s0(Lambda^2 W1)": d["s0"], "I(Lambda^2 W1)": d["I"]}
    log(f"(c) {json.dumps(out)}")
    ok = a1 == 4 and r1 == 4 and rA == 2 and d["s0"] == 3 and d["I"] == -1
    return out, ok


def check_d(log):
    lev = RT.Level(6)
    p = 16624081
    field = T.Field("gf", p=p, r=1, iota=T.gf_root_of_unity(p, 4))
    fm = T.FibreMonodromy(field)
    rT = json.loads((HERE / "census_t_run.txt").read_text())
    h1V = {tuple(x["char"]): x["row"]["pieces"]["V"]["E(a0,a1,t0,r1)"][1] for x in rT["A"] if x["level"] == 6 and x["field"] == f"GF({p})"}
    from collections import Counter
    tally, ok = Counter(), True
    for ab in lev.chars:
        S, B = fm.level(ab, lev.N, 6)
        assert T.dm_rank(B) == 4, "H^0(F) != 0"
        k1 = T.kernel_dims_on_H1(S, B, field.dom.one, maxpow=1)[0]
        key = (str(Fr(ab[0], lev.N)), str(Fr(ab[1], lev.N)))
        ok = ok and k1 == h1V[key]
        tally[k1] += 1
    log(f"(d) dim ker(S^(6) - 1) over the 320 characters: {dict(tally)}; equals route T's h^1(V) everywhere: {ok}")
    return {"distribution of dim ker(S^(6) - 1)": dict(tally), "equals h^1(V) at every character": ok}, ok


def main():
    t0 = time.time()
    lines = []

    def log(msg):
        print(msg, flush=True)
        lines.append(msg)
    rec = {}
    rec["(a) exact over Q(zeta_8)"], oka = check_a(log)
    rec["(b) interior classes on M6"], okb = check_b()
    rec["(c) the Lambda^2 count at a 'both' member"], okc = check_c(log)
    rec["(d) Wang: the fibre monodromy's kernel = h^1(V) at every character of M6"], okd = check_d(log)
    rec["summary"] = {"(a) the four orbits read (+1, -1) at a boundary-type class and (0, -1) at c_int, W2 (-1, +1), exactly; the simple "
                      "contrast (+1, 0)": oka,
                      "(b) both routes find the same interior classes on M6": okb,
                      "(c) r1 = 4 = 2 + 1 + 1, s0 = 3, I(Lambda^2 W1) = -1": okc,
                      "(d) Wang's kernel equals h^1(V) at all 320 characters of M6": okd}
    rec["seconds"] = round(time.time() - t0, 1)
    print(json.dumps(rec["summary"], indent=1))
    print(json.dumps(rec["(b) interior classes on M6"], indent=1))
    if "--record" in sys.argv:
        RECORD.write_text(json.dumps(rec, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
    return rec


if __name__ == "__main__":
    main()
