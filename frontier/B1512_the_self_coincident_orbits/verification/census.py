"""B1512 -- THE SELF-COINCIDENT ORBITS: the sealed run (PREREGISTRATION.md section 7; the seal's digest is in SEAL_LEDGER).

Run as:  python3 census.py --record   (writes census_run.txt)

0  the banked identity: B1511's M4 case-(b) row (the (0,5) class's polynomial equals B1511 Part C1, and the count at the first
   prime-root pair of q^2 - 7q + 1 is I(W1) = +1, I(W2) = -1, I(L2 W1) = 0).  The run stops if it fails.
A  the lemmas re-checked inside the run: the involution (K1), nu o iota = (nu_F^-1, lam) (K2), the Galois classes of M5's four and M6's
   eight self-coincident orbits (K3), the duality D and the strong inversion E (K8), the amphichiral alpha (K10), and the class maps
   under alpha.
B  for each Galois class: P(q, s) over Q (reconstructed from the first member of the class's first orbit), then at one fresh prime:
   every member of both orbits of the class has the same polynomial mod p (deck, involution, Galois), and the polynomial mod p does
   not depend on the choice of the root of unity (zeta -> zeta^k).  Its symmetries (palindromic in s, reciprocal, q -> 1/q), whether
   it equals B1509's Q at q^n, Lemma D's identity P(1/q, s) = s^4 P(q, 1/s) / P(q, 0), how the classes of a level are related
   (equal, reciprocal; Lemma E makes M5's two classes equal), and B1511's banked GF(p) degrees (deg q^(16n) P(q, lam), multiplicities
   of q and q - 1) reproduced for every pair.
C  for each class and lam in mu_4: the real exceptional polynomial (lam = +-1: P(q, lam); lam = +-i: gcd(Re, Im)), its factors over Q
   and their positive real roots other than 1 (exact isolation; arb count cross-check); the set of positive roots is closed under
   q -> 1/q (Lemma D).
D  at each factor with such roots: the numeric fibre data at every positive root (60 digits; rank of the coboundary matrix and the
   kernel dimensions of (S - lam)^j on H^1) for every member of the class; and over GF(p) at the three smallest primes p > 1000,
   p = 1 mod lcm(N, 4), at which the factor is squarefree of full degree with a root, at every root: the fibre data and B1511's
   case-(b) counts (h^1 of L, V_nu, V_eta, V_eta*; I(W1), I(L2 W1), I(W2), I(L2 W2) for every basis class and c1 + c2) for every
   member of both orbits of the class.
E  the 32 pairs' table and the completed per-level table."""
import json
import math
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import selfco_lib as L  # noqa: E402

q, s = L.q, L.s
T, TC = L.T, L.TC
REC1511 = L.B1511 / "tower_census_run.txt"
LEVELS = (4,) if "--dry" in sys.argv else (5, 6)


def lams_of_pairs(n):
    """the lam exponents of the sealed pairs: M5 every lam, M6 lam = +-1 (B1511 resolved lam = +-i there); the dry run every lam"""
    return (0, 2) if n == 6 else (0, 1, 2, 3)


def banked_identity(log):
    rec = json.loads(REC1511.read_text(encoding="utf-8"))
    row = [r for r in rec["C1"]["4"] if r["lam"] == "1" and tuple(r["orbit"][0]) == (0, 5)][0]
    Pb = sp.sympify(row["P(q,s)"], locals={"q": q, "s": s})
    P, _ = L.reconstruct_P((0, 5), 4, 15)
    same = sp.simplify(P - Pb) == 0
    cc = L.CoverCache(4)
    p, roots = L.primes_with_roots(q ** 2 - 7 * q + 1, 60, 1)[0]
    rows = L.counts_at(cc, p, roots[0], [(0, 5)], 15, (0,))
    c = rows["(0, 5)|0"]["counts"]
    vals = (c["W1"]["c1"]["I"], c["W2"]["c1"]["I"], c["W1"]["c1"]["I_L2"])
    ok = same and vals == (1, -1, 0)
    log(f"banked identity: P equals B1511 C1 {same}; count at p = {p}, q = {roots[0]}: {vals}; {'PASS' if ok else 'FAIL'}")
    return {"P equals B1511 Part C1": same, "prime": p, "root": roots[0], "(I(W1), I(W2), I(L2 W1))": list(vals), "pass": ok}


def part_a():
    out = {"involution": L.involution_checks(), "iota_on_characters": [L.iota_on_characters(n) for n in range(1, 7)],
           "duality_and_strong_inversion": L.duality_checks(), "amphichirality": L.amphichiral_checks(),
           "symmetries": L.symmetry_table(), "classes": {}, "alpha_class_map": {}}
    for n in LEVELS:
        N, orbs, idx, sc = L.self_coincident_orbits(n)
        classes = {}
        for k, o in sc:
            cl = tuple(sorted({idx[c] for c in L.galois_class(o[0], N)}))
            classes.setdefault(cl, []).append({"orbit_index": k, "orbit": o,
                                               "Galois-closed within orbit and inverse": L.galois_closure_in_orbit_union(o[0], N)})
        out["classes"][f"level_{n}"] = {"N": N, "classes": [{"orbits": list(cl), "members": rows} for cl, rows in sorted(classes.items())]}
        cls = sorted(classes)
        amap = {}
        for cl in cls:
            k0 = cl[0]
            img = idx[L.alpha_on_character(orbs[k0][0], N)]
            amap[str(list(cl))] = [list(c) for c in cls if img in c][0]
        out["alpha_class_map"][f"level_{n}"] = amap
    return out


def q_power_relation(P, n):
    return sp.simplify(sp.expand(P - T.Q_MONIC.subs(q, q ** n))) == 0


def banked_degrees(n, P, orbit_index, l, rec):
    """B1511's GF(p) record for this pair against the exact polynomial: deg of q^(16n) P(q, lam), multiplicity of q and q - 1, rest"""
    row = [pr for pr in rec["C2"].get(str(n), {}).get("pairs", []) if pr["orbit_index"] == orbit_index and pr["lam"] == l]
    if not row:
        return None
    banked = sorted({(x["deg_f"], x["mult_q"], x["mult_q-1"], x["deg_gcd_without_q_and_q-1"]) for x in row[0]["per_prime"]})
    dom = sp.QQ_I if l in (1, 3) else sp.QQ
    f = sp.expand(sp.expand(P.subs(s, sp.I ** l)) * q ** (16 * n))
    fp = sp.Poly(f, q, domain=dom)
    deg = fp.degree()
    mq = min(m[0] for m in fp.monoms())
    g = sp.Poly(sp.expand(fp.as_expr() / q ** mq), q, domain=dom)
    one = sp.Poly(q - 1, q, domain=dom)
    m1 = 0
    while g.degree() > 0 and g.eval(1) == 0:
        g = sp.quo(g, one)
        m1 += 1
    mine = (deg, mq, m1)
    return {"banked (deg f, mult q, mult q-1, rest of gcd)": [list(b) for b in banked], "exact (deg f, mult q, mult q-1)": list(mine),
            "agrees": all(tuple(b[:3]) == mine for b in banked)}


def part_b(log, a):
    rec = json.loads(REC1511.read_text(encoding="utf-8"))
    out = {}
    for n in LEVELS:
        info = a["classes"][f"level_{n}"]
        N = info["N"]
        mod = N * 4 // math.gcd(N, 4)
        rows = []
        for cl in info["classes"]:
            rep_orbit = cl["members"][0]["orbit"]
            ab = tuple(rep_orbit[0])
            t = time.time()
            P, rr = L.reconstruct_P(ab, n, N, log=None)
            log(f"B: level {n} class {cl['orbits']} from {ab}: reconstructed with {rr['primes_used']} primes, fresh checks "
                f"{rr['all_fresh_agree']} ({time.time() - t:.1f}s)")
            # every member of both orbits of the class, at one fresh prime
            p0 = L.next_prime_1_mod(mod, rr["last_prime"] + 10 ** 6)
            mp = T.ModP(p0, N)
            red_ = [[(int(c.p) * pow(int(c.q), -1, p0)) % p0 for c in row] for row in _coeff_table(P, n)]
            orbs_all = _class_members(n, N, cl["orbits"])
            member_ok = {}
            for c in orbs_all:
                cs = [L._pad(x, 32 * n + 1) for x in L.coeffs_modp(mp, c, n)]
                member_ok[str(c)] = cs == red_
            units = [k for k in range(2, N) if math.gcd(k, N) == 1][:3]
            choice_ok = {k: L.modp_choice_independent(ab, n, N, p0, k) for k in units}
            sym = L.symmetries(P)
            row = {"class_orbits": cl["orbits"], "representative": ab, "P(q,s)": str(P), "P factored": str(sp.factor(P)),
                   "reconstruction": rr, "check_prime": p0, "every member of the class agrees mod p": all(member_ok.values()),
                   "members_checked": len(member_ok), "independent of the root-of-unity choice (k: ok)": choice_ok,
                   "symmetries": sym, f"equals Q(q^{n}, s)": q_power_relation(P, n),
                   "Lemma D: P(1/q, s) = s^4 P(q, 1/s) / P(q, 0)": L.reciprocal_in_q_identity(P),
                   "banked_degrees": {}}
            for o in cl["orbits"]:
                for l in (0, 1, 2, 3):
                    bd = banked_degrees(n, P, o, l, rec)
                    if bd is not None:
                        row["banked_degrees"][f"orbit {o}, lam {['1', 'i', '-1', '-i'][l]}"] = bd
            row["banked_degrees_all_agree"] = all(v["agrees"] for v in row["banked_degrees"].values())
            rows.append({"P": P, **row})
            log(f"B: level {n} class {cl['orbits']}: members agree {row['every member of the class agrees mod p']}, "
                f"palindromic {sym['palindromic in s']}, reciprocal {sym['reciprocal up to the constant term']}, "
                f"equals Q(q^{n}, s) {row[f'equals Q(q^{n}, s)']}, banked degrees {row['banked_degrees_all_agree']}")
        # relations between the classes of the level
        rel = []
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                Pi, Pj = rows[i]["P"], rows[j]["P"]
                ci0 = L.coeff_list(Pi)[0]
                rel.append({"classes": [rows[i]["class_orbits"], rows[j]["class_orbits"]],
                            "equal": sp.simplify(Pi - Pj) == 0,
                            "P_j = reciprocal of P_i": sp.simplify(sp.expand(s ** 4 * Pi.subs(s, 1 / s)) - ci0 * Pj) == 0,
                            "P_j(q, s) = P_i(1/q, s)": sp.simplify(sp.expand(Pi.subs(q, 1 / q) - Pj)) == 0})
        amap = a["alpha_class_map"][f"level_{n}"]
        d9 = []
        for r in rows:
            img = amap[str(list(r["class_orbits"]))]
            tgt = [x for x in rows if list(x["class_orbits"]) == img][0]
            d9.append({"class": r["class_orbits"], "alpha image": img,
                       "P_image(q, s) = P(1/q, s)": sp.simplify(sp.expand(tgt["P"] - r["P"].subs(q, 1 / q))) == 0})
        log(f"B: level {n} D9 (Lemma A) {[(x['class'], x['alpha image'], x['P_image(q, s) = P(1/q, s)']) for x in d9]}")
        out[f"level_{n}"] = {"N": N, "classes": rows, "relations": rel, "D9 (Lemma A)": d9}
    return out


def _coeff_table(P, n):
    c = L.coeff_list(P)
    L_ = 32 * n + 1
    out = []
    for k in range(5):
        e = sp.expand(c[k] * q ** (16 * n))
        Pp = sp.Poly(e, q)
        coeffs = [sp.Rational(Pp.coeff_monomial(q ** d)) for d in range(L_)]
        out.append(coeffs)
    return out


def _class_members(n, N, orbit_indices):
    chars, N2, orbs, idx = TC.orbit_table(n)
    return [c for k in orbit_indices for c in orbs[k]]


def part_c(log, b):
    out = {}
    for n in LEVELS:
        rows = []
        for cl in b[f"level_{n}"]["classes"]:
            P = cl["P"]
            for l in range(4):
                G, info = L.specialisation(P, l)
                rep = L.positive_roots_report(G)
                roots_all = sorted(sp.Float(x, 30) for f in rep for x in f["positive_roots_not_1"])
                closed = all(any(abs(sp.Float(1, 30) / x - y) < sp.Float(10) ** -8 for y in roots_all) for x in roots_all)
                rows.append({"class_orbits": cl["class_orbits"], "lam": ["1", "i", "-1", "-i"][l], "l": l, "info": info,
                             "real exceptional polynomial": None if G is None else str(G.as_expr()), "factors": rep,
                             "has positive root not 1": any(f["positive_roots_not_1"] for f in rep),
                             "positive roots closed under q -> 1/q (Lemma D)": closed})
                log(f"C: level {n} class {cl['class_orbits']} lam {['1', 'i', '-1', '-i'][l]}: factors "
                    f"{[(f['factor'], f['positive_roots_not_1']) for f in rep]}")
        out[f"level_{n}"] = rows
    return out


def part_d(log, b, c):
    out = []
    for n in LEVELS:
        N = b[f"level_{n}"]["N"]
        mod = N * 4 // math.gcd(N, 4)
        cc = L.CoverCache(n)
        for row in c[f"level_{n}"]:
            members = _class_members(n, N, row["class_orbits"])
            for fac in row["factors"]:
                if not fac["positive_roots_not_1"]:
                    continue
                g0 = sp.sympify(fac["factor"], locals={"q": q})
                l = row["l"]
                t = time.time()
                pos = [r for r in sp.real_roots(sp.Poly(g0, q)) if r.is_positive and r != 1]
                numeric = []
                for alpha in pos:
                    for ab in members:
                        d = L.fibre_data_numeric(ab, N, n, alpha, l)
                        numeric.append({"q": str(sp.N(alpha, 15)), "nu": ab, **d})
                modp = []
                for p, roots in L.primes_with_roots(g0, mod, 3):
                    for r_ in roots:
                        rows_ = L.counts_at(cc, p, r_, members, N, (l,))
                        modp.append({"p": p, "q mod p": r_, "rows": rows_})
                vals_W1 = sorted({v["I"] for x in modp for rr in x["rows"].values() for v in rr["counts"]["W1"].values()})
                vals_W2 = sorted({v["I"] for x in modp for rr in x["rows"].values() for v in rr["counts"]["W2"].values()})
                vals_L2 = sorted({v["I_L2"] for x in modp for rr in x["rows"].values() for k in ("W1", "W2") for v in rr["counts"][k].values()})
                fib_modp = sorted({(rr["fibre"]["rank_B"], tuple(rr["fibre"]["ker_dims"])) for x in modp for rr in x["rows"].values()})
                fib_num = sorted({(d["rank_B"], tuple(d["ker_dims"])) for d in numeric})
                h1s = sorted({(rr["counts"]["h1(L)"], rr["counts"]["h1(V_nu)"], rr["counts"]["h1(V_eta)"], rr["counts"]["h1(V_eta*)"])
                              for x in modp for rr in x["rows"].values()})
                datas = sorted({tuple(v["data(a0,a1,t0,r1)"]) for x in modp for rr in x["rows"].values() for v in rr["counts"]["W1"].values()})
                entry = {"level": n, "class_orbits": row["class_orbits"], "lam": row["lam"], "factor": fac["factor"],
                         "positive_roots": fac["positive_roots_not_1"], "numeric_fibre": numeric, "numeric_fibre_values": [list(x) for x in fib_num],
                         "mod_p": modp, "prime_root_pairs": len(modp), "members": len(members),
                         "W1 values": vals_W1, "W2 values": vals_W2, "L2 values": vals_L2, "fibre values mod p": [list(x) for x in fib_modp],
                         "h1 (L, V_nu, V_eta, V_eta*) values": [list(x) for x in h1s], "W1 data values": [list(x) for x in datas],
                         "uniform": len(vals_W1) == 1 and len(vals_W2) == 1 and len(fib_modp) == 1}
                out.append(entry)
                log(f"D: level {n} class {row['class_orbits']} lam {row['lam']} factor {fac['factor']}: {len(modp)} prime-root pairs x "
                    f"{len(members)} members; numeric fibre {fib_num}; mod p fibre {fib_modp}; h1 {h1s}; W1 {vals_W1} W2 {vals_W2} "
                    f"L2 {vals_L2} data {datas} ({time.time() - t:.1f}s)")
    return out


def part_e(b, c, d, a=None):
    """the sealed pairs (M5: every orbit, every lam; M6: every orbit, lam = +-1) and the completed per-level rows"""
    pairs = []
    for n in LEVELS:
        for row in c[f"level_{n}"]:
            if row["l"] not in lams_of_pairs(n):
                continue
            for o in row["class_orbits"]:
                pts = [x for x in d if x["level"] == n and x["class_orbits"] == row["class_orbits"] and x["lam"] == row["lam"]]
                fires = any(any(v != 0 for v in x["W1 values"]) for x in pts)
                pairs.append({"level": n, "orbit_index": o, "lam": row["lam"], "real exceptional points": [r for x in pts for r in x["positive_roots"]],
                              "W1 values": sorted({v for x in pts for v in x["W1 values"]}),
                              "W2 values": sorted({v for x in pts for v in x["W2 values"]}),
                              "fires": fires})
    decided_i = []
    for n in LEVELS:
        for row in c[f"level_{n}"]:
            if row["l"] not in lams_of_pairs(n):
                decided_i.append({"level": n, "class_orbits": row["class_orbits"], "lam": row["lam"],
                                  "positive root not 1": row["has positive root not 1"]})
    # D8 (Lemma D on the counts): W2 at the reciprocal factor with lam^-1 is minus W1 at the factor with lam
    def monic(fs):
        P = sp.Poly(sp.sympify(fs, locals={"q": q}), q)
        return sp.Poly(P.monic().as_expr(), q)

    def recip(fs):
        P = sp.Poly(sp.sympify(fs, locals={"q": q}), q)
        R = sp.Poly(sp.expand(q ** P.degree() * P.as_expr().subs(q, 1 / q)), q)
        return sp.Poly(R.monic().as_expr(), q)

    inv_l = {"1": "1", "-1": "-1", "i": "-i", "-i": "i"}
    d8 = []
    for x in d:
        partner = [y for y in d if y["level"] == x["level"] and y["class_orbits"] == x["class_orbits"] and y["lam"] == inv_l[x["lam"]]
                   and monic(y["factor"]) == recip(x["factor"])]
        if not partner:
            d8.append({"level": x["level"], "class_orbits": x["class_orbits"], "lam": x["lam"], "factor": x["factor"], "partner_found": False})
            continue
        y = partner[0]
        d8.append({"level": x["level"], "class_orbits": x["class_orbits"], "lam": x["lam"], "factor": x["factor"], "partner_found": True,
                   "W1 here": x["W1 values"], "W2 at the reciprocal factor, lam^-1": y["W2 values"],
                   "holds": sorted(-v for v in x["W1 values"]) == y["W2 values"]})
    d10 = []
    if a is not None:
        for x in d:
            img = a["alpha_class_map"][f"level_{x['level']}"][str(list(x["class_orbits"]))]
            partner = [y for y in d if y["level"] == x["level"] and list(y["class_orbits"]) == img and y["lam"] == x["lam"]
                       and monic(y["factor"]) == recip(x["factor"])]
            if not partner:
                d10.append({"level": x["level"], "class_orbits": x["class_orbits"], "lam": x["lam"], "factor": x["factor"], "partner_found": False})
                continue
            y = partner[0]
            d10.append({"level": x["level"], "class_orbits": x["class_orbits"], "lam": x["lam"], "factor": x["factor"], "partner_found": True,
                        "alpha image class": img, "holds": x["W1 values"] == y["W1 values"] and x["W2 values"] == y["W2 values"]})
    return {"D8 (Lemma D on the counts)": d8, "D8 holds everywhere": all(r.get("holds") for r in d8) if d8 else None,
            "D10 (Lemma A on the counts)": d10, "D10 holds everywhere": all(r.get("holds") for r in d10) if d10 else None,
            "pairs": pairs, "count": len(pairs),
            "fires_by_level": {f"level_{n}": any(p["fires"] for p in pairs if p["level"] == n) for n in LEVELS},
            "pairs outside the sealed set (B1511 resolved them; a check)": decided_i}


def main():
    t0 = time.time()
    lines = []

    def log(msg):
        line = f"[{time.time() - t0:7.1f}s] {msg}"
        print(line, flush=True)
        lines.append(line)

    out = {"banked_identity": banked_identity(log)}
    if not out["banked_identity"]["pass"]:
        out["stopped"] = "the banked identity failed"
        return out, lines
    a = part_a()
    out["A"] = a
    log(f"A: involution {all(v for k, v in a['involution'].items() if isinstance(v, bool))}; iota on characters "
        f"{[x['characters not killing it'] for x in a['iota_on_characters']]}; duality and strong inversion "
        f"{all(v for k, v in a['duality_and_strong_inversion'].items() if isinstance(v, bool))}; amphichirality "
        f"{all(v for k, v in a['amphichirality'].items() if isinstance(v, bool))}; alpha class maps {a['alpha_class_map']}")
    b = part_b(log, a)
    out["B"] = {k: {"N": v["N"], "classes": [{kk: vv for kk, vv in r.items() if kk != "P"} for r in v["classes"]], "relations": v["relations"],
                    "D9 (Lemma A)": v["D9 (Lemma A)"]} for k, v in b.items()}
    c = part_c(log, b)
    out["C"] = c
    d = part_d(log, b, c)
    out["D"] = d
    out["E"] = part_e(b, c, d, a)
    log(f"E: {out['E']['count']} pairs; fires by level {out['E']['fires_by_level']}")
    out["seconds"] = round(time.time() - t0, 1)
    return out, lines


if __name__ == "__main__":
    res, lines = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    if "--record" in sys.argv and "--dry" not in sys.argv:
        (HERE / "census_run.txt").write_text(txt + "\n", encoding="utf-8")
        (HERE / "census_log.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    if "--dry" in sys.argv and "--record" in sys.argv:
        (HERE / "census_dry_run_level4.txt").write_text(txt + "\n", encoding="utf-8")
    print(txt[:2000])
