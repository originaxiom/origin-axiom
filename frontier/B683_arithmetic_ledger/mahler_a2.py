import mpmath as mp
mp.mp.dps = 55

def Bpoly(M):
    return M**8 - M**6 - 2*M**4 - M**2 + 1

def integrand(theta):
    M = mp.e**(1j*theta)
    B = Bpoly(M)
    disc = B*B - 4*M**8
    s = mp.sqrt(disc)
    denom = 2*M**4
    L1 = (B + s)/denom; L2 = (B - s)/denom
    m = max(abs(L1), abs(L2))
    return mp.log(m) if m > 1 else mp.mpf(0)

pi = mp.pi
# exact breakpoints (kinks) at pi/3,2pi/3,pi,4pi/3,5pi/3 and touch-zeros at 0,pi,2pi
bp = [mp.mpf(0), pi/3, 2*pi/3, pi, 4*pi/3, 5*pi/3, 2*pi]
I = mp.quad(integrand, bp)
m_A = I/(2*pi)
print("m(A_41) =", mp.nstr(m_A, 45))

# independent check: integrate only support pieces, use symmetry
Ia = mp.quad(integrand, [mp.mpf(0), pi/3])
Ib = mp.quad(integrand, [2*pi/3, pi])
# by theta->2pi-theta and theta->pi symmetry total = 4*(Ia+Ib)? verify numerically
Ic = mp.quad(integrand, [pi, 4*pi/3])
Id = mp.quad(integrand, [5*pi/3, 2*pi])
print("pieces:", mp.nstr(Ia,20), mp.nstr(Ib,20), mp.nstr(Ic,20), mp.nstr(Id,20))
tot = (Ia+Ib+Ic+Id)/(2*pi)
print("m(A_41) [pieces] =", mp.nstr(tot,45))

# also Vol/(2pi)
Vol = mp.mpf('2.029883212819307250042405108549040571883')
print("Vol/(2pi) =", mp.nstr(Vol/(2*pi), 45))
print("ratio m/(Vol/2pi) =", mp.nstr(m_A/(Vol/(2*pi)), 40))
print("ratio (Vol/2pi)/m =", mp.nstr((Vol/(2*pi))/m_A, 40))
