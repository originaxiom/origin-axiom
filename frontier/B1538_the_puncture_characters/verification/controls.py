#!/usr/bin/env python3
"""B1538 -- the controls, written and run before the seal.  They read only banked data, the literature, or quantities a lemma
proved at design time fixes; no puncture character's line or four is read here.

  K0  Lemma 1 (the covers): for d <= DMAX0, the fibre-direction covers enumerated here (lattices x classes) are exactly the
      transitive actions of Gamma of degree d (low_index, through sm:B1536's cover_lib) on which a and b commute and <a, b> is
      transitive, compared as Gamma-sets by sm:B1536's canonical form.
  K1  banked, |D| = 1: on all 541 rows of sm:B1529's census (sm:B1535 Part W's population), route P reproduces Part W's
      banked (h^1, r1) pattern at every (u, kappa in mu_12).  Route W, at every fibre character u != 0, finds exactly one root
      of unity s with h^1 >= 1, h^1 = 1, n = 0, and s = tau_u (1 for +, u(ab)^-1 for -): Part W's mu_u = tau_u.
  K2  Lemma W' (sm:B1535's Lemma W on every M_(D,w); proved at design time), on every cover of population A.  At every
      invariant character trivial on the punctures:
        - for zeta != 1, route W's every root of unity s has n = 0, and route P agrees on h^1, the trivial cusps and n;
        - for every such zeta, zeta = 1 included, route P reads n = 0 at every s in mu_12, and agrees with route W's h^1
          there (0 wherever route W found no root).
  K3  Lemma 2 (b1 = #cusps, n(1) = 0): route T on every cover of population A.
  K4  route T against SnapPy: the multiset of (b1, #cusps) over every cover of degree 2..6 of m004, m003, m135 and m136, from
      route T's integer homology on sm:B1527's presentation, equals SnapPy's (Manifold.covers).
  K5  the transfer on controls: at every puncture-trivial chi = (zeta, s) of K2 with h^1 >= 1 and degree k |D| <= 600,
      route T reads b1(N') - #cusps(N') = 0 (every power of chi is puncture-trivial, so the sum of n is 0 by Lemma W').
  K6  Part F at |D| = 1, banked: on m004, m003, m135 and m136, at every (u, kappa in mu_12), route R (sm:B1536's route_r with
      B1538's own-character scalars), route P4, and sm:B1536's own pulled-back route_r.supplies agree on every supply.  The
      members with capL2 >= 1 are exactly the banked ones: m135's u1, u2 at kappa = 1 (sm:B1530) and m136's u1, u2 at
      kappa = -1 (sm:B1535 C1).
  K7  literature (Burau 1936; Birman, Braids, Links and Mapping Class Groups, Theorem 3.11): for the Artin action of
      beta = (sigma_1 sigma_2^-1)^2 on F_3, whose closure is the figure-eight knot (Alexander polynomial t^2 - 3t + 1), route
      W's Jbar at x_i -> t gives det(I - Jbar) = +-t^k (1 + t + t^2)(t^2 - 3t + 1), checked exactly at t = zeta_m for
      m = 5, 7, 8, 9, 12, 20.
  K8  the Galois-orbit enumeration: the orbit sizes sum to the number of invariant characters != 1 with zeta^m = 1.
  K9  the read-out's logic (read_out.evaluate) on synthetic rows, one case per branch, with the predictions fixed by hand.

    python3 -u controls.py [--record]   ->  controls.json"""
import json
import sys
import time
import warnings
from collections import Counter
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import punct_four as FO  # noqa: E402  (imports sm:B1536's route_r first: it resets PARI's stack)
import punct_covers as F  # noqa: E402
import punct_present as RP  # noqa: E402
import punct_transfer as T  # noqa: E402
import punct_wang as W  # noqa: E402

ROOT = HERE.parents[2]
PART_W_ROWS = ROOT / "frontier" / "B1535_the_cap" / "verification" / "part_w_rows.json"
STATES_A = ["+LR", "-LR", "+LLRR", "-LLRR"]
NAMES = {"+LR": "m004", "-LR": "m003", "+LLRR": "m136", "-LLRR": "m135"}
DMAX_A = 12
DMAX0 = {"+LR": 12, "-LR": 12, "+LLRR": 8, "-LLRR": 8}
K5_DEGREE = 600


def det_m1(st):
    (a, b), (c, d) = st.M
    return abs((a - 1) * (d - 1) - b * c)


def prime_for(L):
    return RP.primes_1_mod(L, 1 << 30, 1)[0]


# ============================================================================================ K0
def k0():
    CL = F.cover_lib()
    out = {}
    for sw in STATES_A:
        st = F.State(sw)
        ours = {}
        for lat, w in F.covers(st, DMAX0[sw], nmin=1):
            C = F.Cover(st, lat, w)
            ours.setdefault(C.d, set()).add(CL.canonical(C.perms, st.G.gens))
        theirs = {}
        for p in CL.low_index_covers(st.G, DMAX0[sw]):
            P = CL.with_inverses(p)
            d = len(p["a"])
            comm = all(P["a"][P["b"][x]] == P["b"][P["a"][x]] for x in range(d))
            seen, todo = {0}, [0]
            while todo:
                x = todo.pop()
                for y in (P["a"][x], P["b"][x], P["_inv"]["a"][x], P["_inv"]["b"][x]):
                    if y not in seen:
                        seen.add(y)
                        todo.append(y)
            if comm and len(seen) == d:
                theirs.setdefault(d, set()).add(CL.canonical(p, st.G.gens))
        agree = ours == theirs
        out[NAMES[sw]] = {"degrees": DMAX0[sw], "covers": {str(d): len(v) for d, v in sorted(ours.items())},
                          "low_index": {str(d): len(v) for d, v in sorted(theirs.items())}, "agree": agree}
    out["holds"] = all(v["agree"] for v in out.values())
    return out


# ============================================================================================ K1
def k1():
    rows = json.loads(PART_W_ROWS.read_text())
    bad, nP, nW = [], 0, 0
    for row in rows:
        sw = row["read as"]
        st = F.State(sw)
        C = F.Cover(st, (1, 0, 1), 0)
        Pr = RP.Presentation(C)
        Dd = det_m1(st)
        us = C.characters(Dd)
        if len(us) != row["X"]["chars"]:
            bad.append([sw, "fibre characters", len(us), row["X"]["chars"]])
            continue
        L = W.lcm(Dd, 12)
        p = prime_for(L)
        pat = Counter()
        for ez in us:
            ezL = [e * (L // Dd) % L for e in ez]
            for kk in range(12):
                kap = kk * (L // 12)
                es = kap if st.sign == "+" else (kap - ezL[0] - ezL[1]) % L
                r = RP.read(Pr, ezL, es, L, p)
                nP += 1
                pat[f"({r['h1']}, {r['r1']})"] += 1
                if r["n"] != 0:
                    bad.append([sw, list(ez), kk, "route P n != 0"])
            if any(e % Dd for e in ez):
                rw = W.read(C, list(ez), Dd)
                nW += 1
                ok = len(rw["rows"]) == 1 and rw["rows"][0]["h1"] == 1 and rw["rows"][0]["n"] == 0
                if ok:
                    j, k = rw["rows"][0]["s"]
                    tau = 0 if st.sign == "+" else (-(ez[0] + ez[1])) % Dd
                    ok = (j * Dd) % k == 0 and ((j * Dd // k) - tau) % Dd == 0
                if not ok:
                    bad.append([sw, list(ez), "route W", rw["rows"]])
        if dict(pat) != row["X"]["h1 pattern"]:
            bad.append([sw, "pattern", dict(pat), row["X"]["h1 pattern"]])
    return {"rows": len(rows), "route P reads": nP, "route W reads": nW, "failures": bad, "holds": not bad}


# ============================================================================================ K2, K3, K5
def k2_k3_k5():
    out2 = {"covers": 0, "zeta": 0, "route W roots": 0, "route P reads": 0, "failures": []}
    out3 = {"covers": 0, "failures": []}
    out5 = {"reads": 0, "skipped (degree)": 0, "failures": []}
    for sw in STATES_A:
        st = F.State(sw)
        for lat, w in F.covers(st, DMAX_A):
            C = F.Cover(st, lat, w)
            Pr = RP.Presentation(C)
            out2["covers"] += 1
            # K3
            r3 = T.read(C, [0] * C.n, 0, 1)
            out3["covers"] += 1
            if r3["n_N'"] != 0 or r3["cusps"] != len(C.cusps):
                out3["failures"].append([sw, list(lat), w, r3])
            # K2
            pt, m = C.puncture_trivial()
            for ez in pt:
                out2["zeta"] += 1
                found = {}
                if any(ez):
                    rw = W.read(C, list(ez), m)
                    for row in rw["rows"]:
                        out2["route W roots"] += 1
                        j, k = row["s"]
                        L = row["L"]
                        ezL = [e * (L // m) % L for e in ez]
                        es = j * (L // k) % L
                        rp = RP.read(Pr, ezL, es, L, prime_for(L))
                        out2["route P reads"] += 1
                        if row["n"] != 0 or (rp["h1"], rp["trivial cusps"], rp["n"]) != (row["h1"], row["trivial cusps"], 0):
                            out2["failures"].append([sw, list(lat), w, list(ez), m, row, rp])
                        found[(j * 12 // k) % 12 if (12 % k == 0) else None] = row["h1"]
                        # K5
                        if C.d * row["L"] <= K5_DEGREE * 4:
                            rt = T.read(C, ezL, es, L)
                            if rt["degree"] <= K5_DEGREE:
                                out5["reads"] += 1
                                if rt["n_N'"] != 0:
                                    out5["failures"].append([sw, list(lat), w, list(ez), m, row["s"], rt])
                            else:
                                out5["skipped (degree)"] += 1
                        else:
                            out5["skipped (degree)"] += 1
                L = W.lcm(m, 12)
                p = prime_for(L)
                for kk in range(12):
                    ezL = [e * (L // m) % L for e in ez]
                    es = kk * (L // 12)
                    rp = RP.read(Pr, ezL, es, L, p)
                    out2["route P reads"] += 1
                    if rp["n"] != 0:
                        out2["failures"].append([sw, list(lat), w, list(ez), m, kk, "route P n != 0", rp])
                    if any(ez) and rp["h1"] != found.get(kk, 0):
                        out2["failures"].append([sw, list(lat), w, list(ez), m, kk, "route W's roots miss", rp, found])
    for o in (out2, out3, out5):
        o["holds"] = not o["failures"]
    return out2, out3, out5


# ============================================================================================ K4
def k4():
    import snappy
    CL = F.cover_lib()
    out = {}
    for sw in STATES_A:
        st = F.State(sw)
        M = snappy.Manifold(NAMES[sw])
        res = {}
        allc = CL.low_index_covers(st.G, 6)
        for d in range(2, 7):
            ours = sorted((T.homology_rank(st.G, p), len(CL.cusps(st.G, p))) for p in allc if len(p["a"]) == d)
            theirs = sorted((N.homology().betti_number(), N.num_cusps()) for N in M.covers(d))
            res[str(d)] = {"covers": len(ours), "agree": ours == theirs}
        out[NAMES[sw]] = res
    out["holds"] = all(v["agree"] for k, r in out.items() if k != "holds" for v in r.values())
    return out


# ============================================================================================ K6
def k6():
    import numpy as np
    out, bad = {}, []
    for sw in STATES_A:
        st = F.State(sw)
        rho, G4 = FO.exact_four(sw)
        assert G4.gens == st.G.gens and G4.rels == st.G.rels
        C = F.Cover(st, (1, 0, 1), 0)
        Dd = det_m1(st)
        L = W.lcm(W.lcm(Dd, 12), 24)
        p = prime_for(L)
        rho_p = FO.four_mod_p(rho, p, L)
        rho_np = {g: np.array(m_, dtype=np.int64) for g, m_ in rho_p.items()}
        cov = FO.R.PCover(st.G, C.perms)
        Pr = RP.Presentation(C)
        r = RP.root_of_unity_mod(L, p)
        members, n = [], 0
        for ez in C.characters(Dd):
            ezL = [e * (L // Dd) % L for e in ez]
            for kk in range(12):
                es = kk * (L // 12) if st.sign == "+" else (kk * (L // 12) - ezL[0] - ezL[1]) % L
                sr = FO.supplies_r(C, rho_p, ezL, es, L, p, cov)
                sp = FO.supplies_p4(C, rho_p, ezL, es, L, p, Pr)
                chi = {"a": pow(r, ezL[0], p), "b": pow(r, ezL[1], p), "t": pow(r, es, p)}
                sb = FO.R.supplies(cov, rho_np, chi, p)
                n += 1
                if not (sr == sp == sb):
                    bad.append([sw, list(ez), kk, sr, sp, sb])
                if sr["h1(V_eta)"] >= 1:
                    members.append({"u": [e / Dd for e in ez], "kappa": f"{kk}/12", "capW": sr["capW"], "capL2": sr["capL2"]})
        out[NAMES[sw]] = {"characters": n, "members": members}
    # the banked members with capL2 >= 1
    want = {"m135": {((0.0, 0.5), "0/12"), ((0.5, 0.0), "0/12")}, "m136": {((0.0, 0.5), "6/12"), ((0.5, 0.0), "6/12")},
            "m004": set(), "m003": set()}
    for name, v in out.items():
        got = {(tuple(m_["u"]), m_["kappa"]) for m_ in v["members"] if m_["capL2"] >= 1}
        v["capL2 >= 1"] = sorted([list(u), k] for u, k in got)
        if got != want[name]:
            bad.append([name, "capL2 >= 1 members", sorted(got), sorted(want[name])])
    m004 = out["m004"]["members"]
    if len(m004) != 1 or m004[0]["u"] != [0.0, 0.0] or m004[0]["kappa"] != "0/12" or m004[0]["capW"] != 1:
        bad.append(["m004", "members", m004])
    out["failures"] = bad
    out["holds"] = not bad
    return out


# ============================================================================================ K7
def k7():
    P = F.pari()
    s1 = {"a": "abA", "b": "a", "c": "c"}
    s2i = {"a": "a", "b": "c", "c": "Cbc"}
    img = {g: g for g in "abc"}
    for step in (s2i, s1, s2i, s1):                      # beta = (sigma_1 sigma_2^-1)^2, applied as substitutions
        img = {g: F.substitute(img[g], step) for g in "abc"}
    idx = {"a": 0, "b": 1, "c": 2}
    images = [[(idx[c.lower()], 1 if c.islower() else -1) for c in img[g]] for g in "abc"]
    res = {}
    for m in (5, 7, 8, 9, 12, 20):
        J = W.fox_jacobian(images, [1, 1, 1], m)
        Jb, _ = W.jbar(J, [1, 1, 1], m)
        phi = P.polcyclo(m, "y")
        z = P.Mod(P("y"), phi)
        det = P.subst(P.charpoly(Jb, "x"), "x", 1)
        lit = (1 + z + z ** 2) * (z ** 2 - 3 * z + 1)
        ratio = det / lit
        res[str(m)] = bool(ratio ** (2 * m) == 1)
    return {"beta": "(sigma_1 sigma_2^-1)^2", "images": img, "det(I - Jbar) / ((1 + t + t^2)(t^2 - 3t + 1)) is +-t^k": res,
            "holds": all(res.values())}


# ============================================================================================ K8
def k8():
    bad, n = [], 0
    for sw in STATES_A:
        st = F.State(sw)
        for lat, w in F.covers(st, DMAX_A):
            C = F.Cover(st, lat, w)
            for m in (2, 3, 4, 6):
                if C.count_characters(m) > 50000:
                    continue
                reps = C.galois_reps(m)
                n += 1
                if sum(o for _, _, o in reps) != C.count_characters(m) - 1:
                    bad.append([sw, list(lat), w, m])
    return {"checks": n, "failures": bad, "holds": not bad}


# ============================================================================================ K9
def k9():
    """the read-out's logic on synthetic rows: each case's predictions are fixed by hand here, before any run.  read_out is
    loaded by its path: sm:B1536's route_r puts sm:B1535's directory, which has its own read_out.py, first on sys.path"""
    import importlib.util
    spec = importlib.util.spec_from_file_location("b1538_read_out", HERE / "read_out.py")
    RO = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RO)

    def cover(state, hits, pdis=0, tdis=0, treads=None):
        return {"cover": state + ".x", "chunk": 0, "chunks": 1, "state": state, "read": True, "puncture orbits": 10,
                "puncture characters": 30,
                "hits": hits, "route P": {"reads": 20, "disagree": [0] * pdis},
                "route T": {"reads": len(hits) if treads is None else treads, "skipped": 0, "disagree": [0] * tdis}}

    def hit(n):
        return {"n": n, "zeta": [1, 0], "m": 3, "s": [1, 6], "h1": n, "trivial cusps": 0}
    ident = {"identity holds": True}
    member2 = {"member": True, "h1 R": 1, "h1 P4": 1, "R": {"capW": 2, "capL2": 2}, "P4": {"capW": 2, "capL2": 2}}
    member1 = {"member": True, "h1 R": 1, "h1 P4": 1, "R": {"capW": 2, "capL2": 1}, "P4": {"capW": 2, "capL2": 1}}
    cases = {
        "no hits": (ident, [cover("m003", [])], None,
                    {"P1": True, "P2": True, "P3": True, "P4": False, "P5": True, "P6": True, "P7": True, "P8": True}),
        "n = 1 on m003": (ident, [cover("m003", [hit(1)])], None,
                          {"P1": True, "P2": True, "P3": True, "P4": True, "P5": True, "P6": True, "P7": True, "P8": True}),
        "n = 1 on m004": (ident, [cover("m004", [hit(1)])], None,
                          {"P1": True, "P2": True, "P3": True, "P4": True, "P5": True, "P6": False, "P7": True, "P8": True}),
        "n = 2, Part F pending": (ident, [cover("m135", [hit(2)])], None,
                                  {"P1": True, "P2": True, "P3": True, "P4": True, "P5": False, "P6": True, "P7": None,
                                   "P8": None}),
        "n = 2, a member with both caps 2": (ident, [cover("m135", [hit(2)])], [member2],
                                             {"P1": True, "P2": True, "P3": True, "P4": True, "P5": False, "P6": True,
                                              "P7": False, "P8": False}),
        "n = 2, members with capL2 1": (ident, [cover("m135", [hit(2)])], [member1],
                                        {"P1": True, "P2": True, "P3": True, "P4": True, "P5": False, "P6": True,
                                         "P7": True, "P8": True}),
        "route P disagrees": (ident, [cover("m003", [], pdis=1)], None,
                              {"P1": True, "P2": False, "P3": True, "P4": False, "P5": True, "P6": True, "P7": True,
                               "P8": True}),
        "route T disagrees": (ident, [cover("m003", [hit(1)], tdis=1)], None,
                              {"P1": True, "P2": True, "P3": False, "P4": True, "P5": True, "P6": True, "P7": True,
                               "P8": True}),
        "identity failed": ({"identity holds": False}, [cover("m003", [])], None,
                            {"P1": False, "P2": True, "P3": True, "P4": False, "P5": True, "P6": True, "P7": True,
                             "P8": True}),
    }
    res, bad = {}, []
    for name, (idn, L, Fr, want) in cases.items():
        got = RO.evaluate(idn, L, Fr, say=lambda s: None)["predictions"]
        res[name] = got == want
        if got != want:
            bad.append([name, got, want])
    return {"cases": res, "failures": bad, "holds": not bad}


def main():
    t0 = time.time()
    out = {}
    for name, fn in (("K9", k9), ("K7", k7), ("K0", k0), ("K8", k8), ("K6", k6), ("K4", k4), ("K1", k1)):
        t = time.time()
        out[name] = fn()
        out[name]["seconds"] = round(time.time() - t, 1)
        print(name, "holds" if out[name]["holds"] else "FAILS", f"{out[name]['seconds']} s", flush=True)
    t = time.time()
    k2, k3, k5 = k2_k3_k5()
    for name, v in (("K2", k2), ("K3", k3), ("K5", k5)):
        v["seconds"] = round(time.time() - t, 1)
        out[name] = v
        print(name, "holds" if v["holds"] else "FAILS", flush=True)
    out["all hold"] = all(v["holds"] for k, v in out.items() if isinstance(v, dict))
    out["seconds"] = round(time.time() - t0, 1)
    print("ALL HOLD" if out["all hold"] else "SOME FAIL", f"{out['seconds']} s")
    if "--record" in sys.argv:
        (HERE / "controls.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    return out


if __name__ == "__main__":
    main()
