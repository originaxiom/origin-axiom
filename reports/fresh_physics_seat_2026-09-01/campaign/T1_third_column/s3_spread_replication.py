"""T1 step 3 -- the observable-spread test, replicated on the REAL block shape (3x3x4),
plus a byte-level re-run of B1232's own (3,4,1) construction for comparability.

MB12 (mandatory bite control): a generic random coupling MUST give a nonzero spread of the
order of B1232's reported 4.83. If the generic control gave 0, the instrument is broken and
the cell would be DEGRADED.

NOTE (Gate 5): all couplings here are SYNTHETIC (standard-normal or structural). The actual
banked coupling's entries are NOT committed to this repo (see s4); no branch below claims
to be the actual coupling. Case A is the structure the actual coupling would have IF it
annihilates C; case B/C are the failure branches.
"""
import numpy as np

N_SPLIT = 2000

# ---------- part 1: byte-level re-run of B1232's construction (their seed 20260901) ----------
rng = np.random.default_rng(20260901)
dC, dV, dT = 3, 4, 1
def splitting(tv):
    s = np.zeros((dV, dT)); s[dC, 0] = 1.0; s[:dC, 0] = tv
    return s
Y_ann = np.zeros((1, dV)); Y_ann[0, dC] = rng.normal()
vals = [float((Y_ann @ splitting(rng.normal(size=dC))).ravel()[0]) for _ in range(N_SPLIT)]
spread_ann_b1232 = max(vals) - min(vals)
Y_gen = rng.normal(size=(1, dV))
vals2 = [float((Y_gen @ splitting(rng.normal(size=dC))).ravel()[0]) for _ in range(N_SPLIT)]
spread_gen_b1232 = max(vals2) - min(vals2)
print(f"[B1232 re-run, seed 20260901] annihilating: spread = {spread_ann_b1232:.3e}"
      f" | generic: spread = {spread_gen_b1232:.3e} (their banked numbers: 0.000e+00 / 4.83)")
assert spread_ann_b1232 == 0.0
assert spread_gen_b1232 > 1.0, "MB12: generic control must be nonzero -- else DEGRADED"

# ---------- part 2: the REAL shape -- 3x3x4 family tensor over the (3,4,1) sequence ----------
# fresh, independent seed for this cell
rng = np.random.default_rng(20260901 + 71)   # 71 = T1 cell salt

def spread_report(T, label):
    """T: (3,3,4) tensor; k=0,1,2 conn (= C), k=3 tail (= the lift of T).
    observable at splitting t: the 3x3 family matrix Y(t)[i,j] = T[i,j,3] + sum_k t_k T[i,j,k].
    Reported spreads: per-entry max spread, and the (0,0)-entry spread (B1232's scalar convention)."""
    ts = rng.normal(size=(N_SPLIT, 3))
    Ys = np.einsum("ijk,nk->nij", T[:, :, :3], ts) + T[:, :, 3][None, :, :]
    per_entry = Ys.max(axis=0) - Ys.min(axis=0)          # 3x3 spreads
    s00 = float(per_entry[0, 0]); smax = float(per_entry.max())
    print(f"  {label:34s} entry(0,0) spread = {s00:.3e} | max entry spread = {smax:.3e}")
    return s00, smax

print(f"\n[real shape 3x3x4, {N_SPLIT} random splittings, seed 20260901+71]")

# CASE A -- coupling annihilates C: 27 Higgs-connecting entries = 0, 9 tail entries generic
T_A = np.zeros((3, 3, 4)); T_A[:, :, 3] = rng.normal(size=(3, 3))
sA00, sAmax = spread_report(T_A, "A: annihilates C (tail-only)")

# CASE B -- generic coupling (MB12 BITE CONTROL): all 36 entries standard normal
T_B = rng.normal(size=(3, 3, 4))
sB00, sBmax = spread_report(T_B, "B: generic (BITE CONTROL)")

# CASE C -- minimal obstruction: exactly ONE nonzero connecting entry
T_C = np.zeros((3, 3, 4)); T_C[:, :, 3] = rng.normal(size=(3, 3)); T_C[1, 2, 0] = 1.0
sC00, sCmax = spread_report(T_C, "C: single conn entry T[1,2,c1]=1")

# ---------- verdict wiring ----------
assert sAmax == 0.0, "annihilating coupling must give spread EXACTLY 0"
assert sBmax > 1.0, "MB12: generic spread must be nonzero and of order B1232's 4.83 -- else DEGRADED"
assert sC00 == 0.0 and sCmax > 1.0, "one conn entry must be visible ONLY in its own family entry"

print(f"""
S3 VERDICT: instrument VALIDATED on the real (3,3,4)-over-(3,4,1) structure.
  * annihilating branch: spread EXACTLY 0.0 (both scalar conventions) -- P^3 invisible;
  * generic bite control: spread {sBmax:.2f} (same order as B1232's 4.83) -- the test CAN fail; not DEGRADED;
  * single-entry obstruction: localized -- entry (1,2) spread {sCmax:.2f} while entry (0,0) stays 0.0,
    so an OBSTRUCTED verdict would name exactly which of the 27 entries is nonzero.
The instrument is ready; what it lacks is the ACTUAL coupling's 27 entries (see s4).""")
