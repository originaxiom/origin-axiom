"""W76: the weave's beta-odd bit. Chern-Simons on every thread to length 16 (8 798 Lyndon words, b++ bundles), and the
bit (0 or pi^2/2) on every mirror-symmetric thread. The rule (W76_RULE.md) was committed before this script.

  B0  the instrument: 8 798 threads, all geometric, no exception; b++LR has CS = 0
  B1  the 2-torsion (control): every mirror-symmetric thread has 2 CS = 0 mod pi^2
  B2  the bit: every mirror-symmetric thread has CS = 0, none pi^2/2
  B3  no stray torsion: no thread that is not mirror-symmetric has 2 CS = 0 mod pi^2
  plus the read-outs: mirror-symmetric threads per length and by kind, their largest |CS|, stray small CS, wall-clock

A census of thread quantities over every thread under a stated rule (a weave census, not a joint-action quantity).

Run: python3 the_weaves_bit.py  ->  the_weaves_bit.json beside it.
"""
import itertools
import json
import math
import time
import warnings
from collections import Counter
from pathlib import Path

import snappy

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
OUT = HERE / "the_weaves_bit.json"
PI2 = math.pi ** 2
GEOMETRIC = "all tetrahedra positively oriented"


def red(v):                                     # reduce mod pi^2 to (-pi^2/2, pi^2/2]
    w = math.fmod(v, PI2)
    if w > PI2 / 2:
        w -= PI2
    if w <= -PI2 / 2:
        w += PI2
    return w


def least_rotation(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def is_lyndon(w):
    return all(w < w[i:] + w[:i] for i in range(1, len(w)))


def swap(w):
    return w.translate(str.maketrans("LR", "RL"))


def main():
    t0 = time.time()
    threads = [w for n in range(2, 17) for w in ("".join(p) for p in itertools.product("LR", repeat=n))
               if is_lyndon(w)]
    cs, sol, errors = {}, {}, []
    for w in threads:
        try:
            M = snappy.Manifold("b++" + w)
            cs[w] = red(complex(M.complex_volume()).imag)
            sol[w] = M.solution_type()
        except Exception as e:                  # recorded, counted against B0
            errors.append([w, repr(e)[:120]])
    nongeo = [[w, s] for w, s in sol.items() if s != GEOMETRIC]
    out = {"status": "W76: the weave's beta-odd bit (the rule W76_RULE.md first; one run)", "snappy": snappy.__version__}
    out["B0"] = {"threads": len(threads), "measured": len(cs), "non-geometric": nongeo, "errors": errors,
                 "CS(b++LR)": cs.get("LR"),
                 "holds": bool(len(threads) == 8798 and len(cs) == 8798 and not nongeo and not errors
                               and abs(cs.get("LR", 1.0)) < 1e-9)}
    kinds, bits, per_len = {}, {}, Counter()
    for w in cs:
        by_rot = least_rotation(swap(w)) == w
        by_rev = least_rotation(swap(w)) == least_rotation(w[::-1])
        if by_rot or by_rev:
            kinds[w] = "both" if (by_rot and by_rev) else ("swap = rotation" if by_rot else "swap = reversal")
            c = cs[w]
            bits[w] = "0" if abs(c) < 1e-8 else ("1/2" if abs(abs(c) - PI2 / 2) < 1e-8 else "neither")
            per_len[len(w)] += 1
    bit_count = Counter(bits.values())
    out["B1"] = {"mirror-symmetric threads": len(bits), "bits": dict(bit_count),
                 "neither": [[w, cs[w]] for w, b in bits.items() if b == "neither"],
                 "holds": bool(len(bits) > 0 and bit_count.get("neither", 0) == 0)}
    out["B2"] = {"threads with bit 1/2": [[w, cs[w]] for w, b in bits.items() if b == "1/2"],
                 "holds": bool(len(bits) > 0 and set(bits.values()) == {"0"})}
    stray = [[w, cs[w]] for w in cs if w not in bits and abs(red(2 * cs[w])) < 1e-6]
    out["B3"] = {"threads not mirror-symmetric with 2 CS = 0": stray, "holds": bool(not stray)}
    small = [[w, cs[w]] for w in cs if w not in bits and abs(cs[w]) < 1e-6]
    out["read-outs"] = {"mirror-symmetric per length": dict(sorted(per_len.items())),
                        "by kind": dict(Counter(kinds.values())),
                        "largest |CS| among them": max((abs(cs[w]) for w in bits), default=None),
                        "not mirror-symmetric with |CS| < 1e-6": small,
                        "wall-clock (s)": round(time.time() - t0, 1)}
    out["cells"] = {k: out[k]["holds"] for k in ("B0", "B1", "B2", "B3")}
    out["threads"] = {w: cs[w] for w in cs}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
