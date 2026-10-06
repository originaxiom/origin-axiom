#!/usr/bin/env python3
"""B1545 -- Lemma F at members, checked on sm:B1538's four room-3 covers at own characters nu over puncture characters.
At each member and class: the cusp partition (A: nu trivial; B: nu^4 trivial, nu not; C: the rest), k, b0, and route R's
h0(dN; W*), h1(dN; W), r1(W), n(W), n(W*); the predictions 2|A| + |B|, sum of 4/3/2/0, r1 <= 3|A| + |B| - k, I >= k - |A| - b0."""
import importlib.util
import json
import random
import sys
from math import gcd
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OUT = HERE / "members_check.json"
B1538V = ROOT / "frontier/B1538_the_puncture_characters/verification"
sys.path.insert(0, str(B1538V))
import punct_four as FO  # noqa: E402  (imports route_r first, as it must)
import punct_covers as F  # noqa: E402
import punct_present as RP  # noqa: E402
R = FO.R
WANT = {"m135.D8.2-0-4.w1": ("-LLRR", (2, 0, 4), 1), "m135.D8.4-0-2.w4": ("-LLRR", (4, 0, 2), 4),
        "m136.D8.2-0-4.w3": ("+LLRR", (2, 0, 4), 3), "m136.D8.4-0-2.w5": ("+LLRR", (4, 0, 2), 5)}
PER_COVER = 4
CAP = 20000                                                 # characters enumerated per order, at most


def lcm(a, b):
    return a * b // gcd(a, b)


def modules(C, cov, rho_p, ez, es, L, p, c=None):
    vals = C.rs_values(ez, es, L)
    r = RP.root_of_unity_mod(L, p)
    nu = [pow(r, C.chi_exp(w, vals, L), p) for w in cov.sword]
    rho_np = {g: np.array(m, dtype=np.int64) for g, m in rho_p.items()}
    rw = [R.base_word(rho_np, w, p) for w in cov.sword]
    Veta = R.CMod([m * pow(v, 5, p) % p for m, v in zip(rw, nu)], p)
    if c is None:
        return Veta, None, None, None
    Ws = []
    for j, (m, v) in enumerate(zip(rw, nu)):
        Lj = pow(v, -4, p)
        W = np.zeros((5, 5), dtype=np.int64)
        W[:4, :4] = m * v % p
        W[:4, 4] = np.array(c[j * 4:(j + 1) * 4], dtype=np.int64) * Lj % p
        W[4, 4] = Lj
        Ws.append(W % p)
    E = R.CMod(Ws, p)
    Es = E.dual()
    Lm = R.CMod([np.array([[pow(v, -4, p)]], dtype=np.int64) for v in nu], p)
    return Veta, E, Es, Lm


def support(CV, c, p, e=4):
    rc = R.mm(CV.R, np.asarray(c, dtype=np.int64).reshape(-1, 1) % p, p)
    out = []
    nc = CV.BP.shape[1] // e
    for i in range(nc):
        BPi = CV.BP[2 * e * i:2 * e * (i + 1), e * i:e * (i + 1)]
        if R.prank(np.hstack([BPi, rc[2 * e * i:2 * e * (i + 1)]]), p) > R.prank(BPi, p):
            out.append(i)
    return out


def covers():
    """the four room-3 covers first, then every other cover of sm:B1538's population with at least three cusps"""
    spec = importlib.util.spec_from_file_location("mc_b1538_run", B1538V / "run.py")
    RUN = importlib.util.module_from_spec(spec)
    sys.modules["mc_b1538_run"] = RUN
    spec.loader.exec_module(RUN)
    out = [(cid, v) for cid, v in WANT.items()]
    if "--wide" in sys.argv:
        for sw, lat, w, cid in RUN.population():
            if cid in WANT:
                continue
            C = F.Cover(F.State(sw), lat, w)
            if len(C.orbits) >= 3:
                out.append((cid, (sw, lat, w)))
    return out


def main():
    rng = random.Random(1545)
    rows = []
    for cid, (sw, lat, w) in covers():
        C = F.Cover(F.State(sw), lat, w)
        cov = R.PCover(C.st.G, C.perms)
        rho, _ = FO.exact_four(sw)
        found = 0
        tried = 0
        # the four room-3 covers: members over puncture characters only (b0 = 0, Corollary G's case), eight of them; the other
        # covers: the trivial chi first (members with nu^4 = 1, b0 = 1), then puncture characters, four members each
        quota = 2 * PER_COVER if cid in WANT else PER_COVER
        cands = [] if cid in WANT else [(tuple([0] * C.n), 1)]
        for M in (2, 4, 3, 6, 12):
            if C.count_characters(M) > CAP:                     # a large character group: skip that order (memory)
                continue
            cands += [(ezc, m) for ezc, m, _ in C.galois_reps(M) if C.is_puncture(ezc, m)]
        for M in (1,):
            for ezc, m in cands:
                if found >= quota:
                    break
                for k in (1, 2, 3, 4, 6):
                    if found >= quota:
                        break
                    for j in range(k):
                        if gcd(j, k) != 1 and not (k == 1 and j == 0):
                            continue
                        for ezp, mp in C.fourth_roots(ezc, m)[:3]:
                            for t in range(4):
                                L = lcm(lcm(mp, 4 * k), 24)
                                ezL = [e_ * (L // mp) % L for e_ in ezp]
                                es = (j + k * t) * (L // (4 * k)) % L
                                p = RP.primes_1_mod(L, 1 << 30, 1)[0]
                                rho_p = FO.four_mod_p(rho, p, L)
                                tried += 1
                                Veta, _, _, _ = modules(C, cov, rho_p, ezL, es, L, p)
                                CV = R.Coh(cov, Veta, keep=True)
                                if CV.h1 < 1:
                                    continue
                                A = set(C.trivial_cusps(ezL, es, L))
                                ez4 = [4 * e_ % L for e_ in ezL]
                                B = set(C.trivial_cusps(ez4, 4 * es % L, L)) - A
                                nc = len(cov.cusps)
                                for draw in range(2):
                                    a = np.array([[rng.randrange(1, p) for _ in range(CV.Zrows.shape[0])]], dtype=np.int64)
                                    c = R.mm(a, CV.Zrows, p).ravel()
                                    _, E, Es, Lm = modules(C, cov, rho_p, ezL, es, L, p, c)
                                    CW, CWs, CL = R.Coh(cov, E), R.Coh(cov, Es), R.Coh(cov, Lm)
                                    supp = support(CV, c, p)
                                    kk = len([T for T in supp if T in A])
                                    b0 = CL.a0
                                    h1pred = sum(4 if (T in A and T not in supp) else 3 if T in A else 2 if T in B else 0
                                                 for T in range(nc))
                                    I = CW.n - CWs.n
                                    row = {"cover": cid, "nu": {"zeta": list(ezp), "m": mp, "s": [j + k * t, 4 * k]},
                                           "chi=nu^4 zeta": list(ezc), "L": L, "p": p, "draw": draw,
                                           "A": sorted(A), "B": sorted(B), "cusps": nc, "support": supp, "k": kk, "b0": b0,
                                           "h0(dN;W*)": CWs.t0, "pred h0(dN;W*)": 2 * len(A) + len(B),
                                           "h1(dN;W)": CW.h1P, "pred h1(dN;W)": h1pred, "r1(W)": CW.r1,
                                           "bound r1": 3 * len(A) + len(B) - kk, "I(W)": I, "bound I": kk - len(A) - b0,
                                           "identity": I == CW.a0 - CWs.a0 + CWs.t0 - CW.r1}
                                    row["holds"] = (row["h0(dN;W*)"] == row["pred h0(dN;W*)"] and row["h1(dN;W)"] ==
                                                    row["pred h1(dN;W)"] and row["r1(W)"] <= row["bound r1"] and
                                                    I >= row["bound I"] and row["identity"] and set(supp) <= set(range(nc)))
                                    rows.append(row)
                                    print(json.dumps({k_: row[k_] for k_ in ("cover", "A", "B", "support", "k", "b0",
                                                                             "h0(dN;W*)", "pred h0(dN;W*)", "h1(dN;W)",
                                                                             "pred h1(dN;W)", "r1(W)", "bound r1", "I(W)",
                                                                             "bound I", "holds")}), flush=True)
                                found += 1
                                if found >= quota:
                                    break
                            if found >= quota:
                                break
                        if found >= quota:
                            break
        print(cid, "members found", found, "fourth roots tried", tried, flush=True)
    OUT.write_text(json.dumps({"rows": rows, "all hold": all(r["holds"] for r in rows), "n": len(rows)}, indent=1) + "\n")
    print("all hold:", all(r["holds"] for r in rows), len(rows))


if __name__ == "__main__":
    main()
