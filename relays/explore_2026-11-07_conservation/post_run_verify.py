"""POST-RUN integrity check (written after conservation_out.txt was read; it changes no verdict):
  (a) the selected departures' apexes by the record's second instrument, D0.highest_matrix (the matrix orbit with its
      S-conjugates), against the run's highest_cf, and against the closed form Im = (n - 1)/2 + sqrt5/2 that the run's
      single-run apexes suggest (6, 21, 61);
  (b) the long single runs' excess volume by an independent Bloch-Wigner sum on a re-randomized triangulation.
    python3 post_run_verify.py"""
import importlib.util
import pathlib
import sys

import mpmath as mp
import snappy

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sp = importlib.util.spec_from_file_location("least_action_check", HERE / "least_action_check.py")
LA = importlib.util.module_from_spec(sp)
sys.modules["least_action_check"] = LA
sp.loader.exec_module(LA)
D0 = LA.D0
mp.mp.dps = 60

print("(a) apexes: highest_cf (the run's) against highest_matrix (second instrument) and the closed form")
for runs in [(2,), (2, 1, 1, 1, 2), (6,), (21,), (61,)]:
    closed = LA.closed_runs(runs, 20)
    letters = [D0.L if i % 2 == 0 else D0.R for i, r in enumerate(closed) for _ in range(r)]  # letter matrices
    im1, re1 = D0.highest_cf(closed, reps=20)
    hm = D0.highest_matrix(letters)
    im2 = hm[1]  # (centre, radius, matrix): the apex height is the radius
    cf = (mp.mpf(runs[0]) - 1) / 2 + mp.sqrt(5) / 2 if len(runs) == 1 else None
    print("  %-16s highest_cf Im %s; highest_matrix %s; closed form %s" % (
        runs, mp.nstr(im1, 15), mp.nstr(im2, 15) if not isinstance(im2, (list, dict)) else im2,
        mp.nstr(cf, 15) if cf is not None else "-"))


def bw(z):
    z = mp.mpc(z)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def vol_bw(name):
    M = snappy.ManifoldHP(name)
    M.randomize()
    return mp.fsum(bw(mp.mpc(str(z.real()), str(z.imag()))) for z in M.tetrahedra_shapes("rect")), M.solution_type()


v4, _ = vol_bw("b++LR")
print("(b) excess volume of the long single runs by Bloch-Wigner (k = 10)")
for n in (21, 41, 61):
    w = "L" * n + "R" + "LR" * 10
    v, st = vol_bw("b++" + w)
    print("  (%d,): dV %s (%s)" % (n, mp.nstr(v - 11 * v4, 13), st))
print("post_run_verify exit 0")
