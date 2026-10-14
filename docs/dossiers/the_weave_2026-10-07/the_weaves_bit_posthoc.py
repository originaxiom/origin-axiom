"""W76, POST HOC (labelled; written after W76's read-out and after reading chat1's root-share check). chat1's run
(`chat1/web-seat` @ f8fe26015, `relays/chat1_2026-10-14_the_scale/t_root_threads.json`) stores Vol and CS for every b++
Lyndon thread to length 18 (31,040), on its own instrument. This reads that file from git and asks two things.

  PH1  W76's B2 extended to length 18 on chat1's data: the threads with |CS| <= 1e-6 are exactly the mirror-symmetric
       Lyndon words (swap(W) a rotation of W or of W reversed), and every mirror-symmetric thread has CS = 0 (never
       pi^2/2); no other thread has 2 CS = 0 mod pi^2
  PH2  the two seats agree: chat1's CS and W76's on the 8,798 common threads, to 1e-8 mod pi^2

Run: python3 the_weaves_bit_posthoc.py  ->  the_weaves_bit_posthoc.json beside it.
"""
import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_weaves_bit_posthoc.json"
REF, PATH = "f8fe26015", "relays/chat1_2026-10-14_the_scale/t_root_threads.json"
PI2 = math.pi ** 2


def red(v):
    w = math.fmod(v, PI2)
    if w > PI2 / 2:
        w -= PI2
    if w <= -PI2 / 2:
        w += PI2
    return w


def least_rotation(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def mirror_symmetric(w):
    s = least_rotation(w.translate(str.maketrans("LR", "RL")))
    return s in (least_rotation(w), least_rotation(w[::-1]))


def main():
    raw = subprocess.run(["git", "show", f"{REF}:{PATH}"], cwd=HERE, capture_output=True, check=True).stdout
    chat1 = {w: (float(v), red(float(c))) for w, (v, c) in json.loads(raw).items()}
    zero = {w for w, (_, c) in chat1.items() if abs(c) <= 1e-6}
    sym = {w for w in chat1 if mirror_symmetric(w)}
    half = sorted(w for w in sym if abs(abs(chat1[w][1]) - PI2 / 2) < 1e-6)
    stray = sorted(w for w in chat1 if w not in sym and abs(red(2 * chat1[w][1])) < 1e-6)
    per_len = {}
    for w in sym:
        per_len[len(w)] = per_len.get(len(w), 0) + 1
    out = {"status": "W76 POST HOC (labelled): the bit on chat1's data to length 18", "chat1's file": f"{REF}:{PATH}",
           "threads": len(chat1)}
    out["PH1"] = {"threads with CS = 0": len(zero), "mirror-symmetric threads": len(sym),
                  "the two sets are equal": zero == sym, "mirror-symmetric with CS = pi^2/2": half,
                  "others with 2 CS = 0": stray, "mirror-symmetric per length": dict(sorted(per_len.items())),
                  "holds": bool(zero == sym and not half and not stray)}
    mine = json.loads((HERE / "the_weaves_bit.json").read_text(encoding="utf-8"))["threads"]
    common = [w for w in mine if w in chat1]
    diff = max(abs(red(mine[w] - chat1[w][1])) for w in common)
    out["PH2"] = {"common threads": len(common), "largest CS difference mod pi^2": diff,
                  "holds": bool(len(common) == 8798 and diff < 1e-8)}
    out["cells"] = {k: out[k]["holds"] for k in ("PH1", "PH2")}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
