"""The Y integrand's closure probed at a generic start of the period (chat1; an instrument check; no data).

tlow2.configuration probes closure by comparing the integrand at the period's first point with the point one period
on, relative to its size there. On some rotations (LRR's three, LLR's LRL) that first point is an image of omega,
e^(i pi/3), where Y3x vanishes, so the probe is 0/0. Here a copy of tlow2.configuration, changed only to start the
period at s0 = -P/2 + SHIFT, probes every primitive thread of trace 3..12 at SHIFT = 0.137, and compares LRR's
integrals at the two starts (a closed integrand's period integral does not depend on where it starts).
tlow2.py itself is not changed; the copy is built in memory from its source.
Usage: python3 -B closure_at_generic_start.py <forms.pkl> > closure_at_generic_start_run.txt
"""
import math, os, pickle, sys, types
HERE = os.path.dirname(os.path.abspath(__file__))
TU = os.path.normpath(os.path.join(HERE, "..", "chat1_2026-10-15_route", "twisted_units"))
src = open(os.path.join(TU, "tlow2.py")).read()
a1 = "        s = -PlA / 2 + PlA * j / Npts\n"
a2 = "    s = PlA / 2\n"
assert src.count(a1) == 1 and src.count(a2) == 1
src = src.replace(a1, "        s = -PlA / 2 + PlA * j / Npts + SHIFT\n").replace(a2, "    s = PlA / 2 + SHIFT\n")
T2s = types.ModuleType("tlow2_shift"); T2s.__dict__["SHIFT"] = 0
exec(compile(src, "tlow2_shift", "exec"), T2s.__dict__)
import flint
from flint import arb
import mpmath as mp
sys.path.insert(0, HERE)
from w_trace_untwisted import threads_by_trace, ZERO

P = pickle.load(open(sys.argv[1], "rb"))


def run(word, shift, k=None, npp=30):
    T2s.SHIFT = arb(shift)
    rot, M, rho, kk, height = T2s.thread_geometry(word, k)
    flint.ctx.prec = 800; F = T2s.Forms(P).prepare(); flint.ctx.prec = T2s.bits_for(height)
    a, b, c, d = M; Pl = 2 * math.acosh((a + d) / 2)
    if height > 4.3: npp = 60
    return rot, T2s.configuration(F, word, (1, 0), 1, {"Z": ZERO}, int(round(Pl * npp)), readings=("minimal",), kforce=k)


worst = 0.0
for t, ws in sorted(threads_by_trace(12).items()):
    for w in ws:
        rot, conf = run(w, 0.137)
        cl = max(conf["closure"].values()); worst = max(worst, cl)
        print(f"t={t:2d} {w:12s} closure at a generic start: {cl:.1e}", flush=True)
print(f"worst over the 29 threads: {worst:.1e}")
for k in range(3):
    for w in ("LRR", "LLR"):
        rot, conf = run(w, 0.137, k)
        print(f"{w} rotation {rot}: closure at a generic start {max(conf['closure'].values()):.1e}", flush=True)
mp.mp.dps = 40
r0 = run("LRR", 0.0)[1]["mn"][(0, 0)]; r1 = run("LRR", 0.137)[1]["mn"][(0, 0)]
dev = max(max(float(abs(r0[k_][i][j] - r1[k_][i][j]).mid()) for i in range(len(r0[k_])) for j in range(len(r0[k_][0])))
          / max(float(abs(r0[k_][i][j]).mid()) for i in range(len(r0[k_])) for j in range(len(r0[k_][0]))) for k_ in r0)
print(f"LRR's Y integrals at the two starts: largest difference relative to each matrix's largest entry {dev:.1e}")
