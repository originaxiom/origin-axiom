"""B973 scout probe: rebuild the FLOOR from the bench's own material and type it.

Uses ONLY frontier/B854_centralizer_exact/e6_centralizer.py (bench-owned build,
the four 2T-invariants) + frontier/B961_frame_instrument/frame.py operations.
No incoming code.
"""
import sys, json, time, io, contextlib
sys.path.insert(0, str(_REPO / "frontier/B961_frame_instrument"))
import sympy as sp
import frame
from fractions import Fraction as F
import pathlib as _pl
_REPO = _pl.Path(__file__).resolve().parents[2]

T0 = time.time()
def log(m): print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)

INV = frame._G["INV"]
CH = {n: INV[n] for n in (8, 14, 16, 22)}
DIM = frame.DIM
R = {}

log("building the four exact ad matrices ...")
AD = {n: frame.ad(CH[n]) for n in (8, 14, 16, 22)}

# ---- the frame: Killing Gram of the four charges (K(x,y) = tr(ad x ad y)) ----
ns = [8, 14, 16, 22]
G = sp.zeros(4, 4)
for i in range(4):
    for j in range(i, 4):
        t = (AD[ns[i]] * AD[ns[j]]).trace()
        G[i, j] = t; G[j, i] = t
log(f"frame Gram = {[[str(G[i,j]) for j in range(4)] for i in range(4)]}")
offdiag_zero = all(G[i, j] == 0 for i in range(4) for j in range(4) if i != j)
diag = [G[i, i] for i in range(4)]
signs = [int(sp.sign(d)) for d in diag]
R["frame_gram_diagonal"] = bool(offdiag_zero)
R["frame_gram_diagonal_entries"] = [str(d) for d in diag]
R["frame_gram_signs"] = signs
R["frame_signature"] = [signs.count(1), signs.count(-1)]
R["frame_gram_det_is_rational_square"] = bool(sp.sqrt(sp.Abs(G.det())).is_rational)
log(f"diagonal: {offdiag_zero}; signs {signs}; det {G.det()}")

# ---- core = z(g8) ----
log("core = z(g8) ...")
core = AD[8].nullspace()
R["dim_z_g8"] = len(core)
Bc = sp.Matrix.hstack(*core)
R["ad16_kills_z_g8"] = bool((AD[16] * Bc).is_zero_matrix)
log(f"dim z(g8) = {len(core)}; ad16 kills it: {R['ad16_kills_z_g8']}")

# ---- floor = z(all four charges) ----
log("floor = z(g8,g14,g16,g22) (via core) ...")
P = (Bc.T * Bc).inv() * Bc.T
C14 = P * AD[14] * Bc
assert (Bc * C14 - AD[14] * Bc).is_zero_matrix
fl = C14.nullspace()
Bf = Bc * sp.Matrix.hstack(*fl)
floor = [[Bf[i, j] for i in range(DIM)] for j in range(Bf.shape[1])]
R["dim_floor"] = len(floor)
R["floor_killed_by_g22"] = bool((AD[22] * Bf).is_zero_matrix)
R["floor_killed_by_g16"] = bool((AD[16] * Bf).is_zero_matrix)
log(f"dim floor = {len(floor)}; ad22 kills: {R['floor_killed_by_g22']}; ad16 kills: {R['floor_killed_by_g16']}")

# the four charges lie in the floor?
stack = sp.Matrix.hstack(Bf, sp.Matrix([[sp.Rational(CH[n][i].numerator, CH[n][i].denominator)
                                          for n in ns] for i in range(DIM)]))
R["charges_inside_floor"] = bool(stack.rank() == len(floor))
log(f"the four charges lie inside the floor: {R['charges_inside_floor']}")

# ---- type the floor ----
log("derived(floor) ...")
d = frame.derived([[F(sp.Rational(x)) for x in v] for v in floor])
R["dim_derived_floor"] = int(frame.dim_of(d))
R["floor_centre_dim"] = len(floor) - R["dim_derived_floor"]
log(f"dim [floor,floor] = {R['dim_derived_floor']}; centre = {R['floor_centre_dim']}")

# is the derived part semisimple (centre 0) and hence A2 = su(3)?
dd = frame.derived(d)
R["dim_derived_of_derived"] = int(frame.dim_of(dd))
R["derived_floor_is_perfect"] = R["dim_derived_of_derived"] == R["dim_derived_floor"]
log(f"[[floor,floor],[floor,floor]] dim = {R['dim_derived_of_derived']}")

# centre of derived(floor)
Ad = [frame.ad(v) for v in d]
k = len(d)
rows = []
Bd = sp.Matrix([[sp.Rational(x) for x in v] for v in d]).T   # DIM x k
for j in range(k):
    Mj = sp.Matrix.hstack(*[Ad[a] * Bd[:, j] for a in range(k)])   # DIM x k
    rows.extend(Mj.tolist())
cen = sp.Matrix(rows).nullspace()
R["centre_of_derived_floor"] = len(cen)
log(f"centre of [floor,floor] = {len(cen)}  (0 => semisimple; dim 8 semisimple is uniquely A2 = su(3))")

json.dump(R, open(str(_REPO / "frontier/B973_L135_frame/scout_probe_results.json"), "w"),
          indent=1, sort_keys=True)
log("DONE")
