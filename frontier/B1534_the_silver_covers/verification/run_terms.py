#!/usr/bin/env python3
"""B1534 sealed run: every twisted term of every member of m135 and m136 at every class the pencils make distinct, in routes E
and N; then every abelian cover's count.  Run only after the seal.  Writes terms.json and run_log.txt.

Part A (route E, exact).  For each state, member nu, and contributing character chi (Lemma Z'):
  - one-class members (h^1(V_eta) = 1): T(nu, chi, the class);
  - two-class members (m135's u = (0, 1/2), (1/2, 0)): the pencils of the four modules at every chi give the special s (Lemma J);
    T(nu, chi, c) is read at c_int, at two generic classes c_{g1}, c_{g2} (s = 3/7 and -11/5, checked off every special s), and
    at every special s (rational: directly; a conjugate pair over K: through the restriction of scalars).
Part B (route N, 60 digits).  The same terms at route E's classes carried by the conjugator; route N's own pencils and special
  s, compared with route E's; at a conjugate pair route N reads both complex roots directly.
Part C (the counts).  For each member, each class read, and each subgroup H of the contributing group, S(nu, c, H) =
  sum over chi in H of T(nu, chi, c).  Generation-shaped: S = (a, a), a != 0; three: |a| = 3.
Part D, route C, is run_route_c.py, after this run."""
import json
import sys
import time
import warnings
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import mpmath as mp

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import silver_lib as SL  # noqa: E402
import silver_n as SN  # noqa: E402

E = SL.E
GEN1, GEN2 = Fraction(3, 7), Fraction(-11, 5)
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def kstr(x):
    return str(x.num(mp)) if hasattr(x, "num") else str(x)


def kfrac(x):
    """a rational element of K as a Fraction, or None"""
    try:
        return x.rational()
    except Exception:
        return None


def main():
    t0 = time.time()
    out = {"started": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "states": {}}
    say(f"B1534 sealed run, {out['started']}")
    for state in ("-LLRR", "+LLRR"):
        st = SL.setup(state)
        stn = SN.setup(st["sign"], st["word"], st["rho"])
        rec = {"name": st["name"], "conjugator": stn["xinfo"], "members": []}
        for m in SL.members(st):
            C = SL.contributing(st, m)
            mrec = {"u": [str(x) for x in m["u"]], "kappa": str(m["kappa"]), "h1": m["h1"], "n": m["n"],
                    "contributing": [SL.key(wk) for wk in C], "classes": {}, "pencils": {}, "terms": {},
                    "route N": {}, "agree": True}
            chis = {SL.key(wk): SL.char(st, *wk) for wk in C}
            V_n, lval_n = SN.member_V(stn, m["u"], m["kappa"])
            # ---------------------------------------------------------------- the classes
            classes = {}            # name -> ("K", s) | ("one", None) | ("int", None) | ("Q", (alpha, beta, d))
            if m["h1"] == 1:
                classes["the class"] = ("one", None)
            else:
                specials_K, specials_Q = [], []
                for ck, chi in chis.items():
                    for which in ("E", "E*", "L2E", "(L2E)*"):
                        Pb, Pi, h1Q, h2S = SL.pencil(st, m, chi, which)
                        sp = SL.special_points(Pb, Pi)
                        Pbn, Pin, infon = SN.pencil(stn, V_n, lval_n, SN.carry(stn, m["c_b"]), SN.carry(stn, m["c_int"]),
                                                    SN.char(stn, *next(wk for wk in C if SL.key(wk) == ck)), which)
                        spn = SN.special_points(Pbn, Pin)
                        e_vals = [s.num(mp) for s in sp["rational"]]
                        for (c0, c1, c2) in sp["quadratic"]:
                            a, b, c = c2.num(mp), c1.num(mp), c0.num(mp)
                            disc = mp.sqrt(b * b - 4 * a * c)
                            e_vals += [(-b + disc) / (2 * a), (-b - disc) / (2 * a)]
                        match = (sp["generic rank"] == spn["generic rank"] and len(e_vals) == len(spn["special"]) and
                                 all(any(abs(x - y) < mp.mpf(10) ** -25 for y in spn["special"]) for x in e_vals))
                        mrec["pencils"][f"{ck} {which}"] = {"h1(Q)": h1Q, "h2(S)": h2S, "generic rank (E)": sp["generic rank"],
                                                            "generic rank (N)": spn["generic rank"],
                                                            "special (E)": [mp.nstr(x, 20) for x in e_vals],
                                                            "special (N)": [mp.nstr(x, 20) for x in spn["special"]],
                                                            "quadratic over K (E)": len(sp["quadratic"]), "agree": match}
                        mrec["agree"] &= match
                        for s in sp["rational"]:
                            if not any(s == t for t in specials_K):
                                specials_K.append(s)
                        for q in sp["quadratic"]:
                            if q not in specials_Q:
                                specials_Q.append(q)
                for s in (GEN1, GEN2):
                    assert not any(E.K.of(s) == t for t in specials_K), "a generic class is special"
                classes["c_int"] = ("int", None)
                classes["c_g1"] = ("K", E.K.of(GEN1))
                classes["c_g2"] = ("K", E.K.of(GEN2))
                for i, s in enumerate(specials_K):
                    classes[f"special {i} (s = {kstr(s)})"] = ("K", s)
                for i, (c0, c1, c2) in enumerate(specials_Q):
                    # s = alpha + beta sqrt(d): alpha = -c1 / (2 c2), beta = 1 / (2 c2), d = c1^2 - 4 c2 c0
                    alpha, beta, d = -c1 / (c2 * 2), E.ONE / (c2 * 2), c1 * c1 - c2 * c0 * 4
                    classes[f"conjugate pair {i}"] = ("Q", (alpha, beta, d))
            mrec["classes"] = {k: (v[0], kstr(v[1]) if v[0] == "K" else None) for k, v in classes.items()}
            # ---------------------------------------------------------------- the terms, both routes
            for cname, (kind, val) in classes.items():
                mrec["terms"][cname], mrec["route N"][cname] = {}, {}
                for wk in C:
                    ck = SL.key(wk)
                    chi, chin = chis[ck], SN.char(stn, *wk)
                    if kind == "one":
                        c = m["classes"]["the class"]
                        T, _ = SL.term(st, m, c, chi)
                        Tn, inf = SN.term(stn, V_n, lval_n, SN.carry(stn, c), chin)
                        Tns = [Tn]
                    elif kind == "int":
                        T, _ = SL.term(st, m, m["c_int"], chi)
                        Tn, inf = SN.term(stn, V_n, lval_n, SN.carry(stn, m["c_int"]), chin)
                        Tns = [Tn]
                    elif kind == "K":
                        c = SL.lin(m["c_b"], m["c_int"], E.ONE, val)
                        T, _ = SL.term(st, m, c, chi)
                        Tn, inf = SN.term(stn, V_n, lval_n, SN.carry(stn, c), chin)
                        Tns = [Tn]
                    else:
                        alpha, beta, d = val
                        T, _ = SL.term_quadratic(st, m, alpha, beta, d, chi)
                        Tns = []
                        for sgn in (1, -1):
                            sval = alpha.num(mp) + sgn * beta.num(mp) * mp.sqrt(d.num(mp))
                            z = SN.carry(stn, m["c_b"]) + sval * SN.carry(stn, m["c_int"])
                            Tn, inf = SN.term(stn, V_n, lval_n, z, chin)
                            Tns.append(Tn)
                    agree = all(x == T for x in Tns) and inf["checks"]
                    mrec["agree"] &= agree
                    mrec["terms"][cname][ck] = list(T)
                    mrec["route N"][cname][ck] = {"T": [list(x) for x in Tns], "checks": inf["checks"],
                                                  "margins": inf["margins"]}
                say(f"{state} u {mrec['u']} kappa {mrec['kappa']} {cname}: "
                    f"{ {k: tuple(v) for k, v in mrec['terms'][cname].items()} } ({time.time() - t0:.0f} s)")
            # ---------------------------------------------------------------- the counts
            subs = SL.subgroups(C)
            counts = {}
            for cname in classes:
                rows = []
                for H in subs:
                    sw = sum(mrec["terms"][cname][SL.key(h)][0] for h in H)
                    sl = sum(mrec["terms"][cname][SL.key(h)][1] for h in H)
                    rows.append({"H": sorted(SL.key(h) for h in H), "order": len(H), "count": [sw, sl]})
                counts[cname] = rows
            mrec["counts"] = counts
            mrec["generation-shaped counts"] = sorted({tuple(r["count"]) for rows in counts.values() for r in rows
                                                      if r["count"][0] == r["count"][1] != 0})
            mrec["three"] = [(cname, r) for cname, rows in counts.items() for r in rows if abs(r["count"][0]) == 3 ==
                             abs(r["count"][1]) and r["count"][0] == r["count"][1]]
            rec["members"].append(mrec)
            say(f"{state} u {mrec['u']} kappa {mrec['kappa']}: generation-shaped counts {mrec['generation-shaped counts']}, "
                f"three {len(mrec['three'])}, routes agree {mrec['agree']}")
        out["states"][state] = rec
    out["seconds"] = round(time.time() - t0)
    (HERE / "terms.json").write_text(json.dumps(out, indent=1, default=str))
    (HERE / "run_log.txt").write_text("\n".join(LOG) + "\n")
    say(f"done ({out['seconds']} s)")


if __name__ == "__main__":
    main()
