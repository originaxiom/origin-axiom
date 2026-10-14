"""W86, POST HOC (labelled; written after the read-out of the_chat1_record_checked.json, committed before its one run).

I6's sub-check "no D4 thread has Lagrange value below 3" failed on an instrument error in this seat's script, not in
chat1's record: `lagrange()` took sqrt(tr^2 - 4)/|c| at the rotation with the least |c|. That is the diameter of one
lift's semicircle, not the closed geodesic's highest arc (it gives 2*sqrt(3)/2 = 1.73 for LLR, whose Lagrange value is
2 sqrt 3 = 3.46, as W84's sampled y_max = 1.7321 already shows). This script re-scores the sub-checks that used it.

  PH1  the Lagrange value of every thread to length 10 by Perron's formula: the maximum over the cyclic sequence of run
       lengths (a_i) of [a_i; a_{i+1}, a_{i+2}, ...] + [0; a_{i-1}, a_{i-2}, ...], each a periodic continued fraction
       summed to 60 digits; cross-checked against twice the highest point of the geodesic reduced into the standard
       fundamental domain (W84's reduce_tau), sampled at 4000 nodes, on every thread to length 8
  PH2  re-scored: the least Lagrange value among the D4 threads to length 8 (and to length 10), and whether it is >= 3;
       LLRR's Lagrange value against sqrt 8; L^n R's against sqrt(n^2 + 4n) (W84's formula), n = 1..8

Run: python3 the_chat1_record_checked_posthoc.py  ->  the_chat1_record_checked_posthoc.json beside it.
"""
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_chat1_record_checked as RC  # noqa: E402  (lyndon_upto, klass, lr, swap)
import the_thread_frame_checked as TF  # noqa: E402  (word_matrix, reduce_tau)

OUT = HERE / "the_chat1_record_checked_posthoc.json"
mp.mp.dps = 60


def runs(w):
    """the cyclic run lengths of a word with both letters, starting at a run boundary"""
    k = next(i for i in range(len(w)) if w[i] != w[i - 1])
    v = w[k:] + w[:k]
    out, cur = [], 1
    for i in range(1, len(v)):
        if v[i] == v[i - 1]:
            cur += 1
        else:
            out.append(cur)
            cur = 1
    out.append(cur)
    return out


def periodic_cf(seq, start, step, terms=400):
    """[a_start; a_{start+step}, a_{start+2 step}, ...] for the periodic sequence seq, evaluated from the tail"""
    n = len(seq)
    x = mp.mpf(0)
    for j in range(terms, 0, -1):
        x = 1 / (seq[(start + j * step) % n] + x)
    return seq[start % n] + x


def perron(w):
    a = runs(w)
    best = mp.mpf(0)
    for i in range(len(a)):
        alpha = periodic_cf(a, i, 1)
        beta = periodic_cf(a, i - 1, -1)
        best = max(best, alpha + 1 / beta)
    return best


def sampled(w, N=4000):
    (a, b), (c, d) = TF.word_matrix(w)
    tr = a + d
    x0 = mp.mpf(a - d) / (2 * c)
    rho = mp.sqrt(tr * tr - 4) / (2 * abs(c))
    P = 2 * mp.acosh(mp.mpf(tr) / 2)
    ymax = mp.mpf(0)
    for j in range(N):
        s = -P / 2 + (j + mp.mpf(1) / 2) * P / N
        t = TF.reduce_tau(x0 + rho * (mp.tanh(s) + mp.mpc(0, 1) / mp.cosh(s)))
        ymax = max(ymax, t.imag)
    return 2 * ymax


def main():
    mp.mp.dps = 30
    t8 = RC.lyndon_upto(8)
    t10 = RC.lyndon_upto(10)
    lag = {w: perron(w) for w in t10}
    worst = mp.mpf(0)
    for w in t8:
        worst = max(worst, abs(sampled(w) - lag[w]) / lag[w])
    d4_8 = min((lag[w], w) for w in t8 if RC.klass(w) == "D4")
    d4_10 = min((lag[w], w) for w in t10 if RC.klass(w) == "D4")
    least = {k: min((lag[w], w) for w in t8 if RC.klass(w) == k) for k in ("A4", "D4", "V4")}
    lnr = {n: float(abs(lag["L" * n + "R"] - mp.sqrt(n * n + 4 * n))) for n in range(1, 9)}
    out = {"status": "W86 post hoc (labelled): the Lagrange values re-scored with Perron's formula",
           "PH1": {"threads to length 10": len(t10),
                   "sampled height against Perron, worst relative (to length 8, 4000 nodes)": float(worst),
                   "holds": bool(worst < 1e-5)},
           "PH2": {"least D4 Lagrange value to length 8": [float(d4_8[0]), d4_8[1]],
                   "least D4 Lagrange value to length 10": [float(d4_10[0]), d4_10[1]],
                   "least Lagrange value per class to length 8": {k: [float(v[0]), v[1]] for k, v in least.items()},
                   "LLRR against sqrt 8": float(abs(lag["LLRR"] - mp.sqrt(8))),
                   "L^n R against sqrt(n^2 + 4n), n = 1..8": lnr,
                   "no D4 thread below 3 (to length 8)": bool(d4_8[0] >= 3),
                   "no D4 thread below 3 (to length 10)": bool(d4_10[0] >= 3)},
           "Lagrange values to length 8": {w: float(lag[w]) for w in t8}}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)
    print(json.dumps({k: out[k] for k in ("PH1", "PH2")}, indent=1))


if __name__ == "__main__":
    main()
