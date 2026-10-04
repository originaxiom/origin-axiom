#!/usr/bin/env python3
"""B1539 -- THE CONTROLS (PREREGISTRATION.md section 6), on banked data or on values the banked rows already fix.  No own
character of order 3 or more is read here.

  K1  route R' and route P' at pulled-back characters of m003's d5.2, d5.3 and d10.4 (every twelfth) reproduce sm:B1536's banked
      route-R supplies; the abelianisation recovers each one as a character of H_1(N).
  K2  the run's own configuration (m = 60, route_primes): the fourteen order-2 own characters of d5.2 and d5.3.  Each N_c
      (own_chars.abelian_cover) is one of sm:B1536's banked degree-10 covers (cover_lib.canonical); route N on N_c, the banked
      row, and the sums n_N(1) + n_N(c), n_N(rho) + n_N(rho c) of route R' and of route P' all agree.
  K3  routes R' and P' agree in every field at every reading of K1, K2 and K7.
  K4  Lemma A' on non-cyclic covers: on d5.2 and d5.3, every (Z/2)^2 subgroup and the whole (Z/2)^3 of order-2 characters:
      route N on N_A equals the sums of K2's readings in both routes.
  K5  the population by structure: each member's orbit count equals the formula sum over k | m of J_r(k)/phi(k) on its free rank
      r (members without torsion), and the orbits partition the characters (own_chars.orbit_reps' own assertions).
  K6  the read-out on synthetic rows (read_out.evaluate): every prediction's True, False and None cases.
  K7  both routes at the trivial character of every member, at the run's primes: (n(1), n(rho)) equal the banked row, with
      capW = 1 + n(1) and capL2 = n(rho).
  K8  Lemma C on banked data: on every Galois orbit of pulled-back characters that sm:B1536 read in full (both states, every
      cover), the banked supplies are constant; and route R' at the Galois conjugates of K1's d5.2 characters equals the
      banked reading at the conjugate.
What K2 and K4 read is fixed by the banked degree-10 rows and Lemma A' (n_N(c) = n(1)(N_c) - n_N(1), and likewise for rho).

    python3 controls.py [--record]     ->  controls.json (about ten minutes)"""
import gzip
import json
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _sib(alias, name):
    """this arc's own modules, by path under unique names (E12: sm:B1536's route_r puts sm:B1535's folder, with its own
    read_out.py and controls.py, first on sys.path, and sm:B1536's has its own population.py and run.py)"""
    import importlib.util
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, HERE / name)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


O = _sib("b1539_own_chars", "own_chars.py")          # loads route_r first: it allocates PARI's stack
PO = _sib("b1539_population", "population.py")
RO = _sib("b1539_read_out", "read_out.py")
import numpy as np  # noqa: E402
from cypari import pari  # noqa: E402

POP = PO.POP
KEYS = ("h1(V_eta)", "n(V_eta)", "b0", "n(L)", "n((VL)*)", "capW", "capL2")


def banked(route, state):
    out = {}
    for line in gzip.open(O.B1536V / f"run_{route}_{state}.jsonl.gz", "rt"):
        r = json.loads(line)
        if not r.get("done"):
            out[(r["cover"], tuple(r["u"]), r["kappa"])] = r
    return out


def pulled_setup(st, perms):
    cus, L, Nroot, chars = POP.characters(st, perms)
    p = O.GF.primes_1_mod(Nroot, 1 << 31, 1)[0]
    B = O.RN.Base(st, O.GF.GF(p, Nroot))
    cov = O.R.PCover(st["G"], perms)
    rho_np = {g: np.asarray(B.rho[g], dtype=np.int64) % p for g in B.gens}
    return chars, Nroot, p, B, cov, rho_np


def along_words(cov, chi, p, Nroot):
    """a pulled-back character's values on the Schreier generators, as exponents of route R's primitive Nroot-th root"""
    r = int(pari.lift(pari.znprimroot(p) ** ((p - 1) // Nroot)))
    table = {pow(r, e, p): e for e in range(Nroot)}
    out = []
    for w in cov.sword:
        v = 1
        for c in w:
            x = int(chi[c.lower()])
            v = v * (x if c.islower() else pow(x, -1, p)) % p
        out.append(table[v])
    return out


def run_config(st, perms, m, route):
    """the run's own setup for one route: (cov, rho mod p, p, Presentation or None)"""
    p = O.route_primes(m)[route]
    B = O.RN.Base(st, O.GF.GF(p, O.root_order(m)))
    rho_np = {g: np.asarray(B.rho[g], dtype=np.int64) % p for g in B.gens}
    cov = O.R.PCover(st["G"], perms)
    Pr = O.punct_present().Presentation(O.Shim(st["G"], perms)) if route == "P" else None
    return cov, rho_np, p, Pr


def reading(st, perms, cfg, exps, m, route):
    cov, rho_np, p, Pr = cfg
    if route == "R":
        return O.frame_own(cov, rho_np, exps, m, p)
    return O.frame_own_p(st["G"], perms, cov, rho_np, exps, m, p, Pr)


def route_n(st, pe):
    cus, L, Nroot, _ = POP.characters(st, pe)
    p = O.GF.primes_1_mod(Nroot, O.RN.P_BOUND, 1)[0]
    B = O.RN.Base(st, O.GF.GF(p, Nroot))
    sN = O.RN.supplies(B, O.RN.perm_arrays(st["G"], pe), B.character((Fr(0), Fr(0)), Fr(0)))
    return sN["n(L)"], sN["n((VL)*)"]


# ============================================================================================ K1 (and K3's share)
def k1(rep):
    st = O.CL.state("m003")
    G = st["G"]
    covs = dict(POP.covers(st))
    rows = banked("R", "m003")
    ok, n, agree, kept = True, 0, True, {}
    for cid in ("d5.2", "d5.3", "d10.4"):
        chars, Nroot, p, B, cov, rho_np = pulled_setup(st, covs[cid])
        ab = O.Ab(cov)
        Pr = O.punct_present().Presentation(O.Shim(G, covs[cid]))
        for (u, kap) in chars[:: max(1, len(chars) // 12)]:
            exps = along_words(cov, B.character(u, kap), p, Nroot)
            a = O.frame_own(cov, rho_np, exps, Nroot, p)
            b = O.frame_own_p(G, covs[cid], cov, rho_np, exps, Nroot, p, Pr)
            bk = rows[(cid, (str(u[0]), str(u[1])), str(kap))]["S"]
            same = all(a[k] == bk[k] for k in KEYS) and ab.coordinates(exps, Nroot) is not None
            ok &= same
            agree &= a == b
            n += 1
            if cid == "d5.2":
                kept[(u, kap)] = (exps, a)
    rep["K1"] = {"readings": n, "holds": ok}
    rep["K3"]["K1 readings agree"] = agree
    return kept


# ============================================================================================ K2, K4 (and K3's share)
def k2_k4(rep):
    st = O.CL.state("m003")
    G = st["G"]
    covs = dict(POP.covers(st))
    rowsN = banked("N", "m003")
    canon = {O.CL.canonical(p, G.gens): cid for cid, p in covs.items() if len(p["a"]) == 10}
    m = 60
    k2, k4, agree, n2, n4, detail = True, True, True, 0, 0, {}
    for cid in ("d5.2", "d5.3"):
        perms = covs[cid]
        cfg = {r: run_config(st, perms, m, r) for r in ("R", "P")}
        cov = cfg["R"][0]
        ab = O.Ab(cov)
        rd = {}
        for c in [c for c in ab.characters(m) if all(x in (0, 30) for x in c)]:
            exps = ab.exponents(c, m)
            rd[c] = {r: reading(st, perms, cfg[r], exps, m, r) for r in ("R", "P")}
            agree &= rd[c]["R"] == rd[c]["P"]
        zero = (0, 0, 0)
        for c in rd:
            if not any(c):
                continue
            pe, nA = O.abelian_cover(cov, ab, [c], m)
            assert nA == 2 and O.CL.check_cover(G, pe)
            cid2 = canon.get(O.CL.canonical(pe, G.gens))
            bk = rowsN[(cid2, ("0", "0"), "0")]["S"]
            sN = route_n(st, pe)
            sums = {r: (rd[zero][r]["n(nu)"] + rd[c][r]["n(nu)"], rd[zero][r]["n(rho nu)"] + rd[c][r]["n(rho nu)"])
                    for r in ("R", "P")}
            ok = sN == (bk["n(L)"], bk["n((VL)*)"]) == sums["R"] == sums["P"]
            k2 &= ok
            n2 += 1
            detail[f"{cid} {c}"] = {"N_c": cid2, "route N": list(sN), "banked": [bk["n(L)"], bk["n((VL)*)"]],
                                    "sums R": list(sums["R"]), "sums P": list(sums["P"])}
        order2 = [c for c in rd if any(c)]
        groups = [list(g) for g in combinations(order2, 2) if len(RO.subgroup(list(g), m)) == 4]
        seen = set()
        for g in groups + [order2[:3]]:
            H = frozenset(RO.subgroup(g, m))
            if H in seen:
                continue
            seen.add(H)
            pe, nA = O.abelian_cover(cov, ab, g, m)
            assert nA == len(H) and O.CL.check_cover(G, pe)
            sN = route_n(st, pe)
            sums = {r: (sum(rd[c][r]["n(nu)"] for c in H), sum(rd[c][r]["n(rho nu)"] for c in H)) for r in ("R", "P")}
            ok = sN == sums["R"] == sums["P"]
            k4 &= ok
            n4 += 1
            detail[f"{cid} A = <{', '.join(map(str, g))}>"] = {"|A|": nA, "degree": len(pe["a"]), "route N": list(sN),
                                                                "sums R": list(sums["R"]), "sums P": list(sums["P"])}
    rep["K2"] = {"order-2 characters": n2, "holds": k2}
    rep["K4"] = {"abelian covers": n4, "holds": k4}
    rep["K3"]["K2 readings agree"] = agree
    rep["K2, K4 detail"] = detail


# ============================================================================================ K5
def jordan(r, k):
    out = k ** r
    for q in range(2, k + 1):
        if k % q == 0 and all(q % s for s in range(2, q)):
            out = out * (q ** r - 1) // (q ** r)
    return out


def k5(rep):
    ok, rows = True, {}
    for st, cid, deg, n1, nr, cus in PO.members():
        S, perms, cov, ab = PO.cover(st, cid)
        m = PO.modulus(deg)
        reps = O.orbit_reps(ab, m)
        r = len(ab.free)
        row = {"orbits": len(reps), "characters": sum(s for _, s, _ in reps)}
        if not ab.torsion:
            want = sum(jordan(r, k) // RO.phi(k) for k in range(1, m + 1) if m % k == 0)
            row["formula"] = want
            ok &= want == len(reps) and row["characters"] == m ** r
        rows[f"{st}:{cid}"] = row
    rep["K5"] = {"members": len(rows), "holds": ok, "by member": rows}


# ============================================================================================ K6
def k6(rep):
    """synthetic members: 'X:a' with characters of Z/6 (one free coordinate) and 'X:b' likewise; readings set by hand"""
    m = 6
    reps = {(0,): 1, (1,): 2, (2,): 2, (3,): 1}
    struct = {"m003:d5.2": {"degree": 5, "m": m, "n(1)": 1, "n(rho)": 1, "reps": dict(reps), "sampled": {(1,): [(1,), (5,)]}}}

    def S(line, four, capW=1, capL2=1):
        s = {f: 0 for f in RO.FRAME}
        s.update({"n(nu)": line, "n(rho nu)": four, "capW": capW, "capL2": capL2})
        return s

    def rows(route, vals, extra=()):
        out = [{"route": route, "state": "m003", "cover": "d5.2", "c": list(c), "S": S(*vals[c])} for c in reps]
        out += [{"route": route, "state": "m003", "cover": "d5.2", "c": [5], "sample of": [1], "S": S(*vals[(1,)])}]
        return out + list(extra)
    base = {(0,): (1, 1), (1,): (0, 0), (2,): (0, 0), (3,): (0, 1)}
    ident = {"identity holds": True}
    cases, ok = {}, True

    def run(name, Rr, Pr, Nr, want):
        nonlocal ok
        res = RO.evaluate(ident, Rr, Pr, Nr, struct, say=lambda s: None)
        got = {k: res["predictions"][k] for k in want}
        cases[name] = {"want": want, "got": got, "pass": got == want}
        ok &= got == want
        return res

    def nrows(vals):
        Rr, Pr = rows("R", vals), rows("P", vals)
        ev = RO.evaluate(ident, Rr, Pr, [], struct, say=lambda s: None)
        sel = RO.selection(ev["witnesses"], struct)
        out = []
        for (key, gens) in sel:
            H = RO.subgroup(list(gens), m)
            M = RO.Member(m, {c: S(*vals[c]) for c in reps})
            n1, nr = M.abelian(H)
            out.append({"state": "m003", "cover": "d5.2", "generators": [list(g) for g in gens], "n(1)": n1, "n(rho)": nr})
        return out
    run("negative, complete", rows("R", base), rows("P", base), nrows(base),
        {"P1": True, "P2": True, "P3": True, "P4": False, "P4c": False, "P5": False, "P6": False, "P7": False})
    pos = dict(base)
    pos[(2,)] = (1, 1)
    run("joint point of order 3: room three on N_c (degree 15)", rows("R", pos), rows("P", pos), nrows(pos),
        {"P1": True, "P3": True, "P4": True, "P4c": True, "P5": True, "P7": True})
    ab_only = dict(base)
    ab_only[(1,)] = (1, 0)                       # the line at order 6 only; the four at order 2 only
    run("line at order 6, four at order 2: N_c of order 6 has (n(1), n(rho)) = (3, 2), room 2; N_m likewise",
        rows("R", ab_only), rows("P", ab_only), nrows(ab_only), {"P3": True, "P4": False, "P4c": False, "P7": True})
    two = dict(base)
    two[(1,)] = (1, 1)
    res = run("line and four at order 6: room three; the witness (order 6, degree 30) is read by route N",
              rows("R", two), rows("P", two), nrows(two), {"P3": True, "P4": True, "P4c": True, "P7": True, "P5": False})
    cases["line and four at order 6: room three; the witness (order 6, degree 30) is read by route N"]["witness"] = \
        res["witnesses"]
    capped = {c: v for c, v in base.items()}
    fr = rows("R", capped)
    fr[2] = dict(fr[2], S=S(0, 0, 3, 3))
    fp = rows("P", capped)
    fp[2] = dict(fp[2], S=S(0, 0, 3, 3))
    run("the frame at nu = c itself has room three (both routes)", fr, fp, [], {"P6": True})
    fp2 = rows("P", capped)
    run("the frame's room three in one route only", fr, fp2, [], {"P1": False, "P6": False})
    run("one route only shows the line: a disagreement, no positive", rows("R", two), rows("P", base), [],
        {"P1": False, "P4": False, "P7": False})
    bad = rows("R", base)
    bad[-1] = dict(bad[-1], S=S(1, 1))
    run("Lemma C fails on the sampled orbit", bad, rows("P", base), nrows(base), {"P2": False})
    run("a missing representative gives None, never False", rows("R", base)[1:], rows("P", base), nrows(base),
        {"P1": None, "P4": None, "P7": None})
    run("a duplicate row gives None", rows("R", base) + rows("R", base)[:1], rows("P", base), nrows(base),
        {"P1": None, "P4": None})
    wrongN = nrows(base)
    if wrongN:
        wrongN[0] = dict(wrongN[0], **{"n(rho)": wrongN[0]["n(rho)"] + 1})
    run("route N disagrees with Lemma A'", rows("R", base), rows("P", base), wrongN, {"P3": False})
    run("route N missing gives P3 None", rows("R", base), rows("P", base), [], {"P3": None})
    rep["K6"] = {"cases": len(cases), "holds": ok, "detail": cases}


# ============================================================================================ K7 (and K3's share)
def k7(rep):
    rooms = json.loads((O.B1536V / "post_run_rooms.json").read_text())
    want = {(st, x["cover"]): (x["n(1)"], x["n(rho)"]) for st in ("m004", "m003")
            for x in rooms[st]["trivial character supplies"]}
    ok, agree, n = True, True, 0
    for st, cid, deg, n1, nr, cus in PO.members():
        S, perms, cov, ab = PO.cover(st, cid)
        m = PO.modulus(deg)
        rr = {}
        for r in ("R", "P"):
            cfg = run_config(S, perms, m, r)
            rr[r] = reading(S, perms, cfg, [0] * ab.n, m, r)
        n1b, nrb = want[(st, cid)]
        for r in rr.values():
            ok &= (r["n(nu)"], r["n(rho nu)"]) == (n1b, nrb) and r["capW"] == 1 + n1b and r["capL2"] == nrb
        agree &= rr["R"] == rr["P"]
        n += 1
    rep["K7"] = {"members": n, "holds": ok}
    rep["K3"]["K7 readings agree"] = agree


# ============================================================================================ K8
def k8(rep, kept):
    total = full = bad = 0
    for state in ("m004", "m003"):
        rows = banked("R", state)
        by_cover = {}
        for (cid, u, kap), r in rows.items():
            by_cover.setdefault(cid, {})[(Fr(u[0]), Fr(u[1]), Fr(kap))] = r["S"]
        for cid, chars in by_cover.items():
            N = 1
            for (a, b, k) in chars:
                for x in (a, b, k):
                    N = N * x.denominator // gcd(N, x.denominator)
            seen = set()
            for ch in chars:
                if ch in seen:
                    continue
                orb = {tuple((a * x) % 1 for x in ch) for a in range(1, N + 1) if gcd(a, N) == 1}
                seen |= orb
                total += 1
                if not orb <= set(chars):
                    continue
                full += 1
                if any(any(chars[o][k] != chars[ch][k] for k in KEYS) for o in orb):
                    bad += 1
    # route R' at the Galois conjugates of K1's d5.2 characters (exponents scaled by a unit) equals the banked conjugate
    st = O.CL.state("m003")
    covs = dict(POP.covers(st))
    rowsR = banked("R", "m003")
    chars, Nroot, p, B, cov, rho_np = pulled_setup(st, covs["d5.2"])
    conj_ok, nconj = True, 0
    for (u, kap), (exps, a0) in list(kept.items())[:6]:
        for a in (7, 11):
            if gcd(a, Nroot) != 1:
                continue
            uc, kc = (Fr(a) * u[0] % 1, Fr(a) * u[1] % 1), Fr(a) * kap % 1
            key = ("d5.2", (str(uc[0]), str(uc[1])), str(kc))
            if key not in rowsR:
                continue
            got = O.frame_own(cov, rho_np, [(a * e) % Nroot for e in exps], Nroot, p)
            conj_ok &= all(got[k] == rowsR[key]["S"][k] for k in KEYS)
            nconj += 1
    rep["K8"] = {"banked Galois orbits": total, "read in full": full, "not constant": bad, "conjugate readings": nconj,
                 "holds": bad == 0 and full > 0 and conj_ok and nconj > 0}


def main():
    rep = {"K3": {}}
    t = {}
    for name, f in (("K1", None), ("K2, K4", k2_k4), ("K5", k5), ("K6", k6), ("K7", k7)):
        t0 = time.time()
        if name == "K1":
            kept = k1(rep)
        else:
            f(rep)
        t[name] = round(time.time() - t0, 1)
        print(name, "done", t[name], "s", flush=True)
    t0 = time.time()
    k8(rep, kept)
    t["K8"] = round(time.time() - t0, 1)
    rep["K3"]["holds"] = all(v for k, v in rep["K3"].items() if k != "holds")
    rep["seconds"] = t
    rep["all hold"] = all(rep[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"))
    for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"):
        print(k, {x: y for x, y in rep[k].items() if x not in ("by member", "detail")})
    print("ALL HOLD:", rep["all hold"])
    if "--record" in sys.argv:
        (HERE / "controls.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")
    return rep


if __name__ == "__main__":
    main()
