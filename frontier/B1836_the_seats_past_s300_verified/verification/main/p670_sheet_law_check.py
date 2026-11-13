"""P-670 sweep numeric checks (read-only; mpmath only).
 (1) the sheet law jtheta(2,0,e^{i pi tau}) / series = (-i)^floor((Re tau+1)/2) on a grid
 (2) B1832 c3b T10g: frame_common.f10 (theta_2^10, theta_3^10, theta_4^10) at tau+8 against the series version
 (3) F_a powers at Re tau in [-1,1) vs outside: which powers a are sign/phase-affected
 (4) B1741-type point Re tau = 3.4: DR / b1656 th_mp do not use jtheta(2): report that th_mp(2) = explicit-root at 3.4
"""
import math, mpmath as mp
mp.mp.dps = 30
def ser2(t): return 2*mp.nsum(lambda n: mp.exp(1j*mp.pi*t*(n+mp.mpf(1)/2)**2), [0, mp.inf])
def lib2(t): return mp.jtheta(2, 0, mp.exp(1j*mp.pi*t))
print("(1) sheet law")
worst = 0
for re in [x/10 for x in range(-55, 56) if abs(abs(x/10)-1) > 1e-9 and abs(abs(x/10)-3) > 1e-9 and abs(abs(x/10)-5) > 1e-9]:
    t = mp.mpc(re, 1.1); r = lib2(t)/ser2(t); pred = mp.mpc(0, -1)**math.floor((re+1)/2)
    worst = max(worst, float(abs(r-pred)))
print("   max |ratio - (-i)^floor| over Re in [-5.5,5.5]:", worst)
print("(2) B1832 c3b T10g f10 at tau+8")
for t0 in (mp.mpc(0.23, 2.15),):
    for sh in (0, 1, 2, 3, 8, 16):
        t = t0 + sh
        a = lib2(t); b = ser2(t)
        print("   shift", sh, "Re", mp.nstr(t.real, 5), "theta2^10 lib/series =", mp.nstr(a**10/b**10, 6), " theta2^2:", mp.nstr(a**2/b**2, 4), " theta2^4:", mp.nstr(a**4/b**4, 4))
print("(3) factor (-i)^(a k) for k = floor((Re+1)/2); a=-10,-6,-2,6,10,14,18,22,26 (all = 2 mod 4 -> sign (-1)^k)")
for k in range(0, 5): print("   k", k, {a: complex(mp.mpc(0, -1)**(a*k)).real for a in (-2, 6, 10)})
print("(4) b1656 th_mp(2) style explicit q4 = exp(i pi T/4) at Re 3.4: agrees with series")
T = mp.mpc(3.4, 2.993); q4 = mp.exp(1j*mp.pi*T/4)
ex = q4*2*mp.nsum(lambda n: mp.exp(1j*mp.pi*T*n*(n+1)), [0, mp.inf])
print("   |explicit - series| =", float(abs(ex-ser2(T))), "; lib/series =", mp.nstr(lib2(T)/ser2(T), 5))
