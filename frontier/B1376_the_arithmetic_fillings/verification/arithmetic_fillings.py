#!/usr/bin/env python3
"""B1376 -- THE ARITHMETIC FILLINGS OF m004, decided on this bench with own code and without Sage, by the cocompact criterion
(Maclachlan-Reid, Theorem 8.3.2): a closed hyperbolic 3-manifold's group Gamma is arithmetic iff (1) its invariant trace field
k = Q(tr gamma^2 : gamma in Gamma) has exactly one complex place, (2) every trace is an algebraic integer, and (3) the invariant
quaternion algebra is ramified at every real place of k.  For a two-generator group k = Q(tr^2 a, tr^2 b, tr a tr b tr ab); the
invariant quaternion algebra is the Hilbert symbol (tr^2 g - 4, tr[g,h] - 2 / k) for g, h in Gamma^(2) generating an irreducible
subgroup with g non-parabolic (here g = a^2, h = b^2), ramified at a real place v iff both entries are negative under v.
Numerics: SnapPy's polished holonomy at 2 000 bits (4 000 on escalation); the minimal polynomial of a primitive element by PARI's
algdep (LLL) followed by factorisation and the choice of the irreducible factor that vanishes (algdep may return a multiple);
membership of the generators and of the Hilbert entries in Q(theta) by PARI's lindep, each relation verified to the working
precision; the signature from the real roots.  An unrecognised field is reported UNRESOLVED, never as a negative.
Usage: python3 arithmetic_fillings.py [controls | grid | p,q ...]"""
import sys, math, time
import snappy
from snappy import snap
from snappy.pari import pari
from fractions import Fraction
pari.allocatemem(2 ** 30, silent=True) if 'silent' in pari.allocatemem.__doc__ else pari.allocatemem(2 ** 30)   # the default 8 MB PARI stack overflows on degree-20 fields

def holonomy(name, bits):
    M = snappy.Manifold(name); G = snap.polished_holonomy(M, bits_prec=bits); return M, G
def tr(X): return X[0, 0] + X[1, 1]
def tiny(x, bits): return abs(x) < pari(2) ** (-(bits // 3))
def minimal_polynomial(z, bits, maxdeg=64):
    """the irreducible integer polynomial vanishing at z (coefficients low -> high, positive leading coefficient), or None"""
    P = z.algdep(maxdeg)
    if P == 0: return None
    for i in range(1, int(P.factor().matsize()[0]) + 1):
        f = P.factor()[i - 1, 0]
        if tiny(f.subst('x', z), bits):
            co = [int(c) for c in f.Vec()][::-1]          # Vec is high -> low
            if co[-1] < 0: co = [-c for c in co]
            return co
    return None
def in_field(y, z, d, bits):
    """y as a rational polynomial in z of degree < d (Fractions, low -> high), or None"""
    rel = pari([y] + [z ** k for k in range(d)]).lindep()
    if int(rel[0]) == 0: return None
    c0 = int(rel[0]); coeffs = [Fraction(-int(rel[k + 1]), c0) for k in range(d)]
    val = y - sum(pari(c.numerator) / pari(c.denominator) * z ** k for k, c in enumerate(coeffs))
    return coeffs if tiny(val, bits) else None
def real_roots(co):
    f = pari('Pol(%s)' % [c for c in co[::-1]]); return [r for r in f.polrootsreal()], int(f.polsturm())
def evaluate(coeffs, t): return sum(pari(c.numerator) / pari(c.denominator) * t ** k for k, c in enumerate(coeffs))

def decide(name, bits=2000):
    M0 = snappy.Manifold(name)
    if M0.solution_type() != 'all tetrahedra positively oriented': return dict(name=name, verdict='NOT HYPERBOLIC (solution type: %s)' % M0.solution_type())
    try: M, G = holonomy(name, bits)
    except Exception as e: return dict(name=name, verdict='UNRESOLVED (holonomy failed: %s)' % str(e)[:50])
    gens = G.generators(); assert len(gens) == 2, gens
    A, B = G.SL2C(gens[0]), G.SL2C(gens[1]); AB = A * B
    ta, tb, tab = tr(A).gen, tr(B).gen, tr(AB).gen
    u = [ta * ta, tb * tb, ta * tb * tab]
    g, h = A * A, B * B; tg, th = tr(g).gen, tr(h).gen; tgh = tr(g * h).gen
    ginv = snap.utilities.Matrix2x2(g[1, 1], -g[0, 1], -g[1, 0], g[0, 0]); hinv = snap.utilities.Matrix2x2(h[1, 1], -h[0, 1], -h[1, 0], h[0, 0])
    tc = tr(g * h * ginv * hinv).gen
    aH, bH = tg * tg - 4, tc - 2
    best = None
    for combo in ((1, 3, 7), (2, -5, 11), (1, 1, 1), (3, 1, -2)):
        z = combo[0] * u[0] + combo[1] * u[1] + combo[2] * u[2]
        co = minimal_polynomial(z, bits)
        if co is None: continue
        d = len(co) - 1
        if all(in_field(x, z, d, bits) is not None for x in u):
            if best is None or d > best[2]: best = (z, co, d, combo)
    if best is None: return dict(name=name, verdict='UNRESOLVED (no primitive element recognised at %d bits)' % bits)
    z, co, d, combo = best
    rr, r1 = real_roots(co); r2 = (d - r1) // 2
    integral = True
    for t in (tg, th, tgh, tc):
        pt = minimal_polynomial(t, bits)
        if pt is None: integral = None; break
        if abs(pt[-1]) != 1: integral = False
    ca, cb = in_field(aH, z, d, bits), in_field(bH, z, d, bits)
    if ca is None or cb is None: return dict(name=name, verdict='UNRESOLVED (Hilbert entries not recognised in the field)', deg=d, r1=r1, r2=r2, minpoly=co)
    ram = []
    for t in rr:
        va, vb = evaluate(ca, t), evaluate(cb, t); ram.append(bool(va < 0 and vb < 0))
    arithmetic = (r2 == 1) and (integral is True) and all(ram)
    why = []
    if r2 != 1: why.append(f"{r2} complex places")
    if integral is False: why.append("a non-integral trace")
    if r2 == 1 and integral is True and not all(ram): why.append("the quaternion algebra splits at a real place")
    f = pari('Pol(%s)' % [c for c in co[::-1]]); D = f.poldisc(); core = int(D.core())      # the squarefree part of the polynomial discriminant
    return dict(name=name, verdict='ARITHMETIC' if arithmetic else 'NON-ARITHMETIC (' + '; '.join(why) + ')', deg=d, r1=r1, r2=r2, minpoly=co, disc_core=core,
                integral=integral, ramified_at_real_places=ram, volume=float(M.volume()), H1=str(M.homology()), combo=combo)

def show(r):
    s = f"  {r['name']:14s} {r['verdict']:60s}"
    if 'deg' in r: s += f" k: degree {r['deg']}, signature ({r['r1']},{r['r2']}), squarefree part of the discriminant {r.get('disc_core')}, minpoly {r.get('minpoly')}, integral traces {r.get('integral')}, ramified at the real places {r.get('ramified_at_real_places')}, vol {r.get('volume', 0):.5f}, H1 {r.get('H1')}"
    print(s, flush=True)

if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'controls'; t0 = time.time()
    if what == 'controls':
        print("=== controls: the Weeks manifold m003(-3,1) (arithmetic, Chinburg-Friedman-Jones-Reid), the Meyerhoff manifold m004(5,1) (arithmetic, Chinburg 1987), m004(6,1), m004(8,1) (B718), and three non-arithmetic fillings ===")
        for name in ('m003(-3,1)', 'm004(5,1)', 'm004(6,1)', 'm004(8,1)', 'm004(7,1)', 'm004(4,3)', 'm004(1,2)'): show(decide(name))
    elif what == 'grid':
        print("=== the grid |p| <= 8, 1 <= q <= 8, gcd = 1: the 78 closed hyperbolic fillings of m004 ===")
        counts = {}
        for q in range(1, 9):
            for p in range(-8, 9):
                if math.gcd(abs(p), q) != 1: continue
                name = f"m004({p},{q})"
                if snappy.Manifold(name).solution_type() != 'all tetrahedra positively oriented':
                    counts['not hyperbolic'] = counts.get('not hyperbolic', 0) + 1; print(f"  {name:14s} not hyperbolic ({snappy.Manifold(name).solution_type()})", flush=True); continue
                try: r = decide(name, bits=2000)
                except Exception as e: r = dict(name=name, verdict='UNRESOLVED (error: %s)' % str(e)[:40])
                if r['verdict'].startswith('UNRESOLVED'):
                    try: r = decide(name, bits=4000)
                    except Exception as e: r = dict(name=name, verdict='UNRESOLVED (error at 4000 bits: %s)' % str(e)[:40])
                show(r); k = r['verdict'].split(' (')[0]; counts[k] = counts.get(k, 0) + 1
        print("  SUMMARY:", counts, f"({time.time() - t0:.0f} s)")
    else:
        for spec in sys.argv[1:]:
            p, q = spec.split(','); show(decide(f"m004({p},{q})"))
    print("DONE")
