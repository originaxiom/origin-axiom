"""Adversarial verifier, item 3, own code from scratch (nothing imported from stage1/ or from the repository).

Part A: algebra from the record's triplet T alone (B1866 join_scrutiny.py lines 317-319), dense complex matrices.
Part B: series for the theta_3 slot of U_9 = eta^9 V/E4 and U_21 = eta^21 V/(E4 E6), eta by the pentagonal-number
series, theta_3 as a two-sided sum, E4/E6 by divisor sums (a different implementation from the first verifier's).
Plants: Q1 (twist chi_m with R -> zeta^+m), Q2 (eta^13/E6 used in place of U_9's normaliser).
"""
import sys
import numpy as np
import mpmath as mp

PLANT = sys.argv[1] if len(sys.argv) > 1 else None
FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""))
    if not ok:
        FAILS.append(name)


z = np.exp(2j * np.pi / 24)


def mono(perm, exps):
    M = np.zeros((3, 3), dtype=complex)
    for j in range(3):
        M[perm[j], j] = z ** exps[j]
    return M


# the record's triplet, transcribed (M e_j = zeta^exps[j] e_perm[j])
TL = mono((0, 2, 1), (-3, 3, 3))
TR = mono((1, 0, 2), (-3, -3, 3))
I3 = np.eye(3)
inv = np.linalg.inv
close = lambda A, B: np.abs(A - B).max() < 1e-9

check("record's T satisfies the braid relation L R^-1 L = R^-1 L R^-1", close(TL @ inv(TR) @ TL, inv(TR) @ TL @ inv(TR)))
ST = TL @ inv(TR) @ TL
check("record's T: S^2 = +i I, S^4 = -I", close(ST @ ST, 1j * I3) and close(np.linalg.matrix_power(ST, 4), -I3))


def to_exp(x):
    """a unit complex number as k in Z/24 (x = zeta^k), or None"""
    if abs(abs(x) - 1) > 1e-9:
        return None
    k = int(round(24 * np.angle(x) / (2 * np.pi))) % 24
    return k if abs(x - z ** k) < 1e-9 else None


def census(AL0, AR0, label):
    rows = {}
    for m in range(24):
        sR = m if PLANT == "Q1" else -m          # Q1: the wrong twist convention R -> zeta^+m
        AL, AR = z ** m * AL0, z ** sR * AR0
        braid = close(AL @ inv(AR) @ AL, inv(AR) @ AL @ inv(AR))
        S = AL @ inv(AR) @ AL
        psl = braid and close(S @ S, I3) and close(np.linalg.matrix_power(S @ AL, 3), I3)
        L2 = AL @ AL
        slots = {}
        for j in range(3):
            e = np.zeros(3); e[j] = 1
            vL, vS = L2 @ e, S @ e
            if close(vL, vL[j] * e) and close(vS, vS[j] * e):
                slots[j + 1] = (to_exp(vL[j]), to_exp(vS[j]))
        rows[m] = (psl, slots)
    pslset = [m for m in range(24) if rows[m][0]]
    signs = {m: rows[m][1] for m in pslset if any(a in (0, 12) and b in (0, 12) for a, b in rows[m][1].values())}
    print("  %s: PSL twists m = %s; slots fixed by <L^2, S> with (L^2, S) eigen-exponents (zeta_24): %s" % (
        label, pslset, {m: rows[m][1] for m in pslset}))
    print("  %s: sign characters at m = %s" % (label, signs))
    return pslset, signs


p_T, s_T = census(TL, TR, "chi_m (x) T")
p_V, s_V = census(TL.conj(), TR.conj(), "chi_m (x) conj T (= V's rep)")
tag = " [PLANT Q1]" if PLANT == "Q1" else ""
check("X1 PSL twists of T are m = 3,7,11,15,19,23; of conj T m = 1,5,9,13,17,21" + tag,
      p_T == [3, 7, 11, 15, 19, 23] and p_V == [1, 5, 9, 13, 17, 21], "T: %s; conj T: %s" % (p_T, p_V))
check("X2 sign characters, all on slot 2 (theta_3): T: m=15 (-1,+1), m=3 (-1,-1); conj T: m=9 (-1,+1), m=21 (-1,-1)" + tag,
      s_T == {3: {2: (12, 12)}, 15: {2: (12, 0)}} and s_V == {9: {2: (12, 0)}, 21: {2: (12, 12)}}, "T: %s; conj T: %s" % (s_T, s_V))
# X3: the relay's displayed one-form pair A = (e(1/8) T_L, e(-1/8) T_R) = chi_3 (x) T (B1866 F1)
AL, AR = z ** 3 * TL, z ** -3 * TR
SA = AL @ inv(AR) @ AL
X3a = close((AL @ AL)[:, 1], -np.eye(3)[:, 1]) and close(SA[:, 1], -np.eye(3)[:, 1])
X3b = close((-AL @ -AL)[:, 1], -np.eye(3)[:, 1]) and close(((-AL) @ inv(-AR) @ (-AL))[:, 1], np.eye(3)[:, 1])
X3c = close(AL.conj(), z ** 21 * TL.conj()) and close(AR.conj(), z ** -21 * TR.conj())
check("X3 B1866 F1's displayed pair: (-1,-1); negated pair (-1,+1); conj(displayed) = chi_21 (x) conj T (U_21's rep)", X3a and X3b and X3c)

# ------------------------------------------------------------------ Part B: series, own implementation
mp.mp.dps = 30


def eta(t):
    q = mp.exp(2j * mp.pi * t)
    s = mp.mpf(0)
    for n in range(-60, 61):
        s += (-1) ** n * q ** (n * (3 * n - 1) // 2)
    return mp.exp(2j * mp.pi * t / 24) * s


def theta3(t):
    return mp.fsum(mp.exp(1j * mp.pi * n * n * t) for n in range(-60, 61))


SIG = {}


def sigma(k, n):
    if (k, n) not in SIG:
        SIG[(k, n)] = sum(d ** k for d in range(1, n + 1) if n % d == 0)
    return SIG[(k, n)]


def Ek(k, t, N=250):
    q = mp.exp(2j * mp.pi * t)
    c = {4: 240, 6: -504}[k]
    return 1 + c * mp.fsum(sigma(k - 1, n) * q ** n for n in range(1, N))


def u_slot(name, t):
    """the theta_3 component of the weight-0 vector: g(t) theta_3^2/eta^3"""
    e = eta(t)
    base = theta3(t) ** 2 / e ** 3
    if name == "U9":
        if PLANT == "Q2":
            return e ** 13 / Ek(6, t) * base         # Q2: the wrong normaliser (m = 13), labelled U_9
        return e ** 9 / Ek(4, t) * base
    if name == "U21":
        return e ** 21 / (Ek(4, t) * Ek(6, t)) * base


pts = [mp.mpc(0.11, 0.95), mp.mpc(-0.27, 1.05), mp.mpc(0.31, 0.83)]
res = {}
for name in ("U9", "U21"):
    rL2 = [u_slot(name, t + 2) / u_slot(name, t) for t in pts]
    rS = [u_slot(name, -1 / t) / u_slot(name, t) for t in pts]
    res[name] = (rL2, rS)
    print("  %s theta_3 slot: L^2 ratios %s; S ratios %s" % (name, [mp.nstr(x, 12) for x in rL2], [mp.nstr(x, 12) for x in rS]))
tol = mp.mpf(10) ** -20
ok9 = all(abs(x + 1) < tol for x in res["U9"][0]) and all(abs(x - 1) < tol for x in res["U9"][1])
ok21 = all(abs(x + 1) < tol for x in res["U21"][0]) and all(abs(x + 1) < tol for x in res["U21"][1])
check("X4 U_9 = eta^9 V/E4 on the theta_3 slot: L^2 -> -1, S -> +1 (three points, < 1e-20)" + (" [PLANT Q2]" if PLANT == "Q2" else ""), ok9)
check("X4 U_21 = eta^21 V/(E4 E6) on the theta_3 slot: L^2 -> -1, S -> -1", ok21)
# a control on the S check itself: the theta_3 slot must map to itself (theta_2's slot does not; (1 3) swap)
t0 = pts[0]
e0 = eta(t0)
th2sq = lambda t: (2 * mp.exp(1j * mp.pi * t / 4) * mp.fsum(mp.exp(1j * mp.pi * n * (n + 1) * t) for n in range(0, 60))) ** 2
th4sq = lambda t: mp.fsum((-1) ** n * mp.exp(1j * mp.pi * n * n * t) for n in range(-60, 61)) ** 2
g9 = lambda t: eta(t) ** 6 / Ek(4, t)
swap = abs(g9(-1 / t0) * th2sq(-1 / t0) - g9(t0) * th4sq(t0))
check("U_9's S swaps the theta_2 and theta_4 slots with sign +1 (S_u = (1 3))", swap < tol, "residual %s" % mp.nstr(swap, 3))
print("FAILED CHECKS:", FAILS if FAILS else "none")
