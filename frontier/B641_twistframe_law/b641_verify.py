"""B641 — the twist-frame tone law verification (prereg b139e03a)."""
import importlib.util
import os
import sys

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "hp_stage", os.path.join(HERE, "..", "B629_interaction_values",
                             "exact_hearing.py"))
hp = importlib.util.module_from_spec(spec)
_argv = sys.argv
sys.argv = [spec.origin]
spec.loader.exec_module(hp)
sys.argv = _argv
mp.mp.dps = 60
PHI = (1 + mp.sqrt(5)) / 2

w, S, T, cc = hp.su3_data(2)
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
        for gname, G in (("R", rho_R), ("L", rho_L)):
            M2 = M * G
            k = fp(M2)
            if k not in elems:
                elems[k] = (wd + gname, M2)
                new.append((wd + gname, M2))
    frontier = new
assert len(elems) == 360

TOL = mp.mpf(10) ** -45

print("== G1: Cayley-Klein membership (det = 1 sector) ==", flush=True)
ck_ok, ck_n = 0, 0
for (wd, M) in elems.values():
    d = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    if abs(d - 1) < TOL:
        ck_n += 1
        if (abs(M[1, 1] - mp.conj(M[0, 0])) < TOL and
                abs(M[1, 0] + mp.conj(M[0, 1])) < TOL):
            ck_ok += 1
print(f"  Cayley-Klein form: {ck_ok}/{ck_n}", flush=True)

print("\n== G2: the twist-frame law (360 x 6 ears, 50+ digits) ==",
      flush=True)
ears = [mp.matrix([mp.mpf(3) / 5, mp.mpf(4) / 5]),
        mp.matrix([mp.mpf(5) / 13, mp.mpf(12) / 13]),
        mp.matrix([mp.mpf(8) / 17, mp.mpf(15) / 17]),
        mp.matrix([mp.mpf(1), mp.mpf(0)]),
        mp.matrix([mp.mpf(7) / 25, mp.mpf(24) / 25]),
        mp.matrix([mp.mpf(20) / 29, mp.mpf(21) / 29])]
maxdev = mp.mpf(0)
tones = {}
silent = 0
for (wd, M) in elems.values():
    Modd = -M
    d = Modd[0, 0] * Modd[1, 1] - Modd[0, 1] * Modd[1, 0]
    zeta = mp.sqrt(d)
    vals = []
    for u in ears:
        A = (u.T * (Modd * u))[0, 0]
        vals.append(mp.re(A / zeta))
    dev = max(abs(v - vals[0]) for v in vals)
    maxdev = max(maxdev, dev)
    t = round(float(vals[0]), 20)
    key = round(abs(t), 18)
    tones[key] = tones.get(key, 0) + 1
    if abs(t) < 1e-18:
        silent += 1
print(f"  max ear-deviation over 360 x 6: {mp.nstr(maxdev, 3)}", flush=True)
print(f"  law holds at 45+ digits: {maxdev < TOL}", flush=True)

print("\n== G3: the corrected table ==", flush=True)
ids = {"0": 0.0, "1/(2phi)": float(1 / (2 * PHI)), "1/2": 0.5,
       "phi/2": float(PHI / 2), "1": 1.0}
census = {}
for t, c in tones.items():
    hit = None
    for nm, v in ids.items():
        if abs(t - v) < 1e-15:
            hit = nm
            break
    census[hit or f"UNIDENTIFIED {t}"] = census.get(hit, 0) + c
print(f"  |tone| census: {census}", flush=True)
print(f"  silent: {silent}/360", flush=True)
print(f"  five absolute tones, all identified: "
      f"{all(not k.startswith('UNID') for k in census)}", flush=True)

print("\n== G4: the accidentals ==", flush=True)
acc = []
for (wd, M) in elems.values():
    d = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    if abs(d - 1) < TOL:
        continue
    Modd = -M
    s01 = (mp.re(Modd[0, 1]) + mp.re(Modd[1, 0])) / 2
    if (abs(mp.re(Modd[0, 0]) - mp.re(Modd[1, 1])) < TOL and
            abs(s01) < TOL):
        # strict law holds in a twisted sector
        scalar = (abs(M[0, 1]) < TOL and abs(M[1, 0]) < TOL and
                  abs(M[0, 0] - M[1, 1]) < TOL)
        o = 0
        P = mp.eye(2)
        for k in range(1, 64):
            P = P * M
            if max(abs(P[i, j] - (1 if i == j else 0)) for i in range(2)
                   for j in range(2)) < mp.mpf(10) ** -30:
                o = k
                break
        tr = M[0, 0] + M[1, 1]
        acc.append((wd, scalar, o, complex(tr)))
print(f"  twisted strict-law exceptions: {len(acc)} (expect 8)", flush=True)
for (wd, sc, o, tr) in acc:
    print(f"    word {wd[:14]:>14} scalar={sc} order={o} "
          f"tr≈{tr:.4f}", flush=True)

print("\n== G5: Plancherel (exact table arithmetic) ==", flush=True)
import sympy as sp
phi_s = (1 + sp.sqrt(5)) / 2
# ker(det) class equation with the golden character values:
cls = [(1, 2), (1, -2), (20, 1), (20, -1), (30, 0),
       (12, phi_s), (12, -phi_s), (12, 1 / phi_s), (12, -1 / phi_s)]
tot = sum(sz * ch ** 2 for sz, ch in cls)
print(f"  <|chi|^2> over ker(det) = {sp.simplify(tot / 120)} (Schur: 1)",
      flush=True)
# mean-square universal tone over ker(det): tone = tr/2 for det=1
ms_tone = sp.simplify(sum(sz * (ch / 2) ** 2 for sz, ch in cls) / 120)
print(f"  mean-square universal tone (det=1) = {ms_tone}", flush=True)
# the quadrature split: <|A|^2> = <tone^2> + <overtone^2> for unit ears;
# by Schur, <|u M u|^2>... report the exact complement:
print(f"  mean-square overtone (Schur complement) = "
      f"{sp.simplify(sp.Rational(1, 2) - ms_tone)}  "
      f"[against <|A|^2> = 1/2 for the 2-dim irrep, unit real ears]",
      flush=True)
print("\nB641 DONE", flush=True)
