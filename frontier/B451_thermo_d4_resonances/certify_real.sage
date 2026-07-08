# EXACT REAL period-n point counts (variety over AA) — the zeta function's objects.
R.<x,y,z> = PolynomialRing(QQ, order='lex')
def T(p):
    return (2*p[0]*p[1] - p[2], p[0], p[1])
I_surf = x^2 + y^2 + z^2 - 2*x*y*z - 1 - QQ(9)/4
for n in range(1, 8):
    p = (x, y, z)
    for _ in range(n):
        p = T(p)
    Idl = R.ideal([p[0] - x, p[1] - y, I_surf])
    try:
        alarm(2400)
        V = Idl.variety(ring=AA)
        print(f"n={n}: EXACT REAL point count = {len(V)}", flush=True)
        cancel_alarm()
    except (AlarmInterrupt, KeyboardInterrupt):
        print(f"n={n}: TIMEOUT(40min)", flush=True)
    except Exception as e:
        print(f"n={n}: error {e}", flush=True)
print("REAL COUNTS DONE", flush=True)
