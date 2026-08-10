"""B1021 R2a spot-check (scratchpad, pre-bank): reproduce the 0-hit null from the
PUBLISHED eigenvalues at the licensed heights. Not the full 28-box rerun -- the
reconstructible subset; the sqrt(-phi) box convention defers to the harvested artifact."""
import mpmath as mp

mp.mp.dps = 40
R2 = mp.mpf("4.9000853730625213014795758")            # lambda_2 (B922, 25 dp)
RP = mp.mpf("7.0720041858752050007371941867273")      # parent (cell 9, 31 figs)
targets = {"r2": R2, "lam2": 1 + R2**2, "rp": RP, "lamp": 1 + RP**2}

hits = []
def box_quadratic(name, d, H):
    s = mp.sqrt(d)
    for tn, t in targets.items():
        rel = mp.pslq([mp.mpf(1), s, t], maxcoeff=H, maxsteps=10**4)
        if rel: hits.append((name, tn, rel))

def box_minpoly(name, deg, H):
    for tn, t in targets.items():
        rel = mp.pslq([t**k for k in range(deg + 1)], maxcoeff=H, maxsteps=10**4)
        if rel: hits.append((name, tn, rel))

def box_cyclo_real(name, n, H):
    c = 2 * mp.cos(2 * mp.pi / n)
    deg = 4  # phi(15)/2 = phi(20)/2 = 4
    for tn, t in targets.items():
        rel = mp.pslq([c**k for k in range(deg)] + [t], maxcoeff=H, maxsteps=10**4)
        if rel: hits.append((name, tn, rel))

box_quadratic("Q(sqrt5)", 5, 10**4)
box_quadratic("Q(sqrt3)", 3, 10**4)
box_quadratic("Q(sqrt15)", 15, 10**4)
box_minpoly("MINPOLY d<=5", 5, 10**3)
box_cyclo_real("Q(zeta15+)", 15, 10**3)
box_cyclo_real("Q(zeta20+)", 20, 10**3)
print(f"boxes run: 6 fields x 4 targets = 24 powered combinations")
print(f"gated hits: {len(hits)}")
for h in hits: print("  HIT:", h)
# positive control: the instrument must FIND a planted relation
ctrl = mp.pslq([mp.mpf(1), mp.sqrt(5), 3 - 2 * mp.sqrt(5)], maxcoeff=10**4)
print("positive control (planted 3-2sqrt5):", "FOUND" if ctrl else "MISSED", ctrl)
