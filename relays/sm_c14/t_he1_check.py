"""SM-C14, a supporting check of T-HE1 (derived on the card before the run): the spectrum of Ballas' rho_q on the
longitude, from B1511's tower_lib (B1509's matrices), and whether it is closed under inversion up to a fourth root of 1."""
import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("tl", ROOT / "frontier/B1511_the_projective_tower/verification/tower_lib.py")
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
out = []
for q in (sp.Rational(1, 3), sp.Rational(1, 2), 1, 2, 3, 17 + 12 * sp.sqrt(2)):
    m_, n_ = T.ballas(q)
    Lm = T.word_matrix({"m": m_, "n": n_}, T.WORD_L).applyfunc(sp.nsimplify)
    ev = sp.Matrix(Lm).eigenvals()
    spec_ = sorted([complex(sp.N(k)) for k, m in ev.items() for _ in range(m)], key=lambda z: (z.real, z.imag))
    inv_ = [1 / z for z in spec_]
    closed = any(sorted([c * z for z in inv_], key=lambda z: (round(z.real, 9), round(z.imag, 9)))
                 == sorted(spec_, key=lambda z: (round(z.real, 9), round(z.imag, 9)))
                 or all(abs(a - b) < 1e-9 for a, b in zip(sorted([c * z for z in inv_], key=lambda z: (z.real, z.imag)), spec_))
                 for c in (1, -1, 1j, -1j))
    out.append({"q": str(q), "longitude spectrum": [[z.real, z.imag] for z in spec_], "closed under inversion": closed})
    print(out[-1])
Path(Path(__file__).with_name("t_he1_check.json")).write_text(json.dumps(out, indent=1))
