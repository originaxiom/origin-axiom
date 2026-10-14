"""The locus, by thread (chat1, 2026-10-14, evening). An exact classification and read-outs; no prediction, so no seal.

B1651 (main; sealed at 6d6f7f660, not yet run) asks where a Higgs can couple the zero modes and whether anything forces
the puncture. Under its premise P1 (an even Higgs at a single point) it couples only at the elliptic involution's four
fixed points: the puncture and the three half-periods. Its covariance analysis has two frames: at one tau (F1) nothing
is imposed; in the surface frame (F2) the covariant loci are the puncture, the half-period orbit, and both.

In the thread frame (H-thread; FINDINGS_THREAD_FRAME.md) a vacuum is a thread W: tau runs once around W's closed
geodesic, and the fibre torus comes back to itself through W's monodromy, which fixes the puncture and permutes the
half-periods through W mod 2 in SL(2, F_2) = S_3 (B1600's parities; B1602's classes A4 / D4 / V4). A field supported
at one point of each fibre is single-valued on the vacuum's mapping torus only if the monodromy fixes that point (the
SM seat's principle: "a label the grammar reads is single-valued on a state only where the act fixes it"). So:
  odd trace       (a 3-cycle on the half-periods; B1602's A4): none fixed  -> 1 single-point locus, the puncture;
  even trace, W != I mod 2 (a transposition; D4):              one fixed   -> 2 loci;
  W = I mod 2     (Gamma(2); V4):                              all fixed   -> 4 loci.
The fibrewise elliptic involution of the mapping torus fixes the half-periods' sweep: 1 closed curve meeting each fibre
three times (A4), 2 curves (D4: one meets each fibre once, one twice), 3 curves (V4).

What this script computes (exact integer arithmetic for the classes; floats only for the weights):
  E1  the class of every Lyndon word of length 2..18 under both letter conventions (they must agree), and B1600's
      parity lemma (odd trace <=> order 3 mod 2) on all of them;
  E2  the census to length 8 up to mirror (L <-> R), against B1602's 16 / 13 / 8 (unsigned; its 74 signed threads);
  R1  the class beside m2/m3 for every thread computed in the thread frame (lagrange_law.json, post_hoc_long_words.json);
  R2  the weave's weight in each class under T-ROOT's measure (t_root_threads.json: 31,040 threads to length 18),
      exp(-c Vol / 6 pi) times (A) 2^-n, (B) 3^-n, (C) 1/(n(n-1)L(n)), on T-ROOT's grid of c.

Run once:  python3 -B locus_by_thread.py > locus_by_thread_run.txt 2>&1   (writes locus_by_thread.json beside itself)
"""
import json, math, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SCALE = HERE.parent / "chat1_2026-10-14_the_scale"
GRID = [0.5, 1, 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]


def lyndon(n, alphabet="LR"):                     # Duval, as in t_root.py
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1
        m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n:
            w.append(w[len(w) - m])
        while w and w[-1] == k - 1:
            w.pop()


def mat(word, conv):
    L, R = ((1, 0), (1, 1)), ((1, 1), (0, 1))
    if conv == 1:                                 # B1651 / B1600: L is tau -> tau + 1, R is tau -> tau/(tau + 1)
        L, R = R, L
    a, b, c, d = 1, 0, 0, 1
    for ch in word:
        (p, q), (r, s) = L if ch == "L" else R
        a, b, c, d = a * p + b * r, a * q + b * s, c * p + d * r, c * q + d * s
    return a, b, c, d


def klass(word, conv=0):
    a, b, c, d = mat(word, conv)
    tr = a + d
    m2 = (a % 2, b % 2, c % 2, d % 2)
    fixed = sum(1 for v in ((1, 0), (0, 1), (1, 1))
                if ((m2[0] * v[0] + m2[1] * v[1]) % 2, (m2[2] * v[0] + m2[3] * v[1]) % 2) == v)
    if tr % 2:
        k = "A4"
    elif m2 == (1, 0, 0, 1):
        k = "V4"
    else:
        k = "D4"
    # order of W mod 2
    e, o = (1, 0, 0, 1), 0
    while True:
        o += 1
        e = ((e[0] * m2[0] + e[1] * m2[2]) % 2, (e[0] * m2[1] + e[1] * m2[3]) % 2,
             (e[2] * m2[0] + e[3] * m2[2]) % 2, (e[2] * m2[1] + e[3] * m2[3]) % 2)
        if e == (1, 0, 0, 1):
            break
    return k, fixed, o, tr


def canon(word):                                  # least rotation
    return min(word[i:] + word[:i] for i in range(len(word)))


def mirror(word):
    return canon(word.translate(str.maketrans("LR", "RL")))


LOCI = {"A4": 1, "D4": 2, "V4": 4}
CURVES = {"A4": [3], "D4": [1, 2], "V4": [1, 1, 1]}
out = {"status": "exact classification and read-outs; no prediction (chat1, 2026-10-14)"}

# ------------------------------------------------------------------ E1
words = [w for w in lyndon(18) if len(w) >= 2]
cls = {}
bad_conv, bad_lemma, bad_fixed = [], [], []
for w in words:
    k0, f0, o0, t0 = klass(w, 0)
    k1, f1, o1, t1 = klass(w, 1)
    if (k0, f0, o0) != (k1, f1, o1) or t0 != t1:
        bad_conv.append(w)
    if (t0 % 2 == 1) != (o0 == 3):
        bad_lemma.append(w)
    if f0 != {"A4": 0, "D4": 1, "V4": 3}[k0]:
        bad_fixed.append(w)
    cls[w] = k0
out["E1"] = {"n_words": len(words), "conventions_disagree": bad_conv[:10], "parity_lemma_fails": bad_lemma[:10],
             "fixed_count_mismatch": bad_fixed[:10],
             "holds": not bad_conv and not bad_lemma and not bad_fixed}
by_len = {}
for w in words:
    by_len.setdefault(len(w), {"A4": 0, "D4": 0, "V4": 0})[cls[w]] += 1
out["E1"]["census by length (Lyndon words)"] = by_len
tot = {"A4": 0, "D4": 0, "V4": 0}
for w in words:
    tot[cls[w]] += 1
out["E1"]["census to length 18"] = tot

# ------------------------------------------------------------------ E2
seen, upto = set(), {"A4": 0, "D4": 0, "V4": 0}
mir_disagree = []
for w in words:
    if len(w) > 8:
        continue
    m = mirror(w)
    if cls[m] != cls[w]:
        mir_disagree.append([w, m])
    key = min(w, m)
    if key in seen:
        continue
    seen.add(key)
    upto[cls[w]] += 1
out["E2"] = {"classes to length 8 up to mirror": upto, "n": len(seen), "B1602 (signed / 2)": {"A4": 16, "D4": 13, "V4": 8},
             "mirror changes the class": mir_disagree[:10], "agrees": upto == {"A4": 16, "D4": 13, "V4": 8}}

# ------------------------------------------------------------------ R1
ll = json.loads((HERE / "lagrange_law.json").read_text())["readouts"]["per thread"]
lw = json.loads((HERE / "post_hoc_long_words.json").read_text())
rows = []
for w, r in sorted(ll.items(), key=lambda kv: kv[1]["y_max"]):
    k, f, o, tr = klass(w)
    rows.append({"thread": w, "class": k, "trace": tr, "single-point loci": LOCI[k], "half-period curves": CURVES[k],
                 "y_max": r["y_max"], "m2/m3": r["m2/m3"], "m1/m3": r["m1/m3"], "admitted": r["admitted"],
                 "CS": r["CS"], "source": "lagrange_law.json"})
for w, r in lw.items():
    k, f, o, tr = klass(w)
    rows.append({"thread": w, "class": k, "trace": tr, "single-point loci": LOCI[k], "half-period curves": CURVES[k],
                 "y_max": r["y_max"], "m2/m3": r["m2/m3"], "m1/m3": r["m1/m3"], "admitted": None, "CS": None,
                 "source": "post_hoc_long_words.json"})
out["R1"] = rows
adm = [r for r in rows if r["admitted"]]
out["R1 summary"] = {k: {"n admitted": sum(1 for r in adm if r["class"] == k),
                         "m2/m3 range": [min((r["m2/m3"] for r in adm if r["class"] == k), default=None),
                                         max((r["m2/m3"] for r in adm if r["class"] == k), default=None)]}
                     for k in ("A4", "D4", "V4")}

# ------------------------------------------------------------------ R2
thr = json.loads((SCALE / "t_root_threads.json").read_text())
tw = list(thr.keys())
L_of_n = {}
for w in words:
    L_of_n[len(w)] = L_of_n.get(len(w), 0) + 1
n_arr = np.array([len(w) for w in tw], dtype=float)
vol = np.array([thr[w][0] for w in tw])
kk = np.array([cls[w] for w in tw])
iroot = tw.index("LR")
logw = {"A": -n_arr * math.log(2), "B": -n_arr * math.log(3),
        "C": np.array([-math.log(len(w) * (len(w) - 1) * L_of_n[len(w)]) for w in tw])}
shares = {}
for key in ("A", "B", "C"):
    shares[key] = {}
    for c in GRID:
        e = logw[key] - c * vol / (6 * math.pi)
        q = np.exp(e - e.max()); q /= q.sum()
        shares[key][str(c)] = {"A4": float(q[kk == "A4"].sum()), "D4": float(q[kk == "D4"].sum()),
                               "V4": float(q[kk == "V4"].sum()), "root": float(q[iroot]),
                               "A4 without the root": float(q[kk == "A4"].sum() - q[iroot])}
out["R2"] = {"n_threads": len(tw), "shares": shares,
             "note": "A4 share = the weave's weight in vacua where P1 forces the puncture (given H-thread)"}

(HERE / "locus_by_thread.json").write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps({k: out[k] for k in ("E1", "E2", "R1 summary")}, indent=1))
print("R2 at c = 6:", json.dumps({k: out["R2"]["shares"][k]["6"] for k in ("A", "B", "C")}, indent=1))
print("R2 at c = 24:", json.dumps({k: out["R2"]["shares"][k]["24"] for k in ("A", "B", "C")}, indent=1))
print("\nR1 (admitted, by height):")
for r in rows:
    if r["admitted"] or r["source"] != "lagrange_law.json":
        print(f"  {r['thread']:<28} {r['class']}  loci {r['single-point loci']}  y {r['y_max']:.4f}  "
              f"m2/m3 {r['m2/m3']:.4g}  m1/m3 {r['m1/m3']:.3g}  [{r['source'].split('.')[0]}]")
