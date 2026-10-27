"""e21b (POST HOC, labelled): written after this seat's read-only referee found that e21's K9 tested the mirror w -> -conj(w)
only in the form tau -> 1 - conj(tau) (b -> -alpha - b), and so missed the apexes on Re tau = 0, where tau -> -conj(tau) fixes
the point and pairs b with -b.  From main's committed census (54cfec661), this seat's own code (e21's loader):
  M1  the apexes on Re tau = 0, and the rows with a partner under each form of the mirror, to what accuracy;
  M2  the apexes with no mirror partner under either form;
  M3  for each of the 15 pairs (2/5, b) <-> (2/5, 3/5 - b): the per-line minimum of chi2_six (seat) over all apexes, over the
      apexes closed under tau -> 1 - conj(tau), and where the lower minimum of an unequal pair sits.
    python3 -B e21b_mirror_at_re_tau_zero.py MAIN_ROOT > e21b_out.txt"""
import sys, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("e21", HERE / "e21_b1786_checking_pass.py")
sys.argv = [sys.argv[0], sys.argv[1]]
E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)


def main():
    T6, s6, _ = E.targets_and_sigmas(); t6 = T6 / s6
    rows = E.read_rows(E.V86 / "census.jsonl.gz", gz=True)
    X, lab, G = E.features(rows, s6)
    d2 = ((X - t6) ** 2).sum(2).min(0)
    key = {(Fr(l[1]), Fr(l[2]), round(l[3], 9), round(l[4], 9), l[5]): t for t, l in enumerate(lab)}
    apex = sorted({(round(l[3], 9), round(l[4], 9)) for l in lab})
    norm = lambda a, b: min((a, b), ((-a) % 1, (-b) % 1))
    on0 = [p for p in apex if abs(p[0]) < 1e-12]
    pa = {"1 - conj(tau), b -> -alpha - b": (lambda re, a, b: (round(1 - re, 9), norm(a, (-a - b) % 1))),
          "-conj(tau), b -> -b (Re tau = 0)": (lambda re, a, b: (round(-re, 9) if abs(re) < 1e-12 else None, norm(a, (-b) % 1)))}
    partnered = np.zeros(len(lab), bool)
    print("M1 apexes on Re tau = 0: %d (Im tau %s)" % (len(on0), ", ".join("%.3f" % p[1] for p in on0)))
    for name, f in pa.items():
        n = 0; mx = 0.0
        for t, l in enumerate(lab):
            a, b = Fr(l[1]), Fr(l[2]); re2, (a2, b2) = f(l[3], a, b)
            if re2 is None: continue
            u = key.get((a2, b2, re2, round(l[4], 9), l[5]))
            if u is None: continue
            n += 1; partnered[t] = True; mx = max(mx, float(np.max(np.abs(G[t] - G[u]))))
        print("   form %-34s rows with a partner %6d; max |delta ln| over the 12 ratios %.1e" % (name, n, mx))
    print("   rows with a partner under either form: %d of %d" % (int(partnered.sum()), len(lab)))
    closed = {p for p in apex if (round(1 - p[0], 9), p[1]) in set(apex)}
    lone = [p for p in apex if p not in closed and abs(p[0]) > 1e-12]
    print("M2 apexes closed under tau -> 1 - conj(tau): %d; on Re tau = 0: %d; with no partner under either form: %d (%s)"
          % (len(closed), len(on0), len(lone), ", ".join("%.4f + %.4fi" % p for p in lone)))
    a25 = np.array([l[1] == "2/5" for l in lab]); bb = [Fr(l[2]) for l in lab]
    inc = np.array([(round(l[3], 9), round(l[4], 9)) in closed for l in lab])
    print("M3 the 15 pairs (2/5, b) <-> (2/5, 3/5 - b): minima over all apexes | over the closed apexes; where the lower sits")
    seen = set()
    for b in sorted({bb[t] for t in np.flatnonzero(a25)}):
        m = (Fr(3, 5) - b) % 1
        if (m, b) in seen: continue
        seen.add((b, m))
        sel = lambda x, mask=None: np.flatnonzero(a25 & np.array([bv == x for bv in bb]) & (mask if mask is not None else True))
        ia, im_ = sel(b), sel(m); ca, cm = d2[ia].min(), d2[im_].min()
        ja, jm = sel(b, inc), sel(m, inc); ka, km = d2[ja].min(), d2[jm].min()
        where = ""
        if abs(ca - cm) > 1e-6 * min(ca, cm):
            i = ia[np.argmin(d2[ia])] if ca < cm else im_[np.argmin(d2[im_])]
            where = "  lower at %.4f + %.4fi" % (lab[i][3], lab[i][4])
        print("   %6s %6s  all: %9.3f %9.3f   closed: %9.3f %9.3f%s" % (b, m, ca, cm, ka, km, where))
    print("e21b exit 0")


if __name__ == "__main__":
    main()
