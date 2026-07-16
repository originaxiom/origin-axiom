"""B640 — the hearing-group verification (prereg 3e000b72, sealed first).

Rebuilds the SU(3)_2 stage (B238's su3_data via B601's conventions) at
60-digit precision; the theta-odd 2-plane; rho = the untwisted weld
restricted to it. Gates R0-R6 per the prereg (R7 = the citation, in
FINDINGS).
"""
import itertools
import os
import sys

import importlib.util
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "hp_stage", os.path.join(HERE, "..", "B629_interaction_values",
                             "exact_hearing.py"))
hp = importlib.util.module_from_spec(spec)
_argv = sys.argv
sys.argv = [spec.origin]
_name = hp.__name__
spec.loader.exec_module(hp)          # 80-dps banked builder (its __main__
                                      # prints are harmless)
sys.argv = _argv
mp.mp.dps = 60

PHI = (1 + mp.sqrt(5)) / 2

# ---- the stage at level k = 2 (kappa = 5), TRUE high precision --------------
w, S, T, cc = hp.su3_data(2)
n = len(w)
Si = S ** -1
Ti = T ** -1

# letters (B601 conventions): W(RL) = T @ (S^-1 T^-1 S)  => R = T, L = S^-1 T^-1 S
R_full = T
L_full = Si * Ti * S

# the theta-odd pair plane: pairs (a,b)<->(b,a), 1/sqrt2 antisymmetric combos
pairs = []
seen = set()
for i, lam in enumerate(w):
    lam_c = (lam[1], lam[0])
    if lam == lam_c:
        continue
    j = w.index(lam_c)
    key = tuple(sorted((i, j)))
    if key not in seen:
        seen.add(key)
        pairs.append((i, j))
assert len(pairs) == 2, f"odd pairs at k=2: {len(pairs)}"
U = mp.zeros(n, len(pairs))
for col, (i, j) in enumerate(pairs):
    U[i, col] = 1 / mp.sqrt(2)
    U[j, col] = -1 / mp.sqrt(2)


def restrict(M):
    return (U.T * M * U)


def resid_invariance(M):
    # || M u - U (U^T M U) coords || for the plane
    full = M * U
    proj = U * restrict(M)
    return max(abs(full[i, j] - proj[i, j]) for i in range(n)
               for j in range(2))


print("== R1: the odd plane's invariance + M_odd = -rho ==", flush=True)
rR, rL = resid_invariance(R_full), resid_invariance(L_full)
print(f"  invariance residuals: R {mp.nstr(rR, 3)}, L {mp.nstr(rL, 3)}",
      flush=True)
rho_R, rho_L = restrict(R_full), restrict(L_full)
# the mirror: C = conjugation permutation; on the odd plane acts as -1:
Cm = mp.zeros(n, n)
for i, lam in enumerate(w):
    Cm[i, w.index((lam[1], lam[0]))] = 1
mo = restrict(Cm * R_full * Cm * R_full * 0 + Cm) if False else None
C_odd = restrict(Cm)
mres = max(abs(C_odd[i, j] + (1 if i == j else 0)) for i in range(2)
           for j in range(2))
print(f"  C|odd = -I residual: {mp.nstr(mres, 3)}", flush=True)

# ---- fingerprints + BFS closure ----------------------------------------------
def fp(M):
    out = []
    for i in range(2):
        for j in range(2):
            z = M[i, j]
            out.append((round(float(z.real), 25), round(float(z.imag), 25)))
    return tuple(out)


def mmul(A, B):
    return A * B


print("\n== R2: the group closure ==", flush=True)
gens = {"R": rho_R, "L": rho_L}
elems = {fp(mp.eye(2)): ("", mp.eye(2))}
frontier = [("", mp.eye(2))]
while frontier:
    new = []
    for (wd, M) in frontier:
        for gname, G in gens.items():
            M2 = M * G
            k = fp(M2)
            if k not in elems:
                elems[k] = (wd + gname, M2)
                new.append((wd + gname, M2))
    frontier = new
    if len(elems) > 2000:
        break
order = len(elems)
print(f"  |im rho| = {order}", flush=True)

# det character
om = mp.exp(2j * mp.pi / 3)
detfail = 0
for (wd, M) in list(elems.values())[:60]:
    d = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    nl = wd.count("L")
    nr = wd.count("R")
    if abs(d - om ** ((nl - nr) % 3)) > mp.mpf(10) ** -30:
        detfail += 1
print(f"  det = omega^(#L-#R mod 3): failures {detfail}/60", flush=True)

# ker(det)
ker = [(wd, M) for (wd, M) in elems.values()
       if abs((M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]) - 1) < mp.mpf(10) ** -30]
print(f"  |ker det| = {len(ker)}", flush=True)


def elem_order(M, cap=64):
    dim = M.rows
    P = mp.eye(dim)
    for k in range(1, cap + 1):
        P = P * M
        if max(abs(P[i, j] - (1 if i == j else 0)) for i in range(dim)
               for j in range(dim)) < mp.mpf(10) ** -30:
            return k
    return 0


prof = {}
invols = 0
for (wd, M) in ker:
    o = elem_order(M)
    prof[o] = prof.get(o, 0) + 1
    if o == 2:
        invols += 1
print(f"  ker(det) order profile: {dict(sorted(prof.items()))}", flush=True)
print(f"  unique involution: {invols == 1}", flush=True)

# character values on ker(det)
vals = {}
gold = {"0": 0, "+1": 1, "-1": -1, "+2": 2, "-2": -2,
        "+phi": float(PHI), "-phi": -float(PHI),
        "+1/phi": float(1 / PHI), "-1/phi": -float(1 / PHI)}
unident = 0
per_class = {}
for (wd, M) in ker:
    t = M[0, 0] + M[1, 1]
    if abs(t.imag) > 1e-25:
        unident += 1
        continue
    tr = float(t.real)
    hit = None
    for nm, v in gold.items():
        if abs(tr - v) < 1e-20:
            hit = nm
            break
    if hit is None:
        unident += 1
    else:
        per_class[hit] = per_class.get(hit, 0) + 1
print(f"  golden character histogram: {dict(sorted(per_class.items()))}; "
      f"unidentified {unident}", flush=True)

# conjugacy classes of ker(det): count via trace+order pairs (2x2 unitary:
# class determined by eigenvalues = (trace, det=1) up to conjugation)
classes = {}
for (wd, M) in ker:
    t = M[0, 0] + M[1, 1]
    key = (round(float(t.real), 18), round(float(t.imag), 18))
    classes[key] = classes.get(key, 0) + 1
print(f"  conjugacy classes (by trace, det=1): {len(classes)} classes, "
      f"sizes {sorted(classes.values())}", flush=True)

print("\n== R0: the order reconciliation table ==", flush=True)
RL = rho_R * rho_L
M_odd_RL = -RL                       # the mirror twist = -1 on the odd plane
print(f"  ord(rho(R))    = {elem_order(rho_R)}", flush=True)
print(f"  ord(rho(L))    = {elem_order(rho_L)}", flush=True)
print(f"  ord(rho(RL))   = {elem_order(RL)}", flush=True)
print(f"  ord(M_odd(RL)) = {elem_order(M_odd_RL)}", flush=True)
Tord = 0
P = mp.eye(n)
for k in range(1, 200):
    P = P * T
    if max(abs(P[i, j] - (1 if i == j else 0)) for i in range(n)
           for j in range(n)) < mp.mpf(10) ** -30:
        Tord = k
        break
print(f"  ord(T) full    = {Tord}", flush=True)
BRL = -(RL)                          # B601's B_odd = -(U^T WRL U) = M_odd
print(f"  ord(B601 B_odd(RL)) = {elem_order(BRL)}   "
      f"[B584 banked the rotation order 10 for e^(3 pi i/5)-type;"
      f" B619's 20 = the FULL-space operator — recomputed here:", flush=True)
Wfull = R_full * L_full
print(f"  ord(W(RL)) on the FULL 6-dim stage = {elem_order(Wfull, 200)}",
      flush=True)

print("\n== R6: the headline ==", flush=True)
trRL = RL[0, 0] + RL[1, 1]
print(f"  tr rho(RL) = {mp.nstr(trRL, 30)}", flush=True)
print(f"  +1/phi     = {mp.nstr(1/PHI, 30)}", flush=True)
print(f"  tr = -1/phi: {abs(trRL + 1/PHI) < mp.mpf(10)**-45}", flush=True)

print("\n== R4: the tone table ==", flush=True)
tones = {}
silent = 0
tonefail = 0
for (wd, M) in elems.values():
    Modd = -M
    # the symmetric part of Re(M_odd) must be cos(theta) I
    s00 = mp.re(Modd[0, 0])
    s11 = mp.re(Modd[1, 1])
    s01 = (mp.re(Modd[0, 1]) + mp.re(Modd[1, 0])) / 2
    if abs(s00 - s11) > mp.mpf(10) ** -30 or abs(s01) > mp.mpf(10) ** -30:
        tonefail += 1
        continue
    tone = round(float(s00), 20)
    tones[tone] = tones.get(tone, 0) + 1
    if abs(tone) < 1e-20:
        silent += 1
print(f"  scalar-symmetric-part law failures: {tonefail}/{order}",
      flush=True)
print(f"  distinct tones: {len(tones)}", flush=True)
print(f"  silent elements: {silent}/{order}", flush=True)
ids = {"0": 0, "1/2phi": float(1/(2*PHI)), "1/2": 0.5,
       "phi/2": float(PHI/2), "1": 1.0, "1/4phi": float(1/(4*PHI)),
       "1/4": 0.25, "phi/4": float(PHI/4)}
named = 0
for t in tones:
    a = abs(t)
    if any(abs(a - v) < 1e-18 for v in ids.values()):
        named += 1
print(f"  tones identified in the golden set (up to sign): {named}/"
      f"{len(tones)}", flush=True)

print("\n== R5: the silent witnesses ==", flush=True)
for word in ("LLRLRR", "LLRRLR", "LRLLRR"):
    M = mp.eye(2)
    for ch in word:
        M = M * (rho_L if ch == "L" else rho_R)
    Modd = -M
    s00 = mp.re(Modd[0, 0])
    s11 = mp.re(Modd[1, 1])
    s01 = (mp.re(Modd[0, 1]) + mp.re(Modd[1, 0])) / 2
    tone_zero = max(abs(s00), abs(s11), abs(s01)) < mp.mpf(10) ** -30
    # real ear u: amplitude u^T Modd u real part = tone * |u|^2 = 0
    u_ear = mp.matrix([mp.mpf(3)/5, mp.mpf(4)/5])
    amp = (u_ear.T * Modd * u_ear)[0, 0]
    print(f"  {word}: tone-zero {tone_zero}; real-ear amplitude Re = "
          f"{mp.nstr(mp.re(amp), 3)} (must be ~0), Im = "
          f"{mp.nstr(mp.im(amp), 6)}", flush=True)

print("\nB640 verification DONE", flush=True)
