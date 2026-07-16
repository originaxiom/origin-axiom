"""B642 — the Galois-conjugate ear (prereg 84680043; P1-P3 sealed first).
The k = 7 Galois twist of the SU(3)_2 stage (fixes omega, flips sqrt5)."""
import itertools
import os

import mpmath as mp

mp.mp.dps = 60
PHI = (1 + mp.sqrt(5)) / 2
GK = 7                                   # the Galois multiplier


def su3_data_galois(k):
    kap = k + 3
    weights = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    n = len(weights)
    def Lvec(w):
        return [mp.mpf(w[0] + w[1] + 2), mp.mpf(w[1] + 1), mp.mpf(0)]
    def ip(u, v):
        s = sum(u[i] * v[i] for i in range(3))
        return s - sum(u) * sum(v) / 3
    perms = list(itertools.permutations(range(3)))
    def sgn(p):
        inv = sum(1 for i in range(3) for j in range(i + 1, 3)
                  if p[i] > p[j])
        return (-1) ** inv
    S = mp.matrix(n, n)
    for i, wl in enumerate(weights):
        Ll = Lvec(wl)
        for j, wm in enumerate(weights):
            Lm = Lvec(wm)
            tot = mp.mpc(0)
            for p in perms:
                Lp = [Ll[p[0]], Ll[p[1]], Ll[p[2]]]
                tot += sgn(p) * mp.e ** (-2j * mp.pi * GK * ip(Lp, Lm) / kap)
            S[i, j] = tot
    norm = mp.sqrt(sum(abs(S[i, 0]) ** 2 for i in range(n)))
    for i in range(n):
        for j in range(n):
            S[i, j] = S[i, j] / norm
    c = mp.mpf(k * 8) / (k + 3)
    T = mp.matrix(n, n)
    for i, (a, b) in enumerate(weights):
        expo = ((mp.mpf(2) / 3) * (a * a + a * b + b * b)
                + 2 * (a + b)) / (2 * kap) - c / 24
        T[i, i] = mp.e ** (2j * mp.pi * GK * expo)
    return weights, S, T, c


w, S, T, cc = su3_data_galois(2)
n = len(w)
Si = S ** -1
Ti = T ** -1
R_full, L_full = T, Si * Ti * S
pairs = []
seen = set()
for i, lam in enumerate(w):
    lc = (lam[1], lam[0])
    if lam == lc:
        continue
    j = w.index(lc)
    key = tuple(sorted((i, j)))
    if key not in seen:
        seen.add(key)
        pairs.append((i, j))
U = mp.zeros(n, 2)
for col, (i, j) in enumerate(pairs):
    U[i, col] = 1 / mp.sqrt(2)
    U[j, col] = -1 / mp.sqrt(2)
# invariance gate
res = max(abs((R_full * U - U * (U.T * R_full * U))[i, j])
          for i in range(n) for j in range(2))
print(f"odd-plane invariance residual (R): {mp.nstr(res, 3)}", flush=True)
rho_R = U.T * R_full * U
rho_L = U.T * L_full * U


def fp(M):
    return tuple((round(float(M[i, j].real), 25),
                  round(float(M[i, j].imag), 25))
                 for i in range(2) for j in range(2))


elems = {fp(mp.eye(2)): ("", mp.eye(2))}
frontier = [("", mp.eye(2))]
while frontier:
    new = []
    for (wd, M) in frontier:
        for g, G in (("R", rho_R), ("L", rho_L)):
            M2 = M * G
            k2 = fp(M2)
            if k2 not in elems:
                elems[k2] = (wd + g, M2)
                new.append((wd + g, M2))
    frontier = new
    if len(elems) > 2000:
        break
print(f"P1: |im rho| = {len(elems)} (sealed: 360)", flush=True)
TOL = mp.mpf(10) ** -45
ker = [(wd, M) for (wd, M) in elems.values()
       if abs((M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]) - 1) < TOL]
classes = {}
for (wd, M) in ker:
    t = M[0, 0] + M[1, 1]
    key = (round(float(t.real), 18), round(float(t.imag), 18))
    classes[key] = classes.get(key, 0) + 1
print(f"P1: |ker det| = {len(ker)}; class sizes "
      f"{sorted(classes.values())} (sealed: SL(2,5)'s "
      f"[1,1,12,12,12,12,20,20,30])", flush=True)

RL = rho_R * rho_L
trRL = RL[0, 0] + RL[1, 1]
print(f"P3: tr rho(RL) = {mp.nstr(trRL, 30)}", flush=True)
print(f"P3: = +phi: {abs(trRL - PHI) < TOL}   "
      f"(phi = {mp.nstr(PHI, 25)})", flush=True)

# P2: the twist-frame tone census
tones = {}
for (wd, M) in elems.values():
    Modd = -M
    d = Modd[0, 0] * Modd[1, 1] - Modd[0, 1] * Modd[1, 0]
    zeta = mp.sqrt(d)
    u = mp.matrix([mp.mpf(3) / 5, mp.mpf(4) / 5])
    A = (u.T * (Modd * u))[0, 0]
    t = round(abs(float(mp.re(A / zeta))), 18)
    tones[t] = tones.get(t, 0) + 1
ids = {"0": 0.0, "1/(2phi)": float(1 / (2 * PHI)), "1/2": 0.5,
       "phi/2": float(PHI / 2), "1": 1.0}
census = {}
for t, c2 in tones.items():
    hit = None
    for nm, v in ids.items():
        if abs(t - v) < 1e-15:
            hit = nm
            break
    census[hit or f"UNID {t}"] = census.get(hit, 0) + c2
print(f"P2: |tone| census = {census}", flush=True)
print(f"P2 sealed prediction: phi/2 and 1/(2phi) multiplicities SWAP "
      f"vs the base stage's {{1:6, phi/2:72, 1/2:120, 1/(2phi):72, 0:90}}",
      flush=True)
print("B642 DONE", flush=True)
