"""(the golden covers dossier, section 6: a draft for the next arc; not sealed, not run) the next arc's read-out: the predictions from the records, once.  Pure evaluate() for synthetic-row controls.

Records: run_R.jsonl, run_P.jsonl (one row per (cover, character); a 'done' row per cover), run_N.jsonl (one row per selected
cyclic subgroup: cover, generator, order, (n(1), n(rho)) of N_e by route N).  The manifest: population_draft.members() and each
cover's characters (counted by structure).
  P1  routes R' and P' agree at every own character (every field).
  P2  Lemma B: at every own character, n(c) = n(-c) and n(rho c) = n(rho (-c)), in each route.
  P3  route N's (n(1), n(rho)) on N_e equals Lemma A's sums at every cyclic subgroup it reads (both routes' sums).
  P4  some cyclic cover N_e of the population has room >= 3 at the trivial character: min(1 + n(1)(N_e), n(rho)(N_e)) >= 3,
      read by Lemma A's sums in both routes and confirmed by route N.
  P5  on d5.2 or d5.3, some own character of order 3 has n(c) >= 1 and n(rho c) >= 1 (both routes).
  P6  some own character of the population has min(capW, capL2) >= 3 at nu = c itself (both routes).
Coverage: a population-wide prediction is True only on complete records (every cover's every character exactly once in both
routes, and route N at every selected subgroup); a refuting row decides False whatever the coverage."""
import json
from math import gcd


def neg(c, m):
    return tuple((-x) % m for x in c)


def order_of(c, m):
    g = m
    for x in c:
        g = gcd(g, x)
    return m // g if any(c) else 1


def sums(rowsby, c, m):
    """Lemma A: (n(1), n(rho)) of N_c from one route's rows at the powers of c"""
    k = order_of(c, m)
    n1 = nr = 0
    for j in range(k):
        key = tuple((x * j) % m for x in c)
        s = rowsby[key]["S"]
        n1 += s["n(nu)"]
        nr += s["n(rho nu)"]
    return n1, nr


def evaluate(R, P, Nrows, manifest):
    """R, P: {(state, cover): {c: row}}; Nrows: list; manifest: {(state, cover): (m, number of characters)}"""
    out, pred = {}, {}
    complete = all(len(R.get(k, {})) == v[1] and len(P.get(k, {})) == v[1] for k, v in manifest.items())
    dis = [(k, c) for k in R for c in R[k] if k in P and c in P[k] and R[k][c]["S"] != P[k][c]["S"]]
    pred["P1"] = False if dis else (True if complete else None)
    lb = []
    for rt in (R, P):
        for k, rows in rt.items():
            m = manifest[k][0]
            for c, r in rows.items():
                d = rows.get(neg(c, m))
                if d and (d["S"]["n(nu)"], d["S"]["n(rho nu)"]) != (r["S"]["n(nu)"], r["S"]["n(rho nu)"]):
                    lb.append((k, c))
    pred["P2"] = False if lb else (True if complete else None)
    p3bad, room3 = [], []
    for nr_ in Nrows:
        k = (nr_["state"], nr_["cover"])
        m = manifest[k][0]
        c = tuple(nr_["c"])
        s_r, s_p = sums(R[k], c, m), sums(P[k], c, m)
        if not (s_r == s_p == (nr_["n(1)"], nr_["n(rho)"])):
            p3bad.append((k, c))
        if min(1 + nr_["n(1)"], nr_["n(rho)"]) >= 3:
            room3.append((k, c))
    pred["P3"] = False if p3bad else (True if complete and Nrows else None)
    pred["P4"] = True if room3 else (False if complete else None)
    out["room-three cyclic covers"] = [[list(k), list(c)] for k, c in room3]
    joint3 = [(k, c) for k in R if k[1] in ("d5.2", "d5.3") for c, r in R[k].items()
              if order_of(c, manifest[k][0]) == 3 and r["S"]["n(nu)"] >= 1 and r["S"]["n(rho nu)"] >= 1
              and P[k][c]["S"]["n(nu)"] >= 1 and P[k][c]["S"]["n(rho nu)"] >= 1]
    pred["P5"] = True if joint3 else (False if complete else None)
    at_c = [(k, c) for k in R for c, r in R[k].items() if r["S"]["h1(V_eta)"] >= 1
            and min(r["S"]["capW"], r["S"]["capL2"]) >= 3 and min(P[k][c]["S"]["capW"], P[k][c]["S"]["capL2"]) >= 3]
    pred["P6"] = True if at_c else (False if complete else None)
    out["predictions"] = pred
    out["complete"] = complete
    return out
