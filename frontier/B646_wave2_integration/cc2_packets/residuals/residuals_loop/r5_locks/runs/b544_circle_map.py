"""B544 reimplementation: 'critical circle map bisection -> winding 0.618033989 = 1/phi
to 9 digits at Omega* ~ 0.6066553 (Shenker's constant)'. No script exists in
frontier/B544_emergent_golden/ -- FINDINGS.md calls this its own 'spot verification'
(distinct from chat-2's original FK-ground-state and 99.95%-itinerary claims, which are
NOT independently re-derived anywhere in the repo and are NOT attempted here -- see the
report for why those are marked UNREPRODUCIBLE).

Method (standard renormalization-theory technique, Feigenbaum-Kadanoff-Shenker /
Ostlund-Rand-Sethna-Siggia): critical (K=1) sine circle map lifted to R,
    f(theta) = theta + Omega - sin(2 pi theta)/(2 pi)
has its unique critical (cubic-inflection) point at theta=0 (f'(0)=1-cos(0)=0). For the
Fibonacci rational approximants p/q = F(n-1)/F(n) to the golden mean, bisect on Omega so
that the critical point's q-th iterate closes up: f^q(0) = p (a periodic-orbit / mode-
locking condition on the critical orbit). Omega_n converges (super-exponentially, by
universality) to the golden-mean critical parameter Omega*.
"""
import mpmath as mp

mp.mp.dps = 40


def f(theta, Omega):
    return theta + Omega - mp.sin(2 * mp.pi * theta) / (2 * mp.pi)


def iterate_critical(Omega, q):
    x = mp.mpf(0)
    for _ in range(q):
        x = f(x, Omega)
    return x


def solve_Omega(p, q, lo, hi, tol=mp.mpf('1e-35')):
    flo = iterate_critical(lo, q) - p
    fhi = iterate_critical(hi, q) - p
    assert flo * fhi < 0, f"bracket fails for p/q={p}/{q}: f(lo)={flo}, f(hi)={fhi}"
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = iterate_critical(mid, q) - p
        if fm == 0 or (hi - lo) < tol:
            return mid
        if (flo < 0) == (fm < 0):
            lo, flo = mid, fm
        else:
            hi, fhi = mid, fm
    return (lo + hi) / 2


# Fibonacci numbers
F = {0: 1, 1: 1}
for k in range(2, 25):
    F[k] = F[k - 1] + F[k - 2]

print("Fibonacci rational approximants p/q -> Omega_n (bisection on the critical orbit):")
omegas = {}
for n in range(3, 18):
    p, q = F[n - 1], F[n]
    lo, hi = mp.mpf(0), mp.mpf(1)   # f^q(0)-p: negative at Omega=0, positive at Omega=1 (robust bracket)
    Om = solve_Omega(p, q, lo, hi)
    omegas[n] = Om
    print(f"  n={n:2d}  p/q={p}/{q:<4d}  Omega_n = {Om}")

Omega_star = omegas[17]
phi = (1 + mp.sqrt(5)) / 2
print()
print(f"Omega* (converged, n=17)        = {Omega_star}")
print(f"target (FINDINGS)                = 0.6066553...")
print(f"convergence: Omega_16 - Omega_17 = {omegas[16] - omegas[17]}")

# Now measure the actual rotation number at Omega* via long iteration (independent check)
x = mp.mpf(1e-10)  # perturb off the critical point for a generic-orbit rotation number
N_iter = 20000
x0 = x
for _ in range(N_iter):
    x = f(x, Omega_star)
rotation_number = (x - x0) / N_iter
print()
print(f"empirical rotation number after {N_iter} iterations at Omega* = {rotation_number}")
print(f"1/phi                                                          = {1/phi}")
print(f"match to 9 digits? {abs(rotation_number - 1/phi) < mp.mpf('1e-9')}")

# also report via continued fraction convergents directly (exact winding = 1/phi by construction
# of the Fibonacci bisection sequence itself, as an independent cross-check)
print(f"\np/q convergents -> 1/phi: F(14)/F(15) = {F[14]}/{F[15]} = {mp.mpf(F[14])/F[15]}")
