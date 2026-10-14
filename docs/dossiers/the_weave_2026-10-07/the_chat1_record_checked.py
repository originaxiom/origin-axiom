"""W86's independent checks (I1 to I7) of chat1's record (chat1/web-seat @ 9fbab9f5e), on this seat's own code. The rule
(W86_RULE.md) was committed before this script; the predictions and priors are there.

  I1  the hybrid: W72's banked surface Yukawa (X4, Y0 = 2) normalised by each thread's own K (W84's instrument, N = 512)
      gives that thread's own m2/m3 within 10%, on chat1's 12 threads
  I2  reversal: (a) exactly, M(rev W) = (D M(W) D)^-1 with D = diag(1, -1), so rev(W)'s geodesic is the reflection
      tau -> -conj(tau) of W's, every rotation keeps |c|, and the least-|c| rotations' apexes reflect (x0 -> -x0 mod 1),
      on every thread to length 12 that is not its own reverse up to rotation; (b) on those to length 7, the thread
      frame's K and Y of rev(W) equal conj(K), conj(Y) of W to 1e-40 relative (W84's instrument, N = 256)
  I3  Rademacher's Psi = Phi - 3 sign(c(a + d)) (Dedekind sums, exact) is constant on rotations and equals #R - #L
      (R upper triangular) on the 745 threads to length 12; and eta(A tau) = e^{i pi Psi / 12} sqrt(c tau + d) eta(tau)
      on 12 threads to length 6 (30 digits)
  I4  W mod 2 sorts the threads to length 8 into A4 (odd trace), D4 (even trace, not 1 mod 2) and V4 (1 mod 2); up to
      the mirror L <-> R the counts are 16, 13 and 8 (the identification with reversal as well is a read-out)
  I5  SnapPy (high precision): rev(W) has W's volume and Chern-Simons invariant, and swap(rev(W)) = W^T has W's volume
      and minus its Chern-Simons invariant (mod pi^2), on 40 threads to length 10 (seed 86), to 1e-12
  I6  over the threads to length 8, the least volume in each class: LR (A4), LLR and LRR (D4), LLRR (V4); LLRR's
      volume is 4 Catalan, its Lagrange value sqrt 8 and its trace 6; no D4 thread has Lagrange value below 3
  I7  T-SIGN: b++W has H1 torsion |tr - 2| and b+-W has |tr + 2| (monodromies M and -M); CS(b+-W) - CS(b++W) is
      pi^2/2 mod pi^2 on 30 threads to length 10 (seed 86); every swap-symmetric thread to length 10 has CS(b++W) = 0
      and CS(b+-W) = pi^2/2 mod pi^2, to 1e-9

Run: python3 the_chat1_record_checked.py  ->  the_chat1_record_checked.json beside it.
"""
import itertools
import json
import math
import random
import sys
import time
import warnings
from fractions import Fraction
from pathlib import Path

import mpmath as mp

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_thread_frame_checked as TF  # noqa: E402  (W84's instrument: Forms, cycle, masses, word_matrix)
import snappy  # noqa: E402

OUT = HERE / "the_chat1_record_checked.json"
HYBRID_THREADS = ["LR", "LLRR", "LLRLR", "LRLRR", "LLR", "LRR", "LLRRR", "LLLRR", "LRRR", "LLLR", "LLLLR", "LRRRR"]
PI2 = math.pi ** 2


def lyndon_upto(n, m=2):
    return [w for k in range(m, n + 1) for w in ("".join(p) for p in itertools.product("LR", repeat=k))
            if all(w < w[i:] + w[:i] for i in range(1, len(w)))]


def lr(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def swap(w):
    return w.translate(str.maketrans("LR", "RL"))


def own_reverse(w):
    return lr(w[::-1]) == lr(w)


def red(x):
    y = math.fmod(x, PI2)
    if y > PI2 / 2:
        y -= PI2
    if y <= -PI2 / 2:
        y += PI2
    return y


def rel(A, B):
    num = max(abs(A[i][j] - B[i][j]) for i in range(3) for j in range(3))
    den = max(abs(A[i][j]) for i in range(3) for j in range(3))
    return num / den


# ------------------------------------------------------------------------------------------------------------- I1
def I1(forms):
    w72 = json.loads((HERE / "the_surface_yukawa.json").read_text(encoding="utf-8"))
    Y72 = [[mp.mpc(z[0], z[1]) for z in row] for row in w72["X4"]["Y (Y0 = 2.0)"]]
    rows, worst = {}, 0.0
    for w in HYBRID_THREADS:
        c = TF.cycle(forms, w, 512)
        own = TF.masses(c["K"], c["Y"])
        hyb = TF.masses(c["K"], Y72)
        r2 = float(mp.exp(hyb["ln m2/m3"] - own["ln m2/m3"]))
        r1 = float(mp.exp(hyb["ln m1/m3"] - own["ln m1/m3"]))
        rows[w] = {"own m2/m3": float(mp.exp(own["ln m2/m3"])), "hybrid m2/m3": float(mp.exp(hyb["ln m2/m3"])),
                   "hybrid / own (m2/m3)": r2, "hybrid / own (m1/m3)": r1}
        worst = max(worst, abs(r2 - 1))
    return {"per thread": rows, "worst |hybrid/own - 1| on m2/m3": worst, "holds": bool(worst < 0.10)}


# ------------------------------------------------------------------------------------------------------------- I2
def least_rotation_matrix(w):
    best = None
    for k in range(len(w)):
        rot = w[k:] + w[:k]
        M = TF.word_matrix(rot)
        if best is None or abs(M[1][0]) < abs(best[1][1][0]):
            best = (rot, M)
    return best


def I2a():
    D = ((1, 0), (0, -1))
    threads = [w for w in lyndon_upto(12) if not own_reverse(w)]
    bad_matrix, bad_c, bad_apex, ties = [], [], [], 0
    for w in threads:
        M = TF.word_matrix(w)
        DMD = TF.mat_mul(TF.mat_mul(D, M), D)
        inv = ((DMD[1][1], -DMD[0][1]), (-DMD[1][0], DMD[0][0]))
        if TF.word_matrix(w[::-1]) != inv:
            bad_matrix.append(w)
        cs_w = sorted(abs(TF.word_matrix(w[k:] + w[:k])[1][0]) for k in range(len(w)))
        cs_r = sorted(abs(TF.word_matrix(w[::-1][k:] + w[::-1][:k])[1][0]) for k in range(len(w)))
        if cs_w != cs_r:
            bad_c.append(w)
        if cs_w.count(cs_w[0]) > 1:
            ties += 1
        _, A = least_rotation_matrix(w)
        _, B = least_rotation_matrix(w[::-1])
        xa = Fraction(A[0][0] - A[1][1], 2 * A[1][0])
        xb = Fraction(B[0][0] - B[1][1], 2 * B[1][0])
        if (xa + xb).denominator != 1 or abs(A[1][0]) != abs(B[1][0]):
            bad_apex.append(w)
    return {"threads": len(threads), "M(rev W) = (D M D)^-1 fails": bad_matrix, "rotation |c| multisets differ": bad_c,
            "least-|c| apexes not reflected": bad_apex, "threads with tied least |c|": ties,
            "holds": bool(threads and not bad_matrix and not bad_c and not bad_apex)}


def I2b(forms):
    threads = [w for w in lyndon_upto(7) if not own_reverse(w)]
    rows, worst = {}, mp.mpf(0)
    for w in threads:
        a = TF.cycle(forms, w, 256)
        b = TF.cycle(forms, w[::-1], 256)
        cK = [[mp.conj(x) for x in row] for row in a["K"]]
        cY = [[mp.conj(x) for x in row] for row in a["Y"]]
        eK, eY = rel(b["K"], cK), rel(b["Y"], cY)
        worst = max(worst, eK, eY)
        rows[w] = {"K": float(eK), "Y": float(eY), "rotations used": [a["rotation"], b["rotation"]]}
    return {"threads": threads, "relative differences": rows, "worst": float(worst),
            "holds": bool(threads and worst < mp.mpf(10) ** -40)}


# ------------------------------------------------------------------------------------------------------------- I3
def dedekind(h, k):
    def saw(x):
        if x.denominator == 1:
            return Fraction(0)
        return x - (x.numerator // x.denominator) - Fraction(1, 2)
    return sum(saw(Fraction(r, k)) * saw(Fraction(h * r, k)) for r in range(1, k))


def psi(M):
    (a, b), (c, d) = M
    if c == 0:
        phi = Fraction(b, d)
    else:
        phi = Fraction(a + d, c) - 12 * (1 if c > 0 else -1) * dedekind(d, abs(c))
    s = (1 if c * (a + d) > 0 else (-1 if c * (a + d) < 0 else 0))
    return phi - 3 * s


def I3():
    threads = lyndon_upto(12)
    not_invariant, not_count = [], []
    for w in threads:
        vals = {psi(TF.word_matrix(w[k:] + w[:k])) for k in range(len(w))}
        if len(vals) != 1:
            not_invariant.append(w)
        if vals != {Fraction(w.count("R") - w.count("L"))}:
            not_count.append(w)
    balanced = sum(1 for w in threads if w.count("R") == w.count("L"))
    mp.mp.dps = 30
    tau = mp.mpc("0.05", "0.9")

    def eta(t):
        return mp.exp(mp.pi * 1j * t / 12) * mp.qp(mp.exp(2 * mp.pi * 1j * t))
    eta_rows, eta_worst = {}, mp.mpf(0)
    for w in lyndon_upto(6)[:12]:
        (a, b), (c, d) = TF.word_matrix(w)
        lhs = eta((a * tau + b) / (c * tau + d))
        rhs = mp.exp(mp.pi * 1j * psi(((a, b), (c, d))).numerator / psi(((a, b), (c, d))).denominator / 12) \
            * mp.sqrt(c * tau + d) * eta(tau)
        e = abs(lhs - rhs) / abs(rhs)
        eta_worst = max(eta_worst, e)
        eta_rows[w] = float(e)
    mp.mp.dps = TF.DPS
    return {"threads": len(threads), "balanced": balanced, "not rotation-invariant": not_invariant,
            "not #R - #L": not_count, "eta multiplier relative errors": eta_rows, "eta worst": float(eta_worst),
            "holds": bool(len(threads) == 745 and not not_invariant and not not_count
                          and eta_worst < mp.mpf(10) ** -25)}


# ------------------------------------------------------------------------------------------------------------- I4
def klass(w):
    (a, b), (c, d) = TF.word_matrix(w)
    if (a + d) % 2 == 1:
        return "A4"
    if a % 2 == 1 and d % 2 == 1 and b % 2 == 0 and c % 2 == 0:
        return "V4"
    return "D4"


def I4():
    threads = lyndon_upto(8)
    plain = {k: sum(1 for w in threads if klass(w) == k) for k in ("A4", "D4", "V4")}
    mirror = {}
    for w in threads:
        rep = min(w, lr(swap(w)))
        mirror[rep] = klass(w)
    by_mirror = {k: sum(1 for v in mirror.values() if v == k) for k in ("A4", "D4", "V4")}
    both = {}
    for w in threads:
        rep = min(w, lr(swap(w)), lr(w[::-1]), lr(swap(w[::-1])))
        both[rep] = klass(w)
    by_both = {k: sum(1 for v in both.values() if v == k) for k in ("A4", "D4", "V4")}
    consistent = all(klass(w) == klass(lr(swap(w))) for w in threads)
    return {"threads": len(threads), "by class": plain, "up to the mirror L <-> R": by_mirror,
            "up to mirror and reversal (read-out)": by_both, "the class is mirror-invariant": consistent,
            "holds": bool(by_mirror == {"A4": 16, "D4": 13, "V4": 8} and consistent)}


# ------------------------------------------------------------------------------------------------------------- I5-I7
def meas(name):
    M = snappy.ManifoldHP(name)
    cv = complex(M.complex_volume())
    return float(M.volume()), red(cv.imag), M


def I5():
    rng = random.Random(86)
    pool = [w for w in lyndon_upto(10, 4) if not own_reverse(w) and lr(swap(w[::-1])) != lr(w)]
    sample = rng.sample(pool, 40)
    rows, worst = {}, 0.0
    for w in sample:
        v, c, _ = meas("b++" + w)
        vr, cr, _ = meas("b++" + w[::-1])
        vt, ct, _ = meas("b++" + swap(w[::-1]))
        e = max(abs(vr - v), abs(red(cr - c)), abs(vt - v), abs(red(ct + c)))
        worst = max(worst, e)
        rows[w] = {"vol": v, "cs": c, "worst": e}
    return {"pool": len(pool), "sample": sample, "worst": worst, "rows": rows, "holds": bool(worst < 1e-12)}


def lagrange(w):
    (a, b), (c, d) = least_rotation_matrix(w)[1]
    return math.sqrt((a + d) ** 2 - 4) / abs(c)


def I6():
    threads = lyndon_upto(8)
    vol = {w: meas("b++" + w)[0] for w in threads}
    least = {}
    for k in ("A4", "D4", "V4"):
        ws = [w for w in threads if klass(w) == k]
        m = min(vol[w] for w in ws)
        least[k] = sorted(w for w in ws if abs(vol[w] - m) < 1e-9)
    catalan = float(mp.catalan)
    llrr = TF.word_matrix("LLRR")
    d4_min = min(lagrange(w) for w in threads if klass(w) == "D4")
    checks = {"least A4": least["A4"] == ["LR"], "least D4": least["D4"] == ["LLR", "LRR"],
              "least V4": least["V4"] == ["LLRR"], "LLRR's volume is 4 Catalan": abs(vol["LLRR"] - 4 * catalan) < 1e-12,
              "LLRR's Lagrange value is sqrt 8": abs(lagrange("LLRR") - math.sqrt(8)) < 1e-12,
              "LLRR's trace is 6": llrr[0][0] + llrr[1][1] == 6, "no D4 thread below Lagrange 3": d4_min >= 3}
    return {"least per class": least, "volumes of the least": {w: vol[w] for ws in least.values() for w in ws},
            "least D4 Lagrange value": d4_min, "checks": checks, "holds": bool(all(checks.values()))}


def torsion_order(M):
    h = M.homology()
    order = 1
    for e in h.elementary_divisors():
        if e != 0:
            order *= int(e)
    return order


def I7():
    rng = random.Random(86)
    pool = lyndon_upto(10, 2)
    sample = rng.sample(pool, 30)
    sym = [w for w in pool if lr(swap(w)) in (w, lr(w[::-1]))]
    bad_h, bad_shift, bad_sym, worst = [], [], [], 0.0
    for w in sorted(set(sample) | set(sym)):
        vp, cp, Mp = meas("b++" + w)
        vm, cm, Mm = meas("b+-" + w)
        M = TF.word_matrix(w)
        tr = M[0][0] + M[1][1]
        if torsion_order(Mp) != abs(tr - 2) or torsion_order(Mm) != abs(tr + 2):
            bad_h.append([w, str(Mp.homology()), str(Mm.homology()), tr])
        shift = abs(abs(red(cm - cp)) - PI2 / 2)
        worst = max(worst, shift)
        if shift > 1e-9:
            bad_shift.append([w, cp, cm])
        if w in sym and (abs(cp) > 1e-9 or abs(abs(cm) - PI2 / 2) > 1e-9):
            bad_sym.append([w, cp, cm])
    return {"sample": sample, "swap-symmetric to length 10": len(sym), "homology mismatches": bad_h,
            "shift not pi^2/2": bad_shift, "swap-symmetric not (0, pi^2/2)": bad_sym, "worst shift deviation": worst,
            "holds": bool(not bad_h and not bad_shift and not bad_sym)}


def main():
    t0 = time.time()
    out = {"status": "W86's independent checks of chat1's record (script committed before its one run)",
           "chat1 commit": "9fbab9f5e", "snappy": snappy.__version__}
    out["I3"] = I3()
    out["I4"] = I4()
    out["I2a"] = I2a()
    out["I5"] = I5()
    out["I6"] = I6()
    out["I7"] = I7()
    forms = TF.Forms()
    out["I1"] = I1(forms)
    out["I2b"] = I2b(forms)
    out["I2"] = {"holds": bool(out["I2a"]["holds"] and out["I2b"]["holds"])}
    out["cells"] = {k: out[k]["holds"] for k in ("I1", "I2", "I3", "I4", "I5", "I6", "I7")}
    out["every cell holds"] = all(out["cells"].values())
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
