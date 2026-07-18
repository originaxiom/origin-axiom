import mpmath as mp
mp.mp.dps = 70

# Vol(4_1) two independent ways
# (i) Bloch-Wigner dilog at the cusp shape: Vol = 2*D(exp(i*pi/3)), D=Bloch-Wigner
z = mp.e**(1j*mp.pi/3)
D = mp.im(mp.polylog(2,z)) + mp.arg(1-z)*mp.log(abs(z))
Vol_bw = 2*D
# (ii) (3 sqrt3/2) L(chi_-3, 2)  (B680)
def Lchi(s):
    # L(chi_-3,s) = sum chi(n)/n^s, chi = Kronecker(-3,.): +1 if n=1mod3, -1 if n=2mod3
    return (mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))/3**s
Vol_L = (3*mp.sqrt(3)/2)*Lchi(2)
print("Vol (Bloch-Wigner) =", mp.nstr(Vol_bw,55))
print("Vol (3sqrt3/2 L)   =", mp.nstr(Vol_L,55))
print("diff               =", mp.nstr(Vol_bw-Vol_L,5))

Vol = Vol_bw

# Mahler measure at dps 70 with exact breakpoints
def integrand(theta):
    M = mp.e**(1j*theta)
    B = M**8 - M**6 - 2*M**4 - M**2 + 1
    disc = B*B - 4*M**8
    s = mp.sqrt(disc)
    L1 = (B + s)/(2*M**4); L2 = (B - s)/(2*M**4)
    mm = max(abs(L1), abs(L2))
    return mp.log(mm) if mm > 1 else mp.mpf(0)
pi = mp.pi
piece = mp.quad(integrand, [mp.mpf(0), pi/3])
print("one support piece  =", mp.nstr(piece,55))
print("Vol/2              =", mp.nstr(Vol/2,55))
print("piece - Vol/2      =", mp.nstr(piece - Vol/2,5))
m_A = 4*piece/(2*pi)
print("m(A_41)            =", mp.nstr(m_A,55))
print("Vol/pi             =", mp.nstr(Vol/pi,55))
print("m(A_41) - Vol/pi   =", mp.nstr(m_A - Vol/pi,5))
