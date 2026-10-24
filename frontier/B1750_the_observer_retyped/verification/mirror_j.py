"""B1750 section 3: the frame's mirror maps J to -J (data-free; B1741's tie pair, already printed by B1741 and W145).
The line (2/5, 9/10) at 3.4 + 2.9933i against (2/5, 3/10) at 3.6 + 2.9933i (the reflection tau -> -conj(tau), b -> -b,
composed with T-shifts), and B1724's T-law (tau -> tau + 1, b -> b - alpha) at 0.4 + 2.9933i on (2/5, 1/10), through
B1726's sealed compute(): every mass key and CKM modulus compared, and J's sign.
    python3 -B mirror_j.py"""
import sys, pathlib
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
import census as K      # noqa: E402

IM = 2.993325909


def compare(x, y):
    dm = max(abs(p - q) for k in x if not k.startswith("ckm") for p, q in zip(x[k], y[k]))
    dc = max(abs(p - q) for k in x if k.startswith("ckm") for p, q in zip(x[k][:3], y[k][:3]))
    js = [(k, x[k][3], y[k][3]) for k in x if k.startswith("ckm")]
    return dm, dc, js


if __name__ == "__main__":
    L = K.lines()
    dm, dc, js = compare(K.compute(3.4, IM, *L[153]), K.compute(3.6, IM, *L[150]))
    print("mirror pair (line 153 at 3.4, line 150 at 3.6): masses equal to %.1e, CKM moduli to %.1e" % (dm, dc))
    for k, a, b in js: print("   %-18s J %+.4e  vs  %+.4e   (sum %.1e)" % (k, a, b, a + b))
    a, b = Fr(2, 5), Fr(1, 10)
    dm, dc, js = compare(K.compute(0.4, IM, a, b), K.compute(1.4, IM, a, (b - a) % 1))
    print("T-law (0.4 vs 1.4, b -> b - alpha): masses equal to %.1e, CKM moduli to %.1e" % (dm, dc))
    for k, a, b in js: print("   %-18s J %+.4e  vs  %+.4e   (difference %.1e)" % (k, a, b, a - b))
