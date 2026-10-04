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
  K9  the read-out's logic (read_out.evaluate) on synthetic rows, one case per branch, with the predictions fixed by hand,
      including the audit lane's R87 coverage cases (a missing, duplicated, short or unexpected record; an empty Part F).
  K10 Proposition H's characters, by structure alone (no line or four is read): on every cover of population A with
      D = Z^2 / 2Z^2, zeta_H(y) = the sign of y's image in the centre of Q_8 under a -> i, b -> j; the same from a -> j,
      b -> k; invariant; -1 at every puncture; one of the run's own Galois representatives.  Recorded for the read-out
      (P9-P11), with the order of the monodromy's permutation of the axes i, j, k (3 on the golden states m004 and m003) and
      whether tau acts on Q_8 as the identity (never on a golden state; on exactly one class wbar of each silver state).
  K11 the population manifest (the audit lane's R87): every cover's chunks and its puncture characters and their Galois
      orbits at m(C), by formula (the Smith form's count and Moebius inversion, minus the enumerated puncture-trivial
      characters), whose per-state totals must equal the seal's table, counted by enumeration.  The read-out certifies no
      population-wide prediction unless the records match this manifest exactly.
  K12 Part F's fourth roots, by brute force (the audit lane's R89): on every cover with |D| <= 5, Cover.fourth_roots at a
      fixed sample of characters of order dividing 12 (Proposition H's zeta_H always among them) equals the set of characters
      of order dividing 48 whose fourth power it is, found by enumerating them all, and the Smith form's count.

    python3 -u controls.py [--record]   ->  controls.json"""
import importlib.util
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
    loaded by its path: sm:B1536's route_r puts sm:B1535's directory, which has its own read_out.py, first on sys.path.
    The coverage cases are the audit lane's R87: missing, duplicate, extra or short records never certify a negative"""
    spec = importlib.util.spec_from_file_location("b1538_read_out", HERE / "read_out.py")
    RO = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RO)

    def cover(state, hits, pdis=0, tdis=0, treads=None, cid=None, chunks=1, chunk=0, orbits=10):
        return {"cover": cid or state + ".x", "chunk": chunk, "chunks": chunks, "state": state, "read": True,
                "puncture orbits": orbits, "puncture characters": 30,
                "hits": hits, "route P": {"reads": 20, "disagree": [0] * pdis},
                "route T": {"reads": len(hits) if treads is None else treads, "skipped": 0, "disagree": [0] * tdis}}

    def man(*cids, chunks=1, orbits=10):
        return {c: {"chunks": chunks, "puncture orbits": orbits} for c in cids}

    def hit(n, zeta=(1, 0), m=3, s=(1, 6)):
        return {"n": n, "zeta": list(zeta), "m": m, "s": list(s), "h1": n, "trivial cusps": 0}

    def qh(n, s):                                          # a hit at the synthetic zeta_H = (1, 1), m = 2
        return hit(n, (1, 1), 2, s)
    chi = {"zeta": [1, 0], "m": 3, "s": [1, 6], "n": 2}

    def head(cid, planned, smith=None):
        return {"kind": "candidate", "cover": cid, "chi": chi, "planned": planned, "fourth roots": planned // 4,
                "fourth roots by the Smith form": planned // 4 if smith is None else smith}

    def reading(cid, k, caps=None):
        f = {"kind": "reading", "cover": cid, "chi": chi, "nu": {"zeta": [k, 0], "m": 12, "s": [k, 24]}, "h1 R": 0,
             "h1 P4": 0, "member": False}
        if caps:
            f.update({"member": True, "h1 R": 1, "h1 P4": 1, "R": dict(zip(("capW", "capL2"), caps)),
                      "P4": dict(zip(("capW", "capL2"), caps))})
        return f
    ident = {"identity holds": True}
    gold = {"m004.q": {"ez": [1, 1], "m": 2, "golden": True, "acts on Q8 as the identity": False}}
    both = dict(gold, **{"m135.q": {"ez": [1, 1], "m": 2, "golden": False, "acts on Q8 as the identity": True}})
    T, F_, N = True, False, None

    def want(p1, p2, p3, p4, p5, p6, p7, p8, p9=N, p10=N, p11=N):
        return {"P1": p1, "P2": p2, "P3": p3, "P4": p4, "P5": p5, "P6": p6, "P7": p7, "P8": p8, "P9": p9, "P10": p10,
                "P11": p11}
    c3, c4, c5 = man("m003.x"), man("m004.x"), man("m135.x")
    cases = {
        "no hits": (ident, [cover("m003", [])], None, None, c3, want(T, T, T, F_, T, T, T, T)),
        "n = 1 on m003": (ident, [cover("m003", [hit(1)])], None, None, c3, want(T, T, T, T, T, T, T, T)),
        "n = 1 on m004": (ident, [cover("m004", [hit(1)])], None, None, c4, want(T, T, T, T, T, F_, T, T)),
        "n = 2, Part F pending": (ident, [cover("m135", [hit(2)])], None, None, c5, want(T, T, T, T, F_, T, N, N)),
        "n = 2, a member with both caps 2": (ident, [cover("m135", [hit(2)])],
                                             [head("m135.x", 4), reading("m135.x", 1, (2, 2))]
                                             + [reading("m135.x", k) for k in (2, 3, 5)], None, c5,
                                             want(T, T, T, T, F_, T, F_, F_)),
        "n = 2, every planned reading, capL2 1": (ident, [cover("m135", [hit(2)])],
                                                  [head("m135.x", 4), reading("m135.x", 1, (2, 1))]
                                                  + [reading("m135.x", k) for k in (2, 3, 5)],
                                                  None, c5, want(T, T, T, T, F_, T, T, T)),
        "route P disagrees": (ident, [cover("m003", [], pdis=1)], None, None, c3, want(T, F_, T, F_, T, T, T, T)),
        "route T disagrees": (ident, [cover("m003", [hit(1)], tdis=1)], None, None, c3, want(T, T, F_, T, T, T, T, T)),
        "identity failed": ({"identity holds": False}, [cover("m003", [])], None, None, c3,
                            want(F_, T, T, F_, T, T, T, T)),
        # coverage (R87): incomplete records never certify a negative
        "a manifest cover missing": (ident, [cover("m003", [])], None, None, man("m003.x", "m135.x"),
                                     want(T, N, N, N, N, N, N, N)),
        "a duplicated chunk": (ident, [cover("m003", []), cover("m003", [])], None, None, c3,
                               want(T, N, N, N, N, N, N, N)),
        "an orbit count short of the manifest": (ident, [cover("m003", [], orbits=9)], None, None, c3,
                                                 want(T, N, N, N, N, N, N, N)),
        "an unexpected cover": (ident, [cover("m003", []), cover("m136", [])], None, None, c3,
                                want(T, N, N, N, N, N, N, N)),
        "no manifest": (ident, [cover("m003", [])], None, None, None, want(T, N, N, N, N, N, N, N)),
        "a refuting row on incomplete records": (ident, [cover("m004", [hit(2)])], None, None, man("m004.x", "m135.x"),
                                                 want(T, N, N, T, F_, F_, N, N)),
        "R87's probe: a candidate with an empty Part F": (ident, [cover("m135", [hit(2)])], [], None, c5,
                                                          want(T, T, T, T, F_, T, N, N)),
        "a candidate short of its planned readings": (ident, [cover("m135", [hit(2)])],
                                                      [head("m135.x", 4)] + [reading("m135.x", k) for k in (1, 2, 3)],
                                                      None, c5, want(T, T, T, T, F_, T, N, N)),
        "a candidate with no fourth root": (ident, [cover("m135", [hit(2)])], [head("m135.x", 0)], None, c5,
                                            want(T, T, T, T, F_, T, T, T)),
        "a candidate whose fourth roots differ from the Smith form's count":
            (ident, [cover("m135", [hit(2)])], [head("m135.x", 4, smith=2)] + [reading("m135.x", k) for k in (1, 2, 3, 5)],
             None, c5, want(T, T, T, T, F_, T, N, N)),
        "a refuting member on an incomplete Part F": (ident, [cover("m135", [hit(2)])],
                                                      [head("m135.x", 4), reading("m135.x", 1, (2, 2))], None, c5,
                                                      want(T, T, T, T, F_, T, F_, F_)),
        # Proposition H
        "H: 2 + 1 + 1 on the golden line, another character's hit not counted":
            (ident, [cover("m004", [qh(2, (1, 6)), qh(1, (1, 3)), qh(1, (2, 3)), hit(1, (0, 1), 2)], cid="m004.q")],
             None, gold, man("m004.q"), want(T, T, T, T, F_, F_, N, N, T, T)),
        "H fails: the sum is 3": (ident, [cover("m004", [qh(2, (1, 6)), qh(1, (1, 3))], cid="m004.q")], None, gold,
                                  man("m004.q"), want(T, T, T, T, F_, F_, N, N, F_, T)),
        "H on the golden line fails: 4 at one s": (ident, [cover("m004", [qh(4, (1, 6))], cid="m004.q")], None, gold,
                                                   man("m004.q"), want(T, T, T, T, F_, F_, N, N, T, F_)),
        "H: the identity cover may carry 4 at one s":
            (ident, [cover("m004", [qh(2, (1, 6)), qh(2, (5, 6))], cid="m004.q"),
                     cover("m135", [qh(4, (0, 1))], cid="m135.q")], None, both, man("m004.q", "m135.q"),
             want(T, T, T, T, F_, F_, N, N, T, T, T)),
        "H on the identity cover fails: an odd n":
            (ident, [cover("m004", [qh(2, (1, 6)), qh(2, (5, 6))], cid="m004.q"),
                     cover("m135", [qh(2, (0, 1)), qh(1, (1, 4)), qh(1, (3, 4))], cid="m135.q")], None, both,
             man("m004.q", "m135.q"), want(T, T, T, T, F_, F_, N, N, T, T, F_)),
        "H: a cover of K10 not read in full": (ident, [cover("m004", [qh(2, (1, 6))], cid="m004.q", chunks=2)], None, gold,
                                               man("m004.q", chunks=2), want(T, N, N, T, F_, F_, N, N, N, N)),
    }
    res, bad = {}, []
    for name, (idn, L, Fr, hcov, mf, w) in cases.items():
        got = RO.evaluate(idn, L, Fr, say=lambda s: None, hcov=hcov, manifest=mf)["predictions"]
        res[name] = got == w
        if got != w:
            bad.append([name, got, w])
    return {"cases": res, "failures": bad, "holds": not bad}


# ============================================================================================ K10
_QM = {("1", "1"): (1, "1"), ("1", "i"): (1, "i"), ("1", "j"): (1, "j"), ("1", "k"): (1, "k"),
       ("i", "1"): (1, "i"), ("i", "i"): (-1, "1"), ("i", "j"): (1, "k"), ("i", "k"): (-1, "j"),
       ("j", "1"): (1, "j"), ("j", "i"): (-1, "k"), ("j", "j"): (-1, "1"), ("j", "k"): (1, "i"),
       ("k", "1"): (1, "k"), ("k", "i"): (1, "j"), ("k", "j"): (-1, "i"), ("k", "k"): (-1, "1")}


def q8(word, gen=None):
    """the image in Q_8 of a word in a, b, A, B under a -> i, b -> j (or the images gen), as (sign, unit)"""
    gen = gen or {"a": (1, "i"), "b": (1, "j")}
    sgn, u = 1, "1"
    for c in word:
        s2, u2 = gen[c.lower()]
        if c.isupper() and u2 != "1":            # (s u)^-1 = -s u for a unit u in {i, j, k}
            s2 = -s2
        s3, u3 = _QM[(u, u2)]
        sgn, u = sgn * s2 * s3, u3
    return sgn, u


def k10():
    """Proposition H's characters, located by structure alone (no line or four is read): on every cover of population A with
    D = Z^2 / 2Z^2, every generator y_i of K = ker(F -> (Z/2)^2) maps into the centre {+-1} of Q_8 under a -> i, b -> j, and
    zeta_H(y_i) = that sign.  Checked: the same character from the generating pair a -> j, b -> k (the kernel of F -> Q_8 is
    characteristic); zeta_H o f = zeta_H; zeta_H(l_x) = -1 at every puncture; (zeta_H, 2, 1) is one of the run's own Galois
    representatives at m(C).  Recorded: zeta_H as the run will record it, the order of the monodromy's permutation of the
    axes i, j, k (3 exactly when the trace of M is odd: the golden states), and whether tau = t w acts on Q_8 (x -> phi(w x
    w^-1)) as the identity.  Proposition H's structure, checked: on a golden state it never does; on a silver state, where
    phi acts on Q_8 / centre trivially, it does on exactly one of the four classes wbar"""
    spec = importlib.util.spec_from_file_location("b1538_run", HERE / "run.py")
    RUN = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RUN)
    out, bad = {"covers": {}}, []
    for sw in STATES_A:
        st = F.State(sw)
        bi, bj = q8(st.phi("a")), q8(st.phi("b"))
        perm = {"i": bi[1], "j": bj[1], "k": _QM[(bi[1], bj[1])][1]}
        order, cur = 1, dict(perm)
        while any(cur[x] != x for x in "ijk"):
            cur = {x: perm[cur[x]] for x in "ijk"}
            order += 1
            assert order <= 3, (sw, perm)
        golden = order == 3
        if golden != ((st.M[0][0] + st.M[1][1]) % 2 == 1):
            bad.append([sw, "the axis permutation's order disagrees with the trace's parity", perm])
        for lat, w in F.covers(st, DMAX_A):
            if tuple(lat) != (2, 0, 2):
                continue
            C = F.Cover(st, lat, w)
            cid = f"{NAMES[sw]}.D4.2-0-2.w{w}"
            v1 = [q8(wd) for wd in C.gword]
            v2 = [q8(wd, {"a": (1, "j"), "b": (1, "k")}) for wd in C.gword]
            ez = [0 if s_ == 1 else 1 for s_, _ in v1]
            m, _ = RUN.modulus(C)
            ti = q8(st.phi(C.w + "a" + F.inv_word(C.w)))
            tj = q8(st.phi(C.w + "b" + F.inv_word(C.w)))
            trivial = ti == (1, "i") and tj == (1, "j")
            checks = {
                "central": all(u == "1" for _, u in v1 + v2),
                "characteristic": [0 if s_ == 1 else 1 for s_, _ in v2] == ez,
                "invariant": all(sum(ez[j] * C.fstar[j][i] for j in range(C.n)) % 2 == ez[i] for i in range(C.n)),
                "every puncture": all(v == 1 for v in C.puncture_values(ez, 2)),
                "a Galois representative": m is not None and (tuple(ez), 2, 1) in C.galois_reps(m),
            }
            out["covers"][cid] = {"ez": ez, "m": 2, "golden": golden, "axis permutation order": order,
                                  "acts on Q8 as the identity": trivial, "tau on i, j": [list(ti), list(tj)],
                                  "cusps": len(C.cusps), "m(C)": m, "checks": checks}
            if not all(checks.values()):
                bad.append([cid, checks])
    out["count"] = len(out["covers"])
    out["golden covers"] = sorted(c for c, v in out["covers"].items() if v["golden"])
    out["identity covers"] = sorted(c for c, v in out["covers"].items() if v["acts on Q8 as the identity"])
    for name in NAMES.values():
        mine = [v for c, v in out["covers"].items() if c.startswith(name + ".")]
        idn = sum(1 for v in mine if v["acts on Q8 as the identity"])
        if mine and mine[0]["golden"] and idn != 0:
            bad.append([name, "a golden state's monodromy acts on Q8 as the identity", idn])
        if mine and not mine[0]["golden"] and (len(mine) != 4 or idn != 1):
            bad.append([name, "a silver state needs four classes, exactly one acting as the identity", len(mine), idn])
    out["failures"] = bad
    out["holds"] = not bad and out["count"] > 0 and len(out["golden covers"]) == 2
    return out


# ============================================================================================ K11
SEAL_TABLE = {"m004": (5, 583, 201), "m003": (9, 39695, 7313), "m136": (29, 807820, 210524), "m135": (37, 1558524, 444950)}


def k11():
    """the population manifest the read-out requires (the audit lane's R87): for every cover of population A, the chunks run.py
    writes and its puncture characters and their Galois orbits at m(C), by formula, not by the run's enumeration:
      - all invariant characters with zeta^m = 1: count_characters(m), the Smith form's product; their Galois orbits
        (zeta != 1): orbit_count(C, m), by Moebius inversion (run.py's own functions);
      - minus the puncture-trivial characters with zeta^m = 1 (Lemma 3's finite group, enumerated) and their Galois orbits.
    The per-state totals must equal the seal's population table (section 5), which was counted by enumeration."""
    from fractions import Fraction as Fr_
    from math import gcd
    spec = importlib.util.spec_from_file_location("b1538_run_k11", HERE / "run.py")
    RUN = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RUN)
    manifest, totals, bad = {}, {}, []
    for sw, lat, w, cid in RUN.population():
        C = F.Cover(F.State(sw), lat, w)
        m, b = RUN.modulus(C)
        if m is None:
            bad.append([cid, "above the budget"])
            continue
        size = RUN.orbit_count(C, m)
        nch = max(1, -(-size // RUN.CHUNK))
        pt, mpt = C.puncture_trivial()
        units = [a for a in range(1, m) if gcd(a, m) == 1]
        chars, seen, orbits = 0, set(), 0
        for ez in pt:
            u = [Fr_(e % mpt, mpt) for e in ez]
            if any((x * m).denominator != 1 for x in u):
                continue                                   # order not dividing m: not in the population's range
            chars += 1
            ezm = tuple(int(x * m) % m for x in u)
            if not any(ezm) or ezm in seen:
                continue
            orb = {tuple(a * e % m for e in ezm) for a in units}
            seen |= orb
            orbits += 1
        rec = {"chunks": nch, "m": m, "b": b, "puncture characters": C.count_characters(m) - chars,
               "puncture orbits": size - orbits, "puncture-trivial characters in range": chars}
        manifest[cid] = rec
        tot = totals.setdefault(NAMES[sw], [0, 0, 0])
        tot[0] += 1
        tot[1] += rec["puncture characters"]
        tot[2] += rec["puncture orbits"]
    for name, want in SEAL_TABLE.items():
        if tuple(totals.get(name, ())) != want:
            bad.append([name, "the totals differ from the seal's table", totals.get(name), want])
    return {"manifest": manifest, "totals": totals, "chunks": sum(v["chunks"] for v in manifest.values()),
            "failures": bad, "holds": not bad and len(manifest) == 80}


# ============================================================================================ K12
K12_SAMPLE = 400


def k12():
    """Part F's fourth roots, certified by brute force (the audit lane's R89 asks for a producer-level fourth-root
    certificate).  On every cover of population A with |D| <= 5: every invariant character nu with nu^48 = 1 is enumerated
    and grouped by nu^4 (in 48ths, nu^4 = zeta exactly when nu = zeta mod 12, coordinate by coordinate).  At every invariant
    zeta with zeta^12 = 1 (a fixed sample of K12_SAMPLE when there are more; Proposition H's zeta_H always), the set
    Cover.fourth_roots(zeta, 12) must equal that group, and its size the Smith form's product of per-coordinate counts.
    Structure only: no line or four is read"""
    from fractions import Fraction as Fr_
    from math import gcd
    out, bad, n_cov, n_chi = {}, [], 0, 0
    for sw in STATES_A:
        st = F.State(sw)
        for lat, w in F.covers(st, 5):
            C = F.Cover(st, lat, w)
            n_cov += 1
            buckets = {}
            for nu in C.characters(48):
                buckets.setdefault(tuple(e % 12 for e in nu), set()).add(tuple(nu))
            chars = sorted(C.characters(12))
            test = chars if len(chars) <= K12_SAMPLE else chars[::-(-len(chars) // K12_SAMPLE)]
            if tuple(lat) == (2, 0, 2):                       # zeta_H, as K10 locates it, scaled to 12ths
                ezh = tuple(6 * (0 if q8(wd)[0] == 1 else 1) for wd in C.gword)
                if ezh not in test:
                    test = list(test) + [ezh]
            for ez in test:
                n_chi += 1
                got = set()
                for ezp, mp in C.fourth_roots(list(ez), 12):
                    assert 48 % mp == 0, (sw, lat, w, ez, mp)
                    got.add(tuple(e * (48 // mp) % 48 for e in ezp))
                want = buckets.get(tuple(e % 12 for e in ez), set())
                c = [sum(Fr_(e % 12, 12) * C.Uinv[k][jj] for k, e in enumerate(ez)) % 1 for jj in range(C.n)]
                count = 1
                for ci, di in zip(c, C.snf):
                    if di == 0:
                        count *= 4
                    else:
                        D_ = abs(di)
                        a = ci * D_
                        count *= gcd(4, D_) if a.denominator == 1 and int(a) % gcd(4, D_) == 0 else 0
                if got != want or len(got) != count:
                    bad.append([NAMES[sw], list(lat), w, list(ez), len(got), len(want), count])
    out.update({"covers": n_cov, "characters": n_chi, "failures": bad[:20], "failure count": len(bad),
                "holds": not bad and n_cov > 0})
    return out


def main():
    t0 = time.time()
    out = {}
    for name, fn in (("K9", k9), ("K10", k10), ("K11", k11), ("K12", k12), ("K7", k7), ("K0", k0), ("K8", k8), ("K6", k6),
                     ("K4", k4), ("K1", k1)):
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
