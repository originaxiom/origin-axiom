#!/usr/bin/env python3
"""B1532 -- design-time controls (before the seal; no twisted term of the sealed population is read).

    python3 -u controls.py [--record]   ->  controls.json, controls_run.txt

K1  the banked identity in both routes: every chi = 1 term of M2-M6 against sm:B1515's census rows at the same prime (one-class
    members' c1 rows; two-class members' generic class against the banked generic row), every B1297 dimension of W1 and
    Lambda^2 W1 (run_terms.part0).
K2  the shared labels: route T's and route L's fibre words for x, y in m, n are the same words, the label sets of T_n^ agree on
    every level, and the two deck maps agree on every label.
K3  Lemma Z (an acyclic torus carries no index) on twists off the cusp (chi(t) in {-1, i, w}): every index 0 at every class read,
    in both routes, on one member of each level and on a two-class member of M6 (its full reader: pencils, specials, gen2).
K4  the subgroups: the closure count equals Toth's s(m, n) (arXiv:1312.1485, Theorem 4.1, eq. (5)) on every level.
K5  route C on banked quantities: h^1(V (x) C[A]) equals the sum over the coset of sm:B1515's banked h^1(nu chi (x) rho), and
    h^1(Lambda^2 V (x) C[A]) = 2|A| (Menal-Ferrer-Porti through sm:B1515's Lemma 3), on the subgroups of order <= 8 of M3
    and of order <= 4 of M6, for two members each.
K6  the class structure in both routes: the two-class members are sm:B1515's 120 on M6 (h^1(V_eta) = 2, interior line of
    dimension one, asserted by both readers), and no other level has one.
K7  the pencils at chi = 1 (both routes): at every two-class member's generic class the four pencils predict h^1 of E, E*,
    Lambda^2 E, (Lambda^2 E)* exactly (the in-run check D2 on banked modules; the special classes are located, not read).
K8  Lemma D on banked rows: I(W2) = -I(W1) and I(Lambda^2 W2) = -I(Lambda^2 W1) at every one-class member (sm:B1515's D6).
K9  the conjugate-pair reader, split: with w^2 = d0 a SQUARE the restriction-of-scalars module R(M(u + v w)) is
    M(u + v sqrt d0) (+) M(u - v sqrt d0), so its raw B1297 data must be the sum of the two direct readings at those rational
    classes.  Read at chi = 1 at generic classes of two-class members of M6 (the generic class at chi = 1 is banked-level), d0 = 4
    and 9, in both routes."""
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cover_lib_l as CL  # noqa: E402
import cover_lib_t as CT  # noqa: E402
import read_out as RO  # noqa: E402
import route_c as RC  # noqa: E402
import run_terms as RUN  # noqa: E402

LEVELS = (2, 3, 4, 5, 6)


def k2():
    out = {"fibre words equal": CT.T.FIBRE == {k: v for k, v in CL.RL.IA.FIBRE_MN.items()},
           "phi equal": CT.T.PHI == CL.RL.IA.PHI}
    for n in LEVELS:
        lev = CT.RT.Level(n)
        labT = {f"{Fr(a, lev.N)},{Fr(b, lev.N)}": (a, b) for a, b in lev.chars}
        chL, D = CL.RL.fibre_characters(n)
        labL = {f"{a},{b}": (a, b) for a, b in chL}
        deck_ok = all(
            f"{Fr(CT.T.deck(labT[x], lev.N)[0], lev.N)},{Fr(CT.T.deck(labT[x], lev.N)[1], lev.N)}"
            == "{},{}".format(*CL.RL.deck_image(labL[x])) for x in labT)
        out[f"M{n}"] = {"labels equal": set(labT) == set(labL), "|T_n|": len(labT), "deck maps agree": deck_ok}
    out["holds"] = out["fibre words equal"] and out["phi equal"] and all(
        v["labels equal"] and v["deck maps agree"] for k, v in out.items() if k.startswith("M"))
    return out


def k3(ps_T, ps_L):
    out, allzero = {}, True
    for n in LEVELS:
        LT = CT.LevelT(n, ps_T[n])
        LL = CL.LevelL(n, ps_L[n])
        rec = {}
        for kind in ("one", "two"):
            abT = next((ab for ab in LT.chars if CT.MemberT(LT, ab).kind == kind), None) if (kind == "one" or n == 6) else None
            if abT is None:
                continue
            lab = LT.label(abT)
            abL = next(ab for ab in LL.chars if LL.label(ab) == lab)
            mT, mL = CT.MemberT(LT, abT), CL.MemberL(LL, abL)
            for lk, lamf in ((6, Fr(1, 2)), (3, Fr(1, 4)), (4, Fr(1, 3))):
                for chiT in LT.chars[:2]:
                    chiL = next(ab for ab in LL.chars if LL.label(ab) == LT.label(chiT))
                    exT = LT.lev.exponents(chiT, lk)
                    valsL = CL.RL.character_values(LL.U, chiL, lamf, 1)
                    if kind == "one":
                        tT = [mT.term(mT.c_one, exT)]
                        W = mL.W1(mL.c_one)
                        tL = [[CL.lsig(CL.RL.index(W.scaled(valsL))), CL.lsig(CL.RL.index(W.wedge2().scaled(valsL)))]]
                    else:
                        orig_e, orig_v = CT.LevelT.exponents, CL.LevelL.vals
                        CT.LevelT.exponents = lambda self, ab, _lk=lk: self.lev.exponents(ab, _lk)
                        CL.LevelL.vals = lambda self, ab, power=1, _l=lamf: CL.RL.character_values(self.U, ab, _l, power)
                        try:
                            rT, rL = mT.read_two(chiT, gen2=True), mL.read_two(chiL, gen2=True)
                        finally:
                            CT.LevelT.exponents, CL.LevelL.vals = orig_e, orig_v
                        tT = [rT["int"], rT["gen"][1], rT["gen2"][1]] + [s[2] for s in rT["special"]]
                        tL = [rL["int"], rL["gen"][1], rL["gen2"][1]] + [s[2] for s in rL["special"]]
                    Is = {t[0][0] for t in tT + tL} | {t[1][0] for t in tT + tL}
                    allzero &= Is == {0}
                    rec[f"{kind} {lab} chi {LT.label(chiT)} lam {lamf}"] = sorted(Is)
        out[f"M{n}"] = rec
    out["holds"] = allzero
    return out


def k4():
    out = {}
    for n in LEVELS:
        lev = CT.RT.Level(n)
        labels = [f"{Fr(a, lev.N)},{Fr(b, lev.N)}" for a, b in lev.chars]
        m, nn = RO.invariant_factors(labels)
        out[f"M{n}"] = {"invariant factors": [m, nn], "subgroups": len(RO.subgroups(labels)), "Toth": RO.toth(m, nn)}
    out["holds"] = all(v["subgroups"] == v["Toth"] for v in out.values())
    return out


def k5(ps_T):
    rec = RUN.banked("T")
    out, ok = {}, True
    for n, maxorder in ((3, 8), (6, 4)):
        LT = CT.LevelT(n, ps_T[n])
        field = f"GF({ps_T[n]})"
        h1V = {",".join(r["char"]): r["row"]["h1"]["V"] for r in rec["A"] if r["level"] == n and r["field"] == field
               and r["lam"] == "1"}
        labels = [LT.label(ab) for ab in LT.chars]
        subs = [B for B in RO.subgroups(labels) if len(B) <= maxorder]
        for ab in LT.chars[1:3]:
            m = CT.MemberT(LT, ab)
            nu = RO.lab_pair(LT.label(ab))
            for B in subs:
                gens = RC.generators(LT, B)
                elems, psi = RC.image_group(LT, [RC.ab_of(LT, x) for x in gens])
                V_A = RC.induced(LT, m.V, elems, psi)
                L2_A = RC.induced(LT, CT.T.wedge2_rep(m.V), elems, psi)
                want = sum(h1V[RO.lab_str(((nu[0] + c[0]) % 1, (nu[1] + c[1]) % 1))] for c in map(RO.lab_pair, B))
                got = CT.T.h1_classes(V_A, LT.rels)[1]
                got2 = CT.T.h1_classes(L2_A, LT.rels)[1]
                good = got == want and got2 == 2 * len(B)
                ok &= good
                out[f"M{n} nu {LT.label(ab)} |B| {len(B)} gens {gens}"] = [got, want, got2, 2 * len(B)]
    out["holds"] = ok
    return out


def k6_k7(ps_T, ps_L):
    from collections import Counter
    out = {"K6": {}, "K7": {}, "K7 pencil shapes at chi = 1 (route, family, m, k, rank, points)": {}}
    ok6, ok7 = True, True
    shapes = Counter()
    for route, ps in (("T", ps_T), ("L", ps_L)):
        fams = CT.FAMILIES if route == "T" else CL.LFAMILIES
        for n in LEVELS:
            L, chars, make, one = RUN.level(route, n, ps[n])
            chi1 = L.exponents((0, 0)) if route == "T" else one          # chi = 1 in the route's own argument form
            members = [make(ab) for ab in chars]
            two = [m for m in members if m.kind == "two"]
            out["K6"][f"{route} M{n}"] = len(two)
            ok6 &= len(two) == (120 if n == 6 else 0)
            fails = 0
            for m in two:
                # the pencils at chi = 1 and the generic term only: the special classes are located, not read
                Fb, Fi = m.family_modules(m.c_b, chi1), m.family_modules(m.c_int, chi1)
                pens = {f: m.pencil(Fb[f], Fi[f], *fams[f]) for f in fams}
                rational = {pt[1] for pc in pens.values() for pt in pc["points"] if pt[0] == "r"}
                s = next(x for x in m.s_gen if x not in rational)
                t = m.term(m.cls_at(s), chi1)
                for f, pc in pens.items():
                    shapes[f"{route} {f} m={pc['m']} k={pc['k']} rank={pc['rank']} points={len(pc['points'])}"] += 1
                    mod, i0, i1 = RO.H1POS[f]
                    d0 = pc["h0Q"] - (t[mod][i0] - pc["h0S"])
                    if pc["k"] + pc["h0S"] - d0 + pc["m"] - pc["rank"] != t[mod][i1]:
                        fails += 1
            out["K7"][f"{route} M{n}"] = {"two-class members": len(two), "prediction failures": fails}
            ok7 &= fails == 0
    out["K6"]["holds"], out["K7"]["holds"] = ok6, ok7
    out["K7 pencil shapes at chi = 1 (route, family, m, k, rank, points)"] = dict(sorted(shapes.items()))
    return out


def k8():
    out, ok = {}, True
    for route in ("T", "L"):
        rec = RUN.banked(route)
        n_ok = n_all = 0
        for r in rec["A"]:
            if r["lam"] != "1" or r["row"].get("h1(V_eta)") != 1:
                continue
            w1, w2 = r["row"]["W1"]["c1"], r["row"]["W2"]["c1"]
            n_all += 1
            n_ok += (w2["I(W2)"] == -w1["W1"]["I"] and w2["I(L2W2)"] == -w1["L2W1"]["I"])
        out[route] = [n_ok, n_all]
        ok &= n_ok == n_all
    out["holds"] = ok
    return out


def k9(ps_T, ps_L):
    out, ok = {}, True
    for route, ps in (("T", ps_T), ("L", ps_L)):
        L, chars, make, one = RUN.level(route, 6, ps[6])
        chi1 = L.exponents((0, 0)) if route == "T" else one
        p = ps[6]
        two = [m for m in (make(ab) for ab in chars[:60]) if m.kind == "two"][:3]
        for m in two:
            for d0, r in ((4, 2), (9, 3)):
                u, v = m.s_gen[0], m.s_gen[1]
                raw = m.restricted(u, v, chi1, d0)
                plus = m.term(m.cls_at((u + r * v) % p), chi1)
                minus = m.term(m.cls_at((u - r * v) % p), chi1)
                want = [[a + b for a, b in zip(plus[i], minus[i])] for i in range(2)]
                good = raw == want
                ok &= good
                out[f"{route} {m.label} d0 = {d0}"] = {"R": raw, "sum of the two readings": want, "equal": good}
    out["holds"] = ok
    return out


def main():
    t0 = time.time()
    lines = []

    def log(msg):
        line = f"[{time.time() - t0:8.1f}s] {msg}"
        print(line, flush=True)
        lines.append(line)
    ps_T, ps_L = RUN.primes("T"), RUN.primes("L")
    rec = {}
    for route in ("T", "L"):
        rec[f"K1 route {route}"] = RUN.part0(route, log)
    rec["K2"] = k2()
    log(f"K2 holds = {rec['K2']['holds']}")
    rec["K3"] = k3(ps_T, ps_L)
    log(f"K3 holds = {rec['K3']['holds']}")
    rec["K4"] = k4()
    log(f"K4 holds = {rec['K4']['holds']} {[(k, v) for k, v in rec['K4'].items() if k != 'holds']}")
    rec["K5"] = k5(ps_T)
    log(f"K5 holds = {rec['K5']['holds']} ({len(rec['K5']) - 1} subgroup readings)")
    rec.update(k6_k7(ps_T, ps_L))
    log(f"K6 {rec['K6']}; K7 {rec['K7']}")
    rec["K8"] = k8()
    log(f"K8 {rec['K8']}")
    rec["K9"] = k9(ps_T, ps_L)
    log(f"K9 holds = {rec['K9']['holds']} ({len(rec['K9']) - 1} split readings)")
    rec["all hold"] = all(v["passed"] if k.startswith("K1") else v["holds"] for k, v in rec.items() if "holds" in v or "passed" in v)
    log(f"K7 pencil shapes: {rec['K7 pencil shapes at chi = 1 (route, family, m, k, rank, points)']}")
    rec["seconds"] = round(time.time() - t0, 1)
    log(f"all hold = {rec['all hold']}")
    if "--record" in sys.argv:
        (HERE / "controls.json").write_text(json.dumps(rec, indent=1, default=str) + "\n", encoding="utf-8")
        (HERE / "controls_run.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
