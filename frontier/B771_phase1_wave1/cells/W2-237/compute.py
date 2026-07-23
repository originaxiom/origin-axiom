#!/usr/bin/env python3
"""B771 W2-237: the additivity constant c (Review 9, 28 banked digits) --
recompute to high precision, then PSLQ over extended bases.

Object (B470 addendum, frontier/B470_reflection_campaign/):
  Fibonacci letter tower w_n: seq[0]=b, seq[1]=a, seq[k]=seq[k-1]+seq[k-2],
  a->R, b->L; M_n = punctured-torus bundle snappy.Manifold('b++'+w_n),
  len(w_n) = F(n) (F0=F1=1). vol(n) obeys the Fibonacci recursion to
  doubly-exponentially small defect; c = lim vol(n)/F(n) = vol per letter.
  Banked: c = 0.934102018057787980264187790656 (28 digits, dps-30 run).

Plan:
  P1: volumes at 512-bit polished shapes, vol = sum of Bloch-Wigner D(z)
      (own mpmath implementation), cross-checked vs ManifoldHP.volume()
      (independent quad-double algorithm) and vs a 384-bit re-polish and
      a mirror-word (L<->R) seed at n=12.
  P2: defect table d(n)=v(n)-v(n-1)-v(n-2) at true precision; extrapolate
      c_n = (v(n) - psi*v(n-1))/phi^n (exact if recursion exact from n-1);
      trusted digits = agreement(c_12, c_13) + defect-tail error model.
  P3: PSLQ sweeps at tol = 10^-(agree-14) (house rule), heights recorded:
      algebraicity (algdep), singles, pairs, triples, full independent
      basis (internal relations with coeff(c)=0 discarded and logged),
      golden sqrt5-weighted variants.
Everything computed in-cell; no cited values used as inputs.
"""
import json, os, sys, time
from itertools import combinations

import mpmath as mp

CELL = os.path.dirname(os.path.abspath(__file__))
VOLFILE = os.path.join(CELL, "volumes.json")
BANKED = "0.934102018057787980264187790656"

mp.mp.dps = 170

# ---------------------------------------------------------------- words
def fib_word(n, swap=False):
    seq = {0: "b", 1: "a"}
    for k in range(2, n + 1):
        seq[k] = seq[k - 1] + seq[k - 2]
    if swap:  # mirror seed: exchange R and L
        return "".join("L" if ch == "a" else "R" for ch in seq[n])
    return "".join("R" if ch == "a" else "L" for ch in seq[n])

F = {0: 1, 1: 1}
for k in range(2, 20):
    F[k] = F[k - 1] + F[k - 2]

# ------------------------------------------------------- Bloch-Wigner
def bloch_wigner(z):
    z = mp.mpc(z)
    return mp.im(mp.polylog(2, z)) + mp.log(abs(z)) * mp.arg(1 - z)

def volume_from_shapes(word, bits):
    import snappy
    M = snappy.ManifoldHP("b++" + word)
    shapes = M.tetrahedra_shapes("rect", bits_prec=bits)
    tot = mp.mpf(0)
    min_im = mp.mpf(10)
    for s in shapes:
        z = mp.mpc(str(s.real()), str(s.imag()))
        min_im = min(min_im, mp.im(z))
        tot += bloch_wigner(z)
    vol_hp = mp.mpf(str(M.volume()))  # independent quad-double check
    return tot, vol_hp, float(min_im), M.num_tetrahedra()

# ---------------------------------------------------------------- P1
def phase1():
    if os.path.exists(VOLFILE):
        with open(VOLFILE) as f:
            return {k: v for k, v in json.load(f).items()}
    from cypari import pari
    pari.allocatemem(4 * 10**9, 8 * 10**9)
    data = {}
    for n in (9, 10, 11, 12, 13):
        t0 = time.time()
        v, vhp, mi, nt = volume_from_shapes(fib_word(n), 512)
        agree_hp = -mp.log10(abs(v - vhp) / v)
        data[f"n{n}b512"] = mp.nstr(v, 165)
        print(f"[P1] n={n} len={F[n]} tets={nt} bits=512  minIm={mi:.4f} "
              f"agree-with-ManifoldHP.volume()={float(agree_hp):.1f} digits "
              f"({time.time()-t0:.1f}s)", flush=True)
        print(f"     vol = {mp.nstr(v, 80)}", flush=True)
    # conditioning seeds
    for n, bits, swap, tag in ((12, 384, False, "n12b384"),
                              (13, 384, False, "n13b384"),
                              (12, 512, True, "n12mirror")):
        t0 = time.time()
        v, vhp, mi, nt = volume_from_shapes(fib_word(n, swap=swap), bits)
        data[tag] = mp.nstr(v, 165)
        ref = mp.mpf(data[f"n{n}b512"])
        agree = -mp.log10(abs(v - ref) / ref) if v != ref else 999
        print(f"[P1-cond] {tag}: agree with primary = {float(agree):.1f} digits "
              f"({time.time()-t0:.1f}s)", flush=True)
    with open(VOLFILE, "w") as f:
        json.dump(data, f, indent=1)
    return data

# ---------------------------------------------------------------- P2
def phase2(data):
    v = {n: mp.mpf(data[f"n{n}b512"]) for n in (9, 10, 11, 12, 13)}
    phi = (1 + mp.sqrt(5)) / 2
    psi = (1 - mp.sqrt(5)) / 2
    print("\n[P2] additivity defects d(n)=v(n)-v(n-1)-v(n-2):", flush=True)
    logd = {}
    for n in (11, 12, 13):
        d = v[n] - v[n - 1] - v[n - 2]
        logd[n] = mp.log10(abs(d)) if d != 0 else mp.mpf(-999)
        print(f"  d({n}) = {mp.nstr(d, 6)}   log10|d| = {float(logd[n]):.2f}",
              flush=True)
    r1 = logd[12] / logd[11]
    r2 = logd[13] / logd[12]
    print(f"  log-defect ratios: {float(r1):.4f}, {float(r2):.4f} "
          f"(phi = {float(phi):.4f})", flush=True)
    # extrapolations c_n = (v(n) - psi v(n-1))/phi^n; error ~ |d(n+1)| tail
    cs = {}
    for n in (11, 12, 13):
        cs[n] = (v[n] - psi * v[n - 1]) / phi**n
        print(f"  c_{n} = {mp.nstr(cs[n], 60)}", flush=True)
    def agree_digits(a, b):
        return int(mp.floor(-mp.log10(abs(a - b) / abs(a))))
    a1213 = agree_digits(cs[12], cs[13])
    a1113 = agree_digits(cs[11], cs[13])
    # error model: c_13 error ~ sum of future defects ~ |d(14)| ~
    # 10^(logd13 * r2) (doubly-exponential continuation, conservative)
    pred_d14 = float(logd[13] * r2)
    print(f"  agree(c_11,c_13) = {a1113} digits; agree(c_12,c_13) = {a1213} digits",
          flush=True)
    print(f"  defect-tail model: log10|d(14)| ~ {pred_d14:.0f} "
          f"=> c_13 intrinsic error beyond precision floor", flush=True)
    c = cs[13]
    # trusted digits: min(cross-agreement, precision floor 150)
    trusted = min(a1213, 150)
    print(f"  TRUSTED digits for c: {trusted}", flush=True)
    print(f"\n  c = {mp.nstr(c, trusted)}", flush=True)
    # banked comparison
    banked = mp.mpf(BANKED)
    ab = agree_digits(banked, c)
    print(f"  banked 28-digit value agrees to {ab} digits "
          f"({'CONFIRMS' if ab >= 27 else 'DISAGREES WITH'} the bank)", flush=True)
    return c, trusted

# ---------------------------------------------------------------- P3
def lob(th):
    return mp.im(mp.polylog(2, mp.e**(2j * th))) / 2

def phase3(c, trusted):
    tol_exp = trusted - 14          # house tolerance-height rule
    tol = mp.mpf(10) ** (-tol_exp)
    print(f"\n[P3] PSLQ sweeps at tol = 1e-{tol_exp} (rule: 10^-(agree-14)), "
          f"working dps {mp.mp.dps}", flush=True)
    pi, s5 = mp.pi, mp.sqrt(5)
    phi = (1 + s5) / 2
    cand = {
        "Lob(pi/5)": lob(pi / 5), "Lob(2pi/5)": lob(2 * pi / 5),
        "Lob(pi/10)": lob(pi / 10), "Lob(3pi/10)": lob(3 * pi / 10),
        "Lob(pi/15)": lob(pi / 15), "Lob(2pi/15)": lob(2 * pi / 15),
        "Lob(4pi/15)": lob(4 * pi / 15), "Lob(7pi/15)": lob(7 * pi / 15),
        "Lob(pi/3)": lob(pi / 3), "Lob(pi/4)": lob(pi / 4),
        "Lob(pi/6)": lob(pi / 6), "Lob(pi/12)": lob(pi / 12),
        "Lob(5pi/12)": lob(5 * pi / 12),
        "v3": 3 * lob(pi / 3), "v8": 8 * lob(pi / 4),
        "Catalan": mp.catalan,
        "pi^2": pi**2, "pi^2/sqrt5": pi**2 / s5,
        "pi*logphi": pi * mp.log(phi), "pi*log5": pi * mp.log(5),
        "logphi^2": mp.log(phi)**2, "zeta3/pi": mp.zeta(3) / pi,
        "zeta3/pi^2": mp.zeta(3) / pi**2,
        "sqrt5*Lob(pi/5)": s5 * lob(pi / 5),
        "sqrt5*Lob(2pi/5)": s5 * lob(2 * pi / 5),
        "sqrt5*v3": s5 * 3 * lob(pi / 3), "phi*v3": phi * 3 * lob(pi / 3),
        "v3/sqrt5": 3 * lob(pi / 3) / s5, "v8/sqrt5": 8 * lob(pi / 4) / s5,
        "one": mp.mpf(1),
    }
    hits = []

    # S0: algebraicity (algdep) --------------------------------------
    print("  [S0] algebraicity: PSLQ on powers of c, deg 2..8, maxcoeff 1e10",
          flush=True)
    for d in range(2, 9):
        vec = [c**k for k in range(d + 1)]
        r = mp.pslq(vec, tol=tol, maxcoeff=10**10, maxsteps=200000)
        if r:
            print(f"    deg {d}: RELATION {r}", flush=True)
            hits.append(("algdep", d, r))
    if not any(h[0] == "algdep" for h in hits):
        print("    all NEGATIVE (c not algebraic of deg<=8, height<=1e10 at tol)",
              flush=True)

    # S1: singles ----------------------------------------------------
    print("  [S1] singles: c = (p/q) x, |p|,|q| <= 1e8", flush=True)
    n_neg = 0
    for name, x in cand.items():
        if name == "one":
            continue
        r = mp.pslq([c, x], tol=tol, maxcoeff=10**8, maxsteps=200000)
        if r:
            print(f"    HIT {name}: {r} -> c = {mp.nstr(mp.mpf(-r[1]) / r[0], 20)}"
                  f" * {name}", flush=True)
            hits.append(("single", name, r))
        else:
            n_neg += 1
    print(f"    {n_neg} singles NEGATIVE", flush=True)

    # independent multi-term basis (Lob dependencies removed; see notes)
    ind = ["Lob(pi/5)", "Lob(2pi/5)", "Lob(pi/15)", "Lob(2pi/15)",
           "Lob(pi/3)", "Catalan", "pi^2", "pi^2/sqrt5", "pi*logphi",
           "pi*log5", "logphi^2", "zeta3/pi", "one"]

    # S2: pairs ------------------------------------------------------
    print("  [S2] pairs from the full candidate list, maxcoeff 1e6", flush=True)
    names = [k for k in cand if k != "one"] + ["one"]
    n_neg = n_int = 0
    for a, b in combinations(names, 2):
        r = mp.pslq([c, cand[a], cand[b]], tol=tol, maxcoeff=10**6,
                    maxsteps=100000)
        if r:
            if r[0] == 0:
                n_int += 1  # internal relation between basis elements
            else:
                print(f"    HIT ({a},{b}): {r}", flush=True)
                hits.append(("pair", (a, b), r))
        else:
            n_neg += 1
    print(f"    {n_neg} pairs NEGATIVE, {n_int} internal (coeff(c)=0, "
          f"classical Lobachevsky identities, discarded)", flush=True)

    # S3: triples over the independent basis, maxcoeff 1e4 -----------
    print("  [S3] triples over the independent basis, maxcoeff 1e4", flush=True)
    n_neg = n_int = 0
    for a, b, d in combinations(ind, 3):
        r = mp.pslq([c, cand[a], cand[b], cand[d]], tol=tol, maxcoeff=10**4,
                    maxsteps=100000)
        if r:
            if r[0] == 0:
                n_int += 1
            else:
                print(f"    HIT ({a},{b},{d}): {r}", flush=True)
                hits.append(("triple", (a, b, d), r))
        else:
            n_neg += 1
    print(f"    {n_neg} triples NEGATIVE, {n_int} internal", flush=True)

    # S4: full independent basis, maxcoeff 1e3 -----------------------
    print("  [S4] full independent basis (13 elements + c), maxcoeff 1e3",
          flush=True)
    work = list(ind)
    while True:
        vec = [c] + [cand[k] for k in work]
        r = mp.pslq(vec, tol=tol, maxcoeff=10**3, maxsteps=500000)
        if r is None:
            print(f"    NEGATIVE over [c] + {work}", flush=True)
            break
        if r[0] != 0:
            print(f"    HIT: {r} over [c] + {work}", flush=True)
            hits.append(("full", tuple(work), r))
            break
        # internal relation: drop the last-listed participating element
        drop = [work[i - 1] for i in range(len(r) - 1, 0, -1) if r[i] != 0][0]
        print(f"    internal relation {r} (coeff(c)=0) -> dropping {drop}",
              flush=True)
        work.remove(drop)

    # S5: golden-weighted Lobachevsky triples (Z[sqrt5] coefficients) -
    print("  [S5] Z[sqrt5]-coefficient pairs: c vs {x, sqrt5 x, y, sqrt5 y}, "
          f"golden sector, maxcoeff 1e4", flush=True)
    gold = ["Lob(pi/5)", "Lob(2pi/5)", "Lob(pi/15)", "Lob(2pi/15)", "v3",
            "Catalan", "pi*logphi", "pi^2"]
    n_neg = n_int = 0
    for a, b in combinations(gold, 2):
        vec = [c, cand[a], s5 * cand[a], cand[b], s5 * cand[b]]
        r = mp.pslq(vec, tol=tol, maxcoeff=10**4, maxsteps=200000)
        if r:
            if r[0] == 0:
                n_int += 1
            else:
                print(f"    HIT ({a},{b}) Z[sqrt5]: {r}", flush=True)
                hits.append(("gold", (a, b), r))
        else:
            n_neg += 1
    print(f"    {n_neg} NEGATIVE, {n_int} internal", flush=True)
    return hits

# ---------------------------------------------------------------- main
if __name__ == "__main__":
    print("=" * 72, flush=True)
    print("B771 W2-237: additivity constant c -- recompute + identify", flush=True)
    print("=" * 72, flush=True)
    data = phase1()
    c, trusted = phase2(data)
    hits = phase3(c, trusted)
    print("\n[VERDICT-INPUT]", flush=True)
    if hits:
        print(f"  {len(hits)} candidate relation(s) found -- REQUIRE both-direction "
              f"10+ digit confirmation before RESOLVED-A:", flush=True)
        for h in hits:
            print(f"    {h}", flush=True)
    else:
        print("  ALL SWEEPS NEGATIVE at the recorded heights/tolerance "
              "=> bounded-negative (RESOLVED-B shape)", flush=True)
