"""Referee check of the paper's sign-pattern census:
   'Of 2804 one-cusped census manifolds with H1 = Z to seven tetrahedra, 2794 realise only the
    inversion, seven realise nothing, and three -- the object among them -- realise the full set.'
   det = s_m * s_l, where s_m is the sign on the meridian and s_l the sign on the longitude."""
import snappy, warnings
warnings.filterwarnings("ignore")
from collections import Counter

sel = []
for M in snappy.OrientableCuspedCensus(cusps=1):
    if M.num_tetrahedra() > 7:
        break
    if str(M.homology()) == 'Z':
        sel.append(M.name())
print("one-cusped, H1 = Z, <= 7 tetrahedra:", len(sel), "(paper: 2804)")

cls = Counter()
full, nothing, inv_only, other = [], [], [], []
errs = []
for n in sel:
    M = snappy.Manifold(n)
    pats = set()
    try:
        isos = M.is_isometric_to(M, return_isometries=True)
    except Exception:
        try:
            M.canonize(); isos = M.is_isometric_to(M, return_isometries=True)
        except Exception:
            errs.append(n); continue
    for iso in isos:
        try:
            A = iso.cusp_maps()[0]
        except Exception:
            continue
        sm = 1 if A[0, 0] > 0 else (-1 if A[0, 0] < 0 else 0)
        sl = 1 if A[1, 1] > 0 else (-1 if A[1, 1] < 0 else 0)
        if sm and sl:
            pats.add((sm, sl))
    nontrivial = pats - {(1, 1)}
    if len(pats) >= 4:
        full.append(n); cls['full set'] += 1
    elif not nontrivial:
        nothing.append(n); cls['nothing'] += 1
    elif nontrivial == {(-1, -1)}:
        inv_only.append(n); cls['inversion only'] += 1
    else:
        other.append((n, sorted(pats))); cls['other'] += 1
print("  classification:", dict(cls), " errors:", len(errs))
print("  FULL SET (all four patterns):", len(full), full)
print("  NOTHING (only the identity pattern):", len(nothing), nothing)
print("  INVERSION ONLY:", len(inv_only))
print("  other partial sets:", len(other), other[:10])
print("  paper: 2794 inversion only, 7 nothing, 3 full set (m004 among them)")
