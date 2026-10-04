#!/usr/bin/env python3
"""B1534 post-run check S (written after run_terms.py read its outcome; disclosed in FINDINGS §4): every term and every
subgroup count of the sealed run, read again on SnapPy's own presentation, cusp and polished holonomy, with route S's own
members, contributing characters, classes, pencils and special classes.

Why.  Routes E and N share inputs that a slip would reach alike:
  - the group: family_lib's bundle presentation <a, b, t>, with cusp words abAB and t' = t or abt;
  - the coordinates (u, kappa) of the characters;
  - the class basis: route N reads route E's classes, carried by the conjugator.
Route S takes the group, the cusp and the point from SnapPy (b+-LLRR = m135, b++LLRR = m136; sm:B1530's post_run_s
loader, unchanged).  It finds the rest itself:
  - its members: every character of order dividing 4 with h^1(nu (x) rho) >= 1.  Here nu^5 = nu, so V_eta = V; Lemma Q
    puts every count of every twist on these;
  - its contributing characters: Lemma Z' read on SnapPy's peripheral curves, chi such that some factor nu chi, nu^-4 chi,
    nu^2 chi, nu^-3 chi is trivial on P;
  - its own classes: an interior basis and a boundary-type class (route N's Classes);
  - its own pencils and special classes (silver_n.pencil and special_points on SnapPy's group).
It reads every term at c_int, at two generic classes and at every special class, and every subgroup's count.  It uses
sm:B1527's cusp_lib class index, as route N does; route E's exact_lib shares no code with it.
Compared per state, as multisets (the two presentations' characters are not matched one to one):
  - the members by (kappa, h^1, interior dimension, |C_nu|);
  - each member's profile: the sorted terms at the interior class, at the generic classes, at each special class, at the
    one class, and the number of special classes;
  - each member's subgroup counts per class kind, as (order, count) multisets.
Writes post_run_s.json and post_run_s_log.txt."""
import itertools
import json
import sys
import time
import warnings
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402

import silver_n as SN  # noqa: E402

S, N = SN.S, SN.N
PS = S.load(SN.B1530V, "post_run_s", "b1530_post_run_s")       # sm:B1530's SnapPy loader, unchanged
mp.mp.dps = 60
n = 4
GENERIC = (mp.mpf(3) / 7, mp.mpf(-11) / 5)
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def pv(k, words, gens):
    """the exponents of nu on the peripheral words, mod n"""
    return tuple(sum(e * x for e, x in zip(PS.exponent_sums(w, gens), k)) % n for w in words)


def add(a, b, m=1):
    return tuple((x + m * y) % n for x, y in zip(a, b))


def subgroups(C):
    """every subgroup of the finite group C (exponent vectors mod n under addition), by closures of at most three
    elements"""
    Cs = set(C)
    zero = tuple(0 for _ in C[0])

    def closure(gs):
        H = {zero}
        frontier = [zero]
        while frontier:
            new = []
            for h in frontier:
                for g in gs:
                    x = add(h, g)
                    if x not in H:
                        H.add(x)
                        new.append(x)
            frontier = new
        return frozenset(H)
    out = set()
    for r in range(0, 4):
        for gs in itertools.combinations(sorted(Cs), r):
            H = closure(gs)
            assert H <= Cs
            out.add(H)
    return sorted(out, key=lambda H: (len(H), sorted(H)))


def run_state(state):
    t0 = time.time()
    gens, rels, (mer, lon), sl2, info = PS.snappy_group(state)
    L = N.lib()
    G = L.Group(gens, rels, (mer, lon), f"{state} (SnapPy)")
    rho = L.Module({g: PS.four(sl2[g]) for g in gens})
    stn = {"G": G}
    zeta = [mp.mpc(1), mp.mpc(0, 1), mp.mpc(-1), mp.mpc(0, -1)]
    chars = PS.characters(gens, rels, n)
    say(f"{state}: SnapPy {info['name']} = {info['identify']}, generators {gens}, relators {rels}, cusp {[mer, lon]}; "
        f"the four's relator residual {mp.nstr(L.relator_residual(G, rho), 3)}; characters of order dividing {n}: "
        f"{len(chars)}")

    def module(k):
        return L.Module({g: zeta[x] * rho.M[g] for g, x in zip(gens, k)})

    def chi_vals(j):
        return {g: zeta[x] for g, x in zip(gens, j)}

    members = []
    for k in chars:
        V = module(k)
        C = N.Classes(G, V)
        if C.h1 == 0:
            continue
        P = pv(k, (mer, lon), gens)
        kappa = "1" if P == (0, 0) else ("-1" if all((2 * x) % n == 0 for x in P) else f"order {n // 2 if 2 in P else n}")
        ints = C.interior()
        bt = C.boundary_type(ints)
        # Lemma Z' on SnapPy's cusp: chi contributes iff a factor (nu chi, nu^-4 chi, nu^2 chi, nu^-3 chi) is trivial on P
        facs = [k, tuple((-4 * x) % n for x in k), tuple((2 * x) % n for x in k), tuple((-3 * x) % n for x in k)]
        Cnu = [j for j in chars if any(pv(add(f, j), (mer, lon), gens) == (0, 0) for f in facs)]
        rec = {"nu": list(k), "kappa": kappa, "nu on (mer, lon)": list(P), "h1": C.h1, "n": ints.cols,
               "boundary-type": bt.cols, "|C|": len(Cnu), "classes": {}, "terms": {}, "pencils": {}, "checks": True}
        zs = {}
        if C.h1 == 1:
            zs["the class"] = ints[:, 0] if ints.cols == 1 else bt[:, 0]
        else:
            assert C.h1 == 2 and ints.cols == 1 and bt.cols == 1, ("a member outside the two shapes", C.h1, ints.cols)
            c_int, c_b = ints[:, 0], bt[:, 0]
            zs["c_int"] = c_int
            specials = []
            for j in Cnu:
                for which in ("E", "E*", "L2E", "(L2E)*"):
                    Pb, Pi, inf = SN.pencil(stn, V, None, c_b, c_int, chi_vals(j), which)
                    sp = SN.special_points(Pb, Pi)
                    rec["pencils"][f"{j} {which}"] = {"h1(Q)": inf["h1(Q)"], "h2(S)": inf["h2(S)"],
                                                      "generic rank": sp["generic rank"],
                                                      "special": [mp.nstr(s, 20) for s in sp["special"]]}
                    for s in sp["special"]:
                        if not any(abs(s - t) < mp.mpf(10) ** -30 for t in specials):
                            specials.append(s)
            for s in GENERIC:
                assert all(abs(s - t) > mp.mpf(10) ** -10 for t in specials), "a generic class is special"
            zs["c_g1"] = c_b + GENERIC[0] * c_int
            zs["c_g2"] = c_b + GENERIC[1] * c_int
            for i, s in enumerate(specials):
                zs[f"special {i}"] = c_b + s * c_int
                rec["classes"][f"special {i}"] = mp.nstr(s, 25)
        for cname, z in zs.items():
            rec["terms"][cname] = {}
            for j in Cnu:
                T, inf = SN.term(stn, V, None, z, chi_vals(j))
                rec["checks"] &= inf["checks"]
                rec["terms"][cname][str(list(j))] = list(T)
        # Lemma Z' off C_nu: two characters outside it read (0, 0) at the first class
        off = [j for j in chars if j not in Cnu][:2]
        rec["off C (Lemma Z')"] = {}
        z0 = next(iter(zs.values()))
        for j in off:
            T, inf = SN.term(stn, V, None, z0, chi_vals(j))
            rec["off C (Lemma Z')"][str(list(j))] = list(T)
        # the counts
        subs = subgroups(Cnu)
        rec["subgroups"] = len(subs)
        rec["counts"] = {}
        for cname in zs:
            rows = []
            for H in subs:
                sw = sum(rec["terms"][cname][str(list(h))][0] for h in H)
                sl = sum(rec["terms"][cname][str(list(h))][1] for h in H)
                rows.append([len(H), [sw, sl]])
            rec["counts"][cname] = rows
        members.append(rec)
        say(f"  member nu {list(k)} kappa {kappa}: h1 {C.h1}, interior {ints.cols}, |C| {len(Cnu)}, subgroups {len(subs)}, "
            f"special classes {sum(1 for c in zs if c.startswith('special'))}; terms "
            f"{ {c: sorted(Counter(tuple(t) for t in v.values()).items()) for c, v in rec['terms'].items()} } "
            f"({time.time() - t0:.0f} s)")
    return {"SnapPy": info, "members": members, "seconds": round(time.time() - t0)}


def kind(cname):
    if cname in ("c_g1", "c_g2"):
        return "generic"
    if cname.startswith("special"):
        return "special"
    return {"c_int": "interior", "the class": "the class"}[cname]


def profile(m, kappa):
    """a member's profile: (kappa, h1, interior, |C|, number of special classes, sorted term multisets per class kind,
    sorted (order, count) multisets per class kind)"""
    def order_count(r):                     # route S rows are [order, count]; route E rows are {"H", "order", "count"}
        return (r["order"], tuple(r["count"])) if isinstance(r, dict) else (r[0], tuple(r[1]))
    terms, counts = {}, {}
    for cname, tv in m["terms"].items():
        kd = kind(cname)
        ms = tuple(sorted(tuple(t) for t in tv.values()))
        cs = tuple(sorted(order_count(r) for r in m["counts"][cname]))
        terms.setdefault(kd, set()).add(ms)
        counts.setdefault(kd, set()).add(cs)
    nspec = sum(1 for c in m["terms"] if c.startswith("special"))
    return (kappa, m["h1"], m["n"], len(next(iter(m["terms"].values()))), nspec,
            tuple(sorted((k, tuple(sorted(v))) for k, v in terms.items())),
            tuple(sorted((k, tuple(sorted(v))) for k, v in counts.items())))


def main():
    t0 = time.time()
    out = {"started": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "states": {}, "comparisons": {}}
    say(f"B1534 post-run check S, {out['started']}")
    T = json.loads((HERE / "terms.json").read_text())
    KMAP = {"0": "1", "1/2": "-1"}
    allok = True
    for state in ("-LLRR", "+LLRR"):
        rs = run_state(state)
        out["states"][state] = rs
        prof_s = Counter(profile(m, m["kappa"]) for m in rs["members"])
        prof_e = Counter(profile(m, KMAP[m["kappa"]]) for m in T["states"][state]["members"])
        agree = prof_s == prof_e
        checks = all(m["checks"] for m in rs["members"])
        offz = all(tuple(v) == (0, 0) for m in rs["members"] for v in m["off C (Lemma Z')"].values())
        gen = sorted({tuple(r[1]) for m in rs["members"] for rows in m["counts"].values() for r in rows
                      if r[1][0] == r[1][1] != 0})
        three = [(m["nu"], c, r) for m in rs["members"] for c, rows in m["counts"].items() for r in rows
                 if abs(r[1][0]) == 3 and r[1][0] == r[1][1]]
        out["comparisons"][state] = {"members (route S)": len(rs["members"]),
                                     "members (route E)": len(T["states"][state]["members"]),
                                     "profiles agree with route E": agree, "identity checks": checks,
                                     "Lemma Z' off C (0, 0)": offz, "generation-shaped counts (route S)": gen,
                                     "three (route S)": three}
        if not agree:
            out["comparisons"][state]["only in route S"] = [str(p) for p in (prof_s - prof_e)]
            out["comparisons"][state]["only in route E"] = [str(p) for p in (prof_e - prof_s)]
        allok &= agree and checks and offz
        say(f"{state}: members S {len(rs['members'])} / E {len(T['states'][state]['members'])}; profiles agree {agree}; "
            f"identity checks {checks}; Lemma Z' off C {offz}; generation-shaped counts {gen}; three {len(three)}")
    out["all agree"] = allok
    out["seconds"] = round(time.time() - t0)
    say(f"post-run check S: all agree {allok} ({out['seconds']} s)")
    (HERE / "post_run_s.json").write_text(json.dumps(out, indent=1, default=str))
    (HERE / "post_run_s_log.txt").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
