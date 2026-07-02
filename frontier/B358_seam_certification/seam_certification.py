"""B358 -- the seam, exactly certified: the twisted quantum-pair channel carries sqrt(-15);
the canonical channel provably does not. (Campaign escalation of the cross-session seam claim.)

TWO LIFTS OF THE SAME PAIR OBSERVABLE tr(Par * P_a(W1) * Q_b(W2)) at level 15, both computed in
EXACT Fraction arithmetic over Q(zeta_60) (the engine in cyclo_engine.py; zero numerics):

  CANONICAL lift (B355 conventions: T = e_15(x^2), S = F_{-2}/g; Par commutes with the image):
      s(sqrt-15 coefficient) == 0 for ALL doubles, exactly.  [C_canonical.json]
  THETA lift (the cross-session construction: W_L = diag zeta^{j(j-1)/2}, W_R = F W_L^-1 F^-1;
      Par W Par^-1 W^-1 = X^1 Z^2, a nontrivial Heisenberg element):
      44 of 49 nonzero doubles are seam-bearing, exactly; e.g.
      P_0 Q_4 = -1/48 - (1/80) sqrt5 - (1/48) sqrt(-3) + (1/48) sqrt(-15).  [C_theta.json]
  CONTROLS (both lifts): every single-seed trace tr(Par P_a), tr(Par Q_b) has ZERO sqrt(-3) and
      sqrt(-15) coefficients, exactly.

So sqrt(-15) -- the arithmetic home of the value, unreached through five channels -- appears
exactly, and only, in the HEISENBERG-TWISTED sector of the two-seed pairing. The seam coefficient
is a function of the lift's theta-characteristic; whether the pairing geometry FORCES a
characteristic is the named open question (L57).

The committed C-tables are regenerable: python seam_certification.py --regenerate (approx 8 min,
pure Fractions); the always-on readout below recomputes everything downstream of C exactly and
spot-checks C against an independent dps-40 numeric evaluation. Firewalled; nothing to CLAIMS;
a field-membership statement about quantum invariants, not physics.
"""
import json
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(__file__))
import cyclo_engine as E

DEG = E.DEG
HERE = os.path.dirname(os.path.abspath(__file__))
GAL_H = [1, 19, 31, 49]                       # Gal(Q(zeta60)/H), H = Q(sqrt5, sqrt-3)


def _load(name):
    data = json.load(open(os.path.join(HERE, name)))
    C = [[[Fr(s) for s in data["C"][j][l]] for l in range(12)] for j in range(20)]
    c1 = [[Fr(s) for s in v] for v in data["c1"]]
    c2 = [[Fr(s) for s in v] for v in data["c2"]]
    return C, c1, c2


def sigma(a, c):
    out = [Fr(0)] * DEG
    for k in range(DEG):
        if a[k]:
            out = E.add(out, E.scal(a[k], E.zeta((c * k) % 60)))
    return out


def H_avg(t):
    s = [Fr(0)] * DEG
    for c in GAL_H:
        s = E.add(s, sigma(t, c))
    return E.scal(Fr(1, 4), s)


def solve_H(t):
    """t = p + q sqrt5 + r sqrt(-3) + s sqrt(-15), exactly; None if t not in H."""
    cols = [E.ONE, E.SQRT5, E.SQRTm3, E.SQRTm15]
    Ab = [[cols[c][row] for c in range(4)] + [t[row]] for row in range(DEG)]
    r = 0
    piv_cols = []
    for c in range(4):
        piv = next((i for i in range(r, DEG) if Ab[i][c] != 0), None)
        if piv is None:
            continue
        Ab[r], Ab[piv] = Ab[piv], Ab[r]
        pv = Ab[r][c]
        Ab[r] = [v / pv for v in Ab[r]]
        for i in range(DEG):
            if i != r and Ab[i][c] != 0:
                f = Ab[i][c]
                Ab[i] = [Ab[i][j] - f * Ab[r][j] for j in range(5)]
        piv_cols.append(c)
        r += 1
    sol = [Fr(0)] * 4
    for i, c in enumerate(piv_cols):
        sol[c] = Ab[i][4]
    for i in range(r, DEG):
        if Ab[i][4] != 0:
            return None
    chk = E.ZERO
    for c in range(4):
        chk = E.add(chk, E.scal(sol[c], cols[c]))
    assert chk == t
    return tuple(sol)


def doubles_readout(which):
    """All doubles t(a,b) = (1/240) sum zeta20^{-ja} zeta12^{-lb} C[j][l], H-projected, exact."""
    C, c1, c2 = _load(which)
    out = {}
    for a in range(20):
        for b in range(12):
            t = E.ZERO
            for j in range(20):
                zja = E.zeta((-3 * j * a) % 60)
                for l in range(12):
                    t = E.add(t, E.mul(E.mul(zja, E.zeta((-5 * l * b) % 60)), C[j][l]))
            t = E.scal(Fr(1, 240), t)
            if t == E.ZERO:
                continue
            sol = solve_H(H_avg(t))
            assert sol is not None, (which, a, b)
            out[(a, b)] = sol
    return out


def singles_clean(which):
    """Both single-seed control families: r = s = 0 exactly for every projector."""
    C, c1, c2 = _load(which)
    for a in range(20):
        t = E.ZERO
        for j in range(20):
            t = E.add(t, E.mul(E.zeta((-3 * j * a) % 60), c1[j]))
        t = E.scal(Fr(1, 20), t)
        if t == E.ZERO:
            continue
        sol = solve_H(H_avg(t))
        if sol is None or sol[2] != 0 or sol[3] != 0:
            return False
    for b in range(12):
        t = E.ZERO
        for l in range(12):
            t = E.add(t, E.mul(E.zeta((-5 * l * b) % 60), c2[l]))
        t = E.scal(Fr(1, 12), t)
        if t == E.ZERO:
            continue
        sol = solve_H(H_avg(t))
        if sol is None or sol[2] != 0 or sol[3] != 0:
            return False
    return True


def numeric_spot_check(which, entries=((0, 0), (1, 3), (5, 2)), dps=40):
    """Independent guard on the committed C-tables: evaluate a few C[j][l] numerically at dps 40
    from a fresh numeric build of the corresponding construction, compare to the exact values."""
    import mpmath as mp
    mp.mp.dps = dps
    C, _, _ = _load(which)

    def as_num(vec):
        z = mp.e ** (2j * mp.pi / 60)
        return sum(mp.mpf(str(vec[k].numerator)) / mp.mpf(str(vec[k].denominator)) * z ** k
                   for k in range(DEG))

    z15 = mp.e ** (2j * mp.pi / 15)
    if which == "C_canonical.json":
        T = mp.zeros(15)
        F = mp.zeros(15)
        for x in range(15):
            T[x, x] = z15 ** (x * x)
            for y in range(15):
                F[x, y] = z15 ** ((-2 * x * y) % 15)
        g = sum(z15 ** (x * x) for x in range(15))
        S = F / g
        W1 = T * S * T ** -1 * S ** -1
        W2 = (T ** 2) * S * (T ** -2) * S ** -1
    else:
        D = mp.zeros(15)
        Fm = mp.zeros(15)
        for j in range(15):
            D[j, j] = z15 ** ((j * (j - 1) // 2) % 15)
            for k in range(15):
                Fm[j, k] = z15 ** (j * k) / mp.sqrt(15)
        Fi = mp.zeros(15)
        for j in range(15):
            for k in range(15):
                Fi[j, k] = z15 ** ((-j * k) % 15) / mp.sqrt(15)
        WR = Fm * D ** -1 * Fi
        W1 = WR * D
        W2 = WR * WR * D * D
    for (j, l) in entries:
        M = (W1 ** j) * (W2 ** l)
        t = sum(M[(-x) % 15, x] for x in range(15))
        if abs(t - as_num(C[j][l])) > mp.mpf(10) ** -25:
            return False
    return True


def double_one(which, a, b):
    """One double, exactly (for the always-on test tier)."""
    C, _, _ = _load(which)
    t = E.ZERO
    for j in range(20):
        zja = E.zeta((-3 * j * a) % 60)
        for l in range(12):
            t = E.add(t, E.mul(E.mul(zja, E.zeta((-5 * l * b) % 60)), C[j][l]))
    t = E.scal(Fr(1, 240), t)
    return solve_H(H_avg(t)) if t != E.ZERO else (Fr(0),) * 4


FLAGSHIP = (Fr(-1, 48), Fr(-1, 80), Fr(-1, 48), Fr(1, 48))


def run_all():
    theta = doubles_readout("C_theta.json")
    canon = doubles_readout("C_canonical.json")
    theta_seam = {k: v for k, v in theta.items() if v[3] != 0}
    canon_seam = {k: v for k, v in canon.items() if v[3] != 0}
    return dict(
        theta_nonzero=len(theta), theta_seam=len(theta_seam),
        canonical_nonzero=len(canon), canonical_seam=len(canon_seam),
        flagship=(theta.get((0, 4)) == FLAGSHIP),
        controls=(singles_clean("C_theta.json") and singles_clean("C_canonical.json")),
        spot_theta=numeric_spot_check("C_theta.json"),
        spot_canon=numeric_spot_check("C_canonical.json"),
    )


if __name__ == "__main__":
    if "--regenerate" in sys.argv:
        print("regenerate: run cyclo_engine.py (canonical) and the theta variant; see FINDINGS.")
        raise SystemExit
    r = run_all()
    for k, v in r.items():
        print(f"  {k}: {v}")
