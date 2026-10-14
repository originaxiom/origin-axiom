"""Read-outs for the meditation of 2026-10-14 (night). Labelled POST HOC; no prediction is scored. Exact where stated.

M1  The Rademacher function. For every Lyndon word to length 12 (thread_frame.py's convention: L = [[1,0],[1,1]],
    R = [[1,1],[0,1]]), Psi(A) = Phi(A) - 3 sign(c(a+d)), with Rademacher's Phi(A) = (a+d)/c - 12 sign(c) s(d,|c|)
    (the form in docs/RECOGNITION.md R1; s the Dedekind sum), computed in exact rationals on every rotation.
    Read-out: is Psi constant on rotations, and is it #L - #R or #R - #L? (Literature: Ghys, link(knot_A, trefoil) =
    Psi(A); the eta multiplier nu_{1/2}(A) = exp(i pi Psi(A)/12); Psi = alternating sum of partial quotients.)
M2  The two faces over T-ROOT's 31,040 threads to length 18: syllables (R-runs), the longest run, the exact Lagrange
    value of the periodic cutting sequence, and the volume (t_root_threads.json). Spearman correlations. On the 59
    admitted thread-frame threads (lagrange_law.json): ln(m2/m3) against the height, the volume and the syllables,
    and the partial correlation with the volume at fixed height.
M3  The minimal thread in each mod-2 class (A4: odd trace; D4: odd length; V4: W = I mod 2) by volume, by Lagrange
    value and by trace.
M4  The weave's weight by height band, for all threads and per class, at c = 6 and c = 24 under T-ROOT's weights
    (A) 2^-n, (B) 3^-n, (C) 1/(n(n-1)L(n)); bands: Lagrange < 3 (Markov), 3 to 3.6, above 3.6.

Run once:  python3 -B meditation_checks.py > meditation_checks_run.txt 2>&1   (writes meditation_checks.json)
"""
import json, math, pathlib
from fractions import Fraction
import numpy as np
from scipy.stats import spearmanr

HERE = pathlib.Path(__file__).resolve().parent
SEL = HERE.parent / "chat1_2026-10-14_selection"
SCALE = HERE.parent / "chat1_2026-10-14_the_scale"
GRID = [6, 24]
out = {"status": "post hoc read-outs (labelled), for the meditation of 2026-10-14; no prediction"}


def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()


def mat(word):
    a, b, c, d = 1, 0, 0, 1
    for ch in word:
        (p, q), (r, s) = ((1, 0), (1, 1)) if ch == "L" else ((1, 1), (0, 1))
        a, b, c, d = a * p + b * r, a * q + b * s, c * p + d * r, c * q + d * s
    return a, b, c, d


def saw(x):
    return Fraction(0) if x.denominator == 1 else x - (x.numerator // x.denominator) - Fraction(1, 2)


def dedekind(h, k):
    return sum((saw(Fraction(r, k)) * saw(Fraction(h * r, k)) for r in range(1, k)), Fraction(0))


def sgn(x):
    return (x > 0) - (x < 0)


def Psi(a, b, c, d):
    if c == 0:
        phi = Fraction(b, d)
    else:
        phi = Fraction(a + d, c) - 12 * sgn(c) * dedekind(d, abs(c))
    return phi - 3 * sgn(c * (a + d))


# ------------------------------------------------------------------ M1
m1_rows, bad_rot, conv = [], [], {"#L-#R": 0, "#R-#L": 0, "neither": 0}
for w in (w for w in lyndon(12) if len(w) >= 2):
    vals = {Psi(*mat(w[k:] + w[:k])) for k in range(len(w))}
    if len(vals) != 1:
        bad_rot.append([w, [str(v) for v in vals]])
    v = next(iter(vals))
    nl, nr = w.count("L"), w.count("R")
    if v == nl - nr: conv["#L-#R"] += 1
    elif v == nr - nl: conv["#R-#L"] += 1
    else: conv["neither"] += 1
    if len(w) <= 4 or w in ("LLRLR", "LLRRLR", "LLLRLRR"):
        m1_rows.append([w, str(v), nl - nr])
out["M1"] = {"rotation-invariance failures": bad_rot[:10], "convention counts": conv, "examples [word, Psi, #L-#R]": m1_rows}
print("M1", json.dumps(out["M1"]))

# ------------------------------------------------------------------ M2
thr = json.loads((SCALE / "t_root_threads.json").read_text())
words = list(thr)


def runs(w):                                   # cyclic run lengths, starting at an L-run
    k = 0
    while w[k] == w[k - 1]: k += 1
    u = w[k:] + w[:k]
    rl, cur, n = [], u[0], 0
    for ch in u:
        if ch == cur: n += 1
        else: rl.append(n); cur, n = ch, 1
    rl.append(n)
    return rl


def cf(seq):                                   # [a0; a1, a2, ...] for a long finite list
    x = 0.0
    for a in reversed(seq[1:]):
        x = 1.0 / (a + x)
    return seq[0] + x


def lagrange(w):
    a = runs(w); n = len(a); rep = 60 // n + 4
    best = 0.0
    for i in range(n):
        fwd = [a[(i + j) % n] for j in range(n * rep)]
        bwd = [a[(i - 1 - j) % n] for j in range(n * rep)]
        best = max(best, cf(fwd) + 1.0 / cf(bwd))
    return best


def klass(w):
    a, b, c, d = mat(w)
    if (a + d) % 2: return "A4"
    return "V4" if (a % 2, b % 2, c % 2, d % 2) == (1, 0, 0, 1) else "D4"


syl = np.array([len(runs(w)) // 2 for w in words])
mrun = np.array([max(runs(w)) for w in words])
lag = np.array([lagrange(w) for w in words])
vol = np.array([thr[w][0] for w in words])
n_arr = np.array([len(w) for w in words])
cls = np.array([klass(w) for w in words])
tr = np.array([sum(mat(w)[i] for i in (0, 3)) for w in words])
sp = lambda x, y: float(spearmanr(x, y).correlation)
out["M2 weave"] = {"Spearman(Vol, syllables)": sp(vol, syl), "Spearman(Vol, longest run)": sp(vol, mrun),
                   "Spearman(Vol, Lagrange)": sp(vol, lag), "Spearman(Lagrange, longest run)": sp(lag, mrun),
                   "Spearman(Lagrange, syllables)": sp(lag, syl)}
ll = json.loads((SEL / "lagrange_law.json").read_text())["readouts"]["per thread"]
adm = [w for w, r in ll.items() if r["admitted"]]
lm = np.array([math.log(ll[w]["m2/m3"]) for w in adm])
y_tf = np.array([ll[w]["y_max"] for w in adm])
v_tf = np.array([ll[w]["Vol"] for w in adm])
s_tf = np.array([len(runs(w)) // 2 for w in adm])
lag_tf = np.array([lagrange(w) for w in adm])
rx = lambda x, z: x - np.polyval(np.polyfit(z, x, 1), z)
out["M2 thread frame (59 admitted)"] = {
    "max |Lagrange/2 - sampled y_max|": float(np.max(np.abs(lag_tf / 2 - y_tf))),
    "Spearman(ln m2/m3, Lagrange)": sp(lm, lag_tf), "Spearman(ln m2/m3, Vol)": sp(lm, v_tf),
    "Spearman(ln m2/m3, syllables)": sp(lm, s_tf),
    "partial Pearson(ln m2/m3, Vol | Lagrange)": float(np.corrcoef(rx(lm, lag_tf), rx(v_tf, lag_tf))[0, 1])}
print("M2", json.dumps({k: out[k] for k in ("M2 weave", "M2 thread frame (59 admitted)")}, indent=1))

# ------------------------------------------------------------------ M3
m3 = {}
for k in ("A4", "D4", "V4"):
    idx = np.where(cls == k)[0]
    m3[k] = {"min Vol": [words[idx[np.argmin(vol[idx])]], float(vol[idx].min())],
             "min Lagrange": [words[idx[np.argmin(lag[idx])]], float(lag[idx].min())],
             "min trace": [words[idx[np.argmin(tr[idx])]], int(tr[idx].min())]}
out["M3"] = m3
print("M3", json.dumps(m3, indent=1))

# ------------------------------------------------------------------ M4
L_of_n = {}
for w in words: L_of_n[len(w)] = L_of_n.get(len(w), 0) + 1
logw = {"A": -n_arr * math.log(2), "B": -n_arr * math.log(3),
        "C": np.array([-math.log(len(w) * (len(w) - 1) * L_of_n[len(w)]) for w in words])}
bands = {"Lagrange < 3": lag < 3 - 1e-9, "3 to 3.6": (lag >= 3 - 1e-9) & (lag < 3.6), "above 3.6": lag >= 3.6}
m4 = {}
for key in ("A", "B", "C"):
    m4[key] = {}
    for c in GRID:
        e = logw[key] - c * vol / (6 * math.pi); q = np.exp(e - e.max()); q /= q.sum()
        row = {b: float(q[mask].sum()) for b, mask in bands.items()}
        for k in ("A4", "D4", "V4"):
            row[k] = {b: float(q[mask & (cls == k)].sum()) for b, mask in bands.items()}
        m4[key][str(c)] = row
out["M4"] = m4
print("M4 c=6", json.dumps({k: m4[k]["6"] for k in m4}, indent=1))
(HERE / "meditation_checks.json").write_text(json.dumps(out, indent=1) + "\n")
