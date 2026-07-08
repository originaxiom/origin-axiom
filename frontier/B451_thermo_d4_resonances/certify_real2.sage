# EXACT REAL period-n counts with the FULL fixed-point system (all 3 components + surface).
R.<x,y,z> = PolynomialRing(QQ, order='lex')
def T(p):
    return (2*p[0]*p[1] - p[2], p[0], p[1])
I_surf = x^2 + y^2 + z^2 - 2*x*y*z - 1 - QQ(9)/4
for n in range(1, 9):
    p = (x, y, z)
    for _ in range(n):
        p = T(p)
    Idl = R.ideal([p[0] - x, p[1] - y, p[2] - z, I_surf])
    try:
        alarm(2400)
        dim = Idl.dimension()
        if dim != 0:
            print(f"n={n}: dim {dim}", flush=True)
            cancel_alarm(); continue
        V = Idl.variety(ring=AA)
        Vc = Idl.vector_space_dimension()
        print(f"n={n}: EXACT REAL count = {len(V)}   (complex-with-mult = {Vc})", flush=True)
        cancel_alarm()
    except (AlarmInterrupt, KeyboardInterrupt):
        print(f"n={n}: TIMEOUT(40min)", flush=True)
    except Exception as e:
        print(f"n={n}: error {e}", flush=True)
print("REAL COUNTS v2 DONE", flush=True)
