"""Check 3: the motion. Lemma 21 (automorphy of D), f = |D|/|rho|^2, the cusp law (Prop 16),
the constant mode 0.31500491 (Census 32), the period phase (Thm 22 / Census 23), escape rates (Census 31),
word/geometry counts (Lemma 4 remark, Census 5)."""
import mpmath as mp, numpy as np, itertools, math
from math import gcd
mp.mp.dps = 30
PI = mp.pi

def thetas(t):
    q = mp.exp(1j*PI*t)
    return mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
def eta(t):
    q = mp.exp(2j*PI*t)
    return mp.exp(2j*PI*t/24) * mp.nprod(lambda n: 1 - q**n, [1, mp.inf])
def h(lam): return lam*mp.log(abs(lam)) + (1-lam)*mp.log(abs(1-lam))
def D(t):
    t2, t3, t4 = thetas(t)
    lam = t2**4/t3**4
    return -t3**4*h(lam)/(4*PI*eta(t)**6)
def rho2(t):
    t2, t3, t4 = thetas(t); e = eta(t)
    return (abs(t2)**4 + abs(t3)**4 + abs(t4)**4)/(4*PI**2*abs(e)**6)
def f(t):
    return abs(D(t))/rho2(t)

print("=== Lemma 21: automorphy of D (weight -1, multiplier of eta^6) ===")
for t in [mp.mpc(0.13, 1.21), mp.mpc(-0.31, 0.95)]:
    d = D(t)
    print("tau =", mp.nstr(t, 5))
    print("   D(tau+1) - i D(tau)              =", mp.nstr(D(t+1) - 1j*d, 3))
    print("   D(-1/tau) - i tau^-1 D(tau)      =", mp.nstr(D(-1/t) - 1j/t*d, 3))
    print("   D(tau/(tau+1)) +i (tau+1)^-1 D   =", mp.nstr(D(t/(t+1)) + 1j/(t+1)*d, 3), "   [R: chi=-i]")
    print("   D(-1/(tau+1)) + (tau+1)^-1 D     =", mp.nstr(D(-1/(t+1)) + 1/(t+1)*d, 3), "   [L^-1 R: chi=-1]")
    print("   f(tau) - f(-1/tau) =", mp.nstr(f(t) - f(-1/t), 3), "  f(tau) - f(tau+1) =", mp.nstr(f(t) - f(t+1), 3))
w = mp.exp(2j*PI/3)
print("f(omega) =", mp.nstr(f(w), 5), "   f(i) =", mp.nstr(f(1j), 10), "  (pi/2) ln 2 =", mp.nstr(PI/2*mp.log(2), 10), "  D(omega) =", mp.nstr(D(w), 3))

print("\n=== Prop 16 cusp law: D/(q |rho|^2) vs e^{-i pi x/2}(8 pi^2 y + 4 pi (1+e^{-2 pi i x}) - 32 pi ln2) ===")
for x in [0, mp.mpf(3)/10, mp.mpf(1)/2, 1]:
    for y in [4, 5]:
        t = mp.mpc(x, y); q = mp.exp(1j*PI*t)
        lhs = D(t)/(q*rho2(t))
        pred = mp.exp(-1j*PI*x/2)*(8*PI**2*y + 4*PI*(1 + mp.exp(-2j*PI*x)) - 32*PI*mp.log(2))
        pred0 = 8*PI**2*y + 8*PI*(1 - 4*mp.log(2))
        print(f"x={float(x):.2f} y={y}: D/(q|rho|^2) = {mp.nstr(lhs,10)}  predicted = {mp.nstr(pred,10)}  rel.err = {mp.nstr(abs(lhs-pred)/abs(pred),3)}" + ("" if x != 0 else f"   [x=0 form {mp.nstr(pred0,10)}]"))

print("\n=== Census 32(1): the constant mode (3/pi) * int_F f dmu ===")
# numpy implementation of f on a grid (double precision suffices)
def f_np(x, y):
    tau = x + 1j*y
    q = np.exp(1j*np.pi*tau)
    n = np.arange(1, 25)
    # theta constants with nome q: th3 = 1 + 2 sum q^{n^2}, th4 = 1 + 2 sum (-1)^n q^{n^2}, th2 = 2 sum q^{(n-1/2)^2}
    qn2 = q[..., None]**(n**2)
    th3 = 1 + 2*np.sum(qn2, axis=-1)
    th4 = 1 + 2*np.sum((-1.0)**n * qn2, axis=-1)
    th2 = 2*np.sum(q[..., None]**((n - 0.5)**2), axis=-1)
    lam = th2**4/th3**4
    hh = lam*np.log(np.abs(lam)) + (1 - lam)*np.log(np.abs(1 - lam))
    return np.pi*np.abs(th3**4*hh)/(np.abs(th2)**4 + np.abs(th3)**4 + np.abs(th4)**4)
print("f_np(i) =", f_np(0.0, 1.0), " f_np(omega) =", f_np(-0.5, np.sqrt(3)/2), " f(0.13+1.21i) mp =", mp.nstr(f(mp.mpc(0.13,1.21)), 12), " np =", f_np(0.13, 1.21))
from numpy.polynomial.legendre import leggauss
def integrate(nx, ny, ymax):
    xs, wx = leggauss(nx); xs = 0.5*xs; wx = 0.5*wx            # x in [-1/2, 1/2]
    total = 0.0
    ys0, wy0 = leggauss(ny)
    for xi, wxi in zip(xs, wx):
        y0 = np.sqrt(1 - xi**2)
        # map [-1,1] -> [y0, ymax] with a substitution concentrating points near y0: y = y0 + (ymax-y0)*((u+1)/2)^2
        u = ys0; yy = y0 + (ymax - y0)*((u + 1)/2)**2; dy = (ymax - y0)*(u + 1)/2
        vals = f_np(np.full_like(yy, xi), yy)/yy**2
        total += wxi*np.sum(wy0*vals*dy)
    return 3/np.pi*total
for nx, ny, ymax in [(60, 120, 10.0), (120, 240, 12.0), (200, 400, 14.0)]:
    print(f"  nx={nx} ny={ny} ymax={ymax}: <f> = {integrate(nx, ny, ymax):.10f}")
print("  paper: 0.31500491")

print("\n=== Theorem 22 / Census 23: the period phase psi(s+l) = i^{#L-#R} psi(s) ===")
Lm = mp.matrix([[1, 1], [0, 1]]); Rm = mp.matrix([[1, 0], [1, 1]])
def word_matrix(wd):
    M = mp.eye(2)
    for c in wd: M = M*(Lm if c == 'L' else Rm)
    return M
def period_phase(wd, s_values=(0.0, 0.7, 1.9), nsamp=4000):
    g = word_matrix(wd)
    a, b, c, d = g[0,0], g[0,1], g[1,0], g[1,1]
    tr = a + d
    lam = (tr + mp.sqrt(tr**2 - 4))/2          # eigenvalue > 1
    ell = 2*mp.log(lam)
    # fixed points: c x^2 + (d - a) x - b = 0 ; attracting = the one with eigenvalue lam: (x,1) eigenvector => c x + d = lam
    disc = mp.sqrt((d - a)**2 + 4*b*c)
    roots = [(-(d - a) + disc)/(2*c), (-(d - a) - disc)/(2*c)]
    xp = roots[0] if abs(c*roots[0] + d - lam) < abs(c*roots[1] + d - lam) else roots[1]
    xm = roots[1] if xp == roots[0] else roots[0]
    sig = 1 if xp > xm else -1
    def z_of(s):
        wv = 1j*mp.exp(s)
        return (xp*wv + sig*xm)/(wv + sig)
    def dz_ds(s):
        wv = 1j*mp.exp(s)
        return sig*(xp - xm)/(wv + sig)**2 * 1j*mp.exp(s)
    out = []
    for s0 in s_values:
        ss = [s0 + ell*k/nsamp for k in range(nsamp + 1)]
        # unwrap the phase of dz/ds along s
        phases = []; prev = None; acc = 0
        for s in ss:
            ph = mp.arg(dz_ds(s))
            if prev is not None:
                dph = ph - prev
                if dph > PI: acc -= 2*PI
                elif dph < -PI: acc += 2*PI
            phases.append(ph + acc); prev = ph
        def root_inv(s, ph): return abs(dz_ds(s))**(-0.5)*mp.exp(-1j*ph/2)
        z0, z1 = z_of(ss[0]), z_of(ss[-1])
        psi0 = D(z0)*root_inv(ss[0], phases[0]); psi1 = D(z1)*root_inv(ss[-1], phases[-1])
        r = root_inv(ss[-1], phases[-1])/root_inv(ss[0], phases[0])   # continuation ratio of (dz/ds)^{-1/2}
        out.append((psi1/psi0, r*(1/(c*z0 + d))**(-1), c*z0 + d, z0, z1 - (a*z0 + b)/(c*z0 + d)))
    return ell, out
for wd in ["LR", "LLR", "LLLR", "LLLLLR", "LLRR", "LRLLR", "LLLLRRL", "LRRRRR"]:
    nL, nR = wd.count('L'), wd.count('R')
    ell, out = period_phase(wd)
    exp_phase = 1j**((nL - nR) % 4)
    print(f"{wd:9s} #L-#R={nL-nR:+d} expected i^(#L-#R)={exp_phase}: length={mp.nstr(ell,6)}")
    for ratio, rr, czd, z0, gap in out:
        print(f"     psi(s+l)/psi(s) = {mp.nstr(ratio, 8)}   branch ratio r/(cz+d) = {mp.nstr(rr, 6)}   cz+d = {mp.nstr(czd,5)}   |z(s+l) - gamma z(s)| = {mp.nstr(abs(gap),2)}")

print("\n=== Census 31: escape rates (Monte Carlo, drift of d(i, g i) per step) ===")
rng = np.random.default_rng(7)
Lf = np.array([[1., 1.], [0., 1.]]); Rf = np.array([[1., 0.], [1., 1.]])
Li = np.linalg.inv(Lf); Ri = np.linalg.inv(Rf)
def run(p, nsteps=4000, nruns=40):
    rates = []; sides = []
    for r in range(nruns):
        g = np.eye(2); logscale = 0.0
        for n in range(nsteps):
            u = rng.random()
            if u < p: m = Li if rng.random() < 0.5 else Ri
            else:     m = Lf if rng.random() < 0.5 else Rf
            g = g @ m
            nrm = np.linalg.norm(g)
            g /= nrm; logscale += np.log(nrm)
        # d(i, g i) = arccosh(||g||_F^2 / 2); with ||g||_F^2 = e^{2 logscale} * ||g_normalized||^2 (=1): d ~ 2 logscale - log 2
        rates.append((2*logscale - np.log(2))/nsteps)
        # side: the limit point xi = lim g(i) is g[0,0]/g[1,0] approx (first column direction)
        sides.append(g[0, 0]*g[1, 0] > 0)
    return np.mean(rates), np.std(rates)/np.sqrt(nruns), np.mean(sides)
for p in [0.0, 0.1, 0.3, 0.5]:
    m, se, side = run(p)
    print(f"  p={p}: escape rate {m:.4f} +- {se:.4f} per step (paper: p=0 -> 0.3959, p=1/2 -> 0.1007);  P(xi>0) ~ {side:.3f}")

print("\n=== word and geometry counts ===")
def mat_of(wd):
    M = np.eye(2, dtype=object)
    for ch in wd: M = M @ (np.array([[1,1],[0,1]], dtype=object) if ch == 'L' else np.array([[1,0],[1,1]], dtype=object))
    return M
words = []
for n in range(2, 9):
    for bits in itertools.product('LR', repeat=n):
        wd = ''.join(bits)
        if 'L' in wd and 'R' in wd: words.append(wd)
odd = sum(1 for wd in words if (mat_of(wd)[0,0] + mat_of(wd)[1,1]) % 2 == 1)
print("words of length 2..8 with both letters:", len(words), " x2 signs =", 2*len(words), " (paper: 988);  odd trace:", odd, " x2 =", 2*odd, " (paper: 448)")
def canon(wd, swap=True):
    rots = [wd[i:] + wd[:i] for i in range(len(wd))]
    if swap:
        sw = wd.translate(str.maketrans('LR', 'RL'))
        rots += [sw[i:] + sw[:i] for i in range(len(sw))]
    return min(rots)
def primitive(wd):
    n = len(wd)
    return all(wd != wd[:n//k]*k for k in range(2, n+1) if n % k == 0)
geoms = {canon(wd) for wd in words if primitive(wd)}
odd_g = sum(1 for wd in geoms if (mat_of(wd)[0,0] + mat_of(wd)[1,1]) % 2 == 1)
print("geometries (primitive cyclic words to length 8 up to rotation and L<->R):", len(geoms), " odd trace:", odd_g, " even:", len(geoms) - odd_g, " (paper: 37 = 16 + 21)")
classes12 = set(); classes12_sw = set()
for n in range(2, 13):
    for bits in itertools.product('LR', repeat=n):
        wd = ''.join(bits)
        if 'L' in wd and 'R' in wd and primitive(wd):
            classes12.add(canon(wd, swap=False)); classes12_sw.add(canon(wd, swap=True))
print("primitive cyclic words to length 12 (up to rotation):", len(classes12), " (up to rotation and swap):", len(classes12_sw), "  (paper's 'every state remains': 758)")
