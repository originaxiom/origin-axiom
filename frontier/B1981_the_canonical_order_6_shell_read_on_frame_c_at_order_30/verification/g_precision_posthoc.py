"""B1981, POST HOC (labelled; written after shell_run.txt was read): reading G's Gramian squares the dynamic range, so at heights
40 and 50 its least eigenvalue (relative ~ e^(-2 pi y rate)) can fall below the working precision 30 + 2y digits. This reruns
reading G only, uniform weight, at the 4 blocks and 'all 96', with the frame's matrices computed as before and the Gramian and
its eigenproblem done at 30 + 5y digits. The card's verdicts stand as run; this says which of reading G's cells were limited.
    python3 -B g_precision_posthoc.py > g_precision_posthoc_run.txt"""
import sys, pathlib, json
from fractions import Fraction as Fr
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
mp = DL.mp
P96 = sorted((Fr(r["a"]), Fr(r["b"])) for r in json.loads((next((ROOT / "frontier").glob("B1977_*")) / "verification" / "rates30_run.json").read_text()))
B = {}
for p in P96: B.setdefault(((6 * p[0]) % 1, (6 * p[1]) % 1), []).append(p)
B = {"p5=(%s,%s)" % k: v for k, v in sorted(B.items())}; B["all 96"] = P96
H = (30.0, 40.0, 50.0); out = {}
for y in H:
    Ys = {(p, s): DL.parts("0.13", y, p[0], p[1], s)[2]["S"] for p in P96 for s in ("up", "down", "lep")}
    mp.mp.dps = int(30 + 5 * y)
    for b, pts in B.items():
        for s in ("up", "down", "lep"):
            Hm = mp.matrix(3, 3)
            for p in pts: Hm += Ys[(p, s)] * Ys[(p, s)].H
            E = sorted(abs(e) for e in mp.eighe(Hm)[0])
            out[(b, s, y)] = (mp.sqrt(E[1] / E[2]), mp.sqrt(E[0] / E[2]))
def rate(a, b): return float(-(mp.log(b) - mp.log(a)) / (mp.pi * 10))
for b in B:
    print("%-16s " % b + " ".join("%s m2/m3 %.4f %.4f m1/m3 %.4f %.4f |" % (s, rate(out[(b, s, 30.0)][0], out[(b, s, 40.0)][0]), rate(out[(b, s, 40.0)][0], out[(b, s, 50.0)][0]),
        rate(out[(b, s, 30.0)][1], out[(b, s, 40.0)][1]), rate(out[(b, s, 40.0)][1], out[(b, s, 50.0)][1])) for s in ("up", "down", "lep")))
print("(each pair: the rate on 30-40, then on 40-50; the matrices at 30 + 2y digits as in shell.py, the Gramian at 30 + 5y)")
