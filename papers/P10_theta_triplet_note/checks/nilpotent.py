"""The nilpotent field (Proposition 1 of the note). With rho = (-theta_2^2, -theta_4^2, i theta_3^2) for the units
(i, j, k) placed at the half-periods (1/2, tau/2, (1+tau)/2) of Z + tau Z, Phi = sum_r rho_r f_r e_r dz has
Phi^2 = -[(rho.rho) wp(z) - sum_r rho_r^2 wp(z_r)] dz^2, so Phi is nilpotent iff rho.rho = 0 and sum_r rho_r^2 wp(z_r) = 0.
The check: both vanish at several tau; the other five assignments of units to half-periods do not."""
import itertools
import mpmath as mp
mp.mp.dps = 30
worst, others = 0, []
for tau in (mp.mpc(0.3, 1.2), mp.mpc(-0.17, 0.95), mp.mpc(0.45, 2.1), mp.mpc(0.0, 1.0)):
    q = mp.exp(1j * mp.pi * tau); t2, t3, t4 = (mp.jtheta(k, 0, q) for k in (2, 3, 4))
    k = mp.pi ** 2 / 3
    e = {"1/2": k * (t3**4 + t4**4), "(1+t)/2": k * (t2**4 - t4**4), "t/2": -k * (t2**4 + t3**4)}
    rho = {"i": -t2**2, "j": -t4**2, "k": 1j * t3**2}
    dot = sum(v ** 2 for v in rho.values())
    stated = rho["i"] ** 2 * e["1/2"] + rho["j"] ** 2 * e["t/2"] + rho["k"] ** 2 * e["(1+t)/2"]
    worst = max(worst, abs(dot), abs(stated))
    for perm in itertools.permutations(["1/2", "t/2", "(1+t)/2"]):
        if perm == ("1/2", "t/2", "(1+t)/2"): continue
        val = sum(rho[u] ** 2 * e[hp] for u, hp in zip("ijk", perm))
        others.append((mp.nstr(tau, 4), perm, abs(val)))
print(f"rho.rho and the stated sum: worst |value| = {mp.nstr(worst, 3)}")
generic = [o for o in others if o[0] != mp.nstr(mp.mpc(0, 1), 4)]
print(f"the other assignments at generic tau: smallest |value| = {mp.nstr(min(o[2] for o in generic), 4)}")
assert worst < 1e-25 and min(o[2] for o in generic) > 1e-3
print("all checks pass")
