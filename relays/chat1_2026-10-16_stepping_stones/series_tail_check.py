"""The stored series' high coefficients, and whether the thread frame's masses feel them (an instrument check; no data).

A referee of canonical_cusp_norm.py found that forms.pkl's coefficients stop following their expected growth near
the top of the stored range. This measures it and tests its effect.
1. For each stored series and component: the growth excess, ln|c_n| - 4 pi sqrt(|p| n / 64) for a series whose
   lowest exponent q^(p/8) is negative (its leading growth), and ln|c_n| - 2 ln n for a cusp form (polynomial growth),
   relative to its median over 40 <= n <= 130, at the top exponents;
   and |Im c| / |Re c| by exponent (the true coefficients are real in this basis: below q^(100/8) the imaginary parts
   are 1e-39 to 1e-20 of the real ones).
   At y = sqrt(3)/2, the lowest height any instrument here evaluates them at, the size of the kept terms' imaginary
   parts and of the terms above q^(140/8).
2. Two mid-height classes (midheight_scan.py's jobs 0 and 6: the highest, h = 5.93, and one at h = 4.56) recomputed
   with every series cut at q^(140/8), by the same instrument, and compared with the scan's masses.
Usage: python3 -B series_tail_check.py <forms.pkl> > series_tail_check_run.txt   (needs midheight_scan.json beside it,
decompressed from midheight_scan.json.xz)
"""
import hashlib, json, math, os, pickle, sys
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import midheight_scan as M

P = pickle.load(open(sys.argv[1], "rb"))
print(f"forms.pkl sha256 {hashlib.sha256(open(sys.argv[1], 'rb').read()).hexdigest()}")
is_series = lambda s: isinstance(s, dict) and s and all(isinstance(k, tuple) and len(k) == 2 for k in s)
named = []
for k, v in P.items():
    if is_series(v):
        named.append((k, v))
    elif isinstance(v, list) and v and all(is_series(x) for x in v):
        named += [(f"{k}[{i}]", x) for i, x in enumerate(v)]

print("1. growth excess at the top exponents (e-folds above the series' own trend), and |Im c|/|Re c|")
top = []
for name, s in named:
    p = min(n for (_, n) in s)
    trend = (lambda n: 4 * math.pi * math.sqrt(abs(p) * n / 64)) if p < 0 else (lambda n: 2 * math.log(n))
    by = {}
    for (l, n), a in s.items():
        c = complex(mp.mpc(a))
        if n > 0 and c != 0:
            by.setdefault(l, []).append((n, math.log(abs(c)) - trend(n),
                                         abs(c.imag) / max(abs(c.real), 1e-300)))
    for l, arr in sorted(by.items()):
        arr.sort()
        base = sorted(e for n, e, _ in arr if 40 <= n <= 130)
        if not base:
            continue
        b = base[len(base) // 2]
        first = next((n for n, e, _ in arr if n > 130 and e - b > 0.5), None)
        hi = arr[-1]
        top.append((hi[1] - b, name, l, hi[0]))
        ir = {n: q for n, _, q in arr}
        ns = sorted(ir)
        pick = sorted({next(n for n in ns if n >= t) for t in (1, 60, 120, 140, 160, 200) if any(n >= t for n in ns)} | {ns[-1]})
        print(f"  {name:8s} {l:3s} lowest exponent {p:+d}/8: first exponent > e^0.5 above trend q^({first}/8); "
              f"at q^({hi[0]}/8) e^{hi[1] - b:.1f} above; Im/Re " + ", ".join(f"q^({n}/8) {ir[n]:.0e}" for n in pick))
top.sort(reverse=True)
print(f"  largest excess at the top exponent: e^{top[0][0]:.1f} ({top[0][1]} {top[0][2]}, q^({top[0][3]}/8))")
y0 = math.sqrt(3) / 2
wk = wt = 0.0
for name, s in named:
    terms = [(n, complex(mp.mpc(a)), math.exp(-2 * math.pi * y0 * n / 8)) for (_, n), a in s.items()]
    lead = max(abs(c) * w for n, c, w in terms)
    wk = max(wk, sum(abs(c.imag) * w for n, c, w in terms if n <= 140) / lead)
    wt = max(wt, sum(abs(c) * w for n, c, w in terms if n > 140) / lead)
print(f"  at y = sqrt(3)/2, relative to each series' largest term: the kept terms' imaginary parts (up to q^(140/8)) sum "
      f"to at most {wk:.1e}; the terms above q^(140/8) to at most {wt:.1e}")


def cut(s):
    return {k: v for k, v in s.items() if k[1] <= 140}


PT = {}
for k, v in P.items():
    if is_series(v):
        PT[k] = cut(v)
    elif isinstance(v, list) and v and all(is_series(x) for x in v):
        PT[k] = [cut(x) for x in v]
    else:
        PT[k] = v
print("2. the masses with every series cut at q^(140/8), against the scan's")
recs = json.load(open(os.path.join(HERE, "midheight_scan.json")))["records"]
jobs = M.jobs_list()
for idx in (0, 6):
    job, rec = jobs[idx], recs[idx]
    assert rec["index"] == idx and rec["word"] == job["word"]
    r = M.one((job, PT))
    worst, smallest = 0.0, 1.0
    for key, c in rec["cells"].items():
        d = r["cells"].get(key)
        if c is None or d is None:
            continue
        smallest = min(smallest, min(c["s"]) / max(c["s"]))
        worst = max(worst, max(abs(math.log(a / b)) for a, b in zip(c["s"], d["s"])))
    print(f"  class {idx}: N={job['N']} {job['word']} h={job['height']:.3f}: point counts {rec['npp']} (scan) and "
          f"{r['npp']} (cut); largest |d ln s| {worst:.1e} over {len(rec['cells'])} assignment-cells; smallest s1/s3 "
          f"{smallest:.1e}", flush=True)
