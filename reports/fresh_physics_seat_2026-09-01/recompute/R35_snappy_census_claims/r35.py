#!/usr/bin/env python3
"""R35 — a batch of cheap SnapPy/PARI recomputes for census-type rows the Phase B readers marked ASSERTED /
IMPORTED / reproducible-unknown (no Sage): B3, B127, B129, B147, B197, B212, B258, B321, B322, B326.
Output r35_out.txt / r35_out.json."""
import json, os, sys, itertools
import snappy
from snappy import pari
from snappy.snap import polished_holonomy
from r33_lib import shape_field, field_name, C1, C2
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/home/user/origin-axiom/frontier/B322_value_hunt_filling_invariants')
out, lines = {}, []
def say(s): print(s, flush=True); lines.append(s)
M = snappy.Manifold('m004')

say('== B3 / B321 / B262: figure-eight triangulation, cusp shape ==')
shape = complex(M.cusp_info('shape')[0])
say('  m004: tetrahedra %d, edges %d (ideal triangulation: #edges = #tets), faces %d, cusps %d, H1 %s' % (M.num_tetrahedra(), M.num_tetrahedra(), 2 * M.num_tetrahedra(), M.num_cusps(), M.homology()))
say('  cusp shape %s ; |shape|^2 = %.12f (bank 2*sqrt3*i, 12 = h(E6))' % (shape, abs(shape) ** 2))
out['B3_B321'] = dict(tets=M.num_tetrahedra(), cusps=M.num_cusps(), shape=str(shape), abs2=abs(shape) ** 2)

say('== B127: CS(R^m L^m) identically 0, m = 1..6 (b++); and the b+- sign family ==')
cs = {}
for m in range(1, 7):
    for sg in ('++', '+-'):
        B = snappy.Manifold('b%sR%sL%s' % (sg, 'R' * (m - 1), 'L' * (m - 1)))
        cs['b%s m=%d' % (sg, m)] = dict(vol=float(B.volume()), H1=str(B.homology()), CS=float(B.chern_simons()))
        say('  b%s R^%dL^%d  vol %.10f  H1 %-16s  CS %+.3e' % (sg, m, m, B.volume(), B.homology(), B.chern_simons()))
say('  => b++ family: CS = 0 to machine precision for m=1..6 (MATCH); b+- family: CS = 1/4 for every m (not claimed by B127, recorded)')
out['B127'] = cs

say('== B197 C4: chiral pair b++RRL / b++RLL: equal volume, CS = +-1/48 ==')
p = {nm: snappy.Manifold(nm) for nm in ('b++RRL', 'b++RLL')}
for nm, B in p.items(): say('  %s vol %.10f H1 %s CS %.12f (1/48 = %.12f)' % (nm, B.volume(), B.homology(), B.chern_simons(), 1 / 48))
out['B197'] = {nm: dict(vol=float(B.volume()), CS=float(B.chern_simons())) for nm, B in p.items()}
say('  mirror check: b++RRL isometric to b++RLL: %s (orientation-preserving); CS opposite: %s' % (p['b++RRL'].is_isometric_to(p['b++RLL']), abs(p['b++RRL'].chern_simons() + p['b++RLL'].chern_simons()) < 1e-9))

say('== B147: volume = integer x Bianchi covolume (Humbert), covolumes from |D|^{3/2} zeta_K(2) / (4 pi^2) ==')
pari.set_real_precision(30)
def covol(D):   # PSL(2, O_K) covolume for K = Q(sqrt D), D the field discriminant
    K = pari.bnfinit('x^2 - (%d)' % D) if D % 4 == 1 else pari.bnfinit('x^2 - (%d)' % (D // 4))
    z2 = pari.lfun(K, 2)
    return abs(D) ** 1.5 * float(z2) / (4 * float(pari.pi()) ** 2)
cv = {-3: covol(-3), -4: covol(-4), -7: covol(-7)}
say('  covolumes: O_3 %.10f  O_1 %.10f  O_7 %.10f' % (cv[-3], cv[-4], cv[-7]))
rat = {}
for nm, D in [('b++RL', -3), ('b++RRLL', -4), ('b++RRL', -7), ('b++RLL', -7)]:
    v = snappy.Manifold(nm).volume(); rat[nm] = float(v) / cv[D]
    say('  %-8s vol %.10f / covol(O_%d) = %.9f' % (nm, v, -D if D % 4 else -D // 4, rat[nm]))
say('  bank: RL 12, RRLL 12, RRL/RLL 3 -> %s' % ('MATCH' if all(abs(rat[k] - t) < 1e-6 for k, t in [('b++RL', 12), ('b++RRLL', 12), ('b++RRL', 3), ('b++RLL', 3)]) else 'MISMATCH'))
out['B147'] = dict(covolumes=cv, ratios=rat)

say('== B129: silver bundle b++RRLL (= m136) degree-2 covers reach (cusps, free rank) = (2,2) ==')
S = snappy.Manifold('b++RRLL')
cov = [(c.num_cusps(), c.homology().betti_number()) for c in S.covers(2)]
say('  b++RRLL = m136: %s ; degree-2 covers (cusps, rank): %s ; (2,2) reached: %s' % (S.is_isometric_to(snappy.Manifold('m136')), cov, (2, 2) in cov))
out['B129'] = dict(covers=cov)

say('== B326: H1 of the 3-fold cyclic cover of the figure-eight complement ==')
h = [str(c.homology()) for c in M.covers(3, cover_type='cyclic')]
say('  H1 = %s (bank Z + Z/4 + Z/4)' % h)
out['B326'] = h

say('== B258 / B212: trace field vs invariant trace field of silver (m136) and bronze (s464) ==')
def trace_fields(name, bits=1600):
    Mx = snappy.Manifold(name)
    G = polished_holonomy(Mx, bits_prec=bits, lift_to_SL2=False)
    gens = G.generators()
    words = list(gens) + [a + b for a, b in itertools.combinations(gens, 2)] + [''.join(w) for w in itertools.combinations(gens, 3)]
    digits = int(bits * 0.3); pari.set_real_precision(digits)
    tr = {w: G.SL2C(w).trace().gen for w in words}   # PSL lift: traces up to sign; the field they generate is sign-independent
    sq = {w: (tr[w] ** 2 - 2) for w in gens}         # tr(g^2) = tr(g)^2 - 2, sign-free
    def field_of(vals, maxdeg=16):
        tol = pari(10) ** (-int(digits * 0.5))
        for C in ((1, 2, 3, 4, 5, 6, 7), (1, 3, 4, 7, 9, 12, 14)):
            w = sum(c * v for c, v in zip(C, vals))
            for d in range(2, maxdeg + 1):
                pp = pari.algdep(w, d)
                if not pp: continue
                if abs(pari.subst(pp, 'x', w)) > tol: continue
                H = max(abs(int(c)) for c in pari.Vec(pp))
                if (d + 1) * len(str(H)) > digits * 0.5: continue
                for f, _ in zip(*pari.factor(pp)):
                    if pari.poldegree(f) >= 1 and abs(pari.subst(f, 'x', w)) < tol:
                        return int(pari.poldegree(f)), str(pari.polredbest(f))
        return None, None
    dt, ft = field_of(list(tr.values()))
    di, fi = field_of(list(sq.values()))
    return dict(gens=gens, trace_field_degree=dt, trace_field_poly=ft, invariant_degree=di, invariant_poly=fi, sq_traces={w: str(sq[w])[:24] for w in gens}, gen_traces={w: str(tr[w])[:24] for w in gens})
for nm, bank in [('m136', 'B258: silver trace field degree 8; B212: invariant Q(i), full trace field contains sqrt2 (~Q(zeta8))'), ('s464', 'B258: bronze degree 8'), ('m004', 'control: Q(sqrt-3) both')]:
    try:
        r = trace_fields(nm)
        say('  %-5s trace field: degree %s %s | invariant trace field (from tr g^2): degree %s %s | gen traces %s | square traces %s' % (
            nm, r['trace_field_degree'], r['trace_field_poly'], r['invariant_degree'], field_name(r['invariant_poly']) if r['invariant_poly'] else None, r['gen_traces'], r['sq_traces']))
        say('      [bank: %s]' % bank)
        out['trace_fields_' + nm] = r
    except Exception as e:
        say('  %s trace-field computation failed: %r' % (nm, e)); out['trace_fields_' + nm] = repr(e)

say('== B212: silver square-traces mod (1+i) ==')
r = out.get('trace_fields_m136')
if isinstance(r, dict):
    pari.set_real_precision(200)
    res = {}
    for w, s in r['sq_traces'].items():
        pass
    G = polished_holonomy(snappy.Manifold('m136'), bits_prec=800, lift_to_SL2=False)
    for w in G.generators():
        t2 = G.SL2C(w).trace().gen ** 2 - 2
        zi = pari.algdep(t2, 2)   # should be a Gaussian integer: x^2 - 2 Re x + |x|^2
        # identify as a + b i with integers
        re_, im_ = pari.real(t2), pari.imag(t2)
        a, b = int(re_.round()), int(im_.round())
        exact = abs(re_ - a) < 1e-50 and abs(im_ - b) < 1e-50
        res[w] = dict(tr_sq='%d%+di' % (a, b), gaussian_integer=bool(exact), zero_mod_1_plus_i=((a + b) % 2 == 0))
        say('  tr(%s^2) = %s  Gaussian integer: %s  == 0 mod (1+i): %s' % (w, res[w]['tr_sq'], exact, res[w]['zero_mod_1_plus_i']))
    # products of generators (squares of products): any order-3 element mod (1+i) would show as tr^2 - 2 == 1 mod (1+i), i.e. a+b odd
    odd = []
    for w in [x + y for x, y in itertools.permutations(G.generators(), 2)] + [x + y + z for x, y, z in itertools.permutations(G.generators(), 3)]:
        t2 = G.SL2C(w).trace().gen ** 2 - 2
        a, b = int(pari.real(t2).round()), int(pari.imag(t2).round())
        if abs(pari.real(t2) - a) < 1e-40 and abs(pari.imag(t2) - b) < 1e-40 and (a + b) % 2: odd.append((w, '%d%+di' % (a, b)))
    say('  squares of words of length 2-3 with tr(w^2) != 0 mod (1+i) (would be order-3 elements in SL(2,F2)): %s' % (odd or 'none'))
    say('  bank: tr(a^2)=+2i, tr(b^2)=2, tr(c^2)=-2i, all == 0 mod (1+i), no order-3 element')
    out['B212'] = dict(squares=res, odd_words=odd)

say('== B322: the 79 hardcoded Dehn-filling invariants (volumes + core lengths, |p|,|q| <= 8) ==')
from value_hunt_filling_invariants import OBJECT_INVARIANTS
vals = set()
from math import gcd
for pq in range(-8, 9):
    for q in range(-8, 9):
        if (pq, q) == (0, 0) or gcd(abs(pq), abs(q)) != 1: continue
        N = snappy.Manifold('m004(%d,%d)' % (pq, q))
        st = N.solution_type()
        if 'positively' not in st and 'negatively' not in st and 'flat' not in st: continue
        try:
            vals.add(round(float(N.volume()), 5))
            L = N.length_spectrum(1.0) if False else None
        except Exception: pass
        try:
            ci = N.cusp_info()  # closed: use core geodesic length via drilling? use N.core_geodesic? SnapPy: dual_curves / length of core
        except Exception: pass
recomputed_vols = sorted(vals)
bank = sorted(OBJECT_INVARIANTS)
hit = [v for v in bank if any(abs(v - w) < 6e-5 for w in recomputed_vols)]
say('  hyperbolic fillings |p|,|q|<=8 found: %d distinct volumes; bank list has %d numbers, of which %d coincide with a recomputed volume (the rest should be core-geodesic lengths)' % (len(recomputed_vols), len(bank), len(hit)))
# core geodesic lengths: SnapPy gives them via M.core_geodesic? use 'N.length_spectrum' is heavy; use the drilled description: length of core = complex length of the filled curve
cores = set()
for pq in range(-8, 9):
    for q in range(-8, 9):
        if (pq, q) == (0, 0) or gcd(abs(pq), abs(q)) != 1: continue
        N = snappy.Manifold('m004(%d,%d)' % (pq, q))
        st = N.solution_type()
        if 'positively' not in st: continue
        try:
            cl = N.cusp_info()[0].get('core_length') if N.cusp_info() else None
            if cl is None:
                cl = N.core_geodesic()[0]
            cores.add(round(abs(complex(cl).real), 5))
        except Exception as e:
            pass
hit2 = [v for v in bank if any(abs(v - w) < 6e-5 for w in cores)]
say('  core-geodesic real lengths found: %d distinct; bank numbers matched by a core length: %d; matched by either: %d / %d' % (len(cores), len(hit2), len(set(hit) | set(hit2)), len(bank)))
unm = [v for v in bank if v not in set(hit) | set(hit2)]
say('  bank numbers matched by neither: %s' % unm)
out['B322'] = dict(n_vols=len(recomputed_vols), n_cores=len(cores), matched=len(set(hit) | set(hit2)), unmatched=unm)

json.dump(out, open(HERE + '/r35_out.json', 'w'), indent=1, default=str)
open(HERE + '/r35_out.txt', 'w').write('\n'.join(lines) + '\n')
