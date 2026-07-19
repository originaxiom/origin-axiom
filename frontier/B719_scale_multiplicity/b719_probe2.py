#!/usr/bin/env python3
"""
B719 PROBE 2 -- is SCALE a distinguished multiplicity, or a FREE covering ladder?

Child m003(-2,3): closed Mostow-rigid hyperbolic 3-manifold, vol 0.98137, H1 = Z/5.
Mostow rigidity fixes the SHAPE but NOT the SIZE. Finite covers give sizes:
  vol(degree-d cover) = d * vol(base)  EXACTLY.

QUESTION: does the object single out a DISTINGUISHED scale (a unique smallest /
canonical / preferred multiplicity), or is every degree freely available (a FREE
ladder, no preferred size => 'how many units' = observer's scale choice)?

Two-outcome:
  A = a distinguished intrinsic scale (canonical/preferred multiplicity)
  B = a FREE covering ladder (no preferred size) => the dimensionful no-go extends
      to multiplicity.

METHOD: enumerate ALL finite covers of each degree d (complete low-index subgroup
enumeration via the SnapPea kernel, M.covers(d)). For each cover record volume
(= d*base, checked) and H1. Characterize the subgroup-growth sequence a(d).

Firewall: structural/arithmetic only. No cosmology, no SM value.
"""
import snappy, time, sys

def log(*a):
    print(*a); sys.stdout.flush()

M = snappy.Manifold('m003(-2,3)')
base = M.volume()
log('=== CHILD m003(-2,3) ===')
log('volume       ', base)
log('solution_type', M.solution_type())
log('H1(base)     ', M.homology())
log('is_closed    ', M.is_closed() if hasattr(M,'is_closed') else 'n/a')
log('')

# ---- 1. subgroup-growth sequence a(d) = number of degree-d connected covers ----
log('=== COVER TOWER: counts / volumes / homologies per degree ===')
MAX_DEG = 13          # push as far as tractable (deg 14+ blows up super-exp.)
PER_DEG_BUDGET = 90.0 # seconds; stop the tower if one degree blows past this
counts = {}
detail = {}
for d in range(2, MAX_DEG+1):
    t = time.time()
    covers = M.covers(d)
    dt = time.time() - t
    counts[d] = len(covers)
    # volume check + homology fingerprint for each cover of this degree
    rows = []
    for i, C in enumerate(covers):
        try:
            v = C.volume()
        except Exception:
            v = float('nan')
        try:
            h = C.homology()
        except Exception:
            h = '?'
        vc = 'ok' if abs(v - d*base) < 1e-6 else 'MISMATCH(%.6f)' % v
        rows.append((i, str(h), v, vc))
    detail[d] = rows
    log('deg %2d : count=%d   (%.2fs)' % (d, len(covers), dt))
    for (i, h, v, vc) in rows:
        log('          cover[%d]  vol=%.6f=%d*base[%s]  H1=%s' % (i, v, d, vc, h))
    if dt > PER_DEG_BUDGET:
        log('   (per-degree budget exceeded at d=%d; tower truncated here)' % d)
        break

log('')
log('=== SUBGROUP-GROWTH SEQUENCE a(d) ===')
seq = [counts.get(d, None) for d in range(2, max(counts)+1)]
log('d      :', list(range(2, max(counts)+1)))
log('a(d)   :', seq)
first_nontrivial = min((d for d in counts if counts[d] > 0), default=None)
log('first (minimal) nontrivial cover degree :', first_nontrivial)
log('degrees with NO cover (gaps)            :', [d for d in counts if counts[d]==0])
log('degrees WITH cover                      :', [d for d in counts if counts[d]>0])
log('is the minimal cover unique?            :',
    (counts.get(first_nontrivial)==1) if first_nontrivial else 'n/a')

# ---- 2. The minimal cover: identify it (should be the cyclic Z/5 homology cover) ----
log('')
log('=== MINIMAL COVER ANATOMY (degree %s) ===' % first_nontrivial)
if first_nontrivial:
    Cmin = M.covers(first_nontrivial)[0]
    log('vol   =', Cmin.volume(), '=', first_nontrivial, '* base  (check %.2e)'
        % abs(Cmin.volume()-first_nontrivial*base))
    log('H1    =', Cmin.homology())
    log('cover type (regular/cyclic?) : degree =', first_nontrivial,
        '= |H1(base)| =', 'Z/5 -> this is the abelian homology cover'
        if first_nontrivial==5 else '?')

log('')
log('=== VERDICT DATA ===')
log('shape fixed (Mostow), size = d*base for every available d.')
log('sizes actually realized (degrees with a cover):',
    [d for d in counts if counts[d]>0])
log('=> distinguished-scale test: is there a UNIQUE preferred size, or a ladder?')
