"""B1957: agy-002's note M34, Part 3 (does a weight on the closed geodesics close the gap between the move count and the
area?), on main's own files.  Data-free: only differences between two theoretical read-outs are printed.
Main's variant, stated plainly: the seat averages the marked point's own read-out over the words that keep the mark;
main has the 24-point average F-bar on B1932's grid (the exact weight), and uses it along the same words' geodesics.
The two populations agree in the long-word limit and not exactly at length 14, so the figures are compared with the
seat's to about a hundredth, not digit for digit.  The words, their eta and the weights are those of agy002_m34.py; the
area values are B1940's corrected file."""
import sys, pathlib, json, math, functools
import numpy as np
print = functools.partial(print, flush=True)
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import agy002_m34 as A
B32 = next((ROOT / "frontier").glob("B1932_*")) / "verification"; sys.path.insert(0, str(B32)); import ergodic_both_worlds as E
AREA = json.loads((next((ROOT / "frontier").glob("B1940_*")) / "verification" / "BIG_RUN_VALUES_v2.json").read_text())["options"]


def thread(M, per_unit=10):
    (a, b), (c, d) = [[int(x) for x in r] for r in M]; tr = a + d; D = tr * tr - 4          # gamma = M^T acts as z -> (a z + c)/(b z + d)
    r1 = ((a - d) + math.sqrt(D)) / (2 * b); r2 = ((a - d) - math.sqrt(D)) / (2 * b); cen, R = (r1 + r2) / 2, abs(r1 - r2) / 2; ell = 2 * math.log((abs(tr) + math.sqrt(D)) / 2)
    nodes = max(32, int(per_unit * ell)); zs = [complex(cen + R * math.tanh(s), R / math.cosh(s)) for s in (-ell / 2 + ell * (j + 0.5) / nodes for j in range(nodes))]
    return np.array([[r.real, r.imag] for r in (E.T.reduce(z, 0.0, 0.0, {"x": 0.0})[0] for z in zs)]), ell


if __name__ == "__main__":
    K, NEG, NXT, _, _ = A.cocycle(); I = E.build(B32 / "fiber_grid_t90.json"); n = 14
    b, k, end = A.etas(n, K, NEG, NXT, (2, 4)); keep = (end != 0) & (b != 0) & (b != (1 << n) - 1); bits, eta = b[keep], k[keep] / 15.0
    F, ell, sel = [], [], []
    for w in bits:
        M = A.word_matrix(int(w), n); pts, l = thread(M); F.append(E.interp(I, pts).mean(0)); ell.append(l); sel.append(1 / math.sqrt(abs(int(M[0, 0] + M[1, 1]) - 2)))
    F, ell, sel = np.array(F), np.array(ell), np.array(sel); ch, c1 = np.cos(0.5 * math.pi * eta), np.cos(math.pi * eta)
    area = {"W-": np.array(AREA["W-|b (area)"]["values"]), "W+": np.array(AREA["W+|b (area)"]["values"])}
    seat = {"length-weighted move count": (0.5247, 0.4203, 0.5146, 0.4243), "uniform over words": (0.5091, 0.4063, 0.5011, 0.4103), "one-loop weight |tr - 2|^(-1/2)": (0.4604, 0.3634, 0.4587, 0.3671),
            "cos(pi eta)": (1.1090, 0.6176, 1.2761, 0.8126), "one-loop weight times cos(pi eta/2)": (1.8718, 1.1136, 4.2732, 2.0398), "cos(pi eta/2)": (3.5094, 2.6767, 3.2991, 2.3927)}
    print("%d words of length %d keep the mark; main's grid average along each word's geodesic; against B1940's corrected area values" % (len(bits), n))
    for lab, wt in (("length-weighted move count", ell), ("uniform over words", np.ones(len(bits))), ("one-loop weight |tr - 2|^(-1/2)", sel), ("cos(pi eta)", c1), ("one-loop weight times cos(pi eta/2)", sel * ch), ("cos(pi eta/2)", ch)):
        v = (wt[:, None] * F).sum(0) / wt.sum(); dm, dp = np.abs(np.log(np.abs(v[:7]) / area["W-"])), np.abs(np.log(np.abs(v[7:]) / area["W+"]))
        print("  %-36s W-: max |d ln| %.4f, rms %.4f; W+: max %.4f, rms %.4f; the weight's mean %+.5f; negative values among the fourteen: %d   (the seat, on the mark's own read-out: %.4f, %.4f, %.4f, %.4f)" % (
            lab, dm.max(), math.sqrt((dm ** 2).mean()), dp.max(), math.sqrt((dp ** 2).mean()), wt.mean() if wt is not ell else 1.0, int((v < 0).sum()), *seat[lab]))
    m40 = {o: np.array(AREA[o]["values"]) for o in AREA}
    print("main's own two measures in B1940's file (forty-letter words against the area): max |d ln| W- %.4f, W+ %.4f" % (np.abs(np.log(m40["W-|a (move count)"] / m40["W-|b (area)"])).max(), np.abs(np.log(m40["W+|a (move count)"] / m40["W+|b (area)"])).max()))
