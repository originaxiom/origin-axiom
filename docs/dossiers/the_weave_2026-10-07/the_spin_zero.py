#!/usr/bin/env python3
"""W11 of the weave: the frame's count at the weave's spin vacuum is zero at every class, on every state at every tick.

This is sm:B1509's T2 and T3 read at the common point. The seat found it after sm:B1552's read-out; it decides that
arc's question for every thread, and it could have been read before the seal.

The statement. Let A be a sum of twists lambda (x) rho_Q of the common point by characters lambda (any parity, any
kappa), on any state at any tick where A is defined. Let c be any non-zero class of H^1(M; A), and W1 = [[A, c], [0, 1]].
Then I(W1) = 0. So F-HE's count there is never (-1, -1), a generation, nor (1, 1).

The proof (frontier/B1509_the_join_on_the_projective_vacuum/FINDINGS.md, T2 and T3):
  (i)   The puncture loop [a, b] acts on A by lambda([a, b]) rho_Q([a, b]) = -1. So the peripheral torus fixes no
        vector, and H*(T; A) = 0 by the Koszul complex. The same holds for A*.
  (ii)  Q8 fixes no vector of C^2, so H^0(F; A) = 0. Hence H^0(M; A) = H^0(M; A*) = 0, and by the Wang sequence
        H^1(M; A) = ker(S_A - 1), with S_A the stable letter's action on H^1(F; A).
  (iii) T2: I(W1) = -r1, and r1 = 1 iff e u c = 0 (e the fibration class). T2's proof does not use h^1(A) = 1. The
        classes from H^1(M; A) restrict into H^1(T; A) = 0, so the restriction of W1's classes still factors through
        H^1(M; 1) = C e.
  (iv)  T3: e u c is the image of c under the natural map ker(S_A - 1) -> coker(S_A - 1). That map is injective when
        S_A is semisimple.
  (v)   S_A is semisimple. It is kappa times an element of the finite group the moves generate: on the parity-twisted
        spin doublets that is W10's group of order 96 (192 with the swap); on the doublet itself it is W9's Z/8.

What this script checks:
  (1) T2's intermediate quantities on sm:B1552's banked record, at all 864 readings:
      - A has h0 = 0 and r1 = 0;
      - W1 has h0 = 0, r1 = 0 and n = n(A) - 1;
      - W1* has h0 = 1, r1 = 2 and n = n(W1);
      - the count's first entry is 0.
  (2) (v) by census. On every state of GENESIS to length 12 (758) with both lifts, the act on V has 96th power the
      identity (to 1e-8), so the act of every tick on every parity it fixes is semisimple.
  (3) The tick's act is the power of the state's act. On the 24 states to length 6 at ticks 1-3 (every resolving tick),
      the deck-compatible act of phi^k with the inherited lift g^k is the k-th power of the act of phi with g.

    python3 the_spin_zero.py   ->  the_spin_zero.json beside it
"""
import gzip
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import the_common_point as CP  # noqa: E402
import the_parity_sectors as S  # noqa: E402
import the_chiral_triplet as CT  # noqa: E402

RECORD = ROOT / "frontier" / "B1552_the_chiral_triplets_count" / "verification"


def check_record():
    out, bad = {"readings": 0, "the count's first entry 0": 0}, []
    for route in (1, 2):
        with gzip.open(RECORD / f"run_{route}.jsonl.gz", "rt") as f:
            for line in f:
                r = json.loads(line)
                if "count" not in r:
                    continue
                out["readings"] += 1
                a, w, ws = r["structure"], r["reads"]["W1"], r["reads"]["W1*"]
                ok = (a["h0"] == 0 and a["r1"] == 0
                      and w["h0"] == 0 and w["r1"] == 0 and w["n"] == a["n"] - 1
                      and ws["h0"] == 1 and ws["r1"] == 2 and ws["n"] == w["n"])
                out["the count's first entry 0"] += int(r["count"][0] == 0)
                if not ok:
                    bad.append({k: r[k] for k in ("route", "state", "module", "lift", "parity", "kappa (eighths)")})
    out["T2's quantities held at every reading"] = not bad
    out["failures"] = bad
    return out


def census():
    I6 = np.eye(6)
    out = {"states": 0, "acts (state, lift)": 0, "96th power the identity": 0, "worst deviation": 0.0}
    for sw in S.states(12):
        sign = 1 if sw[0] == "+" else -1
        phi1 = CP.word_aut(sw[1:], sign)
        out["states"] += 1
        for g in CP.extend(phi1):
            A = CT.on_V(phi1, g)
            d = float(np.abs(np.linalg.matrix_power(A, 96) - I6).max())
            out["acts (state, lift)"] += 1
            out["96th power the identity"] += int(d < 1e-8)
            out["worst deviation"] = max(out["worst deviation"], d)
    return out


def tick_powers():
    out = {"(state, lift, tick)": 0, "agree": 0, "worst deviation": 0.0}
    for sw in S.states(6):
        sign = 1 if sw[0] == "+" else -1
        phi1 = CP.word_aut(sw[1:], sign)
        for g in CP.extend(phi1):
            A = CT.on_V(phi1, g)
            for k in range(1, 4):
                Ak = CT.on_V(CT.power(phi1, k), CT.qpow(g, k))
                d = float(np.abs(Ak - np.linalg.matrix_power(A, k)).max())
                out["(state, lift, tick)"] += 1
                out["agree"] += int(d < 1e-8)
                out["worst deviation"] = max(out["worst deviation"], d)
    return out


if __name__ == "__main__":
    res = {"(1) T2 on sm:B1552's record": check_record(),
           "(2) the act on V is in a finite group, every state to length 12": census(),
           "(3) the tick's act is the power of the state's act, every state to length 6, ticks 1-3": tick_powers()}
    r1, r2, r3 = (res[k] for k in list(res))
    res["all held"] = bool(r1["T2's quantities held at every reading"] and r1["readings"] == 864
                           and r1["the count's first entry 0"] == 864
                           and r2["96th power the identity"] == r2["acts (state, lift)"]
                           and r3["agree"] == r3["(state, lift, tick)"])
    with open(HERE / "the_spin_zero.json", "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res, indent=1))
