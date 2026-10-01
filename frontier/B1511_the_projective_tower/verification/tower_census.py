"""B1511 -- THE PROJECTIVE TOWER: the census, built as sealed (PREREGISTRATION.md section 5; the seal's digest is in SEAL_LEDGER).

Run as:  python3 tower_census.py --record   (writes tower_census_run.txt)

A  s961, case (a): the five non-trivial orbits of size three of T_3 = (Z/4)^2.  For every member nu_F: the characteristic polynomial
   P(q, s) of S^(3) on H^1(F; nu_F (x) rho_q), exactly over Q(i)(q); the deck check (the three members agree); symmetries
   (reciprocity, the conjugate orbit, q -> 1/q); H^0(F) generically.  For lam in mu_4: the real part of the exceptional locus
   (gcd of the real and imaginary parts of the numerator of P(q, lam)), its irreducible factors over Q and their positive roots.
   At every factor g0 with a positive root q != 1: exact data in Q(i)[q]/(g0) (rank of B, the kernel dimensions of (S - lam)^j on
   H^1 for j = 1..4), and the direct count on s961's RS presentation for every member: h^1, and for every basis class (and the sum
   of the first two) I(W1), I(L2 W1), I(W2) = -I(W1[A*]), I(L2 W2) -- exactly when deg g0 <= 8, and over GF(p) at three primes
   (every root) always.
B  M6: at every exceptional point of Part A, the first member pulled back to M6 (lam6 = lam3^2): h^1 and I(W1) of every basis class
   over GF(p), against Shapiro's sum over lam3' = +-lam3.
C  case (b), levels 2, 4, 5, 6: every orbit with nu_F^4 != 1, every lam in mu_4.
   C1 (O^5 = O = O^-1 and lam = +-1, where real roots are generic): exact P over Q(zeta12)(q), the positive roots of f = P(q, lam),
      and at each the direct count of W = [[V_nu, c L], [0, L]] (L = nu^-4, c in H^1(V_{nu^5})) and of the opposite order, over
      GF(p) at three primes, every root, and exactly when deg g0 <= 4.
   C2 (every other pair): over GF(p) at three primes, the gcd of f_{O,lam} with f_{O^5,lam} (and with f_{O^-1,lam^-1} when
      O^5 = O), with the factors q and q - 1 recorded and removed.
D  the per-level table (levels 1-6): firing families by orbit size, from Theorem D, Part A (with Shapiro), Part C."""
import json
import math
import sys
import time
from pathlib import Path

import sympy as sp
import flint
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tower_lib as T  # noqa: E402

q, s = T.Q, T.S_
IUNIT = sp.I


# ============================================================================================ helpers
def primes_for(mod, count=3, start=1000, accept=None):
    out, p = [], start
    while len(out) < count:
        p += 1
        if p % mod == 1 and sp.isprime(p) and (accept is None or accept(p)):
            out.append(p)
    return out


def conj_expr(e):
    return sp.expand(e).xreplace({sp.I: -sp.I})


def re_im_parts(f):
    """for f in Q(i)[q] (expanded): (Re f, Im f) in Q[q], coefficientwise"""
    P = sp.Poly(sp.expand(f), q, sp.I)
    re, im = 0, 0
    for (dq, di), c in P.terms():
        term = c * q ** dq
        k = di % 4
        if k == 0:
            re += term
        elif k == 1:
            im += term
        elif k == 2:
            re -= term
        else:
            im -= term
    return sp.expand(re), sp.expand(im)


def numerator_in_q(expr):
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    return sp.expand(num)


def positive_roots(g0):
    P = sp.Poly(g0, q)
    out = []
    for r in P.real_roots():
        if r.is_positive and r != 1:
            out.append(r)
    return out


def gf_roots_poly(g0, p):
    """roots mod p of g0 in Q[q], and whether g0 is squarefree mod p with no degree drop"""
    P = sp.Poly(g0, q)
    co = []
    for c in P.all_coeffs()[::-1]:
        c = sp.Rational(c)
        co.append(int(c.p) * pow(int(c.q), p - 2, p) % p)
    fp = flint.nmod_poly(co, p)
    ok = fp.degree() == P.degree() and fp.gcd(fp.derivative()).degree() == 0
    roots = sorted(int(r) for r, _ in fp.roots())
    return roots, ok


def h1_of_rep(rep, rels):
    return T.h1_classes(rep, rels)


def counts_case_a(rep, rels, mu, lam, mode, p=None, with_wedge=True):
    """W1 = [[V, c], [0, 1]] for every basis class c of H^1(V) (and c1 + c2), W2 = (W1[V*])*"""
    ix = (lambda R: T.index(R, rels, mu, lam)) if mode == "exact" else (lambda R: T.index_gf(R, rels, mu, lam, p))
    cls, h1 = T.h1_classes(rep, rels)
    clsd, h1d = T.h1_classes(rep.dual(), rels)
    out = {"h1": h1, "h1_dual": h1d, "W1": {}, "W2": {}}
    trials = [(f"c{k + 1}", c) for k, c in enumerate(cls)]
    if len(cls) >= 2:
        trials.append(("c1+c2", cls[0] + cls[1]))
    for name, c in trials:
        W = T.extension_rep(rep, c)
        assert W.check(rels)
        d = ix(W)
        row = {"I": d["I"], "data(a0,a1,t0,r1)": [d["a0"], d["a1"], d["t0"], d["r1"]], "dual(b0,b1,s0,q1)": [d["b0"], d["b1"], d["s0"], d["q1"]]}
        if with_wedge:
            row["I_L2"] = ix(T.wedge2_rep(W))["I"]
        out["W1"][name] = row
    trials = [(f"c{k + 1}", c) for k, c in enumerate(clsd)]
    if len(clsd) >= 2:
        trials.append(("c1+c2", clsd[0] + clsd[1]))
    for name, c in trials:
        Ws = T.extension_rep(rep.dual(), c)
        assert Ws.check(rels)
        d = ix(Ws)
        row = {"I": -d["I"]}
        if with_wedge:
            row["I_L2"] = -ix(T.wedge2_rep(Ws))["I"]
        out["W2"][name] = row
    return out


def line_rep(cov, field, ex_pairs, N, Nl, power):
    """the line nu^power on the RS generators, as 1 x 1 DomainMatrices (ex_pairs: the exponents of nu)"""
    out = {}
    for g in cov["gens"]:
        e1, e2 = ex_pairs[g]
        v = field.unit(power * e1, N) * field.unit(power * e2, Nl)
        out[g] = DomainMatrix([[v]], (1, 1), field.dom)
    return out


def scaled_rep(rep_base, line, cov):
    """V (x) L for a 1-dim L given as 1 x 1 matrices"""
    return T.DMRep(cov["gens"], {g: rep_base.M[g] * line[g][0, 0].element for g in cov["gens"]})


def ext_with_line(V, coc, L, cov):
    """W = [[V, c L], [0, L]] with c a cocycle of V (x) L^-1 (so W is a representation)"""
    gens, d, dom = cov["gens"], V.d, V.dom
    out = {}
    for i, g in enumerate(gens):
        lv = L[g][0, 0].element
        cg = coc[i * d:(i + 1) * d, :] * lv
        top = V.M[g].hstack(cg)
        bot = DomainMatrix.zeros((1, d), dom).hstack(L[g])
        out[g] = top.vstack(bot)
    return T.DMRep(gens, out)


def counts_case_b(cov, field, rho, ab, N, lam_k, Nl, mode, p=None, with_wedge=True):
    """case (b): V = nu (x) rho, L = nu^-4 (non-trivial on the fibre, trivial on z), eta = nu^5 = nu L^-1.
    W1 = [[V, c L], [0, L]] for c in H^1(V_eta); W2 = [[L, *], [0, V]] read through its dual W2* = [[V*, c' L^-1], [0, L^-1]]
    with c' in H^1(V* (x) L) = H^1((V_eta)*)."""
    rels, mu, lam = cov["rels"], cov["mu"], cov["lam"]
    ix = (lambda R: T.index(R, rels, mu, lam)) if mode == "exact" else (lambda R: T.index_gf(R, rels, mu, lam, p))
    ex = T.rs_character_exponents(cov, ab, N, lam_k, Nl)
    V = T.DMRep(cov["gens"], {g: rho[g] * (field.unit(ex[g][0], N) * field.unit(ex[g][1], Nl)) for g in cov["gens"]})
    L = line_rep(cov, field, ex, N, Nl, -4)
    Linv = line_rep(cov, field, ex, N, Nl, 4)
    eta = T.DMRep(cov["gens"], {g: rho[g] * (field.unit(5 * ex[g][0], N) * field.unit(5 * ex[g][1], Nl)) for g in cov["gens"]})
    assert V.check(rels) and eta.check(rels)
    Lrep = T.DMRep(cov["gens"], L)
    clsL, h1L = T.h1_classes(Lrep, rels)
    clsV, h1V = T.h1_classes(V, rels)
    clsE, h1E = T.h1_classes(eta, rels)
    clsEd, h1Ed = T.h1_classes(eta.dual(), rels)
    out = {"h1(L)": h1L, "h1(V_nu)": h1V, "h1(V_eta)": h1E, "h1(V_eta*)": h1Ed, "W1": {}, "W2": {}}
    trials = [(f"c{k + 1}", c) for k, c in enumerate(clsE)] + ([("c1+c2", clsE[0] + clsE[1])] if len(clsE) >= 2 else [])
    for name, c in trials:
        W = ext_with_line(V, c, L, cov)
        assert W.check(rels)
        d = ix(W)
        row = {"I": d["I"], "data(a0,a1,t0,r1)": [d["a0"], d["a1"], d["t0"], d["r1"]], "dual(b0,b1,s0,q1)": [d["b0"], d["b1"], d["s0"], d["q1"]]}
        if with_wedge:
            row["I_L2"] = ix(T.wedge2_rep(W))["I"]
        out["W1"][name] = row
    Vd = V.dual()
    trials = [(f"c{k + 1}", c) for k, c in enumerate(clsEd)] + ([("c1+c2", clsEd[0] + clsEd[1])] if len(clsEd) >= 2 else [])
    for name, c in trials:
        Ws = ext_with_line(Vd, c, Linv, cov)
        assert Ws.check(rels)
        d = ix(Ws)
        row = {"I": -d["I"]}
        if with_wedge:
            row["I_L2"] = -ix(T.wedge2_rep(Ws))["I"]
        out["W2"][name] = row
    return out


# ============================================================================================ Part A
def fibre_P(field, blocks, ab, N, n):
    S = DomainMatrix.eye(8, field.dom)
    cur = tuple(x % N for x in ab)
    for _ in range(n):
        S = T.one_step_closed(field, blocks, cur, N) * S
        cur = T.deck(cur, N)
    assert cur == tuple(x % N for x in ab)
    return S


def symmetries(P, Pconj_orbit):
    c = [sp.cancel(sp.Poly(P, s).coeff_monomial(s ** k)) for k in range(5)]
    recip = sp.expand(s ** 4 * P.subs(s, 1 / s))
    return {"constant_term": str(sp.factor(c[0])),
            "palindromic": sp.simplify(c[0] - 1) == 0 and sp.simplify(c[1] - c[3]) == 0,
            "reciprocal_up_to_constant": sp.simplify(sp.expand(recip - c[0] * P)) == 0,
            "P(1/q, s) = P(q, s)": sp.simplify(P.subs(q, 1 / q) - P) == 0,
            "inverse_orbit_has_the_conjugate_polynomial": None if Pconj_orbit is None else sp.simplify(Pconj_orbit - conj_expr(P)) == 0}


def part_a(log, orbs=None):
    """orbs: the orbits to run (default: the five non-trivial orbits of T_3; the dry run passes [[(0, 0)]])"""
    cov3 = T.rs_cover(3)
    chars, N = T.characters(3)
    all_orbs = T.orbits(chars, N)
    if orbs is None:
        orbs = [o for o in all_orbs if o != [(0, 0)]]
    F = T.Field("sym")
    blocks = [F.mat(A) for A in T.block_mats()]
    polys = {}
    res = {"orbits": []}
    for O in orbs:
        Ps = []
        for ab in O:
            S = fibre_P(F, blocks, ab, N, 3)
            Ps.append(sp.expand(T.charpoly_on_H1(S)))
        same = all(sp.simplify(P - Ps[0]) == 0 for P in Ps[1:])
        polys[tuple(O)] = (Ps[0], same)
        log(f"A: orbit {O} polynomial computed; deck-invariant: {same}")
    inv_of = lambda O: tuple(sorted(((-a) % N, (-b) % N) for a, b in O))
    for O in orbs:
        P, same = polys[tuple(O)]
        Oinv = [o for o in all_orbs if tuple(sorted(o)) == inv_of(O)][0]
        sym = symmetries(P, polys[tuple(Oinv)][0] if tuple(Oinv) in polys else None)
        ab0 = O[0]
        # H^0(F) generically
        Fq = T.Field("sym")
        FM = T.FibreMonodromy(Fq)
        B = FM.coboundary(ab0, N)
        entry = {"orbit": O, "orders": sorted({T.order_of(c, N) for c in O}), "inverse_orbit": Oinv,
                 "P(q,s)": str(sp.factor(P)), "deck_invariant": same, "symmetries": sym,
                 "H0(F)_generic_rank_B": T.dm_rank(B), "lams": {}}
        for l in range(4):
            lam = sp.I ** l
            f = numerator_in_q(P.subs(s, lam))
            lab = ["1", "i", "-1", "-i"][l]
            if f == 0:
                entry["lams"][lab] = {"identically_exceptional": True}
                log(f"A: orbit {O} lam {lab}: IDENTICALLY EXCEPTIONAL")
                continue
            re, im = re_im_parts(f)
            g = sp.gcd(re, im) if im != 0 else re
            g = sp.Poly(g, q).monic().as_expr() if sp.Poly(g, q).degree() > 0 else sp.Integer(1)
            fl = sp.factor_list(g)[1] if g != 1 else []
            factors = []
            for g0, mult in fl:
                roots = positive_roots(g0)
                factors.append({"factor": str(g0), "multiplicity": mult, "degree": sp.Poly(g0, q).degree(),
                                "positive_roots_not_1": [str(sp.N(r, 15)) for r in roots], "_g0": g0})
            entry["lams"][lab] = {"identically_exceptional": False, "f_degree": sp.Poly(f, q).degree(), "f_is_real": im == 0,
                                  "real_locus": str(sp.factor(g)), "factors": factors}
            log(f"A: orbit {O} lam {lab}: real locus {sp.factor(g)}")
        res["orbits"].append(entry)
    # point analysis
    points = []
    for entry in res["orbits"]:
        O = entry["orbit"]
        for l, lab in enumerate(["1", "i", "-1", "-i"]):
            L_ = entry["lams"][lab]
            if L_.get("identically_exceptional"):
                points.append({"orbit": O, "lam": lab, "identically_exceptional": True, **identically_exceptional_point(O, N, l, cov3, log)})
                continue
            for fac in L_["factors"]:
                if not fac["positive_roots_not_1"]:
                    continue
                points.append(point_analysis(O, N, l, lab, fac["_g0"], cov3, log))
    for entry in res["orbits"]:
        for lab in entry["lams"]:
            for fac in entry["lams"][lab].get("factors", []):
                fac.pop("_g0", None)
    res["points"] = points
    return res


def point_analysis(O, N, l, lab, g0, cov3, log):
    rels, mu, lam = cov3["rels"], cov3["mu"], cov3["lam"]
    deg = sp.Poly(g0, q).degree()
    out = {"orbit": O, "lam": lab, "g0": str(g0), "degree": deg, "positive_roots": [str(sp.N(r, 15)) for r in positive_roots(g0)]}
    K = T.Field("ext", g=g0)
    blocks = [K.mat(A) for A in T.block_mats()]
    S = fibre_P(K, blocks, O[0], N, 3)
    FM = T.FibreMonodromy(K)
    B = FM.coboundary(O[0], N)
    out["fibre"] = {"rank_B": T.dm_rank(B), "ker_dims_(S-lam)^j_on_H1": T.kernel_dims_on_H1(S, B, K.unit(l, 4)),
                    "ker_dims_at_-lam": T.kernel_dims_on_H1(S, B, K.unit(l + 2, 4))}
    log(f"A point: orbit {O} lam {lab} g0 deg {deg}: fibre {out['fibre']}")
    if deg <= 8:
        rho = T.rs_rho(cov3, K)
        ex_rows = {}
        for ab in O:
            rep = T.DMRep(cov3["gens"], T.twisted_rep(cov3, K, ab, N, l, 4, rho=rho))
            assert rep.check(rels)
            ex_rows[str(ab)] = counts_case_a(rep, rels, mu, lam, "exact")
        out["exact_counts"] = ex_rows
        log(f"A point exact: {json.dumps(ex_rows, default=str)[:300]}")
    modp = []
    for p in primes_for(4, 3, accept=lambda p: gf_roots_poly(g0, p)[1] and gf_roots_poly(g0, p)[0]):
        roots, _ = gf_roots_poly(g0, p)
        iota = T.gf_root_of_unity(p, 4)
        for r in roots:
            Fp = T.Field("gf", p=p, r=r, iota=iota)
            rho = T.rs_rho(cov3, Fp)
            rows = {}
            for ab in O:
                rep = T.DMRep(cov3["gens"], T.twisted_rep(cov3, Fp, ab, N, l, 4, rho=rho))
                assert rep.check(rels)
                rows[str(ab)] = counts_case_a(rep, rels, mu, lam, "gf", p)
            modp.append({"p": p, "q mod p": r, "counts": rows})
    out["mod_p"] = modp
    log(f"A point mod p: {len(modp)} prime-root pairs")
    return out


def identically_exceptional_point(O, N, l, cov3, log):
    rels, mu, lam = cov3["rels"], cov3["mu"], cov3["lam"]
    Fq = T.Field("sym")
    blocks = [Fq.mat(A) for A in T.block_mats()]
    S = fibre_P(Fq, blocks, O[0], N, 3)
    B = T.FibreMonodromy(Fq).coboundary(O[0], N)
    out = {"generic_ker_dims": T.kernel_dims_on_H1(S, B, Fq.unit(l, 4)), "rational_points": {}}
    for qv in (2, 3, sp.Rational(1, 2)):
        K = T.Field("ext", g=q - qv)
        rho = T.rs_rho(cov3, K)
        rows = {}
        for ab in O:
            rep = T.DMRep(cov3["gens"], T.twisted_rep(cov3, K, ab, N, l, 4, rho=rho))
            rows[str(ab)] = counts_case_a(rep, rels, mu, lam, "exact")
        out["rational_points"][str(qv)] = rows
    log(f"A identically exceptional: {json.dumps(out, default=str)[:300]}")
    return out


# ============================================================================================ Part B
def part_b(a_res, log):
    cov6 = T.rs_cover(6)
    rels, mu, lam = cov6["rels"], cov6["mu"], cov6["lam"]
    out = []
    for pt in a_res["points"]:
        if pt.get("identically_exceptional"):
            continue
        O, lab = pt["orbit"], pt["lam"]
        l3 = ["1", "i", "-1", "-i"].index(lab)
        l6 = (2 * l3) % 4
        g0 = sp.sympify(pt["g0"], locals={"q": q})
        ab = O[0]
        rows = []
        for p in primes_for(4, 3, accept=lambda p: gf_roots_poly(g0, p)[1] and gf_roots_poly(g0, p)[0]):
            roots, _ = gf_roots_poly(g0, p)
            iota = T.gf_root_of_unity(p, 4)
            for r in roots:
                Fp = T.Field("gf", p=p, r=r, iota=iota)
                rep = T.DMRep(cov6["gens"], T.twisted_rep(cov6, Fp, ab, 4, l6, 4))
                assert rep.check(rels)
                c = counts_case_a(rep, rels, mu, lam, "gf", p, with_wedge=False)
                rows.append({"p": p, "q mod p": r, "h1_M6": c["h1"], "W1": {k: v["I"] for k, v in c["W1"].items()},
                             "W2": {k: v["I"] for k, v in c["W2"].items()}})
        # Shapiro: the s961 data at +-lam3 (fibre kernel dims and the mod-p counts at lam3)
        s961_h1 = pt["fibre"]["ker_dims_(S-lam)^j_on_H1"][0] + pt["fibre"]["ker_dims_at_-lam"][0]
        out.append({"orbit": O, "lam3": lab, "lam6": ["1", "i", "-1", "-i"][l6], "g0": pt["g0"],
                    "shapiro_h1_M6 = h1(lam3) + h1(-lam3)": s961_h1, "rows": rows})
        log(f"B: orbit {O} lam3 {lab}: {rows[:2]}")
    return out


# ============================================================================================ Part C
LEVELS_B = (2, 4, 5, 6)


def orbit_table(n):
    chars, N = T.characters(n)
    orbs = T.orbits(chars, N)
    idx = {}
    for k, o in enumerate(orbs):
        for c in o:
            idx[c] = k
    return chars, N, orbs, idx


def classify_pairs(n):
    chars, N, orbs, idx = orbit_table(n)
    pairs = []
    for k, o in enumerate(orbs):
        ab = o[0]
        if all(((4 * x) % N) == 0 for x in ab):
            continue                                       # nu_F^4 = 1: case (a) (or trivial)
        k5 = idx[((5 * ab[0]) % N, (5 * ab[1]) % N)]
        kinv = idx[((-ab[0]) % N, (-ab[1]) % N)]
        for l in range(4):
            linv = (-l) % 4
            if k5 == k and kinv == k and l in (0, 2):
                kind = "exact"
                partners = []
            else:
                kind = "gcd"
                partners = [(k5, l)] if k5 != k else []
                if k5 == k:
                    partners.append((kinv, linv))
            pairs.append({"orbit_index": k, "orbit_rep": ab, "orbit_size": len(o), "order": T.order_of(ab, N), "lam": l,
                          "orbit5_index": k5, "orbit_inv_index": kinv, "kind": kind, "partners": partners})
    return chars, N, orbs, idx, pairs


def strip(fp, p):
    """remove the factors q and q - 1 from an nmod_poly; returns (rest, mult_q, mult_q-1)"""
    X = flint.nmod_poly([0, 1], p)
    X1 = flint.nmod_poly([p - 1, 1], p)
    mq = m1 = 0
    while fp.degree() > 0 and fp.coeffs()[0] == 0:
        fp = fp // X
        mq += 1
    while fp.degree() > 0 and fp(1) == 0:
        fp = fp // X1
        m1 += 1
    return fp, mq, m1


def part_c2(n, log):
    chars, N, orbs, idx, pairs = classify_pairs(n)
    mod = (N * 4) // math.gcd(N, 4)
    primes = primes_for(mod, 3)
    res = {"level": n, "N": N, "primes": primes, "orbits": len(orbs), "pairs": []}
    fpolys = {}
    for p in primes:
        mp = T.ModP(p, N)
        for k, o in enumerate(orbs):
            fl = T.f_polys_modp(mp, o[0], n, (0, 1, 2, 3))
            for l in range(4):
                fpolys[(p, k, l)] = flint.nmod_poly(fl[l], p)
        log(f"C2: level {n} prime {p}: f mod p for {len(orbs)} orbits")
    for pr in pairs:
        if pr["kind"] != "gcd":
            continue
        k, l = pr["orbit_index"], pr["lam"]
        row = dict(pr)
        row["per_prime"] = []
        for p in primes:
            f = fpolys[(p, k, l)]
            g = f
            for (k2, l2) in pr["partners"]:
                g = g.gcd(fpolys[(p, k2, l2)])
            rest, mq, m1 = strip(g, p)
            row["per_prime"].append({"p": p, "deg_f": f.degree(), "deg_partners": [fpolys[(p, k2, l2)].degree() for k2, l2 in pr["partners"]],
                                     "deg_gcd": g.degree(), "mult_q": mq, "mult_q-1": m1, "deg_gcd_without_q_and_q-1": rest.degree()})
        row["no_common_root_other_than_0_1"] = all(x["deg_gcd_without_q_and_q-1"] == 0 for x in row["per_prime"])
        res["pairs"].append(row)
    res["unresolved"] = [ (r["orbit_rep"], r["lam"]) for r in res["pairs"] if not r["no_common_root_other_than_0_1"]]
    res["exact_pairs"] = [(pr["orbit_rep"], pr["lam"]) for pr in pairs if pr["kind"] == "exact"]
    log(f"C2: level {n}: {len(res['pairs'])} gcd pairs, unresolved {res['unresolved']}, exact pairs {res['exact_pairs']}")
    return res


def part_c1(n, exact_pairs, log):
    """the self-coincident real pairs, exactly over Q(zeta12)(q)"""
    chars, N, orbs, idx, pairs = classify_pairs(n)
    cov = T.rs_cover(n)
    rels, mu, lam = cov["rels"], cov["mu"], cov["lam"]
    out = []
    F = T.Field("sym", base="Q12")
    blocks = [F.mat(A) for A in T.block_mats()]
    done = {}
    for ab, l in exact_pairs:
        # the characters of these orbits take values in mu_12: rewrite the exponents over N12 = gcd-reduced order
        o = orbs[idx[tuple(ab)]]
        e = T.order_of(ab, N)
        assert 12 % e == 0, ("an exact pair outside Q(zeta12)", ab, N)
        red = lambda c: ((c[0] * e // N) % e, (c[1] * e // N) % e)
        key = tuple(o)
        if key not in done:
            Ps = [sp.expand(T.charpoly_on_H1(fibre_P(F, blocks, red(c), e, n))) for c in o]
            same = all(sp.simplify(P - Ps[0]) == 0 for P in Ps[1:])
            done[key] = (Ps[0], same)
            log(f"C1: level {n} orbit of {ab}: polynomial computed (deck-invariant {same})")
        P, same = done[key]
        lam_v = sp.I ** l
        f = numerator_in_q(P.subs(s, lam_v))
        f = sp.nsimplify(sp.expand(f))
        row = {"level": n, "orbit": o, "order": e, "lam": ["1", "i", "-1", "-i"][l], "deck_invariant": same,
               "P(q,s)": str(sp.factor(P)), "identically_zero": f == 0}
        if f == 0:
            out.append(row)
            log(f"C1: level {n} orbit {ab} lam {l}: IDENTICALLY ZERO")
            continue
        fr = sp.Poly(f, q)
        row["f_rational"] = all(sp.sympify(c).is_rational for c in fr.all_coeffs())
        fl = sp.factor_list(sp.Poly(f, q).monic().as_expr())[1]
        row["factors"] = []
        for g0, mult in fl:
            roots = positive_roots(g0)
            frow = {"factor": str(g0), "multiplicity": mult, "degree": sp.Poly(g0, q).degree(),
                    "positive_roots_not_1": [str(sp.N(r, 15)) for r in roots]}
            if roots:
                frow["point"] = case_b_point(n, cov, o, red, e, l, g0, log)
            row["factors"].append(frow)
        out.append(row)
    return out


def case_b_point(n, cov, o, red, e, l, g0, log):
    rels, mu, lam = cov["rels"], cov["mu"], cov["lam"]
    deg = sp.Poly(g0, q).degree()
    pt = {"degree": deg}
    # fibre data exactly
    K = T.Field("ext", g=g0, base="Q12")
    blocks = [K.mat(A) for A in T.block_mats()]
    S = fibre_P(K, blocks, red(o[0]), e, n)
    B = T.FibreMonodromy(K).coboundary(red(o[0]), e) if False else None
    FMK = T.FibreMonodromy(K)
    Vx = FMK.rx * K.unit(red(o[0])[0], e)
    Vy = FMK.ry * K.unit(red(o[0])[1], e)
    I4 = DomainMatrix.eye(4, K.dom)
    B = (Vx - I4).vstack(Vy - I4)
    pt["fibre"] = {"rank_B": T.dm_rank(B), "ker_dims_(S-lam)^j_on_H1": T.kernel_dims_on_H1(S, B, K.unit(l, 4))}
    log(f"C1 point: level {n} orbit {o[0]} lam {l} deg {deg}: fibre {pt['fibre']}")
    if deg <= 4:
        rho = T.rs_rho(cov, K)
        rows = {}
        for c in o:
            rows[str(c)] = counts_case_b(cov, K, rho, red(c), e, l, 4, "exact")
        pt["exact_counts"] = rows
        log(f"C1 exact: {json.dumps(rows, default=str)[:300]}")
    modp = []
    for p in primes_for(12, 3, accept=lambda p: gf_roots_poly(g0, p)[1] and gf_roots_poly(g0, p)[0]):
        roots, _ = gf_roots_poly(g0, p)
        iota = T.gf_root_of_unity(p, 4)
        for r in roots:
            Fp = T.Field("gf", p=p, r=r, iota=iota)
            rho = T.rs_rho(cov, Fp)
            rows = {}
            for c in o:
                rows[str(c)] = counts_case_b(cov, Fp, rho, red(c), e, l, 4, "gf", p)
            modp.append({"p": p, "q mod p": r, "counts": rows})
    pt["mod_p"] = modp
    log(f"C1 point mod p: {len(modp)} prime-root pairs")
    return pt


# ============================================================================================ Part D
def part_d(out):
    """the per-level table: the families with a non-zero count, by level and orbit size (Theorem D's pullback is decided at design
    time and entered as such; Part A enters at levels 3 and 6 through Shapiro; Part C1 at its own level)"""
    table = {n: [] for n in range(1, 7)}
    for n in range(1, 7):
        table[n].append({"family": "pullback of B1509's W1 (nu_F = 1)", "orbit_size": 1, "where": "q = 17 +- 12 sqrt2, lam_n = (-1)^n",
                         "count_per_member": {"W1": -1, "W2": +1}, "source": "Theorem D (design time)"})
    for pt in out["A"]["points"]:
        if pt.get("identically_exceptional"):
            continue
        rows = [r for r in pt["mod_p"]]
        vals = sorted({v["I"] for r in rows for m in r["counts"].values() for v in m["W1"].values()})
        vals2 = sorted({v["I"] for r in rows for m in r["counts"].values() for v in m["W2"].values()})
        if any(v != 0 for v in vals + vals2):
            for n in (3, 6):
                table[n].append({"family": f"T_3 orbit {pt['orbit']}", "orbit_size": 3, "where": f"{pt['g0']} = 0, lam3 = {pt['lam']}",
                                 "W1_values": vals, "W2_values": vals2, "source": "Part A" + (" + Shapiro (Part B)" if n == 6 else "")})
    for n, rows in out.get("C1", {}).items():
        for row in rows:
            for fac in row.get("factors", []):
                pt = fac.get("point")
                if not pt:
                    continue
                vals = sorted({v["I"] for r in pt["mod_p"] for m in r["counts"].values() for v in m["W1"].values()})
                vals2 = sorted({v["I"] for r in pt["mod_p"] for m in r["counts"].values() for v in m["W2"].values()})
                if any(v != 0 for v in vals + vals2):
                    table[int(n)].append({"family": f"case (b) orbit {row['orbit'][0]}", "orbit_size": len(row["orbit"]),
                                          "where": f"{fac['factor']} = 0, lam = {row['lam']}", "W1_values": vals, "W2_values": vals2,
                                          "source": "Part C1"})
    unresolved = {n: r["unresolved"] for n, r in out["C2"].items() if r["unresolved"]}
    return {"table": table, "C2_unresolved": unresolved}


# ============================================================================================ the banked identity (section 4)
def banked_identity(log):
    """C1 (B1509's monic Q at level one, symbolic) and C5's first row (B1509's W1 = -1, W2 = +1 at q^2 - 34 q + 1, mu = -1, exactly on
    M_1's RS presentation), re-checked inside the sealed run before Part A is read"""
    F = T.Field("sym", gaussian=False)
    S1, _ = T.FibreMonodromy(F).level((0, 0), 1, 1)
    q_ok = sp.simplify(T.charpoly_on_H1(S1) - T.Q_MONIC) == 0
    cov1 = T.rs_cover(1)
    K = T.Field("ext", g=q ** 2 - 34 * q + 1)
    rep = T.DMRep(cov1["gens"], T.twisted_rep(cov1, K, (0, 0), 1, 2, 4))
    c = counts_case_a(rep, cov1["rels"], cov1["mu"], cov1["lam"], "exact")
    row_ok = c["h1"] == 1 and c["W1"]["c1"]["I"] == -1 and c["W2"]["c1"]["I"] == 1 and c["W1"]["c1"]["I_L2"] == 0
    log(f"banked identity: Q at level one {q_ok}; B1509's first row {row_ok}")
    return {"Q_at_level_one": q_ok, "B1509_row_q^2-34q+1_mu=-1": {"h1": c["h1"], "I(W1)": c["W1"]["c1"]["I"], "I(W2)": c["W2"]["c1"]["I"],
                                                                 "I(L2 W1)": c["W1"]["c1"]["I_L2"]}, "passed": q_ok and row_ok}


# ============================================================================================ main
def main():
    t0 = time.time()
    logs = []

    def log(msg):
        line = f"[{time.time() - t0:7.1f}s] {msg}"
        logs.append(line)
        print(line, flush=True)

    out = {"banked_identity": banked_identity(log)}
    if not out["banked_identity"]["passed"]:
        out["stopped"] = "the banked identity failed; nothing sealed is read"
        return out
    out["A"] = part_a(log)
    out["B"] = part_b(out["A"], log)
    C2 = {}
    exact = {}
    for n in LEVELS_B:
        C2[n] = part_c2(n, log)
        if C2[n]["exact_pairs"]:
            exact[n] = C2[n]["exact_pairs"]
    out["C2"] = C2
    out["C1_expected_only_level4_3torsion"] = sorted(exact) == [4] and all(T.order_of(tuple(ab), 15) == 3 for ab, l in exact[4]) if exact else False
    out["C1"] = {n: part_c1(n, exact[n], log) for n in exact}
    out["D"] = part_d(out)
    out["seconds"] = round(time.time() - t0)
    out["log"] = logs
    return out


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    if "--record" in sys.argv:
        (HERE / "tower_census_run.txt").write_text(txt + "\n", encoding="utf-8")
    print(txt[:4000])
