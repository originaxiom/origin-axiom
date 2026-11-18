"""B1957: the web seat's two further sealed checks of 2026-10-14 in its scale folder, run again on main's own script
written from their seals.  Data-free.
 T-ROOT: the 31,040 threads of length 2 to 18 (SnapPy), weighted by e^(-c Vol/(6 pi)) and by a word weight
   (A) 2^-n, (B) 3^-n, (C) 1/(n (n - 1) L(n)): the root's share p, the chiral share f, the effective number of
   threads, at c = 6; the c at which p reaches 0.5 and 0.99; the composition (chiral or not); the level's footprint
   1 - Re Z(k)/Z(0) under (A) with the phase e^(2 pi i k CS/pi^2).  Main verified this in B1650's addendum.
 T-SIGN: the bundles of -W (SnapPy's b+-): b+-LR is m003 with CS = pi^2/2; every swap-symmetric word to length 14 has
   CS(b+-W) = +-pi^2/2; for every word to length 10 the sign shifts CS by pi^2/2 and keeps the volume."""
import functools, math, warnings, cmath
print = functools.partial(print, flush=True)
import pathlib as _pl, sys as _sys
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))          # the sibling below is found in isolated mode too (the web seat's section 9, 2026-11-18)
import web_selection_exact as S
with warnings.catch_warnings():
    warnings.simplefilter("ignore"); import snappy
PI2 = math.pi ** 2
sw = str.maketrans("LR", "RL"); least = lambda w: min(w[i:] + w[:i] for i in range(len(w)))
red = lambda cs: (cs + PI2 / 2) % PI2 - PI2 / 2


def data(name):
    for attempt in range(4):
        try:
            M = snappy.Manifold(name); cv = M.complex_volume(); return float(cv.real()), red(float(cv.imag())), M.solution_type()
        except Exception:
            continue
    raise RuntimeError("SnapPy failed four times on a bundle")


if __name__ == "__main__":
    words = {n: S.lyndon(n) for n in range(2, 19)}; allw = [w for n in range(2, 19) for w in words[n]]
    D = {w: data("b++" + w) for w in allw}
    chiral = [w for w in allw if abs(D[w][1]) > 1e-6]
    print("T-ROOT: threads %d; all geometric: %s; chiral %d, not chiral %d" % (len(allw), all(D[w][2] == "all tetrahedra positively oriented" for w in allw), len(chiral), len(allw) - len(chiral)))
    wt = {"A": lambda w: 2.0 ** -len(w), "B": lambda w: 3.0 ** -len(w), "C": lambda w: 1.0 / (len(w) * (len(w) - 1) * len(words[len(w)]))}
    def stats(c, key):
        ws = {w: wt[key](w) * math.exp(-c * D[w][0] / (6 * math.pi)) for w in allw}; Z = sum(ws.values()); p = ws["LR"] / Z
        f = sum(ws[w] for w in chiral) / Z; ent = -sum((v / Z) * math.log(v / Z) for v in ws.values()); return p, f, math.exp(ent), ws, Z
    def threshold(level, key):
        lo, hi = 0.0, 600.0
        if stats(lo, key)[0] >= level: return 0.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if stats(mid, key)[0] < level: lo = mid
            else: hi = mid
        return hi
    for key in "ABC":
        p, f, ne, ws, Z = stats(6.0, key); p0 = stats(0.0, key)[0]
        print("T-ROOT: weight (%s) at c = 6: root share %.4f, chiral share %.3f, effective number of threads %.1f; root share at c = 0: %.2f; c at which the root holds 0.5: %.1f; 0.99: %.1f" % (key, p, f, ne, p0, threshold(0.5, key), threshold(0.99, key)))
    for c in (2, 24, 64, 128, 256):
        print("T-ROOT: c = %d: (root share, chiral share, effective number) under (A), (B), (C): %s" % (c, [tuple(round(x, 4 if i < 2 else 2) for i, x in enumerate(stats(float(c), key)[:3])) for key in "ABC"]))
    print("T-ROOT: under (B) at c = 6 the sum Z is %.4f; the c at which the root holds 0.9: %.1f under (A), %.1f under (B), %.1f under (C)" % (stats(6.0, "B")[4], threshold(0.9, "A"), threshold(0.9, "B"), threshold(0.9, "C")))
    p, f, ne, ws, Z = stats(6.0, "A"); top = sorted(allw, key=lambda w: -ws[w])[:6]
    foot = [1 - (sum(ws[w] * cmath.exp(2j * math.pi * k * D[w][1] / PI2) for w in allw) / Z).real for k in (1, 2, 3, 4)]
    print("T-ROOT: the heaviest threads at c = 6 under (A): %s; the level's footprint at k = 1 to 4: %s" % ([(w, round(ws[w] / Z, 3)) for w in top], [round(x, 3) for x in foot]))
    m = snappy.Manifold("b+-LR"); ident = [str(x) for x in m.identify()][:2]; v, cs, st = data("b+-LR")
    print("T-SIGN: b+-LR is %s; its |CS| %.6f (pi^2/2 = %.6f)" % (ident, abs(cs), PI2 / 2))
    sym = [w for n in range(2, 15) for w in words[n] if least(w.translate(sw)) in (w, least(w[::-1]))]
    n1 = sum(1 for w in sym if abs(abs(data("b+-" + w)[1]) - PI2 / 2) < 1e-6)
    ten = [w for n in range(2, 11) for w in words[n]]; n2 = 0; dv = 0.0
    for w in ten:
        vm, cm, _ = data("b+-" + w); d = (cm - D[w][1]) % PI2; n2 += abs(d - PI2 / 2) < 1e-6; dv = max(dv, abs(vm - D[w][0]))
    print("T-SIGN: swap-symmetric words to length 14: %d, with CS(-W) = +-pi^2/2 on %d; words to length 10: %d, with the sign shifting CS by pi^2/2 on %d; the volumes of W and -W differ by at most %.1e" % (len(sym), n1, len(ten), n2, dv))
