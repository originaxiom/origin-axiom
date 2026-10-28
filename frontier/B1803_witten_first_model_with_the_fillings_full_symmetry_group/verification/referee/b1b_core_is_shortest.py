"""Referee B1803, b1b: on the even fillings where SnapPy's symmetry_group is not certified full ('at least Z/2 + Z/2' or a
crash), certify Isom(Q) = F' another way: if the filling's core geodesic is the unique shortest closed geodesic of Q, every
isometry preserves it, so Isom(Q) injects into the slope-preserving symmetries of m004 = D4 cap Stab(p/q); the
orientation-preserving ones are F' (cusp maps +-I), and the orientation-reversing ones send p/q to -p/q != p/q.
Length spectrum from SnapPy's Dirichlet domain with a tight cutoff (1.02 x core length), 60 s per filling.
(A first version with cutoff 1.5 x core over p <= 40 ran > 34 CPU-minutes and was stopped unread; this is the rerun.)
Range: p even 2..24, |q| <= 13 odd."""
import snappy, math, signal, sys, time

class TO(Exception):
    pass
def _alarm(*a):
    raise TO()
signal.signal(signal.SIGALRM, _alarm)
todo, ok, notok, timeouts = 0, 0, [], []
t0 = time.time()
for p in range(2, 25, 2):
    for q in range(-13, 14, 2):
        if math.gcd(p, abs(q)) != 1 or (p, abs(q)) in [(2, 1), (4, 1)]:
            continue
        N = snappy.Manifold("m004"); N.dehn_fill((p, q))
        try:
            S = N.symmetry_group(); certified = S.is_full_group() and str(S) == "Z/2 + Z/2"
        except Exception:
            certified = False
        if certified:
            continue
        todo += 1
        core = float(N.cusp_info()[0]["core_length"].real())
        signal.alarm(60)
        try:
            spec = N.length_spectrum(1.02 * core)
            signal.alarm(0)
            lens = [(float(g.length.real()), int(g.multiplicity)) for g in spec]
            n_at_core = sum(m for l, m in lens if abs(l - core) < 1e-6)
            n_shorter = sum(m for l, m in lens if l < core - 1e-6)
            good = (n_shorter == 0 and n_at_core == 1)
            if good:
                ok += 1
            else:
                notok.append((p, q, round(core, 6), lens[:6]))
            print("m004(%d,%d): core %.6f, geodesics up to 1.02 core: %s -> %s" % (p, q, core, lens, "unique shortest" if good else "NOT"), flush=True)
        except TO:
            timeouts.append((p, q)); print("m004(%d,%d): timeout" % (p, q), flush=True)
        except Exception as e:
            signal.alarm(0); notok.append((p, q, "err %s" % str(e)[:60])); print("m004(%d,%d): err %s" % (p, q, str(e)[:60]), flush=True)
print("uncertified hyperbolic even fillings (p <= 24): %d; core = unique shortest geodesic on %d; timeouts %d %s; %.0fs" % (
    todo, ok, len(timeouts), timeouts, time.time() - t0))
for r in notok:
    print("  NOT certified:", r)
print("b1b exit 0")
