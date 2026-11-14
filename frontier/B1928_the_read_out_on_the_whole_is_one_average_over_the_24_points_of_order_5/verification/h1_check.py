"""H1 of B1928's proof, numerically (written before the run): the frame's outputs jump only where two singular values of a
sector's coupling coincide. Main's argument: with the canonical length-2 end (B1927) the frame is real-analytic in tau,
so the coincidence set is a proper analytic subset of zero area; agy-exp's X-NEG proved the path measure's tau-law has
an L^2 density, so the set is null. The numerical face of it: along random geodesics, the share of nodes where the
smallest relative gap of singular values is below eps should fall like eps (a set of codimension one approached
linearly), not stay finite. EXPECTATION: share(1e-2) / share(1e-3) and share(1e-3) / share(1e-4) near 10.
Printed: shares only."""
import json, math, pathlib, random, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1927_*")) / "verification"))  # the canonical end (B1927)
import canon_readout as CR
T, C = CR.T, CR.C

if __name__ == "__main__":
    rng = random.Random(4471)
    gaps = []
    for _ in range(60):
        w = "".join(rng.choice("LR") for _ in range(24))
        if "L" not in w or "R" not in w:
            continue
        beta, betap, ell, g = T.geodesic(w)
        zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
        n = max(32, int(8 * abs(ell))); s0 = -ell / 2
        a, b = rng.choice([(i / 5, j / 5) for i in range(5) for j in range(5) if (i, j) != (0, 0)])
        for j in range(n):
            tr, a2, b2, _ = T.reduce(zt(s0 + ell * j / n), a, b, {"x": 0.0})
            L = CR.canon(tr); L.pop("_extrapolated")
            o = C.frame(tr, a2, b2, L)          # the frame needs both ends; only the length-2 outputs are tested
            g_min = 1.0
            for k, v in o.items():
                if k.startswith("ckm") or "conjS" in k or "|L_2|" not in k:
                    continue
                r1, r2 = v                       # sigma2/sigma1, sigma3/sigma1
                g_min = min(g_min, 1 - r1, (r1 - r2) / max(r1, 1e-300))
            gaps.append(g_min)
    gaps = np.array(gaps)
    shares = {e: float(np.mean(gaps < e)) for e in (1e-1, 1e-2, 1e-3, 1e-4)}
    print("%d nodes; share with the smallest relative singular-value gap below 1e-1, 1e-2, 1e-3, 1e-4: %s" % (len(gaps), ", ".join("%.2e" % shares[e] for e in sorted(shares, reverse=True))), flush=True)
    for e1, e2 in ((1e-1, 1e-2), (1e-2, 1e-3), (1e-3, 1e-4)):
        print("  share(%g) / share(%g) = %s" % (e1, e2, "%.1f" % (shares[e1] / shares[e2]) if shares[e2] > 0 else "no node below %g" % e2), flush=True)
    (HERE / "h1_check.json").write_text(json.dumps({"n": len(gaps), "shares": {str(k): v for k, v in shares.items()}}, indent=1))
