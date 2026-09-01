#!/usr/bin/env python3
"""R37 — B790 (m004/m003 length spectra to Re l <= 5: 134/150 geodesics, traces in Z[omega], not isospectral),
B777 (V4-genericity table: symmetry groups + amphicheirality of m004, m003, m025, m009, m010), B850 (length-spectrum
multiplicities: SnapPy complex-length classes vs the bank's word-count 'multiplicity'), B894 (K = Q[x]/(x^3-12x-5):
disc 6237 = 3^4 7 11, monogenic, 5 unramified).  Output r37_out.txt / r37_out.json.  SnapPy + PARI, no Sage."""
import snappy, cmath, math, collections, json, os
from snappy import pari
HERE = os.path.dirname(os.path.abspath(__file__)); out, lines = {}, []
def say(s): print(s, flush=True); lines.append(s)
say('== B790 L1/L2: length spectra to Re(l) <= 5, traces 2cosh(l/2) in Z[omega]? ==')
w = complex(-0.5, math.sqrt(3) / 2); spec = {}
for nm in ['m004', 'm003']:
    M = snappy.Manifold(nm); ls = M.length_spectrum(5.0); worst = 0; norms = []
    for g in ls:
        l = complex(g.length); tr = 2 * cmath.cosh(l / 2)
        b = tr.imag / w.imag; a = tr.real - b * w.real
        worst = max(worst, max(abs(a - round(a)), abs(b - round(b)))); norms.append(round(a) ** 2 - round(a) * round(b) + round(b) ** 2)
    spec[nm] = (len(ls), sorted(set(round(complex(g.length).real, 9) for g in ls)), collections.Counter(norms), max(g.multiplicity for g in ls))
    say('  %s: %d geodesics (bank %d), worst deviation of 2cosh(l/2) from Z[omega] %.2e (double-precision lengths; bank 2.6e-15 at 40 dps), %d distinct real lengths, max SnapPy multiplicity %d' % (
        nm, len(ls), {'m004': 134, 'm003': 150}[nm], worst, len(spec[nm][1]), spec[nm][3]))
say('  real-length sets: m004 %d, m003 %d, shared %d -> isospectral: %s; trace-norm multisets equal: %s' % (
    len(spec['m004'][1]), len(spec['m003'][1]), len(set(spec['m004'][1]) & set(spec['m003'][1])), spec['m004'][1] == spec['m003'][1], spec['m004'][2] == spec['m003'][2]))
out['B790'] = {nm: dict(n=v[0], n_real_lengths=len(v[1]), max_mult=v[3]) for nm, v in spec.items()}
say('== B777 V4 genericity (cc verification table): symmetry groups and amphicheirality ==')
bank = {'m004': ('D4', True), 'm003': ('Z/2 + Z/4', True), 'm025': ('Z/6', True), 'm009': ('Z/2 + Z/2', False), 'm010': ('Z/2 + Z/2', False)}
rows = {}
for nm in ['m004', 'm003', 'm025', 'm009', 'm010', 'b++RRLL', 'm015', 'm016']:
    M = snappy.Manifold(nm); S = M.symmetry_group()
    rows[nm] = dict(vol=float(M.volume()), sym=str(S), order=int(S.order()), amphicheiral=bool(S.is_amphicheiral()))
    ok = (str(S) == bank[nm][0] and bool(S.is_amphicheiral()) == bank[nm][1]) if nm in bank else None
    say('  %-8s vol %.10f sym %-12s order %d amphicheiral %-5s  bank %s -> %s' % (nm, M.volume(), S, S.order(), S.is_amphicheiral(), bank.get(nm, '(not in table)'), 'MATCH' if ok else ('' if ok is None else 'MISMATCH')))
out['B777'] = rows
say('== B850: geodesic multiplicities. SnapPy complex-length classes to Re(l) <= 4 (the bank counted holonomy words at 40 dps, max 4/3/4/8/2) ==')
mult = {}
for nm in ['m004', 'm003', 'm136', 'm009', 'm015']:
    M = snappy.Manifold(nm); ls = M.length_spectrum(4.0)
    mult[nm] = dict(n=len(ls), max=max(g.multiplicity for g in ls), mean=sum(g.multiplicity for g in ls) / len(ls))
    say('  %-5s geodesic classes %3d  max multiplicity %2d  mean %.2f' % (nm, len(ls), mult[nm]['max'], mult[nm]['mean']))
out['B850'] = mult
say('== B894: K = Q[x]/(x^3-12x-5) ==')
f = pari('x^3 - 12*x - 5'); nf = pari.nfinit(f)
say('  poldisc %s, nfdisc %s = %s, index %s, Galois %s, signature %s, 5 unramified: %s' % (
    pari.poldisc(f), pari.nfdisc(f), pari.factor(pari.nfdisc(f)).mattranspose(), pari('sqrtint(%s/%s)' % (pari.poldisc(f), pari.nfdisc(f))), pari.polgalois(f)[3], nf[1], all(int(P[2]) == 1 for P in pari.idealprimedec(nf, 5))))
out['B894'] = dict(nfdisc=str(pari.nfdisc(f)), index=1)
json.dump(out, open(HERE + '/r37_out.json', 'w'), indent=1, default=str); open(HERE + '/r37_out.txt', 'w').write('\n'.join(lines) + '\n')
