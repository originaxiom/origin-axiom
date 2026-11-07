"""POST-RUN integrity check (written after least_volume_out.txt was read; it changes no verdict): the decisive numbers by a
second method. SnapPy's verified volumes need Sage (not available here), so: a re-randomized triangulation of each
manifold, its high-precision shapes, and the volume summed independently as the Bloch-Wigner dilogarithm
D(z) = Im Li2(z) + arg(1 - z) log|z| in mpmath at 60 digits -- independent of SnapPy's volume routine and of the run's
triangulation. Checked: the object, the winner (6), the runner-up (5,1,1,1,1,2) and (2,2,2), at k = 10.
    python3 post_run_verify.py"""
import mpmath as mp
import snappy

mp.mp.dps = 60


def bloch_wigner(z):
    z = mp.mpc(z)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def vol_bw(name):
    M = snappy.ManifoldHP(name)
    M.randomize()
    shapes = M.tetrahedra_shapes("rect")
    v = mp.fsum(bloch_wigner(mp.mpc(str(z.real()), str(z.imag()))) for z in shapes)
    return v, float(M.volume()), M.num_tetrahedra(), M.solution_type()


def word(runs, k):
    s = "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(runs))
    return s + ("R" if len(runs) % 2 else "") + "LR" * k


v4, s4, t4, st4 = vol_bw("b++LR")
print("m004: Bloch-Wigner %s; SnapPy %.15f; %d tets; %s" % (mp.nstr(v4, 20), s4, t4, st4))
K = 10
res = {}
for runs in [(6,), (5, 1, 1, 1, 1, 2), (2, 2, 2)]:
    v, s, t, st = vol_bw("b++" + word(runs, K))
    dv = v - (K + (len(runs) + 1) // 2) * v4
    res[runs] = dv
    print("%-20s randomized %d tets (%s): dV by Bloch-Wigner %s; by SnapPy %.12f; difference %.1e" % (
        runs, t, st, mp.nstr(dv, 16), s - (K + (len(runs) + 1) // 2) * s4, float(abs(dv - (s - (K + (len(runs) + 1) // 2) * s4)))))
print("gap (5,1,1,1,1,2) - (6) by Bloch-Wigner: %s" % mp.nstr(res[(5, 1, 1, 1, 1, 2)] - res[(6,)], 16))
print("post_run_verify exit 0")
