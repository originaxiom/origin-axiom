#!/usr/bin/env python3
"""W-B1 (M29): frame D's two constructions by their conjugations, S's level-5 class, and B1936's premise in each.
Data-free; this seat's own code (B1656's theta-with-characteristic formula re-implemented, B1691's triplet R built from
this seat's own theta series). No frame output is computed: no coupling, ratio or mixing; no named tau.

    python3 -I -u wb1_checks.py

DEFINITIONS
  th[a, b](u, T) = sum_n exp(i pi T (n + a)^2 + 2 pi i (n + a)(u + b)) (B1656's thc). N: th[a, b] -> th[-a, -b] (charge
  conjugation as a negated twist, D1). K: f -> conj(f) (charge conjugation as complex conjugation, D2).
  theta2, theta3, theta4 with nome e^{i pi tau}; R = (-theta2^2, -theta4^2, i theta3^2) / (theta2 theta3 theta4) (B1691,
  up to the constant pi); DR = R' / (2 pi i) - (k / 12) E2 R with k = -1/2 (the Serre derivative that builds S).
  Classes: c = 2 (6Y) mod 5; matter Q 1, u^c -4, d^c 2, L -3, e^c 6; a sector's Higgs charge cancels its matter's.

EXPECTATIONS, written before the run (by hand):
  E1  N: th[-a, -b](u, T) = th[a, b](-u, T) (holomorphic), and K: conj th[a, b](u, T) = th[a, -b](-conj u, -conj T)
      (the mirror), at 40 random points, relative residual below 1e-10.
  E2  R(tau + 1) = T_R R(tau) with T_R = [[w, 0, 0], [0, 0, w], [0, w^-3, 0]], w = e^{i pi / 4}; its eigenvalues are
      w, w^-1, w^3, all eighth roots of unity, none a fifth root; DR(tau + 1) = T_R DR(tau) as well (residual below
      1e-6, numerical derivative). So S, built from DR, has no level-5 class of its own.
  E3  D1: matter classes 2, 2, 4, 4, 2; the sectors' Higgs classes up 1, down 4, leptons 4. Every object is holomorphic
      (N keeps holomorphy, E1), so the holomorphic objects meet the odd class 1 and the even classes 2, 4: B1936's
      premise is false in D1.
  E4  D2: matter's frame fields are classes {2, 4} (even), their conjugates {3, 1} (odd). If the holomorphic Higgs has
      class 4, the premise holds and charge gives (up S~, down S, leptons S); if class 1, it fails and charge gives
      (S, S~, S~). So in D2 the premise is the global bit restated.
  E5  D1 against D2, object by object: N th and K th coincide at mirror-fixed points (Re T = 0, b = 0, u real; residual
      below 1e-10) and differ at generic points (relative difference above 1e-3 at every one of 20).
  Plant: K with +b in place of -b fails E1's identity at every point.
"""
import cmath
import math
import random

import mpmath as mp

mp.mp.dps = 30
rng = random.Random(29)
NK = 40


def say(*a):
    print(*a, flush=True)


def th(a, b, u, T):
    return mp.fsum(mp.exp(1j * mp.pi * T * (n + a) ** 2 + 2j * mp.pi * (n + a) * (u + b)) for n in range(-NK, NK + 1))


def rel(x, y):
    return abs(x - y) / max(abs(x), abs(y), mp.mpf(10) ** -25)


def rpoint():
    a, b = mp.mpf(rng.uniform(-1, 1)), mp.mpf(rng.uniform(-1, 1))
    u = mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(-0.3, 0.3))
    T = mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(1.0, 3.0))
    return a, b, u, T


# E1 and the plant
e1, plant_hits, N1 = 0.0, 0, 40
for _ in range(N1):
    a, b, u, T = rpoint()
    e1 = max(e1, rel(th(-a, -b, u, T), th(a, b, -u, T)), rel(mp.conj(th(a, b, u, T)), th(a, -b, -mp.conj(u), -mp.conj(T))))
    plant_hits += rel(mp.conj(th(a, b, u, T)), th(a, b, -mp.conj(u), -mp.conj(T))) > 1e-6
say("E1 max relative residual:", mp.nstr(e1, 3), "| holds:", e1 < 1e-10, "| plant (+b) fails at", plant_hits, "of", N1,
    "| plant caught:", plant_hits == N1)


# E2
def thetas(tau):
    q = mp.exp(1j * mp.pi * tau)
    t3 = mp.fsum(q ** (n * n) for n in range(-NK, NK + 1))
    t4 = mp.fsum((-1) ** abs(n) * q ** (n * n) for n in range(-NK, NK + 1))
    t2 = mp.fsum(mp.exp(1j * mp.pi * tau * (n + mp.mpf(1) / 2) ** 2) for n in range(-NK, NK + 1))
    return t2, t3, t4


def Rv(tau):
    t2, t3, t4 = thetas(tau)
    D = t2 * t3 * t4
    return [-t2 * t2 / D, -t4 * t4 / D, 1j * t3 * t3 / D]


def E2f(tau):
    q = mp.exp(2j * mp.pi * tau)
    return 1 - 24 * mp.fsum(mp.fsum(d for d in range(1, n + 1) if n % d == 0) * q ** n for n in range(1, 120))


def DRv(tau, h=mp.mpf(10) ** -8):
    rp, rm = Rv(tau + h), Rv(tau - h)
    der = [(x - y) / (2 * h) / (2j * mp.pi) for x, y in zip(rp, rm)]
    e2 = E2f(tau)
    return [d - (mp.mpf(-1) / 2) / 12 * e2 * r for d, r in zip(der, Rv(tau))]


w = mp.exp(1j * mp.pi / 4)
TR = mp.matrix([[w, 0, 0], [0, 0, w], [0, w ** -3, 0]])
taus = [mp.mpc(rng.uniform(-0.4, 0.4), rng.uniform(0.9, 1.6)) for _ in range(3)]
X = mp.matrix([Rv(t) for t in taus]).T
Y = mp.matrix([Rv(t + 1) for t in taus]).T
Tfit = Y * mp.inverse(X)
dT = max(abs(Tfit[i, j] - TR[i, j]) for i in range(3) for j in range(3))
ev = mp.eig(TR)[0]
eighth = all(abs(e ** 8 - 1) < 1e-20 for e in ev)
fifth = any(abs(e ** 5 - 1) < 1e-6 for e in ev)
dDR = 0.0
for t in taus:
    lhs = DRv(t + 1)
    rhs = TR * mp.matrix(DRv(t))
    dDR = max(dDR, max(abs(lhs[i] - rhs[i]) / max(abs(rhs[i]), mp.mpf(10) ** -20) for i in range(3)))
e2ok = dT < 1e-15 and eighth and not fifth and dDR < 1e-6
say("E2 fitted T_R against the hand matrix:", mp.nstr(dT, 3), "| eigenvalues:", [mp.nstr(e, 6) for e in ev],
    "| all eighth roots:", eighth, "| any fifth root:", fifth, "| DR(tau+1) = T_R DR(tau), max rel residual:",
    mp.nstr(dDR, 3), "| holds:", e2ok)

# E3 and E4
Y6 = {"Q": 1, "u^c": -4, "d^c": 2, "L": -3, "e^c": 6}
SECT = {"up": ("Q", "u^c"), "down": ("Q", "d^c"), "lep": ("L", "e^c")}
cls = {f: (2 * q) % 5 for f, q in Y6.items()}
hig = {s: (2 * (-(Y6[a] + Y6[b]))) % 5 for s, (a, b) in SECT.items()}
holo_D1 = sorted(set(cls.values()) | set(hig.values()))
parities = {c % 2 for c in holo_D1}
e3 = [cls[f] for f in Y6] == [2, 2, 4, 4, 2] and hig == {"up": 1, "down": 4, "lep": 4} and parities == {0, 1}
say("E3 matter classes", [cls[f] for f in Y6], "| Higgs classes", hig, "| D1's holomorphic classes", holo_D1,
    "| both parities among them:", parities == {0, 1}, "| holds:", e3)


def world(h_holo):
    return {s: ("S" if hig[s] == h_holo else "S~") for s in SECT}


matter_even = all(c % 2 == 0 for c in cls.values()) and all(((5 - c) % 5) % 2 == 1 for c in cls.values())
e4 = matter_even and world(4) == {"up": "S~", "down": "S", "lep": "S"} and world(1) == {"up": "S", "down": "S~", "lep": "S~"}
say("E4 matter even, conjugates odd:", matter_even, "| holomorphic Higgs class 4 ->", world(4), "| class 1 ->", world(1),
    "| holds:", e4)

# E5
fix_res, gen_diffs = 0.0, []
for _ in range(20):
    a = mp.mpf(rng.uniform(-1, 1))
    u = mp.mpf(rng.uniform(-0.5, 0.5))
    T = mp.mpc(0, rng.uniform(1.0, 3.0))
    Nv, Kv = th(-a, 0, u, T), mp.conj(th(a, 0, u, T))
    fix_res = max(fix_res, rel(Nv, Kv))
    a, b, uu, TT = rpoint()
    gen_diffs.append(rel(th(-a, -b, uu, TT), mp.conj(th(a, b, uu, TT))))
e5 = fix_res < 1e-10 and min(gen_diffs) > 1e-3
say("E5 N against K at mirror-fixed points, max residual:", mp.nstr(fix_res, 3), "| at generic points, min relative",
    "difference:", mp.nstr(min(gen_diffs), 3), "| holds:", e5)
say("all hold:", e1 < 1e-10 and plant_hits == N1 and e2ok and e3 and e4 and e5)
