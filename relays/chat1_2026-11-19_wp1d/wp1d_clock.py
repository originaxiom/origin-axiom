#!/usr/bin/env python3
"""W-P1, step 4 (W-P1d): the clock test. Frame C's read-outs under (a), the move count, and (b), length. Data-free: no
frame value is computed here. W-F24's committed fibre table is read, and nothing is compared with a measured number.

    python3 -I -u wp1d_clock.py

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, step 4 (e61768f5c, committed before this script).

THE FIBRE. W-F24's table (../chat1_2026-11-15_wf24/wf24_summary.json, "fibre"): A(tau) and G(tau) for the 12 sector
ratios at its 154 points, heights 0.876 to 6. A node's value: linear interpolation of A and of log G on those points,
the nearest point outside their hull (W-F24's rule). Above the table's top (Im tau > 6):
  T1   clamped: the value at (Re tau, 6);
  T2   the cusp law: log A and log G continue linearly in Im tau from (Re tau, 6), with the least-squares slope of the
       table's column over heights 4, 5, 6, interpolated linearly in Re tau between the 11 columns;
  T2b  as T2, with the slope over heights 2, 2.5, 3, 3.5, 4 (reported, no expectation).

THE THREADS. W-P1c's (../chat1_2026-11-18_wp1/wp1c_heights.py, its functions run as text): one period cut into one
piece per letter, each piece sampled at midpoints (here at least 30 points per unit length and 8 per piece), each
sample reduced to SL(2, Z)'s standard domain keeping Re tau and Im tau, each word weighted by its length. The function
thread_xy below is W-P1c's thread() with Re tau kept and the run radii read from the same ends.
  (a)  W-P1c's words: 2,000 uniform random words of n = 20, 40, 80 letters (seeds 1, 2, 3); standard errors from
       1,000 resamples of the words (seed 7).
  (b)  W-P1c's classes: every primitive cyclic word with both letters and trace at most X, X = 100, 200, 400, 800,
       each counted once (enumerated once at 800 and pooled by trace).
  A_read = sum time * A / sum time;  log G_read = sum time * log G / sum time.

PLANTS AND CONTROLS (the condition's): PL1 constants; PL2 the clock without the frame (the closed form of the
time-weighted mean of (height - 1)^+); PL3 the table's points; PL4 W-F24 reproduced with its own sampler and seed;
PL5 the cusp law's path (log G = -Im tau). An extra control: the run radii taken from the thread's own ends agree with
W-P1c's closed() (W-P1c-F) on the words of (a) n = 20 (the first 200) and the classes of (b) with trace at most 100.
EXPECTED [J]: D0 to D7, as in the condition; each is printed with its verdict.
"""
import json
import math
import pathlib
import random
import time
from multiprocessing import get_context

import mpmath as mp
import numpy as np
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator

HERE = pathlib.Path(__file__).resolve().parent
RELAYS = HERE.parent
WP1C = RELAYS / "chat1_2026-11-18_wp1" / "wp1c_heights.py"
FIBRE = RELAYS / "chat1_2026-11-15_wf24" / "wf24_summary.json"

_src = WP1C.read_text()
exec(compile(_src[:_src.index("# H0: controls")], str(WP1C), "exec"))   # W-P1c's functions; computes nothing
DENS = 30
SWAP = str.maketrans("LR", "RL")
T0 = time.time()


def say(*a):
    print(*a, flush=True)


# ---------------- the table
_S = json.load(open(FIBRE))
FIB = _S["fibre"]
KEYS = ["%s|%s|%s" % (sec, rn, r) for sec in ("up", "down", "lep") for rn in ("S", "St") for r in ("r2", "r3")]
NK = len(KEYS)
XY = np.array([f["tau"] for f in FIB], dtype=float)
TA = np.array([[f["A"][k] for k in KEYS] for f in FIB])
TLG = np.array([[math.log(f["G"][k]) for k in KEYS] for f in FIB])
YTOP = float(XY[:, 1].max())
COLS = sorted(set(XY[:, 0].tolist()))
TRAP = np.array([0.5 if i in (0, len(COLS) - 1) else 1.0 for i in range(len(COLS))])
TRAP = TRAP / TRAP.sum()


def col_slopes(LA, LG, heights):
    """least-squares slope in Im tau of each column's log A and log G over the given heights: (11, 2 NK)"""
    out = np.zeros((len(COLS), 2 * NK))
    for i, x in enumerate(COLS):
        idx = [j for j in range(len(XY)) if XY[j, 0] == x and XY[j, 1] in heights]
        assert len(idx) == len(heights), (x, heights)
        out[i] = np.polyfit(XY[idx, 1], np.hstack([LA[idx], LG[idx]]), 1)[0]
    return out


H46 = (4.0, 5.0, 6.0)
H24 = (2.0, 2.5, 3.0, 3.5, 4.0)


class Field:
    def __init__(self, A, LG):
        V = np.hstack([A, LG])
        self.lin = LinearNDInterpolator(XY, V)
        self.near = NearestNDInterpolator(XY, V)
        self.slopes = {"T2": col_slopes(np.log(A), LG, H46), "T2b": col_slopes(np.log(A), LG, H24)}

    def base(self, x, y):
        P = np.column_stack([x, np.minimum(y, YTOP)])
        V = self.lin(P)
        bad = ~np.isfinite(V).all(axis=1)
        if bad.any():
            V[bad] = self.near(P[bad])
        return V

    def treat(self, V, x, y, t):
        """(A, log G) at the nodes under treatment t, from the clamped values V"""
        A, LG = V[:, :NK], V[:, NK:]
        if t == "T1":
            return A, LG
        hi = y > YTOP
        if not hi.any():
            return A, LG
        S = np.column_stack([np.interp(x[hi], COLS, self.slopes[t][:, j]) for j in range(2 * NK)])
        dy = (y[hi] - YTOP)[:, None]
        A, LG = A.copy(), LG.copy()
        A[hi] = np.exp(np.log(A[hi]) + S[:, :NK] * dy)
        LG[hi] = LG[hi] + S[:, NK:] * dy
        return A, LG


REAL = Field(TA, TLG)
CONST = Field(np.full_like(TA, 0.3), np.full_like(TLG, math.log(0.2)))
SYN = Field(TA, np.repeat(-XY[:, 1:2], NK, axis=1))
TREATS = ("T1", "T2", "T2b")


# ---------------- the threads (W-P1c's, with Re tau kept)
def reduce_xy(zr, zi):
    x, y = zr.copy(), zi.copy()
    for _ in range(200):
        x = x - np.round(x)
        m = x * x + y * y < 1 - 1e-13
        if not m.any():
            break
        d = x[m] * x[m] + y[m] * y[m]
        x[m], y[m] = -x[m] / d, y[m] / d
    return x, y


def runs(word):
    """the maximal cyclic runs: (start index, letter, length); W-P1c-F's"""
    n = len(word)
    k0 = next(i for i in range(n) if word[i] != word[i - 1])
    out, i = [], 0
    while i < n:
        k = (k0 + i) % n
        a = 1
        while a < n and word[(k + a) % n] == word[k]:
            a += 1
        out.append((k, word[k], a))
        i += a
    return out


def closed(word):
    """W-P1c-F's closed(): per run, (length a, rho), each rho from its own rotation's (or swapped word's) axis"""
    out = []
    for k, c, a in runs(word):
        w = word if c == "L" else word.translate(SWAP)
        y, x = ends(mat(w[k:] + w[:k]))
        out.append((a, float((x - y) / 2)))
    return out


def thread_xy(word):
    n = len(word)
    Ms = [mat(word)]
    for k in range(n - 1):
        A = L if word[k] == "L" else R
        Ms.append(mul(mul(inv(A), Ms[-1]), A))
    E = [ends(M) for M in Ms]
    q = [mp.mpc(0, mp.sqrt(-y * x)) for (y, x) in E]
    xs, ys, ws = [], [], []
    for k in range(n):
        y, x = E[k]
        A = L if word[k] == "L" else R
        p1, p2 = q[k], apply(A, q[(k + 1) % n])
        s1, c0, r = s_of(p1, y, x)
        s2, _, _ = s_of(p2, y, x)
        ln = s1 - s2
        assert ln > -mp.mpf(10) ** -40, ("piece order", word, k)
        m = max(8, int(float(ln) * DENS) + 1)
        s = float(s2) + (np.arange(m) + 0.5) / m * float(ln)
        th = 2 * np.arctan(np.exp(s))
        rx, ry = reduce_xy(float(c0) + float(r) * np.cos(th), float(r) * np.sin(th))
        xs.append(rx)
        ys.append(ry)
        ws.append(np.full(m, float(ln) / m))
    rho = []
    for k, c, a in runs(word):
        y, x = E[k]
        rho.append((a, float((x - y) / 2) if c == "L" else float((1 / x - 1 / y) / 2)))
    t = Ms[0][0][0] + Ms[0][1][1]
    return np.concatenate(xs), np.concatenate(ys), np.concatenate(ws), rho, float(2 * mp.acosh(mp.mpf(t) / 2)), t


# ---------------- one word's sums
# layout: 0 time, 1 length, 2 sum w y, 3 sum w (y-6)^+, 4 sum w (y-1)^+, 5 closed form of 4, 6 nodes, 7 trace;
# then per treatment (T1, T2, T2b): sum w A (NK), sum w log G (NK); then T2's sum w log G above 2, 4, 6 (3 NK);
# then CONST per treatment: sum w A (NK), sum w log G (NK); then SYN under T2: sum w log G (NK).
OFF_R = 8
OFF_SH = OFF_R + 6 * NK
OFF_C = OFF_SH + 3 * NK
OFF_P5 = OFF_C + 6 * NK
WIDTH = OFF_P5 + NK
SHARE_H = (2.0, 4.0, 6.0)


def word_stats(word):
    x, y, w, rho, ell, tr = thread_xy(word)
    out = np.zeros(WIDTH)
    out[0], out[1] = w.sum(), ell
    out[2] = w @ y
    out[3] = w @ np.maximum(y - 6.0, 0)
    out[4] = w @ np.maximum(y - 1.0, 0)
    out[5] = sum(2 * (r * math.acos(1 / r) - math.acosh(r)) for a, r in rho if r > 1)
    out[6], out[7] = len(y), tr
    V = REAL.base(x, y)
    for i, t in enumerate(TREATS):
        A, LG = REAL.treat(V, x, y, t)
        out[OFF_R + 2 * i * NK: OFF_R + (2 * i + 1) * NK] = w @ A
        out[OFF_R + (2 * i + 1) * NK: OFF_R + (2 * i + 2) * NK] = w @ LG
        if t == "T2":
            for j, h in enumerate(SHARE_H):
                out[OFF_SH + j * NK: OFF_SH + (j + 1) * NK] = (w * (y > h)) @ LG
    V = CONST.base(x, y)
    for i, t in enumerate(TREATS):
        A, LG = CONST.treat(V, x, y, t)
        out[OFF_C + 2 * i * NK: OFF_C + (2 * i + 1) * NK] = w @ A
        out[OFF_C + (2 * i + 1) * NK: OFF_C + (2 * i + 2) * NK] = w @ LG
    A, LG = SYN.treat(SYN.base(x, y), x, y, "T2")
    out[OFF_P5:OFF_P5 + NK] = w @ LG
    return out


def chunk_stats(words):
    return np.array([word_stats(w) for w in words])


def run_words(words, pool, size=100):
    chunks = [words[i:i + size] for i in range(0, len(words), size)]
    return np.vstack(pool.map(chunk_stats, chunks, chunksize=1))


# ---------------- read-outs from per-word sums
def shares(M):
    """under T2, the share of log G_read's sum that comes from above each of SHARE_H"""
    den = M[:, OFF_R + 3 * NK: OFF_R + 4 * NK].sum(0)
    return {h: M[:, OFF_SH + j * NK: OFF_SH + (j + 1) * NK].sum(0) / den for j, h in enumerate(SHARE_H)}


def readouts(M):
    tot = M[:, 0].sum()
    r = {}
    for i, t in enumerate(TREATS):
        r[t] = (M[:, OFF_R + 2 * i * NK: OFF_R + (2 * i + 1) * NK].sum(0) / tot,
                M[:, OFF_R + (2 * i + 1) * NK: OFF_R + (2 * i + 2) * NK].sum(0) / tot)
    return r


def boot_se(M, seed=7, B=1000):
    rng = np.random.default_rng(seed)
    n = len(M)
    acc = {t: ([], []) for t in ("T1", "T2")}
    for _ in range(B):
        idx = rng.integers(0, n, n)
        r = readouts(M[idx])
        for t in acc:
            acc[t][0].append(r[t][0])
            acc[t][1].append(r[t][1])
    return {t: (np.std(acc[t][0], axis=0, ddof=1), np.std(acc[t][1], axis=0, ddof=1)) for t in acc}


def geometry(M):
    tot, ell = M[:, 0].sum(), M[:, 1].sum()
    pl2 = abs(M[:, 4].sum() / tot - M[:, 5].sum() / ell) / (M[:, 5].sum() / ell)
    pl1 = 0.0
    for i in range(3):
        a = M[:, OFF_C + 2 * i * NK: OFF_C + (2 * i + 1) * NK].sum(0) / tot
        g = np.exp(M[:, OFF_C + (2 * i + 1) * NK: OFF_C + (2 * i + 2) * NK].sum(0) / tot)
        pl1 = max(pl1, float(np.abs(a - 0.3).max()), float(np.abs(g - 0.2).max()))
    ey = M[:, 2].sum() / tot
    pl5 = float(np.abs(M[:, OFF_P5:OFF_P5 + NK].sum(0) / tot + ey).max() / ey)
    return {"time": tot, "E_y": ey, "E_y6": M[:, 3].sum() / tot, "PL1": pl1, "PL2": pl2, "PL5": pl5,
            "nodes": int(M[:, 6].sum()), "words": len(M)}


# ---------------- W-F24's sampler (copied from wf24_run.py)
LM = np.array([[1, 1], [0, 1]])
RM = np.array([[1, 0], [1, 1]])


def reduce_fd(z):
    for _ in range(200):
        z = complex(z.real - math.floor(z.real + 0.5), z.imag)
        if abs(z) < 1 - 1e-12:
            z = -1 / z
        else:
            return z
    return z


def thread_nodes(word):
    W = np.eye(2, dtype=np.int64)
    for ch in word:
        W = W @ (LM if ch == "L" else RM)
    g = W.T
    a, b, c, d = [int(v) for v in g.ravel()]
    tr = a + d
    ell = 2 * math.acosh(abs(tr) / 2)
    disc = math.sqrt((d - a) ** 2 + 4 * b * c)
    r1, r2 = ((a - d) + disc) / (2 * c), ((a - d) - disc) / (2 * c)
    beta, betap = max(r1, r2), min(r1, r2)
    n = max(64, int(30 * ell))
    zs = [(beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1) for s in np.linspace(0, ell, n, endpoint=False)]
    return [reduce_fd(z) for z in zs], ell


def wf24_words():
    rng = random.Random(20261115)
    out = []
    for _ in range(1000):
        word = "".join(rng.choice("LR") for _ in range(40))
        if "L" not in word or "R" not in word:
            continue
        out.append(word)
    return out


def wf24_stats(word):
    zs, ell = thread_nodes(word)
    z = np.array(zs)
    x, y = z.real, z.imag
    w = np.full(len(z), ell / len(z))
    A, LG = REAL.treat(REAL.base(x, y), x, y, "T1")
    row = np.zeros(WIDTH)
    row[0] = w.sum()
    row[OFF_R:OFF_R + NK], row[OFF_R + NK:OFF_R + 2 * NK] = w @ A, w @ LG
    return row


def wf24_chunk(words):
    return np.array([wf24_stats(w) for w in words])


def words_a(n, seed):
    rng = np.random.default_rng(seed)
    words = []
    while len(words) < N_WORDS:
        w = "".join(rng.choice(["L", "R"], size=n))
        if len(set(w)) == 2:
            words.append(w)
    return words


def fmt(v, p=4):
    return "%.*g" % (p, v)


def main():
    out = {}
    say("W-P1d: frame C's read-outs under the two clocks. Data-free; the frame is W-F24's committed table.")
    say("table: %d points, top %.1f, %d columns; DENS %d" % (len(XY), YTOP, len(COLS), DENS))

    # D7 and the slopes
    s46, s24 = REAL.slopes["T2"], REAL.slopes["T2b"]
    sbar46, sbar24 = TRAP @ s46, TRAP @ s24
    d7 = bool((s46 < 0).all())
    say("D7 holds:", d7, "| column slopes over 4 to 6 above zero:", int((s46 >= 0).sum()), "of", s46.size)
    say("  slopes per unit of Im tau, mean over Re tau (trapezoid): log A over 4-6, log G over 4-6, log G over 2-4;"
        " log G over 4-6 min and max over the columns")
    for j, k in enumerate(KEYS):
        say("   %-12s %8.3f %8.3f %8.3f   [%8.3f, %8.3f]" % (k, sbar46[j], sbar46[NK + j], sbar24[NK + j],
                                                             s46[:, NK + j].min(), s46[:, NK + j].max()))
    hi = XY[:, 1] >= 4.0
    say("  table values at heights 4 to 6 below 1e-12: A %d, G %d (of %d each)"
        % (int((TA[hi] < 1e-12).sum()), int((np.exp(TLG[hi]) < 1e-12).sum()), TA[hi].size))
    out["slopes"] = {"T2": s46.tolist(), "T2b": s24.tolist(), "sbar_T2": sbar46.tolist(), "sbar_T2b": sbar24.tolist()}

    # PL3
    V = REAL.base(XY[:, 0], XY[:, 1])
    pl3 = max(float(np.abs(V[:, :NK] / TA - 1).max()), float(np.abs(V[:, NK:] - TLG).max()))
    say("PL3 holds:", pl3 < 1e-12, "| largest difference at the table's points: %.2g" % pl3)

    # the radii control
    ctl = words_a(20, 1)[:200] + [w for w in lyndon_words(100)]
    worst = 0.0
    for w in ctl:
        mine = [r for a, r in thread_xy(w)[3]]
        ref = [r for a, r in closed(w)]
        worst = max(worst, max(abs(p / q - 1) for p, q in zip(mine, ref)))
    say("radii control holds:", worst < 1e-12, "| %d words, largest relative difference %.2g" % (len(ctl), worst))

    with get_context("fork").Pool(2) as pool:
        # PL4: W-F24 reproduced
        ww = wf24_words()
        M24 = np.vstack(pool.map(wf24_chunk, [ww[i:i + 50] for i in range(0, len(ww), 50)], chunksize=1))
        r24 = readouts(M24)["T1"]
        ref_a = np.array([_S["A_read"][k] for k in KEYS])
        ref_g = np.array([_S["G_read"][k] for k in KEYS])
        pl4 = max(float(np.abs(r24[0] / ref_a - 1).max()), float(np.abs(np.exp(r24[1]) / ref_g - 1).max()))
        se24 = boot_se(M24)["T1"]
        say("PL4 holds:", pl4 < 1e-9, "| W-F24's words: %d; largest relative difference from its read-outs %.2g"
            % (len(ww), pl4))
        say("  [%.0f s]" % (time.time() - T0))

        # (a)
        RA, SE, GA = {}, {}, {}
        for n, seed in ((20, 1), (40, 2), (80, 3)):
            M = run_words(words_a(n, seed), pool)
            RA[n], GA[n] = readouts(M), geometry(M)
            if n in (40, 80):
                SE[n] = boot_se(M)
            if n == 40:
                sh_a = shares(M)
            g = GA[n]
            say("(a) n = %d: %d words, %d nodes; E[height] %.4f, E[(height - 6)+] %.3g; PL1 %.2g, PL2 %.2g, PL5 %.2g"
                % (n, g["words"], g["nodes"], g["E_y"], g["E_y6"], g["PL1"], g["PL2"], g["PL5"]),
                "[%.0f s]" % (time.time() - T0))

        # (b): enumerated once at 800, pooled by trace
        cls = lyndon_words(800)
        say("(b): %d classes with trace at most 800, %d letters  [%.0f s]"
            % (len(cls), sum(map(len, cls)), time.time() - T0))
        cls.sort(key=len, reverse=True)
        MB = run_words(cls, pool, size=50)
    say("  [%.0f s]" % (time.time() - T0))
    RB, GB = {}, {}
    for X in (100, 200, 400, 800):
        M = MB[MB[:, 7] <= X]
        RB[X], GB[X] = readouts(M), geometry(M)
        g = GB[X]
        say("(b) X = %d: %d classes, %d nodes; E[height] %.4f, E[(height - 6)+] %.4f; PL1 %.2g, PL2 %.2g, PL5 %.2g"
            % (X, g["words"], g["nodes"], g["E_y"], g["E_y6"], g["PL1"], g["PL2"], g["PL5"]))
        if X == 800:
            sh_b = shares(M)

    allg = list(GA.values()) + list(GB.values())
    say("PL1 holds:", max(g["PL1"] for g in allg) < 1e-12, "| PL2 holds:", max(g["PL2"] for g in allg) < 1e-3,
        "| PL5 holds:", max(g["PL5"] for g in allg) < 5e-3)

    # the read-outs
    say("")
    say("THE READ-OUTS (nothing is set beside a measured value). Per sector ratio: A_read, then G_read.")
    cols = [("a", 20), ("a", 40), ("a", 80), ("b", 100), ("b", 200), ("b", 400), ("b", 800)]
    for t in TREATS:
        say(" %s: columns (a) n = 20, 40, 80; (b) X = 100, 200, 400, 800" % t)
        for j, k in enumerate(KEYS):
            vals = [(RA if c == "a" else RB)[v][t] for c, v in cols]
            say("   %-12s A %s" % (k, " ".join("%9s" % fmt(r[0][j]) for r in vals)))
            say("   %-12s G %s" % ("", " ".join("%9s" % fmt(math.exp(r[1][j])) for r in vals)))
    say(" standard errors at n = 40 (T1, T2): A_read, log G_read")
    for j, k in enumerate(KEYS):
        say("   %-12s %8.2g %8.2g   %8.2g %8.2g" % (k, SE[40]["T1"][0][j], SE[40]["T1"][1][j], SE[40]["T2"][0][j],
                                                    SE[40]["T2"][1][j]))

    # the expectations
    say("")
    d0a = abs(GA[80]["E_y"] - GA[40]["E_y"]) < 0.02
    pred0 = 3 / math.pi * math.log(8)
    rise = GB[800]["E_y"] - GB[100]["E_y"]
    d0b = 0.75 * pred0 <= rise <= 1.25 * pred0
    say("D0 holds:", d0a and d0b, "| (a) E[height] at 40 and 80: %.4f, %.4f | (b) rise 100 to 800: %.4f against %.4f"
        % (GA[40]["E_y"], GA[80]["E_y"], rise, pred0))

    d1 = True
    for t in ("T1", "T2"):
        for q in (0, 1):
            se = np.sqrt(SE[40][t][q] ** 2 + SE[80][t][q] ** 2)
            d1 &= bool((np.abs(RA[80][t][q] - RA[40][t][q]) < 3 * se).all())
    dA = np.abs(RA[40]["T2"][0] / RA[40]["T1"][0] - 1).max()
    dG = np.abs(RA[40]["T2"][1] - RA[40]["T1"][1]).max()
    d1 &= bool(dA < 0.01 and dG < 0.01)
    say("D1 holds:", d1, "| T1 against T2 at n = 40: %.2g relative in A_read, %.2g in log G_read" % (dA, dG))

    z1 = np.abs(RA[40]["T1"][0] - r24[0]) / np.sqrt(SE[40]["T1"][0] ** 2 + se24[0] ** 2)
    z2 = np.abs(RA[40]["T1"][1] - r24[1]) / np.sqrt(SE[40]["T1"][1] ** 2 + se24[1] ** 2)
    say("D1b holds:", bool((z1 < 3).all() and (z2 < 3).all()),
        "| largest distance in combined standard errors: A %.2f, log G %.2f" % (z1.max(), z2.max()))

    d2 = True
    for q in (0, 1):
        d2 &= bool((np.abs(RB[800]["T1"][q] - RB[400]["T1"][q]) < np.abs(RB[200]["T1"][q] - RB[100]["T1"][q])).all())
    say("D2 holds:", d2)

    lg = {X: RB[X]["T2"][1] for X in (100, 200, 400, 800)}
    mono = bool(((lg[100] > lg[200]) & (lg[200] > lg[400]) & (lg[400] > lg[800])).all())
    fall = lg[100] - lg[800]
    pred = -3 / math.pi * sbar46[NK:] * math.log(8)
    ratio = fall / pred
    d3 = mono and bool(((ratio >= 0.75) & (ratio <= 1.25)).all())
    say("D3 holds:", d3, "| falls at each step:", mono)
    say("  per sector ratio: the fall of log G_read from X = 100 to 800 under T2, the law's (3/pi) |sbar| log 8, ratio")
    for j, k in enumerate(KEYS):
        say("   %-12s %8.3f %8.3f %6.3f" % (k, fall[j], pred[j], ratio[j]))

    d4 = True
    for t in ("T1", "T2"):
        d4 &= bool((np.abs(RB[800][t][0] / RB[400][t][0] - 1) < 0.02).all())
    c4 = [float(np.abs(RB[800][t][0] / RB[400][t][0] - 1).max()) for t in ("T1", "T2")]
    say("D4 holds:", d4, "| largest change of A_read from 400 to 800: T1 %.2g, T2 %.2g" % tuple(c4))

    d5 = all(bool((RB[800][t][0] < RA[40][t][0]).all()) for t in ("T1", "T2"))
    say("D5 holds:", d5)

    say("D6: per sector and reading, log G_read(r3) / log G_read(r2) under T2 at X = 100 and 800,"
        " and the slopes' ratio")
    d6 = True
    for sec in ("up", "down", "lep"):
        for rn in ("S", "St"):
            j2, j3 = KEYS.index("%s|%s|r2" % (sec, rn)), KEYS.index("%s|%s|r3" % (sec, rn))
            tgt = sbar46[NK + j3] / sbar46[NK + j2]
            q100, q800 = lg[100][j3] / lg[100][j2], lg[800][j3] / lg[800][j2]
            ok = abs(q800 - tgt) < abs(q100 - tgt)
            d6 &= ok
            qa = RA[40]["T2"][1][j3] / RA[40]["T2"][1][j2]
            say("   %-4s %-3s %7.3f %7.3f   slopes' ratio %7.3f   closer: %s   ((a) n = 40: %7.3f)"
                % (sec, rn, q100, q800, tgt, ok, qa))
    say("D6 holds:", d6)

    # reported
    say("")
    say("REPORTED. Under T2: the share of log G_read from above heights 2, 4, 6, at (a) n = 40 and (b) X = 800")
    for j, k in enumerate(KEYS):
        say("   %-12s (a) %s   (b) %s" % (k, " ".join("%6.3f" % sh_a[h][j] for h in SHARE_H),
                                          " ".join("%6.3f" % sh_b[h][j] for h in SHARE_H)))
    say("REPORTED. (b) at X = 800 over (a) at n = 40: A_read (T1, T2), G_read (T1, T2, T2b)")
    for j, k in enumerate(KEYS):
        say("   %-12s %8.3g %8.3g   %9.3g %9.3g %9.3g" % (
            k, RB[800]["T1"][0][j] / RA[40]["T1"][0][j], RB[800]["T2"][0][j] / RA[40]["T2"][0][j],
            math.exp(RB[800]["T1"][1][j] - RA[40]["T1"][1][j]), math.exp(RB[800]["T2"][1][j] - RA[40]["T2"][1][j]),
            math.exp(RB[800]["T2b"][1][j] - RA[40]["T2b"][1][j])))

    out["a"] = {str(n): {t: [RA[n][t][0].tolist(), RA[n][t][1].tolist()] for t in TREATS} for n in RA}
    out["b"] = {str(X): {t: [RB[X][t][0].tolist(), RB[X][t][1].tolist()] for t in TREATS} for X in RB}
    out["se"] = {str(n): {t: [SE[n][t][0].tolist(), SE[n][t][1].tolist()] for t in SE[n]} for n in SE}
    out["geometry"] = {"a": {str(n): GA[n] for n in GA}, "b": {str(X): GB[X] for X in GB}}
    out["wf24"] = {"readouts": [r24[0].tolist(), r24[1].tolist()], "se": [se24[0].tolist(), se24[1].tolist()]}
    out["keys"] = KEYS
    out["verdicts"] = {"PL3": pl3 < 1e-12, "PL4": pl4 < 1e-9, "D0": d0a and d0b, "D1": d1, "D2": d2, "D3": d3,
                       "D4": d4, "D5": d5, "D6": d6, "D7": d7}
    json.dump(out, open(HERE / "wp1d_summary.json", "w"), indent=1,
              default=lambda v: bool(v) if isinstance(v, np.bool_) else float(v))
    say("done  [%.0f s]" % (time.time() - T0))


if __name__ == "__main__":
    main()
