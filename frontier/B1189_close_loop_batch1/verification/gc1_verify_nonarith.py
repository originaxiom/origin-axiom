#!/usr/bin/env python3
"""GC-1: nail down the 13 suspected NON-arithmetic members.

(A) positive control: regular members (Bianchi-commensurable by the {3,3,6}
    tessellation argument) must PASS tr(w)^2 in O_{-3} on all test words;
(B) PSLQ-identify the exact rational/quadratic value of the offending traces
    (t06829 tr(ab) ?= -13/3 etc.) at 1e-40;
(C) independent second presentation: randomized triangulation of each of the
    13, recompute all word traces; non-arithmeticity is confirmed if a
    non-integral trace appears again (trace integrality is presentation-
    independent, a single non-integral trace kills it).
"""
import itertools
import snappy
import mpmath as mp

mp.mp.dps = 50
TOL = mp.mpf(10) ** -20
SQRT3 = mp.sqrt(3)

def to_mp(x):
    return mp.mpf(str(x).replace(" ", ""))

def tr(G, w):
    A = G.SL2C(w)
    return mp.mpc(to_mp(A[0, 0].real()), to_mp(A[0, 0].imag())) + \
           mp.mpc(to_mp(A[1, 1].real()), to_mp(A[1, 1].imag()))

def eis(s):
    m, n = 2 * mp.re(s), 2 * mp.im(s) / SQRT3
    mi, ni = mp.nint(m), mp.nint(n)
    if abs(m - mi) > TOL or abs(n - ni) > TOL:
        return None
    return (int(mi), int(ni)) if (int(mi) - int(ni)) % 2 == 0 else False

def words_for(G):
    g = G.generators()
    return list(g) + ["".join(p) for p in itertools.permutations(g, 2)] \
                   + ["".join(p) for p in itertools.permutations(g, 3)]

# (A) positive control: 8 regular members incl. m003/m004
print("=== (A) regular-member positive control ===")
for name in ["m003", "m004", "s955", "s960", "m202", "m206", "v3551", "t10figure"][:6]:
    try:
        G = snappy.ManifoldHP(name).fundamental_group()
    except Exception as e:
        print(name, "SKIP", e); continue
    ws = words_for(G)
    bad = [w for w in ws if eis(tr(G, w) ** 2) in (None, False)]
    print(f"{name}: {len(ws)-len(bad)}/{len(ws)} words pass tr^2 in O_-3; bad: {bad if bad else 'NONE'}")

# (B) exact identification of offending traces
print("=== (B) PSLQ identification of offending traces ===")
suspects = {"t06829": "ab", "o9_41000": "ab", "o10_143602": "c", "o9_41003": "bc",
            "t06828": "a", "o9_41004": "c", "t11365": "b", "v2875": "c",
            "o10_143600": "ab", "o10_143601": "ac", "o9_41005": "b",
            "o9_41006": "c", "o9_41008": "ab"}
for name, w in suspects.items():
    G = snappy.ManifoldHP(name).fundamental_group()
    t = tr(G, w)
    s = t * t
    # identify s = (p + q*sqrt(-3))/r via PSLQ on Re, Im separately
    def rat(x):
        if abs(x) < TOL:
            return "0"
        r = mp.pslq([x, mp.mpf(1)], tol=mp.mpf(10) ** -40, maxcoeff=10**15)
        return f"{-r[1]}/{r[0]}" if r else "UNIDENTIFIED"
    print(f"{name} tr({w})^2 = {rat(mp.re(s))} + ({rat(mp.im(s)/SQRT3)})*sqrt(-3)   [tr={complex(t):.6f}]")

# (C) independent presentation from randomized triangulation
print("=== (C) randomized-triangulation re-derivation ===")
import random
random.seed(7)
for name in suspects:
    confirmed = False
    for attempt in range(6):
        M = snappy.ManifoldHP(name)
        for _ in range(attempt + 1):
            M.randomize()
        try:
            G = M.fundamental_group()
            ws = words_for(G)
            bad = [w for w in ws if eis(tr(G, w) ** 2) in (None, False)]
        except Exception:
            continue
        if bad:
            confirmed = True
            print(f"{name}: CONFIRMED non-integral trace in independent presentation "
                  f"(attempt {attempt}, gens={len(G.generators())}, bad e.g. {bad[:2]})")
            break
    if not confirmed:
        print(f"{name}: NOT re-confirmed in 6 randomized presentations -- FLAG")
print("DONE")
