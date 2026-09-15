"""PREREGISTERED PRE-STEP (seal §4): are the added volume directions
LINEARLY DEPENDENT on B1137's existing basis at working precision?  If so
they add nothing and must be dropped, exactly as B1137's own
basis_hygiene_check dropped six redundant entries.  Gate 5: TARGET-FREE —
no SM value is loaded or touched anywhere in this file."""
from mpmath import mp, pslq, polylog, exp, pi, im, mpf
import basis as basismod

DPS = 220
H = 10**6
mp.dps = DPS

def Lam(th): return im(polylog(2, exp(2j*th)))/2

b, forms, R = basismod.build_pruned_basis(dps=DPS)
mp.dps = DPS
VOL = 6*Lam(pi/3)
NEW = {
    'vol':             VOL,
    'vol_pinorm':      VOL/pi,
    'vol_over_zetaK2': VOL/b['zetaK_2'],
}
keys = forms['FULL']
print(f"B1137 pruned basis size: {len(keys)}   working dps={DPS}  H={H}")
print(f"Vol(m004) = {mp.nstr(VOL, 32)}   (computed from Li_2, not quoted)\n")

kept, dropped = [], []
for name, val in NEW.items():
    vec = [val] + [b[k] for k in keys]
    rel = pslq(vec, maxcoeff=H, maxsteps=10**6, tol=mp.mpf(10)**(-(DPS-25)))
    if rel is None or rel[0] == 0:
        kept.append(name)
        print(f"  {name:18s} INDEPENDENT of the existing basis  -> KEEP")
    else:
        terms = [f"{rel[i+1]}*{k}" for i, k in enumerate(keys) if rel[i+1] != 0]
        dropped.append((name, rel[0], terms))
        print(f"  {name:18s} DEPENDENT: {rel[0]}*{name} = -({' + '.join(terms[:4])}...)  -> DROP")
print(f"\nKEPT {len(kept)}: {kept}")
print(f"DROPPED {len(dropped)}: {[d[0] for d in dropped]}")
print("\nGate 5: no SM target was loaded in this check.")
