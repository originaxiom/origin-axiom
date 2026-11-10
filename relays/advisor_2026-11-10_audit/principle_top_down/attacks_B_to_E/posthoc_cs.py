# POST HOC, after the sealed run of walls_and_pin.py: the Chern-Simons invariant of the run of 6 with more periods of the ground.
import warnings; warnings.filterwarnings("ignore")
import snappy
def half(x):
    y = x % 0.5
    return y - 0.5 if y > 0.25 else y
print("post hoc: the run of 6 followed by k more periods of the ground; Chern-Simons reduced modulo 1/2; volume less k+1 periods' volume")
v0 = float(snappy.Manifold("b++LR").volume())
prev = None
for k in range(0, 9):
    M = snappy.Manifold("b++" + "L" * 6 + "R" + "LR" * k)
    c = half(float(M.chern_simons())); v = float(M.volume())
    print("   k = %d   CS %+.9f   step %s   volume %.6f   volume - (k+1) x ground %.6f" % (k, c, ("%+.2e" % (c - prev)) if prev is not None else "   -   ", v, v - (k + 1) * v0))
    prev = c
for name, seq in (("(2,2,2)", lambda k: "LLRRLLR" + "LR" * k),):
    prev = None
    for k in range(0, 6):
        M = snappy.Manifold("b++" + seq(k)); c = half(float(M.chern_simons()))
        print("   %s k = %d   CS %+.9f   step %s" % (name, k, c, ("%+.2e" % (c - prev)) if prev is not None else "   -   "))
        prev = c
