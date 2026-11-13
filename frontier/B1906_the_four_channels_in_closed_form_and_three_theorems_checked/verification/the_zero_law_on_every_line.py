"""B1906, check E5: the zero law of det M (P-337, with P-292 and P-268; Theorem E's fourth corollary), on every line of order 1-12,
three sectors, with B1716's own instrument (B1656's bilinear, its residues and its regularised norms, numpy route).

Main's derivation (the_duplication_identity.py): K_s = P_s/R_s depends only on c_s = 3w + h_s' (the channel's
characteristic mod Z^2), so its regularised norm is a function A(c_s).
  - u -> -u gives A(c) = A(-c) at every tau.
  - at Re tau = 0, u -> conj(u) gives A(a, b) = A(-a, b), so A is invariant under (+-a, +-b).
Group the channels with non-zero residue by the classes of that symmetry (the pairs {c, -c} at generic tau; the orbits of
(+-a, +-b) at Re tau = 0): D = sum_k A_k S_k with S_k = sum over the class of R_s^2, and sum_k S_k = 0 (Z2). So D = 0 if
every S_k = 0 (one class is always enough). PREDICTION, written before the census is run: at generic distinct A_k, D = 0
exactly where every S_k = 0, and nowhere else.
The census computes D directly from the norms (it does not assume the symmetry) and compares; it also measures how equal
the norms within a class are.  No data, no physical quantity.   OMP_NUM_THREADS=1 python3 -B the_zero_law_on_every_line.py"""
import sys, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]                                   # verification -> the arc -> frontier -> the root
sys.path.insert(0, str(ROOT / "frontier" / "B1716_the_zeros_derived" / "verification"))
_argv = sys.argv; sys.argv = ["x"]
import b1656_funcs as B
sys.argv = _argv
OUT = {}; LOG = []
def say(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)

ALPHA = {"1": (Fr(1, 2), Fr(1, 2)), "i": (Fr(1, 2), Fr(0)), "j": (Fr(0), Fr(1, 2)), "k": (Fr(0), Fr(0))}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
def mod1(p): return (p[0] % 1, p[1] % 1)
def lines(N):
    seen, out = set(), []
    for j in range(N):
        for k in range(N):
            if math.gcd(math.gcd(j, k), N) != 1: continue
            a, b = Fr(j, N), Fr(k, N); key = min((a, b), ((-a) % 1, (-b) % 1))
            if key not in seen: seen.add(key); out.append(key)
    return out
def classes(cs, rect):
    """the channels grouped by the symmetry's classes of their characteristic"""
    def key(c):
        a, b = mod1(c)
        if rect: return min(mod1((sa * a, sb * b)) for sa in (1, -1) for sb in (1, -1))
        return min(mod1((a, b)), mod1((-a, -b)))
    out = {}
    for s, c in cs.items(): out.setdefault(key(c), []).append(s)
    return list(out.values())

def on_line(a, b, sec, t, rect):
    """for one line and sector: (predicted zero, |D| relative to its scale, the largest norm spread within a class, defined)"""
    lf, rf = SECT[sec]; ql, qr = B.SIXY[lf], B.SIXY[rf]
    w = float(a) * t + float(b)
    x, y = B.sector_twists(w, t, ql, qr); R = B.residues(x, y, t)
    nr = math.sqrt(B.nR2(R))
    live = {s: R[s] for s in B.UNITS if abs(R[s]) > 1e-9 * nr}
    cs = {s: ((ql + qr) * a + ALPHA[s][0], (ql + qr) * b + ALPHA[s][1]) for s in live}
    cl = classes(cs, rect)
    S = [sum(R[s] ** 2 for s in grp) for grp in cl]
    pred = all(abs(v) < 1e-9 * nr ** 2 for v in S)
    c = B.cA(x, y, t, R)
    if any(c[s] is None for s in live): return pred, None, 0.0, False
    spread = max([max(c[s] for s in grp) - min(c[s] for s in grp) for grp in cl if len(grp) > 1] or [0.0])
    D = sum(c[s] * R[s] ** 2 for s in live)
    scale = max(abs(c[s]) for s in live) * nr ** 2 if live else 1.0
    return pred, (abs(D) / scale if live else 0.0), spread, True

TAUS = {"rect_1.3": complex(0, 1.3), "rect_2.1": complex(0, 2.1), "generic": complex(0.29, 1.83)}
def run():
  res = {}
  for tname, t in TAUS.items():
    rect = abs(t.real) < 1e-15
    agree = disagree = undefined = 0; zmax = 0.0; nzmin = 10.0; spread_max = 0.0; zero_lines = {}
    for N in range(1, 13):
        for (a, b) in lines(N):
            for sec in SECT:
                pred, rel, spread, defined = on_line(a, b, sec, t, rect)
                if not defined: undefined += 1; continue
                spread_max = max(spread_max, spread)
                z = rel < 1e-8
                if z == pred: agree += 1
                else: disagree += 1; say("   DISAGREE", tname, N, (str(a), str(b)), sec, "pred", pred, "rel", "%.2e" % rel)
                if pred: zmax = max(zmax, rel)
                else: nzmin = min(nzmin, rel)
                if z: zero_lines.setdefault("N=%d %s" % (N, sec), []).append("%s,%s" % (a, b))
    res[tname] = {"agree": agree, "disagree": disagree, "undefined": undefined, "max_rel_D_where_predicted_zero": zmax,
                  "min_rel_D_elsewhere": nzmin, "max_norm_spread_within_a_class": spread_max,
                  "zero_line_counts": {k: len(v) for k, v in zero_lines.items()}, "zero_lines": zero_lines}
    say(tname, "agree", agree, "disagree", disagree, "undefined", undefined, "| max rel D where zero predicted %.2e" % zmax,
        "| min elsewhere %.2e" % nzmin, "| largest norm spread within a class %.2e" % spread_max)
    say("   zero line counts:", res[tname]["zero_line_counts"])
  OUT["census"] = res

  # the 12-alpha-odd order-12 lines at Re tau = 0, split by 12-beta parity (P-292's wording, P-337's fix, Theorem E's scoping)
  split = {}
  for tname in ("rect_1.3", "rect_2.1"):
      zl = res[tname]["zero_lines"]
      for sec in ("up", "down"):
          zs = set(zl.get("N=12 %s" % sec, []))
          cand = [(a, b) for (a, b) in lines(12) if (12 * a).denominator == 1 and int(12 * a) % 2 == 1]
          odd = [ab for ab in cand if int(12 * ab[1]) % 2 == 1]; even = [ab for ab in cand if int(12 * ab[1]) % 2 == 0]
          split["%s %s" % (tname, sec)] = {"lines_12a_odd": len(cand),
                                           "12b_odd": [len(odd), sum("%s,%s" % ab in zs for ab in odd)],
                                           "12b_even": [len(even), sum("%s,%s" % ab in zs for ab in even)]}
  OUT["P292_split_lines_and_zeros"] = split
  say("P-292's family at Re tau = 0 ([lines, of which D = 0]):", split)

if __name__ == "__main__":
    run()
    json.dump(OUT, open(HERE / "the_zero_law_on_every_line.json", "w"), indent=1, default=str)
    open(HERE / "the_zero_law_on_every_line_run.txt", "w").write("\n".join(LOG) + "\n")
