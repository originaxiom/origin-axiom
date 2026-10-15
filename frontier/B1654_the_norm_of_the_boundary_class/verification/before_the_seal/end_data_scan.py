"""C1 exploration (main, unsealed): D(tau) = sum_r c_r R_r^2 over the fundamental domain; zeros; the cusp."""
import numpy as np, end_data_defect as m
def c_fixed(r, tau, rho=0.05):
    tot, _ = m.c_r(r, tau, rho, Nth=800, Nr=80)
    s1 = m.laurent(r, tau, 1); s3 = m.laurent(r, tau, 3)
    return tot + abs(s1)**2*np.pi*rho**4/2 + abs(s3)**2*np.pi*rho**8/4
def Dhat(tau):
    Rt = m.R_triplet(tau); cs = {r: c_fixed(r, tau) for r in (2, 3, 4)}
    nR2 = sum(abs(Rt[r])**2 for r in (2, 3, 4))
    return sum(cs[r]*Rt[r]**2 for r in (2, 3, 4))/nR2, cs
print("imaginary axis: y, |q|, D/|R|^2, c2, c3, c4, D/(y|q|)")
for y in [1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]:
    d, cs = Dhat(complex(0, y)); q = np.exp(-np.pi*y)
    print(f"  {y:4.2f} {q:.3e} {d.real:+.6e}{d.imag:+.1e}j  {cs[2]:9.4f} {cs[3]:9.4f} {cs[4]:9.4f}  {abs(d)/(y*q):.4f}")
w = np.exp(2j*np.pi/3)
print("approach to omega along tau = omega + t*(i): t, |D|/|R|^2")
for t in [0.2, 0.1, 0.05, 0.025, 0.0125]:
    d, _ = Dhat(w + 1j*t); print(f"  {t:.4f} {abs(d):.4e}  ratio-to-t {abs(d)/t:.4f}")
print("grid over the fundamental domain |x|<=1/2, |tau|>=1, y<=2: min |D|/|R|^2")
best = []
for x in np.linspace(-0.5, 0.5, 11):
    for y in np.linspace(0.87, 2.0, 10):
        tau = complex(x, y)
        if abs(tau) < 0.999: continue
        d, _ = Dhat(tau); best.append((abs(d), x, y))
best.sort(); print("  smallest five:", [(round(a,5), round(x,2), round(y,3)) for a, x, y in best[:5]])
