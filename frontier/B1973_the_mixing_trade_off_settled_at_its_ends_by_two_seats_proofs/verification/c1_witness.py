"""B1973: main's own check of the agy lane's C1-A witness (2026-11-24): B1736's Y(h; u, 0) = u h^T + h u^T - (u.h) 1 in the null triad
e+ = (1, i, 0)/sqrt2, e- = conj(e+), e3 = (0, 0, 1); h = c+ e- + c- e+ with 2 c+ c- = r, c+^2 + c-^2 = 1; u_down = e+ + (4/1000) e-,
u_up = (1/80000) e+ + e-; at r = 1/2000.  Readings: (a) the one-doublet charge rule (up reads conj h, down reads h), B1969's
question; (b) every sector reading h."""
import mpmath as mp
mp.mp.dps = 60
s2 = mp.sqrt(2); ep = mp.matrix([1 / s2, 1j / s2, 0]); em = mp.matrix([1 / s2, -1j / s2, 0]); e3 = mp.matrix([0, 0, 1])
dot = lambda a, b: sum(a[i] * b[i] for i in range(3))
def Y(h, u):
    M = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3): M[i, j] = u[i] * h[j] + h[i] * u[j] - (dot(u, h) if i == j else 0)
    return M
def U_sv(M):
    U, S, V = mp.svd_c(M); order = sorted(range(3), key=lambda i: S[i]); return mp.matrix([[U[r, order[c]] for c in range(3)] for r in range(3)]), [S[i] for i in order]
r = mp.mpf(1) / 2000; cp = mp.sqrt((1 + mp.sqrt(1 - r ** 2)) / 2); cm = r / (2 * cp)
h = cp * em + cm * ep; hb = mp.matrix([mp.conj(x) for x in h])
print("unit h:", mp.nstr(mp.sqrt(sum(abs(x) ** 2 for x in h)), 10), "| h.h =", mp.nstr(dot(h, h), 10))
ud = ep + mp.mpf(4) / 1000 * em; uu = mp.mpf(1) / 80000 * ep + em
for name, hu in (("(a) charge rule: up conj h, down h", hb), ("(b) every sector h", h)):
    Uu, Su = U_sv(Y(hu, uu)); Ud, Sd = U_sv(Y(h, ud)); V = Uu.H * Ud
    off = max(abs(V[i, j]) for i in range(3) for j in range(3) if i != j); diag = min(abs(V[i, i]) for i in range(3))
    print(name, "| least diagonal |V| %s, largest off-diagonal %s | up m2/m3 %s, m1/m2 %s | down m2/m3 %s, m1/m2 %s" % (
        mp.nstr(diag, 8), mp.nstr(off, 3), mp.nstr(Su[1] / Su[2], 5), mp.nstr(Su[0] / Su[1], 5), mp.nstr(Sd[1] / Sd[2], 5), mp.nstr(Sd[0] / Sd[1], 5)))
