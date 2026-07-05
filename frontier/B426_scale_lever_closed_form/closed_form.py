"""B426 -- the scale-lever closed form (Chat-2 G1, VERIFIED) + the Galois-orbit contraction
theorem (the exact strengthening of the B408 correction).

Chat-2's claim (handoff 2026-07-05): B408's max-embedding seam ratio env45/env15 has the exact
closed form (3a^2+4a-1)/10, a = 2cos(2pi/9), minpoly 1000x^3-1500x^2+360x-19, in Q(zeta9)+,
sqrt5-free. VERIFIED here from the banked B372 sweep45.json exact coefficients:
  - cell (4,8) sqrt-15 sector = (1/96, -1/160, 1/480) on (1, c1, c2)   [exact JSON]
  - global max over 144 cells x 3 embeddings at (4,8), embedding 2      [exhaustive scan]
  - env45 = 1/96 - g/160 + a/480 = (3a^2+4a-1)/480                      [symbolic, mod a^3-3a+1]
  - ratio 48*env45 = (3a^2+4a-1)/10, minpoly 1000x^3-1500x^2+360x-19    [sympy]

THE GALOIS-ORBIT CONTRACTION THEOREM (new, this bud): the three "embeddings" of B408's envelope
are the three Galois conjugates of ONE cubic number (roots 1.2170, 0.2079, 0.0751). Exact
symmetric functionals of the orbit: mean = 1/2, RMS = sqrt(51)/10 ~ 0.714, geometric mean =
(19/1000)^(1/3) ~ 0.267 -- EVERY Galois-invariant functional < 1 (contraction). "Growth" (1.217)
exists ONLY under max, which is not Galois-invariant. This turns the B408 correction
(embedding-max artifact -> RMS 0.7649 contraction) into a theorem: a Galois orbit has no
canonical member; the object supplies no invariant functional under which the seam grows.

G2 structural (Chat-2, inputs verified): by CRT locality (P63) + seam factorization C3*C5 (P66)
+ locality of brightness (P67), the 5-local factor is level-inert 15->45, so the ratio is a pure
3-local quantity in Q(zeta9)+ -- the sqrt5-freeness is FORCED, not accidental. (The quantitative
C9/C3 forward derivation = the open level-9 build; not claimed here.)

Firewall: an envelope ratio of a theta model -- mathematics; "scale lever" is a historical label,
and this bud DEEPENS the negative: no invariant growth. Nothing here licenses a physics claim.
"""
import json, os
from fractions import Fraction as F
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
SWEEP = os.path.join(HERE, "..", "B372_level45_sweeper", "sweep45.json")

A = sp.symbols('A')          # A = alpha = 2cos(2pi/9);  minimal polynomial A^3 - 3A + 1
MINPOLY_A = A**3 - 3*A + 1
BETA  = A**2 - 2             # 2cos(4pi/9) (double angle)
GAMMA = -A - BETA            # 2cos(8pi/9) (trace zero)

def sector_48():
    """the sqrt-15 sector (1,c1,c2)-coefficients of cell (4,8) from the banked exact JSON."""
    d = json.load(open(SWEEP))["pair"]
    cf = [F(x) for x in d["4,8"]]
    return (cf[3], cf[7], cf[11])          # basis index 4*j+k, k=3 = sqrt-15 slot

def exhaustive_max():
    """(value, cell, embedding) of max |sqrt-15 sector| over 144 cells x 3 real embeddings."""
    import mpmath as mp
    mp.mp.dps = 40
    a = 2*mp.cos(2*mp.pi/9); b = 2*mp.cos(4*mp.pi/9); g = 2*mp.cos(8*mp.pi/9)
    embs = [(a, b), (b, g), (g, a)]
    d = json.load(open(SWEEP))["pair"]
    best = None
    for key, coefs in d.items():
        cf = [F(x) for x in coefs]
        s = (cf[3], cf[7], cf[11])
        for ei, (C1, C2) in enumerate(embs):
            v = float(s[0]) + float(s[1])*float(C1) + float(s[2])*float(C2)
            if best is None or abs(v) > abs(best[0]):
                best = (v, key, ei)
    return best

def env45_symbolic():
    """env45 at (4,8)/embedding-2 (c1,c2)=(gamma,alpha), reduced mod the minimal polynomial."""
    s0, s1, s2 = sector_48()
    e = sp.Rational(s0) + sp.Rational(s1)*GAMMA + sp.Rational(s2)*A
    return sp.rem(sp.expand(e*480), MINPOLY_A, A)/480

def ratio_closed_form():
    """48*env45 == (3A^2+4A-1)/10 (env15 = 1/48 banked), and its minimal polynomial."""
    r = sp.expand(48*env45_symbolic())
    target = (3*A**2 + 4*A - 1)/10
    resid = sp.rem(sp.expand((r - target)*10), MINPOLY_A, A)
    x = sp.Symbol('x')
    mp_r = sp.minimal_polynomial(r.subs(A, 2*sp.cos(2*sp.pi/9)), x)
    return r, resid, sp.expand(mp_r)

def galois_orbit_invariants():
    """exact symmetric functionals of the ratio's Galois orbit (from the minpoly)."""
    e1, e2, e3 = sp.Rational(3,2), sp.Rational(9,25), sp.Rational(19,1000)
    mean = e1/3
    rms = sp.sqrt((e1**2 - 2*e2)/3)
    geo = e3**sp.Rational(1,3)
    return dict(mean=mean, rms=sp.simplify(rms), geometric_mean=geo,
                all_below_one=bool(mean < 1 and rms < 1 and geo < 1))

if __name__ == "__main__":
    s = sector_48()
    print("cell (4,8) sqrt-15 sector:", s, " [claim (1/96,-1/160,1/480)]")
    v, cell, emb = exhaustive_max()
    print(f"exhaustive max: |env45|={abs(v):.16f} at cell ({cell}) embedding {emb}")
    r, resid, mp_r = ratio_closed_form()
    print("ratio =", r, "  residual vs (3A^2+4A-1)/10:", resid)
    print("minpoly:", mp_r)
    inv = galois_orbit_invariants()
    print("Galois-orbit invariants:", {k: str(vv) for k, vv in inv.items()})
    json.dump(dict(sector_48=[str(x) for x in s], max_cell=cell, max_embedding=emb,
                   ratio="(3a^2+4a-1)/10", minpoly=str(mp_r),
                   invariants={k: str(vv) for k, vv in inv.items()}),
              open(os.path.join(HERE, "closed_form.json"), "w"), indent=1)
    print("[written] closed_form.json")
