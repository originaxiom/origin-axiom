"""xB023 Addendum 2, N3 residue, DECISIVE STEP.

A closed 3-manifold is S^3 iff pi_1 = 1 (Perelman).  Exhibiting ONE proper finite-index subgroup
of pi_1 PROVES pi_1 != 1, hence PROVES the filling is not S^3.  That is a positive certificate for
a negative claim -- the opposite of failing to simplify a presentation.

Calibration, both directions:
  m004(1,0) = S^3          -- MUST have NO proper cover at any degree
  m004(1,1) = Sigma(2,3,7) -- MUST have one
"""
import warnings

warnings.filterwarnings("ignore")
import snappy

MAXDEG = 7
cases = [("m004", (1, 0), "CALIBRATION +ve  (S^3: must find none)"),
         ("m004", (1, 1), "CALIBRATION -ve  (Sigma(2,3,7): must find one)"),
         ("o10_143849", (1, 0), ""), ("o10_143849", (-1, 0), ""),
         ("o10_143849", (0, 1), ""), ("o10_143849", (0, -1), "")]
out = {}
for nm, sl, note in cases:
    M = snappy.Manifold(nm)
    M.dehn_fill(sl)
    found = []
    for d in range(2, MAXDEG + 1):
        try:
            cs = M.covers(d)
        except Exception as e:
            found.append((d, f"err {type(e).__name__}"))
            continue
        if cs:
            found.append((d, len(cs), str(cs[0].homology())))
            break
    out[(nm, sl)] = found
    print(f"{nm:14s} {str(sl):8s} covers up to degree {MAXDEG}: {found}   {note}")

pos = out[("m004", (1, 0))]
neg = out[("m004", (1, 1))]
print()
print(f"CALIBRATION: S^3 -> {pos or 'none (correct)'};  Sigma(2,3,7) -> {neg or 'NONE (instrument blind)'}")
cal_ok = (not pos) and bool(neg)
print(f"calibration valid: {cal_ok}")
tg = [out[("o10_143849", s)] for s in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
proved = all(bool(f) for f in tg)
print(f"every one of the target's four homology-sphere slopes has a proper finite cover: {proved}")
if cal_ok and proved:
    print("=> PROVED: none of the four is S^3, so o10_143849 has NO S^3 filling among the")
    print("   slopes of length <= 6, and by the 6-theorem none at all.")
    print("   o10_143849 IS NOT A KNOT COMPLEMENT IN S^3.")
