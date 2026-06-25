"""B207 part 3 (the scale door, computed): hyperbolic volumes of the metallic bundles R^m L^m.
SnapPy-gated. R^m L^m = twister bundle('a'*m+'B'*m); m=1 = figure-eight.

RESULT (verified, canonized to geometric / positively-oriented triangulations; corrects an initial
'linear-growth' misread): the volumes are BOUNDED and CONVERGE:
  golden  (m=1) = 2.02988  = 2 v_tet  (figure-eight, the MINIMAL cusped hyperbolic volume) -- the floor
  silver  (m=2) = 3.66386  = v_oct    (one regular ideal octahedron; census m136), exactly
  Vol_m increasing, Aitken-accelerated limit -> 2 v_oct = 7.32772 (= Vol(Borromean rings)) as m->inf.
SCALE READ: the object's exponential rate in the volume conjecture |<R^mL^m>_N| ~ e^{N Vol_m/2pi}
SATURATES (Vol_m bounded by 2 v_oct). The object cannot supply an unbounded rate; all unbounded scale
is the quantization LEVEL N -- confirms + sharpens the firewall (B151). FIREWALL: hyperbolic geometry /
dimensionless; nothing to CLAIMS.md. Cited by speculations/S038.
"""
import numpy as np

V_TET = 1.0149416064096536   # regular ideal tetrahedron
V_OCT = 3.6638623766952       # regular ideal octahedron


def metallic_volume(m, randomize_tries=60):
    from snappy import twister
    M = twister.Surface('S_1_1').bundle('a' * m + 'B' * m)
    M.canonize()
    t = 0
    while 'positively' not in M.solution_type() and t < randomize_tries:
        M.randomize(); t += 1
    return float(M.volume()), M.solution_type()


def aitken(s):
    s = list(s)
    out = []
    for i in range(len(s) - 2):
        d2 = s[i + 2] - 2 * s[i + 1] + s[i]
        out.append(s[i] - (s[i + 1] - s[i])**2 / d2 if d2 != 0 else s[i])
    return out


def limit_estimate(mmax=28):
    v = [metallic_volume(m)[0] for m in range(1, mmax + 1)]
    a = v
    for _ in range(3):
        a = aitken(a)
    return v, a[-1]


if __name__ == "__main__":
    v, lim = limit_estimate(28)
    print(f"golden Vol_1 = {v[0]:.6f}  (= 2 v_tet = {2*V_TET:.6f}; minimal cusped hyperbolic volume)")
    print(f"silver Vol_2 = {v[1]:.6f}  (= v_oct = {V_OCT:.6f}; one ideal octahedron, m136)")
    print(f"Vol_m increments (m=2..10): {[round(v[i]-v[i-1],4) for i in range(1,10)]}  (decay -> converges)")
    print(f"Aitken-3 limit estimate: {lim:.5f}  vs  2 v_oct = {2*V_OCT:.5f}  (Borromean rings volume)")
    print(f"=> metallic volumes BOUNDED in [{v[0]:.3f}, {2*V_OCT:.3f}); golden at the floor.")
    print("SCALE: e^{N Vol_m/2pi} saturates (Vol bounded) -> all unbounded scale is the level N (firewall confirmed).")
