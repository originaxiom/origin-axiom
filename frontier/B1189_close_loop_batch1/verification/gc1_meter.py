#!/usr/bin/env python3
"""GC-1 THE METER: independent verification of the discrete ladder.

Independent of og3_volume_spectrum.py in every load-bearing step:
  * lattice unit V_reg = Im Li2(e^{i pi/3}) computed in mpmath (Bloch-Wigner
    D at the hexic root = volume of the regular ideal tetrahedron), NOT taken
    from snappy's m004 volume;
  * every member volume recomputed TWICE: (a) snappy ManifoldHP volume,
    (b) independently as sum of Bloch-Wigner D(shape_i) over the ManifoldHP
    tetrahedron shapes, evaluated in mpmath at 50 dps;
  * bite control: >=20 census manifolds NOT in members_B, small and large,
    tested against the same lattice;
  * Humbert covolume of PSL2(O_{-3}) from L-series, to express V_reg in the
    minimal-orbifold meter.
"""
import json
import snappy
import mpmath as mp

mp.mp.dps = 50
TOL_MEMBER = mp.mpf(10) ** -25   # member must be THIS close to an integer rung
TOL_XCHECK = mp.mpf(10) ** -25   # agreement between the two volume computations
OFF_MIN = mp.mpf(10) ** -3       # a control is OFF-lattice if farther than this

def D(z):
    """Bloch-Wigner dilogarithm."""
    z = mp.mpc(z)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))

# --- the meter, from first principles ---
V_REG = mp.im(mp.polylog(2, mp.exp(mp.mpc(0, mp.pi / 3))))  # = D(e^{i pi/3})
# sanity: V_reg = Cl2(pi/3) (Clausen; = 3*Lobachevsky(pi/3), the regular ideal tet)
V_REG_clausen = mp.clsin(2, mp.pi / 3)
assert abs(V_REG - V_REG_clausen) < mp.mpf(10) ** -45

fam = json.load(open(str(__import__("pathlib").Path(__file__).resolve().parents[3] / "frontier/B1186_family_is_112/verification/family_census.json")))
members = fam["members_B"]
nonreg = set(fam["members_B"]) - set(fam["members_A"])
assert len(members) == 112 and len(nonreg) == 35

def hp_volume_two_ways(name):
    M = snappy.ManifoldHP(name)
    v_snap = mp.mpf(str(M.volume()).replace(" ", ""))
    v_bw = mp.mpf(0)
    for s in M.tetrahedra_shapes("rect"):
        z = mp.mpc(mp.mpf(str(s.real()).replace(" ", "")),
                   mp.mpf(str(s.imag()).replace(" ", "")))
        v_bw += D(z)
    return M, v_snap, v_bw

# --- (1) the ladder: all 112 members, both volume computations ---
rows, fails, xfails = [], [], []
for name in members:
    M, v_snap, v_bw = hp_volume_two_ways(name)
    r = v_snap / V_REG
    n = int(mp.nint(r))
    ok = abs(r - n) < TOL_MEMBER
    agree = abs(v_snap - v_bw) < TOL_XCHECK
    rows.append({"name": name, "nonregular": name in nonreg,
                 "tets": M.num_tetrahedra(), "rung": n if ok else None,
                 "dist": float(abs(r - n)), "vol_xcheck_diff": float(abs(v_snap - v_bw))})
    if not ok:
        fails.append((name, float(r)))
    if not agree:
        xfails.append((name, float(abs(v_snap - v_bw))))

from collections import Counter
spec_all = Counter(r["rung"] for r in rows)
spec_nonreg = Counter(r["rung"] for r in rows if r["nonregular"])
max_dist = max(r["dist"] for r in rows)
max_x = max(r["vol_xcheck_diff"] for r in rows)
print("LADDER: rung spectrum (all 112):", dict(sorted(spec_all.items(), key=lambda kv: (kv[0] is None, kv[0]))))
print("LADDER: rung spectrum (35 non-regular):", dict(sorted(spec_nonreg.items(), key=lambda kv: (kv[0] is None, kv[0]))))
print("LADDER: off-lattice members:", fails if fails else "NONE")
print(f"LADDER: max |ratio - rung| over 112 = {max_dist:.3e} (tol {float(TOL_MEMBER):.0e})")
print(f"XCHECK: max |snap - Bloch-Wigner| over 112 = {max_x:.3e}; failures:", xfails if xfails else "NONE")

# --- (2) wide bite control: census manifolds NOT in the family ---
memberset = set(members)
controls = []
# small: first 12 orientable-cusped census manifolds not in the family
it = iter(snappy.OrientableCuspedCensus)
while len(controls) < 12:
    name = next(it).name()
    if name not in memberset:
        controls.append(name)
# large/mixed: hand-picked spread across s/v/t/o censuses, incl. the classic
# deliberately-absent targets m015 (5_2, cubic field) and m137/m201 (other fields)
for name in ["m015", "m137", "m201", "s776", "s789", "v1539", "v3209",
             "t12198", "t10000", "o9_00133", "o9_20000", "o9_40000"]:
    if name not in memberset:
        controls.append(name)
ctl_rows, on_lattice_ctl = [], []
for name in controls:
    M = snappy.ManifoldHP(name)
    v = mp.mpf(str(M.volume()).replace(" ", ""))
    r = v / V_REG
    d = abs(r - mp.nint(r))
    ctl_rows.append({"name": name, "ratio": float(r), "dist_to_int": float(d)})
    if d < OFF_MIN:
        on_lattice_ctl.append((name, float(r)))
min_ctl = min(c["dist_to_int"] for c in ctl_rows)
print(f"CONTROL: {len(ctl_rows)} non-members tested; min distance to integer lattice = {min_ctl:.4f} (threshold {float(OFF_MIN)})")
print("CONTROL: accidental on-lattice non-members:", on_lattice_ctl if on_lattice_ctl else "NONE")

# --- (4) the mechanism meter: Humbert covolume of PSL2(O_{-3}) ---
# zeta_K(2) = zeta(2) * L(2, chi_{-3}), chi_{-3}(n) = +1 (n=1 mod 3), -1 (n=2 mod 3)
L2 = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9  # Hurwitz form, exact convergence
zetaK2 = mp.zeta(2) * L2
v_psl = mp.mpf(3) ** mp.mpf("1.5") * zetaK2 / (4 * mp.pi**2)   # Humbert
print(f"MECHANISM: covol(PSL2(O_-3)) = {mp.nstr(v_psl, 30)}")
print(f"MECHANISM: V_reg / covol(PSL2) = {mp.nstr(V_REG / v_psl, 30)}  (integer? dist {float(abs(V_REG/v_psl - mp.nint(V_REG/v_psl))):.1e})")
print(f"MECHANISM: V_reg / covol(PGL2=PSL2/..half) = {mp.nstr(V_REG / (v_psl/2), 30)}")
print(f"MECHANISM: Vol(m004) = 2*V_reg = {mp.nstr(2*V_REG, 30)} = {mp.nstr(2*V_REG/v_psl, 20)} x covol(PSL2)")

json.dump({"V_reg": mp.nstr(V_REG, 45), "rows": rows, "controls": ctl_rows,
           "spectrum_all": {str(k): v for k, v in spec_all.items()},
           "spectrum_nonregular": {str(k): v for k, v in spec_nonreg.items()},
           "max_member_dist": float(max_dist), "max_xcheck": float(max_x),
           "covol_PSL2_O3": mp.nstr(v_psl, 45)},
          open("SCRATCH/b1188/cells/gc1_ladder.json", "w"), indent=1)
print("DONE")
