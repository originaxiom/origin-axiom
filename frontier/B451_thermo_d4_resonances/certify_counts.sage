# B451 boundary compute: EXACT period-n point counts on the lambda=3 surface
# via Groebner degree — certifies the numeric enumeration's completeness per n.
R.<x,y,z> = PolynomialRing(QQ, order='degrevlex')
def T(p):
    return (2*p[0]*p[1] - p[2], p[0], p[1])
I_surf = x^2 + y^2 + z^2 - 2*x*y*z - 1 - QQ(9)/4
import signal
for n in range(1, 9):
    p = (x, y, z)
    for _ in range(n):
        p = T(p)
    ideal_gens = [p[0] - x, p[1] - y, I_surf]
    Idl = R.ideal(ideal_gens)
    try:
        alarm(1800)
        dim = Idl.dimension()
        if dim == 0:
            deg = Idl.vector_space_dimension()
            print(f"n={n}: dim 0, EXACT point count (with multiplicity) = {deg}", flush=True)
        else:
            print(f"n={n}: dim {dim} (unexpected)", flush=True)
        cancel_alarm()
    except (AlarmInterrupt, KeyboardInterrupt):
        print(f"n={n}: TIMEOUT(30min)", flush=True)
print("COUNTS DONE", flush=True)
