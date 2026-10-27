"""Referee: B1656's frame in mpmath (dps 40) at high Im tau on chosen (line, sector); both readings.
    python3 run_high.py tag 'a:b:sec,...' 'y1,y2,...' [nth ns]"""
import sys, json, time
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from fractions import Fraction as Fr
import mpframe as F, mpmath as mp
mp.mp.dps = 40
tag = sys.argv[1]; cases = [c.split(":") for c in sys.argv[2].split(",")]; ys = [float(v) for v in sys.argv[3].split(",")]
nth, ns = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (96, 64)
out = open(__import__("pathlib").Path(__file__).resolve().parent / ("high_%s.jsonl" % tag), "a")
for a, b, sec in cases:
    for y in ys:
        t0 = time.time(); tau = mp.mpc(mp.mpf(1) / 3, y)
        fr = F.Frame(Fr(a), Fr(b), sec, tau)
        c = fr.cA(nth=nth, ns=ns); S = F.S_of(tau); mp.mp.dps = 40
        rat, detM, Mw = F.ratios(fr, c, y, S)
        rec = {"a": a, "b": b, "sec": sec, "y": y, "nth": nth, "ns": ns,
               "c": {s: (None if c[s] is None else mp.nstr(c[s], 30)) for s in c},
               "absR": {s: mp.nstr(abs(fr.R[s]), 15) for s in fr.R},
               "absr": [[mp.nstr(abs(v), 15) for v in r] for r in fr.r],
               "absdetM": mp.nstr(abs(detM), 15), "maxM": mp.nstr(max(abs(Mw[i, j]) for i in range(2) for j in range(2)), 15),
               "S": [mp.nstr(v, 20) for v in rat["S"]], "St": [mp.nstr(v, 20) for v in rat["St"]], "sec_time": round(time.time() - t0, 1)}
        out.write(json.dumps(rec) + "\n"); out.flush()
        print(a, b, sec, y, "S", rec["S"][0][:10], "St", rec["St"][0][:10], "%.0fs" % rec["sec_time"], flush=True)
print("run_high exit 0")
