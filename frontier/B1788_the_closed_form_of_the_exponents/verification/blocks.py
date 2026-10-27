"""Closed-form check, step 1 (data-free): the frame's building blocks and their leading exponents.
Units: an exponent E means modulus ~ exp(-E * 2 pi Im tau) (B1785's convention).
Blocks at u = 0 (b1656_funcs.bil): r00 = Res X0 Y0 / th1, r01 = Res e^{i pi by} X0 Y1 / den, r10 = Res e^{i pi bx} X1 Y0 / den,
and r11 = Res e^{i pi (bx + by)} X1 Y1 / th1(u + tau) (th1 vanishes at u + tau too; |th1'(tau)| = |q|^{-1/2} |th1'(0)|).
Candidate closed forms (twists a = q alpha, thc with T = 2 tau):
  X0 ~ |q|^{||a||^2},  X1 = thc(a, b, tau, 2 tau) ~ |q|^{||a + 1/2||^2 - 1/4},  1/th1'(0) ~ |q|^{-1/8},  1/den ~ |q|^{+1/8}
  E00 = ||ax||^2 + ||ay||^2 - 1/8;  E01 = ||ax||^2 + ||ay + 1/2||^2 - 1/8;  E10 = ||ax + 1/2||^2 + ||ay||^2 - 1/8;
  E11 = ||ax + 1/2||^2 + ||ay + 1/2||^2 - 1/8.
Excluded from the exponent fit (flagged, not fitted): blocks whose theta constant vanishes exactly (q alpha in {0, 1/2} with
2 q beta = 1/2 mod 1 makes X0(0) or X1(0) zero).  Writes blocks.json.
"""
import sys, math, json, pathlib
from fractions import Fraction as Fr
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); _a = sys.argv; sys.argv = ["x"]
import b1656_funcs as B
sys.argv = _a
RE = 1.0 / 3.0
H = (4.0, 5.0, 6.0)


def nd(x):
    x = float(x) % 1.0; return min(x, 1.0 - x)


def blocks(a, b, ql, qr, t):
    w = float(a) * t + float(b)
    x, y = B.sector_twists(w, t, ql, qr)
    (ax, bx), (ay, by) = x, y
    T = 2 * t
    th1p = complex((B.th1(1e-7, t) - B.th1(-1e-7, t)) / 2e-7)
    den_res = 1j * np.exp(-1j * np.pi * t / 2) * th1p
    th1p_tau = complex((B.th1(t + 1e-7, t) - B.th1(t - 1e-7, t)) / 2e-7)
    X0, X1, Y0, Y1 = (complex(B.thc(ax, bx, 0.0, T)), complex(B.thc(ax, bx, t, T)), complex(B.thc(ay, by, 0.0, T)), complex(B.thc(ay, by, t, T)))
    r00 = X0 * Y0 / th1p; r01 = np.exp(1j * np.pi * by) * X0 * Y1 / den_res; r10 = np.exp(1j * np.pi * bx) * X1 * Y0 / den_res
    r11 = np.exp(1j * np.pi * (bx + by)) * X1 * Y1 / th1p_tau
    return dict(X0=X0, X1=X1, Y0=Y0, Y1=Y1, th1p=th1p, r00=r00, r01=r01, r10=r10, r11=r11), (ax, ay)


def fit(vals):
    X = np.array([2 * math.pi * y for y in H]); Y = np.log(np.maximum(np.abs(vals), 1e-300))
    A = np.vstack([X, np.ones(3)]).T; (s, c), *_ = np.linalg.lstsq(A, Y, rcond=None); return float(-s)


def closed(ax, ay):
    nx, ny, nx2, ny2 = nd(ax), nd(ay), nd(ax + 0.5), nd(ay + 0.5)
    return dict(X0=nx ** 2, X1=nx2 ** 2 - 0.25, Y0=ny ** 2, Y1=ny2 ** 2 - 0.25, th1p=0.125,
                r00=nx ** 2 + ny ** 2 - 0.125, r01=nx ** 2 + ny2 ** 2 - 0.125,
                r10=nx2 ** 2 + ny ** 2 - 0.125, r11=nx2 ** 2 + ny2 ** 2 - 0.125)


if __name__ == "__main__":
    # (1) the channel map against the instrument's own residues, on many lines and every sector, at Im tau 4
    t = complex(RE, 4.0); maxerr = {s: 0.0 for s in B.UNITS}; nmap = 0
    for (a, b) in [(Fr(j, N), Fr(k, N)) for N in (5, 7, 10, 12) for j in range(N) for k in range(N) if math.gcd(math.gcd(j, k), N) == 1][::2]:
        for sec, (lf, rf) in B.SECTORS.items():
            w = float(a) * t + float(b); x, y = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, y, t)
            bl, _ = blocks(a, b, B.SIXY[lf], B.SIXY[rf], t)
            pred = {"1": bl["r01"] - bl["r10"], "i": -1j * (bl["r01"] + bl["r10"]), "j": -(bl["r00"] + bl["r11"]), "k": 1j * (bl["r00"] - bl["r11"])}
            scale = max(abs(R[s]) for s in R) or 1.0
            for s_ in R: maxerr[s_] = max(maxerr[s_], abs(R[s_] - pred[s_]) / scale)
            # rank one: r00 r11 = r01 r10 (B1716)
            maxerr.setdefault("rank_one", 0.0)
            maxerr["rank_one"] = max(maxerr["rank_one"], abs(bl["r00"] * bl["r11"] - bl["r01"] * bl["r10"]) / max(abs(bl["r00"] * bl["r11"]), abs(bl["r01"] * bl["r10"]), 1e-300))
            nmap += 1
    print("channel map, worst error relative to the largest residue, over", nmap, "line-sectors:", {k: float("%.2e" % v) for k, v in maxerr.items()})
    # (2) the block exponents (line-free th1' reported once, not counted as a block)
    worst = {}; rows = []; flagged = []
    lines = [(Fr(j, N), Fr(k, N)) for N in (5, 7, 10, 12, 15, 20) for j in range(N) for k in range(N) if math.gcd(math.gcd(j, k), N) == 1]
    for (a, b) in lines[::3]:
        for sec, (lf, rf) in B.SECTORS.items():
            vals = {k: [] for k in ("X0", "X1", "Y0", "Y1", "r00", "r01", "r10", "r11")}
            for y in H:
                bl, (ax, ay) = blocks(a, b, B.SIXY[lf], B.SIXY[rf], complex(RE, y))
                for k in vals: vals[k].append(bl[k])
            cf = closed(ax, ay)
            for k in vals:
                if max(abs(v) for v in vals[k]) < 1e-12:
                    flagged.append((k, str(a), str(b), sec)); continue
                e = fit(vals[k]); d = e - cf[k]; rows.append((k, str(a), str(b), sec, e, cf[k], d))
                worst[k] = max(worst.get(k, 0), abs(d))
    th = [blocks(Fr(0), Fr(0), 1, 1, complex(RE, y))[0]["th1p"] for y in H]
    print("th1'(0), line-free: fit", round(fit(th), 4), "closed 0.125")
    print("blocks fitted:", len(rows), "| flagged (theta constant exactly zero, not fitted):", len(flagged))
    print("max |fit - closed| per block:", {k: round(v, 4) for k, v in worst.items()})
    bad = [r for r in rows if abs(r[6]) > 0.02]
    print("blocks off by > 0.02:", len(bad), "of", len(rows)); print(bad[:12])
    json.dump(dict(channel_map_worst=maxerr, channel_map_line_sectors=nmap, blocks_fitted=len(rows), flagged=flagged,
                   worst_per_block=worst, off_by_more_than_0_02=len(bad)), open(pathlib.Path(__file__).resolve().parent / "blocks.json", "w"), indent=1)
