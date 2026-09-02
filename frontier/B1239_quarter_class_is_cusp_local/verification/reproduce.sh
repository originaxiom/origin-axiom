#!/usr/bin/env bash
# B1239 — THE ¼ CLASS IS CUSP-LOCAL.  Reproduces the fast checks in ~1 min; the census reruns are documented
# below as slow steps (they wrote the JSONs beside this script; rerun with the commands shown).
set -euo pipefail
cd "$(dirname "$0")"
echo "== fast 1: torsion parity / cusp kinds of the 1260 covers (reads r040_census_rerun.json)"
python3 r040_torsion_parity.py
echo "== fast 2: live witnesses (SnapPy)"
python3 - <<'PY'
import snappy
def cls(cs):
    x = cs % 0.5; return "zero" if min(x, 0.5-x) < 1e-9 else ("quarter" if abs(x-0.25) < 1e-9 else "other")
m203 = snappy.Manifold("m203"); isos = m203.is_isometric_to(m203, return_isometries=True)
rev = [i for i in isos if round(i.cusp_maps()[0].det()) == -1]
swap = any(all(i.cusp_images()[j] != j for j in range(m203.num_cusps())) for i in rev)
print("m203: cusps", m203.num_cusps(), "reversing isos", len(rev), "one fixes no cusp:", swap, "class", cls(m203.chern_simons()))
assert swap and cls(m203.chern_simons()) == "zero"
t = snappy.Manifold("t12054"); print("t12054: amphichiral", t.symmetry_group().is_amphicheiral(), "class", cls(t.chern_simons()))
assert t.symmetry_group().is_amphicheiral() and cls(t.chern_simons()) == "quarter"
k = snappy.Manifold("5_2"); mk = k.copy(); mk.reverse_orientation()
print("5_2: is_isometric_to(mirror) =", k.is_isometric_to(mk), "(BLIND); symmetry_group().is_amphicheiral() =", k.symmetry_group().is_amphicheiral())
assert k.is_isometric_to(mk) is True and k.symmetry_group().is_amphicheiral() is False
m0 = snappy.Manifold("m000"); print("m000 (Gieseking): orientable", m0.is_orientable(), "cusp", m0.cusp_info()[0]["topology"])
assert not m0.is_orientable() and "Klein" in m0.cusp_info()[0]["topology"]
print("m004 = orientation double cover of m000:", snappy.Manifold("4_1").is_isometric_to(m0.orientation_cover()))
PY
echo "== slow steps (already run; outputs are the JSONs beside this script):"
echo "   python3 r040_census_rerun.py                 # 1260 covers, double + quad-double      (~25 min)"
echo "   python3 r040_closed_control.py               # 17 closed covers via the parent route  (~1 min)"
echo "   python3 r040_quarter_is_a_cusp_phenomenon.py # full closed census 11031 + 3000 cusped (~40 min)"
echo "   python3 r040_swap_corollary.py               # full cusped census 61911               (~3 h)"
echo "REPRODUCES"
