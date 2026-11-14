#!/usr/bin/env python3
"""SM-C8, the partner test, with the addendum sealed before this run (card relays/cards/SM_C8_the-partner-test.md, § 7).
Population, characters and module recipe are B1441's (tier 1), imported unchanged from a checkout of main (first
argument: population(), get(), group_data(), characters() of B1441's several_cusps.py).  The modules and every count are
computed here in floating point by this seat's instrument (relays/sm_c8/calibration/cal_duality.py).
Per module: C1, C2, C3a, the record's index against B1441's histogram; per non-vacuous join (P, V, T_i): S_i, S*_i,
D_ord, the dimension term d_i, the leak, C3b, dim S_i + dim S*_i = h1(T_i; V); where V splits on T_i the card's
original D; plants P1 (V for V*), P2 (a random line for S*_i), P3 (2 dim A_V = h1(dP; V)).
The run stops at the first module on which a control fails, and says so.
    python3 run_c8.py MAIN_CHECKOUT [out.json]"""
import sys, io, json, math, time, random, pathlib, contextlib, collections, warnings
import numpy as np
warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
B1441 = MAIN / "frontier" / "B1441_the_several_cusped_levels" / "verification"
sys.path.insert(0, str(B1441)); sys.path.insert(0, str(HERE / "calibration"))
with contextlib.redirect_stdout(io.StringIO()):
    import several_cusps as SC
import cal_duality as CD
from cal_duality import rank, null, orth
rng = np.random.default_rng(20261114)
PREVIEWED = {"m129", "m125"}


class GroupC:
    def __init__(self, C):
        gens, rels, per = SC.group_data(C)
        self.gens, self.rels, self.periph = gens, rels, per
        self.n, self.k = len(gens), len(per)

    def idx(self, ch): return self.gens.index(ch.lower()), ch.isupper()


def h1_basis(G, lvals):
    lr = [np.array([[v]]) for v in lvals]
    Zl = null(np.vstack([CD.fox(lr, G, r) for r in G.rels]))
    Bl = orth(np.array(lvals).reshape(-1, 1) - 1)
    if Bl.shape[1]:
        P = np.eye(G.n, dtype=complex) - Bl @ Bl.conj().T
        Q = orth(P @ Zl)
    else:
        Q = orth(Zl)
    return Q                                          # columns: a basis of a complement of B1 in Z1, i.e. of H1(M; l)


def check_module(G, V, Vs):
    hb, hbs = V.h0_bd(), Vs.h0_bd()
    dA, dAs = V.dim_A(), Vs.dim_A()
    zero = [c["B"] for c in V.cusps]; zero_s = [c["B"] for c in Vs.cusps]
    all_s = [c["Z"] for c in Vs.cusps]; allv = [c["Z"] for c in V.cusps]
    out = {"h0": [V.h0, Vs.h0], "h1": [V.h1, Vs.h1], "h0_bd": [hb, hbs], "h1_bd": V.h1_bd(), "dimA": [dA, dAs],
           "I": Vs.h1 - V.h1}
    out["C1"] = dA + dAs == V.h1_bd() == Vs.h1_bd()
    out["C2"] = (Vs.h1 - Vs.h0) - (V.h1 - V.h0) == dAs - hbs
    out["C3a"] = V.n_cond(zero) - Vs.n_cond(all_s) == -hb + V.h0 - Vs.h0
    out["P3_fails"] = not (2 * dA == V.h1_bd())
    joins = []
    for i in range(G.k):
        if V.cusps[i]["h1"] == 0:
            joins.append({"i": i, "vacuous": True}); continue
        S = V.line_cocycles(i, np.array([1, 0], dtype=complex))
        Ss = Vs.line_cocycles(i, np.array([0, 1], dtype=complex))
        dS, dSs = V.quot_dim(i, S), Vs.quot_dim(i, Ss)
        nV = V.n_cond([zero[j] if j != i else S for j in range(G.k)])
        nVs0 = Vs.n_cond([zero_s[j] if j != i else Ss for j in range(G.k)])
        nVsall = Vs.n_cond([all_s[j] if j != i else Ss for j in range(G.k)])
        d_i = dS - hb + V.h0 - Vs.h0
        j = {"i": i, "vacuous": False, "dimS": dS, "dimS*": dSs, "D_ord": nV - nVs0, "d": d_i, "leak": nVsall - nVs0,
             "C3b": nV - nVsall == d_i, "Sperp": dS + dSs == V.cusps[i]["h1"]}
        j["P1_fails"] = not (nV - V.n_cond([allv[jj] if jj != i else S for jj in range(G.k)]) == d_i)
        c = Vs.cusps[i]
        rnd = orth(np.hstack([c["Z"] @ (rng.normal(size=(c["Z"].shape[1], 1)) + 0j), c["B"]]))
        j["P2_fails"] = not (nV - Vs.n_cond([all_s[jj] if jj != i else rnd for jj in range(G.k)]) == d_i)
        split = np.allclose(V.cusps[i]["Rm"][0, 1], 0, atol=1e-9) and np.allclose(V.cusps[i]["Rl"][0, 1], 0, atol=1e-9)
        j["split_on_T"] = bool(split)
        if split:
            Qn = V.line_cocycles(i, np.array([0, 1], dtype=complex))
            j["D_orig"] = nV - V.n_cond([zero[jj] if jj != i else Qn for jj in range(G.k)])
        joins.append(j)
    out["joins"] = joins
    return out


def main():
    out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "c8_results.json"
    b1441 = {}
    for f in sorted(B1441.glob("several_cusps_*.json")):
        for e in json.load(open(f)): b1441[e["tag"]] = e
    res = {"entries": [], "stopped": None}
    t00 = time.time()
    for tag, nm, d, i, N in SC.population():
        if N is not None: continue                                     # tier 2 is not part of the card
        ref = b1441.get(tag, {})
        if ref.get("skipped"): res["entries"].append({"tag": tag, "skipped": ref["skipped"]}); continue
        C = SC.get(nm, d, i); G = GroupC(C)
        b1, tors, Nt = SC.homology(G.gens, G.rels); Nn = max(Nt, 2)
        chars = SC.characters(G.gens, G.rels, Nn); triv = tuple([0] * G.n)
        cv = {c: [complex(np.exp(2j * math.pi * e / Nn)) for e in c] for c in chars}
        rnd = random.Random(1)
        ent = {"tag": tag, "root": nm, "cusps": G.k, "N": Nn, "characters": len(chars), "previewed": nm in PREVIEWED,
               "B1441_I_hist": ref.get("I_hist"), "modules": 0, "I_hist": collections.Counter(), "joins": 0, "vacuous": 0,
               "D_ord": collections.Counter(), "leak": collections.Counter(), "d": collections.Counter(),
               "R_leak": 0, "R_dim": 0, "D_orig": collections.Counter(), "split_joins": 0,
               "fails": collections.Counter(), "plants": collections.Counter(), "witness_leak": []}
        t0 = time.time()
        for lc in chars:
            if lc == triv: continue
            Q = h1_basis(G, cv[lc])
            m = Q.shape[1]
            if m == 0: continue
            combos = [[int(a == b) for b in range(m)] for a in range(m)]
            if m > 1: combos += [[rnd.randrange(1, 50) for _ in range(m)] for _ in range(2)]
            for al in chars:
                be = tuple((a - b) % Nn for a, b in zip(al, lc))
                if al == triv or be == triv: continue
                for co in combos:
                    z = Q @ np.array(co, dtype=complex); z = z / np.linalg.norm(z)
                    rho = [np.array([[cv[al][g], z[g] * cv[be][g]], [0, cv[be][g]]], dtype=complex) for g in range(G.n)]
                    V = CD.Module(G, rho); Vs = CD.Module(G, [np.linalg.inv(r).T for r in rho])
                    if not (V.rel_ok and Vs.rel_ok): ent["fails"]["not_a_representation"] += 1; continue
                    r = check_module(G, V, Vs); ent["modules"] += 1; ent["I_hist"][r["I"]] += 1
                    for key in ("C1", "C2", "C3a"):
                        if not r[key]: ent["fails"][key] += 1
                    ent["plants"]["P3_fails"] += r["P3_fails"]
                    for j in r["joins"]:
                        ent["joins"] += 1
                        if j["vacuous"]: ent["vacuous"] += 1; continue
                        for key in ("C3b", "Sperp"):
                            if not j[key]: ent["fails"][key] += 1
                        ent["plants"]["P1_fails"] += j["P1_fails"]; ent["plants"]["P2_fails"] += j["P2_fails"]
                        ent["D_ord"][j["D_ord"]] += 1; ent["leak"][j["leak"]] += 1; ent["d"][j["d"]] += 1
                        if j["leak"] != 0:
                            ent["R_leak"] += 1
                            if len(ent["witness_leak"]) < 3:
                                ent["witness_leak"].append({"l": list(lc), "alpha": list(al), "combo": co, "cusp": j["i"],
                                                            "D_ord": j["D_ord"], "d": j["d"], "leak": j["leak"], "I": r["I"]})
                        elif j["D_ord"] != 0: ent["R_dim"] += 1
                        if j["split_on_T"]: ent["split_joins"] += 1; ent["D_orig"][j["D_orig"]] += 1
                    if sum(ent["fails"].values()):
                        res["stopped"] = {"tag": tag, "l": list(lc), "alpha": list(al), "combo": co, "fails": dict(ent["fails"])}
                        break
                if res["stopped"]: break
            if res["stopped"]: break
        for key in ("I_hist", "D_ord", "leak", "d", "D_orig", "fails", "plants"):
            ent[key] = {str(k): v for k, v in sorted(ent[key].items())}
        ent["I_matches_B1441"] = (ent["B1441_I_hist"] == ent["I_hist"]) if ent["B1441_I_hist"] is not None else None
        ent["seconds"] = round(time.time() - t0, 1)
        res["entries"].append(ent)
        print(tag, "cusps", G.k, "modules", ent["modules"], "I", ent["I_hist"], "B1441", ent["B1441_I_hist"], "joins",
              ent["joins"], "vacuous", ent["vacuous"], "R_leak", ent["R_leak"], "R_dim", ent["R_dim"], "fails", ent["fails"],
              ent["seconds"], "s", flush=True)
        json.dump(res, open(out_path, "w"), indent=1, default=str)
        if res["stopped"]: break
    E = [e for e in res["entries"] if "modules" in e]
    def tot(pred=lambda e: True, key="R_leak"): return sum(e[key] for e in E if pred(e))
    res["summary"] = {
        "entries_run": len(E), "skipped": sum("skipped" in e for e in res["entries"]), "stopped": res["stopped"],
        "modules": tot(key="modules"), "joins": tot(key="joins"), "vacuous": tot(key="vacuous"),
        "I_matches_B1441_on": [sum(1 for e in E if e["I_matches_B1441"]), sum(1 for e in E if e["I_matches_B1441"] is not None)],
        "R_leak_joins": tot(), "R_dim_joins": tot(key="R_dim"),
        "R_leak_joins_without_previewed": tot(lambda e: not e["previewed"]),
        "R_dim_joins_without_previewed": tot(lambda e: not e["previewed"], "R_dim"),
        "entries_with_R_leak": [e["tag"] for e in E if e["R_leak"]][:40],
        "plants": {k: sum(e["plants"].get(k, 0) for e in E) for k in ("P1_fails", "P2_fails", "P3_fails")},
        "seconds": round(time.time() - t00, 1)}
    s = res["summary"]
    s["outcome"] = ("stopped: a control failed" if res["stopped"] else "R_leak" if s["R_leak_joins"] else
                    "R_dim" if s["R_dim_joins"] else "N")
    json.dump(res, open(out_path, "w"), indent=1, default=str)
    print(json.dumps(s, indent=1, default=str))


if __name__ == "__main__":
    main()
