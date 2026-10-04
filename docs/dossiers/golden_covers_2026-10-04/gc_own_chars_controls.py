#!/usr/bin/env python3
"""The golden covers dossier, section 6: the controls of the next arc's draft instruments (gc_own_chars.py), on banked data or
data the banked rows already fix.  No own character of order 3 or more is read.

  K1  route R' (sm:B1536's route_r on the cover, with nu read along the Schreier words) at pulled-back characters of m003's
      d5.2 and d10.4 reproduces sm:B1536's banked route-R supplies; the abelianisation recovers each one as a character of
      H_1(N), consistent on every Schreier generator.
  K2  every order-2 own character of d5.2 and d5.3: the double cover N_e (gc_own_chars.cyclic_cover) is one of sm:B1536's banked
      degree-10 covers (cover_lib.canonical); route N on N_e (sm:B1536's, by path) at the trivial character, the banked row,
      and route R''s sums n_N(1) + n_N(e), n_N(rho) + n_N(rho e) all agree.
  K3  route P' (sm:B1538's punct_present, by path, on gc_own_chars.Shim) agrees with route R' at the pulled-back characters of
      d5.2, d5.3, d10.4 and the order <= 2 own characters of d5.2, d5.3.
What K2 reads is fixed by the banked degree-10 rows (n_N(e) = n(1)(N_e) - n_N(1) and likewise for rho).

    python3 gc_own_chars_controls.py      (about 20 s)"""
import gzip
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gc_own_chars as O  # noqa: E402  (loads route_r first: it allocates PARI's stack)
import numpy as np  # noqa: E402
from cypari import pari  # noqa: E402

POP = O._load("b1536_population_gc", O.B1536V / "population.py")
N = O._load("b1536_route_n_gc", O.B1536V / "route_n.py")
gf = O._load("b1536_gf_gc", O.B1536V / "gf.py")


def banked_rows(route, state):
    out = {}
    for line in gzip.open(O.B1536V / f"run_{route}_{state}.jsonl.gz", "rt"):
        r = json.loads(line)
        if not r.get("done"):
            out[(r["cover"], tuple(r["u"]), r["kappa"])] = r
    return out


def setup(st, perms):
    cus, L, Nroot, chars = POP.characters(st, perms)
    p = gf.primes_1_mod(Nroot, 1 << 31, 1)[0]
    B = N.Base(st, gf.GF(p, Nroot))
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


def main():
    st = O.CL.state("m003")
    G = st["G"]
    covs = dict(POP.covers(st))
    rowsR, rowsN = banked_rows("R", "m003"), banked_rows("N", "m003")
    keys = ("h1(V_eta)", "n(V_eta)", "b0", "n(L)", "n((VL)*)", "capW", "capL2")
    k1 = k3 = k2 = True
    n1 = n2 = n3 = 0
    canon = {O.CL.canonical(p, G.gens): cid for cid, p in covs.items() if len(p["a"]) == 10}
    for cid in ("d5.2", "d5.3", "d10.4"):
        chars, Nroot, p, B, cov, rho_np = setup(st, covs[cid])
        ab = O.Ab(cov)
        Pr = O.punct_present().Presentation(O.Shim(G, covs[cid]))
        print(f"{cid}: H_1 = Z^{len(ab.free)} + {[d for _, d in ab.torsion]}; prime {p}", flush=True)
        for (u, kap) in chars[:: max(1, len(chars) // 12)]:
            exps = along_words(cov, B.character(u, kap), p, Nroot)
            a = O.frame_own(cov, rho_np, exps, Nroot, p)
            banked = rowsR[(cid, (str(u[0]), str(u[1])), str(kap))]["S"]
            same = all(a[k] == banked[k] for k in keys)
            back = ab.coordinates(exps, Nroot) is not None
            b = O.frame_own_p(G, covs[cid], cov, rho_np, exps, Nroot, p, Pr)
            k1 &= same and back
            k3 &= a == b
            n1 += 1
            n3 += 1
        if cid == "d10.4":
            continue
        base = O.frame_own(cov, rho_np, [0] * ab.n, 2, p)
        for c in ab.characters(2):
            exps = ab.exponents(c, 2)
            own = O.frame_own(cov, rho_np, exps, 2, p)
            k3 &= own == O.frame_own_p(G, covs[cid], cov, rho_np, exps, 2, p, Pr)
            n3 += 1
            if not any(c):
                continue
            pe, k = O.cyclic_cover(cov, ab, c, 2)
            assert k == 2 and O.CL.check_cover(G, pe)
            cid2 = canon.get(O.CL.canonical(pe, G.gens))
            cus2, L2, Nr2, _ = POP.characters(st, pe)
            p2 = gf.primes_1_mod(Nr2, N.P_BOUND, 1)[0]
            B2 = N.Base(st, gf.GF(p2, Nr2))
            sN = N.supplies(B2, N.perm_arrays(G, pe), B2.character((Fr(0), Fr(0)), Fr(0)))
            bk = rowsN[(cid2, ("0", "0"), "0")]["S"]
            sums = (base["n(nu)"] + own["n(nu)"], base["n(rho nu)"] + own["n(rho nu)"])
            ok = (sN["n(L)"], sN["n((VL)*)"]) == (bk["n(L)"], bk["n((VL)*)"]) == sums
            k2 &= ok
            n2 += 1
            print(f"  e = {c}: N_e = {cid2}; (n(1), n(rho)) route N {(sN['n(L)'], sN['n((VL)*)'])}, banked "
                  f"{(bk['n(L)'], bk['n((VL)*)'])}, route R' sums {sums}; n_N(e) = {own['n(nu)']}, n_N(rho e) = "
                  f"{own['n(rho nu)']}", flush=True)
    print(f"K1 ({n1} pulled-back characters): {k1}")
    print(f"K2 ({n2} order-2 own characters): {k2}")
    print(f"K3 ({n3} readings): {k3}")
    print("ALL HOLD:", k1 and k2 and k3)


if __name__ == "__main__":
    main()
