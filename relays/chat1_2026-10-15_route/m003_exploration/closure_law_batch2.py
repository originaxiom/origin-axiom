# EXPLORATION: test the conjectured closure law on unseen threads, lines, orders and charges.
#   phase(sector) = exp(-2 pi i c (qL^2 + qR^2) / N),  c = eps * Q_gamma(w) / N,
#   Q_gamma(a, b) = C a^2 + (A - D) a b - B b^2, gamma = [[A, B], [C, D]], w = (a, b)/N with (a,b)gamma == eps (a,b) mod N
# Quaternion u_s = c_s T_s(ubar) T_s(delta) / theta1', thetas as series in tau; ubar = (qL+qR) w, delta = (qL-qR) w.
import mpmath as mp, math, random
mp.mp.dps = 30
def theta(n, z, tau, M=60):
    e = lambda x: mp.exp(1j * mp.pi * x)
    if n == 3: return mp.fsum(e(k*k*tau + 2*k*z) for k in range(-M, M+1))
    if n == 4: return mp.fsum((-1)**(k % 2) * e(k*k*tau + 2*k*z) for k in range(-M, M+1))
    if n == 2: return mp.fsum(e((k+0.5)**2*tau + 2*(k+0.5)*z) for k in range(-M, M+1))
    if n == 1: return mp.fsum(-1j*(-1)**(k % 2) * e((k+0.5)**2*tau + 2*(k+0.5)*z) for k in range(-M, M+1))
def th1p(tau):  # theta1'(0) = 2 pi eta^3 via the series derivative
    e = lambda x: mp.exp(1j * mp.pi * x)
    return mp.fsum(-1j*(-1)**(k % 2) * 2j*mp.pi*(k+0.5) * e((k+0.5)**2*tau) for k in range(-30, 31))
CH = [(1, -1j), (2, -1), (4, -1), (3, 1j)]
def T(n, al, be, tau): return mp.exp(1j*mp.pi*al*al*tau + 2j*mp.pi*al*be) * theta(n, be + al*tau, tau)
def quat(tau, ub, de): return [c * T(n, *ub, tau) * T(n, *de, tau) / th1p(tau) for n, c in CH]
def mat(w):
    M = [[1,0],[0,1]]
    for ch in w:
        X = [[1,0],[1,1]] if ch == "L" else [[1,1],[0,1]]
        M = [[M[0][0]*X[0][0]+M[0][1]*X[1][0], M[0][0]*X[0][1]+M[0][1]*X[1][1]],
             [M[1][0]*X[0][0]+M[1][1]*X[1][0], M[1][0]*X[0][1]+M[1][1]*X[1][1]]]
    return M
random.seed(7)
tests, worst = 0, 0.0
cases = [("LLLLRLR", 7), ("LLLR", 7), ("LLLRLR", 11), ("LLLRLRR", 9), ("LRLRRR", 11), ("LLRLLRR", 5)]
for word, N in cases:
    (A, B), (C, D) = mat(word)
    tau = mp.mpc(random.uniform(-0.4, 0.4), random.uniform(0.9, 1.3))
    tg = (A*tau + B) / (C*tau + D); J = C*tau + D
    R0, Rg = quat(tau, (0,0), (0,0)), quat(tg, (0,0), (0,0))
    perm = {s: min(range(1,4), key=lambda t: abs(abs(Rg[s])*abs(J)**0.5 - abs(R0[t]))) for s in range(1,4)}
    fac = {s: Rg[s]*mp.sqrt(J)/R0[perm[s]] for s in range(1,4)}
    found = 0
    for eps in (1, -1):
        for a in range(N):
            for b in range(N):
                if (a, b) == (0, 0) or math.gcd(math.gcd(a, b), N) != 1: continue
                if ((a*D + b*B) - eps*a) % N or ((a*C + b*A) - eps*b) % N: continue
                Q = C*a*a + (A - D)*a*b - B*b*b
                c = eps * Q // N
                for (qL, qR) in [(1, -4), (1, 2), (-3, 6), (random.randint(-6, 6), random.randint(-6, 6))]:
                    ub, de = ((qL+qR)*b/N, (qL+qR)*a/N), ((qL-qR)*b/N, (qL-qR)*a/N)
                    u0, ug = quat(tau, ub, de), quat(tg, ub, de)
                    rs = [ug[s]*mp.sqrt(J)/u0[perm[s]]/fac[s] for s in range(1,4) if abs(u0[perm[s]]) > 1e-15]
                    if not rs: continue
                    pred = mp.exp(-2j*mp.pi*c*(qL*qL + qR*qR)/N)
                    dev = max(min(abs(r - pred), abs(r + pred)) for r in rs)   # +-1 is the -I lift's convention
                    worst = max(worst, float(dev)); tests += 1; found += 1
    print(f"{word:8s} N={N}: gamma=[[{A},{B}],[{C},{D}]], cases tested {found}", flush=True)
print("tests", tests, "worst |phase - predicted| (up to sign):", worst)
