"""The explore seat, 2026-11-07: THE LEVEL PREMISE AS A CONSERVATION LAW (PREREGISTRATION_CONSERVATION.md; HL1-HL4).
Data-free: SL(2, Z/N) arithmetic, geodesic lengths, SnapPy volumes, continued-fraction apexes. No frame value, no data, no
held-out quantity. The defects, closed words and actions are the web seat's (modules pinned at ecda7de70, copied here).

  1  HL1  the symmetry reading at 5: the centraliser of LR mod 5 against the line-invisibility set (L)
  2  HL2  the charge reading with locality at N = 2..5: which E conserve the class of every golden background
  3  the premises P0, P1, P1+, P2, P3a, P3b over R1 (the web seat's range) and R2 (extended): the least excess length,
     uniqueness, the excess volume of the five least, the selected departure's highest apex (HL3, HL4)

    python3 conservation_check.py
"""
import importlib.util
import itertools
import math
import pathlib
import sys
import time

import mpmath as mp
import snappy

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def load(name):
    sp = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    mod = importlib.util.module_from_spec(sp)
    sys.modules[name] = mod
    sp.loader.exec_module(mod)
    return mod


LA = load("least_action_check")
PH = load("least_action_posthoc_rung")
D0 = LA.D0
L, R, LR = D0.L, D0.R, D0.LR
VOL4 = float(snappy.ManifoldHP("m004").volume())
RUNGS = (2, 3, 4, 5)
MOD = 60  # lcm of the rungs


def mmul(A, B, n):
    return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % n, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % n),
            ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % n, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % n))


def mred(A, n):
    return ((A[0][0] % n, A[0][1] % n), (A[1][0] % n, A[1][1] % n))


def minv(A, n):  # det 1
    return ((A[1][1] % n, -A[0][1] % n), (-A[1][0] % n, A[0][0] % n))


def mneg(A, n):
    return ((-A[0][0] % n, -A[0][1] % n), (-A[1][0] % n, -A[1][1] % n))


def ident(n):
    return ((1 % n, 0), (0, 1 % n))


def sl2(n):
    out = []
    for a, b, c, d in itertools.product(range(n), repeat=4):
        if (a * d - b * c) % n == 1 % n:
            out.append(((a, b), (c, d)))
    return out


def conj_class(W, G, n):
    return frozenset(mmul(mmul(g, W, n), minv(g, n), n) for g in G)


# powers of L and R mod 60, for fast E mod 60
LP = {r: mred(D0.pw(L, r), MOD) for r in range(0, 70)}
RP = {r: mred(D0.pw(R, r), MOD) for r in range(0, 70)}


def mat_mod(runs):
    M = ident(MOD)
    for i, r in enumerate(runs):
        M = mmul(M, LP[r] if i % 2 == 0 else RP[r], MOD)
    return M


def E_mod(runs):
    return mmul(mat_mod(runs), minv(mat_mod([1] * len(runs)), MOD), MOD)


def pm_identity(E, n):
    e = mred(E, n)
    return e == ident(n) or e == mneg(ident(n), n)


CENT = {}


def commutes(E, n):
    e = mred(E, n)
    lr = mred(LR, n)
    return mmul(e, lr, n) == mmul(lr, e, n)


PREMISES = {
    "P0  none": lambda E: True,
    "P1  symmetry at 5 (line)": lambda E: commutes(E, 5),
    "P1+ symmetry at 2,3,4,5": lambda E: all(commutes(E, n) for n in RUNGS),
    "P2  charge at 5 (rung)": lambda E: pm_identity(E, 5),
    "P3a charge at 4,5": lambda E: pm_identity(E, 4) and pm_identity(E, 5),
    "P3b charge at 2,3,4,5": lambda E: all(pm_identity(E, n) for n in RUNGS),
}


def R2():
    for m, top in ((1, 64), (2, 64), (3, 64), (4, 24), (5, 10)):
        for runs in itertools.product(range(1, top + 1), repeat=m):
            if runs[0] >= 2 and runs[-1] >= 2:
                yield runs


def fast_excess(runs, k=20):
    m = len(runs)
    X = R if m % 2 else D0.I2
    W = D0.mul(D0.mul(LA.mat(runs), X), D0.pw(LR, k))
    G = D0.mul(D0.mul(LA.mat([1] * m), X), D0.pw(LR, k))
    return 2 * (math.log(D0.tr(W)) - math.log(D0.tr(G)))


def letters(runs, k):
    s = "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(runs))
    return s + ("R" if len(runs) % 2 else "") + "LR" * k


def dV(runs, k=10):
    M = snappy.Manifold("b++" + letters(runs, k))
    if M.solution_type() != "all tetrahedra positively oriented":
        return None
    return float(M.volume()) - (k + (len(runs) + 1) // 2) * VOL4


if __name__ == "__main__":
    t0 = time.time()
    print("THE LEVEL PREMISE AS A CONSERVATION LAW -- data-free check (the explore seat, 2026-11-07)")

    print("\n1. HL1 -- the symmetry reading at level 5")
    G5 = sl2(5)
    cent5 = [E for E in G5 if commutes(E, 5)]
    lr5 = mred(LR, 5)
    golden = set()
    P = ident(5)
    for j in range(10):
        golden.add(P)
        golden.add(mneg(P, 5))
        P = mmul(P, lr5, 5)
    pair = LA.PAIR
    lineset = [E for E in G5 if all(D0.pm(D0.act(w, minv(E, 5))) == w for w in pair)]  # mod-5 inverse (attempt 1 used
    # D0.inv, which asserts an integer determinant of +-1 and crashed on mod-5 representatives; disclosed in the relay)
    print("  |SL(2,F5)| = %d; |C5(LR)| = %d; C5(LR) = +-<LR>: %s; |(L)-set| = %d; C5(LR) = (L)-set: %s" % (
        len(G5), len(cent5), set(cent5) == golden, len(lineset), set(cent5) == set(lineset)))
    hl1 = set(cent5) == golden == set(lineset) and len(cent5) == 10
    print("  HL1: %s" % hl1)

    print("\n2. HL2 -- the charge reading with locality, N = 2..5")
    hl2 = True
    for n in RUNGS:
        G = sl2(n)
        lrn = mred(LR, n)
        backs, P = [], ident(n)
        for j in range(24):
            backs.append(P)
            P = mmul(P, lrn, n)
        classes = {W: conj_class(W, G, n) | conj_class(mneg(W, n), G, n) for W in set(backs)}
        keep = [E for E in G if all(mmul(E, W, n) in classes[W] for W in set(backs))]
        pmI = {ident(n), mneg(ident(n), n)}
        ok = set(keep) == pmI
        hl2 &= ok
        order = next((j for j in range(1, 24) if backs[j] == ident(n)), None)
        print("  N = %d: |SL(2,Z/%d)| = %d; ord(LR) = %d; conserving every golden background's class: %s; = +-I: %s" % (
            n, n, len(G), order, sorted(keep), ok))
    print("  HL2: %s" % hl2)

    print("\n3. the premises (R1 = the web seat's range; R2 = extended)")
    space = list(dict.fromkeys(itertools.chain(LA.space(), R2())))
    print("  defects in R1 u R2: %d" % len(space))
    sel = {name: [] for name in PREMISES}
    for runs in space:
        E = E_mod(runs)
        for name, f in PREMISES.items():
            if f(E):
                sel[name].append(runs)
    results = {}
    for name in PREMISES:
        cand = sel[name]
        if name.startswith("P0"):
            cand = list(LA.space())  # P0 ranked in R1 only (every defect qualifies)
        ranked = sorted(((fast_excess(r), r) for r in cand), key=lambda t: t[0])
        top = ranked[:5]
        vols = [(dV(r), r) for _, r in top]
        vbest = min((v for v in vols if v[0] is not None), key=lambda t: t[0])
        best = top[0][1]
        uniq = len(ranked) < 2 or ranked[1][0] - ranked[0][0] > 1e-9
        im, re_ = D0.highest_cf(LA.closed_runs(best), reps=20)
        results[name] = (best, float(im))
        print("\n  %s: %d invisible defects" % (name, len(cand)))
        for (d, r), (v, _) in zip(top, vols):
            print("    %-22s dS %.10f  dV %s" % (r, d, "%.10f" % v if v is not None else "non-geometric"))
        print("    least by length: %s (unique: %s; next gap %.3e); least by volume among these five: %s; same: %s" % (
            best, uniq, (ranked[1][0] - ranked[0][0]) if len(ranked) > 1 else float("nan"), vbest[1], vbest[1] == best))
        print("    selected departure's highest apex: Im %s  Re %s" % (mp.nstr(im, 10), mp.nstr(re_, 6)))

    print("\n4. HL3 / HL4")
    chain = ["P0  none", "P1  symmetry at 5 (line)", "P2  charge at 5 (rung)", "P3a charge at 4,5", "P3b charge at 2,3,4,5"]
    depths = [results[c][1] for c in chain]
    print("  depths along P0 -> P1 -> P2 -> P3a -> P3b: %s" % ", ".join("%.6f" % d for d in depths))
    hl3 = all(depths[i + 1] > depths[i] for i in range(len(depths) - 1)) and results["P2  charge at 5 (rung)"][0] == (6,)
    print("  HL3 (strictly rising, P2 selects (6)): %s" % hl3)
    print("  P1+ (symmetry at every rung) selects %s, apex Im %.6f" % results["P1+ symmetry at 2,3,4,5"])
    print("\nruntime %.1f s" % (time.time() - t0))
    print("conservation_check exit 0")
