#!/usr/bin/env bash
# B1181 -- the amphichirality debt closed: cc3's 83/83, spot-verified here 5/5 by MIRROR-ISOMETRY
# (deliberately not isometry_signature -- the known vacuity trap).
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null
import snappy
for name in ['m004','s955','o10_150700','o10_150684','t12840']:
    M = snappy.Manifold(name); W = M.copy(); W.reverse_orientation()
    amph = None
    for _ in range(8):
        try: amph = M.is_isometric_to(W); break
        except RuntimeError: W.randomize()
    assert amph is True, name
    print(f"  {name}: amphichiral (mirror-isometry) = True")
print("5/5 -- cc3's 83/83 holds on sample. REPRODUCES")
PY
