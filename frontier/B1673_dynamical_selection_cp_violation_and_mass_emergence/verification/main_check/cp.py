import numpy as np, cmath
om=complex(-0.5,3**.5/2)
gs=[(2,3),(2,4),(3,2),(3,4),(4,2),(4,3),(5,6),(5,7),(6,5),(6,7),(7,5),(7,6)]
def inlat(z):
    # z in Z+Z om ?
    b=z.imag/om.imag; a=z.real-b*om.real
    return abs(b-round(b))<1e-9 and abs(a-round(a))<1e-9
zeta=[cmath.exp(2j*cmath.pi*k/6) for k in range(6)]
def even(z): return any(inlat(zt*z.conjugate()-z) for zt in zeta)
true=[(a*om-b)/9 for a,b in gs]
print("true complex points: fixed by reflection:",[even(z) for z in true])
# arc's (wrong?) reading a+b*om
arc=[(a+b*om)/9 for a,b in gs]
print("arc reading a+b om:",sum(even(z) for z in arc),"of 12")
# also classify all 72 on both readings
o9=[(a,b) for a in range(9) for b in range(9) if a%3 or b%3]
print("true reading cp-even among 72:",sum(even((a*om-b)/9) for a,b in o9))
# test: is the set closed under the 6 reflections & mu6 (true)?
S=lambda z:{(round((z.imag/om.imag*9))%9, round(((z.real-z.imag/om.imag*om.real)*9))%9)} 
def key(z):
    z=z; b=z.imag/om.imag; a=z.real-b*om.real
    return (round(b*9)%9, round(a*9)%9)  # (coef om, const)
keys={ (a%9,(-b)%9) for a,b in gs}
ok=all(key(zt*z.conjugate()) in keys for zt in zeta for z in true)
ok2=all(key(zt*z) in keys for zt in zeta for z in true)
print("closed under reflections",ok,"under mu6",ok2)
