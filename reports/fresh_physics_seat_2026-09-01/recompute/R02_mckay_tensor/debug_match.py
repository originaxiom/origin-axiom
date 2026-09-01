#!/usr/bin/env python3
"""Debug the 63/63 match failure with float traces (still blind: no repo scripts read)."""
import itertools, cmath, numpy as np
src = open(__file__.replace('debug_match.py','blind_instrument.py')).read()
src = src.split("results = {}")[0].replace("HERE = __file__.rsplit('/',1)[0]", "HERE='.'")
exec(src)

p = 331
r = run_prime(p, TEXP)
print('order', r['order'], 'classes', r['n_classes'])

# float instrument
z = cmath.exp(2j*cmath.pi/15)
Sf = np.array([[sum(v[k]*z**k for k in range(15)) for v in row] for row in SIGMA])
Tf = np.diag([z**e for e in TEXP])
Rf = Tf
Lf = np.linalg.inv(Sf) @ np.linalg.inv(Tf) @ Sf
Cf = Sf @ Sf / 75.0
print('C =\n', np.round(Cf.real,3))

def evalword(w):
    M = np.eye(6, dtype=complex)
    for ch in w:
        M = M @ (Rf if ch=='R' else Lf)
    return M

gvals = []
for (size, to_p, te_p), w in zip(r['gclass'], r['class_words']):
    ww = '' if w=='(identity)' else w
    M = evalword(ww)
    t = np.trace(M); tc = np.trace(Cf@M)
    gvals.append((size, (t-tc)/2, (t+tc)/2))

# model floats
om = cmath.exp(2j*cmath.pi/3)
def trf(q): return 2*q.w.fl()
mvals = []
for CA in clsT:
    a = CA[0]; chiA = om**chi_exp(a); trA = trf(a)
    for CB in clsI:
        b = CB[0]
        mvals.append((len(CA)*len(CB), chiA*trf(b), trA*trf(b)))

def canon(vals):
    return sorted((s, round(x.real,6), round(x.imag if hasattr(x,'imag') else 0,6),
                   round(y.real if hasattr(y,'real') else y,6), round(y.imag if hasattr(y,'imag') else 0,6))
                  for s,x,y in vals)
cg, cm = canon(gvals), canon(mvals)
print('float multisets equal:', cg == cm)
gm = [x for x in cg if x not in cm]
mg = [x for x in cm if x not in cg]
print('in G not model (first 12):')
for x in gm[:12]: print('  ', x)
print('in model not G (first 12):')
for x in mg[:12]: print('  ', x)
# distribution of odd traces
print('G odd trace magnitudes:', sorted({round(abs(x),4) for _,x,_ in gvals}))
print('model odd trace magnitudes:', sorted({round(abs(x),4) for _,x,_ in mvals}))
print('G even traces:', sorted({round(complex(y).real,4) for _,_,y in gvals}), 'imag max', max(abs(complex(y).imag) for _,_,y in gvals))
print('model even traces:', sorted({round(y,4) for _,_,y in mvals}))
print('G odd args (deg):', sorted({round(cmath.phase(x)*180/cmath.pi,1) for _,x,_ in gvals if abs(x)>1e-8}))
print('model odd args:', sorted({round(cmath.phase(x)*180/cmath.pi,1) for _,x,_ in mvals if abs(x)>1e-8}))
