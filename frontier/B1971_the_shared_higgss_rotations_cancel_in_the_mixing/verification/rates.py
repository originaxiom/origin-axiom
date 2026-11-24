"""B1971 (main, 2026-11-24; data-free): frame C with every sector reading S (B1970 = W-D2's D-1).
At the mark (2/5, 4/5) and the twin (1/5, 2/5), column x = 0.13, read the rate (in units of eps = e^(-pi Im tau)) of:
the Higgs triplet's components, each sector's channels u[s], every entry of Y_up and Y_down, the singular values,
every |U| entry, every |V| entry and |J|.  Rate between heights y1 < y2: -(ln r2 - ln r1) / (pi (y2 - y1))."""
import sys, pathlib, json
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
from fractions import Fraction as Fr
mp = DL.mp

def snap(y, a, b):
    out = {}
    for sec in ("up", "down"):
        RD, Mw, Ys, u, cs, ds = DL.parts("0.13", y, a, b, sec)
        Y = Ys["S"]
        out[sec] = dict(Y=Y, u=u, U=CM.U_of(Y), sv=sorted([abs(s) for s in mp.svd_c(Y, compute_uv=False)]))
        out["h"] = [mp.mpf(abs(RD["S"][0, 1])), None]
    from mpmath import mpc
    c3 = [DL.FM.te.ev(cc, mp.mpc(mp.mpf("0.13"), mp.mpf(y))) for cc in DL.FM.te.B[1]]
    out["c3"] = [abs(c) for c in c3]
    V = out["up"]["U"].H * out["down"]["U"]
    out["V"] = V
    out["J"] = abs(mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0])))
    return out

def rate(v1, v2, y1, y2):
    v1, v2 = abs(v1), abs(v2)
    if v1 == 0 or v2 == 0: return None
    return float(-(mp.log(v2) - mp.log(v1)) / (mp.pi * (y2 - y1)))

if __name__ == "__main__":
    pts = {"mark": (Fr(2, 5), Fr(4, 5)), "twin": (Fr(1, 5), Fr(2, 5))}
    ys = [float(v) for v in sys.argv[1:]] or [20.0, 30.0]
    res = {}
    for name, (a, b) in pts.items():
        S = [snap(y, a, b) for y in ys]
        y1, y2 = ys[-2], ys[-1]; A, Bq = S[-2], S[-1]
        r = {}
        r["c3"] = [rate(A["c3"][k], Bq["c3"][k], y1, y2) for k in range(3)]
        for sec in ("up", "down"):
            r[sec + "_u"] = {s: rate(A[sec]["u"][s], Bq[sec]["u"][s], y1, y2) for s in A[sec]["u"]}
            r[sec + "_Y"] = [[rate(A[sec]["Y"][i, j], Bq[sec]["Y"][i, j], y1, y2) for j in range(3)] for i in range(3)]
            r[sec + "_sv"] = [rate(A[sec]["sv"][k], Bq[sec]["sv"][k], y1, y2) for k in range(3)]
            r[sec + "_U"] = [[rate(A[sec]["U"][i, j], Bq[sec]["U"][i, j], y1, y2) for j in range(3)] for i in range(3)]
        r["V"] = [[rate(A["V"][i, j], Bq["V"][i, j], y1, y2) for j in range(3)] for i in range(3)]
        r["J"] = rate(A["J"], Bq["J"], y1, y2)
        r["absV_at_y2"] = [[float(abs(Bq["V"][i, j])) for j in range(3)] for i in range(3)]
        res[name] = r
        print("==", name, (str(a), str(b)), "heights", y1, y2, flush=True)
        fmt = lambda x: "  -  " if x is None else "%6.3f" % x
        print("  Higgs triplet |c_k| rates:", " ".join(fmt(x) for x in r["c3"]))
        for sec in ("up", "down"):
            print("  %s channels u[s] rates:" % sec, {s: (None if v is None else round(v, 3)) for s, v in r[sec + "_u"].items()})
            print("  %s singular values (ascending) rates:" % sec, " ".join(fmt(x) for x in r[sec + "_sv"]))
            for i in range(3): print("  %s Y row %d: %s     |U| row %d: %s" % (sec, i, " ".join(fmt(x) for x in r[sec + "_Y"][i]), i, " ".join(fmt(x) for x in r[sec + "_U"][i])))
        for i in range(3): print("  |V| row %d rates: %s    |V| at y2: %s" % (i, " ".join(fmt(x) for x in r["V"][i]), " ".join("%.2e" % x for x in r["absV_at_y2"][i])))
        print("  |J| rate:", fmt(r["J"]), flush=True)
    json.dump(res, open(pathlib.Path(__file__).with_name("rates_run_%s.json" % "_".join(str(int(y)) for y in ys)), "w"), indent=1)
