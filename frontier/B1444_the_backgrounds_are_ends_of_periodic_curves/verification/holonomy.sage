# The peripheral holonomy along the twisted period-3 curve of the root:  X = u - 1,  Y = -Z,  Z^2 = 1 + 1/u^2.
# Work in the algebra A = <1, x, y, xy> (x^2 = Xx - 1, y^2 = Yy - 1, yx = Z - XY + Yx + Xy - xy); find T with
# T g = sigma(g) Phi^3(g) T for g = x, y; then  tr^2(T)/det(T) = m + 1/m + 2  and  tr [x,y] = kappa = l + 1/l.
K.<u> = FunctionField(QQ); Rt.<t> = K[]
L.<Z> = K.extension(t^2 - 1 - 1/u^2)
X = L(u - 1); Y = -Z
def mul(a, b):
    # basis 1, x, y, xy
    a0,a1,a2,a3 = a; b0,b1,b2,b3 = b
    # products of basis elements e_i e_j as 4-vectors
    return sum((ai*bj*v for i, ai in enumerate(a) for j, bj in enumerate(b) for v in [TAB[i][j]]), V0)
V = L^4; V0 = V(0)
one, ex, ey, exy = V([1,0,0,0]), V([0,1,0,0]), V([0,0,1,0]), V([0,0,0,1])
xx = X*ex - one; yy = Y*ey - one; yx = (Z - X*Y)*one + Y*ex + X*ey - exy
# x*(xy) = x^2 y = (Xx - 1) y = X xy - y ;  (xy)*y = x y^2 = Y xy - x
# y*(xy) = (yx) y = ((Z - XY) + Yx + Xy - xy) y = (Z-XY) y + Y xy + X (Yy - 1) - x(Yy - 1)... careful: xy*y = x y^2
x_xy = X*exy - ey; xy_y = Y*exy - ex
y_xy = (Z - X*Y)*ey + Y*exy + X*yy - xy_y
xy_x = None
# (xy) x = x (yx) = x((Z-XY) + Yx + Xy - xy) = (Z-XY) x + Y x^2 + X xy - x*xy
xy_x = (Z - X*Y)*ex + Y*xx + X*exy - x_xy
# (xy)(xy) = Z xy - 1
xy_xy = Z*exy - one
TAB = [[one, ex, ey, exy], [ex, xx, exy, x_xy], [ey, yx, yy, y_xy], [exy, xy_x, xy_y, xy_xy]]
def tr(a): return 2*a[0] + X*a[1] + Y*a[2] + Z*a[3]
def inv(a):
    # a^{-1} = (tr(a) - a)/det(a),  det = (tr(a)^2 - tr(a^2))/2
    d = (tr(a)^2 - tr(mul(a, a)))/2
    return (tr(a)*one - a)/d
def word(w, gx, gy):
    r = one
    for c in w:
        g = {"x": gx, "y": gy, "X": inv(gx), "Y": inv(gy)}[c]; r = mul(r, g)
    return r
def Phi(word_letters, k):
    gx, gy = ex, ey
    # automorphism word applied k times: L: x->x, y->yx ; R: x->xy, y->y   (images of the generators as algebra elements)
    imgs = ("x", "y")
    def comp(im, letter):
        ix, iy = im
        sub = {"L": {"x": "x", "y": "yx"}, "R": {"x": "xy", "y": "y"}}[letter]
        low = {"x": "X", "y": "Y"}
        def s(wd):
            out = ""
            for c in wd:
                if c in "xy": out += sub[c]
                else: out += "".join(low[d] for d in reversed(sub[c.lower()]))
            return out
        return (s(ix), s(iy))
    for _ in range(k):
        for c in reversed(word_letters): imgs = comp(imgs, c)      # Phi = tau_{w1} o tau_{w2} o ... (the convention of periodic_curves.sage)
    return imgs
wx, wy = Phi("LR", 3)
print("Phi^3(x) =", wx, "  Phi^3(y) =", wy)
Px, Py = word(wx, ex, ey), word(wy, ex, ey)
print("check traces: tr Phi^3(x) / X =", tr(Px)/X, "  tr Phi^3(y)/Y =", tr(Py)/Y, "  tr(Phi^3(x)Phi^3(y))/Z =", tr(mul(Px, Py))/Z)
sx, sy = tr(Px)/X, tr(Py)/Y
# solve T x = sx Px T,  T y = sy Py T
def lin(g, P, s):
    cols = []
    for b in (one, ex, ey, exy): cols.append(mul(b, g) - s*mul(P, b))
    return matrix(L, cols).transpose()
M = lin(ex, Px, sx).stack(lin(ey, Py, sy))
ker = M.right_kernel()
print("dim of solutions T:", ker.dimension())
T = V(ker.basis()[0])
dT = (tr(T)^2 - tr(mul(T, T)))/2
mm = tr(T)^2/dT                     # = m + 1/m + 2
kap = X^2 + Y^2 + Z^2 - X*Y*Z - 2
print("kappa =", kap)
print("m + 1/m + 2 =", mm)
w = L(u - 1/u)
print("kappa - 2 - w(w-1) =", kap - 2 - w*(w-1))
print("m + 1/m - 2 =", mm - 4, "   norm:", (mm - 4).norm().factor())
print("l + 1/l - 2 =", kap - 2)
