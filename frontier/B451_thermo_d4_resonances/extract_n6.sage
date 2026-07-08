R.<x,y,z> = PolynomialRing(QQ, order='lex')
def T(p):
    return (2*p[0]*p[1] - p[2], p[0], p[1])
I_surf = x^2 + y^2 + z^2 - 2*x*y*z - 1 - QQ(9)/4
p = (x, y, z)
for _ in range(6):
    p = T(p)
Idl = R.ideal([p[0] - x, p[1] - y, p[2] - z, I_surf])
V = Idl.variety(ring=AA)
print(f"{len(V)} points")
for v in V:
    print(f"{float(v[x]):.15f} {float(v[y]):.15f} {float(v[z]):.15f}", flush=True)
