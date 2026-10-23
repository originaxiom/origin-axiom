"""B1741 C1 (ii) post hoc diagnosis (labelled; no data): is the frame periodic in the line's b with period 1, or only 2?
Compares B1726's compute() at (0.4 + 2.993i, (2/5, 1/10)) with (3.4 + 2.993i, (2/5, b)) for b = 1/10 - 6/5 (B1724's law,
unreduced), its reductions mod 1 and mod 2, and at a fixed tau the shifts b -> b + 1, b + 2."""
import sys, math, pathlib, json
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
import census as K
IM = 2.993325909
def dev(x, y): return max((abs(math.log(p / q)) for k in x for p, q in zip(x[k][:3] if k.startswith("ckm") else x[k], y[k][:3] if k.startswith("ckm") else y[k]) if p > 1e-10 and q > 1e-10), default=0.0)
base = K.compute(0.4, IM, Fr(2, 5), Fr(1, 10))
out = {}
for name, (re, b) in {"B1724 unreduced b = -11/10": (3.4, Fr(-11, 10)), "reduced mod 1: 9/10 (the control's)": (3.4, Fr(9, 10)),
                      "reduced mod 2: 9/10 (= -11/10 + 2)": (3.4, Fr(9, 10)), "tau fixed, b + 1 = 11/10": (0.4, Fr(11, 10)),
                      "tau fixed, b + 2 = 21/10": (0.4, Fr(21, 10)), "tau fixed, sign: (-2/5, -1/10)": (0.4, None)}.items():
    r = K.compute(re, IM, Fr(-2, 5), Fr(-1, 10)) if b is None else K.compute(re, IM, Fr(2, 5), b)
    out[name] = dev(base, r)
print(json.dumps(out, indent=1))
json.dump(out, open(pathlib.Path(__file__).with_name("c1_diagnosis.json"), "w"), indent=1)
