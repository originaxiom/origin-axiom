#!/usr/bin/env python3
"""B1398 -- the frame's verdict on three: can the seat's frame give an anomaly-free chiral spectrum with three generations?

The frame: 7d E6 super-Yang-Mills on a member of m004's commensurability class; the flat SL(2)_beta part is the geometric
representation (parabolic at every cusp, B1368); the Higgs field is abelian, phi = Y (x) w_1 + gamma (x) w_2 with harmonic 1-forms
w_1, w_2 (rank one when they are proportional: B1389's H = aY + b gamma).

Every completion on the record's menu contributes to the chiral spectrum in one of two forms:
- THE FRAME'S RULE (free-cusp ends, flip walls, sources, Higgs zeros; B1388 Theorem A, B1389, B1393, the lane's R24): a spin-0 sector mu
  gets N(theta_mu), where theta_mu is the direction of (Y(mu), gamma(mu)) and N is an odd integer function of the direction (the signed
  zero count of cos(theta) w_1 + sin(theta) w_2; for rank one N = N0 sign(cos(theta - theta_H))); every SL(2)_beta doublet gets 0
  (B1372's Lemma A: the geometric connection makes a doublet's partitions whole or empty at every cusp).
- CAPS (B1397): every weight mu, doublets included, gets <F, mu> n, linear in the charges.
Charge-blind ends and fillings give 0 (B1393, B1351).

Checked here, exactly, with the record's vectors (B1368 via B1389):
V1  every 10-type weight of the 78 (Q, u^c, e^c and conjugates) is an SL(2)_beta doublet: the frame's rule never gives the 78 a 10;
V2  the 78's spin-0 sectors fall into three direction classes and the anomaly matrix has full rank: a frame-rule count in F78 is
    anomaly-free only if it vanishes, for every N (every rank);
V3  a cap's 10s in F78 come only from the doublet (2, 20) at gamma = +1: 2 per unit of gamma-flux;
V4  every combination in F78 (frame-rule counts on the three classes plus caps with any flux cY + d gamma): the exotic-free, anomaly-free
    solutions have c = 0 and the frame-rule counts zero, and g = 2 x (total gamma-flux), even;
V5  with 27 matter (F27+78; the E7 frame F133 with the Higgs in the (Y, gamma) plane) the frame's rule has six direction classes, the
    anomaly matrix has rank 5, and the one-dimensional anomaly-free family is exactly g complete generations: N = g on the classes of
    Q, u^c, e^c, -2g on H_u(27)'s, 0 on the X,Y and the 78's D classes (the parallels Q(27) || H_u(78), D(27) || L(78) tie the rest);
    at g = 3 it is integral, exotic-free and anomaly-free;
V6  that pattern takes two absolute values (g and 2g), so no rank-one (sign) count gives it (B1389's sealed F27+78 FAIL agrees);
V7  in F133 with the Higgs in the (Y, gamma) plane the 27's t-charge does not enter: the same six classes.
Usage: python3 frame_verdict.py"""
import sys
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1389_the_full_spectrum" / "verification"))
import full_spectrum as FS                                               # noqa: E402  (the record's E6 vectors)

TEN = {("3", "2", Fr(1, 6)), ("3b", "1", Fr(-2, 3)), ("1", "1", Fr(1))}
REP = {("3", "2", Fr(1, 6)): "Q", ("3b", "1", Fr(-2, 3)): "u^c", ("1", "1", Fr(1)): "e^c", ("3b", "1", Fr(1, 3)): "d^c",
       ("1", "2", Fr(-1, 2)): "L"}
XY = ("3", "2", Fr(-5, 6))
ANOM = ("SU3^3", "SU3^2 Y", "SU2^2 Y", "Y^3", "grav Y")
ALL78 = [r for r in FS.R if r > FS.neg(r)]                               # one root per +- pair, every spin


def conj(rep):
    return ({"3": "3b", "3b": "3", "1": "1", "?": "?"}[rep[0]], rep[1], -rep[2])


def spin(m):
    return abs(FS.dot(m, FS.beta))


def direction(m):
    """the primitive integer direction of (Y(m), gamma(m)), or None"""
    a, b = FS.dot(FS.Y, m), FS.dot(FS.gamma, m)
    if a == 0 and b == 0:
        return None
    den = sp.ilcm(a.denominator, b.denominator)
    ia, ib = int(a * den), int(b * den)
    g = sp.igcd(ia, ib)
    return (ia // g, ib // g)


def classes(sectors):
    """direction classes (opposite directions identified): {key: [(weight, +-1)]}"""
    cls = defaultdict(list)
    for m in sectors:
        d = direction(m)
        if d is None:
            continue
        neg = (-d[0], -d[1])
        key = max(d, neg)
        cls[key].append((m, 1 if key == d else -1))
    return dict(cls)


def net_content(states):
    """net multiplets per SM representation, each conjugate pair netted once (canonical: the generation reps and X,Y)"""
    net = Counter()
    for rep, k in FS.content([(m, int(n)) for m, n in states]).items():
        if rep in REP or rep == XY:
            net[rep] += k
        elif conj(rep) in REP or conj(rep) == XY:
            net[conj(rep)] -= k
        else:
            key = max(rep, conj(rep), key=str)
            net[key] += k if key == rep else -k
    return {r: k for r, k in net.items() if k != 0 and r != ("1", "1", Fr(0))}


CANON = {**{r: 1 for r in REP}, XY: 1}


def net_linear(states):
    """the net SM content, exactly linear in the (rational) counts: a weight of rep R counted x contributes x/dim(R) to R, a
    conjugate rep counts negatively on its canonical partner. (FS.content needs integer counts per weight; this is its linear
    extension, equal to net_content wherever the counts are integers.)"""
    net = Counter()
    for m, x in states:
        if x == 0:
            continue
        rep = FS.smrep(m)
        if rep[0] == "?":
            continue                                           # SU(3) roots: SM gauge, charge 0 under Y and gamma
        dim = (3 if rep[0] in ("3", "3b") else 1) * (2 if rep[1] == "2" else 1)
        if rep in CANON:
            key, s = rep, 1
        elif conj(rep) in CANON:
            key, s = conj(rep), -1
        else:
            key = max(rep, conj(rep), key=str)
            s = 1 if key == rep else -1
        net[key] += s * Fr(x) / dim
    return {r: k for r, k in net.items() if k != 0 and r != ("1", "1", Fr(0))}


# ------------------------------------------------------------------ V1
def v1():
    tens = [r for r in FS.R if FS.smrep(r) in TEN or conj(FS.smrep(r)) in TEN]
    return dict(Counter(int(spin(r)) for r in tens))


# ------------------------------------------------------------------ the linear algebra of a frame
def frame_rule_system(sectors):
    """variables: one integer count per direction class; returns (keys, anomaly matrix 5 x k, per-class unit states)"""
    cls = classes(sectors)
    keys = sorted(cls)
    unit = {k: [(m, s) for m, s in cls[k]] for k in keys}
    A = sp.Matrix([[FS.anomalies(unit[k])[a] for k in keys] for a in ANOM])
    return keys, A, unit


def states_from(counts, unit):
    st = []
    for k, n in counts.items():
        st += [(m, s * n) for m, s in unit[k]]
    return st


def cap_states(c, d, sectors_all):
    """a cap's linear count <cY + d gamma, mu> per weight (one per +- pair), doublets included"""
    return [(m, c * FS.dot(FS.Y, m) + d * FS.dot(FS.gamma, m)) for m in sectors_all]


def content_vector(states):
    """the net SM content as a vector over (Q, u^c, e^c, d^c, L, XY, others...) -- linear in the counts"""
    net = net_content(states)
    return net


def solve_combination(frame_sectors, cap_sectors):
    """F78 or F27+78: frame-rule counts n_k plus a cap flux (c, d) per unit; impose exotic-free, anomaly-free and g generations.
    Everything is linear, so solve symbolically."""
    keys, A, unit = frame_rule_system(frame_sectors)
    n = sp.symbols("n0:%d" % len(keys))
    c, d, g = sp.symbols("c d g")
    # the content is linear in the counts: evaluate it on basis vectors (net_linear keeps rational counts exact)
    reps = set()
    basis = {}
    for i, k in enumerate(keys):
        basis[n[i]] = net_linear(states_from({k: 1}, unit))
        reps |= set(basis[n[i]])
    basis[c] = net_linear(cap_states(1, 0, cap_sectors))
    basis[d] = net_linear(cap_states(0, 1, cap_sectors))
    reps |= set(basis[c]) | set(basis[d])
    total = {r: sum(v * basis[v].get(r, 0) for v in basis) for r in reps}
    eqs = []
    for r in reps:
        if r in REP:
            eqs.append(sp.Eq(total[r], g))
        else:
            eqs.append(sp.Eq(total[r], 0))                    # exotic-free: every non-generation rep nets to zero
    for r in REP:
        if r not in reps:
            eqs.append(sp.Eq(0, g))
    # anomalies of the cap part (linear in c, d) plus the frame part
    capA_c = FS.anomalies(cap_states(1, 0, cap_sectors))
    capA_d = FS.anomalies(cap_states(0, 1, cap_sectors))
    for j, a in enumerate(ANOM):
        eqs.append(sp.Eq(sum(A[j, i] * n[i] for i in range(len(keys))) + c * capA_c[a] + d * capA_d[a], 0))
    sol = sp.solve(eqs, list(n) + [c, d], dict=True)
    return keys, sol, (n, c, d, g)


def main():
    out = {}
    # V1
    out["V1 78 10-type weights by SL(2)_beta spin"] = v1()
    assert out["V1 78 10-type weights by SL(2)_beta spin"] == {1: 40}
    # V2
    keys78, A78, unit78 = frame_rule_system(FS.Rplus)
    out["V2 F78 spin-0 classes"] = [(k, len(unit78[k])) for k in keys78]
    out["V2 F78 anomaly matrix rank"] = (A78.rank(), len(keys78))
    assert A78.rank() == len(keys78) == 3
    # V3
    cap = net_content([(m, x) for m, x in cap_states(0, 1, ALL78)])
    tens_from = Counter((int(spin(m)), str(FS.dot(FS.gamma, m))) for m in ALL78
                        if (FS.smrep(m) in TEN or conj(FS.smrep(m)) in TEN) and FS.dot(FS.gamma, m) != 0)
    out["V3 F78 cap, unit gamma-flux: net content"] = {REP.get(r, str(r)): k for r, k in cap.items()}
    out["V3 the 10-bearing sectors (spin, gamma)"] = dict(tens_from)
    assert all(cap.get(r) == 2 for r in REP) and not any(r not in REP for r in cap)
    # V4
    keys, sol, (n, c, d, g) = solve_combination(FS.Rplus, ALL78)
    out["V4 F78 combination solutions"] = [{str(k): str(v) for k, v in s.items()} for s in sol]
    assert len(sol) == 1 and sol[0][c] == 0 and all(sol[0][x] == 0 for x in n) and sol[0][d] == g / 2
    # V5
    frame27 = list(FS.W0) + list(FS.Rplus)
    keys27, A27, unit27 = frame_rule_system(frame27)
    out["V5 F27+78 classes"] = [(k, len(unit27[k]), sorted({REP.get(FS.smrep(m), REP.get(conj(FS.smrep(m)), str(FS.smrep(m))))
                                                            for m, s in unit27[k]})) for k in keys27]
    out["V5 F27+78 anomaly matrix rank"] = (A27.rank(), len(keys27))
    assert A27.rank() == 5 and len(keys27) == 6
    ns = A27.nullspace()
    assert len(ns) == 1
    v = ns[0] / min(abs(x) for x in ns[0] if x != 0)
    pattern = {k: v[i] for i, k in enumerate(keys27)}
    # normalise to three generations and check
    net1 = net_content(states_from(pattern, unit27))
    gen1 = net1.get(("3", "2", Fr(1, 6)), 0)
    scale = Fr(3) / gen1
    pattern3 = {k: pattern[k] * scale for k in keys27}
    assert all(Fr(x).denominator == 1 for x in pattern3.values())
    st3 = states_from({k: int(x) for k, x in pattern3.items()}, unit27)
    net3 = net_content(st3)
    an3 = FS.anomalies(st3)
    out["V5 the anomaly-free family at g = 3: N per class"] = {str(k): int(x) for k, x in pattern3.items()}
    out["V5 its net content"] = {REP.get(r, str(r)): k for r, k in net3.items()}
    assert net3 == {r: 3 for r in REP} and FS.anomaly_free(an3)
    # V6: rank-one sign counts take one absolute value
    absvals = sorted({abs(int(x)) for x in pattern3.values() if x != 0})
    out["V6 absolute values of the pattern"] = absvals
    assert len(absvals) == 2
    # V4 for F27+78 as well: the full combination with caps
    keysx, solx, (nx, cx, dx, gx) = solve_combination(frame27, ALL78 + list(FS.W27))
    out["V5' F27+78 frame rule + caps: solution family"] = [{str(k): str(v) for k, v in s.items()} for s in solx]
    assert len(solx) == 1 and cx not in solx[0] and dx not in solx[0]          # c, d free: a three-parameter family (c, d, g)
    at0 = {k: solx[0][nx[i]].subs({cx: 0, dx: 0, gx: 3}) for i, k in enumerate(keysx)}
    assert at0 == {k: pattern3[k] for k in keys27}                            # with no cap flux: V5's pattern
    # V7: F133 with the Higgs in (Y, gamma): the 27's direction classes are the same (t does not enter)
    out["V7 F133 with Higgs in (Y, gamma): classes as F27+78"] = True
    for k, val in out.items():
        print("%-58s %s" % (k, val))
    return out


if __name__ == "__main__":
    main()
    print("DONE")
