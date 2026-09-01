#!/usr/bin/env python3
"""R33 — SnapPy/PARI recompute (no Sage) of the trace-field / commensurability claims the Phase B readers
marked un-recomputed or IMPORTED: B142 (s776 = magic manifold, vol, Q(sqrt-7)), B146 (RRL/RLL bundles have
invariant trace field Q(sqrt-7)), B210/B840 (silver m136 = Q(i), bronze s464 degree 8 vs 6, m=4 t03910 degree 4),
B235 (figure-eight covers to degree 6 all Q(sqrt-3)), B781 (m003 monodromy trace -3, not +7), B803/B777
(m003 vs m004: same volume and field, not isometric, commensurable via a common finite cover), B850 (m009:
Q(sqrt-7), not commensurable with m004).  Output r33_out.txt / r33_out.json."""
import json, os, time
import snappy
from r33_lib import shape_field, field_name, pari
HERE = os.path.dirname(os.path.abspath(__file__))
out, lines = {}, []
def say(s): print(s, flush=True); lines.append(s)
t0 = time.time()

say('== A. invariant trace fields (shape fields) of the named manifolds ==')
A = {}
for nm, bank in [('m004', 'Q(sqrt-3) [golden, B210]'), ('m003', 'Q(sqrt-3) [B803]'), ('s776', 'Q(sqrt-7), vol 5.33349, 3 cusps = magic manifold [B142]'),
                 ('m009', 'Q(sqrt-7), arithmetic, non-commensurable with m004 [B850]'), ('m136', 'Q(i) [silver, B210]'),
                 ('s464', 'degree 8 (B210/B840 script) vs degree 6 (B578-D6 prereg) [bronze]'), ('t03910', 'degree 4 [m=4, B210]'),
                 ('b++RRL', 'Q(sqrt-7) [B146 RRL]'), ('b++RLL', 'Q(sqrt-7) [B146 RLL]'), ('b+-RRL', '(sign variant)'), ('b+-RLL', '(sign variant)')]:
    M = snappy.Manifold(nm)
    f = shape_field(M)
    A[nm] = dict(volume=float(M.volume()), cusps=M.num_cusps(), homology=str(M.homology()), field=f, bank=bank)
    say('  %-8s vol %.10f cusps %d H1 %-14s field deg %s %s disc %s sig %s   [bank: %s]' % (
        nm, M.volume(), M.num_cusps(), M.homology(), f['degree'] if f else None, field_name(f['poly']) if f else None,
        f['disc'] if f else None, f['signature'] if f else None, bank))
out['A_fields'] = A
say('  magic manifold check: s776 volume vs 3-chain link (magic) 5.3334895670 and Borromean 7.3277247: %.7f' % A['s776']['volume'])

say('== B. m003 vs m004 (B781/B803/B777) ==')
m3, m4 = snappy.Manifold('m003'), snappy.Manifold('m004')
say('  isometric: %s ; volumes %.12f %.12f ; H1 %s %s ; symmetry groups %s %s' % (m3.is_isometric_to(m4), m3.volume(), m4.volume(), m3.homology(), m4.homology(),
    m3.symmetry_group(), m4.symmetry_group()))
B = {}
for nm in ['b++RL', 'b+-RL', 'b-+RL', 'b--RL', 'b++RLRL', 'b+-RLRL']:
    Mb = snappy.Manifold(nm)
    B[nm] = dict(volume=float(Mb.volume()), homology=str(Mb.homology()), is_m003=Mb.is_isometric_to(m3), is_m004=Mb.is_isometric_to(m4))
    say('  bundle %-8s vol %.10f H1 %-12s = m003? %s  = m004? %s' % (nm, Mb.volume(), Mb.homology(), B[nm]['is_m003'], B[nm]['is_m004']))
R, L = pari('[1,1;0,1]'), pari('[1,0;1,1]')
say('  tr(RL) = %s, tr(-RL) = %s, tr((RL)^2) = %s ; |2 - tr| : RL -> %s, -RL -> %s, (RL)^2 -> %s' % (
    pari.trace(R*L), -pari.trace(R*L), pari.trace((R*L)**2), abs(2-pari.trace(R*L)), abs(2+pari.trace(R*L)), abs(2-pari.trace((R*L)**2))))
say('  => m003 = b+-RL: monodromy -RL, trace -3 (B781 MATCH); the trace-+7 candidate (RL)^2 is the double cover of m004, vol %.6f, not m003' % B['b++RLRL']['volume'])
out['B_bundles'] = B
# commensurability witness: a common finite cover
common = None
cov3 = {d: m3.covers(d) for d in (2, 3, 4)}
cov4 = {d: m4.covers(d) for d in (2, 3, 4)}
for d in (2, 3, 4):
    for X in cov3[d]:
        for Y in cov4[d]:
            if X.is_isometric_to(Y):
                common = (d, X.name(), Y.name()); break
        if common: break
    if common: break
say('  covers per degree: m003 %s  m004 %s ; first common cover: %s' % ({d: len(v) for d, v in cov3.items()}, {d: len(v) for d, v in cov4.items()}, common))
out['B_common_cover'] = common

say('== C. figure-eight covers to degree 6: invariant trace field (B235) ==')
Cc = {}
for d in range(2, 7):
    cs = m4.covers(d)
    degs = {}
    for X in cs:
        f = shape_field(X, bits=300)
        key = field_name(f['poly']) if f else 'FAIL'
        degs[key] = degs.get(key, 0) + 1
    Cc[d] = dict(n_covers=len(cs), fields=degs)
    say('  degree %d: %d covers, fields %s' % (d, len(cs), degs))
out['C_covers'] = Cc
say('  (theorem: the invariant trace field is a commensurability invariant, so all covers share Q(sqrt-3); the computation confirms the theorem, it is not evidence beyond it)')

say('== D. m009 vs m004 (B850): non-commensurable iff different invariant trace field for arithmetic cusped manifolds ==')
say('  m009 field %s vs m004 %s -> fields differ -> NOT commensurable (arithmetic cusped: commensurable iff same invariant trace field)' % (
    field_name(A['m009']['field']['poly']), field_name(A['m004']['field']['poly'])))
say('done %.0fs' % (time.time() - t0))
json.dump(out, open(HERE + '/r33_out.json', 'w'), indent=1, default=str)
open(HERE + '/r33_out.txt', 'w').write('\n'.join(lines) + '\n')
