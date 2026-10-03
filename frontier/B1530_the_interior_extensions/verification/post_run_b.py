#!/usr/bin/env python3
"""B1530 post-run reading of the kappa = -1 members (PREREGISTRATION sections 4 and 9; written after the census found such
members, as section 4 said it would be, and disclosed in FINDINGS).

Why.  Population B at kappa = -1 is not empty: route T reads h^1(nu (x) rho) = 1 at kappa = -1 on some word states (the first
found: +LLRR, at u = (0, 1/2) and (1/2, 0)), with route G agreeing.  A member is nu = (u, -1) with nu^5 among those characters.
By Lemma N such a member is generation-shaped only in case (a), reading (-1, -1).  Section 4: "Every kappa = -1 member is read
by routes N and W (sm:B1527 wang_lib, Lemma E) at every class of a basis and the sum of the basis."

What this does.  The members are taken from census_bc.json (or, before the summary exists, from census_bc.jsonl): for every
route-T hit (u', kappa') with kappa' = -1 and every torsion character u fixed by phi with 5u = u', the member nu = (u, -1).
At each member, at the hyperbolic point (route N's four, 60 digits):
  - V = nu (x) rho, V_eta = nu^5 (x) rho, L = nu^-4; the classes of H^1(V_eta) by route N's Classes (every class is interior,
    the cusp being acyclic at kappa = -1; checked);
  - at every class of the orthonormal basis and at the sum of the basis, W1 = [[V, c L], [0, L]] is read by route N
    (cusp_lib.class_index on W1 and Lambda^2 W1, its identities checked) and by route W (sm:B1527 wang_lib.index_wang on the
    same matrices: Wang's sequence and Lemma E, no linear algebra shared with cusp_lib);
  - the two routes are compared reading by reading.
Rows are appended to post_run_b.jsonl as they finish (resume-safe); post_run_b.json holds the summary, with the key
"generation-shaped" that read_out.py reads.
Usage: python3 post_run_b.py [--only STATE ...]"""
import json
import sys
import time
import warnings
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp  # noqa: E402

import exact_states as S  # noqa: E402
import route_n as N  # noqa: E402

WL = S.load(S.B1527, "wang_lib", "wang_lib")
mp.mp.dps = 60
OUT = HERE / "post_run_b.jsonl"
HALF = Fraction(1, 2)


def census_rows():
    js = HERE / "census_bc.json"
    if js.exists():
        return [r for r in json.loads(js.read_text())["records"] if "error" not in r], "census_bc.json"
    return [r for r in (json.loads(x) for x in (HERE / "census_bc.jsonl").read_text().splitlines()) if "error" not in r], \
        "census_bc.jsonl"


def members(rows):
    """[(state, read as, golden, u, the hit u')] for every kappa = -1 member"""
    out = []
    for r in rows:
        hits = [h for h in r["B"]["route T: h1 >= 1 at"] if h[2] == "-1"]
        if not hits:
            continue
        sign, word = r["read as"][0], r["read as"][1:]
        G, img, chars, D = N.group(sign, word)
        for ua, ub, _, g in hits:
            up = (Fraction(ua), Fraction(ub))
            for u in chars:
                if ((5 * u[0]) % 1, (5 * u[1]) % 1) == up:
                    out.append((r["state"], r["read as"], r["golden"], u, up, g))
    return out


def pair(r):
    return (r["I(W)"], r["I(L2W)"])


def read_member(state, read_as, golden, u, up, g):
    t0 = time.time()
    L = N.lib()
    sign, word = read_as[0], read_as[1:]
    G, img, chars, D = N.group(sign, word)
    mats = N.four_mats(sign, word)
    ch = N.char_values(sign, u, HALF)
    V = N.module(mats, ch)
    lval = N.char_power(ch, -4)
    trivial_L = all(abs(v - 1) < mp.mpf(10) ** -40 for v in lval.values())
    Veta = N.module(mats, N.char_power(ch, 5))
    C = N.Classes(G, Veta)
    ints = C.interior()
    bt = C.boundary_type(ints)
    row = {"state": state, "read as": read_as, "golden": golden, "u": [str(u[0]), str(u[1])], "kappa": "-1",
           "nu^5 (the hit)": [str(up[0]), str(up[1])], "route T's g": g, "case": "(a)" if trivial_L else "(b)",
           "h1(V_eta)": C.h1, "interior": ints.cols, "boundary-type": bt.cols, "readings": {}}
    zs = {f"basis {k}": ints[:, k] for k in range(ints.cols)}
    if ints.cols >= 2:
        s = ints[:, 0]
        for k in range(1, ints.cols):
            s = s + ints[:, k]
        zs["the sum of the basis"] = s
    elif ints.cols == 1:
        zs["the sum of the basis"] = ints[:, 0]
    for name, z in zs.items():
        W1 = N.extension(V, z, G.gens, None if trivial_L else lval)
        rn = N.reading(G, W1)
        mW = {x: W1.M[x] for x in "abt"}
        m2 = {x: L.wedge2(W1.M[x]) for x in "abt"}
        ww = WL.index_wang(img, G.cusp, mW)
        w2 = WL.index_wang(img, G.cusp, m2)
        row["readings"][name] = {"route N": [rn["I(W)"], rn["I(L2W)"]], "route W": [ww["I"], w2["I"]],
                                 "N checks": rn["checks"], "N margins": rn["margins"],
                                 "W data": {"W": {k: v for k, v in ww.items() if k != "margins"},
                                            "L2W": {k: v for k, v in w2.items() if k != "margins"}},
                                 "W margins": [ww["margins"], w2["margins"]],
                                 "agree": [rn["I(W)"], rn["I(L2W)"]] == [ww["I"], w2["I"]]}
    row["routes agree"] = all(v["agree"] for v in row["readings"].values()) and ints.cols == C.h1
    row["generation-shaped"] = [name for name, v in row["readings"].items()
                                if v["route N"][0] == v["route N"][1] != 0 or v["route W"][0] == v["route W"][1] != 0]
    row["margins (classes)"] = C.mg.as_dict()
    row["seconds"] = round(time.time() - t0)
    return row


def main():
    a = sys.argv[1:]
    only = a[a.index("--only") + 1:] if "--only" in a else None
    rows, src = census_rows()
    ms = members(rows)
    if only:
        ms = [m for m in ms if m[0] in only]
    done = set()
    if OUT.exists():
        for line in OUT.read_text().splitlines():
            r = json.loads(line)
            done.add((r["state"], tuple(r["u"])))
    print(f"post_run_b: {len(ms)} kappa = -1 members from {src}; {len(done)} already read", flush=True)
    for m in ms:
        key = (m[0], (str(m[3][0]), str(m[3][1])))
        if key in done:
            continue
        r = read_member(*m)
        with open(OUT, "a") as fh:
            fh.write(json.dumps(r, default=str) + "\n")
        print(f"{r['state']} u {r['u']}: case {r['case']}, h1(V_eta) {r['h1(V_eta)']}, interior {r['interior']}; "
              f"{ {k: (v['route N'], v['route W']) for k, v in r['readings'].items()} }; agree {r['routes agree']}; "
              f"{r['seconds']} s", flush=True)
    allrows = [json.loads(x) for x in OUT.read_text().splitlines()] if OUT.exists() else []
    summary = {"source": src, "members": len(ms), "read": len(allrows),
               "routes agree everywhere": all(r["routes agree"] for r in allrows),
               "readings": sorted({(tuple(v["route N"]), tuple(v["route W"])) for r in allrows
                                   for v in r["readings"].values()}),
               "generation-shaped": [{"state": r["state"], "u": r["u"], "classes": r["generation-shaped"],
                                      "golden": r["golden"]} for r in allrows if r["generation-shaped"]],
               "states with members": sorted({r["state"] for r in allrows}),
               "rows": allrows}
    if not only:
        (HERE / "post_run_b.json").write_text(json.dumps(summary, indent=1, default=str))
    print(json.dumps({k: v for k, v in summary.items() if k != "rows"}, indent=1, default=str), flush=True)


if __name__ == "__main__":
    main()
